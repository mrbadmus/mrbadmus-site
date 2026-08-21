"""ks3_art.kit — the shared drawing and formatting primitives.

Everything here is used by MORE THAN ONE unit, which is the only reason it is
here rather than in a unit module. Moved verbatim out of ``build_ks3.py`` by
MRB-271; the bytes are unchanged.

⚠️ THIS FILE IS SHARED. A lane that changes it changes every unit's output, so
say so before you start — see ``docs/ks3/worktrees.md``.
"""

import html
import json
import math
import re


# ⛔ FAMILY_BLURB REMOVED 2026-08-07 — MRB-181, architecture.md §8.10.
# It rendered §6's seven architecture families as a one-line gloss on every
# coming-soon page ("One idea explains a whole class of behaviour"). That is
# the platform describing its own compositional grammar to a twelve-year-old
# who came looking for a lesson and found a placeholder. The families are real
# and stay — in §6, in structure.py, and in what an authored lesson is shaped
# like. They are not page copy.


def e(s):
    return html.escape(str(s if s is not None else ""), quote=True)
# ── the drawn marks (SPEC.md §9.3) ───────────────────────────────────────
#
# ✓ ✕ → ARE DRAWN, NEVER TYPED. Design's own five latin woff2 subsets — the
# exact bytes now in shared/fonts/ — contain none of U+2713, U+2715 or U+2192;
# confirmed by reading the cmap of each file. Typed as characters all three
# drop to a system font mid-glyph, and inside a 27px Bricolage-800 badge that
# is a visible defect rather than a subtlety. R2 makes the marks load-bearing
# (colour is never the only signal on a state), so they cannot simply be
# dropped either. Inline SVG on `currentColor` satisfies both, and `.ks3-mark`
# in shared/ks3.css sizes it to 1em of whatever it sits in.
#
# MARK_TICK and MARK_CROSS are the canonical paths for the ladder's ANSWERED
# option states. shared/ks3.js draws them at runtime — a resting ladder badge
# carries its letter, not a mark — so no renderer emits them today. They live
# here so there is exactly one definition of each path in the system: if the
# ladder ever needs a mark at build time it takes it from here rather than
# growing a second copy that is free to drift.
MARK_ARROW = ('<svg class="ks3-mark ks3-mark-arrow" viewBox="0 0 24 24" '
              'aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>')
MARK_TICK = ('<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true">'
             '<path d="M4 13l5 5L20 7"/></svg>')
MARK_CROSS = ('<svg class="ks3-mark" viewBox="0 0 24 24" aria-hidden="true">'
              '<path d="M6 6l12 12M18 6L6 18"/></svg>')
# Escaped TEXT, with the three marks DRAWN rather than typed.
#
# ⚠️ Text nodes only — never an attribute value. MARK_ARROW carries double
# quotes, so substituting inside `data-feedback="…"` or an `aria-label` would
# terminate the attribute and emit broken markup. `e()` stays the attribute
# escaper for exactly that reason, and the split is the whole safety property:
# if you cannot tell whether a slot is text or an attribute, it is an attribute.
#
# This matters because authored copy uses the arrow as chemistry notation —
# "Solid → liquid", "warmer → faster", "smaller box → twice as many wall hits".
# The content is not touched; the same character is simply rendered with a glyph
# the fonts actually have.
MARKS = (("\u2192", MARK_ARROW), ("\u2713", MARK_TICK), ("\u2715", MARK_CROSS))
def t(s):
    out = e(s)
    for ch, mark in MARKS:
        if ch in out:
            out = out.replace(ch, mark)
    return out
# ── inline emphasis (⊕ B1 round two) ─────────────────────────────────────
#
# Design's authored strings carry `<em>` and `<strong>` — the key fact, the key
# note, the MRS GREN explainer, a scorecard note and the hook's reveal all use
# one or the other, and §4.8.1 B's own field note sanctions `<em>` in a key
# fact. `t()` is `html.escape`, so every one of those was rendering as a
# LITERAL `<em>` on the page: Design's emphasis silently turned into visible
# tag soup. Found by the b1-01 authoring run before it could ship.
#
# The fix is an allow-list and deliberately a small one. Escape everything, then
# put back exactly two tags. Nothing else is permitted — not `<a>`, not `<span
# class>`, not a bare `<b>` — because the authored strings are the surface a
# lesson's science lands on, and a general HTML pass-through there is an
# injection hole and a styling backdoor at the same time. Two tags carry every
# case in the delivery, and a third needs a ruling rather than a regex.
#
# ⊕ THE THIRD TAG, RULED 20 Aug 2026 (MRB-272, C3). The line above said a
# third needed a ruling rather than a regex. This is the ruling, and `<sub>`
# is admitted.
#
# What forced it: c3-06 writes the Rf symbol as `R<sub>f</sub>` in three
# strings, because Design ruled the convention for the whole course under C2
# flag 13 — a real `<sub>` element, never a Unicode subscript. It is not a
# preference. THERE IS NO UNICODE SUBSCRIPT `f`, so for this symbol the
# alternative does not exist, and without the tag the page shipped a visible
# `R&lt;sub&gt;f&lt;/sub&gt;` to a student. That is the escape-as-visible
# defect, not a styling nicety.
#
# It meets the bar the allow-list is drawn at, which is why it is admitted
# and `<a>` and `<span class>` still are not:
#   * it is SEMANTIC, not styling — a subscript in Rf, and in CaCO3, is part
#     of how the symbol is spelled, and a reader who loses it loses meaning;
#   * it CARRIES NO ATTRIBUTES, so it is neither an injection hole nor a
#     styling backdoor, which is the two-part test the paragraph above sets;
#   * it is needed beyond this unit — C4 renders every formula from
#     `parts: [{sym, sub}]` precisely so that subscripts are real elements,
#     and C4/C5 cannot be built without it.
#
# Measured before admitting it: no lesson outside C3 authors `<sub>` in any
# string, so this widens what `rich()` will emit without changing a byte of
# any page already built.
_RICH_OK = ("em", "strong", "sub")
_RICH_RE = re.compile(r"&lt;(/?)(%s)&gt;" % "|".join(_RICH_OK))
def rich(s):
    """`t()` plus `<em>`, `<strong>` and `<sub>`, and nothing else."""
    return _RICH_RE.sub(r"<\1\2>", t(s))
# ⚠️ ← (U+2190) is absent from the same subsets, and the browse layer used to
# open three back-links with one. Design's system has no left-arrow mark to
# draw instead, so those links now say "Back to …" in words — which is what R2
# would have asked for anyway.

OPTION_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def option_letter(i):
    """A B C D … — the resting content of an option's mark badge."""
    return OPTION_LETTERS[i] if i < len(OPTION_LETTERS) else str(i + 1)
# ── SVG ART · code draws the diagrams (Mide's ruling, 18 Aug 2026) ────────
#
# The third figure state. `r_figure` had two: `needed` printed an honest
# "Diagram coming soon" placeholder, and anything else printed
# `<img src="/ks3/figures/<id>.svg">`. Seventeen figures were declared across
# B1–B5 and fifteen sat at `needed`, because the second branch needs an asset
# nobody had drawn — `ks3/figures/` does not exist and never has, so the only
# reachable branch was the placeholder.
#
# Mide's ruling closes that: code draws them itself, Design does not author a
# pass for it, and the drawing is INLINE SVG with no external asset, no raster
# and no new font. So the `<img>` branch is not the one that gets used; a new
# `drawn` status is, and it dispatches into a closed registry exactly as
# `_css_art` does for the hook.
#
# Closed, with a raise on an unknown name, for `_css_art`'s reason: a figure
# that silently renders nothing is a hole the page hides. `status: "drawn"`
# with no `art`, or an `art` the registry does not know, fails the build.
#
# WHAT THE RULING BINDS, and where each clause is honoured below:
#   · inline only, no external asset      — every drawer returns markup; no
#                                           `<image>`, no `url(`, no @font-face
#   · --ks3-* tokens for every colour     — `_SVG_INK` … `_SVG_TINTS`; not one
#                                           literal hex in a drawer
#   · --st-accent-text under 24px         — `_SVG_ACCENT_TEXT`. `--ks3-accent`
#                                           is 3.4:1 and is never given to a
#                                           label; the token comment in
#                                           shared/tokens.css says so and this
#                                           is the second place it is enforced
#   · never colour-alone                  — every distinction carries a second
#                                           channel. The thread is accent AND
#                                           a 3px stroke AND a numbered badge;
#                                           a non-feeding link is dashed AND
#                                           labelled in words
#   · <title> and <desc> on every figure  — `_svg_open` requires both and
#                                           raises without them
#   · sensible screen-reader order        — `role="img"` +
#                                           `aria-labelledby="<t> <d>"` makes
#                                           the figure ONE announced image
#                                           carrying the whole description,
#                                           and the drawers still emit rows
#                                           top-down so a traversing AT reads
#                                           the web in trophic order

# Tokens, once. A drawer that wants a colour takes it from here, so "every
# colour is a --ks3-* token" is checkable by grepping this block rather than
# by reading every drawer.
_SVG_INK         = "var(--ks3-ink)"
_SVG_INK_BODY    = "var(--ks3-ink-body)"
_SVG_INK_MUTED   = "var(--ks3-ink-muted)"
_SVG_GROUND      = "var(--ks3-ground)"
_SVG_CARD        = "var(--ks3-card)"
_SVG_BAND        = "var(--ks3-band)"
_SVG_INSET       = "var(--ks3-inset)"
_SVG_ACCENT      = "var(--ks3-accent)"
_SVG_ACCENT_TEXT = "var(--ks3-accent-text)"
_SVG_ACCENT_TINT = "var(--ks3-accent-tint)"
_SVG_RULE_STRONG = "var(--ks3-rule-strong)"
def _svg_open(fig, width, height):
    """The wrapper every drawer opens with. `title` and `desc` are REQUIRED.

    Not defaulted to the caption: the caption is a sentence for a sighted
    reader who can already see the drawing, and a `<desc>` has to carry what
    the drawing SHOWS to someone who cannot. Defaulting one to the other would
    satisfy the grep and fail the reader, so an absent `desc` raises.
    """
    for key in ("title", "desc"):
        if not fig.get(key):
            raise ValueError(
                "figure %r is status 'drawn' but has no %r. Mide's diagram "
                "ruling requires <title> AND <desc> on every figure, and the "
                "caption is not a substitute: the caption addresses a reader "
                "who can see the drawing." % (fig.get("id"), key))
    fid = fig["id"]
    # ⊕ MRB-254 — THE DRAWING DECLARES ITS OWN READABLE WIDTH, and the
    # stylesheet's `min-width: 700px` becomes the floor rather than the answer.
    #
    # 700 was measured once, against three figures that are all 760 wide, and
    # it was close enough to be invisible: a 760-unit drawing held at 700px is
    # scaled to 92%, so a 15px label lands at 13.8px and nobody notices. The
    # biology kit is 860 and 900 units wide. At 700 those are scaled to 81% and
    # 78%, and Design's 13px key lines arrive at 10.5px — under the floor
    # `_label` refuses at source, reintroduced by the stylesheet after the
    # drawer has done everything right.
    #
    # So the width the drawer chose is the width the figure keeps, and the
    # narrow reader scrolls. `.ks3-figure-scroll` is told whether it is
    # actually overflowing by ks3.js rather than by a guessed breakpoint —
    # with fourteen different widths there is no single breakpoint that could
    # be right, which is what forced the measurement.
    return (
        '<svg class="ks3-figure-svg" viewBox="0 0 %d %d" role="img" '
        'style="min-width:%dpx" '
        'aria-labelledby="%s-t %s-d" preserveAspectRatio="xMidYMid meet">'
        '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>'
        % (width, height, width, e(fid), e(fid), e(fid), e(fig["title"]),
           e(fid), e(fig["desc"])))
def _svg_text(x, y, s, size=15, fill=_SVG_INK, weight="600", anchor="middle",
              family="'Plus Jakarta Sans', sans-serif", spacing=None, cls=None,
              **data):
    """One text node, with the under-24px accent rule enforced at the source.

    `--ks3-accent` measures 3.4:1 on the ground. It is legal for large display
    type and illegal for a label, and the whole point of routing every drawer's
    text through one function is that the rule is checked once, in code, rather
    than trusted fifty times in markup.
    """
    if fill == _SVG_ACCENT and size < 24:
        raise ValueError(
            "text %r is %dpx in --ks3-accent. Accent is 3.4:1 and is never a "
            "contrast partner for text under 24px — use --ks3-accent-text "
            "(6.0:1). This is the ruling, and shared/tokens.css says the same "
            "thing beside the token." % (s, size))
    extra = ' letter-spacing="%s"' % e(spacing) if spacing else ""
    # ⊕ MRB-254 — `data_*` hooks on a LABEL, not only on a shape. A
    # content-truth row that has to assert "this square's printed genotype is
    # the one its column and row make" needs the printed string and the two
    # gametes reachable from the same node; without it the row matches a text
    # element by its position, which is the assertion measuring the frame
    # again. No output changes where none is passed.
    extra += "".join(_data_attrs(data))
    # ⚠️ COLOUR GOES IN `style`, NEVER IN `fill="…"`. A custom property is only
    # substituted inside a CSS declaration; `fill="var(--ks3-ink)"` is an SVG
    # PRESENTATION attribute, `var(--ks3-ink)` is not a valid <paint>, and the
    # attribute is dropped — so the element falls back to the initial value,
    # which is opaque black. Nothing warns. The first render of this drawing
    # came out as five black bars with black text inside them, and the token
    # grep was clean the whole time because the tokens were all there, in the
    # one place where they do nothing. Every drawer in this file routes paint
    # through `style` for that reason.
    return ('<text%s x="%s" y="%s" font-family="%s" font-size="%s" '
            'font-weight="%s" style="fill:%s" text-anchor="%s"%s>%s</text>'
            % (' class="%s"' % e(cls) if cls else "",
               x, y, family, size, weight, fill, anchor, extra, e(s)))
_SVG_MONO = "'DM Mono', monospace"
# ── ⊕ MRB-254 · the biology figure kit ──────────────────────────────────
#
# Fourteen figures arrive at once (Design's twelve for the WS1 diagram gaps,
# plus two drawn here), against three that existed. Three drawers could each
# spell their own rects; seventeen cannot, and the reason is not tidiness:
#
#   · THE PAINT LAW IS ONE LINE OF CODE OR IT IS SEVENTEEN CHANCES TO FORGET
#     IT. `fill="var(--ks3-ink)"` is a dropped attribute and an opaque-black
#     element, silently — the note on `_svg_text` records what that cost the
#     first time. Routing every shape through `_shape` below means the law is
#     kept once, where it can be read, instead of trusted a few thousand times
#     across seventeen drawings.
#   · EVERY ARROW, TICK AND CROSS IS DRAWN. The latin subsets carry none of
#     `→ ✓ ✕`, so a typed one silently falls back to whatever the system has,
#     at a size and weight nobody chose. `_arrow_head` is the drawn one.
#   · A HOOK A GATE CAN NAME. `data-*` on a shape is what lets a content-truth
#     row measure the ENCODING rather than the frame — the distinction MRB-257
#     decision 4 was written for. `**data` on every emitter makes adding one
#     free, so there is no reason to skip it.

_SVG_RULE        = "var(--ks3-rule)"
_SVG_INK_FAINT   = "var(--ks3-ink-faint)"
_SVG_INK_GHOST   = "var(--ks3-ink-ghost)"
_SVG_BLUE_TEXT   = "var(--ks3-blue-text)"
# ⚠️ `--ks3-font-body` IS INSTRUMENT SANS, and the three figures that predate
# this kit draw their labels in Plus Jakarta Sans — which is self-hosted, so it
# renders, and is therefore invisible as a defect: the figure's labels are
# simply set in a different face from the prose around them. Design's twelve
# name Instrument Sans throughout, which is the page's own body font, so the
# new drawers take `_SVG_BODY` and the old three are left alone rather than
# re-drawn under a ticket that does not own them. Recorded in the MRB-254
# report as drift, not fixed here.
_SVG_BODY    = "'Instrument Sans', system-ui, sans-serif"
_SVG_DISPLAY = "'Bricolage Grotesque', system-ui, sans-serif"
# The smallest a label may be set. Design's notes claim nothing below 13px and
# five labels across three of the twelve are 12px — raised on implementation,
# because 12px inside a plate that is already being scrolled sideways on a
# phone is the size the scroll container exists to avoid.
_SVG_MIN_LABEL = 13
def _svg_attrs(fill, stroke, w, dash, opacity, cls, data):
    """The paint and the hooks, in the one place the paint law is kept."""
    bits = []
    if cls:
        bits.append(' class="%s"' % e(cls))
    paint = []
    # `none` is a keyword, not a colour, and it belongs in the attribute where
    # it costs nothing. Everything else is a token and goes through `style`.
    if fill is not None:
        paint.append("fill:%s" % fill)
    if stroke is not None:
        paint.append("stroke:%s" % stroke)
    if paint:
        bits.append(' style="%s"' % ";".join(paint))
    if w is not None:
        bits.append(' stroke-width="%s"' % w)
    if dash:
        bits.append(' stroke-dasharray="%s"' % dash)
    if opacity is not None:
        bits.append(' opacity="%s"' % opacity)
    bits.extend(_data_attrs(data))
    return "".join(bits)
def _data_attrs(data):
    """`data_wall="inner"` becomes `data-wall="inner"`, and nothing else does.

    ⚠️ THE PREFIX IS WRITTEN AT THE CALL SITE AND STRIPPED HERE, and both
    halves of that are a gate. This started as `'data-%s' % k.replace('_','-')`
    over a bare kwarg, so a caller writing the self-documenting
    `data_wall="inner"` — which is what the porting contract asked for, and
    what reads correctly at the call site — emitted `data-data-wall`. A hook a
    content-truth row cannot find is worse than no hook: the row does not fail,
    it returns nothing and reports green, which is precisely the shape of
    absence MRB-257 decision 4 exists to close.

    So a key that does not start with `data_` raises, rather than silently
    becoming a presentation attribute nobody asked for. There is no legitimate
    reason for an emitter to take an arbitrary attribute by keyword; if one
    ever appears it should arrive through its own named parameter.
    """
    out = []
    for k in sorted(data):
        if not k.startswith("data_") or len(k) < 6:
            raise ValueError(
                "an emitter was given the keyword %r. The only keywords an "
                "emitter takes beyond its named ones are HOOKS, spelled "
                "`data_<name>`, and they become `data-<name>` on the element. "
                "A bare keyword would land as a presentation attribute, where "
                "it does nothing and looks like it does something." % k)
        if data[k] is None:
            continue
        out.append(' data-%s="%s"'
                   % (k[5:].replace("_", "-"), e(str(data[k]))))
    return out
def _n(v):
    """A number, trimmed. `240.0` and `240` are the same point; only one of
    them should reach the file, or a byte-comparison of two builds turns on
    whether a coordinate came out of arithmetic or out of a literal."""
    if isinstance(v, float):
        s = "%.2f" % v
        s = s.rstrip("0").rstrip(".")
        return s if s not in ("", "-0") else "0"
    return str(v)
def _path(d, fill="none", stroke=None, w=None, dash=None, opacity=None,
          cls=None, **data):
    return '<path d="%s"%s/>' % (d, _svg_attrs(fill, stroke, w, dash,
                                               opacity, cls, data))
def _rect(x, y, width, height, rx=None, fill="none", stroke=None, w=None,
          dash=None, opacity=None, cls=None, **data):
    return ('<rect x="%s" y="%s" width="%s" height="%s"%s%s/>'
            % (_n(x), _n(y), _n(width), _n(height),
               ' rx="%s"' % _n(rx) if rx is not None else "",
               _svg_attrs(fill, stroke, w, dash, opacity, cls, data)))
def _circle(cx, cy, r, fill="none", stroke=None, w=None, dash=None,
            opacity=None, cls=None, **data):
    return ('<circle cx="%s" cy="%s" r="%s"%s/>'
            % (_n(cx), _n(cy), _n(r),
               _svg_attrs(fill, stroke, w, dash, opacity, cls, data)))
def _ellipse(cx, cy, rx, ry, fill="none", stroke=None, w=None, dash=None,
             opacity=None, cls=None, **data):
    return ('<ellipse cx="%s" cy="%s" rx="%s" ry="%s"%s/>'
            % (_n(cx), _n(cy), _n(rx), _n(ry),
               _svg_attrs(fill, stroke, w, dash, opacity, cls, data)))
def _line(x1, y1, x2, y2, stroke=None, w=None, dash=None, opacity=None,
          cls=None, **data):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s"%s/>'
            % (_n(x1), _n(y1), _n(x2), _n(y2),
               _svg_attrs(None, stroke, w, dash, opacity, cls, data)))
def _label(x, y, s, size=15, fill=_SVG_INK, weight="600", anchor="middle",
           family=None, spacing=None, cls=None, **data):
    """`_svg_text` with the body face and the 13px floor, for the new kit.

    Separate from `_svg_text` rather than a change to it, because the three
    figures that predate this ticket are drawn in Plus Jakarta Sans and
    re-facing an approved drawing is not this ticket's call.
    """
    if size < _SVG_MIN_LABEL:
        raise ValueError(
            "label %r is set at %dpx. %dpx is the floor: these plates are "
            "already scrolled sideways on a phone, and a label below it is "
            "the thing the scroll container exists to prevent."
            % (s, size, _SVG_MIN_LABEL))
    if not str(s).strip():
        raise ValueError(
            "an empty label was asked for at (%s, %s). A `<text>` with no "
            "content renders as nothing at all — Design's nine-row key came "
            "out as nine empty badges exactly this way, and it is the same "
            "class of hole as `{brace}` and `[object Object]`." % (x, y))
    return _svg_text(x, y, s, size=size, fill=fill, weight=weight,
                     anchor=anchor, family=family or _SVG_BODY,
                     spacing=spacing, cls=cls, **data)
def _mono(x, y, s, size=15, fill=_SVG_INK_MUTED, weight="500",
          anchor="start", spacing=None, cls=None, **data):
    """The mono voice: measurements, magnifications, notes on the plate."""
    return _label(x, y, s, size=size, fill=fill, weight=weight, anchor=anchor,
                  family=_SVG_MONO, spacing=spacing, cls=cls, **data)
def _activity(lesson, act_id):
    return next((a for a in lesson.get("activities", []) if a["id"] == act_id), None)
def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)
def _self_check(a, act_id):
    """MRB-196's self-check, shared by the sorter and settles-it.

    Extracted rather than written twice: it is one component, ruled once, and
    two copies is how one copy quietly stops obeying the rule below.

    There is no `answer` key and there must never be one. The student is asked
    how many of their OWN judgements matched, and only the student knows. A
    right answer here would put a mark on an activity option, which R3 forbids.
    """
    sc = a.get("self_check")
    if not sc:
        return ""
    if "answer" in sc:
        raise ValueError(
            "%r's self_check carries an `answer` key. It must not: only the "
            "student knows how many of their own marks matched, and a right "
            "answer here would mark an activity option, which R3 forbids."
            % act_id)
    opts = "".join(_option_li(i, o, ' aria-pressed="false"')
                   for i, o in enumerate(sc.get("options") or []))
    note = ('<p class="ks3-selfcheck-note">%s</p>' % rich(sc["note"])
            if sc.get("note") else "")
    return ('<div class="ks3-selfcheck" data-selfcheck hidden>'
            '<p class="ks3-selfcheck-q">%s</p>'
            '<ul class="ks3-options ks3-selfcheck-options" role="list">%s</ul>'
            '%s</div>' % (t(sc.get("question", "")), opts, note))
def _option_li(i, text, extra=""):
    """One answer button. The letter badge is the resting mark (R2/§5).

    Shared by activities and the ladder so the two are the same control, and
    the ONLY difference between them is the attributes: an activity option
    takes `aria-pressed` and shows that it was chosen; a ladder option takes
    `data-correct` and `data-feedback` and gets marked. R3 lives in that gap —
    if `data-correct` ever appears on an activity option, the student reads the
    whole page as a test and committing before revealing loses its point.
    """
    return ('<li><button type="button" class="ks3-option" data-i="%d"%s>'
            '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (i, extra, option_letter(i), t(text)))
def r_activity_options(options):
    """R3: chosen, never correct. No data-correct, no green, never disabled."""
    return ('<ul class="ks3-options" role="list">%s</ul>'
            % "".join(_option_li(i, o, ' aria-pressed="false"')
                      for i, o in enumerate(options)))
def r_bench_gate(gate):
    """C6's commit gate — four options, then the gate is GONE.

    Gating by ABSENCE, not by disable: Design removes the whole block when it
    is answered rather than greying it, so the instrument arrives in the space
    the question was occupying. `wireBenchGate` hides this and unhides
    `[data-benchbody]`; nothing else on the page can open it.
    """
    if not gate:
        return "", ""
    return ('<div class="ks3-benchgate" data-benchgate>'
            '<p class="ks3-commit">%s</p>%s</div>'
            % (t(gate.get("prompt", "")),
               r_activity_options(gate.get("options") or [])),
            ' hidden data-benchbody')
# ═══ C2 · Atoms, elements and compounds (⊕ MRB-220) ══════════════════════
#
# Nine instruments across six lessons. Everything below has markup here, real
# CSS in `shared/ks3.css`, real behaviour in `shared/ks3.js` reached from
# `wireInstruments()`, and at least one measured row in `ks3_parity.COMPONENTS`
# on a page that renders it. A dispatch-table entry is not a component.


def _canvas_frame(inner, foot, row=False):
    """The dark-canvas frame — one shape, used four times in C2 (map N12).

    c2-01's zoom, c2-03's dish, c2-05's builder and c2-06's balance all draw
    into the same wrapper: a `--ks3-r-card` box with a 2px `--ks3-on-dark-muted`
    outline, `overflow: hidden`, and a `--ks3-dark-panel` strip under the canvas
    carrying the controls or the caption. It was unnamed in the map because
    Design inlines it four times; it is one component here so the fifth
    instrument that wants it inherits a measured box rather than a fourth copy.
    """
    return ('<div class="ks3-canvas-frame">%s'
            '<div class="ks3-canvas-foot"%s>%s</div></div>'
            % (inner, ' data-row="1"' if row else "", foot))
def _lever_decimals(step):
    """How many decimal places a control's own step needs.

    DERIVED, never authored. A step of 0.5 needs one place and an integer set
    needs none; a `decimals` key would be a second statement of the same fact
    and a second place for it to disagree with the slider.
    """
    if step is None:
        return 0
    return 0 if float(step) == int(float(step)) else 1
def _lever_num(value, decimals, fmt):
    """One readout, formatted. `fmt` is an authored "{n} kg"-shaped string."""
    return (fmt or "{n}").replace("{n}", "%.*f" % (decimals, float(value)))
# DISPATCH: "lever-steps": ("ks3-lstep-block", ' data-instrument data-lstepblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "lever-steps":            r_lever_steps,
#
# ╔═══════════════════════════════════════════════════════════════════════╗
# ║  TWO HAND EDITS, AND THIS FRAGMENT IS WRONG WITHOUT BOTH.             ║
# ║  Neither is derivable from the file, so neither can be spliced        ║
# ║  mechanically. `arm-lever`, `meter-compare` and `cover-triangle`      ║
# ║  need none — this is the only one.                                    ║
# ╚═══════════════════════════════════════════════════════════════════════╝
#
# ── EDIT 1 · this kind takes the LESSON — and needs NO edit ─────────────
#
# ⊕ Superseded 16 Aug 2026 (MRB-228). This used to say "add it to
# `_KIND_FN_TAKES_LESSON` beside the three already there", and that set no
# longer exists: `_kinds_taking_lesson()` reads the signature, so a renderer
# whose first parameter is named `lesson` is handed the lesson.
#
# The instruction was written because leaving it out made the build die with a
# TypeError naming the kind — loud, immediate, not a silent wrong render. It
# did exactly that when `lever-steps` first spliced in. Loud is not the same as
# unnecessary: name the parameter `lesson` and there is nothing to remember.
#
# It has to take the lesson because the block's whole argument is that it is
# the SAME problem as the rig upstairs: it reads that instrument's own control
# defaults out of `lesson["activities"]` to render its resting state, and
# refuses to build if the rig it names is missing. A copy of "2 kg at 32 cm,
# muscle at 4 cm" here would go stale the first time anyone moved a slider in
# the payload, and nothing would say so.
#
# ── EDIT 2 · the block heading ships its braces without this ────────────
#
# Design draws this block's <h2> as the LIVE rig line — *"Your rig: 2.0 kg at
# 32 cm, muscle at 4.0 cm."* — and the shell emits the <h2> before any
# instrument renderer runs, so `r_lever_steps` cannot reach it. Add these two
# lines to `r_activity`, anywhere after `kind` is computed (~line 6372) and
# before the `if a.get("heading") and not hc:` branch (~line 6440):
#
#     # ⊕ b2-04 #s-build — this block's heading quotes the rig the student
#     # left set, so it is filled from that instrument before the shell
#     # emits the <h2>. `wireLeverSteps` repaints the same element.
#     if kind == "lever-steps":
#         a = dict(a, heading=_lever_steps_heading(lesson, a))
#
# WITHOUT IT the page ships `<h2>Your rig: {load} kg at {hand} cm, muscle at
# {ins} cm.</h2>` — which the wiring then overwrites, so it is invisible in a
# browser and permanent in the HTML a crawler reads and in every no-JS view.
#
# Filling it at BUILD TIME as well as at runtime is the whole point.
# `dict(a, …)` rather than `a["heading"] = …` so the lesson record is never
# mutated: `r_activity` runs once per page, but the record is shared with
# every gate that reads it afterwards.
#
# Place `r_lever_steps` and its two helpers beside `r_fifa_pick`
# (build_ks3.py ~3888), which is the component it is closest to. Needs `e`,
# `t`, `rich`, and `_lever_num` / `_lever_decimals` from the `arm-lever`
# fragment — splice that one first.


def _lever_steps_rig(lesson, a, act_id):
    """The `arm-lever` this block mirrors, and the substitutions it implies.

    Returns `(subs, fill)`. Separated from the renderer because the block's
    own <h2> is emitted by the shell and has to be filled from the same three
    values through the same formatter — two copies of "how many decimal
    places does 0.04 get" is two answers to it.
    """
    rig_id = a.get("rig")
    rig = next((x for x in (lesson.get("activities") or [])
                if x.get("id") == rig_id), None)
    if rig is None:
        raise ValueError(
            "lever-steps %r reads rig %r and the lesson declares no activity "
            "with that id. The block's whole claim is that it is the same "
            "problem as the bench upstairs." % (act_id, rig_id))
    if rig.get("kind") != "arm-lever":
        raise ValueError(
            "lever-steps %r names rig %r, which is a %r. Only `arm-lever` "
            "carries the load, the two distances and g that every template "
            "here interpolates." % (act_id, rig_id, rig.get("kind")))

    controls = {c["key"]: c for c in (rig.get("controls") or [])}
    missing = [k for k in ("load", "ins", "hand") if k not in controls]
    if missing:
        raise ValueError(
            "lever-steps %r reads rig %r, which has no %s control. Every "
            "template in this block interpolates all three."
            % (act_id, rig_id, ", ".join(missing)))
    dp = {k: (0 if controls[k].get("options")
              else _lever_decimals(controls[k].get("step")))
          for k in ("load", "ins", "hand")}
    start = {k: float(controls[k]["start"]) for k in ("load", "ins", "hand")}
    g = float(rig.get("g") or 0)

    W = start["load"] * g
    dM, dL = start["ins"] / 100.0, start["hand"] / 100.0
    # ⚠️ Two decimal places on the distances and on the turning effect, and
    # NONE on the weight or the force. That is Design's own arithmetic and it
    # is not tidiness: `0.04` and `0.32` are the metre conversions a student
    # writes down, and `6.40` is what `20 × 0.32` gives on a calculator. A
    # weight and a force are whole newtons on this page.
    subs = {
        "{load}": _lever_num(start["load"], dp["load"], "{n}"),
        "{ins}": _lever_num(start["ins"], dp["ins"], "{n}"),
        "{hand}": _lever_num(start["hand"], dp["hand"], "{n}"),
        "{W}": "%.0f" % W,
        "{dM}": "%.2f" % dM,
        "{dL}": "%.2f" % dL,
        "{TE}": "%.2f" % (W * dL),
        "{F}": "%.0f" % (W * dL / dM),
        "{ratio}": "%.1f" % (start["hand"] / start["ins"]),
    }

    def fill(s):
        out = s or ""
        for k, v in subs.items():
            out = out.replace(k, v)
        return out

    return subs, fill
def _pctnum(v):
    """A percentage as short a decimal as says the same thing."""
    s = "%.4f" % float(v)
    s = s.rstrip("0").rstrip(".")
    return s or "0"
# renderers: ═══ END B5 ═══

# renderers: ═══ BEGIN B7 ═══
#
# ── B7 · Photosynthesis (⊕ MRB-245) ──
#
# Four instruments, and ALL FOUR ON INK. Measured off Design's own markup on
# all four pages — `ks3-block ks3-dark ks3-practical`, no exceptions — which is
# what `ks3_data/b7/__init__.py::_INSTRUMENT_SEGMENTS` records and what every
# colour rule under `/* ═══ BEGIN B7 ═══ */` in `shared/ks3.css` is scoped for.
#
# NOTHING IN THIS UNIT ANIMATES, uses a timer, or draws to a canvas — NOTES-B7
# §3 says it of the unit and all four pages bear it out. So there is no rAF tick
# here to consult `prefers-reduced-motion` inside (MRB-220 R4), and, by the same
# decision as B5, not one `transition` or `@keyframes` is added by this section.
# Design's pages animate one thing, `[data-arrive]` on a panel the runtime is
# already unhiding; adopting it would create a reduced-motion obligation in
# order to interpolate the arrival of a panel that was not there before.
#
# ⚠️ EVERY CONTROL IS SERVER-RENDERED, and on `#s-tuner` that is load-bearing
# rather than tidy. `ks3_parity.check_rail_reachable()` searches the built
# page's STATIC html for one of five literal signals, and Design builds all four
# benches' controls in JavaScript (`let cls = 'ks3-option'`), which does not
# match `class="ks3-option`. A bench whose whole UI arrives at runtime has a
# rail stop that can never tick and cannot be seen to be broken by anything
# except a browser. So the dials, the steps and the food tabs are drawn here, in
# HTML, inside `<ul class="ks3-options">` — which also puts them under the
# existing `.ks3-dark .ks3-option` tone rules, where an ink-dark bench belongs.
#
# ⚠️ AND NO TEXT RULE IN THIS UNIT IS WRITTEN BARE. `.ks3-dark p` is (0,1,1) and
# a bare component class is (0,1,0), so an unscoped `color` LOSES and the text
# ships present, correct and invisible. Ten builds have now paid for that.
# `ks3_parity.check_dark_text_specificity()` resolves the real cascade winner on
# every element on every ink ground and fails when a generic `.ks3-dark <type>`
# rule beats a component's own colour, so the trap is a red build rather than a
# thing to remember — but the rules are still written at (0,2,0), because a
# gate that fires is not the same as a defect that never happened.


def _need(a, act_id, keys, why=""):
    """Every one of `keys` is authored, or the build stops here."""
    for k in keys:
        if not a.get(k):
            raise ValueError(
                "%s %r declares no %r.%s"
                % (a.get("kind") or "?", act_id, k, (" " + why) if why else ""))
def _dials(a, act_id, factors):
    """`dials[]`, validated. `factors` are the numeric keys every option carries.

    A dial with one setting is a label, and a factor missing from one option is
    a readout that silently reads `NaN%` for exactly one combination — which is
    the shape of defect a browser finds and a grep does not.
    """
    dials = a.get("dials") or []
    if len(dials) < 2:
        raise ValueError(
            "%s %r declares %d dial(s). The whole argument of these benches is "
            "that the readouts move against each other, which needs more than "
            "one thing to move." % (a.get("kind") or "?", act_id, len(dials)))
    seen = set()
    for d in dials:
        if not (d.get("id") and d.get("name")):
            raise ValueError("%s %r dial %r needs `id` and `name`."
                             % (a.get("kind") or "?", act_id, d.get("id")))
        if d["id"] in seen:
            raise ValueError("%s %r declares dial id %r twice."
                             % (a.get("kind") or "?", act_id, d["id"]))
        seen.add(d["id"])
        opts = d.get("options") or []
        if len(opts) < 2:
            raise ValueError(
                "%s %r dial %r offers %d setting(s). A dial that cannot be "
                "changed is a caption."
                % (a.get("kind") or "?", act_id, d["id"], len(opts)))
        oseen = set()
        for o in opts:
            if not (o.get("id") and o.get("label")):
                raise ValueError(
                    "%s %r dial %r has an option missing `id` or `label`."
                    % (a.get("kind") or "?", act_id, d["id"]))
            if o["id"] in oseen:
                raise ValueError(
                    "%s %r dial %r declares option id %r twice."
                    % (a.get("kind") or "?", act_id, d["id"], o["id"]))
            oseen.add(o["id"])
            for f in factors:
                if f not in o:
                    raise ValueError(
                        "%s %r dial %r option %r declares no %r. Every option "
                        "carries every factor, or one combination of the dials "
                        "computes a readout out of nothing."
                        % (a.get("kind") or "?", act_id, d["id"], o["id"], f))
    return dials
def _verdict_ids(a, act_id, expected, what):
    """`verdicts` names exactly `expected`, both ways.

    Both directions fail differently and are reported differently. A MISSING
    branch is a state the bench can reach with nothing to say; a SPARE one is
    authored copy — lifted from Design's page, under R5 — that no student can
    ever reach.
    """
    verdicts = a.get("verdicts") or {}
    missing = [k for k in expected if k not in verdicts]
    if missing:
        raise ValueError(
            "%s %r has no verdict for %s. %s"
            % (a.get("kind") or "?", act_id, ", ".join(map(repr, missing)), what))
    spare = sorted(set(verdicts) - set(expected))
    if spare:
        raise ValueError(
            "%s %r declares verdict(s) %s that the bench can never reach. "
            "Design's copy is lifted byte-identical, so an unreachable branch "
            "is a paragraph of hers that no student will read."
            % (a.get("kind") or "?", act_id, ", ".join(map(repr, spare))))
    return verdicts
def _dial_block(ns, act_id, dials, chosen, extra):
    """The dials, as static server-rendered options. See the section note.

    `extra` is called per (dial, option) and returns the numeric data
    attributes that option contributes — `data-f` on the remover, `data-r` and
    `data-w` on the tuner. The numbers live on the buttons rather than in a
    JSON blob because the button IS the thing that carries them, and a student
    reading the DOM sees the model rather than a payload.
    """
    return ('<div class="ks3-%s-dials">%s</div>'
            % (ns, "".join(
                '<div class="ks3-%s-dial">'
                '<p class="ks3-%s-dialname" id="%s-%s-name" '
                'data-dial="%s">%s</p>'
                '<ul class="ks3-options ks3-%s-opts" role="list" '
                'aria-labelledby="%s-%s-name">%s</ul></div>'
                % (ns, ns, e(act_id), e(d["id"]), e(d["id"]), t(d["name"]), ns,
                   e(act_id), e(d["id"]), "".join(
                       '<li><button type="button" class="ks3-option ks3-%s-opt" '
                       'data-dial="%s" data-opt="%s"%s aria-pressed="%s">'
                       '<span class="ks3-opt-label">%s</span></button></li>'
                       % (ns, e(d["id"]), e(o["id"]), extra(d, o),
                          "true" if chosen.get(d["id"]) == o["id"] else "false",
                          t(o["label"]))
                       for o in d["options"]))
                for d in dials)))
def _with_suffix(value, suffix):
    """A number and its unit, joined the way the unit is written.

    Design writes `100% of maximum` and `40 per minute` from the same code
    path: a suffix that opens with a symbol is set tight against the number and
    a suffix that opens with a word takes a space. Getting this wrong reads as
    a typo in a readout the student is asked to watch move.
    """
    s = str(suffix or "")
    return "%s%s%s" % (value, "" if (s[:1] and not s[:1].isalnum()) else " ", s)
# renderers: ═══ END B7 ═══


# renderers: ═══ BEGIN B8 ═══
#
# ── B8 · Respiration (⊕ MRB-248) ──
#
# Five instruments, all DOM-only, all on ink. No canvas, no rAF, no timer
# anywhere in the unit — grepped across all five approved pages and zero on
# every term, and the runtime section in `shared/ks3.js` keeps it that way.
#
# ⚠️ ALL FIVE SHIP ON `ks3-block ks3-dark ks3-practical`, measured off Design's
# own `#s-bench` markup on all five pages character for character. `.ks3-dark p`
# is (0,1,1) and a bare component class is (0,1,0), so every colour rule in the
# B8 stylesheet is written under `.ks3-dark …` at (0,2,0). Since MRB-245 that is
# gated as well as written, but the gate firing is not the same as the defect
# never happening.


def _js_round(x):
    """`Math.round` — half away from zero at .5, which Python's `round` is not.

    Design's benches are ported arithmetic and the port has to agree with the
    approved page at every printed value. `round(0.5)` is 0 in Python and 1 in
    JavaScript, so a shared helper is the only way the static render and the
    runtime can be guaranteed to print the same number.
    """
    return int(math.floor(float(x) + 0.5))
def _group_digits(n, on):
    """`1404` → `1,404`, when the payload asked for it.

    ⚠️ `toLocaleString()` IS NOT A FORMATTING RULE, and Design writes exactly
    that. It is the BROWSER's locale, not ours, so a student whose machine is
    set to a European locale reads `1.404 kJ` — one thousand four hundred and
    four printed as if it were one point four. The grouping is authored
    explicitly and applied here so the page cannot say something different in
    different countries.
    """
    return ("{:,}".format(int(n)) if on else str(int(n)))
def _attr_safe(value, act_id, where):
    """A string bound for a `data-` attribute the RUNTIME writes as text.

    ⚠️ THE DRAWN MARKS SURVIVE `t()` AND DIE IN AN ATTRIBUTE, and the difference
    is invisible to a grep. → ✓ ✕ are absent from all five of Design's latin
    subsets, so they are never typed: `t()` swaps each for a drawn `<svg>` and
    the page gets a real glyph. An attribute goes through `e()` instead, which
    escapes and does not substitute — so the codepoint survives into
    `data-note="… glucose → ethanol …"`, and the instant JS assigns it to
    `textContent` the browser has to render a character no shipped font
    contains. Tofu, or a mid-word fall through to a system font, in the middle
    of a reaction equation.

    Static markup is the fix and is what these five instruments use wherever a
    reaction line appears — every fermenter branch is drawn in full and hidden,
    rather than being written in by the runtime. This guards the remaining
    attribute paths so the next author to put an arrow in a note discovers it
    at build time rather than a student discovering it on the page.

    ⚑ Nothing is shipping broken today: B1, B7 and C1 all type U+2192 in their
    records and all of them reach the page through `t()`. This is a fence
    around the one route that would not.
    """
    s = str(value or "")
    bad = [ch for ch, _ in MARKS if ch in s]
    if bad:
        raise ValueError(
            "%s: %s carries %s, which is a DRAWN mark and not a typed glyph — "
            "no shipped font subset contains it. This string reaches the page "
            "through a data attribute that the runtime writes as text, so `t()` "
            "never sees it and the student gets tofu. Say it in words, or move "
            "the string into static markup where `t()` can draw it."
            % (act_id, where,
               " and ".join("U+%04X" % ord(ch) for ch in bad)))
    return s
def _placeholders(value, act_id, where, required, forbidden=()):
    """A composed string, checked for the braces it must and must not carry.

    ⚠️ AN UNFILLED `{ppm}` IS INVISIBLE TO EVERY OTHER GATE. The build renders
    it, the specificity gate resolves its colour, the rail ticks — and a
    student reads a brace. B7's `b7-chain-traced` drive fails a build for
    exactly this, having found it in a browser; this catches the same defect at
    the source, where the message can say which key is wrong.
    """
    s = str(value or "")
    for token in required:
        if token not in s:
            raise ValueError(
                "%s: %s names no %s. That number is computed from the bench's "
                "own state and cannot be authored as a literal — a verdict "
                "that quotes a fixed figure is a verdict that is wrong on "
                "every setting but one." % (act_id, where, token))
    for token in forbidden:
        if token in s:
            raise ValueError(
                "%s: %s names %s, and nothing fills it here. This branch is "
                "the one that quotes no number — it is the CONTROL, and its "
                "whole point is that there is no figure to report."
                % (act_id, where, token))
    return s
def _json_attr(obj):
    """A payload map for a `data-` attribute, stable across builds."""
    return e(json.dumps(obj, separators=(",", ":"), sort_keys=True))
# renderers: ═══ END B9 ═══


# renderers: ═══ BEGIN B10 ═══
#
# ── B10 · Inheritance and DNA (⊕ MRB-248) ──
#
# Five instruments, one per lesson. All five are DOM-only: `canvas`,
# `requestAnimationFrame`, `setTimeout` and `setInterval` appear ZERO times
# across all five of Design's delivered pages (schema §0.1), and
# `shared/ks3.js` keeps it that way. The only motion in the unit is CSS — a
# height/width transition on `[data-fill]` — and the platform's R6 rule
# (`*,*::before,*::after { transition-duration:.001ms !important }`) already
# neutralises it under `prefers-reduced-motion`, so there is no tick in this
# unit that would have to test the query inside itself (contract R4, the
# b2-03 slip).
#
# ⚠️ ALL FIVE SHIP ON `ks3-block ks3-dark ks3-practical`, measured off
# Design's own `#s-bench` class attribute on all five pages (b10-01 L105,
# b10-02 L105, b10-03 L105, b10-04 L105, b10-05 L105). Under
# `ACTIVITY_SHELLS` that string is `segment: "practical"`. `.ks3-dark p` is
# (0,1,1) and a bare component class is (0,1,0), so every colour rule in the
# B10 stylesheet is written under `.ks3-dark …` at (0,2,0) and every one of
# them is resolved by `ks3_parity.check_dark_text_specificity()` on the real
# cascade.
#
# ⚖️ THREE OF THE FIVE BENCHES ADJUDICATE A STUDENT COMMITMENT, and that is a
# DELIBERATE DEPARTURE FROM B7 §0.6 recorded in schema §0.6 rather than a
# drift. b10-01 prints `Your prediction was right` / `Not what you predicted`,
# b10-03 prints `rules this model out` against a failing evidence card, and
# b10-05 prints `That is the answer` / `Not quite`. Measured off Design's own
# pages, soft in every case, and confronting the IDEA rather than the student.
# ⛔ THE VERDICT IS WORDS AND ONLY WORDS. No green, no red, no badge, no mark
# on an option button, and never the amber `is-wrong` ladder treatment. Only
# the mastery ladder marks correctness (MRB-196 R10).
#
# ⚠️ AND EACH BENCH'S MARKER IS READ TWICE (MRB-249). The band section beside
# it — `s-two`, `s-model`, `s-who`, `s-steps`, `s-test` — carries no control of
# its own, so its rail entry MIRRORS `s-bench` and ticks the moment this
# marker flips. Design states each threshold in her own `isDone()` and schema
# §8 records all five: b10-01 three plotted · b10-02 all six levels shown ·
# b10-03 solved · b10-04 twenty seeds · b10-05 five cases opened. A threshold
# moved for convenience here moves TWO stops, not one, which is why each of
# the five renderers below refuses a payload that cannot reach its own.


def _progress_suffix(a, kind):
    """`progress_suffix`, validated where the head row is composed from it.

    ⚠️ THE HEAD ROW IS BUILT BEFORE THE INSTRUMENT RUNS, so a missing suffix
    would otherwise reach the page as "3 of 6 " with the sentence cut off, and
    the renderer's own message — which knows what the word is FOR — never gets
    to complain. One message per mistake, raised at the first point that can
    see it. Same reasoning as `_b9_head`.
    """
    sfx = a.get("progress_suffix")
    if not sfx:
        raise ValueError(
            "%s declares no `progress_suffix`. Design's head row reads "
            "'{n} of {total} <word>' and the word is the only authored part "
            "of it; without one the block ships a counter with its sentence "
            "cut off mid-air." % kind)
    return _attr_safe(sfx, a.get("id") or "?", "`progress_suffix`")
# Runs to twelve because the browse layer counts lessons in a card, not just
# ladder rungs (which never exceed four), and because the sorter says "All eight
# sorted" (Design's own string). `_count_word` already falls back to digits above
# the tuple, so lengthening it changes no existing output. Spelling numbers stays
# in ONE place: `r_sort_rows` emits the word alongside the count so
# `shared/ks3.js` never has to carry a second, drifting copy of this table.
NUMBER_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve")
def _count_word(n):
    return NUMBER_WORDS[n] if n < len(NUMBER_WORDS) else str(n)
