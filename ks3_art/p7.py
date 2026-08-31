"""ks3_art.p7 — P7 *Light*, the unit where a wave crosses nothing at all.

Every instrument here is authored against Claude Design's delivered pages
in `docs/ks3/design-reference/p7/`. Her page wins outright: a shape that
is not in her drawing is not in this module, and where her NOTES and her
drawing disagree the DRAWING IS MEASURED and the note is reported.

── ⚖️ MRB-204 · ONE TRIANGLE AND ONE BEAM IN SEVEN LESSONS ───────────

    p7-01  d = c × t                            a PRODUCT   TRIANGLE
    p7-02  r = i                                an EQUALITY BEAM, no covers
    p7-03  no block — statute is qualitative
    p7-04  no block — her FLAG 4, and it is Mide's call
    p7-05  no block — a system lesson
    p7-06  no block — statute says "qualitative only" in terms
    p7-07  no block — a contrast

⚖️ **THE BEAM CARRIES NO COVER BUTTONS.** Covering one side of an
equality asks a question whose answer is written on the other side. That
is the `p1-08` ruling and Design drew `p7-02` that way before anyone
asked.

── ⊕ NO INSTRUMENT HERE DRAWS ITS OWN HEAD ROW ───────────────────────

P4, P5 and P6 each author `eyebrow` / `heading` / `progress` on the
activity AND draw a second head inside the instrument, so every bench in
those three units ships its eyebrow and its `<h2>` twice. Measured in the
built bytes, not inferred.

`r_activity`'s `.ks3-blockhead` IS Design's row — eyebrow and heading on
the left, a right-aligned mono readout on the right — and MRB-220 built
the head counter for exactly this. So every P7 bench authors
`head_counter` with Design's own two states, the drawers below start at
the commit gate, and the wiring drives the shared `[data-count]` element
through `setCount`. One eyebrow, one heading, one readout.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with
no opt-out. Nothing here uses any of the four. The band block's shapes
are `table`, `straw`, `pair` and `spectrum` for that reason.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────

`ks3_art.load()` asserts it since MRB-279. Checked before these were
written: none of `ks3-lrace-`, `ks3-rsurf-`, `ks3-rblock-`, `ks3-pinh-`,
`ks3-eyecam-`, `ks3-prism-`, `ks3-clamp-`, `ks3-lband-` or `ks3-p7cfa-`
was taken. ⚠️ `ks3-cbench-` WAS taken (C7's), which is why the colour
bench is `clamp` and not `cbench`.

── ⚠️ HUE IS NEVER THE ONLY CHANNEL ──────────────────────────────────

`p7-06` and `p7-07` use colour as part of the message, because colour is
the subject. Every state therefore also prints the colour AS A WORD in a
readout tile, in the caption and in the note, and where nothing comes
back the ray is drawn DASHED as well as being called *nothing comes
back*. Her FLAG 10, honoured.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ═══ shared P7 primitives ════════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P7 bench opens behind."""
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "%s %r has no commit gate. A bench read before a commitment "
            "confirms whatever the student already believed."
            % (family, act_id))
    opts = "".join(
        '<li><button type="button" class="ks3-option" data-%s-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button></li>'
        % (hook, i, chr(65 + i), t(o))
        for i, o in enumerate(gate["options"]))
    return ('<div class="ks3-%s-gate" data-%s-gate><p class="ks3-commit">%s'
            '</p><ul class="ks3-options">%s</ul></div>'
            % (hook, hook, t(gate["prompt"]), opts))


def _tiles(hook, specs, act_id, family):
    """Design's readout row. A tile with a `sub` gets a live sub-line."""
    if len(specs) < 3:
        raise ValueError(
            "%s %r declares %d readout tile(s). Design's row is four on "
            "every P7 bench, and the fourth is always the verdict — the one "
            "that says in WORDS what the drawing has just said in geometry."
            % (family, act_id, len(specs)))
    cells = ""
    for s in specs:
        sub = ('<p class="ks3-%s-tile-sub" data-%s-sub="%s">%s</p>'
               % (hook, hook, e(s["id"]), t(s.get("sub", "")))
               ) if s.get("sub") else ""
        cells += ('<div class="ks3-%s-tile">'
                  '<p class="ks3-%s-tile-label">%s</p>'
                  '<p class="ks3-%s-tile-value" data-%s-out="%s">%s</p>%s'
                  '</div>'
                  % (hook, hook, t(s["label"]), hook, hook, e(s["id"]),
                     t(s.get("value", "—")), sub))
    return '<div class="ks3-%s-tiles">%s</div>' % (hook, cells)


def _slider(act_id, hook, spec, key=""):
    k = key or "v"
    for f in ("min", "max", "step", "start", "label"):
        if f not in spec:
            raise ValueError("%s slider %r has no %r." % (act_id, k, f))
    return ('<div class="ks3-%s-row"><div class="ks3-%s-rowhead">'
            '<label for="%s-%s">%s</label>'
            '<p class="ks3-%s-reading" data-%s-out="%s">%s</p></div>'
            '<input class="ks3-%s-slider" type="range" id="%s-%s" '
            'min="%s" max="%s" step="%s" value="%s" data-%s-slider="%s">'
            '</div>'
            % (hook, hook, e(act_id), e(k), t(spec["label"]),
               hook, hook, e(k), t(spec.get("value", "—")),
               hook, e(act_id), e(k), e(spec["min"]), e(spec["max"]),
               e(spec["step"]), e(spec["start"]), hook, e(k)))


# ⚠️ THE POSITIONED ANCESTOR IS THE INNER DIV, NOT THE PANEL.
#
# Every live value on a P7 bench is an absolutely positioned HTML span over
# the SVG, and its `left`/`top` are PERCENTAGES OF DESIGN'S OWN viewBox. Her
# markup nests them one level deeper than the panel — a padded
# `background: var(--ks3-dark-panel)` card, and inside it a bare
# `position: relative` div holding the SVG and the spans — so her
# percentages resolve against the DRAWING.
#
# The first cut here made the padded panel itself the positioned ancestor,
# which resolves them against the panel INCLUDING its 18px of padding.
# Every label on all seven benches therefore sat about 18px left and 18px
# high of where she put it, and on `p7-07` that slid "White light" under the
# lamp so the page read "hite light". Found by cropping the figure and
# looking at it, not by a gate: the spans were present, filled, correctly
# coloured and in front — every assertion a sweep makes was true.
#
# So the SVG and the spans go in an inner div and the padding stays on the
# outer one. `.ks3-<hook>-figinner` is the positioning context; the panel
# keeps `position: relative` as well, which is harmless because the nearest
# positioned ancestor is what governs, and which keeps the §5A rule about
# absolutely positioned children of a scroller true of both elements.


def _picker(hook, label, tabs):
    return ('<div class="ks3-%s-picker"><p class="ks3-%s-pickerlabel">%s</p>'
            '<div class="ks3-%s-tabrow">%s</div></div>'
            % (hook, hook, t(label), hook, tabs))


# ── ⊕ MRB-297 · P7-04 · ONE ARROWHEAD, AND IT IS DESIGN'S OWN ─────────
#
# **A line with no arrow is not a ray.** Not one light ray in this unit
# carried a direction, and three of the drawings therefore read as the
# negation of the lesson beside them: the reflection bench is mirror-
# symmetric about the normal, so nothing said which line was the incident
# one; the refraction block read right-to-left shows light bending AWAY
# from the normal on entering glass; and the eye bench and the straw figure
# both drew an undirected line between a scene and an eye, on the two pages
# whose registered misconception is `LIGHT-17`, *your eyes send something
# out in order to see*.
#
# ⚖️ **THE SHAPE IS NOT NEW.** It is the head Design already draws on
# `p7-01`'s two race lanes — `M900 46 L882 36 M900 46 L882 56` for the
# light and the same eighteen-by-ten open V composed in `shared/ks3.js`
# for the sound — and the same head again on her `p7-04` object arrow
# (`l-11 18`), her `p7-05` scene arrow and her `p7-06` band arrows. An
# open V, 18 long and 10 either side, in a 1000-wide viewBox. Every P7
# viewBox except the lens pair's is 1000 wide, so ONE size is consistent
# across the unit and the head is therefore `markerUnits="userSpaceOnUse"`:
# it must NOT scale with the shaft, or `p7-07`'s 11-wide ray would carry a
# head twice the size of `p7-05`'s 4-wide one.
#
# ⚠️ **NOT ON CONSTRUCTION LINES.** Normals, the refraction block's ghost,
# the prism's ghost and the straw's back-projection are lines a student
# DRAWS, not paths light TAKES, and the whole value of the arrowhead is
# that the difference reads. They stay headless, deliberately, and the
# list is in the report.
#
# ⚠️ **THE DEFINITION IS INERT OUTSIDE P7.** The marker is emitted into
# each of this module's own `<svg>` elements with an id of its own hook, so
# no other unit's bytes can move: nothing outside `ks3_art/p7.py` names
# `ks3-rayhead-`, and `shared/ks3.css` is not touched. Turning arrowheads
# on for biology, chemistry or the other physics units is a wider change
# than a physics S1 fix and wants its own verification pass.
#
# ⚠️ **`context-stroke` WITH A LITERAL FALLBACK, IN THAT ORDER.** The head
# has to take the colour of the ray it sits on — `p7-06` draws six colours
# and `p7-07` recolours its ray at paint time from the lamp — and only
# `context-stroke` can read it. A browser that does not know the keyword
# drops that declaration and keeps the one before it, so the head is the
# instrument's base colour rather than invisible.

P7_HEAD_LEN, P7_HEAD_HALF = 18, 10


def _rayhead(hook, width, fallback):
    """The `<defs>` block for one instrument's ray arrowhead.

    `width` is the stroke width of the rays it will sit on, so the head is
    drawn at the weight of its own shaft; `fallback` is that instrument's
    base ray colour, used only where `context-stroke` is unsupported.

    ⚠️ The SIZE is `P7_HEAD_LEN` × `P7_HEAD_HALF` for every instrument and
    does NOT follow the width. That is Design's own practice here — the
    same 18×10 head sits on her 8-wide race lane, her 8-wide object arrow
    and her 4-wide band arrow — and it is what keeps `p7-07`'s 11-wide ray
    and `p7-05`'s 4-wide ray wearing the same mark.
    """
    ln, half, pad = P7_HEAD_LEN, P7_HEAD_HALF, width
    tipx, tipy = ln + pad, half + pad
    return (
        '<defs><marker id="ks3-rayhead-%s" markerUnits="userSpaceOnUse" '
        'markerWidth="%s" markerHeight="%s" refX="%s" refY="%s" '
        'orient="auto" overflow="visible">'
        '<path d="M%s %s L%s %s M%s %s L%s %s" fill="none" '
        'stroke-linecap="round" stroke-linejoin="round" stroke-width="%s" '
        'style="stroke:%s;stroke:context-stroke"/></marker></defs>'
        % (hook, _n(tipx + pad), _n(tipy + half + pad),
           _n(tipx), _n(tipy),
           _n(tipx), _n(tipy), _n(pad), _n(pad),
           _n(tipx), _n(tipy), _n(pad), _n(tipy + half),
           _n(width), fallback))


def _head(hook, *where):
    """`marker-end` (and friends) as presentation ATTRIBUTES.

    ⚠️ Attributes, never `style`: `shared/ks3.js` overwrites the `style` of
    `[data-clamp-in]`, `[data-clamp-back]`, `[data-prism-beam]`,
    `[data-prism-inner]` and `[data-prism-outbeam]` on every paint, and a
    marker declared there would be wiped at the first click.
    """
    return "".join(' marker-%s="url(#ks3-rayhead-%s)"' % (w, hook)
                   for w in (where or ("end",)))


def _sibling(a):
    """`data-sibling` — the band stop this bench ticks, at its own count.

    Five P7 pages have one, and on all five Design's own `DONE` gives the
    band section the GATE alone while the bench needs the gate AND a
    control touched: `p7-03`'s `s-inout`, `p7-04`'s `s-lens`, `p7-05`'s
    `s-parts`, `p7-06`'s `s-band`, `p7-07`'s `s-grid`. Same shape as P4's
    and P6's, and `mirrors` is not used because it would tick them LATE
    and because the manifest derives no mirror here — her two expressions
    genuinely differ.
    """
    # ⚠️ A NEAR-MISS KEY IS AN ERROR, NOT A SILENT NOTHING. P6 shipped two
    # dead rail stops by writing `sibling` / `sibling_at`; the drawer read
    # `band_anchor` / `band_at`, found neither and returned "". MRB-208's
    # gate cannot catch it — a band section carries `data-stage-done="0"`,
    # which IS one of the signals `doneByDom()` reads, so the stop looks
    # reachable and simply never becomes true.
    for wrong in ("sibling", "sibling_at", "band", "mirror", "mirrors"):
        if wrong in a:
            raise ValueError(
                "%r carries %r. The keys this drawer reads are `band_anchor` "
                "and `band_at`, and a near-miss is silently ignored — which "
                "ships a rail stop that can never tick and that MRB-208's "
                "gate reads as reachable." % (a.get("id"), wrong))
    sib = a.get("band_anchor")
    if not sib:
        return ""
    at = a.get("band_at")
    if not isinstance(at, int) or at < 1:
        raise ValueError(
            "%r names a band sibling %r with no `band_at` count."
            % (a.get("id"), sib))
    return ' data-sibling="%s" data-sibling-at="%d"' % (e(sib), at)


def _unique(rows, act_id, family, what, key="id"):
    seen, dupes = set(), []
    for r in rows:
        rid = r.get(key)
        if rid in seen:
            dupes.append(rid)
        seen.add(rid)
    if dupes:
        raise ValueError(
            "%s %r has two %ss with %s %s. The second is unreachable and the "
            "failure is silent."
            % (family, act_id, what, key, sorted(set(dupes))))


def _branches(hook, branches, need, act_id, family):
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "%s %r has no note for state(s) %s. Every reachable state has "
            "something true to say, and a state with no note ships a blank "
            "paragraph where the teaching goes."
            % (family, act_id, ", ".join(missing)))
    return "".join(
        '<span data-%s-branch="%s" data-note="%s" hidden></span>'
        % (hook, e(k), e(branches[k])) for k in need)


def _no_head(a, act_id, family):
    """Every P7 bench takes the SHELL's head row. See the module note.

    ⚠️ A bench that authors `progress` instead of `head_counter` gets
    `r_activity`'s string branch, which is a COUNT format with no zero
    state — so the resting page would read Design's "both controls live"
    before a control had been touched. Her readout has two states and the
    counter's `zero` is what carries the first one.
    """
    if a.get("progress"):
        raise ValueError(
            "%s %r authors `progress`. P7 benches take Design's TWO-STATE "
            "readout through `head_counter` (`format` + `zero`), because "
            "her resting row says \"Change a control to begin\" and her live "
            "one says \"Both controls live\" — a bare format string would "
            "ship the live sentence on a page nobody had touched."
            % (family, act_id))
    hc = a.get("head_counter") or {}
    if not hc.get("format") or not hc.get("zero"):
        raise ValueError(
            "%s %r has no two-state `head_counter`. Design's head row is a "
            "live readout and the shell draws it; without `format` and "
            "`zero` the block ships a head row that never changes."
            % (family, act_id))


# ═══ p7-01 · #s-race · a flash and a bang, set off together ══════════════

def r_two_speed_race(a, act_id):
    """⊕ p7-01 `#s-race` — one start, two messengers, a log distance axis.

    ⚖️ **A DECADE AXIS, AND THE DRAWING SAYS SO ON ITS FACE.** The gap
    runs 1 m to 100 km and the two travel times are about a million times
    apart; a ruler scale would put every interesting distance in the first
    pixel. Design's own foot line — *"EACH MARK IS TEN TIMES THE ONE
    BEFORE IT"* — is drawn rather than assumed.

    ⚖️ **THE VACUUM CHANGES THE SOUND READING AND NOT THE LIGHT ONE.**
    That is the whole lesson in two tiles: take the air away and the bang
    stops arriving at all — not faintly, not late — while the light time
    does not move by a digit. The sound arrow stops short AND goes dashed,
    so the drawing carries it on two channels.

    ⚠️ **THE LIGHT TIME IS NEVER ROUNDED TO ZERO.** Design's `fmtT` steps
    down through seconds, milliseconds, millionths and billionths rather
    than printing `0.00 s`, because "no time at all" is `LIGHT-01` exactly.

    HOOKS: `data-lrace` (wrapper, `data-c`, `data-v-sound`,
    `data-decades`) · `data-lrace-gate` · `data-lrace-gopt` ·
    `data-lrace-body` · `data-lrace-med` · `data-lrace-slider` ·
    `data-lrace-mark` · `data-lrace-sound` · `data-lrace-fill` ·
    `data-lrace-out` · `data-lrace-note`.
    """
    _no_head(a, act_id, "two-speed-race")
    media = a.get("media") or []
    if len(media) != 2:
        raise ValueError(
            "two-speed-race %r declares %d medium(s). The lesson is air "
            "against a vacuum, and one of them on its own makes no "
            "comparison." % (act_id, len(media)))
    _unique(media, act_id, "two-speed-race", "medium")
    if not any(m.get("vacuum") for m in media):
        raise ValueError(
            "two-speed-race %r has no vacuum in the deck. It is the state "
            "the lesson is named after and the one the commit gate asks "
            "about." % act_id)
    for m in media:
        for f in ("caption", "sound_sub", "label"):
            if not m.get(f):
                raise ValueError(
                    "two-speed-race %r medium %r has no %r."
                    % (act_id, m.get("id"), f))

    labels = a.get("decade_labels") or []
    decades = int(a.get("decades") or 5)
    if len(labels) != decades + 1:
        raise ValueError(
            "two-speed-race %r spans %d decade(s) and labels %d mark(s). "
            "Every mark on a decade axis is labelled, or the axis is a line "
            "with no scale on it." % (act_id, decades, len(labels)))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-lrace-med", m["label"],
             pressed=(i == 0), data_lrace_med=m["id"],
             data_vacuum="1" if m.get("vacuum") else "0",
             data_caption=m["caption"], data_sound_sub=m["sound_sub"],
             data_name=m["label"])
        for i, m in enumerate(media))

    # Design's own 1000×322 viewBox. The decade labels are LITERAL text —
    # they never change — and only the marker and the sound arrow move.
    X0, X1 = 60.0, 940.0
    ticks = ""
    for d in range(decades + 1):
        x = X0 + (X1 - X0) * d / float(decades)
        ticks += ('<path class="ks3-lrace-tick" d="M%.1f 236 v14"/>'
                  '<text class="ks3-lrace-ticklabel" x="%.1f" y="276" '
                  'text-anchor="middle">%s</text>'
                  % (x, x, t(labels[d])))

    svg = (
        '<svg class="ks3-lrace-svg" viewBox="0 0 1000 322" role="img" '
        'aria-label="" data-lrace-alt>'
        '<path class="ks3-lrace-axis" d="M60 236 H940"/>%s'
        '<path class="ks3-lrace-mark" data-lrace-mark d="M0 0"/>'
        '<text class="ks3-lrace-lanelabel" x="60" y="34">%s</text>'
        '<text class="ks3-lrace-lanelabel" x="60" y="132">%s</text>'
        '<path class="ks3-lrace-light" d="M160 46 H900 M900 46 L882 36 '
        'M900 46 L882 56"/>'
        '<path class="ks3-lrace-sound" data-lrace-sound d="M0 0"/>'
        '<text class="ks3-lrace-axislabel" x="940" y="316" '
        'text-anchor="end">%s</text></svg>'
        % (ticks, t(a.get("light_label", "LIGHT")),
           t(a.get("sound_label", "SOUND")),
           t(a.get("axis_label", ""))))

    fills = "".join(
        '<span class="ks3-lrace-fill ks3-lrace-%s" data-lrace-fill="%s">'
        '</span>' % (k, k) for k in ("lt", "st", "mark"))

    branch_data = _branches("lrace", a.get("branches") or {},
                            ("air", "vacuum"), act_id, "two-speed-race")

    return ('<div class="ks3-lrace" data-lrace data-c="%s" data-v-sound="%s" '
            'data-decades="%s"%s>%s'
            '<div class="ks3-lrace-body" data-lrace-body hidden>'
            '<div class="ks3-lrace-controls">%s%s</div>'
            '<div class="ks3-lrace-figwrap">'
            '<div class="ks3-lrace-figinner">%s%s</div></div>%s'
            '<p class="ks3-lrace-note" data-lrace-note></p>%s</div></div>'
            % (e(a.get("c", 300000000)), e(a.get("v_sound", 340)),
               e(decades), _sibling(a),
               _gate(act_id, "two-speed-race", a.get("gate") or {}, "lrace"),
               _picker("lrace", a.get("med_label", "What is in between"),
                       tabs),
               _slider(act_id, "lrace", a.get("dist") or {}, "d"),
               svg, fills,
               _tiles("lrace", a.get("readouts") or [], act_id,
                      "two-speed-race"),
               branch_data))


# ═══ p7-02 · #s-ray · a ray box, a protractor and four surfaces ══════════

def r_ray_surface(a, act_id):
    """⊕ p7-02 `#s-ray` — one rule, four surfaces, four different results.

    ⚖️ **THE ANGLE IS THE SAME ON ALL FOUR, AND THAT IS THE POINT.** The
    readout for the angle of reflection reads the incidence angle back on
    every surface, including the two that scatter, because every one of
    the fanned rays has obeyed the law at its own facet. A bench that
    printed *"random"* for paper would be teaching `LIGHT-05`.

    ⚖️ **SPREAD AND ABSORPTION ARE TWO INDEPENDENT CONTROLS OF THE
    DRAWING**, which is what makes crumpled foil legible: it scatters like
    paper and stays as bright as a mirror, so the fan is wide and the
    strokes are full weight. Matt black card scatters the same way and the
    strokes go thin and faded. `back < 20` is the threshold.

    ⚠️ **A SURFACE WITH SPREAD 0 DRAWS ONE RAY, NOT A FAN OF ONE.** The
    mirror's single reflected ray IS the preserved arrangement; drawing it
    as a degenerate fan would say the pattern nearly survived.

    HOOKS: `data-rsurf` (wrapper) · `data-rsurf-gate` · `data-rsurf-gopt` ·
    `data-rsurf-body` · `data-rsurf-surf` · `data-rsurf-slider` ·
    `data-rsurf-surface` · `data-rsurf-in` · `data-rsurf-refrays` ·
    `data-rsurf-arcs` · `data-rsurf-fill` · `data-rsurf-out` (valued with
    a readout id) · `data-rsurf-sub` · `data-rsurf-note`.

    ⚠️ THE REFLECTED-RAY PATH IS `data-rsurf-refrays`, NOT
    `data-rsurf-out`. A bare `data-<hook>-out` sits in the SAME attribute
    namespace as the readout tiles, whose hook is `data-<hook>-out="id"`,
    so a `querySelectorAll("[data-rsurf-out]")` returns the SVG path
    alongside the four tiles and reads its text as an empty readout. Found
    by a state-space drive rather than by a gate, on three of the seven
    benches at once.
    """
    _no_head(a, act_id, "ray-surface")
    surfs = a.get("surfaces") or []
    if len(surfs) != 4:
        raise ValueError(
            "ray-surface %r declares %d surface(s). Design's deck is four, "
            "and the set is the argument: two that scatter and two that do "
            "not, crossed with two that absorb and two that do not — foil is "
            "the one that separates shiny from smooth."
            % (act_id, len(surfs)))
    _unique(surfs, act_id, "ray-surface", "surface")
    for s in surfs:
        for f in ("label", "spread", "back", "profile", "kind", "caption",
                  "note"):
            if s.get(f) is None or s.get(f) == "":
                raise ValueError(
                    "ray-surface %r surface %r has no %r."
                    % (act_id, s.get("id"), f))
        if s["profile"] not in ("flat", "wavy", "faceted"):
            raise ValueError(
                "ray-surface %r surface %r asks for profile %r. The three "
                "drawn are flat, wavy and faceted, and the profile IS the "
                "explanation for the spread."
                % (act_id, s.get("id"), s["profile"]))
    if not any(float(s["spread"]) == 0 for s in surfs):
        raise ValueError(
            "ray-surface %r has no specular surface. Without one there is "
            "nothing for the scattering surfaces to be different FROM."
            % act_id)
    if not any(float(s["back"]) < 20 for s in surfs):
        raise ValueError(
            "ray-surface %r has no strongly absorbing surface, so the "
            "thinned-and-faded drawing state is unreachable and absorption "
            "is a word on the page rather than something a student can see."
            % act_id)
    if not a.get("branch_tail"):
        raise ValueError(
            "ray-surface %r has no `branch_tail`. Every state on this bench "
            "ends by naming the live angle and the live fraction; without it "
            "a student can read four surface notes that never mention the "
            "control they moved." % act_id)

    tabs = "".join(
        _seg("ks3-seg-btn ks3-rsurf-surf", s["label"], pressed=(i == 0),
             data_rsurf_surf=s["id"], data_spread=s["spread"],
             data_back=s["back"], data_profile=s["profile"],
             data_kind=s["kind"], data_caption=s["caption"],
             data_note=s["note"], data_name=s["label"])
        for i, s in enumerate(surfs))

    # Design's own 1000×420 viewBox. The normal is a fixed dashed line at
    # the landing point; everything else is a hole.
    svg = (
        '<svg class="ks3-rsurf-svg" viewBox="0 0 1000 420" role="img" '
        'aria-label="" data-rsurf-alt>%s'
        '<path class="ks3-rsurf-surface" data-rsurf-surface d="M120 340 '
        'H880"/>'
        '<path class="ks3-rsurf-normal" d="M500 340 V60"/>'
        '<text class="ks3-rsurf-normallabel" x="510" y="52">%s</text>'
        '<path class="ks3-rsurf-in" data-rsurf-in d="M0 0"%s/>'
        '<path class="ks3-rsurf-out" data-rsurf-refrays d="M0 0"%s/>'
        '<path class="ks3-rsurf-arcs" data-rsurf-arcs d="M0 0"/></svg>'
        % (_rayhead("rsurf", 6, "var(--ks3-blue-light)"),
           t(a.get("normal_label", "NORMAL")),
           _head("rsurf"), _head("rsurf", "mid", "end")))

    fills = "".join(
        '<span class="ks3-rsurf-fill ks3-rsurf-%s" data-rsurf-fill="%s">'
        '</span>' % (k, k) for k in ("caption", "inc", "ref"))

    return ('<div class="ks3-rsurf" data-rsurf data-tail="%s"%s>%s'
            '<div class="ks3-rsurf-body" data-rsurf-body hidden>'
            '<div class="ks3-rsurf-controls">%s%s</div>'
            '<div class="ks3-rsurf-figwrap">'
            '<div class="ks3-rsurf-figinner">%s%s</div></div>%s'
            '<p class="ks3-rsurf-note" data-rsurf-note></p></div></div>'
            % (e(a["branch_tail"]), _sibling(a),
               _gate(act_id, "ray-surface", a.get("gate") or {}, "rsurf"),
               _slider(act_id, "rsurf", a.get("inc") or {}, "a"),
               _picker("rsurf", a.get("surf_label", "What it lands on"),
                       tabs),
               svg, fills,
               _tiles("rsurf", a.get("readouts") or [], act_id,
                      "ray-surface")))


# ═══ p7-03 · #s-block · a ray box and a rectangular block ════════════════

def r_refraction_block(a, act_id):
    """⊕ p7-03 `#s-block` — send one ray in, watch where it goes.

    ⚖️ **THE ZERO-ANGLE STATE IS ITS OWN BRANCH AND ITS OWN VERDICT
    WORD.** A ray along the normal slows and does not bend, which is the
    state that proves the mechanism rather than an edge case of it: the
    slowing is the same and the bending is absent, so the bending cannot
    be caused by the slowing alone. The ghost line is NOT drawn there,
    because a dashed continuation of a path the ray actually took would
    say a comparison had been made when none had.

    ⚖️ **THE ANGLE INSIDE IS COMPUTED FROM THE INDEX, NOT AUTHORED.**
    `asin(sin i / n)`, rounded to the degree, and the drawing is built
    from the same number the readout prints — so a student who measures
    the picture with a protractor gets the tile's figure.

    ⚠️ **THE RAY LEAVES THE FAR FACE AT THE ANGLE IT ARRIVED AT.** Two
    bends, equal and opposite, and the exit point moves with the angle
    inside. That is what makes the dashed original-direction line a
    comparison worth drawing.

    HOOKS: `data-rblock` (wrapper) · `data-rblock-gate` ·
    `data-rblock-gopt` · `data-rblock-body` · `data-rblock-mat` ·
    `data-rblock-slider` · `data-rblock-normal2` · `data-rblock-in` ·
    `data-rblock-mid` · `data-rblock-exit` · `data-rblock-ghost` ·
    `data-rblock-fill` · `data-rblock-out` (valued with a readout id) ·
    `data-rblock-sub` · `data-rblock-note`.
    """
    _no_head(a, act_id, "refraction-block")
    mats = a.get("materials") or []
    if len(mats) < 3:
        raise ValueError(
            "refraction-block %r declares %d material(s). The pattern being "
            "taught is slower material, bigger bend, and an order needs at "
            "least three points in it." % (act_id, len(mats)))
    _unique(mats, act_id, "refraction-block", "material")
    for m in mats:
        for f in ("label", "n", "v", "caption", "note"):
            if not m.get(f):
                raise ValueError(
                    "refraction-block %r material %r has no %r."
                    % (act_id, m.get("id"), f))
        if float(m["n"]) <= 1:
            raise ValueError(
                "refraction-block %r material %r has index %s. A material "
                "that does not slow light cannot bend it, and the bench has "
                "nothing to show." % (act_id, m.get("id"), m["n"]))
    order = [float(m["n"]) for m in mats]
    if order != sorted(order):
        raise ValueError(
            "refraction-block %r lists its materials out of index order. "
            "Design draws them least-slowing first because the tab row "
            "itself teaches the pattern." % act_id)

    inc = a.get("inc") or {}
    if float(inc.get("min", 1)) != 0:
        raise ValueError(
            "refraction-block %r starts its angle at %s. Zero is the state "
            "the lesson turns on — light along the normal slows and does not "
            "bend — and a slider that cannot reach it makes the gate's own "
            "question unanswerable at the bench."
            % (act_id, inc.get("min")))

    tails = a.get("branch_tail") or {}
    for k in ("straight", "bent"):
        if not tails.get(k):
            raise ValueError(
                "refraction-block %r has no %r branch tail." % (act_id, k))
    verdicts = a.get("verdicts") or {}
    for k in ("straight", "bent"):
        if not verdicts.get(k):
            raise ValueError(
                "refraction-block %r has no %r verdict word." % (act_id, k))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-rblock-mat", m["label"],
             pressed=(i == int(a.get("start_mat", 0))),
             data_rblock_mat=m["id"], data_n=m["n"], data_v=m["v"],
             data_caption=m["caption"], data_note=m["note"],
             data_name=m["label"])
        for i, m in enumerate(mats))

    # Design's own 1000×460 viewBox: the block across the middle, the first
    # normal fixed at the entry point, the second one moving with the exit.
    svg = (
        '<svg class="ks3-rblock-svg" viewBox="0 0 1000 460" role="img" '
        'aria-label="" data-rblock-alt>%s'
        '<rect class="ks3-rblock-block" x="140" y="150" width="720" '
        'height="160" rx="6"/>'
        '<path class="ks3-rblock-normal" d="M400 40 V420"/>'
        '<path class="ks3-rblock-normal" data-rblock-normal2 d="M0 0"/>'
        '<text class="ks3-rblock-normallabel" x="410" y="36">%s</text>'
        '<path class="ks3-rblock-ray" data-rblock-in d="M0 0"%s/>'
        '<path class="ks3-rblock-inner" data-rblock-mid d="M0 0"%s/>'
        '<path class="ks3-rblock-ray" data-rblock-exit d="M0 0"%s/>'
        '<path class="ks3-rblock-ghost" data-rblock-ghost d="M0 0"/>'
        '<text class="ks3-rblock-airlabel" x="150" y="140">%s</text></svg>'
        % (_rayhead("rblock", 6, "var(--ks3-blue-light)"),
           t(a.get("normal_label", "NORMAL")),
           _head("rblock"), _head("rblock"), _head("rblock"),
           t(a.get("air_label", "AIR"))))

    fills = "".join(
        '<span class="ks3-rblock-fill ks3-rblock-%s" data-rblock-fill="%s">'
        '</span>' % (k, k) for k in ("caption", "inc", "ref"))

    return ('<div class="ks3-rblock" data-rblock data-tail-straight="%s" '
            'data-tail-bent="%s" data-verdict-straight="%s" '
            'data-verdict-bent="%s" data-start-mat="%s"%s>%s'
            '<div class="ks3-rblock-body" data-rblock-body hidden>'
            '<div class="ks3-rblock-controls">%s%s</div>'
            '<div class="ks3-rblock-figwrap">'
            '<div class="ks3-rblock-figinner">%s%s</div></div>%s'
            '<p class="ks3-rblock-note" data-rblock-note></p></div></div>'
            % (e(tails["straight"]), e(tails["bent"]),
               e(verdicts["straight"]), e(verdicts["bent"]),
               e(a.get("start_mat", 0)), _sibling(a),
               _gate(act_id, "refraction-block", a.get("gate") or {},
                     "rblock"),
               _slider(act_id, "rblock", inc, "a"),
               _picker("rblock", a.get("mat_label", "What the block is"),
                       tabs),
               svg, fills,
               _tiles("rblock", a.get("readouts") or [], act_id,
                      "refraction-block")))


# ═══ p7-04 · #s-camera · the pinhole camera ══════════════════════════════

def r_pinhole_camera(a, act_id):
    """⊕ p7-04 `#s-camera` — three controls, and two of them fight.

    ⚖️ **THE HOLE WIDTH MOVES THE BLUR AND NOT THE HEIGHT, AND EVERY
    NOTE SAYS THE HEIGHT DID NOT MOVE.** `LIGHT-14` is *a bigger hole
    makes a bigger picture*, and a bench that reported only the blur
    would leave it standing — a student sees something change and
    attributes it to the control under their finger. All three hole notes
    quote the live picture height.

    ⚖️ **THE TWO ARROW HEIGHTS ARE TO ONE SCALE AND THE AXIS IS NOT**,
    and the drawing says so in its own foot line. The hole is placed at
    `OX + (IX − OX) / (1 + v/u)` so the drawn rays stay straight at any
    ratio, which is what keeps the picture-to-object ratio exact while
    2000 mm and 50 mm share one line.

    ⚠️ **THE BLUR IS THE STROKE WIDTH, WITH A FLOOR.** Two pixels
    minimum, because a zero-width arrow is not a sharp picture, it is no
    picture — and the millimetre reading beside it is the second channel.

    HOOKS: `data-pinh` (wrapper, `data-object-mm`) · `data-pinh-gate` ·
    `data-pinh-gopt` · `data-pinh-body` · `data-pinh-hole` ·
    `data-pinh-slider` (valued `u` / `v`) · `data-pinh-box` ·
    `data-pinh-raytop` · `data-pinh-raybot` · `data-pinh-img` ·
    `data-pinh-fill` · `data-pinh-out` · `data-pinh-note`.
    """
    _no_head(a, act_id, "pinhole-camera")
    holes = a.get("holes") or []
    if len(holes) < 3:
        raise ValueError(
            "pinhole-camera %r declares %d hole(s). The trade needs both "
            "ends and the middle: sharp and dim, the compromise, bright and "
            "blurred." % (act_id, len(holes)))
    _unique(holes, act_id, "pinhole-camera", "hole")
    for h in holes:
        for f in ("label", "d", "note"):
            if not h.get(f):
                raise ValueError(
                    "pinhole-camera %r hole %r has no %r."
                    % (act_id, h.get("id"), f))
        if "{img}" not in h["note"]:
            raise ValueError(
                "pinhole-camera %r hole %r never names the picture height. "
                "Every hole note quotes it, because the claim this bench "
                "exists to make is that the height DID NOT MOVE — and a note "
                "that only reports the blur leaves `a bigger hole makes a "
                "bigger picture` standing." % (act_id, h.get("id")))
    ds = [float(h["d"]) for h in holes]
    if ds != sorted(ds):
        raise ValueError(
            "pinhole-camera %r lists its holes out of width order. The tab "
            "row runs narrow to wide because the trade does." % act_id)

    obj = float(a.get("object_mm") or 0)
    if obj <= 0:
        raise ValueError(
            "pinhole-camera %r has no object height. The picture height is "
            "computed from it and the readout's own working line quotes it."
            % act_id)

    tabs = "".join(
        _seg("ks3-seg-btn ks3-pinh-hole", h["label"],
             pressed=(i == int(a.get("start_hole", 0))),
             data_pinh_hole=h["id"], data_d=h["d"], data_note=h["note"],
             data_name=h["label"])
        for i, h in enumerate(holes))

    # Design's own 1000×440 viewBox.
    svg = (
        '<svg class="ks3-pinh-svg" viewBox="0 0 1000 440" role="img" '
        'aria-label="" data-pinh-alt>%s'
        '<path class="ks3-pinh-axis" d="M60 220 H960"/>'
        '<path class="ks3-pinh-object" d="M120 220 V130 M120 130 l-11 18 '
        'M120 130 l11 18"/>'
        '<path class="ks3-pinh-box" data-pinh-box d="M0 0"/>'
        '<path class="ks3-pinh-ray" data-pinh-raytop d="M0 0"%s/>'
        '<path class="ks3-pinh-ray" data-pinh-raybot d="M0 0"%s/>'
        '<path class="ks3-pinh-img" data-pinh-img d="M0 0"/>'
        '<text class="ks3-pinh-partlabel" x="60" y="118">%s</text>'
        '<text class="ks3-pinh-partlabel" x="960" y="118" '
        'text-anchor="end">%s</text>'
        '<text class="ks3-pinh-axislabel" x="60" y="424">%s</text></svg>'
        % (_rayhead("pinh", 4, "var(--ks3-blue-light)"),
           _head("pinh"), _head("pinh"),
           t(a.get("object_label", "")), t(a.get("screen_label", "SCREEN")),
           t(a.get("axis_note", ""))))

    fills = ('<span class="ks3-pinh-fill ks3-pinh-hole-label" '
             'data-pinh-fill="hole"></span>')

    return ('<div class="ks3-pinh" data-pinh data-object-mm="%s" '
            'data-start-hole="%s"%s>%s'
            '<div class="ks3-pinh-body" data-pinh-body hidden>'
            '<div class="ks3-pinh-controls">%s%s%s</div>'
            '<div class="ks3-pinh-figwrap">'
            '<div class="ks3-pinh-figinner">%s%s</div></div>%s'
            '<p class="ks3-pinh-note" data-pinh-note></p></div></div>'
            % (e(obj), e(a.get("start_hole", 0)), _sibling(a),
               _gate(act_id, "pinhole-camera", a.get("gate") or {}, "pinh"),
               _slider(act_id, "pinh", a.get("u") or {}, "u"),
               _slider(act_id, "pinh", a.get("v") or {}, "v"),
               _picker("pinh", a.get("hole_label", "How wide the hole is"),
                       tabs),
               svg, fills,
               _tiles("pinh", a.get("readouts") or [], act_id,
                      "pinhole-camera")))


# ═══ p7-05 · #s-eye · the eye and the camera ════════════════════════════

def r_eye_camera(a, act_id):
    """⊕ p7-05 `#s-eye` — one scene, two ways of catching it (her FLAG 8).

    ⚖️ **ONE BENCH HOLDS TWO INSTRUMENTS, AND THE WHOLE DRAWING
    SWITCHES.** The body, the opening, the lens, the back surface and the
    inverted picture arrow all change together, so a student is never
    left with two answers to *describe the apparatus*. Design flags it
    against "one practical per bench" and says why it stands: the
    comparison IS the lesson.

    ⚖️ **EVERY BRANCH NAMES BOTH OPENINGS AT THE CURRENT LIGHT LEVEL.**
    The eye's note quotes the camera's aperture and the camera's quotes
    the pupil, because a reading of one on its own is a fact and the pair
    is the comparison. `r_eye_camera` refuses a system that does not
    declare which of the level's two widths is its own.

    ⚠️ **THE OPENING IS DRAWN TO SCALE IN MILLIMETRES**, at a different
    pixels-per-millimetre for the two instruments, because 2 mm of pupil
    and 50 mm of aperture cannot share one scale inside one 400-unit
    drawing. The number beside it is the honest channel and the caption
    names which instrument it belongs to.

    HOOKS: `data-eyecam` (wrapper) · `data-eyecam-gate` ·
    `data-eyecam-gopt` · `data-eyecam-body` · `data-eyecam-sys` ·
    `data-eyecam-slider` · `data-eyecam-level` · `data-eyecam-case` ·
    `data-eyecam-stop` · `data-eyecam-lens` · `data-eyecam-back` ·
    `data-eyecam-rays` · `data-eyecam-img` · `data-eyecam-fill` ·
    `data-eyecam-out` · `data-eyecam-note`.
    """
    _no_head(a, act_id, "eye-camera")
    systems = a.get("systems") or []
    if len(systems) != 2:
        raise ValueError(
            "eye-camera %r declares %d system(s). The lesson is an eye "
            "AGAINST a camera and one of them alone makes no comparison."
            % (act_id, len(systems)))
    _unique(systems, act_id, "eye-camera", "system")
    levels = a.get("levels") or []
    if len(levels) < 4:
        raise ValueError(
            "eye-camera %r declares %d light level(s). The opening has to "
            "move over a range a student can recognise, from a moonless "
            "night to bright sun." % (act_id, len(levels)))
    _unique(levels, act_id, "eye-camera", "level")

    # ⚠️ THE TWO WIDTH KEYS ARE A CLOSED SET, and the wiring branches on
    # them by literal name (`data-eye` / `data-cam`) rather than composing
    # the attribute — a composed name is a read site nothing outside the
    # function can see, and `ks3_key_audit` reported one of the two widths
    # as authored-and-read-by-nothing for exactly that reason. Naming the
    # pair here is what keeps the payload, the drawer and the runtime
    # agreeing about which two words they are.
    keys = [s.get("key") for s in systems]
    for k in keys:
        if k not in ("eye", "cam"):
            raise ValueError(
                "eye-camera %r declares system key %r. The wiring reads a "
                "level's two widths as `data-eye` and `data-cam` by literal "
                "name, so a third key would render as a blank opening with "
                "nothing said." % (act_id, k))
    for s in systems:
        for f in ("label", "key", "stop_name", "focus", "absorb",
                  "absorb_name", "caption", "tail"):
            if not s.get(f):
                raise ValueError(
                    "eye-camera %r system %r has no %r."
                    % (act_id, s.get("id"), f))
    for L in levels:
        for f in ("label", "lux"):
            if not L.get(f):
                raise ValueError(
                    "eye-camera %r level %r has no %r."
                    % (act_id, L.get("id"), f))
        for k in keys:
            if not L.get(k):
                raise ValueError(
                    "eye-camera %r level %r gives no width for system key "
                    "%r. Every branch names BOTH openings at the current "
                    "level — the reading on its own is a fact and the pair "
                    "is the comparison." % (act_id, L.get("id"), k))

    branches = a.get("branches") or {}
    for s in systems:
        if not branches.get(s["id"]):
            raise ValueError(
                "eye-camera %r has no branch for system %r."
                % (act_id, s.get("id")))
    if not a.get("branch_middle"):
        raise ValueError(
            "eye-camera %r has no `branch_middle`. Design's shared sentence "
            "— the opening is only the doorway — is what stops the bench "
            "reading as though the aperture were the whole instrument."
            % act_id)

    sys_tabs = "".join(
        _seg("ks3-seg-btn ks3-eyecam-sys", s["label"], pressed=(i == 0),
             data_eyecam_sys=s["id"], data_key=s["key"],
             data_stop_name=s["stop_name"], data_focus=s["focus"],
             data_absorb=s["absorb"], data_absorb_name=s["absorb_name"],
             data_caption=s["caption"], data_tail=s["tail"],
             data_name=s["label"])
        for i, s in enumerate(systems))

    level_data = "".join(
        '<span data-eyecam-level="%d" data-label="%s" data-lux="%s"%s '
        'hidden></span>'
        % (i, e(L["label"]), e(L["lux"]),
           "".join(' data-%s="%s"' % (e(k), e(L[k])) for k in keys))
        for i, L in enumerate(levels))

    # Design's own 1000×400 viewBox. The scene arrow on the left is fixed;
    # everything about the instrument is a hole.
    svg = (
        '<svg class="ks3-eyecam-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-eyecam-alt>%s'
        '<path class="ks3-eyecam-scene" d="M120 200 V90 M120 90 l-11 18 '
        'M120 90 l11 18"/>'
        '<text class="ks3-eyecam-partlabel" x="60" y="72">%s</text>'
        '<path class="ks3-eyecam-case" data-eyecam-case d="M0 0"/>'
        '<path class="ks3-eyecam-stop" data-eyecam-stop d="M0 0"/>'
        '<path class="ks3-eyecam-lens" data-eyecam-lens d="M0 0"/>'
        '<path class="ks3-eyecam-back" data-eyecam-back d="M0 0"/>'
        '<path class="ks3-eyecam-rays" data-eyecam-rays d="M0 0"%s/>'
        '<path class="ks3-eyecam-img" data-eyecam-img d="M0 0"/></svg>'
        % (_rayhead("eyecam", 4, "var(--ks3-blue-light)"),
           t(a.get("scene_label", "THE SCENE")),
           _head("eyecam", "start", "mid", "end")))

    fills = "".join(
        '<span class="ks3-eyecam-fill ks3-eyecam-%s" data-eyecam-fill="%s">'
        '</span>' % (k, k) for k in ("caption", "stop", "absorb"))

    branch_data = "".join(
        '<span data-eyecam-branch="%s" data-note="%s" hidden></span>'
        % (e(s["id"]), e(branches[s["id"]])) for s in systems)

    return ('<div class="ks3-eyecam" data-eyecam data-middle="%s" '
            'data-start-level="%s"%s>%s'
            '<div class="ks3-eyecam-body" data-eyecam-body hidden>'
            '<div class="ks3-eyecam-controls">%s%s</div>'
            '<div class="ks3-eyecam-figwrap">'
            '<div class="ks3-eyecam-figinner">%s%s</div></div>%s'
            '<p class="ks3-eyecam-note" data-eyecam-note></p>%s%s'
            '</div></div>'
            % (e(a["branch_middle"]), e(a.get("start_level", 0)),
               _sibling(a),
               _gate(act_id, "eye-camera", a.get("gate") or {}, "eyecam"),
               _picker("eyecam", a.get("sys_label", "Which instrument"),
                       sys_tabs),
               _slider(act_id, "eyecam", {
                   "label": a.get("light_label", "How bright the scene is"),
                   "min": 0, "max": len(levels) - 1, "step": 1,
                   "start": int(a.get("start_level", 0)),
                   "value": levels[int(a.get("start_level", 0))]["label"]},
                   "l"),
               svg, fills,
               _tiles("eyecam", a.get("readouts") or [], act_id,
                      "eye-camera"),
               level_data, branch_data))


# ═══ p7-06 · #s-prism · a ray box, a prism and a white screen ════════════

# ── ⚠️ THE FAN'S GEOMETRY IS COMPUTED HERE, NOT IN THE RUNTIME ──────────
#
# It used to be a JS-only constant (`P7_PRISM_Y` in `shared/ks3.js`) with the
# landing points derived at paint time. Nothing in the build could see it, so
# nothing in the build could check it — and what shipped, for as long as the
# unit has existed, was `LIGHT-23` drawn by the instrument built to kill it:
# every colour deviated toward the APEX, and red deviated MOST. It survived
# every review because the six rays still read R,O,Y,G,B,V top to bottom.
#
# So the numbers live here, `_prism_fan()` refuses a backwards one, and the
# runtime does nothing but read the attributes and join them into path
# strings. The check runs at import, on every build, for free.
#
# ⚠️ THE DRAWING IS A SCHEMATIC AND SAYS SO. A real 60° prism deviates a
# horizontal ray by about 43° and separates red from violet by under a
# degree; drawn to scale on this 1000×420 canvas the fan would leave the
# frame and the six colours would be one line. So the SEPARATION is
# exaggerated — about eighteen-fold — while the three things a student can
# be wrong about are exact: every colour bends toward the BASE, violet bends
# furthest and red least, and the light bends TWICE, once at each face.

P7_APEX = (300.0, 90.0)          # her prism: M300 90 L400 270 L200 270 Z
P7_BASE_Y = 270.0
P7_HALF_BASE = 100.0
P7_FACE = (P7_BASE_Y - P7_APEX[1]) / P7_HALF_BASE   # 1.8 down per 1 out
P7_BEAM_X0 = 40.0                # where the ray box's beam starts
P7_BEAM_Y = 160.0                # horizontal in, so the ghost is this line
P7_INSIDE = 0.1405408            # tan 8° — the ray's slope inside the glass
P7_SCREEN_X = 925.0              # the rays stop just short of the screen
P7_SCREEN_SPAN = (48.0, 372.0)   # the drawn screen is M930 40 V380
P7_MIN_DEV = 60.0                # red is deviated too, and must look it

# The six landings on the screen, low frequency first. The GAPS are in the
# ratio of the real red→violet spread in crown glass (n−1 = .514 .517 .519
# .523 .529 .539), which is why they widen toward violet rather than being
# evenly spaced: dispersion is not linear in colour.
P7_FAN = (("R", 265.0), ("O", 276.0), ("Y", 284.0),
          ("G", 298.0), ("B", 321.0), ("V", 358.0))

# The second prism, the other way up: apex DOWN at (660,300), base along the
# top. Its base side is therefore UP, so it bends every colour back the way
# it came — most for violet — which is the whole argument.
P7_TWO_PATH = "M660 300 L560 120 L760 120 Z"
P7_TWO_LEFT_TOP = (560.0, 120.0)
P7_TWO_APEX = (660.0, 300.0)
P7_TWO_EXIT = (710.0, 210.0)     # on its right face; the beam leaves level


def _n(v):
    """One decimal place, and no trailing `.0` in a path string."""
    s = "%.1f" % v
    return s[:-2] if s.endswith(".0") else s


def _prism_fan(fan, beam_y=P7_BEAM_Y, inside=P7_INSIDE):
    """Every drawn number for the prism bench — and the refusal.

    ⚖️ **VIOLET IS DEVIATED MOST, RED LEAST, AND BOTH TOWARD THE BASE.**
    Drawn the other way round the bench teaches `LIGHT-23`, the registered
    misconception it exists to kill, and contradicts its own rung 1 one
    screen below. That cannot be left to a reviewer's eye: the top-to-bottom
    colour order still reads R,O,Y,G,B,V when the physics is inverted, which
    is exactly how it shipped.
    """
    ax, ay = P7_APEX
    entry_x = ax - (beam_y - ay) / P7_FACE
    # Right face  y = ay + FACE·(x − ax);  inside ray  y = beam_y + m·(x − entry_x)
    exit_x = ((beam_y - inside * entry_x - ay + P7_FACE * ax)
              / (P7_FACE - inside))
    exit_y = ay + P7_FACE * (exit_x - ax)

    keys = [k for k, _ in fan]
    land = dict(fan)
    slope, hit, dev = {}, {}, {}
    tx, ty = P7_TWO_LEFT_TOP
    for k in keys:
        s = (land[k] - exit_y) / (P7_SCREEN_X - exit_x)
        slope[k] = s
        dev[k] = land[k] - beam_y
        # the left face of the second prism: y = ty + FACE·(x − tx)
        hx = ((exit_y - s * exit_x - ty + P7_FACE * tx) / (P7_FACE - s))
        hit[k] = (hx, ty + P7_FACE * (hx - tx))

    faults = []
    if not (ay <= beam_y <= P7_BASE_Y):
        faults.append("the beam enters off the left face (y=%s)" % _n(beam_y))
    if not (ay <= exit_y <= P7_BASE_Y):
        faults.append("the ray leaves off the right face (y=%s)" % _n(exit_y))

    apex_side = [k for k in keys if dev[k] <= 0]
    if apex_side:
        faults.append(
            "%s deviated toward the APEX, not the base. A prism deviates "
            "every colour toward its BASE — here the base is the bottom edge "
            "at y=%s, so every ray must land BELOW the undeviated line at "
            "y=%s." % ("/".join(apex_side), _n(P7_BASE_Y), _n(beam_y)))

    order = [abs(dev[k]) for k in keys]
    if any(b <= a for a, b in zip(order, order[1:])):
        faults.append(
            "the deviations do not increase with frequency. %s is the "
            "lowest frequency drawn and %s the highest, so %s must land "
            "NEAREST the undeviated line and %s FURTHEST from it."
            % (keys[0], keys[-1], keys[0], keys[-1]))

    if order and min(order) < P7_MIN_DEV:
        faults.append(
            "%s is drawn barely deviated (%s units). A prism deviates every "
            "colour strongly; only the DIFFERENCE between them is small."
            % (keys[0], _n(min(order))))

    off = [k for k in keys
           if not (P7_SCREEN_SPAN[0] <= land[k] <= P7_SCREEN_SPAN[1])]
    if off:
        faults.append("%s lands off the screen (y must be %s–%s)"
                      % ("/".join(off), _n(P7_SCREEN_SPAN[0]),
                         _n(P7_SCREEN_SPAN[1])))

    flat = [k for k in keys if slope[k] <= inside]
    if flat:
        faults.append(
            "%s does not bend AWAY from the normal on the way out. Light "
            "leaving glass bends away from the normal, so every exit ray "
            "must be steeper than the ray inside the glass (slope %s), "
            "which is itself steeper than the beam going in."
            % ("/".join(flat), "%.4f" % inside))

    stray = [k for k in keys
             if not (tx <= hit[k][0] <= P7_TWO_APEX[0]
                     and ty <= hit[k][1] <= P7_TWO_APEX[1])]
    if stray:
        faults.append(
            "%s misses the second prism's left face, so the recombination "
            "state draws light entering glass through thin air."
            % "/".join(stray))

    if faults:
        table = "".join(
            "\n    %s  lands %8s   %s the undeviated line by %s"
            % (k, _n(land[k]), "below" if dev[k] > 0 else "ABOVE",
               _n(abs(dev[k]))) for k in keys)
        raise ValueError(
            "prism-bench: the drawn fan is wrong — %s.%s\n\n"
            "  This is not a cosmetic geometry check. Violet deviated least "
            "and red most IS `LIGHT-23`, the misconception registered on "
            "this very page as the one this bench exists to kill, and it "
            "contradicts the page's own rung 1 — 'which colour lands "
            "closest to where the undeviated beam would have gone' — one "
            "screen below. It survives a glance because the top-to-bottom "
            "colour order still reads R,O,Y,G,B,V."
            % ("; ".join(f.rstrip(".") for f in faults), table))

    return {
        "keys": keys, "land": land, "slope": slope, "hit": hit, "dev": dev,
        "entry": (entry_x, beam_y), "exit": (exit_x, exit_y),
        "in_path": "M%s %s L%s %s" % (_n(P7_BEAM_X0), _n(beam_y),
                                      _n(entry_x), _n(beam_y)),
        "inner_path": "M%s %s L%s %s" % (_n(entry_x), _n(beam_y),
                                         _n(exit_x), _n(exit_y)),
        "ghost_path": "M%s %s L%s %s" % (_n(entry_x), _n(beam_y),
                                         _n(P7_SCREEN_X), _n(beam_y)),
        "from": "%s %s" % (_n(exit_x), _n(exit_y)),
        "two_path": P7_TWO_PATH,
        "two_exit": "%s %s" % (_n(P7_TWO_EXIT[0]), _n(P7_TWO_EXIT[1])),
        "out_path": "M%s %s L%s %s" % (_n(P7_TWO_EXIT[0]), _n(P7_TWO_EXIT[1]),
                                       _n(P7_SCREEN_X), _n(P7_TWO_EXIT[1])),
        "screen_x": _n(P7_SCREEN_X),
    }


P7_PRISM = _prism_fan(P7_FAN)


def r_prism_bench(a, act_id):
    """⊕ p7-06 `#s-prism` — send white light in, sort what comes out.

    ⚖️ **THE SECOND PRISM IS A CONTROL, NOT A SENTENCE.** `LIGHT-21` is
    *the prism adds the colour*, and being told it is wrong does not kill
    it. Putting a second prism the other way up in the fanned beam does:
    if glass made colour, a second piece would make more, and it makes
    less. Newton's own experiment, on the bench rather than in the prose.

    ⚖️ **A SINGLE-COLOUR INPUT IS ITS OWN STATE AND ITS OWN NOTE.** Red
    in, red out, shifted sideways and no fan at all — which is the state
    that shows nothing is added. It also has nothing for a second prism to
    recombine, and her note says so rather than leaving the control
    looking broken.

    ⚠️ **THE FAN IS SIX FIXED RAYS BECAUSE SIX IS WHAT CAN BE TOLD
    APART**, and the legal line declares that the real spectrum is
    continuous. Each ray is one path string; there is no `<sc-for>` in an
    SVG.

    HOOKS: `data-prism` (wrapper) · `data-prism-gate` ·
    `data-prism-gopt` · `data-prism-body` · `data-prism-in-tab` ·
    `data-prism-second` · `data-prism-beam` · `data-prism-inner` ·
    `data-prism-ghost` · `data-prism-ray` (valued R/O/Y/G/B/V, each
    carrying `data-prism-y` and `data-prism-hit`) · `data-prism-two` ·
    `data-prism-outbeam` · `data-prism-fill` · `data-prism-out` ·
    `data-prism-note`. The wrapper carries the eight geometry strings
    `data-prism-inpath` / `-innerpath` / `-ghostpath` / `-from` /
    `-screenx` / `-twopath` / `-twoexit` / `-outpath`.
    """
    _no_head(a, act_id, "prism-bench")
    ins = a.get("inputs") or []
    if len(ins) < 3:
        raise ValueError(
            "prism-bench %r declares %d input(s). The argument needs white "
            "light, at least one single colour and at least one mixture that "
            "is not white." % (act_id, len(ins)))
    _unique(ins, act_id, "prism-bench", "input")
    for i2 in ins:
        for f in ("label", "keys", "word", "sub", "least", "most", "colour"):
            if not i2.get(f):
                raise ValueError(
                    "prism-bench %r input %r has no %r."
                    % (act_id, i2.get("id"), f))
        # ⚖️ RECOMBINED IS NOT THE SAME WORD AS WHITE, and the verdict has to
        # be authored per mixture rather than assumed. Blue and red put back
        # together give magenta; white needs every frequency, and this bench
        # offers a mixture that is not white precisely so a student can see
        # that a prism gives back only what went in. A shared string here
        # said "One white patch" over a drawing stroked dusky pink.
        if len(i2["keys"]) > 1:
            for f in ("two_screen", "two_beam"):
                if not i2.get(f):
                    raise ValueError(
                        "prism-bench %r mixture %r has no %r. A mixture that "
                        "is not white must say what the second prism "
                        "actually puts back together — the tile and the note "
                        "cannot both default to white."
                        % (act_id, i2.get("id"), f))
    if not any(len(i2["keys"]) == 1 for i2 in ins):
        raise ValueError(
            "prism-bench %r offers no single-colour input. It is the state "
            "that shows the prism adds nothing — one colour in, the same "
            "colour out — and without it `the prism adds the colour` is "
            "answered only in prose." % act_id)
    if not any(len(i2["keys"]) > 1 for i2 in ins):
        raise ValueError(
            "prism-bench %r offers no mixture, so nothing ever disperses."
            % act_id)

    second = a.get("second") or []
    if len(second) != 2:
        raise ValueError(
            "prism-bench %r declares %d second-prism state(s); it is in or "
            "out." % (act_id, len(second)))

    caps = a.get("captions") or {}
    for k in ("one", "two"):
        if not caps.get(k):
            raise ValueError(
                "prism-bench %r has no %r caption." % (act_id, k))

    in_tabs = "".join(
        _seg("ks3-seg-btn ks3-prism-in", x["label"], pressed=(i == 0),
             data_prism_in_tab=x["id"], data_keys=",".join(x["keys"]),
             data_word=x["word"], data_sub=x["sub"], data_least=x["least"],
             data_most=x["most"], data_colour=x["colour"],
             data_two_screen=x.get("two_screen", ""),
             data_two_beam=x.get("two_beam", ""),
             data_name=x["label"])
        for i, x in enumerate(ins))
    second_tabs = "".join(
        _seg("ks3-seg-btn ks3-prism-second", x["label"], pressed=(i == 0),
             data_prism_second=x["id"], data_on="1" if x.get("on") else "0")
        for i, x in enumerate(second))

    # Design's own 1000×420 viewBox. The first prism and the screen are
    # fixed; the second prism, the beams and the six rays are holes.
    #
    # ⚠️ EACH RAY CARRIES ITS OWN TWO NUMBERS — where it lands on the screen,
    # and where it meets the second prism's left face. Both come from
    # `_prism_fan`, which has already refused a backwards fan, so the runtime
    # never computes a landing and cannot reintroduce one.
    G = P7_PRISM
    rays = "".join(
        '<path class="ks3-prism-ray ks3-prism-ray-%s" data-prism-ray="%s" '
        'data-prism-y="%s" data-prism-hit="%s %s" d="M0 0"%s/>'
        % (k.lower(), k, _n(G["land"][k]),
           _n(G["hit"][k][0]), _n(G["hit"][k][1]),
           _head("prism")) for k in G["keys"])
    # ⚠️ ORDER IS LOAD-BEARING, and it changed. The second prism used to be
    # painted AFTER the rays, which was harmless while they stopped in mid
    # air at x=640; now that they run to its far face, a filled triangle on
    # top of them would hide the recombination inside the glass. Ghost first
    # (it is under everything), then both pieces of glass, then the light.
    #
    # ⚠️ THE GHOST IS INLINE-STYLED rather than given a class, because it is
    # the refraction bench's `.ks3-rblock-ghost` treatment exactly — #5C554D,
    # 3 wide, 10/10 dashes — and a second class declaring the same four
    # values would be a token to keep in sync for no gain.
    svg = (
        '<svg class="ks3-prism-svg" viewBox="0 0 1000 420" role="img" '
        'aria-label="" data-prism-alt>%s'
        '<path data-prism-ghost d="M0 0" style="fill:none;stroke:#5C554D;'
        'stroke-width:3;stroke-dasharray:10 10"/>'
        '<path class="ks3-prism-glass" d="M300 90 L400 270 L200 270 Z"/>'
        '<path class="ks3-prism-glass" data-prism-two d="M0 0"/>'
        '<path class="ks3-prism-beam" data-prism-beam d="M0 0"%s/>'
        '<path class="ks3-prism-beam" data-prism-inner d="M0 0"%s/>%s'
        '<path class="ks3-prism-beam" data-prism-outbeam d="M0 0"%s/>'
        '<path class="ks3-prism-screen" d="M930 40 V380"/>'
        '<text class="ks3-prism-partlabel" x="930" y="30" '
        'text-anchor="end">%s</text></svg>'
        % (_rayhead("prism", 6, "#F2ECDD"),
           _head("prism"), _head("prism"), rays, _head("prism"),
           t(a.get("screen_label", "SCREEN"))))

    fills = ('<span class="ks3-prism-fill ks3-prism-caption" '
             'data-prism-fill="caption"></span>')

    branch_data = _branches("prism", a.get("branches") or {},
                            ("single", "recombined", "dispersed"), act_id,
                            "prism-bench")

    geom = (' data-prism-inpath="%s" data-prism-innerpath="%s"'
            ' data-prism-ghostpath="%s" data-prism-from="%s"'
            ' data-prism-screenx="%s" data-prism-twopath="%s"'
            ' data-prism-twoexit="%s" data-prism-outpath="%s"'
            % (e(G["in_path"]), e(G["inner_path"]), e(G["ghost_path"]),
               e(G["from"]), e(G["screen_x"]), e(G["two_path"]),
               e(G["two_exit"]), e(G["out_path"])))

    return ('<div class="ks3-prism" data-prism data-cap-one="%s" '
            'data-cap-two="%s"%s%s>%s'
            '<div class="ks3-prism-body" data-prism-body hidden>'
            '<div class="ks3-prism-controls">%s%s</div>'
            '<div class="ks3-prism-figwrap">'
            '<div class="ks3-prism-figinner">%s%s</div></div>%s'
            '<p class="ks3-prism-note" data-prism-note></p>%s</div></div>'
            % (e(caps["one"]), e(caps["two"]), geom, _sibling(a),
               _gate(act_id, "prism-bench", a.get("gate") or {}, "prism"),
               _picker("prism", a.get("in_label", "What goes into the prism"),
                       in_tabs),
               _picker("prism", a.get("second_label",
                                      "A second prism, the other way up"),
                       second_tabs),
               svg, fills,
               _tiles("prism", a.get("readouts") or [], act_id,
                      "prism-bench"),
               branch_data))


# ═══ p7-07 · #s-lamp · one lamp, one object, a dark room ════════════════

def r_colour_bench(a, act_id):
    """⊕ p7-07 `#s-lamp` — change the object, change the light.

    ⚖️ **THE SEEN COLOUR IS COMPUTED FROM THE INTERSECTION**, never
    authored per cell. Twenty states — five objects by four lamps — and
    the answer in all twenty is *what the lamp contains AND the surface
    reflects*. Computing it is what makes every state true by
    construction, including the three a per-cell author would get wrong:
    white-on-white, black under anything, and the two empty
    intersections that are empty for different reasons.

    ⚖️ **"ALMOST BLACK", NEVER "BLACK".** Real dyes and real lamps are
    broad bands, so the perfect case does not occur and her legal line
    says so. The drawer refuses a payload whose empty-intersection word
    is "Black".

    ⚠️ **HUE IS NEVER THE ONLY CHANNEL** (her FLAG 10). The object
    rectangle takes the computed colour AND the tile prints the word; the
    outgoing ray goes dashed and grey when nothing comes back AND the
    label says *nothing comes back*.

    HOOKS: `data-clamp` (wrapper) · `data-clamp-gate` ·
    `data-clamp-gopt` · `data-clamp-body` · `data-clamp-obj` ·
    `data-clamp-lamp` · `data-clamp-in` · `data-clamp-rect` ·
    `data-clamp-back` · `data-clamp-seen` · `data-clamp-fill` ·
    `data-clamp-out` (valued with a readout id) · `data-clamp-sub` ·
    `data-clamp-note`.
    """
    _no_head(a, act_id, "colour-bench")
    objs = a.get("objects") or []
    lamps = a.get("lamps") or []
    if len(objs) < 4 or len(lamps) < 3:
        raise ValueError(
            "colour-bench %r declares %d object(s) and %d lamp(s). The grid "
            "is the argument: a white one that takes the lamp's colour, a "
            "black one that takes none, and enough coloured ones that an "
            "empty intersection is reachable more than one way."
            % (act_id, len(objs), len(lamps)))
    _unique(objs, act_id, "colour-bench", "object")
    _unique(lamps, act_id, "colour-bench", "lamp")

    seen = a.get("seen") or []
    if len(seen) < 3:
        raise ValueError(
            "colour-bench %r declares %d seen-colour(s). Every colour the "
            "bench can report needs a WORD as well as a hue — hue is never "
            "the only channel." % (act_id, len(seen)))
    _unique(seen, act_id, "colour-bench", "seen colour")
    prims = {s["id"] for s in seen}

    for o in objs:
        for f in ("label", "hex", "desc"):
            if not o.get(f):
                raise ValueError(
                    "colour-bench %r object %r has no %r."
                    % (act_id, o.get("id"), f))
        if o.get("reflects") is None:
            raise ValueError(
                "colour-bench %r object %r declares no `reflects` list. An "
                "empty list is the black card and is legal; a missing one is "
                "an object the bench cannot compute." % (act_id, o.get("id")))
        stray = [c for c in o["reflects"] if c not in prims]
        if stray:
            raise ValueError(
                "colour-bench %r object %r reflects %s, which the `seen` map "
                "has no word for — so the readout would print a colour it "
                "cannot name." % (act_id, o.get("id"), sorted(stray)))
    for L in lamps:
        for f in ("label", "hex", "word"):
            if not L.get(f):
                raise ValueError(
                    "colour-bench %r lamp %r has no %r."
                    % (act_id, L.get("id"), f))
        stray = [c for c in (L.get("has") or []) if c not in prims]
        if stray:
            raise ValueError(
                "colour-bench %r lamp %r contains %s, which the `seen` map "
                "has no word for." % (act_id, L.get("id"), sorted(stray)))
    if not any(not o["reflects"] for o in objs):
        raise ValueError(
            "colour-bench %r has no object that reflects nothing. The black "
            "card is the control: it is the one surface whose answer does "
            "not depend on the lamp." % act_id)
    if not any(len(o["reflects"]) >= len(prims) for o in objs):
        raise ValueError(
            "colour-bench %r has no object that reflects everything. The "
            "white one is what makes 'it takes the colour of the lamp' "
            "something a student can see rather than be told." % act_id)

    branches = a.get("branches") or {}
    branch_data = _branches("clamp", branches,
                            ("nothing", "everything", "some"), act_id,
                            "colour-bench")
    if "almost black" not in (branches.get("nothing") or "").lower():
        raise ValueError(
            "colour-bench %r's empty-intersection branch does not say "
            "\"almost black\". Design uses the hedge everywhere on this page "
            "and her legal line explains it: real dyes and real lamps are "
            "broad bands, so the perfect case does not occur." % act_id)

    obj_tabs = "".join(
        _seg("ks3-seg-btn ks3-clamp-obj", o["label"],
             pressed=(i == int(a.get("start_object", 0))),
             data_clamp_obj=o["id"], data_reflects=",".join(o["reflects"]),
             data_hex=o["hex"], data_desc=o["desc"], data_name=o["label"])
        for i, o in enumerate(objs))
    lamp_tabs = "".join(
        _seg("ks3-seg-btn ks3-clamp-lamp", L["label"],
             pressed=(i == int(a.get("start_lamp", 0))),
             data_clamp_lamp=L["id"], data_has=",".join(L.get("has") or []),
             data_hex=L["hex"], data_word=L["word"], data_name=L["label"])
        for i, L in enumerate(lamps))

    seen_data = "".join(
        '<span data-clamp-seen="%s" data-word="%s" data-hex="%s" hidden>'
        '</span>' % (e(s["id"]), e(s["word"]), e(s["hex"])) for s in seen)

    # Design's own 1000×380 viewBox: the lamp at the top left, the object
    # in the middle, the eye at the top right.
    svg = (
        '<svg class="ks3-clamp-svg" viewBox="0 0 1000 380" role="img" '
        'aria-label="" data-clamp-alt>%s'
        '<path class="ks3-clamp-lampbody" d="M120 40 h150 l-40 70 h-70 Z"/>'
        '<text class="ks3-clamp-partlabel" x="120" y="30">%s</text>'
        '<path class="ks3-clamp-in" data-clamp-in d="M205 114 L440 216"%s/>'
        '<rect class="ks3-clamp-rect" data-clamp-rect x="440" y="150" '
        'width="200" height="140" rx="10"/>'
        '<path class="ks3-clamp-out" data-clamp-back d="M640 216 L880 130"%s/>'
        '<circle class="ks3-clamp-eye" cx="920" cy="118" r="26"/>'
        '<circle class="ks3-clamp-pupil" cx="920" cy="118" r="9"/>'
        '<text class="ks3-clamp-partlabel" x="880" y="80">%s</text></svg>'
        % (_rayhead("clamp", 8, "#F2ECDD"),
           t(a.get("lamp_glyph_label", "LAMP")), _head("clamp"),
           _head("clamp"), t(a.get("eye_label", "EYE"))))

    fills = "".join(
        '<span class="ks3-clamp-fill ks3-clamp-%s" data-clamp-fill="%s">'
        '</span>' % (k, k)
        for k in ("absorbcap", "objcap", "inlabel", "outlabel"))

    return ('<div class="ks3-clamp" data-clamp data-nothing-hex="%s" '
            'data-white-hex="%s" data-start-obj="%s" data-start-lamp="%s"%s>%s'
            '<div class="ks3-clamp-body" data-clamp-body hidden>'
            '<div class="ks3-clamp-controls">%s%s</div>'
            '<div class="ks3-clamp-figwrap">'
            '<div class="ks3-clamp-figinner">%s%s</div></div>%s'
            '<p class="ks3-clamp-note" data-clamp-note></p>%s%s</div></div>'
            % (e(a.get("nothing_hex", "#151312")),
               e(a.get("white_hex", "#F2ECDD")),
               e(a.get("start_object", 0)), e(a.get("start_lamp", 0)),
               _sibling(a),
               _gate(act_id, "colour-bench", a.get("gate") or {}, "clamp"),
               _picker("clamp", a.get("obj_label", "The object"), obj_tabs),
               _picker("clamp", a.get("lamp_label", "The light falling on it"),
                       lamp_tabs),
               svg, fills,
               _tiles("clamp", a.get("readouts") or [], act_id,
                      "colour-bench"),
               seen_data, branch_data))


# ═══ the band blocks · #s-figure #s-inout #s-lens #s-parts #s-band #s-grid ═

def r_light_band(a, act_id):
    """⊕ The fixed figure Design puts beside six of the seven benches.

    ⚖️ **`table` / `straw` / `pair` / `spectrum`, NOT `cards`.** `cards`
    is claimed by `r_activity` itself with NO opt-out, so a payload using
    it gets two renderers and renders blank. The key names are
    deliberately different for that reason and no other.

    ⚖️ **FIVE OF THE SIX ARE TICKED BY THE BENCH BESIDE THEM.** These
    blocks carry no control: they are the payoff of the instrument, and
    each bench marks its own band sibling at Design's own earlier
    threshold. `p7-01`'s comparison table is the exception and takes no
    rail stop at all — her `RAIL` for that page is four entries and the
    figure is not among them.

    Four shapes go through here, and the payload decides which:
      `p7-01 #s-figure`  a six-row comparison table
      `p7-03 #s-inout`   the apparent-depth drawing
      `p7-04 #s-lens`    two lens diagrams side by side
      `p7-05 #s-parts`   a five-row job table
      `p7-06 #s-band`    the six-segment spectrum with two arrows
      `p7-07 #s-grid`    a five-by-three colour grid
    """
    body = ""
    if a.get("table"):
        body += _band_table(a["table"], act_id)
    if a.get("straw"):
        body += _band_straw(a["straw"], act_id)
    if a.get("pair"):
        body += _band_pair(a["pair"], act_id)
    if a.get("spectrum"):
        body += _band_spectrum(a["spectrum"], act_id)

    if not body:
        raise ValueError(
            "light-band %r renders nothing — no table, straw, pair or "
            "spectrum. An empty band block is a section heading with a gap "
            "under it." % act_id)

    close = ('<p class="ks3-lband-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")
    if not a.get("close"):
        raise ValueError(
            "light-band %r has no closing line. Every one of Design's six "
            "figures ends with the sentence that says what the picture was "
            "FOR, and without it the block is a diagram with no claim."
            % act_id)

    # ⊕ ONE HEAD ROW, NOT TWO. The `check` shell (`r_activity`'s
    # `.ks3-blockhead`) already emits this block's eyebrow and `<h2>` from
    # the same two keys, which is Design's own section head. P6's
    # `r_wave_band` emits them a second time inside the band, so every
    # shipped P6 figure carries its eyebrow and heading twice (measured in
    # `how-sound-is-made.html`: two "The figure", two "Four stages, every
    # time"). P7 does not repeat it; the shell's row is the only one.
    return ('<div class="ks3-lband" data-lband>%s%s</div>' % (body, close))


def _band_table(spec, act_id):
    """A comparison table, in a scroller that is `position: relative`.

    ⚠️ **THE FIRST CELL OF EVERY ROW IS A ROW HEADER.** Design writes it
    as `<th scope="row">` and it is the only thing that makes the table
    navigable to a screen reader — a grid of `<td>` with no headers is a
    list of words in an order nobody can recover.
    """
    cols = spec.get("columns") or []
    rows = spec.get("rows") or []
    if len(cols) < 3 or len(rows) < 3:
        raise ValueError(
            "band-table %r has %d column(s) and %d row(s). Design's tables "
            "compare at least two things over at least three properties."
            % (act_id, len(cols), len(rows)))
    for r in rows:
        if len(r) != len(cols):
            raise ValueError(
                "band-table %r has a row of %d cell(s) against %d column(s). "
                "A short row shifts every cell after it into the wrong "
                "column, silently." % (act_id, len(r), len(cols)))

    head = "".join('<th scope="col">%s</th>' % rich(c) for c in cols)
    tbody = ""
    for r in rows:
        cells = "".join("<td>%s</td>" % rich(c) for c in r[1:])
        tbody += '<tr><th scope="row">%s</th>%s</tr>' % (rich(r[0]), cells)
    return ('<div class="ks3-lband-scroller">'
            '<table class="ks3-lband-table"><caption class="ks3-sr-only">%s'
            '</caption><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
            '</div>'
            % (t(spec.get("aria_label", "")), head, tbody))


def _band_straw(spec, act_id):
    """p7-03 `#s-inout` — the straw, the ray, and the line the brain drew.

    ⚖️ **BOTH POSITIONS ARE MARKED AND BOTH ARE LABELLED.** *Where it
    is* and *where it looks* — a figure with only the apparent position
    would be the illusion drawn rather than explained, and one with only
    the real position would not be about seeing at all.

    ⚠️ Every string here is a constant at build time, so `<text>` is
    right: MRB-254 forbids a `<text>` that ships empty to be filled later,
    and none of these is.

    ── ⊕ MRB-297 · P7-10 · THE BACK-PROJECTION IS NOW THE RAY'S OWN ────

    ⚖️ **THE FIGURE THAT EXISTS TO EXPLAIN THE ILLUSION DREW THE ILLUSION
    WRONGLY.** The dashed line was `M520 140 L740 296` — down and to the
    RIGHT of the refraction point, out through the right-hand wall of the
    glass, ending in mid-air. It is meant to be the emergent ray continued
    straight BACKWARDS. That ray is `M520 140 L800 90`, so backwards from
    (520, 140) the direction is (−280, +50): up the page and to the left,
    the opposite quadrant to the one drawn. Continued 128 units back in x
    it reaches (392, 162.9), which is `M520 140 L392 163`.

    ⚖️ **AND THE MARKER WAS ON THE WRONG LINE.** *WHERE IT LOOKS* sat at
    (452, 253), which is not on the back-projection and never was — it is
    a point on the REAL in-water ray `M400 330 L520 140`, which passes
    through (452, 248). So the drawing asserted that the straw's end
    appears at a place the light genuinely goes through, and the one
    construction line that would have shown why pointed elsewhere. Every
    rung-3 and rung-4 answer on this page depends on the figure.

    The marker is now at (400, 161), which IS on the new dashed line and
    is directly above *WHERE IT IS* at (400, 330). The vertical gap
    between the two rings is the apparent-depth story, and both labels sit
    at x=240 outside the glass so the gap is legible as a gap. Her own
    `aria_label` — *"a point higher and closer than the real end"* — is
    now true of the drawing: (400, 161) is 169 units higher, and it is
    nearer the eye at (840, 80) than the real end is, by 447 against 506.

    ⚠️ **THE DASHED LINE STAYS HEADLESS.** It is a construction line — the
    line a brain draws, not a path light takes — and P7-04's arrowheads
    are on this figure's two real rays precisely so that the difference
    between the two kinds of line can be read. The normal stays headless
    for the same reason.

    ⚠️ **THE DRAWN EMERGENT ANGLE IS STILL ~80°, AND WATER ALLOWS ~45°.**
    Not fixed here, and it cannot be without moving the water line, the
    exit point, the straw and the eye: with the exit at (520, 140), an eye
    outside the glass (x > 620) and a 380-unit canvas, 45° from the normal
    leaves the frame. Reported as a Design brief with the two-ray version.
    The lesson's `convention_note` now declares the exaggeration.
    """
    for f in ("aria_label", "surface_label", "normal_label", "eye_label",
              "looks_label", "is_label"):
        if not spec.get(f):
            raise ValueError("band-straw %r has no %r." % (act_id, f))
    return (
        '<div class="ks3-lband-figwrap">'
        '<svg class="ks3-lband-svg" viewBox="0 0 1000 380" role="img" '
        'aria-label="%s">%s'
        '<path class="ks3-lband-glass" d="M300 60 V340 H620 V60"/>'
        '<rect class="ks3-lband-water" x="303" y="140" width="314" '
        'height="197"/>'
        '<path class="ks3-lband-surface" d="M300 140 H620"/>'
        '<text class="ks3-lband-figlabel" x="240" y="134" '
        'text-anchor="end">%s</text>'
        '<path class="ks3-lband-straw" d="M470 60 L400 330"/>'
        '<path class="ks3-lband-rayline" d="M400 330 L520 140"%s/>'
        '<path class="ks3-lband-rayline" d="M520 140 L800 90"%s/>'
        '<path class="ks3-lband-back" d="M520 140 L392 163"/>'
        '<path class="ks3-lband-normal" d="M520 140 V60"/>'
        '<text class="ks3-lband-figlabel" x="530" y="54">%s</text>'
        '<circle class="ks3-lband-eye" cx="840" cy="80" r="26"/>'
        '<circle class="ks3-lband-pupil" cx="840" cy="80" r="9"/>'
        '<text class="ks3-lband-figlabel" x="874" y="86">%s</text>'
        '<circle class="ks3-lband-looks" cx="400" cy="161" r="11"/>'
        '<text class="ks3-lband-looklabel" x="240" y="166" '
        'text-anchor="end">%s</text>'
        '<circle class="ks3-lband-is" cx="400" cy="330" r="11"/>'
        '<text class="ks3-lband-figlabel" x="240" y="336" '
        'text-anchor="end">%s</text></svg></div>'
        % (e(spec["aria_label"]),
           _rayhead("straw", 5, "var(--ks3-accent)"),
           t(spec["surface_label"]),
           _head("straw"), _head("straw"),
           t(spec["normal_label"]), t(spec["eye_label"]),
           t(spec["looks_label"]), t(spec["is_label"])))


def _band_pair(cards, act_id):
    """p7-04 `#s-lens` — two lens diagrams, and both are drawn.

    ⚖️ **THE PAIR IS THE ARGUMENT.** The first card says a lens gathers a
    whole bundle and brings it to one point; the second says the rays
    still cross, so the picture is still inverted. Either one alone makes
    a claim the other half was there to balance, so `_band_pair` refuses a
    single card.
    """
    if len(cards) != 2:
        raise ValueError(
            "band-pair %r declares %d card(s). Design's figure is a pair — "
            "what a lens gathers, and what it does not fix — and one on its "
            "own makes a claim the other half was there to answer."
            % (act_id, len(cards)))
    for c in cards:
        for f in ("shape", "title", "aria_label", "body"):
            if not c.get(f):
                raise ValueError(
                    "band-pair %r card %r has no %r."
                    % (act_id, c.get("id"), f))
        if c["shape"] not in ("focus", "image"):
            raise ValueError(
                "band-pair %r card %r is shape %r; the two are `focus` and "
                "`image`." % (act_id, c.get("id"), c["shape"]))

    def draw(c):
        if c["shape"] == "focus":
            art = (
                '<path class="ks3-lband-axis" d="M20 110 H420"/>'
                '<path class="ks3-lband-lens" d="M200 34 Q236 110 200 186 '
                'Q164 110 200 34 Z"/>'
                '<path class="ks3-lband-beam" d="M20 50 H188 M20 80 H196 '
                'M20 110 H200 M20 140 H196 M20 170 H188"/>'
                '<path class="ks3-lband-beam" d="M212 50 L360 110 '
                'M208 80 L360 110 M200 110 L420 110 M208 140 L360 110 '
                'M212 170 L360 110"/>'
                '<circle class="ks3-lband-focus" cx="360" cy="110" r="10"/>'
                '<text class="ks3-lband-figlabel" x="376" y="146">%s</text>'
                % t(c.get("focus_label", "FOCUS")))
        else:
            art = (
                '<path class="ks3-lband-axis" d="M20 110 H420"/>'
                '<path class="ks3-lband-object" d="M60 110 V40 M60 40 l-9 15 '
                'M60 40 l9 15"/>'
                '<path class="ks3-lband-lens" d="M200 40 Q230 110 200 180 '
                'Q170 110 200 40 Z"/>'
                '<path class="ks3-lband-beam" d="M60 40 L196 62 '
                'M60 40 L200 110 M60 40 L196 158"/>'
                '<path class="ks3-lband-beam" d="M204 62 L340 172 '
                'M200 110 L340 172 M204 158 L340 172"/>'
                '<path class="ks3-lband-screen" d="M360 30 V196"/>'
                '<path class="ks3-lband-image" d="M340 110 V172 '
                'M340 172 l-9 -15 M340 172 l9 -15"/>')
        return ('<svg class="ks3-lband-pairsvg" viewBox="0 0 440 220" '
                'role="img" aria-label="%s">%s</svg>'
                % (e(c["aria_label"]), art))

    cells = "".join(
        '<div class="ks3-lband-paircard">'
        '<p class="ks3-lband-pairtitle">%s</p>%s'
        '<p class="ks3-lband-pairbody">%s</p></div>'
        % (t(c["title"]), draw(c), rich(c["body"])) for c in cards)
    return '<div class="ks3-lband-pair">%s</div>' % cells


def _band_spectrum(spec, act_id):
    """p7-06 `#s-band` — the band, its six names, and two arrows.

    ⚖️ **THE TWO ARROWS POINT THE SAME WAY, AND THAT IS DISPERSION.**
    Frequency increases to the right; a prism bends it further to the
    right. Drawing them as two separate facts and letting the reader
    notice they agree is the whole of the figure.

    ⚠️ **THE NAMES ARE DRAWN UNDER THE BAND, NOT INSIDE IT.** Hue is
    part of the message here and it is never the only channel: every
    segment carries its own word in ink on the card ground, where the
    contrast does not depend on the segment's colour.
    """
    segs = spec.get("segments") or []
    if len(segs) < 5:
        raise ValueError(
            "band-spectrum %r draws %d segment(s). Design's band is six, and "
            "the six names are the point — they are labels on something "
            "continuous rather than six separate things."
            % (act_id, len(segs)))
    arrows = spec.get("arrows") or []
    if len(arrows) != 2:
        raise ValueError(
            "band-spectrum %r declares %d arrow(s). The figure IS the two of "
            "them pointing the same way; one on its own is a colour chart."
            % (act_id, len(arrows)))
    for s in segs:
        for f in ("name", "hex"):
            if not s.get(f):
                raise ValueError(
                    "band-spectrum %r segment %r has no %r."
                    % (act_id, s.get("name"), f))

    X0, X1, Y, H = 40.0, 960.0, 30, 80
    w = (X1 - X0) / len(segs)
    bars, names = "", ""
    for i, s in enumerate(segs):
        x = X0 + i * w
        bars += ('<rect class="ks3-lband-seg" x="%.1f" y="%d" width="%.1f" '
                 'height="%d" style="fill:%s"/>'
                 % (x, Y, w, H, e(s["hex"])))
        names += ('<text class="ks3-lband-segname" x="%.1f" y="140" '
                  'text-anchor="middle">%s</text>'
                  % (x + w / 2.0, t(s["name"])))
    return (
        '<div class="ks3-lband-figwrap">'
        '<svg class="ks3-lband-svg" viewBox="0 0 1000 260" role="img" '
        'aria-label="%s">%s'
        '<rect class="ks3-lband-segframe" x="40" y="30" width="920" '
        'height="80"/>%s'
        '<path class="ks3-lband-arrow" d="M40 182 H940 M940 182 L920 171 '
        'M940 182 L920 193"/>'
        '<text class="ks3-lband-arrowlabel" x="40" y="170">%s</text>'
        '<path class="ks3-lband-arrow ks3-lband-arrow-accent" '
        'd="M40 232 H940 M940 232 L920 221 M940 232 L920 243"/>'
        '<text class="ks3-lband-arrowlabel" x="40" y="220">%s</text>'
        '</svg></div>'
        % (e(spec["aria_label"]), bars, names,
           t(arrows[0]), t(arrows[1])))


# ═══ the CFIFA attempt ═══════════════════════════════════════════════════

def r_p7_attempt(a, act_id):
    """⊕ P7's half of Design's `Cfifa`: the student's own five lines.

    The drawing is `ks3_art.kit.r_cfifa_attempt`, shared with P4, P5 and
    P6. The FAMILY is P7's own, so `ks3_art.load()`'s one-family-one-module
    rule holds and the placement gates see it as this unit's.

    ⚠️ `p7-02` passes `one_question_because`, which is the ONLY payload
    that lifts the helper's two-question check. See that lesson's record
    for Design's own reason.
    """
    # ⊕ ONE EYEBROW, NOT TWO. The `check` shell already prints this
    # activity's eyebrow in Design's `.ks3-blockhead`; the kit helper prints
    # it again unless told not to. P4–P6 ship it twice (measured); P7 opts
    # out by passing `None`, which the helper reads as "already printed".
    return r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p7cfa")


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P7's own — `ks3_art/core.py` is
# untouched. Shell stems checked against the whole registry first.

ART = {}

KIND_SHELL = {
    'two-speed-race':   ("ks3-lrace-block",
                         ' data-instrument data-lraceblock '
                         'data-stage-done="0"'),
    'ray-surface':      ("ks3-rsurf-block",
                         ' data-instrument data-rsurfblock '
                         'data-stage-done="0"'),
    'refraction-block': ("ks3-rblock-block",
                         ' data-instrument data-rblockblock '
                         'data-stage-done="0"'),
    'pinhole-camera':   ("ks3-pinh-block",
                         ' data-instrument data-pinhblock '
                         'data-stage-done="0"'),
    'eye-camera':       ("ks3-eyecam-block",
                         ' data-instrument data-eyecamblock '
                         'data-stage-done="0"'),
    'prism-bench':      ("ks3-prism-block",
                         ' data-instrument data-prismblock '
                         'data-stage-done="0"'),
    'colour-bench':     ("ks3-clamp-block",
                         ' data-instrument data-clampblock '
                         'data-stage-done="0"'),
    'light-band':       ("ks3-lband-block",
                         ' data-instrument data-lbandblock '
                         'data-stage-done="0"'),
    'p7-attempt':       ("ks3-p7cfa-block",
                         ' data-instrument data-p7cfablock '
                         'data-stage-done="0"'),
}

KIND_FN = {
    'two-speed-race':   r_two_speed_race,
    'ray-surface':      r_ray_surface,
    'refraction-block': r_refraction_block,
    'pinhole-camera':   r_pinhole_camera,
    'eye-camera':       r_eye_camera,
    'prism-bench':      r_prism_bench,
    'colour-bench':     r_colour_bench,
    'light-band':       r_light_band,
    'p7-attempt':       r_p7_attempt,
}
