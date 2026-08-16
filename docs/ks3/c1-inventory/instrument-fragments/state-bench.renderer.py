# DISPATCH: "state-bench": ("ks3-sbench-block", ' data-instrument data-sbenchblock data-stage-done="0"'),
#
# Splice `r_state_bench` into build_ks3.py beside the other C1 instruments, and
# add `if kind == "state-bench": parts.append(r_state_bench(a, act_id))` to
# `r_activity`'s dispatch run.


def r_state_bench(a, act_id):
    """⊕ c1-02 `#s-bench` — one substance, three arrangements, on a canvas.

    ⚠️ A LIGHT `.ks3-block`, not a practical. c1-02 is the only C1 lesson with
    no dark ground but the hook and the keynote (map §2.3), and the particle
    drawing is cream-on-cream: painting the shell ink would resolve every text
    token wrong and put a #FFFDF8 canvas on a #221E1B block.

    ⚖️ THE FIXED-SIZE REFERENCE PARTICLE IS THE LESSON. NOTES §3 flag 3 names
    it non-negotiable, and it is: one particle, the same radius as every
    particle in every state, captioned, drawn under the box in all three states
    and in every setting. It is the visible form of the sentence the whole
    lesson defends — the particles do not change, the spaces do. So
    `reference_particle` is REQUIRED and this raises without it, rather than
    rendering a bench that has quietly lost its argument to a layout tidy-up.

    ⚖️ EIGHT NOTES, ALL IN THE DOCUMENT, SEVEN HIDDEN. squash × 2, paths × 3,
    resting × 3. Emit-both-show-one rather than a `textContent` swap out of an
    attribute: these are the sentences that carry the science, and rebuilding
    one in JS is how an `<em>` gets eaten and how a string ends up living in an
    attribute where nothing reviews it. The two toggle LABELS take the same
    treatment for the same reason — each is a pair of authored words and
    neither is composed.

    ⚠️ NOT `particle-states`. `SIM_ARIA`'s box-of-particles is driven by a
    TEMPERATURE SLIDER and `SIM_CONTROLS` offers temperature / volume /
    particles / medium. Design's bench has no temperature control at all: it has
    three named state buttons, a motion toggle, a path toggle and a squash
    toggle. Rendering it as the sim would hand the student a dial Design did not
    draw and hide three Design did — the MRB-205 failure exactly (map §2.6).

    ⊕ The counter opens at ZERO. Design's `benchProgress` (page line 614) adds
    one for the state the bench is *about* to show, so an untouched page reads
    "1 of 3 states seen" above a bench still behind its gate. `head_counter`
    carries `start: 0`; the gate banks the opening state when it is answered,
    which is the first moment a student has seen anything.
    """
    states = a.get("states") or []
    if not states:
        raise ValueError("state-bench %r declares no states[]." % act_id)
    for s in states:
        missing = [k for k in ("key", "label", "alt") if not s.get(k)]
        if missing:
            raise ValueError(
                "state-bench %r state %r is missing %s. `label` is the button "
                "face AND the caption the canvas prints; `alt` is that state's "
                "whole aria-label, authored as one finished sentence rather "
                "than composed at runtime from the key."
                % (act_id, s.get("key"), ", ".join(missing)))
    keys = [s["key"] for s in states]

    ref = a.get("reference_particle")
    if not ref:
        raise ValueError(
            "state-bench %r authors no `reference_particle`. NOTES §3 flag 3 "
            "makes the fixed-size reference particle and its caption "
            "non-negotiable — it is the drawn form of the claim the lesson "
            "exists to defend, and a bench without it is a picture of three "
            "arrangements with the argument removed." % act_id)

    banner = a.get("squash_banner") or {}
    for k in ("gas", "other"):
        if not banner.get(k):
            raise ValueError(
                "state-bench %r squash_banner is missing %r; the piston prints "
                "one of two authored lines and there is no third." % (act_id, k))

    ctl = a.get("controls") or {}
    pairs = (("motion", "running", "frozen"), ("trails", "shown", "hidden"))
    for name, on_key, off_key in pairs:
        c = ctl.get(name) or {}
        if not (c.get(on_key) and c.get(off_key)):
            raise ValueError(
                "state-bench %r control %r needs both %r and %r. The label is "
                "keyed by the state the control is IN, never by what pressing "
                "it does, so the two can never be swapped by accident."
                % (act_id, name, on_key, off_key))
    if not (ctl.get("squash") or {}).get("label"):
        raise ValueError(
            "state-bench %r control 'squash' needs a `label`." % act_id)

    notes = a.get("notes") or {}
    for k in ("gas", "other"):
        if not (notes.get("squash") or {}).get(k):
            raise ValueError(
                "state-bench %r notes.squash is missing %r." % (act_id, k))
    for group in ("trails", "rest"):
        for k in keys:
            if not (notes.get(group) or {}).get(k):
                raise ValueError(
                    "state-bench %r notes.%s is missing state %r; every state "
                    "answers every instrument." % (act_id, group, k))

    groups = a.get("groups") or {}
    gate_html, hide = r_bench_gate(a.get("gate") or {})
    first = states[0]

    # ── the state row ──
    # `aria-pressed` on the opening state is TRUE because it is where the bench
    # is, and this is a segmented picker rather than an answer: R3 is untouched,
    # nothing here is marked right or wrong. `data-instrument` on the section is
    # what keeps `wirePredictions` off these buttons.
    state_btns = "".join(
        '<button type="button" class="ks3-sbench-seg" data-sbench-state="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(s["key"]), "true" if i == 0 else "false", t(s["label"]))
        for i, s in enumerate(states))

    # ── the instrument row ──
    # ⊕ CORRECTED: `aria-pressed` follows the TINT, not Design's `motionOn`.
    # Design draws the motion button lit when the motion is FROZEN
    # (`motionStyle: this.seg(!s.motion)`, line 711) and announces
    # `aria-pressed="true"` when it is RUNNING (line 709) — so a screen reader
    # hears "pressed" on a control that looks unpressed, and hears nothing
    # change when a student freezes the bench. Its own sibling, the paths
    # toggle, is consistent (lit and pressed both mean "paths are on"). This is
    # a slip rather than an intention, and R2 requires the announced state and
    # the visible state to be the same state, so the announcement is moved onto
    # the tint rather than the tint onto the announcement — the alternative
    # would light the button on page load, before the student has touched it.
    def toggle(name, on_label, off_label, pressed):
        return ('<button type="button" class="ks3-sbench-seg" data-sbench-%s '
                'aria-pressed="%s">'
                '<span data-lbl="on"%s>%s</span>'
                '<span data-lbl="off"%s>%s</span></button>'
                % (name, "true" if pressed else "false",
                   "" if pressed else " hidden", t(on_label),
                   " hidden" if pressed else "", t(off_label)))

    motion = ctl["motion"]
    trails = ctl["trails"]
    # The bench opens with the motion RUNNING and the paths hidden, so the
    # motion button shows "Freeze the motion" unpressed and the paths button
    # shows "Show the paths" unpressed. Nothing is lit until the student acts.
    inst_btns = (
        toggle("motion", motion["frozen"], motion["running"], False)
        + toggle("trails", trails["shown"], trails["hidden"], False)
        + '<button type="button" class="ks3-sbench-seg" data-sbench-squash '
          'aria-pressed="false">%s</button>' % t(ctl["squash"]["label"]))

    # ── the eight notes, all present, seven hidden ──
    # The resting note for the opening state is the one shown, which is what a
    # student reads the instant the gate is answered.
    live = "rest:%s" % first["key"]
    rows = []
    for group in ("squash", "trails", "rest"):
        for k, text in sorted((notes.get(group) or {}).items()):
            nid = "%s:%s" % (group, k)
            rows.append('<p class="ks3-sbench-note-text" data-note="%s"%s>%s</p>'
                        % (e(nid), "" if nid == live else " hidden",
                           rich(text)))

    # ⚠️ `role="status"` on the NOTE, never on the instrument root and never on
    # the gated body. A live region wrapped round the whole bench would
    # re-announce the canvas, both control groups and the note every time a
    # student pressed a toggle; wrapped round the note it announces exactly the
    # sentence that changed. `wireStateBench` therefore opens the gate itself
    # rather than calling `wireBenchGate`, which sets `role="status"` on
    # `[data-benchbody]` — see the wire function.
    note_html = ('<div class="ks3-sbench-note" data-sbench-note role="status">'
                 '%s</div>' % "".join(rows))

    canvas = ('<canvas class="ks3-sbench-canvas" width="1800" height="620" '
              'role="img" aria-label="%s" data-sbench-canvas></canvas>'
              % e(first["alt"]))

    foot = ('<div class="ks3-sbench-foot">'
            '<div class="ks3-sbench-group">'
            '<p class="ks3-sbench-grouplabel">%s</p>'
            '<div class="ks3-sbench-row">%s</div></div>'
            '<div class="ks3-sbench-group">'
            '<p class="ks3-sbench-grouplabel">%s</p>'
            '<div class="ks3-sbench-row">%s</div></div></div>'
            % (t(groups.get("states") or ""), state_btns,
               t(groups.get("instruments") or ""), inst_btns))

    # ⊕ The published state lives on the WRAPPER, which is never hidden, so
    # `state-matrix` can read it whether or not the gate has been answered and
    # whatever order the two instruments happen to wire in. These four
    # attributes are the single source of truth for the bench's settings —
    # nothing keeps a second copy (map §2.5.2's cross-block capability).
    return (gate_html
            + '<div class="ks3-sbench" data-sbench data-state="%s" '
              'data-motion="1" data-trails="0" data-squash="0" '
              'data-states="%s" data-banner-gas="%s" data-banner-other="%s" '
              'data-reference="%s"%s>'
              '<div class="ks3-sbench-body"%s>'
              '<div class="ks3-sbench-frame">%s%s</div>%s</div></div>'
            % (e(first["key"]),
               e(json.dumps([{"key": s["key"], "label": s["label"],
                              "alt": s["alt"]} for s in states],
                            separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(banner["gas"]), e(banner["other"]), e(ref),
               # Design's `benchProgress` reads "all three seen" once every
               # state has been visited, and `_head_counter` has no slot for a
               # bespoke FULL string (it has `zero`, which is the other end).
               # Carried here and written by the wire function, so the sentence
               # is authored exactly once.
               (' data-full="%s"' % e(a["progress_full"]))
               if a.get("progress_full") else "",
               hide, canvas, foot, note_html))
