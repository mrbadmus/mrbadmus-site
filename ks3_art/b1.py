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
