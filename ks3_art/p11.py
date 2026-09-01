"""ks3_art.p11 — P11 *Matter and the particle model*, four benches on one shell.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p11/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported in
`DEPARTURES-P11.md` beside the delivery.

── ⚖️ ONE SHELL, FOUR MODELS — AND THAT IS DESIGN'S OWN DECISION ─────────

`Bench.dc.html` is a CHILD COMPONENT she wrote once and mounted on all ten
P11/P12 pages with `<dc-import name="Bench" …>`: commit gate → tab row →
optional slider → a dark panel of proportional bars → readout cards → the
closing note. The lesson supplies the physics and the component owns the
layout. So `matter-bench` is one family with one drawer, and the arithmetic
that differs page to page is selected by `model` — `density`, `brownian`,
`internal-energy`, `ice` — which names the function in `shared/ks3.js`.

P12 is building the same shell under its own family from the same payload
schema, deliberately: two lanes, two families (the registry refuses a shared
one), one shape.

── ⚖️ EVERY VARYING FIGURE IS HTML TEXT. NO LIVE LABEL IN AN SVG. ────────

Design's §3: *"No SVG diagram carries a live label anywhere in these ten
lessons. Every varying figure is HTML text — a bar label, a readout card or
the note — which sidesteps the interpolated-text-in-`<text>` trap entirely."*
There is no `<svg>` in this module at all, which is why there is no `<desc>`
convention here to follow: the bars are HTML, and the panel carries Design's
own `role="img"` + `aria-label` composed live from the values.

── ⚖️ MRB-204 · ONE FORMULA BLOCK IN THE UNIT, ON `p11-01`, AND IT IS A
   TRIANGLE ───────────────────────────────────────────────────────────────

`m = d × V` is a genuine PRODUCT, so the triangle is the right figure and
`m` is the letter on top. Design draws exactly that — her `<path>` puts `m`
above the dividing line and `d × V` below it — and her `COVERS` map gives
the three arrangements. `p11-02`, `p11-03` and `p11-04` carry no formula
block and none is missing: her audit says *"the rule is not to invent a
calculation to fill the block"*, and all three are MODEL/CONTRAST lessons.

The triangle itself is drawn by the shared `r_cover_triangle`; this module
adds nothing to it. The five-step attempt below it is `p11-attempt`, which
is `ks3_art.kit.r_cfifa_attempt` in P11's own namespace — the same route
`ks3_art/p7.py` takes, and for the same reason: Design's `Cfifa.dc.html` in
this folder is BYTE-IDENTICAL to P7's, so the engine already renders it.

── ⚖️ AMBER IS NOT A SELECTION COLOUR, AND `--ks3-data` ALONE CANNOT MARK
   THE SELECTED BAR ────────────────────────────────────────────────────────

Design fills the bar in focus with `var(--ks3-alert)` on three of the four
benches (`p11-01`, `p11-03`, `p11-04` — the selected material/amount/state)
and on `p11-02` marks the one visible quantity with it. MRB-252's ruling
reserves amber for warning and confrontation and sends category and
selection to `--ks3-data`.

⚠️ **THE SUBSTITUTION ON ITS OWN WOULD ERASE THE HIGHLIGHT.**
`--ks3-data` and `--ks3-blue-light` are the SAME VALUE today (`#8FB7FF`,
minted that way on purpose so the roles can separate later), and the other
bars are `--ks3-blue-light`. Swapping the token would leave six bars in one
colour and make the panel's own aria-label — *"…with gold highlighted"* —
false. That is the `p9-03` test-point argument exactly.

So the focus bar takes BOTH halves: the `--ks3-data` token, so the role is
named correctly and the two colours can move apart, AND a structural mark
that works today — a 3px `--ks3-on-dark` ring on its track and its label at
800. That is 5A.4's ruled answer where no legal category hue is available:
*"a figure that carries no category hue carries the distinction on something
else, and says so."* Registered in `DEPARTURES-P11.md`.

── ⚠️ `matter-think` IS A SHELL, NOT A DRAWING ───────────────────────────

`#s-think` is the THIRD RAIL STOP on `p11-02`, `p11-03` and `p11-04`.
Design's `DONE` for it reads

    if (id === 's-think') return s.answers.r1 !== null || s.hookChoice !== null;

— it ticks when the hook is committed OR ladder rung 1 is answered, which is
a page-level predicate and not a sibling of the bench. `mirrors` cannot
express it: `ks3_rail_manifest` derives the mirror map from her `isDone()`
and this expression matches no other stop's, so a declared mirror fails
`check_rail_matches_design` outright — which is why the manifest's `mirrors`
column reads `—` on all four rows.

A rail anchor has to satisfy two gates a plain `predict` confrontation
cannot: `check_rail_reachable` wants a signal `doneByDom()` reads, and
`check_nothing_ticks_on_load` wants any `data-instrument` section that is a
rail anchor to declare `data-stage-done="0"` **in the shipped bytes**,
because the rail's first paint runs before the instruments wire.
`ks3_art/core.py`'s shared `confrontation` shell emits the marker without
the declaration, and that file belongs to ten units.

So P11 registers its own family for those three sections, exactly as P9's
`charge-think` and P8's `circ-think` do. `r_matter_think` draws NOTHING, on
purpose: `r_activity` renders a `misconception` BLOCK's two quotes and two
bodies from its BLOCK TYPE (`r_confrontation`) and sets
`head_emitted_content` before the kind's renderer is reached, so the
empty-activity gate is satisfied by real content rather than bypassed, and
anything returned here would be markup Design did not draw landing UNDER her
second quote.

⊕ This is the second unit to put `#s-think` on a rail. `p9-01`'s package
note flags *"Think-again as a rail stop"* as open for Mide; three more
lessons arrive at it from Design's own `DONE`, and the flag is NOT re-raised
here — it is noted in the misconception register beside the P11 entries so
one decision covers all four.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279. `ks3-mtbench-`, `ks3-mtthink` and
`ks3-p11cfa-` were checked against every module before they were written.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. The worked examples on `p11-01` DO author `fifa`, which is correct
and intended — that is the staged five-step reveal. Nothing else in the unit
uses any of the four.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ═══ shared P11 primitives ═══════════════════════════════════════════════

# Which per-tab fields each model needs. This is a REAL gate rather than
# bookkeeping: a bench whose tabs are missing a field renders a bar whose
# value is the literal template, and the liveness sweep sees a live block.
# Naming them here also keeps every key a literal in both this file and
# `shared/ks3.js`, which is what `ks3_key_audit` reads.
MODEL_FIELDS = {
    "density":         ("label", "name", "d"),
    "brownian":        ("label", "name", "speck", "hidden", "v_mol", "ratio"),
    "internal-energy": ("label", "name", "m", "m_label"),
    "ice":             ("label", "name", "solid", "liquid", "mp"),
}

# The branch names each model can return, and therefore exactly the set of
# `notes` a payload must author. Every reachable state has something true to
# say (5A.1), and a branch that renders nothing ships an empty note panel.
#
# ⚠️ `density` HAS THREE, AND DESIGN'S PAGE HAS TWO. Her verdict is
# `const floats = T.d < 1.00;`, so WATER — one of her six tabs — falls to the
# else branch and the bench tells a student that water dropped in water
# **sinks**, at *"over 1.00 g/cm³"*, when it is exactly 1.00 and does
# neither. That is 5A.1's equal-state rule and the alveoli defect exactly: a
# comparative that is true on the majority of the state space. The EQUAL
# state gets its own branch, and it is the most useful state on the bench —
# 1.00 is the line the other five materials are read against. Registered in
# `DEPARTURES-P11.md`.
MODEL_BRANCHES = {
    "density":         ("floats", "sinks", "same"),
    "brownian":        ("always",),
    "internal-energy": ("biggest", "rest"),
    "ice":             ("odd", "ordinary"),
}

# The short strings each model selects between and drops into a template.
# Authored beside the physics rather than typed into `shared/ks3.js`, for
# P9's reason: a sentence a student reads that lives in the engine is a
# sentence no content gate can see and no examiner can find.
MODEL_WORDS = {
    # ⚖️ P11-02 adds the four `convert_*` strings. They are the attempt's
    # Convert line and note, branched on whether the balance has gone over a
    # kilogram, and they live here for the same reason the verdicts do: a
    # sentence a student reads must sit where a content gate can see it.
    # They carry `{mass}` / `{mass_kg}` / `{v}` of their own, and the model
    # fills them before they reach the panel.
    "density":         ("float_verdict", "sink_verdict", "same_verdict",
                        "float_sub", "sink_sub", "same_sub",
                        "convert_g_line", "convert_g_note",
                        "convert_kg_line", "convert_kg_note"),
    "brownian":        (),
    "internal-energy": ("biggest_holds", "rest_holds"),
    "ice":             ("float_verdict", "sink_verdict",
                        "float_sub", "sink_sub",
                        "expands", "contracts"),
}


def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, gate):
    """Design's commit gate. The bench is LOCKED until it is answered.

    Her `bOpen` is `s.gate !== null` on all four pages, and her `DONE` for
    `#s-bench` is `s.gate !== null && s.touched` — so the gate is not
    decoration, it is half of what ticks the second rail stop. A bench read
    before a commitment confirms whatever the student already believed.
    """
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "matter-bench %r has no commit gate. Design locks all ten P11/P12 "
            "benches behind one, and her own `DONE` reads the gate."
            % act_id)
    opts = "".join(
        '<li><button type="button" class="ks3-option" data-mtbench-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button></li>'
        % (i, chr(65 + i), t(o))
        for i, o in enumerate(gate["options"]))
    return ('<div class="ks3-mtbench-gate" data-mtbench-gate>'
            '<p class="ks3-commit">%s</p><ul class="ks3-options">%s</ul></div>'
            % (t(gate["prompt"]), opts))


def _slider(act_id, spec):
    """Design's single slider. `values` is the LIST she indexes into.

    Her `bSliderMin`/`bSliderMax` are `0` and `values.length - 1` on every
    page, and the readable value comes from the list rather than from the
    input — which is why `p11-04` can slide between two WORDS.
    """
    values = spec.get("values") or []
    if len(values) < 2:
        raise ValueError(
            "matter-bench %r declares a slider with %d value(s). A control "
            "with one position is a caption." % (act_id, len(values)))
    start = spec.get("start")
    if not isinstance(start, int) or not (0 <= start < len(values)):
        raise ValueError(
            "matter-bench %r slider starts at %r, outside its %d values."
            % (act_id, start, len(values)))
    if not spec.get("label") or not spec.get("value_label"):
        raise ValueError(
            "matter-bench %r slider has no `label` or no `value_label`."
            % act_id)
    # ⚠️ THE READING OPENS AS AN EM DASH AND THE WIRING PAINTS IT ON LOAD.
    # Authoring the resting figure here would be a SECOND source for a fact
    # the model already carries (5A.1), and the two would drift the moment a
    # slider value moved — silently, because the wiring overwrites it a
    # millisecond later and only a JavaScript-off reader would ever see the
    # stale one.
    return ('<div class="ks3-mtbench-row">'
            '<div class="ks3-mtbench-rowhead">'
            '<label for="%s-sv">%s</label>'
            '<p class="ks3-mtbench-reading" data-mtbench-out="sv">—</p></div>'
            '<input class="ks3-mtbench-slider" type="range" id="%s-sv" '
            'min="0" max="%d" step="1" value="%d" data-mtbench-slider>'
            '</div>'
            % (e(act_id), t(spec["label"]),
               e(act_id), len(values) - 1, start))


def _unique(rows, act_id, what):
    seen, dupes = set(), []
    for r in rows:
        if r.get("id") in seen:
            dupes.append(r.get("id"))
        seen.add(r.get("id"))
    if dupes:
        raise ValueError(
            "matter-bench %r has two %ss with id %s. The second is "
            "unreachable and the failure is silent."
            % (act_id, what, sorted(set(dupes))))


def _bars(act_id, bars):
    """Design's proportional bar panel — label, value, fill, sub.

    ⚖️ THE FILL IS THE RATIO THE LABEL CLAIMS. Every bar's width comes from
    the same arithmetic that produces its printed value, so the drawing
    cannot disagree with the number beside it.

    ⚠️ EXACTLY ONE FOCUS BAR. Either one bar authors `focus` — `p11-02`'s
    jiggle bar, which is the one visible quantity and not a selection — or
    none does and the MODEL picks it from the control. Two would be two
    claims about which one you are looking at; none, on a bench whose alt
    text says one is highlighted, would be a false aria-label.
    """
    if len(bars) < 2:
        raise ValueError(
            "matter-bench %r draws %d bar(s). The panel is a comparison."
            % (act_id, len(bars)))
    _unique(bars, act_id, "bar")
    focus = [b for b in bars if b.get("focus")]
    if len(focus) > 1:
        raise ValueError(
            "matter-bench %r marks %d bars as `focus`. One bar is in focus, "
            "and the panel's aria-label says which."
            % (act_id, len(focus)))
    for b in bars:
        for f in ("id", "label", "value"):
            if not b.get(f):
                raise ValueError(
                    "matter-bench %r bar %r has no %r. An unfilled template "
                    "renders as its own braces and reads as a live bench."
                    % (act_id, b.get("id"), f))
        if b.get("focus") and b.get("muted"):
            raise ValueError(
                "matter-bench %r bar %r is both `focus` and `muted`."
                % (act_id, b["id"]))
    out = ""
    for b in bars:
        cls = "ks3-mtbench-bar"
        if b.get("muted"):
            cls += " is-muted"
        out += ('<div class="%s" data-mtbench-bar="%s" data-label="%s" '
                'data-value="%s" data-sub="%s"%s%s>'
                '<div class="ks3-mtbench-barhead">'
                '<span class="ks3-mtbench-barlabel" '
                'data-mtbench-barlabel="%s"></span>'
                '<span class="ks3-mtbench-barvalue" '
                'data-mtbench-barvalue="%s"></span></div>'
                '<span class="ks3-mtbench-bartrack">'
                '<span class="ks3-mtbench-barfill" '
                'data-mtbench-barfill="%s"></span></span>'
                '<p class="ks3-mtbench-barsub" data-mtbench-barsub="%s"></p>'
                '</div>'
                % (cls, e(b["id"]), e(b["label"]), e(b["value"]),
                   e(b.get("sub", "")),
                   # ⚠️ `data-fixed-focus` IS WHAT STOPS THE WIRING MOVING
                   # IT. p11-02's focus bar is a CATEGORY claim that is true
                   # whatever the controls say; the other three benches let
                   # the model move the focus with the control.
                   (' data-focus="1" data-fixed-focus="1"'
                    if b.get("focus") else ""),
                   ' data-muted="1"' if b.get("muted") else "",
                   e(b["id"]), e(b["id"]), e(b["id"]), e(b["id"])))
    return out


def _tiles(act_id, specs):
    if len(specs) < 2:
        raise ValueError(
            "matter-bench %r has %d readout(s). Design draws four on every "
            "page in the unit." % (act_id, len(specs)))
    _unique(specs, act_id, "readout")
    cells = ""
    for s in specs:
        for f in ("id", "label", "value"):
            if not s.get(f):
                raise ValueError(
                    "matter-bench %r readout %r has no %r."
                    % (act_id, s.get("id"), f))
        cells += ('<div class="ks3-mtbench-tile" data-value="%s" '
                  'data-sub="%s">'
                  '<p class="ks3-mtbench-tile-label">%s</p>'
                  '<p class="ks3-mtbench-tile-value" '
                  'data-mtbench-out="%s">—</p>'
                  '<p class="ks3-mtbench-tile-sub" data-mtbench-sub="%s">—'
                  '</p></div>'
                  % (e(s["value"]), e(s.get("sub", "")), t(s["label"]),
                     e(s["id"]), e(s["id"])))
    return '<div class="ks3-mtbench-tiles">%s</div>' % cells


def _notes(act_id, a, model):
    spec = a.get("notes") or {}
    need = MODEL_BRANCHES[model]
    missing = [k for k in need if not spec.get(k)]
    if missing:
        raise ValueError(
            "matter-bench %r has no note for branch(es) %s. Every reachable "
            "state has something true to say (5A.1), and a branch that "
            "renders nothing ships an empty note panel."
            % (act_id, ", ".join(missing)))
    extra = sorted(set(spec) - set(need))
    if extra:
        raise ValueError(
            "matter-bench %r authors note(s) %s, which the %r model can "
            "never select. Authored copy no student will read."
            % (act_id, ", ".join(extra), model))
    return "".join(
        '<span data-mtbench-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(spec[k])) for k in need)


def _words(act_id, a, model):
    spec = a.get("words") or {}
    need = MODEL_WORDS[model]
    missing = [k for k in need if not spec.get(k)]
    if missing:
        raise ValueError(
            "matter-bench %r has no `words` entry for %s. These are strings a "
            "student READS; a missing one renders as an empty readout tile, "
            "which every gate in the build reads as a live instrument."
            % (act_id, ", ".join(missing)))
    extra = sorted(set(spec) - set(need))
    if extra:
        raise ValueError(
            "matter-bench %r authors `words` %s, which nothing reads."
            % (act_id, ", ".join(extra)))
    return "".join(
        '<span data-mtbench-word="%s" data-text="%s" hidden></span>'
        % (e(k), e(spec[k])) for k in need)


# ═══ #s-bench on all four pages · Design's shared Bench shell ════════════

def r_matter_bench(a, act_id):
    """⊕ Design's `Bench` child component, ported.

    ⚖️ **HER SHELL, HER ORDER.** Commit gate → tab row → optional slider →
    the dark panel of proportional bars → the readout cards → the note. Every
    element below is one of hers and there is nothing here she did not draw.

    ⚖️ **NO SENTENCE IS COMPOSED IN JAVASCRIPT.** Every bar label, bar value,
    bar sub-line, readout value, readout sub-line, aria-label and note on all
    four pages is an authored template with `{token}` holes; the wiring
    computes NUMBERS and fills them. That is the P9 seam, and it is what puts
    the prose where a content gate and an examiner can both see it.

    ⚖️ **THE COMPARATIVE WORDS ARE DERIVED.** `floats` / `sinks`, and which
    state of a substance is the denser, come from the values at render time
    and never from a string authored beside a control (5A.1) — which makes
    them true in the equal state by construction as well as in the ordinary
    ones.

    HOOKS: `data-mtbench` (wrapper, `data-model`, `data-values`,
    `data-value-label`, `data-alt`) · `data-mtbench-gate` ·
    `data-mtbench-gopt` · `data-mtbench-body` · `data-mtbench-tab`
    (carrying the model's own per-tab fields) · `data-mtbench-slider` ·
    `data-mtbench-bar` / `-barlabel` / `-barvalue` / `-barfill` / `-barsub` ·
    `data-mtbench-out` · `data-mtbench-sub` · `data-mtbench-note` ·
    `data-mtbench-branch` · `data-mtbench-word`.
    """
    model = a.get("model")
    if model not in MODEL_FIELDS:
        raise ValueError(
            "matter-bench %r names model %r. The four Design drew are %s, and "
            "the name selects the arithmetic in `shared/ks3.js` — an unknown "
            "one would ship a bench whose every readout is a raw template."
            % (act_id, model, ", ".join(sorted(MODEL_FIELDS))))

    tabs = a.get("tabs") or []
    if len(tabs) < 2:
        raise ValueError(
            "matter-bench %r has %d tab(s). Design's tab rows are four, four, "
            "four and six." % (act_id, len(tabs)))
    _unique(tabs, act_id, "tab")
    fields = MODEL_FIELDS[model]
    for tab in tabs:
        if not tab.get("id"):
            raise ValueError("matter-bench %r has a tab with no id." % act_id)
        for f in fields:
            if tab.get(f) in (None, ""):
                raise ValueError(
                    "matter-bench %r tab %r has no %r, which the %r model "
                    "reads for every bar and every readout."
                    % (act_id, tab["id"], f, model))

    slider = a.get("slider")
    bars = a.get("bars") or []

    # ⚠️ A BRANCH SET IS ONLY COMPLETE IF THE PAYLOAD CANNOT REACH A FIFTH
    # STATE. 5A.1: where a defensive branch exists BECAUSE of a property of
    # the payload, gate the property. Both of these are cheap and both close
    # the exact hole the `density` model was found with — a comparative that
    # is true on the majority of the state space.
    if model == "ice":
        for tab in tabs:
            if float(tab["solid"]) == float(tab["liquid"]):
                raise ValueError(
                    "matter-bench %r (ice) gives %r the same density as a "
                    "solid and as its own liquid. The bench has two branches "
                    "— the solid floats on its melt or it sinks — and a tie "
                    "would fall to whichever one is written second and say "
                    "something false." % (act_id, tab["id"]))
    if model == "density":
        # The three branches are `floats`, `sinks` and `same`, and `same` is
        # the one Design's page could not reach. It is authored, so it has to
        # BE reachable — a branch nothing can select is authored copy no
        # student will read, which is the other half of the same rule.
        if not any(abs(float(tab["d"]) - 1.00) < 1e-9 for tab in tabs):
            raise ValueError(
                "matter-bench %r (density) has no tab at exactly 1.00 g/cm³, "
                "so the `same` branch — the one that says a material at the "
                "water line does neither — can never be selected. Water is "
                "the line the whole bench is read against and it belongs in "
                "the deck." % act_id)
    if model == "internal-energy":
        for v in (slider or {}).get("values") or []:
            if float(v) <= 0:
                raise ValueError(
                    "matter-bench %r (internal-energy) can slide to %r. The "
                    "energies are measured ABOVE 0 °C, so a zero position "
                    "would put every bar at nothing and the note would be "
                    "describing a reading the panel cannot show."
                    % (act_id, v))
        masses = [float(tab["m"]) for tab in tabs]
        if masses.count(max(masses)) != 1:
            raise ValueError(
                "matter-bench %r (internal-energy) has %d tabs tied at the "
                "largest mass. The `biggest` branch names ONE of them as the "
                "thing everything else is compared with, and a tie makes that "
                "sentence untrue for whichever it did not name."
                % (act_id, masses.count(max(masses))))
        if masses.count(min(masses)) != 1:
            raise ValueError(
                "matter-bench %r (internal-energy) has %d tabs tied at the "
                "smallest mass. The `biggest` branch names the SMALLEST one "
                "by label, and a tie makes that sentence name the wrong tab "
                "half the time." % (act_id, masses.count(min(masses))))
        if min(masses) <= 0:
            raise ValueError(
                "matter-bench %r (internal-energy) has a tab of mass %r. The "
                "ratio in the fourth readout divides by it."
                % (act_id, min(masses)))

    start = a.get("start_tab", 0)
    if not isinstance(start, int) or not (0 <= start < len(tabs)):
        raise ValueError(
            "matter-bench %r opens on tab %r, outside its %d tabs."
            % (act_id, start, len(tabs)))

    if not a.get("tabs_label"):
        raise ValueError(
            "matter-bench %r has no `tabs_label`. Design's mono label above "
            "the row is what says WHAT the row chooses between." % act_id)
    if not a.get("bars_caption") or not a.get("bars_alt"):
        raise ValueError(
            "matter-bench %r has no `bars_caption` or no `bars_alt`. The "
            "panel is `role=\"img\"` and an empty label is a panel a screen "
            "reader cannot read at all." % act_id)

    # ⚠️ THE FOCUS BAR AND THE CONTROL HAVE TO AGREE, and only the payload
    # knows. Where no bar authors `focus` the model picks it — by tab id for
    # `density` and `internal-energy`, by slider value for `ice` — so the ids
    # have to line up or the highlight lands on nothing.
    if not any(b.get("focus") for b in bars):
        if model in ("density", "internal-energy"):
            ids = {b["id"] for b in bars}
            for tab in tabs:
                if tab["id"] not in ids:
                    raise ValueError(
                        "matter-bench %r (%s) has a tab %r with no bar of the "
                        "same id. The model highlights the selected tab's "
                        "bar, and a mismatch highlights nothing while the "
                        "aria-label says otherwise."
                        % (act_id, model, tab["id"]))
        elif model == "ice":
            ids = {b["id"] for b in bars}
            for v in (slider or {}).get("values") or []:
                if v not in ids:
                    raise ValueError(
                        "matter-bench %r (ice) slides to %r with no bar of "
                        "that id." % (act_id, v))

    tabrow = "".join(
        _seg("ks3-seg-btn ks3-mtbench-tab", tab["label"],
             pressed=(i == start),
             data_mtbench_tab=tab["id"],
             **{("data_%s" % f): tab[f] for f in fields})
        for i, tab in enumerate(tabs))

    lead = ('<p class="ks3-mtbench-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    slider_html = _slider(act_id, slider) if slider else ""
    slider_attrs = ""
    if slider:
        slider_attrs = (' data-values="%s" data-value-label="%s"'
                        % (e("|".join(str(v) for v in slider["values"])),
                           e(slider["value_label"])))

    return ('<div class="ks3-mtbench" data-mtbench data-model="%s" '
            'data-start-tab="%d"%s>%s%s'
            '<div class="ks3-mtbench-body" data-mtbench-body hidden>'
            '<div class="ks3-mtbench-controls">'
            '<div class="ks3-mtbench-picker">'
            '<p class="ks3-mtbench-pickerlabel">%s</p>'
            '<div class="ks3-mtbench-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-mtbench-panel">'
            '<p class="ks3-mtbench-barscaption">%s</p>'
            '<div class="ks3-mtbench-bars" role="img" aria-label="%s" '
            'data-mtbench-alt data-alt="%s">%s</div></div>%s'
            '<p class="ks3-mtbench-note" data-mtbench-note></p>%s%s'
            '</div></div>'
            % (e(model), start, slider_attrs, lead,
               _gate(act_id, a.get("gate") or {}),
               t(a["tabs_label"]), tabrow, slider_html,
               t(a["bars_caption"]),
               # ⚠️ THE RESTING LABEL IS THE CAPTION, NOT AN EMPTY STRING.
               # `role="img"` with no accessible name is a panel a screen
               # reader announces as "image" and nothing else; the caption is
               # true before any control is touched, and the wiring replaces
               # it with the live composition on load.
               e(a["bars_caption"]), e(a["bars_alt"]),
               _bars(act_id, bars),
               _tiles(act_id, a.get("readouts") or []),
               _notes(act_id, a, model), _words(act_id, a, model)))


# ═══ p11-02/03/04 · #s-think · the shell of a rail-bearing confrontation ══

def r_matter_think(a, act_id):
    """⊕ `#s-think` on the three MODEL/CONTRAST pages. THE SHELL IS THE
    WHOLE COMPONENT.

    This renderer draws nothing, on purpose, and the reason is in the module
    docstring at length. Briefly: Design's `DONE` puts `#s-think` on the rail
    on all three pages, a rail anchor has to declare `data-stage-done="0"` in
    the SHIPPED BYTES and carry a signal `doneByDom()` reads, and the shared
    `confrontation` shell in `ks3_art/core.py` emits the marker without the
    declaration — in a file ten units share.

    The block's content is already on the page when this is called:
    `r_activity` renders a `misconception` block's two quotes and two bodies
    from its BLOCK TYPE (`r_confrontation`), sets `head_emitted_content`, and
    only then reaches the kind's renderer. So the empty-activity gate is
    satisfied by real content rather than bypassed, and anything returned
    here would be markup Design did not draw, landing under her second quote.

    ⚠️ THE PAYLOAD IS STILL VALIDATED. A `matter-think` block with no
    `statements` would render the REGISTER's paraphrase of the belief rather
    than the page's own wording — the `b1-01` defect exactly, and the one
    `r_confrontation`'s docstring says is dangerous because it renders
    something and therefore looks finished.
    """
    if len(a.get("statements") or []) < 2:
        raise ValueError(
            "matter-think %r declares %d statement(s). Design draws TWO wrong "
            "ideas in this block, the second behind her amber divider, and a "
            "block with none falls back to the register's paraphrase — which "
            "renders, and therefore looks finished."
            % (act_id, len(a.get("statements") or [])))
    # ⚠️ THE STOP HAS NO CONTROL OF ITS OWN AND NO SIBLING BENCH MARKS IT.
    # Design's predicate is `s.answers.r1 !== null || s.hookChoice !== null`
    # — the HOOK or ladder rung 1, both outside this section — so the wiring
    # has to be told, in the payload, that this is a rail stop rather than
    # inferring it. `band_target` is P9's word for the same idea and would be
    # read by nothing here, so a near-miss is refused outright.
    for wrong in ("band_anchor", "band_at", "band_target", "mirrors"):
        if wrong in a:
            raise ValueError(
                "matter-think %r carries %r. This stop is not ticked by a "
                "sibling bench: `wireMatterThink` watches the hook and ladder "
                "rung 1, which is Design's own predicate. A near-miss key is "
                "silently ignored and ships a stop that can never tick."
                % (act_id, wrong))
    if not a.get("ticks_when"):
        raise ValueError(
            "matter-think %r does not declare `ticks_when`. The section is a "
            "RAIL STOP with no control inside it, and the one sentence saying "
            "what ticks it is the only thing standing between a reader and "
            "the conclusion that the stop is dead." % act_id)
    return ""


# ═══ p11-01 · the CFIFA attempt ══════════════════════════════════════════

def r_p11_attempt(a, act_id):
    """⊕ P11's half of Design's `Cfifa`: the student's own five lines.

    Her `Cfifa.dc.html` in this folder is byte-identical to P7's, so the
    drawing is `ks3_art.kit.r_cfifa_attempt` and nothing is re-typed. The
    FAMILY is P11's own, so `ks3_art.load()`'s one-family-one-module rule
    holds and the placement gates see it as this unit's.

    ⊕ ONE EYEBROW, NOT TWO. The `check` shell already prints this activity's
    eyebrow in Design's `.ks3-blockhead`; the kit helper prints it again
    unless told not to. P4–P6 ship it twice (measured); P7 opted out by
    passing `None`, and so does this.
    """
    return r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p11cfa")


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P11's own — `ks3_art/core.py` and
# `ks3_art/kit.py` are untouched. Shell stems checked against the whole
# registry first (MRB-279): `ks3-mtbench-`, `ks3-mtthink` and `ks3-p11cfa-`
# are all free.

ART = {}

KIND_SHELL = {
    'matter-bench':  ("ks3-mtbench-block",
                      ' data-instrument data-mtbenchblock '
                      'data-stage-done="0"'),
    # ⚠️ SHELL ONLY. See `r_matter_think`. The declaration is the component.
    'matter-think':  ("ks3-mtthink",
                      ' data-instrument data-mtthink '
                      'data-stage-done="0"'),
    'p11-attempt':   ("ks3-p11cfa-block",
                      ' data-instrument data-p11cfablock '
                      'data-stage-done="0"'),
}

KIND_FN = {
    'matter-bench':  r_matter_bench,
    'matter-think':  r_matter_think,
    'p11-attempt':   r_p11_attempt,
}
