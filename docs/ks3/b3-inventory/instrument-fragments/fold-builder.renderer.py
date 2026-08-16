# DISPATCH: "fold-builder": ("ks3-fold-block", ' data-instrument data-foldblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B3 rows:
#     "fold-builder":           r_fold_builder,
#
# Place `r_fold_builder` in the B3 group, after `r_enzyme_run`. Needs `e`, `t`,
# `rich` — and nothing else; there is no canvas, no timer and no third-party
# anything in this instrument.
#
# ⚠️ THIS RENDERER DOES NOT CONSUME `options` OR `reveal`. Its controls are
# three state toggles, which are not answer buttons and are not `.ks3-option`;
# the activity authors neither key, so `_kinds_consuming()` correctly leaves
# both generic branches off. Do not start reading `options` here — the block
# has no question in it and R3 would have nowhere to stand.


def _fold_area_text(value):
    """Design's own three-branch number format, for the RESTING render only.

    `wireFoldBuilder` carries the same four lines and recomputes on every
    toggle. Two copies is a real cost and it buys the thing `head_counter`'s
    `start` buys one level up: the HTML that ships already says `0.50 m²`, so a
    crawler, a reader with JS off and anything that quotes the page all get the
    number the page means rather than a placeholder or an empty element.

    ⚠️ `int(v + 0.5)` and NOT `round()`. Python rounds half to even and
    JavaScript's `Math.round` rounds half up, so `round(10.5)` is 10 here and
    11 there — a divergence that would be invisible at rest (0 levels reads
    0.50 either way) and visible the moment someone reused this helper for a
    driven state. The two implementations agree by construction instead.
    Areas and multiples are positive by construction, so truncation after the
    half-add is a floor, and `math` does not have to be imported for it.
    """
    if value < 1:
        return "%.2f" % value
    if value < 10:
        return "%.1f" % value
    return "%d" % int(value + 0.5)


def _fold_multiple_text(ratio):
    """The same rule at one decimal below ten, whole numbers above."""
    if ratio < 10:
        return "%.1f" % ratio
    return "%d" % int(ratio + 0.5)


def _fold_factor_text(factor):
    """A level's multiplier as it is printed on its own button face.

    Whole numbers print whole — Design's `'On · ×' + l.factor` on an integer
    factor gives `×3`, and `×3.0` would read as a measured quantity rather
    than as the count of times the sheet was folded.
    """
    return ("%d" % factor) if float(factor).is_integer() else ("%g" % factor)


def r_fold_builder(a, act_id):
    """⊕ b3-07 `#s-fold` — build the surface up, one folding level at a time.

    ⚖️ THE MODEL IS BUILT UP, NOT BROKEN DOWN, and that is the family. B3's
    other switch instrument (`job-switch`, b3-08) starts with everything
    working and takes things away; this one starts with a plain tube and adds.
    Same control, opposite direction, and the direction is the lesson: the
    student watches half a square metre become thirty while the length written
    beside it never moves.

    ⚖️ THE LENGTH NEVER CHANGES, AND THE COPY SAYS SO AT EVERY STEP. All four
    notes are authored (NOTES-B3 §3.5) and three of them name the six metres
    again. That repetition is the whole confrontation of `#s-think` — *"Villi
    make the intestine longer"* — done with a number instead of a sentence, so
    it is not something to tidy out of the payload.

    ⚠️ THE NOTES ARE INDEXED BY **HOW MANY** LEVELS ARE ON, NOT BY WHICH.
    Four strings, one per count, exactly as NOTES-B3 §3.5 specifies. A note per
    level would be three strings and would have nothing to say about the plain
    tube, which is the state the whole comparison is measured from.

    ⚠️ NOTHING MARKS. There is no right answer here and no `answer_index` to
    check: a level is on or off and both are legitimate places to stand. The
    three toggles are `aria-pressed` toggle buttons and are deliberately NOT
    `.ks3-option`, so no R3 gate has to make an exception for them.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every text rule in the stylesheet is scoped to at least
    (0,2,0). See the CSS; the readout note is the row that would ship broken.

    Emit-both-show-one: all four notes are in the document, three hidden, and
    `wireFoldBuilder` swaps which is shown. No authored sentence is ever
    rebuilt in JS from an attribute — only the two NUMBERS are, which is what
    an arithmetic readout is for.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError(
            "fold-builder %r declares %d level(s). The block's argument is "
            "that folding COMPOUNDS — folds on folds on folds — and one "
            "multiplier is not a compounding." % (act_id, len(levels)))

    base = a.get("base_area")
    if not isinstance(base, (int, float)) or isinstance(base, bool) or base <= 0:
        raise ValueError(
            "fold-builder %r needs a positive `base_area` — every number the "
            "block prints is a multiple of it." % act_id)

    for l in levels:
        for key in ("id", "name", "factor", "what", "scale"):
            if not l.get(key):
                raise ValueError(
                    "fold-builder %r level %r is missing %r. `scale` is not "
                    "optional: it is what tells a student that the three "
                    "levels are three different SIZES of the same trick, and "
                    "without it they read as three unrelated facts."
                    % (act_id, l.get("id") or l.get("name"), key))
        if not isinstance(l["factor"], (int, float)) or isinstance(l["factor"], bool):
            raise ValueError(
                "fold-builder %r level %r has factor %r, which is not a "
                "number." % (act_id, l["id"], l["factor"]))

    notes = a.get("notes") or []
    if len(notes) != len(levels) + 1:
        raise ValueError(
            "fold-builder %r declares %d note(s) for %d level(s); it needs "
            "%d — one per COUNT, including the plain tube at zero. A missing "
            "note is a state the instrument can reach with nothing to say "
            "about it." % (act_id, len(notes), len(levels), len(levels) + 1))

    labels = a.get("labels") or {}
    off_label = labels.get("off")
    on_label = labels.get("on")
    if not off_label or not on_label:
        raise ValueError(
            "fold-builder %r needs `labels.off` and `labels.on` — the button "
            "face is the only thing that says what pressing it will do."
            % act_id)

    rows = []
    for l in levels:
        # `{factor}` is filled HERE rather than in JS, so the button carries
        # its two finished labels and the runtime only swaps between them.
        # Design writes `'On · ×' + l.factor`; the multiplication
        # sign is U+00D7 and IS in the five latin subsets (unlike → ✓ ✕), so
        # it is typed rather than drawn.
        lit = on_label.replace("{factor}", _fold_factor_text(l["factor"]))
        rows.append(
            '<li class="ks3-fold-level" data-level="%s" data-factor="%s" '
            'data-on="0">'
            '<div class="ks3-fold-levelmain">'
            '<div class="ks3-fold-levelwhat">'
            '<p class="ks3-fold-name">%s</p>'
            '<p class="ks3-fold-what">%s</p>'
            '<p class="ks3-fold-scale">%s</p></div>'
            '<button type="button" class="ks3-fold-toggle" data-fold-toggle '
            'aria-pressed="false" data-label-on="%s" data-label-off="%s">%s'
            '</button></div></li>'
            % (e(l["id"]), e(l["factor"]), t(l["name"]), rich(l["what"]),
               t(l["scale"]), e(lit), e(off_label), t(off_label)))

    # Emit-both-show-one. Index 0 is the plain tube and is the one shown.
    note_html = "".join(
        '<p class="ks3-fold-note" data-note="%d"%s>%s</p>'
        % (i, "" if i == 0 else " hidden", rich(n))
        for i, n in enumerate(notes))

    area_format = a.get("area_format") or "{a}"
    multiple_format = a.get("multiple_format") or "{x}"
    if "{a}" not in area_format:
        raise ValueError(
            "fold-builder %r `area_format` %r has no {a} placeholder, so the "
            "area would never be printed." % (act_id, area_format))
    if "{x}" not in multiple_format:
        raise ValueError(
            "fold-builder %r `multiple_format` %r has no {x} placeholder."
            % (act_id, multiple_format))

    # The resting values, computed here so the shipped HTML is already right.
    total = base
    for l in levels:
        total *= l["factor"]
    rest_width = max(2.0, (base / total) * 100.0)

    return ('<div class="ks3-fold" data-fold data-base="%s" '
            'data-area-format="%s" data-multiple-format="%s">'
            '<ul class="ks3-fold-levels" role="list">%s</ul>'
            '<div class="ks3-fold-readout">'
            '<div class="ks3-fold-readhead">'
            '<p class="ks3-fold-readlabel">%s</p>'
            '<p class="ks3-fold-area" data-fold-area>%s</p></div>'
            '<span class="ks3-fold-track">'
            '<span class="ks3-fold-bar" data-fold-bar data-full="0" '
            'style="width:%.1f%%"></span></span>'
            # ⚠️ `role="status"` on the NOTE, never on the instrument root. A
            # live region wrapping the whole block would re-announce three
            # level descriptions and a bar every time a toggle moved.
            '<div class="ks3-fold-noteline" role="status">%s</div>'
            '<p class="ks3-fold-multiple" data-fold-multiple>%s</p>'
            '</div></div>'
            % (e(base), e(area_format), e(multiple_format), "".join(rows),
               t(a.get("readout_label") or ""),
               t(area_format.replace("{a}", _fold_area_text(base))),
               rest_width, note_html,
               t(multiple_format.replace("{x}", _fold_multiple_text(1.0)))))
