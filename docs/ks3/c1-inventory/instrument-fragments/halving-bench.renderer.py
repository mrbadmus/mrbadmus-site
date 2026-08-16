# DISPATCH: "halving-bench": ("ks3-cut-block", ' data-instrument data-cutblock data-stage-done="0"'),
#
# Splice `r_halving_bench` into build_ks3.py beside the other instrument
# renderers, add the dispatch row above to ACTIVITY_KIND_RENDERERS, and add
#     if kind == "halving-bench":
#         parts.append(r_halving_bench(a, act_id))
# to r_activity's dispatch run. `_sig` and `_size_label` are module-level
# because the RESTING render needs the same ladder the runtime uses, and two
# copies of a formatter are two answers to "how big is the piece now".

# No new imports: `build_ks3.py` does not import `math`, and the one place
# this needed it (`math.floor(v + .5)`) is `int(v + .5)` for a positive v,
# which every value on this ladder is.


# ── the size ladder (c1-01 page lines 452–464) ───────────────────────────
#
# Engine, not payload (map §1.2): 1 cm / 2ⁿ, formatted mm above 0.1 cm, µm
# above 1e-4 cm, nm below that. It is here in Python AND in `shared/ks3.js`
# for the same reason `_scale_alt` is — the build has to render the resting
# readout and the resting aria-label, and the runtime has to render every
# other state. Same composition, same output, checked at n = 0 and n = FLOOR.
#
# ⚠️ µ is U+00B5 MICRO SIGN, which Bricolage and DM Mono carry and Instrument
# Sans does not. The value lands in the DISPLAY face (`.ks3-cut-value`) and on
# the canvas in mono, so it is covered; a µ in body copy would not be.

def _sig(v):
    """Design's `sig()`, digit for digit — including the one trailing zero.

    ⚠️ `int(v + .5)`, not `round()`. JS `Math.round(312.5)` is 313 and Python's
    `round(312.5)` is 312, and 312.5 µm is a real value on this ladder (five
    cuts in). Banker's rounding here would print a different number in the built
    page from the one the student sees after the first click.
    """
    if v >= 100:
        return str(int(v + 0.5))
    if v >= 10:
        out = "%.1f" % v
        return out[:-2] if out.endswith(".0") else out
    # Design strips ONE trailing zero, then a bare point: 0.60 → 0.6, and
    # 5.00 → 5.0. Reproduced rather than tidied — the ladder's output is
    # printed on the page and in Rung 2's premise.
    out = "%.2f" % v
    if out.endswith("0"):
        out = out[:-1]
    return out[:-1] if out.endswith(".") else out


def _size_label(n, start_cm=1):
    cm = float(start_cm) / (2 ** n)
    if cm >= 0.1:
        return _sig(cm * 10) + " mm"
    if cm >= 1e-4:
        return _sig(cm * 1e4) + " µm"
    return _sig(cm * 1e7) + " nm"


_CUT_SOURCES = {"count", "size", "verdict"}
_CUT_ACTIONS = {"cut", "undo"}
_CUT_DISABLED = {"at_floor", "at_start"}
_CUT_NOTES = ("at_floor", "near_floor", "at_start", "mid")


def r_halving_bench(a, act_id):
    """⊕ c1-01 `#s-cut` — halve a sugar cube until halving runs out.

    ⚖️ THE NUMBERS ARE THE LESSON, NOT THE PICTURE. The lede says so
    ("watch the size, not the picture") and the instrument is built that way:
    three readouts, a scale bar and a progress strip, and a drawing that stays
    deliberately dull until four cuts from the floor. An instrument that made
    the cube prettier every click would teach that small is interesting; this
    one teaches that halving TERMINATES, which is a different claim and the one
    the unit rests on.

    ⚖️ THE FLOOR IS STICKY. `reachedFloor` is a one-way flag on Design's page
    and it stays one-way here: undoing a cut walks the piece back up the ladder
    and does NOT untick the rail. What a student found out at 24 cuts cannot be
    un-found by pressing undo, and MRB-208's rail records participation.

    ⚠️ A LIGHT `check` block. Measured off Design's markup (`ks3-block`, no
    `ks3-dark`), and the sibling on the same page — `#s-gap` — IS ink-dark, so
    the two are a deliberate pair rather than an oversight.

    ⊕ Additions inside the drawn component, both stated in the report:
      * `progress_full` — Design's head counter reads `floor reached` at the
        floor, which `_head_counter`'s format/zero/two-state shapes cannot
        express. Carried on the instrument and swapped in by `wireHalvingBench`.
      * `start_cm` / `grain_at` — Design hard-codes `1 /` and `FLOOR - 4` in
        two functions each. Authored once, read here and in the JS.

    ⚠️ The canvas labels ARE assembled from attributes, which the DOM rule
    forbids. Canvas text is not a DOM node: there is no element to hide and no
    `<em>` to lose, and `fillText` takes a string or nothing. Every DOM-borne
    string in this instrument — the four notes and the two verdict words — is
    emit-both-show-one instead.
    """
    floor = int(a.get("floor") or 0)
    if floor < 1:
        raise ValueError(
            "halving-bench %r declares floor %r; the bench counts down to a "
            "floor and needs a positive one." % (act_id, a.get("floor")))

    readouts = a.get("readouts") or []
    if not readouts:
        raise ValueError("halving-bench %r declares no readouts[]." % act_id)
    for r in readouts:
        if r.get("source") not in _CUT_SOURCES:
            raise ValueError(
                "halving-bench %r readout %r names source %r; the drawn set is "
                "%s." % (act_id, r.get("label"), r.get("source"),
                         ", ".join(sorted(_CUT_SOURCES))))

    buttons = a.get("buttons") or []
    if not buttons:
        raise ValueError("halving-bench %r declares no buttons[]." % act_id)
    for b in buttons:
        if b.get("action") not in _CUT_ACTIONS:
            raise ValueError(
                "halving-bench %r button %r names action %r; the bench does %s."
                % (act_id, b.get("label"), b.get("action"),
                   " and ".join(sorted(_CUT_ACTIONS))))
        if b.get("disabled_when") not in _CUT_DISABLED:
            raise ValueError(
                "halving-bench %r button %r disables on %r; the two ends are "
                "%s." % (act_id, b.get("label"), b.get("disabled_when"),
                         ", ".join(sorted(_CUT_DISABLED))))
        if int(b.get("step") or 0) < 1:
            raise ValueError(
                "halving-bench %r button %r takes step %r; a control that moves "
                "nothing is a control a student presses twice."
                % (act_id, b.get("label"), b.get("step")))

    notes = a.get("notes") or {}
    missing = [k for k in _CUT_NOTES if not notes.get(k)]
    if missing:
        raise ValueError(
            "halving-bench %r is missing note branch(es) %s. All four are "
            "authored — the floor, the grain, the untouched cube and the long "
            "middle — and a missing one would leave the student reading the "
            "previous state's sentence." % (act_id, ", ".join(missing)))

    verdict = a.get("verdict") or {}
    if not (verdict.get("open") and verdict.get("floor")):
        raise ValueError(
            "halving-bench %r needs both verdict words (open and floor)."
            % act_id)

    # ⚠️ The grain threshold squares: the drawing lays out 2^grain across and
    # 4^grain circles in total. Design's 4 gives 16 across and 256 circles, and
    # 6 is already 4,096. Bounded here rather than discovered as a frozen tab.
    grain = int(a.get("grain_at") or 0)
    if not 1 <= grain <= 6:
        raise ValueError(
            "halving-bench %r sets grain_at %r; it must be 1–6, because the "
            "drawing paints 4^grain particles (Design's 4 is 256)."
            % (act_id, a.get("grain_at")))

    alt = a.get("alt") or {}
    for key in ("template", "smooth", "grainy"):
        if not alt.get(key):
            raise ValueError(
                "halving-bench %r alt is missing %r; the readouts are in the "
                "DOM but the piece, the scale bar and the progress strip are "
                "only on the canvas, so this label is the whole drawing for a "
                "screen reader." % (act_id, key))

    labels = a.get("canvas_labels") or {}
    for key in ("ghost", "one", "many", "start", "end"):
        if not labels.get(key):
            raise ValueError(
                "halving-bench %r canvas_labels is missing %r." % (act_id, key))

    start_cm = a.get("start_cm") or 1
    gate_html, hide = r_bench_gate(a.get("gate"))

    # ── the resting state: nothing cut ──
    size0 = _size_label(0, start_cm)
    alt0 = (alt["template"].replace("{n}", "0").replace("{size}", size0)
            .replace("{tail}", alt["grainy"] if 0 >= floor - grain
                     else alt["smooth"]))

    cells = []
    for r in readouts:
        src = r["source"]
        if src == "verdict":
            # Both words in the document, one hidden. The floor word is the one
            # the stylesheet paints in accent-text, so the state is never a
            # colour JS applied.
            value = ('<span data-verdict="open">%s</span>'
                     '<span data-verdict="floor" hidden>%s</span>'
                     % (t(verdict["open"]), t(verdict["floor"])))
        elif src == "size":
            value = t(size0)
        else:
            value = "0"
        cells.append('<div class="ks3-cut-cell">'
                     '<p class="ks3-cut-label">%s</p>'
                     '<p class="ks3-cut-value" data-cut-out="%s">%s</p></div>'
                     % (t(r.get("label", "")), e(src), value))

    btns = []
    for b in buttons:
        # The resting page is at zero cuts, so an at_start control is already
        # spent and says so in the markup rather than waiting for JS.
        off = " disabled" if b["disabled_when"] == "at_start" else ""
        btns.append('<button type="button" class="ks3-sim-seg-btn ks3-cut-btn" '
                    'data-act="%s" data-step="%d" data-dis="%s"%s>%s</button>'
                    % (e(b["action"]), int(b["step"]), e(b["disabled_when"]),
                       off, t(b.get("label", ""))))

    note_ps = "".join(
        '<p data-note="%s"%s>%s</p>'
        % (e(k), "" if k == "at_start" else " hidden", rich(notes[k]))
        for k in _CUT_NOTES)

    canvas = ('<canvas class="ks3-cut-canvas" width="1800" height="640" '
              'role="img" aria-label="%s" data-cut-canvas></canvas>' % e(alt0))

    return (gate_html
            + '<div class="ks3-cut" data-cut%s data-floor="%d" '
              'data-start-cm="%s" data-grain="%d" data-full="%s" '
              'data-alt="%s" data-alt-smooth="%s" data-alt-grainy="%s" '
              'data-label-ghost="%s" data-label-one="%s" data-label-many="%s" '
              'data-label-start="%s" data-label-end="%s">'
              '<div class="ks3-cut-frame">%s'
              '<div class="ks3-cut-foot">'
              '<div class="ks3-cut-readouts">%s</div>'
              '<div class="ks3-cut-btns">%s</div></div></div>'
              '<div class="ks3-cut-note" data-cut-note role="status">%s</div>'
              '</div>'
            % (hide, floor, e(start_cm), grain,
               e(a.get("progress_full") or ""),
               e(alt["template"]), e(alt["smooth"]), e(alt["grainy"]),
               e(labels["ghost"]), e(labels["one"]), e(labels["many"]),
               e(labels["start"]),
               e(labels["end"].replace("{floor}", str(floor))),
               canvas, "".join(cells), "".join(btns), note_ps))
