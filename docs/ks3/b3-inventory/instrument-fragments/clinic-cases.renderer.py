# DISPATCH: "clinic-cases": ("ks3-clinic-block", ' data-instrument data-clinicblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "clinic-cases":           r_clinic_cases,
#
# Place `r_clinic_cases` beside `r_settles_it` — it is CONTRAST's other
# flagship and shares the ruling that shapes it. Needs `e`, `t`, `rich` and
# `_self_check`, all of which build_ks3.py already defines.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options`. The three imbalance buttons are
# a MULTI-SELECT and are authored as `kinds[]`, not as `options[]`, so
# `_KIND_FN_OWNS_OPTIONS` does not pick this kind up and must not: a lesson
# that ever authors a genuine single-answer `options` list beside this block
# still gets the generic list, which is correct. The `self_check` options are
# drawn by `_self_check` and are not `a["options"]` either.


def r_clinic_cases(a, act_id):
    """⊕ b3-04 `#s-cases` — five clinics, and two of them have two answers.

    ⚖️ THE MULTI-SELECT IS THE LESSON. Every other case instrument in the key
    stage asks for ONE answer per item — `job-sort`, `verdict-cards`,
    `sort-task`. This one asks the student to tick *every* imbalance that
    applies, and clinics 2 and 5 have two. NOTES-B3 §2 states the pedagogy in
    one line: "Refusing to tick two is the error being taught." Rendering this
    as a one-of-three picker would remove the only thing the block exists for,
    which is why it is not `verdict-cards` with three options.

    ⚖️ CLINIC 5 IS NOT A DIET PROBLEM AT ALL — an adequate plate and a
    shortened intestine — and it is deliberately inside a diet lesson, because
    it is the bridge into lessons 5 to 7. `min_multi` below refuses a payload
    in which no case carries more than one answer: a five-clinic set where
    every clinic has exactly one answer is a different exercise wearing this
    one's markup, and it would pass every other gate silently.

    ⚠️ MRB-196 R10, AND IT MOVES DESIGN'S COPY. Design computes whether the
    student's ticks matched exactly and spends it on the verdict LABEL —
    "You had it exactly" / "Two imbalances apply here" / "Not quite". Two of
    those three branches are the page marking an activity, which R3 forbids
    and R10 replaces with a self-check the student answers for themselves.

    The third branch is not a verdict on the student at all: "Two imbalances
    apply here" is a fact about the CASE. So it survives — as `verdict_label`,
    authored per case and shown to everyone identically. That also fixes a
    defect in Design's own logic, and it is the more serious half: a student
    who ticked BOTH answers on clinic 2 took the `exact` branch and therefore
    never saw the line telling them two imbalances apply. The page's own
    teaching sentence was shown only to the students who got it wrong.

    ⚠️ NOTHING MARKS. The pick buttons are `.ks3-clinic-pick`, not
    `.ks3-option`, so the reveal may disable them without failing R3's runtime
    assertion — the same construction `settles-it` uses for its two choice
    buttons. After the diagnosis the UNCHOSEN picks dim, which records what was
    spent and not whether it was right; nothing anywhere carries `data-correct`
    and nothing green or red appears on any control in this block.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    On this block the intake line is the one that would visibly break: amber
    mono is how a student finds the number, and unscoped it falls to on-dark
    body copy and reads as another sentence of the description.

    Emit-all-show-one: five panels are in the document and one is shown. No
    authored sentence is ever rebuilt in JS from an attribute, so the em
    dashes, the right single quotes and the ⚠️-flagged tone of this lesson
    survive exactly as written.
    """
    cases = a.get("cases") or []
    kinds = a.get("kinds") or []
    if len(cases) < 2:
        raise ValueError(
            "clinic-cases %r declares %d case(s). The block is a run of "
            "judgements read against each other and one case is not a run."
            % (act_id, len(cases)))
    if len(kinds) < 2:
        raise ValueError(
            "clinic-cases %r offers %d kind(s) to tick. The whole exercise is "
            "choosing among them — and choosing more than one."
            % (act_id, len(kinds)))

    known = []
    for k in kinds:
        if not k.get("id") or not k.get("label"):
            raise ValueError(
                "clinic-cases %r kind %r needs both `id` and `label`."
                % (act_id, k))
        known.append(k["id"])

    multi = 0
    for c in cases:
        for key in ("id", "label", "description", "intake", "verdict_label",
                    "answer", "why"):
            if not c.get(key):
                raise ValueError(
                    "clinic-cases %r case %r is missing %r. Every one of the "
                    "seven is drawn, and an empty one renders as a gap in the "
                    "panel." % (act_id, c.get("id"), key))
        picks = c.get("kinds") or []
        if not picks:
            raise ValueError(
                "clinic-cases %r case %r names no correct kinds[]; a clinic "
                "with no answer cannot be diagnosed."
                % (act_id, c.get("id")))
        for p in picks:
            if p not in known:
                raise ValueError(
                    "clinic-cases %r case %r names kind %r, which is not one "
                    "of the %d offered: %s."
                    % (act_id, c["id"], p, len(known), ", ".join(known)))
        if len(picks) > 1:
            multi += 1

    # ⚖️ Build time only, and it never reaches the page. See the docstring:
    # a set in which nothing has two answers is a different exercise.
    if not multi:
        raise ValueError(
            "clinic-cases %r has no case with more than one correct kind. "
            "This instrument exists because refusing to tick two is the error "
            "being taught; with one answer everywhere it is a picker."
            % act_id)

    counts = a.get("count_labels") or {}
    for key in ("none", "some", "done"):
        if not counts.get(key):
            raise ValueError(
                "clinic-cases %r count_labels is missing %r. The readout has "
                "three states and a missing one renders as an empty span."
                % (act_id, key))
    if "{n}" not in counts["some"]:
        raise ValueError(
            "clinic-cases %r count_labels['some'] is %r and carries no {n}. "
            "It is the live one." % (act_id, counts["some"]))

    tabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-clinic-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(c["id"]), "true" if i == 0 else "false",
           t(c.get("tab_label") or c["label"]))
        for i, c in enumerate(cases))

    panels = []
    for i, c in enumerate(cases):
        picks = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-clinic-pick" '
            'data-kind="%s" aria-pressed="false">%s</button>'
            % (e(k["id"]), t(k["label"])) for k in kinds)
        panels.append(
            '<div class="ks3-clinic-panel" data-case="%s" data-open="0"%s>'
            '<div class="ks3-clinic-brief">'
            '<p class="ks3-clinic-label">%s</p>'
            '<p class="ks3-clinic-desc">%s</p>'
            '<p class="ks3-clinic-intake">%s</p></div>'
            '<p class="ks3-clinic-picklabel">%s</p>'
            '<div class="ks3-clinic-picks">%s</div>'
            '<div class="ks3-clinic-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-clinic-reveal" '
            'data-clinic-reveal disabled>%s</button>'
            '<span class="ks3-clinic-count" data-clinic-count role="status" '
            'data-none="%s" data-some="%s" data-done="%s">%s</span></div>'
            '<div class="ks3-clinic-verdict" hidden data-reveal>'
            '<p class="ks3-clinic-verdict-label">%s</p>'
            '<p class="ks3-clinic-answer">%s</p>'
            '<p class="ks3-clinic-why">%s</p></div></div>'
            % (e(c["id"]), "" if i == 0 else " hidden",
               t(c["label"]), rich(c["description"]), t(c["intake"]),
               t(a.get("pick_label") or "Tick every imbalance that applies"),
               picks,
               t(a.get("reveal_label") or "Show the diagnosis"),
               e(counts["none"]), e(counts["some"]), e(counts["done"]),
               t(counts["none"]),
               t(c["verdict_label"]), rich(c["answer"]), rich(c["why"])))

    return ('<div class="ks3-clinic" data-clinic data-total="%d">'
            '<div class="ks3-clinic-tabs" role="list">%s</div>%s</div>%s'
            % (len(cases), tabs, "".join(panels), _self_check(a, act_id)))
