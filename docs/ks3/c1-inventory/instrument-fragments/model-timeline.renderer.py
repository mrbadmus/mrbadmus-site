# DISPATCH: "model-timeline": ("ks3-mtl-block", ' data-instrument data-mtlblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "model-timeline":
#         parts.append(r_model_timeline(a, act_id))
#
# Place the function next to `r_evidence_bench`. Needs `e`, `t`, `rich`.


def r_model_timeline(a, act_id):
    """⊕ c1-06 `#s-history` — five models, in order, one open at a time.

    ⚠️ A LIGHT `.ks3-block`, and it has NO nearest existing kind. `zoom-ladder`
    is a slider over magnifications with a tick row and an authored next-box;
    `scale-zoom` is two step buttons over five drawings. This is five named
    positions, each with a claim, a body and the evidence that killed it, and
    the step control is a **third control geometry** in the unit — left-aligned,
    `10px 14px`, a two-line stack of mono year over 700 name. It is registered
    as its own thing rather than folded into `seg()`, which is one line and one
    weight, because a year over a name is not a segment label.

    ⚠️ `default_index` IS NOT ZERO, and that is the teaching. The row opens on
    Dalton (index 1), not Democritus: Dalton is the model the student has been
    using all unit, and the point of the row is that it already has a before
    and an after. A component that opened on the first entry would put a
    twenty-century dead end in front of the student as the headline.

    ⚖️ THE RAIL PREDICATE IS A SET, NOT AN INEQUALITY. Design's page ticks this
    stage on `history !== 1`, which unticks the moment a student who has read
    all five comes back to Dalton — a rail that goes backwards. `wireModelTimeline`
    counts a set of visited indices, seeded with the default, and never empties
    it. Same class of defect as c1-04's `Math.max(touched, N)`.

    Emit-all-show-one, the same trick the board and the switch use: five detail
    cards in the document, one shown. Going back to a model finds it exactly as
    it was, no state lives anywhere but the DOM, and the 25 authored strings —
    two of which carry an arrow and a right single quote — are never rebuilt in
    JS from an attribute.
    """
    steps = a.get("steps") or []
    if not steps:
        raise ValueError("model-timeline %r declares no steps[]." % act_id)

    broke_label = a.get("broke_label")
    if not broke_label:
        raise ValueError(
            "model-timeline %r declares no broke_label — the static bold prefix "
            "on the rule-topped line, and the thing that makes the sentence a "
            "cause rather than an aside." % act_id)

    start = int(a.get("default_index") or 0)
    if not 0 <= start < len(steps):
        raise ValueError(
            "model-timeline %r opens on index %d of %d step(s)."
            % (act_id, start, len(steps)))

    for i, s in enumerate(steps):
        missing = [k for k in ("year", "who", "label", "claim", "body", "broke")
                   if not s.get(k)]
        if missing:
            raise ValueError(
                "model-timeline %r step %d (%r) is missing %s. Every one of the "
                "six is drawn, and an empty one renders as a gap in the card."
                % (act_id, i, s.get("who"), ", ".join(missing)))

    btns = "".join(
        '<button type="button" class="ks3-mtl-step" data-step="%d" '
        'aria-pressed="%s">'
        '<span class="ks3-mtl-year">%s</span>'
        '<span class="ks3-mtl-who">%s</span></button>'
        # `t()` on the year, not `e()`: 1913 → now carries U+2192, which none of
        # the five latin woff2 subsets contains. Typed as a character it drops
        # to a system font inside a 12px mono span; `t()` draws it.
        % (i, "true" if i == start else "false", t(s["year"]), t(s["who"]))
        for i, s in enumerate(steps))

    cards = "".join(
        '<div class="ks3-mtl-card" data-step="%d"%s>'
        '<p class="ks3-mtl-label">%s</p>'
        '<p class="ks3-mtl-claim">%s</p>'
        '<p class="ks3-mtl-body">%s</p>'
        '<p class="ks3-mtl-broke"><strong>%s</strong> %s</p></div>'
        % (i, "" if i == start else " hidden",
           t(s["label"]), rich(s["claim"]), rich(s["body"]),
           t(broke_label), rich(s["broke"]))
        for i, s in enumerate(steps))

    return ('<div class="ks3-mtl" data-mtl data-total="%d" data-default="%d">'
            '<div class="ks3-mtl-steps">%s</div>'
            '<div class="ks3-mtl-cards">%s</div></div>'
            % (len(steps), start, btns, cards))
