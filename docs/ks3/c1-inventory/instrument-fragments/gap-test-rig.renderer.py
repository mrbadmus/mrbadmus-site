# DISPATCH: "gap-test-rig": ("ks3-gap-block", ' data-instrument data-gapblock data-stage-done="0"'),
#
# Splice `r_gap_test_rig` into build_ks3.py beside the other instrument
# renderers, add the dispatch row above to ACTIVITY_KIND_RENDERERS, and add
#     if kind == "gap-test-rig":
#         parts.append(r_gap_test_rig(a, act_id))
# to r_activity's dispatch run. No new imports.


def r_gap_test_rig(a, act_id):
    """⊕ c1-01 `#s-gap` — put something in the gap and watch three tests fail.

    ⚖️ EVERY WRONG ANSWER FAILS THE SAME THREE TESTS, AND THAT IS THE
    ARGUMENT. The rig does not mark the choice. It takes whatever the student
    put in the gap, packs the space solid on the right-hand box, and then lets
    them run a test whose outcome they already know from the top of the page:
    a gas can be squashed, 50 and 50 make 97, a smell crosses a still room. The
    answer that survives is the one that never contradicts any of the three.
    Marking the option instead would turn an argument into a quiz — and R3 and
    MRB-196 R10 both say the marking belongs to the ladder.

    ⚠️ `empty_choice` IS POSITIONAL, AND IT IS AUTHORED FOR THAT REASON.
    Design's discriminator is `gapChoice !== null && gapChoice !== 3`: a bare
    index, three lines from the list it indexes, with nothing tying the two
    together. Reordering the options there inverts every outcome on the page
    silently. Here the index is authored next to its list and validated against
    it at build time, so the same edit is a build failure instead.

    ⚠️ INK-DARK (`practical`). The block's own text colours come from
    `.ks3-dark`, and `.ks3-dark p` is (0,1,1) — every text rule in this
    instrument's stylesheet is scoped past that or the note renders in the
    block's body colour instead of its own.

    ⊖ The four options are rendered HERE, not by the activity shell. The shell
    emits `options` AFTER the instrument, which would put the question below
    the answer; `choices` is the same list under a name the shell does not
    claim, and `r_activity_options` keeps the markup identical to every other
    option list in the key stage.
    """
    choices = a.get("choices") or []
    if len(choices) < 2:
        raise ValueError(
            "gap-test-rig %r offers %d choice(s); the rig contrasts an empty "
            "gap with a filled one and needs both on offer."
            % (act_id, len(choices)))

    empty = a.get("empty_choice")
    if not isinstance(empty, int) or isinstance(empty, bool) \
            or not 0 <= empty < len(choices):
        raise ValueError(
            "gap-test-rig %r sets empty_choice %r, which is not an index into "
            "its %d choices. This index decides whether every test reads its "
            "`on` or its `off` paragraph — it is the whole discriminator and "
            "may not be implied by option order."
            % (act_id, empty, len(choices)))

    tests = a.get("tests") or []
    if not tests:
        raise ValueError("gap-test-rig %r declares no tests[]." % act_id)
    for tt in tests:
        missing = [k for k in ("id", "label", "on", "off") if not tt.get(k)]
        if missing:
            raise ValueError(
                "gap-test-rig %r test %r is missing %s. Both outcomes are "
                "authored: `on` is what the test does when the gap is really "
                "empty and `off` is how it fails when it is not, and a missing "
                "one would leave a student reading the previous test's result."
                % (act_id, tt.get("id") or tt.get("label"),
                   ", ".join(missing)))

    notes = a.get("notes") or {}
    if not (notes.get("empty") and notes.get("filled")):
        raise ValueError(
            "gap-test-rig %r needs both opening notes (empty and filled) — the "
            "line a student reads after choosing and before testing." % act_id)

    labels = a.get("canvas_labels") or {}
    for key in ("empty", "filled", "foot_empty", "foot_filled"):
        if not labels.get(key):
            raise ValueError(
                "gap-test-rig %r canvas_labels is missing %r." % (act_id, key))

    alt = a.get("alt") or {}
    for key in ("template", "filled", "empty"):
        if not alt.get(key):
            raise ValueError(
                "gap-test-rig %r alt is missing %r; the two boxes exist only "
                "on the canvas." % (act_id, key))

    test_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-gap-test" '
        'data-test="%s" aria-pressed="false">%s</button>'
        % (e(tt["id"]), t(tt["label"]))
        for tt in tests)

    # Emit-both-show-one, eight ways: the two opening notes and both outcomes
    # of all three tests. Nothing here is ever assembled in JS, so an authored
    # `<em>` survives into any state and no sentence is built from an attribute.
    note_ps = ['<p data-note="empty">%s</p>' % rich(notes["empty"]),
               '<p data-note="filled" hidden>%s</p>' % rich(notes["filled"])]
    for tt in tests:
        note_ps.append('<p data-note="%s-on" hidden>%s</p>'
                       % (e(tt["id"]), rich(tt["on"])))
        note_ps.append('<p data-note="%s-off" hidden>%s</p>'
                       % (e(tt["id"]), rich(tt["off"])))

    canvas = ('<canvas class="ks3-gap-canvas" width="1800" height="520" '
              'role="img" aria-label="%s" data-gap-canvas></canvas>'
              % e(alt["template"].replace("{right}", alt["empty"])))
    foot = ('<p class="ks3-gap-caption">%s</p>'
            '<div class="ks3-gap-btns">%s</div>'
            % (t(a.get("caption", "")), test_btns))

    return ('<div class="ks3-gap" data-gap data-total="%d" '
            'data-empty-choice="%d" data-alt="%s" data-alt-filled="%s" '
            'data-alt-empty="%s" data-label-empty="%s" data-label-filled="%s" '
            'data-foot-empty="%s" data-foot-filled="%s">%s'
            '<div class="ks3-gap-rig" hidden data-gap-rig>%s'
            '<div class="ks3-gap-note" data-gap-note role="status">%s</div>'
            '</div></div>'
            % (len(tests), empty, e(alt["template"]), e(alt["filled"]),
               e(alt["empty"]), e(labels["empty"]), e(labels["filled"]),
               e(labels["foot_empty"]), e(labels["foot_filled"]),
               r_activity_options(choices),
               _canvas_frame(canvas, foot), "".join(note_ps)))
