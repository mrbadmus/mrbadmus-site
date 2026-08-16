# DISPATCH: "prediction-stack": ("ks3-predict-block", ' data-instrument data-predictblock data-stage-done="0"'),
#
# Splice point: `ACTIVITY_KIND_RENDERERS` in build_ks3.py, in the new
# "C1 · Particles and their behaviour" section. Also add to `r_activity`:
#
#     if kind == "prediction-stack":
#         parts.append(r_prediction_stack(a, act_id))
#
# The function below belongs beside the other C1 renderers and uses `e`, `t`
# and `rich`, all of which build_ks3.py already defines.


def r_prediction_stack(a, act_id):
    """⊕ c1-04 `#s-predict` — three predictions in one block, one option set.

    ⚠️ NOT the generic `predict` kind. That is one prompt, one option list and
    one reveal; this is three questions that share an option set, each with its
    own answer index and its own note, and rendering it as the generic shell
    would keep the first question and lose the other two.

    ⚖️ THE THREE ARE COMPARABLE BECAUSE THE OPTIONS ARE SHARED. `Goes up /
    Stays the same / Goes down` is asked about three different single changes,
    so a student who answers all three has produced a small table of the
    model's behaviour rather than three unrelated multiple choices. Authoring
    the options once is what makes that true rather than coincidental.

    ⚖️ ONE SHARED WRONG-ANSWER NOTE, and it deliberately does not give the
    answer: it sends the student back up to the bench, which is the only place
    on the page that can settle it. Three per-prediction wrong notes would be
    three more chances to leak the right one. Design authors it inside
    `renderVals` (page line 738), so it is not in the extracted constants and
    was lifted by hand.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every text rule in the stylesheet is self-scoped
    `.ks3-predict …` at (0,2,0). Two separate builds have shipped this defect.

    ⚑ Design paints the RIGHT panel's border in `--ks3-alert` and the WRONG
    note's text in `--ks3-alert` too — the same token doing two jobs three
    lines apart. On ink the palette has already swapped accent → alert for
    every lit state (`.ks3-dark .ks3-sim-seg-btn[aria-pressed="true"]`), so
    this is consistent with the system rather than with §8's "amber is a wrong
    idea"; reproduced as drawn and recorded here so it is a decision rather
    than an accident.
    """
    preds = a.get("predictions") or []
    # ⚠️ `shared_options`, NOT `options`. `options` is the SHELL's key —
    # `r_activity` renders any `options` it finds as a standard A/B/C answer
    # list — so authoring the shared set under that name emits a fourth,
    # orphaned copy of the three choices below the three panels, answering no
    # question. The map's payload block calls it `options`; that name is taken.
    options = a.get("shared_options") or []
    wrong = a.get("wrong_note") or ""

    if not preds:
        raise ValueError(
            "prediction-stack %r declares no predictions[]." % act_id)
    if len(options) < 2:
        raise ValueError(
            "prediction-stack %r needs the shared options[] — the three "
            "predictions are only comparable because they are asked the same "
            "way; got %r." % (act_id, options))
    if not wrong:
        raise ValueError(
            "prediction-stack %r has no `wrong_note`. One shared fallback is "
            "the whole shape: without it a wrong answer gets silence."
            % act_id)
    for p in preds:
        if not p.get("id") or not p.get("question") or not p.get("note"):
            raise ValueError(
                "prediction-stack %r: every prediction needs `id`, `question` "
                "and `note`; got %r." % (act_id, p))
        ans = p.get("answer")
        if not isinstance(ans, int) or not 0 <= ans < len(options):
            raise ValueError(
                "prediction-stack %r: prediction %r answers %r, which is not "
                "an index into the %d shared options."
                % (act_id, p.get("id"), ans, len(options)))

    panels = []
    for p in preds:
        # `.ks3-sim-seg-btn` on the dark ground gives Design's own `segDark`
        # pair: the lit state is the alert yellow with ink text, the resting
        # state transparent on the muted rule. A private control here would be
        # a second copy of a ruled one.
        btns = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-predict-btn" '
            'data-i="%d" aria-pressed="false">%s</button>'
            % (i, t(opt)) for i, opt in enumerate(options))
        # Emit-both-show-one. Both notes are in the document and one is
        # hidden, so no student-facing string is ever assembled in JS and any
        # `<em>` in an authored note survives. The live region is the WRAPPER,
        # never the instrument root.
        panels.append(
            '<div class="ks3-predict" data-prediction="%s" '
            'data-answer="%d">'
            '<p class="ks3-predict-q">%s</p>'
            '<div class="ks3-predict-btns">%s</div>'
            '<div class="ks3-predict-notes" data-predict-notes role="status">'
            '<p class="ks3-predict-note" data-tone="right" hidden>%s</p>'
            '<p class="ks3-predict-note" data-tone="wrong" hidden>%s</p>'
            '</div></div>'
            % (e(p["id"]), int(p["answer"]), t(p["question"]), btns,
               rich(p["note"]), rich(wrong)))

    return ('<div class="ks3-predicts" data-predictstack data-total="%d">%s'
            '</div>' % (len(preds), "".join(panels)))
