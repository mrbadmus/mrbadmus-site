"""ks3_art.p6 — P6 *Waves and sound*, the unit where a disturbance travels.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p6/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported.

── ⚖️ MRB-204 · TWO TRIANGLES AND TWO BARS IN NINE LESSONS ────────────────

    p6-01  no formula figure — OBW.01 is qualitative, and the wave equation
           is GCSE. It was not invented to have something to put in a
           triangle.
    p6-02  R = a + b  (in step) / a − b  (out of step)   a SUM   PART-WHOLE
    p6-03  no figure — a process
    p6-04  no figure — a contrast
    p6-05  N = f × t                                  a PRODUCT  TRIANGLE
    p6-06  d = v × t                                  a PRODUCT  TRIANGLE
    p6-07  s = d + d                                  a SUM      PART-WHOLE
    p6-08  no figure — a system lesson about ranges
    p6-09  no figure — see the unit note on FLAG 3

⚖️ **THE TWO BARS KEEP THEIR COVER BUTTONS AND THE TRIANGLES KEEP THEIRS.**
This is the split Design's flag 0a draws and it is not arbitrary: a
PART–WHOLE bar has buttons because covering a part asks a real question
(*what is left?*), and P5's stack and balance do not because covering a
layer of water asks nothing. `p6-02` and `p6-07` are part–whole bars, so
they take the engine's own `r_cover_bar`, buttons and all.

── ⚠️ `p6-01` NAMES NO FREQUENCY, DELIBERATELY (her FLAG 2) ───────────────

A wave has one, and the lesson is about the SHAPE of a wave rather than its
rate. Putting a hertz readout on the ripple tank would make `p6-01` a second
claimant of `SND.01`, which `p6-05` owns. The tank reports amplitude and
wavelength in millimetres and describes the paddle rate in words only.
`r_ripple_tank` refuses a payload carrying a frequency for that reason.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. Nothing here uses any of the four.

── ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY ─────────────────

`ks3_art.load()` asserts it since MRB-279, and it caught `ks3-srig-` in P4
on the first run. Checked again before these were written.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

import math

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ═══ shared P6 primitives ════════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P6 bench opens behind."""
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


def _slider(act_id, hook, spec, key=""):
    k = key or "v"
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


def _sibling(a):
    """`data-sibling` — the band stop this bench ticks, at its own count.

    Three P6 pages have one, and on all three Design's own `DONE` gives the
    band section the GATE alone while the bench needs the gate AND a control
    touched: `p6-04`'s `s-compare`, `p6-08`'s `s-chart`, `p6-09`'s `s-uses`.
    Same shape as P4's, same reason `mirrors` is not used.
    """
    # ⚠️ A TYPO HERE SHIPS A DEAD RAIL STOP, IN SILENCE, AND IT DID.
    # `p6-08` and `p6-09` were authored with `sibling` / `sibling_at`.
    # This function reads `band_anchor` / `band_at`, found neither,
    # returned "" — and the wrapper went out with no `data-sibling`, so
    # nothing ever ticked `#s-chart` or `#s-uses`. MRB-208's gate cannot
    # catch it: a band section carries `data-stage-done="0"`, which IS one
    # of the signals `doneByDom()` looks for, so the stop reads as
    # reachable and simply never becomes true. That is the dead-stop
    # failure the brief names, arriving by a route no gate watches.
    #
    # So a near-miss key is now an ERROR rather than a silent nothing. A
    # payload that means to name a sibling and misspells the key gets a
    # build failure with the right key in the message.
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


def _wave_path(x0, x1, mid, amp, lam, step=4):
    """A sampled sine, as ONE path string.

    ⚠️ NO `<sc-for>` INSIDE AN `<svg>`, and no per-sample element. Design's
    own note for the generator: repeated marks are built as one `d`, because
    a single attribute hole is the shape that is known to be safe.
    """
    d = ""
    x = float(x0)
    while x <= x1:
        y = mid - amp * math.sin((2 * math.pi * (x - x0)) / lam)
        d += ("%s%.1f %.1f" % (" L" if d else "M", x, y))
        x += step
    return d


# ═══ p6-01 · #s-parts · the wave anatomy figure ══════════════════════════

def r_wave_anatomy(a, act_id):
    """⊕ p6-01 `#s-parts` — a fixed reference wave with a four-way selector.

    ⚖️ **THE UNSELECTED STATE SHOWS THE WAVE WITH NOTHING MARKED, AND SAYS
    SO.** Design's own resting note gives the two measurements and marks
    neither. A figure that opened with everything labelled would answer the
    only question the block asks, which is *which of these four is which*.

    ⚖️ **CREST-TO-TROUGH IS NOT THE AMPLITUDE, AND THE FIGURE SAYS IT
    TWICE.** The trough note names 0.16 m and adds *"and that is not the
    amplitude"*; the amplitude note measures from the still level. That is
    `WAVE-03`, and it is the single most common misreading of a wave
    diagram.

    HOOKS: `data-wanat` (wrapper) · `data-wanat-tab` · `data-wanat-mark`
    (valued with the part id) · `data-wanat-note` · `data-wanat-alt`.
    """
    parts = a.get("parts") or []
    if len(parts) != 4:
        raise ValueError(
            "wave-anatomy %r declares %d part(s). Design's selector is four "
            "— crest, trough, amplitude, wavelength — and the set is the "
            "point: two are places on the wave and two are measurements of "
            "it." % (act_id, len(parts)))
    _unique(parts, act_id, "wave-anatomy", "part")
    for p in parts:
        if not p.get("note"):
            raise ValueError(
                "wave-anatomy %r part %r has no note." % (act_id, p.get("id")))
    if not a.get("resting_note"):
        raise ValueError(
            "wave-anatomy %r has no resting note. The unselected state shows "
            "the wave with nothing marked, and it still has to say what the "
            "wave is." % act_id)

    tabs = "".join(
        _seg("ks3-seg-btn ks3-wanat-tab", p["label"], data_wanat_tab=p["id"])
        for p in parts)

    amp, lam = 72.0, 360.0
    wave = _wave_path(50, 950, 190, amp, lam)
    # Design's own 1000×340 viewBox. The still level is dashed through the
    # middle and the direction arrow sits under it.
    marks = (
        '<g class="ks3-wanat-mark" data-wanat-mark="crest" hidden>'
        '<circle cx="140" cy="118" r="13"/><circle cx="500" cy="118" r="13"/>'
        '<circle cx="860" cy="118" r="13"/></g>'
        '<g class="ks3-wanat-mark" data-wanat-mark="trough" hidden>'
        '<circle cx="320" cy="262" r="13"/><circle cx="680" cy="262" r="13"/>'
        '</g>'
        '<g class="ks3-wanat-dim" data-wanat-mark="amp" hidden>'
        '<path d="M140 190 V118 M128 190 H152 M128 118 H152"/></g>'
        '<g class="ks3-wanat-dim" data-wanat-mark="wav" hidden>'
        '<path d="M140 78 H500 M140 66 V90 M500 66 V90"/></g>')

    notes = "".join(
        '<span data-wanat-note="%s" data-note="%s" hidden></span>'
        % (e(p["id"]), e(p["note"])) for p in parts)

    return ('<div class="ks3-wanat" data-wanat data-resting="%s" '
            'data-alt-base="%s">'
            '<div class="ks3-wanat-tabrow">%s</div>'
            '<div class="ks3-wanat-figwrap">'
            '<svg class="ks3-wanat-svg" viewBox="0 0 1000 340" role="img" '
            'aria-label="%s" data-wanat-alt>'
            '<path class="ks3-wanat-still" d="M40 190 H960"/>'
            '<path class="ks3-wanat-wave" d="%s"/>'
            '<path class="ks3-wanat-travel" d="M420 316 H580 M580 316 '
            'l-14 -9 M580 316 l-14 9"/>'
            '<text class="ks3-wanat-travellabel" x="410" y="322" '
            'text-anchor="end">%s</text>%s</svg></div>'
            '<p class="ks3-wanat-note" data-wanat-note-out>%s</p>%s</div>'
            # ⊕ MRB-223 — eyebrow and heading come from the `check` shell's own
            # head row; the figure printed them a second time (measured).
            % (e(a["resting_note"]), e(a.get("alt_base", "")), tabs,
               e(a.get("alt_base", "")), wave,
               t(a.get("travel_label", "the wave travels this way")), marks,
               t(a["resting_note"]), notes))


# ═══ p6-01 · #s-tank · the ripple tank ═══════════════════════════════════

def r_ripple_tank(a, act_id):
    """⊕ p6-01 `#s-tank` — one paddle, two things you can change about it.

    ⚖️ **BOTH AXES TO ONE SCALE, SO THE STEEPNESS IS DRAWABLE** (her flag 7).
    That makes the largest amplitude 35 px on a 1000-wide viewBox, which
    looks small — and it is deliberate: exaggerating the vertical would
    make the drawn geometry contradict the 1-in-7 label beside it.

    ⚖️ **THE FLOAT RISES AND FALLS AND STAYS PUT.** It is the whole hook,
    and the readout says both halves: how far it swings, and that it goes
    nowhere. `WAVE-01` is *the water travels along with the wave*, and the
    tile is what kills it.

    ⚠️ **NO FREQUENCY ANYWHERE** (her flag 2). A hertz readout here would
    make this lesson a second claimant of `SND.01`, which `p6-05` owns. The
    renderer refuses one.

    HOOKS: `data-rtank` (wrapper, `data-width-m`, `data-break-at`) ·
    `data-rtank-gate` · `data-rtank-gopt` · `data-rtank-body` ·
    `data-rtank-slider` (valued `amp` / `wav`) · `data-rtank-wave` ·
    `data-rtank-float` · `data-rtank-swing` · `data-rtank-out` ·
    `data-rtank-note`.
    """
    for banned in ("frequency", "hz", "freq"):
        if banned in {str(k).lower() for k in a}:
            raise ValueError(
                "ripple-tank %r carries a %r. This lesson names no frequency "
                "at all: a hertz readout here would make it a second "
                "claimant of KS3.P.SND.01, which p6-05 owns, and Design's "
                "flag 2 says so in terms." % (act_id, banned))

    amp = a.get("amp") or {}
    wav = a.get("wav") or {}
    for spec, name in ((amp, "amp"), (wav, "wav")):
        for k in ("min", "max", "step", "start", "label"):
            if k not in spec:
                raise ValueError(
                    "ripple-tank %r %s control has no %r."
                    % (act_id, name, k))

    branches = a.get("branches") or {}
    need = ("breaking", "ordinary", "swell")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "ripple-tank %r has no note for steepness band(s) %s. Every "
            "reachable state falls in one of the three."
            % (act_id, ", ".join(missing)))

    # Design's own 1000×520 viewBox.
    svg = (
        '<svg class="ks3-rtank-svg" viewBox="0 0 1000 520" role="img" '
        'aria-label="" data-rtank-alt>'
        '<rect class="ks3-rtank-tank" x="40" y="120" width="920" '
        'height="300" rx="6"/>'
        '<path class="ks3-rtank-still" d="M60 300 H940"/>'
        '<path class="ks3-rtank-wave" data-rtank-wave d="M0 0"/>'
        '<rect class="ks3-rtank-paddle" x="46" y="200" width="18" '
        'height="140" rx="4"/>'
        '<circle class="ks3-rtank-float" data-rtank-float cx="500" cy="300" '
        'r="15"/>'
        '<path class="ks3-rtank-swing" data-rtank-swing d="M0 0"/>'
        '<text class="ks3-rtank-widthlabel" x="500" y="470" '
        'text-anchor="middle">%s</text></svg>'
        % t(a.get("width_label", "1.00 m ACROSS")))

    fills = ('<span class="ks3-rtank-fill ks3-rtank-swing-label" '
             'data-rtank-fill="swing"></span>')

    branch_data = "".join(
        '<span data-rtank-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-rtank-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-rtank" data-rtank data-width-m="%s" '
            'data-break-at="%s" data-px-per-mm="%s">%s%s%s'
            '<div class="ks3-rtank-body" data-rtank-body hidden>'
            '<div class="ks3-rtank-controls">%s%s</div>'
            '<div class="ks3-rtank-figwrap">%s%s</div>%s'
            '<p class="ks3-rtank-note" data-rtank-note></p>%s</div></div>'
            % (e(a.get("width_m", 1.0)), e(a.get("break_at", 0.143)),
               e(a.get("px_per_mm", 0.88)),
               _head("rtank", a), lead,
               _gate(act_id, "ripple-tank", a.get("gate") or {}, "rtank"),
               _slider(act_id, "rtank", amp, "amp"),
               _slider(act_id, "rtank", wav, "wav"),
               svg, fills, _tiles("rtank", a.get("readouts") or []),
               branch_data))


# ═══ p6-02 · #s-meet · two wave trains in one channel ════════════════════

def r_superposition_lanes(a, act_id):
    """⊕ p6-02 `#s-meet` — set two waves going, read the third.

    ⚖️ **THREE TRACES ON ONE PX-PER-MILLIMETRE SCALE.** The claim is that
    the bottom trace is the SUM of the two above it, and a scale that
    differed between lanes would make that unreadable.

    ⚖️ **ZERO DRAWS A FLAT LINE, NOT NOTHING.** A wave of 0 mm amplitude is
    a real state — one paddle switched off — and it is different from the
    lane being absent. Design draws the flat trace, and the note for that
    state says in terms that *"this is not cancelling — cancelling needs two
    waves, and there are none"*.

    ⚖️ **FIVE BRANCHES, KEYED TO WHAT THE TWO WAVES DO** — nothing running,
    one wave only, adding, cancelling exactly, partly cancelling. The exact
    cancel is its own branch because it is the state the misconception is
    about: both waves are still there, and both leave the overlap unchanged.

    HOOKS: `data-slane` (wrapper, `data-px-per-mm`) · `data-slane-gate` ·
    `data-slane-gopt` · `data-slane-body` · `data-slane-slider` (valued
    `a` / `b`) · `data-slane-step` · `data-slane-trace` (valued `a`/`b`/`r`)
    · `data-slane-out` · `data-slane-note`.
    """
    lanes = a.get("lanes") or []
    if len(lanes) != 2:
        raise ValueError(
            "superposition-lanes %r declares %d input wave(s); the lesson is "
            "two meeting in one channel." % (act_id, len(lanes)))
    branches = a.get("branches") or {}
    need = ("none", "one_only", "adding", "cancels_exactly", "partly")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "superposition-lanes %r has no note for state(s) %s. The exact "
            "cancel is its own branch because it is the state `WAVE-05` is "
            "about." % (act_id, ", ".join(missing)))

    rows = "".join(_slider(act_id, "slane", L, L["id"]) for L in lanes)
    steps = "".join(
        _seg("ks3-seg-btn ks3-slane-step", x["label"],
             pressed=(x["in_step"] == a.get("start_in_step", True)),
             data_slane_step=("1" if x["in_step"] else "0"))
        for x in (a.get("phases") or []))

    # Design's own 1000×520 viewBox — three stacked traces on one scale.
    lanes_svg = ""
    for key, mid, label in (("a", 80, a.get("label_a", "WAVE A")),
                            ("b", 210, a.get("label_b", "WAVE B")),
                            ("r", 390, a.get("label_r", "WHERE THEY MEET"))):
        lanes_svg += (
            '<path class="ks3-slane-still" d="M120 %d H960"/>'
            '<text class="ks3-slane-lanelabel" x="110" y="%d" '
            'text-anchor="end">%s</text>'
            '<path class="ks3-slane-trace ks3-slane-trace-%s" '
            'data-slane-trace="%s" d="M0 0"/>'
            % (mid, mid + 5, t(label), key, key))

    svg = ('<svg class="ks3-slane-svg" viewBox="0 0 1000 520" role="img" '
           'aria-label="" data-slane-alt>%s</svg>' % lanes_svg)

    branch_data = "".join(
        '<span data-slane-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-slane-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-slane" data-slane data-px-per-mm="%s" '
            'data-start-in-step="%s">%s%s%s'
            '<div class="ks3-slane-body" data-slane-body hidden>'
            '<div class="ks3-slane-controls">%s'
            '<div class="ks3-slane-picker"><p class="ks3-slane-pickerlabel">'
            '%s</p><div class="ks3-slane-tabrow">%s</div></div></div>'
            '<div class="ks3-slane-figwrap">%s</div>%s'
            '<p class="ks3-slane-note" data-slane-note></p>%s</div></div>'
            % (e(a.get("px_per_mm", 2.5)),
               "1" if a.get("start_in_step", True) else "0",
               _head("slane", a), lead,
               _gate(act_id, "superposition-lanes", a.get("gate") or {},
                     "slane"),
               rows, t(a.get("phase_label", "How B arrives")), steps,
               svg, _tiles("slane", a.get("readouts") or []), branch_data))


# ═══ p6-03 · #s-chain · source, air, detector ════════════════════════════

def r_vibration_chain(a, act_id):
    """⊕ p6-03 `#s-chain` — change what vibrates; the chain does not change.

    ⚖️ **FIVE SOURCES × TWO DETECTORS, AND ALL TEN STATES CARRY A NOTE.**
    Design authors a note per source and a clause per detector and combines
    them, which is what makes ten states from seven strings. The renderer
    requires both halves.

    ⚖️ **EVERY SOURCE IS DRAWN FROM ITS OWN PATH PAIR** — the shape at rest
    and the dashed extremes it swings between — so a student can see WHAT
    is moving before reading which. The vocal folds and the drum skin do not
    look alike, and they should not.

    ⚠️ **THE MOVEMENT IS GREATLY EXAGGERATED AND THE PAGE SAYS SO.** A
    tuning fork's prongs move about half a millimetre. Drawn to scale the
    figure would be a straight line.

    HOOKS: `data-vchain` (wrapper) · `data-vchain-gate` ·
    `data-vchain-gopt` · `data-vchain-body` · `data-vchain-source` ·
    `data-vchain-det` · `data-vchain-shape` · `data-vchain-ghost` ·
    `data-vchain-arrow` · `data-vchain-out` · `data-vchain-note`.
    """
    sources = a.get("sources") or []
    dets = a.get("detectors") or []
    if len(sources) < 3 or len(dets) < 2:
        raise ValueError(
            "vibration-chain %r declares %d source(s) and %d detector(s). "
            "The claim is that the chain is the same whatever sits at either "
            "end, and one of each proves nothing."
            % (act_id, len(sources), len(dets)))
    _unique(sources, act_id, "vibration-chain", "source")
    _unique(dets, act_id, "vibration-chain", "detector")
    for s in sources:
        for f in ("moves", "driven", "amp", "freq", "note", "path", "ghost",
                  "arrow", "caption"):
            if not s.get(f):
                raise ValueError(
                    "vibration-chain %r source %r has no %r."
                    % (act_id, s.get("id"), f))
    for d in dets:
        for f in ("out", "note", "caption"):
            if not d.get(f):
                raise ValueError(
                    "vibration-chain %r detector %r has no %r."
                    % (act_id, d.get("id"), f))

    src_tabs = "".join(
        _seg("ks3-seg-btn ks3-vchain-source", s["label"],
             pressed=(i == int(a.get("start_source", 0))),
             data_vchain_source=s["id"], data_moves=s["moves"],
             data_driven=s["driven"], data_amp=s["amp"], data_freq=s["freq"],
             data_note=s["note"], data_path=s["path"], data_ghost=s["ghost"],
             data_arrow=s["arrow"], data_caption=s["caption"])
        for i, s in enumerate(sources))
    det_tabs = "".join(
        _seg("ks3-seg-btn ks3-vchain-det", d["label"],
             pressed=(i == int(a.get("start_det", 0))),
             data_vchain_det=d["id"], data_out=d["out"], data_note=d["note"],
             data_caption=d["caption"])
        for i, d in enumerate(dets))

    # Design's own 1000×340 viewBox: source at the left, columns of air in
    # the middle bunched and spread, detector diaphragm at the right.
    svg = (
        '<svg class="ks3-vchain-svg" viewBox="0 0 1000 340" role="img" '
        'aria-label="" data-vchain-alt>'
        '<path class="ks3-vchain-ghost" data-vchain-ghost d="M0 0"/>'
        '<path class="ks3-vchain-shape" data-vchain-shape d="M0 0"/>'
        '<path class="ks3-vchain-arrow" data-vchain-arrow d="M0 0"/>'
        '<path class="ks3-vchain-air" data-vchain-air d="M0 0"/>'
        '<rect class="ks3-vchain-diaphragm" x="880" y="110" width="14" '
        'height="120" rx="6"/>'
        '<path class="ks3-vchain-travel" d="M330 300 H820 M820 300 '
        'l-16 -10 M820 300 l-16 10"/>'
        '<text class="ks3-vchain-travellabel" x="575" y="288" '
        'text-anchor="middle">%s</text></svg>'
        % t(a.get("travel_label", "THE DISTURBANCE TRAVELS THIS WAY")))

    fills = "".join(
        '<span class="ks3-vchain-fill ks3-vchain-%s" '
        'data-vchain-fill="%s"></span>' % (k, k) for k in ("src", "det"))

    lead = ('<p class="ks3-vchain-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-vchain" data-vchain data-start-source="%s" '
            'data-start-det="%s">%s%s%s'
            '<div class="ks3-vchain-body" data-vchain-body hidden>'
            '<div class="ks3-vchain-controls">'
            '<div class="ks3-vchain-picker">'
            '<p class="ks3-vchain-pickerlabel">%s</p>'
            '<div class="ks3-vchain-tabrow">%s</div></div>'
            '<div class="ks3-vchain-picker">'
            '<p class="ks3-vchain-pickerlabel">%s</p>'
            '<div class="ks3-vchain-tabrow">%s</div></div></div>'
            '<div class="ks3-vchain-figwrap">%s%s</div>%s'
            '<p class="ks3-vchain-note" data-vchain-note></p></div></div>'
            % (e(a.get("start_source", 0)), e(a.get("start_det", 0)),
               _head("vchain", a), lead,
               _gate(act_id, "vibration-chain", a.get("gate") or {},
                     "vchain"),
               t(a.get("source_label", "What is vibrating")), src_tabs,
               t(a.get("det_label", "What is listening")), det_tabs,
               svg, fills, _tiles("vchain", a.get("readouts") or [])))


# ═══ p6-04 · #s-slinky · one slinky, driven two ways ═════════════════════

def r_slinky_dual(a, act_id):
    """⊕ p6-04 `#s-slinky` — drive it two ways, watch one coil.

    ⚖️ **THE SAME 60 mm OF MOVEMENT AND THE SAME 300 mm REPEAT IN BOTH
    DRIVES.** That is the whole contrast: nothing about the size of the
    disturbance changes, only its DIRECTION relative to travel. A bench
    where the two drives differed in amplitude would let a student explain
    the difference by the wrong variable.

    ⚖️ **SIX BRANCHES, THREE PER DRIVE, KEYED TO THE REGION THE MARKED COIL
    SITS IN.** Crest, trough and crossing for transverse; compression,
    rarefaction and between for longitudinal. The `mid` states are the
    load-bearing ones — a coil at its rest position is still in a
    transverse wave, because what makes it transverse is the direction it
    TRAVELS, not where it happens to be at one instant.

    ⚠️ **THE LONGITUDINAL DRIVE DRAWS COIL TICKS AT VARYING SPACING, NEVER A
    SINE.** Drawing sound as a wavy line is `WAVE-13`, and a bench that drew
    the longitudinal case as a curve would be committing it.

    HOOKS: `data-slink` (wrapper, `data-amp-mm`, `data-lam-mm`) ·
    `data-slink-gate` · `data-slink-gopt` · `data-slink-body` ·
    `data-slink-drive` · `data-slink-mark` · `data-slink-coils` ·
    `data-slink-marked` · `data-slink-rest` · `data-slink-arrow` ·
    `data-slink-out` · `data-slink-note`.
    """
    drives = a.get("drives") or []
    if len(drives) != 2:
        raise ValueError(
            "slinky-dual %r declares %d drive(s). The lesson is one slinky "
            "driven TWO ways." % (act_id, len(drives)))
    branches = a.get("branches") or {}
    need = ("trans-crest", "trans-trough", "trans-mid",
            "long-comp", "long-rare", "long-mid")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "slinky-dual %r has no note for region(s) %s. The `mid` states "
            "are not filler: a coil at its rest position is still in a "
            "transverse wave, and saying so is the point."
            % (act_id, ", ".join(missing)))

    mark = a.get("mark") or {}
    for k in ("min", "max", "step", "start", "label"):
        if k not in mark:
            raise ValueError("slinky-dual %r mark control has no %r."
                             % (act_id, k))

    drive_tabs = "".join(
        _seg("ks3-seg-btn ks3-slink-drive", d["label"],
             pressed=(d["id"] == a.get("start_drive", drives[0]["id"])),
             data_slink_drive=d["id"], data_kind=d["kind"],
             data_caption=d["caption"])
        for d in drives)

    # Design's own 1000×360 viewBox.
    svg = (
        '<svg class="ks3-slink-svg" viewBox="0 0 1000 360" role="img" '
        'aria-label="" data-slink-alt>'
        '<path class="ks3-slink-axis" d="M60 180 H940"/>'
        '<path class="ks3-slink-coils" data-slink-coils d="M0 0"/>'
        '<path class="ks3-slink-rest" data-slink-rest d="M0 0"/>'
        '<circle class="ks3-slink-marked" data-slink-marked cx="500" '
        'cy="180" r="13"/>'
        '<path class="ks3-slink-arrow" data-slink-arrow d="M0 0"/>'
        '<path class="ks3-slink-travel" d="M400 330 H600 M600 330 '
        'l-16 -10 M600 330 l-16 10"/>'
        '<text class="ks3-slink-travellabel" x="390" y="336" '
        'text-anchor="end">%s</text></svg>'
        % t(a.get("travel_label", "the wave travels this way")))

    fills = ('<span class="ks3-slink-fill ks3-slink-caption" '
             'data-slink-fill="caption"></span>')

    branch_data = "".join(
        '<span data-slink-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-slink-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-slink" data-slink data-amp-mm="%s" '
            'data-lam-mm="%s" data-length-mm="%s" data-start-drive="%s"%s>'
            '%s%s%s'
            '<div class="ks3-slink-body" data-slink-body hidden>'
            '<div class="ks3-slink-controls">'
            '<div class="ks3-slink-picker"><p class="ks3-slink-pickerlabel">'
            '%s</p><div class="ks3-slink-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-slink-figwrap">%s%s</div>%s'
            '<p class="ks3-slink-note" data-slink-note></p>%s</div></div>'
            % (e(a.get("amp_mm", 60)), e(a.get("lam_mm", 300)),
               e(a.get("length_mm", 1200)),
               e(a.get("start_drive", drives[0]["id"])), _sibling(a),
               _head("slink", a), lead,
               _gate(act_id, "slinky-dual", a.get("gate") or {}, "slink"),
               t(a.get("drive_label", "How the end is driven")), drive_tabs,
               _slider(act_id, "slink", mark, "mark"),
               svg, fills, _tiles("slink", a.get("readouts") or []),
               branch_data))


# ═══ p6-05 · #s-signal · the signal generator and the oscilloscope ═══════

def r_scope_trace(a, act_id):
    """⊕ p6-05 `#s-signal` — two dials, two different things happen.

    ⚖️ **THE SECOND SENTENCE IS ALWAYS PRESENT AND IT NAMES THE OTHER DIAL'S
    INDEPENDENCE WITH LIVE FIGURES.** Design's own rule for this bench: every
    branch ends by saying what moving the OTHER dial would do, with the
    numbers. `WAVE-17` is *a loud note is a high note*, and a bench that let
    a student change one dial and read one number would never confront it.

    ⚖️ **THE WINDOW IS A FIXED DURATION AND THE COUNT IS DERIVED.** 20 ms,
    always, so the trace crowds as the frequency rises and the count in the
    readout is `f × 0.02` rather than an authored number. That is what makes
    the hertz mean something on the page.

    HOOKS: `data-scope` (wrapper, `data-window-ms`) · `data-scope-gate` ·
    `data-scope-gopt` · `data-scope-body` · `data-scope-slider` (valued
    `f` / `a`) · `data-scope-trace` · `data-scope-bracket` ·
    `data-scope-out` · `data-scope-note`.
    """
    freq = a.get("freq") or {}
    amp = a.get("amp") or {}
    for spec, name in ((freq, "freq"), (amp, "amp")):
        for k in ("min", "max", "step", "start", "label"):
            if k not in spec:
                raise ValueError("scope-trace %r %s has no %r."
                                 % (act_id, name, k))
    window = float(a.get("window_ms") or 0)
    if window <= 0:
        raise ValueError(
            "scope-trace %r has no window duration. The count of complete "
            "vibrations on screen is derived from it, and without one the "
            "hertz on the readout would mean nothing on the page." % act_id)

    branches = a.get("branches") or {}
    need = ("low", "middle", "high")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "scope-trace %r has no note for pitch band(s) %s."
            % (act_id, ", ".join(missing)))
    if not a.get("independence"):
        raise ValueError(
            "scope-trace %r has no `independence` sentence. Every state on "
            "this bench ends by naming what the OTHER dial would do, with "
            "live figures — without it a student can change one dial, read "
            "one number, and never meet `a loud note is a high note`."
            % act_id)

    # Design's own 1000×420 viewBox — one scope window, both axes to scale.
    svg = (
        '<svg class="ks3-scope-svg" viewBox="0 0 1000 420" role="img" '
        'aria-label="" data-scope-alt>'
        '<rect class="ks3-scope-screen" x="60" y="40" width="880" '
        'height="300" rx="8"/>'
        '<path class="ks3-scope-zero" d="M70 190 H930"/>'
        '<path class="ks3-scope-ticks" data-scope-ticks d="M0 0"/>'
        '<path class="ks3-scope-trace" data-scope-trace d="M0 0"/>'
        '<path class="ks3-scope-bracket" data-scope-bracket d="M0 0"/>'
        '<text class="ks3-scope-axislabel" x="500" y="384" '
        'text-anchor="middle">%s</text></svg>'
        % t(a.get("axis_label", "TIME — ONE WINDOW OF 20 ms")))

    fills = ('<span class="ks3-scope-fill ks3-scope-amp" '
             'data-scope-fill="amp"></span>')

    branch_data = "".join(
        '<span data-scope-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-scope-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-scope" data-scope data-window-ms="%s" '
            'data-independence="%s" data-bands="%s">%s%s%s'
            '<div class="ks3-scope-body" data-scope-body hidden>'
            '<div class="ks3-scope-controls">%s%s</div>'
            '<div class="ks3-scope-figwrap">%s%s</div>%s'
            '<p class="ks3-scope-note" data-scope-note></p>%s</div></div>'
            % (e(window), e(a["independence"]),
               e("%s|%s" % (a.get("low_below", 200),
                            a.get("high_above", 600))),
               _head("scope", a), lead,
               _gate(act_id, "scope-trace", a.get("gate") or {}, "scope"),
               _slider(act_id, "scope", freq, "f"),
               _slider(act_id, "scope", amp, "a"),
               svg, fills, _tiles("scope", a.get("readouts") or []),
               branch_data))


# ═══ p6-06 · #s-range · striker and microphone across a gap ══════════════

def r_medium_range(a, act_id):
    """⊕ p6-06 `#s-range` — same bang, change what is in the way.

    ⚖️ **THE VACUUM REFUSES TO REPORT A SPEED AND PRINTS "IT NEVER
    ARRIVES".** Not a very large time, not a very small number: NO sound, at
    any distance, for any length of time. A bench that printed a slow speed
    for a vacuum would teach that sound crosses it faintly, which is
    `WAVE-21` exactly. The renderer requires a zero-speed medium in the deck
    and refuses to compute a time for it.

    ⚖️ **EVERY MATERIAL COMPARES ITSELF WITH AIR AT THE SAME GAP**, and the
    vacuum branch names the air time too — so the state that reports nothing
    still says what the same gap WOULD give if it had particles in it.

    ⚖️ **THE PARTICLES ARE DRAWN AT THE SPACING THE SPEED FOLLOWS FROM.**
    Scattered dots for a gas, close rows for a liquid, a linked lattice for
    a solid. The drawing is the explanation, not decoration, and the note
    for each material names the same arrangement in words.

    HOOKS: `data-mrange` (wrapper) · `data-mrange-gate` ·
    `data-mrange-gopt` · `data-mrange-body` · `data-mrange-mat` (carrying
    `data-v`) · `data-mrange-slider` · `data-mrange-particles` ·
    `data-mrange-links` · `data-mrange-out` · `data-mrange-note`.
    """
    mats = a.get("materials") or []
    if len(mats) < 4:
        raise ValueError(
            "medium-range %r declares %d material(s). The pattern being "
            "taught runs gas → liquid → solid, and needs one of each plus "
            "the vacuum." % (act_id, len(mats)))
    _unique(mats, act_id, "medium-range", "material")
    vac = [m for m in mats if float(m.get("v") or 0) == 0]
    if not vac:
        raise ValueError(
            "medium-range %r has no vacuum in the deck. It is the state the "
            "lesson is named after, and the one the hook is about." % act_id)
    for m in mats:
        for f in ("note", "state", "caption", "pattern"):
            if not m.get(f):
                raise ValueError(
                    "medium-range %r material %r has no %r."
                    % (act_id, m.get("id"), f))
        if m.get("pattern") not in ("gas", "liquid", "lattice", "none"):
            raise ValueError(
                "medium-range %r material %r asks for particle pattern %r. "
                "The four drawn are gas, liquid, lattice and none — and the "
                "pattern IS the explanation for the speed."
                % (act_id, m.get("id"), m.get("pattern")))

    ordered = [float(m["v"]) for m in mats if float(m["v"]) > 0]
    if ordered != sorted(ordered):
        raise ValueError(
            "medium-range %r lists its materials out of speed order. Design "
            "draws them slowest first because the pattern — closer and more "
            "strongly linked passes the shove on sooner — is what the tab "
            "row itself teaches." % act_id)

    dist = a.get("dist") or {}
    for k in ("min", "max", "step", "start", "label"):
        if k not in dist:
            raise ValueError("medium-range %r dist has no %r." % (act_id, k))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-mrange-mat", m["label"],
             pressed=(i == int(a.get("start_mat", 0))),
             data_mrange_mat=m["id"], data_v=m["v"], data_note=m["note"],
             data_state=m["state"], data_caption=m["caption"],
             data_pattern=m["pattern"], data_name=m["label"])
        for i, m in enumerate(mats))

    # Design's own 1000×340 viewBox.
    svg = (
        '<svg class="ks3-mrange-svg" viewBox="0 0 1000 340" role="img" '
        'aria-label="" data-mrange-alt>'
        '<rect class="ks3-mrange-gapbox" x="150" y="80" width="740" '
        'height="140" rx="6"/>'
        '<path class="ks3-mrange-links" data-mrange-links d="M0 0"/>'
        '<path class="ks3-mrange-particles" data-mrange-particles d="M0 0"/>'
        '<rect class="ks3-mrange-striker" x="70" y="110" width="60" '
        'height="80" rx="8"/>'
        '<rect class="ks3-mrange-mic" x="910" y="110" width="24" '
        'height="80" rx="6"/>'
        '<path class="ks3-mrange-dim" d="M150 268 H890 M150 256 V280 '
        'M890 256 V280"/></svg>')

    fills = "".join(
        '<span class="ks3-mrange-fill ks3-mrange-%s" '
        'data-mrange-fill="%s"></span>' % (k, k) for k in ("gap", "caption"))

    lead = ('<p class="ks3-mrange-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-mrange" data-mrange data-air-v="%s" '
            'data-start-mat="%s">%s%s%s'
            '<div class="ks3-mrange-body" data-mrange-body hidden>'
            '<div class="ks3-mrange-controls">'
            '<div class="ks3-mrange-picker">'
            '<p class="ks3-mrange-pickerlabel">%s</p>'
            '<div class="ks3-mrange-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-mrange-figwrap">%s%s</div>%s'
            '<p class="ks3-mrange-note" data-mrange-note></p></div></div>'
            % (e(a.get("air_v", 340)), e(a.get("start_mat", 0)),
               _head("mrange", a), lead,
               _gate(act_id, "medium-range", a.get("gate") or {}, "mrange"),
               t(a.get("mat_label", "What fills the gap")), tabs,
               _slider(act_id, "mrange", dist, "dist"),
               svg, fills, _tiles("mrange", a.get("readouts") or [])))


# ═══ p6-07 · #s-cliff · shout at a surface ═══════════════════════════════

def r_echo_range(a, act_id):
    """⊕ p6-07 `#s-cliff` — move the wall, change the wall.

    ⚖️ **TWO CONDITIONS, AND THE VERDICT NAMES WHICH ONE FAILED.** An echo
    needs enough sound back AND enough time. Design's three branches are
    keyed to exactly that: too little returns, too close in time, or both
    met. A bench with one verdict word would let a student in a carpeted
    bedroom conclude that the room is too small, and in a sports hall that
    the walls are too soft.

    ⚖️ **THE RETURNING ARROW'S STROKE WIDTH IS THE FRACTION REFLECTED**, and
    it goes DASHED below the audible threshold. Two channels, not one, so
    the drawing is not carrying the verdict on thickness alone.

    ⚠️ **THE TWO THRESHOLDS ARE APPROXIMATE AND THE PAGE SAYS SO.** About a
    tenth of a second, and roughly 17 m. Both are fixed here so that the
    states can be reached; the foot line declares them.

    HOOKS: `data-echo` (wrapper, `data-v`, `data-min-frac`,
    `data-min-time`) · `data-echo-gate` · `data-echo-gopt` ·
    `data-echo-body` · `data-echo-slider` · `data-echo-surf` (carrying
    `data-frac`) · `data-echo-out` · `data-echo-back` · `data-echo-note`.
    """
    surfs = a.get("surfaces") or []
    if len(surfs) < 4:
        raise ValueError(
            "echo-range %r declares %d surface(s). The deck has to hold "
            "both good reflectors and good absorbers, and more than one of "
            "each." % (act_id, len(surfs)))
    _unique(surfs, act_id, "echo-range", "surface")

    v = float(a.get("v") or 0)
    min_frac = float(a.get("min_frac") or 0)
    min_time = float(a.get("min_time") or 0)
    if v <= 0 or min_frac <= 0 or min_time <= 0:
        raise ValueError(
            "echo-range %r needs a speed of sound, a minimum returning "
            "fraction and a minimum delay. All three are what the verdict "
            "is computed from." % act_id)

    loud = [s for s in surfs if float(s["frac"]) >= min_frac]
    quiet = [s for s in surfs if float(s["frac"]) < min_frac]
    if not loud or not quiet:
        raise ValueError(
            "echo-range %r has %d surface(s) above the audible fraction and "
            "%d below. Both verdicts have to be reachable from the tab row "
            "alone, or one of the two conditions is never met."
            % (act_id, len(loud), len(quiet)))

    dist = a.get("dist") or {}
    for k in ("min", "max", "step", "start", "label"):
        if k not in dist:
            raise ValueError("echo-range %r dist has no %r." % (act_id, k))
    if float(dist["min"]) * 2 / v >= min_time:
        raise ValueError(
            "echo-range %r: even the shortest distance clears the %s s "
            "threshold, so `too close in time` is a dead verdict."
            % (act_id, min_time))

    branches = a.get("branches") or {}
    need = ("too_quiet", "too_close", "heard")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "echo-range %r has no note for verdict(s) %s."
            % (act_id, ", ".join(missing)))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-echo-surf", s["label"],
             pressed=(i == int(a.get("start_surf", 0))),
             data_echo_surf=s["id"], data_frac=s["frac"],
             data_caption=s["caption"], data_use=s.get("use", ""),
             data_name=s["label"])
        for i, s in enumerate(surfs))

    # Design's own 1000×360 viewBox.
    svg = (
        '<svg class="ks3-echo-svg" viewBox="0 0 1000 360" role="img" '
        'aria-label="" data-echo-alt>'
        '<path class="ks3-echo-ground" d="M60 300 H960"/>'
        '<circle class="ks3-echo-person" cx="150" cy="250" r="26"/>'
        '<rect class="ks3-echo-wall" data-echo-wall x="0" y="90" width="26" '
        'height="210" rx="4"/>'
        '<path class="ks3-echo-out" data-echo-out-arrow d="M0 0"/>'
        '<path class="ks3-echo-back" data-echo-back d="M0 0"/>'
        '<path class="ks3-echo-dim" data-echo-dim d="M0 0"/></svg>')

    fills = "".join(
        '<span class="ks3-echo-fill ks3-echo-%s" data-echo-fill="%s">'
        '</span>' % (k, k) for k in ("dist", "back", "caption"))

    branch_data = "".join(
        '<span data-echo-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-echo-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-echo" data-echo data-v="%s" data-min-frac="%s" '
            'data-min-time="%s" data-start-surf="%s">%s%s%s'
            '<div class="ks3-echo-body" data-echo-body hidden>'
            '<div class="ks3-echo-controls">%s'
            '<div class="ks3-echo-picker"><p class="ks3-echo-pickerlabel">%s'
            '</p><div class="ks3-echo-tabrow">%s</div></div></div>'
            '<div class="ks3-echo-figwrap">%s%s</div>%s'
            '<p class="ks3-echo-note" data-echo-note></p>%s</div></div>'
            % (e(v), e(min_frac), e(min_time), e(a.get("start_surf", 0)),
               _head("echo", a), lead,
               _gate(act_id, "echo-range", a.get("gate") or {}, "echo"),
               _slider(act_id, "echo", dist, "dist"),
               t(a.get("surf_label", "What the surface is")), tabs,
               svg, fills, _tiles("echo", a.get("readouts") or []),
               branch_data))


# ═══ p6-08 · #s-range · one tone, one listener ═══════════════════════════

def r_log_range(a, act_id):
    """⊕ p6-08 `#s-range` — sound one tone, ask one pair of ears.

    ⚖️ **A DECADE AXIS, AND THE PAGE SAYS SO ON ITS FACE.** The ranges here
    run from 1 Hz to 110 000 Hz — five powers of ten. A linear bar cannot
    carry that: the entire human range would be the first fifth of it and
    every animal band would pile up at one end. Design's own note says *"the
    family exists because a linear bar cannot carry these ranges"*, and the
    lesson's lead tells the student the axis multiplies by ten at every
    mark. `r_log_range` refuses a payload whose span is under three decades,
    because below that a decade axis is a complication with nothing to buy.

    ⚖️ **EVERY BRANCH NAMES A SECOND SPECIES AT THE SAME FREQUENCY.** That is
    what turns "the dog can hear it" into "and you cannot" — the comparison
    is the lesson, not the reading.

    ⚖️ **THE VERDICT IS A WORD, NOT A COLOUR.** Inside, below, above. Hue is
    never the only channel.

    HOOKS: `data-lrange` (wrapper, `data-decades`, `data-f-min`) ·
    `data-lrange-gate` · `data-lrange-gopt` · `data-lrange-body` ·
    `data-lrange-who` (carrying `data-lo`, `data-hi`) ·
    `data-lrange-slider` · `data-lrange-band` · `data-lrange-marker` ·
    `data-lrange-out` · `data-lrange-note`.
    """
    who = a.get("listeners") or []
    if len(who) < 4:
        raise ValueError(
            "log-range %r declares %d listener(s). The comparison needs "
            "enough of them that the human range is one case among several "
            "rather than the reference everything is measured against."
            % (act_id, len(who)))
    _unique(who, act_id, "log-range", "listener")
    for w in who:
        for f in ("lo", "hi", "note"):
            if w.get(f) in (None, ""):
                raise ValueError(
                    "log-range %r listener %r has no %r."
                    % (act_id, w.get("id"), f))
        if float(w["lo"]) >= float(w["hi"]):
            raise ValueError(
                "log-range %r listener %r runs from %s to %s."
                % (act_id, w.get("id"), w["lo"], w["hi"]))

    lo = min(float(w["lo"]) for w in who)
    hi = max(float(w["hi"]) for w in who)
    decades = math.log10(hi / lo)
    if decades < 3:
        raise ValueError(
            "log-range %r spans %.1f decade(s). Below about three a decade "
            "axis is a complication that buys nothing, and a linear bar "
            "would read more honestly." % (act_id, decades))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-lrange-who", w["label"],
             pressed=(i == int(a.get("start_who", 0))),
             data_lrange_who=w["id"], data_lo=w["lo"], data_hi=w["hi"],
             data_note=w["note"], data_name=w["label"])
        for i, w in enumerate(who))

    freq = a.get("freq") or {}
    for k in ("min", "max", "step", "start", "label"):
        if k not in freq:
            raise ValueError("log-range %r freq has no %r." % (act_id, k))

    # Design's own 1000×300 viewBox. The decade labels are LITERAL text —
    # they never change — and only the band and the marker move.
    ticks = ""
    for d in range(0, 6):
        x = 90 + d * 164
        ticks += ('<path class="ks3-lrange-tick" d="M%d 190 V210"/>'
                  '<text class="ks3-lrange-ticklabel" x="%d" y="238" '
                  'text-anchor="middle">%s</text>'
                  % (x, x, t(["1", "10", "100", "1 000", "10 000",
                              "100 000"][d])))

    svg = (
        '<svg class="ks3-lrange-svg" viewBox="0 0 1000 300" role="img" '
        'aria-label="" data-lrange-alt>'
        '<path class="ks3-lrange-axis" d="M90 190 H910"/>%s'
        '<rect class="ks3-lrange-band" data-lrange-band x="0" y="110" '
        'width="0" height="56" rx="8"/>'
        '<path class="ks3-lrange-marker" data-lrange-marker d="M0 0"/>'
        # Design's caption over the band. It is a CONSTANT string at build
        # time, so a `<text>` is right here — MRB-254 forbids one that ships
        # empty and is filled later, which this never is.
        '<text class="ks3-lrange-bandlabel" x="90" y="96">%s</text>'
        '<text class="ks3-lrange-axislabel" x="500" y="278" '
        'text-anchor="middle">%s</text></svg>'
        % (ticks, t(a.get("band_label", "WHAT THIS LISTENER CAN HEAR")),
           t(a.get("axis_label",
                          "FREQUENCY IN HERTZ — EACH MARK IS TEN TIMES "
                          "THE ONE BEFORE"))))

    fills = ('<span class="ks3-lrange-fill ks3-lrange-mark" '
             'data-lrange-fill="mark"></span>')

    # ⚠️ THE BRANCH NOTES WERE NEITHER VALIDATED NOR EMITTED. The payload
    # carried all three and this drawer read none of them, so the bench's
    # note panel was empty in every state — and the note is the one place
    # this instrument says "and you cannot", which is the whole lesson.
    # Caught by driving the below-the-band and above-the-band states and
    # finding no note at all; every other P6 bench validates its branches,
    # and this one is now the same shape as the rest.
    branches = a.get("branches") or {}
    need = ("inside", "below", "above")
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "log-range %r has no note for state(s) %s. A frequency is "
            "inside a listener's range, below the bottom of it or above "
            "the top, and the three are not the same sentence."
            % (act_id, ", ".join(missing)))
    for k in need:
        if "{other}" not in branches[k]:
            raise ValueError(
                "log-range %r branch %r names no second listener. \"The dog "
                "can hear it\" is a reading; \"the dog can hear it and you "
                "cannot\" is the lesson, and `{other}` is where the "
                "comparison goes." % (act_id, k))
    branch_data = "".join(
        '<span data-lrange-branch="%s" data-note="%s" hidden></span>'
        % (e(k), e(branches[k])) for k in need)

    lead = ('<p class="ks3-lrange-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    # ⚠️ THE SPAN IS READ, NOT ASSUMED. It was hardcoded to 5 and 1 while
    # the payload carried `decades` and `f_min` that nothing read — which
    # `ks3_key_audit` calls what it is. The chart geometry above genuinely
    # assumes six decade marks, so the defaults stay 5 and 1; the point is
    # that a payload saying otherwise now reaches the page instead of being
    # silently ignored.
    freq_spec = a.get("freq") or {}
    return ('<div class="ks3-lrange" data-lrange data-decades="%s" '
            'data-f-min="%s" data-start-who="%s"%s>%s%s%s'
            '<div class="ks3-lrange-body" data-lrange-body hidden>'
            '<div class="ks3-lrange-controls">'
            '<div class="ks3-lrange-picker">'
            '<p class="ks3-lrange-pickerlabel">%s</p>'
            '<div class="ks3-lrange-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-lrange-figwrap">%s%s</div>%s'
            '<p class="ks3-lrange-note" data-lrange-note></p>%s</div></div>'
            % (e(freq_spec.get("decades", 5)), e(freq_spec.get("f_min", 1)),
               e(a.get("start_who", 0)), _sibling(a),
               _head("lrange", a), lead,
               _gate(act_id, "log-range", a.get("gate") or {}, "lrange"),
               t(a.get("who_label", "Who is listening")), tabs,
               _slider(act_id, "lrange", freq, "f"),
               svg, fills, _tiles("lrange", a.get("readouts") or []),
               branch_data))


# ═══ p6-09 · #s-gauge · the ultrasonic flaw gauge ════════════════════════

def r_flaw_gauge(a, act_id):
    """⊕ p6-09 `#s-gauge` — send a pulse in, time what comes out.

    ⚖️ **THE BENCH PRINTS ITS OWN WORKING AND TAKES NO FORMULA BLOCK** (her
    FLAG 3). The gauge computes a depth from an echo time, which is
    `d = v × t` followed by halving — `p6-06`'s triangle and `p6-07`'s bar,
    both already owned one and two lessons back. A third speed block in the
    same unit would be the fourth `d = v × t` triangle in two units. Instead
    the readouts show the path and the time line by line, and both owning
    lessons are carried as edges.

    **If a reviewer rules that a page which computes must carry a block,
    this one needs one and it will be a duplicate.** That is Design's own
    sentence and it is Mide's call, not a lane's.

    ⚖️ **THE TIMING TRACE IS A SENT PIP AT ZERO AND AN ECHO PIP PLACED TO
    SCALE IN A FIXED WINDOW**, so a faster material visibly brings the two
    pips together. That is the whole of what the material control does, and
    it is why the gauge has to be told which material it is on.

    HOOKS: `data-fgauge` (wrapper, `data-window-ms`) · `data-fgauge-gate` ·
    `data-fgauge-gopt` · `data-fgauge-body` · `data-fgauge-mat` (carrying
    `data-v`) · `data-fgauge-slider` · `data-fgauge-flaw` ·
    `data-fgauge-down` · `data-fgauge-up` · `data-fgauge-pip` ·
    `data-fgauge-out` · `data-fgauge-note`.
    """
    mats = a.get("materials") or []
    if len(mats) < 3:
        raise ValueError(
            "flaw-gauge %r declares %d material(s). Every branch compares "
            "the same depth in another material, so there has to be another "
            "one." % (act_id, len(mats)))
    _unique(mats, act_id, "flaw-gauge", "material")
    for m in mats:
        for f in ("v", "note", "state", "caption"):
            if not m.get(f):
                raise ValueError(
                    "flaw-gauge %r material %r has no %r."
                    % (act_id, m.get("id"), f))
        if float(m["v"]) <= 0:
            raise ValueError(
                "flaw-gauge %r material %r has no speed of sound. A gauge "
                "cannot time an echo through a vacuum, and this bench does "
                "not offer one." % (act_id, m.get("id")))

    depth = a.get("depth") or {}
    for k in ("min", "max", "step", "start", "label"):
        if k not in depth:
            raise ValueError("flaw-gauge %r depth has no %r." % (act_id, k))

    tabs = "".join(
        _seg("ks3-seg-btn ks3-fgauge-mat", m["label"],
             pressed=(i == int(a.get("start_mat", 0))),
             data_fgauge_mat=m["id"], data_v=m["v"], data_note=m["note"],
             data_state=m["state"], data_caption=m["caption"],
             data_name=m["label"])
        for i, m in enumerate(mats))

    # Design's own 1000×420 viewBox: the block in cross-section on the left,
    # the timing window on the right.
    svg = (
        '<svg class="ks3-fgauge-svg" viewBox="0 0 1000 420" role="img" '
        'aria-label="" data-fgauge-alt>'
        '<rect class="ks3-fgauge-block" x="60" y="90" width="420" '
        'height="240" rx="6"/>'
        '<rect class="ks3-fgauge-probe" x="220" y="60" width="100" '
        'height="30" rx="6"/>'
        '<text class="ks3-fgauge-partlabel" x="330" y="82">%s</text>'
        '<rect class="ks3-fgauge-flaw" data-fgauge-flaw x="200" y="0" '
        'width="140" height="12" rx="4"/>'
        '<path class="ks3-fgauge-down" data-fgauge-down d="M0 0"/>'
        '<path class="ks3-fgauge-up" data-fgauge-up d="M0 0"/>'
        '<path class="ks3-fgauge-dim" data-fgauge-dim d="M0 0"/>'
        '<rect class="ks3-fgauge-screen" x="540" y="120" width="420" '
        'height="180" rx="8"/>'
        '<path class="ks3-fgauge-base" d="M560 280 H940"/>'
        '<path class="ks3-fgauge-pip" data-fgauge-pip="sent" '
        'd="M560 280 V170"/>'
        '<text class="ks3-fgauge-partlabel" x="560" y="160" '
        'text-anchor="middle">%s</text>'
        '<path class="ks3-fgauge-pip" data-fgauge-pip="echo" d="M0 0"/>'
        '<text class="ks3-fgauge-screenlabel" x="750" y="330" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("probe_label", "PROBE")),
           t(a.get("sent_label", "SENT")),
           t(a.get("screen_label", "SENT — AND WHAT CAME BACK"))))

    fills = "".join(
        '<span class="ks3-fgauge-fill ks3-fgauge-%s" '
        'data-fgauge-fill="%s"></span>' % (k, k) for k in ("depth", "caption"))

    lead = ('<p class="ks3-fgauge-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")

    return ('<div class="ks3-fgauge" data-fgauge data-window-ms="%s" '
            'data-start-mat="%s"%s>%s%s%s'
            '<div class="ks3-fgauge-body" data-fgauge-body hidden>'
            '<div class="ks3-fgauge-controls">'
            '<div class="ks3-fgauge-picker">'
            '<p class="ks3-fgauge-pickerlabel">%s</p>'
            '<div class="ks3-fgauge-tabrow">%s</div></div>%s</div>'
            '<div class="ks3-fgauge-figwrap">%s%s</div>%s'
            '<p class="ks3-fgauge-note" data-fgauge-note></p></div></div>'
            % (e(a.get("window_ms", 0.30)), e(a.get("start_mat", 0)),
               _sibling(a),
               _head("fgauge", a), lead,
               _gate(act_id, "flaw-gauge", a.get("gate") or {}, "fgauge"),
               t(a.get("mat_label", "What the block is")), tabs,
               _slider(act_id, "fgauge", depth, "d"),
               svg, fills, _tiles("fgauge", a.get("readouts") or [])))


# ═══ the band blocks · #s-stages · #s-compare · #s-chart · #s-uses ═══════

def r_wave_band(a, act_id):
    """⊕ The band block Design puts beside four of the nine benches.

    ⚖️ **`panels`, NOT `cards`.** `cards` is claimed by `r_activity` itself
    with NO opt-out, so a payload using it gets two renderers and renders
    blank. The key is deliberately different for that reason and no other.

    ⚖️ **THE BAND STOP IS TICKED BY THE BENCH BESIDE IT.** These blocks carry
    no control: they are the payoff of the instrument, exactly as MRB-249
    describes, and each bench marks its own band sibling at Design's own
    earlier threshold. `mirrors` would tick them late.

    Five shapes go through here, and the payload decides which:
      `p6-03 #s-stages`   a four-column process strip plus a closing line
      `p6-04 #s-compare`  a two-column contrast table
      `p6-07 #s-figure`   a five-row percentage bar chart with a threshold
      `p6-08 #s-chart`    a fixed multi-row decade chart
      `p6-09 #s-uses`     a four-panel split, energy uses against
                          information uses
    """
    lead = ('<p class="ks3-wband-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")
    close = ('<p class="ks3-wband-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    body = ""
    if a.get("strip"):
        body += '<div class="ks3-wband-strip">%s</div>' % _strip(a["strip"],
                                                                act_id)
    if a.get("chart"):
        body += '<div class="ks3-wband-chart">%s</div>' % _chart(a["chart"],
                                                                act_id)
    if a.get("bars"):
        body += '<div class="ks3-wband-chart">%s</div>' % _bars(a["bars"],
                                                               act_id)
    if a.get("speeds"):
        body += ('<div class="ks3-wband-chart">%s</div>'
                 % _speeds(a["speeds"], act_id))
    if a.get("pair"):
        body += _pair(a["pair"], act_id)

    panels = a.get("panels") or []
    if panels:
        _unique(panels, act_id, "wave-band", "panel", key="num")
        items = ""
        for p in panels:
            for f in ("num", "name", "body"):
                if not p.get(f):
                    raise ValueError(
                        "wave-band %r panel %r has no %r."
                        % (act_id, p.get("num"), f))
            tell = ('<p class="ks3-wband-tell">%s</p>' % rich(p["tell"])
                    if p.get("tell") else "")
            items += ('<li class="ks3-wband-item">'
                      '<span class="ks3-wband-num" aria-hidden="true">%s'
                      '</span><p class="ks3-wband-name">%s</p>'
                      '<p class="ks3-wband-body">%s</p>%s</li>'
                      % (t(p["num"]), t(p["name"]), rich(p["body"]), tell))
        body += '<ol class="ks3-wband-list">%s</ol>' % items

    cols = a.get("columns") or []
    if cols:
        if len(cols) != 2:
            raise ValueError(
                "wave-band %r declares %d column(s). Design's is a pair, and "
                "one on its own makes a claim the other half was there to "
                "balance." % (act_id, len(cols)))
        cells = "".join(
            '<div class="ks3-wband-col"><p class="ks3-wband-coltitle">%s</p>'
            '<ul class="ks3-wband-collist">%s</ul></div>'
            % (t(c["title"]),
               "".join("<li>%s</li>" % rich(x) for x in (c.get("items") or [])))
            for c in cols)
        body += '<div class="ks3-wband-cols">%s</div>' % cells

    if not body:
        raise ValueError(
            "wave-band %r renders nothing — no strip, chart, bars, speeds, "
            "panels or columns. An empty band block is a section heading with a gap "
            "under it." % act_id)

    # ⊕ THE ONE BAND STOP IN P6 THAT TICKS ON THE HOOK — and it takes
    # MRB-249's `mirrors`, not a mechanism of its own.
    #
    # `p6-03`'s `#s-stages` sits ABOVE the bench and Design's own DONE for
    # it reads `s.hookChoice !== null`. Every other band stop in the key
    # stage takes its tick from the instrument beside it; there is no
    # instrument above this one to give it one.
    #
    # A bespoke `after_anchor` attribute was built here first, watching the
    # hook section's DOM and writing this section's own `data-stage-done`.
    # It worked, and it was still wrong: MRB-249's gate reads Design's
    # `isDone()` as a MIRROR MAP and compares it against what the rail
    # DECLARES, so a stop that ticks by a private route still fails — and
    # it did. `ks3_parity`'s own `_TICK_EXEMPT` note says the answer is
    # `mirrors` rather than a new predicate, and it is right. The stop now
    # declares `"mirrors": "s-hook"` in its rail row and the engine
    # resolves it, which is also what makes R2 accept it as reachable.

    # ⊕ MRB-223 — the `check` shell already emits this figure's eyebrow and
    # <h2>; the band printed them a second time (measured: two "The figure",
    # two "Four stages, every time" on how-sound-is-made.html).
    return ('<div class="ks3-wband" data-wband>'
            '%s%s%s</div>'
            % (lead, body, close))


def _strip(strip, act_id):
    """p6-03 `#s-stages` — the four-column process figure.

    ⚠️ REUSED SHAPE, NOT REUSED CODE. P4's `stage-strip` draws four columns
    of ARROWS at a fixed weight; this draws four columns of GLYPHS with a
    caption each, and the two have nothing in common but the grid. Sharing a
    drawer would mean one of them growing a mode flag.
    """
    cols = strip.get("columns") or []
    if len(cols) != 4:
        raise ValueError(
            "stage-strip %r draws %d column(s); the chain is four stages."
            % (act_id, len(cols)))
    out = ""
    for i, c in enumerate(cols):
        px = 30 + i * 250
        out += ('<text class="ks3-wband-stagelabel" x="%d" y="30">%s</text>'
                '<rect class="ks3-wband-stagebox" x="%d" y="60" width="190" '
                'height="150" rx="10"/>'
                '<path class="ks3-wband-stageglyph" d="%s"/>'
                '<text class="ks3-wband-stagecaption" x="%d" y="252">%s'
                '</text>'
                % (px, t(c.get("title", "")), px, c.get("glyph", "M0 0"),
                   px, t(c.get("caption", ""))))
        if i < 3:
            out += ('<path class="ks3-wband-stagearrow" d="M%d 135 H%d '
                    'M%d 135 l-12 -8 M%d 135 l-12 8"/>'
                    % (px + 196, px + 242, px + 242, px + 242))
    return ('<svg class="ks3-wband-stripsvg" viewBox="0 0 1000 280" '
            'role="img" aria-label="%s">%s</svg>'
            % (e(strip.get("aria_label", "")), out))


def _bars(bars, act_id):
    """p6-07 `#s-figure` — five surfaces against how much each sends back.

    ⚖️ **THE THRESHOLD IS A DRAWN LINE AND A WRITTEN NUMBER**, not a colour
    change. Design's chart puts a dashed rule at 15% and labels it in words,
    so the reason bare rock echoes and foam does not is legible without
    reading a hue. `_bars` refuses a payload with no threshold, because a
    percentage chart with nothing to compare against teaches an ordering the
    lesson never needed a figure for.

    ⚖️ **EVERY BAR CARRIES ITS OWN NUMBER AND ITS OWN PLACE.** The value
    ("about 90%") sits at the end of the bar and the use ("a quarry") beside
    it, so the row reads without the axis. Bar LENGTH is the redundant second
    channel, never the only one.

    ⚠️ **THE VALUE STRINGS ARE AUTHORED, NOT FORMATTED.** Design writes
    "about 90%", with the hedge, because these are round teaching figures for
    a typical surface. A renderer printing "90%" from `pct` would quietly
    promote an approximation to a measurement.

    ⚠️ **NO `<text>` HOLDS AN AUTHORED STRING** (MRB-254). Every label here
    is a real string at build time; nothing is filled in later, so there is
    no empty `<text>` to ship.
    """
    rows = bars.get("rows") or []
    if len(rows) < 3:
        raise ValueError(
            "surface-bars %r draws %d row(s). The figure exists to put a "
            "range of surfaces side by side, and under three of them is a "
            "list." % (act_id, len(rows)))
    _unique(rows, act_id, "surface-bars", "row", key="label")
    if not bars.get("threshold"):
        raise ValueError(
            "surface-bars %r declares no `threshold`. Without the line the "
            "chart is an ordering, and the lesson's point is that there is a "
            "level below which no echo is heard at all." % act_id)
    thr = float(bars["threshold"])
    for r in rows:
        for f in ("label", "pct", "value"):
            if not r.get(f):
                raise ValueError(
                    "surface-bars %r row %r has no %r. Every bar carries its "
                    "own number in words; length is never the only channel."
                    % (act_id, r.get("label"), f))

    X0, X1 = 250.0, 900.0
    ROW, TOP = 46, 58

    def xf(pct):
        return X0 + (max(0.0, min(100.0, float(pct))) / 100.0) * (X1 - X0)

    body = ('<text class="ks3-wband-axhead" x="240" y="34" '
            'text-anchor="end">%s</text>'
            '<text class="ks3-wband-axhead" x="%.1f" y="34">%s</text>'
            % (t(bars.get("name_label", "SURFACE")), X0,
               t(bars.get("axis_label", ""))))

    tx = xf(thr)
    body += ('<path class="ks3-wband-bound" d="M%.1f 42 V%d"/>'
             '<text class="ks3-wband-boundlabel" x="%.1f" y="%d">%s</text>'
             % (tx, TOP + len(rows) * ROW - 6,
                tx + 8, TOP + len(rows) * ROW + 14,
                t(bars.get("threshold_label", ""))))

    for i, r in enumerate(rows):
        y = TOP + i * ROW
        w = max(4.0, xf(r["pct"]) - X0)
        body += ('<text class="ks3-wband-rowlabel" x="240" y="%d" '
                 'text-anchor="end">%s</text>'
                 '<rect class="ks3-wband-rowband" x="%.1f" y="%d" '
                 'width="%.1f" height="24" rx="6"/>'
                 '<text class="ks3-wband-rowvalue" x="%.1f" y="%d">%s</text>'
                 % (y + 17, t(r["label"]), X0, y, w,
                    X0 + w + 12, y + 17,
                    t("%s · %s" % (r["value"], r["use"]) if r.get("use")
                      else r["value"])))

    return ('<svg class="ks3-wband-chartsvg" viewBox="0 0 1000 %d" '
            'role="img" aria-label="%s">%s</svg>'
            % (TOP + len(rows) * ROW + 30, e(bars.get("aria_label", "")), body))


def _pair(spec, act_id):
    """p6-04 `#s-compare` — two cards, each with the wave drawn.

    ⚖️ **THE DIFFERENCE IS DRAWN, NOT TABULATED.** Design puts a shaken
    rope beside a squeezed chain, each with one marked particle and an
    arrow showing WHICH WAY THAT PARTICLE MOVES, against a second arrow
    showing which way the wave goes. The whole lesson is the angle between
    those two arrows, and a table of sentences cannot make that angle.

    ⚖️ **BOTH CARDS CARRY BOTH ARROWS.** A card showing only the particle's
    movement would leave a reader to assume the direction of travel; a card
    showing only the travel would lose the point. `_pair` refuses a card
    without both.

    ⚠️ **NO LIVE VALUES AND NO HOLES.** Everything here is a constant at
    build time, which is why the labels are SVG `<text>` and not overlay
    spans — MRB-254 forbids a `<text>` that ships empty to be filled later,
    and none of these is.
    """
    cards = spec.get("cards") or []
    if len(cards) != 2:
        raise ValueError(
            "wave-pair %r declares %d card(s). Design's figure is a pair — "
            "transverse against longitudinal — and one on its own makes a "
            "claim the other half was there to answer." % (act_id, len(cards)))
    for c in cards:
        for f in ("title", "kind", "body", "aria_label"):
            if not c.get(f):
                raise ValueError(
                    "wave-pair %r card %r has no %r."
                    % (act_id, c.get("title"), f))
        if c["kind"] not in ("transverse", "longitudinal"):
            raise ValueError(
                "wave-pair %r card %r is kind %r; the two are `transverse` "
                "and `longitudinal`." % (act_id, c.get("title"), c["kind"]))

    def draw(kind, aria):
        MID, X0, X1 = 100, 20, 420
        if kind == "transverse":
            d, x = "", float(X0)
            while x <= X1:
                d += ("%s%.1f %.1f" % (" L" if d else "M", x,
                                       MID - 38 * math.sin(
                                           (2 * math.pi * (x - X0)) / 110)))
                x += 4
            art = ('<path class="ks3-wband-pairwave" d="%s"/>'
                   '<circle class="ks3-wband-pairdot" cx="185" cy="%.1f" '
                   'r="11"/>'
                   '<path class="ks3-wband-pairmove" d="M185 %d V26 '
                   'M185 26 l-9 13 M185 26 l9 13 M185 %d V174 '
                   'M185 174 l-9 -13 M185 174 l9 -13"/>'
                   % (d, MID - 38 * math.sin((2 * math.pi * 165) / 110),
                      MID - 38, MID + 38))
        else:
            art = ""
            for i in range(26):
                base = X0 + 8 + i * 15.6
                off = 11 * math.sin((2 * math.pi * (base - X0)) / 110)
                art += ('<path class="ks3-wband-paircoil" d="M%.1f 58 V142"/>'
                        % (base + off))
            # ⚠️ THE TWO WORDS THE LESSON IS ABOUT, DRAWN WHERE THEY
            # HAPPEN. The coils crowd where the spacing derivative is
            # smallest — every 110 units from x = 75 — and open out halfway
            # between. Her card names both and this one did not, which left
            # a reader to work out from the picture which bunching was
            # which. Constants at build time, so `<text>` is right: nothing
            # here is filled in later.
            art += ('<circle class="ks3-wband-pairdot" cx="185" cy="100" '
                    'r="11"/>'
                    '<path class="ks3-wband-pairmove" d="M215 100 H255 '
                    'M255 100 l-13 -9 M255 100 l-13 9 M155 100 H115 '
                    'M115 100 l13 -9 M115 100 l13 9"/>'
                    '<text class="ks3-wband-pairregion" x="185" y="46" '
                    'text-anchor="middle">%s</text>'
                    '<text class="ks3-wband-pairregion" x="295" y="46" '
                    'text-anchor="middle">%s</text>'
                    % (t(spec.get("comp_label", "COMPRESSION")),
                       t(spec.get("rare_label", "RAREFACTION"))))
        return ('<svg class="ks3-wband-pairsvg" viewBox="0 0 440 200" '
                'role="img" aria-label="%s">%s'
                '<path class="ks3-wband-pairtravel" d="M300 174 H420 '
                'M420 174 L406 165 M420 174 L406 183"/>'
                '<text class="ks3-wband-pairtravellabel" x="300" y="158">'
                '%s</text></svg>'
                % (e(aria), art, t(spec.get("travel_label", "travels"))))

    cells = "".join(
        '<div class="ks3-wband-paircard">'
        '<p class="ks3-wband-pairtitle">%s</p>%s'
        '<p class="ks3-wband-pairbody">%s</p></div>'
        % (t(c["title"]), draw(c["kind"], c["aria_label"]), rich(c["body"]))
        for c in cards)
    return '<div class="ks3-wband-pair">%s</div>' % cells


def _speeds(spec, act_id):
    """p6-06 `#s-range`'s figure — five materials, one scale, and the
    particles beside each bar.

    ⚖️ **THE PARTICLES ARE THE EXPLANATION AND THE BAR IS THE RESULT**, side
    by side, which is the whole argument of the lesson in one picture: the
    order of the speeds follows the order of the spacings. Design's own
    closing line says it — *"The order runs with the particles, not against
    them"* — so a chart with the bars and no particles would be a ranking
    with the reason left out.

    ⚖️ **THE VACUUM'S ROW IS EMPTY AND SAYS SO IN WORDS.** No bar, no
    particles, and `no sound at all` where every other row carries a speed.
    A zero-length bar would read as a very small number; `WAVE-21` is
    exactly that misreading.

    ⚠️ **ONE SCALE FOR ALL FIVE.** The bars are drawn from the speeds, so
    steel really is fifteen times air. That is the claim, and drawing it any
    other way would make the picture argue against the numbers beside it.
    """
    rows = spec.get("rows") or []
    if len(rows) < 4:
        raise ValueError(
            "speed-chart %r draws %d row(s). The point is the ORDER, and an "
            "order needs the whole range in it." % (act_id, len(rows)))
    _unique(rows, act_id, "speed-chart", "row", key="label")
    if not any(float(r.get("v") or 0) <= 0 for r in rows):
        raise ValueError(
            "speed-chart %r has no zero-speed row. The vacuum is the row "
            "that makes the other four mean something, and it is the one a "
            "chart drawn from numbers alone quietly leaves out." % act_id)
    for r in rows:
        for f in ("label", "value", "pattern"):
            if not r.get(f):
                raise ValueError(
                    "speed-chart %r row %r has no %r. Every row carries its "
                    "own speed in words and its own particle arrangement; "
                    "bar length is never the only channel."
                    % (act_id, r.get("label"), f))

    X0, X1, ROW, TOP = 330.0, 950.0, 52, 76
    top_v = max(float(r["v"]) for r in rows) or 1.0
    body = ('<text class="ks3-wband-axhead" x="30" y="46">%s</text>'
            '<text class="ks3-wband-axhead" x="150" y="46">%s</text>'
            '<text class="ks3-wband-axhead" x="%.0f" y="46">%s</text>'
            % (t(spec.get("name_label", "MATERIAL")),
               t(spec.get("particle_label", "PARTICLES")),
               X0, t(spec.get("speed_label", "SPEED OF SOUND"))))

    for i, r in enumerate(rows):
        y = TOP + i * ROW
        v = float(r["v"])
        body += ('<text class="ks3-wband-rowlabel" x="30" y="%d">%s</text>'
                 % (y + 17, t(r["label"])))
        # the particles: spacing IS the pattern, and each row says which.
        kind = r["pattern"]
        if kind == "none":
            body += ('<text class="ks3-wband-rowempty" x="150" y="%d">%s'
                     '</text>' % (y + 17, t(r.get("particle_note",
                                                  "NOTHING HERE"))))
        else:
            cols = {"gas": 4, "liquid": 7, "lattice": 9}.get(kind, 6)
            gap = 150.0 / (cols + 1)
            link = ""
            for c in range(cols):
                px = 150 + gap * (c + 1) + (((c * 29) % 13) - 6
                                            if kind == "gas" else 0)
                body += ('<circle class="ks3-wband-particle" cx="%.1f" '
                         'cy="%d" r="4"/>' % (px, y + 12))
                if kind == "lattice" and c:
                    link += ("M%.1f %d H%.1f "
                             % (px - gap, y + 12, px))
            if link:
                body += ('<path class="ks3-wband-lattice" d="%s"/>' % link)
        if v > 0:
            w = max(4.0, (v / top_v) * (X1 - X0 - 150))
            body += ('<rect class="ks3-wband-rowband" x="%.0f" y="%d" '
                     'width="%.1f" height="24" rx="6"/>' % (X0, y, w))
            body += ('<text class="ks3-wband-rowvalue" x="%.1f" y="%d">%s'
                     '</text>' % (X0 + w + 12, y + 17, t(r["value"])))
        else:
            body += ('<text class="ks3-wband-rowempty" x="%.0f" y="%d">%s'
                     '</text>' % (X0, y + 17, t(r["value"])))

    return ('<svg class="ks3-wband-chartsvg" viewBox="0 0 1000 %d" '
            'role="img" aria-label="%s">%s</svg>'
            % (TOP + len(rows) * ROW + 20, e(spec.get("aria_label", "")), body))


def _chart(chart, act_id):
    """p6-08 `#s-chart` — every range side by side on one decade axis.

    ⚖️ **ALL GEOMETRY IS COMPUTED FROM LOGARITHMS AT BUILD TIME**, so the
    chart is in the bytes rather than assembled in JS. It never changes:
    it is the fixed counterpart of the live bench above it.

    ⚖️ **THE HUMAN BAND IS SHADED BEHIND EVERY ROW**, which is what makes
    "ultrasound" and "infrasound" visibly statements about US rather than
    about the sound. The two boundaries are drawn as dashed lines and
    labelled.
    """
    rows = chart.get("rows") or []
    if len(rows) < 4:
        raise ValueError(
            "range-chart %r draws %d row(s). The point of the chart is that "
            "the human range is one case among several."
            % (act_id, len(rows)))
    lo_hz, decades = 1.0, 5.0
    X0, X1 = 200.0, 950.0

    def xf(hz):
        return X0 + (math.log10(max(float(hz), lo_hz) / lo_hz) / decades) \
            * (X1 - X0)

    human = chart.get("human") or {}
    body = ""
    if human:
        body += ('<rect class="ks3-wband-humanband" x="%.1f" y="40" '
                 'width="%.1f" height="%d" rx="6"/>'
                 % (xf(human["lo"]), xf(human["hi"]) - xf(human["lo"]),
                    36 + len(rows) * 44))
        for key, label in (("lo", chart.get("infra_label", "INFRASOUND")),
                           ("hi", chart.get("ultra_label", "ULTRASOUND"))):
            body += ('<path class="ks3-wband-bound" d="M%.1f 40 V%d"/>'
                     % (xf(human[key]), 76 + len(rows) * 44))
        body += ('<text class="ks3-wband-boundlabel" x="%.1f" y="34" '
                 'text-anchor="end">%s</text>'
                 '<text class="ks3-wband-boundlabel" x="%.1f" y="34">%s'
                 '</text>'
                 % (xf(human["lo"]) - 8, t(chart.get("infra_label",
                                                     "INFRASOUND")),
                    xf(human["hi"]) + 8, t(chart.get("ultra_label",
                                                     "ULTRASOUND"))))
    for i, r in enumerate(rows):
        y = 56 + i * 44
        body += ('<text class="ks3-wband-rowlabel" x="190" y="%d" '
                 'text-anchor="end">%s</text>'
                 '<rect class="ks3-wband-rowband" x="%.1f" y="%d" '
                 'width="%.1f" height="22" rx="6"/>'
                 % (y + 16, t(r["label"]), xf(r["lo"]), y,
                    max(4.0, xf(r["hi"]) - xf(r["lo"]))))
    for d in range(0, 6):
        x = xf(10 ** d)
        body += ('<path class="ks3-wband-tick" d="M%.1f %d V%d"/>'
                 '<text class="ks3-wband-ticklabel" x="%.1f" y="%d" '
                 'text-anchor="middle">%s</text>'
                 % (x, 46 + len(rows) * 44, 62 + len(rows) * 44,
                    x, 88 + len(rows) * 44,
                    t(["1", "10", "100", "1 000", "10 000", "100 000"][d])))
    return ('<svg class="ks3-wband-chartsvg" viewBox="0 0 1000 %d" '
            'role="img" aria-label="%s">%s</svg>'
            % (110 + len(rows) * 44, e(chart.get("aria_label", "")), body))


# ═══ the CFIFA attempt ═══════════════════════════════════════════════════

def r_p6_attempt(a, act_id):
    """⊕ P6's half of Design's `Cfifa`: the student's own five lines.

    The drawing is `ks3_art.kit.r_cfifa_attempt`, shared with P4 and P5. The
    FAMILY is P6's own, so `ks3_art.load()`'s one-family-one-module rule
    holds and the placement gates see it as this unit's.
    """
    # ⊕ MRB-223 — ONE EYEBROW, NOT TWO. The `check` shell already prints
    # this activity's eyebrow in Design's `.ks3-blockhead`; the kit helper
    # printed it again. `None` tells the helper it is already on the page
    # (the P7 opt-out, applied here after it was measured on live pages).
    return r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p6cfa")


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P6's own — `ks3_art/core.py` is
# untouched. Shell stems checked against the whole registry first.

ART = {}

KIND_SHELL = {
    'wave-anatomy':         ("ks3-wanat-block",
                             ' data-instrument data-wanatblock '
                             'data-stage-done="0"'),
    'ripple-tank':          ("ks3-rtank-block",
                             ' data-instrument data-rtankblock '
                             'data-stage-done="0"'),
    'superposition-lanes':  ("ks3-slane-block",
                             ' data-instrument data-slaneblock '
                             'data-stage-done="0"'),
    'vibration-chain':      ("ks3-vchain-block",
                             ' data-instrument data-vchainblock '
                             'data-stage-done="0"'),
    'slinky-dual':          ("ks3-slink-block",
                             ' data-instrument data-slinkblock '
                             'data-stage-done="0"'),
    'scope-trace':          ("ks3-scope-block",
                             ' data-instrument data-scopeblock '
                             'data-stage-done="0"'),
    'medium-range':         ("ks3-mrange-block",
                             ' data-instrument data-mrangeblock '
                             'data-stage-done="0"'),
    'echo-range':           ("ks3-echo-block",
                             ' data-instrument data-echoblock '
                             'data-stage-done="0"'),
    'log-range':            ("ks3-lrange-block",
                             ' data-instrument data-lrangeblock '
                             'data-stage-done="0"'),
    'flaw-gauge':           ("ks3-fgauge-block",
                             ' data-instrument data-fgaugeblock '
                             'data-stage-done="0"'),
    'wave-band':            ("ks3-wband-block",
                             ' data-instrument data-wbandblock '
                             'data-stage-done="0"'),
    'p6-attempt':           ("ks3-p6cfa-block",
                             ' data-instrument data-p6cfablock '
                             'data-stage-done="0"'),
}

KIND_FN = {
    'wave-anatomy':         r_wave_anatomy,
    'ripple-tank':          r_ripple_tank,
    'superposition-lanes':  r_superposition_lanes,
    'vibration-chain':      r_vibration_chain,
    'slinky-dual':          r_slinky_dual,
    'scope-trace':          r_scope_trace,
    'medium-range':         r_medium_range,
    'echo-range':           r_echo_range,
    'log-range':            r_log_range,
    'flaw-gauge':           r_flaw_gauge,
    'wave-band':            r_wave_band,
    'p6-attempt':           r_p6_attempt,
}
