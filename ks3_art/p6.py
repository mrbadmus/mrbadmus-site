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


# ═══════════════════════════════════════════════════════════════════════════
# LEAN WAVE 2 (P6 lane A: lessons 1 to 5) · five drawn figures
# ═══════════════════════════════════════════════════════════════════════════
#
#   "p6-transverse-wave"  data {"show": "parts"}                      crest, trough, rest line,
#                                                                      amplitude, wavelength, travel
#                         data {"show": "motion", "motion_label": s,  one piece of the material
#                               "travel_note": s (optional)}
#                                                                      moving up and down, the wave
#                                                                      travelling across
#   "p6-superposition"    data {"cases": [{"title", "a", "b", "sign"}] x2}  two waves and where they
#                                                                      meet, drawn to one scale (mm)
#   "p6-sound-chain"      data {"steps": [{"title", "lines": [..]}] x4} source, air, sheet, signal
#   "p6-longitudinal"     data {}                                      a loudspeaker and the air in
#                                                                      front of it: compressions,
#                                                                      rarefactions, wavelength
#   "p6-sound-traces"     data {"rows": [{"title", "panels": [{"label", "amp", "waves"}] x2}] x2}
#
# All 340 wide, so they sit in a phone card without scrolling; every label is 13px or more.
# Every colour is a --ks3-* token; the wave traces are ink, the one piece of material that is
# followed is accent AND a filled dot AND named in words, so nothing rests on colour alone.
from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_RULE_STRONG,
    _circle,
    _label,
    _line,
    _n,
    _path,
    _rect,
    _svg_open,
)

_P6A_W = 340


def _p6a_open(fig, h, body):
    return (_svg_open(fig, _P6A_W, int(math.ceil(h)))
            + '<g stroke-linecap="round" stroke-linejoin="round">' + "".join(body) + "</g></svg>")


def _p6a_head(x, y, ang, paint=_SVG_INK, size=8.0, **data):
    """A filled arrowhead with its tip at (x, y), pointing along `ang` (radians)."""
    bx, by = x - size * math.cos(ang), y - size * math.sin(ang)
    px, py = -math.sin(ang) * size * 0.55, math.cos(ang) * size * 0.55
    return _path("M %s,%s L %s,%s L %s,%s Z"
                 % (_n(round(x, 2)), _n(round(y, 2)), _n(round(bx + px, 2)), _n(round(by + py, 2)),
                    _n(round(bx - px, 2)), _n(round(by - py, 2))),
                 fill=paint, data_part=data.pop("data_part", "arrowhead"), **data)


def _p6a_arrow(x1, y1, x2, y2, paint=_SVG_INK, w=2, both=False, part="arrow"):
    """A straight arrow from (x1, y1) to (x2, y2); `both` puts a head on each end."""
    ang = math.atan2(y2 - y1, x2 - x1)
    inset = 6.0
    sx = x1 + (inset * math.cos(ang) if both else 0)
    sy = y1 + (inset * math.sin(ang) if both else 0)
    ex, ey = x2 - inset * math.cos(ang), y2 - inset * math.sin(ang)
    o = [_line(round(sx, 2), round(sy, 2), round(ex, 2), round(ey, 2), stroke=paint, w=w,
               data_part=part),
         _p6a_head(x2, y2, ang, paint)]
    if both:
        o.append(_p6a_head(x1, y1, ang + math.pi, paint))
    return "".join(o)


def _p6a_wave_y(x, mid, amp, lam, crest_x):
    """Height of a sine wave at x: a crest (highest point) at `crest_x`."""
    return mid - amp * math.cos(2 * math.pi * (x - crest_x) / lam)


def _p6a_wave_d(x0, x1, mid, amp, lam, crest_x, step=2.0):
    pts, x = [], float(x0)
    while x < x1:
        pts.append("%s,%s" % (_n(round(x, 2)), _n(round(_p6a_wave_y(x, mid, amp, lam, crest_x), 2))))
        x += step
    pts.append("%s,%s" % (_n(round(float(x1), 2)), _n(round(_p6a_wave_y(x1, mid, amp, lam, crest_x), 2))))
    return "M " + " L ".join(pts)


def _p6a_transverse_wave(fig):
    """A transverse wave on a rest line, two wavelengths long.

    show "parts":  crest, trough, rest line, the amplitude (rest line up to a crest) and the
                   wavelength (one crest to the next), with the direction of travel.
    show "motion": one piece of the material marked on the wave, its up-and-down movement as a
                   double arrow, and the direction of travel. `motion_label` names the material.
    """
    d = fig.get("data") or {}
    show = d.get("show")
    if show not in ("parts", "motion"):
        raise ValueError("figure %r: p6-transverse-wave needs data.show 'parts' or 'motion'"
                         % fig.get("id"))
    MID, AMP, LAM = 118.0, 38.0, 120.0
    X0, X1 = 90.0, 330.0
    C1, C2 = 120.0, 240.0               # the two crests
    T1 = 180.0                          # the first trough
    o = [_line(8, MID, 332, MID, stroke=_SVG_RULE_STRONG, w=2, dash="6,5", data_part="rest-line")]
    # direction of travel, along the top
    o.append(_label(8, 24, "direction of travel", size=13, weight="600", anchor="start",
                    fill=_SVG_INK_BODY, data_part="travel-label"))
    o.append(_p6a_arrow(160, 20, 330, 20, paint=_SVG_INK, w=2.5, part="travel-arrow"))
    o.append(_path(_p6a_wave_d(X0 if show == "parts" else 30.0, X1, MID, AMP, LAM, C1),
                   stroke=_SVG_INK, w=3, data_part="wave"))
    if show == "parts":
        o.append(_label(8, MID + 20, "rest line", size=13, weight="600", anchor="start",
                        fill=_SVG_INK_BODY, data_part="rest-label"))
        # wavelength: crest to crest, above the crests
        WY = MID - AMP - 24
        o.append(_line(C1, MID - AMP - 4, C1, WY - 6, stroke=_SVG_INK_MUTED, w=1.5,
                       data_part="wavelength-tick"))
        o.append(_line(C2, MID - AMP - 4, C2, WY - 6, stroke=_SVG_INK_MUTED, w=1.5,
                       data_part="wavelength-tick"))
        o.append(_p6a_arrow(C1, WY, C2, WY, paint=_SVG_ACCENT_TEXT, w=2.5, both=True,
                            part="wavelength-arrow"))
        o.append(_label((C1 + C2) / 2.0, WY - 8, "wavelength", size=14, weight="700",
                        fill=_SVG_ACCENT_TEXT, data_part="wavelength-label"))
        o.append(_label(C2 + 6, MID - AMP - 8, "crest", size=13, weight="700", anchor="start",
                        data_part="crest-label"))
        o.append(_label(T1, MID + AMP + 22, "trough", size=13, weight="700",
                        data_part="trough-label"))
        # amplitude: rest line up to the height of a crest, drawn clear of the wave on the left
        AX = 45.0
        o.append(_line(AX - 10, MID - AMP, C1, MID - AMP, stroke=_SVG_INK_MUTED, w=1.5,
                       dash="3,4", data_part="crest-guide"))
        o.append(_p6a_arrow(AX, MID, AX, MID - AMP, paint=_SVG_ACCENT_TEXT, w=2.5, both=True,
                            part="amplitude-arrow"))
        o.append(_label(AX, MID - AMP - 10, "amplitude", size=14, weight="700",
                        fill=_SVG_ACCENT_TEXT, data_part="amplitude-label"))
        return _p6a_open(fig, MID + AMP + 34, o)
    # motion: one piece of the material, halfway between a crest and a trough
    label = d.get("motion_label")
    if not label:
        raise ValueError("figure %r: show 'motion' needs data.motion_label" % fig.get("id"))
    PX = 150.0
    PY = _p6a_wave_y(PX, MID, AMP, LAM, C1)
    o.append(_p6a_arrow(PX, MID - AMP - 6, PX, MID + AMP + 6, paint=_SVG_ACCENT_TEXT,
                        w=2.5, both=True, part="motion-arrow"))
    o.append(_circle(PX, round(PY, 2), 7, fill=_SVG_ACCENT, stroke=_SVG_INK, w=2,
                     data_part="particle"))
    o.append(_label(8, MID + AMP + 30, label, size=14, weight="700", anchor="start",
                    fill=_SVG_ACCENT_TEXT, data_part="motion-label"))
    o.append(_label(8, MID + AMP + 50, d.get("travel_note") or "The wave travels across, at right angles.",
                    size=13, weight="600", anchor="start", fill=_SVG_INK_BODY,
                    data_part="right-angles"))
    return _p6a_open(fig, MID + AMP + 60, o)


def _p6a_superposition(fig):
    """Two cases side by side, each three traces to one scale (2 px per mm): the first wave,
    the second wave, and the water where they meet, with the sum written under it.
    sign +1 is crest on crest (the heights add), -1 is crest on trough (they subtract)."""
    d = fig.get("data") or {}
    cases = d.get("cases") or []
    if len(cases) != 2:
        raise ValueError("figure %r: p6-superposition draws exactly two cases" % fig.get("id"))
    PX = 2.0
    rows = [60.0, 112.0, 182.0]          # centre of each trace
    o = []
    for ci, c in enumerate(cases):
        a, b, sign = c.get("a"), c.get("b"), c.get("sign")
        if not (isinstance(a, int) and isinstance(b, int) and sign in (1, -1) and c.get("title")):
            raise ValueError("figure %r: each case needs title, whole-mm a and b, sign 1 or -1"
                             % fig.get("id"))
        r = a + sign * b
        if r < 0 or a * PX > 24 or b * PX > 16 or r * PX > 30:
            raise ValueError("figure %r: case %r does not fit its rows" % (fig.get("id"), c))
        x0 = 4.0 + ci * 170.0
        tx0, tx1 = x0 + 54.0, x0 + 160.0
        lam = (tx1 - tx0) / 2.0
        crest = tx0 + lam / 2.0
        o.append(_label(x0 + 81, 18, c["title"], size=14, weight="700", data_part="case-title",
                        data_case=str(ci)))
        o.append(_label(x0 + 81, 150, "where they meet", size=13, weight="600",
                        fill=_SVG_INK_BODY, data_part="meet-label", data_case=str(ci)))
        o.append(_line(x0 + 4, 134, x0 + 160, 134, stroke=_SVG_INK_MUTED, w=1.5,
                       data_part="meet-rule", data_case=str(ci)))
        for ri, (h, part) in enumerate(((a, "wave-a"), (sign * b, "wave-b"), (r, "together"))):
            cy = rows[ri]
            o.append(_line(tx0, cy, tx1, cy, stroke=_SVG_RULE_STRONG, w=1.5, dash="5,4",
                           data_part="rest-line"))
            if h == 0:
                o.append(_line(tx0, cy, tx1, cy, stroke=_SVG_INK, w=3, data_part=part,
                               data_mm="0"))
            else:
                o.append(_path(_p6a_wave_d(tx0, tx1, cy, h * PX, lam, crest), stroke=_SVG_INK,
                               w=3 if ri == 2 else 2.5, data_part=part, data_mm=str(h)))
            o.append(_label(x0 + 2, cy + 5, "%d mm" % abs(h), size=14 if ri == 2 else 13,
                            weight="700", anchor="start", data_part="height", data_row=part))
        sym = "+" if sign == 1 else "−"
        o.append(_label(x0 + 81, 232, "%d %s %d = %d mm" % (a, sym, b, r), size=14,
                        weight="700", fill=_SVG_ACCENT_TEXT, data_part="sum", data_case=str(ci)))
    o.append(_line(170, 8, 170, 238, stroke=_SVG_RULE_STRONG, w=1.5, data_part="divider"))
    return _p6a_open(fig, 244, o)


def _p6a_chain_icon(i, x, y):
    """The small drawing beside each step: a plucked string, layers of air, a thin sheet,
    and a signal. (x, y) is the top left of a 64 by 56 box."""
    cx, cy = x + 32, y + 28
    o = [_rect(x, y, 64, 56, rx=8, fill=_SVG_INSET, stroke=_SVG_INK_MUTED, w=1.5,
               data_part="icon-box", data_step=str(i + 1))]
    if i == 0:      # a string, drawn at both ends of its swing
        o.append(_circle(x + 8, cy, 3, fill=_SVG_INK))
        o.append(_circle(x + 56, cy, 3, fill=_SVG_INK))
        o.append(_path("M %s,%s Q %s,%s %s,%s" % (_n(x + 8), _n(cy), _n(cx), _n(cy - 32), _n(x + 56), _n(cy)),
                       stroke=_SVG_INK, w=2.5, data_part="string"))
        o.append(_path("M %s,%s Q %s,%s %s,%s" % (_n(x + 8), _n(cy), _n(cx), _n(cy + 32), _n(x + 56), _n(cy)),
                       stroke=_SVG_INK_MUTED, w=2, dash="4,4", data_part="string-swing"))
    elif i == 1:    # layers of air, bunched then spread
        for xx in (10, 14, 18, 22, 32, 44, 54):
            o.append(_line(x + xx, y + 12, x + xx, y + 44, stroke=_SVG_INK, w=2, data_part="air-layer"))
    elif i == 2:    # a thin sheet, drawn at both ends of its swing
        o.append(_path("M %s,%s Q %s,%s %s,%s" % (_n(x + 30), _n(y + 8), _n(x + 16), _n(cy), _n(x + 30), _n(y + 48)),
                       stroke=_SVG_INK, w=3, data_part="sheet"))
        o.append(_path("M %s,%s Q %s,%s %s,%s" % (_n(x + 44), _n(y + 8), _n(x + 30), _n(cy), _n(x + 44), _n(y + 48)),
                       stroke=_SVG_INK_MUTED, w=2, dash="4,4", data_part="sheet-swing"))
    else:           # a signal leaving along a wire
        pts = [(x + 6, cy), (x + 14, cy), (x + 19, cy - 14), (x + 27, cy + 14), (x + 35, cy - 14),
               (x + 43, cy + 14), (x + 48, cy)]
        o.append(_path("M " + " L ".join("%s,%s" % (_n(a), _n(b)) for a, b in pts), stroke=_SVG_INK,
                       w=2.5, data_part="signal"))
        o.append(_p6a_arrow(x + 48, cy, x + 60, cy, paint=_SVG_INK, w=2.5, part="signal-arrow"))
    return "".join(o)


def _p6a_sound_chain(fig):
    """How a sound gets from a source to a listener, in four numbered steps down the page:
    a drawing in a box on the left, a title and up to two short lines on the right, and an
    arrow down between the boxes."""
    d = fig.get("data") or {}
    steps = d.get("steps") or []
    if len(steps) != 4:
        raise ValueError("figure %r: p6-sound-chain draws exactly four steps" % fig.get("id"))
    PITCH, TX = 80.0, 88.0
    o = []
    for i, s in enumerate(steps):
        lines = s.get("lines") or []
        if not s.get("title") or not 1 <= len(lines) <= 2:
            raise ValueError("figure %r: step %d needs a title and one or two lines" % (fig.get("id"), i + 1))
        y = 6 + i * PITCH
        o.append(_p6a_chain_icon(i, 8, y))
        o.append(_label(TX, y + 18, "%d  %s" % (i + 1, s["title"]), size=15, weight="700",
                        anchor="start", data_part="step-title", data_step=str(i + 1)))
        for j, ln in enumerate(lines):
            o.append(_label(TX, y + 37 + j * 17, ln, size=13, weight="500", anchor="start",
                            fill=_SVG_INK_BODY, data_part="step-line", data_step=str(i + 1)))
        if i < 3:
            o.append(_p6a_arrow(40, y + 58, 40, y + PITCH, paint=_SVG_INK_MUTED, w=2,
                                part="step-arrow"))
    return _p6a_open(fig, 6 + 3 * PITCH + 62, o)


def _p6a_longitudinal(fig):
    """A loudspeaker and the air in front of it, drawn as layers. The layers crowd together at
    each compression and spread out at each rarefaction. Labels: compression, rarefaction,
    wavelength (one compression to the next), the direction of travel, and one layer of air
    marked to show it moves back and forth along that direction."""
    X0, X1 = 56.0, 334.0
    TOP, BOT = 52.0, 108.0
    LAM, SP = 112.0, 8.0
    C1, C2 = 106.0, 218.0                         # centres of two compressions
    k = 2 * math.pi / LAM
    A = 0.6 / k                                   # spacing runs from 0.4 to 1.6 of the rest spacing
    xs, n = [], 0
    while True:
        rest = X0 + n * SP
        if rest > X1:
            break
        # displacement s(x) = A sin(k (x - C1)): layers move in towards each compression centre
        x = rest - A * math.sin(k * (rest - C1))
        if X0 - 0.01 <= x <= X1:
            xs.append(round(x, 2))
        n += 1
    o = []
    # the loudspeaker: a magnet block and a cone opening to the right
    o.append(_rect(8, 70, 14, 20, rx=2, fill=_SVG_INK, data_part="speaker-magnet"))
    o.append(_path("M 22,72 L 44,%s L 44,%s L 22,88 Z" % (_n(TOP), _n(BOT)), fill=_SVG_INSET,
                   stroke=_SVG_INK, w=2, data_part="speaker-cone"))
    o.append(_p6a_arrow(14, 120, 50, 120, paint=_SVG_INK_MUTED, w=2, both=True, part="cone-arrow"))
    marked = min(xs, key=lambda v: abs(v - 292.0))      # one layer of air, after the second compression
    for x in xs:
        is_m = (x == marked)
        o.append(_line(x, TOP, x, BOT, stroke=_SVG_ACCENT if is_m else _SVG_INK,
                       w=4 if is_m else 2, data_part="air-layer-marked" if is_m else "air-layer"))
    # the direction of travel
    o.append(_label(56, 24, "the sound travels this way", size=13, weight="600", anchor="start",
                    fill=_SVG_INK_BODY, data_part="travel-label"))
    o.append(_p6a_arrow(250, 20, 330, 20, paint=_SVG_INK, w=2.5, part="travel-arrow"))
    # one compression and one rarefaction named, above the layers
    o.append(_label(C1, 44, "compression", size=13, weight="700", data_part="compression-label"))
    o.append(_label(C2 + LAM / 2.0, 44, "rarefaction", size=13, weight="700",
                    data_part="rarefaction-label"))
    # wavelength: one compression centre to the next
    WY = 120.0
    o.append(_line(C1, BOT + 2, C1, WY + 4, stroke=_SVG_INK_MUTED, w=1.5, data_part="wavelength-tick"))
    o.append(_line(C2, BOT + 2, C2, WY + 4, stroke=_SVG_INK_MUTED, w=1.5, data_part="wavelength-tick"))
    o.append(_p6a_arrow(C1, WY, C2, WY, paint=_SVG_ACCENT_TEXT, w=2.5, both=True,
                        part="wavelength-arrow"))
    o.append(_label((C1 + C2) / 2.0, WY + 20, "wavelength", size=14, weight="700",
                    fill=_SVG_ACCENT_TEXT, data_part="wavelength-label"))
    # the marked layer moves back and forth along the direction of travel
    o.append(_p6a_arrow(marked - 18, WY, marked + 18, WY, paint=_SVG_ACCENT_TEXT, w=2.5,
                        both=True, part="layer-arrow"))
    MY = 166.0
    o.append(_label(8, MY, "The marked layer of air moves back and forth.", size=13,
                    weight="700", anchor="start", fill=_SVG_ACCENT_TEXT, data_part="layer-label"))
    return _p6a_open(fig, MY + 10, o)


def _p6a_sound_traces(fig):
    """Four sound traces as a microphone and oscilloscope show them, time across. Each row
    changes one thing: the first keeps the frequency and changes the amplitude, the second
    keeps the amplitude and changes the frequency."""
    d = fig.get("data") or {}
    rows = d.get("rows") or []
    if len(rows) != 2 or any(len(r.get("panels") or []) != 2 for r in rows):
        raise ValueError("figure %r: p6-sound-traces draws two rows of two panels" % fig.get("id"))
    PW, PH = 158.0, 76.0
    o = []
    y = 4.0
    for ri, r in enumerate(rows):
        if not r.get("title"):
            raise ValueError("figure %r: row %d needs a title" % (fig.get("id"), ri))
        o.append(_label(8, y + 14, r["title"], size=13, weight="700", anchor="start",
                        fill=_SVG_INK_BODY, data_part="row-title", data_row=str(ri)))
        py = y + 22
        for pi, p in enumerate(r["panels"]):
            amp, waves = p.get("amp"), p.get("waves")
            if not (p.get("label") and isinstance(amp, (int, float)) and 4 <= amp <= 32
                    and isinstance(waves, int) and 1 <= waves <= 6):
                raise ValueError("figure %r: panel %r needs a label, amp 4 to 32 and whole waves 1 to 6"
                                 % (fig.get("id"), p))
            px = 8.0 + pi * (PW + 8)
            mid = py + PH / 2.0
            o.append(_rect(px, py, PW, PH, rx=6, fill=_SVG_INSET, stroke=_SVG_INK_MUTED, w=1.5,
                           data_part="screen", data_label=p["label"]))
            o.append(_line(px + 6, mid, px + PW - 6, mid, stroke=_SVG_RULE_STRONG, w=1.5,
                           dash="5,4", data_part="rest-line"))
            lam = (PW - 12) / float(waves)
            o.append(_path(_p6a_wave_d(px + 6, px + PW - 6, mid, amp, lam, px + 6 + lam / 4.0),
                           stroke=_SVG_INK, w=2.5, data_part="trace", data_amp=_n(amp),
                           data_waves=str(waves)))
            o.append(_label(px + PW / 2.0, py + PH + 18, p["label"], size=14, weight="700",
                            data_part="panel-label"))
        y = py + PH + 30
    o.append(_label(8, y + 10, "Time goes across each screen.", size=13, weight="500",
                    anchor="start", fill=_SVG_INK_BODY, data_part="time-note"))
    return _p6a_open(fig, y + 18, o)


ART.update({
    "p6-transverse-wave": _p6a_transverse_wave,
    "p6-superposition": _p6a_superposition,
    "p6-sound-chain": _p6a_sound_chain,
    "p6-longitudinal": _p6a_longitudinal,
    "p6-sound-traces": _p6a_sound_traces,
})


# ─── LEAN WAVE 2 (P6 lane B: lessons 6-9), pasted from ~/tmp/lean-ks3-w2/waves/drawers-laneB.py ───
import math
from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_CARD,
    _SVG_INK,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _circle,
    _label,
    _line,
    _n,
    _path,
    _rect,
    _svg_open,
)

_P6B_W = 340


def _p6b_open(fig, h, body):
    return (_svg_open(fig, _P6B_W, int(math.ceil(h)))
            + '<g stroke-linecap="round" stroke-linejoin="round">'
            + "".join(body) + "</g></svg>")


def _p6b_need(fig, keys):
    d = fig.get("data") or {}
    for k in keys:
        if d.get(k) in (None, "", [], {}):
            raise ValueError("figure %r: data has no %r" % (fig.get("id"), k))
    return d


def _p6b_arrow(x1, y1, x2, y2, paint=_SVG_INK, w=2.5, head=8.0, dash=None, **data):
    """A straight arrow from (x1, y1) to (x2, y2), its head at the far end."""
    ang = math.atan2(y2 - y1, x2 - x1)
    a1, a2 = ang + math.radians(150), ang - math.radians(150)
    hx1, hy1 = x2 + head * math.cos(a1), y2 + head * math.sin(a1)
    hx2, hy2 = x2 + head * math.cos(a2), y2 + head * math.sin(a2)
    return (_line(x1, y1, x2, y2, stroke=paint, w=w, dash=dash, **data)
            + _path("M %s,%s L %s,%s L %s,%s" % (_n(hx1), _n(hy1), _n(x2), _n(y2), _n(hx2), _n(hy2)),
                    stroke=paint, w=w))


def _p6b_leader(x1, y1, x2, y2):
    return (_line(x1, y1, x2, y2, stroke=_SVG_INK_MUTED, w=1.5, data_part="leader")
            + _circle(x2, y2, 2.5, fill=_SVG_INK, data_part="leader-end"))


def _p6b_dim(o, x1, x2, y, text, tick=6):
    """A horizontal measuring line with end ticks and a label under its middle."""
    o.append(_line(x1, y, x2, y, stroke=_SVG_INK_MUTED, w=1.5, data_part="dimension"))
    for x in (x1, x2):
        o.append(_line(x, y - tick, x, y + tick, stroke=_SVG_INK_MUTED, w=1.5, data_part="dimension-end"))
    o.append(_label((x1 + x2) / 2.0, y + 20, text, size=14, weight="700", data_part="dimension-label"))


# ── p6-medium-bell-jar: the bell jar, with air and without ───────────────

def _p6b_bell_jar(fig):
    """Two panels side by side. Each: a glass jar on a base plate, a pipe to the
    vacuum pump, and an electric buzzer hanging inside with its hammer beating
    on its bell (drawn with short motion marks in BOTH panels: it never stops).
    The left jar is full of air (dots); sound arcs leave it. The right jar has
    no dots and no arcs.

    data: panels, two {"title", "result", "air": bool}; pump (label under the pipe).
    """
    d = _p6b_need(fig, ("panels", "pump"))
    panels = d["panels"]
    if len(panels) != 2:
        raise ValueError("figure %r: needs exactly two panels" % fig.get("id"))
    o = []
    o.append(_line(170, 8, 170, 244, stroke=_SVG_RULE, w=1.5, data_part="divider"))
    for i, p in enumerate(panels):
        for k in ("title", "result"):
            if not p.get(k):
                raise ValueError("figure %r: panel %d has no %r" % (fig.get("id"), i, k))
        ox = 170 * i
        cx = ox + 80
        o.append(_label(ox + 85, 20, p["title"], size=14, weight="700", data_part="panel-title",
                        data_key=str(i)))
        # the glass jar: straight sides and a domed top, open at the bottom onto the plate
        jar = ("M %s,%s L %s,%s C %s,%s %s,%s %s,%s L %s,%s"
               % (_n(cx - 52), 172, _n(cx - 52), 84, _n(cx - 52), 40, _n(cx + 52), 40,
                  _n(cx + 52), 84, _n(cx + 52), 172))
        o.append(_path(jar + " Z", fill=_SVG_CARD, data_part="jar-inside"))
        if p.get("air"):
            for row, y in enumerate(range(66, 170, 16)):
                for x in range(int(cx - 44) + (row % 2) * 8, int(cx + 46), 16):
                    if abs(x - cx) < 26 and 52 <= y <= 146:
                        continue           # leave the buzzer clear
                    if y < 78 and abs(x - cx) > 34:
                        continue           # stay inside the dome
                    o.append(_circle(x, y, 2.4, fill=_SVG_INK_MUTED, data_part="air-particle"))
        o.append(_path(jar, stroke=_SVG_INK, w=3, data_part="jar"))
        o.append(_rect(cx - 7, 32, 14, 9, rx=2, fill=_SVG_RULE_STRONG, stroke=_SVG_INK, w=2,
                       data_part="jar-knob"))
        # the base plate and the pipe to the pump
        o.append(_rect(cx - 66, 172, 132, 10, rx=2, fill=_SVG_RULE_STRONG, stroke=_SVG_INK, w=2,
                       data_part="plate"))
        o.append(_rect(cx - 5, 182, 10, 16, fill=_SVG_INSET, stroke=_SVG_INK, w=2, data_part="pipe"))
        o.append(_label(cx, 214, d["pump"], size=13, weight="600", fill=_SVG_INK_MUTED,
                        data_part="pump-label"))
        # the buzzer: a wire, a box, a bell, a hammer
        o.append(_line(cx, 44, cx, 82, stroke=_SVG_INK, w=2, data_part="wire"))
        o.append(_rect(cx - 18, 82, 36, 20, rx=3, fill=_SVG_INSET, stroke=_SVG_INK, w=2.5,
                       data_part="buzzer"))
        o.append(_path("M %s,%s C %s,%s %s,%s %s,%s Z"
                       % (_n(cx - 16), 138, _n(cx - 16), 112, _n(cx + 16), 112, _n(cx + 16), 138),
                       fill=_SVG_RULE_STRONG, stroke=_SVG_INK, w=2.5, data_part="bell"))
        o.append(_line(cx + 10, 102, cx + 21, 120, stroke=_SVG_INK, w=2.5, data_part="hammer-arm"))
        o.append(_circle(cx + 21, 121, 4, fill=_SVG_INK, data_part="hammer"))
        for k in (0, 1):               # the hammer is still beating, in both jars
            o.append(_line(cx + 29 + 5 * k, 112 - 4 * k, cx + 33 + 5 * k, 106 - 4 * k,
                           stroke=_SVG_ACCENT_TEXT, w=2, data_part="hammer-moving"))
        if p.get("air"):
            for k, r in enumerate((10, 17, 24)):    # sound leaving the jar
                a0, a1 = math.radians(-35), math.radians(35)
                sx, sy = ox + 136, 124
                o.append(_path("M %s,%s A %s,%s 0 0 1 %s,%s"
                               % (_n(sx + r * math.cos(a0)), _n(sy + r * math.sin(a0)), r, r,
                                  _n(sx + r * math.cos(a1)), _n(sy + r * math.sin(a1))),
                               stroke=_SVG_ACCENT_TEXT, w=2.5, data_part="sound"))
        o.append(_label(ox + 85, 238, p["result"], size=14, weight="700", data_part="result",
                        data_key=str(i)))
    return _p6b_open(fig, 248, o)


# ── p6-medium-rail: one blow, two paths to the listener ──────────────────

def _p6b_rail(fig):
    """A hammer strikes the left end of a long steel rail. A listener stands at the
    right end. One arrow runs along the rail (through the steel), one runs through
    the air above it. A measuring line under the rail gives its length.

    data: length (label); steel, air (the two path labels).
    """
    d = _p6b_need(fig, ("length", "steel", "air"))
    o = []
    x0, x1, ry = 40, 296, 112
    # the air path, above
    o.append(_label(168, 40, d["air"], size=14, weight="700", data_part="path-label", data_key="air"))
    o.append(_p6b_arrow(60, 54, 280, 54, paint=_SVG_INK_MUTED, w=2.5, dash="7,5",
                        data_part="path", data_key="air"))
    # the rail
    o.append(_rect(x0, ry, x1 - x0, 12, rx=2, fill=_SVG_RULE_STRONG, stroke=_SVG_INK, w=2.5,
                   data_part="rail"))
    # the steel path, along the rail
    o.append(_p6b_arrow(60, 100, 280, 100, paint=_SVG_ACCENT_TEXT, w=3, data_part="path",
                        data_key="steel"))
    o.append(_label(168, 90, d["steel"], size=14, weight="700", fill=_SVG_ACCENT_TEXT,
                    data_part="path-label", data_key="steel"))
    # the hammer, its head just touching the left end of the rail
    o.append(_line(14, 66, 30, 104, stroke=_SVG_INK, w=4, data_part="hammer-handle"))
    o.append(_path("M 22,108 L 42,100 L 48,114 L 28,122 Z", fill=_SVG_INK_MUTED, stroke=_SVG_INK,
                   w=2, data_part="hammer-head"))
    # the listener: a head, ear towards the rail
    o.append(_circle(318, 92, 13, fill=_SVG_CARD, stroke=_SVG_INK, w=2.5, data_part="listener"))
    o.append(_path("M 312,98 C 306,98 306,88 312,88", stroke=_SVG_INK, w=2.5, data_part="ear"))
    o.append(_line(318, 105, 318, 136, stroke=_SVG_INK, w=2.5, data_part="listener-body"))
    _p6b_dim(o, x0, x1, 146, d["length"])
    return _p6b_open(fig, 176, o)


# ── p6-echo-boundary: what sound does at a surface ───────────────────────

def _p6b_boundary(fig):
    """Sound arrives from the left at a wall. One arrow goes back (reflected), one
    carries on through to the right (transmitted), and a wavy line dies away inside
    the wall (absorbed). Each is labelled in words.

    data: labels {"in", "reflected", "absorbed", "transmitted", "wall"}.
    """
    d = _p6b_need(fig, ("labels",))
    lab = d["labels"]
    for k in ("in", "reflected", "absorbed", "transmitted", "wall"):
        if not lab.get(k):
            raise ValueError("figure %r: no label %r" % (fig.get("id"), k))
    o = []
    wx0, wx1 = 148, 192
    o.append(_rect(wx0, 30, wx1 - wx0, 130, fill=_SVG_INSET, stroke=_SVG_INK, w=2.5, data_part="wall"))
    for y in range(44, 146, 18):        # hatching, so the wall reads as solid
        o.append(_line(wx0 + 4, y + 10, wx1 - 4, y - 4, stroke=_SVG_RULE_STRONG, w=1.5,
                       data_part="hatch"))
    o.append(_label(170, 22, lab["wall"], size=14, weight="700", data_part="wall-label"))
    # in
    o.append(_label(16, 56, lab["in"], size=14, weight="700", anchor="start", data_part="label",
                    data_key="in"))
    o.append(_p6b_arrow(16, 70, 144, 70, paint=_SVG_INK, w=3, data_part="ray", data_key="in"))
    # reflected: straight on in, so straight back out along the same line. Drawn just
    # below the incoming arrow and parallel to it, so both can be seen.
    o.append(_p6b_arrow(144, 88, 16, 88, paint=_SVG_ACCENT_TEXT, w=3, data_part="ray",
                        data_key="reflected"))
    o.append(_label(16, 114, lab["reflected"], size=14, weight="700", anchor="start",
                    fill=_SVG_ACCENT_TEXT, data_part="label", data_key="reflected"))
    # transmitted: on through, thinner
    o.append(_p6b_arrow(196, 70, 322, 70, paint=_SVG_INK, w=2, dash="6,4", data_part="ray",
                        data_key="transmitted"))
    o.append(_label(324, 56, lab["transmitted"], size=14, weight="700", anchor="end",
                    data_part="label", data_key="transmitted"))
    # absorbed: a wave inside the wall that gets smaller and stops
    pts = []
    for k in range(0, 31):
        x = wx0 + 6 + k
        amp = 7.0 * (1 - k / 30.0)
        pts.append("%s,%s" % (_n(x), _n(110 + amp * math.sin(k * 0.9))))
    o.append(_path("M " + " L ".join(pts), stroke=_SVG_INK, w=2.5, data_part="absorbed-wave"))
    o.append(_label(212, 132, lab["absorbed"], size=14, weight="700", anchor="start",
                    data_part="label", data_key="absorbed"))
    o.append(_p6b_leader(210, 127, 182, 112))
    return _p6b_open(fig, 168, o)


# ── p6-echo-cliff: there and back ────────────────────────────────────────

def _p6b_cliff(fig):
    """A person on the left shouts at a cliff on the right. One arrow goes out to the
    cliff, one comes back. A measuring line on the ground marks the distance to the
    cliff. Two lines of given data sit at the top.

    data: given (one or two lines); there, back (arrow labels); distance (measuring label).
    """
    d = _p6b_need(fig, ("given", "there", "back", "distance"))
    given = d["given"]
    if not 1 <= len(given) <= 2:
        raise ValueError("figure %r: one or two lines of given data" % fig.get("id"))
    o = []
    for i, s in enumerate(given):
        o.append(_label(170, 20 + 18 * i, s, size=14, weight="700", data_part="given", data_key=str(i)))
    gy = 150                           # the ground
    o.append(_line(4, gy, 286, gy, stroke=_SVG_INK, w=2.5, data_part="ground"))
    # the cliff: a rock face rising on the right
    o.append(_path("M 286,%s L 290,%s L 284,86 L 292,64 L 288,52 L 336,52 L 336,%s Z" % (gy, gy - 40, gy),
                   fill=_SVG_INSET, stroke=_SVG_INK, w=2.5, data_part="cliff"))
    for (x1, y1, x2, y2) in ((298, 70, 312, 82), (300, 104, 322, 96), (304, 128, 318, 140)):
        o.append(_line(x1, y1, x2, y2, stroke=_SVG_RULE_STRONG, w=2, data_part="rock"))
    # the person: head, body, legs, an open mouth facing the cliff
    o.append(_circle(26, 92, 10, fill=_SVG_CARD, stroke=_SVG_INK, w=2.5, data_part="person"))
    o.append(_line(26, 102, 26, 128, stroke=_SVG_INK, w=2.5, data_part="person"))
    o.append(_line(26, 128, 18, gy, stroke=_SVG_INK, w=2.5, data_part="person"))
    o.append(_line(26, 128, 34, gy, stroke=_SVG_INK, w=2.5, data_part="person"))
    o.append(_line(26, 110, 36, 116, stroke=_SVG_INK, w=2.5, data_part="person"))
    # out and back
    o.append(_label(160, 66, d["there"], size=14, weight="700", fill=_SVG_ACCENT_TEXT,
                    data_part="path-label", data_key="there"))
    o.append(_p6b_arrow(44, 78, 278, 78, paint=_SVG_ACCENT_TEXT, w=3, data_part="path", data_key="there"))
    o.append(_p6b_arrow(278, 100, 44, 100, paint=_SVG_INK, w=3, data_part="path", data_key="back"))
    o.append(_label(160, 122, d["back"], size=14, weight="700", data_part="path-label", data_key="back"))
    _p6b_dim(o, 26, 286, 162, d["distance"])
    return _p6b_open(fig, 192, o)


# ── p6-ear-parts: the ear and the path to the brain ──────────────────────

def _p6b_spiral(cx, cy, r0, r1, turns, start):
    """An inward spiral as one path of short straight pieces."""
    n = int(48 * turns)
    pts = []
    for k in range(n + 1):
        f = k / float(n)
        a = start + f * turns * 2 * math.pi
        r = r0 + (r1 - r0) * f
        pts.append("%s,%s" % (_n(cx + r * math.cos(a)), _n(cy + r * math.sin(a))))
    return "M " + " L ".join(pts)


def _p6b_ear(fig):
    """A side-on sketch of the ear, left to right: the outer ear flap, the ear canal,
    the eardrum, the three small bones, the coiled cochlea, and the auditory nerve
    running up to the brain. An arrow in the canal shows the way the sound comes in.
    Every part is named, with a leader to it.

    data: labels {"outer", "canal", "eardrum", "bones", "cochlea", "nerve", "brain"}.
    """
    d = _p6b_need(fig, ("labels",))
    lab = d["labels"]
    for k in ("outer", "canal", "eardrum", "bones", "cochlea", "nerve", "brain"):
        if not lab.get(k):
            raise ValueError("figure %r: no label %r" % (fig.get("id"), k))
    o = []
    cy = 112
    # the ear canal: a tube from the outer ear to the eardrum
    o.append(_rect(46, cy - 12, 88, 24, fill=_SVG_INSET, data_part="canal"))
    o.append(_line(46, cy - 12, 134, cy - 12, stroke=_SVG_INK, w=2.5, data_part="canal-wall"))
    o.append(_line(46, cy + 12, 134, cy + 12, stroke=_SVG_INK, w=2.5, data_part="canal-wall"))
    o.append(_p6b_arrow(58, cy, 118, cy, paint=_SVG_INK_MUTED, w=2.5, head=7, data_part="sound-in"))
    # the outer ear flap
    o.append(_path("M 58,54 C 50,38 26,36 18,58 C 8,84 10,140 20,160 C 28,178 48,180 54,166",
                   stroke=_SVG_INK, w=5, data_part="outer-ear"))
    o.append(_path("M 46,%s C 34,%s 30,84 38,72" % (cy - 12, cy - 16), stroke=_SVG_INK, w=3,
                   data_part="outer-ear-fold"))
    o.append(_path("M 46,%s C 34,%s 30,140 38,152" % (cy + 12, cy + 16), stroke=_SVG_INK, w=3,
                   data_part="outer-ear-fold"))
    # the eardrum
    o.append(_path("M 136,%s Q 143,%s 136,%s" % (cy - 20, cy, cy + 20), stroke=_SVG_ACCENT_TEXT, w=4,
                   data_part="eardrum"))
    # the three small bones
    o.append(_line(142, cy - 2, 158, cy - 8, stroke=_SVG_INK, w=2.5, data_part="bone-link"))
    o.append(_line(158, cy - 8, 174, cy, stroke=_SVG_INK, w=2.5, data_part="bone-link"))
    o.append(_path("M 142,%s C 142,%s 150,%s 150,%s C 150,%s 142,%s 142,%s Z"
                   % (cy - 14, cy - 18, cy - 18, cy - 8, cy + 4, cy + 4, cy - 14),
                   fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="bone", data_key="hammer"))
    o.append(_circle(159, cy - 9, 6, fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="bone",
                     data_key="anvil"))
    o.append(_path("M 170,%s L 178,%s L 182,%s L 174,%s Z" % (cy - 6, cy - 6, cy + 8, cy + 8),
                   fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="bone", data_key="stirrup"))
    # the cochlea: a coil, starting where the last bone touches it
    o.append(_path(_p6b_spiral(208, cy, 24, 5, 2.4, math.pi), stroke=_SVG_INK, w=4,
                   data_part="cochlea"))
    # the auditory nerve, up to the brain
    o.append(_path("M 226,%s C 250,%s 262,70 288,56" % (cy - 16, cy - 30), stroke=_SVG_ACCENT_TEXT,
                   w=4, data_part="nerve"))
    o.append(_path("M 288,26 C 300,10 330,12 334,30 C 340,44 328,58 308,56 C 290,58 278,46 288,26 Z",
                   fill=_SVG_INSET, stroke=_SVG_INK, w=2.5, data_part="brain"))
    o.append(_label(309, 41, lab["brain"], size=14, weight="700", data_part="label", data_key="brain"))
    # labels and leaders: a top row and a bottom row, so none can touch
    o.append(_label(6, 26, lab["outer"], size=14, weight="700", anchor="start", data_part="label",
                    data_key="outer"))
    o.append(_p6b_leader(34, 31, 30, 46))
    o.append(_label(150, 50, lab["eardrum"], size=14, weight="700", data_part="label", data_key="eardrum"))
    o.append(_p6b_leader(146, 56, 139, cy - 18))
    o.append(_label(70, 196, lab["canal"], size=14, weight="700", data_part="label", data_key="canal"))
    o.append(_p6b_leader(80, 181, 92, cy + 13))
    o.append(_label(156, 196, lab["bones"], size=14, weight="700", data_part="label", data_key="bones"))
    o.append(_p6b_leader(158, 181, 159, cy + 2))
    o.append(_label(232, 196, lab["cochlea"], size=14, weight="700", data_part="label", data_key="cochlea"))
    o.append(_p6b_leader(226, 181, 212, cy + 22))
    nerve = lab["nerve"].split(" ", 1)
    for i, s in enumerate(nerve):
        o.append(_label(300, 104 + 18 * i, s, size=14, weight="700", data_part="label", data_key="nerve"))
    o.append(_p6b_leader(282, 96, 262, 79))
    return _p6b_open(fig, 206, o)


# ── p6-ear-range: hearing ranges on a times-ten scale ────────────────────

_P6B_FMIN, _P6B_FMAX = 1.0, 300000.0
_P6B_X0, _P6B_X1 = 14.0, 326.0


def _p6b_fx(f):
    span = math.log10(_P6B_FMAX) - math.log10(_P6B_FMIN)
    return _P6B_X0 + (_P6B_X1 - _P6B_X0) * (math.log10(f) - math.log10(_P6B_FMIN)) / span


def _p6b_hz(v):
    """10000 -> '10 000', the way the lesson writes it."""
    s = "%d" % v
    if len(s) > 4:
        s = s[:-3] + " " + s[-3:]
    return s


def _p6b_range(fig):
    """A frequency axis from 1 Hz to 300 000 Hz, each mark ten times the one before.
    The zone below 20 Hz is named infrasound and the zone above 20 000 Hz is named
    ultrasound, each with a dashed boundary and its number. Each listener is a bar
    from the lowest to the highest frequency it hears, with its name and numbers above.

    data: rows, each {"label", "lo", "hi"}; zones {"infra", "human", "ultra"}; axis, note.
    """
    d = _p6b_need(fig, ("rows", "zones", "axis", "note"))
    z = d["zones"]
    for k in ("infra", "human", "ultra"):
        if not z.get(k):
            raise ValueError("figure %r: no zone label %r" % (fig.get("id"), k))
    rows = d["rows"]
    o = []
    top, pitch = 50.0, 42.0
    yax = top + 12 + pitch * len(rows)
    xa, xb = _p6b_fx(20), _p6b_fx(20000)
    o.append(_rect(_P6B_X0, top, xa - _P6B_X0, yax - top, fill=_SVG_INSET, data_part="zone", data_key="infra"))
    o.append(_rect(xb, top, _P6B_X1 - xb, yax - top, fill=_SVG_INSET, data_part="zone", data_key="ultra"))
    o.append(_label(xa - 4, 18, z["infra"], size=13, weight="700", anchor="end", data_part="zone-label",
                    data_key="infra"))
    o.append(_label((xa + xb) / 2.0, 18, z["human"], size=13, weight="700", data_part="zone-label",
                    data_key="human"))
    o.append(_label(xb + 4, 18, z["ultra"], size=13, weight="700", anchor="start", data_part="zone-label",
                    data_key="ultra"))
    # each row's name sits above its bar; a boundary line stops short of any name it would cross
    gaps = []
    for i, r in enumerate(rows):
        y = top + 12 + pitch * i
        text = "%s: %s to %s Hz" % (r.get("label"), _p6b_hz(r.get("lo") or 0), _p6b_hz(r.get("hi") or 0))
        gaps.append((18 - 3, 18 + len(text) * 14 * 0.6 + 3, y, y + 18))
    for x, s in ((xa, "20 Hz"), (xb, "20 000 Hz")):
        y = 46.0                       # starts under its own number, so it never strikes through it
        for (gx0, gx1, gy0, gy1) in gaps:
            if gx0 <= x <= gx1:
                o.append(_line(x, y, x, gy0, stroke=_SVG_INK, w=1.5, dash="5,4", data_part="boundary"))
                y = gy1
        o.append(_line(x, y, x, yax, stroke=_SVG_INK, w=1.5, dash="5,4", data_part="boundary"))
        o.append(_label(x, 40, s, size=13, weight="700", fill=_SVG_ACCENT_TEXT, data_part="boundary-label"))
    for i, r in enumerate(rows):
        for k in ("label", "lo", "hi"):
            if not r.get(k):
                raise ValueError("figure %r: row %d has no %r" % (fig.get("id"), i, k))
        if not _P6B_FMIN <= r["lo"] < r["hi"] <= _P6B_FMAX:
            raise ValueError("figure %r: row %r is off the scale" % (fig.get("id"), r["label"]))
        y = top + 12 + pitch * i
        o.append(_label(18, y + 14, "%s: %s to %s Hz" % (r["label"], _p6b_hz(r["lo"]), _p6b_hz(r["hi"])),
                        size=14, weight="700", anchor="start", data_part="row-label", data_key=r["label"]))
        x1, x2 = _p6b_fx(r["lo"]), _p6b_fx(r["hi"])
        o.append(_rect(x1, y + 20, x2 - x1, 14, rx=3, fill=_SVG_ACCENT, stroke=_SVG_INK, w=2,
                       data_part="range-bar", data_key=r["label"], data_lo=r["lo"], data_hi=r["hi"]))
    o.append(_line(_P6B_X0, yax, _P6B_X1, yax, stroke=_SVG_INK, w=2.5, data_part="axis"))
    for p in range(0, 6):
        f = 10 ** p
        x = _p6b_fx(f)
        o.append(_line(x, yax, x, yax + 6, stroke=_SVG_INK, w=2, data_part="tick"))
        o.append(_label(x, yax + 22, _p6b_hz(f), size=13, weight="600", data_part="tick-label"))
    o.append(_label(170, yax + 42, d["axis"], size=14, weight="700", data_part="axis-label"))
    o.append(_label(170, yax + 60, d["note"], size=13, weight="600", fill=_SVG_INK_MUTED, data_part="axis-note"))
    return _p6b_open(fig, yax + 68, o)


# ── p6-ultra-probe: a pulse, a crack, an echo ────────────────────────────

def _p6b_probe(fig):
    """A steel block seen from the side, with a probe pressed on its top face. A short
    crack lies inside it. One arrow goes down from the probe to the crack, one comes
    back up. A measuring line beside the block marks the depth. The given data sits
    in the right-hand column.

    data: block, probe, crack, depth (labels); given (two to four short lines).
    """
    d = _p6b_need(fig, ("block", "probe", "crack", "depth", "given"))
    given = d["given"]
    if not 2 <= len(given) <= 4:
        raise ValueError("figure %r: two to four lines of given data" % fig.get("id"))
    for s in given:
        if len(s) > 18:
            raise ValueError("figure %r: given line %r is over 18 characters" % (fig.get("id"), s))
    o = []
    bx0, bx1, by0, by1 = 16, 176, 64, 204
    cyk = 146                          # the crack's depth
    o.append(_rect(bx0, by0, bx1 - bx0, by1 - by0, fill=_SVG_INSET, stroke=_SVG_INK, w=2.5,
                   data_part="block"))
    o.append(_label(bx0 + 8, by1 - 10, d["block"], size=14, weight="700", anchor="start",
                    data_part="label", data_key="block"))
    # the probe on the top face
    o.append(_rect(76, 32, 40, 32, rx=4, fill=_SVG_CARD, stroke=_SVG_INK, w=2.5, data_part="probe"))
    o.append(_line(96, 32, 96, 14, stroke=_SVG_INK, w=2.5, data_part="probe-lead"))
    o.append(_label(66, 52, d["probe"], size=14, weight="700", anchor="end", data_part="label",
                    data_key="probe"))
    # the crack: a short jagged line
    o.append(_path("M 74,%s L 84,%s L 94,%s L 104,%s L 114,%s L 122,%s"
                   % (cyk, cyk - 3, cyk + 2, cyk - 2, cyk + 3, cyk), stroke=_SVG_INK, w=4,
                   data_part="crack"))
    o.append(_label(160, 176, d["crack"], size=14, weight="700", anchor="end", data_part="label",
                    data_key="crack"))
    o.append(_p6b_leader(134, 164, 118, cyk + 3))
    # the pulse down and the echo back
    o.append(_p6b_arrow(88, 68, 88, cyk - 8, paint=_SVG_ACCENT_TEXT, w=3, head=7, data_part="pulse",
                        data_key="down"))
    o.append(_p6b_arrow(106, cyk - 8, 106, 68, paint=_SVG_INK, w=3, head=7, data_part="pulse",
                        data_key="back"))
    # the depth, beside the block
    dx = 190
    o.append(_line(dx, by0, dx, cyk, stroke=_SVG_INK_MUTED, w=1.5, data_part="dimension"))
    for y in (by0, cyk):
        o.append(_line(dx - 6, y, dx + 6, y, stroke=_SVG_INK_MUTED, w=1.5, data_part="dimension-end"))
    o.append(_line(bx1, cyk, dx - 6, cyk, stroke=_SVG_INK_MUTED, w=1, dash="3,3", data_part="dimension-guide"))
    o.append(_label(202, (by0 + cyk) / 2.0 + 5, d["depth"], size=14, weight="700", anchor="start",
                    data_part="dimension-label"))
    for i, s in enumerate(given):
        o.append(_label(212, 166 + 18 * i, s, size=14, weight="700", anchor="start", data_part="given",
                        data_key=str(i)))
    return _p6b_open(fig, 166 + 18 * (len(given) - 1) + 14, o)


ART.update({
    "p6-medium-bell-jar": _p6b_bell_jar,
    "p6-medium-rail": _p6b_rail,
    "p6-echo-boundary": _p6b_boundary,
    "p6-echo-cliff": _p6b_cliff,
    "p6-ear-parts": _p6b_ear,
    "p6-ear-range": _p6b_range,
    "p6-ultra-probe": _p6b_probe,
})


# ─── LEAN WAVE 2 (P6 figure fixes, 25 Nov 2026) ───────────────────────────────
#
#   "p6-compression-graph"  data {"labels": {"compression", "rarefaction", "peak", "dip"}}
#                           a row of air particles with compressions and rarefactions, and
#                           under it the wavy line drawn as a graph: peaks under compressions,
#                           dips under rarefactions, joined by dashed guide lines
#   "p6-vibration-count"    data {"heading", "slices", "span", "lines": [..] x1-2,
#                                 "slice_label" (under every slice) or "mark" (first slice)}
#                           a trace cut into one-second slices, for the frequency worked examples
#
# Both 340 wide, labels 13px or more, every colour a --ks3-* token.

def _p6c_need(fig, keys):
    d = fig.get("data") or {}
    for k in keys:
        if not d.get(k):
            raise ValueError("figure %r: data has no %r" % (fig.get("id"), k))
    return d


# ── p6-compression-graph: why sound is drawn as a wavy line ──────────────────

def _p6c_compression_graph(fig):
    """Air particles in four rows, bunched at each compression and spread at each
    rarefaction (the same displacement model as p6-longitudinal). Under them, the
    wavy line: how squashed the air is at each place. Its peaks sit straight under the
    compressions and its dips under the rarefactions; dashed guides join them."""
    d = _p6c_need(fig, ("labels",))
    lab = d["labels"]
    for k in ("compression", "rarefaction", "peak", "dip"):
        if not lab.get(k):
            raise ValueError("figure %r: no label %r" % (fig.get("id"), k))
    X0, X1 = 14.0, 326.0
    LAM, SP = 128.0, 10.0
    C1 = 70.0                                     # a compression centre; others every LAM
    k = 2 * math.pi / LAM
    A = 0.55 / k                                  # spacing runs from 0.45 to 1.55 of the rest spacing
    comps = [C1, C1 + LAM]
    rares = [C1 + LAM / 2.0, C1 + 1.5 * LAM]
    BAND0, BAND1 = 34.0, 84.0
    MID, AMP = 140.0, 26.0
    o = []
    # dashed guides first, so the particles and the line sit on top of them
    for x in comps:
        o.append(_line(x, BAND1 + 4, x, MID - AMP - 3, stroke=_SVG_RULE_STRONG, w=1.5, dash="4,4",
                       data_part="guide", data_key="compression"))
    for x in rares:
        o.append(_line(x, BAND1 + 4, x, MID + AMP - 3, stroke=_SVG_RULE_STRONG, w=1.5, dash="4,4",
                       data_part="guide", data_key="rarefaction"))
    # the air particles
    for row in range(4):
        y = BAND0 + 6 + row * 12.7
        off = SP / 2.0 if row % 2 else 0.0
        n = 0
        while True:
            rest = X0 + off + n * SP
            if rest > X1:
                break
            x = rest - A * math.sin(k * (rest - C1))  # layers move in towards each compression
            if X0 - 0.01 <= x <= X1 + 0.01:
                o.append(_circle(round(x, 2), round(y, 2), 2.2, fill=_SVG_INK_BODY,
                                 data_part="particle"))
            n += 1
    o.append(_label(C1, 22, lab["compression"], size=13, weight="700", data_part="label",
                    data_key="compression"))
    o.append(_label(rares[1], 22, lab["rarefaction"], size=13, weight="700", data_part="label",
                    data_key="rarefaction"))
    # the graph: a rest line, and the wave with its peaks at the compressions
    o.append(_line(X0, MID, X1, MID, stroke=_SVG_RULE_STRONG, w=1.5, dash="5,4", data_part="rest-line"))
    o.append(_path(_p6a_wave_d(X0, X1, MID, AMP, LAM, C1), stroke=_SVG_ACCENT_TEXT, w=3,
                   data_part="trace"))
    o.append(_label(C1 + 8, MID - AMP - 6, lab["peak"], size=13, weight="700", anchor="start",
                    fill=_SVG_ACCENT_TEXT, data_part="label", data_key="peak"))
    o.append(_label(rares[1], MID + AMP + 22, lab["dip"], size=13, weight="700",
                    fill=_SVG_ACCENT_TEXT, data_part="label", data_key="dip"))
    return _p6a_open(fig, MID + AMP + 32, o)


# ── p6-vibration-count: counting vibrations, second by second ────────────────

def _p6c_vibration_count(fig):
    """A trace on a screen, cut into one-second slices by dividers. Either every slice is
    labelled with its count (multiply), or the first slice is picked out (divide). A
    double arrow under the screen marks the whole time, and one or two lines under that
    carry the sum, with the same numbers as the worked example."""
    d = _p6c_need(fig, ("heading", "slices", "span", "lines"))
    n = d["slices"]
    if not (isinstance(n, int) and 1 <= n <= 40):
        raise ValueError("figure %r: slices must be a whole number 1 to 40" % fig.get("id"))
    if not 1 <= len(d["lines"]) <= 2:
        raise ValueError("figure %r: one or two lines under the figure" % fig.get("id"))
    if bool(d.get("slice_label")) == bool(d.get("mark")):
        raise ValueError("figure %r: give slice_label or mark, not both" % fig.get("id"))
    X0, X1 = 14.0, 326.0
    TOP, BOT = 30.0, 86.0
    MID, AMP = (TOP + BOT) / 2.0, 18.0
    sw = (X1 - X0) / n
    cyc = max(1, int(sw // 22))
    lam = sw / cyc
    o = [_label(X0, 18, d["heading"], size=14, weight="700", anchor="start", data_part="heading")]
    o.append(_rect(X0, TOP, X1 - X0, BOT - TOP, rx=6, fill=_SVG_INSET, stroke=_SVG_INK_MUTED, w=1.5,
                   data_part="screen"))
    if d.get("mark"):
        o.append(_rect(X0, TOP, sw, BOT - TOP, fill=_SVG_ACCENT_TINT, data_part="slice-marked"))
    for i in range(1, n):
        x = X0 + i * sw
        o.append(_line(round(x, 2), TOP, round(x, 2), BOT, stroke=_SVG_RULE_STRONG,
                       w=1.5 if n <= 10 else 1, dash="4,3" if n <= 10 else None, data_part="second"))
    o.append(_path(_p6a_wave_d(X0, X1, MID, AMP, lam, X0 + lam / 4.0, step=1.0), stroke=_SVG_INK,
                   w=2.2 if n <= 10 else 1.6, data_part="trace"))
    if d.get("slice_label"):
        for i in range(n):
            o.append(_label(round(X0 + (i + 0.5) * sw, 2), BOT + 20, d["slice_label"], size=14,
                            weight="700", data_part="slice-label"))
    else:
        o.append(_rect(X0, TOP, sw, BOT - TOP, fill="none", stroke=_SVG_ACCENT_TEXT, w=2.5,
                       data_part="slice-marked-edge"))
        o.append(_line(X0 + sw / 2.0, BOT + 2, X0 + sw / 2.0, BOT + 8, stroke=_SVG_ACCENT_TEXT, w=2,
                       data_part="mark-leader"))
        o.append(_label(X0, BOT + 24, d["mark"], size=14, weight="700", anchor="start",
                        fill=_SVG_ACCENT_TEXT, data_part="mark-label"))
    DY = BOT + 44
    for x in (X0, X1):
        o.append(_line(x, DY - 8, x, DY + 8, stroke=_SVG_INK_MUTED, w=1.5, data_part="span-tick"))
    o.append(_p6a_arrow(X0, DY, X1, DY, paint=_SVG_INK, w=2, both=True, part="span-arrow"))
    o.append(_label((X0 + X1) / 2.0, DY + 22, d["span"], size=14, weight="700", data_part="span-label"))
    y = DY + 52
    for s in d["lines"]:
        o.append(_label(X0, y, s, size=14, weight="700", anchor="start", fill=_SVG_ACCENT_TEXT,
                        data_part="sum"))
        y += 20
    return _p6a_open(fig, y - 10, o)


ART.update({
    "p6-compression-graph": _p6c_compression_graph,
    "p6-vibration-count": _p6c_vibration_count,
})
