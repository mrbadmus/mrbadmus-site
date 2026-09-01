"""ks3_art.p12 — P12 *Space*, the unit where one number changes and one does not.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p12/`. Her page wins outright: a shape that is not in
her drawing is not in this module, and where her NOTES and her drawing disagree
the DRAWING IS MEASURED and the note is reported in `DEPARTURES-P12.md` beside
the delivery.

── ⚖️ ONE BENCH SHELL, SIX MODELS ───────────────────────────────────────

Design ships `Bench.dc.html` — ONE shared child component mounted by all six
P12 pages (and by all four P11 pages) with `<dc-import name="Bench" …>`. Its
shape is fixed and hers:

    commit gate  →  tab row  →  optional slider  →  a dark panel of
    proportional BARS  →  READOUT cards  →  the closing NOTE

The lesson supplies the physics; the component owns the layout. So this module
registers ONE family, `space-bench`, and the six pages differ only in the
`model` their payload names — which selects the arithmetic in `shared/ks3.js`
and nothing else. Six drawers for one drawn component would be six chances for
her layout to drift apart page by page.

⚠️ **NO SVG CARRIES A LIVE LABEL ON ANY P12 PAGE, AND THAT IS DESIGN'S OWN
NOTE.** `NOTES-P11-P12.md` §3: *"No SVG diagram carries a live label anywhere in
these ten lessons. Every varying figure is HTML text — a bar label, a readout
card or the note — which sidesteps the interpolated-text-in-`<text>` trap
entirely."* Measured and true: the bench draws no `<svg>` at all. The bars are
`<span>`s whose width is a percentage, so there is no `position: relative`
wrapper to get wrong and no `<text>` hole to render nothing.

── ⚖️ MRB-204 · THREE PAGES CARRY A TRIANGLE, THREE CARRY NONE ──────────

    p12-01  W = m × g          triangle + CFIFA   (QUANTITATIVE)
    p12-02  W = m × g          triangle + CFIFA   (CONTRAST — see below)
    p12-03  no block           nothing quantitative in the lesson
    p12-04  no block           nothing quantitative in the lesson
    p12-05  no block           nothing quantitative in the lesson
    p12-06  d = c × t          triangle + CFIFA   (QUANTITATIVE)

Both are PRODUCTS, so both take the triangle and neither takes a beam or a bar.
Design's README states why `p12-02` keeps the block although it is declared
CONTRAST: *"W = m × g is the whole content of the contrast, and the
gram-to-kilogram trap is where the distinction between mass and weight is
actually lost."* Her page draws it; MRB-205 makes her page the authority.

Her audit's other half is honoured too: *"P12 `p12-03`–`p12-05` have no worked
examples, correctly: nothing in either unit is quantitative, and the rule is not
to invent a calculation to fill the block."* Nothing is invented for them.

── ⚠️ `space-think` IS A SHELL, NOT A DRAWING ────────────────────────────

`p12-03`, `p12-04` and `p12-05` put `#s-think` on the rail. Design's `DONE` says
so in plain JavaScript:

    if (id === 's-think') return s.answers.r1 !== null || s.hookChoice !== null;

That is NOT the expression she gives `#s-bench` (`s.gate !== null && s.touched`),
so `ks3_rail_manifest` — which derives the mirror map by comparing her `isDone()`
expressions for equality — records no mirror for these three pages, and a
declared `mirrors` would fail `check_rail_matches_design` outright. The manifest
rows say `—` in the mirrors column for all six P12 lessons.

It is also not `band_anchor` / `band_at`: the bench does not tick it. Her
predicate is satisfied by the HOOK, which sits ABOVE the bench, or by the
LADDER, which sits below it — so a student can complete this stop without
touching the bench at all, and marking it from the bench would tick it late and
on the wrong event.

So P12 registers its OWN shell-only family for the section, exactly as `p9-01`'s
`charge-think` and `p8-01`'s `circ-think` do, and gives it a wire function of
its own — which is the one difference from both of those, and it is forced by
her predicate rather than chosen.

`r_space_think` draws NOTHING, deliberately, and that is not a hole:
`r_activity` renders a `misconception` BLOCK's whole body from its block type
(`r_confrontation`, both quotes and both bodies) and sets
`head_emitted_content` BEFORE the kind's renderer is reached, so the
empty-activity gate is satisfied by real content rather than bypassed. Markup
returned here would be markup Design did not draw, landing under her second
quote.

The shell exists for one reason: `check_nothing_ticks_on_load` requires any
`data-instrument` section that IS a rail anchor to declare `data-stage-done="0"`
in the SHIPPED BYTES, because the rail's first paint runs before the instruments
wire. `ks3_art/core.py`'s shared `confrontation` shell emits the marker without
the declaration, and that file belongs to ten units.

`p12-01`, `p12-02` and `p12-06` keep the ordinary `predict` kind on their
`#s-think`, because on those three pages the third stop is `#s-formula` and the
confrontation is off the rail exactly as everywhere else in the key stage.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279, and it mattered here: `ks3-sbench-`
and `ks3-bbench-` — the two obvious stems for a bench — are both TAKEN by other
units. This unit uses `ks3-spbench-`, `ks3-spthink` and `ks3-p12cfa-`, all three
checked against `ks3_art/*.py`, `shared/ks3.js` and `shared/ks3.css` first.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. The bench uses none of the four; the worked examples DO use `fifa`,
which is exactly what that key is for.

── ⚠️ NO `_head` HERE, AND THAT IS A REPAIR RATHER THAN AN OMISSION ──────

P4, P5 and P6 each define one and each of their benches calls it — and so does
`r_activity`'s own shell, from the same payload keys, so those units ship every
bench heading twice. P7, P8 and P9 stopped doing it and this unit does not start
again. The shell owns the head row: eyebrow and heading left, the readout right,
driven through the engine's own `setCountState`, which IS Design's layout.

⚠️ The readout is authored as a MAP OF NAMED STATES (`idle` / `live`), not as a
string. A string routes to `_head_counter` as a COUNT FORMAT; the dict routes to
`_progress_readout`, which is the shape Design's bench actually has — two named
states, no number in either. And nothing in `r_space_bench` reads that key, so
`_kinds_consuming` correctly leaves the head row to the shell.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

import re

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ═══ the six models, and what each one's payload has to carry ════════════
#
# ⚖️ A MODEL IS A CONTRACT, NOT A LABEL. `model` selects the arithmetic in
# `shared/ks3.js`; the tables below are what makes that selection checkable at
# BUILD time rather than in a browser. A page that names a model and then fails
# to author a note branch it will reach ships a bench with an empty note panel
# in some reachable state — the p5-01 defect — and every gate in the build reads
# an empty note panel as a live instrument.
#
# `branches` are the note templates the model can select between; `words` are
# the short readout strings it interpolates. Both are asserted exactly: a
# missing one raises, and so does an extra one nothing reads (R5).
_MODELS = {
    # p12-01 · five places to stand × five masses on the scales.
    "field-strength": {
        "branches": ("field", "zero"),
        "words": ("mass_sub", "g_sub", "weight_sub", "ratio_sub",
                  "zero_ratio", "bar_sub", "list_join"),
        "slider": True,
        "needs": ("earth_g",),
    },
    # p12-02 · one object × four places, two columns, one of them still.
    "weight-in-four-places": {
        "branches": ("same", "less", "more"),
        "words": ("mass_sub", "g_sub", "weight_sub", "measured_value",
                  "measured_sub", "bar_sub", "list_join"),
        "slider": True,
        "needs": ("earth_g",),
    },
    # p12-03 · four gravitational pairs × four separations.
    "inverse-square": {
        "branches": ("real", "moved"),
        "words": ("pull_value", "real_sub", "multiple_sub",
                  "multiple_sub_real", "partner_value", "partner_sub",
                  "bar_full", "bar_frac", "list_join"),
        "slider": True,
        "needs": (),
    },
    # p12-04 · five rungs of the LADDER OF SCALE. No slider: her `SLIDER`
    # is the empty array, so `hasSlider` is false and the component draws
    # none.
    #
    # ⊕ MRB-297 · 1 Sep 2026 — this said "the distance ladder", which is
    # what the page called it before this run renamed it. Kept rather than
    # deleted so the rename is findable from either name. ⚠️ The MODEL KEY
    # below is still `distance-ladder`, and must stay: it is the string
    # `shared/ks3.js` dispatches on and the payload authors. The rename was
    # to the student-visible wording only.
    "distance-ladder": {
        "branches": ("rung",),
        "words": ("what_sub", "distance_sub", "size_sub", "stars_sub",
                  "list_join"),
        "slider": False,
        "needs": ("scale",),
    },
    # p12-05 · four dates in the orbit × three places on the Earth.
    "seasons": {
        "branches": ("season",),
        "words": ("date_sub", "daylight_sub", "noon_sub", "energy_sub",
                  "bar_value", "bar_sub", "verdict_summer", "verdict_winter",
                  "verdict_between", "verdict_even", "list_join"),
        "slider": True,
        "needs": (),
    },
    # p12-06 · five light journeys, one speed. No slider, as p12-04.
    "light-time": {
        "branches": ("journey",),
        "words": ("takes_sub", "distance_sub", "metres_sub", "seeing_value",
                  "seeing_sub", "list_join"),
        "slider": False,
        "needs": ("c", "scale"),
    },
}

_FIELD_NAME = re.compile(r"^[a-z][a-z0-9]*$")
_TOKEN_RE = re.compile(r"\{([a-zA-Z0-9_]+)\}")


def _rest_fill(tpl, rest, act_id, where):
    """Fill a `{token}` template with the bench's OPENING values.

    ⚠️ THE BYTES A CRAWLER GETS ARE THE RESTING STATE, AND THEY HAVE TO BE
    REAL. `ks3_smoke --static` gates exactly this: a template left unexpanded
    in the shipped HTML ships the brace itself to a reader with JavaScript off,
    to a crawler, and into the search snippet. `ks3_art.kit._rest_fill` learned
    it on the CFIFA block and the same rule applies to any live string the
    bench owns — Design's `p12-03` readout card is labelled *"At × 1 the
    distance"* and the 1 moves with the slider.

    So the template is filled HERE from the tab and slider positions the bench
    OPENS on, and `data-template` is kept beside it for the wiring to refill
    from live state. A token with no resting value RAISES.
    """
    def sub(m):
        key = m.group(1)
        if key not in rest:
            raise ValueError(
                "space-bench %r: %s uses {%s}, and neither the opening tab nor "
                "the opening slider position gives it a value. The RESTING "
                "text has to be the bench's opening state — otherwise the "
                "brace itself ships to a student reading without JavaScript, "
                "which is what `ks3_smoke --static` gates."
                % (act_id, where, key))
        return str(rest[key])
    return _TOKEN_RE.sub(sub, tpl or "")


def _rest_map(tabs, start_tab, slider):
    """The opening state, as a token map: the start tab's fields, then the
    start slider position's, which wins on a collision because it is the
    control nearer the reading."""
    rest = {}
    for row in (tabs[start_tab],):
        rest.update({k: v for k, v in row.items() if k != "id"})
    if slider:
        row = slider["values"][int(slider["start"])]
        rest.update({k: v for k, v in row.items() if k != "id"})
    return rest


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


def _fields(row, act_id):
    """A row's model fields, as `data-f-*` attributes.

    Every per-tab and per-slider-value number Design's `renderVals` reads —
    `g`, `m`, `F`, `ly`, `dia`, `count`, `dec`, `lat`, `t` — travels to the
    wiring this way rather than as a per-model dict in JavaScript. The names
    are constrained so the attribute cannot be ambiguous: a key with an
    underscore or a capital would collide with the `data-*` → dataset
    lowercasing rule and silently arrive under a different name.
    """
    out = ""
    for key in sorted(row):
        if key in ("id", "label"):
            continue
        if not _FIELD_NAME.match(key):
            raise ValueError(
                "space-bench %r: model field %r must be lowercase letters and "
                "digits only. `data-*` attribute names are lowercased by the "
                "DOM, so %r would arrive in the wiring under a name nothing "
                "reads, and it would do it in silence."
                % (act_id, key, key))
        out += ' data-f-%s="%s"' % (key, e(row[key]))
    return out


def _gate(act_id, gate):
    """The commit gate the bench opens behind.

    All ten P11/P12 benches are locked until a prediction is made, and on all
    ten Design's own `DONE` for `#s-bench` reads `s.gate !== null && s.touched`
    — so the gate is not decoration, it is half of what ticks the second rail
    stop. Her `Bench` hides the gate the moment it is answered
    (`gateShown: … && !p.open`), which is gating by replacement: the instrument
    arrives in the space the question was occupying.
    """
    if not gate.get("prompt") or len(gate.get("options") or []) != 4:
        raise ValueError(
            "space-bench %r has no four-option commit gate. A bench read "
            "before a commitment confirms whatever the student already "
            "believed, and Design draws four options on every one of the six."
            % act_id)
    if not isinstance(gate.get("answer"), int):
        raise ValueError(
            "space-bench %r declares no `answer` on its gate. Nothing on the "
            "page marks it — MRB-196 R10 forbids that here — but the note "
            "beneath the bench is written knowing which one is right, and an "
            "unrecorded answer is a fact about the lesson kept nowhere."
            % act_id)
    opts = "".join(
        '<li><button type="button" class="ks3-option" data-spbench-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button></li>'
        % (i, chr(65 + i), t(o))
        for i, o in enumerate(gate["options"]))
    return ('<div class="ks3-spbench-gate" data-spbench-gate>'
            '<p class="ks3-commit">%s</p><ul class="ks3-options">%s</ul>'
            '</div>' % (t(gate["prompt"]), opts))


def _branches(a, act_id, need):
    """The per-state note templates, as hidden spans the wiring reads.

    ⚖️ **EVERY SENTENCE A STUDENT READS LIVES IN THE LESSON RECORD.** Design
    composes her note in `renderVals` with `+` and a ternary; ported literally
    that would put a paragraph of teaching prose inside `shared/ks3.js`, where
    no content gate can see it and no examiner can find it. Here the note is an
    authored `{token}` template per branch and the wiring fills it — arithmetic
    in the engine, sentences in the record.
    """
    spec = a.get("notes") or {}
    missing = [k for k in need if not spec.get(k)]
    if missing:
        raise ValueError(
            "space-bench %r has no note for state(s) %s. Every reachable state "
            "has something true to say (5A.1), and a branch that renders "
            "nothing ships a bench with an empty note panel — which every "
            "gate in the build reads as a live instrument."
            % (act_id, ", ".join(missing)))
    extra = sorted(set(spec) - set(need))
    if extra:
        raise ValueError(
            "space-bench %r authors note branch(es) %s, which model %r never "
            "selects. An authored branch no student can reach is copy nobody "
            "will read." % (act_id, ", ".join(extra), a.get("model")))
    return "".join(
        '<span data-spbench-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(spec[k])) for k in need)


def _words(a, act_id, need):
    """The short readout strings — the ones that are not a whole sentence.

    Same seam as `_branches` and the same argument: `the same everywhere`,
    `weight only, never mass`, `a spring balance would give the weight` are all
    strings a student READS, so they are authored beside the physics rather
    than typed into the engine. A missing one renders as an empty readout tile,
    which looks like a live instrument to every gate there is.
    """
    spec = a.get("words") or {}
    missing = [k for k in need if not spec.get(k)]
    if missing:
        raise ValueError(
            "space-bench %r has no `words` entry for %s."
            % (act_id, ", ".join(missing)))
    extra = sorted(set(spec) - set(need))
    if extra:
        raise ValueError(
            "space-bench %r authors `words` %s, which nothing reads. An "
            "authored key no renderer looks at is what `ks3_key_audit` is for, "
            "and a string a student was meant to see and never does is worse "
            "than a missing one." % (act_id, ", ".join(extra)))
    return "".join(
        '<span data-spbench-word="%s" data-text="%s" hidden></span>'
        % (e(k), e(spec[k])) for k in need)


# ═══ #s-bench · Design's shared Bench, on all six pages ══════════════════

def r_space_bench(a, act_id):
    """⊕ P12's `#s-bench` — one shell, six models.

    ⚖️ **THE MODEL IS THE LESSON, AND EVERY FIGURE ON THE BENCH IS DERIVED
    FROM IT.** Nothing is authored beside a value it could contradict: the bar
    values, the bar percentages, the readouts, the comparative words and the
    `aria-label` are all computed from the tab and slider fields at render
    time. 5A.1's rule, and the reason the equal state and the zero state are
    true by construction rather than by somebody remembering.

    ⚖️ **THE `aria-label` NAMES EVERY BAR THAT IS DRAWN.** Composed from the
    bars themselves through the `{list}` token, so a sixth bar cannot arrive
    without appearing in it. Design's own `barsAlt` on `p12-01` lists four of
    the five she draws — deep space, at 0.0 N/kg, is the one it leaves out, and
    it is the state the whole second half of the lesson turns on. Registered in
    `DEPARTURES-P12.md`.

    ⚖️ **WEIGHT IS ALWAYS mass × 10 N/kg ON EARTH, AND THE PAGE SAYS SO.**
    `g = 10 N/kg` is statutory (`KS3.P.SPACE.01`) and is the figure used
    throughout; the legal line on each page records that Earth's true mean
    value is 9.81.

    HOOKS: `data-spbench` (wrapper, `data-model`, `data-start-tab`,
    `data-start-slider`, `data-c`, `data-log-offset`, `data-log-span`,
    `data-min-pct`) · `data-spbench-gate` · `data-spbench-gopt` ·
    `data-spbench-body` · `data-spbench-tab` (carrying `data-f-*`) ·
    `data-spbench-slider` · `data-spbench-sv` (carrying `data-f-*`) ·
    `data-spbench-bar` / `-barvalue` / `-barfill` / `-barsub` ·
    `data-spbench-bars` (the `role="img"` whose label is rewritten) ·
    `data-spbench-out` · `data-spbench-sub` · `data-spbench-note` ·
    `data-spbench-branch` · `data-spbench-word`.
    """
    model = a.get("model")
    spec = _MODELS.get(model)
    if spec is None:
        raise ValueError(
            "space-bench %r names model %r, which `shared/ks3.js` has no "
            "compute function for. Known: %s. A bench whose model nothing "
            "implements renders its gate, opens on a press and then shows five "
            "em dashes for ever."
            % (act_id, model, ", ".join(sorted(_MODELS))))

    for key in spec["needs"]:
        if not a.get(key):
            raise ValueError(
                "space-bench %r names model %r and authors no %r. That model "
                "reads it in `shared/ks3.js`, so without it the arithmetic "
                "runs on NaN and every readout on the bench prints "
                "\u201cNaN\u201d — which is a rendered page, and therefore a "
                "page every gate in the build reads as fine."
                % (act_id, model, key))
    if a.get("scale"):
        for key in ("log_offset", "log_span", "min_pct"):
            if key not in a["scale"]:
                raise ValueError(
                    "space-bench %r authors a `scale` with no %r. The two "
                    "ladders span eleven and fifteen orders of magnitude and "
                    "are Design's own log placement; a missing constant "
                    "collapses every bar onto the floor." % (act_id, key))

    tabs = a.get("tabs") or []
    if len(tabs) < 4:
        raise ValueError(
            "space-bench %r declares %d tab(s). Design draws four or five on "
            "every P12 bench, and a tab row of three cannot carry the "
            "comparison any of these lessons is making." % (act_id, len(tabs)))
    _unique(tabs, act_id, "space-bench", "tab")
    for row in tabs:
        for f in ("id", "label"):
            if not row.get(f):
                raise ValueError("space-bench %r tab %r has no %r."
                                 % (act_id, row.get("id"), f))

    slider = a.get("slider") or None
    if bool(slider) != spec["slider"]:
        raise ValueError(
            "space-bench %r %s a slider and model %r %s one. Design's "
            "`hasSlider` is `!!p.sliderLabel`, so `p12-04` and `p12-06` — "
            "whose `SLIDER` is the empty array — draw no slider at all, and a "
            "bench that grew one would be a control Design did not draw."
            % (act_id, "authors" if slider else "authors no", model,
               "needs" if spec["slider"] else "draws none"))
    if slider:
        for f in ("id", "label", "values", "start", "value_label"):
            if f not in slider:
                raise ValueError("space-bench %r slider has no %r."
                                 % (act_id, f))
        _unique(slider["values"], act_id, "space-bench", "slider value")
        if len(slider["values"]) < 3:
            raise ValueError(
                "space-bench %r gives its slider %d position(s). Design's "
                "shortest is three." % (act_id, len(slider["values"])))
        if not 0 <= int(slider["start"]) < len(slider["values"]):
            raise ValueError(
                "space-bench %r opens its slider at index %r, which is not one "
                "of its %d positions — the bench would open on a state that "
                "does not exist."
                % (act_id, slider["start"], len(slider["values"])))

    bars = a.get("bars") or []
    if len(bars) < 3:
        raise ValueError(
            "space-bench %r draws %d bar(s). The bar panel IS the comparison "
            "on all six pages, and Design's smallest is three."
            % (act_id, len(bars)))
    _unique(bars, act_id, "space-bench", "bar")
    if not a.get("bars_alt") or "{list}" not in a["bars_alt"]:
        raise ValueError(
            "space-bench %r has no `bars_alt` carrying `{list}`. The label on "
            "the bar panel is the whole figure to a reader who cannot see it, "
            "and composing it from the bars themselves is what stops it naming "
            "four of five drawn bars — which is what Design's own `p12-01` "
            "label does." % act_id)

    readouts = a.get("readouts") or []
    if len(readouts) != 4:
        raise ValueError(
            "space-bench %r declares %d readout card(s); Design draws four on "
            "every one of the six." % (act_id, len(readouts)))
    _unique(readouts, act_id, "space-bench", "readout")

    start_tab = int(a.get("start_tab", 0))
    if not 0 <= start_tab < len(tabs):
        raise ValueError(
            "space-bench %r opens on tab index %d of %d."
            % (act_id, start_tab, len(tabs)))

    rest = _rest_map(tabs, start_tab, slider)

    tabrow = "".join(
        '<button type="button" class="ks3-seg-btn ks3-spbench-tab" '
        'data-spbench-tab="%s" data-label="%s" aria-pressed="%s"%s>%s</button>'
        % (e(row["id"]), e(row["label"]),
           "true" if i == start_tab else "false",
           _fields(row, act_id), t(row["label"]))
        for i, row in enumerate(tabs))

    control = ""
    svdata = ""
    if slider:
        control = (
            '<div class="ks3-spbench-row">'
            '<div class="ks3-spbench-rowhead">'
            '<label for="%s-sv">%s</label>'
            '<p class="ks3-spbench-reading" data-spbench-out="slider" '
            'data-template="%s">%s</p>'
            '</div>'
            '<input class="ks3-spbench-slider" type="range" id="%s-sv" '
            'min="0" max="%d" step="1" value="%d" data-spbench-slider>'
            '</div>'
            % (e(act_id), t(slider["label"]),
               e(slider["value_label"]),
               t(_rest_fill(slider["value_label"], rest, act_id,
                            "the slider's reading")),
               e(act_id), len(slider["values"]) - 1, int(slider["start"])))
        svdata = "".join(
            '<span data-spbench-sv="%d" data-id="%s" data-label="%s"%s '
            'hidden></span>'
            % (i, e(row["id"]), e(row.get("label", "")), _fields(row, act_id))
            for i, row in enumerate(slider["values"]))

    barrows = "".join(
        '<div class="ks3-spbench-bar" data-spbench-bar="%s">'
        '<div class="ks3-spbench-barhead">'
        '<span class="ks3-spbench-barlabel">%s</span>'
        '<span class="ks3-spbench-barvalue" data-spbench-barvalue="%s">'
        '—</span></div>'
        '<span class="ks3-spbench-track">'
        '<span class="ks3-spbench-fill" data-spbench-barfill="%s"></span>'
        '</span>'
        '<p class="ks3-spbench-barsub" data-spbench-barsub="%s"></p></div>'
        % (e(row["id"]), t(row["label"]), e(row["id"]), e(row["id"]),
           e(row["id"]))
        for row in bars)

    tiles = "".join(
        '<div class="ks3-spbench-tile">'
        '<p class="ks3-spbench-tile-label" data-spbench-tlabel="%s" '
        'data-template="%s">%s</p>'
        '<p class="ks3-spbench-tile-value" data-spbench-out="%s">—</p>'
        '<p class="ks3-spbench-tile-sub" data-spbench-sub="%s">—</p>'
        '</div>'
        % (e(row["id"]), e(row["label"]),
           t(_rest_fill(row["label"], rest, act_id,
                        "readout %r's label" % row["id"])),
           e(row["id"]), e(row["id"]))
        for row in readouts)

    lead = ('<p class="ks3-spbench-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    scale = a.get("scale") or {}
    scale_attrs = "".join(
        ' data-%s="%s"' % (k.replace("_", "-"), e(v))
        for k, v in sorted(scale.items()))
    speed = (' data-c="%s"' % e(a["c"])) if a.get("c") else ""
    if a.get("earth_g"):
        speed += ' data-earth-g="%s"' % e(a["earth_g"])

    return ('<div class="ks3-spbench" data-spbench data-model="%s" '
            'data-start-tab="%d"%s%s%s>%s%s'
            '<div class="ks3-spbench-body" data-spbench-body hidden>'
            '<div class="ks3-spbench-controls">'
            '<div class="ks3-spbench-picker">'
            '<p class="ks3-spbench-pickerlabel">%s</p>'
            '<div class="ks3-spbench-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-spbench-panel">'
            '<p class="ks3-spbench-caption">%s</p>'
            '<div class="ks3-spbench-bars" role="img" aria-label="" '
            'data-spbench-bars data-template="%s">%s</div></div>'
            '<div class="ks3-spbench-readouts">%s</div>'
            '<p class="ks3-spbench-note" data-spbench-note></p>'
            '%s%s%s</div></div>'
            % (e(model), start_tab,
               (' data-start-slider="%d"' % int(slider["start"])) if slider
               else "",
               speed, scale_attrs,
               lead, _gate(act_id, a.get("gate") or {}),
               t(a.get("tabs_label", "")), tabrow, control,
               t(a.get("bars_caption", "")), e(a["bars_alt"]), barrows,
               tiles,
               svdata,
               _branches(a, act_id, spec["branches"]),
               _words(a, act_id, spec["words"])))


# ═══ #s-formula · the CFIFA attempt on p12-01, p12-02 and p12-06 ═════════

def r_p12_attempt(a, act_id):
    """⊕ P12's half of Design's `Cfifa`: the student's own five lines.

    Her `Cfifa.dc.html` in this delivery is BYTE-IDENTICAL to the one in
    `docs/ks3/design-reference/p7/` — checked, not assumed — so the drawing is
    `ks3_art.kit.r_cfifa_attempt`, shared with P4, P5, P6 and P7, and the
    FAMILY is P12's own so `ks3_art.load()`'s one-family-one-module rule holds
    and the placement gates see it as this unit's.

    ⊕ ONE EYEBROW, NOT TWO. The `check` shell already prints this activity's
    eyebrow in Design's `.ks3-blockhead`; the kit helper prints it again unless
    told not to. P4–P6 ship it twice (measured); P7 opts out by passing `None`
    and so does this.

    ⚠️ `p12-01`'s QUESTION 1 CAN BE BLOCKED, AND THE BLOCKED LINE IS HERS.
    Her Q1 carries `blocked: T.g === 0` — in deep space every weight comes out
    as nothing, so the five lines have nothing to say — plus a `lead` shown
    only in that state and a `blockedProgress` string for the little readout
    beside the Check button. The kit already draws the blocked paragraph from
    `blocked_lead`; the progress string has no slot in it, and rather than edit
    a file five units share it travels as a span of this unit's own, read by
    `wireCfifaAttemptP12`.
    """
    hint = ""
    if a.get("blocked_hint"):
        if not any((q.get("blocked_lead") or "")
                   for q in (a.get("questions") or [])):
            raise ValueError(
                "p12-attempt %r authors a `blocked_hint` and no question that "
                "can be blocked. The string would never be shown." % act_id)
        hint = ('<span data-p12cfa-blockhint data-text="%s" hidden></span>'
                % e(a["blocked_hint"]))
    return r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p12cfa") + hint


# ═══ #s-think · the shell of a rail-bearing confrontation ════════════════

def r_space_think(a, act_id):
    """⊕ `p12-03`, `p12-04` and `p12-05`'s `#s-think`. THE SHELL IS THE WHOLE
    COMPONENT.

    This renderer draws nothing, on purpose; the module docstring says why at
    length. Briefly: the block's content is already on the page when this is
    called, because `r_activity` renders a `misconception` block's two quotes
    and two bodies from its BLOCK TYPE before the kind dispatch runs. Anything
    returned here would land under Design's second quote and would be markup
    she did not draw.

    ⚠️ THE PAYLOAD IS STILL VALIDATED. A `space-think` block with no
    `statements` would fall back to rendering the REGISTER's paraphrase of the
    belief rather than the page's own wording — the `b1-01` defect exactly, and
    the dangerous kind, because it renders something and therefore looks
    finished.
    """
    if len(a.get("statements") or []) < 2:
        raise ValueError(
            "space-think %r declares %d statement(s). Design draws TWO wrong "
            "ideas in this block, the second behind her amber rule, and a "
            "block with none falls back to the register's paraphrase — which "
            "renders, and therefore looks finished."
            % (act_id, len(a.get("statements") or [])))
    # ⚠️ A TYPO IN THE TICKING CONTRACT SHIPS A DEAD RAIL STOP, IN SILENCE, AND
    # IT DID IN P6. This section is a RAIL STOP on all three pages that use it
    # and carries no control of its own: `wireSpaceThink` ticks it from the
    # HOOK's options and from ladder rung 1, which is Design's own predicate
    # (`s.answers.r1 !== null || s.hookChoice !== null`). The near-miss keys
    # below are the ones a bench-ticked section would carry, and a bench cannot
    # tick this one — her predicate is satisfied without touching it.
    for wrong in ("band_anchor", "band_at", "sibling", "mirrors", "mirror"):
        if wrong in a:
            raise ValueError(
                "space-think %r carries %r. This section is NOT ticked by the "
                "bench: Design's predicate is the hook OR ladder rung 1, both "
                "of which a student can reach without touching the bench, so "
                "marking it from the bench would tick it late and on the wrong "
                "event. `wireSpaceThink` owns it." % (act_id, wrong))
    return ""


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P12's own — `ks3_art/core.py` and
# `ks3_art/kit.py` are untouched. Shell stems were checked against the whole
# registry first and two obvious ones were already taken: `ks3-sbench-` and
# `ks3-bbench-`. That is the MRB-279 collision exactly, and it is cheaper to
# find here than in a browser open on somebody else's page.

ART = {}

KIND_SHELL = {
    'space-bench':  ("ks3-spbench-block",
                     ' data-instrument data-spbenchblock '
                     'data-stage-done="0"'),
    'p12-attempt':  ("ks3-p12cfa-block",
                     ' data-instrument data-p12cfablock '
                     'data-stage-done="0"'),
    # ⚠️ SHELL ONLY. See `r_space_think`. The declaration is the component.
    'space-think':  ("ks3-spthink",
                     ' data-instrument data-spthink '
                     'data-stage-done="0"'),
}

KIND_FN = {
    'space-bench':  r_space_bench,
    'p12-attempt':  r_p12_attempt,
    'space-think':  r_space_think,
}
