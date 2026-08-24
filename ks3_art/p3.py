"""ks3_art.p3 — P3 *Describing motion*, the unit that makes a speed.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p3/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the drawing is measured and the note is reported.

── ⚖️ MRB-204 · ONE TRIANGLE IN THE UNIT, AND NO BEAM ──────────────────────

    p3-01  s = d ÷ t          rearranges to d = s × t   a PRODUCT   TRIANGLE
    p3-02  no formula figure — the speed is a GRADIENT read off a line,
           not a quantity computed from a rule
    p3-03  no formula figure — 30 + 30 = 60 and 25 − 20 = 5 are a SUM and
           a DIFFERENCE, and a triangle over either teaches a relationship
           that does not exist

`p3-03` is the lesson where getting this wrong would have been easiest,
because `p3-01` two lessons earlier has a triangle and the habit is to carry
it forward. Design draws none — "triangle" appears zero times on her page
— and `r_passing_speeds` asserts that every one of its four `sum` strings
is an addition or a subtraction, so a later edit cannot slip a product in
under a shape that could not hold one.

No beam either: a beam is for a sum that BALANCES (`total before = total
after`, as `p1-03` and `p2-04` use it). A relative speed is a combination,
not an equality, so neither figure fits and the lesson carries none.

── ⚖️ THE QUANTITATIVE FAMILY PATTERN, ENFORCED ───────────────────────────

Design's `NOTES-P3.md` §1 defines the family here, and its load-bearing step
is: *the instrument produces raw measurements and refuses to do the
arithmetic.* `r_light_gates` REQUIRES the third readout — the one that
reads "not measured — you work it out" — because an instrument that
hands over the answer has removed the lesson.

── ⚠️ THE PLOTTING GRID IS REAL BUTTONS, NOT CANVAS HIT-TESTING ──────────

Design's "For Code" §6, and she is right that this is the one that gets lost
silently: *"If that is re-implemented as canvas clicks during the port, it
will silently drop keyboard access — the R15 failure will not show up in
a screenshot."* Every intersection is a real `<button>` with a coordinate
name, and `r_graph_plot` asserts the count against the grid.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` itself with NO
opt-out. Nothing here uses `cards`, `sim` or `scorecards`; `fifa` appears
only on `worked-example` activities, which is the kind that branch draws.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279. Checked before writing: `ks3-
jmatch-block` was already taken by another unit, so this one's journey
matcher renders into `ks3-jwalk-block`.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

from ks3_art.kit import e, rich, t


# ═══ shared P3 primitives ════════════════════════════════════════════════

def _p3_seg(cls, label, pressed=False, **attrs):
    """A segmented-control button, the shape every P3 control picks from."""
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _unique_ids(rows, act_id, family, what):
    seen, dupes = set(), []
    for r in rows:
        rid = r.get("id")
        if rid in seen:
            dupes.append(rid)
        seen.add(rid)
    if dupes:
        raise ValueError(
            "%s %r has two %ss with id %s. The second is unreachable and the "
            "failure is silent." % (family, act_id, what, sorted(set(dupes))))


def _gate(act_id, family, gate, hook):
    """The commit gate every P3 bench opens behind."""
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "%s %r has no commit gate. A bench read before a commitment "
            "confirms whatever the student already believed."
            % (family, act_id))
    opts = "".join(
        '<button type="button" class="ks3-option" data-%s-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (hook, i, chr(65 + i), t(o))
        for i, o in enumerate(gate["options"]))
    return ('<div class="ks3-%s-gate" data-%s-gate><p class="ks3-commit">%s'
            '</p><ul class="ks3-options">%s</ul></div>'
            % (hook, hook, t(gate["prompt"]), opts))


# ═══ p3-01 · #s-track · the light gates ══════════════════════════════════

def r_light_gates(a, act_id):
    """⊕ p3-01 `#s-track` — two beams, a distance and a time. No speed.

    ⚖️ **THE THIRD READOUT IS THE FAMILY PATTERN, AND IT IS ASSERTED.**
    Design's `NOTES-P3.md` §1 step (2): the instrument produces raw
    measurements and REFUSES to do the arithmetic. The third tile reads
    "speed — not measured — you work it out". An instrument that
    hands the answer over has removed the lesson, so this renderer refuses
    a payload whose `speed` readout carries a computed value.

    ⚖️ **THE TIMER RUNS ONLY BETWEEN THE BEAMS.** It starts at gate A and
    freezes at gate B — which is what makes the reading a speed over a
    KNOWN distance rather than over the whole runway.

    ⚖️ **THE RUNS SCATTER, AND THE SCATTER IS SYMMETRIC.** Unlike p1-08's
    lever bench — where friction makes the error one-directional and a
    symmetric scatter would show energy appearing from nowhere — a
    release-to-release variation here genuinely goes both ways. Rung 3 asks
    for the MEAN of three times, which only makes sense if they can fall
    either side.

    HOOKS: `data-lgate` (wrapper, `data-scatter`, `data-target`) ·
    `data-lgate-gate` · `data-lgate-gopt` · `data-lgate-bench` ·
    `data-lgate-ramp` (valued with the ramp index, carrying `data-v`) ·
    `data-lgate-gap` (the slider) · `data-lgate-release` ·
    `data-lgate-record` · `data-lgate-out` (valued with the readout id) ·
    `data-lgate-rows` · `data-lgate-close`.
    """
    ramps = a.get("ramps") or []
    outs_spec = a.get("readouts") or []
    cols = a.get("columns") or []

    if len(ramps) < 2:
        raise ValueError(
            "light-gates %r offers %d ramp(s). The gate's commit asks what "
            "happens to the TIME when the ramp is raised, which needs at "
            "least two heights to answer." % (act_id, len(ramps)))
    _unique_ids(ramps, act_id, "light-gates", "ramp")
    for r in ramps:
        if float(r.get("speed_ms") or 0) <= 0:
            raise ValueError(
                "light-gates %r ramp %r has no positive speed."
                % (act_id, r.get("id")))

    # ⚖️ THE INSTRUMENT MUST NOT DO THE DIVISION. See the ruling above.
    speed_out = None
    for o in outs_spec:
        if o.get("id") == "speed":
            speed_out = o
    if speed_out is None:
        raise ValueError(
            "light-gates %r has no `speed` readout. Design draws a third "
            "tile that says the speed is NOT measured, and it is the whole "
            "QUANTITATIVE family pattern: the student does the division."
            % act_id)
    val = (speed_out.get("value") or "")
    if not val or any(ch.isdigit() for ch in val):
        raise ValueError(
            "light-gates %r gives its `speed` readout the value %r. That "
            "tile must say the speed has NOT been measured — an "
            "instrument that hands over the answer has removed the lesson "
            "(NOTES-P3 §1 step 2)." % (act_id, val))

    lo = float(a.get("gap_min") or 0)
    hi = float(a.get("gap_max") or 0)
    step = float(a.get("gap_step") or 0)
    start = float(a.get("gap_start") or 0)
    if not (0 < lo < hi) or step <= 0 or not (lo <= start <= hi):
        raise ValueError(
            "light-gates %r has an unusable gate separation range "
            "%r..%r step %r start %r." % (act_id, lo, hi, step, start))

    picks = "".join(
        _p3_seg("ks3-seg-btn", r["label"],
                pressed=(i == int(a.get("start_ramp") or 0)),
                data_lgate_ramp=i, data_v=float(r["speed_ms"]))
        for i, r in enumerate(ramps))

    outs = "".join(
        '<div class="ks3-lgate-out"><p class="ks3-lgate-outlabel">%s</p>'
        '<p class="ks3-lgate-outval%s" data-lgate-out="%s">%s</p></div>'
        % (t(o["label"]),
           " is-unmeasured" if o.get("id") == "speed" else "",
           e(o["id"]), t(o.get("value", "")))
        for o in outs_spec)

    heads = "".join('<th scope="col">%s</th>' % t(c) for c in cols)

    return ('<div class="ks3-lgate" data-lgate data-scatter="%s" '
            'data-target="%d">%s'
            '<div class="ks3-lgate-bench" data-lgate-bench hidden>'
            '<div class="ks3-lgate-ramps" role="group" '
            'aria-label="Ramp height">%s</div>'
            '<div class="ks3-lgate-track" role="img" aria-label="%s">'
            '<span class="ks3-lgate-slope" aria-hidden="true"></span>'
            '<span class="ks3-lgate-trolley" data-lgate-trolley '
            'aria-hidden="true"></span>'
            '<span class="ks3-lgate-beam is-a" aria-hidden="true"></span>'
            '<span class="ks3-lgate-beam is-b" data-lgate-beamb '
            'aria-hidden="true"></span></div>'
            '<label class="ks3-lgate-sliderlabel" for="%s-g">'
            'Gate separation · <span data-lgate-gaplabel></span></label>'
            '<input class="ks3-lgate-slider" id="%s-g" type="range" '
            'min="%s" max="%s" step="%s" value="%s" data-lgate-gap>'
            '<div class="ks3-lgate-outs">%s</div>'
            '<div class="ks3-lgate-acts">'
            '<button type="button" class="ks3-seg-btn" data-lgate-release>'
            '%s</button>'
            '<button type="button" class="ks3-seg-btn" data-lgate-record '
            'disabled>%s</button></div>'
            '<div class="ks3-lgate-tablewrap">'
            '<table class="ks3-lgate-table"><thead><tr>%s</tr></thead>'
            '<tbody data-lgate-rows></tbody></table></div>'
            '<p class="ks3-lgate-close" data-lgate-close hidden>%s</p>'
            '</div></div>'
            % (float(a.get("scatter_pct") or 3),
               int(a.get("runs_to_record") or 3),
               _gate(act_id, "light-gates", a.get("gate") or {}, "lgate"),
               picks, e(a.get("alt", "")), e(act_id), e(act_id),
               lo, hi, step, start, outs,
               t(a.get("release_label") or "Release the trolley"),
               t(a.get("record_label") or "Record this run"),
               heads, rich(a.get("close") or "")))


# ═══ p3-01 · #s-compare · three pairs ════════════════════════════════════

def r_compare_pairs(a, act_id):
    """⊕ p3-01 `#s-compare` — two things, and the eye gets it wrong.

    ⚖️ **ONE PAIR MUST BE A DEAD HEAT.** Design's pair 3 is 72 km/h against
    20 m/s, and it is the pair that forces the conversion: without a "they
    are the same" option a student can pick either and never discover that
    the two numbers were not comparable. The renderer requires at least one
    pair whose answer is `same`.

    ⚖️ **THE SUM IS REVEALED, NOT THE VERDICT FIRST.** Choosing shows the
    arithmetic for BOTH sides before it shows why — so the student reads
    two numbers rather than a mark.

    HOOKS: `data-spair` (wrapper, `data-target`) · `data-spair-row` (valued
    with the pair id, carrying `data-answer`) · `data-spair-pick` (valued
    `a`/`b`/`same`) · `data-spair-sums` · `data-spair-why` ·
    `data-spair-close`.
    """
    pairs = a.get("pairs") or []
    if len(pairs) < 2:
        raise ValueError(
            "compare-pairs %r has %d pair(s). The block's claim is that the "
            "eye is unreliable MORE THAN ONCE." % (act_id, len(pairs)))
    _unique_ids(pairs, act_id, "compare-pairs", "pair")

    if not any(p.get("answer") == "same" for p in pairs):
        raise ValueError(
            "compare-pairs %r has no dead heat. Design's third pair is "
            "72 km/h against 20 m/s, and it is the only thing that forces "
            "the unit conversion: with every pair having a winner, a student "
            "can guess and never learn that two speeds in different units "
            "are not comparable." % act_id)

    for p in pairs:
        if p.get("answer") not in ("a", "b", "same"):
            raise ValueError(
                "compare-pairs %r pair %r has answer %r; expected 'a', 'b' "
                "or 'same'." % (act_id, p.get("id"), p.get("answer")))
        if not p.get("sums") or not p.get("why"):
            raise ValueError(
                "compare-pairs %r pair %r is missing its `sums` or its "
                "`why`. The arithmetic is what makes this a measurement "
                "rather than a guess." % (act_id, p.get("id")))

    same_label = a.get("same_label") or "A dead heat"
    rows = "".join(
        '<li class="ks3-spair-row" data-spair-row="%s" data-answer="%s" '
        'data-sums="%s" data-why="%s">'
        '<p class="ks3-spair-label">%s</p>'
        '<div class="ks3-spair-picks">'
        '<button type="button" class="ks3-seg-btn" data-spair-pick="a" '
        'aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-seg-btn" data-spair-pick="same" '
        'aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-seg-btn" data-spair-pick="b" '
        'aria-pressed="false">%s</button></div>'
        '<p class="ks3-spair-sums" data-spair-sums hidden></p>'
        '<p class="ks3-spair-why" data-spair-why hidden></p></li>'
        % (e(p["id"]), e(p["answer"]), e(p["sums"]), e(p["why"]),
           t(p.get("label", "")), t(p["a"]), t(same_label), t(p["b"]))
        for p in pairs)

    return ('<div class="ks3-spair" data-spair data-target="%d">'
            '<ul class="ks3-spair-list" role="list">%s</ul>'
            '<p class="ks3-spair-close" data-spair-close hidden>%s</p>'
            '</div>' % (len(pairs), rows, rich(a.get("close") or "")))


# ═══ p3-02 · #s-plot · plot the readings ═════════════════════════════════

def r_graph_plot(a, act_id):
    """⊕ p3-02 `#s-plot` — a grid of REAL BUTTONS, one per intersection.

    ⚖️ **BUTTONS, NOT CANVAS HIT-TESTING, AND THIS IS THE ONE THAT GETS
    LOST SILENTLY.** Design's "For Code" §6: re-implementing this as clicks
    on a canvas drops every keyboard and screen-reader user, and *"the R15
    failure will not show up in a screenshot"*. Each button carries its own
    coordinates as its accessible name. The renderer asserts the button
    count equals `len(t_values) × len(d_values)` so a later
    "optimisation" cannot quietly thin the grid.

    ⚖️ **A WRONG TAP GETS A LOCATION, NOT A MARK (R3).** The wiring reports
    the coordinates of the cell the student actually chose, in the graph's
    own units. That is a statement about where they tapped, and it leaves
    the verdict to them.

    ⚖️ **EVERY DATUM MUST LIE ON THE GRID.** A reading that falls between
    two intersections cannot be plotted with buttons at all, and the block
    would render a grid the task cannot be completed on.

    HOOKS: `data-gplot` (wrapper, `data-target`) · `data-gplot-cell`
    (valued `<t>,<d>`) · `data-gplot-seek` · `data-gplot-join` ·
    `data-gplot-line` · `data-gplot-read` (valued with the read id) ·
    `data-gplot-opt` · `data-gplot-why` · `data-gplot-close`.
    """
    ts = a.get("t_values") or []
    ds = a.get("d_values") or []
    data = a.get("data") or []
    reads = a.get("reads") or []

    if len(ts) < 3 or len(ds) < 3:
        raise ValueError(
            "graph-plot %r has a %dx%d grid. A journey needs enough "
            "intersections to be readable." % (act_id, len(ts), len(ds)))
    if not data:
        raise ValueError("graph-plot %r has no readings to plot." % act_id)

    tset, dset = set(ts), set(ds)
    off = [(p["t"], p["d"]) for p in data
           if p["t"] not in tset or p["d"] not in dset]
    if off:
        raise ValueError(
            "graph-plot %r has reading(s) %s that do not sit on an "
            "intersection of its own grid. The grid is real buttons, so a "
            "reading between two of them cannot be plotted at all and the "
            "task could never be completed." % (act_id, off))

    _unique_ids(reads, act_id, "graph-plot", "read-back question")
    for r in reads:
        if not isinstance(r.get("answer"), int) or \
                not (0 <= r["answer"] < len(r.get("options") or [])):
            raise ValueError(
                "graph-plot %r read %r has no valid answer index."
                % (act_id, r.get("id")))
        if not r.get("why"):
            raise ValueError(
                "graph-plot %r read %r has no `why`." % (act_id, r.get("id")))

    # One real button per intersection, each naming its own coordinates.
    cells = []
    for d in reversed(ds):
        for tv in ts:
            cells.append(
                '<button type="button" class="ks3-gplot-cell" '
                'data-gplot-cell="%s,%s" aria-label="%s seconds, %s metres">'
                '</button>' % (tv, d, tv, d))
    if len(cells) != len(ts) * len(ds):
        raise ValueError(
            "graph-plot %r built %d cells for a %dx%d grid."
            % (act_id, len(cells), len(ts), len(ds)))

    order = "|".join("%s,%s" % (p["t"], p["d"]) for p in data)

    reads_html = "".join(
        '<li class="ks3-gplot-read" data-gplot-read="%s" data-answer="%d" '
        'data-why="%s"><p class="ks3-gplot-q">%s</p>'
        '<div class="ks3-gplot-opts">%s</div>'
        '<p class="ks3-gplot-why" data-gplot-why hidden></p></li>'
        % (e(r["id"]), int(r["answer"]), e(r["why"]), t(r["question"]),
           "".join(_p3_seg("ks3-seg-btn", o, data_gplot_opt=i)
                   for i, o in enumerate(r["options"])))
        for r in reads)

    return ('<div class="ks3-gplot" data-gplot data-target="%d" '
            'data-order="%s">'
            '<p class="ks3-gplot-seek">Looking for: '
            '<span data-gplot-seek></span></p>'
            '<div class="ks3-gplot-wrap">'
            '<span class="ks3-gplot-ylab">%s</span>'
            '<div class="ks3-gplot-grid" role="group" aria-label="%s" '
            'style="--cols:%d;--rows:%d">%s'
            '<svg class="ks3-gplot-line" data-gplot-line aria-hidden="true" '
            'viewBox="0 0 100 100" preserveAspectRatio="none"></svg>'
            '</div>'
            '<span class="ks3-gplot-xlab">%s</span></div>'
            '<button type="button" class="ks3-seg-btn ks3-gplot-join" '
            'data-gplot-join disabled>%s</button>'
            '<ul class="ks3-gplot-reads" role="list">%s</ul>'
            '<p class="ks3-gplot-close" data-gplot-close hidden>%s</p>'
            '</div>'
            % (len(data), e(order), t(a.get("d_label", "")),
               e(a.get("alt", "")), len(ts), len(ds), "".join(cells),
               t(a.get("t_label", "")),
               t(a.get("join_label") or "Join the points"),
               reads_html, rich(a.get("close") or "")))


# ═══ p3-02 · #s-match · walk the graph ═══════════════════════════════════

def r_journey_match(a, act_id):
    """⊕ p3-02 `#s-match` — choose four segments, send the walker.

    ⚖️ **THE LINE IS DRAWN AS THE WALKER MOVES, NEVER SWAPPED IN AT THE
    END** (Law 9). A finished line that appears when the animation stops
    would let a student match the target without watching what produced it.

    ⚖️ **THE COMPARISON IS FACTUAL AND CARRIES NO VERDICT (R3).** Design
    reports "your line ends at 6 m, the target ends at 6 m" and stops there.
    Whether that counts as a match is the student's call.

    ⚠️ **ONE MODE MUST BE NEGATIVE.** Without a "walk back" the target can
    never require the line to fall, and the lesson's whole `FORCE-06`
    confrontation — that a falling line is the journey home rather than
    a hill — has nothing to stand on.

    ⚠️ RENDERS INTO `ks3-jwalk-block`, not `ks3-jmatch-block`: that stem was
    already registered by another unit, and two families wearing one shell
    class puts one unit's stylesheet on the other's instrument, silently
    (MRB-279).

    HOOKS: `data-jwalk` (wrapper, `data-secs`, `data-target`) ·
    `data-jwalk-seg` (valued with the segment index) · `data-jwalk-mode`
    (valued with the mode id, carrying `data-v`) · `data-jwalk-send` ·
    `data-jwalk-clear` · `data-jwalk-walker` · `data-jwalk-read` ·
    `data-jwalk-line` · `data-jwalk-verdict` · `data-jwalk-close`.
    """
    modes = a.get("modes") or []
    target = a.get("target") or []

    if len(modes) < 3:
        raise ValueError(
            "journey-match %r offers %d mode(s)." % (act_id, len(modes)))
    _unique_ids(modes, act_id, "journey-match", "mode")

    if not any(float(m.get("speed_ms") or 0) < 0 for m in modes):
        raise ValueError(
            "journey-match %r has no mode with a NEGATIVE speed. Without a "
            "walk-back the line can never fall, and p3-02's whole FORCE-06 "
            "confrontation — that a falling line is the journey home "
            "rather than a hill — has nothing to stand on." % act_id)
    if not any(float(m.get("speed_ms") or 0) == 0 for m in modes):
        raise ValueError(
            "journey-match %r has no STAND STILL mode, so the target can "
            "never contain a flat section — and 'a flat line is stopped, "
            "not slow' is this lesson's key fact." % act_id)

    ids = {m["id"] for m in modes}
    bad = [x for x in target if x not in ids]
    if bad:
        raise ValueError(
            "journey-match %r targets mode(s) %s that do not exist."
            % (act_id, bad))
    if not target:
        raise ValueError(
            "journey-match %r has no target, so there is nothing to match."
            % act_id)

    segs = "".join(
        '<div class="ks3-jwalk-seg" data-jwalk-seg="%d">'
        '<p class="ks3-jwalk-seglabel">Seconds %d to %d</p>'
        '<div class="ks3-jwalk-modes">%s</div></div>'
        % (i, i * int(a.get("seg_seconds") or 3),
           (i + 1) * int(a.get("seg_seconds") or 3),
           "".join(_p3_seg("ks3-seg-btn", m["label"],
                           data_jwalk_mode=m["id"],
                           data_v=float(m["speed_ms"]))
                   for m in modes))
        for i in range(len(target)))

    return ('<div class="ks3-jwalk" data-jwalk data-secs="%d" '
            'data-target="%s" data-n="%d">'
            '<div class="ks3-jwalk-corridor" role="img" aria-label="%s">'
            '<span class="ks3-jwalk-walker" data-jwalk-walker '
            'aria-hidden="true"></span></div>'
            '<p class="ks3-jwalk-read" data-jwalk-read aria-live="polite">'
            '</p>'
            '<svg class="ks3-jwalk-graph" viewBox="0 0 300 160" '
            'aria-hidden="true">'
            '<polyline class="ks3-jwalk-targetline" data-jwalk-targetline '
            'points=""></polyline>'
            '<polyline class="ks3-jwalk-line" data-jwalk-line points="">'
            '</polyline></svg>'
            '<div class="ks3-jwalk-segs">%s</div>'
            '<div class="ks3-jwalk-acts">'
            '<button type="button" class="ks3-seg-btn" data-jwalk-send>%s'
            '</button>'
            '<button type="button" class="ks3-seg-btn" data-jwalk-clear>%s'
            '</button></div>'
            '<p class="ks3-jwalk-verdict" data-jwalk-verdict hidden></p>'
            '<p class="ks3-jwalk-close" data-jwalk-close hidden>%s</p>'
            '</div>'
            % (int(a.get("seg_seconds") or 3), e("|".join(target)),
               len(target), e(a.get("alt", "")), segs,
               t(a.get("send_label") or "Send the walker"),
               t(a.get("clear_label") or "Clear the line"),
               rich(a.get("close") or "")))


# ═══ p3-03 · #s-frames · change who watches ══════════════════════════════

def r_relative_frames(a, act_id):
    """⊕ p3-03 `#s-frames` — two cars, three viewpoints, four readings.

    ⚖️ **EVERY READING IS COMPUTED FROM THE TWO SLIDERS.** `v − v_observer`,
    every time. Authoring any of the four would let a viewpoint show a
    number that does not follow from the speeds above it.

    ⚖️ **ONE READING IS ALWAYS ZERO — WHICHEVER BELONGS TO THE CURRENT
    VIEWPOINT.** That is the lesson: nothing about either car changed, and
    something is now stationary. The wiring outlines it rather than hiding
    the others.

    ⚠️ **A CAR DOES NOT TURN ROUND WHEN YOU CHANGE VIEWPOINT** (Design's
    flag 11, kept deliberately). A car's drawn ORIENTATION follows its
    ground velocity; its MOTION follows its relative velocity. So from car
    B's seat, car A can face right while drifting left. That is correct and
    it is exactly the sort of thing a reviewer reports as a bug. It is not
    one. Do not "fix" it.

    ⚠️ **THE ROAD BELONGS TO THE GROUND**, so the markings and posts slide
    in a car's frame. Without that the viewpoint change would have nothing
    visible to hang on.

    HOOKS: `data-rframe` (wrapper) · `data-rframe-gate` ·
    `data-rframe-gopt` · `data-rframe-bench` · `data-rframe-va` /
    `data-rframe-vb` (the sliders) · `data-rframe-dir` ·
    `data-rframe-obs` (valued with the observer id) · `data-rframe-out`
    (valued with the readout id) · `data-rframe-road` · `data-rframe-sent` ·
    `data-rframe-close`.
    """
    obs = a.get("observers") or []
    outs_spec = a.get("readouts") or []

    if len(obs) < 3:
        raise ValueError(
            "relative-frames %r offers %d observer(s). The lesson's claim is "
            "that the SAME situation gives different numbers from different "
            "seats, which needs the ground and both cars." % (act_id, len(obs)))
    _unique_ids(obs, act_id, "relative-frames", "observer")
    if not any(o.get("id") == "ground" for o in obs):
        raise ValueError(
            "relative-frames %r has no `ground` observer. It is the frame "
            "every earlier lesson used without saying so, and the one this "
            "lesson exists to make visible." % act_id)

    want = {"a_ground", "b_ground", "b_from_a", "a_from_b"}
    have = {o.get("id") for o in outs_spec}
    if want - have:
        raise ValueError(
            "relative-frames %r is missing the %s readout(s). All four have "
            "to be on screen together, or a student cannot see that changing "
            "the viewpoint changed the number and not the car."
            % (act_id, sorted(want - have)))

    lo = float(a.get("speed_min", 0))
    hi = float(a.get("speed_max") or 0)
    step = float(a.get("speed_step") or 0)
    if hi <= lo or step <= 0:
        raise ValueError(
            "relative-frames %r has an unusable speed range." % act_id)

    picks = "".join(
        _p3_seg("ks3-seg-btn", o["label"], pressed=(o["id"] == "ground"),
                data_rframe_obs=o["id"]) for o in obs)

    outs = "".join(
        '<div class="ks3-rframe-out" data-rframe-outwrap="%s">'
        '<p class="ks3-rframe-outlabel">%s</p>'
        '<p class="ks3-rframe-outval" data-rframe-out="%s"></p></div>'
        % (e(o["id"]), t(o["label"]), e(o["id"])) for o in outs_spec)

    return ('<div class="ks3-rframe" data-rframe>%s'
            '<div class="ks3-rframe-bench" data-rframe-bench hidden>'
            '<div class="ks3-rframe-picks" role="group" '
            'aria-label="Who is watching">%s</div>'
            '<div class="ks3-rframe-scene" role="img" aria-label="%s">'
            '<span class="ks3-rframe-road" data-rframe-road '
            'aria-hidden="true"></span>'
            '<span class="ks3-rframe-car is-a" data-rframe-car="a" '
            'aria-hidden="true">A</span>'
            '<span class="ks3-rframe-car is-b" data-rframe-car="b" '
            'aria-hidden="true">B</span>'
            '<span class="ks3-rframe-still" data-rframe-still></span></div>'
            '<div class="ks3-rframe-controls">'
            '<label for="%s-a">Speed of car A · '
            '<span data-rframe-valabel></span></label>'
            '<input id="%s-a" type="range" min="%s" max="%s" step="%s" '
            'value="%s" data-rframe-va>'
            '<label for="%s-b">Speed of car B · '
            '<span data-rframe-vblabel></span></label>'
            '<input id="%s-b" type="range" min="%s" max="%s" step="%s" '
            'value="%s" data-rframe-vb>'
            '<button type="button" class="ks3-seg-btn" data-rframe-dir '
            'aria-pressed="%s" data-same="%s" data-opp="%s">%s</button>'
            '</div>'
            '<div class="ks3-rframe-outs">%s</div>'
            '<p class="ks3-rframe-sent" data-rframe-sent '
            'aria-live="polite"></p>'
            '<p class="ks3-rframe-close" data-rframe-close hidden>%s</p>'
            '</div></div>'
            % (_gate(act_id, "relative-frames", a.get("gate") or {},
                     "rframe"),
               picks, e(a.get("alt", "")),
               e(act_id), e(act_id), lo, hi, step,
               float(a.get("a_start") or 0),
               e(act_id), e(act_id), lo, hi, step,
               float(a.get("b_start") or 0),
               "true" if a.get("start_same_direction") else "false",
               e(a.get("same_direction_label") or "Same way"),
               e(a.get("opposite_direction_label") or "Opposite ways"),
               t(a.get("same_direction_label") or "Same way"),
               outs, rich(a.get("close") or "")))


# ═══ p3-03 · #s-pass · four passes ═══════════════════════════════════════

def r_passing_speeds(a, act_id):
    """⊕ p3-03 `#s-pass` — four situations, add or subtract.

    ⚖️ **MRB-204, ASSERTED RATHER THAN PROMISED.** Every `sum` on this page
    must be an ADDITION or a SUBTRACTION. A product here would be a
    relationship the lesson does not have — and it would also make a
    triangle look defensible on a page that must not carry one. The check
    is cheap and it is the reason this renderer exists rather than the
    generic branch.

    ⚖️ **THE SUM APPEARS BEFORE THE WHY.** Choosing reveals the arithmetic
    first, so the student reads two numbers rather than a verdict.

    HOOKS: `data-pass` (wrapper, `data-target`) · `data-pass-row` (valued
    with the pass id, carrying `data-answer`, `data-sum`, `data-why`) ·
    `data-pass-opt` · `data-pass-sum` · `data-pass-why` · `data-pass-close`.
    """
    passes = a.get("passes") or []
    if len(passes) < 3:
        raise ValueError(
            "passing-speeds %r has %d pass(es). Same-way, opposite-ways and "
            "a walk inside a moving frame are three different cases and the "
            "block's claim needs all of them." % (act_id, len(passes)))
    _unique_ids(passes, act_id, "passing-speeds", "pass")

    for p in passes:
        s = p.get("sum") or ""
        if not s:
            raise ValueError(
                "passing-speeds %r pass %r has no `sum`." % (act_id, p["id"]))
        # ⚖️ MRB-204 — an addition or a subtraction, never a product.
        if ("+" not in s) and ("−" not in s) and ("-" not in s):
            raise ValueError(
                "passing-speeds %r pass %r has the sum %r, which is neither "
                "an addition nor a subtraction. Every relative speed in this "
                "lesson is one or the other; a product here would be a "
                "relationship the lesson does not have, and would make a "
                "formula triangle look defensible on a page that must not "
                "carry one (MRB-204)." % (act_id, p["id"], s))
        if "×" in s or "*" in s:
            raise ValueError(
                "passing-speeds %r pass %r multiplies (%r). See above: "
                "relative speed is a sum or a difference."
                % (act_id, p["id"], s))
        if not isinstance(p.get("answer"), int) or \
                not (0 <= p["answer"] < len(p.get("options") or [])):
            raise ValueError(
                "passing-speeds %r pass %r has no valid answer index."
                % (act_id, p["id"]))

    rows = "".join(
        '<li class="ks3-pass-row" data-pass-row="%s" data-answer="%d" '
        'data-sum="%s" data-why="%s">'
        '<p class="ks3-pass-label">%s</p>'
        '<p class="ks3-pass-q">%s</p>'
        '<div class="ks3-pass-opts">%s</div>'
        '<p class="ks3-pass-sum" data-pass-sum hidden></p>'
        '<p class="ks3-pass-why" data-pass-why hidden></p></li>'
        % (e(p["id"]), int(p["answer"]), e(p["sum"]), e(p["why"]),
           t(p.get("label", "")), t(p["question"]),
           "".join(_p3_seg("ks3-seg-btn", o, data_pass_opt=i)
                   for i, o in enumerate(p["options"])))
        for p in passes)

    return ('<div class="ks3-pass" data-pass data-target="%d">'
            '<ul class="ks3-pass-list" role="list">%s</ul>'
            '<p class="ks3-pass-close" data-pass-close hidden>%s</p>'
            '</div>' % (len(passes), rows, rich(a.get("close") or "")))


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. `ks3_art.check_placements` gate 2 fails a family
# registered and never placed and gate 3 fails one placed and never
# registered. Every family is P3's own — `ks3_art/core.py` is untouched.
#
# ⚠️ SHELL STEMS WERE CHECKED AGAINST THE WHOLE REGISTRY BEFORE BEING
# WRITTEN. `ks3-jmatch-block` was already taken, so the journey matcher
# renders into `ks3-jwalk-block`.

KIND_SHELL = {
    'light-gates':     ("ks3-lgate-block",
                        ' data-instrument data-lgateblock '
                        'data-stage-done="0"'),
    'compare-pairs':   ("ks3-spair-block",
                        ' data-instrument data-spairblock '
                        'data-stage-done="0"'),
    'graph-plot':      ("ks3-gplot-block",
                        ' data-instrument data-gplotblock '
                        'data-stage-done="0"'),
    'journey-match':   ("ks3-jwalk-block",
                        ' data-instrument data-jwalkblock '
                        'data-stage-done="0"'),
    'relative-frames': ("ks3-rframe-block",
                        ' data-instrument data-rframeblock '
                        'data-stage-done="0"'),
    'passing-speeds':  ("ks3-pass-block",
                        ' data-instrument data-passblock '
                        'data-stage-done="0"'),
}

KIND_FN = {
    'light-gates':     r_light_gates,
    'compare-pairs':   r_compare_pairs,
    'graph-plot':      r_graph_plot,
    'journey-match':   r_journey_match,
    'relative-frames': r_relative_frames,
    'passing-speeds':  r_passing_speeds,
}
