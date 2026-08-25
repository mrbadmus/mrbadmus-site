"""ks3_art.p8 — P8 *Electric circuits*, the unit where nothing is used up.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p8/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the DRAWING IS MEASURED and the note is reported.

── ⚖️ MRB-204 · TWO BARS AND TWO TRIANGLES IN SEVEN LESSONS ───────────────

    p8-01  no formula figure — a model lesson. Charge in coulombs is GCSE.
    p8-02  no formula figure — a contrast; both its rules are qualitative.
    p8-03  I = a + b                                   a SUM      PART-WHOLE
    p8-04  V = a + b                                   a SUM      PART-WHOLE
    p8-05  V = I × R                                   a PRODUCT  TRIANGLE
    p8-06  V = I × R                                   a PRODUCT  TRIANGLE
    p8-07  no formula figure — a method lesson.

⚖️ **`p8-06` CARRIES THE SAME TRIANGLE AS `p8-05`, AND THE DUPLICATION IS
RULED CLOSED** (Mide, 21 Aug 2026). Her NOTES FLAG 3 asks whether a page that
computes on every state must carry a block and warns that the answer means a
second `R = V ÷ I` triangle three slots after the first. The answer is yes,
and repetition is a feature here rather than a cost: `p8-06` divides 6.0 V by
an ammeter reading in five different unit prefixes, and a student meeting that
without the shape in front of them is doing arithmetic rather than physics.

⚠️ **HER DRAWING HAD ALREADY DONE IT.** The delivered `p8-06` page carries
`#s-formula` — the triangle, both worked examples and both attempts — while
`NOTES-P8-P9.md` §3 still lists the lesson as **no block**. The note is
older than the drawing. Measured, not inferred; see `DEPARTURES-P8.md`.

⚖️ **THE TWO PART–WHOLE BARS KEEP THEIR COVER BUTTONS AND BOTH TRIANGLES KEEP
THEIRS.** `p8-03`'s parts are UNEQUAL — 337 against 213 of a 560-wide whole,
measured off her SVG — because the split at a junction is lopsided and a bar
drawn in halves would teach the very thing `CIRC-09` is.

── ⚠️ `p8-01`'s `#s-think` IS A RAIL STOP, AND IT IS THE ONLY ONE IN THE
   KEY STAGE THAT HAS TO CARRY `data-stage-done` WITHOUT A CONTROL ─────────

Design's `DONE('s-think', s)` on `p8-01` reads `s.gate !== null`: the
misconception block ticks when the bench above it takes the student's
commitment. Every other P8 band stop is a light figure section and goes
through `circ-band`; this one is the amber "Think again" block, so it takes
its own family, `circ-think`, whose whole job is to put Design's two quotes
into the `misconception` shell WITH the `data-stage-done="0"` attribute that
`ks3_parity.check_rail_reachable` reads out of the SHIPPED BYTES.

`confrontation` (ks3_art/core.py) could not do it: its shell carries
`data-instrument data-confront` and no `data-stage-done`, and core.py is a
shared file this lane may not edit. `predict` carries no marker at all, so
the section ships with none of the five signals `doneByDom()` looks for and
the gate — correctly — calls the stop unreachable.

⚠️ It renders NO CONTROL, on its only placement, which is what
`ks3_instrument_liveness` calls STATIC BY DESIGN. That is the same standing
`circ-band` has and the same one `confrontation` and `state-matrix` already
have. A family that gains a control on one page and loses it on another is
the failure that gate exists for; this one has neither.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` ITSELF, with no
opt-out. Nothing here uses any of the four: the band block's payload keys are
`symbols`, `table` and `bars`.

── ⚠️ SHELL CLASSES AND FAMILY NAMES ARE UNIQUE ACROSS THE WHOLE REGISTRY ──

`ks3_art.load()` asserts both since MRB-279. Checked before these were
written, and two obvious stems were already taken: `ks3-cut-block` (C-something
else) and `ks3-fault-block`, which is why `component-under-test` wears
`ks3-cundt-` and `circ-band` draws the fault table rather than a `fault-table`
family of its own.

── ⚠️ THE OHM SIGN IS U+03A9 `Ω`, NEVER U+2126 ────────────────────────────

Design's font law, measured before P8 was authored: the shipped latin subsets
carry the Greek capital omega and do not carry the ohm sign, so U+2126 falls
back to a system font and changes typeface mid-word. Subscript digits are
absent from the same subsets, which is why `p8-03` and `p8-04` label their bar
parts `a` and `b`.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Full words — `easier`, `standard`, `harder`. Never `s` or `h`.
"""

import math

from ks3_art.kit import e, r_cfifa_attempt, rich, t


# ═══ shared P8 primitives ════════════════════════════════════════════════
#
# Deliberately this module's own, not imported from `ks3_art/p6.py`. One
# unit, one module: a helper reached across two unit modules is a shared file
# that nothing says is shared, and `docs/ks3/worktrees.md` §2 is the list of
# files that ARE.

def _seg(cls, label, pressed=False, **attrs):
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _gate(act_id, family, gate, hook):
    """The commit gate every P8 bench opens behind.

    ⚖️ Every one of Design's seven benches is behind one, and every one of
    her `DONE`s for a bench reads `s.gate !== null && …`. A bench read before
    a commitment confirms whatever the student already believed.
    """
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "%s %r has no commit gate. Design puts one in front of all seven "
            "P8 benches and her own DONE reads it." % (family, act_id))
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
    """Design's readout row. `alt` is a SECOND value element in the same tile.

    ⚠️ `alt` exists for exactly one tile in the unit — `p8-06`'s ammeter,
    which reads a mono figure for six of its seven specimens and the sentence
    *"limited by the supply, not by the wire"* for copper. Two elements and a
    `hidden` toggle, because the two are different type at different sizes and
    a single element switching class is a second styling mechanism for one
    readout.
    """
    cells = ""
    for s in specs:
        sub = ('<p class="ks3-%s-tile-sub" data-%s-sub="%s">%s</p>'
               % (hook, hook, e(s["id"]), t(s.get("sub", "")))
               ) if s.get("sub") else ""
        alt = ('<p class="ks3-%s-tile-alt" data-%s-alt="%s" hidden>%s</p>'
               % (hook, hook, e(s["id"]), t(s["alt"]))) if s.get("alt") else ""
        cells += ('<div class="ks3-%s-tile">'
                  '<p class="ks3-%s-tile-label">%s</p>'
                  '<p class="ks3-%s-tile-value%s" data-%s-out="%s">%s</p>%s%s'
                  '</div>'
                  % (hook, hook, t(s["label"]), hook,
                     " ks3-%s-tile-word" % hook if s.get("word") else "",
                     hook, e(s["id"]), t(s.get("value", "—")), alt, sub))
    return '<div class="ks3-%s-tiles">%s</div>' % (hook, cells)


# ⚠️ THERE IS NO `_head()` HERE, AND THAT IS THE POINT.
#
# `r_activity`'s shell ALREADY draws Design's head row — eyebrow on the left,
# `<h2>` under it, the progress readout right-aligned and mono on the same
# line — from the payload's own `eyebrow`, `heading` and `progress`. An
# instrument that draws a second one ships the eyebrow and the heading TWICE,
# one under the other, on every bench in the unit.
#
# ⚠️ MEASURED, IN A BROWSER, NOT REASONED ABOUT. The first cut of this module
# copied P6's `_head()` and every P8 bench duplicated its own title. P6's nine
# benches and its four band blocks do the same thing on the live site today —
# `ks3/physics/waves-and-sound/sound-needs-a-medium.html` carries "At the bench
# · a striker and a microphone" twice, forty characters apart — so this is a
# defect inherited by copying rather than one invented here — measured: its
# nine benches, its wave-anatomy figure and its six wave-band blocks all do
# it. Fixed in THIS unit; P6 is not this lane's to change.
#
# The readout is therefore the shell's `[data-count]`, and `progress` is
# authored as a MAP of named states rather than as a string: a string is read
# as a COUNT FORMAT (MRB-248's widening) and these are not counts.


def _picker(hook, label, tabs):
    return ('<div class="ks3-%s-picker"><p class="ks3-%s-pickerlabel">%s</p>'
            '<div class="ks3-%s-tabrow">%s</div></div>'
            % (hook, hook, t(label), hook, tabs))


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

    Four P8 pages have one, and on all four Design's own `DONE` gives the band
    section the GATE alone while the bench needs the gate AND a control
    touched: `p8-01`'s `s-think`, `p8-02`'s `s-compare`, `p8-06`'s `s-scale`
    and `p8-07`'s `s-fault`. `mirrors` would tick them late; MRB-249's mirror
    map is derived from IDENTICAL expressions and these are not identical.

    ⚠️ A NEAR-MISS KEY SHIPS A DEAD RAIL STOP IN SILENCE, and it did in P6.
    `p6-08` and `p6-09` were authored with `sibling` / `sibling_at`, which
    this function does not read; it returned "" and the wrapper went out with
    no `data-sibling`, so nothing ever ticked. MRB-208's gate cannot see it:
    a band section carries `data-stage-done="0"`, which IS one of the signals
    `doneByDom()` reads, so the stop looks reachable and simply never becomes
    true. The near-miss is an ERROR here for that reason.
    """
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


def _branch_data(hook, branches, need, act_id, family, why=""):
    missing = [k for k in need if not branches.get(k)]
    if missing:
        raise ValueError(
            "%s %r has no note for state(s) %s. %s"
            % (family, act_id, ", ".join(missing), why))
    return "".join(
        '<span data-%s-branch="%s" data-note="%s" hidden></span>'
        % (hook, e(k), e(branches[k])) for k in need)


def _lead(hook, a):
    return ('<p class="ks3-%s-lead">%s</p>' % (hook, rich(a["lead"]))
            if a.get("lead") else "")


def _fills(hook, keys):
    return "".join(
        '<span class="ks3-%s-fill ks3-%s-%s" data-%s-fill="%s"></span>'
        % (hook, hook, k, hook, k) for k in keys)


def _need(a, act_id, family, keys):
    for k in keys:
        if a.get(k) in (None, ""):
            raise ValueError("%s %r has no %r." % (family, act_id, k))


# ═══ p8-01 · #s-loop · one loop, one meter, three places to put it ═══════

def r_circuit_loop(a, act_id):
    """⊕ p8-01 `#s-loop` — move the meter; the reading does not move.

    ⚖️ **THE METER POSITION IS A CONTROL WITH AN AUTHORED CONSEQUENCE, AND
    THE CONSEQUENCE IS THAT NOTHING CHANGES.** That is the whole lesson, and
    it is the one case in the key stage where a dial that alters no number is
    the point rather than a defect. Every branch note therefore names the
    live reading AND says the other two positions give the same — a bench
    that merely failed to move the number would teach nothing.

    ⚖️ **THE LOOP IS ONE BASE PATH WITH A GAP AT EVERY METER POSITION, PLUS A
    COMPUTED PATH THAT BRIDGES THE TWO IT IS NOT IN.** Design's own note for
    the generator. It means the wire is continuous in every state without any
    element being added or removed, and it is why the three positions are
    genuinely interchangeable rather than three drawings.

    ⚠️ **THE CELL PLATES ARE ONE PATH STRING**, built in the wiring. No
    `<sc-for>` inside an `<svg>`, and no per-cell element.

    HOOKS: `data-cloop` (wrapper, `data-volts-per-cell`, `data-amps-per-cell`)
    · `data-cloop-gate` · `data-cloop-gopt` · `data-cloop-body` ·
    `data-cloop-cells` · `data-cloop-sw` · `data-cloop-slot` (carrying the
    slot geometry) · `data-cloop-bridge` · `data-cloop-cellpath` ·
    `data-cloop-lever` · `data-cloop-bulb` · `data-cloop-rays` ·
    `data-cloop-meter` · `data-cloop-meterlabel` · `data-cloop-out` ·
    `data-cloop-note`.
    """
    slots = a.get("slots") or []
    if len(slots) != 3:
        raise ValueError(
            "circuit-loop %r declares %d meter position(s). Design's is three "
            "— before the bulb, after it, and beside the cells — and the set "
            "is the argument: two would let a student read it as a special "
            "case." % (act_id, len(slots)))
    _unique(slots, act_id, "circuit-loop", "meter position")
    for s in slots:
        _need(s, act_id, "circuit-loop slot",
              ("id", "label", "x", "y", "caption", "name", "lx", "ly"))

    cells = a.get("cells") or {}
    _need(cells, act_id, "circuit-loop cells", ("label", "max", "start"))
    if int(cells["max"]) < 2:
        raise ValueError(
            "circuit-loop %r offers %s cell(s). The claim that more push means "
            "a faster flow everywhere at once needs more than one setting."
            % (act_id, cells["max"]))

    slot_tabs = "".join(
        _seg("ks3-seg-btn ks3-cloop-slot", s["label"],
             pressed=(i == int(a.get("start_slot", 0))),
             data_cloop_slot=s["id"], data_x=s["x"], data_y=s["y"],
             data_caption=s["caption"], data_name=s["name"],
             data_lx=s["lx"], data_ly=s["ly"])
        for i, s in enumerate(slots))
    cell_tabs = "".join(
        _seg("ks3-seg-btn ks3-cloop-cells",
             (cells.get("one_label", "1 cell") if n == 1
              else cells.get("many_label", "%d cells") % n),
             pressed=(n == int(cells["start"])), data_cloop_cells=n)
        for n in range(1, int(cells["max"]) + 1))
    sw_tabs = "".join(
        _seg("ks3-seg-btn ks3-cloop-sw", lab,
             pressed=(v == ("1" if a.get("start_closed", True) else "0")),
             data_cloop_sw=v)
        for v, lab in (("1", a.get("closed_label", "Closed")),
                       ("0", a.get("open_label", "Open"))))

    # Design's own 1000×400 viewBox. The gaps in the base path are the three
    # meter positions; `data-cloop-fill` bridges the two the meter is not in.
    svg = (
        '<svg class="ks3-cloop-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-cloop-alt>'
        '<path class="ks3-cloop-wire" d="M120 300 V250 M120 150 V100 H330 '
        'M430 100 H604 M696 100 H880 V158 M880 242 V300 H696 M604 300 H346 '
        'M254 300 H120"/>'
        '<path class="ks3-cloop-wire" data-cloop-bridge d="M0 0"/>'
        '<path class="ks3-cloop-cell" data-cloop-cellpath d="M0 0"/>'
        '<circle class="ks3-cloop-dot" cx="330" cy="100" r="7"/>'
        '<circle class="ks3-cloop-dot" cx="430" cy="100" r="7"/>'
        '<path class="ks3-cloop-lever" data-cloop-lever d="M0 0"/>'
        '<circle class="ks3-cloop-bulb" data-cloop-bulb cx="880" cy="200" '
        'r="42"/>'
        '<path class="ks3-cloop-filament" d="M851 171 L909 229 M909 171 '
        'L851 229"/>'
        '<path class="ks3-cloop-rays" data-cloop-rays d="M0 0"/>'
        '<circle class="ks3-cloop-meter" data-cloop-meter cx="650" cy="100" '
        'r="46"/>'
        '<text class="ks3-cloop-meterletter" data-cloop-meterlabel x="650" '
        'y="115" text-anchor="middle">A</text>'
        '<text class="ks3-cloop-partlabel" x="120" y="365" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-cloop-partlabel" x="380" y="62" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-cloop-partlabel" x="880" y="365" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("cells_label_svg", "CELLS")),
           t(a.get("switch_label_svg", "SWITCH")),
           t(a.get("bulb_label_svg", "BULB"))))

    branches = _branch_data(
        "cloop", a.get("branches") or {}, ("open", "one", "many"), act_id,
        "circuit-loop",
        "The open switch, one cell and more than one cell are the three "
        "things the loop can be doing, and Design authors one note for each.")

    return ('<div class="ks3-cloop" data-cloop data-volts-per-cell="%s" '
            'data-amps-per-cell="%s" data-start-cells="%s" '
            'data-start-closed="%s" data-start-slot="%s"%s>%s%s'
            '<div class="ks3-cloop-body" data-cloop-body hidden>'
            '<div class="ks3-cloop-controls">%s%s%s</div>'
            '<div class="ks3-cloop-figwrap">%s%s</div>%s'
            '<p class="ks3-cloop-note" data-cloop-note></p>%s</div></div>'
            % (e(a.get("volts_per_cell", 1.5)),
               e(a.get("amps_per_cell", 0.15)),
               e(cells["start"]), "1" if a.get("start_closed", True) else "0",
               e(a.get("start_slot", 0)), _sibling(a),
               _lead("cloop", a),
               _gate(act_id, "circuit-loop", a.get("gate") or {}, "cloop"),
               _picker("cloop", cells["label"], cell_tabs),
               _picker("cloop", a.get("switch_label", "The switch"), sw_tabs),
               _picker("cloop", a.get("slot_label",
                                      "Where the ammeter goes"), slot_tabs),
               svg, _fills("cloop", ("reading",)),
               _tiles("cloop", a.get("readouts") or []), branches))


# ═══ p8-02 · #s-bench · the same two bulbs, wired two ways ═══════════════

def r_two_arrangement_loop(a, act_id):
    """⊕ p8-02 `#s-bench` — rewire it, then take one out.

    ⚖️ **THE TWO ARRANGEMENTS ARE TWO WHOLE DRAWINGS, SWITCHED WHOLESALE.**
    Design's own construction, and it is right: a series loop and a parallel
    pair are not one picture with a wire moved, and morphing between them
    would suggest that they are.

    ⚖️ **A REMOVED BULB IS DRAWN AS A DASHED EMPTY CIRCLE, NOT AS A GAP.** The
    socket is still there; what has gone is the filament. In series that empty
    socket is a break in the only path, and the drawing has to let a student
    see the difference between "the bulb is out" and "the bulb is dark".

    ⚖️ **EVERY BRIGHTNESS WORD IS COMPUTED.** `CIRC-05` is *in parallel the
    current is shared out, so each bulb is dimmer*, and the only thing that
    kills it is reading `at full brightness` twice beside a total that has
    doubled. An authored word per control would be a second source for a fact
    the numbers already carry.

    HOOKS: `data-parr` (wrapper) · `data-parr-gate` · `data-parr-gopt` ·
    `data-parr-body` · `data-parr-wire` · `data-parr-out-btn` ·
    `data-parr-fig` (valued `series` / `parallel`) · `data-parr-bulb`
    (valued `1s`/`2s`/`1p`/`2p`) · `data-parr-cross` · `data-parr-rays` ·
    `data-parr-out` · `data-parr-note`.
    """
    _need(a, act_id, "two-arrangement-loop", ("volts", "one_amps"))
    outs = a.get("removals") or []
    if len(outs) != 3:
        raise ValueError(
            "two-arrangement-loop %r declares %d removal state(s). Design's "
            "are both in, bulb 1 out and bulb 2 out — and the two single "
            "removals are not the same state in series, where a student has "
            "to see that it does not matter which one goes."
            % (act_id, len(outs)))

    wire_tabs = "".join(
        _seg("ks3-seg-btn ks3-parr-wire", w["label"],
             pressed=(w["id"] == a.get("start_wire", "series")),
             data_parr_wire=w["id"])
        for w in (a.get("arrangements") or []))
    out_tabs = "".join(
        _seg("ks3-seg-btn ks3-parr-out-btn", o["label"],
             pressed=(int(o["id"]) == int(a.get("start_out", 0))),
             data_parr_out_btn=o["id"])
        for o in outs)

    def bulb(key, cx, cy):
        return ('<circle class="ks3-parr-bulb" data-parr-bulb="%s" cx="%d" '
                'cy="%d" r="40"/>'
                '<path class="ks3-parr-cross" data-parr-cross="%s" d="M0 0"/>'
                '<path class="ks3-parr-rays" data-parr-rays="%s" d="M0 0"/>'
                % (key, cx, cy, key, key))

    meter = ('<circle class="ks3-parr-meter" cx="300" cy="280" r="44"/>'
             '<text class="ks3-parr-meterletter" x="300" y="295" '
             'text-anchor="middle">A</text>')

    # Design's own 1000×360 viewBox, twice — one drawing per arrangement.
    series = (
        '<svg class="ks3-parr-svg" data-parr-fig="series" viewBox="0 0 1000 '
        '360" role="img" aria-label="" data-parr-alt="series">'
        '<path class="ks3-parr-wirepath" d="M120 280 V212 M120 148 V80 H360 '
        'M440 80 H600 M680 80 H880 V280 H120"/>'
        '<path class="ks3-parr-cell" d="M84 154 H156 M104 167 H136 '
        'M84 193 H156 M104 206 H136"/>%s%s%s'
        '<path class="ks3-parr-wirepath" d="M254 280 H120 M344 280 H880"/>'
        '<text class="ks3-parr-partlabel" x="400" y="152" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-parr-partlabel" x="640" y="152" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-parr-partlabel" x="120" y="330" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-parr-partlabel" x="640" y="330" '
        'text-anchor="middle">%s</text></svg>'
        % (bulb("1s", 400, 80), bulb("2s", 640, 80), meter,
           t(a.get("bulb1_label", "BULB 1")),
           t(a.get("bulb2_label", "BULB 2")),
           t(a.get("battery_label", "3.0 V")),
           t(a.get("series_caption", "ONE PATH ROUND"))))

    parallel = (
        '<svg class="ks3-parr-svg" data-parr-fig="parallel" viewBox="0 0 1000 '
        '360" role="img" aria-label="" data-parr-alt="parallel" hidden>'
        '<path class="ks3-parr-wirepath" d="M120 280 V212 M120 148 V80 H740 '
        'M740 80 V140 M740 220 V280 M740 280 H344 M254 280 H120"/>'
        '<path class="ks3-parr-wirepath" d="M440 80 V140 M440 220 V280"/>'
        '<path class="ks3-parr-cell" d="M84 154 H156 M104 167 H136 '
        'M84 193 H156 M104 206 H136"/>'
        '<circle class="ks3-parr-dot" cx="440" cy="80" r="9"/>'
        '<circle class="ks3-parr-dot" cx="440" cy="280" r="9"/>%s%s%s'
        '<text class="ks3-parr-partlabel" x="440" y="46" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-parr-partlabel" x="740" y="46" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-parr-partlabel" x="120" y="330" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-parr-partlabel" x="600" y="330" '
        'text-anchor="middle">%s</text></svg>'
        % (bulb("1p", 440, 180), bulb("2p", 740, 180), meter,
           t(a.get("bulb1_label", "BULB 1")),
           t(a.get("bulb2_label", "BULB 2")),
           t(a.get("battery_label", "3.0 V")),
           t(a.get("parallel_caption",
                   "TWO PATHS, ONE JUNCTION EACH END"))))

    branches = _branch_data(
        "parr", a.get("branches") or {},
        ("series_both", "series_out", "parallel_both", "parallel_out"),
        act_id, "two-arrangement-loop",
        "Arrangement and whether a bulb is out are the two things this bench "
        "changes, and all six reachable states fall in one of the four.")

    return ('<div class="ks3-parr" data-parr data-volts="%s" '
            'data-one-amps="%s" data-start-wire="%s" data-start-out="%s"%s>'
            '%s%s'
            '<div class="ks3-parr-body" data-parr-body hidden>'
            '<div class="ks3-parr-controls">%s%s</div>'
            '<div class="ks3-parr-figwrap">%s%s%s</div>%s'
            '<p class="ks3-parr-note" data-parr-note></p>%s</div></div>'
            % (e(a["volts"]), e(a["one_amps"]),
               e(a.get("start_wire", "series")), e(a.get("start_out", 0)),
               _sibling(a),
               _lead("parr", a),
               _gate(act_id, "two-arrangement-loop", a.get("gate") or {},
                     "parr"),
               _picker("parr", a.get("wire_label", "How they are wired"),
                       wire_tabs),
               _picker("parr", a.get("out_label", "Unscrew a bulb"),
                       out_tabs),
               series, parallel, _fills("parr", ("total",)),
               _tiles("parr", a.get("readouts") or []), branches))


# ═══ p8-03 · #s-junction · two branches, three ammeters ═════════════════

def r_junction_bench(a, act_id):
    """⊕ p8-03 `#s-junction` — change what is in the branches.

    ⚖️ **THE EQUAL STATE IS REAL AND IT HAS ITS OWN BRANCH.** Two lamps, or
    two resistors, or two buzzers, genuinely split the main current in half —
    and the note for that state says in terms that halving works *only*
    because the branches happen to match. `CIRC-09` is *at a junction the
    current halves, because there are two ways to go*, and a bench that never
    reached the equal state would leave a student unable to see that it is a
    special case rather than a rule.

    ⚖️ **THE ZERO STATE IS REAL TOO, AND SO IS ONE-BRANCH-OPEN.** Both
    branches empty is 0.00 A at all three meters with the junction still
    there; one branch empty is the state that shows the surviving branch
    reading exactly what it would read on its own, which is `CIRC-10`.

    ⚖️ **EVERY COMPONENT IS ONE STROKED PATH AND ONE FILLED PATH**, so a
    lamp, a resistor, a buzzer and an empty socket are the same two attributes
    at different values. Design's own note for the generator, and it is why
    the branch drawing never gains or loses an element.

    ⚠️ **THE ARROW WIDTHS ARE THE CURRENTS AND THE LABELS ARE THE NUMBERS.**
    Width alone is never the channel: every arrow has a mono reading beside
    it and a tile under it.

    HOOKS: `data-junc` (wrapper) · `data-junc-gate` · `data-junc-gopt` ·
    `data-junc-body` · `data-junc-a` · `data-junc-b` · `data-junc-comp`
    (valued `a`/`b`) · `data-junc-compfill` · `data-junc-arrow` (valued
    `a`/`b`/`main`) · `data-junc-fill` · `data-junc-out` · `data-junc-note`.
    """
    parts = a.get("parts") or []
    if len(parts) < 4:
        raise ValueError(
            "junction-bench %r offers %d component(s) per branch. Design's "
            "four — lamp, resistor, buzzer and nothing — are what make the "
            "equal split, the uneven split and the open branch all reachable "
            "from the tab row alone." % (act_id, len(parts)))
    _unique(parts, act_id, "junction-bench", "component")
    for p in parts:
        _need(p, act_id, "junction-bench component",
              ("id", "label", "name", "amps", "sub", "shape"))
        if p["shape"] not in ("lamp", "res", "buz", "none"):
            raise ValueError(
                "junction-bench %r component %r asks for shape %r; the four "
                "drawn are lamp, res, buz and none."
                % (act_id, p.get("id"), p["shape"]))
    if not any(float(p["amps"]) == 0 for p in parts):
        raise ValueError(
            "junction-bench %r has no empty-branch component. `I = a + b` "
            "with one part at zero is the state that shows the sum still "
            "holding, and it is the one a deck of live components cannot "
            "reach." % act_id)
    vals = sorted({float(p["amps"]) for p in parts if float(p["amps"]) > 0})
    if len(vals) < 2:
        raise ValueError(
            "junction-bench %r offers one non-zero current, so the split is "
            "even in every reachable state and `it halves` is never "
            "contradicted." % act_id)

    def tabs(side):
        return "".join(
            _seg("ks3-seg-btn ks3-junc-%s" % side, p["label"],
                 pressed=(i == int(a.get("start_%s" % side, 0))),
                 **{"data_junc_%s" % side: p["id"], "data_amps": p["amps"],
                    "data_name": p["name"], "data_sub": p["sub"],
                    "data_shape": p["shape"], "data_label": p["label"]})
            for i, p in enumerate(parts))

    # Design's own 1000×440 viewBox.
    svg = (
        '<svg class="ks3-junc-svg" viewBox="0 0 1000 440" role="img" '
        'aria-label="" data-junc-alt>'
        '<path class="ks3-junc-wire" d="M100 380 V266 M100 201 V100 H208 '
        'M292 100 H760 M100 380 H760 M430 100 V127 M430 203 V232 '
        'M430 308 V380 M760 100 V127 M760 203 V232 M760 308 V380"/>'
        '<path class="ks3-junc-cell" d="M64 214 H136 M84 227 H116 '
        'M64 240 H136 M84 253 H116"/>'
        '<circle class="ks3-junc-dot" cx="430" cy="100" r="9"/>'
        '<circle class="ks3-junc-dot" cx="430" cy="380" r="9"/>'
        '<circle class="ks3-junc-meter" cx="250" cy="100" r="42"/>'
        '<text class="ks3-junc-meterletter" x="250" y="114" '
        'text-anchor="middle">A</text>'
        '<circle class="ks3-junc-meter" cx="430" cy="165" r="38"/>'
        '<text class="ks3-junc-meterletter ks3-junc-meterletter-sm" x="430" '
        'y="178" text-anchor="middle">A</text>'
        '<circle class="ks3-junc-meter" cx="760" cy="165" r="38"/>'
        '<text class="ks3-junc-meterletter ks3-junc-meterletter-sm" x="760" '
        'y="178" text-anchor="middle">A</text>'
        '<path class="ks3-junc-comp" data-junc-comp="a" d="M0 0"/>'
        '<path class="ks3-junc-compfill" data-junc-compfill="a" d="M0 0"/>'
        '<path class="ks3-junc-comp" data-junc-comp="b" d="M0 0"/>'
        '<path class="ks3-junc-compfill" data-junc-compfill="b" d="M0 0"/>'
        '<path class="ks3-junc-arrow" data-junc-arrow="main" d="M0 0"/>'
        '<path class="ks3-junc-arrow" data-junc-arrow="a" d="M0 0"/>'
        '<path class="ks3-junc-arrow" data-junc-arrow="b" d="M0 0"/>'
        '<text class="ks3-junc-partlabel" x="100" y="425" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-junc-partlabel" x="430" y="60" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-junc-partlabel" x="290" y="425" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("battery_label", "3.0 V")),
           t(a.get("junction_label", "JUNCTION")),
           t(a.get("main_label", "MAIN WIRE"))))

    branches = _branch_data(
        "junc", a.get("branches") or {},
        ("none", "one_open", "equal", "uneven"), act_id, "junction-bench",
        "Nothing flowing, one branch open, the branches equal and the "
        "branches unequal are four different sentences, and the equal one is "
        "the state `CIRC-09` is about.")

    return ('<div class="ks3-junc" data-junc data-start-a="%s" '
            'data-start-b="%s">%s%s'
            '<div class="ks3-junc-body" data-junc-body hidden>'
            '<div class="ks3-junc-controls">%s%s</div>'
            '<div class="ks3-junc-figwrap">%s%s</div>%s'
            '<p class="ks3-junc-note" data-junc-note></p>%s</div></div>'
            % (e(a.get("start_a", 0)), e(a.get("start_b", 0)),
               _lead("junc", a),
               _gate(act_id, "junction-bench", a.get("gate") or {}, "junc"),
               _picker("junc", a.get("a_label", "In branch A"), tabs("a")),
               _picker("junc", a.get("b_label", "In branch B"), tabs("b")),
               svg,
               _fills("junc", ("main", "a", "b", "aname", "bname")),
               _tiles("junc", a.get("readouts") or []), branches))


# ═══ p8-04 · #s-volt · one loop, one voltmeter, four places ═════════════

def r_voltmeter_tap(a, act_id):
    """⊕ p8-04 `#s-volt` — move the voltmeter across.

    ⚖️ **THE TWO LEADS ARE ROUTED AT TWO DIFFERENT y LEVELS AND NEVER CROSS.**
    Design's own construction, and it is the whole legibility of the block: a
    voltmeter is defined by having one lead on each of two points, and leads
    that crossed would read as a short.

    ⚖️ **THE WIRE LINK IS A REAL COMPONENT AND IT READS 0.00 V.** That is not
    a degenerate state to be avoided — it is the cleanest demonstration in the
    lesson that a p.d. is a difference and that something with nothing to
    resist the flow has almost no difference across its ends.

    ⚖️ **ACROSS BOTH COMPONENTS READS THE BATTERY'S OWN VALUE**, which is the
    sharing rule seen in a single measurement. `CIRC-15` is *a reading equal
    to the battery's p.d. across one component must be a fault*, and the
    four-position tab row is what makes it obviously not.

    ⚠️ **THE SHARE IS COMPUTED FROM THE RESISTANCES, NEVER AUTHORED.** Two
    lamps split 3.0 V evenly; a lamp and a 20 Ω resistor split it one to two.
    A note that named the larger share as a fixed component would be wrong on
    half the states.

    HOOKS: `data-vtap` (wrapper, `data-lamp-ohms`) · `data-vtap-gate` ·
    `data-vtap-gopt` · `data-vtap-body` · `data-vtap-batt` · `data-vtap-comp`
    · `data-vtap-pos` · `data-vtap-battpath` · `data-vtap-comp2` ·
    `data-vtap-lead` · `data-vtap-tap` · `data-vtap-meter` ·
    `data-vtap-fill` · `data-vtap-out` · `data-vtap-note`.
    """
    comps = a.get("components") or []
    if len(comps) < 3:
        raise ValueError(
            "voltmeter-tap %r offers %d second component(s). Design's three — "
            "a matching lamp, a bigger resistor and a plain wire link — are "
            "an equal share, an unequal share and a zero share, and the three "
            "are what the block is for." % (act_id, len(comps)))
    _unique(comps, act_id, "voltmeter-tap", "component")
    for c in comps:
        _need(c, act_id, "voltmeter-tap component",
              ("id", "label", "name", "ohms", "sub", "shape"))
        if c["shape"] not in ("lamp", "res", "wire"):
            raise ValueError(
                "voltmeter-tap %r component %r asks for shape %r; the three "
                "drawn are lamp, res and wire."
                % (act_id, c.get("id"), c["shape"]))
    if not any(float(c["ohms"]) == 0 for c in comps):
        raise ValueError(
            "voltmeter-tap %r has no zero-resistance component. The wire link "
            "is the state that shows a p.d. really is a DIFFERENCE, and "
            "without it the block never reads 0.00 V anywhere." % act_id)

    pos = a.get("positions") or []
    if len(pos) != 4:
        raise ValueError(
            "voltmeter-tap %r declares %d voltmeter position(s); Design's are "
            "four — the battery, each component, and both at once."
            % (act_id, len(pos)))
    _unique(pos, act_id, "voltmeter-tap", "position")
    for p in pos:
        _need(p, act_id, "voltmeter-tap position",
              ("id", "label", "caption", "name", "lead", "taps"))

    batts = a.get("batteries") or []
    if len(batts) < 2:
        raise ValueError(
            "voltmeter-tap %r offers %d battery setting(s). The shares have "
            "to be seen adding to two different totals, or `the shares add up "
            "to the battery` is one arithmetic coincidence." % (act_id,
                                                                len(batts)))

    batt_tabs = "".join(
        _seg("ks3-seg-btn ks3-vtap-batt", b["label"],
             pressed=(int(b["cells"]) == int(a.get("start_cells",
                                                   batts[0]["cells"]))),
             data_vtap_batt=b["cells"], data_sub=b["sub"])
        for b in batts)
    comp_tabs = "".join(
        _seg("ks3-seg-btn ks3-vtap-comp", c["label"],
             pressed=(i == int(a.get("start_comp", 0))),
             data_vtap_comp=c["id"], data_ohms=c["ohms"], data_name=c["name"],
             data_sub=c["sub"], data_shape=c["shape"])
        for i, c in enumerate(comps))
    pos_tabs = "".join(
        _seg("ks3-seg-btn ks3-vtap-pos", p["label"],
             pressed=(i == int(a.get("start_pos", 0))),
             data_vtap_pos=p["id"], data_caption=p["caption"],
             data_name=p["name"], data_lead=p["lead"], data_taps=p["taps"])
        for i, p in enumerate(pos))

    # Design's own 1000×460 viewBox. The first lamp is a literal path — it is
    # in every state — and only the second component is computed.
    svg = (
        '<svg class="ks3-vtap-svg" viewBox="0 0 1000 460" role="img" '
        'aria-label="" data-vtap-alt>'
        '<path class="ks3-vtap-wire" d="M110 380 V271 M110 206 V110 H340 '
        'M420 110 H620 M700 110 H890 V380 H110"/>'
        '<path class="ks3-vtap-cell" data-vtap-battpath d="M0 0"/>'
        '<path class="ks3-vtap-comp" d="M340 110 a 40 40 0 1 0 80 0 '
        'a 40 40 0 1 0 -80 0 M353 83 L407 137 M407 83 L353 137"/>'
        '<path class="ks3-vtap-comp" data-vtap-comp2 d="M0 0"/>'
        '<path class="ks3-vtap-lead" data-vtap-lead d="M0 0"/>'
        '<path class="ks3-vtap-tap" data-vtap-tap d="M0 0"/>'
        '<circle class="ks3-vtap-meter" cx="500" cy="270" r="46"/>'
        '<text class="ks3-vtap-meterletter" x="500" y="286" '
        'text-anchor="middle">V</text>'
        '<text class="ks3-vtap-partlabel" x="110" y="430" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-vtap-partlabel" x="820" y="430" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("battery_label", "BATTERY")),
           t(a.get("loop_label", "ONE LOOP, ONE CURRENT"))))

    branches = _branch_data(
        "vtap", a.get("branches") or {},
        ("battery", "both", "zero", "share"), act_id, "voltmeter-tap",
        "Across the battery, across both, across something with no "
        "resistance and across one component with a share are four different "
        "readings and four different sentences.")

    return ('<div class="ks3-vtap" data-vtap data-lamp-ohms="%s" '
            'data-volts-per-cell="%s" data-start-cells="%s" '
            'data-start-comp="%s" data-start-pos="%s">%s%s'
            '<div class="ks3-vtap-body" data-vtap-body hidden>'
            '<div class="ks3-vtap-controls">%s%s%s</div>'
            '<div class="ks3-vtap-figwrap">%s%s</div>%s'
            '<p class="ks3-vtap-note" data-vtap-note></p>%s</div></div>'
            % (e(a.get("lamp_ohms", 10)), e(a.get("volts_per_cell", 1.5)),
               e(a.get("start_cells", batts[0]["cells"])),
               e(a.get("start_comp", 0)), e(a.get("start_pos", 0)),
               _lead("vtap", a),
               _gate(act_id, "voltmeter-tap", a.get("gate") or {}, "vtap"),
               _picker("vtap", a.get("batt_label", "The battery"), batt_tabs),
               _picker("vtap", a.get("comp_label", "The second component"),
                       comp_tabs),
               _picker("vtap", a.get("pos_label",
                                     "The voltmeter goes across"), pos_tabs),
               svg, _fills("vtap", ("reading", "lamp", "comp2")),
               _tiles("vtap", a.get("readouts") or []), branches))


# ═══ p8-05 · #s-bench · one component under test ════════════════════════

def r_component_under_test(a, act_id):
    """⊕ p8-05 `#s-bench` — two readings, one division.

    ⚖️ **THE LAMP'S RESISTANCE RISES WITH THE SUPPLY AND THE PAGE NEVER SAYS
    THE RISE IS EVEN.** ⊕ Ruled by Mide, 21 Aug 2026. Design's model is a
    straight line — about 6 Ω at 1.5 V to about 18 Ω at 12 V — and the
    straight line STAYS, because the teaching point is that resistance is not
    fixed and the true concave I–V curve is GCSE. What may not stand is any
    claim that the climb is steady, even, in step, or the same amount each
    time: the model fixes the two ENDS of the rise and makes no claim about
    its shape in between, and her own legal line says exactly that. The
    renderer refuses a payload that says otherwise.

    ⚖️ **THE VERDICT IS COMPUTED FROM THE RATIO ACROSS THE WHOLE SLIDER, NOT
    FROM THE COMPONENT'S NAME.** `CIRC-18` is *a component has one resistance,
    whatever you test it on*, and the tile that kills it says what happens
    when you turn the supply up — which is a property of the model, not a
    label on a tab.

    ⚠️ **THE COMPONENT IS ONE COMPUTED PATH PLUS ONE COMPUTED STYLE**, so a
    thick wire, a thin wire, a resistor and a lamp are the same element at
    different stroke widths and shapes. Design's own note for the generator.

    HOOKS: `data-cundt` (wrapper, `data-lamp-base`, `data-lamp-slope`) ·
    `data-cundt-gate` · `data-cundt-gopt` · `data-cundt-body` ·
    `data-cundt-comp` · `data-cundt-slider` · `data-cundt-comppath` ·
    `data-cundt-flow` · `data-cundt-fill` · `data-cundt-out` ·
    `data-cundt-note`.
    """
    comps = a.get("components") or []
    if len(comps) < 4:
        raise ValueError(
            "component-under-test %r offers %d component(s). The claim is "
            "that the ratio is a property of the component, and it needs "
            "several ohmic ones plus the lamp to be worth making."
            % (act_id, len(comps)))
    _unique(comps, act_id, "component-under-test", "component")
    lamps = [c for c in comps if c.get("band") == "lamp"]
    if len(lamps) != 1:
        raise ValueError(
            "component-under-test %r declares %d filament lamp(s). One is the "
            "counter-example the whole bench is built around."
            % (act_id, len(lamps)))
    for c in comps:
        _need(c, act_id, "component-under-test component",
              ("id", "label", "name", "band", "shape"))
        if c["band"] not in ("low", "high", "lamp"):
            raise ValueError(
                "component-under-test %r component %r is band %r; the three "
                "are low, high and lamp." % (act_id, c.get("id"), c["band"]))
        if c["band"] != "lamp" and not c.get("ohms"):
            raise ValueError(
                "component-under-test %r component %r has no resistance."
                % (act_id, c.get("id")))

    volts = a.get("volts") or []
    if len(volts) < 4:
        raise ValueError(
            "component-under-test %r offers %d supply setting(s). The point "
            "is that the ratio does not move, and two readings cannot show "
            "that." % (act_id, len(volts)))

    # ⚖️ THE STEADINESS SWEEP, RUN AT BUILD TIME (Mide's p8-05 ruling).
    #
    # Not a phrase list. Every string in the payload is read, and any word
    # that asserts the RATE of the lamp's climb is refused — the page may say
    # the resistance rises, and may not say how evenly.
    _refuse_even_rise(a, act_id)

    comp_tabs = "".join(
        _seg("ks3-seg-btn ks3-cundt-comp", c["label"],
             pressed=(i == int(a.get("start_comp", 0))),
             data_cundt_comp=c["id"], data_ohms=c.get("ohms", 0),
             data_band=c["band"], data_name=c["name"], data_shape=c["shape"],
             data_width=c.get("stroke", 0))
        for i, c in enumerate(comps))

    supply = a.get("supply") or {}
    _need(supply, act_id, "component-under-test supply",
          ("label", "min", "max", "step", "start"))

    # Design's own 1000×460 viewBox.
    svg = (
        '<svg class="ks3-cundt-svg" viewBox="0 0 1000 460" role="img" '
        'aria-label="" data-cundt-alt>'
        '<path class="ks3-cundt-wire" d="M110 380 V271 M110 206 V110 H400 '
        'M500 110 H890 V199 M890 291 V380 H110"/>'
        '<path class="ks3-cundt-cell" d="M74 219 H146 M94 232 H126 '
        'M74 245 H146 M94 258 H126"/>'
        '<path class="ks3-cundt-dial" d="M52 285 L168 192 M168 192 L146 194 '
        'M168 192 L166 214"/>'
        '<path class="ks3-cundt-comppath" data-cundt-comppath d="M0 0"/>'
        '<path class="ks3-cundt-lead" d="M404 300 V240 H370 V110 '
        'M496 300 V240 H530 V110"/>'
        '<path class="ks3-cundt-tap" d="M361 110 a 9 9 0 1 0 18 0 '
        'a 9 9 0 1 0 -18 0 Z M521 110 a 9 9 0 1 0 18 0 a 9 9 0 1 0 -18 0 Z"/>'
        '<circle class="ks3-cundt-meter" cx="450" cy="300" r="46"/>'
        '<text class="ks3-cundt-meterletter" x="450" y="316" '
        'text-anchor="middle">V</text>'
        '<circle class="ks3-cundt-meter" cx="890" cy="245" r="46"/>'
        '<text class="ks3-cundt-meterletter" x="890" y="261" '
        'text-anchor="middle">A</text>'
        '<path class="ks3-cundt-flow" data-cundt-flow d="M0 0"/>'
        '<text class="ks3-cundt-partlabel" x="110" y="430" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-cundt-partlabel" x="700" y="430" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("supply_label_svg", "VARIABLE SUPPLY")),
           t(a.get("loop_label", "ONE LOOP, ONE CURRENT"))))

    branches = _branch_data(
        "cundt", a.get("branches") or {}, ("lamp", "low", "high"), act_id,
        "component-under-test",
        "A low ohmic resistance, a high one and the lamp whose ratio climbs "
        "are three different things for this bench to say.")

    return ('<div class="ks3-cundt" data-cundt data-lamp-base="%s" '
            'data-lamp-slope="%s" data-volts="%s" data-start-comp="%s">'
            '%s%s'
            '<div class="ks3-cundt-body" data-cundt-body hidden>'
            '<div class="ks3-cundt-controls">%s%s</div>'
            '<div class="ks3-cundt-figwrap">%s%s</div>%s'
            '<p class="ks3-cundt-note" data-cundt-note></p>%s</div></div>'
            % (e(a.get("lamp_base", 4)), e(a.get("lamp_slope", 1.2)),
               e("|".join(str(v) for v in volts)),
               e(a.get("start_comp", 0)),
               _lead("cundt", a),
               _gate(act_id, "component-under-test", a.get("gate") or {},
                     "cundt"),
               _picker("cundt", a.get("comp_label",
                                      "The component under test"), comp_tabs),
               _slider(act_id, "cundt", supply, "v"),
               svg, _fills("cundt", ("v", "i", "name", "r")),
               _tiles("cundt", a.get("readouts") or []), branches))


# ⚖️ MIDE'S `p8-05` RULING, ENFORCED AT BUILD TIME RATHER THAN BY A SWEEP
# SOMEBODY HAS TO REMEMBER TO RUN.
#
# The filament lamp stays LINEAR — that is the ruling's first half, and the
# reason is pedagogical: what a Year 8 needs from this bench is that
# resistance is not fixed, and the true concave curve is GCSE. The second
# half is that the page may not then assert the rise is EVEN, because the
# straight line is a modelling convenience and a student who reads "rises
# steadily" has been handed a fact the model invented.
#
# The word list is a floor and not the test — the ruling says "sweep by
# concept". These are the forms that actually appear in physics prose about
# a rising quantity; anything else is caught by reading, which is what the
# register row records.
_EVEN_RISE = (
    "steadily", "steady rise", "steady climb", "evenly", "at an even",
    "in step", "constant rate", "steady rate", "even rate", "uniform rate",
    "same amount each", "equal steps in", "straight-line rise",
    "in proportion", "proportional to the p.d", "linearly",
)


def _refuse_even_rise(a, act_id):
    def walk(v, where):
        if isinstance(v, str):
            low = v.lower()
            for phrase in _EVEN_RISE:
                if phrase in low:
                    raise ValueError(
                        "component-under-test %r: %s asserts that the "
                        "filament lamp's resistance rises %r.\n"
                        "⚖️ Ruled by Mide, 21 Aug 2026: the linear model "
                        "STAYS — resistance is not fixed is the teaching "
                        "point and the true concave curve is GCSE — but the "
                        "page may not claim the rise is even. It fixes the "
                        "two ENDS, about 6 ohms at 1.5 V and about 18 at "
                        "12 V, and makes no claim about the shape between "
                        "them. Say that it RISES." % (act_id, where, phrase))
        elif isinstance(v, dict):
            for k, sub in v.items():
                walk(sub, "%s.%s" % (where, k))
        elif isinstance(v, (list, tuple)):
            for i, sub in enumerate(v):
                walk(sub, "%s[%d]" % (where, i))
    walk(a, "the payload")


# ═══ p8-06 · #s-test · a test gap on a fixed supply ═════════════════════

def r_test_gap(a, act_id):
    """⊕ p8-06 `#s-test` — clip a specimen in and divide.

    ⚖️ **THE COPPER STATE REPORTS NO CURRENT, AND SAYS WHY.** ⊕ Ruled by
    Mide, 21 Aug 2026, and Design's delivered page had already drawn it that
    way — 6.0 V ÷ 0.05 Ω is 120 A, which is a division result and not a
    reading, because no school supply delivers it and what limits the current
    in that state is the supply's own internal resistance. So the RESISTANCE
    readout keeps its real value and the CURRENT readout reads *"limited by
    the supply, not by the wire"*. The renderer refuses a payload that prints
    a figure there.

    ⚠️ **COPPER STILL DRAWS ITS BAR AND STILL ANSWERS THE COMPARISON**, on
    the chart beside this bench. It is the reference every other specimen is
    measured against, and a blank row would be worse than the division was.

    ⚖️ **THE ARROW REFUSES TO DRAW BELOW A MICROAMP**, and goes dashed
    between a milliamp and a nanoamp. Two channels, not one: the reading is
    always a number in words as well.

    ⚖️ **THE VERDICT IS COMPUTED FROM THE RESISTANCE AND CARRIES ITS HEDGE.**
    `an insulator, in practice` — the three words are the content of
    `CIRC-21`, and a tile that said `an insulator` would be the claim of zero
    conduction that the same page's own reading contradicts.

    HOOKS: `data-tgap` (wrapper, `data-volts`, `data-copper`) ·
    `data-tgap-gate` · `data-tgap-gopt` · `data-tgap-body` ·
    `data-tgap-spec` · `data-tgap-len` · `data-tgap-flow` · `data-tgap-fill`
    · `data-tgap-out` · `data-tgap-alt` · `data-tgap-note`.
    """
    specs = a.get("specimens") or []
    if len(specs) < 6:
        raise ValueError(
            "test-gap %r offers %d specimen(s). The lesson's whole claim is "
            "that the range is CONTINUOUS, and a deck with a gap in the "
            "middle of it argues the opposite." % (act_id, len(specs)))
    _unique(specs, act_id, "test-gap", "specimen")
    for s in specs:
        _need(s, act_id, "test-gap specimen",
              ("id", "label", "name", "ohms", "carriers"))
    ordered = [float(s["ohms"]) for s in specs]
    if ordered != sorted(ordered):
        raise ValueError(
            "test-gap %r lists its specimens out of resistance order. Design "
            "draws them lowest first because the tab row itself is the "
            "continuum the lesson is about." % act_id)
    if math.log10(ordered[-1] / ordered[0]) < 10:
        raise ValueError(
            "test-gap %r spans %.1f decade(s). The lesson is named after the "
            "fourteen zeros; below ten the chart beside it is a complication "
            "with nothing to buy."
            % (act_id, math.log10(ordered[-1] / ordered[0])))

    short = a.get("short_circuit")
    if not short:
        raise ValueError(
            "test-gap %r names no short-circuit specimen. ⚖️ Ruled 21 Aug "
            "2026: the copper state must NOT print 6.0 V ÷ 0.05 Ω = 120 A. "
            "That is a division result and not a reading — no school supply "
            "delivers it, because the supply's own internal resistance is "
            "what limits the current. Name the specimen whose current reads "
            "`limited by the supply, not by the wire`." % act_id)
    if short not in {s["id"] for s in specs}:
        raise ValueError(
            "test-gap %r names %r as the short-circuit specimen and no "
            "specimen has that id." % (act_id, short))
    for key in ("short_reading", "short_sub", "short_div", "short_mark",
                "short_head"):
        if not a.get(key):
            raise ValueError(
                "test-gap %r has no %r. The copper state replaces a number "
                "with a sentence in five places — the tile, its sub-line, the "
                "division line, the mark on the drawing and the attempt "
                "panel's own head — and a missing one ships the number back."
                % (act_id, key))
    if any(ch.isdigit() for ch in str(a["short_reading"])):
        raise ValueError(
            "test-gap %r: `short_reading` is %r and carries a figure. Nothing "
            "on this page may still say 120 A or imply the wire carried it."
            % (act_id, a["short_reading"]))

    lengths = a.get("lengths") or []
    if len(lengths) != 2:
        raise ValueError(
            "test-gap %r declares %d length(s); Design's control is two, and "
            "the tenfold factor between them is what the second sentence of "
            "every non-copper note names." % (act_id, len(lengths)))

    spec_tabs = "".join(
        _seg("ks3-seg-btn ks3-tgap-spec", s["label"],
             pressed=(i == int(a.get("start_spec", 0))),
             data_tgap_spec=s["id"], data_ohms=s["ohms"], data_name=s["name"],
             data_carriers=s["carriers"], data_label=s["label"])
        for i, s in enumerate(specs))
    len_tabs = "".join(
        _seg("ks3-seg-btn ks3-tgap-len", L["label"],
             pressed=(i == int(a.get("start_len", 0))),
             data_tgap_len=L["mult"], data_word=L["word"])
        for i, L in enumerate(lengths))

    # Design's own 1000×400 viewBox.
    svg = (
        '<svg class="ks3-tgap-svg" viewBox="0 0 1000 400" role="img" '
        'aria-label="" data-tgap-alt>'
        '<path class="ks3-tgap-wire" d="M110 320 V236 M110 171 V100 H380 '
        'M620 100 H890 V164 M890 256 V320 H110"/>'
        '<path class="ks3-tgap-cell" d="M74 184 H146 M94 197 H126 '
        'M74 210 H146 M94 223 H126"/>'
        '<path class="ks3-tgap-clip" d="M380 76 L380 124 L410 100 Z '
        'M620 76 L620 124 L590 100 Z"/>'
        '<rect class="ks3-tgap-specimen" x="404" y="70" width="192" '
        'height="60" rx="8"/>'
        '<circle class="ks3-tgap-meter" cx="890" cy="210" r="46"/>'
        '<text class="ks3-tgap-meterletter" x="890" y="226" '
        'text-anchor="middle">A</text>'
        '<path class="ks3-tgap-flow" data-tgap-flow d="M0 0"/>'
        '<text class="ks3-tgap-partlabel" x="110" y="370" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-tgap-partlabel" x="500" y="46" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("supply_label_svg", "6.0 V FIXED")),
           t(a.get("gap_label", "THE TEST GAP"))))

    branches = _branch_data(
        "tgap", a.get("branches") or {},
        ("short", "good", "poor", "ins", "longer"), act_id, "test-gap",
        "Copper, a conductor, a poor conductor and an insulator are four "
        "bands, and `longer` is the sentence the length control adds to every "
        "state that is not copper.")

    return ('<div class="ks3-tgap" data-tgap data-volts="%s" '
            'data-copper="%s" data-short="%s" data-short-reading="%s" '
            'data-short-sub="%s" data-short-div="%s" data-short-mark="%s" '
            'data-short-head="%s" '
            'data-good-below="%s" data-poor-below="%s" data-start-spec="%s" '
            'data-start-len="%s"%s>%s%s'
            '<div class="ks3-tgap-body" data-tgap-body hidden>'
            '<div class="ks3-tgap-controls">%s%s</div>'
            '<div class="ks3-tgap-figwrap">%s%s</div>%s'
            '<p class="ks3-tgap-note" data-tgap-note></p>%s</div></div>'
            % (e(a.get("volts", 6.0)), e(a.get("copper_ohms", 0.05)),
               e(short), e(a["short_reading"]), e(a["short_sub"]),
               e(a["short_div"]), e(a["short_mark"]), e(a["short_head"]),
               e(a.get("good_below", 100)), e(a.get("poor_below", 100000)),
               e(a.get("start_spec", 0)), e(a.get("start_len", 0)),
               _sibling(a),
               _lead("tgap", a),
               _gate(act_id, "test-gap", a.get("gate") or {}, "tgap"),
               _picker("tgap", a.get("spec_label", "The specimen in the gap"),
                       spec_tabs),
               _picker("tgap", a.get("len_label", "How much of it"),
                       len_tabs),
               svg, _fills("tgap", ("name", "r", "i")),
               _tiles("tgap", a.get("readouts") or []), branches))


# ═══ p8-07 · #s-wire · one lamp, two meters to place ════════════════════

def r_meter_placement(a, act_id):
    """⊕ p8-07 `#s-wire` — wire it wrong on purpose.

    ⚖️ **THE LOOSE CONNECTION DOMINATES, AND THAT IS THE LESSON.** Three
    booleans give eight states and only five sentences, because a break in the
    loop makes both meter positions irrelevant. Design's own branch structure,
    and it is what makes `CIRC-25` — *if a meter reads zero the meter must be
    broken* — meet its answer: the commonest failure in the whole practical
    looks exactly like a broken instrument.

    ⚖️ **BOTH WRONG PLACEMENTS ARE REACHABLE AND THEY FAIL DIFFERENTLY.** An
    ammeter across the lamp shorts it out and the current is limited only by
    the battery; a voltmeter in the loop strangles it and reads almost the
    whole battery p.d. Two failures that both give a dark lamp, distinguished
    by which meter is lying, which is the whole of the fault table beside it.

    ⚠️ **THE SHORT-CIRCUIT AMMETER READS `off the scale` AND NEVER A
    FIGURE.** What a real supply and a real meter do in that state depends on
    the equipment and none of it is a measurement, which her legal line says.
    The renderer refuses a numeric reading there.

    HOOKS: `data-mplace` (wrapper) · `data-mplace-gate` · `data-mplace-gopt`
    · `data-mplace-body` · `data-mplace-a` · `data-mplace-v` ·
    `data-mplace-j` · `data-mplace-bridge` · `data-mplace-alead` ·
    `data-mplace-vlead` · `data-mplace-tap` · `data-mplace-ameter` ·
    `data-mplace-vmeter` · `data-mplace-lamp` · `data-mplace-rays` ·
    `data-mplace-joint` · `data-mplace-out` · `data-mplace-note`.
    """
    for key in ("a_label", "v_label", "j_label"):
        if not a.get(key):
            raise ValueError("meter-placement %r has no %r." % (act_id, key))
    short = a.get("short_reading")
    if not short:
        raise ValueError(
            "meter-placement %r has no `short_reading`. The ammeter across "
            "the lamp is a short circuit, and what flows then depends on the "
            "supply rather than on the circuit — so the tile reads a phrase, "
            "never a figure." % act_id)
    if any(ch.isdigit() for ch in str(short)):
        raise ValueError(
            "meter-placement %r: `short_reading` is %r and carries a figure. "
            "None of it is a measurement." % (act_id, short))

    def two(kind, opts):
        return "".join(
            _seg("ks3-seg-btn ks3-mplace-%s" % kind, o["label"],
                 pressed=(int(o["v"]) == int(a.get("start_%s" % kind, 0))),
                 **{"data_mplace_%s" % kind: o["v"]})
            for o in opts)

    # Design's own 1000×520 viewBox.
    svg = (
        '<svg class="ks3-mplace-svg" viewBox="0 0 1000 520" role="img" '
        'aria-label="" data-mplace-alt>'
        '<path class="ks3-mplace-wire" d="M110 400 V266 M110 201 V140 H456 '
        'M544 140 H730 M810 140 H890 V400 M890 400 H700 M640 400 H370 '
        'M290 400 H110"/>'
        '<path class="ks3-mplace-wire" data-mplace-bridge d="M0 0"/>'
        '<path class="ks3-mplace-cell" d="M74 214 H146 M94 227 H126 '
        'M74 240 H146 M94 253 H126"/>'
        '<circle class="ks3-mplace-lamp" data-mplace-lamp cx="500" cy="140" '
        'r="44"/>'
        '<path class="ks3-mplace-filament" d="M469 109 L531 171 M531 109 '
        'L469 171"/>'
        '<path class="ks3-mplace-rays" data-mplace-rays d="M0 0"/>'
        '<path class="ks3-mplace-lead" data-mplace-alead d="M0 0"/>'
        '<path class="ks3-mplace-lead" data-mplace-vlead d="M0 0"/>'
        '<path class="ks3-mplace-tap" data-mplace-tap d="M0 0"/>'
        '<circle class="ks3-mplace-meter" data-mplace-ameter cx="770" '
        'cy="140" r="40"/>'
        '<text class="ks3-mplace-meterletter" data-mplace-aletter x="770" '
        'y="153" text-anchor="middle">A</text>'
        '<circle class="ks3-mplace-meter" data-mplace-vmeter cx="500" '
        'cy="52" r="40"/>'
        '<text class="ks3-mplace-meterletter" data-mplace-vletter x="500" '
        'y="65" text-anchor="middle">V</text>'
        '<path class="ks3-mplace-joint" data-mplace-joint d="M0 0"/>'
        '<text class="ks3-mplace-partlabel" x="110" y="450" '
        'text-anchor="middle">%s</text>'
        '<text class="ks3-mplace-partlabel" x="500" y="222" '
        'text-anchor="middle">%s</text></svg>'
        % (t(a.get("battery_label", "3.0 V")),
           t(a.get("lamp_label", "LAMP, 10 OHMS"))))

    branches = _branch_data(
        "mplace", a.get("branches") or {},
        ("loose", "shorted", "strangled", "both", "correct"), act_id,
        "meter-placement",
        "Eight states, five sentences: a loose joint dominates whatever the "
        "meters are doing, and the two wrong placements fail in opposite "
        "ways.")

    return ('<div class="ks3-mplace" data-mplace data-start-a="%s" '
            'data-start-v="%s" data-start-j="%s" data-short-reading="%s"%s>'
            '%s%s'
            '<div class="ks3-mplace-body" data-mplace-body hidden>'
            '<div class="ks3-mplace-controls">%s%s%s</div>'
            '<div class="ks3-mplace-figwrap">%s%s</div>%s'
            '<p class="ks3-mplace-note" data-mplace-note></p>%s</div></div>'
            % (e(a.get("start_a", 0)), e(a.get("start_v", 0)),
               e(a.get("start_j", 0)), e(short), _sibling(a),
               _lead("mplace", a),
               _gate(act_id, "meter-placement", a.get("gate") or {},
                     "mplace"),
               _picker("mplace", a["a_label"],
                       two("a", a.get("ammeter") or [])),
               _picker("mplace", a["v_label"],
                       two("v", a.get("voltmeter") or [])),
               _picker("mplace", a["j_label"],
                       two("j", a.get("joint") or [])),
               svg, _fills("mplace", ("a", "v", "joint")),
               _tiles("mplace", a.get("readouts") or []), branches))


# ═══ the band blocks · every fixed figure in the unit ═══════════════════

def r_circ_band(a, act_id):
    """⊕ The figure Design puts beside six of the seven benches.

    ⚖️ **`symbols`, `table` AND `bars`, NOT `cards`.** `cards` is claimed by
    `r_activity` itself with NO opt-out, so a payload using it gets two
    renderers and renders blank. The keys are deliberately different for that
    reason and no other.

    ⚖️ **THE BAND STOP IS TICKED BY THE BENCH BESIDE IT.** These blocks carry
    no control: they are the payoff of the instrument, exactly as MRB-249
    describes, and each bench marks its own band sibling at Design's own
    earlier threshold (`gate !== null`). `mirrors` would tick them late, and
    MRB-249 derives its mirror map from IDENTICAL expressions — which these
    are not.

    Three shapes go through here, and the payload decides which:
      `p8-01`  eight circuit symbols, each a small literal SVG
      `p8-02`  a five-row two-column comparison table
      `p8-04`  a four-row ratings table
      `p8-05`  a six-row two-component results table
      `p8-06`  `#s-scale`, the decade chart — all geometry from logarithms
      `p8-07`  `#s-fault`, the six-row troubleshooting table
    """
    lead = ('<p class="ks3-cband-lead">%s</p>' % rich(a["lead"])
            if a.get("lead") else "")
    close = ('<p class="ks3-cband-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    body = ""
    if a.get("symbols"):
        body += _symbols(a["symbols"], act_id)
    if a.get("table"):
        body += _table(a["table"], act_id)
    if a.get("bars"):
        body += _bars(a["bars"], act_id)

    if not body:
        raise ValueError(
            "circ-band %r renders nothing — no symbols, table or bars. An "
            "empty band block is a section heading with a gap under it."
            % act_id)

    # ⚠️ NO EYEBROW AND NO HEADING HERE — the shell draws both, from the
    # payload's own `eyebrow` and `heading`, before this renderer runs. See
    # the note where `_head` used to be: an instrument that draws its own
    # head ships the title twice, one under the other.
    return ('<div class="ks3-cband" data-cband>%s%s%s</div>'
            % (lead, body, close))


def _symbols(specs, act_id):
    """p8-01's eight-symbol key.

    ⚖️ **EIGHT SYMBOLS, AND THE SET IS THE CLAIM.** A circuit diagram is a
    closed vocabulary, and a key with six of the eight would leave a student
    meeting the seventh on the next page with nothing to look it up in.

    ⚠️ **EVERY LABEL IS A REAL STRING AT BUILD TIME**, so `<text>` is right
    here — MRB-254 forbids one that ships empty and is filled later, and none
    of these ever is. The two that carry a letter, the ammeter and the
    voltmeter, are the only `<text>` elements in the figure and both are
    constants.
    """
    if len(specs) != 8:
        raise ValueError(
            "symbol-key %r draws %d symbol(s). Design's set is eight — cell, "
            "battery, lamp, switch, ammeter, voltmeter, resistor and variable "
            "resistor — and it is chosen to cover the whole unit."
            % (act_id, len(specs)))
    _unique(specs, act_id, "symbol-key", "symbol")
    cells = ""
    for s in specs:
        for f in ("id", "label", "note", "aria_label"):
            if not s.get(f):
                raise ValueError(
                    "symbol-key %r symbol %r has no %r."
                    % (act_id, s.get("id"), f))
        art = ""
        for p in (s.get("paths") or []):
            art += ('<path class="ks3-cband-symstroke" d="%s" '
                    'style="stroke-width:%s"/>' % (e(p["d"]), e(p.get("w", 5))))
        for c in (s.get("circles") or []):
            art += ('<circle class="ks3-cband-symstroke" cx="%s" cy="%s" '
                    'r="%s" style="stroke-width:%s"/>'
                    % (e(c["cx"]), e(c["cy"]), e(c["r"]), e(c.get("w", 5))))
        for r in (s.get("rects") or []):
            art += ('<rect class="ks3-cband-symstroke" x="%s" y="%s" '
                    'width="%s" height="%s" rx="%s" style="stroke-width:%s"/>'
                    % (e(r["x"]), e(r["y"]), e(r["w"]), e(r["h"]),
                       e(r.get("rx", 4)), e(r.get("sw", 5))))
        if s.get("letter"):
            art += ('<text class="ks3-cband-symletter" x="90" y="54" '
                    'text-anchor="middle">%s</text>' % t(s["letter"]))
        if not art:
            raise ValueError(
                "symbol-key %r symbol %r draws nothing."
                % (act_id, s.get("id")))
        cells += ('<div class="ks3-cband-symcard">'
                  '<svg class="ks3-cband-symsvg" viewBox="0 0 180 80" '
                  'role="img" aria-label="%s">%s</svg>'
                  '<p class="ks3-cband-symname">%s</p>'
                  '<p class="ks3-cband-symnote">%s</p></div>'
                  % (e(s["aria_label"]), art, t(s["label"]), t(s["note"])))
    return '<div class="ks3-cband-symbols">%s</div>' % cells


def _table(spec, act_id):
    """The four fixed tables — p8-02, p8-04, p8-05 and p8-07.

    ⚖️ **EVERY ROW HAS A ROW HEADER, and it is a `<th scope="row">.`** These
    are not layout grids: each row is a named thing being described, and a
    screen reader that cannot say which row a cell belongs to is reading a
    list of unattached phrases.

    ⚠️ **THE SCROLLER IS `position: relative`.** An absolutely positioned
    element inside a scroller with no positioned ancestor resolves against the
    page and widens the document on a phone. Nothing here is absolutely
    positioned today; the rule is cheap and the failure is silent.

    A cell may declare `span: True` to run to the end of the row — Design's
    `p8-04` last row does exactly that, because a battery's rating is not the
    same kind of fact as a component's and forcing it into the two columns
    would have made it look like one.
    """
    cols = spec.get("columns") or []
    rows = spec.get("rows") or []
    if len(cols) < 2:
        raise ValueError(
            "band-table %r declares %d column(s). A table with one column is "
            "a list." % (act_id, len(cols)))
    if len(rows) < 3:
        raise ValueError(
            "band-table %r draws %d row(s)." % (act_id, len(rows)))
    head = "".join('<th scope="col">%s</th>' % t(c) for c in cols)
    body = ""
    for r in rows:
        if not r.get("head"):
            raise ValueError(
                "band-table %r has a row with no row header. Every row here "
                "is a named thing being described." % act_id)
        cells = ""
        for c in (r.get("cells") or []):
            if isinstance(c, dict):
                cells += ('<td%s>%s</td>'
                          % (' colspan="%d"' % (len(cols) - 1)
                             if c.get("span") else "", rich(c.get("text", ""))))
            else:
                cells += "<td>%s</td>" % rich(c)
        # A `same` row lightens its ROW HEADER and nothing else — the word
        # `same resistor` is what carries the meaning and the weight is the
        # redundant second channel. No class on the `<tr>`: an unstyled one
        # is a hook nothing reads.
        body += ('<tr><th scope="row"%s>%s</th>%s</tr>'
                 % (' class="ks3-cband-samehead"' if r.get("same") else "",
                    t(r["head"]), cells))
    return ('<div class="ks3-cband-scroll">'
            '<table class="ks3-cband-table" style="min-width:%dpx">'
            '<thead><tr><th scope="col">%s</th>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            % (int(spec.get("min_width", 620)),
               t(spec.get("corner", "")), head, body))


def _bars(spec, act_id):
    """p8-06 `#s-scale` — seven resistances on an axis of fourteen decades.

    ⚖️ **ALL GEOMETRY IS COMPUTED FROM LOGARITHMS AT BUILD TIME**, so the
    chart is in the bytes rather than assembled in JS. It never changes: it is
    the fixed counterpart of the live bench above it. Measured against
    Design's own drawing — her copper bar is 34px, nichrome 100, pencil lead
    170, salt water 224, tap water 322, dry wood 424, plastic 697, on an axis
    from x=180 to x=863 — and the logarithms reproduce every one of them to
    the pixel.

    ⚖️ **THE BOUNDARY IS DASHED AND ITS LABEL SAYS `NO SHARP LINE`.** It is a
    convenience, not a real dividing line, and the figure has to say so on its
    own face rather than in a caption a reader may not reach. `_bars` refuses
    a boundary with no label.

    ⚖️ **BAR TONE IS DERIVED FROM THE BOUNDARY, NEVER AUTHORED PER ROW.** Two
    rows sit above it and five below, and a hand-assigned tone would be free
    to disagree with the line drawn through them. Every bar also carries its
    own value in words, so tone is the redundant channel and never the only
    one.
    """
    rows = spec.get("rows") or []
    if len(rows) < 5:
        raise ValueError(
            "decade-bars %r draws %d row(s). The point is the RANGE, and a "
            "range needs the whole of it." % (act_id, len(rows)))
    _unique(rows, act_id, "decade-bars", "row", key="label")
    for r in rows:
        for f in ("label", "ohms", "value"):
            if not r.get(f):
                raise ValueError(
                    "decade-bars %r row %r has no %r. Every bar carries its "
                    "own resistance in words; bar length is never the only "
                    "channel." % (act_id, r.get("label"), f))
    bound = spec.get("boundary") or {}
    if not bound.get("ohms") or not bound.get("label"):
        raise ValueError(
            "decade-bars %r has no labelled boundary. The line is the "
            "lesson's one hedge made visible — `no sharp line`, `roughly "
            "where useful conduction gives out` — and an unlabelled dash is "
            "a claim that there IS a line." % act_id)

    lo = float(spec.get("axis_min", 0.01))
    hi = float(spec.get("axis_max", 1e14))
    X0, X1 = 180.0, 863.0
    decades = math.log10(hi / lo)
    ROW, TOP, H = 42, 64, 28
    AXIS_Y = TOP + len(rows) * ROW + 8

    def xf(ohms):
        return X0 + (math.log10(float(ohms) / lo) / decades) * (X1 - X0)

    body = ('<path class="ks3-cband-axis" d="M%.0f 60 V%.0f"/>'
            '<path class="ks3-cband-axis" d="M%.0f %.0f H970"/>'
            % (X0, AXIS_Y, X0, AXIS_Y))

    ticks, labels = "", ""
    for tk in (spec.get("ticks") or []):
        x = xf(tk["ohms"])
        ticks += "M%.0f %.0f v12 " % (x, AXIS_Y)
        labels += ('<text class="ks3-cband-ticklabel" x="%.0f" y="%.0f" '
                   'text-anchor="middle">%s</text>'
                   % (x, AXIS_Y + 34, t(tk["label"])))
    body += ('<path class="ks3-cband-tick" d="%s"/>%s' % (ticks.strip(),
                                                          labels))
    body += ('<text class="ks3-cband-axisnote" x="575" y="%.0f" '
             'text-anchor="middle">%s</text>'
             % (AXIS_Y + 60, t(spec.get("axis_note", ""))))

    bx = xf(bound["ohms"])
    body += '<path class="ks3-cband-bound" d="M%.0f 52 V%.0f"/>' % (bx, AXIS_Y)
    for i, line in enumerate(bound["label"] if isinstance(bound["label"], list)
                             else [bound["label"]]):
        body += ('<text class="ks3-cband-boundlabel" x="%.0f" y="%d">%s</text>'
                 % (bx + 8, 26 + i * 20, t(line)))

    for i, r in enumerate(rows):
        y = TOP + i * ROW
        w = max(4.0, xf(r["ohms"]) - X0)
        above = float(r["ohms"]) >= float(bound["ohms"])
        body += ('<rect class="ks3-cband-bar%s" x="%.0f" y="%d" width="%.0f" '
                 'height="%d" rx="5"/>'
                 '<text class="ks3-cband-rowlabel" x="170" y="%d" '
                 'text-anchor="end">%s</text>'
                 '<text class="ks3-cband-rowvalue" x="%.0f" y="%d">%s</text>'
                 % (" ks3-cband-bar-high" if above else "", X0, y, w, H,
                    y + 21, t(r["label"]), X0 + w + 10, y + 21,
                    t(r["value"])))

    return ('<div class="ks3-cband-chartwrap">'
            '<svg class="ks3-cband-chart" viewBox="0 0 1000 %d" role="img" '
            'aria-label="%s">%s</svg></div>'
            % (AXIS_Y + 76, e(spec.get("aria_label", "")), body))


# ═══ p8-01 · #s-think · the one confrontation that is a rail stop ═══════

def r_circ_think(a, act_id):
    """⊕ `p8-01`'s `#s-think`, in the misconception shell, WITH a completion.

    Design's `DONE('s-think', s)` on that page reads `s.gate !== null` — the
    block ticks when the bench above it takes the student's commitment. That
    is a `markSibling` from the bench, and `markSibling` writes
    `data-stage-done`; but `ks3_parity.check_rail_reachable` reads the SHIPPED
    BYTES, so the attribute has to be in the built page at 0 before anything
    is pressed. Neither `confrontation` nor `predict` emits one.

    So this family exists to put Design's two quotes into the amber "Think
    again" shell WITH the attribute. It renders the same three classes
    `r_confrontation` does — `.ks3-mis-quote`, `.ks3-mis-body` and the
    `.ks3-mis-next` divider — so nothing about the treatment moves.

    ⚠️ **NO `statements`, `targets` OR `paragraphs` ON THE ACTIVITY.** The
    `misconception` block type calls `r_confrontation` first and would render
    the quotes a second time from any of the three.
    """
    quotes = a.get("quotes") or []
    if len(quotes) != 2:
        raise ValueError(
            "circ-think %r declares %d quote(s). Design draws two wrong ideas "
            "behind an amber divider on every P8 page, and one on its own "
            "loses the pairing." % (act_id, len(quotes)))
    for bad in ("statements", "targets", "paragraphs"):
        if a.get(bad):
            raise ValueError(
                "circ-think %r carries %r. The `misconception` block type "
                "runs `r_confrontation` before this drawer, so the quotes "
                "would render twice." % (act_id, bad))
    out = ""
    for i, q in enumerate(quotes):
        if not q.get("quote") or not q.get("body"):
            raise ValueError(
                "circ-think %r quote %d has no quote or no body."
                % (act_id, i + 1))
        inner = ('<p class="ks3-mis-quote">%s</p>' % t(_quoted(q["quote"])))
        for para in q["body"]:
            inner += '<p class="ks3-mis-body">%s</p>' % rich(para)
        out += ('<div class="ks3-mis-next">%s</div>' % inner) if i else inner
    return '<div class="ks3-cthink" data-cthink>%s</div>' % out


def _quoted(s):
    """Curly quotation marks round a wrong idea, as `r_confrontation` does."""
    s = str(s or "").strip()
    if s.startswith("“"):
        return s
    return "“%s”" % s


# ═══ the CFIFA attempt ═══════════════════════════════════════════════════

def r_p8_attempt(a, act_id):
    """⊕ P8's half of Design's CFIFA: the student's own five lines.

    The drawing is `ks3_art.kit.r_cfifa_attempt`, shared with P4, P5 and P6.
    The FAMILY is P8's own, so `ks3_art.load()`'s one-family-one-module rule
    holds and the placement gates see it as this unit's.

    ⚠️ **DESIGN'S `p8-06` QUESTION 2 IS `mode: 'pick'` AND THIS KIT IS
    WRITE-IT-OUT ONLY.** Her own README says seven of the eight P8 attempts
    are write-it-out and that `p8-06`'s second keeps the lighter
    pick-the-line variant. The kit has one shape — five inputs, a Check
    button and a self-marked reveal — so that question ships as write-it-out
    with HER five model lines, HER head and HER closing sentence. It is the
    one register row in `DEPARTURES-P8.md` that is a capability difference
    rather than a judgement.
    """
    # ⊕ ONE EYEBROW, NOT TWO (as P7): the `check` shell already prints this
    # activity's eyebrow in Design's `.ks3-blockhead`; `eyebrow: None` tells
    # the kit it is already printed. P4–P6 still print it twice (measured).
    html = r_cfifa_attempt(dict(a, eyebrow=None), act_id, "p8cfa")
    # ⚖️ HER `blockedProgress` — the readout while `p8-06`'s copper short
    # leaves nothing to divide: "Waiting on a specimen the ammeter can read".
    # Carried on the wrapper so `paintAttemptP8` can print it while blocked.
    q1 = (a.get("questions") or [{}])[0]
    if q1.get("blocked_progress"):
        html = html.replace(
            '<div class="ks3-cfa" data-p8cfa ',
            '<div class="ks3-cfa" data-p8cfa data-blocked-progress="%s" '
            % e(q1["blocked_progress"]), 1)
    return html


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. Every family is P8's own — `ks3_art/core.py` is
# untouched. Shell stems checked against the whole registry first: two
# obvious ones were already taken (`ks3-cut-block`, `ks3-fault-block`).

ART = {}

KIND_SHELL = {
    'circuit-loop':          ("ks3-cloop-block",
                              ' data-instrument data-cloopblock '
                              'data-stage-done="0"'),
    'two-arrangement-loop':  ("ks3-parr-block",
                              ' data-instrument data-parrblock '
                              'data-stage-done="0"'),
    'junction-bench':        ("ks3-junc-block",
                              ' data-instrument data-juncblock '
                              'data-stage-done="0"'),
    'voltmeter-tap':         ("ks3-vtap-block",
                              ' data-instrument data-vtapblock '
                              'data-stage-done="0"'),
    'component-under-test':  ("ks3-cundt-block",
                              ' data-instrument data-cundtblock '
                              'data-stage-done="0"'),
    'test-gap':              ("ks3-tgap-block",
                              ' data-instrument data-tgapblock '
                              'data-stage-done="0"'),
    'meter-placement':       ("ks3-mplace-block",
                              ' data-instrument data-mplaceblock '
                              'data-stage-done="0"'),
    'circ-band':             ("ks3-cband-block",
                              ' data-instrument data-cbandblock '
                              'data-stage-done="0"'),
    'circ-think':            ("ks3-cthink-block",
                              ' data-instrument data-cthinkblock '
                              'data-stage-done="0"'),
    'p8-attempt':            ("ks3-p8cfa-block",
                              ' data-instrument data-p8cfablock '
                              'data-stage-done="0"'),
}

KIND_FN = {
    'circuit-loop':          r_circuit_loop,
    'two-arrangement-loop':  r_two_arrangement_loop,
    'junction-bench':        r_junction_bench,
    'voltmeter-tap':         r_voltmeter_tap,
    'component-under-test':  r_component_under_test,
    'test-gap':              r_test_gap,
    'meter-placement':       r_meter_placement,
    'circ-band':             r_circ_band,
    'circ-think':            r_circ_think,
    'p8-attempt':            r_p8_attempt,
}
