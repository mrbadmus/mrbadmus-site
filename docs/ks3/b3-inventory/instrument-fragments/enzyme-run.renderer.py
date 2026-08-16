# DISPATCH: "enzyme-run": ("ks3-erun-block", ' data-instrument data-erunblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "enzyme-run":             r_enzyme_run,
#
# Place `r_enzyme_run` and `_erun_rate` beside `r_gut_journey`. Needs `e`, `t`,
# `rich` and `json`, all of which build_ks3.py already imports or defines.
#
# ⚠️ THE ONLY TIMER IN THE UNIT. NOTES-B3 §6 says so in as many words:
# "`enzyme-run` is the only one with a timer. Nothing else in the unit
# animates." That is why this is the one B3 fragment with a reduced-motion
# contract to honour, and why `reduced_motion_scale` is authored rather than
# assumed.


def _erun_rate(model, temp, ph, opt_ph):
    """The rate curve, as a fraction of maximum — Design's own model.

    ⚠️ `rateFor()` in `shared/ks3.js` is THIS FUNCTION, and the two must agree
    exactly. It exists in Python for one reason: the resting page has to print
    the same rate the first repaint computes, or the number visibly jumps on
    load and the shipped HTML — which is what a crawler and a reader with JS
    off get — carries a figure the instrument disagrees with. Same reason
    `heating-bench` duplicates its rounding rule.

    It is deliberately not a second MODEL: every constant comes from the
    authored `model` dict, so a corrected curve is one data edit and the two
    evaluations move together.
    """
    denature = float(model["denature_c"])
    if temp >= denature:
        return 0.0
    opt = float(model["optimum_c"])
    if temp <= opt:
        t_term = (temp / opt) ** float(model["rise_exponent"]) if opt else 0.0
    else:
        t_term = max(0.0, 1.0 - ((temp - opt) / float(model["fall_divisor"])) ** 2)
    gap = abs(float(ph) - float(opt_ph))
    p_term = max(0.0, 1.0 - gap / float(model["ph_span"]))
    return max(0.0, min(1.0, t_term * p_term))


def _erun_band(bands, denatured, temp, denature_c):
    """Which of the six temperature notes is showing, at rest.

    Same branch order as `noteFor()` in shared/ks3.js, for the same reason
    `_erun_rate` exists: the note on the shipped page must be the note the
    first repaint chooses.
    """
    if denatured and temp >= denature_c:
        return "denatured_hot"
    if denatured:
        return "denatured_cool"
    if temp >= bands["past_optimum"]:
        return "past_optimum"
    if temp >= bands["optimum"]:
        return "optimum"
    if temp >= bands["cold"]:
        return "cold"
    return "freezing"


def r_enzyme_run(a, act_id):
    """⊕ b3-06 `#s-bench` — three counters, and one of them never moves.

    ⚖️ THE THIRD COUNTER IS THE LESSON. NOTES-B3 §2 puts it in one line: "a
    running reaction with three counters, one of which never moves. That
    counter *is* the lesson." So the enzyme count is emitted as an authored
    STRING with a full-width bar and NO `data-value` and NO `data-bar` handle
    for the runtime to take hold of. It is the same construction as
    `heating-bench`'s mass tile, and for the same reason: the one number the
    prose says must not move is wired to nothing, so it cannot move even by
    accident.

    ⚖️ THE DENATURE LATCH IS THE OTHER HALF, and it is the misconception the
    block exists to kill. Heat past the threshold and the enzyme is finished;
    cooling does not bring it back, switching enzyme does not bring it back
    while the tube is still hot, and only a fresh tube clears it. The latch
    fires on the TEMPERATURE control rather than inside the run tick —
    NOTES-B3 flag 16 records that a student who dragged to 60 °C, read 0%, and
    dragged back to 37 °C used to be shown a full recovery, so the instrument
    built to kill the idea was demonstrating it.

    ⚠️ ONE THRESHOLD, AUTHORED ONCE. `model.denature_c` is quoted in the key
    fact, in two of the six temperature notes, in the key note, in a ladder
    correction and in the stretch layer. It reaches the runtime through
    `data-cfg` and the prose through the lesson record; there is exactly one
    number, and the module docstring lists every sentence that repeats it.

    ⚠️ EVERY BRANCHING SENTENCE IS IN THE DOCUMENT. Six temperature notes and
    three verdicts, all nine emitted, eight hidden — emit-all-show-one. None is
    assembled in JS from an attribute, so the em dashes, right single quotes
    and degree signs survive and a science correction is a data edit. Only two
    live numbers are ever substituted: the tick count and the rate percentage.

    ⊕ ADDED INSIDE A COMPONENT DESIGN DREW, where the page is silent. Design
    shows the verdict on `clock >= ticks || (everRan && !running && denatured)`.
    A run at a rate of exactly zero that is NOT denatured — stomach protease
    dropped into pH 8, which is one press of one button — finishes on its first
    tick and shows no verdict at all: the bench goes quiet and says nothing,
    and the "slow" verdict that exists to send the student back to the pH dial
    never appears. The wiring shows the verdict whenever a run has FINISHED,
    whatever finished it. Design's three branches are unchanged.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    Here the rate readout and the temperature figure are what would visibly
    break: amber mono is how a student reads a dial, and unscoped they fall to
    on-dark body copy and stop looking like numbers.

    ⚑ FOR MIDE, recorded here as well as in the lesson module: the enzyme
    counter's bar is `--ks3-ok`. That token's own comment in `tokens.css`
    reserves green for the ladder marking correctness, and this is a bar
    meaning "unchanged" on a block that marks nothing. Design drew it; it is
    reproduced as drawn and registered in a parity row, so the day the palette
    question is ruled the gate says exactly where the value lives. Same
    handling as `scale-cards`' amber distance label.
    """
    enzymes = a.get("enzymes") or []
    phs = a.get("phs") or []
    if len(enzymes) < 2:
        raise ValueError(
            "enzyme-run %r declares %d enzyme(s). One cannot show that each "
            "has its own substrate and its own best pH." % (act_id, len(enzymes)))
    if len(phs) < 2:
        raise ValueError(
            "enzyme-run %r offers %d pH setting(s); the pH dial is half the "
            "bench." % (act_id, len(phs)))

    for z in enzymes:
        missing = [k for k in ("id", "label", "equation", "counter_substrate",
                               "counter_product") if not z.get(k)]
        if missing:
            raise ValueError(
                "enzyme-run %r enzyme %r is missing %s. The counter names are "
                "authored per enzyme rather than built from a substrate word, "
                "because 'Fatty acids and glycerol made' is a sentence and not "
                "a capitalisation." % (act_id, z.get("id"), ", ".join(missing)))
        if z.get("opt_ph") is None:
            raise ValueError(
                "enzyme-run %r enzyme %r declares no opt_ph; the pH term is "
                "the gap to it." % (act_id, z["id"]))

    for p in phs:
        if p.get("value") is None or not p.get("label"):
            raise ValueError(
                "enzyme-run %r pH setting %r needs both `value` and `label`."
                % (act_id, p))

    model = a.get("model") or {}
    for key in ("denature_c", "optimum_c", "rise_exponent", "fall_divisor",
                "ph_span"):
        if model.get(key) is None:
            raise ValueError(
                "enzyme-run %r model is missing %r. The curve is a simplified "
                "model and all five constants are authored, so the legal line "
                "can say so truthfully." % (act_id, key))

    run = a.get("run") or {}
    for key in ("ticks", "tick_ms", "units_per_tick", "start_substrate",
                "reduced_motion_scale", "slow_below_pct"):
        if run.get(key) is None:
            raise ValueError("enzyme-run %r run is missing %r." % (act_id, key))
    labels = run.get("labels") or {}
    for key in ("start", "more", "running", "reset", "clock", "clock_fresh",
                "rate"):
        if not labels.get(key):
            raise ValueError(
                "enzyme-run %r run.labels is missing %r." % (act_id, key))
    if "{n}" not in labels["clock"] or "{total}" not in labels["clock"]:
        raise ValueError(
            "enzyme-run %r run.labels['clock'] is %r; it carries both live "
            "numbers and needs {n} and {total}." % (act_id, labels["clock"]))
    if "{pct}" not in labels["rate"]:
        raise ValueError(
            "enzyme-run %r run.labels['rate'] is %r and carries no {pct}."
            % (act_id, labels["rate"]))

    units = a.get("units_format")
    if not units or "{n}" not in units:
        raise ValueError(
            "enzyme-run %r units_format is %r; the counter values are authored "
            "copy and carry the live count as {n}." % (act_id, units))
    if not a.get("enzyme_counter_label") or not a.get("enzyme_counter_value"):
        raise ValueError(
            "enzyme-run %r needs enzyme_counter_label and "
            "enzyme_counter_value. The third counter's value is a CONSTANT "
            "string — it is the one readout nothing may compute." % act_id)

    # ⚠️ SIX BRANCHES, ALL NAMED. The wiring chooses among these keys and
    # nothing else; a missing one leaves the note blank at exactly the
    # temperature the student dragged to.
    notes = a.get("temp_notes") or {}
    for key in ("denatured_hot", "denatured_cool", "past_optimum", "optimum",
                "cold", "freezing"):
        if not notes.get(key):
            raise ValueError(
                "enzyme-run %r temp_notes is missing %r. Both denatured "
                "branches are required and they say different things: "
                "'cool it, then take a fresh tube' has to be distinguishable "
                "from 'cooling changes nothing'." % (act_id, key))
    bands = a.get("temp_bands") or {}
    for key in ("past_optimum", "optimum", "cold"):
        if bands.get(key) is None:
            raise ValueError(
                "enzyme-run %r temp_bands is missing %r." % (act_id, key))

    verdicts = a.get("verdicts") or {}
    for key in ("denatured", "slow", "worked"):
        if not verdicts.get(key):
            raise ValueError(
                "enzyme-run %r verdicts is missing %r. Three branches are "
                "drawn and the denatured one is the block's whole argument."
                % (act_id, key))

    groups = a.get("group_labels") or {}
    for key in ("enzyme", "ph", "temp"):
        if not groups.get(key):
            raise ValueError(
                "enzyme-run %r group_labels is missing %r." % (act_id, key))

    temp = a.get("temp") or {}
    for key in ("min", "max", "start", "step", "format", "field_label"):
        if temp.get(key) is None:
            raise ValueError("enzyme-run %r temp is missing %r." % (act_id, key))
    if "{t}" not in temp["format"]:
        raise ValueError(
            "enzyme-run %r temp['format'] is %r and carries no {t}."
            % (act_id, temp["format"]))

    start_ph = a.get("start_ph", phs[0]["value"])
    if start_ph not in [p["value"] for p in phs]:
        raise ValueError(
            "enzyme-run %r opens at pH %r, which is not one of the %d offered."
            % (act_id, start_ph, len(phs)))

    cfg = {
        "denature_c": model["denature_c"],
        "optimum_c": model["optimum_c"],
        "rise_exponent": model["rise_exponent"],
        "fall_divisor": model["fall_divisor"],
        "ph_span": model["ph_span"],
        "ticks": run["ticks"],
        "tick_ms": run["tick_ms"],
        "units_per_tick": run["units_per_tick"],
        "start_substrate": run["start_substrate"],
        "reduced_motion_scale": run["reduced_motion_scale"],
        "slow_below_pct": run["slow_below_pct"],
        "temp_format": temp["format"],
        "units_format": units,
        "bands": {"past_optimum": bands["past_optimum"],
                  "optimum": bands["optimum"], "cold": bands["cold"]},
        "labels": dict(labels),
        "opt_ph": {z["id"]: z["opt_ph"] for z in enzymes},
    }

    # The resting readouts, from the same constants the runtime uses.
    rest_rate = int(round(_erun_rate(model, float(temp["start"]), start_ph,
                                     enzymes[0]["opt_ph"]) * 100))
    rest_note = _erun_band(bands, False, float(temp["start"]),
                           float(model["denature_c"]))
    field = "erun-temp-%s" % act_id

    ztabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-erun-enzyme" '
        'data-enzyme="%s" aria-pressed="%s">%s</button>'
        % (e(z["id"]), "true" if i == 0 else "false", t(z["label"]))
        for i, z in enumerate(enzymes))

    ptabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-erun-ph" '
        'data-ph="%s" aria-pressed="%s">%s</button>'
        % (e(p["value"]), "true" if p["value"] == start_ph else "false",
           t(p["label"]))
        for p in phs)

    # One equation per enzyme, all in the document. `t()` DRAWS the arrow:
    # U+2192 is absent from all five latin woff2 subsets, and typed as a
    # character it drops to a system font mid-line.
    equations = "".join(
        '<span class="ks3-erun-equation" data-enzyme="%s"%s>%s</span>'
        % (e(z["id"]), "" if i == 0 else " hidden", t(z["equation"]))
        for i, z in enumerate(enzymes))

    def names(key):
        return "".join(
            '<span class="ks3-erun-countername" data-enzyme="%s"%s>%s</span>'
            % (e(z["id"]), "" if i == 0 else " hidden", t(z[key]))
            for i, z in enumerate(enzymes))

    counters = (
        '<li class="ks3-erun-counter" data-counter="substrate">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue" data-value="substrate">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar" data-bar="substrate" style="width:100%%">'
        '</span></span></li>'
        '<li class="ks3-erun-counter" data-counter="product">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue" data-value="product">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar" data-bar="product" style="width:0%%">'
        '</span></span></li>'
        # ⚖️ NO HANDLE. No `data-value`, no `data-bar` — the counter the prose
        # says must not move has nothing for the runtime to take hold of.
        '<li class="ks3-erun-counter" data-counter="enzyme">'
        '<div class="ks3-erun-counterhead">'
        '<p class="ks3-erun-counterlabel">%s</p>'
        '<p class="ks3-erun-countervalue">%s</p></div>'
        '<span class="ks3-erun-track">'
        '<span class="ks3-erun-bar ks3-erun-bar-fixed" style="width:100%%">'
        '</span></span></li>'
        % (names("counter_substrate"),
           t(units.replace("{n}", str(run["start_substrate"]))),
           names("counter_product"), t(units.replace("{n}", "0")),
           t(a["enzyme_counter_label"]), t(a["enzyme_counter_value"])))

    tnotes = "".join(
        '<span class="ks3-erun-tempnote" data-note="%s"%s>%s</span>'
        % (key, "" if key == rest_note else " hidden", rich(notes[key]))
        for key in ("denatured_hot", "denatured_cool", "past_optimum",
                    "optimum", "cold", "freezing"))

    vnotes = "".join(
        '<span class="ks3-erun-verdicttext" data-verdict="%s" hidden>%s</span>'
        % (key, rich(verdicts[key]))
        for key in ("denatured", "slow", "worked"))

    return ('<div class="ks3-erun" data-erun data-cfg="%s">'
            '<div class="ks3-erun-dials">'
            '<div class="ks3-erun-dial"><p class="ks3-erun-diallabel">%s</p>'
            '<div class="ks3-erun-seg">%s</div></div>'
            '<div class="ks3-erun-dial"><p class="ks3-erun-diallabel">%s</p>'
            '<div class="ks3-erun-seg">%s</div></div></div>'

            '<div class="ks3-erun-temp">'
            '<div class="ks3-erun-temphead">'
            '<p class="ks3-erun-diallabel">%s</p>'
            '<p class="ks3-erun-tempvalue" data-temp-value>%s</p></div>'
            '<label class="ks3-erun-srlabel" for="%s">%s</label>'
            '<input class="ks3-erun-slider" type="range" id="%s" min="%s" '
            'max="%s" step="%s" value="%s" data-temp aria-valuetext="%s">'
            '<p class="ks3-erun-tempnotes" data-tempnotes role="status">%s</p>'
            '</div>'

            '<div class="ks3-erun-tube">'
            '<div class="ks3-erun-tubehead">'
            '<p class="ks3-erun-reaction">%s</p>'
            '<p class="ks3-erun-rate" data-rate>%s</p></div>'
            '<ul class="ks3-erun-counters" role="list">%s</ul>'
            '<div class="ks3-erun-controls">'
            '<button type="button" class="ks3-reveal-btn ks3-erun-run" '
            'data-run>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-erun-reset" '
            'data-reset>%s</button>'
            '<span class="ks3-erun-clock" data-clock>%s</span></div>'
            '<p class="ks3-erun-verdict" hidden data-reveal>%s</p>'
            '</div></div>'
            % (e(json.dumps(cfg, sort_keys=True)),
               t(groups["enzyme"]), ztabs, t(groups["ph"]), ptabs,
               t(groups["temp"]),
               t(temp["format"].replace("{t}", str(temp["start"]))),
               e(field), t(temp["field_label"]), e(field),
               e(temp["min"]), e(temp["max"]), e(temp["step"]),
               e(temp["start"]),
               e(temp["format"].replace("{t}", str(temp["start"]))),
               tnotes, equations,
               t(labels["rate"].replace("{pct}", str(rest_rate))),
               counters, t(labels["start"]), t(labels["reset"]),
               t(labels["clock_fresh"]), vnotes))
