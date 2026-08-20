"""ks3_art.b10 — B10's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import json
import math
import os
import re
from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_CARD,
    _SVG_DISPLAY,
    _SVG_GROUND,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_FAINT,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_MONO,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _b10_suffix,
    _b7_need,
    _b8_plain,
    _b9_placeholders,
    _circle,
    _ellipse,
    _label,
    _line,
    _mono,
    _n,
    _path,
    _pctnum,
    _rect,
    _svg_open,
    _svg_text,
    e,
    t,
)


_SVG_OK_TINT     = "var(--ks3-ok-tint)"
def _arrow_head(x, y, angle, size=9, fill=None, cls=None, **data):
    """A drawn triangle at (x, y), pointing along `angle` radians.

    ⛔ THE ONLY ARROWHEAD. Not `→`, not a `<marker>`: a marker inherits the
    line's `stroke-dasharray` in some engines and a dashed leader then arrives
    with a dashed head, which is how a drawn arrow stops reading as an arrow.
    A triangle is three points and cannot be surprised.
    """
    dx, dy = math.cos(angle), math.sin(angle)
    px, py = -dy, dx
    return _path("M %s,%s L %s,%s L %s,%s Z"
                 % (_n(x), _n(y),
                    _n(x - dx * size + px * size * 0.52),
                    _n(y - dy * size + py * size * 0.52),
                    _n(x - dx * size - px * size * 0.52),
                    _n(y - dy * size - py * size * 0.52)),
                 fill=fill or _SVG_INK, cls=cls, **data)
def _arrow(x1, y1, x2, y2, stroke=None, w=2, dash=None, head=9, cls=None,
           **data):
    """Line plus drawn head, ending exactly at (x2, y2)."""
    ang = math.atan2(y2 - y1, x2 - x1)
    paint = stroke or _SVG_INK
    return (_line(x1, y1, x2 - math.cos(ang) * head * 0.6,
                  y2 - math.sin(ang) * head * 0.6,
                  stroke=paint, w=w, dash=dash, cls=cls, **data)
            + _arrow_head(x2, y2, ang, size=head, fill=paint, cls=cls, **data))
def _base_pairs(fig):
    """The two strands, the rungs between them, and why the width never changes.

    ⚖️ WHY THIS LESSON GETS A DIAGRAM WHEN THE REST OF B10 DOES NOT. `model-builder`
    beside it is a REASONING instrument: the student sets dials and the evidence
    cards rule models out, so they argue their way to two strands with the bases
    paired inside and never once see it. The lesson's KEY FACT is then a purely
    structural claim — *"two strands twisted round each other, with the bases
    paired on the inside — A always with T, C always with G"* — and a structural
    claim with no drawing is a sentence to be memorised. That is Mide's test for
    a diagram: genuinely spatial or structural, not decoration.

    ⚖️ AND THE DIAGRAM TEACHES THE REASON, not just the rule. A always with T and
    C always with G is usually met as an arbitrary fact. It is not: A and G are
    the big bases and C and T the small ones, so a big one paired with a small one
    is the only combination that keeps every rung the same length — and a molecule
    whose rungs were different lengths could not have the constant width Franklin
    measured off the diffraction pattern on this same page. The constant-width
    guide down the right-hand side is therefore the point of the drawing, not an
    annotation on it.

    Never colour-alone, three ways over: a base carries its LETTER, its WIDTH
    (big or small, drawn to scale against each other), and a written size word in
    the key. A reader who cannot separate the tints still has all of it.
    """
    d = fig.get("data") or {}
    rungs = d.get("rungs") or []
    if not rungs:
        raise ValueError("base-pairs figure %r has no rungs." % fig.get("id"))

    # Big bases (purines) and small ones (pyrimidines), drawn to their real
    # relative sizes rather than to two arbitrary widths — the whole argument is
    # that big + small is a constant total.
    BIG, SMALL = 96.0, 62.0
    SIZE = {"A": BIG, "G": BIG, "C": SMALL, "T": SMALL}
    WORD = {"A": "big", "G": "big", "C": "small", "T": "small"}
    # ⊕ MRB-257 · audit 5.42 / 3.1 — THE FILL IS A PROPERTY OF THE BASE, and
    # this map is the whole fix.
    #
    # The two rects below used to be painted `_SVG_ACCENT_TINT` on the left and
    # `_SVG_OK_TINT` on the right, unconditionally — keyed to the COLUMN. The
    # key underneath says accent = "A and G — the big bases" and ok = "C and T
    # — the small bases", so every rung authored small-first (`("T", "A")`,
    # `("C", "G")`) painted a small base in the big colour and a big base in
    # the small one. Four of ten boxes on `how-we-worked-out-dna`.
    #
    # The widths were right throughout, which is exactly why it survived: the
    # drawing was structurally correct and only the colour lied. A student who
    # reads the key and applies it classifies T and C as the big bases — the
    # inversion of the one fact the figure exists to teach, and the fact the
    # "every rung is one big + one small" argument rests on.
    #
    # Derived from the same letter that picks the width, so the two encodings
    # cannot drift apart again: one lookup, one truth.
    TINT = {"A": _SVG_ACCENT_TINT, "G": _SVG_ACCENT_TINT,
            "C": _SVG_OK_TINT, "T": _SVG_OK_TINT}

    # ⊕ MRB-254 — STILL 760 WIDE, 40 TALLER. The two repairs below cost no
    # width: the vertical guide they replace was itself occupying the whole
    # right-hand third (a 2px line at x=515 and a label running to x≈721), and
    # the "now twist it" panel moves into exactly the space it vacates. The
    # ladder, the rung labels and the key are at the coordinates they were at.
    W, PAD_TOP, ROW_H, BAR_W = 760, 34, 62, 26
    # ⚠️ 200, not 300. At 300 the ladder sat centred with 200px of dead space on
    # its left, and the constant-width guide's label ran off the right-hand edge
    # of the viewBox — it rendered as "every rung the same", losing the one word
    # that carries the whole point. Nothing warns: SVG text simply draws outside
    # the box and is clipped. Moving the ladder left buys the label its room and
    # spends space that was doing nothing.
    MID = 200.0                       # centre of the rung span
    H = PAD_TOP + len(rungs) * ROW_H + 136

    for left, right in rungs:
        for b in (left, right):
            if b not in SIZE:
                raise ValueError(
                    "base-pairs figure %r names base %r, which is not one of "
                    "A, T, C or G." % (fig.get("id"), b))
        # ⚖️ The constant width is an ASSERTION, not a hope. If a pair ever
        # summed differently the drawing would quietly teach that rungs vary,
        # which is the opposite of the lesson — so it fails the build instead.
        if SIZE[left] + SIZE[right] != BIG + SMALL:
            raise ValueError(
                "base-pairs figure %r pairs %s with %s, which are both %s. Every "
                "rung must pair a big base with a small one — that is why the "
                "molecule has a constant width, and a rung that does not would "
                "draw a helix that could not exist."
                % (fig.get("id"), left, right, WORD[left]))

    out = [_svg_open(fig, W, H)]
    span = BIG + SMALL
    x0 = MID - span / 2.0

    # The two backbones, drawn as continuous bars so they read as one molecule
    # each rather than as a stack of blocks.
    top, bot = PAD_TOP, PAD_TOP + len(rungs) * ROW_H
    for bx in (x0 - BAR_W - 10, x0 + span + 10):
        out.append('<rect x="%.1f" y="%s" width="%s" height="%s" rx="12" '
                   'style="fill:%s;stroke:%s" stroke-width="2"/>'
                   % (bx, top, BAR_W, bot - top, _SVG_BAND, _SVG_INK))
    out.append(_svg_text(x0 - BAR_W / 2.0 - 10, top - 12, "backbone", size=13,
                         fill=_SVG_INK_MUTED, weight="700", family=_SVG_MONO))
    out.append(_svg_text(x0 + span + BAR_W / 2.0 + 10, top - 12, "backbone",
                         size=13, fill=_SVG_INK_MUTED, weight="700",
                         family=_SVG_MONO))

    for i, (left, right) in enumerate(rungs):
        cy = PAD_TOP + i * ROW_H + ROW_H / 2.0
        lw, rw = SIZE[left], SIZE[right]
        # Left base from the left backbone, right base meeting it in the middle.
        # `data-base` / `data-size` are HOOKS FOR THE GATE, and MRB-257
        # decision 4 is why they exist: "every code-drawn figure's parity rows
        # must include at least one assertion tying the visual encoding to the
        # scientific fact it teaches." The colour defect above passed parity
        # for weeks because no row could name a box's base — every rect looked
        # like every other rect to a selector. Now `rect[data-base="T"]` is a
        # thing a parity row can measure the fill of, and the inversion cannot
        # come back without a red gate.
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="34" rx="9" '
                   'data-base="%s" data-size="%s" '
                   'style="fill:%s;stroke:%s" stroke-width="2"/>'
                   % (x0, cy - 17, lw, e(left), e(WORD[left]),
                      TINT[left], _SVG_INK))
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="34" rx="9" '
                   'data-base="%s" data-size="%s" '
                   'style="fill:%s;stroke:%s" stroke-width="2"/>'
                   % (x0 + lw, cy - 17, rw, e(right), e(WORD[right]),
                      TINT[right], _SVG_INK))
        out.append(_svg_text(x0 + lw / 2.0, cy + 7, left, size=19,
                             weight="800", family=_SVG_MONO))
        out.append(_svg_text(x0 + lw + rw / 2.0, cy + 7, right, size=19,
                             weight="800", family=_SVG_MONO))
        # The join, so the pair reads as two things held together rather than
        # as one block that happens to be two colours.
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                   'style="stroke:%s" stroke-width="2" stroke-dasharray="4 3"/>'
                   % (x0 + lw, cy - 17, x0 + lw, cy + 17, _SVG_INK_MUTED))
        out.append(_svg_text(x0 + span + BAR_W + 34, cy + 5,
                             "%s with %s" % (left, right), size=14,
                             fill=_SVG_INK_BODY, weight="600", anchor="start"))

    # ⊕ MRB-254 — THE CONSTANT-WIDTH GUIDE, RE-DRAWN. IT WAS MEASURING THE
    # WRONG AXIS.
    #
    # It used to be a VERTICAL line at `x0 + span + BAR_W + 210` — 236px to the
    # right of the rungs — running from the top of the stack to the bottom of
    # it, with a tick at each end and the words "every rung the same width"
    # beside it. Every property of that mark says HEIGHT. It is vertical, it
    # spans the full stack top to bottom, its ticks cap the first and last
    # rows, and it is nowhere near the thing it refers to. Read as a
    # dimension — which is exactly what it is drawn as — it says "the stack is
    # this tall", and the one word it carries then has to argue the reader out
    # of what the drawing shows them. On a figure whose entire argument is that
    # a horizontal distance never changes, the mark for that distance was the
    # one line pointing the other way.
    #
    # A width is measured across the thing that has it. So: two horizontal
    # dimension lines, drawn ON the rungs, spanning exactly the base pair from
    # the left edge of the left base to the right edge of the right one — with
    # extension lines up into the boxes, which is what makes it read as a
    # measurement of THOSE boxes rather than a rule that happens to be under
    # them. Two of them, on the first rung and the last, because sameness is
    # shown by measuring twice and because the first and last rungs are the two
    # a reader compares by eye anyway. They are the same length, they start and
    # end at the same two x values, and the label sits centred beneath.
    #
    # ⚠️ Both dimension lines span `span`, which is `BIG + SMALL` — the SAME
    # constant the loop above raises on. There is no second source for the
    # number: if a rung could ever be a different width the build has already
    # failed before this line runs.
    def _dim(y, tick_up):
        """One horizontal dimension line across the pair, with extension
        lines. `tick_up` puts the extensions above the line (for a mark drawn
        under a rung) or below it."""
        s = []
        s.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                 'style="stroke:%s" stroke-width="2"/>'
                 % (x0, y, x0 + span, y, _SVG_ACCENT))
        for ex in (x0, x0 + span):
            s.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                     'style="stroke:%s" stroke-width="2"/>'
                     % (ex, y, ex, y - 7 if tick_up else y + 7, _SVG_ACCENT))
        return "".join(s)

    first_cy = PAD_TOP + ROW_H / 2.0
    last_cy = PAD_TOP + (len(rungs) - 1) * ROW_H + ROW_H / 2.0
    out.append(_dim(first_cy + 22, True))
    out.append(_dim(last_cy + 22, True))
    out.append(_svg_text(x0 + span / 2.0, last_cy + 46,
                         d.get("guide_label")
                         or "every rung the same width", size=13,
                         fill=_SVG_ACCENT_TEXT, weight="700"))

    # ⊕ MRB-254 — "NOW TWIST IT". A STUDENT COULD FINISH B10 WITHOUT EVER
    # SEEING A HELIX.
    #
    # The lesson's KEY FACT is "two strands TWISTED ROUND EACH OTHER, with the
    # bases paired on the inside". `model-builder` argues its way to the
    # pairing and draws nothing; this figure drew the pairing as a flat ladder,
    # which is the right way to show why a big base must meet a small one and
    # is not a picture of DNA. Nothing else in the unit draws one. So the shape
    # every student can already half-picture — the one thing about this
    # molecule that has escaped into general culture — was the one shape the
    # unit never put in front of them, and the page's own words for it had
    # nothing to attach to.
    #
    # It is the SAME ladder, stated as such and drawn as such: the same two
    # backbones, the same five rungs, the same colours, turned. Drawn as a
    # projection, so the rungs foreshorten towards the crossovers — which is
    # honest and is the reason the width claim is repeated here in the form it
    # takes once the thing is twisted. THE WIDTH OF A HELIX IS ITS DIAMETER,
    # and the two dashed envelope lines with a dimension across them are the
    # same measurement as the two on the ladder, on the same figure, so a
    # reader can see they are one claim rather than two.
    hx = x0 + span + BAR_W + 310          # centre of the twisted panel
    hy0, hy1 = top + 24, bot - 4
    # ⚖️ THE HELIX'S DIAMETER IS THE LADDER'S RUNG WIDTH, exactly, because it
    # is the same molecule. `span` is `BIG + SMALL` — the constant every rung
    # is asserted against a hundred lines above — so the dimension across the
    # twisted panel and the two dimensions across the ladder are the same
    # number by construction, not by two authors agreeing. That is the whole
    # reason the width claim can be repeated here without becoming a second
    # source for it.
    amp = span / 2.0                       # half the diameter, in user units
    turn = (hy1 - hy0) / 2.0               # two full turns down the panel

    # ⚠️ A HELIX DRAWN WITHOUT A DEPTH BREAK IS NOT A HELIX, IT IS A COLUMN OF
    # LOZENGES. Two full sine curves in antiphase meet at every half-turn, and
    # with both drawn end to end the eye closes each meeting into an eye shape
    # and stacks them. The first render of this panel came out as four lenses
    # in a row and nothing about it said "spiral".
    #
    # What makes it read is the one thing a projection carries and a pair of
    # curves does not: WHICH STRAND IS IN FRONT. The helix is
    # `x = sin θ, z = cos θ`, so a strand is in front exactly where `cos θ > 0`
    # — and the fix is the draughtsman's: paint what is behind, then paint what
    # is in front over the top of it, with a casing in the ground colour so it
    # genuinely occludes rather than merely overlapping.
    def _runs(phase):
        """The strand, split into (front?, points) runs by depth."""
        n, runs, cur, cur_front = 120, [], [], None
        for k in range(n + 1):
            y = hy0 + (hy1 - hy0) * k / float(n)
            th = 2 * math.pi * (y - hy0) / turn + phase
            x = hx + amp * math.sin(th)
            front = math.cos(th) > 0
            if cur_front is None:
                cur_front = front
            if front != cur_front:
                # Carry the boundary point into both runs so the curve has no
                # gap at the crossover — the break is in DEPTH, not in the
                # molecule.
                cur.append((x, y))
                runs.append((cur_front, cur))
                cur, cur_front = [(x, y)], front
            cur.append((x, y))
        runs.append((cur_front, cur))
        return runs

    def _d(pts):
        return "".join("%s%.1f,%.1f" % ("M " if i == 0 else " L ", p[0], p[1])
                       for i, p in enumerate(pts))

    strands = [_runs(0.0), _runs(math.pi)]
    # 1 · everything behind.
    for runs in strands:
        for front, pts in runs:
            if not front:
                out.append('<path d="%s" style="fill:none;stroke:%s" '
                           'stroke-width="3" stroke-linecap="round"/>'
                           % (_d(pts), _SVG_INK_MUTED))
    # 2 · the rungs. Behind the front strand, because they run between the two
    # backbones and one of those two is nearer the reader than they are.
    #
    # ⚠️ EVENLY IN Y, AND THE ONES AT A CROSSOVER ARE NOT DRAWN. The rungs were
    # first placed at five positions to match the ladder's five, which put one
    # of them exactly on a crossover — where the two strands are at the same x
    # and the rung between them has zero length. It rendered as nothing, which
    # is the correct picture of an impossible thing and a silent hole in a
    # figure. Separation in this projection is `2·amp·|sin θ|`, so a rung is
    # only drawn where that clears the width of the strokes it runs between;
    # near a half-turn the rung really is edge-on to the reader and really
    # cannot be seen, and omitting it is what the projection says.
    #
    # The count is therefore NOT tied to `rungs`. It was, briefly, on the
    # reasoning that the two panels should be countably the same molecule —
    # but the ladder is five rungs because the lesson names five pairs, and the
    # helix is a picture of a molecule that has millions. A reader who counts
    # the spiral's rungs and gets five would have learned something false.
    _HELIX_RUNGS = 13
    for i in range(_HELIX_RUNGS):
        y = hy0 + (hy1 - hy0) * (i + 0.5) / float(_HELIX_RUNGS)
        th = 2 * math.pi * (y - hy0) / turn
        a = hx + amp * math.sin(th)
        b = hx + amp * math.sin(th + math.pi)
        if abs(a - b) < 26:
            continue
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                   'style="stroke:%s" stroke-width="2.2" '
                   'stroke-linecap="round"/>' % (a, y, b, y, _SVG_INK_BODY))
    # 3 · everything in front, cased in the ground so it cuts what it crosses.
    for runs in strands:
        for front, pts in runs:
            if front:
                out.append('<path d="%s" style="fill:none;stroke:%s" '
                           'stroke-width="8" stroke-linecap="round"/>'
                           % (_d(pts), _SVG_GROUND))
                out.append('<path d="%s" style="fill:none;stroke:%s" '
                           'stroke-width="3.4" stroke-linecap="round"/>'
                           % (_d(pts), _SVG_INK))
    # The envelope: the width, once it is twisted, is the diameter — and it is
    # the same distance the two dimension lines on the ladder measure.
    for ex in (hx - amp, hx + amp):
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                   'style="stroke:%s" stroke-width="1.6" '
                   'stroke-dasharray="5 5"/>'
                   % (ex, hy0 - 6, ex, hy1 + 18, _SVG_RULE_STRONG))
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
               'style="stroke:%s" stroke-width="2"/>'
               % (hx - amp, hy1 + 18, hx + amp, hy1 + 18, _SVG_ACCENT))
    for ex in (hx - amp, hx + amp):
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                   'style="stroke:%s" stroke-width="2"/>'
                   % (ex, hy1 + 18, ex, hy1 + 11, _SVG_ACCENT))
    out.append(_svg_text(hx, hy1 + 42, "still the same width", size=13,
                         fill=_SVG_ACCENT_TEXT, weight="700"))
    out.append(_svg_text(hx, top + 8, "the same ladder, twisted", size=14,
                         fill=_SVG_INK, weight="700"))

    ly = bot + 74
    out.append('<line x1="0" y1="%s" x2="%d" y2="%s" style="stroke:%s" '
               'stroke-width="2"/>' % (ly - 18, W, ly - 18, _SVG_RULE_STRONG))
    for j, (letters, word, tint) in enumerate(
            [("A and G", "the big bases", _SVG_ACCENT_TINT),
             ("C and T", "the small bases", _SVG_OK_TINT)]):
        kx = 18 + j * 300
        # The swatch is drawn at the base's OWN width — 34 for a small base and
        # 52 for a big one — so the key repeats the size distinction rather than
        # reducing it to two colours. That is the never-colour-alone rule doing
        # real work: the widths in the key are the widths in the drawing.
        out.append('<rect x="%s" y="%s" width="%s" height="22" rx="7" '
                   'style="fill:%s;stroke:%s" stroke-width="2"/>'
                   % (kx, ly + 4, 34 if j else 52, tint, _SVG_INK))
        out.append(_svg_text(kx + (34 if j else 52) + 12, ly + 20,
                             "%s — %s" % (letters, word), size=13,
                             fill=_SVG_INK_BODY, weight="600", anchor="start"))
    out.append('</svg>')
    return "".join(out)
# ── the Punnett square for Pp × Pp (b10-04) ──────────────────────────────

_PUNNETT_GRID_X, _PUNNETT_GRID_Y, _PUNNETT_CELL = 300.0, 240.0, 140.0
# ── the Punnett square for Pp × Pp (b10-04) ──────────────────────────────

_PUNNETT_GRID_X, _PUNNETT_GRID_Y, _PUNNETT_CELL = 300.0, 240.0, 140.0
# ── the Punnett square for Pp × Pp (b10-04) ──────────────────────────────

_PUNNETT_GRID_X, _PUNNETT_GRID_Y, _PUNNETT_CELL = 300.0, 240.0, 140.0
def _punnett_flower(cx, cy, filled, scale=1.0):
    """One flower mark. FILLED is the dominant phenotype, OPEN is the
    recessive one.

    ⛔ NEVER A HUE. Purple and white are the two phenotypes this lesson names,
    and painting them purple and white is the one thing this figure may not do:
    `--ks3-data` is not in the shipped token set, a literal purple is a colour
    Design never specified, and a white-on-cream flower is not a flower. So the
    distinction is FILL INVERSION — solid petals against outlined ones — which
    is the same device the reproductive-systems figure uses for "this one has
    no counterpart", and every mark carries its phenotype in words beside it
    regardless.
    """
    out = []
    petal = 15.0 * scale
    for k in range(5):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        px = cx + math.cos(a) * petal
        py = cy + math.sin(a) * petal
        out.append(_ellipse(px, py, petal * 0.72, petal * 0.72,
                            fill=_SVG_INK_BODY if filled else _SVG_GROUND,
                            stroke=_SVG_INK, w=2))
    out.append(_circle(cx, cy, petal * 0.5,
                       fill=_SVG_BAND if filled else _SVG_CARD,
                       stroke=_SVG_INK, w=2))
    return "".join(out)
def _punnett_gamete(cx, cy, letter, r=25.0):
    """A gamete badge: the single letter one parent puts into one seed."""
    return (_circle(cx, cy, r, fill=_SVG_CARD, stroke=_SVG_INK, w=2.5)
            + _label(cx, cy + 9, letter, size=25, weight="800",
                     family=_SVG_MONO))
def _punnett(fig):
    """Pp x Pp, all four combinations, and the 3 : 1 read off them.

    ⚖️ WHY THIS LESSON GETS A DIAGRAM (WS1 audit #8). The bench beside it grows
    a hundred seeds and returns TALLIES — "Purple 77 · 77%", "Ratio 3.35 : 1".
    It is a good instrument and it is deliberately unseeded, so a student who
    runs it twice gets two numbers either side of three and learns that chance
    decides each seed. What it never shows is WHY three. The four gamete
    combinations that produce the ratio are the mechanism, they happen inside
    the model, and the lesson the page is NAMED FOR is therefore simulated and
    asserted but never explained. A student can leave this page having watched
    3:1 arrive a dozen times without being able to say where it comes from.

    ⚖️ AND IT IS THE MISCONCEPTION'S DIAGRAM TOO. `blending-and-the-skipped-
    generation` (GENE-07) is the claim that a version which is not shown has
    gone away. The bottom-right cell is the refutation and needs no words: both
    parents are purple, both carry p, and one seed in four gets p twice. That
    is why the note sits on that cell and nowhere else — it is the only cell
    where the misconception is visibly wrong.

    ⚖️ THE GAMETES ARE DRAWN LEAVING THE PARENTS. A Punnett square handed to a
    student as a bare 2x2 is a mnemonic: fill in the letters, read off the
    ratio. The two fans of arrows are what make it an ARGUMENT — each parent
    has two versions, passes one, and the grid is every way those two choices
    can land. Without them the row and column headings are just labels.

    ⛔ NO COLOUR CARRIES A FACT. See `_punnett_flower`. Filled against open,
    plus the word, plus the genotype, three channels for two categories.

    ⚠️ THE FOUR CELLS ARE DERIVED, NEVER AUTHORED. `_PUNNETT_*` names the two
    parents and nothing else; every genotype, every phenotype and every mark is
    computed from them, and the ratio line is counted from the computed cells.
    A figure that hardcoded "3 : 1" beside a grid it also hardcoded would agree
    with itself no matter what the grid said, which is the shape of defect the
    base-pair fills were — right structure, lying annotation.
    """
    d = fig.get("data") or {}
    p1 = d.get("parent1") or "Pp"
    p2 = d.get("parent2") or "Pp"
    dom = d.get("dominant") or "purple"
    rec = d.get("recessive") or "white"

    for who, g in (("parent1", p1), ("parent2", p2)):
        if len(g) != 2 or sorted(g.lower()) != ["p", "p"]:
            raise ValueError(
                "punnett figure %r gives %s the genotype %r. This drawer draws "
                "ONE gene with two versions written as the same letter in two "
                "cases — the lesson's P and p — and a genotype outside that is "
                "a different diagram." % (fig.get("id"), who, g))

    # ⚖️ DOMINANT-FIRST, EVERYWHERE, and it is not cosmetic. The bench beside
    # this figure normalises a seed that received p then P to `Pp` and never
    # `pP`, because `pP` on a card reads as a fourth genotype. The grid has to
    # agree with the bench or the page carries two spellings of one thing.
    def _norm(a, b):
        return (a + b) if a.isupper() else (b + a)

    # ⚠️ DOMINANT FIRST, AND `sorted(reverse=True)` DOES NOT DO IT. Lowercase
    # `p` is 0x70 and uppercase `P` is 0x50, so a reverse sort puts the
    # RECESSIVE gamete first — which put `pp` in square 1 and `PP` in square 4,
    # and then the bracket that gathers "three of the four, purple" gathered
    # squares 1 to 3, the first of which was the white one. The grid was right
    # and the thing reading it off was wrong: exactly the base-pair defect,
    # where the structure is correct and only the annotation lies.
    cols = sorted(set(p1), key=lambda c: (c.islower(), c))
    rows = sorted(set(p2), key=lambda c: (c.islower(), c))
    if len(cols) != 2 or len(rows) != 2:
        raise ValueError(
            "punnett figure %r asks for a cross where a parent gives only one "
            "kind of gamete. The 3 : 1 is a property of TWO carriers, and a "
            "grid with a repeated row is a different lesson." % fig.get("id"))

    W, H = 900, 812
    GX, GY, C = _PUNNETT_GRID_X, _PUNNETT_GRID_Y, _PUNNETT_CELL
    out = [_svg_open(fig, W, H)]

    out.append(_mono(24, 40, "%s  CROSSED WITH  %s" % (p1, p2), size=14,
                     fill=_SVG_INK_MUTED, spacing="1.4"))

    # ── the two parents, and the choice each of them makes ──
    # Parent 1 above the grid, fanning down into the two column headings;
    # parent 2 to the left, fanning across into the two row headings. The
    # geometry IS the sentence "one from each parent, chosen at random".
    p1cx, p1cy = GX + C, 96.0
    out.append(_rect(p1cx - 74, p1cy - 30, 148, 60, rx=18,
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2.5))
    out.append(_label(p1cx, p1cy + 11, p1, size=28, weight="800",
                      family=_SVG_MONO))
    out.append(_mono(p1cx, p1cy - 46, "PARENT 1", size=13, anchor="middle",
                     fill=_SVG_INK_MUTED, spacing="1.2"))

    p2cx, p2cy = 132.0, GY + C
    out.append(_rect(p2cx - 74, p2cy - 32, 148, 64, rx=18,
                     fill=_SVG_BAND, stroke=_SVG_INK, w=2.5))
    out.append(_label(p2cx, p2cy + 11, p2, size=28, weight="800",
                      family=_SVG_MONO))
    out.append(_mono(p2cx, p2cy - 46, "PARENT 2", size=13, anchor="middle",
                     fill=_SVG_INK_MUTED, spacing="1.2"))

    head_r = 25.0
    col_cx = [GX + C * 0.5, GX + C * 1.5]
    row_cy = [GY + C * 0.5, GY + C * 1.5]
    head_y = GY - 50.0
    head_x = GX - 46.0

    for j, letter in enumerate(cols):
        # ⚠️ THE FAN NEEDS ROOM TO BE A FAN. Drawn from the badge's edge to the
        # gamete circle's edge, these were first given 3px of vertical travel
        # and rendered as two horizontal stubs with their heads pointing away
        # from the circles — an arrow that says nothing about where it goes.
        # The badge sits higher and the headings lower so each arrow has a
        # real diagonal, which is the whole content of the mark: this parent,
        # that gamete.
        out.append(_arrow(p1cx + (-42 if j == 0 else 42), p1cy + 32,
                          col_cx[j], head_y - head_r - 7,
                          stroke=_SVG_ACCENT, w=2.4, head=9,
                          data_gamete=letter, data_from="parent1"))
        out.append(_punnett_gamete(col_cx[j], head_y, letter, head_r))
    for i, letter in enumerate(rows):
        out.append(_arrow(p2cx + 76, p2cy + (-40 if i == 0 else 40),
                          head_x - head_r - 6, row_cy[i],
                          stroke=_SVG_ACCENT, w=2.4, head=9,
                          data_gamete=letter, data_from="parent2"))
        out.append(_punnett_gamete(head_x, row_cy[i], letter, head_r))

    out.append(_mono(p1cx + 96, p1cy + 6, "one or the other,", size=13,
                     fill=_SVG_ACCENT_TEXT))
    out.append(_mono(p1cx + 96, p1cy + 24, "chosen at random", size=13,
                     fill=_SVG_ACCENT_TEXT))

    # ── the grid ──
    cells = []
    n = 0
    for i, rl in enumerate(rows):
        for j, cl in enumerate(cols):
            n += 1
            g = _norm(cl, rl)
            shows_dom = any(ch.isupper() for ch in g)
            cells.append({"n": n, "g": g, "col": cl, "row": rl,
                          "pheno": dom if shows_dom else rec,
                          "filled": shows_dom,
                          "cx": col_cx[j], "cy": row_cy[i]})

    for c in cells:
        x, y = c["cx"] - C / 2, c["cy"] - C / 2
        out.append(_rect(x, y, C, C, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                         w=2.5, data_cell=c["n"], data_genotype=c["g"],
                         data_col_gamete=c["col"], data_row_gamete=c["row"],
                         data_phenotype=c["pheno"]))
        # The numeral is the cell's second channel and the strip below reads
        # off it — no leader lines, which at four cells would cross twice.
        out.append(_circle(x + 24, y + 24, 15, fill=_SVG_INSET,
                           stroke=_SVG_INK, w=2))
        out.append(_label(x + 24, y + 29, str(c["n"]), size=14, weight="700",
                          family=_SVG_MONO))
        out.append(_label(c["cx"], y + 58, c["g"], size=32, weight="800",
                          family=_SVG_MONO, data_cell_genotype=c["n"]))
        out.append(_punnett_flower(c["cx"], y + 96, c["filled"]))
        out.append(_label(c["cx"], y + 128, c["pheno"], size=15, weight="700",
                          fill=_SVG_INK_BODY))

    # ⚖️ The note sits on the recessive cell and on no other, because it is the
    # only cell where the skipped generation is visibly happening.
    rec_cell = [c for c in cells if not c["filled"]]
    if len(rec_cell) != 1:
        raise ValueError(
            "punnett figure %r produces %d recessive cell(s). The whole figure "
            "is the argument that exactly one of the four combinations shows "
            "the hidden version." % (fig.get("id"), len(rec_cell)))
    rc = rec_cell[0]
    nx = rc["cx"] + C / 2 + 26
    out.append(_line(rc["cx"] + C / 2 + 4, rc["cy"], nx - 4, rc["cy"],
                     stroke=_SVG_ACCENT, w=2, dash="5 4"))
    out.append(_mono(nx, rc["cy"] - 8, "neither parent is", size=13,
                     fill=_SVG_ACCENT_TEXT))
    out.append(_mono(nx, rc["cy"] + 10, "%s. This one is." % rec, size=13,
                     fill=_SVG_ACCENT_TEXT))

    # ── the strip: the same four, in a row, so they can be counted ──
    sy = GY + 2 * C + 74
    out.append(_line(24, sy - 40, W - 24, sy - 40, stroke=_SVG_RULE, w=2))
    out.append(_mono(24, sy - 14, "COUNT THE FOUR", size=13,
                     fill=_SVG_INK_MUTED, spacing="1.2"))
    sx0, step = 150.0, 170.0
    for k, c in enumerate(cells):
        cx = sx0 + k * step
        out.append(_circle(cx - 46, sy + 24, 14, fill=_SVG_INSET,
                           stroke=_SVG_INK, w=2))
        out.append(_label(cx - 46, sy + 29, str(c["n"]), size=13,
                          weight="700", family=_SVG_MONO))
        out.append(_punnett_flower(cx - 4, sy + 24, c["filled"], scale=0.86))
        out.append(_label(cx + 44, sy + 30, c["g"], size=21, weight="800",
                          family=_SVG_MONO, data_strip_genotype=c["n"]))

    # The two brackets, each spanning exactly the entries it counts. Drawn, so
    # the ratio is READ OFF the strip rather than printed beside it.
    #
    # ⚠️ GROUPED BY PHENOTYPE, NEVER BY POSITION. This was `cells[:n_dom]` and
    # `cells[n_dom:]` — three cells then one — which is right only because the
    # dominant squares happen to come first, and they only happen to come first
    # because of the gamete ordering fixed above. The first version of that
    # ordering put `pp` in square 1, and this bracket then gathered squares 1
    # to 3 and labelled them PURPLE with the white one inside it. So the run is
    # found from the phenotypes themselves, and a phenotype that is not
    # contiguous fails the build rather than being bracketed across a cell it
    # does not contain.
    by = sy + 58
    runs, run = [], [cells[0]]
    for c in cells[1:]:
        if c["pheno"] == run[-1]["pheno"]:
            run.append(c)
        else:
            runs.append(run)
            run = [c]
    runs.append(run)
    seen = [r[0]["pheno"] for r in runs]
    if len(set(seen)) != len(seen):
        raise ValueError(
            "punnett figure %r lays its squares out as %s. A bracket spans a "
            "CONTIGUOUS run, so a phenotype that appears in two separate runs "
            "cannot be gathered under one — and a bracket drawn across the "
            "gap would enclose a square it is not counting."
            % (fig.get("id"), " ".join(c["pheno"] for c in cells)))
    n_dom = sum(1 for c in cells if c["filled"])
    for span in runs:
        k0, k1 = cells.index(span[0]), cells.index(span[-1])
        word, count = span[0]["pheno"], len(span)
        x0 = sx0 + k0 * step - 62
        x1 = sx0 + k1 * step + 66
        out.append(_path("M %s,%s V %s H %s V %s"
                         % (_n(x0), _n(by), _n(by + 12), _n(x1), _n(by)),
                         stroke=_SVG_ACCENT, w=2.4))
        out.append(_label((x0 + x1) / 2, by + 36,
                          "%d of the four — %s" % (count, word),
                          size=15, weight="700", fill=_SVG_ACCENT_TEXT,
                          data_tally=word, data_tally_count=count,
                          data_tally_from=span[0]["n"],
                          data_tally_to=span[-1]["n"]))

    out.append(_label(24, by + 92,
                      "%d %s : %d %s"
                      % (n_dom, dom, len(cells) - n_dom, rec),
                      size=30, weight="800", anchor="start",
                      family=_SVG_DISPLAY, data_ratio="1"))
    out.append(_mono(24, by + 118,
                     "filled flower = %s  ·  open flower = %s" % (dom, rec),
                     size=13, fill=_SVG_INK_MUTED))
    out.append(_label(W - 30, by + 88,
                      "P beats p. A plant is %s only if it gets p from "
                      "both parents." % rec,
                      size=14, weight="600", anchor="end",
                      fill=_SVG_INK_BODY))
    out.append('</svg>')
    return "".join(out)
# ── ⊕ MRB-254 · WS1 #1, b10-nested-scale — Design's fig-01, ported ───────
#
# Every number below is Design's. The tables are here rather than inside the
# function because they are the parts a reader might want to check line for
# line against her `renderVals()` and her `<svg>`, and a five-row coordinate
# grid buried 200 lines into a drawing is a table nobody checks.

# ── the nucleus grid ────────────────────────────────────────────────────
#
# 5 rows × 5 columns = 25 slots, two of them skipped, 23 remaining, each drawn
# as a PAIR of marks. 23 × 2 = 46, which is the number the panel's own label
# claims. Design's comment in `renderVals()` says exactly why the grid is built
# this way rather than drawn: *"46 marks, so a student who counts them finds
# the number the label claims."*
#
# ⊕ THE TWO SKIPPED SLOTS ARE THE FIRST AND THE LAST, which is why the
# surviving slot numbers are 1…23 with no gap in them, and why `data-pair` can
# carry the slot index directly and still read as "pair 1 of 23". That is a
# property of `_NESTED_SCALE_SKIP` being exactly `(0, 24)`, not a coincidence
# to rely on blindly — move a skip into the middle and the pair numbers grow a
# hole, which the count row would catch (still 46 marks, still 23 pairs) but
# the numbering would no longer be 1…23.
_NESTED_SCALE_ROWS = (356, 382, 408, 434, 460)
_NESTED_SCALE_COLS = (176, 201, 226, 251, 276)
_NESTED_SCALE_SKIP = (0, 24)
_NESTED_SCALE_PICKED = 1          # the slot whose second member the figure follows
# ── the four callout wedges ─────────────────────────────────────────────
#
# `(from panel, to panel, wedge fill, upper dashed edge, lower dashed edge,
#   the orange ribbon that carries the strand across the gap)`.
#
# The ribbon is the part that matters and the part that would be easiest to
# drop as decoration: it is the followed strand LEAVING one frame and ARRIVING
# in the next, drawn across the white space between them, so the continuity
# claim is on the page rather than in the caption.
_NESTED_SCALE_WEDGES = (
    (1, 2,
     "M 192,182 L 36,300 L 416,300 L 260,182 Z",
     "M 192,182 L 36,300", "M 260,182 L 416,300",
     "M 222,240 C 218,262 196,282 180,300 L 222,300 C 228,282 230,262 230,240 Z"),
    (2, 3,
     "M 176,378 L 36,556 L 416,556 L 226,378 Z",
     "M 176,378 L 36,556", "M 226,378 L 416,556",
     "M 196,498 C 192,518 168,538 152,556 L 208,556 C 210,538 208,518 206,498 Z"),
    (3, 4,
     "M 340,792 L 36,852 L 416,852 L 372,792 Z",
     "M 340,792 L 36,852", "M 372,792 L 416,852",
     "M 344,786 C 340,808 318,832 288,852 L 340,852 C 356,832 358,808 358,786 Z"),
    (4, 5,
     "M 192,990 L 36,1108 L 416,1108 L 250,990 Z",
     "M 192,990 L 36,1108", "M 250,990 L 416,1108",
     "M 206,1050 C 200,1070 174,1090 156,1108 L 256,1108 C 250,1090 234,1070 232,1050 Z"),
)
# ── the caption block beside each frame ─────────────────────────────────
#
# `(frame top, numeral, heading, magnification, body lines)`. Design lays every
# block out against the top of its own frame — badge at +4, numeral at +26,
# heading at +28, magnification at +62, body from +92 in 22s — and holds that
# rule across all five, including the frame that is 236 tall rather than 210.
# So the offsets are computed from `top` here instead of being five sets of
# absolute y values that only a diff could tell apart.
_NESTED_SCALE_CAPTIONS = (
    (44, "01", "A cell", "0.02 mm across",
     ("Any body cell will do. The instructions",
      "are kept in the nucleus.")),
    (300, "02", "The nucleus", "0.006 mm across",
     ("46 chromosomes, in 23 pairs. We follow",
      "one of them from here down.")),
    (556, "03", "A chromosome", "0.002 mm long",
     ("One DNA molecule, coiled and wound",
      "around proteins. Not a different",
      "substance from DNA — DNA, packed.")),
    (852, "04", "A gene", "a section of the same strand",
     ("A length of it, carrying the instruction",
      "for one characteristic. Part of the",
      "strand, not an object attached to it.")),
    (1108, "05", "The bases", "0.0000003 mm apart",
     ("Four letters, paired across the strand.",
      "The order of them along the gene is",
      "the information.")),
)
# The proteins the strand is wound around in panel 03. Literal in Design's
# delivery — the zigzag is composed, not generated.
_NESTED_SCALE_PROTEINS = ((205, 582), (155, 602), (205, 622),
                          (155, 642), (205, 662), (155, 682))
# Panel 05: `(x, top letter, bottom letter)`. A is always across from T and C
# is always across from G — the pairing rule, held as data so a row can assert
# it rather than four pairs of hand-placed strings that could each be wrong on
# their own.
_NESTED_SCALE_BASES = ((116, "A", "T"), (196, "C", "G"),
                       (276, "T", "A"), (356, "G", "C"))
# The gene in panel 04: the x range of the thickened stretch of backbone, and
# of the bracket under it. ONE pair of numbers, used by both, because the claim
# the panel makes is that they are the same length.
_NESTED_SCALE_GENE = (158, 280)
def _nested_scale(fig):
    """One DNA molecule at five magnifications, each frame cut out of the one
    above it, with a single orange strand running the whole height of the plate.

    ⚖️ THE CONTINUITY IS THE FIGURE. b10's named misconception is that a
    chromosome, a gene and DNA are *three different things in the nucleus*, and
    the bench beside this figure renders six equally-sized sibling cards stacked
    down the page — so the bench's own layout teaches the misconception it is
    trying to correct. Six cards of equal weight say six things; they cannot say
    "one thing at three magnifications", because nothing in a stack of siblings
    is inside anything else. This drawing says it structurally: every frame is
    entered through a wedge whose narrow end sits on the dashed ring in the
    frame above, and the orange strand is drawn CROSSING each wedge, so it
    leaves one frame and arrives in the next without a break. A reader can put a
    finger on the fleck in panel 01 and trace it to a letter in panel 05 without
    lifting it.

    ⚖️ AND IT IS ASSERTABLE, NOT MERELY DRAWN. Three hooks carry the three
    claims a screenshot cannot check:

      · `data-followed="1"` + `data-panel="1"…"5"` on exactly ONE element per
        panel — the fleck, the picked chromosome, the coiled strand, the upper
        backbone, the upper backbone again. Five elements, five panels, and a
        row can assert all five resolve to the SAME computed stroke. That
        identity of paint is what carries "this is the same molecule"; if panel
        04's backbone drifted to a different orange the drawing would still look
        right and the claim would be gone.
      · `data-chromosome="1"…"46"`, `data-pair`, `data-member` on all 46 marks
        in panel 02 — see the note on the grid table above. The label says 46,
        so 46 has to be countable, and a row can check the indices are 1…46 with
        none missing or repeated and that they fall into 23 pairs of exactly two.
      · `data-zoom-from` / `data-zoom-to` on every wedge, so a row can assert
        panel N is opened from panel N−1 and from no other. A wedge drawn from
        the WRONG frame still looks exactly like a wedge — this is the one
        defect in the figure that is invisible to the eye and to a screenshot,
        which is what MRB-257 decision 4 means by measuring the encoding rather
        than the frame.

    ⚖️ THE GENE IS A SEGMENT, NOT AN OBJECT. Panel 04's whole job is that a
    gene is a marked LENGTH of the strand that was coiled in panel 03, not a
    bead sitting on it. So the thickened stretch of backbone and the bracket
    beneath it are drawn from the same pair of numbers (`_NESTED_SCALE_GENE`)
    and both carry `data-gene-from` / `data-gene-to`: a row can assert the
    bracket spans exactly the thickened length, and the two cannot drift apart.

    ⚠️ `jitter` IS A HASH, NOT A RANDOM. `Math.sin(n * 12.9898) * 43758.5453`,
    fractional part — the standard shader trick. `Math.random()` and
    `Date.now()` appear nowhere in Design's JS and appear nowhere here: the
    build has to be byte-identical run to run, and a scatter that moved between
    builds would make every future diff of this file unreadable. Python and JS
    both evaluate this in IEEE doubles, so the port reproduces her 46 paths bit
    for bit; verified against `node` on the port, not assumed.

    ⚠️ `Math.round`, NOT `round`. Her `r()` is `Math.round(v * 10) / 10`.
    Python's `round` is banker's rounding and JavaScript's `Math.round` is
    round-half-up, so the two disagree on any exact `.5` — and `x * 10` on
    coordinates that are already one-decimal jitter outputs lands on ties. The
    port spells it `math.floor(v * 10 + 0.5) / 10`, which is `Math.round`'s
    definition rather than a near-miss of it.

    ⊕ THE RING IN PANEL 02 IS DERIVED, NOT PLACED. Design hard-codes it at
    `(201, 356)`; that is exactly `COLS[PICKED % 5], ROWS[PICKED // 5]`, i.e.
    the grid slot of the pair the figure follows. Computed here from the same
    two tables, so moving `_NESTED_SCALE_PICKED` moves the ring onto the new
    pair instead of leaving it circling a chromosome nobody follows.

    ⚠️ CLIP IDS ARE DERIVED FROM THE FIGURE ID. Design's are `f1p3`…`f1p5`,
    unique inside a review file holding one figure. A lesson page can hold
    several of these drawings, `id` is document-scoped, and a duplicate
    `clipPath` id means the second figure silently clips to the first one's
    rectangle. Nothing warns; the drawing just loses half of itself.
    """
    W, H = 860, 1400
    cid = e(fig["id"])
    out = [_svg_open(fig, W, H)]

    # The three windows. Raw markup rather than an emitter call because a
    # <clipPath> carries no paint — there is no paint law to keep here.
    out.append(
        '<defs>'
        '<clipPath id="%s-c-p3"><rect x="36" y="556" width="380" '
        'height="236" rx="18"/></clipPath>'
        '<clipPath id="%s-c-p4"><rect x="36" y="852" width="380" '
        'height="210" rx="18"/></clipPath>'
        '<clipPath id="%s-c-p5"><rect x="36" y="1108" width="380" '
        'height="210" rx="18"/></clipPath>'
        '</defs>' % (cid, cid, cid))

    # Design's root group. Round caps and joins on everything: the coil, the
    # chromosome arcs and the strand ends are all organic, and a butt cap on a
    # 10-unit stroke reads as a cut end rather than a continuing molecule.
    out.append('<g fill="none" stroke-linecap="round" stroke-linejoin="round">')

    # ── the four callout wedges, drawn first so every frame sits on top ─────
    #
    # ⚠️ HOOKS ARE SPELLED `data_zoom_from=` AT THE CALL SITE. `_data_attrs`
    # requires the prefix and strips it; a bare `zoom_from=` now RAISES rather
    # than landing as a presentation attribute that does nothing and looks like
    # it does something. A hook a parity row cannot find does not fail the row —
    # it returns nothing and reports green.
    for src, dst, wedge, edge_hi, edge_lo, ribbon in _NESTED_SCALE_WEDGES:
        out.append(_path(wedge, fill=_SVG_ACCENT_TINT, stroke="none",
                         data_zoom_from=src, data_zoom_to=dst))
        for edge in (edge_hi, edge_lo):
            out.append(_path(edge, stroke=_SVG_RULE_STRONG, w=1.6, dash="6 5",
                             data_zoom_from=src, data_zoom_to=dst))
        # The strand itself, crossing the gap. Not `data_followed` — that is
        # one element per PANEL, and this is between two of them.
        out.append(_path(ribbon, fill=_SVG_ACCENT, stroke="none", opacity=0.9,
                         data_zoom_from=src, data_zoom_to=dst,
                         data_strand="carried"))

    # ── panel 01 · a cell ───────────────────────────────────────────────────
    out.append(_rect(36, 44, 380, 210, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_frame="1"))
    out.append(_ellipse(226, 149, 146, 78, fill=_SVG_INSET, stroke=_SVG_INK,
                        w=2.5))
    out.append(_circle(226, 149, 30, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    # Five grey flecks and one orange one. The grey are the other 45 marks at
    # this magnification — unresolvable, and drawn as such rather than omitted,
    # so the nucleus is not an empty circle with one thing in it.
    for d in ("M 213,141 q 6,-7 12,0", "M 228,138 q 7,6 13,-1",
              "M 212,157 q 8,7 15,0", "M 231,160 q 7,-6 12,1",
              "M 219,150 q 6,4 12,-1"):
        out.append(_path(d, stroke=_SVG_INK_FAINT, w=2))
    out.append(_path("M 220,146 q 7,8 14,1", stroke=_SVG_ACCENT, w=3.2,
                     data_followed="1", data_panel="1"))
    out.append(_circle(226, 149, 42, stroke=_SVG_INK, w=1.6, dash="6 5",
                       data_zoom_ring="2"))

    # ── panel 02 · the nucleus, and the 46 ──────────────────────────────────
    out.append(_rect(36, 300, 380, 210, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_frame="2"))
    out.append(_circle(226, 405, 88, fill=_SVG_BAND, stroke=_SVG_INK, w=2.5))
    out.append(_circle(226, 405, 82, stroke=_SVG_INK, w=1.4))

    index = 0
    slot = -1
    for row in _NESTED_SCALE_ROWS:
        for col in _NESTED_SCALE_COLS:
            slot += 1
            if slot in _NESTED_SCALE_SKIP:
                continue
            seed = slot * 7 + 3
            # `jitter(seed)`, `jitter(seed + 1)`, `jitter(seed + 2)`, inlined
            # rather than given a nested helper: the drawer is one function.
            j = []
            for k in (seed, seed + 1, seed + 2):
                x = math.sin(k * 12.9898) * 43758.5453
                j.append(x - math.floor(x))
            cx = col + (j[0] - 0.5) * 7
            cy = row + (j[1] - 0.5) * 7
            angle = (j[2] - 0.5) * 2.2
            for member in (1, 2):
                index += 1
                picked = (slot == _NESTED_SCALE_PICKED and member == 2)
                # The picked one is drawn longer and more strongly bowed as
                # well as orange: the distinction never rests on the hue alone.
                half = 13 if picked else 9
                bow = 6 if picked else 4.5
                px = cx + (-4.5 if member == 1 else 4.5)
                py = cy + (-1.5 if member == 1 else 1.5)
                dx, dy = math.sin(angle), -math.cos(angle)
                pts = (px - dx * half, py - dy * half,
                       px + dy * bow, py - dx * bow,
                       px + dx * half, py + dy * half)
                # `Math.round(v * 10) / 10` — see the ⚠️ in the docstring.
                r = [math.floor(v * 10 + 0.5) / 10.0 for v in pts]
                d = ("M %s,%s Q %s,%s %s,%s"
                     % (_n(r[0]), _n(r[1]), _n(r[2]),
                        _n(r[3]), _n(r[4]), _n(r[5])))
                hooks = {"data_chromosome": index,
                         "data_pair": slot,
                         "data_member": member}
                if picked:
                    hooks["data_followed"] = "1"
                    hooks["data_panel"] = "2"
                out.append(_path(
                    d, stroke=_SVG_ACCENT if picked else _SVG_INK_FAINT,
                    w=4.4 if picked else 2.3, **hooks))

    # Design places this ring at (201, 356). That is the picked pair's own grid
    # slot — computed, so it cannot end up circling the wrong chromosome.
    out.append(_circle(_NESTED_SCALE_COLS[_NESTED_SCALE_PICKED % 5],
                       _NESTED_SCALE_ROWS[_NESTED_SCALE_PICKED // 5],
                       25, stroke=_SVG_INK, w=1.6, dash="6 5",
                       data_zoom_ring="3"))

    # ── panel 03 · one chromosome, coiled ───────────────────────────────────
    out.append(_rect(36, 556, 380, 236, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_frame="3"))
    out.append('<g clip-path="url(#%s-c-p3)">' % cid)
    for cx, cy in _NESTED_SCALE_PROTEINS:
        out.append(_circle(cx, cy, 13, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    # The coil twice: a wide ink stroke underneath, the orange strand on top of
    # it. The ink is the packed chromosome as it is SEEN; the orange inside it
    # is what it is MADE OF. Drawing them as one stroke would make the
    # chromosome a different substance from DNA, which is the sentence in the
    # caption block beside this very frame.
    _coil = ("M 180,566 Q 226,576 180,586 Q 134,596 180,606 Q 226,616 180,626 "
             "Q 134,636 180,646 Q 226,656 180,666 Q 134,676 180,686 "
             "Q 228,698 180,712 Q 130,728 184,742 C 216,756 256,762 300,760 "
             "C 344,758 382,764 %d,770")
    out.append(_path(_coil % 416, stroke=_SVG_INK, w=10))
    # ⚠️ 424, NOT 416, AND IT MAKES NO DIFFERENCE ON THE PAGE. Design's orange
    # ends 8 units right of her ink; the clip rectangle cuts both at 416, so
    # the overrun is invisible and it would be easy to "tidy" the two to the
    # same number. Kept as she drew it — MRB-205, refine inside her shape —
    # and recorded here so the next reader does not spend the same five
    # minutes deciding whether it is a typo. It is harmless either way.
    out.append(_path(_coil % 424, stroke=_SVG_ACCENT, w=6,
                     data_followed="1", data_panel="3"))
    out.append('</g>')
    out.append(_circle(352, 766, 24, stroke=_SVG_INK, w=1.6, dash="6 5",
                       data_zoom_ring="4"))
    out.append(_mono(248, 576, "proteins", size=15, weight="400"))
    out.append(_path("M 244,580 L 216,582", stroke=_SVG_INK_MUTED, w=1.4))

    # ── panel 04 · a gene, as a length of that strand ───────────────────────
    gene_from, gene_to = _NESTED_SCALE_GENE
    out.append(_rect(36, 852, 380, 210, rx=18, fill=_SVG_CARD, stroke=_SVG_INK,
                     w=2.5, data_frame="4"))
    out.append('<g clip-path="url(#%s-c-p4)">' % cid)
    out.append(_rect(gene_from, 920, gene_to - gene_from, 58, rx=10,
                     fill=_SVG_ACCENT_TINT, stroke="none", data_gene="1",
                     data_gene_from=gene_from, data_gene_to=gene_to))
    # Both backbones run the full width of the frame and out of it on either
    # side — the strand does not begin or end here, it passes through.
    out.append(_path("M 30,930 H 422", stroke=_SVG_ACCENT, w=5,
                     data_followed="1", data_panel="4",
                     data_strand="backbone-upper"))
    out.append(_path("M 30,968 H 422", stroke=_SVG_ACCENT, w=5,
                     data_strand="backbone-lower"))
    # The gene: the SAME backbone, drawn thicker over one stretch of it. Not a
    # separate shape laid on top — same paint, same line, more weight.
    out.append(_path("M %d,928 H %d" % (gene_from, gene_to), stroke=_SVG_ACCENT,
                     w=8, data_gene="1", data_gene_from=gene_from,
                     data_gene_to=gene_to, data_strand="backbone-upper"))
    out.append(_path("M %d,970 H %d" % (gene_from, gene_to), stroke=_SVG_ACCENT,
                     w=8, data_gene="1", data_gene_from=gene_from,
                     data_gene_to=gene_to, data_strand="backbone-lower"))
    rungs = " ".join("M %d,932 V 966" % (68 + i * 24) for i in range(14))
    out.append(_path(rungs, stroke=_SVG_INK, w=2.2, data_rungs=14))
    out.append('</g>')
    out.append(_path("M %d,994 v 12 H %d v -12" % (gene_from, gene_to),
                     stroke=_SVG_INK, w=2.5, data_gene="1",
                     data_gene_from=gene_from, data_gene_to=gene_to))
    # Design puts both of these at x=219, which is the midpoint of the gene
    # span — derived here for the same reason the panel-02 ring is: the label
    # and the ring belong to the bracket, and should move with it.
    #
    # ⚠️ `_n(gene_mid)` ON THE TEXT, not the bare float. The shape emitters run
    # `_n` over their coordinates; `_svg_text` does not, so a float x arrives in
    # the markup as `219.0`. It renders identically and it breaks a
    # byte-comparison of two builds, which is the only thing that would ever
    # tell us a drawing had changed by accident.
    gene_mid = (gene_from + gene_to) / 2.0
    out.append(_mono(_n(gene_mid), 1032, "one gene", size=17, fill=_SVG_INK,
                     weight="400", anchor="middle", data_gene="1"))
    out.append(_circle(gene_mid, 949, 30, stroke=_SVG_INK, w=1.6, dash="6 5",
                       data_zoom_ring="5"))
    out.append(_mono(52, 898, "the same strand, uncoiled", size=15,
                     weight="400"))

    # ── panel 05 · the bases ────────────────────────────────────────────────
    out.append(_rect(36, 1108, 380, 210, rx=18, fill=_SVG_CARD,
                     stroke=_SVG_INK, w=2.5, data_frame="5"))
    out.append('<g clip-path="url(#%s-c-p5)">' % cid)
    out.append(_path("M 30,1166 H 422", stroke=_SVG_ACCENT, w=7,
                     data_followed="1", data_panel="5",
                     data_strand="backbone-upper"))
    out.append(_path("M 30,1266 H 422", stroke=_SVG_ACCENT, w=7,
                     data_strand="backbone-lower"))
    out.append('</g>')
    # Each rung in three pieces: down from the top backbone, a short bar
    # BETWEEN the two lettered boxes, and up from the bottom backbone. The
    # middle piece is the bond, and it is what makes the pair a pair.
    for y0, y1, part in ((1170, 1188, "upper"), (1214, 1218, "bond"),
                         (1244, 1262, "lower")):
        d = " ".join("M %d,%d V %d" % (x, y0, y1)
                     for x, _t, _b in _NESTED_SCALE_BASES)
        out.append(_path(d, stroke=_SVG_INK, w=2.2, data_rung_part=part))
    # A is across from T and C is across from G, everywhere, drawn from one
    # table so the four pairs cannot each be wrong on their own.
    for pair, (x, top, bottom) in enumerate(_NESTED_SCALE_BASES, start=1):
        for y, letter, side in ((1188, top, "top"), (1218, bottom, "bottom")):
            out.append(_rect(x - 22, y, 44, 26, rx=8, fill=_SVG_BAND,
                             stroke=_SVG_INK, w=2, data_base_pair=pair,
                             data_base_side=side, data_base=letter))
        out.append(_mono(x, 1207, top, size=18, fill=_SVG_INK, weight="400",
                         anchor="middle", data_base_pair=pair,
                         data_base_side="top", data_base=top,
                         data_base_partner=bottom))
        out.append(_mono(x, 1237, bottom, size=18, fill=_SVG_INK, weight="400",
                         anchor="middle", data_base_pair=pair,
                         data_base_side="bottom", data_base=bottom,
                         data_base_partner=top))
    out.append(_mono(56, 1148, "four rungs of that same length", size=15,
                     weight="400"))

    # ── the caption block beside each frame ─────────────────────────────────
    for top, numeral, heading, magnification, lines in _NESTED_SCALE_CAPTIONS:
        out.append(_rect(452, top + 4, 42, 32, rx=10, fill=_SVG_BAND,
                         stroke=_SVG_INK, w=2))
        out.append(_mono(473, top + 26, numeral, size=17, fill=_SVG_INK,
                         weight="400", anchor="middle"))
        out.append(_label(506, top + 28, heading, size=25, fill=_SVG_INK,
                          weight="800", anchor="start", family=_SVG_DISPLAY,
                          spacing="-.5"))
        # ⚠️ `--ks3-accent-text`, NOT `--ks3-accent`. Accent measures 3.4:1 on
        # the ground and is a graphic value only; `_svg_text` refuses it under
        # 24px at source, and this is 16px.
        out.append(_mono(452, top + 62, magnification, size=16,
                         fill=_SVG_ACCENT_TEXT, weight="400"))
        for n, line in enumerate(lines):
            out.append(_label(452, top + 92 + n * 22, line, size=17,
                              fill=_SVG_INK_BODY, weight="400",
                              anchor="start"))
    # Panel 03's block carries a sixth line, set bold and dropped clear of the
    # other three: it is the sentence that hands the reader on to panel 04.
    out.append(_label(452, 726, "It unwinds at the bottom of the frame.",
                      size=17, fill=_SVG_INK, weight="700", anchor="start"))

    # ── the legend ──────────────────────────────────────────────────────────
    #
    # Two swatches, and both of them are LABELLED. Orange is not carrying "DNA"
    # on its own anywhere on this plate — every panel names what it is showing
    # in words beside it — but the legend is what makes the one rule explicit,
    # and it is the sentence the whole column depends on.
    out.append(_path("M 36,1348 H 824", stroke=_SVG_RULE, w=2))
    out.append(_path("M 44,1376 h 34", stroke=_SVG_ACCENT, w=6,
                     data_legend="dna"))
    out.append(_label(88, 1382, "DNA — the same molecule in all five panels",
                      size=17, fill=_SVG_INK, weight="700", anchor="start",
                      data_legend="dna"))
    out.append(_path("M 470,1376 h 34", stroke=_SVG_INK, w=6,
                     data_legend="not-dna"))
    out.append(_label(514, 1382, "Everything that is not DNA", size=17,
                      fill=_SVG_INK, weight="400", anchor="start",
                      data_legend="not-dna"))

    out.append('</g>')
    out.append('</svg>')
    return "".join(out)
# ⚖️ SIX LEVELS AND FOUR QUESTIONS, BOTH CLOSED. Design's `isDone()` for
# `s-bench` is `s.shown >= LEVELS.length` and the `s-model` band stop mirrors
# it, so the level count IS the rail threshold on two stops (MRB-249). Her own
# progress line says "all six levels" in words, which a seventh row would
# contradict on screen. The four say-it-back questions are one row of tabs on
# one panel and Design draws exactly four.
_B10_ZB_LEVELS = 6
_B10_ZB_QUESTIONS = 4
def _b10_zoom_progress(pg, act_id):
    """b10-02's head readout, validated where it is composed.

    Design's line is `bottomed ? 'all six levels' : 'level ' + shown + ' of ' +
    total` — a count with a bespoke sentence at the TOP end, which is exactly
    `head_counter`'s `format` + `full` shape. Schema §1 names the three
    fragments `all`, `step_prefix` and `step_join`, so they are composed here
    rather than asking an author to write "level {n} of {total}" and get the
    braces right. Reading them here is their R5 read site, and validating
    before `r_activity` composes the head row is what keeps one message per
    mistake: without it a missing `step_join` reaches the page as
    "level 36" and no gate says a word.
    """
    if not isinstance(pg, dict):
        raise ValueError(
            "zoom-bench %r declares no `progress`. Design draws a live readout "
            "in this block's head row, right-aligned and mono, and without it "
            "the row is the eyebrow and the heading with a hole in it."
            % act_id)
    for k in ("all", "step_prefix", "step_join"):
        if not pg.get(k):
            raise ValueError(
                "zoom-bench %r progress declares no %r. The readout is one "
                "count with a bespoke sentence at the top — 'level 3 of 6' "
                "then 'all six levels' — and each fragment is authored exactly "
                "once. A missing join reads 'level 36'." % (act_id, k))
    return pg
# ⚖️ THE FOUR NOTE BRANCHES, IN DESIGN'S EVALUATION ORDER. First match wins,
# and the ORDER IS THE MEANING (schema §5.2): `both_carriers` must be tested
# before `mixed` or Pp × Pp — Mendel's 3:1, the result the whole lesson is
# built on — falls through to the generic line. The predicates are implemented
# once here and once in `wirePeaCross`, keyed by these ids, which is why the id
# set is closed and ordered rather than free.
# MRB-257 / MRB-255 (5.38) — SIX BRANCHES, NOT FOUR, AND STILL ORDERED.
# `one_pure_dominant` covered THREE crosses and its sentence is true of only
# one: it ends "…and some of them are quietly carrying p, which will show up in
# the generation after." That is right for PP × Pp. With both parents PP no
# offspring can carry p at all; for PP × pp every single one does. A promise of
# hidden recessives that cannot exist is the misconception this lesson exists
# to remove, printed by the lesson. The two specific cases are tested BEFORE
# the general one, which keeps its name and narrows to PP × Pp.
_B10_PC_NOTES = ("both_pure_dominant", "pure_dominant_x_pure_recessive",
                 "one_pure_dominant", "both_pure_recessive", "both_carriers",
                 "mixed")
# ⚖️ THREE VERDICTS, AND FIVE CASES OPENED. The third verdict is the
# instrument (schema §6.1) and the letters A/B/C are derived from position, so
# the list is ordered and its length is fixed. Design's `isDone()` for
# `s-bench` is `openedCount >= 5` and the `s-test` band stop mirrors it.
_B10_SC_VERDICTS = 3
_B10_SC_THRESHOLD = 5
def _b10_pea_progress(pg, act_id):
    """b10-04's head readout, validated where it is composed.

    Design's line is three states, not two: `total === 0 ? 'no seeds grown' :
    total + ' seed' + (total === 1 ? '' : 's') + ' grown'`. So it is a count
    with a bespoke ZERO **and a singular/plural split** — the only readout in
    the key stage that needs the split, because one seed is a state a student
    reaches deliberately on this bench and "1 seeds grown" would undercut the
    sentence beside it.

    ⚠️ THE UNDERSCORED NAMES ARE THE SCHEMA'S AND ARE NOT NEGOTIABLE (§5). They
    are only legal because THIS function reads them — an instrument that
    consumes `progress` takes the key back from the shell, and the shell's
    `_progress_readout` would otherwise reject `suffix_one` as a
    `data-state-…` name. b10-02 ships `step_prefix`/`step_join` under exactly
    the same arrangement.
    """
    if not isinstance(pg, dict):
        raise ValueError(
            "pea-cross %r declares no `progress`. Design draws a live readout "
            "in this block's head row, right-aligned and mono." % act_id)
    for k in ("none", "suffix_one", "suffix_many"):
        if not pg.get(k):
            raise ValueError(
                "pea-cross %r progress declares no %r. The readout is three "
                "states — 'no seeds grown', '1 seed grown', '100 seeds grown' "
                "— and the singular is a state a student reaches on purpose "
                "here, so it is authored rather than derived."
                % (act_id, k))
    return pg
# ── b10-01 `#s-bench` · variation-plotter ────────────────────────────────

# ⚖️ THE TWO DATA TYPES, CLOSED. `data_type` is not a label: it decides the
# bar gap, the display-weight verdict line and whether the prediction was
# right, so a third spelling would silently make every one of those three
# wrong at once. Design's own `kind` field takes exactly these two values.
_B10_DATA_TYPES = ("continuous", "discontinuous")
# ⚖️ DESIGN'S OWN THRESHOLD, AND IT IS READ TWICE. `isDone()` on b10-01 is
# `n >= 3` for `s-bench` AND for `s-two` — the band stop mirrors the bench
# (MRB-249, schema §8) — so this number is not a tuning choice. Three of six
# is the point at which a student has met both data types and can have seen
# the gap change; the constant is here rather than inline so the renderer's
# refusal, the emitted attribute and the wire function cannot drift apart.
_B10_VP_THRESHOLD = 3
# Chassis, not content (schema §2): the rule and the bold lead-in are drawn on
# every one of the six panels and belong to the instrument. `cause` is the
# authored half.
_B10_VP_CAUSE_LEAD = "What causes it:"
def r_variation_plotter(a, act_id):
    """⊕ b10-01 `#s-bench` — predict the shape, then plot it.

    ⚖️ THE BAR GAP IS DERIVED FROM `data_type` AND IS NOT AUTHORED. Design
    computes `gap = kind === 'continuous' ? '0px' : '6px'` and gives every bar
    `width: calc(100% - gap)` inside an equal-width flex column, so a
    continuous characteristic's bars TOUCH and a discontinuous one's STAND
    APART. That is the histogram/bar-chart convention being taught by the
    rendering itself, and schema §2 is explicit that it must not be
    overridable: there is no `gap` key, no `spacing` key and no `chart_type`
    key, because an authored one would let a record ship touching bars for
    blood group. The rule lives in the stylesheet, keyed on
    `[data-vp-type]`, and a parity row reads the computed width of both.

    ⚖️ THE STUDENT CANNOT SEE THE GRAPH BEFORE COMMITTING TO A SHAPE. The plot
    button is `disabled` until a prediction exists for the CURRENT
    characteristic, which is Law 4 built into the instrument rather than
    layered over it. Once plotted, the predict buttons for that characteristic
    go away and the plot cannot be re-run — six characteristics, one
    prediction each, and there is NO RESET.

    ⚖️ SHAPE AND CAUSE ARE TWO QUESTIONS AND THE PANEL ASKS THEM SEPARATELY.
    `shape` answers "what shape is it"; `cause` answers "what caused it", under
    a rule and a bold lead-in. The split is the second half of the lesson's
    argument and the whole of `#s-think`: height is continuous AND strongly
    inherited, so the shape of the graph says nothing about the cause. A
    renderer that merged the two paragraphs would delete the lesson.

    ⚠️ EVERY CHARACTERISTIC'S GRAPH IS IN THE DOCUMENT, hidden, so the shipped
    bytes carry all six data sets and both verdict tags rather than being
    written in by the runtime. Nothing here assigns a science-bearing string
    to `textContent`.

    ⛔ AND THE VERDICT IS THE ONE THING IN THIS UNIT THAT JUDGES A PREDICTION
    (schema §0.6). It is a mono tag in accent-TEXT on the cream panel — the
    same tone whichever way it went — and it takes no green, no red and no
    badge. The prediction is a wrong IDEA being corrected, not a student being
    marked.
    """
    _b7_need(a, act_id, ("options_label", "characteristics", "predict_label",
                         "predict_options", "kind_lines", "run_label",
                         "run_done_label", "verdicts", "progress_suffix"))

    kind_lines = a["kind_lines"]
    for k in _B10_DATA_TYPES:
        if not kind_lines.get(k):
            raise ValueError(
                "variation-plotter %r kind_lines declares no %r. The display-"
                "weight line is what NAMES the shape the student has just "
                "looked at — 'Continuous — a histogram, bars touching' — and "
                "without it the verdict panel opens on the tag and then the "
                "prose, with the answer missing from between them."
                % (act_id, k))

    verdicts = a["verdicts"]
    for k in ("right", "wrong"):
        if not verdicts.get(k):
            raise ValueError(
                "variation-plotter %r verdicts declares no %r. Both tags are "
                "drawn in the same tone on the same panel (schema §0.6): the "
                "bench says whether the PREDICTION held, in words, and a "
                "missing branch is a graph that arrives with no answer to the "
                "question the student was made to commit to." % (act_id, k))

    # ⚠️ THE PREDICT OPTIONS ARE THE DATA TYPES, and their `id`s are compared
    # against `data_type` to decide the verdict. An option whose id is not one
    # of the two can never be right, on any characteristic, for ever — and the
    # page would look completely normal.
    popts = a["predict_options"]
    pids = [p.get("id") for p in popts]
    if sorted(pids) != sorted(_B10_DATA_TYPES):
        raise ValueError(
            "variation-plotter %r offers predictions %r. The two buttons ARE "
            "the two data types and their ids are compared against each "
            "characteristic's `data_type` — an id outside %r is a prediction "
            "that is wrong on all six characteristics and looks entirely "
            "normal on the page." % (act_id, pids, list(_B10_DATA_TYPES)))
    for p in popts:
        if not p.get("label"):
            raise ValueError(
                "variation-plotter %r predict option %r declares no `label`."
                % (act_id, p.get("id")))

    chars = a["characteristics"]
    # ⚖️ THE MIRROR STOP NEEDS THREE (MRB-249, schema §8). Design's `isDone()`
    # for BOTH `s-bench` and `s-two` is `n >= 3` plotted, so a bench with fewer
    # than three characteristics ships two rail stops that can never tick.
    if len(chars) < _B10_VP_THRESHOLD:
        raise ValueError(
            "variation-plotter %r declares %d characteristic(s). The bench's "
            "stage predicate is %d plotted and the `s-two` band stop MIRRORS "
            "it (MRB-249), so a shorter bench ships two rail stops that no "
            "student can ever tick." % (act_id, len(chars), _B10_VP_THRESHOLD))

    # ⚖️ AND BOTH TYPES HAVE TO BE ON THE BENCH. The argument is the CONTRAST —
    # touching bars against separated bars, and a smooth hump against four
    # columns with nothing between them. Six characteristics all of one type is
    # a bench that cannot make it, and the gap rule would draw one gap for ever
    # with nothing on screen to compare it to.
    seen, kinds = set(), set()
    for c in chars:
        for f in ("id", "label", "name", "data_type", "axis", "bins", "shape",
                  "cause"):
            if not c.get(f):
                raise ValueError(
                    "variation-plotter %r characteristic %r declares no %r. "
                    "`shape` and `cause` are the lesson's TWO QUESTIONS and "
                    "neither may be folded into the other; `axis` is the mono "
                    "caption that says in words why the bars touch or do not."
                    % (act_id, c.get("id"), f))
        if c["id"] in seen:
            raise ValueError("variation-plotter %r declares characteristic id "
                             "%r twice." % (act_id, c["id"]))
        seen.add(c["id"])
        if c["data_type"] not in _B10_DATA_TYPES:
            raise ValueError(
                "variation-plotter %r characteristic %r has data_type %r. It "
                "must be one of %r: the value decides the BAR GAP, the "
                "display-weight verdict line and whether the prediction was "
                "right, so an unknown spelling makes all three wrong at once "
                "and draws a plausible graph while doing it."
                % (act_id, c["id"], c["data_type"], list(_B10_DATA_TYPES)))
        kinds.add(c["data_type"])
        if len(c["bins"]) < 2:
            raise ValueError(
                "variation-plotter %r characteristic %r has %d bin(s). One bar "
                "cannot show a shape, and the gap rule needs two columns "
                "before there is a gap to see."
                % (act_id, c["id"], len(c["bins"])))
        for b in c["bins"]:
            if not b.get("label") or b.get("n") is None:
                raise ValueError(
                    "variation-plotter %r characteristic %r has a bin missing "
                    "`label` or `n`." % (act_id, c["id"]))
            if int(b["n"]) < 0:
                raise ValueError(
                    "variation-plotter %r characteristic %r bin %r counts %r "
                    "students." % (act_id, c["id"], b["label"], b["n"]))
        if max(int(b["n"]) for b in c["bins"]) <= 0:
            raise ValueError(
                "variation-plotter %r characteristic %r surveyed nobody — "
                "every bin is zero, so the tallest bar is the floor and the "
                "graph is a flat row of stubs." % (act_id, c["id"]))
    if kinds != set(_B10_DATA_TYPES):
        raise ValueError(
            "variation-plotter %r declares only %r data. The bench's whole "
            "argument is the CONTRAST between touching bars and separated "
            "ones, and a student who never sees the other kind has nothing to "
            "compare the gap to." % (act_id, sorted(kinds)))

    preds = "".join(
        '<li><button type="button" class="ks3-option ks3-vp-pred" '
        'data-vp-pred="%s" aria-pressed="false">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(p["id"]), t(p["label"])) for p in popts)

    tabs, panels = [], []
    for i, c in enumerate(chars):
        first = i == 0
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-vp-tab" '
            'data-vp-char="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(c["id"]), "true" if first else "false", t(c["label"])))

        # Bar height is `max(3, n / maxN * 100)`%, and `maxN` is PER
        # CHARACTERISTIC — each graph is scaled to its own tallest bin, so the
        # shape is readable whether the biggest bin holds 39 students or 2.
        # The floor of 3 keeps a one-student bin on screen rather than letting
        # it round away to a hairline the eye reads as an empty category.
        max_n = max(int(b["n"]) for b in c["bins"])
        cols = []
        for b in c["bins"]:
            h = max(3.0, (int(b["n"]) / float(max_n)) * 100.0)
            cols.append(
                '<span class="ks3-vp-col">'
                '<span class="ks3-vp-n">%s</span>'
                '<span class="ks3-vp-bar" data-fill style="height:%s%%">'
                '</span>'
                '<span class="ks3-vp-binlabel">%s</span></span>'
                % (t(str(int(b["n"]))), e(_pctnum(h)), t(b["label"])))

        # ⚠️ EACH CHARACTERISTIC CARRIES ITS OWN PREDICT GROUP, because the
        # prediction IS per characteristic — Design's `predicts` is a map keyed
        # by id, and the buttons disappear for a characteristic once it has
        # been plotted while staying live for the other five. One shared group
        # would need the runtime to remember six answers and repaint two
        # buttons from them; six groups make the DOM the state, which is what
        # every other tabbed bench in the key stage does.
        panels.append(
            '<div class="ks3-vp-charpanel" data-vp-charpanel="%s"%s>'
            '<p class="ks3-vp-name">%s</p>'
            '<div class="ks3-vp-predict" data-vp-predict>'
            '<p class="ks3-vp-predictlabel">%s</p>'
            '<ul class="ks3-options ks3-vp-preds" role="list">%s</ul></div>'
            '<div class="ks3-vp-graph" data-vp-graph hidden>'
            '<div class="ks3-vp-chart" data-vp-type="%s">%s</div>'
            '<p class="ks3-vp-axis">%s</p>'
            '<div class="ks3-vp-verdict">'
            '<p class="ks3-vp-tag" data-vp-tag="right" hidden>%s</p>'
            '<p class="ks3-vp-tag" data-vp-tag="wrong" hidden>%s</p>'
            '<p class="ks3-vp-kind">%s</p>'
            '<p class="ks3-vp-shape">%s</p>'
            '<p class="ks3-vp-cause"><strong>%s</strong> %s</p>'
            '</div></div></div>'
            % (e(c["id"]), "" if first else " hidden", t(c["name"]),
               t(a["predict_label"]), preds,
               e(c["data_type"]), "".join(cols), t(c["axis"]),
               t(verdicts["right"]), t(verdicts["wrong"]),
               t(kind_lines[c["data_type"]]), t(c["shape"]),
               _B10_VP_CAUSE_LEAD, t(c["cause"])))

    # ⚠️ THE PLOT BUTTON SHIPS `disabled`, because the resting page has no
    # prediction on it. That is Law 4 in the BYTES, before any JS runs.
    return ('<div class="ks3-vp" data-vp data-run-label="%s" '
            'data-run-done-label="%s" data-threshold="%d">'
            '<div class="ks3-vp-tabsgroup">'
            '<p class="ks3-vp-tabslabel" id="%s-chars">%s</p>'
            '<ul class="ks3-options ks3-vp-tabs" role="list" '
            'aria-labelledby="%s-chars">%s</ul></div>'
            '<div class="ks3-vp-panel">%s'
            '<div class="ks3-vp-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-vp-plot" '
            'data-vp-plot disabled>%s</button></div>'
            '</div></div>'
            % (e(_b8_plain(a["run_label"], act_id, "`run_label`")),
               e(_b8_plain(a["run_done_label"], act_id, "`run_done_label`")),
               _B10_VP_THRESHOLD,
               e(act_id), t(a["options_label"]), e(act_id), "".join(tabs),
               "".join(panels), t(a["run_label"])))
# ── b10-02 `#s-bench` · zoom-bench ───────────────────────────────────────

def r_zoom_bench(a, act_id):
    """⊕ b10-02 `#s-bench` — from a whole person to four letters.

    ⚖️ EVERY LEVEL IS DRAWN FROM THE START AND ONLY THE `body` ARRIVES. The
    `name` and the `scale` are on screen from the first paint at 45% opacity,
    so a student can see how far down there is to go — and, more importantly,
    can see the SCALE COLUMN as a column. That column is the argument of the
    lesson: it is the thing that makes six levels feel like one journey rather
    than six facts. Hiding the unreached rows would turn the bench into a
    reveal-list and delete it.

    ⚖️ AND NOTHING IS SWAPPED FOR ANYTHING ELSE ON THE WAY DOWN. Each level is
    INSIDE the one above it, which is why the rows are drawn as a single
    numbered ladder in document order rather than as tabs or cards: the
    ordering is the claim. `#s-think` on this page confronts exactly the
    belief that a gene is a separate object stuck to a chromosome.

    ⚠️ LEVEL 5 PRINTS NO NUMBER, AND THAT IS MEASURED (schema §3.1). A gene has
    no characteristic length, so Design writes `a section of the strand` where
    every other row has a figure. The renderer therefore checks that `scale` is
    PRESENT on all six and never that it looks like a measurement — a check for
    a digit here would fail the one row whose whole point is that there is no
    digit to give.

    ⚠️ THE SAY-IT-BACK PANEL IS PART OF THIS INSTRUMENT, not a second activity.
    Measured: it is inside `<section id="s-bench">`. It gates nothing and marks
    nothing — every answer is visible the moment its question is chosen, and
    the tabs record which question is being looked at, not whether anyone was
    right (MRB-196 R10).

    ⚖️ AND THE STAGE TICKS ON ALL SIX LEVELS, WHICH IS DESIGN'S OWN `isDone()`
    (`s.shown >= LEVELS.length`). The `s-model` band stop mirrors it (MRB-249),
    so the count is read by two rail entries and a bench of five levels would
    ship two stops that can never tick.
    """
    _b7_need(a, act_id, ("levels", "in_label", "in_done_label", "reset_label",
                         "close", "progress", "say_it_back"))
    _b10_zoom_progress(a.get("progress"), act_id)

    levels = a["levels"]
    if len(levels) != _B10_ZB_LEVELS:
        raise ValueError(
            "zoom-bench %r declares %d level(s). The bench is %d — person, "
            "cell, nucleus, chromosome, gene, bases — and BOTH the `s-bench` "
            "stop and the `s-model` band stop that mirrors it tick on all of "
            "them being open (MRB-249). Design's progress line reads 'all six "
            "levels' in words, so a seventh row or a missing one contradicts "
            "the counter above it as well as the rail beside it."
            % (act_id, len(levels), _B10_ZB_LEVELS))
    rows = []
    for i, L in enumerate(levels):
        for f in ("name", "scale", "body"):
            if not L.get(f):
                raise ValueError(
                    "zoom-bench %r level %d declares no %r. `scale` is the "
                    "COLUMN, and the column is the argument — a blank cell in "
                    "it is the one thing on this bench a student would read as "
                    "'nothing is known here'. Level 5 is the row with no "
                    "number, and Design fills it with words (`a section of the "
                    "strand`) rather than leaving it empty."
                    % (act_id, i + 1, f))
        first = i == 0
        rows.append(
            '<li class="ks3-zb-level" data-zb-level="%d"%s%s>'
            '<span class="ks3-zb-num" aria-hidden="true">%d</span>'
            '<span class="ks3-zb-cell">'
            '<span class="ks3-zb-head">'
            '<span class="ks3-zb-name">%s</span>'
            '<span class="ks3-zb-scale">%s</span></span>'
            '<span class="ks3-zb-body"%s>%s</span></span></li>'
            % (i, ' data-shown=""' if first else "",
               ' data-here=""' if first else "", i + 1,
               t(L["name"]), t(L["scale"]),
               "" if first else " hidden", t(L["body"])))

    say = a["say_it_back"]
    for f in ("options_label", "opens_on", "questions"):
        if not say.get(f):
            raise ValueError(
                "zoom-bench %r say_it_back declares no %r." % (act_id, f))
    qs = say["questions"]
    if len(qs) != _B10_ZB_QUESTIONS:
        raise ValueError(
            "zoom-bench %r say_it_back asks %d question(s), and Design draws "
            "%d — longest, contains, howmany, same. They are one row of tabs "
            "on one panel; a fifth wraps the row and a third leaves the panel "
            "looking like it lost one."
            % (act_id, len(qs), _B10_ZB_QUESTIONS))
    # ⚠️ `opens_on` IS AUTHORED BECAUSE IT IS NOT THE FIRST QUESTION (schema
    # §0.3 and §3.2). `state.quiz` opens on `contains` — *"What contains
    # what?"* — which is `questions[1]`, and it opens there because that one
    # question states the whole nesting the bench has just walked down. That is
    # a teaching choice, so it gets a key; an opening selection that IS the
    # first entry gets none and the renderer defaults to index 0.
    ids = [q.get("id") for q in qs]
    if say["opens_on"] not in ids:
        raise ValueError(
            "zoom-bench %r opens the say-it-back panel on %r, and the "
            "questions are %r. `opens_on` is authored ONLY because the opening "
            "question is not the first one (schema §3.2) — pointed at nothing, "
            "it silently falls back to the first, and the panel opens on a "
            "question chosen by list order rather than by teaching."
            % (act_id, say["opens_on"], ids))
    if len(set(ids)) != len(ids):
        raise ValueError("zoom-bench %r say_it_back declares a duplicate "
                         "question id: %r." % (act_id, ids))
    tabs, answers = [], []
    for q in qs:
        for f in ("id", "label", "answer"):
            if not q.get(f):
                raise ValueError(
                    "zoom-bench %r say_it_back question %r declares no %r. The "
                    "answer is ALWAYS VISIBLE for the selected question — this "
                    "panel gates nothing and marks nothing — so a missing one "
                    "is a tab that empties the panel."
                    % (act_id, q.get("id"), f))
        on = q["id"] == say["opens_on"]
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-zb-qtab" '
            'data-zb-q="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(q["id"]), "true" if on else "false", t(q["label"])))
        answers.append(
            '<p class="ks3-zb-answer" data-zb-answer="%s"%s>%s</p>'
            % (e(q["id"]), "" if on else " hidden", t(q["answer"])))

    return ('<div class="ks3-zb" data-zb data-in-label="%s" '
            'data-in-done-label="%s" data-total="%d">'
            '<div class="ks3-zb-panel">'
            '<ol class="ks3-zb-levels" role="list">%s</ol>'
            '<div class="ks3-zb-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-zb-in" '
            'data-zb-in>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-zb-out" '
            'data-zb-out>%s</button></div>'
            '<p class="ks3-zb-close" data-zb-close hidden>%s</p></div>'
            '<div class="ks3-zb-say">'
            '<p class="ks3-zb-saylabel" id="%s-say">%s</p>'
            '<ul class="ks3-options ks3-zb-qtabs" role="list" '
            'aria-labelledby="%s-say">%s</ul>%s</div></div>'
            % (e(_b8_plain(a["in_label"], act_id, "`in_label`")),
               e(_b8_plain(a["in_done_label"], act_id, "`in_done_label`")),
               len(levels), "".join(rows), t(a["in_label"]),
               t(a["reset_label"]), t(a["close"]),
               e(act_id), t(say["options_label"]), e(act_id),
               "".join(tabs), "".join(answers)))
# ── b10-03 `#s-bench` · model-builder ────────────────────────────────────

# ⛔ CHASSIS, NOT CONTENT, AND DELIBERATELY NOT AUTHORED. Design's two card
# verdicts are fixed strings on her own page and schema §4 gives them no key.
# They are the instrument saying what it just did to the MODEL — `consistent`
# or `rules this model out` — and both are drawn in the same place, in the same
# type, on every card. Making them authorable would let one lesson's four cards
# disagree with each other about what a verdict is called, and would put the
# wording of a judgement into a payload that has no other judgement in it.
_B10_MB_PASS_LABEL = "consistent"
_B10_MB_FAIL_LABEL = "rules this model out"
def _b10_mb_pass(model, ev):
    """One evidence card against one model. The rule, in one place.

    ⚖️ A CARD PASSES WHEN EVERY `requires` PAIR MATCHES **AND** THE `forbids`
    MAP IS NOT MATCHED IN FULL. Three of Design's four tests are a single
    equality; the fourth — Pauling's triple helix — is a NEGATED CONJUNCTION,
    `!(strands === '3' && bases === 'out')`, which is why `forbids` is a map
    and not a list. Read it as an OR of the required pairs and it fires on
    three strands alone, which would rule out row 9 as well and break the
    "exactly one of twelve" claim the lesson rests on.

    Written once and used by the static render, by the renderer's own
    twelve-row proof, and — reimplemented in three lines — by `wireModelBuilder`.
    """
    for k, v in (ev.get("requires") or {}).items():
        if model.get(k) != v:
            return False
    forbids = ev.get("forbids") or {}
    if forbids and all(model.get(k) == v for k, v in forbids.items()):
        return False
    return True
def r_model_builder(a, act_id):
    """⊕ b10-03 `#s-bench` — twelve models, four tests, and exactly one survivor.

    ⚖️⚖️ THE BENCH OPENS ON PAULING'S WRONG MODEL AND THAT IS THE WHOLE DESIGN.
    `start` is three strands, bases out, any base with any base — row 12 of the
    twelve, and the UNIQUE combination that fails all four tests. So the
    student opens with four red cards, the most emphatic opening available, and
    every dial they touch can only improve it. Elimination as a method,
    presented as a monotone descent. The renderer PROVES this rather than
    trusting the preset: it works all twelve combinations and refuses a payload
    whose `start` is not the unique 0/4 and whose `correct` is not the unique
    4/4.

    ⚖️ AND `pauling` IS NOT AN INDEPENDENT CONSTRAINT — it fails only rows 11
    and 12, both of which already fail `photo` and `water`. There is no model
    anywhere in the twelve that passes the other three and fails it. Its job is
    not to eliminate: it is to make the opening state cost FOUR failures rather
    than three, and to teach that a wrong model published by the most respected
    chemist alive was itself useful evidence. Schema §4.2 says in words: do not
    tidy it as redundant. Removing it would leave the opening at 3/4 and delete
    the lesson's only worked example of a rival being ruled out.

    ⛔ THERE IS NO RUN BUTTON AND NO RESET BUTTON (schema §4.3). The four cards
    re-evaluate live on every dial press, and the header counter is the only
    running feedback. B7's `reactant-remover` and `method-breaker` both had a
    run control and copying that across would add something Design did not
    draw — so `run_label` and `reset_label` are not read here and must not be
    authored.

    ⛔ AND THE VERDICT IS ON THE MODEL, NEVER ON THE STUDENT (schema §0.6). A
    failing card prints `rules this model out` in alert and unhides the line
    that says WHAT it rules out; a passing one prints `consistent` in green.
    That is one of the three B10 benches that adjudicate a commitment, and it
    is shipped as Design drew it. The DIAL BUTTONS take no mark at any point —
    a pressed dial is the alert ground, meaning "this is the model on the
    bench", and never a verdict. Only the mastery ladder marks correctness.

    ⚠️ `solved` IS STICKY, by Design's own construction (`solved: st.solved ||
    ok`). A student who reaches the double helix and then goes back to break
    the model on purpose keeps the stop — and the `s-who` band stop mirrors it
    (MRB-249), so an unticking predicate would move two.
    """
    _b7_need(a, act_id, ("dials", "start", "correct", "evidence",
                         "verdict_tags", "verdicts", "progress_suffix"))
    for f in ("run_label", "reset_label"):
        if a.get(f):
            raise ValueError(
                "model-builder %r authors %r. There is no run control and no "
                "reset control on this bench (schema §4.3): the four evidence "
                "cards re-evaluate live on every dial press, and the header "
                "counter is the only running feedback. B7's benches had one, "
                "and copying that across adds a control Design did not draw."
                % (act_id, f))

    dials = a["dials"]
    if len(dials) < 2:
        raise ValueError(
            "model-builder %r declares %d dial(s). The bench is a COMBINATION "
            "of decisions and one decision has no combinations."
            % (act_id, len(dials)))
    dial_ids, choices = [], {}
    for d in dials:
        for f in ("id", "name", "options"):
            if not d.get(f):
                raise ValueError("model-builder %r dial %r declares no %r."
                                 % (act_id, d.get("id"), f))
        if d["id"] in choices:
            raise ValueError("model-builder %r declares dial id %r twice."
                             % (act_id, d["id"]))
        if len(d["options"]) < 2:
            raise ValueError(
                "model-builder %r dial %r offers %d option(s). A dial with one "
                "setting is a label." % (act_id, d["id"], len(d["options"])))
        for o in d["options"]:
            for f in ("id", "label", "phrase"):
                if not o.get(f):
                    raise ValueError(
                        "model-builder %r dial %r option %r declares no %r. "
                        "`label` is the BUTTON text and `phrase` is the same "
                        "option's sentence fragment for the model line above "
                        "the cards — 'Two' against 'Two strands', 'Inside, "
                        "facing each other' against 'bases on the inside'. The "
                        "two genuinely differ, so both are content and neither "
                        "can be derived from the other."
                        % (act_id, d["id"], o.get("id"), f))
        dial_ids.append(d["id"])
        choices[d["id"]] = [o["id"] for o in d["options"]]

    for which in ("start", "correct"):
        m = a[which]
        if sorted(m) != sorted(dial_ids):
            raise ValueError(
                "model-builder %r `%s` sets %r and the dials are %r. Every "
                "dial takes a position or the bench opens with a control at no "
                "setting at all." % (act_id, which, sorted(m), sorted(dial_ids)))
        for k, v in m.items():
            if v not in choices[k]:
                raise ValueError(
                    "model-builder %r `%s` sets dial %r to %r, which it does "
                    "not offer (%r)." % (act_id, which, k, v, choices[k]))

    evidence = a["evidence"]
    if len(evidence) < 2:
        raise ValueError(
            "model-builder %r declares %d test(s). One test is not evidence, "
            "it is an answer key." % (act_id, len(evidence)))
    seen = set()
    for ev in evidence:
        for f in ("id", "name", "what", "why"):
            if not ev.get(f):
                raise ValueError(
                    "model-builder %r evidence %r declares no %r. `why` is the "
                    "ELIMINATION TEXT — the line that names what this evidence "
                    "rules out — and it is the only thing on the bench that "
                    "tells a student which decision to change."
                    % (act_id, ev.get("id"), f))
        if ev["id"] in seen:
            raise ValueError("model-builder %r declares evidence id %r twice."
                             % (act_id, ev["id"]))
        seen.add(ev["id"])
        if not (ev.get("requires") or ev.get("forbids")):
            raise ValueError(
                "model-builder %r evidence %r constrains nothing. A card with "
                "neither `requires` nor `forbids` passes every model in the "
                "matrix, which makes it a card that is always green and never "
                "teaches anything." % (act_id, ev["id"]))
        # ⚖️ A `forbids` MAP IS A NEGATED CONJUNCTION AND MUST NAME AT LEAST
        # TWO DIALS. Design's only one is Pauling's — `!(strands === '3' &&
        # bases === 'out')` — and the AND is the whole of it: his model was
        # ruled out by the COMBINATION, not by three strands, and not by the
        # bases facing out. A one-pair `forbids` is a single equality written
        # in the negative, and it quietly turns this card into an independent
        # constraint that eliminates models the historical evidence did not
        # eliminate. Schema §4.2 measured that it fails rows 11 and 12 only;
        # with one pair it would fail 9 and 10 as well, the twelve-row proof
        # below would still pass, and nothing on the page would look wrong.
        # Found by mutation: this is the one renderer check the matrix cannot
        # make for itself.
        if ev.get("forbids") is not None and len(ev["forbids"]) < 2:
            raise ValueError(
                "model-builder %r evidence %r forbids %r — one pair. `forbids` "
                "is a NEGATED CONJUNCTION and the AND is the science: a rival "
                "model is ruled out by a COMBINATION of decisions, not by one "
                "of them. Written with a single pair it becomes an independent "
                "constraint that rules out models the evidence does not, and "
                "the twelve-row proof below cannot see the difference."
                % (act_id, ev["id"], ev["forbids"]))
        for which in ("requires", "forbids"):
            for k, v in (ev.get(which) or {}).items():
                if k not in choices:
                    raise ValueError(
                        "model-builder %r evidence %r %s names dial %r, which "
                        "the bench does not have." % (act_id, ev["id"], which, k))
                if v not in choices[k]:
                    raise ValueError(
                        "model-builder %r evidence %r %s wants dial %r at %r, "
                        "which it does not offer (%r)."
                        % (act_id, ev["id"], which, k, v, choices[k]))

    # ⚖️⚖️ THE TWELVE ROWS, WORKED. Schema §4.2 states the claim the whole
    # lesson rests on — "exactly one combination survives all four" — and this
    # is where it stops being an assertion in a document. Every combination of
    # every dial is built and scored; the payload is refused unless `correct`
    # is the UNIQUE model that passes everything and `start` is the UNIQUE
    # model that passes nothing. A retuned `requires` that quietly admitted a
    # second 4/4 would leave the bench looking entirely normal while the
    # sentence above it, the verdict below it and rung 2 all became false.
    combos = [{}]
    for did in dial_ids:
        combos = [dict(c, **{did: o}) for c in combos for o in choices[did]]
    all_pass = [c for c in combos if all(_b10_mb_pass(c, ev) for ev in evidence)]
    none_pass = [c for c in combos if not any(_b10_mb_pass(c, ev)
                                              for ev in evidence)]
    if len(all_pass) != 1 or all_pass[0] != a["correct"]:
        raise ValueError(
            "model-builder %r: of %d combinations, %d pass every test (%r), "
            "and `correct` is %r. The lesson's claim — and the sentence above "
            "the bench, and the closing verdict, and rung 2 — is that EXACTLY "
            "ONE model survives all the evidence. A second survivor makes the "
            "bench a lie that nothing else in the build can see."
            % (act_id, len(combos), len(all_pass), all_pass, a["correct"]))
    if len(none_pass) != 1 or none_pass[0] != a["start"]:
        raise ValueError(
            "model-builder %r: %d combination(s) fail every test (%r), and the "
            "bench opens on %r. The opening state is not an accident of the "
            "preset — it IS the preset (schema §4.2): the unique 0-of-%d row, "
            "so a student opens with every card red and every dial they touch "
            "can only improve it. Elimination as a monotone descent."
            % (act_id, len(none_pass), none_pass, a["start"], len(evidence)))

    tags = a["verdict_tags"]
    for f in ("pass", "fail_one", "fail_many"):
        if not tags.get(f):
            raise ValueError(
                "model-builder %r verdict_tags declares no %r. Design writes "
                "the count in words on both sides of one — '1 test still "
                "failing' against '3 tests still failing' — and a missing "
                "branch is a heading that vanishes at exactly one count."
                % (act_id, f))
    for f in ("fail_one", "fail_many"):
        if "{n}" not in tags[f]:
            raise ValueError(
                "model-builder %r verdict_tags %r names no {n}. The number of "
                "failing tests is computed from the model on the bench and "
                "cannot be authored as a literal — a tag that quotes a fixed "
                "figure is wrong on every setting but one."
                % (act_id, f))
    if "{n}" in tags["pass"]:
        raise ValueError(
            "model-builder %r verdict_tags `pass` names {n}, and nothing fills "
            "it there. This is the branch where the count is ZERO and the "
            "sentence says so in words instead." % (act_id, tags["pass"]))
    verdicts = a["verdicts"]
    for f in ("pass", "fail"):
        if not verdicts.get(f):
            raise ValueError(
                "model-builder %r verdicts declares no %r." % (act_id, f))

    groups = []
    for d in dials:
        opts = "".join(
            '<li><button type="button" class="ks3-option ks3-dh-opt" '
            'data-dh-dial="%s" data-dh-opt="%s" data-dh-phrase="%s" '
            'aria-pressed="%s"><span class="ks3-opt-label">%s</span>'
            '</button></li>'
            % (e(d["id"]), e(o["id"]),
               e(_b8_plain(o["phrase"], act_id, "option `phrase`")),
               "true" if a["start"][d["id"]] == o["id"] else "false",
               t(o["label"])) for o in d["options"])
        groups.append(
            '<div class="ks3-dh-dial">'
            '<p class="ks3-dh-dialname" id="%s-%s">%s</p>'
            '<ul class="ks3-options ks3-dh-opts" role="list" '
            'aria-labelledby="%s-%s">%s</ul></div>'
            % (e(act_id), e(d["id"]), t(d["name"]),
               e(act_id), e(d["id"]), opts))

    cards, passes = [], 0
    for ev in evidence:
        ok = _b10_mb_pass(a["start"], ev)
        if ok:
            passes += 1
        cards.append(
            '<li class="ks3-dh-card" data-dh-card="%s" data-dh-requires="%s" '
            'data-dh-forbids="%s"%s>'
            '<div class="ks3-dh-cardhead">'
            '<p class="ks3-dh-cardname">%s</p>'
            '<p class="ks3-dh-tag" data-dh-tag="pass"%s>%s</p>'
            '<p class="ks3-dh-tag" data-dh-tag="fail"%s>%s</p></div>'
            '<p class="ks3-dh-what">%s</p>'
            '<p class="ks3-dh-why"%s>%s</p></li>'
            % (e(ev["id"]),
               e(json.dumps(ev.get("requires") or {}, separators=(",", ":"),
                            sort_keys=True)),
               e(json.dumps(ev.get("forbids") or {}, separators=(",", ":"),
                            sort_keys=True)),
               ' data-pass=""' if ok else "",
               t(ev["name"]),
               "" if ok else " hidden", _B10_MB_PASS_LABEL,
               " hidden" if ok else "", _B10_MB_FAIL_LABEL,
               t(ev["what"]), " hidden" if ok else "", t(ev["why"])))

    n_fail = len(evidence) - passes
    return ('<div class="ks3-dh" data-dh data-tag-pass="%s" '
            'data-tag-fail-one="%s" data-tag-fail-many="%s" '
            'data-verdict-pass="%s" data-verdict-fail="%s" '
            'data-target="%s" data-total="%d">'
            '<div class="ks3-dh-dials">%s</div>'
            '<div class="ks3-dh-panel">'
            '<p class="ks3-dh-modelline" data-dh-modelline>%s</p>'
            '<ul class="ks3-dh-cards" role="list">%s</ul>'
            '<div class="ks3-dh-verdict">'
            '<p class="ks3-dh-verdicttag" data-dh-verdicttag>%s</p>'
            '<p class="ks3-dh-verdictbody" data-dh-verdictbody>%s</p>'
            '</div></div></div>'
            % (e(_b8_plain(tags["pass"], act_id, "verdict_tags `pass`")),
               e(_b8_plain(tags["fail_one"], act_id, "verdict_tags `fail_one`")),
               e(_b8_plain(tags["fail_many"], act_id,
                           "verdict_tags `fail_many`")),
               e(_b8_plain(verdicts["pass"], act_id, "verdicts `pass`")),
               e(_b8_plain(verdicts["fail"], act_id, "verdicts `fail`")),
               e(json.dumps(a["correct"], separators=(",", ":"),
                            sort_keys=True)),
               len(evidence), "".join(groups),
               t(_b10_mb_modelline(a, a["start"])),
               "".join(cards),
               t(_b10_mb_tag(tags, n_fail)),
               t(verdicts["pass"] if n_fail == 0 else verdicts["fail"])))
def _b10_mb_modelline(a, model):
    """`", ".join(phrase)`, in DIAL ORDER — Design's own composition.

    The order is the order the decisions are drawn in, which is the order the
    sentence has to read in: *"Three strands, bases on the outside, any base
    with any base."* Built once here for the shipped bytes and once in
    `wireModelBuilder`, from the same `data-dh-phrase` attributes.
    """
    out = []
    for d in a["dials"]:
        for o in d["options"]:
            if o["id"] == model[d["id"]]:
                out.append(o["phrase"])
    return ", ".join(out)
def _b10_mb_tag(tags, n_fail):
    if n_fail == 0:
        return tags["pass"]
    key = "fail_one" if n_fail == 1 else "fail_many"
    return tags[key].replace("{n}", str(n_fail))
# ── b10-04 `#s-bench` · pea-cross ────────────────────────────────────────

def r_pea_cross(a, act_id):
    """⊕ b10-04 `#s-bench` — two parents, one gene, and real chance.

    ⚖️⚖️ THE RANDOMNESS IS REAL AND UNSEEDED AND MUST STAY THAT WAY (schema
    §5.1). One `Math.random()` per gamete, per parent, per seed; no PRNG, no
    seed, and NO `seed` KEY — grepped across all five B10 pages, this is the
    unit's only call. A seeded bench would deliver 75/25 on cue, which teaches
    exactly the belief the page's legal line and rung 4 are written to break: a
    3:1 ratio is a SAMPLING result, not a property of any one litter. The
    hundred-seed button exists because one seed is not enough, and that only
    lands if one seed is genuinely unpredictable. The renderer therefore
    refuses a `seed` key rather than leaving the door open.

    ⚖️ THE FOUR NOTES ARE ORDERED AND THE ORDER IS THE MEANING (schema §5.2).
    Design evaluates them as an if/else chain and the first match wins:
    `one_pure_dominant` → `both_pure_recessive` → `both_carriers` → `mixed`.
    Moving `both_carriers` below `mixed` would let `Pp × Pp` — Mendel's 3:1,
    the whole point of the lesson — fall through to the generic line. The four
    ids are a CLOSED, ORDERED set here for that reason, and `wirePeaCross`
    branches on them in the same order.

    ⚠️ CHANGING EITHER PARENT CLEARS THE TALLY AND THE LAST SEED. Measured on
    Design's own handler. Load-bearing rather than tidy: without it a student
    accumulates counts across two DIFFERENT crosses and reads a ratio that
    describes neither of them. Wire the clear or the instrument silently lies.

    ⚠️ AND GROWING A HUNDRED HIDES THE MOST-RECENT-SEED CARD (`last: n === 1 ?
    last : null`). The single seed is the "chance decides each one" story; the
    hundred is the "only totals show the pattern" story. Design never puts them
    on screen together and neither does this.

    ⚖️ THE GENOTYPE ON THE LAST-SEED CARD IS NORMALISED DOMINANT-FIRST. A seed
    that received `p` then `P` prints `Pp`, never `pP` — measured. Without it
    the same genotype appears under two spellings on the same bench and a
    student reasonably concludes they are different things.

    ⛔ AND *DOMINANT* AND *RECESSIVE* ARE NEVER NAMED (NOTES flag 13, ruled and
    confirmed in schema §16). The page says "overrides" and "hidden"; the
    LETTERS carry the idea. There is no `dominant_term` key and there must not
    be one — `phenotypes` maps the two outcomes to their colour words and that
    is as far as the vocabulary goes. The keys `dominant`/`recessive` are
    internal ids and reach no student.
    """
    _b7_need(a, act_id, ("genotypes", "parents", "start", "phenotypes",
                         "one_label", "many_label", "reset_label",
                         "cross_join", "last_label", "last_template",
                         "tally_rows", "ratio_template",
                         "no_recessive_template", "notes", "progress"))
    if a.get("many_n") is None:
        raise ValueError("pea-cross %r declares no `many_n`." % act_id)
    if a.get("seed") is not None:
        raise ValueError(
            "pea-cross %r authors a `seed`. THE RANDOMNESS ON THIS BENCH IS "
            "REAL AND UNSEEDED AND STAYS THAT WAY (schema §5.1). A 3:1 ratio "
            "is a sampling result, not a property of one litter — a seeded "
            "bench hands the student 75/25 on cue and teaches precisely the "
            "misconception the legal line and rung 4 exist to break. No "
            "student sees the same cross twice." % act_id)
    _b10_pea_progress(a.get("progress"), act_id)

    many_n = int(a["many_n"])
    if many_n < 20:
        raise ValueError(
            "pea-cross %r grows %d seeds on the big button. It is there "
            "BECAUSE one seed is not enough to show a proportion, and a "
            "handful is not either — a run that small would show noise and "
            "teach that the prediction fails." % (act_id, many_n))

    pheno = a["phenotypes"]
    for f in ("dominant", "recessive"):
        if not pheno.get(f):
            raise ValueError(
                "pea-cross %r phenotypes declares no %r. These are the COLOUR "
                "WORDS — purple and white — and they are as far as this "
                "lesson's vocabulary goes: `dominant` and `recessive` are "
                "internal ids and are never printed (NOTES flag 13)."
                % (act_id, f))

    # ⚖️ THE ALLELE ALPHABET IS DERIVED FROM THE GENOTYPES AND CHECKED, because
    # every downstream claim rests on it: which letter overrides which, which
    # combination is white, and whether `pp` can ever be reached at all.
    genos, alleles = {}, set()
    for g in a["genotypes"]:
        for f in ("id", "label", "alleles"):
            if not g.get(f):
                raise ValueError("pea-cross %r genotype %r declares no %r."
                                 % (act_id, g.get("id"), f))
        if len(g["alleles"]) != 2:
            raise ValueError(
                "pea-cross %r genotype %r carries %d allele(s). Every parent "
                "carries TWO copies of the gene and passes ONE — that is the "
                "whole mechanism the bench models."
                % (act_id, g["id"], len(g["alleles"])))
        genos[g["id"]] = g["alleles"]
        alleles.update(g["alleles"])
    if len(alleles) != 2:
        raise ValueError(
            "pea-cross %r uses %d allele letter(s) (%r). The bench is ONE gene "
            "with two versions: one that overrides and one that is hidden."
            % (act_id, len(alleles), sorted(alleles)))
    # ⚖️ THE DOMINANT LETTER IS THE CAPITAL ONE, DERIVED AND NEVER AUTHORED.
    # An authored letter could disagree with the genotype list, and the bench
    # would then print one thing and compute another — white seeds tallied
    # under the purple bar, with every string on screen still correct.
    # `sorted()` is ASCII, where every capital sorts before every lower-case
    # letter, so the capital is always first. The convention it depends on —
    # capital for the version that overrides, lower case for the one that is
    # hidden — is the one the page teaches in its own opening sentence, and
    # the check below refuses a genotype set that does not follow it.
    dom, rec = sorted(alleles)
    if not (dom.isupper() and rec.islower() and dom.lower() == rec):
        raise ValueError(
            "pea-cross %r uses the letters %r and %r. The bench derives which "
            "version overrides from the CASE of the letter, because that is "
            "the convention the page's own opening sentence teaches — P gives "
            "purple and beats p. Two letters that are not the same letter in "
            "two cases leave the instrument guessing which bar a seed belongs "
            "in." % (act_id, dom, rec))
    if not any(sorted(v) == sorted([rec, rec]) for v in genos.values()):
        raise ValueError(
            "pea-cross %r offers no genotype carrying two %r. The hidden "
            "version can only show when there is nothing left to override it, "
            "so without that genotype the recessive phenotype is unreachable "
            "and the white bar is decoration." % (act_id, rec))

    parents = a["parents"]
    if len(parents) != 2:
        raise ValueError(
            "pea-cross %r declares %d parent(s). A cross is two."
            % (act_id, len(parents)))
    for p in parents:
        for f in ("id", "name"):
            if not p.get(f):
                raise ValueError("pea-cross %r parent %r declares no %r."
                                 % (act_id, p.get("id"), f))
        if a["start"].get(p["id"]) not in genos:
            raise ValueError(
                "pea-cross %r opens parent %r on %r, which is not one of %r. "
                "`start` is authored (schema §0.3) BECAUSE the bench opens on "
                "the second genotype, not the first: the only cross that "
                "produces the 3:1, so the headline result is one press away "
                "and the student has to change something to find the others."
                % (act_id, p["id"], a["start"].get(p["id"]), sorted(genos)))

    rows = a["tally_rows"]
    row_ids = [r.get("id") for r in rows]
    if sorted(row_ids) != ["dominant", "recessive"]:
        raise ValueError(
            "pea-cross %r tallies %r. There are exactly two outcomes on this "
            "bench and their ids are the phenotype ids, because the bar the "
            "runtime fills is found by that id." % (act_id, row_ids))
    for r in rows:
        if not r.get("name"):
            raise ValueError("pea-cross %r tally row %r declares no `name`."
                             % (act_id, r.get("id")))

    _b9_placeholders(a["ratio_template"], act_id, "`ratio_template`",
                     ("{ratio}",))
    _b9_placeholders(a["no_recessive_template"], act_id,
                     "`no_recessive_template`", ("{total}",), ("{ratio}",))
    # MRB-257 (5.45 / 5.44) — the other three count lines. `no_dominant_*` is
    # the branch that was missing entirely, so `pp × pp` printed a ratio with
    # zero underneath it; the `_one` pair are the singulars a sample of one
    # reaches, and a sample of one ALWAYS has one of the two counts at zero.
    for key in ("no_recessive_template_one", "no_dominant_template",
                "no_dominant_template_one"):
        if not a.get(key):
            raise ValueError(
                "pea-cross %r is missing `%s`. Growing a single seed puts one "
                "of the two counts at zero every time, so all four of these "
                "lines are states the bench reaches on its first press."
                % (act_id, key))
        _b9_placeholders(a[key], act_id, "`%s`" % key, ("{total}",),
                         ("{ratio}",))
    _b9_placeholders(a["last_template"], act_id, "`last_template`",
                     ("{g1}", "{g2}", "{genotype}", "{phenotype}"))

    notes = a["notes"]
    if list(notes) and set(notes) != set(_B10_PC_NOTES):
        raise ValueError(
            "pea-cross %r declares notes %r; the bench branches on %r. The "
            "FOUR ARE ORDERED and the order is the meaning (schema §5.2): "
            "first match wins, and `both_carriers` must be tested before "
            "`mixed` or Pp × Pp — Mendel's 3:1, the whole point of the lesson "
            "— falls through to the generic line."
            % (act_id, sorted(notes), list(_B10_PC_NOTES)))
    for k in _B10_PC_NOTES:
        if not notes.get(k):
            raise ValueError(
                "pea-cross %r notes declares no %r. Every combination of "
                "parents a student can set reaches one of the four, so a "
                "missing branch is a panel that empties on exactly the crosses "
                "it does not cover." % (act_id, k))

    groups = []
    for p in parents:
        opts = "".join(
            '<li><button type="button" class="ks3-option ks3-pc-geno" '
            'data-pc-parent="%s" data-pc-geno="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(p["id"]), e(g["id"]),
               "true" if a["start"][p["id"]] == g["id"] else "false",
               t(g["label"])) for g in a["genotypes"])
        groups.append(
            '<div class="ks3-pc-parent">'
            '<p class="ks3-pc-parentname" id="%s-%s">%s</p>'
            '<ul class="ks3-options ks3-pc-genos" role="list" '
            'aria-labelledby="%s-%s">%s</ul></div>'
            % (e(act_id), e(p["id"]), t(p["name"]),
               e(act_id), e(p["id"]), opts))

    bars = "".join(
        '<li class="ks3-pc-row" data-pc-row="%s">'
        '<div class="ks3-pc-rowhead">'
        '<p class="ks3-pc-rowname">%s</p>'
        '<p class="ks3-pc-rowvalue" data-pc-value>0</p></div>'
        '<span class="ks3-pc-track">'
        '<span class="ks3-pc-bar" data-fill data-pc-bar style="width:0%%">'
        '</span></span></li>'
        % (e(r["id"]), t(r["name"])) for r in rows)

    # ⚠️ THE NOTES ARE ALL IN THE DOCUMENT, one per branch, and the runtime
    # shows one. Nothing science-bearing is assigned to `textContent`, and a
    # reader with JS off gets the opening cross's note rather than a blank.
    opening_note = _b10_pc_note(a["start"][parents[0]["id"]],
                                a["start"][parents[1]["id"]], genos, dom, rec)
    note_els = "".join(
        '<p class="ks3-pc-note" data-pc-note="%s"%s>%s</p>'
        % (e(k), "" if k == opening_note else " hidden", t(notes[k]))
        for k in _B10_PC_NOTES)

    pg = a["progress"]
    return ('<div class="ks3-pc" data-pc data-many-n="%d" data-dominant="%s" '
            'data-recessive="%s" data-genotypes="%s" data-cross-join="%s" '
            'data-last-template="%s" data-pheno-dominant="%s" '
            'data-pheno-recessive="%s" data-ratio-template="%s" '
            'data-no-recessive-template="%s" '
            'data-no-recessive-template-one="%s" '
            'data-no-dominant-template="%s" '
            'data-no-dominant-template-one="%s" data-suffix-one="%s" '
            'data-suffix-many="%s">'
            '<div class="ks3-pc-parents">%s</div>'
            '<div class="ks3-pc-panel">'
            '<p class="ks3-pc-crossline" data-pc-crossline>%s</p>'
            '<div class="ks3-pc-last" data-pc-last hidden>'
            '<p class="ks3-pc-lastlabel">%s</p>'
            '<p class="ks3-pc-lastline" data-pc-lastline></p></div>'
            '<div class="ks3-pc-tally" data-pc-tally hidden>'
            '<ul class="ks3-pc-rows" role="list">%s</ul>'
            '<p class="ks3-pc-ratio" data-pc-ratio></p></div>'
            '%s'
            '<div class="ks3-pc-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-pc-one" '
            'data-pc-one>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-pc-many" '
            'data-pc-many>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-pc-clear" '
            'data-pc-clear>%s</button></div>'
            '</div></div>'
            % (many_n, e(dom), e(rec),
               e(json.dumps(genos, separators=(",", ":"), sort_keys=True)),
               e(_b8_plain(a["cross_join"], act_id, "`cross_join`")),
               e(_b8_plain(a["last_template"], act_id, "`last_template`")),
               e(_b8_plain(pheno["dominant"], act_id, "phenotypes `dominant`")),
               e(_b8_plain(pheno["recessive"], act_id,
                           "phenotypes `recessive`")),
               e(_b8_plain(a["ratio_template"], act_id, "`ratio_template`")),
               e(_b8_plain(a["no_recessive_template"], act_id,
                           "`no_recessive_template`")),
               e(_b8_plain(a["no_recessive_template_one"], act_id,
                           "`no_recessive_template_one`")),
               e(_b8_plain(a["no_dominant_template"], act_id,
                           "`no_dominant_template`")),
               e(_b8_plain(a["no_dominant_template_one"], act_id,
                           "`no_dominant_template_one`")),
               e(_b8_plain(pg["suffix_one"], act_id, "progress `suffix_one`")),
               e(_b8_plain(pg["suffix_many"], act_id, "progress `suffix_many`")),
               "".join(groups),
               t("%s %s %s" % (a["start"][parents[0]["id"]],
                               a["cross_join"],
                               a["start"][parents[1]["id"]])),
               t(a["last_label"]), bars, note_els,
               t(a["one_label"]), t(a["many_label"]), t(a["reset_label"])))
def _b10_pc_note(g1, g2, genos, dom, rec):
    """Design's four-branch chain, in HER order. First match wins.

    ⚖️ `both_carriers` IS TESTED BEFORE `mixed` and that is the whole reason
    this is an ordered chain rather than a lookup. Pp × Pp is Mendel's 3:1 and
    it must never fall through to the generic line. Reimplemented identically
    in `wirePeaCross`; the ids are the branch names and the set is closed.
    """
    a1, a2 = genos[g1], genos[g2]
    if not (rec in a1 and rec in a2) and (a1 == [dom, dom] or a2 == [dom, dom]):
        # 5.38 — the two specific cases first, in `wirePeaCross`'s own order.
        if a1 == [dom, dom] and a2 == [dom, dom]:
            return "both_pure_dominant"
        if ((a1 == [dom, dom] and a2 == [rec, rec])
                or (a1 == [rec, rec] and a2 == [dom, dom])):
            return "pure_dominant_x_pure_recessive"
        return "one_pure_dominant"
    if a1 == [rec, rec] and a2 == [rec, rec]:
        return "both_pure_recessive"
    if sorted(a1) == sorted([dom, rec]) and sorted(a2) == sorted([dom, rec]):
        return "both_carriers"
    return "mixed"
# ── b10-05 `#s-bench` · species-cases ────────────────────────────────────

def r_species_cases(a, act_id):
    """⊕ b10-05 `#s-bench` — seven hard cases, and a test that runs out.

    ⚖️⚖️ THERE ARE THREE VERDICTS AND THE THIRD IS THE INSTRUMENT. *"The test
    does not settle it"* is not a hedge and not an I-don't-know: it is the
    CORRECT answer for three of the seven cases — bacteria, dandelions, the
    ring of gulls — and a student who never selects it cannot score above four
    out of seven. Dropping to a boolean would delete the lesson, so the
    renderer refuses anything but a three-entry ordered list, and refuses one
    whose third verdict is never the answer.

    ⚖️ THE CASE ORDER IS AUTHORED AND IS NOT SORTED. The three unsettleable
    cases are last and consecutive, so the bench spends its first four
    establishing the test and its last three showing where it runs out — which
    is what the lead means by "read the last two carefully". Kept as authored.

    ⚖️ COMMIT THEN REVEAL, PER CASE. `run_label` is disabled until a verdict is
    chosen, and once pressed the pick is FROZEN and the unchosen verdicts drop
    to half opacity. Same gate as `variation-plotter` and for the same reason:
    a student who can see the answer before choosing has not been asked
    anything.

    ⛔ AND THE BENCH ADJUDICATES — one of the three in B10 that do (schema
    §0.6). It prints `That is the answer` or `Not quite` on the cream panel,
    in ONE tone, above the verdict it should have been. The three verdict
    buttons take NO mark at any point: the chosen one keeps the alert outline
    it had, right or wrong, and the others simply dim. A wrong idea is
    corrected on the panel, never marked on the button (MRB-196 R10).

    ⚖️ THE LETTERS A/B/C ARE DERIVED FROM POSITION, never authored — which is
    why the verdict list is ordered and why re-ordering it re-letters the
    buttons without anything else having to change.
    """
    _b7_need(a, act_id, ("verdicts", "options_label", "commit_label", "cases",
                         "run_label", "run_done_label", "verdict_tags",
                         "progress_suffix", "tally"))
    verdicts = a["verdicts"]
    if len(verdicts) != _B10_SC_VERDICTS:
        raise ValueError(
            "species-cases %r offers %d verdict(s). There are %d, ordered, and "
            "the THIRD IS THE INSTRUMENT: 'the test does not settle it' is the "
            "correct answer for three of the seven cases, and a bench that "
            "offers only same/different cannot ask the question this lesson "
            "exists to ask." % (act_id, len(verdicts), _B10_SC_VERDICTS))
    vids = []
    for v in verdicts:
        for f in ("id", "text"):
            if not v.get(f):
                raise ValueError("species-cases %r verdict %r declares no %r."
                                 % (act_id, v.get("id"), f))
        if v["id"] in vids:
            raise ValueError("species-cases %r declares verdict id %r twice."
                             % (act_id, v["id"]))
        vids.append(v["id"])

    tags = a["verdict_tags"]
    for f in ("right", "wrong"):
        if not tags.get(f):
            raise ValueError(
                "species-cases %r verdict_tags declares no %r. Both are drawn "
                "in the same tone on the same cream panel (schema §0.6): the "
                "bench says whether the commitment held, in words, and never "
                "marks the button." % (act_id, f))
    tal = a["tally"]
    for f in ("all", "remaining_suffix"):
        if not tal.get(f):
            raise ValueError(
                "species-cases %r tally declares no %r. The line beside the "
                "check button counts DOWN — '4 still to settle' then 'all "
                "seven settled' — and a missing end is a counter that stops "
                "saying anything at the moment it matters most."
                % (act_id, f))

    cases = a["cases"]
    if len(cases) < _B10_SC_THRESHOLD:
        raise ValueError(
            "species-cases %r declares %d case(s). The stage predicate is %d "
            "opened and the `s-test` band stop MIRRORS it (MRB-249), so a "
            "shorter bench ships two rail stops that no student can tick."
            % (act_id, len(cases), _B10_SC_THRESHOLD))
    seen, answers, tabs, panels = set(), set(), [], []
    for i, c in enumerate(cases):
        for f in ("id", "label", "title", "facts", "answer", "why"):
            if not c.get(f):
                raise ValueError(
                    "species-cases %r case %r declares no %r. `facts` is what "
                    "the student decides ON and `why` is the reasoning they "
                    "get back — a case missing either is a question with no "
                    "evidence or an answer with no argument."
                    % (act_id, c.get("id"), f))
        if c["id"] in seen:
            raise ValueError("species-cases %r declares case id %r twice."
                             % (act_id, c["id"]))
        seen.add(c["id"])
        if c["answer"] not in vids:
            raise ValueError(
                "species-cases %r case %r answers %r, and the verdicts are %r. "
                "An answer outside the offered set can never be selected, so "
                "that case is wrong however the student decides it."
                % (act_id, c["id"], c["answer"], vids))
        answers.add(c["answer"])

    # ⚖️ THE THIRD VERDICT MUST BE SOMEBODY'S ANSWER. A bench that offers it
    # and never needs it teaches that it is the safe box you do not tick, which
    # is the opposite of the lesson.
    if vids[-1] not in answers:
        raise ValueError(
            "species-cases %r offers %r and no case answers it. The third "
            "verdict is the instrument: it is where the test RUNS OUT, and a "
            "bench that never lands on it has taught a student that the "
            "honest answer is always the wrong one."
            % (act_id, verdicts[-1]["text"]))

    for i, c in enumerate(cases):
        first = i == 0
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-sc-tab" '
            'data-sc-case="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(c["id"]), "true" if first else "false", t(c["label"])))
        opts = "".join(
            '<li><button type="button" class="ks3-option ks3-sc-verdict" '
            'data-sc-verdict="%s" aria-pressed="false">'
            '<span class="ks3-sc-letter" aria-hidden="true">%s</span>'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(v["id"]), t(chr(65 + j)), t(v["text"]))
            for j, v in enumerate(verdicts))
        answer_text = next(v["text"] for v in verdicts if v["id"] == c["answer"])
        panels.append(
            '<div class="ks3-sc-case" data-sc-panel="%s" data-sc-answer="%s"%s>'
            '<p class="ks3-sc-title">%s</p>'
            '<p class="ks3-sc-facts">%s</p>'
            '<p class="ks3-sc-commit">%s</p>'
            '<ul class="ks3-options ks3-sc-verdicts" role="list">%s</ul>'
            '<div class="ks3-sc-out" data-sc-out hidden>'
            '<p class="ks3-sc-tag" data-sc-tag="right" hidden>%s</p>'
            '<p class="ks3-sc-tag" data-sc-tag="wrong" hidden>%s</p>'
            '<p class="ks3-sc-answer">%s</p>'
            '<p class="ks3-sc-why">%s</p></div></div>'
            % (e(c["id"]), e(c["answer"]), "" if first else " hidden",
               t(c["title"]), t(c["facts"]), t(a["commit_label"]), opts,
               t(tags["right"]), t(tags["wrong"]),
               t(answer_text), t(c["why"])))

    return ('<div class="ks3-sc" data-sc data-run-label="%s" '
            'data-run-done-label="%s" data-tally-all="%s" '
            'data-tally-suffix="%s" data-total="%d" data-threshold="%d">'
            '<div class="ks3-sc-tabsgroup">'
            '<p class="ks3-sc-tabslabel" id="%s-cases">%s</p>'
            '<ul class="ks3-options ks3-sc-tabs" role="list" '
            'aria-labelledby="%s-cases">%s</ul></div>'
            '<div class="ks3-sc-panel">%s'
            '<div class="ks3-sc-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-sc-check" '
            'data-sc-check disabled>%s</button>'
            '<span class="ks3-sc-tally" data-sc-tally>%s</span></div>'
            '</div></div>'
            % (e(_b8_plain(a["run_label"], act_id, "`run_label`")),
               e(_b8_plain(a["run_done_label"], act_id, "`run_done_label`")),
               e(_b8_plain(tal["all"], act_id, "tally `all`")),
               e(_b8_plain(tal["remaining_suffix"], act_id,
                           "tally `remaining_suffix`")),
               len(cases), _B10_SC_THRESHOLD,
               e(act_id), t(a["options_label"]), e(act_id), "".join(tabs),
               "".join(panels), t(a["run_label"]),
               t("%d %s" % (len(cases), tal["remaining_suffix"]))))


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'base-pairs': _base_pairs,
    'nested-scale': _nested_scale,
    'punnett': _punnett,
}

KIND_SHELL = {
    'variation-plotter': ("ks3-vp-block",
                          ' data-instrument data-vpblock data-stage-done="0"'),
    'zoom-bench': ("ks3-zb-block",
                         ' data-instrument data-zbblock data-stage-done="0"'),
    'model-builder': ("ks3-dh-block",
                         ' data-instrument data-dhblock data-stage-done="0"'),
    'pea-cross': ("ks3-pc-block",
                         ' data-instrument data-pcblock data-stage-done="0"'),
    'species-cases': ("ks3-sc-block",
                         ' data-instrument data-scblock data-stage-done="0"'),
}

KIND_FN = {
    'variation-plotter': r_variation_plotter,
    'zoom-bench': r_zoom_bench,
    'model-builder': r_model_builder,
    'pea-cross': r_pea_cross,
    'species-cases': r_species_cases,
}

KIND_HEAD_TOTAL = {
    'variation-plotter': lambda a: len(a.get("characteristics") or []),
    'zoom-bench': lambda a: len(a.get("levels") or []),
    'model-builder': lambda a: len(a.get("evidence") or []),
    'species-cases': lambda a: len(a.get("cases") or []),
}

KIND_HEAD_FROM = {
    'variation-plotter': lambda a: {
        "format": "{n} of {total} %s" % _b10_suffix(a, "variation-plotter"),
        "start": 0},
    'zoom-bench': lambda a: (lambda pg: {
        "format": "%s{n}%s{total}" % (pg["step_prefix"], pg["step_join"]),
        "full": pg["all"], "start": 1})(
            _b10_zoom_progress(a.get("progress"), a.get("id") or "?")),
    'model-builder': lambda a: {
        "format": "{n} of {total} %s" % _b10_suffix(a, "model-builder"),
        "start": sum(1 for ev in (a.get("evidence") or [])
                     if _b10_mb_pass(a.get("start") or {}, ev))},
    'pea-cross': lambda a: (lambda pg: {
        "format": "{n} %s" % pg["suffix_many"], "zero": pg["none"],
        "start": 0})(_b10_pea_progress(a.get("progress"),
                                       a.get("id") or "?")),
    'species-cases': lambda a: {
        "format": "{n} of {total} %s" % _b10_suffix(a, "species-cases"),
        "start": 0},
}
