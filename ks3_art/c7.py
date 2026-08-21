"""ks3_art.c7 — C7's instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C7 is *Energy changes in reactions*: four
lessons, SIX instrument families and NO drawn figure, all DOM, no canvas
anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY. Everything an instrument has to COMPUTE at run time is the JS's
job; this file emits the data it needs and the RESTING DOM — the state the page
is in before a line of JavaScript has run, which is also the state a crawler
and a no-JS reader see. A resting render that disagrees with the payload is a
wrong number in the bytes, not a flicker.

Two conventions run through every renderer below and both are load-bearing:

  · EMIT-BOTH-SHOW-ONE, wherever a panel has a small closed set of states.
    Every state's text is in the document and one is shown. Nothing is ever
    assembled out of an attribute at run time, so ``<em>``, ``<strong>`` and an
    ampersand survive exactly as the author wrote them, and no sentence is
    duplicated between Python and JS where the two could drift. C7 leans on
    this harder than any unit so far: the heating curve emits EIGHTEEN readout
    states, the temperature bench five and the rig builder eight, and not one
    of them is composed by `shared/ks3.js`.
  · NUMBERS ARE DERIVED, NEVER AUTHORED TWICE. Every delta on the temperature
    bench, every "lost" figure on the rig builder, every bar height on the
    heating curve and every count a block's lead claims is computed here from
    the payload and cross-checked against what the author wrote. Where the two
    disagree the build fails.

═══════════════════════════════════════════════════════════════════════════
THE HOOKS ARE AN INTERFACE
═══════════════════════════════════════════════════════════════════════════

Every ``data-`` attribute emitted below is named systematically off the
family's short name (hcurve / tempb / esort / euse / rplan / rigb) and is the
contract ``shared/ks3.js`` binds against. Renaming one here without renaming it
there is a silent dead instrument, so they are documented in each renderer's
docstring as well as in the report.

⚠️ ``data-rplan``, NOT ``data-critiq``. `ks3_art/c3.py` already claims
``[data-critiq]`` for c3-07's plan critique, and ``[data-critique]`` was
already claimed by a biology family before that. Three families, three
selectors, and the two collisions that were nearly made are recorded in c3's
own header. C7's is the same SHAPE with a different plan in it and it gets its
own name, because a family name is an owner and not a description.

═══════════════════════════════════════════════════════════════════════════
THE RULES THAT BIND ALL SIX
═══════════════════════════════════════════════════════════════════════════

  · Every C7 instrument sits in a LIGHT ``ks3-block``. There is no ink-dark
    practical block anywhere in the unit — measured off Design's markup, all
    eight anchored instrument sections carry ``class="ks3-block"`` and nothing
    else. The ink PANELS inside the two benches are readouts nested in a light
    block, which is a different thing.
  · ONLY THE LADDER MARKS. Nothing green and nothing red reaches any control
    in any of these six. A verdict panel says in words what happened; the
    chosen option keeps the ordinary chosen treatment and the unchosen ones
    dim. No ``data-correct`` on any activity option, ever.
  · Every family here ticks a rail stop, so every family carries
    ``data-stage-done="0"``. NOTHING IS TICKED ON LOAD.
  · Author text reaches the page through ``e()`` / ``t()`` / ``rich()``.
    ``e()`` for attribute values — it is the only one safe there, because
    ``t()`` can emit an SVG mark carrying double quotes — ``rich()`` for
    prose, ``t()`` for labels.
  · Arrows are DRAWN AS SVG, never the character U+2192. The shipped font
    subsets do not contain it, so a typed arrow drops to a system font
    mid-line inside a 26px display row. NOTES-C7 §6 asks for SVG arrows in
    c7-02's start→peak readout and that is what `_tempb_arrow` draws.
  · CONTAINMENT, NOT CLIPPING. Nothing in this unit is absolutely positioned
    inside a scroller, so the C5 trap (65 escaped screen-reader labels) has
    nothing to bite on here — but the rule is why the heating curve's trace is
    a flex row of proportional heights rather than a positioned plot.
"""

from ks3_art.kit import e, option_letter, rich, t


# ═══ shared inside C7 ════════════════════════════════════════════════════

def _c7_seg(cls, pressed, label, **attrs):
    """One segmented-control button.

    `.ks3-seg-btn` is the key stage's ONE segmented control (the Drift-4
    ruling), with a family class beside it for layout. R2: the pressed state
    carries `aria-pressed`, a WORD, not colour alone. There is no `correct`
    parameter here and there must never be one.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _c7_lettered(options, hook):
    """A lettered A/B/C commit list inside an instrument.

    The same markup `r_activity_options` emits, because Design draws the SAME
    control for a prediction whether it stands alone in a block or sits inside
    a bench. It gets a hook of its own because the shell's `wirePredictions`
    refuses to touch anything inside `[data-instrument]`: an instrument owns
    every option inside it, which means it also has to wire them.

    Nothing is pressed at rest. MRB-208.
    """
    return ('<ul class="ks3-options" role="list" %s>%s</ul>'
            % (hook,
               "".join(
                   '<li><button type="button" class="ks3-option" data-i="%d" '
                   'aria-pressed="false"><span class="ks3-opt-mark" '
                   'aria-hidden="true">%s</span>'
                   '<span class="ks3-opt-label">%s</span></button></li>'
                   % (i, option_letter(i), t(o))
                   for i, o in enumerate(options))))


def _counter_agrees(a, act_id, n, what):
    """The block-head counter's denominator must be the number of things.

    ⚖️ THE SMALLEST §5A ASSERTION IN THE UNIT AND THE ONE THAT WOULD SHIP
    SILENTLY. `head_counter.total` is authored beside the payload, not derived
    from it, so a ninth card arriving under a counter that still says eight
    produces a page reading "9 of 8" — clamped by `setCount` to "8 of 8", which
    means the rail ticks a stop the student has not finished and the readout
    lies in the direction that looks fine.
    """
    hc = a.get("head_counter") or {}
    if not hc:
        return
    total = hc.get("total")
    if total is not None and int(total) != int(n):
        raise ValueError(
            "%s: the block-head counter says %s of %s and the payload holds "
            "%d %s. The denominator is a claim about the instrument under it."
            % (act_id, "{n}", total, n, what))


def _close_panel(a, cls, hook):
    """The payoff panel: title, paragraphs, an optional `id`, always hidden.

    The `id` is authored (`close_id`) rather than composed here, because on
    three of C7's four pages it is a misconception's `confronted_by` and
    MRB-244 resolves that against the BUILT page. A name composed in a
    renderer is a name the register cannot be checked against.
    """
    paras = a.get("close") or []
    if not paras:
        return ""
    ident = (' id="%s"' % e(a["close_id"])) if a.get("close_id") else ""
    title = (('<p class="%s-closetitle">%s</p>' % (cls, t(a["close_title"])))
             if a.get("close_title") else "")
    return ('<div class="%s-close"%s hidden %s>%s%s</div>'
            % (cls, ident, hook, title,
               "".join("<p>%s</p>" % rich(p) for p in paras)))


# ═══ c7-01 · heating-curve ═══════════════════════════════════════════════

def r_heating_curve(a, act_id):
    """⊕ c7-01 `#s-curve` — eighteen minutes, one tap at a time.

    ⚖️ **THE PLATEAUS ARE THE LESSON AND WAITING IS HOW THEY ARE TAUGHT.**
    NOTES-C7 §2: "the two flat steps are the whole lesson and they have to be
    experienced as *waiting*, which a static graph cannot do." So there is one
    control, it does one thing, and the eight consecutive taps that report
    100 °C are not a defect in the instrument — they are the instrument.

    ⚖️ **THE DATA IS THE COMMANDER'S RULING AND THIS RENDERER ENFORCES ITS
    SHAPE.** Design drew both plateaus three minutes long while her own note
    said boiling is longer; the ruling rebuilt the array so melting runs three
    minutes and boiling eight. What is checked here is the PROPERTY that ruling
    asserts, not the numbers themselves: at least two plateaus, the last
    strictly longer than the first, and a temperature that never falls. A later
    re-pointing of this instrument at a different substance keeps the property
    or fails the build.

    ⚠️ NOTHING IS COMPUTED AT RUN TIME. All eighteen readouts — temperature,
    state, minute label and note — are in the document at rest and one is
    unhidden, so `<strong>`, an em dash and a degree sign survive exactly as
    the author wrote them and the resting render cannot disagree with the
    runtime one. The bar heights are computed HERE, from `scale`, and become
    literal bytes.

    ⚠️ THE FLAT BARS ARE MARKED IN THE MARKUP, NOT IN THE JS. `data-flat="1"`
    is a property of the curve — this reading repeats the one before it — so it
    is decided at build time. The JS only decides which bars are LIT, which is
    the only thing that changes when the student taps.

    ⚠️ NOTHING HERE MARKS (R3). The lit bars take the ink fill and the flat
    ones the accent; neither is a verdict on anything the student did, and
    there is no green and no red anywhere in this instrument.

    HOOKS: `data-hcurve` (wrapper, `data-total`) · `data-hcurve-point` (valued
    with the index) · `data-hcurve-bar` (valued with the index) ·
    `data-hcurve-step` · `data-hcurve-reset` · `data-hcurve-steplabel` ·
    `data-hcurve-endlabel` · `data-hcurve-close`.
    """
    curve = a.get("curve") or []
    if len(curve) < 4:
        raise ValueError(
            "heating-curve %r declares %d point(s). A heating curve needs a "
            "climb, a plateau and a climb out of it before it is a curve at "
            "all." % (act_id, len(curve)))

    # ── §5A · walk EVERY element, not a sample ──────────────────────────
    for i, p in enumerate(curve):
        if p.get("t") is None:
            raise ValueError(
                "heating-curve %r point %d has no `t`. The temperature is the "
                "measurement and every other number on the page is derived "
                "from it." % (act_id, i))
        for key in ("state", "note"):
            if not p.get(key):
                raise ValueError(
                    "heating-curve %r point %d has no %r. A reading with no "
                    "state is a number nobody named, and a reading with no "
                    "note is a tap that says nothing back."
                    % (act_id, i, key))
        if i and float(p["t"]) < float(curve[i - 1]["t"]):
            raise ValueError(
                "heating-curve %r falls from %s to %s at point %d. This is a "
                "HEATING curve: the flame is on for the whole run, so the "
                "temperature may hold but it may never drop."
                % (act_id, curve[i - 1]["t"], p["t"], i))

    # ── §5A · the plateaus, DERIVED, and the ruling's property asserted ──
    plateaus, i = [], 0
    while i < len(curve):
        j = i
        while j + 1 < len(curve) and curve[j + 1]["t"] == curve[i]["t"]:
            j += 1
        if j > i:
            plateaus.append((curve[i]["t"], j - i))
        i = j + 1
    if len(plateaus) < 2:
        raise ValueError(
            "heating-curve %r draws %d plateau(s). The lesson's whole claim is "
            "that there are two of them and that the second is longer, and a "
            "curve with one cannot make it." % (act_id, len(plateaus)))
    if plateaus[-1][1] <= plateaus[0][1]:
        raise ValueError(
            "heating-curve %r draws a %d-minute plateau at %s °C and a "
            "%d-minute plateau at %s °C. The closing panel and the point notes "
            "both say the boiling step is longer, and the commander's ruling "
            "of 21 Aug 2026 is that the DATA carries that claim rather than "
            "the prose rescuing it."
            % (act_id, plateaus[0][1], plateaus[0][0],
               plateaus[-1][1], plateaus[-1][0]))

    # ── the readout: eighteen states, all present, one shown ─────────────
    scale = a.get("scale") or {}
    floor = float(scale.get("floor", -30))
    span = float(scale.get("span", 150)) or 150.0
    fmt = a.get("minute_format") or "Minute {n}"
    flat_suffix = a.get("flat_suffix") or ""

    points, bars = [], []
    for i, p in enumerate(curve):
        flat = bool(i and curve[i - 1]["t"] == p["t"])
        # Composed HERE, at build time, so it is literal bytes in the document
        # and never a sentence assembled by the runtime.
        minute = fmt.replace("{n}", str(i)) + (flat_suffix if flat else "")
        points.append(
            '<div class="ks3-hcurve-point"%s data-hcurve-point="%d">'
            '<p class="ks3-hcurve-temp">%s °C</p>'
            '<div class="ks3-hcurve-names">'
            '<p class="ks3-hcurve-state">%s</p>'
            '<p class="ks3-hcurve-minute">%s</p></div>'
            '<p class="ks3-hcurve-note">%s</p></div>'
            % ("" if i == 0 else " hidden", i, t(str(p["t"])),
               t(p["state"]), t(minute), rich(p["note"])))
        height = max(2.0, min(100.0, ((float(p["t"]) - floor) / span) * 100.0))
        bars.append(
            '<span class="ks3-hcurve-bar%s" data-hcurve-bar="%d"%s '
            'style="height:%.4g%%"></span>'
            % (" is-lit" if i == 0 else "", i,
               ' data-flat="1"' if flat else "", height))

    trace = ('<div class="ks3-hcurve-trace">'
             '<p class="ks3-hcurve-tracelabel">%s</p>'
             '<div class="ks3-hcurve-bars" role="img" aria-label="%s">%s</div>'
             '<p class="ks3-hcurve-axis">%s</p></div>'
             % (t(a.get("trace_label") or "Temperature against time"),
                e(a.get("trace_alt")
                  or "A bar chart of temperature against time, with a short "
                     "flat run partway up and a much longer flat run near the "
                     "top."),
                "".join(bars), t(a.get("axis_label") or "")))

    # ⚠️ BOTH BUTTON LABELS ARE IN THE DOCUMENT AND ONE IS SHOWN. Design swaps
    # "Heat for one more minute" for "Run complete" at the end of the run; the
    # swap is a choice between two authored strings, never a string built in
    # the JS.
    controls = (
        '<div class="ks3-hcurve-controls">'
        '<button type="button" class="ks3-seg-btn ks3-hcurve-step" '
        'data-hcurve-step>'
        '<span data-hcurve-steplabel>%s</span>'
        '<span data-hcurve-endlabel hidden>%s</span></button>'
        '<button type="button" class="ks3-hcurve-reset" data-hcurve-reset>'
        '%s</button></div>'
        % (t(a.get("step_label") or "Heat for one more minute"),
           t(a.get("end_label") or "Run complete"),
           t(a.get("reset_label") or "Start again")))

    close = _close_panel(a, "ks3-hcurve", "data-hcurve-close")

    return ('<div class="ks3-hcurve" data-hcurve data-total="%d">'
            '<div class="ks3-hcurve-grid">'
            '<div class="ks3-hcurve-readout">%s%s</div>%s</div>%s</div>'
            % (len(curve), "".join(points), controls, trace, close))


# ═══ c7-02 · temp-bench ══════════════════════════════════════════════════

def _tempb_arrow(word):
    """Design's start→peak arrow, DRAWN, with its spoken word beside it.

    ⚠️ Never the character U+2192. Geometry measured off Design's own markup:
    viewBox `0 0 44 24`, `M4 12h30M26 5l8 7-8 7`, 2.6px stroke, round caps and
    joins, on `currentColor` so it inherits the on-dark of the readout panel it
    lands in. NOTES-C7 §6 asks for exactly this.
    """
    return ('<svg class="ks3-tempb-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" '
            'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>'
            '<span class="ks3-visually-hidden">%s</span>' % t(word))


def r_temp_bench(a, act_id):
    """⊕ c7-02 `#s-bench` — five beakers, one thermometer, one odd one out.

    ⚖️ **THE VERDICT IS DERIVED FROM THE ARITHMETIC (§5A).** Design's page
    reads `rx.exo` and prints "exothermic" or "not exothermic" beside a delta
    it computes separately, so the flag and the subtraction could disagree and
    nothing would say so. Here the delta is computed, the verdict is derived
    from its SIGN, and the authored `exo` flag is a GUARD that must agree.

    ⚖️ **AND ZERO IS REFUSED RATHER THAN GUESSED.** §5A asks for the whole
    state space enumerated including zero. A delta of zero is a state this
    bench has no label for — Design draws two verdicts, not three — so a run
    that reached it would print "not exothermic" for a reaction that did
    nothing. The renderer raises instead. Drawing a third verdict is not the
    fix: none of the five reactions has a zero delta, and inventing a state to
    make an assertion pass is the defect the assertion exists to find.

    ⚠️ THE PREDICTION GATE HOLDS THE READOUT (Law 4) AND THEN STAYS ON SCREEN.
    Design's `needPredict` is `!ran`, which REMOVES the gate the moment it is
    answered — taking the student's own commitment off the page at the exact
    moment the reading arrives to be compared against it, which is the
    comparison Law 4 exists to create. Every gate in C3, C4 and C5 stays put.
    This one stays put.

    ⚠️ EMIT-BOTH-SHOW-ONE. All five set-ups, all five readouts and all five
    reasons are in the document at rest and one set is unhidden.

    ⚠️ NOTHING HERE MARKS (R3). A prediction that turned out wrong looks
    exactly like one that turned out right: same pressed treatment, same ink
    panel, same reading. The correction, where there is one, is the reading.

    HOOKS: `data-tempb` (wrapper, `data-total`) · `data-tempb-tab` (valued with
    the reaction id) · `data-tempb-card` (valued with the reaction id) ·
    `data-tempb-predict` · `data-tempb-run` · `data-tempb-close`.
    """
    reactions = a.get("reactions") or []
    predict = a.get("predict") or {}
    if len(reactions) < 3:
        raise ValueError(
            "temp-bench %r declares %d reaction(s). The bench's whole argument "
            "is a pattern and an exception, and neither is visible in two."
            % (act_id, len(reactions)))
    if not predict.get("options"):
        raise ValueError(
            "temp-bench %r has no prediction options. Law 4: the reading is "
            "not shown until the student has said what they expect." % act_id)
    _counter_agrees(a, act_id, len(reactions), "reaction(s)")

    seen = set()
    exo_n = 0
    cards = []
    tabs = []
    for idx, r in enumerate(reactions):
        for key in ("id", "label", "setup", "why"):
            if not r.get(key):
                raise ValueError(
                    "temp-bench %r reaction %r has no %r. Every run opens a "
                    "set-up, a reading and a reason; a run with nothing to "
                    "report is a control that does nothing."
                    % (act_id, r.get("id"), key))
        if r["id"] in seen:
            raise ValueError(
                "temp-bench %r authors the reaction id %r twice. One card "
                "would be unreachable and no gate would see it."
                % (act_id, r["id"]))
        seen.add(r["id"])
        if r.get("start") is None or r.get("end") is None:
            raise ValueError(
                "temp-bench %r reaction %r has no start or no end "
                "temperature. The readout is one subtraction and it cannot be "
                "done." % (act_id, r["id"]))

        delta = float(r["end"]) - float(r["start"])
        if delta == 0:
            raise ValueError(
                "temp-bench %r reaction %r starts and ends at %s °C. This "
                "bench draws two verdicts, exothermic and not, and has no "
                "label for a reaction that changed nothing — so a zero delta "
                "would print a verdict about a run that did not happen."
                % (act_id, r["id"], r["start"]))
        derived_exo = delta > 0
        if bool(r.get("exo")) != derived_exo:
            raise ValueError(
                "temp-bench %r reaction %r is flagged exo=%r and runs %s → %s, "
                "which is %+g °C. The flag is what the record believes and the "
                "subtraction is what the student reads; when they disagree the "
                "page argues with itself."
                % (act_id, r["id"], bool(r.get("exo")), r["start"], r["end"],
                   delta))
        if derived_exo:
            exo_n += 1

        # Composed at build time from the derived delta and the two authored
        # verdict words. Never assembled at run time.
        badge = "%+g °C · %s" % (
            delta, (a.get("label_exo") or "exothermic") if derived_exo
            else (a.get("label_not_exo") or "not exothermic"))

        tabs.append(_c7_seg("ks3-tempb-tab", idx == 0, r["label"],
                            data_tempb_tab=r["id"]))
        cards.append(
            '<div class="ks3-tempb-card"%s data-tempb-card="%s">'
            '<p class="ks3-tempb-title">%s</p>'
            '<p class="ks3-tempb-setup"><span class="ks3-tempb-setuplabel">'
            '%s</span>%s</p>'
            '<div class="ks3-tempb-gate">'
            '<p class="ks3-commit">%s</p>%s</div>'
            '<div class="ks3-tempb-run" hidden data-tempb-run>'
            '<div class="ks3-tempb-readout">'
            '<div class="ks3-tempb-figure">'
            '<p class="ks3-tempb-figlabel">%s</p>'
            '<p class="ks3-tempb-value">%s °C</p></div>%s'
            '<div class="ks3-tempb-figure">'
            '<p class="ks3-tempb-figlabel">%s</p>'
            '<p class="ks3-tempb-value">%s °C</p></div>'
            '<span class="ks3-tempb-delta"%s>%s</span></div>'
            '<p class="ks3-tempb-why">%s</p></div></div>'
            % ("" if idx == 0 else " hidden", e(r["id"]),
               t(r["label"]),
               t(a.get("setup_label") or "The set-up"), t(r["setup"]),
               rich(predict.get("prompt") or ""),
               "".join(_c7_seg("ks3-tempb-predict", False,
                               o.get("label", ""),
                               data_tempb_predict=o.get("id", ""))
                       for o in predict["options"]),
               t(a.get("start_label") or "Start"), t(str(r["start"])),
               _tempb_arrow(a.get("arrow_word") or "rises to"),
               t(a.get("peak_label") or "Highest reading"), t(str(r["end"])),
               ' data-exo="1"' if derived_exo else "",
               t(badge), rich(r["why"])))

    # ⚖️ THE CLOSING PANEL'S CLAIM, CHECKED. "Four went up. One went down."
    # is a statement about this payload, and it is the sentence a student
    # reads after five taps. Derived rather than trusted.
    if exo_n != len(reactions) - 1:
        raise ValueError(
            "temp-bench %r holds %d exothermic run(s) of %d. The closing panel "
            "is written on there being exactly one exception, and it is the "
            "handover to the next lesson."
            % (act_id, exo_n, len(reactions)))

    close = _close_panel(a, "ks3-tempb", "data-tempb-close")

    return ('<div class="ks3-tempb" data-tempb data-total="%d">'
            '<div class="ks3-tempb-tabs">%s</div>%s%s</div>'
            % (len(reactions), "".join(tabs), "".join(cards), close))


# ═══ c7-03 · energy-sorter ═══════════════════════════════════════════════

def r_energy_sorter(a, act_id):
    """⊕ c7-03 `#s-compare` — eight changes, two directions, three pairs.

    ⚖️ **THE PAIRS ARE THE INSTRUMENT'S ARGUMENT AND THEY ARE ASSERTED.**
    NOTES-C7 §2: the sorter carries "three deliberate pairs (melting/freezing,
    photosynthesis/respiration) so the reversal rule falls out of the sort
    rather than being stated." The closing panel then names them. So the pairs
    are authored as a payload field and checked here: both members present,
    and OPPOSITE flags. Without that check the panel's rule — run a change
    backwards and the energy runs backwards with it — is a claim the cards
    above it might not support.

    ⚖️ **AND THE COUNT IN THE LEAD IS DERIVED.** "Three of the eight are
    endothermic" is a number in a sentence a student reads before they sort
    anything. It is computed from the items and asserted against the authored
    claim, so a flipped flag fails the build rather than shipping a lead that
    contradicts the cards under it.

    ⚠️ THE VERDICT LINE IS ONE OF TWO AUTHORED STRINGS, CHOSEN BY THE FLAG. It
    is not a mark: both verdicts take the same treatment, and a student who
    pressed the other button reads the same panel. Only the ladder marks (R3).

    ⚠️ AND EACH `why` IS CHECKED TO NAME THE RIGHT WORD FIRST. A card whose
    reason opens by saying "exothermic" under a verdict that says endothermic
    is a page arguing with itself in front of a student, and nothing else in
    the build could see it.

    HOOKS: `data-esort` (wrapper, `data-total`) · `data-esort-item` (valued
    with the item id) · `data-esort-opt` (valued with the option id) ·
    `data-esort-reveal` · `data-esort-close`.
    """
    items = a.get("items") or []
    options = a.get("options") or []
    if len(items) < 4:
        raise ValueError(
            "energy-sorter %r declares %d item(s). The lesson's claim is that "
            "the list is LOPSIDED and that it contains reversal pairs, and "
            "neither is visible in three." % (act_id, len(items)))
    if len(options) != 2:
        raise ValueError(
            "energy-sorter %r offers %d option(s). Every change is one of two "
            "directions, and a third option would be a different question."
            % (act_id, len(options)))
    _counter_agrees(a, act_id, len(items), "item(s)")

    verdicts = {True: a.get("verdict_endo"), False: a.get("verdict_exo")}
    if not verdicts[True] or not verdicts[False]:
        raise ValueError(
            "energy-sorter %r needs both `verdict_endo` and `verdict_exo`. "
            "The card opens on a commitment and the verdict is the first "
            "thing that opens." % act_id)

    by_id, endo_n = {}, 0
    cards = []
    for row in items:
        for key in ("id", "name", "where", "why"):
            if not row.get(key):
                raise ValueError(
                    "energy-sorter %r item %r has no %r. A card with no place "
                    "is a change with no context, and a card with no reason "
                    "reveals nothing when it opens."
                    % (act_id, row.get("id"), key))
        if row["id"] in by_id:
            raise ValueError(
                "energy-sorter %r authors the item id %r twice."
                % (act_id, row["id"]))
        by_id[row["id"]] = row
        endo = bool(row.get("endo"))
        endo_n += 1 if endo else 0

        # ── the content-truth assertion, per card ────────────────────────
        low = row["why"].lower()
        want, other = ("endothermic", "exothermic") if endo \
            else ("exothermic", "endothermic")
        at_want = low.find(want)
        at_other = low.find(other)
        if at_want < 0 or (at_other >= 0 and at_other < at_want):
            raise ValueError(
                "energy-sorter %r item %r is flagged endo=%r, so its verdict "
                "will read %r — but its reason names %r first. The verdict and "
                "the reason are read together and one of them is wrong."
                % (act_id, row["id"], endo, verdicts[endo], other))

        cards.append(
            '<div class="ks3-esort-item" data-esort-item="%s" data-open="0">'
            '<div class="ks3-esort-head">'
            '<p class="ks3-esort-name">%s</p>'
            '<p class="ks3-esort-where">%s</p></div>'
            '<div class="ks3-esort-opts">%s</div>'
            '<div class="ks3-esort-reveal" hidden data-esort-reveal>'
            '<p class="ks3-esort-verdict">%s</p>'
            '<p class="ks3-esort-why">%s</p></div></div>'
            % (e(row["id"]), t(row["name"]), t(row["where"]),
               "".join(_c7_seg("ks3-esort-opt", False, o.get("label", ""),
                               data_esort_opt=o.get("id", ""))
                       for o in options),
               t(verdicts[endo]), rich(row["why"])))

    claim = a.get("endo_count_claim")
    if claim is not None and int(claim) != endo_n:
        raise ValueError(
            "energy-sorter %r says %s of the items are endothermic in its "
            "lead and holds %d. The lead is read BEFORE anything is sorted, "
            "so it is a promise about the cards under it."
            % (act_id, claim, endo_n))

    for pair in (a.get("pairs") or []):
        if len(pair) != 2:
            raise ValueError(
                "energy-sorter %r declares a `pairs` entry of %d id(s). A "
                "reversal pair is two changes." % (act_id, len(pair)))
        missing = [p for p in pair if p not in by_id]
        if missing:
            raise ValueError(
                "energy-sorter %r pairs %s and %s are not items on this "
                "bench. The closing panel names the pair by name."
                % (act_id, pair, missing))
        if bool(by_id[pair[0]].get("endo")) == bool(by_id[pair[1]].get("endo")):
            raise ValueError(
                "energy-sorter %r pairs %r with %r and both carry endo=%r. "
                "The closing panel's rule is that running a change backwards "
                "reverses its energy transfer, and a pair pointing the same "
                "way is evidence against it."
                % (act_id, pair[0], pair[1],
                   bool(by_id[pair[0]].get("endo"))))

    close = _close_panel(a, "ks3-esort", "data-esort-close")
    return ('<div class="ks3-esort" data-esort data-total="%d">%s%s</div>'
            % (len(items), "".join(cards), close))


# ═══ c7-01, c7-02, c7-03 · energy-uses ═══════════════════════════════════

def r_energy_uses(a, act_id):
    """⊕ `#s-uses` on three pages — one rule, three places it decides.

    ⚖️ **ONE FAMILY, PLACED THREE TIMES.** Design draws this block on c7-01,
    c7-02 and c7-03 with the same shape every time: three cards, one final
    commitment each, an answer paragraph on the card that opens. That is one
    instrument used three times, not three instruments that look alike, and
    modelling it as three families would be three copies of this renderer with
    three chances to drift. See `ks3_data/c7/__init__.py` for the argument.

    ⚠️ THE COMMITMENT IS FINAL. The answer is on screen the instant the card is
    decided, so a second press would be a student choosing something they can
    already read. Both siblings disable and the one not pressed dims.

    ⚠️ NOTHING HERE MARKS (R3). `correct` reaches NO markup — not as a class,
    not as `data-correct`, not as anything. It is the author's record of what
    the card is for, read once here as a guard that it names an option a
    student can actually press.

    ⊖ AND THE GUARD STOPS THERE, DELIBERATELY. c5-04's `reactivity-use` can
    assert that its answer paragraph OPENS with the verdict, because its cards
    are yes-or-no and Design wrote the answers that way. These are not: the
    options are three sentences and the answers are prose that argues rather
    than adjudicating ("It genuinely helps, and it looks like madness"). An
    assertion that demanded a formulaic opening would be an assertion that
    rewrote Design's answers to satisfy itself. What IS checked is everything
    structural — every card, every option, every id — plus the block-head
    counter's denominator, which is the number on this block that could
    otherwise ship wrong in silence.

    ⚠️ EVERY CARD CARRIES A REAL `id`, AND ON c7-02 IT IS LOAD-BEARING.
    `ENER-04`'s `elicited_by` is `use-fireworks` and its `confronted_by` is
    `use-fireworks-reveal`; MRB-244/248 resolve those against `id="…"` on the
    built page, so both are emitted from the authored id rather than composed.

    HOOKS: `data-euse` (wrapper, `data-total`) · `data-euse-card` (valued with
    the card id) · `data-euse-opt` (valued with the option id) ·
    `data-euse-reveal`.
    """
    uses = a.get("uses") or []
    if len(uses) < 2:
        raise ValueError(
            "energy-uses %r declares %d card(s). The block's own heading is "
            "that ONE idea decides several different questions, and one card "
            "shows nothing of the sort." % (act_id, len(uses)))
    _counter_agrees(a, act_id, len(uses), "card(s)")

    seen = set()
    cards = []
    for u in uses:
        for key in ("id", "q", "answer", "correct"):
            if not u.get(key):
                raise ValueError(
                    "energy-uses %r card %r has no %r. The card opens on the "
                    "commitment and the answer is the whole of what opens."
                    % (act_id, u.get("id"), key))
        if u["id"] in seen:
            raise ValueError(
                "energy-uses %r authors the card id %r twice. It becomes a "
                "DOM id, and a duplicate is a misconception join that resolves "
                "to whichever came first." % (act_id, u["id"]))
        seen.add(u["id"])

        opts = u.get("options") or []
        if len(opts) < 2:
            raise ValueError(
                "energy-uses %r card %r offers %d option(s). A judgement needs "
                "something to judge against." % (act_id, u["id"], len(opts)))
        ids = [o.get("id") for o in opts]
        if len(set(ids)) != len(ids):
            raise ValueError(
                "energy-uses %r card %r reuses an option id: %s."
                % (act_id, u["id"], ids))
        for o in opts:
            if not o.get("label"):
                raise ValueError(
                    "energy-uses %r card %r has an option with no label."
                    % (act_id, u["id"]))
        if u["correct"] not in ids:
            raise ValueError(
                "energy-uses %r card %r marks %r correct and the buttons offer "
                "%s. The flag is the author's intent; it has to name one of "
                "the things a student can actually press."
                % (act_id, u["id"], u["correct"], sorted(ids)))

        cards.append(
            '<div class="ks3-euse-card" id="%s" data-euse-card="%s" '
            'data-open="0">'
            '<p class="ks3-euse-q">%s</p>'
            '<div class="ks3-euse-opts">%s</div>'
            '<p class="ks3-euse-answer" id="%s-reveal" data-euse-reveal '
            'hidden>%s</p></div>'
            % (e(u["id"]), e(u["id"]), rich(u["q"]),
               "".join(_c7_seg("ks3-euse-opt", False, o["label"],
                               data_euse_opt=o["id"]) for o in opts),
               e(u["id"]), rich(u["answer"])))

    return ('<div class="ks3-euse" data-euse data-total="%d">%s</div>'
            % (len(uses), "".join(cards)))


# ═══ c7-04 · rig-plan-critique ═══════════════════════════════════════════

def r_rig_plan_critique(a, act_id):
    """⊕ c7-04 `#s-plan` — five judgements on somebody else's method.

    ⚖️ **CRITIQUE COMES BEFORE CONSTRUCT** (NOTES-C7 §2, and the map's rule for
    an INVESTIGATION lesson). This is the FIRST instrument on the page: a
    student rules on five steps of a plan that is not theirs, discovers that
    two are sound, two are flawed and one would wreck the result on its own,
    and only then builds a rig. Judging somebody else's work first is what
    makes the construction a decision instead of a recipe.

    ⚠️ `data-rplan`, NOT `data-critiq` OR `data-critique`. Both are taken —
    `ks3_art/c3.py` owns the first for c3-07 and a biology family owns the
    second — and a shared selector would hand this instrument to another one's
    handler, after which neither works. Same shape, own family, own hooks.

    ⚖️ **THE THREE COUNTS IN THE LEAD ARE DERIVED AND ASSERTED.** "Two of the
    five are sound, two are flawed, and one would wreck the result on its own"
    is a sentence a student reads BEFORE ruling on anything, so it is a promise
    about the cards under it. All three numbers are computed from `sound` and
    `fatal` and checked against the authored claims.

    ⚠️ AND EACH VERDICT IS CHECKED TO OPEN WITH THE WORD THE RECORD BELIEVES.
    Design's step 1 reads "Sound as far as it goes, but the glass beaker is the
    weak point", which opens by agreeing with a student who pressed Sound and
    then disagrees with them. The lesson record states the judgement first and
    keeps her sentence whole underneath; this assertion is what keeps it that
    way.

    ⚠️ NOTHING MARKS. Two options, one shot, and a reveal in the same tone
    whichever button was pressed.

    HOOKS: `data-rplan` (wrapper, `data-total`) · `data-rplan-step` (valued
    with the step id) · `data-rplan-opt` (valued with the option id) ·
    `data-rplan-reveal`.
    """
    steps = a.get("steps") or []
    options = a.get("options") or []
    if not steps:
        raise ValueError("rig-plan-critique %r declares no steps[]." % act_id)
    if len(options) != 2:
        raise ValueError(
            "rig-plan-critique %r offers %d option(s); the judgement Design "
            "draws is two-way — is this step sound, or is it not."
            % (act_id, len(options)))
    _counter_agrees(a, act_id, len(steps), "step(s)")

    for o in options:
        if not o.get("id") or not o.get("label"):
            raise ValueError(
                "rig-plan-critique %r has an option with no id or no label."
                % act_id)
    # The FIRST option is the sound one and the second is the flawed one, in
    # the payload's own order — the same convention every dial in C3, C4 and C5
    # follows, and the reason the resting state is a property of the payload
    # rather than a string repeated here and again in the JS.
    sound_label = options[0]["label"]
    flawed_label = options[1]["label"]

    sound_n = fatal_n = 0
    cards = []
    for s in steps:
        for key in ("id", "tag", "step", "verdict", "why"):
            if not s.get(key):
                raise ValueError(
                    "rig-plan-critique %r step %r has no %r. Nothing here "
                    "marks, so the verdict and its reason are the only things "
                    "the instrument says." % (act_id, s.get("id"), key))
        is_sound = bool(s.get("sound"))
        is_fatal = bool(s.get("fatal"))
        if is_sound and is_fatal:
            raise ValueError(
                "rig-plan-critique %r step %r is flagged both sound and "
                "fatal." % (act_id, s["id"]))
        sound_n += 1 if is_sound else 0
        fatal_n += 1 if is_fatal else 0

        want = sound_label if is_sound else flawed_label
        if not s["verdict"].strip().lower().startswith(want.strip().lower()):
            raise ValueError(
                "rig-plan-critique %r step %r is flagged sound=%r, so a "
                "student presses %r and reads a verdict opening %r. The "
                "verdict has to state the judgement it was filed under, or "
                "the panel agrees and disagrees in one sentence."
                % (act_id, s["id"], is_sound, want, s["verdict"][:40]))

        cards.append(
            '<div class="ks3-rplan-step" data-rplan-step="%s" data-open="0">'
            '<p class="ks3-rplan-tag">%s</p>'
            '<p class="ks3-rplan-quote">%s</p>'
            '<div class="ks3-rplan-opts">%s</div>'
            '<div class="ks3-rplan-reveal" hidden data-rplan-reveal>'
            '<p class="ks3-rplan-verdict">%s</p>'
            '<p class="ks3-rplan-why">%s</p></div></div>'
            % (e(s["id"]), t(s["tag"]), t(s["step"]),
               "".join(_c7_seg("ks3-rplan-opt", False, o["label"],
                               data_rplan_opt=o["id"]) for o in options),
               t(s["verdict"]), rich(s["why"])))

    flawed_n = len(steps) - sound_n - fatal_n
    for claim, actual, what in (
            (a.get("sound_claim"), sound_n, "sound"),
            (a.get("flawed_claim"), flawed_n, "flawed but survivable"),
            (a.get("fatal_claim"), fatal_n, "fatal")):
        if claim is not None and int(claim) != actual:
            raise ValueError(
                "rig-plan-critique %r claims %s %s step(s) in its lead and "
                "holds %d. The lead is read before any card is decided."
                % (act_id, claim, what, actual))

    return ('<div class="ks3-rplan" data-rplan data-total="%d">%s</div>'
            % (len(steps), "".join(cards)))


# ═══ c7-04 · rig-builder ═════════════════════════════════════════════════

def _rigb_fix(v):
    return "%.1f" % float(v)


def r_rig_builder(a, act_id):
    """⊕ c7-04 `#s-bench` — three dials, eight rigs, and a value never reached.

    ⚖️ **THE BEST RIG STILL READS LOW, AND THAT IS THE INSTRUMENT.** The payoff
    panel is not congratulation: it is "you found the best rig — and it still
    reads low", which is the only honest place `ENER-08` can be confronted
    from. Everything this renderer checks is in service of that one claim being
    true of the data as well as of the prose.

    ⚖️ **THE WHOLE STATE SPACE IS ENUMERATED AND CHECKED (§5A).** Two vessels
    crossed with two tops crossed with two timings is eight rigs, and all eight
    are authored. A missing combination would show the previous rig's reading
    under the new rig's label; a surplus one is a rig nobody can reach and
    nobody would notice was wrong.

    ⚖️ **AND THREE MORE THINGS ARE DERIVED RATHER THAN TRUSTED:**

      · EVERY reading is strictly below the true value. The lesson says the
        error runs one way; a rig that over-read would make that false and
        would still render.
      · `best` really is the highest reading. It gates the payoff panel, so a
        stale `best` would open the panel on a rig that is not the best one and
        the panel's own arithmetic ("6.8 of the 7.0 degrees") would contradict
        the reading beside it.
      · The "lost" figure is `true − reading`, computed here. It is the one
        number on this bench that exists only to be subtracted, which is
        exactly the kind that gets authored twice and drifts.

    ⚠️ THE RIG TITLE IS COMPOSED AT BUILD TIME, ONCE PER COMBINATION, AND
    LIVES IN THE DOCUMENT. Design's page builds it in JS from three ternaries;
    that is a sentence assembled at run time and it is the thing this unit does
    not do. Each dial option carries a `phrase` — "lid fitted" against the
    button's "Lid with a hole" — and the eight titles are joined here.

    ⚠️ NOTHING HERE MARKS (R3). The accent on the best rig's lost-badge is a
    reading about the apparatus, not a verdict on the student: it says this
    arrangement is the closest the bench gets, and the panel beside it says
    that is still not enough.

    HOOKS: `data-rigb` (wrapper, `data-done-after`, `data-best`) ·
    `data-rigb-for` / `data-rigb-val` (dials) · `data-rigb-title` (valued with
    the rig key) · `data-rigb-run` · `data-rigb-panel` (valued with the rig
    key) · `data-rigb-close`.
    """
    dials = a.get("dials") or []
    rigs = a.get("rigs") or []
    if len(dials) != 3:
        raise ValueError(
            "rig-builder %r declares %d dial(s). NOTES-C7 §3 draws a "
            "three-dial apparatus chooser and the lookup is keyed on three "
            "values." % (act_id, len(dials)))
    if a.get("true_value") is None:
        raise ValueError(
            "rig-builder %r has no `true_value`. Every reading on this bench "
            "is reported as a shortfall against it." % act_id)
    true_v = float(a["true_value"])

    for d in dials:
        if not d.get("id") or not d.get("label"):
            raise ValueError(
                "rig-builder %r has a dial with no id or no label." % act_id)
        opts = d.get("options") or []
        if len(opts) < 2:
            raise ValueError(
                "rig-builder %r dial %r offers %d option(s). A dial with one "
                "setting is a control that does nothing, and §5A forbids "
                "drawing one." % (act_id, d["id"], len(opts)))
        for o in opts:
            for key in ("id", "label", "phrase"):
                if not o.get(key):
                    raise ValueError(
                        "rig-builder %r dial %r option %r has no %r. The label "
                        "is the button and the phrase is the title; both are "
                        "authored because Design words them differently."
                        % (act_id, d["id"], o.get("id"), key))

    # ── §5A · the whole state space ─────────────────────────────────────
    combos = [[]]
    for d in dials:
        combos = [c + [o] for c in combos for o in d["options"]]
    reachable = {"|".join(o["id"] for o in c): c for c in combos}
    authored = [r.get("id") for r in rigs]
    missing = sorted(set(reachable) - set(authored))
    surplus = sorted(set(authored) - set(reachable))
    if missing or surplus:
        raise ValueError(
            "rig-builder %r does not model what it draws. Dial combination(s) "
            "with no rig: %s. Rig(s) no dial can reach: %s. A bench with a "
            "hole in it shows the last rig's reading under the new rig's "
            "label." % (act_id, missing or "none", surplus or "none"))
    if len(set(authored)) != len(authored):
        raise ValueError(
            "rig-builder %r authors the same rig twice. One panel would be "
            "unreachable and no gate would see it." % act_id)

    best_id, best_v = None, None
    panels, titles = [], []
    for r in rigs:
        if not r.get("why"):
            raise ValueError(
                "rig-builder %r rig %r has no `why`. Eight readings with no "
                "explanations is a lookup table, not a lesson."
                % (act_id, r.get("id")))
        if r.get("v") is None:
            raise ValueError(
                "rig-builder %r rig %r has no reading." % (act_id, r["id"]))
        v = float(r["v"])
        if v >= true_v:
            raise ValueError(
                "rig-builder %r rig %r reads %s against a true value of %s. "
                "The lesson's claim is that every reading is an underestimate "
                "and that the error runs one way; a rig that reaches or passes "
                "the true value makes the closing panel false."
                % (act_id, r["id"], v, true_v))
        if best_v is None or v > best_v:
            best_id, best_v = r["id"], v

        title = " · ".join(o["phrase"] for o in reachable[r["id"]])
        titles.append(
            '<p class="ks3-rigb-title"%s data-rigb-title="%s">%s</p>'
            % ("" if r["id"] == "|".join(
                d["options"][0]["id"] for d in dials) else " hidden",
               e(r["id"]), t(title)))
        panels.append(
            '<div class="ks3-rigb-panel" hidden data-rigb-panel="%s">'
            '<div class="ks3-rigb-readout">'
            '<div class="ks3-rigb-figure">'
            '<p class="ks3-rigb-figlabel">%s</p>'
            '<p class="ks3-rigb-value">+%s °C</p></div>'
            '<div class="ks3-rigb-figure">'
            '<p class="ks3-rigb-figlabel">%s</p>'
            '<p class="ks3-rigb-value">+%s °C</p></div>'
            '<span class="ks3-rigb-lost"%s>%s%s</span></div>'
            '<p class="ks3-rigb-why">%s</p></div>'
            % (e(r["id"]),
               t(a.get("reading_label") or "Your reading"), t(_rigb_fix(v)),
               t(a.get("true_label") or "True value"), t(_rigb_fix(true_v)),
               ' data-best="1"' if r["id"] == a.get("best") else "",
               t(_rigb_fix(true_v - v)),
               t(a.get("lost_suffix") or " °C lost"),
               rich(r["why"])))

    if a.get("best") != best_id:
        raise ValueError(
            "rig-builder %r names %r as its best rig and the highest reading "
            "is %r at %s. `best` gates the payoff panel, whose own arithmetic "
            "quotes that reading."
            % (act_id, a.get("best"), best_id, best_v))

    dial_html = []
    for d in dials:
        dial_html.append(
            '<div class="ks3-rigb-dial">'
            '<p class="ks3-rigb-diallabel">%s</p>'
            '<div class="ks3-rigb-dialrow">%s</div></div>'
            % (t(d["label"]),
               "".join(_c7_seg("ks3-rigb-opt", i == 0, o["label"],
                               data_rigb_for=d["id"], data_rigb_val=o["id"])
                       for i, o in enumerate(d["options"]))))

    run = ('<div class="ks3-rigb-runrow" data-rigb-runrow>'
           '<button type="button" class="ks3-seg-btn ks3-rigb-run" '
           'data-rigb-run>%s</button></div>'
           % t(a.get("run_label") or "Run it"))

    close = _close_panel(a, "ks3-rigb", "data-rigb-close")

    return ('<div class="ks3-rigb" data-rigb data-done-after="%d" '
            'data-best="%s">'
            '<div class="ks3-rigb-dials">%s</div>'
            '<div class="ks3-rigb-bench">%s%s%s</div>%s</div>'
            % (int(a.get("done_after") or len(rigs)), e(a.get("best") or ""),
               "".join(dial_html), "".join(titles), run, "".join(panels),
               close))


# ═══ registrations ═══════════════════════════════════════════════════════
#
# ⊖ NO `ART`. NOTES-C7 §6 declares no drawn figure anywhere in the unit and
# every lesson record carries `figures: []`. An empty table is the same as no
# table to `ks3_art.load()`, and an ART entry with no `core[]` figure block
# behind it would fail registry gate 2 (registered but never placed).
#
# ⚠️ SIX FAMILIES, SIX DISTINCT SHELL CLASSES. MRB-279's assertion compares the
# CLASS each family renders into, not just the family name, because two
# families wearing one class puts one unit's stylesheet block on another unit's
# instrument and does it silently. Every class below was greped across
# `ks3_art/*.py`, `shared/ks3.js` and `shared/ks3.css` before it was taken.
#
# ⚠️ `rig-plan-critique` / `ks3-rplan-block`, NOT `plan-critique` /
# `ks3-critique-block`. Both of those are `ks3_art/c3.py`'s, for c3-07. Design's
# NOTES-C7 §3 calls C7's instrument "`c3-07`'s instrument with a different plan
# in it", which is true of the SHAPE and not of the OWNERSHIP: a lane may not
# edit another unit's module, so C7 draws its own and the two live side by side.

KIND_SHELL = {
    'heating-curve': ("ks3-hcurve-block",
                      ' data-instrument data-hcurveblock data-stage-done="0"'),
    'temp-bench': ("ks3-tempb-block",
                   ' data-instrument data-tempbblock data-stage-done="0"'),
    'energy-sorter': ("ks3-esort-block",
                      ' data-instrument data-esortblock data-stage-done="0"'),
    'energy-uses': ("ks3-euse-block",
                    ' data-instrument data-euseblock data-stage-done="0"'),
    'rig-plan-critique': ("ks3-rplan-block",
                          ' data-instrument data-rplanblock '
                          'data-stage-done="0"'),
    'rig-builder': ("ks3-rigb-block",
                    ' data-instrument data-rigbblock data-stage-done="0"'),
}

KIND_FN = {
    'heating-curve': r_heating_curve,
    'temp-bench': r_temp_bench,
    'energy-sorter': r_energy_sorter,
    'energy-uses': r_energy_uses,
    'rig-plan-critique': r_rig_plan_critique,
    'rig-builder': r_rig_builder,
}
