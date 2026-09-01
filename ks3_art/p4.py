"""ks3_art.p4 — P4 *Forces*, the unit where a force gets both its ends named.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p4/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported.

── ⚖️ MRB-204 · ONE TRIANGLE IN NINE LESSONS, AND IT IS `p4-07` ───────────

    p4-01  no formula figure — a classification
    p4-02  resultant = bigger − smaller       a DIFFERENCE   three-bar BEAM
    p4-03  upward force = weight              an EQUALITY    two-panel BEAM
    p4-04  no formula figure — qualitative in statute
    p4-05  no formula figure — qualitative in statute
    p4-06  no formula figure — the bench already draws the balance
    p4-07  moment = force × distance          a PRODUCT      TRIANGLE
    p4-08  extension ∝ load                   a RATIO        BEAM + GRAPH
    p4-09  no formula figure — a classification

`p4-07` is the FIRST product in the unit and the only triangle in it. Four of
the first six relationships are additive, which is the trap: the reflex is to
reach for a triangle because physics has triangles. `r_p4_formula_art` refuses
to draw a triangle, so a later edit cannot slip one in here at all — the
triangle path is `r_cover_triangle` in the engine and nothing in this module
can reach it.

⚠️ EVERY BAR IN `p4-02`'s BEAM IS MEASURED OFF DESIGN'S SVG. She draws 700 px
for 40 N, 437 px for 25 N and 263 px for 15 N — and 437 + 263 = 700 exactly,
to the pixel, because the arithmetic IS the teaching. The drawer derives the
widths from the authored newtons at one scale rather than laying them out by
flex, so a bar model that does not add up cannot be authored.

── ⚖️ THE BAND STOP TICKS EARLIER THAN THE BENCH, ON PURPOSE ──────────────

Design's own `DONE(id, s)` on five of the nine pages gives the band section a
LOWER threshold than the practical above it:

    p4-01   s-bench  opened >= 3        s-pairs   opened >= 1
    p4-04   s-bench  gate && touched    s-three   gate
    p4-05   s-bench  gate && touched    s-rules   gate
    p4-06   s-bench  gate && touched    s-stages  gate
    p4-09   s-bench  all 8 labelled     s-three   1 labelled

MRB-249's `mirrors` would tie the two together and make the band stop tick
LATE. It is not used here for that reason. Each bench instead ticks its band
sibling itself, at Design's own earlier threshold, through
`data-<hook>-sibling` — the section id is on the wrapper and the wiring marks
it. Measured off her drawing, not inferred from the pattern.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. Nothing in this module uses `cards`, `sim` or `scorecards`; the band
renderer's numbered list is `panels`, deliberately not `cards`, because a
payload using `cards` gets two renderers and renders blank. `fifa` appears
only on `worked-example` activities, which is the engine's own branch.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279. Checked against every other module
before these were written.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

import re as _re

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ═══ shared P4 primitives ════════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    """A segmented-control button, the shape every P4 control picks from."""
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P4 bench opens behind.

    ⚖️ A BENCH READ BEFORE A COMMITMENT CONFIRMS WHATEVER THE STUDENT ALREADY
    BELIEVED. Design puts one on eight of the nine P4 benches; `p4-09`'s
    sorter is the ninth and commits per case instead, which is why it does not
    come through here.
    """
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


def _tiles(hook, specs):
    """The readout row every P4 bench closes on. `value` is the resting text."""
    cells = "".join(
        '<div class="ks3-%s-tile"><p class="ks3-%s-tile-label">%s</p>'
        '<p class="ks3-%s-tile-value" data-%s-out="%s">%s</p></div>'
        % (hook, hook, t(s["label"]), hook, hook, e(s["id"]),
           t(s.get("value", "—")))
        for s in specs)
    return '<div class="ks3-%s-tiles">%s</div>' % (hook, cells)


def _head(hook, a):
    """⊕ MRB-223, 25 Aug 2026 — RETURNS NOTHING, DELIBERATELY. A live defect.

    This used to draw a second head row — eyebrow, `<h2>` and a progress
    paragraph — inside every bench in this unit. `r_activity` had ALREADY
    drawn Design's row (`.ks3-blockhead`, from the same `eyebrow` /
    `heading` / `progress` keys), so every shipped bench in P4, P5 and P6
    printed its eyebrow and its heading twice. Measured in the built bytes:
    one duplicated `<h2>` on all 22 lesson pages; 16 placements in P6 alone.
    P7 onwards never drew the second row (see `ks3_art/p7.py`); this brings
    the three earlier units to the same shape without touching any of the
    templates that call it. The wiring now writes the readout into the
    shell's own `[data-count]`, which is the element the student was always
    reading first.
    """
    return ""


def _sibling(a):
    """`data-*-sibling` — the band stop this bench ticks, at its own count.

    See the module note. Design's band stop ticks EARLIER than the bench, so
    it cannot be an MRB-249 mirror; the bench marks it directly.
    """
    sib = a.get("band_anchor")
    at = a.get("band_at")
    if not sib:
        return ""
    if not isinstance(at, int) or at < 1:
        raise ValueError(
            "%r names a band sibling %r with no `band_at` count. Design's "
            "band stop ticks earlier than the bench; without the threshold "
            "the two would tick together and the earlier stop is lost."
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
            "%s %r has two %ss with id %s. The second is unreachable and the "
            "failure is silent." % (family, act_id, what, sorted(set(dupes))))


# ═══ p4-01 · #s-bench · the interaction board ════════════════════════════

def r_interaction_board(a, act_id):
    """⊕ p4-01 `#s-bench` — five cases, and the object on the other end.

    ⚖️ **THE VERDICT IS SEALED UNTIL THE STUDENT NAMES THE PARTNER.** Design
    opens each case with the question and NO diagram: the three options are
    the whole of the unopened state. Drawing the pair first would hand over
    the answer to the only question the case asks, so the renderer refuses a
    case whose `notes` do not answer every option — a missing note is a case
    that opens on to nothing.

    ⚖️ **NO BAR FOR FORCE SIZE, AND THAT IS DESIGN'S RULING NOT AN OMISSION.**
    The five cases span about 2 N to about 200 billion billion N. A linear bar
    cannot carry twenty orders of magnitude, so the sizes are printed as
    values with units and both arrows are drawn at ONE FIXED LENGTH. The
    equality the drawing asserts is that the two forces are the SAME, which is
    true in every case; it asserts nothing about how big.

    ⚠️ **THE HEDGE IS LOAD-BEARING.** Every size reads "about", because these
    are typical values that depend on how hard, how fast and how far apart.
    Removing the hedge makes twelve false statements. The renderer does not
    police the wording; the lesson's legal line declares it.

    HOOKS: `data-iboard` (wrapper, `data-target`, `data-sibling`) ·
    `data-iboard-tab` · `data-iboard-prompt` · `data-iboard-ask` ·
    `data-iboard-opt` (valued with the option index) · `data-iboard-panel` ·
    `data-iboard-arrow` (valued `push` / `pull`) · `data-iboard-join`
    (valued `contact` / `gap`) · `data-iboard-fill` (valued with the slot) ·
    `data-iboard-out` · `data-iboard-note` · `data-iboard-progress`.
    """
    cases = a.get("cases") or []
    if len(cases) < 3:
        raise ValueError(
            "interaction-board %r declares %d case(s). The board's whole "
            "demand is that the same question has a different second object "
            "every time." % (act_id, len(cases)))
    _unique(cases, act_id, "interaction-board", "case")

    for c in cases:
        opts = c.get("options") or []
        notes = c.get("notes") or []
        if len(opts) < 3:
            raise ValueError(
                "interaction-board %r case %r offers %d option(s); the case "
                "needs at least three or the naming is not a choice."
                % (act_id, c.get("id"), len(opts)))
        if len(notes) != len(opts):
            raise ValueError(
                "interaction-board %r case %r has %d option(s) and %d note(s)."
                " Every option opens the board, so every option needs the "
                "sentence it opens on to — a missing one opens on to nothing."
                % (act_id, c.get("id"), len(opts), len(notes)))
        if c.get("kind") not in ("push", "pull"):
            raise ValueError(
                "interaction-board %r case %r is kind %r. A force on this "
                "board is a push or a pull and the arrows are drawn from it."
                % (act_id, c.get("id"), c.get("kind")))
        for field in ("a", "b", "size", "cap_a", "cap_b", "prompt"):
            if not c.get(field):
                raise ValueError(
                    "interaction-board %r case %r has no %r. Both ends of "
                    "the pair are named on the drawing."
                    % (act_id, c.get("id"), field))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-iboard-tab", c["tab"], pressed=(i == 0),
             data_iboard_tab=i)
        for i, c in enumerate(cases))

    # ⚠️ EMIT-BOTH-SHOW-ONE. Every case's prompt, options and notes are in the
    # document; the wiring swaps which is shown. Nothing science-bearing is
    # rebuilt in JS, so `×`, `÷` and the em dashes survive a case change.
    panels = ""
    for i, c in enumerate(cases):
        opts = "".join(
            '<button type="button" class="ks3-iboard-opt" '
            'data-iboard-opt="%d" aria-pressed="false">%s</button>'
            % (j, t(o)) for j, o in enumerate(c["options"]))
        notes = "".join(
            '<p class="ks3-iboard-note" data-iboard-note="%d" hidden>%s</p>'
            % (j, rich(n)) for j, n in enumerate(c["notes"]))
        panels += (
            '<div class="ks3-iboard-case" data-iboard-case="%d"%s>'
            '<p class="ks3-iboard-prompt">%s</p>'
            '<div class="ks3-iboard-ask" data-iboard-ask>%s</div>'
            '<div class="ks3-iboard-notes">%s</div></div>'
            % (i, "" if i == 0 else " hidden", t(c["prompt"]), opts, notes))

    # Design's own 1120×300 viewBox and geometry (page lines 143–166). The two
    # bodies, the two arrows and the joiner are literal; every VALUE label is
    # an absolutely-positioned HTML span at the matching viewBox percentage,
    # because a `<span>` created in the SVG namespace is not a renderable
    # element and the failure is SILENT.
    svg = (
        '<svg class="ks3-iboard-svg" viewBox="0 0 1120 300" role="img" '
        'aria-label="" data-iboard-alt>'
        '<rect class="ks3-iboard-body" x="250" y="110" width="200" '
        'height="84" rx="14"/>'
        '<rect class="ks3-iboard-body" x="670" y="110" width="200" '
        'height="84" rx="14"/>'
        '<g data-iboard-arrow="push" hidden>'
        '<path class="ks3-iboard-shaft" d="M410 80 H286"/>'
        '<path class="ks3-iboard-head" d="M260 80 L290 63 L290 97 Z"/>'
        '<path class="ks3-iboard-shaft" d="M710 80 H834"/>'
        '<path class="ks3-iboard-head" d="M860 80 L830 63 L830 97 Z"/></g>'
        '<g data-iboard-arrow="pull" hidden>'
        '<path class="ks3-iboard-shaft" d="M290 80 H414"/>'
        '<path class="ks3-iboard-head" d="M440 80 L410 63 L410 97 Z"/>'
        '<path class="ks3-iboard-shaft" d="M830 80 H706"/>'
        '<path class="ks3-iboard-head" d="M680 80 L710 63 L710 97 Z"/></g>'
        '<rect class="ks3-iboard-touch" data-iboard-join="contact" hidden '
        'x="450" y="143" width="220" height="18"/>'
        '<path class="ks3-iboard-gapline" data-iboard-join="gap" hidden '
        'd="M450 152 H670"/>'
        '</svg>')

    fills = "".join(
        '<span class="ks3-iboard-fill ks3-iboard-%s" data-iboard-fill="%s">'
        '</span>' % (slot.replace("_", "-"), slot)
        for slot in ("name_a", "name_b", "size_a", "size_b", "join",
                     "cap_a", "cap_b"))

    tiles = _tiles("iboard", [
        {"id": "pair", "label": "The two objects"},
        {"id": "size", "label": "Each force"},
        {"id": "kind", "label": "Push or pull"},
    ])

    payload = "".join(
        '<span data-iboard-data="%d" data-a="%s" data-b="%s" data-size="%s" '
        'data-kind="%s" data-contact="%s" data-capa="%s" data-capb="%s" '
        'data-pair="%s" data-alt="%s" hidden></span>'
        % (i, e(c["a"]), e(c["b"]), e(c["size"]), e(c["kind"]),
           "1" if c.get("contact") else "0", e(c["cap_a"]), e(c["cap_b"]),
           e(c.get("pair") or "%s and %s" % (c["a"], c["b"].lower())),
           e(c.get("alt", "")))
        for i, c in enumerate(cases))

    target = int(a.get("target") or 3)
    return ('<div class="ks3-iboard" data-iboard data-total="%d" '
            'data-target="%d"%s>%s'
            '<div class="ks3-iboard-tabs"><p class="ks3-iboard-tabslabel">%s'
            '</p><div class="ks3-iboard-tabrow">%s</div></div>'
            '<div class="ks3-iboard-stage">%s'
            '<div class="ks3-iboard-panel" data-iboard-panel hidden>'
            '<div class="ks3-iboard-figwrap">%s%s</div>%s'
            '<p class="ks3-iboard-live" data-iboard-live aria-live="polite">'
            '</p></div></div>%s</div>'
            % (len(cases), target, _sibling(a), _head("iboard", a),
               t(a.get("tabs_label", "Pick a case")), tabs, panels,
               svg, fills, tiles, payload))


# ═══ p4-02 · #s-bench · the sledge on ice ════════════════════════════════

def r_resultant_bench(a, act_id):
    """⊕ p4-02 `#s-bench` — two pulls, one arrow, and one scale for all three.

    ⚖️ **ONE PX-PER-NEWTON SCALE, AND THE PAGE SAYS SO.** Design's `SCALE` is
    `380 / 60` — every arrow on this bench, including the resultant, is drawn
    at the same 6.33 px per newton. That is the claim the lesson's own
    misconception block is about: two arrows the same length are a claim that
    two forces are equal, and a bench that drew them to convenience would be
    teaching the thing the block exists to kill. The scale is emitted as
    `data-scale` and there is exactly one of it.

    ⚖️ **ZERO PRINTS `0 N`; IT DOES NOT DRAW A STUB.** A zero-length arrow is
    not a small arrow, and the equal state — both ropes at the same pull — is
    the one a student is most likely to leave the bench in. Design draws no
    arrow and prints the words instead.

    ⚠️ **FIVE BRANCHES, KEYED TO WHICH SLIDER IS NON-ZERO** — both zero, right
    only, left only, equal, unequal. The unequal branch names the two sizes it
    is holding, so no state is described in words the numbers contradict.

    HOOKS: `data-rbench` (wrapper, `data-scale`) · `data-rbench-gate` ·
    `data-rbench-gopt` · `data-rbench-body` · `data-rbench-slider` (valued
    `right` / `left`) · `data-rbench-shaft` · `data-rbench-head` ·
    `data-rbench-out` · `data-rbench-note` · `data-rbench-branch`.
    """
    sliders = a.get("sliders") or []
    if len(sliders) != 2:
        raise ValueError(
            "resultant-bench %r declares %d slider(s); the lesson is two "
            "pulls along one line." % (act_id, len(sliders)))
    _unique(sliders, act_id, "resultant-bench", "slider")

    branches = a.get("branches") or {}
    need = ("both_zero", "right_only", "left_only", "equal", "unequal")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "resultant-bench %r has no note for state(s) %s. Every state a "
            "student can leave the bench in carries an authored sentence, "
            "and the equal state is the one they are most likely to reach."
            % (act_id, ", ".join(missing)))

    scale = float(a.get("scale") or 0)
    if scale <= 0:
        raise ValueError(
            "resultant-bench %r has no px-per-newton scale. Two arrows drawn "
            "to different scales are a diagram that lies, which is exactly "
            "the misconception this lesson confronts." % act_id)

    rows = ""
    for s in sliders:
        rows += (
            '<div class="ks3-rbench-row">'
            '<div class="ks3-rbench-rowhead">'
            '<label for="%s-%s">%s</label>'
            '<p class="ks3-rbench-reading" data-rbench-out="%s">%s N</p></div>'
            '<input class="ks3-rbench-slider" type="range" id="%s-%s" '
            'min="%s" max="%s" step="%s" value="%s" data-rbench-slider="%s">'
            '</div>'
            % (e(act_id), e(s["id"]), t(s["label"]), e(s["id"]),
               e(s.get("start", 0)), e(act_id), e(s["id"]),
               e(s.get("min", 0)), e(s.get("max", 60)),
               e(s.get("step", 5)), e(s.get("start", 0)), e(s["id"])))

    # Design's own 1120×380 viewBox (page lines 118–137).
    svg = (
        '<svg class="ks3-rbench-svg" viewBox="0 0 1120 380" role="img" '
        'aria-label="" data-rbench-alt>'
        '<path class="ks3-rbench-ice" d="M300 232 H820"/>'
        '<rect class="ks3-rbench-sledge" x="460" y="158" width="200" '
        'height="66" rx="12"/>'
        '<text class="ks3-rbench-caption" x="560" y="199" '
        'text-anchor="middle">%s</text>'
        '<path class="ks3-rbench-shaft" data-rbench-shaft="right" d="M0 0" '
        'hidden/><path class="ks3-rbench-head" data-rbench-head="right" '
        'd="M0 0" hidden/>'
        '<path class="ks3-rbench-shaft" data-rbench-shaft="left" d="M0 0" '
        'hidden/><path class="ks3-rbench-head" data-rbench-head="left" '
        'd="M0 0" hidden/>'
        '<path class="ks3-rbench-base" d="M120 292 H1000"/>'
        '<text class="ks3-rbench-baselabel" x="120" y="278">%s</text>'
        '<path class="ks3-rbench-shaft ks3-rbench-res" '
        'data-rbench-shaft="res" d="M0 0" hidden/>'
        '<path class="ks3-rbench-head ks3-rbench-res" '
        'data-rbench-head="res" d="M0 0" hidden/>'
        '<text class="ks3-rbench-nores" x="560" y="330" text-anchor="middle" '
        'data-rbench-nores hidden>%s</text></svg>'
        % (t(a.get("body_label", "Sledge")),
           t(a.get("base_label", "ONE ARROW INSTEAD OF TWO")),
           t(a.get("zero_label", "no arrow to draw · 0 N"))))

    fills = "".join(
        '<span class="ks3-rbench-fill" data-rbench-fill="%s"></span>' % k
        for k in ("right", "left", "res"))

    tiles = _tiles("rbench", a.get("readouts") or [])

    branch_data = "".join(
        '<span data-rbench-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    return ('<div class="ks3-rbench" data-rbench data-scale="%s"%s>%s%s'
            '<div class="ks3-rbench-body" data-rbench-body hidden>'
            '<div class="ks3-rbench-controls">%s</div>'
            '<div class="ks3-rbench-figwrap">%s%s</div>%s'
            '<p class="ks3-rbench-note" data-rbench-note></p>%s</div></div>'
            % (e("%.6f" % scale), _sibling(a), _head("rbench", a),
               _gate(act_id, "resultant-bench", a.get("gate") or {}, "rbench"),
               rows, svg, fills, tiles, branch_data))


# ═══ p4-03 · #s-bench · the support rig ══════════════════════════════════

def r_support_rig(a, act_id):
    """⊕ p4-03 `#s-bench` — change what is holding it up.

    ⚖️ **THE PAPER'S BREAKING POINT IS MADE UP, AND THE PAGE DECLARES IT.**
    Design gives the sheet a 2 N cap so that *unbalanced* is a state a student
    can reach on a support that is not simply absent — the alternative is a
    bench where the only way to see a leftover force is to remove the support
    entirely, which teaches that unbalanced means unsupported. The legal line
    on the lesson says the number is invented. The renderer requires a `cap`
    on every support for the same reason it requires a note: an uncapped
    support and an infinitely strong one are different claims.

    ⚖️ **`upward = min(weight, cap)`, AND THE LEFTOVER IS THE REMAINDER.** A
    support that cannot match the weight supplies what it can and the rest is
    left over downwards. That is the whole arithmetic of the block, and it is
    computed in one place.

    ⚠️ **THE SPRING'S COIL LENGTH TRACKS THE FORCE.** Design redraws the zig
    at `20 + U * 1.6` px, so the drawing agrees with rung 3 — the spring stops
    stretching where its pull reaches the weight. A fixed coil would make the
    figure contradict the answer the lesson marks.

    HOOKS: `data-hrig` (wrapper, `data-g`, `data-scale`, `data-paper-max`) ·
    `data-hrig-gate` · `data-hrig-gopt` · `data-hrig-body` ·
    `data-hrig-support` (valued with the support id, carrying `data-cap`) ·
    `data-hrig-mass` · `data-hrig-shaft` · `data-hrig-head` ·
    `data-hrig-coil` · `data-hrig-out` · `data-hrig-note`.
    """
    supports = a.get("supports") or []
    if len(supports) < 3:
        raise ValueError(
            "support-rig %r declares %d support(s). The rig contrasts what "
            "different things underneath can and cannot supply."
            % (act_id, len(supports)))
    _unique(supports, act_id, "support-rig", "support")
    for s in supports:
        if "cap" not in s:
            raise ValueError(
                "support-rig %r support %r declares no `cap`. An uncapped "
                "support and an infinitely strong one are different claims, "
                "and the leftover arrow is derived from this number."
                % (act_id, s.get("id")))
        if not s.get("note"):
            raise ValueError(
                "support-rig %r support %r has no note. Every support is a "
                "reachable state." % (act_id, s.get("id")))
        if not s.get("word"):
            raise ValueError(
                "support-rig %r support %r has no `word` for the drawing's "
                "own caption." % (act_id, s.get("id")))

    mass = a.get("mass") or {}
    for k in ("min", "max", "step", "start"):
        if k not in mass:
            raise ValueError(
                "support-rig %r mass control has no %r." % (act_id, k))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-hrig-support", s["tab"],
             pressed=(s["id"] == a.get("start_support", supports[0]["id"])),
             data_hrig_support=s["id"],
             data_cap=("inf" if s["cap"] is None else s["cap"]),
             data_word=s["word"], data_note=s["note"],
             data_torn=("1" if s.get("tears") else "0"),
             data_note_ok=s.get("note_ok", s["note"]),
             data_shape=s.get("shape", "solid"))
        for s in supports)

    # Design's own 1000×460 viewBox (page lines 154–186).
    svg = (
        '<svg class="ks3-hrig-svg" viewBox="0 0 1000 460" role="img" '
        'aria-label="" data-hrig-alt>'
        '<path class="ks3-hrig-coil" data-hrig-coil d="M0 0" hidden/>'
        '<g data-hrig-shape="solid" hidden>'
        '<rect class="ks3-hrig-slab" x="330" y="238" width="340" '
        'height="26" rx="6"/>'
        '<path class="ks3-hrig-hatch" d="M340 264 l-18 26 M380 264 l-18 26 '
        'M420 264 l-18 26 M460 264 l-18 26 M500 264 l-18 26 M540 264 l-18 26 '
        'M580 264 l-18 26 M620 264 l-18 26 M660 264 l-18 26"/></g>'
        '<path class="ks3-hrig-sheet" data-hrig-shape="sheet" hidden '
        'd="M330 250 Q500 268 670 250"/>'
        '<path class="ks3-hrig-sheet ks3-hrig-torn" data-hrig-shape="torn" '
        'hidden d="M330 250 Q410 262 470 286 M530 286 Q590 262 670 250"/>'
        '<rect class="ks3-hrig-load" x="430" y="150" width="140" '
        'height="88" rx="12"/>'
        '<path class="ks3-hrig-shaft" data-hrig-shaft="weight" d="M0 0"/>'
        '<path class="ks3-hrig-head" data-hrig-head="weight" d="M0 0"/>'
        '<path class="ks3-hrig-shaft" data-hrig-shaft="up" d="M0 0" hidden/>'
        '<path class="ks3-hrig-head" data-hrig-head="up" d="M0 0" hidden/>'
        '<path class="ks3-hrig-shaft ks3-hrig-over" data-hrig-shaft="over" '
        'd="M0 0" hidden/>'
        '<path class="ks3-hrig-head ks3-hrig-over" data-hrig-head="over" '
        'd="M0 0" hidden/></svg>')

    fills = "".join(
        '<span class="ks3-hrig-fill ks3-hrig-%s" data-hrig-fill="%s"></span>'
        % (k, k) for k in ("mass", "weight", "up", "over", "word"))

    return ('<div class="ks3-hrig" data-hrig data-g="%s" data-scale="%s" '
            'data-start="%s"%s>%s%s'
            '<div class="ks3-hrig-body" data-hrig-body hidden>'
            '<div class="ks3-hrig-controls">'
            '<div class="ks3-hrig-picker"><p class="ks3-hrig-pickerlabel">%s'
            '</p><div class="ks3-hrig-tabrow">%s</div></div>'
            '<div class="ks3-hrig-row"><div class="ks3-hrig-rowhead">'
            '<label for="%s-mass">%s</label>'
            '<p class="ks3-hrig-reading" data-hrig-out="mass">%s kg</p></div>'
            '<input class="ks3-hrig-slider" type="range" id="%s-mass" '
            'min="%s" max="%s" step="%s" value="%s" data-hrig-mass></div>'
            '</div>'
            '<div class="ks3-hrig-figwrap">%s%s</div>%s'
            '<p class="ks3-hrig-note" data-hrig-note></p></div></div>'
            % (e(a.get("g", 10)), e(a.get("scale", 3)),
               e(a.get("start_support", supports[0]["id"])), _sibling(a),
               _head("hrig", a),
               _gate(act_id, "support-rig", a.get("gate") or {}, "hrig"),
               t(a.get("support_label", "What is holding it up")), tabs,
               e(act_id), t(mass.get("label", "Mass")), e(mass["start"]),
               e(act_id), e(mass["min"]), e(mass["max"]), e(mass["step"]),
               e(mass["start"]),
               svg, fills, _tiles("hrig", a.get("readouts") or [])))


# ═══ p4-04 · #s-bench · the trolley and the light gates ══════════════════

def r_gate_run(a, act_id):
    """⊕ p4-04 `#s-bench` — same trolley, same start, four resultants.

    ⚖️ **EVERY RUN STARTS AT THE SAME SPEED, AND THAT IS THE CONTROL.** Design
    fixes gate 1 at 2.0 m/s for all eight combinations. The lesson's claim is
    that the RESULTANT decides what changes, so the only thing allowed to vary
    between runs is the resultant and how long it acts.

    ⚖️ **THE SIDEWAYS CASE REPORTS A SPEED AND A BENT PATH, AND STOPS THERE.**
    Resolving it into components is GCSE. Design's own numbers are internally
    exact for a 1 kg trolley under 1 N — 2.2 m/s at one second is
    `sqrt(2² + 1²)`, and 3.6 m/s at three is `sqrt(2² + 3²)` — so a student
    who checks later finds the page was telling the truth, without the page
    ever having done the vector arithmetic in front of them.

    ⚠️ **EIGHT AUTHORED NOTES, ONE PER COMBINATION.** Not four notes with the
    duration interpolated: the three-second note on the backwards case is
    about the trolley having already stopped and reversed, which is a
    different fact rather than a bigger number.

    ⚠️ **`s-three` TICKS ON THE GATE ALONE.** See the module note.

    HOOKS: `data-grun` (wrapper, `data-sibling`) · `data-grun-gate` ·
    `data-grun-gopt` · `data-grun-body` · `data-grun-case` ·
    `data-grun-secs` · `data-grun-track` · `data-grun-trolley` ·
    `data-grun-force` · `data-grun-out` · `data-grun-note`.
    """
    cases = a.get("cases") or []
    times = a.get("times") or []
    if len(cases) < 3 or len(times) < 2:
        raise ValueError(
            "gate-run %r declares %d case(s) and %d duration(s). The bench "
            "contrasts what a resultant does with how long it does it for."
            % (act_id, len(cases), len(times)))
    _unique(cases, act_id, "gate-run", "case")

    for c in cases:
        notes = c.get("notes") or {}
        after = c.get("after") or {}
        for tspec in times:
            key = str(tspec["secs"])
            if key not in {str(k) for k in notes}:
                raise ValueError(
                    "gate-run %r case %r has no note at %s s. Eight states "
                    "are reachable and every one of them carries a sentence."
                    % (act_id, c.get("id"), key))
            if key not in {str(k) for k in after}:
                raise ValueError(
                    "gate-run %r case %r has no gate-2 reading at %s s."
                    % (act_id, c.get("id"), key))
        if c.get("dir") not in ("none", "fwd", "back", "side"):
            raise ValueError(
                "gate-run %r case %r has direction %r; the drawing knows "
                "none, fwd, back and side." % (act_id, c.get("id"), c["dir"]))

    case_tabs = "".join(
        _seg("ks3-seg-btn ks3-grun-case", c["tab"],
             pressed=(c["id"] == a.get("start_case", cases[0]["id"])),
             data_grun_case=c["id"])
        for c in cases)
    time_tabs = "".join(
        _seg("ks3-seg-btn ks3-grun-secs", tspec["label"],
             pressed=(tspec["secs"] == a.get("start_secs", times[0]["secs"])),
             data_grun_secs=tspec["secs"])
        for tspec in times)

    data = ""
    for c in cases:
        for tspec in times:
            k = str(tspec["secs"])
            note = {str(x): y for x, y in (c.get("notes") or {}).items()}[k]
            after = {str(x): y for x, y in (c.get("after") or {}).items()}[k]
            data += ('<span data-grun-data="%s|%s" data-after="%s" '
                     'data-note="%s" hidden></span>'
                     % (e(c["id"]), e(k), e(after), e(note)))
    for c in cases:
        data += ('<span data-grun-case-data="%s" data-dir="%s" '
                 'data-label="%s" data-path="%s" data-changed="%s" '
                 'data-same="%s" hidden></span>'
                 % (e(c["id"]), e(c["dir"]), e(c["label"]), e(c["path"]),
                    e(c["changed"]), e(c["same"])))

    # Design's own 1080×330 viewBox (page lines 148–172).
    svg = (
        '<svg class="ks3-grun-svg" viewBox="0 0 1080 330" role="img" '
        'aria-label="" data-grun-alt>'
        '<path class="ks3-grun-rail" d="M180 264 H900"/>'
        '<path class="ks3-grun-gate" d="M180 190 V264"/>'
        '<path class="ks3-grun-gate" d="M900 190 V264"/>'
        '<text class="ks3-grun-gatelabel" x="180" y="300" '
        'text-anchor="middle">GATE 1</text>'
        '<text class="ks3-grun-gatelabel" x="900" y="300" '
        'text-anchor="middle">GATE 2</text>'
        '<path class="ks3-grun-track" data-grun-track d="M0 0"/>'
        '<rect class="ks3-grun-trolley" data-grun-trolley x="0" y="0" '
        'width="120" height="56" rx="10"/>'
        '<path class="ks3-grun-shaft" data-grun-force="shaft" d="M0 0" '
        'hidden/><path class="ks3-grun-head" data-grun-force="head" '
        'd="M0 0" hidden/></svg>')

    fills = "".join(
        '<span class="ks3-grun-fill ks3-grun-%s" data-grun-fill="%s"></span>'
        % (k, k) for k in ("force", "path"))

    lead = ('<p class="ks3-grun-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-grun" data-grun data-start-case="%s" '
            'data-start-secs="%s"%s>%s%s%s'
            '<div class="ks3-grun-body" data-grun-body hidden>'
            '<div class="ks3-grun-controls">'
            '<div class="ks3-grun-picker"><p class="ks3-grun-pickerlabel">%s'
            '</p><div class="ks3-grun-tabrow">%s</div></div>'
            '<div class="ks3-grun-picker"><p class="ks3-grun-pickerlabel">%s'
            '</p><div class="ks3-grun-tabrow">%s</div></div></div>'
            '<div class="ks3-grun-figwrap">%s%s</div>%s'
            '<p class="ks3-grun-note" data-grun-note></p>%s</div></div>'
            % (e(a.get("start_case", cases[0]["id"])),
               e(a.get("start_secs", times[0]["secs"])), _sibling(a),
               _head("grun", a), lead,
               _gate(act_id, "gate-run", a.get("gate") or {}, "grun"),
               t(a.get("case_label", "The resultant force")), case_tabs,
               t(a.get("time_label", "How long it acts")), time_tabs,
               svg, fills, _tiles("grun", a.get("readouts") or []), data))


# ═══ p4-05 · #s-bench · block and spring balance ═════════════════════════

def r_drag_lane(a, act_id):
    """⊕ p4-05 `#s-bench` — two readings from every drag test.

    ⚖️ **TWO LANES, ONE SCALE, AND THE GAP IS THE LESSON.** Design draws the
    break-away pull and the sliding pull one above the other at the same px
    per newton, because the whole hook is that starting is harder than
    keeping going. Two separate figures at two scales would show the same
    numbers and hide the point.

    ⚖️ **THE BREAK-AWAY IS MODELLED AS A FIXED FRACTION ABOVE THE SLIDE, AND
    THE LEGAL LINE SAYS SO.** Design uses one fifth. It is a teaching model,
    not a measurement — real surfaces vary with polish, dust, damp and wear —
    and the renderer keeps the factor as data so the page and the disclosure
    cannot drift apart.

    ⚠️ **THE SECOND SENTENCE IS ALWAYS PRESENT.** Every state carries a
    surface branch AND a comparison against another load on the same surface,
    so the student is never left with a reading whose only meaning is itself.

    ⚠️ **NO ARROW IS EVER ZERO HERE.** The smallest reading on the bench is
    `4 kg × 10 N/kg × 0.20 = 8 N`, so the drawing has no zero state to handle
    and does not pretend to.

    HOOKS: `data-dlane` (wrapper, `data-g`, `data-scale`, `data-start-factor`)
    · `data-dlane-gate` · `data-dlane-gopt` · `data-dlane-body` ·
    `data-dlane-surface` (carrying `data-grip`) · `data-dlane-mass` ·
    `data-dlane-texture` · `data-dlane-shaft` · `data-dlane-head` ·
    `data-dlane-out` · `data-dlane-note` · `data-dlane-compare`.
    """
    surfaces = a.get("surfaces") or []
    masses = a.get("masses") or []
    if len(surfaces) < 3 or len(masses) < 2:
        raise ValueError(
            "drag-lane %r declares %d surface(s) and %d load(s). Rule 2 of "
            "the block below it is that friction depends on BOTH surfaces, "
            "and rule 3 that it grows with the load; one control cannot show "
            "either." % (act_id, len(surfaces), len(masses)))
    _unique(surfaces, act_id, "drag-lane", "surface")
    for s in surfaces:
        if not s.get("note"):
            raise ValueError(
                "drag-lane %r surface %r has no note." % (act_id, s.get("id")))
        if not isinstance(s.get("grip"), (int, float)) or s["grip"] <= 0:
            raise ValueError(
                "drag-lane %r surface %r has no positive grip figure. A "
                "surface with no friction is the misconception this lesson "
                "confronts, not a state it draws."
                % (act_id, s.get("id")))
        if s.get("texture") not in ("gloss", "planks", "loops", "grit"):
            raise ValueError(
                "drag-lane %r surface %r asks for texture %r. The four drawn "
                "are gloss, planks, loops and grit — and the texture is how "
                "a reader tells the surfaces apart without reading the tab."
                % (act_id, s.get("id"), s.get("texture")))

    if not a.get("compare"):
        raise ValueError(
            "drag-lane %r has no `compare` sentence. Every state on this "
            "bench carries a surface branch AND a comparison against another "
            "load on the same surface, so the student is never left with a "
            "reading whose only meaning is itself — which is what makes "
            "rule 3 something they have seen rather than been told."
            % act_id)

    start_factor = float(a.get("start_factor") or 0)
    if start_factor <= 1:
        raise ValueError(
            "drag-lane %r sets start_factor %r. The break-away reading is "
            "larger than the sliding reading — that is the hook — so the "
            "factor is above 1." % (act_id, a.get("start_factor")))

    surf_tabs = "".join(
        _seg("ks3-seg-btn ks3-dlane-surface", s["tab"],
             pressed=(s["id"] == a.get("start_surface", surfaces[0]["id"])),
             data_dlane_surface=s["id"], data_grip=s["grip"],
             data_texture=s["texture"], data_note=s["note"],
             data_name=s["tab"])
        for s in surfaces)
    mass_tabs = "".join(
        _seg("ks3-seg-btn ks3-dlane-mass", "%s kg" % m,
             pressed=(m == a.get("start_mass", masses[0])),
             data_dlane_mass=m)
        for m in masses)

    lanes = ""
    for lane, y in (("start", 212), ("slide", 402)):
        lanes += (
            '<path class="ks3-dlane-floor" d="M40 %d H960"/>'
            '<path class="ks3-dlane-texture" data-dlane-texture="%s" '
            'd="M0 0"/>'
            '<rect class="ks3-dlane-block" x="400" y="%d" width="180" '
            'height="72" rx="10"/>'
            '<path class="ks3-dlane-shaft" data-dlane-shaft="pull-%s" '
            'd="M0 0"/><path class="ks3-dlane-head" '
            'data-dlane-head="pull-%s" d="M0 0"/>'
            '<path class="ks3-dlane-shaft ks3-dlane-fric" '
            'data-dlane-shaft="fric-%s" d="M0 0"/>'
            '<path class="ks3-dlane-head ks3-dlane-fric" '
            'data-dlane-head="fric-%s" d="M0 0"/>'
            '<text class="ks3-dlane-lanelabel" x="40" y="%d">%s</text>'
            % (y, lane, y - 72, lane, lane, lane, lane, y - 96,
               t("BREAKING AWAY" if lane == "start" else "SLIDING STEADILY")))

    svg = ('<svg class="ks3-dlane-svg" viewBox="0 0 1000 430" role="img" '
           'aria-label="" data-dlane-alt>%s</svg>' % lanes)

    fills = "".join(
        '<span class="ks3-dlane-fill ks3-dlane-%s" data-dlane-fill="%s">'
        '</span>' % (k, k)
        for k in ("pull-start", "fric-start", "pull-slide", "fric-slide"))

    lead = ('<p class="ks3-dlane-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-dlane" data-dlane data-g="%s" data-scale="%s" '
            'data-start-factor="%s" data-start-surface="%s" '
            'data-start-mass="%s"%s>%s%s%s'
            '<div class="ks3-dlane-body" data-dlane-body hidden>'
            '<div class="ks3-dlane-controls">'
            '<div class="ks3-dlane-picker"><p class="ks3-dlane-pickerlabel">'
            '%s</p><div class="ks3-dlane-tabrow">%s</div></div>'
            '<div class="ks3-dlane-picker"><p class="ks3-dlane-pickerlabel">'
            '%s</p><div class="ks3-dlane-tabrow">%s</div></div></div>'
            '<div class="ks3-dlane-figwrap">%s%s</div>%s'
            '<p class="ks3-dlane-note" data-dlane-note></p>'
            '<p class="ks3-dlane-compare" data-dlane-compare '
            'data-template="%s"></p>'
            '</div></div>'
            % (e(a.get("g", 10)), e(a.get("scale", 3)), e(start_factor),
               e(a.get("start_surface", surfaces[0]["id"])),
               e(a.get("start_mass", masses[0])), _sibling(a),
               _head("dlane", a), lead,
               _gate(act_id, "drag-lane", a.get("gate") or {}, "dlane"),
               t(a.get("surface_label", "The surface underneath")), surf_tabs,
               t(a.get("mass_label", "The load in the block")), mass_tabs,
               # ⊕ MRB-223, 25 Aug 2026 — ARGUMENT ORDER. `compare` was passed
               # HERE, one slot early, so on the live friction page the raw
               # compare template ("At {mass} kg the sliding reading is
               # {slide} N…") printed as visible text inside the figure
               # wrap, the fills landed where the tiles go, and the tiles'
               # HTML went into `data-template`. ks3_smoke had been red on
               # physics/forces for exactly this and nobody had run it.
               svg, fills, _tiles("dlane", a.get("readouts") or []),
               e(a.get("compare", ""))))


# ═══ p4-06 · #s-bench · the fall ═════════════════════════════════════════

def r_fall_balance(a, act_id):
    """⊕ p4-06 `#s-bench` — watch the two arrows close the gap.

    ⚖️ **THE WEIGHT ARROW NEVER MOVES, AND THAT IS THE ARGUMENT.** Design
    draws it at one fixed length for every object and every speed. The whole
    lesson is that terminal velocity is a BALANCE and not a limit: the weight
    is the same 750 N the whole way down, and it is the resistance that
    changes. A weight arrow that scaled with anything would undo it.

    ⚖️ **RESISTANCE GROWS WITH THE SQUARE OF THE SPEED FRACTION.** `drag =
    weight × f²`, which is exactly why it reaches the weight at `f = 1` for
    every object without the drawer knowing anything about the object. It is
    also why the arrow grows so slowly at first, which the note names.

    ⚠️ **125 PER CENT IS A REAL STATE AND IT IS REACHABLE.** It is the second
    after a canopy opens: resistance above weight, resultant upwards, and the
    skydiver still going down. Design gives it its own branch because it is
    the one place a student will read an upward resultant as upward motion.

    ⚠️ **THE HAILSTONE IS 1 N AND ITS READINGS NEED TWO DECIMALS.** A single
    rounding rule across a bench spanning 1 N to 750 N prints `0.0 N` for the
    hailstone at half speed, which is a bench that says the resistance is
    nothing when it is a quarter of the weight. The precision follows the
    object.

    HOOKS: `data-fall` (wrapper, `data-weight-px`) · `data-fall-gate` ·
    `data-fall-gopt` · `data-fall-body` · `data-fall-object` (carrying
    `data-weight`, `data-term`) · `data-fall-frac` · `data-fall-shaft` ·
    `data-fall-head` · `data-fall-streaks` · `data-fall-out` ·
    `data-fall-note`.
    """
    bodies = a.get("bodies") or []
    if len(bodies) < 3:
        raise ValueError(
            "fall-balance %r declares %d object(s). The bench contrasts what "
            "changes the steady speed — posture, canopy, size — against the "
            "weight, which does not." % (act_id, len(bodies)))
    _unique(bodies, act_id, "fall-balance", "object")
    for b in bodies:
        for field in ("weight", "term", "word", "w", "r"):
            if b.get(field) in (None, ""):
                raise ValueError(
                    "fall-balance %r object %r has no %r."
                    % (act_id, b.get("id"), field))
        if b["weight"] <= 0 or b["term"] <= 0:
            raise ValueError(
                "fall-balance %r object %r has a non-positive weight or "
                "terminal speed." % (act_id, b.get("id")))

    branches = a.get("branches") or {}
    need = ("at_rest", "growing", "matched", "past", "canopy")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "fall-balance %r has no note for state(s) %s. The matched state "
            "is terminal velocity and the past state is the second after a "
            "canopy opens; both are the point of the lesson."
            % (act_id, ", ".join(missing)))

    frac = a.get("frac") or {}
    for k in ("min", "max", "step", "start"):
        if k not in frac:
            raise ValueError("fall-balance %r frac has no %r." % (act_id, k))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-fall-object", b["tab"],
             pressed=(b["id"] == a.get("start_body", bodies[0]["id"])),
             data_fall_object=b["id"], data_weight=b["weight"],
             data_term=b["term"], data_word=b["word"], data_w=b["w"],
             data_r=b["r"], data_canopy=("1" if b.get("canopy") else "0"))
        for b in bodies)

    # Design's own 1000×520 viewBox (page lines 152–178).
    svg = (
        '<svg class="ks3-fall-svg" viewBox="0 0 1000 520" role="img" '
        'aria-label="" data-fall-alt>'
        '<path class="ks3-fall-streaks" data-fall-streaks d="M0 0"/>'
        '<rect class="ks3-fall-body" data-fall-body-shape x="0" y="212" '
        'width="0" height="76" rx="0"/>'
        '<path class="ks3-fall-shaft" data-fall-shaft="weight" d="M0 0"/>'
        '<path class="ks3-fall-head" data-fall-head="weight" d="M0 0"/>'
        '<path class="ks3-fall-shaft ks3-fall-drag" '
        'data-fall-shaft="drag" d="M0 0" hidden/>'
        '<path class="ks3-fall-head ks3-fall-drag" data-fall-head="drag" '
        'd="M0 0" hidden/>'
        '<text class="ks3-fall-nodrag" x="500" y="180" text-anchor="middle" '
        'data-fall-nodrag hidden>%s</text>'
        '<path class="ks3-fall-shaft ks3-fall-over" '
        'data-fall-shaft="over" d="M0 0" hidden/>'
        '<path class="ks3-fall-head ks3-fall-over" data-fall-head="over" '
        'd="M0 0" hidden/></svg>' % t(a.get("zero_label", "0 N")))

    fills = "".join(
        '<span class="ks3-fall-fill ks3-fall-%s" data-fall-fill="%s"></span>'
        % (k, k) for k in ("drag", "weight", "over", "word"))

    lead = ('<p class="ks3-fall-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    branch_data = "".join(
        '<span data-fall-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    return ('<div class="ks3-fall" data-fall data-weight-px="%s" '
            'data-start-body="%s"%s>%s%s%s'
            '<div class="ks3-fall-bench" data-fall-bench hidden>'
            '<div class="ks3-fall-controls">'
            '<div class="ks3-fall-picker"><p class="ks3-fall-pickerlabel">%s'
            '</p><div class="ks3-fall-tabrow">%s</div></div>'
            '<div class="ks3-fall-row"><div class="ks3-fall-rowhead">'
            '<label for="%s-frac">%s</label>'
            '<p class="ks3-fall-reading" data-fall-out="speed">—</p></div>'
            '<input class="ks3-fall-slider" type="range" id="%s-frac" '
            'min="%s" max="%s" step="%s" value="%s" data-fall-frac></div>'
            '</div>'
            '<div class="ks3-fall-figwrap">%s%s</div>%s'
            '<p class="ks3-fall-note" data-fall-note></p>%s</div></div>'
            % (e(a.get("weight_px", 130)),
               e(a.get("start_body", bodies[0]["id"])), _sibling(a),
               _head("fall", a), lead,
               _gate(act_id, "fall-balance", a.get("gate") or {}, "fall"),
               t(a.get("body_label", "What is falling")), tabs,
               e(act_id), t(frac.get("label", "How fast it is going")),
               e(act_id), e(frac["min"]), e(frac["max"]), e(frac["step"]),
               e(frac["start"]),
               svg, fills, _tiles("fall", a.get("readouts") or []),
               branch_data))


# ═══ p4-07 · #s-bench · the spanner and the tight nut ════════════════════

def r_spanner_rig(a, act_id):
    """⊕ p4-07 `#s-bench` — one nut, two ways to shift it.

    ⚖️ **TWO ROUTES TO THE SAME THRESHOLD, NAMED WITH LIVE FIGURES.** Design's
    two branches both say what would ALSO have worked: the same pull further
    out, or a smaller pull at this distance. That is the product being taught
    rather than a number being reported, and it is why the note computes
    `NEED ÷ arm` and `NEED ÷ force` rather than describing them.

    ⚖️ **THE HANDLE IS DRAWN TO SCALE; THE FORCE ARROW IS NOT ON THE SAME
    SCALE.** Design uses 1400 px per metre for the handle and 0.9 px per
    newton for the pull, and the legal line says so. They are different
    quantities — a length and a force — so one scale for both would be
    meaningless rather than more honest. Two scales are emitted separately so
    neither can be read as the other.

    ⚠️ **THE TURN ARROW IS SOLID WHEN THE MOMENT CLEARS THE THRESHOLD AND
    DASHED WHEN IT DOES NOT**, and the verdict is also a WORD. Hue is never
    the only channel.

    ⚠️ **"AT RIGHT ANGLES" IS LOAD-BEARING.** The lesson handles only the
    perpendicular case; dropping the phrase makes the formula wrong rather
    than simplified. It rides in the symbol key of the formula block and in
    the bench lead, and the renderer requires the lead.

    HOOKS: `data-span` (wrapper, `data-need`, `data-arm-scale`,
    `data-f-scale`) · `data-span-gate` · `data-span-gopt` · `data-span-body`
    · `data-span-arm` · `data-span-force` · `data-span-handle` ·
    `data-span-grip` · `data-span-shaft` · `data-span-head` ·
    `data-span-turn` · `data-span-dim` · `data-span-out` · `data-span-note`.
    """
    arms = a.get("arms") or []
    if len(arms) < 3:
        raise ValueError(
            "spanner-rig %r declares %d arm(s). The whole demand is that the "
            "same pull does different work at different distances."
            % (act_id, len(arms)))
    force = a.get("force") or {}
    for k in ("min", "max", "step", "start"):
        if k not in force:
            raise ValueError("spanner-rig %r force has no %r." % (act_id, k))
    need = a.get("need")
    if not isinstance(need, (int, float)) or need <= 0:
        raise ValueError(
            "spanner-rig %r has no loosening moment. Without a threshold the "
            "bench reports a number and asks nothing." % act_id)
    if not a.get("lead"):
        raise ValueError(
            "spanner-rig %r has no lead. The lead is where 'at right angles' "
            "is stated, and without it the relationship on the page is wrong "
            "rather than simplified." % act_id)

    reach = [x for x in arms if float(force["max"]) * float(x) >= need]
    if not reach:
        raise ValueError(
            "spanner-rig %r: no arm reaches %s N m even at the largest pull "
            "of %s N, so the nut can never turn and the threshold is a dead "
            "state." % (act_id, need, force["max"]))
    stuck = [x for x in arms if float(force["max"]) * float(x) < need]
    if not stuck:
        raise ValueError(
            "spanner-rig %r: every arm clears %s N m at the largest pull, so "
            "the 'does not budge' verdict is unreachable and half the bench "
            "is unauthored." % (act_id, need))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-span-arm", "%.2f m" % float(x),
             pressed=(float(x) == float(a.get("start_arm", arms[0]))),
             data_span_arm=("%.2f" % float(x)))
        for x in arms)

    # Design's own 1000×420 viewBox (page lines 150–180).
    svg = (
        '<svg class="ks3-span-svg" viewBox="0 0 1000 420" role="img" '
        'aria-label="" data-span-alt>'
        '<path class="ks3-span-nut" d="M250 250 L206 224 L206 172 L250 146 '
        'L294 172 L294 224 Z"/>'
        '<circle class="ks3-span-pivot" cx="250" cy="198" r="9"/>'
        '<rect class="ks3-span-handle" data-span-handle x="250" y="176" '
        'width="0" height="44" rx="10"/>'
        '<rect class="ks3-span-grip" data-span-grip x="0" y="168" '
        'width="46" height="60" rx="12"/>'
        '<path class="ks3-span-shaft" data-span-shaft d="M0 0"/>'
        '<path class="ks3-span-head" data-span-head d="M0 0"/>'
        '<path class="ks3-span-dim" data-span-dim d="M0 0"/>'
        '<path class="ks3-span-turn" data-span-turn d="M250 118 '
        'A80 80 0 0 1 330 198"/></svg>')

    fills = "".join(
        '<span class="ks3-span-fill ks3-span-%s" data-span-fill="%s"></span>'
        % (k, k) for k in ("force", "dist", "turn"))

    branches = a.get("branches") or {}
    need_keys = ("turns", "stuck", "stuck_far")
    missing = [k for k in need_keys if not branches.get(k)]
    if missing:
        raise ValueError(
            "spanner-rig %r has no note for state(s) %s. `stuck_far` is the "
            "state where the arm needed is longer than any spanner offered, "
            "and it is a different sentence rather than a bigger number — "
            "it is where the length of pipe comes in."
            % (act_id, ", ".join(missing)))
    branch_data = "".join(
        '<span data-span-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need_keys)

    return ('<div class="ks3-span" data-span data-need="%s" '
            'data-arm-scale="%s" data-f-scale="%s" data-start-arm="%s"%s>%s'
            '<p class="ks3-span-lead">%s</p>%s'
            '<div class="ks3-span-body" data-span-body hidden>'
            '<div class="ks3-span-controls">'
            '<div class="ks3-span-picker"><p class="ks3-span-pickerlabel">%s'
            '</p><div class="ks3-span-tabrow">%s</div></div>'
            '<div class="ks3-span-row"><div class="ks3-span-rowhead">'
            '<label for="%s-force">%s</label>'
            '<p class="ks3-span-reading" data-span-out="force">%s N</p></div>'
            '<input class="ks3-span-slider" type="range" id="%s-force" '
            'min="%s" max="%s" step="%s" value="%s" data-span-force></div>'
            '</div>'
            '<div class="ks3-span-figwrap">%s%s</div>%s'
            '<p class="ks3-span-note" data-span-note></p>%s</div></div>'
            % (e(need), e(a.get("arm_scale", 1400)), e(a.get("f_scale", 0.9)),
               e("%.2f" % float(a.get("start_arm", arms[0]))), _sibling(a),
               _head("span", a),
               rich(a["lead"]).replace("{need}", "%s N m" % need),
               _gate(act_id, "spanner-rig", a.get("gate") or {}, "span"),
               t(a.get("arm_label", "Distance from the pivot")), tabs,
               e(act_id), t(force.get("label", "Your pull")),
               e(force["start"]), e(act_id), e(force["min"]),
               e(force["max"]), e(force["step"]), e(force["start"]),
               svg, fills, _tiles("span", a.get("readouts") or []),
               branch_data))


# ═══ p4-08 · #s-bench · loading a spring ═════════════════════════════════

def r_spring_plot(a, act_id):
    """⊕ p4-08 `#s-bench` — take the readings, plot them, find where it bends.

    ⚖️ **THE GRAPH SHOWS ONLY WHAT THE STUDENT CHOSE TO RECORD.** Design plots
    the recorded readings and nothing else, so an incomplete investigation
    LOOKS incomplete. A bench that drew the whole curve on load would have
    answered the question the investigation exists to ask — where does the
    line stop being straight — before the student took a single reading. The
    rail does not count the bench done until two readings are plotted, and
    the renderer refuses a target below two: one point defines no line.

    ⚖️ **THE BEND IS REACHABLE AND THE PERMANENT DEFORMATION IS REACHABLE.**
    `limit` and `spoil` must both lie inside the slider's range, or the whole
    second half of the lesson is a state the bench cannot show. Asserted.

    ⚠️ **POINTS ARE ARCS IN ONE PATH STRING, NOT `<circle>` ELEMENTS.**
    Design's note for the generator: no `<sc-for>` inside an `<svg>` and no
    per-point element. The wiring rebuilds one `d` attribute.

    ⚠️ **`extension = load × per_n` UP TO THE LIMIT, THEN `past` PER NEWTON.**
    Two straight segments, and the second is steeper. The renderer requires
    `past > per_n`, because a bench where the line bends the other way would
    say a spring gets stiffer past its limit.

    ⚠️ **THE SPRING REMEMBERS.** ⊕ P4-03, 31 Aug 2026. The wiring keeps the
    largest load the spring has seen and carries the stretch that did not
    come back into every reading below it, including the zero. Before this
    the bench announced permanent deformation at 10 N and then, one drag
    later, read 40 mm at 2 N again — exactly what it read before it was
    ruined. `data-splot-newspring` is the way back and is not optional: a
    bench that can be ruined and not reset is a dead end.

    HOOKS: `data-splot` (wrapper, `data-per-n`, `data-limit`, `data-spoil`,
    `data-past`, `data-target`, `data-past-lead`, `data-spoiled-lead`) ·
    `data-splot-gate` · `data-splot-gopt` ·
    `data-splot-body` · `data-splot-load` · `data-splot-record` ·
    `data-splot-clear` · `data-splot-newspring` · `data-splot-coil` ·
    `data-splot-extbar` ·
    `data-splot-grid` · `data-splot-dots` · `data-splot-dots-set` ·
    `data-splot-line` ·
    `data-splot-out` · `data-splot-note`.
    """
    per_n = a.get("per_n")
    limit = a.get("limit")
    spoil = a.get("spoil")
    past = a.get("past")
    load = a.get("load") or {}
    for k in ("min", "max", "step", "start"):
        if k not in load:
            raise ValueError("spring-plot %r load has no %r." % (act_id, k))
    for name, v in (("per_n", per_n), ("limit", limit),
                    ("spoil", spoil), ("past", past)):
        if not isinstance(v, (int, float)) or v <= 0:
            raise ValueError(
                "spring-plot %r has no positive %s." % (act_id, name))
    if past <= per_n:
        raise ValueError(
            "spring-plot %r gives %s mm per newton past the limit against %s "
            "mm on the straight line. Past the limit each newton adds MORE, "
            "not less — a bench bending the other way teaches that a spring "
            "stiffens when it is overloaded." % (act_id, past, per_n))
    if not (float(load["min"]) < limit < float(load["max"])):
        raise ValueError(
            "spring-plot %r puts the limit of proportionality at %s N, "
            "outside the slider's %s–%s N. The bend is the lesson and it has "
            "to be reachable." % (act_id, limit, load["min"], load["max"]))
    if not (limit < spoil <= float(load["max"])):
        raise ValueError(
            "spring-plot %r puts permanent deformation at %s N, which is not "
            "above the limit and inside the range. Rung 2 is about exactly "
            "that state." % (act_id, spoil))

    target = int(a.get("target") or 0)
    if target < 2:
        raise ValueError(
            "spring-plot %r counts the bench done at %d reading(s). One "
            "point defines no line, so the investigation is not begun."
            % (act_id, target))

    branches = a.get("branches") or {}
    # ⊕ P4-03, 31 Aug 2026 — `zero_set` and `under_set` ARE REQUIRED, and
    # the bench is wrong without them. It announces permanent deformation
    # ("taking the load off will not bring it back") and the wiring now
    # carries that set into every later reading, so a bench with no note
    # for the way back down demonstrates the misconception the lesson
    # registers as FORCE-43 on the student's very next drag of the slider.
    need = ("zero", "on_line", "at_limit", "past_limit", "deformed",
            "zero_set", "under_set")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "spring-plot %r has no note for state(s) %s."
            % (act_id, ", ".join(missing)))
    # ⊕ P4-02, 31 Aug 2026 — the attempt panel's two refusals. Scaling a
    # ratio up is legal on the straight line and nowhere else; a bench that
    # hands the five lines a reading from past the limit, or from a spring
    # that no longer returns, is endorsing the arithmetic the lesson two
    # screens above has just disproved.
    for k in ("attempt_past_limit", "attempt_spoiled"):
        if not a.get(k):
            raise ValueError(
                "spring-plot %r has no %r. The five lines below the bench "
                "read this bench's live load, and there are two states "
                "where no prediction can honestly be made from it — past "
                "the limit of proportionality, and after the spring has "
                "taken a permanent set. Each needs its own refusal."
                % (act_id, k))

    # Design's own two viewBoxes (page lines 168–212): the spring at 300×460
    # and the graph at 1000×400.
    spring = (
        '<svg class="ks3-splot-spring" viewBox="0 0 300 460" role="img" '
        'aria-label="" data-splot-springalt>'
        '<path class="ks3-splot-clamp" d="M60 30 H240"/>'
        '<path class="ks3-splot-natural" d="M60 110 H240"/>'
        '<path class="ks3-splot-coil" data-splot-coil d="M0 0"/>'
        '<rect class="ks3-splot-hanger" data-splot-hanger x="90" y="0" '
        'width="120" height="34" rx="8"/>'
        '<path class="ks3-splot-extbar" data-splot-extbar d="M0 0"/></svg>')
    graph = (
        '<svg class="ks3-splot-graph" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-splot-graphalt>'
        '<path class="ks3-splot-axis" d="M120 40 V340 H960"/>'
        '<path class="ks3-splot-grid" data-splot-grid d="M0 0"/>'
        '<path class="ks3-splot-prop" data-splot-prop d="M0 0"/>'
        '<path class="ks3-splot-line" data-splot-line d="M0 0"/>'
        '<path class="ks3-splot-dots" data-splot-dots d="M0 0"/>'
        # ⊕ P4-03 — points recorded AFTER the spring took a permanent set,
        # drawn hollow. A filled and a hollow ring differ in shape and not
        # only in hue, and the two sets must not be joined by the line:
        # they are two different springs' worth of readings.
        '<path class="ks3-splot-dots" data-splot-dots-set '
        'style="fill:none;stroke:var(--ks3-accent);stroke-width:3" '
        'd="M0 0"/>'
        '<text class="ks3-splot-axislabel" x="540" y="386" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-splot-axislabel" x="40" y="190" '
        'transform="rotate(-90 40 190)" text-anchor="middle">%s</text>'
        '</svg>'
        % (t(a.get("x_label", "Load in newtons")),
           t(a.get("y_label", "Extension in millimetres"))))

    branch_data = "".join(
        '<span data-splot-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-splot-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-splot" data-splot data-per-n="%s" '
            'data-limit="%s" data-spoil="%s" data-past="%s" '
            'data-target="%d" data-past-lead="%s" data-spoiled-lead="%s"'
            '%s>%s%s%s'
            '<div class="ks3-splot-body" data-splot-body hidden>'
            '<div class="ks3-splot-controls">'
            '<div class="ks3-splot-row"><div class="ks3-splot-rowhead">'
            '<label for="%s-load">%s</label>'
            '<p class="ks3-splot-reading" data-splot-out="load">%s N</p>'
            '</div><input class="ks3-splot-slider" type="range" id="%s-load" '
            'min="%s" max="%s" step="%s" value="%s" data-splot-load></div>'
            '<div class="ks3-splot-btns">'
            '<button type="button" class="ks3-seg-btn ks3-splot-record" '
            'data-splot-record>%s</button>'
            '<button type="button" class="ks3-seg-btn ks3-splot-clear" '
            'data-splot-clear>%s</button>'
            '<button type="button" class="ks3-seg-btn ks3-splot-clear" '
            'data-splot-newspring hidden>%s</button></div></div>'
            '<div class="ks3-splot-figs">'
            '<div class="ks3-splot-figwrap">%s'
            '<span class="ks3-splot-fill ks3-splot-ext" '
            'data-splot-fill="ext"></span>'
            '<span class="ks3-splot-fill ks3-splot-load" '
            'data-splot-fill="load"></span></div>'
            '<div class="ks3-splot-figwrap ks3-splot-graphwrap">%s</div>'
            '</div>%s<p class="ks3-splot-note" data-splot-note></p>%s'
            '</div></div>'
            % (e(per_n), e(limit), e(spoil), e(past), target,
               e(a["attempt_past_limit"]), e(a["attempt_spoiled"]),
               _sibling(a),
               _head("splot", a), lead,
               _gate(act_id, "spring-plot", a.get("gate") or {}, "splot"),
               e(act_id), t(load.get("label", "Load on the spring")),
               e(load["start"]), e(act_id), e(load["min"]), e(load["max"]),
               e(load["step"]), e(load["start"]),
               t(a.get("record_label", "Record this reading")),
               t(a.get("clear_label", "Clear the readings")),
               t(a.get("new_spring_label", "Fit a new spring")),
               spring, graph,
               _tiles("splot", a.get("readouts") or []), branch_data))


# ═══ p4-09 · #s-bench · the sorter ═══════════════════════════════════════

def r_force_sorter(a, act_id):
    """⊕ p4-09 `#s-bench` — eight situations, four labels, nothing revealed.

    ⚖️ **THE UNLABELLED STATE SHOWS THE DIAGRAM AND REVEALS NOTHING.** Design
    draws the two bodies, the gap or contact marker and the arrow BEFORE the
    student commits, and shows no verdict at all until they do. That is the
    point: the drawing carries the evidence the classification is made from,
    and printing the answer beside it would remove the only demand the block
    makes. The renderer emits every verdict hidden and the wiring reveals one.

    ⚖️ **A LABEL LOCKS ON COMMIT.** A sorter that lets a student cycle through
    four labels until the tick appears has been reduced to a guessing game,
    so the four buttons disable once one is pressed. The verdict then names
    both what they said and what it is.

    ⚠️ **AIR RESISTANCE IS FILED AS A CONTACT FORCE, DELIBERATELY.** It is the
    card a student who has only half-heard `p4-01` gets wrong, and the note on
    that case argues it rather than asserting it. The renderer takes the
    answer as authored and does not second-guess it.

    HOOKS: `data-fsort` (wrapper, `data-total`, `data-sibling`) ·
    `data-fsort-tab` · `data-fsort-case` · `data-fsort-label` ·
    `data-fsort-body` (valued `a` / `b`) · `data-fsort-join` ·
    `data-fsort-shaft` · `data-fsort-head` · `data-fsort-out` ·
    `data-fsort-note` · `data-fsort-sealed`.
    """
    cases = a.get("cases") or []
    labels = a.get("labels") or []
    if len(cases) < 4 or len(labels) < 3:
        raise ValueError(
            "force-sorter %r declares %d case(s) and %d label(s)."
            % (act_id, len(cases), len(labels)))
    _unique(cases, act_id, "force-sorter", "case")
    _unique(labels, act_id, "force-sorter", "label")

    label_ids = {x["id"] for x in labels}
    used = set()
    for c in cases:
        if c.get("answer") not in label_ids:
            raise ValueError(
                "force-sorter %r case %r answers %r, which is not one of the "
                "four labels %s." % (act_id, c.get("id"), c.get("answer"),
                                     sorted(label_ids)))
        used.add(c["answer"])
        for field in ("title", "a", "b", "sense", "note"):
            if not c.get(field):
                raise ValueError(
                    "force-sorter %r case %r has no %r."
                    % (act_id, c.get("id"), field))
    unused = sorted(label_ids - used)
    if unused:
        raise ValueError(
            "force-sorter %r offers label(s) %s that no case is an example "
            "of. A label that is never right is a distractor the student can "
            "learn to skip." % (act_id, unused))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-fsort-tab", c["tab"], pressed=(i == 0),
             data_fsort_tab=i)
        for i, c in enumerate(cases))

    buttons = "".join(
        '<button type="button" class="ks3-fsort-label" '
        'data-fsort-label="%s" aria-pressed="false">%s</button>'
        % (e(x["id"]), t(x["label"])) for x in labels)

    # Design's own 1000×340 viewBox (page lines 128–150).
    svg = (
        '<svg class="ks3-fsort-svg" viewBox="0 0 1000 340" role="img" '
        'aria-label="" data-fsort-alt>'
        '<circle class="ks3-fsort-body" data-fsort-body="a" cx="0" cy="150" '
        'r="74"/>'
        '<circle class="ks3-fsort-body" data-fsort-body="b" cx="0" cy="150" '
        'r="74"/>'
        '<path class="ks3-fsort-shaft" data-fsort-shaft d="M0 0"/>'
        '<path class="ks3-fsort-head" data-fsort-head d="M0 0"/>'
        '<path class="ks3-fsort-gap" data-fsort-join="gap" d="M0 0" hidden/>'
        '<path class="ks3-fsort-touch" data-fsort-join="contact" d="M0 0" '
        'hidden/>'
        '</svg>')

    # ⚠️ THE JOIN WORD IS A SPAN, NOT AN SVG `<text>`. It is a LIVE value —
    # it changes with the case — and an SVG `<text>` with no content ships
    # an empty element in the bytes, which MRB-254 gates and which caught
    # the first draft of this renderer. Every live value on a P4 diagram is
    # an absolutely-positioned HTML span for exactly this reason.
    fills = "".join(
        '<span class="ks3-fsort-fill ks3-fsort-%s" data-fsort-fill="%s">'
        '</span>' % (k, k) for k in ("a", "b", "join"))

    data = "".join(
        '<span data-fsort-data="%d" data-title="%s" data-a="%s" data-b="%s" '
        'data-answer="%s" data-answer-label="%s" data-touch="%s" '
        'data-kind="%s" data-sense="%s" data-note="%s" data-alt="%s" '
        'hidden></span>'
        % (i, e(c["title"]), e(c["a"]), e(c["b"]), e(c["answer"]),
           e({x["id"]: x["label"] for x in labels}[c["answer"]]),
           "1" if c.get("touch") else "0",
           e("Contact" if c["answer"] == a.get("contact_label_id", "contact")
             else "Non-contact"),
           e(c["sense"]), e(c["note"]), e(c.get("alt", "")))
        for i, c in enumerate(cases))

    lead = ('<p class="ks3-fsort-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-fsort" data-fsort data-total="%d" '
            'data-target="%d"%s>%s%s'
            '<div class="ks3-fsort-tabrow">%s</div>'
            '<p class="ks3-fsort-title" data-fsort-title></p>'
            '<div class="ks3-fsort-figwrap">%s%s</div>'
            '<p class="ks3-fsort-askhead">%s</p>'
            '<div class="ks3-fsort-labels">%s</div>'
            '<div class="ks3-fsort-verdict" data-fsort-verdict hidden>%s'
            '<p class="ks3-fsort-note" data-fsort-note></p></div>'
            '<p class="ks3-fsort-sealed" data-fsort-sealed>%s</p>%s</div>'
            % (len(cases), int(a.get("target") or len(cases)), _sibling(a),
               _head("fsort", a), lead, tabs, svg, fills,
               t(a.get("ask_label", "Give it a label")), buttons,
               _tiles("fsort", a.get("readouts") or []),
               t(a.get("sealed_label",
                       "Unlabelled. Nothing is revealed until you commit to "
                       "one of the four.")),
               data))


# ═══ the band sections · #s-pairs · #s-three · #s-rules · #s-stages ══════

def r_force_band(a, act_id):
    """⊕ The band card block Design puts under five of the nine benches.

    ⚖️ **`panels`, NOT `cards`.** `cards` is claimed by `r_activity` itself
    with NO opt-out, so a payload using it gets two renderers and renders
    blank. The key is deliberately different for that reason and for no other.

    ⚖️ **THE BAND STOP IS A RAIL STOP, AND IT IS TICKED BY THE BENCH ABOVE
    IT.** This block carries no control of its own — it is the payoff of the
    instrument beside it, exactly as MRB-249 describes — so its section is
    marked from the bench's own wiring at Design's earlier threshold rather
    than by anything here. See the module note.

    HOOKS: none. This block is drawn and does not move.
    """
    panels = a.get("panels") or []
    if len(panels) < 3:
        raise ValueError(
            "force-band %r declares %d panel(s). Every band block in P4 is a "
            "numbered set of at least three." % (act_id, len(panels)))
    _unique(panels, act_id, "force-band", "panel", key="num")

    items = ""
    for p in panels:
        for field in ("num", "name", "body"):
            if not p.get(field):
                raise ValueError(
                    "force-band %r panel %r has no %r."
                    % (act_id, p.get("num"), field))
        tell = ('<p class="ks3-fband-tell">%s</p>' % rich(p["tell"])
                if p.get("tell") else "")
        items += ('<li class="ks3-fband-item">'
                  '<span class="ks3-fband-num" aria-hidden="true">%s</span>'
                  '<p class="ks3-fband-name">%s</p>'
                  '<p class="ks3-fband-body">%s</p>%s</li>'
                  % (t(p["num"]), t(p["name"]), rich(p["body"]), tell))

    strip = ""
    if a.get("strip"):
        strip = ('<div class="ks3-fband-strip">%s</div>'
                 % _strip_svg(a["strip"], act_id))

    columns = ""
    cols = a.get("columns") or []
    if cols:
        if len(cols) != 2:
            raise ValueError(
                "force-band %r declares %d column(s). Design's is a pair — "
                "wanted here, not wanted here — and one column on its own "
                "makes a claim the other half was there to balance."
                % (act_id, len(cols)))
        cells = "".join(
            '<div class="ks3-fband-col"><p class="ks3-fband-coltitle">%s</p>'
            '<ul class="ks3-fband-collist">%s</ul></div>'
            % (t(c["title"]),
               "".join("<li>%s</li>" % rich(x) for x in (c.get("items") or [])))
            for c in cols)
        columns = '<div class="ks3-fband-cols">%s</div>' % cells

    lead = ('<p class="ks3-fband-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")
    close = ('<p class="ks3-fband-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    # ⊕ MRB-223 — the `check` shell already emits this figure's eyebrow and
    # <h2> from the same two keys; the band printed them a second time
    # (measured on every P4 figure page). The shell's row is the only one.
    return ('<div class="ks3-fband" data-fband>'
            '%s%s<ol class="ks3-fband-list">%s</ol>%s%s</div>'
            % (lead, strip, items, columns, close))


# ═══ the drawn figures ═══════════════════════════════════════════════════
#
# ⚠️ NONE OF THESE IS A TRIANGLE, AND NONE OF THEM CAN BECOME ONE. The
# triangle is `r_cover_triangle` in the engine and nothing in this module
# reaches it. `p4-07` is the unit's only product and the only page that takes
# the triangle path; every figure below draws a sum, a difference or a ratio.

def _arrow_v(x, y0, length, down=True, head=26, half=18):
    """A vertical arrow as two paths, Design's own head geometry."""
    tip = y0 + length if down else y0 - length
    base = tip - head if down else tip + head
    return ('<path class="ks3-p4fig-shaft" d="M%s %s V%s"/>'
            '<path class="ks3-p4fig-head" d="M%s %s L%s %s L%s %s Z"/>'
            % (x, y0, base, x, tip, x - half, base, x + half, base))


def _resultant_beam(fig, act_id):
    """p4-02 — three bars on one scale, and the lower two fill the top one.

    ⚖️ **THE PARTS SUM TO THE WHOLE, TO THE PIXEL, AND IT IS ASSERTED.**
    Design draws 700 px for 40 N, 437 for 25 N and 263 for 15 N: 437 + 263 =
    700 exactly. The widths are DERIVED from the authored newtons at one
    scale, so a beam whose halves do not add up cannot be authored — which is
    the whole reason this relationship gets a beam rather than a triangle.
    """
    whole = fig.get("whole") or {}
    parts = fig.get("parts") or []
    if len(parts) != 2:
        raise ValueError(
            "resultant-beam %r draws %d part(s). The relationship is one bar "
            "filled by two." % (act_id, len(parts)))
    wn = float(whole.get("newtons") or 0)
    total = sum(float(p.get("newtons") or 0) for p in parts)
    if wn <= 0 or abs(total - wn) > 1e-9:
        raise ValueError(
            "resultant-beam %r: the parts are %s N and the whole is %s N. "
            "The two lower bars fill the top one EXACTLY — that arithmetic is "
            "the teaching, and a bar model that does not add up lies."
            % (act_id, total, wn))

    # Design's own row baselines: 38, 150, 238. NOT an even 112 apart — the
    # third bar sits tight under the second so the two tie-lines that run
    # from the whole down to the remainder are short, and the eye reads them
    # as one join rather than as a third row of its own. Measured off her
    # SVG, not interpolated.
    X, W = 300.0, 700.0
    YS = (38, 150, 238)
    scale = W / wn
    rows = ""
    y = YS[0]
    x = X
    specs = [(whole, X, "whole")] + [(p, None, "part") for p in parts]
    for i, (spec, fixed, _kind) in enumerate(specs):
        n = float(spec["newtons"])
        w = n * scale
        bx = X if fixed is not None else x
        if i == 1:
            bx = X
            x = X + w
        elif i == 2:
            bx = X + float(parts[0]["newtons"]) * scale
        right = spec.get("dir", "right") == "right"
        head = ('<path class="ks3-p4fig-head" d="M%.1f %d L%.1f %d L%.1f %d Z"/>'
                % (bx + w + 42, y + 24, bx + w, y - 4, bx + w, y + 52)) if right \
            else ('<path class="ks3-p4fig-head" d="M%.1f %d L%.1f %d L%.1f %d Z"/>'
                  % (bx - 42, y + 24, bx, y - 4, bx, y + 52))
        rows += ('<text class="ks3-p4fig-rowlabel" x="230" y="%d" '
                 'text-anchor="end">%s</text>'
                 '<rect class="ks3-p4fig-bar" x="%.1f" y="%d" width="%.1f" '
                 'height="48" rx="6"/>%s'
                 '<text class="ks3-p4fig-barlabel" x="%.1f" y="%d" '
                 'text-anchor="middle">%s</text>'
                 % (y + 28, t(spec.get("label", "")), bx, y, w, head,
                    bx + w / 2.0, y + 32, t("%s N" % spec["newtons"])))
        y = YS[i + 1] if i + 1 < len(YS) else y + 112

    tie_x = X + float(parts[0]["newtons"]) * scale
    ties = ('<path class="ks3-p4fig-tie" d="M%.1f 86 V238"/>'
            '<path class="ks3-p4fig-tie" d="M%.1f 86 V238"/>'
            % (tie_x, X + W))
    return ('<svg class="ks3-p4fig ks3-p4fig-beam" viewBox="0 0 1060 300" '
            'role="img" aria-label="%s">%s%s</svg>'
            % (e(fig.get("aria_label", "")), rows, ties))


def _balance_beam(fig, act_id):
    """p4-03 — two panels to one scale: balanced, and unbalanced.

    ⚖️ **BOTH PANELS ARE DRAWN AT THE SAME PX PER NEWTON.** The claim is that
    equal-length arrows mean equal forces, so the two panels have to share a
    scale or the right-hand one proves nothing.
    """
    panels = fig.get("panels") or []
    if len(panels) != 2:
        raise ValueError(
            "balance-beam %r draws %d panel(s); the contrast is two."
            % (act_id, len(panels)))
    scale = float(fig.get("scale") or 0)
    if scale <= 0:
        raise ValueError("balance-beam %r has no px-per-newton scale."
                         % act_id)

    out = ""
    for i, p in enumerate(panels):
        px = 60 + i * 480
        up = float(p.get("up") or 0)
        down = float(p.get("down") or 0)
        over = round(down - up, 6)
        out += ('<text class="ks3-p4fig-panellabel" x="%d" y="42">%s</text>'
                '<rect class="ks3-p4fig-panel" x="%d" y="58" width="400" '
                'height="300" rx="14"/>'
                '<rect class="ks3-p4fig-load" x="%d" y="188" width="120" '
                'height="46" rx="8"/>'
                % (px, t(p.get("title", "")), px, px + 140))
        cx = px + 200
        out += _arrow_v(cx, 188, up * scale, down=False)
        out += _arrow_v(cx, 234, down * scale, down=True)
        out += ('<text class="ks3-p4fig-arrowlabel" x="%d" y="%d">%s</text>'
                '<text class="ks3-p4fig-arrowlabel" x="%d" y="%d">%s</text>'
                % (cx + 40, 188 - up * scale + 38, t("up %s N" % p.get("up")),
                   cx + 40, 234 + down * scale - 20,
                   t("down %s N" % p.get("down"))))
        if over > 0:
            out += _arrow_v(px + 58, 234, over * scale, down=True)
        out += ('<text class="ks3-p4fig-verdict" x="%d" y="352">%s</text>'
                % (px + 20, t(p.get("verdict", ""))))
    return ('<svg class="ks3-p4fig ks3-p4fig-panels" viewBox="0 0 1000 380" '
            'role="img" aria-label="%s">%s</svg>'
            % (e(fig.get("aria_label", "")), out))


def _spring_beam_graph(fig, act_id):
    """p4-08 — equal helpings, and the same fact as a line that bends.

    ⚖️ **THE BARS ARE EQUAL HELPINGS AND THE GRAPH BENDS.** A proportionality
    is not a product, so there is no triangle here: the bars show that three
    newtons is three helpings of one newton's worth, and the graph shows the
    same fact plus the thing the bars cannot — where the rule gives out.
    """
    rows = fig.get("rows") or []
    if len(rows) < 3:
        raise ValueError(
            "spring-beam %r draws %d row(s). Fewer than three cannot show "
            "that the helpings are equal." % (act_id, len(rows)))
    per = float(fig.get("per_n") or 0)
    if per <= 0:
        raise ValueError("spring-beam %r has no mm-per-newton." % act_id)
    px_per_mm = float(fig.get("px_per_mm") or 5.0)

    out = ('<text class="ks3-p4fig-rowlabel" x="40" y="40">%s</text>'
           % t(fig.get("title", "")))
    y = 94
    for r in rows:
        n = float(r["newtons"])
        mm = n * per
        w = mm * px_per_mm
        ticks = "".join(
            "M%.1f %d V%d " % (110 + w * (k + 1) / n, y - 22, y + 8)
            for k in range(int(n) - 1))
        out += ('<text class="ks3-p4fig-rowlabel" x="40" y="%d">%s N</text>'
                '<rect class="ks3-p4fig-bar" x="110" y="%d" width="%.1f" '
                'height="30" rx="6"/>'
                '<path class="ks3-p4fig-tick" d="%s"/>'
                '<text class="ks3-p4fig-rowlabel" x="%.1f" y="%d">%s mm'
                '</text>'
                % (y, t(r["newtons"]), y - 22, w, ticks or "M0 0",
                   110 + w + 18, y, t(int(mm))))
        y += 70

    out += ('<text class="ks3-p4fig-note" x="40" y="310">%s</text>'
            '<text class="ks3-p4fig-note" x="40" y="344">%s</text>'
            % (t(fig.get("ratio_line", "")), t(fig.get("ratio_sums", ""))))
    out += ('<path class="ks3-p4fig-axis" d="M600 40 V340 H960"/>'
            '<path class="ks3-p4fig-line" d="M600 340 L840 148"/>'
            '<path class="ks3-p4fig-curve" d="M840 148 Q890 112 930 52"/>'
            '<path class="ks3-p4fig-limit" d="M840 148 V340"/>'
            '<text class="ks3-p4fig-axislabel" x="840" y="366" '
            'text-anchor="middle">%s</text>'
            '<text class="ks3-p4fig-axislabel" x="620" y="70">%s</text>'
            '<text class="ks3-p4fig-axislabel" x="880" y="330">%s</text>'
            % (t(fig.get("limit_label", "limit")),
               t(fig.get("y_label", "EXTENSION")),
               t(fig.get("x_label", "LOAD"))))
    return ('<svg class="ks3-p4fig ks3-p4fig-spring" viewBox="0 0 1000 400" '
            'role="img" aria-label="%s">%s</svg>'
            % (e(fig.get("aria_label", "")), out))


def _strip_svg(strip, act_id):
    """p4-06 `#s-stages` — one jump, four columns, one weight arrow each.

    ⚖️ **THE WEIGHT ARROW IS IDENTICAL IN ALL FOUR COLUMNS.** That is the
    fixed counterpart to the live bench above it, and it is the claim the
    lesson turns on. The drawer takes the weight length from the figure and
    uses the SAME number in every column; only the resistance fraction is per
    column, so a column cannot be authored with a different weight.
    """
    cols = strip.get("columns") or []
    if len(cols) != 4:
        raise ValueError(
            "stage-strip %r draws %d column(s); Design's is four stages."
            % (act_id, len(cols)))
    wlen = float(strip.get("weight_px") or 98)
    out = ""
    for i, c in enumerate(cols):
        px = 30 + i * 250
        cx = px + 85
        frac = float(c.get("resistance", 0))
        if frac < 0:
            raise ValueError(
                "stage-strip %r column %d has a negative resistance share."
                % (act_id, i + 1))
        out += ('<text class="ks3-p4fig-panellabel" x="%d" y="30">%s</text>'
                '<rect class="ks3-p4fig-load" x="%d" y="180" width="86" '
                'height="40" rx="8"/>' % (px, t(c.get("title", "")), px + 42))
        out += _arrow_v(cx, 220, wlen, down=True, head=30)
        if frac > 0:
            out += _arrow_v(cx, 180, wlen * frac, down=False, head=30)
        out += ('<text class="ks3-p4fig-verdict" x="%d" y="378">%s</text>'
                % (px, t(c.get("caption", ""))))
    return ('<svg class="ks3-p4fig ks3-p4fig-strip" viewBox="0 0 1000 400" '
            'role="img" aria-label="%s">%s</svg>'
            % (e(strip.get("aria_label", "")), out))


def r_p4_stage_strip(fig):
    """`figures[]` entry point for the four-stage strip."""
    return _strip_svg(fig, fig.get("id"))


def r_p4_resultant_beam(fig):
    return _resultant_beam(fig, fig.get("id"))


def r_p4_balance_beam(fig):
    return _balance_beam(fig, fig.get("id"))


def r_p4_spring_beam(fig):
    return _spring_beam_graph(fig, fig.get("id"))


# ═══ the CFIFA attempt · #s-formula, under the worked examples ═══════════

# ── the arithmetic gate on the five lines ────────────────────────────────
#
# ⊕ P5-12, 31 Aug 2026 — EVERY LINE OF THE SHAPE `a op b = c` IS EVALUATED
# AT BUILD TIME, and a false one fails the build.
#
# The bench printed "2.4 − 10 = 7.6" on the one step whose entire job is to
# be the arithmetic, in three reachable states, and nothing caught it: the
# renderer checks the letters, the labels and that a line is non-empty, and
# nothing anywhere checks that the sum is true. The 2026-08-28 physics
# audit found the same shape of defect in P2 by hand ("2000 x 180 = 360 kJ").
#
# ⚠️ THIS BELONGS IN `ks3_art.kit.r_cfifa_attempt`, where it would cover
# every unit and every worked example rather than these two. It is here,
# twice, because MRB-297's lanes hold `kit.py`. Lift it and delete both
# copies.
#
# A Fine-tune line may legitimately be prose ("Nothing needed converting"),
# so a line that does not MATCH the shape is passed over; only a line that
# claims a sum is held to it. The claim is judged at the precision it is
# written to, so a line that rounds ("1.2 / 0.35 = 3.4") passes and one
# that has the sign or the order wrong does not.

_ARITH_N = (r"[-+−]?\d[\d \u00a0\u2009,]*(?:\.\d+)?"
            r"(?:[eE][-+]?\d+)?")
_ARITH_U = r"(?:\s*[A-Za-z°%/µΩ²³]+)?"
_ARITH = _re.compile(
    r"^\s*(%s)%s\s*([\u00d7x*\u00f7/+\u2212-])\s*(%s)%s"
    r"\s*=\s*(%s)%s(?![\d.])"
    % (_ARITH_N, _ARITH_U, _ARITH_N, _ARITH_U, _ARITH_N, _ARITH_U))


def _arith_num(s):
    s = s.replace("\u2212", "-")
    for junk in ("\u00a0", "\u2009", " ", ","):
        s = s.replace(junk, "")
    return float(s)


def _check_arithmetic(act_id, where, line):
    """Fail the build on a line that states a sum and states it wrongly."""
    m = _ARITH.match(line or "")
    if not m:
        return
    a, op, b, c = (_arith_num(m.group(1)), m.group(2),
                   _arith_num(m.group(3)), _arith_num(m.group(4)))
    if op in ("\u00d7", "x", "*"):
        got = a * b
    elif op in ("\u00f7", "/"):
        if b == 0:
            return
        got = a / b
    elif op == "+":
        got = a + b
    else:
        got = a - b
    # Judged at the precision the line is WRITTEN to, so a line that
    # rounds ("1.2 / 0.35 = 3.4") and one that truncates ("1.20 / 0.84 =
    # 1.4285...") both pass, and a line with the sign or the order the
    # wrong way round does not: "2.4 - 10 = 7.6" is out by 15.2.
    tail = m.group(4).split(".")[1] if "." in m.group(4) else ""
    dp = len(tail.split("e")[0].split("E")[0])
    if abs(got - c) >= max(10.0 ** -dp, abs(c) * 1e-3):
        raise ValueError(
            "cfifa-attempt %r, %s, states %r. %s %s %s is %s, not %s. A "
            "model line a student writes their own working against has to "
            "be true as written."
            % (act_id, where, line.strip(), m.group(1), op, m.group(3),
               ("%%.%df" % dp) % got, m.group(4)))


def _check_attempt_arithmetic(a, act_id):
    """Every line of every question, with question 1's tokens resolved.

    Question 1 is live on the bench, so its lines carry `{token}`s; the
    payload's `rest` block is the state the page ships in and is the one
    set of values a build can see. Question 2 is fixed and is checked as
    written.
    """
    rest = a.get("rest") or {}
    for qi, q in enumerate(a.get("questions") or []):
        for si, st in enumerate(q.get("steps") or []):
            line = st.get("line") or ""
            if qi == 0:
                for k, v in rest.items():
                    line = line.replace("{%s}" % k, str(v))
            if "{" in line:
                continue          # a token no resting value supplies
            _check_arithmetic(
                act_id, "question %d step %d (%s)"
                % (qi + 1, si + 1, st.get("label")), line)


def r_p4_attempt(a, act_id):
    """⊕ P4's half of Design's `Cfifa`: the student's own five lines.

    The drawing is `ks3_art.kit.r_cfifa_attempt` — shared, because P4, P5
    and P6 all carry it and three copies of one block is how three copies
    drift. The FAMILY is P4's own, so the placement gates still see it as
    this unit's and `ks3_art.load()`'s one-family-one-module rule holds.

    ⚖️ **QUESTION 1 IS LIVE ON THE BENCH ABOVE IT.** Its head, its five
    lines and its closing sentence carry `{token}` placeholders that the
    bench's own wiring fills from the state it already computes, so the
    scaffold can never contradict the instrument the student is reading.
    Question 2 is fixed and is always the one that needs a conversion.
    """
    # ⊕ MRB-223 — ONE EYEBROW, NOT TWO. The `check` shell already prints
    # this activity's eyebrow in Design's `.ks3-blockhead`; the kit helper
    # printed it again. `None` tells the helper it is already on the page
    # (the P7 opt-out, applied here after it was measured on live pages).
    _check_attempt_arithmetic(a, act_id)
    html = r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p4cfa")
    # ⊕ MRB-297 · 1 Sep 2026 — THE READOUT WHILE THE PANEL IS BLOCKED.
    #
    # P4's Check button can now refuse — at zero load, and past this spring's
    # limit of proportionality — and while it refused, the readout beside the
    # disabled button went on saying "5 of 5 written", which is true of the
    # boxes and useless as an account of why nothing happens when you press.
    # `shared/ks3.js` deliberately invents no wording when the attribute is
    # absent (it says so, at its own read), so the sentence is authored here,
    # in the lesson, exactly as P8's is. Same key name, same mechanism, one
    # copy of the idea.
    q1 = (a.get("questions") or [{}])[0]
    if q1.get("blocked_progress"):
        html = html.replace(
            '<div class="ks3-cfa" data-p4cfa ',
            '<div class="ks3-cfa" data-p4cfa data-blocked-progress="%s" '
            % e(q1["blocked_progress"]), 1)
    return html


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. `ks3_art.check_placements` gate 2 fails a family
# registered and never placed and gate 3 fails one placed and never
# registered. Every family is P4's own — `ks3_art/core.py` is untouched.
#
# ⚠️ SHELL STEMS WERE CHECKED AGAINST THE WHOLE REGISTRY BEFORE BEING
# WRITTEN. None of `ks3-iboard-`, `ks3-rbench-`, `ks3-hrig-`, `ks3-grun-`,
# `ks3-dlane-`, `ks3-fall-`, `ks3-span-`, `ks3-splot-`, `ks3-fsort-` or
# `ks3-fband-` was taken.

# ⚠️ `p4-stage-strip` IS NOT HERE, AND THAT IS CORRECT. The four-stage strip
# is drawn from inside `force-band`'s own `strip` payload — it is part of
# that family's drawing, not a family a lesson can place by name. Registering
# it would claim a placeable family that nothing places, which is exactly
# what gate 2 exists to report. `r_p4_stage_strip` is kept as the `figures[]`
# entry point should a later lesson want the strip on its own.
ART = {
    'p4-resultant-beam': r_p4_resultant_beam,
    'p4-balance-beam':   r_p4_balance_beam,
    'p4-spring-beam':    r_p4_spring_beam,
}

KIND_SHELL = {
    'interaction-board': ("ks3-iboard-block",
                          ' data-instrument data-iboardblock '
                          'data-stage-done="0"'),
    'resultant-bench':   ("ks3-rbench-block",
                          ' data-instrument data-rbenchblock '
                          'data-stage-done="0"'),
    'support-rig':       ("ks3-hrig-block",
                          ' data-instrument data-hrigblock '
                          'data-stage-done="0"'),
    'gate-run':          ("ks3-grun-block",
                          ' data-instrument data-grunblock '
                          'data-stage-done="0"'),
    'drag-lane':         ("ks3-dlane-block",
                          ' data-instrument data-dlaneblock '
                          'data-stage-done="0"'),
    'fall-balance':      ("ks3-fall-block",
                          ' data-instrument data-fallblock '
                          'data-stage-done="0"'),
    'spanner-rig':       ("ks3-span-block",
                          ' data-instrument data-spanblock '
                          'data-stage-done="0"'),
    'spring-plot':       ("ks3-splot-block",
                          ' data-instrument data-splotblock '
                          'data-stage-done="0"'),
    'force-sorter':      ("ks3-fsort-block",
                          ' data-instrument data-fsortblock '
                          'data-stage-done="0"'),
    # ⚠️ THE BAND BLOCK DECLARES `data-stage-done="0"` LIKE EVERY OTHER
    # INSTRUMENT, AND THE FIRST DRAFT OF THIS FILE DID NOT. The reasoning
    # then was that a block with no control of its own should not claim to
    # know when it is finished. MRB-208's gate disagreed, in both directions
    # at once: `no instrument ships already ticked` failed because the
    # section carried no declaration at all, and `every rail stop can
    # actually reach done` failed because `doneByDom()` then fell through to
    # its heuristics and found nothing on a band of prose.
    #
    # The gate is right and the reasoning was wrong. The declaration is
    # AUTHORITATIVE IN BOTH DIRECTIONS — that is exactly what MRB-208 ruled
    # after b1-06 ticked on page load — so a section that opens at 0 and is
    # marked to 1 by the bench above it is the honest shape, and a section
    # with no attribute at all is the one making no statement.
    'force-band':        ("ks3-fband-block",
                          ' data-instrument data-fbandblock '
                          'data-stage-done="0"'),
    # The attempt panel is a DEMAND and it does declare its own completion:
    # the reveal is what `s.buildOpen` is on Design's page, and it is what
    # the `#s-formula` rail stop ticks on.
    'p4-attempt':        ("ks3-p4cfa-block",
                          ' data-instrument data-p4cfablock '
                          'data-stage-done="0"'),
}

KIND_FN = {
    'interaction-board': r_interaction_board,
    'resultant-bench':   r_resultant_bench,
    'support-rig':       r_support_rig,
    'gate-run':          r_gate_run,
    'drag-lane':         r_drag_lane,
    'fall-balance':      r_fall_balance,
    'spanner-rig':       r_spanner_rig,
    'spring-plot':       r_spring_plot,
    'force-sorter':      r_force_sorter,
    'force-band':        r_force_band,
    'p4-attempt':        r_p4_attempt,
}
