# DISPATCH: "lever-steps": ("ks3-lstep-block", ' data-instrument data-lstepblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "lever-steps":            r_lever_steps,
#
# ╔═══════════════════════════════════════════════════════════════════════╗
# ║  TWO HAND EDITS, AND THIS FRAGMENT IS WRONG WITHOUT BOTH.             ║
# ║  Neither is derivable from the file, so neither can be spliced        ║
# ║  mechanically. `arm-lever`, `meter-compare` and `cover-triangle`      ║
# ║  need none — this is the only one.                                    ║
# ╚═══════════════════════════════════════════════════════════════════════╝
#
# ── EDIT 1 · this kind takes the LESSON, not just the activity ──────────
#
# Add it to `_KIND_FN_TAKES_LESSON` beside the three already there:
#
#     _KIND_FN_TAKES_LESSON = {"fifa-construct", "sabotage", "fifa-pick",
#                              "lever-steps"}
#
# WITHOUT IT the dispatch calls `r_lever_steps(a, act_id)` against a
# three-parameter function and the build dies with a TypeError naming this
# kind — loud, immediate, and not a silent wrong render, which is the one
# consolation.
#
# It has to take the lesson because the block's whole argument is that it is
# the SAME problem as the rig upstairs: it reads that instrument's own control
# defaults out of `lesson["activities"]` to render its resting state, and
# refuses to build if the rig it names is missing. A copy of "2 kg at 32 cm,
# muscle at 4 cm" here would go stale the first time anyone moved a slider in
# the payload, and nothing would say so.
#
# ── EDIT 2 · the block heading ships its braces without this ────────────
#
# Design draws this block's <h2> as the LIVE rig line — *"Your rig: 2.0 kg at
# 32 cm, muscle at 4.0 cm."* — and the shell emits the <h2> before any
# instrument renderer runs, so `r_lever_steps` cannot reach it. Add these two
# lines to `r_activity`, anywhere after `kind` is computed (~line 6372) and
# before the `if a.get("heading") and not hc:` branch (~line 6440):
#
#     # ⊕ b2-04 #s-build — this block's heading quotes the rig the student
#     # left set, so it is filled from that instrument before the shell
#     # emits the <h2>. `wireLeverSteps` repaints the same element.
#     if kind == "lever-steps":
#         a = dict(a, heading=_lever_steps_heading(lesson, a))
#
# WITHOUT IT the page ships `<h2>Your rig: {load} kg at {hand} cm, muscle at
# {ins} cm.</h2>` — which the wiring then overwrites, so it is invisible in a
# browser and permanent in the HTML a crawler reads and in every no-JS view.
#
# Filling it at BUILD TIME as well as at runtime is the whole point.
# `dict(a, …)` rather than `a["heading"] = …` so the lesson record is never
# mutated: `r_activity` runs once per page, but the record is shared with
# every gate that reads it afterwards.
#
# Place `r_lever_steps` and its two helpers beside `r_fifa_pick`
# (build_ks3.py ~3888), which is the component it is closest to. Needs `e`,
# `t`, `rich`, and `_lever_num` / `_lever_decimals` from the `arm-lever`
# fragment — splice that one first.


def _lever_steps_rig(lesson, a, act_id):
    """The `arm-lever` this block mirrors, and the substitutions it implies.

    Returns `(subs, fill)`. Separated from the renderer because the block's
    own <h2> is emitted by the shell and has to be filled from the same three
    values through the same formatter — two copies of "how many decimal
    places does 0.04 get" is two answers to it.
    """
    rig_id = a.get("rig")
    rig = next((x for x in (lesson.get("activities") or [])
                if x.get("id") == rig_id), None)
    if rig is None:
        raise ValueError(
            "lever-steps %r reads rig %r and the lesson declares no activity "
            "with that id. The block's whole claim is that it is the same "
            "problem as the bench upstairs." % (act_id, rig_id))
    if rig.get("kind") != "arm-lever":
        raise ValueError(
            "lever-steps %r names rig %r, which is a %r. Only `arm-lever` "
            "carries the load, the two distances and g that every template "
            "here interpolates." % (act_id, rig_id, rig.get("kind")))

    controls = {c["key"]: c for c in (rig.get("controls") or [])}
    missing = [k for k in ("load", "ins", "hand") if k not in controls]
    if missing:
        raise ValueError(
            "lever-steps %r reads rig %r, which has no %s control. Every "
            "template in this block interpolates all three."
            % (act_id, rig_id, ", ".join(missing)))
    dp = {k: (0 if controls[k].get("options")
              else _lever_decimals(controls[k].get("step")))
          for k in ("load", "ins", "hand")}
    start = {k: float(controls[k]["start"]) for k in ("load", "ins", "hand")}
    g = float(rig.get("g") or 0)

    W = start["load"] * g
    dM, dL = start["ins"] / 100.0, start["hand"] / 100.0
    # ⚠️ Two decimal places on the distances and on the turning effect, and
    # NONE on the weight or the force. That is Design's own arithmetic and it
    # is not tidiness: `0.04` and `0.32` are the metre conversions a student
    # writes down, and `6.40` is what `20 × 0.32` gives on a calculator. A
    # weight and a force are whole newtons on this page.
    subs = {
        "{load}": _lever_num(start["load"], dp["load"], "{n}"),
        "{ins}": _lever_num(start["ins"], dp["ins"], "{n}"),
        "{hand}": _lever_num(start["hand"], dp["hand"], "{n}"),
        "{W}": "%.0f" % W,
        "{dM}": "%.2f" % dM,
        "{dL}": "%.2f" % dL,
        "{TE}": "%.2f" % (W * dL),
        "{F}": "%.0f" % (W * dL / dM),
        "{ratio}": "%.1f" % (start["hand"] / start["ins"]),
    }

    def fill(s):
        out = s or ""
        for k, v in subs.items():
            out = out.replace(k, v)
        return out

    return subs, fill


def _lever_steps_heading(lesson, a):
    """The block's <h2>, filled from the rig. Spliced into `r_activity`."""
    _, fill = _lever_steps_rig(lesson, a, a.get("id"))
    return fill(a.get("heading", ""))


def r_lever_steps(lesson, a, act_id):
    """⊕ b2-04 `#s-build` — MRB-204 step 4, on the student's OWN rig.

    ⚖️ NOT `fifa-pick`, and the difference is arithmetic rather than taste.
    c2-06's block has the same furniture — two pick ladders, a number field, a
    unit select, a locked open button and a four-step ink reveal — and every
    string in it is STATIC. Here, five of the eight authored strings are
    templates over three live values: the heading quotes the rig, the second
    ladder's three options are this student's own numbers arranged three ways,
    all four reveal steps carry them, and the closing line holds the student's
    typed answer against the force their own rig implies. `r_fifa_pick` emits
    finished text and `wirePick` never recomputes anything, so pointing this
    payload at it would print `F × {dM} = {W} × {dL}` into a button.

    ⚖️ AND THE GENERATION IS THE PEDAGOGY, not a convenience. Authoring the
    insert options would pin the rig at 2 kg and 32 cm and make every other
    setting of the sliders unanswerable — the block would quietly stop being
    about the student's own arm the moment they touched a control, which is
    the one thing the whole page asked them to do.

    ⚠️ NOT `fifa-construct` either: four free-text inputs and a tick list
    against two multiple-choice ladders and a number, and that renderer
    asserts `len(fields) == len(model) == len(success)` — three commitments
    against four model lines and no criteria would raise, and rightly.

    ── ⊕ CORRECTION: THE RAIL STOP DEMANDS SOMETHING ────────────────────

    Design ticks `#s-build` on `buildOpen` alone — on the student pressing
    "Show the four steps". A student who scrolls here and presses the button
    has committed to nothing and the rail says the stage is done. MRB-208 has
    a rail stop requiring the student to DO something, so the stop now ticks
    on the three commitments the block itself asks for: the formula picked,
    the insertion picked, and a non-empty answer WITH a unit.

    That is strictly earlier than the button, which needs the same three, so
    nothing a student can do gets harder — the stop simply stops being
    reachable by pressing one thing. It is also why the reveal is not the
    signal: opening an answer is the reward for committing, not the commitment.

    ⚠️ THE UNIT IS ITS OWN COMMITMENT. "160" is not an answer to a question
    about force, and the placeholder `<option>` carries an EMPTY value so that
    a student who never chose one cannot satisfy the gate. Measured in a
    browser on c2-06, not read off the source.

    ⚠️ NO `value` ATTRIBUTE ON THE INPUT. An authored `value` is an attribute,
    the element reads it only as its default, and the first repaint wipes what
    the student typed. B1 fixed this once already; Design's page re-introduces
    it (`<input … value="{{ ansValue }}">`) and it is not reproduced.
    """
    subs, fill = _lever_steps_rig(lesson, a, act_id)

    picks = a.get("picks") or []
    if len(picks) != 2:
        raise ValueError(
            "lever-steps %r declares %d pick ladder(s); it takes two — the "
            "rule and the insertion." % (act_id, len(picks)))
    steps = a.get("steps") or []
    if not steps:
        raise ValueError("lever-steps %r reveals no steps[]." % act_id)
    field = a.get("field") or {}
    if not field.get("units"):
        raise ValueError(
            "lever-steps %r offers no units[]. The unit is a separate "
            "commitment: `160` is not an answer to a question about force."
            % act_id)

    panels = []
    for i, p in enumerate(picks):
        opts = "".join(
            '<button type="button" class="ks3-lstep-opt" data-group="%d" '
            'data-i="%d" data-template="%s" aria-pressed="false">%s</button>'
            # ⚠️ BOTH the filled text AND the template are emitted. The button
            # renders finished at build time and the wiring refills it from
            # the same template when the rig moves, so there is exactly one
            # authored string and no second copy in JS to drift from it.
            % (i, j, e(o), t(fill(o)))
            for j, o in enumerate(p.get("options") or []))
        panels.append(
            '<div class="ks3-lstep-panel">'
            '<p class="ks3-lstep-label">%s</p>'
            '<p class="ks3-lstep-q">%s</p>'
            '<div class="ks3-lstep-opts">%s</div></div>'
            % (t(p.get("label", "")), t(p.get("question", "")), opts))

    aid, uid = "%s-ans" % act_id, "%s-unit" % act_id
    units = ('<option value="">%s</option>' % t(field["unit_placeholder"])
             if field.get("unit_placeholder") else "")
    units += "".join('<option value="%s">%s</option>' % (e(u), t(u))
                     for u in field["units"])
    panels.append(
        '<div class="ks3-lstep-panel">'
        '<p class="ks3-lstep-label">%s</p>'
        '<p class="ks3-lstep-q">%s</p>'
        '<div class="ks3-lstep-answer">'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<input class="ks3-lstep-input" type="text" inputmode="decimal" '
        'id="%s" placeholder="%s" autocomplete="off" data-lstep-ans>'
        '<label class="ks3-sr-only" for="%s">%s</label>'
        '<select class="ks3-sim-units ks3-lstep-unit" id="%s" data-lstep-unit>'
        '%s</select></div></div>'
        % (t(field.get("label", "")), t(field.get("question", "")),
           e(aid), t(field.get("hint", "")), e(aid),
           e(field.get("placeholder", "")), e(uid),
           t(field.get("unit_hint", "")), e(uid), units))

    reveal = "".join(
        '<div class="ks3-lstep-step">'
        '<span class="ks3-lstep-chip" aria-hidden="true">%s</span>'
        '<div class="ks3-lstep-stepbody">'
        '<p class="ks3-lstep-steplabel">%s</p>'
        '<p class="ks3-lstep-stepline" data-template="%s">%s</p>'
        '<p class="ks3-lstep-stepnote" data-template="%s">%s</p></div></div>'
        % (t(s.get("letter", "")), t(s.get("label", "")),
           e(s.get("line", "")), t(fill(s.get("line", ""))),
           e(s.get("note", "")), rich(fill(s.get("note", ""))))
        for s in steps)

    close = a.get("close") or {}
    progress = a.get("progress") or {}
    return ('<div class="ks3-lstep" data-lstep data-rig="%s" data-total="3" '
            'data-head="%s" '
            'data-close="%s" data-blank="%s" data-progress="%s" '
            'data-done-label="%s">'
            '<div class="ks3-lstep-panels">%s</div>'
            '<div class="ks3-lstep-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-lstep-btn" '
            'data-lstep-open disabled>%s</button>'
            '<span class="ks3-lstep-progress" data-lstep-progress>%s</span>'
            '</div>'
            '<div class="ks3-lstep-reveal" hidden data-reveal>'
            '<p class="ks3-lstep-revealhead">%s</p>%s'
            '<p class="ks3-lstep-close" data-lstep-close></p></div></div>'
            # The heading's raw template rides on the instrument so
            # `wireLeverSteps` can repaint the shell's <h2> from the same
            # authored string the build filled — never from a second copy.
            % (e(a.get("rig", "")), e(a.get("heading", "")),
               e(close.get("template", "")),
               e(close.get("blank") or "—"),
               e(progress.get("format", "")),
               e(progress.get("done", "")),
               "".join(panels), t(a.get("button", "")),
               t(progress.get("format", "").replace("{n}", "0")),
               t(a.get("reveal_head", "")), reveal))
