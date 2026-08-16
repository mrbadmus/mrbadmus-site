# DISPATCH: "meter-compare": ("ks3-meters-block", ' data-instrument data-metersblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "meter-compare":          r_meter_compare,
#
# ⚠️ THIS RENDERER CONSUMES `options`, so `_KIND_FN_OWNS_OPTIONS` picks it up
# on its own — the literal `a.get("options")` below is what
# `_kinds_consuming()` reads out of the source. Nothing has to be added to a
# list by hand, which is the whole point of that mechanism, but it also means
# a future edit that stopped reading `options` would silently hand them back
# to the generic branch. It reads them; do not "tidy" that away.
#
# Place `r_meter_compare` beside `r_job_sort` in the B2 group
# (build_ks3.py ~2846). Needs `e`, `t`, `rich`, `r_activity_options`.


def r_meter_compare(a, act_id):
    """⊕ b2-04 `#s-meters` — three muscle groups, three readings each.

    ⚖️ THIS BLOCK IS WHY THE LESSON BELONGS TO BIOLOGY. `KS3.B.SKEL.02` asks
    for "the measurement of force exerted by different muscles" in as many
    words, and this is the only place on the page where a force is measured
    rather than calculated. Everything else here is a lever; this is a
    dynamometer and a mean.

    ⚖️ AND THE MEAN IS THE SECOND LESSON. Every group is reported as the mean
    of three readings that disagree — 312, 298, 305 — with the closing band
    saying in words that a single pull would have told you almost nothing.
    Three cards each showing one number would teach that muscles have exact
    strengths, which is the opposite.

    ⚠️ NOT `verdict-cards` and not `job-sort`. Both of those reveal PER ITEM,
    the instant that item is decided, and that is the pedagogy in each — a
    student finds out about item 1 before committing on item 2. Here there is
    ONE commitment about all three groups at once (their ORDER), and all three
    cards arrive together, because a ranking cannot be revealed a third at a
    time without giving the rest away.

    ⚠️ R3 — NOTHING MARKS. The three options are ranked orders and the cards
    arrive whichever one was chosen. There is no `data-correct` in this
    instrument, no per-option feedback and no disabling: the block is a
    commitment device, and the data is what settles it.

    `answer_index` is read HERE AND ONLY HERE — at build time, to check it is
    in range and, more usefully, that the numbers still support it. If a
    `rows` edit ever reordered the means, the build says so instead of the
    page quietly arguing for an option the data no longer backs. It reaches no
    attribute, no class and no student; the precedent is `keyed-commit`'s.

    ⚠️ A LIGHT `check` block on the DEFAULT card ground. `#s-build` directly
    above it takes the inset one. Two light blocks, two different grounds,
    measured off Design's markup — which is why this activity authors no
    `ground` key at all rather than authoring `card`.
    """
    rows = a.get("rows") or []
    if len(rows) < 2:
        raise ValueError(
            "meter-compare %r declares %d row(s). The block asks a student to "
            "rank groups against each other and one group is not a ranking."
            % (act_id, len(rows)))
    for r in rows:
        for key in ("name", "readings", "mean"):
            if not r.get(key):
                raise ValueError(
                    "meter-compare %r row %r is missing %r. The readings and "
                    "the mean are the pair that teaches: a mean with no "
                    "spread behind it is just a number."
                    % (act_id, r.get("name"), key))

    options = a.get("options") or []
    if len(options) < 2:
        raise ValueError(
            "meter-compare %r offers %d option(s); the commitment is a choice "
            "between candidate orderings." % (act_id, len(options)))

    # ⚠️ Build time only. See the docstring — this never reaches the page.
    ans = a.get("answer_index")
    if ans is not None:
        if not isinstance(ans, int) or isinstance(ans, bool):
            raise ValueError(
                "meter-compare %r answer_index is %r; it is an index into "
                "options[]." % (act_id, ans))
        if not 0 <= ans < len(options):
            raise ValueError(
                "meter-compare %r answer_index %d is out of range for %d "
                "option(s)." % (act_id, ans, len(options)))
        # ⚖️ The useful half of the check. Every row's name has to appear in
        # the option the lesson argues for, in descending order of its own
        # mean — so a row whose readings changed, or a fourth group added
        # without touching the options, fails the build instead of leaving
        # the page arguing for an order its own data contradicts.
        order = sorted(rows, key=lambda r: _meter_mean(r, act_id), reverse=True)
        text = options[ans].lower()
        at = -1
        for r in order:
            # The card's name qualifies the group ("Biceps, pulling up") and
            # the option names it plainly ("Biceps"), so the match is on the
            # head of the name — everything before the first comma. Matching
            # the whole string would fail on Design's own payload, and
            # authoring a second short name per row would be one more place
            # for the two to disagree.
            head = r["name"].split(",")[0].strip().lower()
            i = text.find(head)
            if i < 0:
                raise ValueError(
                    "meter-compare %r names %r as the correct order and it "
                    "does not mention %r at all."
                    % (act_id, options[ans], head))
            if i < at:
                raise ValueError(
                    "meter-compare %r says the correct order is %r, but its "
                    "own means rank them %s. The data and the answer have "
                    "stopped agreeing."
                    % (act_id, options[ans],
                       ", ".join(x["name"] for x in order)))
            at = i

    cards = "".join(
        '<div class="ks3-meters-card">'
        '<p class="ks3-meters-name">%s</p>'
        '<p class="ks3-meters-readings">%s</p>'
        '<p class="ks3-meters-mean">%s</p>'
        '<p class="ks3-meters-meanlabel">%s</p></div>'
        % (t(r["name"]), t(r["readings"]), t(r["mean"]),
           t(a.get("mean_label", "")))
        for r in rows)

    close = ('<p class="ks3-meters-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    # `r_activity_options` rather than a second copy of the answer button:
    # this block's commitment is an ordinary four-square option list and the
    # only thing that differs is the measure it is set on.
    return ('<div class="ks3-meters" data-meters>'
            '<div class="ks3-meters-commit">%s</div>'
            '<div class="ks3-meters-reveal" hidden data-reveal>'
            '<div class="ks3-meters-cards">%s</div>%s</div></div>'
            % (r_activity_options(options), cards, close))


def _meter_mean(row, act_id):
    """The leading number of a row's `mean` string, for the build-time check.

    Parsed rather than authored as a second numeric field: the string on the
    page IS the value, and a `mean_value: 305` beside `mean: "305 N"` is two
    places for one number to live.
    """
    m = re.match(r"\s*(-?\d+(?:\.\d+)?)", str(row.get("mean", "")))
    if not m:
        raise ValueError(
            "meter-compare %r row %r has mean %r, which does not start with a "
            "number. The ordering check reads it."
            % (act_id, row.get("name"), row.get("mean")))
    return float(m.group(1))
