# DISPATCH: "random-walk-bench": ("ks3-walk-block", ' data-instrument data-walkblock data-stage-done="0"'),
#
# Goes in ACTIVITY_KIND_RENDERERS beside the C2 entries, plus the two lines
# `r_activity` needs:
#
#     if kind == "random-walk-bench":
#         parts.append(r_random_walk_bench(a, act_id))
#
# Place `_walk_alt` and `r_random_walk_bench` after `r_scale_zoom` in
# build_ks3.py. Needs `json`, `e`, `t`, `rich`, `r_bench_gate` — all already
# in scope there.


def _walk_alt(alt, even, left, right):
    """The tank canvas's aria-label. Composed the same way in JS.

    ⊕ `{left}` and `{right}` are an ADDITION to Design's sentence, and the
    reason is the c1-04 ruling reached by a different route: the half counts
    are DRAWN INSIDE the canvas (page lines 534–535) and appear nowhere in the
    DOM, so without them in the label a screen-reader user is told a bar chart
    exists and never told what it says. Design's own clause is unchanged; one
    sentence is appended.
    """
    return (alt.get("template", "")
            .replace("{state}", alt.get("even" if even else "uneven", ""))
            .replace("{left}", str(left))
            .replace("{right}", str(right)))


def r_random_walk_bench(a, act_id):
    """⊕ c1-05 `#s-walk` — 130 particles, no one steering.

    ⚠️ A LIGHT `.ks3-block`, not a practical. Design draws the tank on cream
    inside a card-ground frame; painting it on ink resolves every text token
    wrong and turns the dye purple-on-black. Same trap the map names for
    c2-01's claim switch.

    ⚖️ **THE TWO CROSSING COUNTERS NEVER RESET WHEN THE TANK EVENS OUT.** They
    are cleared by "Put the drop back" and by nothing else (page lines
    439–440). That is the whole confrontation of `PART-11`: the spreading
    finishes and the moving does not, and a student watching the two numbers
    climb together after "Spread out? Yes" is reading the argument rather than
    being told it. `#s-think`'s reveal then quotes those counters in words. An
    optimisation that zeroed them on `even` would delete the lesson and leave
    an animation.

    ⚠️ THE FOUR NOTES ARE ALL IN THE DOCUMENT AND ONE IS SHOWN. Emit-both-
    show-one, because a note is a science sentence and JS must never rebuild
    one from an attribute — `<em>` would not survive the round trip and a
    string assembled in two places is a string that drifts in one of them.

    ⚠️ The canvas frame here is NOT `_canvas_frame`. That wrapper is the DARK
    one — a 2px `--ks3-on-dark-muted` rule over a `--ks3-dark-panel` foot — and
    this bench is light: a 2px INK rule over a `--ks3-inset` foot. Two grounds,
    two components; reusing the dark one would put an on-dark border on cream.
    """
    n = int(a.get("particles") or 0)
    labels = a.get("labels") or {}
    canvas_labels = a.get("canvas_labels") or {}
    notes = a.get("notes") or {}
    progress = a.get("progress") or {}
    alt = a.get("alt") or {}
    seed = a.get("seed") or {}
    step = a.get("step") or {}
    bounds = a.get("bounds") or {}
    even = a.get("even") or {}

    if n < 2:
        raise ValueError(
            "random-walk-bench %r seeds %d particle(s); the instrument is a "
            "crowd leaving one side and needs a crowd." % (act_id, n))

    need = {
        "labels": (labels, ("cross_right", "cross_left", "even", "even_yes",
                            "even_no", "run_start", "run_pause",
                            "run_continue", "reset", "trace_on", "trace_off",
                            "warm_on", "warm_off")),
        "canvas_labels": (canvas_labels, ("left_half", "right_half",
                                          "profile")),
        # Four branches, and all four are Design's. A missing one would render
        # as an empty panel at exactly the moment the bench has something to
        # say — see `walkNote`, page lines 575–584.
        "notes": (notes, ("idle", "spreading", "even", "tracing")),
        "progress": (progress, ("idle", "spreading", "even")),
        "alt": (alt, ("template", "even", "uneven")),
        "seed": (seed, ("x", "y")),
        "step": (step, ("cool", "warm", "y_scale")),
        "bounds": (bounds, ("x", "y")),
        "even": (even, ("tolerance", "hz")),
    }
    for key, (got, wanted) in sorted(need.items()):
        missing = [k for k in wanted if got.get(k) in (None, "")]
        if missing:
            raise ValueError(
                "random-walk-bench %r is missing %s: %s."
                % (act_id, key, ", ".join(missing)))
    for key in ("trail_max", "bins", "reduced_scale"):
        if not a.get(key):
            raise ValueError(
                "random-walk-bench %r declares no %s." % (act_id, key))

    # ⊕ The block head's readout and `progress.idle` are the SAME WORD in two
    # records — the resting render comes from `head_counter`, the live one from
    # `progress` — so they are checked against each other rather than trusted.
    # Drift here is invisible: the page would open on one word and change to a
    # different one the first time anything is pressed.
    opening = ((a.get("head_counter") or {}).get("start_extra") or {}).get("phase")
    if opening != progress["idle"]:
        raise ValueError(
            "random-walk-bench %r opens its head counter on %r and its live "
            "readout on %r. They are the same readout and must be the same "
            "word." % (act_id, opening, progress["idle"]))

    gate_html, hide = r_bench_gate(a.get("gate"))

    cfg = {"particles": n, "seed": seed, "step": step, "bounds": bounds,
           "even": even, "trail_max": int(a["trail_max"]),
           "bins": int(a["bins"]), "reduced_scale": a["reduced_scale"],
           "canvas_labels": canvas_labels, "alt": alt, "progress": progress}

    def readout(label, inner, extra=""):
        return ('<div class="ks3-walk-readout">'
                '<p class="ks3-walk-readout-label">%s</p>'
                '<p class="ks3-walk-readout-value"%s>%s</p></div>'
                % (t(label), extra, inner))

    # Both words are present and one is hidden — the same rule as the notes.
    # "Yes" and "Not yet" are the answer to the question the gate asked.
    even_words = ('<span data-walk-even-no>%s</span>'
                  '<span data-walk-even-yes hidden>%s</span>'
                  % (t(labels["even_no"]), t(labels["even_yes"])))

    readouts = (readout(labels["cross_right"], "0", " data-walk-cross-right")
                + readout(labels["cross_left"], "0", " data-walk-cross-left")
                + readout(labels["even"], even_words, ' data-walk-even="0"'))

    def swap(attr, pairs, first):
        """A control whose LABEL changes with its state, one span per label."""
        return "".join(
            '<span data-%s="%s"%s>%s</span>'
            % (attr, e(key), "" if key == first else " hidden", t(text))
            for key, text in pairs)

    controls = (
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-run aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-reset>%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-trace aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-warm aria-pressed="false">%s</button>'
        % (swap("run-label", (("start", labels["run_start"]),
                              ("pause", labels["run_pause"]),
                              ("continue", labels["run_continue"])), "start"),
           t(labels["reset"]),
           swap("trace-label", (("on", labels["trace_on"]),
                                ("off", labels["trace_off"])), "on"),
           swap("warm-label", (("on", labels["warm_on"]),
                               ("off", labels["warm_off"])), "on")))

    note_html = "".join(
        '<p data-note="%s"%s>%s</p>'
        % (e(key), "" if key == "idle" else " hidden", rich(notes[key]))
        for key in ("idle", "spreading", "even", "tracing"))

    return (gate_html
            + '<div class="ks3-walk" data-walk%s data-cfg="%s">'
              '<div class="ks3-walk-frame">'
              '<canvas class="ks3-walk-canvas" width="1800" height="640" '
              'role="img" aria-label="%s" data-walk-canvas></canvas>'
              '<div class="ks3-walk-foot">'
              '<div class="ks3-walk-readouts">%s</div>'
              '<div class="ks3-walk-controls">%s</div>'
              '</div></div>'
              # `role="status"` on the note panel, never on the instrument
              # root: the root contains the canvas and the counters, and a live
              # region over a 60 fps drawing announces nothing usable.
              '<div class="ks3-walk-note" data-walk-note role="status">%s</div>'
              '</div>'
            % (hide,
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(_walk_alt(alt, False, n, 0)),
               readouts, controls, note_html))
