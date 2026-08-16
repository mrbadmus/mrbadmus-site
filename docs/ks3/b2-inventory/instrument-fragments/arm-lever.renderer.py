# DISPATCH: "arm-lever": ("ks3-lever-block", ' data-instrument data-leverblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "arm-lever":              r_arm_lever,
#
# Place `r_arm_lever` and the two helpers below beside `r_muscle_pair` in the
# B2 group (build_ks3.py ~3079). Needs `e`, `t`, `r_bench_gate`. No new
# imports: the only arithmetic here is a divide and a round, and
# `int(v + 0.5)` is `math.floor` for a positive v, which every value on this
# rig is (the sliders' floors are 0.5 kg and 3 cm).
#
# ⚠️ `_lever_num` and `_lever_alt` are MODULE-LEVEL, not nested, because the
# RESTING render needs the same formatter and the same composition the runtime
# uses. Two copies of "how is this number written" is two answers to it, and
# the number is on screen before any JS runs.


# Values the rig COMPUTES rather than reads off a control. Both are Design's
# `.toFixed(0)` — a weight and a force are whole newtons on this page.
_LEVER_COMPUTED = {"weight": 0, "force": 0}


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


def _lever_alt(alt, load, ins, hand, force=None):
    """The canvas's aria-label, composed the same way in Python and in JS.

    ⚖️ THE LABEL IS THE WHOLE DRAWING for a screen-reader user: the two
    dimension lines, the load's weight arrow and the joint are painted inside
    the canvas and exist nowhere in the DOM. So every number a sighted student
    can see on the drawing has to be in here.

    ⚠️ AND NOT ONE MORE THAN THAT. `force` is appended only once the meter has
    been fitted — the same gate the muscle tile takes, reached by the other
    route. Handing the answer to a screen-reader user before they have worked
    it out is not an accommodation, it is a different lesson.

    ⚠️ SINGULAR/PLURAL. C1 shipped "after 1 halvings" and it had to be fixed,
    so the guard is here from the start rather than after somebody reads it
    aloud. No control on this rig can currently reach a bare 1 — `load` and
    `ins` render to one decimal ("1.0 kilograms" is correct English) and
    `hand` offers 32 and 16 — but a future payload with `step: 1` on the load
    would, and a plural that only breaks for one authored value is exactly the
    kind of defect that ships.
    """
    out = (alt.get("template", "")
           .replace("{load}", load).replace("{ins}", ins)
           .replace("{hand}", hand))
    if force is not None and alt.get("measured"):
        out += alt["measured"].replace("{force}", force)
    for word in ("kilogram", "centimetre", "newton"):
        out = out.replace(" 1 %ss" % word, " 1 %s" % word)
    return out


def r_arm_lever(a, act_id):
    """⊕ b2-04 `#s-bench` — the forearm rig, and the number it will not give you.

    ⚖️ THE MISSING FOURTH NUMBER IS THE WHOLE INSTRUMENT. The rig hands over
    the load and both distances and refuses the muscle force: the tile reads
    the authored `unmeasured` sentence, and the muscle arrow on the canvas
    carries the bare word "muscle" and deliberately no magnitude. A student
    who could read the force off the rig would never divide anything, and the
    meter exists so they can CHECK their arithmetic rather than skip it.
    That gate is why the meter button is one-way and why fitting it is half
    the rail stop.

    ⚠️ NOT `sim`, and not `joint-bench`. Three measured differences, any one
    of which is fatal:

      * `sim`'s controls are a CLOSED ENUM validated against `SIM_CONTROLS`;
        this rig's three are a mass, an attachment distance and a two-tab
        distance, and none of them is in that list. Adding them would give
        every KS3 sim a "muscle attached at" slider.
      * `joint-bench` reads a per-joint record and paints a linkage; every
        readout it has is a lookup. Every readout here is ARITHMETIC on the
        three live values, and the one that matters is withheld.
      * a mixed control topology — two sliders and an exclusive two-tab set —
        whose product decides four readouts, a canvas and a rail predicate.

    ⚠️ INK-DARK, so every text rule in the stylesheet is scoped `.ks3-dark …`.
    `.ks3-dark p` is (0,1,1) and a bare instrument class is (0,1,0): unscoped,
    the tile labels and the meter note lose and render in on-dark body copy
    against a panel that is not the ground they were coloured for. That is the
    defect B1 shipped with the zoom instrument and B2 was bitten by again.

    ⊕ ADDITIONS inside the drawn component, both stated in the report:
      * `alt.measured` — Design's `benchAlt` never mentions the muscle force,
        so once the meter is fitted a screen-reader user is the only person on
        the page who cannot read it. Appended, and only then.
      * `done_at` — Design hard-codes `>= 2` inside its own rail predicate.
        Authored once here and read by the wiring, so the rail's demand is
        data rather than a number nobody can find.
    """
    controls = a.get("controls") or []
    if not controls:
        raise ValueError("arm-lever %r declares no controls[]." % act_id)

    by_key, decimals = {}, {}
    for c in controls:
        key = c.get("key")
        if not key:
            raise ValueError(
                "arm-lever %r has a control with no `key`; the key is what the "
                "tiles, the canvas and the steps block all name it by."
                % act_id)
        if c.get("options"):
            if c.get("start") not in c["options"]:
                raise ValueError(
                    "arm-lever %r control %r starts at %r, which is not one of "
                    "the tabs it offers (%s)."
                    % (act_id, key, c.get("start"),
                       ", ".join(str(o) for o in c["options"])))
            decimals[key] = 0
        else:
            for bound in ("min", "max", "step"):
                if c.get(bound) is None:
                    raise ValueError(
                        "arm-lever %r control %r is a slider and declares no "
                        "`%s`; a range with an open end renders as a browser "
                        "default and reads any value at all."
                        % (act_id, key, bound))
            if not float(c["min"]) <= float(c["start"]) <= float(c["max"]):
                raise ValueError(
                    "arm-lever %r control %r starts at %r, outside its own "
                    "%r–%r range." % (act_id, key, c.get("start"),
                                      c.get("min"), c.get("max")))
            decimals[key] = _lever_decimals(c.get("step"))
        by_key[key] = c

    tiles = a.get("tiles") or []
    if not tiles:
        raise ValueError("arm-lever %r declares no tiles[]." % act_id)
    for tl in tiles:
        if tl.get("key") not in by_key and tl.get("key") not in _LEVER_COMPUTED:
            raise ValueError(
                "arm-lever %r tile %r reads %r, which is neither a control nor "
                "a computed value (%s). A tile with no source is a box that "
                "never fills." % (act_id, tl.get("label"), tl.get("key"),
                                  ", ".join(sorted(_LEVER_COMPUTED))))

    meter = a.get("meter") or {}
    for key in ("label", "label_done", "note", "note_done"):
        if not meter.get(key):
            raise ValueError(
                "arm-lever %r meter is missing %r. All four are drawn: the "
                "button says two things and the line beside it says two more, "
                "and a missing one leaves the previous state's sentence on "
                "screen after the meter is fitted." % (act_id, key))
    if not a.get("unmeasured"):
        raise ValueError(
            "arm-lever %r declares no `unmeasured` sentence. That string IS "
            "the gate — without it the force tile would open empty and the "
            "block would look broken rather than withholding." % act_id)

    canvas = a.get("canvas") or {}
    for key in ("title", "joint", "muscle", "load"):
        if not canvas.get(key):
            raise ValueError(
                "arm-lever %r canvas is missing %r." % (act_id, key))
    alt = a.get("alt") or {}
    if not alt.get("template"):
        raise ValueError(
            "arm-lever %r has no alt template; the dimension lines, the weight "
            "arrow and the joint are painted on the canvas and reach a screen "
            "reader through nothing else." % act_id)

    done_at = int(a.get("done_at") or 0)
    if not 1 <= done_at <= len(controls):
        raise ValueError(
            "arm-lever %r ticks its rail stop at %r control(s) moved; it "
            "offers %d. A stop that cannot be reached is worse than none."
            % (act_id, a.get("done_at"), len(controls)))

    g = float(a.get("g") or 0)
    if g <= 0:
        raise ValueError(
            "arm-lever %r declares g = %r N/kg. The whole page's arithmetic "
            "runs through it." % (act_id, a.get("g")))

    # ── the resting state, computed here so the page is never a set of empty
    # boxes for the instant before the wiring runs ──
    start = {k: float(c["start"]) for k, c in by_key.items()}
    weight = start["load"] * g
    values = {"weight": weight, "force": weight * start["hand"] / start["ins"]}

    def readout(key, fmt):
        if key in _LEVER_COMPUTED:
            return _lever_num(values[key], _LEVER_COMPUTED[key], fmt)
        return _lever_num(start[key], decimals[key], fmt)

    rows = []
    for c in controls:
        key = c["key"]
        cid = "%s-%s" % (act_id, key)
        if c.get("options"):
            tabs = "".join(
                '<button type="button" class="ks3-sim-seg-btn ks3-lever-tab" '
                'data-lever-tab="%s" data-value="%s" aria-pressed="%s">%s'
                '</button>'
                % (e(key), e(o), "true" if float(o) == start[key] else "false",
                   t(_lever_num(o, decimals[key], c.get("format"))))
                for o in c["options"])
            rows.append('<div class="ks3-lever-control">'
                        '<p class="ks3-lever-label">%s</p>'
                        '<div class="ks3-lever-tabs">%s</div></div>'
                        % (t(c.get("label", "")), tabs))
            continue
        # ⚠️ The <label> is real and its `for` reaches a real id. A slider
        # whose only name is the paragraph above it is unnamed to a screen
        # reader, and this one is the difference between two distances.
        rows.append(
            '<div class="ks3-lever-control">'
            '<div class="ks3-lever-row">'
            '<label class="ks3-lever-label" for="%s">%s</label>'
            '<p class="ks3-lever-value" data-lever-value="%s" '
            'data-format="%s">%s</p></div>'
            '<input class="ks3-slider ks3-lever-slider" type="range" id="%s" '
            'min="%s" max="%s" step="%s" value="%s" data-lever-input="%s">'
            '</div>'
            % (e(cid), t(c.get("label", "")), e(key),
               e(c.get("format") or "{n}"),
               t(readout(key, c.get("format"))), e(cid),
               e(c["min"]), e(c["max"]), e(c["step"]), e(c["start"]), e(key)))

    cells = []
    for tl in tiles:
        key = tl["key"]
        # The force tile opens on the withheld sentence, not on a number.
        value = (a["unmeasured"] if key == "force"
                 else readout(key, tl.get("format")))
        cells.append('<div class="ks3-lever-tile">'
                     '<p class="ks3-lever-tile-label">%s</p>'
                     '<p class="ks3-lever-tile-value%s" data-lever-out="%s" '
                     'data-format="%s">%s</p></div>'
                     % (t(tl.get("label", "")),
                        " ks3-lever-tile-mono" if tl.get("mono") else "",
                        e(key), e(tl.get("format") or "{n}"), t(value)))

    gate_html, hide = r_bench_gate(a.get("gate"))

    return (gate_html
            + '<div class="ks3-lever" data-lever%s data-rig="%s" data-g="%s" '
              'data-done-at="%d" data-load="%s" data-ins="%s" data-hand="%s" '
              'data-dp-load="%d" data-dp-ins="%d" data-dp-hand="%d" '
              'data-unmeasured="%s" data-alt="%s" data-alt-measured="%s" '
              'data-canvas-title="%s" data-canvas-joint="%s" '
              'data-canvas-muscle="%s" data-canvas-load="%s" '
              'data-meter-label="%s" data-meter-done="%s" '
              'data-meter-note="%s" data-meter-note-done="%s">'
              '<div class="ks3-lever-controls">%s</div>'
              '<div class="ks3-lever-stage">'
              '<canvas class="ks3-lever-canvas" width="1800" height="700" '
              'role="img" aria-label="%s" data-lever-canvas></canvas></div>'
              '<div class="ks3-lever-tiles">%s</div>'
              '<div class="ks3-lever-foot">'
              '<button type="button" class="ks3-sim-seg-btn ks3-lever-meter" '
              'data-lever-meter>%s</button>'
              '<p class="ks3-lever-note" data-lever-note role="status">%s</p>'
              '</div></div>'
            % (hide, e(act_id), e(a["g"]), done_at,
               e(start["load"]), e(start["ins"]), e(start["hand"]),
               decimals["load"], decimals["ins"], decimals["hand"],
               e(a["unmeasured"]), e(alt.get("template", "")),
               e(alt.get("measured", "")),
               e(canvas["title"]), e(canvas["joint"]), e(canvas["muscle"]),
               e(canvas["load"]),
               e(meter["label"]), e(meter["label_done"]),
               e(meter["note"]), e(meter["note_done"]),
               "".join(rows),
               e(_lever_alt(alt,
                            _lever_num(start["load"], decimals["load"], "{n}"),
                            _lever_num(start["ins"], decimals["ins"], "{n}"),
                            _lever_num(start["hand"], decimals["hand"], "{n}"))),
               "".join(cells),
               t(meter["label"]), t(meter["note"])))
