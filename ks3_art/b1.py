"""ks3_art.b1 — B1's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import html
import json
import re
from ks3_art.kit import (
    _activity,
    _count_word,
    _option_li,
    _self_check,
    e,
    r_activity_options,
    rich,
    t,
)


# ── the CLASSIFY instruments (⊕ §4.8.2 · G3, G4) ─────────────────────────
#
# Two activity KINDS, not two block types. §5.1.1's block vocabulary stays
# closed: both render inside a `check` shell, which is what `core` names, and
# `activities[].kind` is what distinguishes them. See ks3_data/b1/__init__.py's
# header for the same ruling from the data side.
#
# ⚠️ BOTH ARE RENDERED WHOLE, AT BUILD TIME. Design's page holds all 28 lamp
# results and all 8 evidence lines in a JavaScript constant and templates the
# DOM from it; nothing in this generator works that way, and a page whose
# content only exists once a script has run is a page that says nothing when the
# script 404s. So every specimen panel and every evidence line is real markup,
# `hidden` until the student has earned it — exactly the shape `_rung_self`
# already uses for the ladder's success criteria.
#
# The consequence, stated plainly: a student who reads the page source can find
# the answers. That is true of the ladder criteria too, and it is the accepted
# trade in this system — the alternative is a lesson that is blank without JS.


def _lamp_li(test, result):
    """One lamp. R2: the state carries a WORD, never colour alone.

    The word starts as "Tap to test" and ks3.js writes "Yes"/"No" from
    `data-yes` when the lamp is tapped. It cannot be emitted resolved: the
    verdict IS the finding the tap is supposed to produce.

    The lamp is deliberately NOT a `.ks3-option`. Its resolved state differs by
    the specimen's property, and R3's runtime assertion requires every
    `.ks3-option` outside the ladder to render alike whichever was pressed — a
    lamp that lit differently for "yes" and "no" would fail it, and rightly, if
    it claimed to be an answer button. It is not one: it reports the SPECIMEN,
    not the student.
    """
    yes, note = (result + [""])[:2] if isinstance(result, list) else (result, "")
    return ('<li><button type="button" class="ks3-lamp" data-test="%s" '
            'data-yes="%d" aria-pressed="false">'
            '<span class="ks3-lamp-row">'
            '<span class="ks3-lamp-badge" aria-hidden="true">%s</span>'
            '<span class="ks3-lamp-name">%s</span>'
            '<span class="ks3-lamp-verdict" data-lamp-verdict>Tap to test</span>'
            '</span>'
            '<span class="ks3-lamp-note">%s</span></button></li>'
            % (e(test["key"]), 1 if yes else 0, t(test.get("initial", "")),
               t(test.get("name", "")), t(note)))
def _board_panel(a, spec, tests):
    """One specimen's whole instrument: gate, lamps, verdict.

    All four panels are in the document and only one is shown, which is what
    makes the four instruments' progress independent WITHOUT any state to keep:
    the DOM is the state. Switching specimens shows a panel that still holds
    whatever the student did to it.
    """
    results = spec.get("results") or {}
    predict = a.get("predict") or {}
    opts = "".join(
        _option_li(i, o, ' aria-pressed="false"')
        for i, o in enumerate(predict.get("options") or []))

    # ⊕ F4, Code's call (inventory §8c). Design REMOVES the prediction from the
    # DOM the moment it is made, so a student cannot see what they wagered.
    # It stays here, in its chosen state, and it stays CHANGEABLE — not
    # `disabled`. Both halves are forced: R3's runtime assertion fails an
    # activity option that is disabled, and fails a group whose options do not
    # all render alike, which a one-way gate would produce the moment its
    # unchosen sibling stayed resting. Keeping it live satisfies F4 and R3 at
    # once, and contradicts nothing Design drew — the gate still opens the
    # board, and the board never closes again.
    gate = ('<div class="ks3-board-predict">'
            '<p class="ks3-board-ask">%s</p>'
            '<ul class="ks3-options ks3-board-options" role="list">%s</ul>'
            '</div>' % (t(predict.get("prompt", "")), opts))

    lamps = "".join(_lamp_li(x, results.get(x["key"])) for x in tests)

    verdict = ('<div class="ks3-reveal ks3-board-verdict" data-reveal hidden>'
               '<p class="ks3-board-verdict-head">%s</p>'
               '<p class="ks3-board-verdict-body">%s</p>'
               '<div class="ks3-board-extra">'
               '<span class="ks3-board-extra-label">%s</span>'
               '<span class="ks3-board-extra-answer">%s</span>'
               '<span class="ks3-board-extra-note">%s</span>'
               '</div></div>'
               % (rich(spec.get("verdict_head", "")),
                  rich(spec.get("verdict_body", "")),
                  t(spec.get("extra_label", "The eighth test")),
                  t(spec.get("extra_answer", "")),
                  rich(spec.get("extra_note", ""))))

    return ('<div class="ks3-board-panel" data-specimen="%s"%s>'
            '<p class="ks3-board-name">%s</p>'
            '<p class="ks3-board-blurb">%s</p>'
            '%s'
            '<div class="ks3-board-tests" data-board-tests hidden>'
            '<div class="ks3-board-head">'
            '<p class="ks3-board-instruction" data-board-instruction>'
            'Tap each test to run it.</p>'
            '<p class="ks3-board-tally" data-board-tally role="status">'
            '0 of %d lit</p></div>'
            '<ul class="ks3-lamps" role="list">%s</ul>'
            '%s</div></div>'
            % (e(spec["id"]), "" if spec.get("_first") else " hidden",
               t(spec.get("name", "")), t(spec.get("blurb", "")),
               gate, len(tests), lamps, verdict))
def r_test_board(a, act_id):
    """⊕ G3 — the seven-tests board. CLASSIFY's decision instrument.

    Validation is the same discipline `r_sim` applies to a sim payload: an
    instrument that renders half a specimen is worse than one that refuses to
    build, because the hole is silent and the lesson still looks finished.
    """
    tests = a.get("tests") or []
    specimens = a.get("specimens") or []
    if not tests:
        raise ValueError("test-board %r declares no tests[] — there would be "
                         "nothing to tap." % act_id)
    keys = [x.get("key") for x in tests]
    if len(keys) != len(set(keys)) or not all(keys):
        raise ValueError(
            "test-board %r has missing or duplicate test key(s): %r. `initial` "
            "may repeat (MRS GREN has two R's); `key` may not, because it is "
            "what each specimen's results are looked up by." % (act_id, keys))
    if len(specimens) < 2:
        raise ValueError(
            "test-board %r declares %d specimen(s). The instrument's whole "
            "argument is comparison — a board with one specimen teaches that a "
            "score settles it, which is the misconception it exists to break."
            % (act_id, len(specimens)))
    if not (a.get("predict") or {}).get("options"):
        raise ValueError(
            "test-board %r has no predict.options — Law 4's gate is what opens "
            "the board, and without it the lamps are readable before the "
            "student has committed to anything." % act_id)
    for sp in specimens:
        missing = [k for k in keys if k not in (sp.get("results") or {})]
        if missing:
            raise ValueError(
                "test-board %r specimen %r supplies no result for test(s) %s. "
                "Every specimen answers every test or the board has a lamp that "
                "cannot resolve." % (act_id, sp.get("id"), ", ".join(missing)))

    tabs = "".join(
        '<li><button type="button" class="ks3-tab" data-specimen="%s" '
        'aria-pressed="%s">%s</button></li>'
        % (e(sp["id"]), "true" if i == 0 else "false", t(sp.get("name", "")))
        for i, sp in enumerate(specimens))

    panels = "".join(
        _board_panel(a, dict(sp, _first=(i == 0)), tests)
        for i, sp in enumerate(specimens))

    return ('<ul class="ks3-tabs" role="list">%s</ul>%s' % (tabs, panels))
def r_sort_rows(a, act_id):
    """⊕ G4 — the three-way sorter, plus MRB-196's self-check.

    R3 is the whole design constraint here and it is obeyed twice over: a chip
    takes the same chosen treatment whichever category it names, and after the
    reveal a wrong row is pixel-identical to a right one. The page states what
    settles each item; it never says whether the student had it.

    ⚖️ THE SELF-CHECK (MRB-196, ruled by Mide 13 Aug 2026). Design's sorter
    reveals eight answers and never asks the student whether they matched, so
    the student commits and never finds out — which Law 4 forbids. The record
    carries `self_check` and it renders ONLY once the evidence is showing,
    because before that there is nothing to compare against. There is no
    `answer` key and there must never be one: nothing on any option button and
    nothing on any row changes by what is picked. The page asks; it does not
    grade.
    """
    cats = a.get("categories") or []
    items = a.get("items") or []
    if len(cats) < 2:
        raise ValueError("sort-rows %r needs at least 2 categories, got %d — "
                         "one box is not a sort." % (act_id, len(cats)))
    if not items:
        raise ValueError("sort-rows %r declares no items[]." % act_id)
    for it in items:
        if it.get("answer") not in cats:
            raise ValueError(
                "sort-rows %r item %r answers %r, which is not one of the "
                "declared categories %r. The evidence line's lead word IS the "
                "answer, so a stray one renders a category the student was "
                "never offered." % (act_id, it.get("id"), it.get("answer"), cats))
        if not (it.get("evidence") or "").strip():
            raise ValueError(
                "sort-rows %r item %r has no evidence. The reveal exists to say "
                "what settles each one; a blank line says nothing and the "
                "student has no way to self-mark it." % (act_id, it.get("id")))

    rows = []
    for it in items:
        chips = "".join(
            '<button type="button" class="ks3-sort-chip" data-cat="%s" '
            'aria-pressed="false">%s</button>' % (e(c), t(c)) for c in cats)
        # ⊕ F7, Code's call. Design's evidence carries `data-reveal` WITHOUT
        # `class="ks3-reveal"`, so `animation-name` resolves to `none` and the
        # 220ms reveal never fires — measured, inventory §3.2. The class is the
        # animation's only hook; `.ks3-sort-evidence` then takes the panel back
        # off it, exactly as `.ks3-dark .ks3-reveal` already re-paints the same
        # base class for the ink-dark surface.
        rows.append(
            '<li class="ks3-sortrow" data-item="%s">'
            '<div class="ks3-sortrow-main">'
            '<span class="ks3-sortrow-name">%s</span>'
            '<span class="ks3-sortrow-chips">%s</span></div>'
            '<p class="ks3-reveal ks3-sort-evidence" data-reveal hidden>'
            '<strong class="ks3-sort-answer">%s</strong> — %s</p></li>'
            % (e(it.get("id", "")), t(it.get("name", "")), chips,
               t(it["answer"]), rich(it["evidence"])))

    self_check = _self_check(a, act_id)

    return ('<ul class="ks3-sortrows" role="list">%s</ul>'
            '<div class="ks3-sort-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-sort-reveal" '
            'data-sort-reveal disabled>%s</button>'
            '<span class="ks3-sort-progress" data-sort-progress '
            'data-total="%d" data-total-word="%s">0 of %d sorted</span>'
            '</div>%s'
            % ("".join(rows),
               t(a.get("reveal_label") or "Show what settles each one"),
               len(items), e(_count_word(len(items))), len(items), self_check))
def r_critique_steps(a, act_id):
    """⊕ Judge someone else's method before you write your own.

    Six steps, three of which cost him. A CHECKBOX SET, not a radio group —
    the student marks every step they would change, so the demand is "find all
    the faults", not "find the fault". Rendered as an empty section before this.

    R3 holds and is worth stating: the verdict panels are keyed off the STEP's
    own `fault`, which is the method's property and not the student's. Every
    step opens identically whether or not it was tapped.
    """
    steps = a.get("steps") or []
    if len(steps) < 3:
        raise ValueError("critique-steps %r declares %d step(s)."
                         % (act_id, len(steps)))
    if not any(s.get("fault") for s in steps):
        raise ValueError(
            "critique-steps %r has no faulty step — there is nothing to find, "
            "and a student who taps nothing is right." % act_id)

    rows = "".join(
        '<li class="ks3-step" data-fault="%d">'
        '<button type="button" class="ks3-step-btn" aria-pressed="false">'
        '<span class="ks3-step-num" aria-hidden="true">%d</span>'
        '<span class="ks3-step-text">%s</span></button>'
        '<p class="ks3-step-verdict" hidden data-reveal>'
        '<strong class="ks3-step-word">%s</strong> %s</p></li>'
        % (1 if s.get("fault") else 0, i + 1, rich(s.get("text", "")),
           t(s.get("word", "")), rich(s.get("verdict", "")))
        for i, s in enumerate(steps))

    return ('<ul class="ks3-steps" role="list">%s</ul>'
            '<div class="ks3-steps-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-steps-reveal" '
            'data-steps-reveal disabled>%s</button>'
            '<span class="ks3-steps-progress" data-steps-progress '
            'data-zero="%s">%s</span></div>'
            % (rows, t(a.get("reveal_label") or "Open them up"),
               e(a.get("progress_zero") or "Pick at least one"),
               t(a.get("progress_zero") or "Pick at least one")))
def r_fifa_construct(lesson, a, act_id):
    """⊕ MRB-204 step 4 — the student fills the steps before full FIFA.

    Law 5's "the same artifact, produced by the student": the stepper's letters
    and these fields' letters must match in order, and the model, the fields
    and the success criteria must be the same length. Asserted here rather
    than trusted, because the claim is the whole point of the pairing.

    Two defects on Design's page are fixed rather than reproduced, both stated:

    1. **Check accepts an empty attempt** and reveals the full model. A student
       who taps it first has been handed the answer before writing anything,
       which is what steps 3 and 4 exist to prevent. Gated on a non-empty field.
    2. **The typed working does not survive a re-render.** `<input value=…>`
       sets an ATTRIBUTE, which the element reads only as its default, so the
       first tick wipes what the student wrote. No `value` attribute is emitted.
    """
    fields = a.get("fields") or []
    model = a.get("model") or []
    success = a.get("success") or []
    if not (len(fields) == len(model) == len(success)):
        raise ValueError(
            "fifa-construct %r has %d fields, %d model lines and %d success "
            "criteria. Law 5 says the student produces the SAME artifact, and "
            "three different lengths cannot describe one."
            % (act_id, len(fields), len(model), len(success)))

    stepper = next((x for x in (lesson.get("activities") or [])
                    if x.get("kind") == "worked-example" and x.get("staged")), None)
    if stepper:
        want = [s.get("letter") for s in (stepper.get("fifa") or [])]
        got = [f.get("letter") for f in fields]
        if want != got:
            raise ValueError(
                "fifa-construct %r asks for %r and the worked example it "
                "mirrors shows %r. The letters and their ORDER are the shared "
                "artifact." % (act_id, got, want))

    rows = "".join(
        '<div class="ks3-fifa-field">'
        '<label class="ks3-fifa-label" for="%s">'
        '<span class="ks3-fifa-letter" aria-hidden="true">%s</span> %s</label>'
        '<input class="ks3-fifa-input" type="text" id="%s" data-fifa-input '
        'placeholder="%s" autocomplete="off"></div>'
        % (e("ks3-fifa-%s" % f["id"]), t(f.get("letter", "")),
           t(f.get("label", "")), e("ks3-fifa-%s" % f["id"]),
           e(f.get("placeholder", "")))
        for f in fields)

    lines = "".join('<li class="ks3-model-line">%s</li>' % t(m) for m in model)
    ticks = "".join(
        '<li class="ks3-tick"><input type="checkbox" id="%s" data-crit>'
        '<label for="%s"><span class="ks3-tick-num">%d</span> %s</label></li>'
        % (e("ks3-fifa-crit-%s-%d" % (act_id, i)),
           e("ks3-fifa-crit-%s-%d" % (act_id, i)), i + 1, t(s))
        for i, s in enumerate(success))

    return ('<div class="ks3-construct">%s'
            '<div class="ks3-construct-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-construct-check" '
            'data-construct-check disabled>%s</button>'
            '<span class="ks3-construct-hint" data-construct-hint>%s</span>'
            '</div>'
            '<div class="ks3-construct-out" hidden data-reveal>'
            '<p class="ks3-model-lead">%s</p>'
            '<ol class="ks3-model" role="list">%s</ol>'
            '<p class="ks3-crit-lead">Did you do all of these?</p>'
            '<ul class="ks3-ticks" role="list">%s</ul>'
            '<p class="ks3-construct-tally" hidden data-construct-tally '
            'role="status">%s</p></div></div>'
            % (rows, t(a.get("check_label") or "Check my working"),
               t("Write at least one step first"),
               t(a.get("model_lead", "")), lines, ticks,
               t(a.get("tally_met", ""))))
def r_cell_bench(a, act_id):
    """⊕ MODEL's flagship — seven parts, two cells, two ways of looking.

    b1-03 is the approved reference screen for MODEL, which carries 50 lesson
    slots, so this is the single highest-reach component in B1. It rendered as
    an empty section.

    The instrument's argument is the second view. A textbook drawing shows all
    seven parts; a school microscope shows three. Switching between them is
    how a student learns to tell "not there" from "there but you cannot see
    it" — which is the misconception the lesson exists to break, and it cannot
    be taught by a diagram alone.

    Every part carries `mark[specimen]` — the circles the canvas draws over
    the chosen part — so the marks live with the part rather than with the
    drawing, and a part that is absent from a specimen simply has none.
    """
    parts = a.get("parts") or []
    specimens = a.get("specimens") or []
    views = a.get("views") or []
    if not parts:
        raise ValueError("cell-bench %r declares no parts[]." % act_id)
    if len(specimens) < 2:
        raise ValueError(
            "cell-bench %r declares %d specimen(s). The whole instrument is "
            "'watch which parts stay put when you switch the cell'."
            % (act_id, len(specimens)))
    for p in parts:
        for sp in specimens:
            marks = (p.get("mark") or {}).get(sp["id"])
            if marks is None and p.get("where") != "plant":
                raise ValueError(
                    "cell-bench %r part %r has no mark for specimen %r. A part "
                    "the student can select and the canvas cannot point at is "
                    "a control that does nothing."
                    % (act_id, p.get("id"), sp["id"]))

    labels = a.get("control_labels") or {}
    where_labels = a.get("where_labels") or {}
    start = a.get("start") or specimens[0]["id"]

    def seg_row(name, items, current, extra=""):
        btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-bench-%s" '
            'data-%s="%s" aria-pressed="%s"%s>%s</button>'
            % (name, name, e(it["id"]),
               "true" if it["id"] == current else "false",
               ' data-locked="1"' if it.get("locked_until_gate") else "",
               t(it.get("label", "")))
            for it in items)
        return ('<div class="ks3-bench-control"><p class="ks3-bench-control-label">'
                '%s</p><div class="ks3-bench-seg">%s</div></div>'
                % (t(labels.get(name, name.title())), btns))

    controls = seg_row("specimen", specimens, start)
    if views:
        controls += seg_row("view", views, views[0]["id"])

    gate = ""
    g = a.get("gate") or {}
    if g.get("options"):
        gate = ('<div class="ks3-bench-gate" data-bench-gate>'
                '<p class="ks3-bench-gate-q">%s</p>%s</div>'
                % (t(g.get("q", "")), r_activity_options(g["options"])))

    part_btns = "".join(
        '<li><button type="button" class="ks3-part" data-part="%s" '
        'aria-pressed="%s"><span class="ks3-part-num" aria-hidden="true">%s'
        '</span><span class="ks3-part-body">'
        '<span class="ks3-part-name">%s</span>'
        '<span class="ks3-part-tag" data-where="%s"></span>'
        '</span></button></li>'
        % (e(p["id"]), "true" if i == 0 else "false", t(p.get("num", "")),
           t(p.get("name", "")), e(p.get("where", "")))
        for i, p in enumerate(parts))

    meta = json.dumps({
        "parts": [{"id": p["id"], "num": p.get("num", ""),
                   "name": p.get("name", ""), "where": p.get("where", ""),
                   "job": p.get("job", ""), "detail": p.get("detail", ""),
                   "visible": bool(p.get("visible")),
                   "scope_note": p.get("scope_note", ""),
                   "mark": p.get("mark") or {}} for p in parts],
        "specimens": [{"id": s["id"], "label": s.get("label", ""),
                       "art": s.get("art", ""), "alt": s.get("alt", ""),
                       "caption": s.get("caption", ""),
                       "tally": s.get("tally", ""),
                       "absent_tag": s.get("absent_tag", ""),
                       "absent_detail": s.get("absent_detail", "")}
                      for s in specimens],
        "where_labels": where_labels,
        "scope_words": a.get("scope_words") or {},
        "space": a.get("mark_space") or {"w": 900, "h": 560},
    }, sort_keys=True)

    return ('<div class="ks3-bench-controls">%s</div>%s'
            '<div class="ks3-bench" data-bench-grid="1" data-cellbench="%s">'
            '<ul class="ks3-parts" role="list">%s</ul>'
            '<div class="ks3-bench-main">'
            '<div class="ks3-bench-figure">'
            '<canvas class="ks3-bench-canvas" width="1800" height="1120" '
            'role="img" data-bench-canvas></canvas>'
            '<p class="ks3-bench-caption" data-bench-caption></p></div>'
            '<div class="ks3-readout" data-readout>'
            '<div class="ks3-readout-head">'
            '<span class="ks3-readout-num" aria-hidden="true" data-readout-num>'
            '</span>'
            '<span class="ks3-readout-name" data-readout-name></span>'
            '<span class="ks3-readout-where" data-readout-where></span></div>'
            '<p class="ks3-readout-job" data-readout-job></p>'
            '<p class="ks3-readout-detail" data-readout-detail></p>'
            '<p class="ks3-readout-scope" hidden data-readout-scope>'
            '<strong class="ks3-readout-scope-word" data-readout-scope-word>'
            '</strong> <span data-readout-scope-note></span></p></div>'
            '<p class="ks3-bench-tally" data-bench-tally></p>'
            '</div></div>'
            % (controls, gate, e(meta), part_btns))
def r_sort_pairs(a, act_id):
    """⊕ The two-way sorter — wall or membrane, the pair swapped most often.

    Rendered as an empty section. Structurally the three-way sorter's sibling,
    and deliberately NOT built on it: this one sends each statement to one of
    two named things rather than sorting rows into categories, and Design draws
    it as a row with the two names as buttons. One component that tried to be
    both would be the "nearest shape that exists" failure again.

    R3: nothing is marked here, and the intro says so in as many words.
    """
    rows = a.get("rows") or []
    cats = a.get("categories") or []
    if len(cats) != 2:
        raise ValueError(
            "sort-pairs %r declares %d categories. It is the TWO-way sorter; "
            "three or more is `sort-rows`." % (act_id, len(cats)))
    ids = {c["id"] for c in cats}
    for r in rows:
        if r.get("answer") not in ids:
            raise ValueError(
                "sort-pairs %r row %r answers %r, which is neither of %r."
                % (act_id, r.get("id"), r.get("answer"), sorted(ids)))

    lookup = {c["id"]: c.get("label", c["id"]) for c in cats}
    out = []
    for r in rows:
        chips = "".join(
            '<button type="button" class="ks3-seg-btn ks3-pair-chip" '
            'data-cat="%s" aria-pressed="false">%s</button>'
            % (e(c["id"]), t(c.get("label", ""))) for c in cats)
        out.append(
            '<li class="ks3-pairrow" data-row="%s">'
            '<p class="ks3-pairrow-text">%s</p>'
            '<div class="ks3-pairrow-chips">%s</div>'
            '<p class="ks3-pairrow-note" hidden data-reveal>'
            '<strong class="ks3-pairrow-word">%s</strong> %s</p></li>'
            % (e(r.get("id", "")), rich(r.get("text", "")), chips,
               t(lookup[r["answer"]] + "."), rich(r.get("note", ""))))

    unit = a.get("progress_unit") or "sent"
    panel = _pair_panel(a.get("reveal_panel"))
    return ('<ul class="ks3-pairrows" role="list">%s</ul>'
            '<div class="ks3-pair-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-pair-reveal" '
            'data-pair-reveal disabled>%s</button>'
            '<span class="ks3-pair-progress" data-pair-progress '
            'data-total="%d" data-unit="%s">0 of %d %s</span></div>%s'
            % ("".join(out), t(a.get("reveal_label") or "Show the answers"),
               len(rows), e(unit), len(rows), t(unit), panel))
def _pair_panel(payload):
    """The sorter's answer panel — `{headline, body}` or a bare string.

    ⊕ MRB-257 · audit 5.3 / MRB-253 — THIS SHIPPED A PYTHON DICT TO STUDENTS.
    The line was `rich(a["reveal_panel"])`, and `rich()` is `html.escape()` with
    two tags put back: handed a dict it stringifies it, so `animal-and-plant-
    cells` published

        {'headline': 'The wall is the box. The membrane is the door.', 'body': …}

    as the panel a student opens after sorting five statements. Verified as the
    only occurrence in 58 lessons — because it is the only record that authored
    the two-key form, which nothing on the render side ever knew about.

    Both shapes are accepted rather than one being declared wrong. The dict is
    the better authoring shape (a headline earns its own line), the string is
    what every other record would write, and a renderer that raises on the
    string form would turn a schema preference into a build failure for an
    author who did the obvious thing.

    ⚠️ `wirePairs()` in shared/ks3.js only calls `setHidden(panel, false)` — it
    never renders a payload — so the markup this returns is exactly what the
    student reads. Nothing downstream can rescue a bad shape here.

    The 14px gap is inline rather than a class because `.ks3-pair-panel` has no
    `p + p` rule and this generator does not invent classes the stylesheet has
    never heard of; 14px is the value `.ks3-reveal-panel p + p` already uses for
    the same job. Handed off to be moved into shared/ks3.css.
    """
    if not payload:
        return ""
    if isinstance(payload, dict):
        head = payload.get("headline") or ""
        body = payload.get("body") or ""
        inner = ""
        if head:
            inner += "<p><strong>%s</strong></p>" % rich(head)
        if body:
            inner += "<p>%s</p>" % rich(body)
    else:
        inner = rich(payload)
    return '<div class="ks3-pair-panel" hidden data-pair-panel>%s</div>' % inner
def r_fit_parts(lesson, a, act_id):
    """⊕ Build four real cells from one parts list, then run them.

    "Which parts" becomes a consequence of "what job". Rendered as an empty
    section. The parts list is `parts_from` — it names the bench's activity, so
    the two instruments share one list and a part cannot exist in the builder
    and not on the bench.

    ⊕ MRB-242 — takes `lesson` (which is all `_kinds_taking_lesson` needs to
    see: it asks the signature) so that `parts_from` can be RESOLVED here, at
    build time, instead of being trusted at runtime. The instrument shipped
    with zero part chips for a fortnight because the runtime lookup silently
    found the wrong element and `catch {}` swallowed it; the fix in
    `wireFit` reads the bench through this id, and a build error is the only
    thing that can stop a renamed or misspelt id doing it again quietly.
    """
    specimens = a.get("specimens") or []
    if not specimens:
        raise ValueError("fit-parts %r declares no specimens[]." % act_id)
    for sp in specimens:
        if not sp.get("needs"):
            raise ValueError(
                "fit-parts %r specimen %r needs no parts at all — there would "
                "be nothing to get right." % (act_id, sp.get("id")))

    # ⊕ MRB-242 / R5 — `parts_from` finally has a read site, and this is half
    # of it. The runtime half is `wireFit`, which resolves the bench by
    # `[data-activity="<parts_from>"]`; both halves fail loudly rather than
    # rendering an instrument with nothing in it.
    src_id = a.get("parts_from") or ""
    src = _activity(lesson, src_id) if src_id else None
    if not src or not src.get("parts"):
        raise ValueError(
            "fit-parts %r names parts_from=%r, which is not an activity in "
            "this lesson carrying a parts[] list. The builder's chips ARE the "
            "bench's parts; with no source there is nothing to install."
            % (act_id, src_id))

    # ⊕ MRB-242 / R5 — the verdict copy is AUTHORED, in full, or the build
    # stops. `wireFit` used to read `verdicts.ok` and `verdicts.problem`, two
    # keys this lesson has never authored, so every run printed one of two
    # strings hardcoded in the ENGINE — "It runs." / "It runs, after a
    # fashion." — and all five real headlines and all three badges were dead
    # keys. That is the B1-replay failure exactly: 146 unread keys, one of
    # them an approved science correction that never reached a student.
    #
    # So there is no fallback prose, here or in the engine. Every word a
    # student reads is a word someone wrote for this lesson; a missing one is
    # a build error, the way `parts_from` above is.
    verdicts = a.get("verdicts") or {}
    for state, keys in (("works", ("badge", "headline")),
                        ("waste", ("badge", "headline")),
                        ("fails", ("badge", "headline_one", "headline_many"))):
        block = verdicts.get(state) or {}
        for k in keys:
            if not str(block.get(k) or "").strip():
                raise ValueError(
                    "fit-parts %r authors no verdicts[%r][%r]. A run lands in "
                    "one of three states — works / waste / fails — and each "
                    "carries its own badge and headline. The engine has no "
                    "fallback prose and must never invent student-facing "
                    "copy." % (act_id, state, k))
    # `headline_many` is the plural branch and the number is the only thing
    # that varies in it, so it has to say where the number goes.
    many = str(verdicts["fails"]["headline_many"])
    if "{n}" not in many:
        raise ValueError(
            "fit-parts %r: verdicts['fails']['headline_many'] is chosen when "
            "two or more parts are missing and must carry the {n} "
            "placeholder for that count. Got %r." % (act_id, many))

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-fit-tab" data-fit="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(sp["id"]), "true" if i == 0 else "false", t(sp.get("label", "")))
        for i, sp in enumerate(specimens))

    meta = json.dumps({
        "specimens": [{"id": s["id"], "label": s.get("label", ""),
                       "kind": s.get("kind", ""), "job": s.get("job", ""),
                       "where": s.get("where", ""),
                       "needs": list(s.get("needs") or []),
                       "waste": s.get("waste") or {},
                       "note": s.get("note", "")} for s in specimens],
        "labels": {
            "job": a.get("job_label", "The job"),
            "install": a.get("install_label", "Install the parts"),
            "run": a.get("run_label", "Run this cell"),
            "rerun": a.get("rerun_label", "Run it again"),
            "clear": a.get("clear_label", "Strip it back out"),
            "empty": a.get("install_empty_hint", "Install something first"),
            # ⊕ MRB-242 — `unit` ("cells run") is gone. It was serialised here
            # and read by nothing: the words belong to the BLOCK-HEAD counter
            # Design draws, which is now authored as `head_counter` and
            # rendered by `_head_counter` like every other one. `installed` is
            # the foot hint's unit word and is read — "5 of 7 installed".
            "installed": a.get("install_unit", "installed"),
        },
        "verdicts": verdicts,
        "finding_words": a.get("finding_words") or {},
        "consequence": a.get("consequence") or {},
        "note_when": a.get("note_when", ""),
        "waste_fallback": a.get("waste_fallback", ""),
        "parts_from": a.get("parts_from", ""),
    }, sort_keys=True)

    return ('<div class="ks3-fit" data-fit-spec="%s">'
            '<div class="ks3-fit-tabs">%s</div>'
            '<div class="ks3-fit-job"><p class="ks3-fit-job-label"></p>'
            '<p class="ks3-fit-job-text"></p>'
            '<p class="ks3-fit-job-where"></p></div>'
            '<p class="ks3-fit-install-label"></p>'
            '<ul class="ks3-fit-parts" role="list" data-fit-parts></ul>'
            '<div class="ks3-fit-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-fit-run" '
            'data-fit-run></button>'
            '<button type="button" class="ks3-fit-clear" data-fit-clear>'
            '</button>'
            '<span class="ks3-fit-progress" data-fit-progress></span></div>'
            '<div class="ks3-fit-out" hidden data-reveal>'
            # ⊕ MRB-242 — Design draws a mono uppercase pill ABOVE the
            # headline, its fill carrying the state (reference line 328 /
            # `verdictBadgeStyle` line 1243). No badge element was ever
            # emitted, so `verdicts.*.badge` had nowhere to land.
            '<p class="ks3-fit-badge" data-fit-badge></p>'
            '<p class="ks3-fit-verdict" data-fit-verdict></p>'
            '<ul class="ks3-fit-findings" role="list" data-fit-findings></ul>'
            '<p class="ks3-fit-note" data-fit-note></p></div>'
            '</div>' % (e(meta), tabs))
ZOOM_DRAWINGS = {"plant", "plant-shoot", "one-leaf", "leaf-section", "one-cell"}
def r_zoom_ladder(a, act_id):
    """⊕ Five stops from a whole plant to one cell, without leaving the leaf.

    A slider and a tick row over one canvas, with an orange dashed box showing
    where the NEXT stop down is hiding inside this one. The panel underneath
    says what this level can do that the level below cannot — which is the
    lesson's whole argument, and the reason the ladder is not a size chart.

    The `next_box` rectangles are AUTHORED, one per level in the payload's own
    design space, so the drawing and the box cannot drift apart. The last level
    has none: there is no stop below a cell.
    """
    levels = a.get("levels") or []
    if len(levels) < 2:
        raise ValueError("zoom-ladder %r declares %d level(s)."
                         % (act_id, len(levels)))
    for lv in levels:
        if lv.get("drawing") not in ZOOM_DRAWINGS:
            raise ValueError(
                "zoom-ladder %r level %r asks for drawing %r. Known: %s."
                % (act_id, lv.get("tick"), lv.get("drawing"),
                   ", ".join(sorted(ZOOM_DRAWINGS))))

    canvas = a.get("canvas") or {}
    buf = canvas.get("buffer") or [1800, 1000]
    space = canvas.get("design_space") or [900, 500]
    start = a.get("start")
    idx = next((i for i, lv in enumerate(levels)
                if lv.get("tick", "").lower().startswith(str(start).lower())), 0)

    ticks = "".join(
        '<button type="button" class="ks3-seg-btn ks3-zoom-tick" '
        'data-zoom="%d" aria-pressed="%s">%s</button>'
        % (i, "true" if i == idx else "false", t(lv.get("tick", "")))
        for i, lv in enumerate(levels))

    panels = "".join(
        '<div class="ks3-zoom-panel" data-zoom="%d"%s>'
        '<p class="ks3-zoom-name">%s</p>'
        '<p class="ks3-zoom-what">%s</p>'
        '<div class="ks3-zoom-gain">'
        '<p class="ks3-zoom-gain-label">%s</p>'
        '<p class="ks3-zoom-gain-text">%s</p></div>'
        '<p class="ks3-zoom-human"><strong>%s</strong> %s</p></div>'
        % (i, "" if i == idx else " hidden", t(lv.get("name", "")),
           rich(lv.get("what", "")), t(lv.get("gain_label", "")),
           rich(lv.get("gain", "")), t(a.get("human_prefix") or "In you:"),
           rich(lv.get("human", "")))
        for i, lv in enumerate(levels))

    meta = json.dumps(
        [{"drawing": lv["drawing"], "box": lv.get("next_box"),
          "size": lv.get("size", ""), "alt": lv.get("alt", "")}
         for lv in levels], sort_keys=True)

    aid = "ks3-zoom-%s" % act_id
    fmt = a.get("step_format") or "Stop {n} of {total}"
    return ('<div class="ks3-zoom" data-zoom-levels="%s" data-space="%d,%d" '
            'data-box-label="%s">'
            '<div class="ks3-zoom-frame">'
            '<canvas class="ks3-zoom-canvas" width="%d" height="%d" role="img" '
            'aria-label="%s" data-zoom-canvas></canvas>'
            '<div class="ks3-zoom-controls">'
            '<div class="ks3-zoom-head">'
            '<p class="ks3-zoom-step" data-zoom-step data-format="%s">%s</p>'
            '<p class="ks3-zoom-size" data-zoom-size>%s</p></div>'
            '<label class="ks3-visually-hidden" for="%s">%s</label>'
            '<input class="ks3-zoom-range" type="range" id="%s" min="0" '
            'max="%d" step="1" value="%d" data-zoom-range>'
            '<div class="ks3-zoom-ticks">%s</div>'
            '</div></div>%s</div>'
            % (e(meta), space[0], space[1],
               e(a.get("next_box_label") or "NEXT STOP IS HERE"),
               buf[0], buf[1], e(levels[idx].get("alt", "")), e(fmt),
               t(fmt.replace("{n}", str(idx + 1))
                    .replace("{total}", str(len(levels)))),
               t(levels[idx].get("size", "")), e(aid),
               t(a.get("slider_label") or "Zoom level"), e(aid),
               len(levels) - 1, idx, ticks, panels))
def r_sort_task(a, act_id):
    """⊕ Eight things that get put on the wrong rung.

    THE activity Mide rejected by name on 11 August: "name the level for each
    of these eight and say what settled it" rendered as a four-option multiple
    choice with eight items in the prompt, because CLASSIFY had no sorting
    component and the content was forced into the nearest shape that existed.

    ⚠️ R3 and the row. After the reveal the ROW is marked — inset on ink when
    the student had it, alert-tint on the alert border when they did not — and
    the CHOICE BUTTONS are untouched, identical before and after and identical
    on a right row and a wrong one. Verified by driving Design's page. The mark
    is on a container, never on a control, which is what keeps a deferred,
    self-service, student-opened mark clear of R3. Do not move it onto the
    buttons for tidiness; that is the whole distinction.
    """
    items = a.get("items") or []
    choices = a.get("choices") or []
    if len(choices) < 3:
        raise ValueError(
            "sort-task %r offers %d rung(s). The awkward cases need every rung "
            "AND the off-ladder answer, or the hard ones have nowhere to go."
            % (act_id, len(choices)))
    for it in items:
        if it.get("answer") not in choices:
            raise ValueError(
                "sort-task %r item %r answers %r, which is not one of the "
                "offered rungs %r." % (act_id, it.get("id"), it.get("answer"),
                                       choices))

    rows = []
    for it in items:
        chips = "".join(
            '<button type="button" class="ks3-seg-btn ks3-rung-chip" '
            'data-rung="%s" aria-pressed="false">%s</button>' % (e(c), t(c))
            for c in choices)
        rows.append(
            '<li class="ks3-hardrow" data-item="%s" data-answer="%s">'
            '<p class="ks3-hardrow-item">%s</p>'
            '<div class="ks3-hardrow-chips">%s</div>'
            '<p class="ks3-hardrow-answer" hidden data-reveal>'
            '<strong class="ks3-hardrow-word">%s</strong> %s</p></li>'
            % (e(it.get("id", "")), e(it["answer"]), t(it.get("item", "")),
               chips, t(it["answer"] + "."), rich(it.get("note", ""))))

    counter = a.get("counter") or "{n} of {total} placed"
    return ('<ul class="ks3-hardrows" role="list">%s</ul>'
            '<div class="ks3-hard-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-hard-reveal" '
            'data-hard-reveal disabled>%s</button>'
            '<span class="ks3-hard-progress" data-hard-progress '
            'data-total="%d" data-format="%s">%s</span></div>'
            % ("".join(rows), t(a.get("gate_label") or "Open the answers"),
               len(items), e(counter),
               t(counter.replace("{n}", "0")
                        .replace("{total}", str(len(items))))))
def r_removal_cases(a, act_id):
    """⊕ Keep every cell alive. Remove the organisation.

    Four cases, each a commitment then a consequence. Replaces the retired
    `system-parts` sim, which is why b1-05 has no `.ks3-sim` at all and why the
    parity gate's `sim-unlocked` drive found nothing to unlock on this page.

    ⚠️ CORRECTION TO DESIGN. `caseLevelLost` is `'Level lost: ' + kase.lost`
    and only ONE of the four cases authors `lost`, so Design's own page renders
    **"Level lost: undefined"** on three of them. The pill is omitted when
    there is nothing to name.
    """
    cases = a.get("cases") or []
    if not cases:
        raise ValueError("removal-cases %r declares no cases[]." % act_id)

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-removal-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(k["id"]), "true" if i == 0 else "false", t(k.get("label", "")))
        for i, k in enumerate(cases))

    panels = []
    for i, k in enumerate(cases):
        lost = (k.get("lost") or "").strip()
        pill = ('<p class="ks3-removal-lost">%s%s</p>'
                % (t(a.get("lost_prefix") or "Level lost: "), t(lost))
                if lost else "")
        panels.append(
            '<div class="ks3-removal-panel" data-case="%s"%s>'
            '<div class="ks3-removal-what">'
            '<p class="ks3-removal-what-label">%s</p>'
            '<p class="ks3-removal-what-text">%s</p>'
            '<p class="ks3-removal-intact">%s</p></div>'
            '<div class="ks3-removal-predict">'
            '<p class="ks3-commit">%s</p>%s</div>'
            '<div class="ks3-removal-out" hidden data-reveal>%s'
            '<p class="ks3-removal-headline">%s</p>'
            '<p class="ks3-removal-body">%s</p>'
            '<p class="ks3-removal-principle"><strong>%s</strong> %s</p>'
            '</div></div>'
            % (e(k["id"]), "" if i == 0 else " hidden",
               t(a.get("what_label") or "What we did"),
               rich(k.get("what", "")), rich(k.get("intact", "")),
               t(a.get("commit") or "Commit first. What stops working?"),
               r_activity_options(k.get("predict") or []),
               pill, rich(k.get("headline", "")), rich(k.get("body", "")),
               t(a.get("principle_prefix") or "The principle:"),
               rich(k.get("principle", ""))))

    counter = a.get("counter") or "{n} of {total} explored"
    return ('<div class="ks3-removal" data-total="%d">'
            '<p class="ks3-removal-progress" data-removal-progress '
            'data-format="%s">%s</p>'
            '<p class="ks3-removal-lede">%s</p>'
            '<div class="ks3-removal-tabs">%s</div>%s</div>'
            % (len(cases), e(counter),
               t(counter.replace("{n}", "0")
                        .replace("{total}", str(len(cases)))),
               rich(a.get("lede", "")), tabs, "".join(panels)))
def r_system_bench(a, act_id):
    """⊕ SYSTEM's reference screen — four cells, the same seven parts, tuned.

    Rendered as an empty section before this: the payload declares
    `specimens[]` with `job`/`where`/`tuning`/`problem`/`drawing` and the
    generic shell reads none of them.

    Emit-all-show-one, the same shape the seven-tests board uses. Four panels
    and four figures are in the document and one of each is shown, so the DOM
    is the state and going back to a cell finds it as you left it.

    ⚠️ The cell picker is NOT the segmented control, and drift 4 says so
    explicitly: b1-04's light `seg()` branch is `width:100%`, `text-align:left`,
    `min-height:56px`, `--ks3-r-option` — a full-width option ROW that happens
    to share a helper name with the segment. Generating it as a segment would
    produce the wrong component. It gets `.ks3-bench-cell` of its own.
    """
    specimens = a.get("specimens") or []
    if len(specimens) < 2:
        raise ValueError(
            "system-bench %r declares %d specimen(s). The instrument's claim is "
            "that the SAME seven parts are tuned differently, and one cell "
            "cannot show a difference." % (act_id, len(specimens)))
    for sp in specimens:
        if not sp.get("tuning"):
            raise ValueError(
                "system-bench %r specimen %r declares no tuning[] — the bench "
                "would show a cell with nothing turned up or down, which is the "
                "one thing this lesson says never happens."
                % (act_id, sp.get("id")))
        if sp.get("drawing") not in CELL_DRAWINGS:
            raise ValueError(
                "system-bench %r specimen %r asks for drawing %r, which the "
                "engine cannot paint. Known: %s."
                % (act_id, sp.get("id"), sp.get("drawing"),
                   ", ".join(sorted(CELL_DRAWINGS))))

    start = a.get("start") or specimens[0].get("id")
    picker, figures, panels = [], [], []
    for sp in specimens:
        on = sp.get("id") == start
        picker.append(
            '<li><button type="button" class="ks3-bench-cell" data-cell="%s" '
            'aria-pressed="%s">'
            '<span class="ks3-bench-cell-name">%s</span>'
            '<span class="ks3-bench-cell-tag">%s</span></button></li>'
            % (e(sp["id"]), "true" if on else "false",
               t(sp.get("name", "")), t(sp.get("tag", ""))))

        figures.append(
            '<div class="ks3-bench-figure" data-cell="%s"%s>'
            '<canvas class="ks3-bench-canvas" width="1800" height="1120" '
            'data-drawing="%s" role="img" aria-label="%s"></canvas>'
            '<p class="ks3-bench-caption">%s</p></div>'
            % (e(sp["id"]), "" if on else " hidden", e(sp["drawing"]),
               e(sp.get("alt", "")), t(sp.get("caption", ""))))

        dials = "".join(
            '<li class="ks3-tune"><span class="ks3-tune-dial" '
            'data-dial="%s" aria-hidden="true">%s</span>'
            '<span class="ks3-tune-body">'
            '<span class="ks3-tune-part">%s</span>'
            '<span class="ks3-tune-why">%s</span></span></li>'
            % (e(d.get("dial", "")), t(d.get("dial", "")),
               t(d.get("part", "")), rich(d.get("why", "")))
            for d in sp["tuning"])

        panels.append(
            '<div class="ks3-bench-panel" data-cell="%s"%s>'
            '<p class="ks3-bench-eyebrow">Its job</p>'
            '<p class="ks3-bench-job">%s</p>'
            '<p class="ks3-bench-where">%s</p>'
            '<ul class="ks3-tuning" role="list">%s</ul>'
            '<p class="ks3-bench-problem">'
            '<strong>The problem it solves:</strong> %s</p></div>'
            % (e(sp["id"]), "" if on else " hidden",
               rich(sp.get("job", "")), rich(sp.get("where", "")),
               dials, rich(sp.get("problem", ""))))

    return ('<div class="ks3-bench" data-bench-grid="1" data-current="%s">'
            '<ul class="ks3-bench-cells" role="list">%s</ul>'
            '<div class="ks3-bench-main">%s<div class="ks3-bench-read">%s</div>'
            '</div></div>'
            % (e(start), "".join(picker), "".join(figures), "".join(panels)))
# The four cell drawings `shared/ks3.js` can paint, ported verbatim from
# Design's approved b1-04. Named here so the generator can REFUSE a specimen
# that asks for one that does not exist, rather than emitting a blank canvas.
CELL_DRAWINGS = {"red", "root", "sperm", "nerve"}
def r_sabotage(lesson, a, act_id):
    """⊕ Break one thing and follow it out from the cell to the organism.

    The instrument that makes b1-04 a SYSTEM lesson rather than a labelling
    exercise: perturbation over naming. It rendered as an empty section.

    It follows the bench's chosen cell — `bench` names the bench's anchor —
    so every (cell × sabotage) panel is in the document and the pair that is
    showing is the bench's cell and this section's chosen sabotage.

    ⚖️ `named_conditions` is FALSE, ruled by Mide 14 Aug. Design's page carries
    both strings per sabotage and picks between them at RUNTIME from a prop,
    which leaves the named condition in the page source either way. It is
    resolved here, at build time, so `close` never reaches a browser: naming
    hereditary spherocytosis and multiple sclerosis to a Year 7 in a
    cell-biology lesson is what the ruling is about, and shipping it in a
    hidden attribute would honour the letter and miss the point.
    """
    safe = lesson.get("named_conditions") is False
    groups = a.get("specimens") or []
    if not groups:
        raise ValueError("sabotage %r declares no specimens[]." % act_id)

    panels, tabs, total = [], [], 0
    for g in groups:
        cell = g.get("specimen")
        opts = g.get("options") or []
        if not opts:
            raise ValueError(
                "sabotage %r offers cell %r no sabotages — there would be "
                "nothing to break." % (act_id, cell))
        for i, o in enumerate(opts):
            total += 1
            if safe and not (o.get("close_safe") or "").strip():
                raise ValueError(
                    "sabotage %r option %r has no `close_safe`, and this "
                    "lesson sets named_conditions False. The safe copy is the "
                    "one that ships; there is no silent fallback to the named "
                    "one." % (act_id, o.get("id")))
            tabs.append(
                '<button type="button" class="ks3-seg-btn ks3-sab-tab" '
                'data-cell="%s" data-sab="%s" aria-pressed="%s"%s>%s</button>'
                % (e(cell), e(o["id"]), "true" if i == 0 else "false",
                   "" if i == 0 else "", t(o.get("label", ""))))

            chain = "".join(
                '<li class="ks3-chain-link"><p class="ks3-chain-scale">%s</p>'
                '<p class="ks3-chain-text">%s</p></li>'
                % (t(c.get("scale", "")), rich(c.get("text", "")))
                for c in (o.get("chain") or []))

            panels.append(
                '<div class="ks3-sab-panel" data-cell="%s" data-sab="%s" hidden>'
                '<div class="ks3-sab-what">'
                '<p class="ks3-sab-what-label">The sabotage</p>'
                '<p class="ks3-sab-what-text">%s</p></div>'
                '<div class="ks3-sab-predict">'
                '<p class="ks3-commit">%s</p>%s</div>'
                '<div class="ks3-sab-chain" hidden data-reveal>'
                '<div class="ks3-sab-figure">'
                '<canvas class="ks3-sab-canvas" width="1800" height="840" '
                'data-drawing="%s" data-sab="%s" role="img" aria-label="%s">'
                '</canvas>'
                '<p class="ks3-sab-caption">%s</p></div>'
                '<p class="ks3-sab-pick" data-sab-pick></p>'
                '<ol class="ks3-chain" role="list">%s</ol>'
                '<p class="ks3-sab-close">%s</p></div></div>'
                % (e(cell), e(o["id"]), rich(o.get("what", "")),
                   t(a.get("commit") or "Commit first. What breaks first?"),
                   r_activity_options(o.get("predict") or []),
                   e(_drawing_for(lesson, cell)), e(o["id"]),
                   e(o.get("alt", "")), t(o.get("caption", "")),
                   chain,
                   rich((o.get("close_safe") if safe else o.get("close")) or "")))

    lede = a.get("lede") or ""
    # ⚠️ RICHIFY FIRST, THEN SUBSTITUTE — and this is a repair of a LIVE page.
    #
    # The placeholder was replaced before `rich()` ran, so the `<strong
    # data-sab-specimen>` went through `t()` and came out escaped: `rich()`
    # only un-escapes a BARE `<strong>`, so the opening tag with its attribute
    # stayed escaped while the closing `</strong>` was restored. b1-06 shipped
    # `Sabotage one thing about &lt;strong data-sab-specimen&gt;` as visible
    # text, in the lede of its own bench, on a page in front of students.
    #
    # Found by the escape-leak gate added in the same pass (verify_ks3.py), on
    # its first run — which is the fifth instance of this exact failure and the
    # first one no author had to notice by eye. `{specimen}` survives `rich()`
    # untouched because braces are not escaped, so the substitution lands on
    # the same string it always did.
    head_lede = rich(lede).replace(
        "{specimen}", '<strong data-sab-specimen></strong>')

    return ('<div class="ks3-sab" data-bench-ref="%s" data-total="%d">'
            '<p class="ks3-sab-progress" data-sab-progress>0 of %d sabotages '
            'run</p>'
            '<p class="ks3-sab-lede">%s</p>'
            '<div class="ks3-sab-tabs">%s</div>%s</div>'
            % (e(a.get("bench", "")), total, total, head_lede,
               "".join(tabs), "".join(panels)))
def _drawing_for(lesson, specimen_id):
    """Which drawing a sabotage's broken canvas paints — the cell's own."""
    for act in lesson.get("activities") or []:
        if act.get("kind") != "system-bench":
            continue
        for sp in act.get("specimens") or []:
            if sp.get("id") == specimen_id:
                return sp.get("drawing", "")
    raise ValueError(
        "sabotage names specimen %r, which the bench does not declare. The two "
        "instruments share a cast and this one is off it." % specimen_id)
def r_settles_it(a, act_id):
    """⊕ CONTRAST's flagship — sixteen judgements, and most of them decide nothing.

    Four mystery cells, four true facts each. The student marks every fact
    SETTLES IT or SETTLES NOTHING before anything is revealed. Most settle
    nothing, because they are true of single-celled organisms AND of cells
    inside a body, and the discriminating fact is never the most interesting
    one — cell 4 changes shape and engulfs another cell, and both settle
    nothing, because a white blood cell does both. Discriminators run 1, 2, 2,
    2 so the pattern never degrades into "find the one".

    Before this it rendered as an **empty section**: `r_activity` emitted the
    shell, the eyebrow and the heading and stopped, because the generic shell
    reads `prompt`/`options`/`reveal` and this payload declares
    `instruction`/`choice_labels`/`cases`. Not one of the sixteen judgements
    reached the page. The kind is inherited by 18 CONTRAST lessons.

    ⚖️ MRB-196, ruled by Mide 13 Aug, resolves the inventory's F36. Design
    computes whether the student agreed and then spends it on the why
    paragraph's COLOUR — `--ks3-ink` against `--ks3-ink-body`, about 6 ΔL*
    apart — which is a mark nobody can read and, being a mark at all, sits
    badly beside R3. The computation goes, the why paragraph takes one tone,
    and the self-check asks the student directly. Same shape as the rail on
    MRB-208: where the approved page and a ruling collide, the ruling wins.

    R3 is safe by construction and worth stating, because it looks close to
    the line. The row's ground records whether the FACT settles it — the
    page's own answer, revealed to everyone identically — never whether the
    student said so. The choice buttons carry the chosen tint and nothing
    else, and they are not `.ks3-option`s, so the reveal may disable them
    without failing R3's runtime assertion.
    """
    cases = a.get("cases") or []
    labels = a.get("choice_labels") or []
    openers = a.get("why_openers") or []
    if len(cases) < 2:
        raise ValueError(
            "settles-it %r declares %d case(s). The instrument is a "
            "discrimination exercise and one case cannot discriminate."
            % (act_id, len(cases)))
    if len(labels) != 2:
        raise ValueError(
            "settles-it %r needs exactly two choice_labels — the two things a "
            "fact can do. Got %r." % (act_id, labels))
    if len(openers) != 2:
        raise ValueError(
            "settles-it %r needs exactly two why_openers, the SETTLES and the "
            "SETTLES-NOTHING word, in that order. Got %r." % (act_id, openers))

    for k in cases:
        feats = k.get("features") or []
        if not feats:
            raise ValueError("settles-it %r case %r declares no features."
                             % (act_id, k.get("id")))
        for f in feats:
            if "settles" not in f:
                raise ValueError(
                    "settles-it %r case %r has a feature with no `settles` "
                    "verdict: %r. Every fact is either the one that decides it "
                    "or one that does not, and the whole exercise is telling "
                    "them apart." % (act_id, k.get("id"), f.get("text")))
            if not (f.get("why") or "").strip():
                raise ValueError(
                    "settles-it %r case %r feature %r has no `why`. The reveal "
                    "exists to say what settles each one."
                    % (act_id, k.get("id"), f.get("text")))
        if not sum(1 for f in feats if f.get("settles")):
            raise ValueError(
                "settles-it %r case %r has no discriminating feature at all — "
                "nothing settles it, so the case has no answer."
                % (act_id, k.get("id")))

    fmt = a.get("progress_format") or "{n} of {total} marked"
    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-case-tab" '
        'data-case="%s" aria-pressed="%s">%s</button>'
        % (e(k["id"]), "true" if i == 0 else "false",
           t(k.get("tab_label") or k.get("label", "")))
        for i, k in enumerate(cases))

    panels = []
    for i, k in enumerate(cases):
        feats = k.get("features") or []
        rows = []
        for f in feats:
            settles = bool(f.get("settles"))
            choices = "".join(
                '<button type="button" class="ks3-settle-choice" '
                'data-pick="%s" aria-pressed="false">%s</button>'
                % (pick, t(lab))
                for pick, lab in (("yes", labels[0]), ("no", labels[1])))
            rows.append(
                '<li class="ks3-feature" data-settles="%d">'
                '<p class="ks3-feature-text">%s</p>'
                '<div class="ks3-feature-choices">%s</div>'
                '<p class="ks3-feature-why" hidden data-reveal>'
                '<strong class="ks3-why-word">%s</strong> %s</p></li>'
                % (1 if settles else 0, rich(f.get("text", "")), choices,
                   t(openers[0] if settles else openers[1]), rich(f["why"])))

        panels.append(
            '<div class="ks3-case-panel" data-case="%s"%s>'
            '<div class="ks3-case-head">'
            '<p class="ks3-case-label">%s</p>'
            '<p class="ks3-case-desc">%s</p></div>'
            '<ul class="ks3-features" role="list">%s</ul>'
            '<div class="ks3-settle-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-settle-reveal" '
            'data-settle-reveal disabled>%s</button>'
            '<span class="ks3-settle-progress" data-settle-progress '
            'data-total="%d" data-format="%s" data-opened="%s">%s</span></div>'
            '<div class="ks3-case-verdict" hidden data-case-verdict>'
            '<p class="ks3-case-verdict-label">%s</p>'
            '<p class="ks3-case-answer">%s</p>'
            '<p class="ks3-case-why">%s</p></div></div>'
            % (e(k["id"]), "" if i == 0 else " hidden",
               t(k.get("label", "")), rich(k.get("description", "")),
               "".join(rows),
               t(a.get("reveal_label") or "Show what settles it"),
               len(feats), e(fmt), e(a.get("progress_opened") or "Opened"),
               t(fmt.replace("{n}", "0").replace("{total}", str(len(feats)))),
               t(k.get("verdict_label", "")), rich(k.get("answer", "")),
               rich(k.get("why", ""))))

    return ('<div class="ks3-case-tabs" role="list">%s</div>%s%s'
            % (tabs, "".join(panels), _self_check(a, act_id)))


# ── registrations ────────────────────────────────────────────────────────
KIND_SHELL = {
    'test-board': ("ks3-board",
                      ' data-instrument data-board data-stage-done="0"'),
    'sort-rows': ("ks3-sort",
                      ' data-instrument data-sort data-stage-done="0"'),
    'critique-steps': ("ks3-critique",
                       ' data-instrument data-critique data-stage-done="0"'),
    'fifa-construct': ("ks3-construct-block",
                       ' data-instrument data-construct data-stage-done="0"'),
    'cell-bench': ("ks3-cellbench-block",
                      ' data-instrument data-cellbench data-stage-done="0"'),
    'sort-pairs': ("ks3-pairs", ' data-instrument data-pairs data-stage-done="0"'),
    'fit-parts': ("ks3-fit-block",
                      ' data-instrument data-fitblock data-stage-done="0"'),
    'zoom-ladder': ("ks3-zoom-block",
                      ' data-instrument data-zoomblock data-stage-done="0"'),
    'sort-task': ("ks3-hard", ' data-instrument data-hard data-stage-done="0"'),
    'removal-cases': ("ks3-removal-block",
                      ' data-instrument data-removal data-stage-done="0"'),
    'system-bench': ("ks3-bench-block",
                      ' data-instrument data-benchblock data-stage-done="0"'),
    'sabotage': ("ks3-sab-block",
                      ' data-instrument data-sabotage data-stage-done="0"'),
    'settles-it': ("ks3-settles",
                      ' data-instrument data-settles data-stage-done="0"'),
}

KIND_FN = {
    'test-board': r_test_board,
    'sort-rows': r_sort_rows,
    'settles-it': r_settles_it,
    'critique-steps': r_critique_steps,
    'fifa-construct': r_fifa_construct,
    'cell-bench': r_cell_bench,
    'sort-pairs': r_sort_pairs,
    'fit-parts': r_fit_parts,
    'zoom-ladder': r_zoom_ladder,
    'sort-task': r_sort_task,
    'removal-cases': r_removal_cases,
    'system-bench': r_system_bench,
    'sabotage': r_sabotage,
}



# ══ lean wave · B1's drawn figures ═══════════════════════════════════════
#
# Seven plates for the lean B1 pages, appended below the retired instruments
# and registered in ART at the foot of this file. Every plate is 340 units
# wide and stacks its parts one under another, so each label reads at full
# size on a phone.
#
# Paint: outlines, text and neutral grounds are --ks3-* tokens. Organelles
# carry a FIXED fill (nucleus purple, chloroplast green, mitochondrion orange,
# red blood cell red), always outlined in --ks3-ink, so a part looks the same
# in the light and dark themes. Labels sit beside their part with a ruled
# leader line and no arrowhead, the way a biological drawing is labelled.
#
#   "b1-light-microscope"   data {"labels": [{"part", "text"}], "light_path": bool}
#       part ∈ eyepiece | objectives | stage | clips | coarse | fine | diaphragm | lamp
#   "b1-biological-drawing" data {"cells": int, "specimen": str,
#                                 "good": {"labels": [str ×3], "magnification": str},
#                                 "poor": {"faults": [str]}}
#   "b1-cell-pair"          data {"cells": [{"kind": "animal"|"plant", "label", "parts": [str]}],
#                                 "highlight_extras": [str]}
#   "b1-specialised-cells"  data {"cells": [{"kind": "red"|"sperm"|"nerve"|"root", "label",
#                                  "marks": [str]}], "to_scale": false}
#   "b1-diffusion"          data {"particle", "left": {"label", "tag", "count"},
#                                 "right": {...}, "arrows": int, "barrier": str}
#   "b1-levels"             data {"levels": [{"level", "example"} ×5]}
#   "b1-unicellular"        data {"organisms": [{"kind": "amoeba"|"paramecium"|"euglena",
#                                  "label", "parts": [str]}], "to_scale": false}

import math as _b1x_math
from ks3_art.kit import (
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_CARD,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_FAINT,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _circle,
    _ellipse,
    _label,
    _line,
    _n,
    _path,
    _rect,
    _svg_open,
)

_B1X_W = 340
_B1X_BLUE = "var(--ks3-blue)"
_B1X_BLUE_TINT = "var(--ks3-blue-tint)"
_B1X_OK = "var(--ks3-ok)"
# fixed fills, each always outlined in ink
_B1X_NUC = "#7C6AA6"      # nucleus (the old canvas drawings' purple)
_B1X_CHL = "#3E9B4F"      # chloroplast
_B1X_MITO = "#E39B4E"     # mitochondrion
_B1X_RED = "#C2372B"      # red blood cell
_B1X_RED_PALE = "#E58C80"  # its thin middle
_B1X_MUSCLE = "#D9796E"   # muscle cell
_B1X_LAMP = "#F2D23C"     # lamp
_B1X_O = "#D8412F"        # oxygen atom (as C2's particle boxes)
_B1X_EYE = "#D8412F"      # Euglena's eyespot
_B1X_LEAD = dict(stroke=_SVG_INK_MUTED, w=1.5)


def _b1x_need(fig, key):
    v = (fig.get("data") or {}).get(key)
    if not v:
        raise ValueError("figure %r: %s needs data.%s" % (fig.get("id"), fig.get("art"), key))
    return v


def _b1x_open(fig, h, body):
    return (_svg_open(fig, _B1X_W, int(_b1x_math.ceil(h)))
            + '<g stroke-linecap="round" stroke-linejoin="round">' + "".join(body) + "</g></svg>")


def _b1x_text(x, y, s, anchor="start", size=14, weight="600", fill=_SVG_INK, gap=17, **data):
    """A label; a "\\n" in it stacks a second line `gap` below the first."""
    return "".join(_label(x, y + i * gap, line, size=size, weight=weight, fill=fill, anchor=anchor, **data)
                   for i, line in enumerate(str(s).split("\n")))


def _b1x_lead(x1, y1, x2, y2, key):
    return _line(x1, y1, x2, y2, data_part="leader", data_key=key, **_B1X_LEAD)


def _b1x_tw(s, size=14, weight="600"):
    """A generous estimate of a label's drawn width, for pills and clearance."""
    k = 0.55 if weight in ("700", "800") else 0.52
    return max(len(line) for line in str(s).split("\n")) * size * k


def _b1x_smooth(pts):
    """A closed Catmull-Rom curve through `pts`, as cubic Béziers."""
    n = len(pts)
    d = "M %s,%s" % (_n(pts[0][0]), _n(pts[0][1]))
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        d += " C %s,%s %s,%s %s,%s" % (_n(c1[0]), _n(c1[1]), _n(c2[0]), _n(c2[1]), _n(p2[0]), _n(p2[1]))
    return d + " Z"


def _b1x_polyd(pts):
    return "M " + " L ".join("%s,%s" % (_n(x), _n(y)) for x, y in pts)


def _b1x_rot(svg, ang, cx, cy):
    return '<g transform="rotate(%s %s %s)">%s</g>' % (_n(ang), _n(cx), _n(cy), svg)


def _b1x_nucleus(cx, cy, rx, ry=None, **data):
    return _ellipse(cx, cy, rx, ry or rx, fill=_B1X_NUC, stroke=_SVG_INK, w=2, data_part="nucleus", **data)


def _b1x_mito(cx, cy, ang=0, s=1.0):
    rx, ry = 10 * s, 5 * s
    z = _b1x_polyd([(cx - 6 * s, cy), (cx - 3.5 * s, cy - 2.5 * s), (cx - 1 * s, cy + 2.5 * s),
                    (cx + 1.5 * s, cy - 2.5 * s), (cx + 4 * s, cy + 2.5 * s), (cx + 6 * s, cy)])
    return _b1x_rot(_ellipse(cx, cy, rx, ry, fill=_B1X_MITO, stroke=_SVG_INK, w=1.5, data_part="mitochondrion")
                    + _path(z, stroke="#5A3410", w=1), ang, cx, cy)


def _b1x_chloro(cx, cy, ang=0, rx=8, ry=4.5):
    return _b1x_rot(_ellipse(cx, cy, rx, ry, fill=_B1X_CHL, stroke=_SVG_INK, w=1.5, data_part="chloroplast"),
                    ang, cx, cy)


def _b1x_arrow(x1, y1, x2, y2, stroke=_SVG_INK, w=2.5, head=9, **data):
    from ks3_art.b4 import _b4_arrow
    return _b4_arrow(x1, y1, x2, y2, stroke=stroke, w=w, head=head, **data)


def _b1x_tick(x, y, s=1.0):
    return _path("M %s,%s L %s,%s L %s,%s" % (_n(x), _n(y + 7 * s), _n(x + 6 * s), _n(y + 13 * s),
                                              _n(x + 17 * s), _n(y)),
                 stroke=_B1X_OK, w=3.5, data_part="tick")


def _b1x_cross(x, y, s=1.0):
    return (_line(x, y, x + 13 * s, y + 13 * s, stroke=_SVG_ACCENT_TEXT, w=3.5, data_part="cross")
            + _line(x + 13 * s, y, x, y + 13 * s, stroke=_SVG_ACCENT_TEXT, w=3.5, data_part="cross"))


def _b1x_divider(y):
    return _line(8, y, _B1X_W - 8, y, stroke=_SVG_RULE, w=1.5, data_part="divider")


def _b1x_heading(y, s, key):
    return _label(8, y, s, size=15, weight="700", anchor="start", data_part="heading", data_key=key)


# ── b1-light-microscope ─────────────────────────────────────────────────
# A straight-tube school microscope from the side: the arm at the back (left),
# the tube, turret and stage in front of it, the lamp in the base under the
# hole in the stage. The light path, when drawn, runs up the tube's axis.
_B1X_SCOPE_TARGETS = {
    # part: (label x, label baseline y, anchor, leader from, leader to)
    "eyepiece":   (196, 31, "start", (192, 26), (174, 26)),
    "objectives": (236, 174, "start", (232, 169), (182, 174)),
    "clips":      (236, 215, "start", (232, 210), (209, 207)),
    "stage":      (236, 241, "start", (232, 236), (221, 225)),
    "diaphragm":  (236, 266, "start", (232, 261), (181, 239)),
    "lamp":       (236, 305, "start", (232, 300), (170, 300)),
    "coarse":     (62, 254, "end", (65, 258), (77, 258)),
    "fine":       (62, 294, "end", (65, 298), (85, 298)),
}
_B1X_SCOPE_SPLIT = {"Objective lenses": "Objective\nlenses", "Coarse focus": "Coarse\nfocus",
                    "Fine focus": "Fine\nfocus"}


def _b1x_light_microscope(fig):
    data = fig.get("data") or {}
    labels = _b1x_need(fig, "labels")
    o = []
    X = 160
    # base and arm (behind everything)
    o.append(_rect(70, 330, 180, 26, rx=6, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="base"))
    o.append(_path("M 82,330 L 82,140 Q 82,84 132,84 L 142,84 L 142,118 L 132,118 Q 108,118 108,150 L 108,330 Z",
                   fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="arm"))
    # lamp in the base, under the hole
    o.append(_rect(146, 304, 28, 26, rx=3, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="lamp-housing"))
    o.append(_circle(X, 298, 9, fill=_B1X_LAMP, stroke=_SVG_INK, w=1.5, data_part="lamp"))
    # diaphragm under the stage, hung from it
    o.append(_line(146, 224, 146, 234, stroke=_SVG_INK, w=2))
    o.append(_line(174, 224, 174, 234, stroke=_SVG_INK, w=2))
    o.append(_rect(139, 234, 42, 7, rx=3, fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="diaphragm"))
    # the stage, in two pieces either side of its hole
    o.append(_rect(108, 214, 44, 10, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="stage"))
    o.append(_rect(168, 214, 54, 10, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="stage"))
    # the slide over the hole, held by two clips
    o.append(_rect(126, 210, 68, 4, fill=_B1X_BLUE_TINT, stroke=_SVG_INK, w=1.5, data_part="slide"))
    for x0, x1, post in ((111, 134, 111), (186, 209, 205)):
        o.append(_rect(post, 205, 4, 9, fill=_SVG_INK, data_part="clip-post"))
        o.append(_rect(x0, 204, x1 - x0, 4, rx=2, fill=_SVG_INK_BODY, stroke=_SVG_INK, w=1, data_part="clip"))
    # tube, turret and three objectives of different lengths
    o.append(_rect(142, 58, 36, 90, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="tube"))
    o.append(_path("M 132,148 L 188,148 L 184,164 L 136,164 Z", fill=_SVG_BAND, stroke=_SVG_INK, w=2,
                   data_part="turret"))
    for x0, x1, y1, power in ((139, 149, 178, "low"), (154, 166, 200, "high"), (171, 181, 189, "medium")):
        o.append(_rect(x0, 164, x1 - x0, y1 - 164, rx=2, fill=_SVG_CARD, stroke=_SVG_INK, w=2,
                       data_part="objective", data_key=power))
        o.append(_line(x0 + 2, y1, x1 - 2, y1, stroke=_B1X_BLUE, w=2.5))
    # eyepiece on top, its lens at the top
    o.append(_rect(147, 27, 26, 31, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="eyepiece"))
    o.append(_ellipse(X, 27, 13, 4, fill=_B1X_BLUE_TINT, stroke=_SVG_INK, w=1.5, data_part="eyepiece-lens"))
    # focus knobs on the arm: coarse large, fine small
    o.append(_circle(95, 258, 17, fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="knob", data_key="coarse"))
    o.append(_circle(95, 258, 5, fill=_SVG_INK_FAINT, stroke=_SVG_INK, w=1.5))
    o.append(_circle(95, 298, 9, fill=_SVG_CARD, stroke=_SVG_INK, w=2, data_part="knob", data_key="fine"))
    o.append(_circle(95, 298, 3, fill=_SVG_INK_FAINT))
    if data.get("light_path"):
        o.append(_line(X, 288, X, 17, stroke=_SVG_ACCENT_TEXT, w=2, dash="5 4", data_part="light-path"))
        o.append(_path("M %s,6 L %s,17 L %s,17 Z" % (X, X - 6, X + 6), fill=_SVG_ACCENT_TEXT,
                       data_part="light-path"))
    for lab in labels:
        part, text = lab["part"], lab["text"]
        if part not in _B1X_SCOPE_TARGETS:
            raise ValueError("figure %r: no microscope part %r" % (fig.get("id"), part))
        lx, ly, anchor, a, b = _B1X_SCOPE_TARGETS[part]
        o.append(_b1x_lead(a[0], a[1], b[0], b[1], part))
        o.append(_b1x_text(lx, ly, _B1X_SCOPE_SPLIT.get(text, text), anchor=anchor,
                           data_part="label", data_key=part))
    return _b1x_open(fig, 362, o)


# ── b1-biological-drawing ───────────────────────────────────────────────
# The same onion cells twice: a good drawing (thin single lines, no shading,
# a title, ruled labels, the magnification) over a poor one (sketchy doubled
# lines, shading, colouring, nothing written on it).
def _b1x_onion_cells(ox, oy, n, w=166, h=36):
    """[(x, y, w, h, nucleus cx, nucleus cy)] for n long cells stacked like bricks."""
    cells = []
    for i in range(n):
        shift = 18 if i % 2 else 0
        x = ox + shift
        cells.append((x, oy + i * h, w, h, x + (40 if i % 2 else w - 44), oy + i * h + h / 2))
    return cells


def _b1x_biological_drawing(fig):
    data = fig.get("data") or {}
    n = int(data.get("cells") or 3)
    good = data.get("good") or {}
    poor = data.get("poor") or {}
    labs = good.get("labels") or []
    if len(labs) != 3:
        raise ValueError("figure %r: b1-biological-drawing needs three good.labels" % fig.get("id"))
    faults = set(poor.get("faults") or [])
    title = {"onion": "Onion cells"}.get(data.get("specimen"), str(data.get("specimen") or "Cells").capitalize())
    pencil = _SVG_INK_BODY
    o = []
    # ── the good drawing ──
    o.append(_b1x_tick(10, 6))
    o.append(_label(36, 19, "Good drawing", size=15, weight="700", anchor="start", data_part="heading",
                    data_key="good"))
    o.append(_label(102, 50, title, size=14, weight="600", anchor="middle", fill=pencil,
                    data_part="drawing-title"))
    cells = _b1x_onion_cells(12, 62, n)
    for (x, y, w, h, nx, ny) in cells:
        o.append(_rect(x, y, w, h, fill="none", stroke=pencil, w=1.5, data_part="cell-wall"))
        o.append(_ellipse(nx, ny, 9, 6, fill="none", stroke=pencil, w=1.5, data_part="nucleus"))
    # ruled labels: wall (top cell's right end), nucleus (middle cell), cytoplasm (bottom cell)
    x0, y0, w0, h0 = cells[0][:4]
    xm, ym, wm, hm, nxm, nym = cells[min(1, n - 1)]
    xb, yb, wb, hb, nxb, nyb = cells[-1]
    targets = [(x0 + w0, y0 + 12), (nxm + 9, nym), (xb + wb - 20, yb + hb / 2 + 6)]
    lys = [y0 + 12, nym, yb + hb / 2 + 6]
    for text, (tx, ty), ly in zip(labs, targets, lys):
        o.append(_line(222, ly, tx, ty, stroke=pencil, w=1.2, data_part="leader", data_key=text))
        o.append(_label(228, ly + 5, text, size=14, weight="600", anchor="start", fill=pencil,
                        data_part="label", data_key=text))
    mag = good.get("magnification")
    bottom = yb + hb
    if mag:
        o.append(_label(102, bottom + 24, "Magnification %s" % mag, size=14, weight="600", anchor="middle",
                        fill=pencil, data_part="magnification"))
        bottom += 24
    y = bottom + 18
    o.append(_b1x_divider(y))
    # ── the poor drawing ──
    y += 14
    o.append(_b1x_cross(12, y + 1))
    o.append(_label(36, y + 13, "Poor drawing", size=15, weight="700", anchor="start", data_part="heading",
                    data_key="poor"))
    top = y + 30
    cells = _b1x_onion_cells(12, top, n)
    if "colouring" in faults:
        for (x, yy, w, h, nx, ny) in cells:
            o.append(_rect(x + 1, yy + 1, w - 2, h - 2, fill="#8C857D", opacity="0.4", data_part="colouring"))
    if "shading" in faults:
        clip = "%s-shade" % fig["id"]
        rects = "".join(_rect(x, yy, w, h) for (x, yy, w, h, nx, ny) in cells)
        o.append('<defs><clipPath id="%s">%s</clipPath></defs>' % (clip, rects))
        hatch = []
        for k in range(-10, 30):
            hx = 12 + k * 9
            hatch.append(_line(hx, top + n * 36, hx + n * 36, top, stroke=_SVG_INK, w=1, opacity="0.45"))
        o.append('<g clip-path="url(#%s)" data-part="shading">%s</g>' % (clip, "".join(hatch)))
    for ci, (x, yy, w, h, nx, ny) in enumerate(cells):
        sketch = "sketchy lines" in faults
        passes = ((0, 0), (1.6, -1.4), (-1.2, 1.8)) if sketch else ((0, 0),)
        for pi, (dx, dy) in enumerate(passes):
            j = (ci * 3 + pi) % 4 - 1.5
            pts = [(x + dx - 2, yy + dy + j), (x + w * .5, yy + dy - j * .6), (x + w + dx + 3, yy + dy + .8 * j),
                   (x + w + dx - j * .5, yy + h + dy), (x + w * .45, yy + h + dy + j * .7),
                   (x + dx + 1.5, yy + h + dy - j * .4), (x + dx - 2, yy + dy + j)]
            o.append(_path(_b1x_polyd(pts), stroke=_SVG_INK, w=1.6, data_part="sketch-line"))
        o.append(_ellipse(nx, ny, 9, 6, fill="#4A443F", stroke=_SVG_INK, w=1.5, data_part="nucleus"))
        if sketch:
            o.append(_ellipse(nx + 1.5, ny - 1, 10, 6.5, fill="none", stroke=_SVG_INK, w=1.2))
    H = top + n * 36 + 20
    return _b1x_open(fig, H, o)


# ── b1-cell-pair ────────────────────────────────────────────────────────
# Animal cell over plant cell. Every part the animal cell has, the plant cell
# has too; the plant's extras are named on a tinted pill and keyed underneath.
_B1X_PART_NAMES = {"cell membrane": "Cell membrane", "cytoplasm": "Cytoplasm", "nucleus": "Nucleus",
                   "mitochondria": "Mitochondria", "cell wall": "Cell wall", "vacuole": "Large vacuole",
                   "chloroplasts": "Chloroplasts"}


def _b1x_extra_label(x, y, text, key):
    w = _b1x_tw(text, 14, "700")
    return (_rect(x - 5, y - 15, w + 10, 21, rx=10, fill=_SVG_ACCENT_TINT, stroke=_SVG_ACCENT_TEXT, w=1.5,
                  data_part="extra-pill", data_key=key)
            + _label(x, y, text, size=14, weight="700", anchor="start", fill=_SVG_ACCENT_TEXT,
                     data_part="label", data_key=key, data_extra="1"))


def _b1x_part_label(x, y, key, extras):
    name = _B1X_PART_NAMES.get(key, key[:1].upper() + key[1:])
    if key in extras:
        return _b1x_extra_label(x, y, name, key)
    return _label(x, y, name, size=14, weight="600", anchor="start", data_part="label", data_key=key)


def _b1x_animal_cell(oy, parts, extras):
    o = []
    cx, cy = 100, oy + 82
    rs = (70, 64, 60, 66, 72, 66, 58, 62, 68, 64)
    pts = []
    for i, r in enumerate(rs):
        a = 2 * _b1x_math.pi * i / len(rs)
        pts.append((cx + r * 1.12 * _b1x_math.cos(a), cy + r * 0.86 * _b1x_math.sin(a)))
    o.append(_path(_b1x_smooth(pts), fill=_SVG_BAND, stroke=_SVG_INK, w=2.5, data_part="cell-membrane"))
    o.append(_b1x_nucleus(cx - 8, cy + 2, 20))
    for mx, my, ang in ((cx + 38, cy - 26, 20), (cx - 50, cy + 28, -30), (cx + 22, cy + 34, 10),
                        (cx - 44, cy - 28, 35)):
        o.append(_b1x_mito(mx, my, ang))
    # targets on the right half, top to bottom
    tgt = {"cell membrane": (cx + 58, cy - 32), "mitochondria": (cx + 47, cy - 22),
           "nucleus": (cx + 12, cy + 2), "cytoplasm": (cx + 52, cy + 22)}
    ys = {"cell membrane": cy - 50, "mitochondria": cy - 20, "nucleus": cy + 10, "cytoplasm": cy + 40}
    for key in parts:
        if key not in tgt:
            raise ValueError("b1-cell-pair: no animal-cell part %r" % key)
        tx, ty = tgt[key]
        o.append(_b1x_lead(206, ys[key] - 5, tx, ty, key))
        o.append(_b1x_part_label(212, ys[key], key, ()))
    return o, oy + 146


def _b1x_plant_cell(oy, parts, extras):
    o = []
    L, T, R, B = 14, oy + 6, 194, oy + 176
    o.append(_rect(L, T, R - L, B - T, rx=4, fill=_SVG_RULE_STRONG, stroke=_SVG_INK, w=2.5, data_part="cell-wall"))
    o.append(_rect(L + 8, T + 8, R - L - 16, B - T - 16, rx=2, fill=_SVG_CARD, stroke=_SVG_INK, w=1))
    o.append(_rect(L + 11, T + 11, R - L - 22, B - T - 22, rx=2, fill=_SVG_BAND, stroke=_SVG_INK, w=1.5,
                   data_part="cell-membrane"))
    vx0, vy0, vx1, vy1 = L + 30, T + 30, R - 46, B - 30
    o.append(_rect(vx0, vy0, vx1 - vx0, vy1 - vy0, rx=18, fill=_B1X_BLUE_TINT, stroke=_SVG_INK, w=1.5,
                   data_part="vacuole"))
    nx, ny = R - 27, T + 72
    o.append(_b1x_nucleus(nx, ny, 12))
    chl = [(L + 28, T + 20, 0), (L + 62, T + 20, 0), (L + 98, T + 20, 0), (L + 134, T + 20, 0),
           (R - 26, T + 25, 30),
           (L + 20, T + 58, 90), (L + 20, T + 98, 90), (L + 20, T + 138, 90),
           (L + 46, B - 20, 0), (L + 82, B - 20, 0), (L + 118, B - 20, 0)]
    for x, y, a in chl:
        o.append(_b1x_chloro(x, y, a))
    o.append(_b1x_mito(R - 24, T + 112, 80, s=.85))
    o.append(_b1x_mito(L + 20, T + 118, 90, s=.85))
    tgt = {"cell wall": (R - 3, T + 6), "chloroplasts": (R - 20, T + 28), "cell membrane": (R - 11, T + 50),
           "nucleus": (nx + 11, ny + 4), "vacuole": (vx1 - 2, T + 98), "mitochondria": (R - 18, T + 116),
           "cytoplasm": (R - 26, B - 32)}
    ys = {"cell wall": T + 6, "chloroplasts": T + 30, "cell membrane": T + 54, "nucleus": T + 78,
          "vacuole": T + 102, "mitochondria": T + 126, "cytoplasm": T + 150}
    for key in parts:
        if key not in tgt:
            raise ValueError("b1-cell-pair: no plant-cell part %r" % key)
        tx, ty = tgt[key]
        o.append(_b1x_lead(206, ys[key] - 5, tx, ty, key))
        o.append(_b1x_part_label(212, ys[key], key, extras))
    return o, B


def _b1x_cell_pair(fig):
    data = fig.get("data") or {}
    cells = _b1x_need(fig, "cells")
    extras = set(data.get("highlight_extras") or [])
    o = []
    y = 4
    for i, c in enumerate(cells):
        if i:
            o.append(_b1x_divider(y + 10))
            y += 24
        o.append(_b1x_heading(y + 16, c["label"], c["kind"]))
        y += 26
        fn = {"animal": _b1x_animal_cell, "plant": _b1x_plant_cell}.get(c["kind"])
        if not fn:
            raise ValueError("figure %r: no cell kind %r" % (fig.get("id"), c["kind"]))
        part, y = fn(y, c.get("parts") or [], extras)
        o.extend(part)
    if extras:
        y += 22
        o.append(_rect(14, y - 8, 30, 16, rx=8, fill=_SVG_ACCENT_TINT, stroke=_SVG_ACCENT_TEXT, w=1.5,
                       data_part="key-pill"))
        o.append(_label(52, y + 5, "Only in plant cells", size=14, weight="600", anchor="start",
                        data_part="key"))
        y += 12
    return _b1x_open(fig, y + 8, o)


# ── b1-specialised-cells ────────────────────────────────────────────────
# Four rows, one cell each, not to scale. Each row: the cell's name, the
# drawing, and its marks on short ruled lines.
def _b1x_spec_red(oy, marks):
    o = []
    fx, sx, cy = 70, 222, oy + 70
    o.append(_label(fx, oy + 30, "From above", size=14, weight="500", fill=_SVG_INK_MUTED, data_part="view"))
    o.append(_label(sx, oy + 30, "From the side", size=14, weight="500", fill=_SVG_INK_MUTED, data_part="view"))
    o.append(_circle(fx, cy, 30, fill=_B1X_RED, stroke=_SVG_INK, w=2, data_part="red-cell-face"))
    o.append(_circle(fx, cy, 13, fill=_B1X_RED_PALE, data_part="thin-middle"))
    # biconcave disc seen edge-on: thick rim, thin middle
    d = ("M %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s Z"
         % tuple(_n(v) for v in (sx - 44, cy,
                                 sx - 40, cy - 16, sx - 22, cy - 16, sx, cy - 6,
                                 sx + 22, cy - 16, sx + 40, cy - 16, sx + 44, cy,
                                 sx + 40, cy + 16, sx + 22, cy + 16, sx, cy + 6,
                                 sx - 22, cy + 16, sx - 40, cy + 16, sx - 44, cy)))
    o.append(_path(d, fill=_B1X_RED, stroke=_SVG_INK, w=2, data_part="red-cell-side"))
    pos = [(fx, cy, fx, cy + 50, "middle"), (sx, cy + 7, sx, cy + 50, "middle")]
    for m, (tx, ty, lx, ly, anc) in zip(marks, pos):
        o.append(_b1x_lead(tx, ty, lx, ly - 15, m))
        o.append(_b1x_text(lx, ly, m, anchor=anc, data_part="mark", data_key=m))
    return o, cy + 56


def _b1x_spec_sperm(oy, marks):
    o = []
    cy = oy + 64
    hx = 46
    tail = []
    for i in range(0, 61):
        t = i / 60.0
        x = 104 + t * 222
        tail.append((x, cy + 11 * (1 - .55 * t) * _b1x_math.sin(t * 2 * _b1x_math.pi * 2.2)))
    o.append(_path(_b1x_polyd(tail), stroke=_SVG_INK, w=3, data_part="tail"))
    o.append(_rect(66, cy - 8, 40, 16, rx=7, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="midpiece"))
    for mx in (74, 86, 98):
        o.append(_ellipse(mx, cy, 5, 4, fill=_B1X_MITO, stroke=_SVG_INK, w=1.2, data_part="mitochondrion"))
    o.append(_ellipse(hx, cy, 24, 17, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="head"))
    o.append(_b1x_nucleus(hx + 2, cy, 15, 11))
    labs = {"Head with genetic material": ((hx, cy - 17), (hx, oy + 34), (10, oy + 30), "start", "above"),
            "Mitochondria": ((86, cy + 8), (86, cy + 30), (86, cy + 45), "middle", "below"),
            "Tail": ((236, cy + 9), (236, cy + 30), (236, cy + 45), "middle", "below")}
    for m in marks:
        if m not in labs:
            raise ValueError("b1-specialised-cells: no sperm mark %r" % m)
        a, b, (lx, ly), anc, _side = labs[m]
        o.append(_b1x_lead(a[0], a[1], b[0], b[1], m))
        o.append(_b1x_text(lx, ly, m, anchor=anc, data_part="mark", data_key=m))
    return o, cy + 50


def _b1x_spec_nerve(oy, marks):
    o = []
    cy = oy + 70
    bx = 58
    # dendrites from the cell body
    for ang, ln in ((195, 20), (150, 20), (240, 18), (115, 18), (285, 14)):
        a = _b1x_math.radians(ang)
        x1, y1 = bx + 20 * _b1x_math.cos(a), cy + 20 * _b1x_math.sin(a)
        x2, y2 = bx + (20 + ln) * _b1x_math.cos(a), cy + (20 + ln) * _b1x_math.sin(a)
        o.append(_line(x1, y1, x2, y2, stroke=_SVG_INK, w=2.5))
        for da in (-28, 28):
            b = _b1x_math.radians(ang + da)
            o.append(_line(x2, y2, x2 + 9 * _b1x_math.cos(b), y2 + 9 * _b1x_math.sin(b), stroke=_SVG_INK, w=2))
    # the long fibre
    o.append(_line(bx + 18, cy, 270, cy, stroke=_SVG_INK, w=8, data_part="fibre"))
    o.append(_line(bx + 18, cy, 270, cy, stroke=_SVG_BAND, w=4))
    # branched ends
    ends = []
    for dy in (-22, -8, 8, 22):
        ex, ey = 312, cy + dy
        ends.append(_path("M 270,%s Q 290,%s %s,%s" % (_n(cy), _n(cy + dy * .4), _n(ex), _n(ey)),
                          stroke=_SVG_INK, w=2.5))
        ends.append(_circle(ex + 3, ey, 4, fill=_SVG_BAND, stroke=_SVG_INK, w=2))
    o.extend(ends)
    pts = []
    for i, r in enumerate((22, 19, 23, 20, 22, 18, 21, 20)):
        a = 2 * _b1x_math.pi * i / 8
        pts.append((bx + r * _b1x_math.cos(a), cy + r * _b1x_math.sin(a)))
    o.append(_path(_b1x_smooth(pts), fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="cell-body"))
    o.append(_b1x_nucleus(bx, cy, 8))
    labs = {"Long fibre": ((170, cy - 4), (170, cy - 26), (170, cy - 31), "middle"),
            "Branched ends": ((300, cy + 22), (300, cy + 36), (330, cy + 51), "end")}
    for m in marks:
        if m not in labs:
            raise ValueError("b1-specialised-cells: no nerve mark %r" % m)
        a, b, (lx, ly), anc = labs[m]
        o.append(_b1x_lead(a[0], a[1], b[0], b[1], m))
        o.append(_b1x_text(lx, ly, m, anchor=anc, data_part="mark", data_key=m))
    return o, cy + 56


def _b1x_spec_root(oy, marks):
    o = []
    hy = oy + 70
    L, T, R, B = 12, oy + 30, 110, oy + 112
    # soil particles around the hair
    for x, y, r in ((150, hy - 24, 13), (192, hy + 22, 12), (232, hy - 22, 14), (276, hy + 21, 12),
                    (312, hy - 23, 11), (166, hy + 36, 9), (256, hy + 42, 10), (300, hy + 46, 9),
                    (206, hy - 40, 9), (322, hy + 38, 7)):
        o.append(_circle(x, y, r, fill="#A9845A", stroke=_SVG_INK, w=1.5, data_part="soil"))

    def outline(i, hw):
        """The cell and its hair as one outline, `i` units inside the outer edge."""
        return ("M %s,%s L %s,%s L %s,%s L %s,%s Q %s,%s %s,%s L %s,%s L %s,%s L %s,%s Z"
                % tuple(_n(v) for v in (L + i, T + i, R - i, T + i, R - i, hy - hw, 318 - i, hy - hw,
                                        327 - i, hy, 318 - i, hy + hw, R - i, hy + hw, R - i, B - i,
                                        L + i, B - i)))
    # cell wall outside, cell membrane just inside it
    o.append(_path(outline(0, 8), fill=_SVG_RULE_STRONG, stroke=_SVG_INK, w=2.5, data_part="cell-wall"))
    o.append(_path(outline(4, 4), fill=_SVG_BAND, stroke=_SVG_INK, w=1.5, data_part="cell-membrane"))
    o.append(_rect(L + 16, T + 16, 52, B - T - 40, rx=10, fill=_B1X_BLUE_TINT, stroke=_SVG_INK, w=1.5,
                   data_part="vacuole"))
    o.append(_b1x_nucleus(R - 17, hy - 22, 8))
    for x, y, a in ((R - 17, B - 22, 30), (L + 10, T + 46, 90)):
        o.append(_b1x_mito(x, y, a, s=.8))
    labs = {"Long hair": ((282, hy - 8), (282, hy - 38), (266, hy - 46), "start"),
            # a fact about the whole cell, so a plain line under it rather than a leader to one spot
            "No chloroplasts": (None, None, (L, B + 22), "start")}
    for m in marks:
        if m not in labs:
            raise ValueError("b1-specialised-cells: no root-hair mark %r" % m)
        a, b, (lx, ly), anc = labs[m]
        if a:
            o.append(_b1x_lead(a[0], a[1], b[0], b[1], m))
        o.append(_b1x_text(lx, ly, m, anchor=anc, data_part="mark", data_key=m))
    return o, B + 28


def _b1x_specialised_cells(fig):
    cells = _b1x_need(fig, "cells")
    fns = {"red": _b1x_spec_red, "sperm": _b1x_spec_sperm, "nerve": _b1x_spec_nerve, "root": _b1x_spec_root}
    o = []
    y = 4
    for i, c in enumerate(cells):
        if c["kind"] not in fns:
            raise ValueError("figure %r: no cell kind %r" % (fig.get("id"), c["kind"]))
        if i:
            o.append(_b1x_divider(y + 8))
            y += 18
        o.append(_b1x_heading(y + 16, c["label"], c["kind"]))
        part, y = fns[c["kind"]](y + 8, c.get("marks") or [])
        o.extend(part)
    return _b1x_open(fig, y + 6, o)


# ── b1-diffusion ────────────────────────────────────────────────────────
# A membrane down the middle; oxygen molecules crowded on one side, few on
# the other; arrows across it from high to low.
_B1X_LEFT_SPOTS = ((30, 92), (78, 84), (122, 96), (40, 124), (100, 120), (24, 156), (70, 146),
                   (116, 146), (44, 186), (96, 180), (24, 214), (74, 212), (114, 198), (50, 236),
                   (106, 238), (130, 124))
_B1X_RIGHT_SPOTS = ((268, 108), (296, 186), (236, 232), (300, 236), (262, 150))


def _b1x_o2(cx, cy, ang=0):
    r = 6.5
    return _b1x_rot(_circle(cx - r, cy, r, fill=_B1X_O, stroke=_SVG_INK, w=1.5)
                    + _circle(cx + r, cy, r, fill=_B1X_O, stroke=_SVG_INK, w=1.5), ang, cx, cy)


def _b1x_diffusion(fig):
    data = fig.get("data") or {}
    left, right = data.get("left") or {}, data.get("right") or {}
    nl, nr = int(left.get("count") or 0), int(right.get("count") or 0)
    if nl > len(_B1X_LEFT_SPOTS) or nr > len(_B1X_RIGHT_SPOTS) or nl <= nr:
        raise ValueError("figure %r: b1-diffusion counts %r/%r" % (fig.get("id"), nl, nr))
    if data.get("direction", "left-to-right") != "left-to-right":
        raise ValueError("figure %r: b1-diffusion draws left-to-right only" % fig.get("id"))
    o = []
    M = 170
    o.append(_rect(8, 64, 324, 192, rx=10, fill=_SVG_INSET, stroke=_SVG_RULE, w=1.5, data_part="field"))
    o.append(_rect(M - 5, 64, 10, 192, fill=_SVG_BAND, data_part="membrane"))
    o.append(_line(M - 5, 64, M - 5, 256, stroke=_SVG_INK, w=2.5, data_part="membrane"))
    o.append(_line(M + 5, 64, M + 5, 256, stroke=_SVG_INK, w=2.5, data_part="membrane"))
    barrier = data.get("barrier")
    if barrier:
        o.append(_label(M, 18, barrier, size=14, weight="600", anchor="middle", data_part="barrier"))
        o.append(_b1x_lead(M, 24, M, 64, "barrier"))
    o.append(_label(87, 52, left.get("label", ""), size=14, weight="700", data_part="side", data_key="left"))
    o.append(_label(255, 52, right.get("label", ""), size=14, weight="700", data_part="side", data_key="right"))
    for i, (x, y) in enumerate(_B1X_LEFT_SPOTS[:nl]):
        o.append(_b1x_o2(x, y, (i * 37) % 180))
    for i, (x, y) in enumerate(_B1X_RIGHT_SPOTS[:nr]):
        o.append(_b1x_o2(x, y, (i * 53 + 20) % 180))
    n = int(data.get("arrows") or 3)
    for k in range(n):
        ay = 64 + 192 * (k + 1) / (n + 1)
        o.append(_b1x_arrow(146, ay, 216, ay, stroke=_SVG_INK, w=3, head=11, data_part="arrow"))
    o.append(_label(87, 282, left.get("tag", ""), size=14, weight="600", fill=_SVG_ACCENT_TEXT,
                    data_part="tag", data_key="left"))
    o.append(_label(255, 282, right.get("tag", ""), size=14, weight="600", fill=_SVG_ACCENT_TEXT,
                    data_part="tag", data_key="right"))
    if data.get("particle"):
        o.append(_b1x_o2(118, 308))
        o.append(_label(138, 313, "= one %s molecule" % data["particle"], size=14, weight="600",
                        anchor="start", fill=_SVG_INK_MUTED, data_part="key"))
    return _b1x_open(fig, 326, o)


# ── b1-levels ───────────────────────────────────────────────────────────
# Cell → tissue → organ → organ system → organism, top to bottom, each
# picture bigger than the last, joined by arrows pointing down.
def _b1x_muscle_cell(cx, cy, hw, hh):
    """One muscle cell: a long rounded cell, cross-striped, its nucleus in the middle."""
    out = [_rect(cx - hw, cy - hh, 2 * hw, 2 * hh, rx=hh, fill=_B1X_MUSCLE, stroke=_SVG_INK, w=1.8,
                 data_part="muscle-cell")]
    k = cx - hw + hh + 2
    while k < cx + hw - hh:
        if abs(k - cx) > hh * 1.2:
            out.append(_line(k, cy - hh + 2, k, cy + hh - 2, stroke="#8E3B32", w=1.2))
        k += 5
    out.append(_ellipse(cx, cy, hh * .9, hh * .55, fill=_B1X_NUC, stroke=_SVG_INK, w=1.2, data_part="nucleus"))
    return "".join(out)


def _b1x_heart(cx, cy, s):
    """A front-view heart, its top vessels cut short; (cx, cy) is its middle, s its scale (1 = 100 units)."""
    def P(x, y):
        return "%s,%s" % (_n(cx + (x - 50) * s), _n(cy + (y - 55) * s))
    body = ("M %s C %s %s %s C %s %s %s C %s %s %s C %s %s %s C %s %s %s Z"
            % (P(28, 32), P(8, 40), P(8, 66), P(32, 84), P(44, 94), P(56, 100), P(60, 98),
               P(80, 82), P(94, 58), P(84, 36), P(76, 24), P(62, 24), P(54, 32), P(46, 26), P(36, 26),
               P(28, 32)))
    ves = []
    for d in ("M %s Q %s %s" % (P(48, 30), P(48, 6), P(70, 8)),
              "M %s L %s" % (P(38, 30), P(30, 10)),
              "M %s L %s" % (P(66, 28), P(74, 18))):
        ves.append(_path(d, stroke=_SVG_INK, w=max(2, 11 * s)))
        ves.append(_path(d, stroke=_B1X_RED, w=max(1, 7 * s)))
    return ("".join(ves) + _path(body, fill=_B1X_RED, stroke=_SVG_INK, w=2, data_part="heart")
            + _path("M %s Q %s %s" % (P(56, 34), P(48, 62), P(58, 92)), stroke=_SVG_INK, w=1.5, opacity="0.6"))


def _b1x_level_pic(i, cx, cy):
    o = []
    if i == 0:
        o.append(_b1x_muscle_cell(cx, cy, 30, 8))
        return o, 20
    if i == 1:
        for r, dx in ((-1, 0), (0, 23), (1, 0)):
            for k in (-1, 0, 1):
                o.append(_b1x_muscle_cell(cx + k * 46 + dx - 12, cy + r * 14, 22, 7))
        return o, 44
    if i == 2:
        o.append(_b1x_heart(cx, cy, .62))
        return o, 66
    if i == 3:
        cy += 4
        # vessels leave the heart and branch out to the head, arms and legs
        segs = [((0, -14), (0, -30), 3.5), ((0, -30), (0, -46), 2.5), ((0, -30), (-24, -34), 2.5),
                ((-24, -34), (-38, -14), 2.5), ((0, -30), (24, -34), 2.5), ((24, -34), (38, -14), 2.5),
                ((0, 12), (0, 26), 3.5), ((0, 26), (-14, 50), 2.5), ((0, 26), (14, 50), 2.5)]
        ends = [((0, -46), -90), ((-38, -14), 115), ((38, -14), 65), ((-14, 50), 110), ((14, 50), 70)]
        for (x1, y1), (x2, y2), wd in segs:
            o.append(_line(cx + x1, cy + y1, cx + x2, cy + y2, stroke=_B1X_RED, w=wd, data_part="vessel"))
        for (x, y), ang in ends:
            for da in (-35, 0, 35):
                a = _b1x_math.radians(ang + da)
                o.append(_line(cx + x, cy + y, cx + x + 9 * _b1x_math.cos(a), cy + y + 9 * _b1x_math.sin(a),
                               stroke=_B1X_RED, w=1.6, data_part="vessel"))
        o.append(_b1x_heart(cx, cy, .36))
        return o, 120
    # organism: a person, arms down
    def limb(x1, y1, x2, y2, wd):
        return (_line(x1, y1, x2, y2, stroke=_SVG_INK, w=wd + 4)
                + _line(x1, y1, x2, y2, stroke=_SVG_BAND, w=wd))
    top = cy - 62
    o.append(limb(cx - 10, top + 76, cx - 14, top + 120, 12))
    o.append(limb(cx + 10, top + 76, cx + 14, top + 120, 12))
    o.append(limb(cx - 20, top + 32, cx - 32, top + 76, 9))
    o.append(limb(cx + 20, top + 32, cx + 32, top + 76, 9))
    o.append(_rect(cx - 22, top + 24, 44, 58, rx=14, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="body"))
    o.append(_circle(cx, top + 12, 13, fill=_SVG_BAND, stroke=_SVG_INK, w=2, data_part="head"))
    o.append(_b1x_heart(cx + 5, top + 44, .15))
    return o, 126


def _b1x_levels(fig):
    levels = _b1x_need(fig, "levels")
    if len(levels) != 5:
        raise ValueError("figure %r: b1-levels draws five levels" % fig.get("id"))
    o = []
    cx = 86
    y = 6
    for i, lv in enumerate(levels):
        _, h = _b1x_level_pic(i, cx, 0)
        cy = y + h / 2
        part, _ = _b1x_level_pic(i, cx, cy)
        o.append('<g data-part="level" data-key="%s">' % lv["level"].lower().replace(" ", "-"))
        o.extend(part)
        o.append("</g>")
        o.append(_label(184, cy - 2, lv["level"], size=16, weight="700", anchor="start",
                        data_part="level-name", data_key=lv["level"]))
        o.append(_label(184, cy + 17, lv["example"], size=14, weight="500", anchor="start",
                        fill=_SVG_INK_MUTED, data_part="example", data_key=lv["level"]))
        y += h
        if i < len(levels) - 1:
            o.append(_b1x_arrow(cx, y + 6, cx, y + 32, stroke=_SVG_INK, w=2.5, head=9, data_part="arrow"))
            y += 38
    return _b1x_open(fig, y + 8, o)


# ── b1-unicellular ──────────────────────────────────────────────────────
# Amoeba, Paramecium and Euglena, one per row, not to scale; ruled labels on
# the right, in top-to-bottom order of the parts they name.
_B1X_UNI_NAMES = {"nucleus": "Nucleus", "food vacuole": "Food vacuole",
                  "contractile vacuole": "Contractile\nvacuole", "cell membrane": "Cell membrane",
                  "cilia": "Cilia", "oral groove": "Oral groove", "flagellum": "Flagellum",
                  "eyespot": "Eyespot", "chloroplasts": "Chloroplasts"}


def _b1x_cvac(cx, cy, star):
    o = [_circle(cx, cy, 6, fill=_B1X_BLUE_TINT, stroke=_SVG_INK, w=1.5, data_part="contractile-vacuole")]
    if star:
        for k in range(6):
            a = 2 * _b1x_math.pi * k / 6 + .3
            o.append(_line(cx + 6 * _b1x_math.cos(a), cy + 6 * _b1x_math.sin(a),
                           cx + 14 * _b1x_math.cos(a), cy + 14 * _b1x_math.sin(a), stroke=_SVG_INK, w=1.5))
    return "".join(o)


def _b1x_uni_amoeba(oy):
    o = []
    cx, cy = 96, oy + 70
    pts = [(cx - 70, cy - 4), (cx - 52, cy - 34), (cx - 20, cy - 40), (cx + 4, cy - 52), (cx + 24, cy - 70),
           (cx + 44, cy - 62), (cx + 40, cy - 36), (cx + 66, cy - 22), (cx + 92, cy - 14), (cx + 92, cy + 4),
           (cx + 64, cy + 14), (cx + 44, cy + 40), (cx + 4, cy + 46), (cx - 36, cy + 38), (cx - 66, cy + 22)]
    o.append(_path(_b1x_smooth(pts), fill=_SVG_BAND, stroke=_SVG_INK, w=2.5, data_part="cell-membrane"))
    o.append(_b1x_nucleus(cx - 14, cy - 12, 14))
    o.append(_circle(cx + 14, cy + 22, 15, fill=_SVG_CARD, stroke=_SVG_INK, w=1.5, data_part="food-vacuole"))
    o.append(_ellipse(cx + 14, cy + 22, 8, 6, fill=_B1X_CHL, stroke=_SVG_INK, w=1.2, data_part="prey"))
    o.append(_b1x_cvac(cx + 62, cy - 5, False))
    tgt = {"cell membrane": (cx + 40, cy - 52), "nucleus": (cx - 1, cy - 17),
           "contractile vacuole": (cx + 68, cy - 5), "food vacuole": (cx + 29, cy + 24)}
    ys = {"cell membrane": cy - 56, "nucleus": cy - 26, "contractile vacuole": cy + 2, "food vacuole": cy + 44}
    return o, tgt, ys, cy + 54


def _b1x_slipper(cx, cy, a=86, b=26):
    """Boundary points of a Paramecium: a long oval, blunter at the front (left),
    with the oral groove dipping in along the lower side."""
    pts = []
    for k in range(48):
        t = 2 * _b1x_math.pi * k / 48
        x = cx + a * _b1x_math.cos(t)
        bb = b * (1.08 if _b1x_math.cos(t) < 0 else .92)
        y = cy + bb * _b1x_math.sin(t)
        if _b1x_math.sin(t) > 0:
            dip = _b1x_math.exp(-((_b1x_math.cos(t) + .15) ** 2) / .06)
            y -= 9 * dip * _b1x_math.sin(t)
        pts.append((x, y))
    return pts


def _b1x_uni_paramecium(oy):
    o = []
    cx, cy = 100, oy + 54
    pts = _b1x_slipper(cx, cy)
    n = len(pts)
    for k in range(n):
        x0, y0 = pts[k - 1]
        x1, y1 = pts[(k + 1) % n]
        tx, ty = x1 - x0, y1 - y0
        ln = _b1x_math.hypot(tx, ty) or 1
        nx, ny = ty / ln, -tx / ln
        px, py = pts[k]
        o.append(_line(px, py, px + nx * 8, py + ny * 8, stroke=_SVG_INK, w=1.3, data_part="cilium"))
    o.append(_path(_b1x_smooth(pts), fill=_SVG_BAND, stroke=_SVG_INK, w=2.5, data_part="cell-membrane"))
    gx = cx - .15 * 86
    o.append(_path("M %s,%s Q %s,%s %s,%s" % (_n(gx - 22), _n(cy + 20), _n(gx), _n(cy + 2), _n(gx + 20), _n(cy + 6)),
                   stroke=_SVG_INK, w=2.5, data_part="oral-groove"))
    o.append(_ellipse(cx + 12, cy - 6, 18, 11, fill=_B1X_NUC, stroke=_SVG_INK, w=2, data_part="nucleus"))
    o.append(_b1x_cvac(cx - 54, cy - 6, True))
    o.append(_b1x_cvac(cx + 60, cy - 4, True))
    tgt = {"cilia": (cx + 66, cy - 26), "contractile vacuole": (cx + 74, cy - 4),
           "nucleus": (cx + 26, cy + 2), "oral groove": (gx - 9, cy + 11)}
    ys = {"cilia": cy - 32, "contractile vacuole": cy - 8, "nucleus": cy + 34, "oral groove": cy + 58}
    return o, tgt, ys, cy + 64


def _b1x_uni_euglena(oy):
    o = []
    cy = oy + 64
    L, R = 22, 166
    # front (right) rounded, back (left) drawn out to a point
    d = ("M %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s C %s,%s %s,%s %s,%s Z"
         % tuple(_n(v) for v in (L, cy + 4,
                                 L + 40, cy - 8, L + 70, cy - 24, R - 30, cy - 22,
                                 R - 6, cy - 20, R + 2, cy - 4, R, cy + 2,
                                 R - 2, cy + 14, R - 24, cy + 22, R - 46, cy + 20,
                                 L + 64, cy + 18, L + 30, cy + 10, L, cy + 4)))
    flag = []
    for i in range(0, 41):
        t = i / 40.0
        x = R - 2 + t * 70
        flag.append((x, cy - 6 - t * 44 + 5 * _b1x_math.sin(t * 2 * _b1x_math.pi * 2)))
    o.append(_path(_b1x_polyd(flag), stroke=_SVG_INK, w=2.5, data_part="flagellum"))
    o.append(_path(d, fill=_SVG_BAND, stroke=_SVG_INK, w=2.5, data_part="cell-membrane"))
    for x, y, a in ((52, cy + 3, 0), (70, cy - 8, -15), (72, cy + 11, 15), (118, cy - 13, 5),
                    (132, cy + 9, -10), (142, cy - 5, 30)):
        o.append(_b1x_chloro(x, y, a, rx=7, ry=4))
    o.append(_b1x_nucleus(96, cy + 1, 11, 9))
    o.append(_ellipse(R - 12, cy - 9, 5, 3.5, fill=_B1X_EYE, stroke=_SVG_INK, w=1.2, data_part="eyespot"))
    tgt = {"flagellum": (R + 60, cy - 42), "eyespot": (R - 8, cy - 11), "chloroplasts": (139, cy + 10),
           "nucleus": (99, cy + 9)}
    ys = {"flagellum": cy - 48, "eyespot": cy - 14, "chloroplasts": cy + 20, "nucleus": cy + 42}
    return o, tgt, ys, cy + 48


def _b1x_unicellular(fig):
    orgs = _b1x_need(fig, "organisms")
    fns = {"amoeba": _b1x_uni_amoeba, "paramecium": _b1x_uni_paramecium, "euglena": _b1x_uni_euglena}
    o = []
    y = 4
    for i, org in enumerate(orgs):
        if org["kind"] not in fns:
            raise ValueError("figure %r: no organism %r" % (fig.get("id"), org["kind"]))
        if i:
            o.append(_b1x_divider(y + 8))
            y += 18
        o.append(_b1x_heading(y + 16, org["label"], org["kind"]))
        part, tgt, ys, bottom = fns[org["kind"]](y + 18)
        o.extend(part)
        for key in org.get("parts") or []:
            if key not in tgt:
                raise ValueError("figure %r: no %s part %r" % (fig.get("id"), org["kind"], key))
            tx, ty = tgt[key]
            lx = 244 if org["kind"] == "euglena" and key == "flagellum" else 214
            o.append(_b1x_lead(lx - 6, ys[key] - 5, tx, ty, key))
            o.append(_b1x_text(lx, ys[key], _B1X_UNI_NAMES.get(key, key.capitalize()),
                               data_part="label", data_key=key))
        y = bottom
    return _b1x_open(fig, y + 6, o)


ART = {
    'b1-light-microscope': _b1x_light_microscope,
    'b1-biological-drawing': _b1x_biological_drawing,
    'b1-cell-pair': _b1x_cell_pair,
    'b1-specialised-cells': _b1x_specialised_cells,
    'b1-diffusion': _b1x_diffusion,
    'b1-levels': _b1x_levels,
    'b1-unicellular': _b1x_unicellular,
}
