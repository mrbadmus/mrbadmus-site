# DISPATCH: "test-bench": ("ks3-tbench-block", ' data-instrument data-tbenchblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "test-bench":             r_test_bench,
#
# Place `r_test_bench` after `r_band_commit` in the B3 group. Needs `e`, `t`,
# `rich`, `r_activity_options`.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME the activity's own `options` key, because
# the activity does not author one — the two prediction buttons live under
# `predict.options`, where they belong to the gate rather than to the block.
# `_kinds_consuming()` will therefore NOT list this kind, which is correct:
# there is no top-level `options` for the generic branch to draw twice.


def r_test_bench(a, act_id):
    """⊕ b3-02 `#s-bench` — five foods, four tests, twenty honest results.

    ⚖️ PREDICTING **RUNS** THE TEST. There is no separate run button, and that
    is the mechanism rather than a saving: the commitment IS the action, so a
    student cannot watch the colour first and decide afterwards what they
    thought. Twenty combinations, each gated by its own two-option prediction.

    ⚖️ EVERY RESULT ENDS IN A CLAIM LINE, and for a negative it is the HEDGED
    wording. This is the whole lesson — *“No starch was detected in potato
    under these conditions.” Not “there is none”.* — and the four deliberate
    false negatives in Design's payload (potato/Biuret at 2% protein, apple
    juice/Biuret at 0.3%, and the two that are true negatives and say so) only
    teach anything if the sentence a student is licensed to write is printed
    under every one of them. `claims` is REQUIRED and this renderer raises
    without both halves.

    ⚠️ THE TUBE COLOUR IS REAL AND IS NOT A TOKEN. NOTES-B3 §3.2: the tube is
    the only colour-bearing element in the unit and the colours are the
    reagents' own — Benedict's blue #2E63B8 to brick red #B03A16. They are
    authored as literal hex on the test, never as `var(--ks3-accent)`, because
    an accent-tinted tube would be teaching a colour change that does not
    happen. They reach the page as an attribute on the test tab and are set on
    the tube's fill; that is a COLOUR travelling through an attribute, not a
    sentence.

    ⚠️ EVERYTHING A STUDENT READS IS COMPOSED HERE, AT BUILD TIME. The twenty
    prediction prompts and the twenty claim lines are filled from two authored
    templates and the foods' and tests' own names, in Python, and emitted into
    the document hidden. The browser only ever unhides one of them. Design's
    page assembles all forty in `renderVals()` with `+`, `.toLowerCase()` and
    `.split(' (')[0]`, which is how "Potato" becomes "potato" and "reducing
    sugar (glucose, fructose)" becomes "reducing sugar" — three string
    transformations applied to authored science in the browser. `lower` and
    `detects` are authored instead, so nothing is transformed anywhere.

    ⚠️ ON INK. `.ks3-dark p` is (0,1,1); every text rule in the stylesheet is
    scoped `.ks3-dark …`, and the result panel is CREAM inside the ink block,
    so its four paragraphs are the ones that would silently lose. See the CSS.
    """
    tests = a.get("tests") or []
    foods = a.get("foods") or []
    if len(tests) < 2 or len(foods) < 2:
        raise ValueError(
            "test-bench %r declares %d test(s) and %d food(s). The block's "
            "argument is that one test answers one question, and it cannot be "
            "made with a single row or a single column."
            % (act_id, len(tests), len(foods)))

    for tst in tests:
        for key in ("id", "label", "detects", "detects_full", "method"):
            if not tst.get(key):
                raise ValueError(
                    "test-bench %r test %r is missing %r. `detects` is the "
                    "short form the prompt and the claim line use "
                    "(“reducing sugar”) and `detects_full` is the one the "
                    "method panel prints (“reducing sugar (glucose, "
                    "fructose)”); deriving one from the other would put a "
                    "`.split()` between a student and an authored phrase."
                    % (act_id, tst.get("id"), key))
        for out in ("pos", "neg"):
            spec = tst.get(out) or {}
            for key in ("colour", "name", "headline"):
                if not spec.get(key):
                    raise ValueError(
                        "test-bench %r test %r %s.%s is missing. `name` is the "
                        "tube's own state line and `headline` is the finished "
                        "sentence over the result — both are authored, "
                        "because capitalising the first letter of a reagent "
                        "colour in the browser is a transformation of science "
                        "copy." % (act_id, tst["id"], out, key))

    test_ids = [tst["id"] for tst in tests]
    for f in foods:
        for key in ("id", "label", "lower"):
            if not f.get(key):
                raise ValueError(
                    "test-bench %r food %r is missing %r. `lower` is the form "
                    "the sentence uses (“…in apple juice…”); lower-casing "
                    "`label` at runtime would also lower-case a proper noun "
                    "the moment one is added." % (act_id, f.get("id"), key))
        has, notes = f.get("has") or {}, f.get("notes") or {}
        for tid in test_ids:
            if tid not in has:
                raise ValueError(
                    "test-bench %r: food %r declares no result for test %r. "
                    "Every combination is reachable from the tabs, so a "
                    "missing one is a tube that runs and reports nothing."
                    % (act_id, f["id"], tid))
            if not notes.get(tid):
                raise ValueError(
                    "test-bench %r: food %r has no note for test %r. The note "
                    "is where the honest reading of that result lives — four "
                    "of these are deliberate false negatives and the note is "
                    "the only thing that says so." % (act_id, f["id"], tid))

    predict = a.get("predict") or {}
    if not predict.get("prompt") or len(predict.get("options") or []) < 2:
        raise ValueError(
            "test-bench %r declares no prediction gate. Predicting is what "
            "RUNS the test in this block; without it the tube is a lookup "
            "table." % act_id)
    claims = a.get("claims") or {}
    if not (claims.get("positive") and claims.get("negative")):
        raise ValueError(
            "test-bench %r declares no %s claim line. The claim line is the "
            "lesson." % (act_id,
                         "positive" if not claims.get("positive") else "negative"))
    verdicts = a.get("verdicts") or {}
    if not (verdicts.get("hit") and verdicts.get("miss")):
        raise ValueError("test-bench %r needs both `verdicts` branches." % act_id)

    first_food, first_test = foods[0], tests[0]

    def fill(template, food, tst):
        """One authored template, twenty finished sentences, at BUILD time.

        `{food_lower}` is replaced first: `{food}` is a prefix of it, so the
        other order would leave a stray `_lower` in every negative claim line.
        """
        return (template
                .replace("{food_lower}", food["lower"])
                .replace("{food}", food["label"])
                .replace("{test}", tst["label"])
                .replace("{detects}", tst["detects"]))

    # ── the two tab groups ───────────────────────────────────────────────
    groups = a.get("groups") or {}
    food_tabs = "".join(
        '<button type="button" class="ks3-tbench-tab" data-food="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(f["id"]), "true" if f is first_food else "false", t(f["label"]))
        for f in foods)
    # ⚠️ The two reagent colours ride on the TEST TAB, because the tube shows
    # the negative colour of the selected test before anything is run — so the
    # colours have to be reachable from the selection, not only from a result
    # panel that does not exist yet.
    test_tabs = "".join(
        '<button type="button" class="ks3-tbench-tab" data-test="%s" '
        'data-neg="%s" data-pos="%s" aria-pressed="%s">%s</button>'
        % (e(tst["id"]), e(tst["neg"]["colour"]), e(tst["pos"]["colour"]),
           "true" if tst is first_test else "false", t(tst["label"]))
        for tst in tests)

    # ── the tube ─────────────────────────────────────────────────────────
    # The label is TWO switched spans with a literal join between them, not a
    # string built in the browser: "Potato" and "Iodine" are both authored and
    # both already in the document, so there is nothing to concatenate.
    tube = a.get("tube") or {}
    lfoods = "".join(
        '<span class="ks3-tbench-lfood" data-lfood="%s"%s>%s</span>'
        % (e(f["id"]), "" if f is first_food else " hidden", t(f["label"]))
        for f in foods)
    ltests = "".join(
        '<span class="ks3-tbench-ltest" data-ltest="%s"%s>%s</span>'
        % (e(tst["id"]), "" if tst is first_test else " hidden", t(tst["label"]))
        for tst in tests)
    states = ['<span data-sname="rest">%s</span>' % t(tube.get("not_run") or "")]
    for tst in tests:
        for out in ("pos", "neg"):
            states.append('<span data-sname="%s:%s" hidden>%s</span>'
                          % (e(tst["id"]), out, t(tst[out]["name"])))

    # ── the method card ──────────────────────────────────────────────────
    methods = "".join(
        '<p class="ks3-tbench-method" data-method="%s"%s>%s</p>'
        '<p class="ks3-tbench-detects" data-detects="%s"%s>%s</p>'
        % (e(tst["id"]), "" if tst is first_test else " hidden", t(tst["method"]),
           e(tst["id"]), "" if tst is first_test else " hidden",
           t((a.get("detects_label") or "{detects}")
             .replace("{detects}", tst["detects_full"])))
        for tst in tests)

    # ── twenty prompts and twenty result panels ──────────────────────────
    prompts, results = [], []
    for f in foods:
        for tst in tests:
            key = "%s:%s" % (f["id"], tst["id"])
            cur = f is first_food and tst is first_test
            prompts.append(
                '<p class="ks3-commit ks3-tbench-prompt" data-prompt="%s"%s>%s</p>'
                % (e(key), "" if cur else " hidden",
                   t(fill(predict["prompt"], f, tst))))
            positive = bool(f["has"][tst["id"]])
            side = tst["pos"] if positive else tst["neg"]
            claim = fill(claims["positive"] if positive else claims["negative"],
                         f, tst)
            results.append(
                '<div class="ks3-tbench-result" data-result="%s" '
                'data-outcome="%s" data-colour="%s" hidden>'
                '<p class="ks3-tbench-verdict" data-verdict="hit" hidden>%s</p>'
                '<p class="ks3-tbench-verdict" data-verdict="miss" hidden>%s</p>'
                '<p class="ks3-tbench-head">%s</p>'
                '<p class="ks3-tbench-why">%s</p>'
                '<p class="ks3-tbench-claim"><strong>%s</strong> %s</p></div>'
                % (e(key), "pos" if positive else "neg", e(side["colour"]),
                   t(verdicts["hit"]), t(verdicts["miss"]),
                   t(side["headline"]), rich(f["notes"][tst["id"]]),
                   t(a.get("claim_label") or "What you may write down:"),
                   rich(claim)))

    return ('<div class="ks3-tbench" data-tbench data-food="%s" data-test="%s" '
            'data-target="%d">'
            '<div class="ks3-tbench-picks">'
            '<div class="ks3-tbench-group"><p class="ks3-tbench-grouplabel">%s</p>'
            '<div class="ks3-tbench-tabs">%s</div></div>'
            '<div class="ks3-tbench-group"><p class="ks3-tbench-grouplabel">%s</p>'
            '<div class="ks3-tbench-tabs">%s</div></div></div>'
            '<div class="ks3-tbench-readout">'
            '<div class="ks3-tbench-tubecard">'
            '<span class="ks3-tbench-tube" aria-hidden="true">'
            '<span class="ks3-tbench-fill" data-tube data-run="0" '
            'style="background:%s"></span></span>'
            '<div class="ks3-tbench-tubemeta">'
            '<p class="ks3-tbench-cap">%s</p>'
            '<p class="ks3-tbench-tubelabel">%s'
            '<span class="ks3-tbench-join" aria-hidden="true">%s</span>%s</p>'
            '<p class="ks3-tbench-state" data-state role="status">%s</p>'
            '</div></div>'
            '<div class="ks3-tbench-methodcard">'
            '<p class="ks3-tbench-cap">%s</p>%s</div></div>'
            '<div class="ks3-tbench-predict" data-predict>%s%s</div>'
            '<div class="ks3-tbench-results">%s</div></div>'
            % (e(first_food["id"]), e(first_test["id"]),
               int(a.get("rail_after") or 4),
               t(groups.get("food") or "Food"), food_tabs,
               t(groups.get("test") or "Test"), test_tabs,
               e(first_test["neg"]["colour"]),
               t(tube.get("caption") or "In the tube"),
               lfoods, t(tube.get("label_join") or " + "), ltests,
               "".join(states),
               t(a.get("method_label") or "Method"), methods,
               "".join(prompts), r_activity_options(predict["options"]),
               "".join(results)))
