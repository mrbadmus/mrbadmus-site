# DISPATCH: "heating-bench": ("ks3-hb-block", ' data-instrument data-hbblock data-stage-done="0"'),
#
# Splice into build_ks3.py beside the other C1 instruments, plus the dispatch
# line in `r_activity`:
#
#     if kind == "heating-bench":
#         parts.append(r_heating_bench(a, act_id))
#
# ⚠️ It must also be added to ks3_parity.COMPONENTS (see heating-bench.parity.py)
# and reached from `wireInstruments()` (see heating-bench.js).


# The two tones Design paints the phase word in: ordinary ink for a state that
# is simply warming, accent-text for a state that is changing. A closed map
# rather than an interpolated var() call, so a typo is a build error and never
# a `color: var(--ks3-taupe)` that resolves to nothing — same discipline as
# `_GROUNDS`.
_HB_TONES = {"ink", "accent"}

# The design-space canvas, doubled into the backing store. 900 × 330 is
# Design's own frame (c1-03 lines 467–476) and the readouts under it are DOM,
# so the only thing that has to reach a screen reader through the canvas is
# the state-bound `aria-label`.
_HB_CANVAS = (1800, 660)


def _hb_segments(keys):
    """`keys` as [(x0, t0, x1, t1), …] — one per phase band."""
    return [(keys[i][0], keys[i][1], keys[i + 1][0], keys[i + 1][1])
            for i in range(len(keys) - 1)]


def _hb_temp_at(keys, x):
    """Design's `tempAt`: piecewise-linear over the authored breakpoints."""
    for x0, t0, x1, t1 in _hb_segments(keys):
        if x <= x1:
            return t0 + (t1 - t0) * ((x - x0) / float(x1 - x0))
    return keys[-1][1]


def _hb_phase_at(keys, x):
    """The index of the band `x` falls in. Bands are [x0, x1), last inclusive."""
    for i, (x0, _t0, x1, _t1) in enumerate(_hb_segments(keys)):
        if x < x1:
            return i
    return len(keys) - 2


def _hb_round(t):
    """`Math.round` semantics, so Python and JS never disagree by one degree.

    Python's `round` takes halves to even and JS's `Math.round` takes them up;
    every readout on this bench is composed in both places, so the tie has to
    break the same way. Floor division rather than `int()` because `int()`
    truncates towards zero and this curve starts below it.
    """
    return int((t + 0.5) // 1)


def _hb_degrees(t, unit):
    """`−20 °C` — U+2212 MINUS, not a hyphen. Design's own readout (line 716).

    The unit is authored once in `labels.unit` and read here and in the JS.
    """
    n = _hb_round(t)
    return "%s%d %s" % ("−" if n < 0 else "", abs(n), unit)


def _hb_fill(template, t, label):
    """`{t}` and `{phase}`, composed the same way in Python and in JS.

    `{t}` is the plain rounded number, ASCII minus and all: it is spoken by a
    screen reader, and "minus 20" is what a reader makes of `-20`. The typeset
    U+2212 belongs on the visible readout and nowhere else.
    """
    return (template.replace("{t}", str(_hb_round(t)))
            .replace("{phase}", (label or "").lower()))


def r_heating_bench(a, act_id):
    """⊕ c1-03 `#s-curve` — scrub through a heating curve and watch it stop.

    ⚠️ A LIGHT `.ks3-block`, not a practical (map §3.3). The graph is drawn on
    cream and the readouts sit on `--ks3-inset`; on ink every token resolves
    wrong and the paper the curve is drawn on becomes a hole in the block.

    ⚖️ **THE MASS NEVER MOVES, AND IT IS NOT STATE.** `Mass in the flask ·
    50.0 g` is markup on Design's page and markup here: emitted once, never
    read by the runtime, never recomputed. It is the whole confrontation of
    the lesson — the temperature changes, the picture changes, and the one
    number that could say something was lost does not move — so the renderer
    RAISES on a bench that does not declare it rather than rendering two
    readouts and a gap.

    ⚖️ **EVERY BAND IS DERIVED FROM `keys`.** The five phase boundaries, the
    two shaded plateaus, the flask's melt and boil fractions and the head
    counter's total all come out of the same six breakpoints, so the plateau
    ratio can be corrected in one place and nothing drifts out of step with
    it. Design's page hard-codes the boundaries a second time in `phaseAt`
    (lines 459–466) and a third time in the two flask fractions (574, 592);
    all three had to agree by hand.

    ⚠️ Emit-both-show-one for the phase word and for the five plateau notes.
    Those notes are the science of the lesson and they are never rebuilt in JS
    from an attribute: all five are in the document, four are `hidden`, and
    the runtime toggles which one is shown.
    """
    keys = a.get("keys") or []
    phases = a.get("phases") or []
    labels = a.get("labels") or {}
    graph = a.get("graph") or {}
    flask = a.get("flask") or {}
    alt = a.get("alt") or {}

    if len(keys) < 2 or any(len(k) != 2 for k in keys):
        raise ValueError(
            "heating-bench %r needs keys[] as at least two [x, temperature] "
            "breakpoints." % act_id)
    xs = [k[0] for k in keys]
    if xs != sorted(xs) or len(set(xs)) != len(xs):
        raise ValueError(
            "heating-bench %r has keys[] out of order: x must increase "
            "strictly, got %s." % (act_id, xs))
    if xs[0] != 0 or xs[-1] != 100:
        raise ValueError(
            "heating-bench %r draws a curve from %s to %s; the scrub runs "
            "0–100 and the curve must span it, or the student can drag past "
            "the end of the run." % (act_id, xs[0], xs[-1]))
    if len(phases) != len(keys) - 1:
        raise ValueError(
            "heating-bench %r declares %d phase(s) for %d segment(s). One "
            "band per segment — the bands ARE the segments."
            % (act_id, len(phases), len(keys) - 1))

    segs = _hb_segments(keys)
    plateaus = [i for i, (_x0, t0, _x1, t1) in enumerate(segs) if t0 == t1]
    if not plateaus:
        raise ValueError(
            "heating-bench %r draws no plateau. A curve that only climbs is "
            "not this lesson." % act_id)
    for i, ph in enumerate(phases):
        if ph.get("tone") not in _HB_TONES:
            raise ValueError(
                "heating-bench %r phase %r tone %r; the drawn set is %s."
                % (act_id, ph.get("id"), ph.get("tone"),
                   ", ".join(sorted(_HB_TONES))))
        # A plateau carries the two captions the canvas draws over it; a ramp
        # carries neither, and authoring one on a ramp would paint a stripe
        # over a stretch that is not holding still.
        if (i in plateaus) != bool(ph.get("band")):
            raise ValueError(
                "heating-bench %r phase %r: `band` is the caption over a "
                "SHADED PLATEAU and this segment %s a plateau in keys[]."
                % (act_id, ph.get("id"), "is" if i in plateaus else "is not"))
        if (i in plateaus) != bool(ph.get("banner")):
            raise ValueError(
                "heating-bench %r phase %r: `banner` is the line drawn across "
                "the flask while the state is changing, so it belongs to a "
                "plateau and to nothing else." % (act_id, ph.get("id")))
        if not ph.get("note"):
            raise ValueError(
                "heating-bench %r phase %r has no note. The note is what the "
                "band teaches; a band without one is a colour."
                % (act_id, ph.get("id")))
    if not a.get("mass"):
        raise ValueError(
            "heating-bench %r declares no `mass`. The constant mass readout "
            "IS the confrontation of this lesson — see the module comment."
            % act_id)
    for key in ("scrub", "temperature", "phase", "mass", "unit"):
        if not labels.get(key):
            raise ValueError(
                "heating-bench %r has no labels[%r]; every readout on this "
                "bench is labelled on Design's page." % (act_id, key))
    for jump in a.get("jumps") or []:
        v = jump.get("value")
        if not isinstance(v, int) or v < 0 or v > 100:
            raise ValueError(
                "heating-bench %r jump %r targets %r, which is not a whole "
                "number on the 0–100 scrub." % (act_id, jump.get("label"), v))
    for field, template in (("alt.template", alt.get("template", "")),
                            ("valuetext", a.get("valuetext", ""))):
        if "{t}" not in template or "{phase}" not in template:
            raise ValueError(
                "heating-bench %r %s must carry both {t} and {phase}: it is "
                "the only reading a screen reader gets of a canvas."
                % (act_id, field))

    gate_html, hide = r_bench_gate(a.get("gate"))

    # The resting frame. Every value below is what the page SHOWS before any
    # JS runs, so the document is correct on its own and the first paint is
    # never a wrong number waiting to be corrected.
    start = 0
    t0 = _hb_temp_at(keys, start)
    ph0 = _hb_phase_at(keys, start)
    first = phases[ph0]

    words = "".join(
        '<span class="ks3-hb-phase" data-phase="%s" data-tone="%s"%s>%s</span>'
        % (e(ph.get("id", "")), e(ph.get("tone", "ink")),
           "" if i == ph0 else " hidden", t(ph.get("label", "")))
        for i, ph in enumerate(phases))
    notes = "".join(
        '<p class="ks3-hb-note" data-phase="%s"%s>%s</p>'
        % (e(ph.get("id", "")), "" if i == ph0 else " hidden",
           rich(ph.get("note", "")))
        for i, ph in enumerate(phases))
    jumps = "".join(
        '<button type="button" class="ks3-seg-btn ks3-hb-jump" data-v="%d" '
        'aria-pressed="%s">%s</button>'
        % (j["value"], "true" if abs(start - j["value"]) < 3 else "false",
           t(j.get("label", "")))
        for j in a.get("jumps") or [])

    sid = "ks3-hb-scrub-%s" % act_id
    cfg = {"keys": keys,
           "phases": [{"id": p.get("id", ""), "label": p.get("label", ""),
                       "band": p.get("band", ""), "banner": p.get("banner", "")}
                      for p in phases],
           "graph": graph, "flask": flask, "alt": alt,
           "valuetext": a.get("valuetext", ""), "unit": labels["unit"]}

    return (gate_html
            + '<div class="ks3-hb" data-hb%s data-total="%d" data-cfg="%s">'
              '<div class="ks3-hb-frame">'
              '<canvas class="ks3-hb-canvas" width="%d" height="%d" '
              'role="img" aria-label="%s" data-hb-canvas></canvas>'
              '<div class="ks3-hb-foot">'
              '<label class="ks3-hb-scrub-label" for="%s">%s</label>'
              '<input class="ks3-hb-scrub" id="%s" type="range" min="0" '
              'max="100" step="1" value="%d" aria-valuetext="%s" data-hb-scrub>'
              '<div class="ks3-hb-tiles">'
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value" data-hb-temp>%s</p></div>'
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value">%s</p></div>'
              # ⚠️ NO `data-` hook on the mass tile, deliberately. There is
              # nothing for the runtime to bind to, which is the point.
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value ks3-hb-mass">%s</p></div>'
              '</div>'
              '<div class="ks3-hb-jumps">%s</div>'
              '</div></div>'
              '<div class="ks3-hb-notes" data-hb-notes role="status">%s</div>'
              '</div>'
            % (hide, len(plateaus),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               _HB_CANVAS[0], _HB_CANVAS[1],
               e(_hb_fill(alt.get("template", ""), t0, first.get("label", ""))),
               e(sid), t(labels["scrub"]), e(sid), start,
               e(_hb_fill(a.get("valuetext", ""), t0, first.get("label", ""))),
               t(labels["temperature"]), t(_hb_degrees(t0, labels["unit"])),
               t(labels["phase"]), words,
               t(labels["mass"]), t(a["mass"]),
               jumps, notes))
