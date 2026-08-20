"""ks3_art.b2 — B2's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import json
import math
import re
from ks3_art.kit import (
    _lever_decimals,
    _lever_num,
    _lever_steps_rig,
    _option_li,
    e,
    r_activity_options,
    r_bench_gate,
    rich,
    t,
)


def r_job_sort(a, act_id):
    """⊕ b2-01 `#s-sort` · b2-02 `#s-cases` · b2-03 `#s-pairs`.

    The per-item sorter, and the unit's highest-reuse component: 14 authored
    items across three lessons. It is NOT `sort-task` and NOT `sort-rows`, and
    the difference is the whole pedagogy — both of those gate every row behind
    one "open the answers" button, and this one reveals EACH ROW THE INSTANT
    THAT ROW IS DECIDED. A student finds out about item 1 before committing on
    item 2, which is what makes the sequence teach.

    ⚠️ NO ANSWER VALIDATION, deliberately. `sort-task` asserts every item's
    `answer` is one of the offered choices, and b2-01's item `i4` answers
    "Movement and protection — both." — a fifth string that is not one of the
    four jobs, and is the whole point of that item. Validating here would
    refuse Design's payload at build time.

    ⚠️ R3 / MRB-196 R10. Nothing marks correctness: the chosen option keeps
    the ordinary chosen treatment, the unchosen ones dim, the ROW's border
    goes to ink, and the why paragraph is one tone whether the student had it
    or not. Do not add a verdict here for tidiness — the sorter is a sequence
    of commitments, not a test.
    """
    items = a.get("items") or []
    if not items:
        raise ValueError("job-sort %r declares no items[]." % act_id)
    shared = [c.get("label", "") for c in (a.get("categories") or [])]

    rows = []
    for it in items:
        labels = it.get("options") or shared
        if not labels:
            raise ValueError(
                "job-sort %r item %r offers no options and the activity "
                "declares no shared categories[]." % (act_id, it.get("id")))
        opts = "".join(
            '<button type="button" class="ks3-jobsort-opt" data-i="%d" '
            'aria-pressed="false">%s</button>' % (i, t(lab))
            for i, lab in enumerate(labels))
        rows.append(
            '<li class="ks3-jobsort-item" data-item="%s">'
            '<p class="ks3-jobsort-text">%s</p>'
            '<div class="ks3-jobsort-opts">%s</div>'
            '<p class="ks3-jobsort-why" hidden data-reveal>'
            '<strong class="ks3-jobsort-answer">%s</strong> %s</p></li>'
            % (e(it.get("id", "")), t(it.get("text", "")), opts,
               t(it.get("answer", "")), rich(it.get("why", ""))))

    close = ('<div class="ks3-jobsort-close" hidden data-jobsort-close>'
             '<p>%s</p></div>' % rich(a["close_all"])) if a.get("close_all") else ""
    return ('<div class="ks3-jobsort" data-jobsort data-total="%d">'
            '<ul class="ks3-jobsort-list" role="list">%s</ul>%s</div>'
            % (len(items), "".join(rows), close))
def r_system_switch(a, act_id):
    """⊕ b2-01 `#s-switch` — take one part away and follow the damage.

    Close to `sabotage` and not the same component. Three measured
    differences, any one of which is fatal:

      * `sabotage` is CAST-COUPLED — `_drawing_for()` raises unless a
        `system-bench` on the same page declares the specimen. b2-01 has no
        bench and no cells.
      * `sabotage` paints a `<canvas data-drawing>` per panel from
        `CELL_DRAWINGS`. B2 is deliberately drawing-free (NOTES flag 17: no
        anatomical diagrams anywhere in the unit).
      * `sabotage` renders the ink-dark `practical` shell. `#s-switch` is a
        LIGHT `.ks3-block` with an ink-dark panel inside it, after the reveal.

    Emit-all-show-one, the same trick the board uses: four panels in the
    document, one shown, so going back to a part finds it as you left it and
    no state lives anywhere but the DOM.

    ⊕ `show_levels: False` OMITS the chip and collapses the grid. Design's own
    page keeps rendering an empty pill in a 104px column that holds nothing —
    a prop that half works. Nothing in B2 authors it; the branch exists so the
    prop means what it says the day a lesson wants it.
    """
    parts_ = a.get("parts") or []
    if not parts_:
        raise ValueError("system-switch %r declares no parts[]." % act_id)
    show_levels = a.get("show_levels") is not False
    labels = a.get("labels") or {}

    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-switch-tab" '
        'data-part="%s" aria-pressed="%s">%s</button>'
        % (e(p["id"]), "true" if i == 0 else "false", t(p.get("tab", "")))
        for i, p in enumerate(parts_))

    panels = []
    for i, p in enumerate(parts_):
        opts = "".join(_option_li(j, o, ' aria-pressed="false"')
                       for j, o in enumerate(p.get("options") or []))
        chain = []
        for st in p.get("chain") or []:
            level = st.get("level") or ""
            # Chip colour is a function of the LEVEL STRING, not of position:
            # the chains do not all climb (femur ends at Cell, marrow starts
            # and ends there), so the chip can never be a rendering of index.
            chip = ('<span class="ks3-switch-chip" data-level="%s">%s</span>'
                    % (e(level.lower()), t(level))) if show_levels else ""
            chain.append('<div class="ks3-switch-row"%s>%s'
                         '<p class="ks3-switch-step">%s</p></div>'
                         % ("" if show_levels else ' data-nolevel="1"',
                            chip, rich(st.get("text", ""))))
        panels.append(
            '<div class="ks3-switch-panel" data-part="%s"%s>'
            '<div class="ks3-switch-what">'
            '<p class="ks3-switch-name">%s</p>'
            '<p class="ks3-switch-does">%s</p></div>'
            '<div class="ks3-switch-predict"><p class="ks3-commit">%s</p>'
            '<ul class="ks3-options" role="list">%s</ul></div>'
            '<div class="ks3-switch-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-switch-btn" '
            'data-switch data-done-label="%s" disabled>%s</button>'
            '<span class="ks3-switch-hint" data-switch-hint>%s</span></div>'
            '<div class="ks3-switch-chain" hidden data-switch-chain>'
            '<p class="ks3-switch-title">%s</p>'
            '<div class="ks3-switch-rows">%s</div>'
            '<p class="ks3-switch-close">%s</p></div></div>'
            % (e(p["id"]), "" if i == 0 else " hidden",
               t(p.get("name", "")), rich(p.get("does", "")),
               t(p.get("prompt", "")), opts,
               e(labels.get("switched") or "Switched off"),
               t(labels.get("switch") or "Switch this part off"),
               t(labels.get("hint_locked") or ""),
               t(p.get("title", "")), "".join(chain),
               rich(p.get("close", ""))))

    close = ('<div class="ks3-switch-all" hidden data-switch-all><p>%s</p>'
             '</div>' % rich(a["close_all"])) if a.get("close_all") else ""
    return ('<div class="ks3-switch" data-switch-block data-total="%d" '
            'data-hint-ready="%s" data-hint-done="%s">'
            '<div class="ks3-switch-tabs">%s</div>%s%s</div>'
            % (len(parts_), e(labels.get("hint_ready") or ""),
               e(labels.get("hint_done") or ""), tabs, "".join(panels), close))
def _joint_payload(a, act_id):
    """The joint bench's data, as JSON the canvas engine reads.

    Everything the drawing needs is a function of `bend[]` and `twist`, which
    is what makes this the one genuinely parametric instrument in the unit —
    the sweep, the joint glyph, the seam and the twist verdict are all
    derived. Nothing here is a per-joint magic number except the two Design
    authored: the bend range and the starting angle.
    """
    joints = a.get("joints") or []
    if not joints:
        raise ValueError("joint-bench %r declares no joints[]." % act_id)
    out = []
    for j in joints:
        bend = list(j.get("bend") or [0, 0])
        if len(bend) != 2:
            raise ValueError(
                "joint-bench %r joint %r declares bend=%r; it takes exactly "
                "[min, max] in degrees." % (act_id, j.get("id"), bend))
        out.append({
            "id": j["id"], "name": j.get("name", ""),
            "bend": [int(bend[0]), int(bend[1])],
            "twist": bool(j.get("twist")),
            # ⚠️ The starting angle lives ON THE JOINT, not in a
            # `{joint_id: angle}` map beside it. Design authors the map; a map
            # keyed by id makes every joint's NAME a dict key, and a key that
            # is only ever reached by iterating is invisible to
            # `ks3_key_audit.py` — which reported `pivot` as authored-and-
            # unread, correctly, because nothing in the engine ever needs to
            # say the word. Put on the joint it is a schema field with one read
            # site, and the audit is right about it either way.
            "start": int(j.get("start", bend[0])),
            "axes": j.get("axes", ""), "where": j.get("where", ""),
            "hold": j.get("hold", ""), "trade": j.get("trade", ""),
            "angle_label": j.get("angle_label", ""),
            "twist_yes": j.get("twist_yes", ""),
            "twist_no": j.get("twist_no", ""),
        })
    return out
def r_joint_bench(a, act_id):
    """⊕ b2-02 `#s-bench` — a two-bone linkage, drawn from the data.

    The nearest shipped canvas engines are the microscope and the four
    `CELL_DRAWINGS`, which are a fixed enum of portraits. This is not that: a
    joint whose allowed sweep, glyph radius, groove, seam and twist verdict
    are all computed from `bend[]` and `twist` is a drawing of the payload,
    and adding a fifth joint needs no new drawing code.

    ⚠️ The REFUSAL IS DRAWN, and that is the lesson. A pivot and a fixed joint
    get a disabled slider, the literal readout `locked`, and a label that says
    the joint does not bend — three coordinated readouts. A generic range
    control gives none of them, which is why this is not `sim`.
    """
    joints = _joint_payload(a, act_id)
    labels = a.get("labels") or {}
    alt = a.get("alt") or {}
    locked_word = labels.get("locked") or "locked"
    first = joints[0]
    gate_html, hide = r_bench_gate(a.get("gate"))

    tabs = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-joint-tab" '
        'data-joint="%s" aria-pressed="%s">%s</button>'
        % (e(j["id"]), "true" if i == 0 else "false", t(j.get("tab", "")))
        for i, j in enumerate(a.get("joints") or []))

    def tile(label, key, value, mono=False):
        return ('<div class="ks3-joint-tile">'
                '<p class="ks3-joint-tile-label">%s</p>'
                '<p class="ks3-joint-tile-value%s" data-tile="%s">%s</p>'
                '</div>' % (t(label), " ks3-joint-tile-mono" if mono else "",
                            e(key), t(value)))

    # The resting readouts are rendered from the FIRST joint here rather than
    # left blank for JS to fill: a page with JS still loading must never show
    # an instrument full of empty boxes, and the values are known at build
    # time. `wireJointBench` repaints the same elements from the same data.
    first_note = ((labels.get("twist_idle") or "") if first["twist"]
                  else first["twist_no"])
    body = (
        '<div class="ks3-joint" data-jointbench%s data-total="%d" '
        'data-joints="%s" data-alt="%s" data-alt-can="%s" data-alt-cannot="%s" '
        'data-locked="%s" data-twist-off="%s" data-twist-on="%s" '
        'data-twist-idle="%s">'
        '<div class="ks3-joint-tabs">%s</div>'
        '<div class="ks3-joint-stage">'
        '<canvas class="ks3-joint-canvas" width="1800" height="740" '
        'role="img" aria-label="%s" data-joint-canvas></canvas>'
        '<div class="ks3-joint-controls">'
        '<div class="ks3-joint-anglerow">'
        '<label class="ks3-joint-anglelabel" for="%s-angle" data-angle-label>'
        '%s</label>'
        '<p class="ks3-joint-anglevalue" data-angle-value>%s</p></div>'
        '<input class="ks3-slider" type="range" id="%s-angle" min="%d" '
        'max="%d" step="1" value="%d" data-angle%s>'
        '<div class="ks3-joint-twistrow">'
        '<button type="button" class="ks3-sim-seg-btn ks3-joint-twist" '
        'data-twist aria-pressed="false">%s</button>'
        '<p class="ks3-joint-twistnote" data-twist-note>%s</p>'
        '</div></div></div>'
        '<div class="ks3-joint-tiles">%s%s%s</div>'
        '<p class="ks3-joint-trade"><strong>%s</strong> '
        '<span data-tile="trade">%s</span></p></div>'
        % (hide, len(joints),
           # `ensure_ascii=False` so the attribute carries the real
           # characters — an em dash written as `\\u2014` round-trips
           # correctly through JSON.parse but is unreadable in
           # view-source and invisible to a byte-identity grep.
           e(json.dumps(joints, separators=(",", ":"), sort_keys=True,
                        ensure_ascii=False)),
           e(alt.get("template", "")), e(alt.get("can", "")),
           e(alt.get("cannot", "")), e(locked_word),
           e(labels.get("twist") or ""), e(labels.get("twisting") or ""),
           e(labels.get("twist_idle") or ""),
           tabs,
           e(_joint_alt(alt, first, first["start"])),
           e(act_id), t(first["angle_label"]),
           t("%d°" % first["start"] if first["bend"][1] > 0 else locked_word),
           e(act_id), first["bend"][0], first["bend"][1] or 1, first["start"],
           " disabled" if first["bend"][1] == 0 else "",
           t(labels.get("twist") or ""), t(first_note),
           tile(labels.get("axes") or "", "axes", first["axes"], mono=True),
           tile(labels.get("where") or "", "where", first["where"]),
           tile(labels.get("hold") or "", "hold", first["hold"]),
           t(labels.get("trade") or ""), t(first["trade"])))
    return gate_html + body
def _joint_alt(alt, j, angle):
    """The canvas's aria-label, composed the same way in Python and in JS.

    Composed rather than authored: it quotes three live values, so an authored
    string would be a fourth copy of the state and would go stale the moment
    the slider moved.
    """
    return (alt.get("template", "")
            .replace("{name}", (j.get("name") or "").lower())
            .replace("{angle}", str(angle))
            .replace("{max}", str(j["bend"][1]))
            .replace("{twist}", alt.get("can" if j.get("twist")
                                        else "cannot", "")))
def r_muscle_pair(a, act_id):
    """⊕ b2-03 `#s-bench` — two muscles, one elbow, and a continuous state.

    The only B2 instrument with physics running in it. The mechanism IS the
    teaching and is not chrome:

        both pulling   → the joint LOCKS wherever it is
        biceps only    → 135°
        triceps only   → 6°
        neither        → 6°, and it FALLS at 55 °/s where a pull moves at 90

    ⚠️ Do not flatten the two rates. "Gravity straightens a hanging arm for
    free" is taught by pressing *Neither* and watching it go down more slowly
    than it came up; equal rates delete the lesson and leave the animation.

    ⚠️ Two independent control groups — an exclusive four-tab mode group and a
    NON-exclusive two-toggle kill group, whose product decides every readout.
    No shipped instrument has this topology, which is most of why this is not
    a `sim`.

    ⊕ CORRECTION (contract R4). Design's page reads `prefers-reduced-motion`
    once at construction and never consults it in the tick, so the arm
    animates under reduced motion; its own sibling b2-02 checks correctly.
    Here the loop asks every frame and snaps straight to the target when
    motion is reduced — the arm still ends up where the mechanism says, it
    just does not travel there. Reduced motion is a complete experience, not a
    lesser one (R6).
    """
    modes = a.get("modes") or []
    kills = a.get("kills") or []
    if len(modes) != 4 or len(kills) != 2:
        raise ValueError(
            "muscle-pair %r takes exactly four contraction modes and two kill "
            "switches; got %d and %d." % (act_id, len(modes), len(kills)))
    labels = a.get("labels") or {}
    gate_html, hide = r_bench_gate(a.get("gate"))

    mode_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-muscle-mode" '
        'data-mode="%s" aria-pressed="%s">%s</button>'
        % (e(m["id"]), "true" if m["id"] == a.get("start_mode") else "false",
           t(m.get("label", "")))
        for m in modes)
    kill_btns = "".join(
        '<button type="button" class="ks3-sim-seg-btn ks3-muscle-kill" '
        'data-kill="%s" aria-pressed="false">%s</button>'
        % (e(k["id"]), t(k.get("label", ""))) for k in kills)

    cfg = {
        "start_angle": a.get("start_angle", 10),
        "targets": a.get("targets") or {},
        "rates": a.get("rates") or {},
        "notes": a.get("notes") or {},
        "status": a.get("status") or {},
        "states": a.get("states") or {},
        "canvas_labels": a.get("canvas_labels") or {},
        "alt": a.get("alt") or {},
    }
    tile = ('<div class="ks3-joint-tile">'
            '<p class="ks3-joint-tile-label">%s</p>'
            '<p class="ks3-joint-tile-value%s" data-tile="%s">%s</p></div>')
    return (gate_html
            + '<div class="ks3-muscle" data-musclepair%s data-total="%d" '
              'data-cfg="%s">'
              '<div class="ks3-muscle-groups">'
              '<div class="ks3-muscle-group">'
              '<p class="ks3-muscle-grouplabel">%s</p>'
              '<div class="ks3-muscle-btns">%s</div></div>'
              '<div class="ks3-muscle-group">'
              '<p class="ks3-muscle-grouplabel">%s</p>'
              '<div class="ks3-muscle-btns">%s</div></div></div>'
              '<div class="ks3-joint-stage">'
              '<canvas class="ks3-joint-canvas" width="1800" height="740" '
              'role="img" aria-label="%s" data-muscle-canvas></canvas>'
              '<div class="ks3-joint-controls">'
              '<p class="ks3-muscle-status" data-muscle-status>%s</p>'
              '</div></div>'
              '<div class="ks3-joint-tiles">%s%s%s</div>'
              '<p class="ks3-joint-trade"><strong>%s</strong> '
              '<span data-tile="note">%s</span></p></div>'
            % (hide, a.get("settings_total", 4),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               t(labels.get("contract") or ""), mode_btns,
               t(labels.get("kill") or ""), kill_btns,
               e(_muscle_alt(a.get("alt") or {}, "relaxed", "relaxed")),
               t((a.get("status") or {}).get(a.get("start_mode") or "none", "")),
               tile % (t(labels.get("angle") or ""), " ks3-joint-tile-mono",
                       "angle", t("%d°" % int(a.get("start_angle", 10)))),
               tile % (t(labels.get("biceps") or ""), "", "biceps",
                       t((a.get("states") or {}).get("relaxed", ""))),
               tile % (t(labels.get("triceps") or ""), "", "triceps",
                       t((a.get("states") or {}).get("relaxed", ""))),
               t(labels.get("note") or ""),
               t((a.get("notes") or {}).get(a.get("start_mode") or "none", ""))))
def _muscle_alt(alt, biceps_key, triceps_key):
    """The arm canvas's aria-label. Same composition in Python and in JS."""
    words = alt.get("words") or {}
    return (alt.get("template", "")
            .replace("{biceps}", words.get(biceps_key, ""))
            .replace("{triceps}", words.get(triceps_key, "")))
# renderers: ═══ END C1 ═══





# renderers: ═══ BEGIN B2 ═══
# DISPATCH: "arm-lever": ("ks3-lever-block", ' data-instrument data-leverblock data-stage-done="0"'),
#
# and in ACTIVITY_KIND_FN, beside the other B2 rows:
#     "arm-lever":              r_arm_lever,
#
# Place `r_arm_lever` and the two helpers below beside `r_muscle_pair` in the
# B2 group (build_ks3.py ~3079). Needs `e`, `t`, `r_bench_gate`. No new
# imports: the only arithmetic here is a divide and a round, and
# `int(v + 0.5)` is `math.floor` for a positive v, which every value on this
# rig is (the sliders' floors are 0.5 kg and 3 cm).
#
# ⚠️ `_lever_num` and `_lever_alt` are MODULE-LEVEL, not nested, because the
# RESTING render needs the same formatter and the same composition the runtime
# uses. Two copies of "how is this number written" is two answers to it, and
# the number is on screen before any JS runs.


# Values the rig COMPUTES rather than reads off a control. Both are Design's
# `.toFixed(0)` — a weight and a force are whole newtons on this page.
_LEVER_COMPUTED = {"weight": 0, "force": 0}
def _lever_alt(alt, load, ins, hand, force=None):
    """The canvas's aria-label, composed the same way in Python and in JS.

    ⚖️ THE LABEL IS THE WHOLE DRAWING for a screen-reader user: the two
    dimension lines, the load's weight arrow and the joint are painted inside
    the canvas and exist nowhere in the DOM. So every number a sighted student
    can see on the drawing has to be in here.

    ⚠️ AND NOT ONE MORE THAN THAT. `force` is appended only once the meter has
    been fitted — the same gate the muscle tile takes, reached by the other
    route. Handing the answer to a screen-reader user before they have worked
    it out is not an accommodation, it is a different lesson.

    ⚠️ SINGULAR/PLURAL. C1 shipped "after 1 halvings" and it had to be fixed,
    so the guard is here from the start rather than after somebody reads it
    aloud. No control on this rig can currently reach a bare 1 — `load` and
    `ins` render to one decimal ("1.0 kilograms" is correct English) and
    `hand` offers 32 and 16 — but a future payload with `step: 1` on the load
    would, and a plural that only breaks for one authored value is exactly the
    kind of defect that ships.
    """
    out = (alt.get("template", "")
           .replace("{load}", load).replace("{ins}", ins)
           .replace("{hand}", hand))
    if force is not None and alt.get("measured"):
        out += alt["measured"].replace("{force}", force)
    for word in ("kilogram", "centimetre", "newton"):
        out = out.replace(" 1 %ss" % word, " 1 %s" % word)
    return out
def r_arm_lever(a, act_id):
    """⊕ b2-04 `#s-bench` — the forearm rig, and the number it will not give you.

    ⚖️ THE MISSING FOURTH NUMBER IS THE WHOLE INSTRUMENT. The rig hands over
    the load and both distances and refuses the muscle force: the tile reads
    the authored `unmeasured` sentence, and the muscle arrow on the canvas
    carries the bare word "muscle" and deliberately no magnitude. A student
    who could read the force off the rig would never divide anything, and the
    meter exists so they can CHECK their arithmetic rather than skip it.
    That gate is why the meter button is one-way and why fitting it is half
    the rail stop.

    ⚠️ NOT `sim`, and not `joint-bench`. Three measured differences, any one
    of which is fatal:

      * `sim`'s controls are a CLOSED ENUM validated against `SIM_CONTROLS`;
        this rig's three are a mass, an attachment distance and a two-tab
        distance, and none of them is in that list. Adding them would give
        every KS3 sim a "muscle attached at" slider.
      * `joint-bench` reads a per-joint record and paints a linkage; every
        readout it has is a lookup. Every readout here is ARITHMETIC on the
        three live values, and the one that matters is withheld.
      * a mixed control topology — two sliders and an exclusive two-tab set —
        whose product decides four readouts, a canvas and a rail predicate.

    ⚠️ INK-DARK, so every text rule in the stylesheet is scoped `.ks3-dark …`.
    `.ks3-dark p` is (0,1,1) and a bare instrument class is (0,1,0): unscoped,
    the tile labels and the meter note lose and render in on-dark body copy
    against a panel that is not the ground they were coloured for. That is the
    defect B1 shipped with the zoom instrument and B2 was bitten by again.

    ⊕ ADDITIONS inside the drawn component, both stated in the report:
      * `alt.measured` — Design's `benchAlt` never mentions the muscle force,
        so once the meter is fitted a screen-reader user is the only person on
        the page who cannot read it. Appended, and only then.
      * `done_at` — Design hard-codes `>= 2` inside its own rail predicate.
        Authored once here and read by the wiring, so the rail's demand is
        data rather than a number nobody can find.
    """
    controls = a.get("controls") or []
    if not controls:
        raise ValueError("arm-lever %r declares no controls[]." % act_id)

    by_key, decimals = {}, {}
    for c in controls:
        key = c.get("key")
        if not key:
            raise ValueError(
                "arm-lever %r has a control with no `key`; the key is what the "
                "tiles, the canvas and the steps block all name it by."
                % act_id)
        if c.get("options"):
            if c.get("start") not in c["options"]:
                raise ValueError(
                    "arm-lever %r control %r starts at %r, which is not one of "
                    "the tabs it offers (%s)."
                    % (act_id, key, c.get("start"),
                       ", ".join(str(o) for o in c["options"])))
            decimals[key] = 0
        else:
            for bound in ("min", "max", "step"):
                if c.get(bound) is None:
                    raise ValueError(
                        "arm-lever %r control %r is a slider and declares no "
                        "`%s`; a range with an open end renders as a browser "
                        "default and reads any value at all."
                        % (act_id, key, bound))
            if not float(c["min"]) <= float(c["start"]) <= float(c["max"]):
                raise ValueError(
                    "arm-lever %r control %r starts at %r, outside its own "
                    "%r–%r range." % (act_id, key, c.get("start"),
                                      c.get("min"), c.get("max")))
            decimals[key] = _lever_decimals(c.get("step"))
        by_key[key] = c

    tiles = a.get("tiles") or []
    if not tiles:
        raise ValueError("arm-lever %r declares no tiles[]." % act_id)
    for tl in tiles:
        if tl.get("key") not in by_key and tl.get("key") not in _LEVER_COMPUTED:
            raise ValueError(
                "arm-lever %r tile %r reads %r, which is neither a control nor "
                "a computed value (%s). A tile with no source is a box that "
                "never fills." % (act_id, tl.get("label"), tl.get("key"),
                                  ", ".join(sorted(_LEVER_COMPUTED))))

    meter = a.get("meter") or {}
    for key in ("label", "label_done", "note", "note_done"):
        if not meter.get(key):
            raise ValueError(
                "arm-lever %r meter is missing %r. All four are drawn: the "
                "button says two things and the line beside it says two more, "
                "and a missing one leaves the previous state's sentence on "
                "screen after the meter is fitted." % (act_id, key))
    if not a.get("unmeasured"):
        raise ValueError(
            "arm-lever %r declares no `unmeasured` sentence. That string IS "
            "the gate — without it the force tile would open empty and the "
            "block would look broken rather than withholding." % act_id)

    canvas = a.get("canvas") or {}
    for key in ("title", "joint", "muscle", "load"):
        if not canvas.get(key):
            raise ValueError(
                "arm-lever %r canvas is missing %r." % (act_id, key))
    alt = a.get("alt") or {}
    if not alt.get("template"):
        raise ValueError(
            "arm-lever %r has no alt template; the dimension lines, the weight "
            "arrow and the joint are painted on the canvas and reach a screen "
            "reader through nothing else." % act_id)

    done_at = int(a.get("done_at") or 0)
    if not 1 <= done_at <= len(controls):
        raise ValueError(
            "arm-lever %r ticks its rail stop at %r control(s) moved; it "
            "offers %d. A stop that cannot be reached is worse than none."
            % (act_id, a.get("done_at"), len(controls)))

    g = float(a.get("g") or 0)
    if g <= 0:
        raise ValueError(
            "arm-lever %r declares g = %r N/kg. The whole page's arithmetic "
            "runs through it." % (act_id, a.get("g")))

    # ── the resting state, computed here so the page is never a set of empty
    # boxes for the instant before the wiring runs ──
    start = {k: float(c["start"]) for k, c in by_key.items()}
    weight = start["load"] * g
    values = {"weight": weight, "force": weight * start["hand"] / start["ins"]}

    def readout(key, fmt):
        if key in _LEVER_COMPUTED:
            return _lever_num(values[key], _LEVER_COMPUTED[key], fmt)
        return _lever_num(start[key], decimals[key], fmt)

    rows = []
    for c in controls:
        key = c["key"]
        cid = "%s-%s" % (act_id, key)
        if c.get("options"):
            tabs = "".join(
                '<button type="button" class="ks3-sim-seg-btn ks3-lever-tab" '
                'data-lever-tab="%s" data-value="%s" aria-pressed="%s">%s'
                '</button>'
                % (e(key), e(o), "true" if float(o) == start[key] else "false",
                   t(_lever_num(o, decimals[key], c.get("format"))))
                for o in c["options"])
            rows.append('<div class="ks3-lever-control">'
                        '<p class="ks3-lever-label">%s</p>'
                        '<div class="ks3-lever-tabs">%s</div></div>'
                        % (t(c.get("label", "")), tabs))
            continue
        # ⚠️ The <label> is real and its `for` reaches a real id. A slider
        # whose only name is the paragraph above it is unnamed to a screen
        # reader, and this one is the difference between two distances.
        rows.append(
            '<div class="ks3-lever-control">'
            '<div class="ks3-lever-row">'
            '<label class="ks3-lever-label" for="%s">%s</label>'
            '<p class="ks3-lever-value" data-lever-value="%s" '
            'data-format="%s">%s</p></div>'
            '<input class="ks3-slider ks3-lever-slider" type="range" id="%s" '
            'min="%s" max="%s" step="%s" value="%s" data-lever-input="%s">'
            '</div>'
            % (e(cid), t(c.get("label", "")), e(key),
               e(c.get("format") or "{n}"),
               t(readout(key, c.get("format"))), e(cid),
               e(c["min"]), e(c["max"]), e(c["step"]), e(c["start"]), e(key)))

    cells = []
    for tl in tiles:
        key = tl["key"]
        # The force tile opens on the withheld sentence, not on a number.
        value = (a["unmeasured"] if key == "force"
                 else readout(key, tl.get("format")))
        cells.append('<div class="ks3-lever-tile">'
                     '<p class="ks3-lever-tile-label">%s</p>'
                     '<p class="ks3-lever-tile-value%s" data-lever-out="%s" '
                     'data-format="%s">%s</p></div>'
                     % (t(tl.get("label", "")),
                        " ks3-lever-tile-mono" if tl.get("mono") else "",
                        e(key), e(tl.get("format") or "{n}"), t(value)))

    gate_html, hide = r_bench_gate(a.get("gate"))

    return (gate_html
            + '<div class="ks3-lever" data-lever%s data-rig="%s" data-g="%s" '
              'data-done-at="%d" data-load="%s" data-ins="%s" data-hand="%s" '
              'data-dp-load="%d" data-dp-ins="%d" data-dp-hand="%d" '
              'data-unmeasured="%s" data-alt="%s" data-alt-measured="%s" '
              'data-canvas-title="%s" data-canvas-joint="%s" '
              'data-canvas-muscle="%s" data-canvas-load="%s" '
              'data-meter-label="%s" data-meter-done="%s" '
              'data-meter-note="%s" data-meter-note-done="%s">'
              '<div class="ks3-lever-controls">%s</div>'
              '<div class="ks3-lever-stage">'
              '<canvas class="ks3-lever-canvas" width="1800" height="700" '
              'role="img" aria-label="%s" data-lever-canvas></canvas></div>'
              '<div class="ks3-lever-tiles">%s</div>'
              '<div class="ks3-lever-foot">'
              '<button type="button" class="ks3-sim-seg-btn ks3-lever-meter" '
              'data-lever-meter>%s</button>'
              '<p class="ks3-lever-note" data-lever-note role="status">%s</p>'
              '</div></div>'
            % (hide, e(act_id), e(a["g"]), done_at,
               e(start["load"]), e(start["ins"]), e(start["hand"]),
               decimals["load"], decimals["ins"], decimals["hand"],
               e(a["unmeasured"]), e(alt.get("template", "")),
               e(alt.get("measured", "")),
               e(canvas["title"]), e(canvas["joint"]), e(canvas["muscle"]),
               e(canvas["load"]),
               e(meter["label"]), e(meter["label_done"]),
               e(meter["note"]), e(meter["note_done"]),
               "".join(rows),
               e(_lever_alt(alt,
                            _lever_num(start["load"], decimals["load"], "{n}"),
                            _lever_num(start["ins"], decimals["ins"], "{n}"),
                            _lever_num(start["hand"], decimals["hand"], "{n}"))),
               "".join(cells),
               t(meter["label"]), t(meter["note"])))
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


# ── registrations ────────────────────────────────────────────────────────
KIND_SHELL = {
    'job-sort': ("ks3-jobsort-block",
                      ' data-instrument data-jobsort-block data-stage-done="0"'),
    'system-switch': ("ks3-switch-block",
                      ' data-instrument data-switchblock data-stage-done="0"'),
    'joint-bench': ("ks3-joint-block",
                      ' data-instrument data-jointblock data-stage-done="0"'),
    'muscle-pair': ("ks3-muscle-block",
                      ' data-instrument data-muscleblock data-stage-done="0"'),
    'arm-lever': ("ks3-lever-block", ' data-instrument data-leverblock data-stage-done="0"'),
    'lever-steps': ("ks3-lstep-block", ' data-instrument data-lstepblock data-stage-done="0"'),
    'meter-compare': ("ks3-meters-block", ' data-instrument data-metersblock data-stage-done="0"'),
}

KIND_FN = {
    'job-sort': r_job_sort,
    'system-switch': r_system_switch,
    'joint-bench': r_joint_bench,
    'muscle-pair': r_muscle_pair,
    'arm-lever': r_arm_lever,
    'lever-steps': r_lever_steps,
    'meter-compare': r_meter_compare,
}
