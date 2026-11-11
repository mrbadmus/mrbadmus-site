# -*- coding: utf-8 -*-
"""lean_blocks.py: the shared HTML for the lean lesson shape (KS3 and KS4).

One lesson is one record of words (docs/lessons/LEAN-RECORD.md). This file turns
the pieces of a record into markup, once, for both key stages:

    key_words()      the three or four chips
    card()           a Key knowledge or Dive deeper card (closed until tapped)
    reveal()         a tap-to-reveal comparison table, one real <table>
    key_fact()       the one or two sentences an examiner wants written
    deeper()         the Dive deeper section (closed until tapped)
    try_link()       "Try it: <simulation> ->", same tab, so Back returns here
    knowledge()      the Key knowledge section

Look and behaviour live in shared/lean.css and shared/lean.js. This file only
writes markup and never styles anything.

STATE LIVES IN ATTRIBUTES THE TEMPLATE NEVER WRITES. An open card carries
`data-lean-open` and its button `aria-expanded`; both are put on by shared/lean.js.
KS4's runtime (shared/ks4-runtime.js `patchAttr`) rewrites any attribute the
TEMPLATE names back to the template's value on every render, so a template that
carried `aria-expanded="false"` or `hidden` would snap every open card shut on
the next scroll or click. `Ctx(state_attrs=False)` leaves those attributes out
and shared/lean.js adds them on load. KS3 pages are plain HTML, so they keep
`aria-expanded="false"` in the markup (`state_attrs=True`).

Visibility is CSS-driven from `[data-lean-open]`, never from a `hidden` attribute,
for the same reason, and because print can then open everything with one rule.

Prose goes through `Ctx.fmt`. The default escapes everything and puts back
<strong>, <em>, <sub> and <sup>. KS3 passes its own `rich` (formula subscripts).
"""
import html
import re

_ALLOWED = re.compile(r"&lt;(/?)(strong|em|sub|sup)&gt;")


def prose(s):
    """Escape `s`, then put back the four inline tags a record may use."""
    return _ALLOWED.sub(r"<\1\2>", html.escape(str(s), quote=False))


def esc(s):
    return html.escape(str(s), quote=True)


# The drawn marks. Typed characters would drop to a fallback font.
MARK_RIGHT = ('<svg class="lean-mark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
              '<path d="M4 13l5 5L20 7"/></svg>')
MARK_WRONG = ('<svg class="lean-mark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
              '<path d="M6 6l12 12M18 6L6 18"/></svg>')
CHEVRON = ('<svg class="lean-chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
           '<path d="M6 9l6 6 6-6"/></svg>')

ROUTES = ("CF", "CH", "TF", "TH")
# The only route sets a record may use, and the template flag that names each.
ROUTE_FLAG = {
    frozenset(("CH", "TH")): "isHigher",
    frozenset(("TF", "TH")): "isTriple",
    frozenset(("CF", "TF")): "notHigher",
    frozenset(("CF", "CH")): "notTriple",
    frozenset(("TH",)): "isTH",
}


EASY_MISTAKES_ID = "easy-mistakes"


def card_id(c):
    """A card's stable page id: the record's own `id`, or `easy-mistakes` for the Easy
    mistakes card, so misconceptions can point at a real element."""
    if c.get("id"):
        return c["id"]
    return EASY_MISTAKES_ID if str(c.get("title", "")).strip().lower() == "easy mistakes" else None


def route_flag(routes):
    """The template flag for a record's `routes`, or None for every route."""
    if not routes:
        return None
    key = frozenset(routes)
    if key == frozenset(ROUTES):
        return None
    if not key <= frozenset(ROUTES) or key not in ROUTE_FLAG:
        raise ValueError(
            "lean record: routes %r is not one of CH+TH (Higher), TF+TH (Triple), "
            "CF+TF (not Higher), CF+CH (not Triple) or TH. Other route sets need "
            "a flag in lean_blocks.ROUTE_FLAG and in ks4-lib.js's route()." % (routes,))
    return ROUTE_FLAG[key]


class Ctx:
    """Per-page state: unique ids, the prose formatter, and the two seams a
    key stage fills in.

    prefix       id prefix, so two pages' ids never collide in tests.
    fmt          prose formatter (escapes; allows inline tags).
    state_attrs  True: write aria-expanded="false" into the markup (KS3).
                 False: leave it to shared/lean.js (KS4, see module docstring).
    part         part(dict) -> html or None. Handles {"slot":..} and {"figure":..}.
    route_wrap   route_wrap(flag, html) -> html. KS4 wraps in <sc-if>.
    defs         {lower-case word: definition} for the Key words chips.
    """

    def __init__(self, prefix="lean", fmt=prose, state_attrs=True, part=None,
                 route_wrap=None, defs=None):
        self.prefix = prefix
        self.fmt = fmt
        self.state_attrs = state_attrs
        self.part = part
        self.route_wrap = route_wrap
        self.defs = defs or {}
        self._n = 0

    def nid(self, kind):
        self._n += 1
        return "%s-%s-%d" % (self.prefix, kind, self._n)

    def expanded(self):
        return ' aria-expanded="false"' if self.state_attrs else ""


# ── parts of a card ──────────────────────────────────────────────────────

def _part(ctx, p):
    if isinstance(p, str):
        return '<p class="lean-p">%s</p>' % ctx.fmt(p)
    if isinstance(p, dict):
        if "points" in p:
            return ('<ul class="lean-list">%s</ul>'
                    % "".join("<li>%s</li>" % ctx.fmt(x) for x in p["points"]))
        if "mistakes" in p:
            rows = []
            for wrong, right in p["mistakes"]:
                rows.append(
                    '<li class="lean-mistake">'
                    '<p class="lean-wrong">%s<span class="lean-sr">Wrong: </span>%s</p>'
                    '<p class="lean-right">%s<span class="lean-sr">Right: </span>%s</p></li>'
                    % (MARK_WRONG, ctx.fmt(wrong), MARK_RIGHT, ctx.fmt(right)))
            return '<ul class="lean-mistakes">%s</ul>' % "".join(rows)
        if "slot" in p or "figure" in p:
            out = ctx.part(p) if ctx.part else None
            if out is None:
                raise ValueError("lean record: nothing handles %r on this page" % (p,))
            return out
    raise ValueError("lean record: unknown card part %r" % (p,))


def card(ctx, c):
    """One card: a heading holding a real button, and the body it controls."""
    if c.get("kind") != "card":
        raise ValueError("lean record: expected a card, got %r" % (c.get("kind"),))
    bid, cid = ctx.nid("b"), ctx.nid("c")
    body = "".join(_part(ctx, p) for p in c["body"])
    cid_attr = (' id="%s"' % esc(card_id(c))) if card_id(c) else ""
    out = ('<div class="lean-card"%s data-lean-card>'
           '<h3 class="lean-card-h"><button type="button" class="lean-card-btn" id="%s" '
           'aria-controls="%s"%s><span class="lean-card-title">%s</span>%s</button></h3>'
           '<div class="lean-card-body" id="%s">%s</div></div>'
           % (cid_attr, bid, cid, ctx.expanded(), ctx.fmt(c["title"]), CHEVRON, cid, body))
    return _routed(ctx, c, out)


def reveal(ctx, t):
    """A comparison table. Every answer cell is hidden until tapped."""
    if t.get("kind") != "reveal":
        raise ValueError("lean record: expected a reveal table, got %r" % (t.get("kind"),))
    cols = t["cols"]
    head = ('<tr><th scope="col" class="lean-th-corner"><span class="lean-sr">%s</span></th>%s</tr>'
            % ("Row", "".join('<th scope="col">%s</th>' % ctx.fmt(c) for c in cols)))
    rows = []
    for row in t["rows"]:
        label, cells = row[0], row[1:]
        if len(cells) != len(cols):
            raise ValueError("lean record: reveal row %r has %d cells for %d columns"
                             % (label, len(cells), len(cols)))
        tds = []
        for col, text in zip(cols, cells):
            tid = ctx.nid("r")
            tds.append(
                '<td><button type="button" class="lean-cell" data-lean-cell '
                'aria-controls="%s"%s>'
                '<span class="lean-cell-hint">Tap<span class="lean-sr"> to show %s, %s</span></span>'
                '<span class="lean-cell-text" id="%s">%s</span></button></td>'
                % (tid, ctx.expanded(), esc(label), esc(col), tid, ctx.fmt(text)))
        rows.append('<tr><th scope="row">%s</th>%s</tr>' % (ctx.fmt(label), "".join(tds)))
    out = ('<div class="lean-reveal" data-lean-reveal>'
           '<div class="lean-reveal-head"><h3 class="lean-reveal-h">%s</h3>'
           '<button type="button" class="lean-showall" data-lean-showall%s>'
           'Show all</button></div>'
           '<table class="lean-table"><thead>%s</thead><tbody>%s</tbody></table></div>'
           % (ctx.fmt(t["title"]), ' aria-pressed="false"' if ctx.state_attrs else "",
              head, "".join(rows)))
    return _routed(ctx, t, out)


def _routed(ctx, item, out):
    flag = route_flag(item.get("routes"))
    if flag and ctx.route_wrap:
        return ctx.route_wrap(flag, out)
    return out


def items(ctx, lst):
    out = []
    for it in lst:
        k = it.get("kind")
        out.append(card(ctx, it) if k == "card" else reveal(ctx, it))
    return "".join(out)


# ── sections ─────────────────────────────────────────────────────────────

def section(ctx, kind, title, inner, sid=None, extra=""):
    hid = "%s-h-%s" % (ctx.prefix, kind)
    return ('<section class="lean-sec lean-sec-%s"%s data-lean-sec="%s" aria-labelledby="%s"%s>'
            '<h2 class="lean-h" id="%s">%s</h2>%s</section>'
            % (kind, (' id="%s"' % esc(sid)) if sid else "", kind, hid, extra, hid,
               esc(title), inner))


def key_words(ctx, words, sid=None):
    lis = []
    for w in words:
        d = ctx.defs.get(w.lower())
        if d:
            did = ctx.nid("w")
            lis.append('<li class="lean-word"><button type="button" class="lean-chip lean-chip-btn" '
                       'data-lean-word aria-controls="%s"%s>%s</button>'
                       '<p class="lean-word-def" id="%s">%s</p></li>'
                       % (did, ctx.expanded(), ctx.fmt(w), did, ctx.fmt(d)))
        else:
            lis.append('<li class="lean-word"><span class="lean-chip">%s</span></li>' % ctx.fmt(w))
    return section(ctx, "words", "Key words",
                   '<ul class="lean-words" role="list">%s</ul>' % "".join(lis), sid=sid)


def knowledge(ctx, lst, sid=None, extra=""):
    return section(ctx, "knowledge", "Key knowledge",
                   '<div class="lean-stack">%s</div>' % items(ctx, lst), sid=sid, extra=extra)


def key_fact(ctx, text, sid=None):
    return ('<section class="lean-sec lean-sec-fact"%s data-lean-sec="fact" aria-labelledby="%s-h-fact">'
            '<div class="lean-fact"><h2 class="lean-fact-label" id="%s-h-fact">Key fact</h2>'
            '<p class="lean-fact-body">%s</p></div></section>'
            % ((' id="%s"' % esc(sid)) if sid else "", ctx.prefix, ctx.prefix, ctx.fmt(text)))


def deeper(ctx, lst, sid=None):
    """Dive deeper. Closed until tapped; the box holds ordinary cards."""
    bid, cid = ctx.nid("db"), ctx.nid("dc")
    return ('<section class="lean-sec lean-sec-deeper"%s data-lean-sec="deeper">'
            '<div class="lean-deeper" data-lean-deeper>'
            '<h2 class="lean-h lean-deeper-h"><button type="button" class="lean-deeper-btn" id="%s" '
            'aria-controls="%s"%s><span>Dive deeper</span>%s</button></h2>'
            '<div class="lean-deeper-body" id="%s"><div class="lean-stack">%s</div></div>'
            '</div></section>'
            % ((' id="%s"' % esc(sid)) if sid else "", bid, cid, ctx.expanded(), CHEVRON,
               cid, items(ctx, lst)))


def fig_wrap(html_):
    """A diagram inside a card: the drawing, then its "Zoom in" / "Fit to screen" button.

    shared/lean.js fits the drawing to the card and shows the button only where the drawing's
    natural width is over the room. The wrapper and button are plain markup; the state
    (`data-lean-needs`, `data-lean-zoom`) is put on by lean.js, never here, so KS4's runtime
    leaves it alone."""
    return ('<div class="lean-fig" data-lean-fig>%s'
            '<button type="button" class="lean-zoom" data-lean-zoom-btn>'
            '<span class="lean-zoom-in">Zoom in</span><span class="lean-zoom-out">Fit to screen</span>'
            '</button></div>' % html_)


def try_link(spec):
    """The "Try it" link, or "" when no simulation matches the lesson.

    Same tab on purpose: the Back button then returns to the lesson."""
    if not spec:
        return ""
    return ('<p class="lean-try"><a class="lean-try-link" href="%s">Try it: %s '
            '<svg class="lean-mark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            '<path d="M4 12h15M13 6l6 6-6 6"/></svg></a></p>'
            % (esc(spec["href"]), prose(spec["label"])))
