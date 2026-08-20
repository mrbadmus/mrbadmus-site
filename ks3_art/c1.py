"""ks3_art.c1 — C1's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import html
import json
import math
import re
from ks3_art.kit import (
    _canvas_frame,
    _option_li,
    e,
    r_activity_options,
    r_bench_gate,
    rich,
    t,
)


# ⊕ The activity-kind dispatch table, as a module-level constant.
#
# It is a constant rather than a dict literal inside `r_activity` so that
# `verify_ks3.py` can read the REAL table and report every authored kind that
# has no entry. That gate exists because MRB-203's registry works one level
# above this one: it asks whether a BLOCK TYPE has a registered component, and
# cannot see that an activity KIND it does not know falls through to the
# generic prompt/options/reveal shell — which renders, validates, and passes
# every gate while being the wrong component.
#
# That is not hypothetical. It is what Mide rejected on 11 August: B1-06's task
# is "name the level for each of these eight and say what settled it" and it
# rendered as a four-option multiple choice with eight items in the prompt.
#
#   kind -> (modifier class, marker attributes)
#
# The class is what the stylesheet hangs the instrument on; the attribute is
# what shared/ks3.js dispatches on, and it also tells `wirePredictions` to keep
# its hands off — an instrument owns every option inside it.
#
# ⊕ The attribute string carries `data-stage-done="0"` for an instrument that
# HAS a completion contract, and omits it for one that does not. It used to be
# appended automatically to every entry, which was right while both entries
# were tasks and wrong the moment an expository kind joined them: `#s-think` is
# a rail stop on none of the six lessons, because MRB-208 ruled the rail
# carries "only sections that require the student to do something", and a
# confrontation asks for nothing. Emitting the attribute anyway would declare a
# completion contract the section can never discharge.
#
# ⊕ Every entry also carries `data-instrument`. That is what tells
# `wirePredictions` to keep its hands off, and until 14 Aug 2026 the comment
# here claimed it did while **no such check existed in `shared/ks3.js`**. The
# consequence was live and exactly what this comment predicted: the generic
# Law 4 wiring selects every `.ks3-option` in the section and the FIRST
# `[data-reveal]` it finds, so on the board it would have wired all four
# specimen panels' predictions together and unhidden specimen one's verdict
# panel on any of them. An instrument owns every option inside it.
# renderers: ═══ BEGIN C1 ═══
# DISPATCH: "collision-counter": ("ks3-counter-block", ' data-instrument data-counterblock data-stage-done="0"'),
#
# Splice point: `ACTIVITY_KIND_RENDERERS` in build_ks3.py, in the new
# "C1 · Particles and their behaviour" section. Also add to `r_activity`:
#
#     if kind == "collision-counter":
#         parts.append(r_collision_counter(a, act_id))
#
# The function below belongs beside the other C1 renderers. It uses `e`, `t`,
# `r_bench_gate` and `json`, all of which build_ks3.py already imports/defines.


# The three control groups, as (payload key, value key, caption key, css/data
# name). One table rather than three near-identical blocks, because the ONLY
# thing that differs between them is which authored list they read — and a
# fourth group would otherwise arrive as a fourth copy of the same markup.
#
# ⊕ MRB-254 (carrying MRB-257) — the middle row's value key is `volume`, and it
# was `scale`. The dial is a VOLUME factor now, not a linear one, so that the
# label, the drawing and the physics state one ratio instead of three; see the
# note beside `VOLS` in `ks3_data/c1/lesson_04_gas_pressure.py`.
#
# ⚠️ THIS LINE IS WHY THE RENAME IS SAFE TO MAKE, and it is also the line that
# caught it being made incompletely: the value key is used for one thing, a
# presence check in the validator below, and the row dict is serialised whole
# into the payload. So renaming the field in the record without renaming it
# here does not produce a wrong drawing — it fails the build outright, on every
# page, with "every vols entry needs `label` and `scale`". Which it did.
_COUNTER_GROUPS = (
    ("temps", "speed_multiplier", "temperature", "temp"),
    ("vols", "volume", "volume", "vol"),
    ("counts", "n", "particles", "count"),
)
def _counter_alt(alt, temps, vols, counts, temp, vol, count, hits, kpa_per_hit=7,
                 unit="kPa"):
    """The bench canvas's aria-label. Same composition in Python and in JS.

    ⊕ CORRECTION (PAYLOAD-MAP §4.6). Design's label (page 705–706) names the
    temperature, the container and the particle count and stops — it does not
    say how many wall hits there were, which is the one number the lesson is
    about and the one a sighted student is reading in 58px type. Every readout
    on this bench is drawn INSIDE the canvas, so `aria-label` is the only route
    to any of it. Design's sentence is carried byte-identical and the count is
    added as a second sentence after it.
    """
    k = hits * kpa_per_hit
    return (alt.get("template", "")
            .replace("{temp}", (temps[temp].get("label") or "").lower())
            .replace("{vol}", (vols[vol].get("label") or "").lower())
            .replace("{n}", str(counts[count].get("n", "")))
            .replace("{hits}", str(hits))
            # Same rounding rule as `draw()`: whole kilopascals, one decimal
            # below 10. The static label is written with hits = 0, which is
            # honest — the gas has not started moving when the page is built.
            .replace("{kpa}", ("%.1f" % k if k < 10 else "%d" % round(k))
                     + " " + unit))
def r_collision_counter(a, act_id):
    """⊕ c1-04 `#s-bench` — a real count of collisions with the wall.

    ⚠️ A LIGHT `.ks3-block`, not a practical. Page line 109 carries no
    `ks3-dark`, and the canvas draws its own cream box: on ink the drawing
    would sit in a black surround and every text token in the control strip
    would resolve to its on-dark value.

    ⚖️ THE BUMPS TOGGLE IS PART-08's ENTIRE CONFRONTATION. The wrong idea is
    "pressure is the particles pushing against each other", and this is the one
    instrument in the key stage that draws those pushes — grey rings, dozens of
    them, in the middle of the box — and then does not count a single one. Drop
    the toggle and the lesson is a picture of a gas with a number over it.

    ⚖️ THE COUNTING IS REAL. `step()` pushes a timestamp on every wall bounce
    and shifts entries older than `window_ms`, so the number is an actual count
    of the last second rather than a formula evaluated for effect. That is what
    makes "smaller box, same particles, same speed, and the count is up"
    something a student watches rather than something the page claims.

    ⊕ SUPERSEDES NOTES flag 6 (Mide, 19 Aug 2026). The flag said pressure is
    "a COUNT and a BAR, never a pascal", and what shipped was a `PRESSURE`
    caption over an unlabelled bar — a dial with no value on it, teaching
    nothing quantitative about the one quantity the lesson is for. Pressure is
    now drawn as a NUMBER in kilopascals beside the bar, which stays.

    ⚖️ The number is a STATED CALIBRATION, not a calculation from first
    principles: twelve particles in a box have no meaningful pressure, and a
    literal figure would be ~10⁻²³ kPa, which is a lie wearing rigour. The
    bench models a SAMPLE of a real gas, so `kpa_per_hit` anchors the resting
    setting (warm, large, 24 particles → 14.4 hits/s) at ~101 kPa. Pressure is
    then EXACTLY linear in the hit rate at every one of the 27 control
    combinations, because it is `hits × kpa_per_hit` and nothing else — and
    that proportionality is the lesson. A reading that drifted from the count
    would teach the opposite of it.

    ⊕ Two corrections, both reported: the aria-label gains the wall-hit count
    (see `_counter_alt`), and the rail's "controls tried" predicate is a SET of
    three distinct groups rather than Design's `Math.max(touched, N)`, which
    ticks on the particle-count button alone.
    """
    labels = a.get("labels") or {}
    bumps = a.get("bumps") or {}
    canvas_labels = a.get("canvas_labels") or {}
    notes = a.get("notes") or {}
    alt = a.get("alt") or {}
    start = a.get("start") or {}
    hc = a.get("head_counter") or {}

    groups = {}
    for key, value_key, caption_key, _name in _COUNTER_GROUPS:
        rows = a.get(key) or []
        if len(rows) != 3:
            raise ValueError(
                "collision-counter %r needs exactly three %s; got %d. Design "
                "draws three three-way segmented groups and the grid is built "
                "for them." % (act_id, key, len(rows)))
        for row in rows:
            if not row.get("label") or row.get(value_key) is None:
                raise ValueError(
                    "collision-counter %r: every %s entry needs `label` and "
                    "%r; got %r." % (act_id, key, value_key, row))
        if not labels.get(caption_key):
            raise ValueError(
                "collision-counter %r has no `labels.%s` caption. A group with "
                "no caption is three buttons a student cannot name."
                % (act_id, caption_key))
        groups[key] = rows

    # The six authored branches, and all six must be present: the note is the
    # sentence that says what just happened, and a missing branch is a silent
    # empty panel at exactly the setting a student went looking for.
    for branch in ("bumps", "smaller_box", "hot", "cold", "more_particles",
                   "resting"):
        if not notes.get(branch):
            raise ValueError(
                "collision-counter %r has no `notes.%s`. Design authors six "
                "branches (page 631–644) and the renderer emits all six."
                % (act_id, branch))

    for field in ("on_label", "off_label", "caption"):
        if not bumps.get(field):
            raise ValueError(
                "collision-counter %r has no `bumps.%s`. The bumps toggle is "
                "PART-08's confrontation and cannot ship unlabelled."
                % (act_id, field))

    # ⊕ `{kpa}` joins the list for exactly the reason `{hits}` is in it: the
    # pressure number is drawn INSIDE the canvas like every other readout, so
    # a label without it shows the ruled figure to sighted students only.
    for token in ("{temp}", "{vol}", "{n}", "{hits}", "{kpa}"):
        if token not in (alt.get("template") or ""):
            raise ValueError(
                "collision-counter %r: `alt.template` is missing %s. Every "
                "readout is drawn inside the canvas, so the label is the only "
                "thing a screen reader gets." % (act_id, token))

    temp0 = int(start.get("temp", 1))
    vol0 = int(start.get("vol", 0))
    count0 = int(start.get("count", 1))

    gate_html, hide = r_bench_gate(a.get("gate"))

    # ── the three segmented groups ──
    # `.ks3-sim-seg-btn` deliberately, not a private control: drift 4 ruled ONE
    # segmented control for the key stage, and a second copy at Design's 16px
    # is exactly the drift the ruling exists to stop.
    group_html = []
    for key, _value_key, caption_key, name in _COUNTER_GROUPS:
        chosen = {"temps": temp0, "vols": vol0, "counts": count0}[key]
        btns = "".join(
            '<button type="button" class="ks3-sim-seg-btn ks3-counter-btn" '
            'data-group="%s" data-i="%d" aria-pressed="%s">%s</button>'
            % (e(name), i, "true" if i == chosen else "false",
               t(row.get("label", "")))
            for i, row in enumerate(groups[key]))
        group_html.append(
            '<div class="ks3-counter-group">'
            '<p class="ks3-counter-grouplabel">%s</p>'
            '<div class="ks3-counter-btns">%s</div></div>'
            % (t(labels[caption_key]), btns))

    # ── the bumps toggle ──
    # Emit-both-show-one rather than a textContent swap out of two attributes:
    # no student-facing string is ever rebuilt in JS, and the label survives
    # whatever punctuation an author puts in it.
    # `on_label` is the label that turns the rings ON ("Show …"), so it is the
    # one visible while they are off. The attribute names follow the WORDS, not
    # the state, because that is what stops the two getting swapped.
    bump_btn = ('<button type="button" class="ks3-sim-seg-btn '
                'ks3-counter-bumpbtn" data-counter-bumps aria-pressed="false">'
                '<span data-bump-show>%s</span>'
                '<span data-bump-hide hidden>%s</span></button>'
                % (t(bumps["on_label"]), t(bumps["off_label"])))

    # ── the six notes, one shown ──
    # One live region holding six paragraphs, five hidden. The wrapper carries
    # `role="status"`, never the instrument root.
    note_html = "".join(
        '<p class="ks3-counter-note" data-note="%s"%s>%s</p>'
        % (e(branch), "" if branch == "resting" else " hidden",
           t(notes[branch]))
        for branch in ("bumps", "smaller_box", "hot", "cold", "more_particles",
                       "resting"))

    cfg = {
        "temps": groups["temps"],
        "vols": groups["vols"],
        "counts": groups["counts"],
        "start": {"temp": temp0, "vol": vol0, "count": count0},
        "bump_threshold": bumps.get("threshold", 0.0022),
        "canvas_labels": canvas_labels,
        "pressure_full": a.get("pressure_full", 170),
        # ⊕ RULING (Mide, 19 Aug 2026). Kilopascals per wall hit per second.
        # See the docstring above and `draw()` in shared/ks3.js: the resting
        # bench runs at 14.4 hits/s, so 7 puts it at ~101 kPa — atmospheric.
        "kpa_per_hit": a.get("kpa_per_hit", 7),
        "window_ms": a.get("window_ms", 1000),
        "flash_ms": a.get("flash_ms", 420),
        # ⊕ RULING (Mide, 19 Aug 2026). How much simulation one displayed
        # reading averages over, and how often the display may change. The
        # raw count churned every frame; a number a student cannot read
        # cannot show them which way it moved, and the direction of the
        # move is the lesson. `hits × kpa_per_hit` is exact on the pair
        # actually drawn, so the proportionality is unaffected.
        "smooth_ms": a.get("smooth_ms", 900),
        "readout_ms": a.get("readout_ms", 500),
        "reduced_motion_scale": a.get("reduced_motion_scale", 0.35),
        "step_per_frame": a.get("step_per_frame", 0.0075),
        "alt": alt,
    }

    return (gate_html
            + '<div class="ks3-counter" data-counter%s data-total="3" '
              'data-full-label="%s" data-cfg="%s">'
              '<div class="ks3-counter-stage">'
              '<canvas class="ks3-counter-canvas" width="1800" height="680" '
              'role="img" aria-label="%s" data-counter-canvas></canvas>'
              '<div class="ks3-counter-controls">'
              '<div class="ks3-counter-groups">%s</div>'
              '<div class="ks3-counter-bumps">%s'
              '<p class="ks3-counter-bumpnote">%s</p></div>'
              '</div></div>'
              '<div class="ks3-counter-notes" data-counter-notes '
              'role="status">%s</div></div>'
            % (hide,
               # Design's terminal label for the head counter (page 691).
               # `_head_counter` has `zero` but no `full`, so the string is
               # carried here and `wireCollisionCounter` writes it on the
               # counter element the shared updater owns — one element, one
               # place, one authored copy of each of the two strings.
               e(hc.get("full") or ""),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(_counter_alt(alt, groups["temps"], groups["vols"],
                              groups["counts"], temp0, vol0, count0, 0,
                              a.get("kpa_per_hit", 7),
                              canvas_labels.get("pressure_unit") or "kPa")),
               "".join(group_html), bump_btn, t(bumps["caption"]),
               note_html))
# DISPATCH: "evidence-bench": ("ks3-ebench-block", ' data-instrument data-ebenchblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "evidence-bench":
#         parts.append(r_evidence_bench(a, act_id))
#
# Place the function next to `r_claim_switch`. It needs `e`, `t`, `rich` only —
# no gate helper, because this instrument has none (see the docstring).


def r_evidence_bench(a, act_id):
    """⊕ c1-06 `#s-bench` — seven observations, judged one at a time.

    ⚠️ A LIGHT `.ks3-block`, and **NO GATE**. This is the only flagship
    instrument in C1 that is open from the start, and that is deliberate rather
    than an omission: the seven judgements ARE the commitment, so a fourth
    option in front of them would ask the student to commit to committing.
    `r_bench_gate` is not called and must not be added.

    The nearest shipped kinds are `test-board` and `removal-cases`, and both are
    the wrong shape. This is seven BINARY judgements, each with one authored
    verdict on a two-tone panel, plus a whole-set tally that reports how many
    the student called correctly **before** the verdicts opened. Nothing else in
    the key stage scores a call made before a reveal.

    ⚖️ THE TALLY SCORES THE FIRST CALL, NOT THE CURRENT ONE. Design recomputes
    it from live state (`rightCalls`, page line 488), so a student who flips an
    answer after reading the verdict raises a number whose own sentence says
    "before opening the verdict". The buttons stay live — Design leaves them
    live and the verdict does not change when they are pressed again — but the
    scored call is latched on the first press, in `data-called`. That is the
    smallest change that makes the drawn sentence true.

    ⚠️ R3 / MRB-196 R10 — NOTHING HERE MARKS THE STUDENT. The chosen button
    takes the ordinary chosen treatment, the case's border goes to ink, and the
    verdict panel's two grounds are a fact about THE MODEL (`ok`), not about the
    answer. A student who called every one wrong sees exactly the same panels.

    ⚠️ `benchProgress` has two shapes (page line 544): the running count, which
    is `head_counter`'s job, and a bespoke label once the set closes.
    `_head_counter` has no "full" branch, so `progress_all` rides on the
    instrument root and `wireEvidenceBench` writes it into the block-head
    counter. The alternative was retyping "all seven judged" into the engine.
    """
    cases = a.get("cases") or []
    if not cases:
        raise ValueError("evidence-bench %r declares no cases[]." % act_id)

    buttons = a.get("buttons") or {}
    if not (buttons.get("yes") and buttons.get("no")):
        raise ValueError(
            "evidence-bench %r needs buttons={'yes': …, 'no': …}; both labels "
            "are authored and neither has a default worth guessing." % act_id)

    labels = a.get("verdict_labels") or {}
    if not (labels.get("ok") and labels.get("fail")):
        raise ValueError(
            "evidence-bench %r needs verdict_labels={'ok': …, 'fail': …} — the "
            "pair the panel prints above each authored verdict." % act_id)

    tally = a.get("tally") or ""
    if "{n}" not in tally:
        raise ValueError(
            "evidence-bench %r tally carries no {n}: it is the one live number "
            "in the block and the sentence is meaningless without it." % act_id)

    for c in cases:
        if not c.get("id"):
            raise ValueError("evidence-bench %r has a case with no id." % act_id)
        if "ok" not in c:
            raise ValueError(
                "evidence-bench %r case %r declares no `ok`. It decides which "
                "verdict label and which of the two panel grounds the case "
                "takes, and there is no safe default."
                % (act_id, c.get("id")))
        if not c.get("verdict"):
            raise ValueError(
                "evidence-bench %r case %r has no verdict; the panel would open "
                "empty." % (act_id, c.get("id")))

    rows = []
    for c in cases:
        ok = bool(c["ok"])
        rows.append(
            '<div class="ks3-ebench-case" data-case="%s" data-ok="%s">'
            '<div class="ks3-ebench-row">'
            '<div class="ks3-ebench-what">'
            '<p class="ks3-ebench-tag">%s</p>'
            '<p class="ks3-ebench-text">%s</p></div>'
            '<div class="ks3-ebench-btns">'
            '<button type="button" class="ks3-ebench-btn" data-call="1" '
            'aria-pressed="false">%s</button>'
            '<button type="button" class="ks3-ebench-btn" data-call="0" '
            'aria-pressed="false">%s</button>'
            '</div></div>'
            # The verdict is in the document from the start and hidden, not
            # built on demand: the authored sentence carries an em dash and a
            # right single quote, and nothing science-bearing is ever assembled
            # in JS.
            '<div class="ks3-ebench-verdict" hidden data-reveal>'
            '<p class="ks3-ebench-vlabel">%s</p>'
            '<p class="ks3-ebench-vtext">%s</p></div></div>'
            % (e(c["id"]), "1" if ok else "0",
               t(c.get("tag", "")), rich(c.get("text", "")),
               t(buttons["yes"]), t(buttons["no"]),
               t(labels["ok"] if ok else labels["fail"]),
               rich(c["verdict"])))

    # ⚠️ The shared-cause paragraph is STATIC MARKUP, not the tally. NOTES §3
    # flag 9 says "the tally text says so" and it is wrong: the tally is the
    # count line, and the claim the whole C1 → C2 bridge rests on is this
    # paragraph — which is why it is authored prose with an <em> in it and
    # never touched by JS.
    cause = ('<p class="ks3-ebench-cause">%s</p>' % rich(a["shared_cause"])
             if a.get("shared_cause") else "")

    return ('<div class="ks3-ebench" data-ebench data-total="%d" '
            'data-tally="%s" data-all="%s">'
            '<div class="ks3-ebench-list">%s</div>'
            '<div class="ks3-ebench-tally" hidden data-ebench-tally>'
            '<p class="ks3-ebench-tallyline" data-tallyline role="status"></p>'
            '%s</div></div>'
            % (len(cases), e(tally), e(a.get("progress_all") or ""),
               "".join(rows), cause))
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
# DISPATCH: "halving-bench": ("ks3-cut-block", ' data-instrument data-cutblock data-stage-done="0"'),
#
# Splice `r_halving_bench` into build_ks3.py beside the other instrument
# renderers, add the dispatch row above to ACTIVITY_KIND_RENDERERS, and add
#     if kind == "halving-bench":
#         parts.append(r_halving_bench(a, act_id))
# to r_activity's dispatch run. `_sig` and `_size_label` are module-level
# because the RESTING render needs the same ladder the runtime uses, and two
# copies of a formatter are two answers to "how big is the piece now".

# No new imports: `build_ks3.py` does not import `math`, and the one place
# this needed it (`math.floor(v + .5)`) is `int(v + .5)` for a positive v,
# which every value on this ladder is.


# ── the size ladder (c1-01 page lines 452–464) ───────────────────────────
#
# Engine, not payload (map §1.2): 1 cm / 2ⁿ, formatted mm above 0.1 cm, µm
# above 1e-4 cm, nm below that. It is here in Python AND in `shared/ks3.js`
# for the same reason `_scale_alt` is — the build has to render the resting
# readout and the resting aria-label, and the runtime has to render every
# other state. Same composition, same output, checked at n = 0 and n = FLOOR.
#
# ⚠️ µ is U+00B5 MICRO SIGN, which Bricolage and DM Mono carry and Instrument
# Sans does not. The value lands in the DISPLAY face (`.ks3-cut-value`) and on
# the canvas in mono, so it is covered; a µ in body copy would not be.

def _sig(v):
    """Design's `sig()`, digit for digit — including the one trailing zero.

    ⚠️ `int(v + .5)`, not `round()`. JS `Math.round(312.5)` is 313 and Python's
    `round(312.5)` is 312, and 312.5 µm is a real value on this ladder (five
    cuts in). Banker's rounding here would print a different number in the built
    page from the one the student sees after the first click.
    """
    if v >= 100:
        return str(int(v + 0.5))
    if v >= 10:
        out = "%.1f" % v
        return out[:-2] if out.endswith(".0") else out
    # Design strips ONE trailing zero, then a bare point: 0.60 → 0.6, and
    # 5.00 → 5.0. Reproduced rather than tidied — the ladder's output is
    # printed on the page and in Rung 2's premise.
    out = "%.2f" % v
    if out.endswith("0"):
        out = out[:-1]
    return out[:-1] if out.endswith(".") else out
def _size_label(n, start_cm=1):
    cm = float(start_cm) / (2 ** n)
    if cm >= 0.1:
        return _sig(cm * 10) + " mm"
    if cm >= 1e-4:
        return _sig(cm * 1e4) + " µm"
    return _sig(cm * 1e7) + " nm"
_CUT_SOURCES = {"count", "size", "verdict"}
_CUT_ACTIONS = {"cut", "undo"}
_CUT_DISABLED = {"at_floor", "at_start"}
_CUT_NOTES = ("at_floor", "near_floor", "at_start", "mid")
def r_halving_bench(a, act_id):
    """⊕ c1-01 `#s-cut` — halve a sugar cube until halving runs out.

    ⚖️ THE NUMBERS ARE THE LESSON, NOT THE PICTURE. The lede says so
    ("watch the size, not the picture") and the instrument is built that way:
    three readouts, a scale bar and a progress strip, and a drawing that stays
    deliberately dull until four cuts from the floor. An instrument that made
    the cube prettier every click would teach that small is interesting; this
    one teaches that halving TERMINATES, which is a different claim and the one
    the unit rests on.

    ⊕ SUPERSEDED BY MIDE, 19 Aug 2026, and kept because it records what was
    believed. The flag is right that decoration is not evidence — and what it
    produced was a drawing pinned at 176px for all 24 cuts, so a student cut
    five times and watched a NUMBER fall beside a PICTURE that did not move.
    That is not a dull drawing, it is a drawing contradicting the readout
    beside it, and the claim the unit rests on was left to a caption. The rule
    now is Mide's: what matters is that a student sees the science happen. The
    piece halves visibly at every cut; the view rescales in stages and says so;
    the lede was reworded, because it was telling students to ignore the one
    thing that now shows them the answer. Nothing was made prettier — the same
    box, the same ghost, the same ruler, at an honest size.

    ⚖️ THE FLOOR IS STICKY. `reachedFloor` is a one-way flag on Design's page
    and it stays one-way here: undoing a cut walks the piece back up the ladder
    and does NOT untick the rail. What a student found out at 24 cuts cannot be
    un-found by pressing undo, and MRB-208's rail records participation.

    ⚠️ A LIGHT `check` block. Measured off Design's markup (`ks3-block`, no
    `ks3-dark`), and the sibling on the same page — `#s-gap` — IS ink-dark, so
    the two are a deliberate pair rather than an oversight.

    ⊕ Additions inside the drawn component, both stated in the report:
      * `progress_full` — Design's head counter reads `floor reached` at the
        floor, which `_head_counter`'s format/zero/two-state shapes cannot
        express. Carried on the instrument and swapped in by `wireHalvingBench`.
      * `start_cm` / `grain_at` — Design hard-codes `1 /` and `FLOOR - 4` in
        two functions each. Authored once, read here and in the JS.

    ⚠️ The canvas labels ARE assembled from attributes, which the DOM rule
    forbids. Canvas text is not a DOM node: there is no element to hide and no
    `<em>` to lose, and `fillText` takes a string or nothing. Every DOM-borne
    string in this instrument — the four notes and the two verdict words — is
    emit-both-show-one instead.
    """
    floor = int(a.get("floor") or 0)
    if floor < 1:
        raise ValueError(
            "halving-bench %r declares floor %r; the bench counts down to a "
            "floor and needs a positive one." % (act_id, a.get("floor")))

    readouts = a.get("readouts") or []
    if not readouts:
        raise ValueError("halving-bench %r declares no readouts[]." % act_id)
    for r in readouts:
        if r.get("source") not in _CUT_SOURCES:
            raise ValueError(
                "halving-bench %r readout %r names source %r; the drawn set is "
                "%s." % (act_id, r.get("label"), r.get("source"),
                         ", ".join(sorted(_CUT_SOURCES))))

    buttons = a.get("buttons") or []
    if not buttons:
        raise ValueError("halving-bench %r declares no buttons[]." % act_id)
    for b in buttons:
        if b.get("action") not in _CUT_ACTIONS:
            raise ValueError(
                "halving-bench %r button %r names action %r; the bench does %s."
                % (act_id, b.get("label"), b.get("action"),
                   " and ".join(sorted(_CUT_ACTIONS))))
        if b.get("disabled_when") not in _CUT_DISABLED:
            raise ValueError(
                "halving-bench %r button %r disables on %r; the two ends are "
                "%s." % (act_id, b.get("label"), b.get("disabled_when"),
                         ", ".join(sorted(_CUT_DISABLED))))
        if int(b.get("step") or 0) < 1:
            raise ValueError(
                "halving-bench %r button %r takes step %r; a control that moves "
                "nothing is a control a student presses twice."
                % (act_id, b.get("label"), b.get("step")))

    notes = a.get("notes") or {}
    missing = [k for k in _CUT_NOTES if not notes.get(k)]
    if missing:
        raise ValueError(
            "halving-bench %r is missing note branch(es) %s. All four are "
            "authored — the floor, the grain, the untouched cube and the long "
            "middle — and a missing one would leave the student reading the "
            "previous state's sentence." % (act_id, ", ".join(missing)))

    verdict = a.get("verdict") or {}
    if not (verdict.get("open") and verdict.get("floor")):
        raise ValueError(
            "halving-bench %r needs both verdict words (open and floor)."
            % act_id)

    # ⚠️ The grain threshold squares: the drawing lays out 2^grain across and
    # 4^grain circles in total. Design's 4 gives 16 across and 256 circles, and
    # 6 is already 4,096. Bounded here rather than discovered as a frozen tab.
    grain = int(a.get("grain_at") or 0)
    if not 1 <= grain <= 6:
        raise ValueError(
            "halving-bench %r sets grain_at %r; it must be 1–6, because the "
            "drawing paints 4^grain particles (Design's 4 is 256)."
            % (act_id, a.get("grain_at")))

    alt = a.get("alt") or {}
    for key in ("template", "smooth", "grainy"):
        if not alt.get(key):
            raise ValueError(
                "halving-bench %r alt is missing %r; the readouts are in the "
                "DOM but the piece, the scale bar and the progress strip are "
                "only on the canvas, so this label is the whole drawing for a "
                "screen reader." % (act_id, key))

    labels = a.get("canvas_labels") or {}
    # ⊕ `zoom` joins the required set (Mide, 19 Aug 2026). It is the only
    # thing the instrument says when the view rescales, and a bench that
    # rescaled without saying so is the defect the ruling removes — so a
    # payload that forgets it should fail the build, not ship silently.
    for key in ("ghost", "one", "many", "start", "end", "zoom"):
        if not labels.get(key):
            raise ValueError(
                "halving-bench %r canvas_labels is missing %r." % (act_id, key))

    start_cm = a.get("start_cm") or 1
    gate_html, hide = r_bench_gate(a.get("gate"))

    # ── the resting state: nothing cut ──
    size0 = _size_label(0, start_cm)
    alt0 = (alt["template"].replace("{n}", "0").replace("{size}", size0)
            .replace("{tail}", alt["grainy"] if 0 >= floor - grain
                     else alt["smooth"]))

    cells = []
    for r in readouts:
        src = r["source"]
        if src == "verdict":
            # Both words in the document, one hidden. The floor word is the one
            # the stylesheet paints in accent-text, so the state is never a
            # colour JS applied.
            value = ('<span data-verdict="open">%s</span>'
                     '<span data-verdict="floor" hidden>%s</span>'
                     % (t(verdict["open"]), t(verdict["floor"])))
        elif src == "size":
            value = t(size0)
        else:
            value = "0"
        cells.append('<div class="ks3-cut-cell">'
                     '<p class="ks3-cut-label">%s</p>'
                     '<p class="ks3-cut-value" data-cut-out="%s">%s</p></div>'
                     % (t(r.get("label", "")), e(src), value))

    btns = []
    for b in buttons:
        # The resting page is at zero cuts, so an at_start control is already
        # spent and says so in the markup rather than waiting for JS.
        off = " disabled" if b["disabled_when"] == "at_start" else ""
        btns.append('<button type="button" class="ks3-sim-seg-btn ks3-cut-btn" '
                    'data-act="%s" data-step="%d" data-dis="%s"%s>%s</button>'
                    % (e(b["action"]), int(b["step"]), e(b["disabled_when"]),
                       off, t(b.get("label", ""))))

    note_ps = "".join(
        '<p data-note="%s"%s>%s</p>'
        % (e(k), "" if k == "at_start" else " hidden", rich(notes[k]))
        for k in _CUT_NOTES)

    # ⊕ 640 → 760 (Mide, 19 Aug 2026). The piece is drawn at up to 240px now
    # instead of a pinned 176, and the ruler under it — the one element that
    # always states the true edge length — fell off the bottom of a 320-tall
    # design space at the largest stage. The drawing gained 60 design px of
    # headroom rather than the ruler being moved out from under the piece.
    canvas = ('<canvas class="ks3-cut-canvas" width="1800" height="760" '
              'role="img" aria-label="%s" data-cut-canvas></canvas>' % e(alt0))

    return (gate_html
            + '<div class="ks3-cut" data-cut%s data-floor="%d" '
              'data-start-cm="%s" data-grain="%d" data-full="%s" '
              'data-alt="%s" data-alt-smooth="%s" data-alt-grainy="%s" '
              'data-label-ghost="%s" data-label-one="%s" data-label-many="%s" '
              'data-label-start="%s" data-label-end="%s" '
              'data-label-zoom="%s">'
              '<div class="ks3-cut-frame">%s'
              '<div class="ks3-cut-foot">'
              '<div class="ks3-cut-readouts">%s</div>'
              '<div class="ks3-cut-btns">%s</div></div></div>'
              '<div class="ks3-cut-note" data-cut-note role="status">%s</div>'
              '</div>'
            % (hide, floor, e(start_cm), grain,
               e(a.get("progress_full") or ""),
               e(alt["template"]), e(alt["smooth"]), e(alt["grainy"]),
               e(labels["ghost"]), e(labels["one"]), e(labels["many"]),
               e(labels["start"]),
               e(labels["end"].replace("{floor}", str(floor))),
               e(labels["zoom"]),
               canvas, "".join(cells), "".join(btns), note_ps))
# DISPATCH: "heating-bench": ("ks3-hb-block", ' data-instrument data-hbblock data-stage-done="0"'),
#
# Splice into build_ks3.py beside the other C1 instruments, plus the dispatch
# line in `r_activity`:
#
#     if kind == "heating-bench":
#         parts.append(r_heating_bench(a, act_id))
#
# ⚠️ It must also be added to ks3_parity.COMPONENTS (see heating-bench.parity.py)
# and reached from `wireInstruments()` (see heating-bench.js).


# The two tones Design paints the phase word in: ordinary ink for a state that
# is simply warming, accent-text for a state that is changing. A closed map
# rather than an interpolated var() call, so a typo is a build error and never
# a `color: var(--ks3-taupe)` that resolves to nothing — same discipline as
# `_GROUNDS`.
_HB_TONES = {"ink", "accent"}
# The design-space canvas, doubled into the backing store. 900 × 330 is
# Design's own frame (c1-03 lines 467–476) and the readouts under it are DOM,
# so the only thing that has to reach a screen reader through the canvas is
# the state-bound `aria-label`.
_HB_CANVAS = (1800, 660)
def _hb_segments(keys):
    """`keys` as [(x0, t0, x1, t1), …] — one per phase band."""
    return [(keys[i][0], keys[i][1], keys[i + 1][0], keys[i + 1][1])
            for i in range(len(keys) - 1)]
def _hb_temp_at(keys, x):
    """Design's `tempAt`: piecewise-linear over the authored breakpoints."""
    for x0, t0, x1, t1 in _hb_segments(keys):
        if x <= x1:
            return t0 + (t1 - t0) * ((x - x0) / float(x1 - x0))
    return keys[-1][1]
def _hb_phase_at(keys, x):
    """The index of the band `x` falls in. Bands are [x0, x1), last inclusive."""
    for i, (x0, _t0, x1, _t1) in enumerate(_hb_segments(keys)):
        if x < x1:
            return i
    return len(keys) - 2
def _hb_round(t):
    """`Math.round` semantics, so Python and JS never disagree by one degree.

    Python's `round` takes halves to even and JS's `Math.round` takes them up;
    every readout on this bench is composed in both places, so the tie has to
    break the same way. Floor division rather than `int()` because `int()`
    truncates towards zero and this curve starts below it.
    """
    return int((t + 0.5) // 1)
def _hb_degrees(t, unit):
    """`−20 °C` — U+2212 MINUS, not a hyphen. Design's own readout (line 716).

    The unit is authored once in `labels.unit` and read here and in the JS.
    """
    n = _hb_round(t)
    return "%s%d %s" % ("−" if n < 0 else "", abs(n), unit)
def _hb_fill(template, t, label):
    """`{t}` and `{phase}`, composed the same way in Python and in JS.

    `{t}` is the plain rounded number, ASCII minus and all: it is spoken by a
    screen reader, and "minus 20" is what a reader makes of `-20`. The typeset
    U+2212 belongs on the visible readout and nowhere else.
    """
    return (template.replace("{t}", str(_hb_round(t)))
            .replace("{phase}", (label or "").lower()))
def r_heating_bench(a, act_id):
    """⊕ c1-03 `#s-curve` — scrub through a heating curve and watch it stop.

    ⚠️ A LIGHT `.ks3-block`, not a practical (map §3.3). The graph is drawn on
    cream and the readouts sit on `--ks3-inset`; on ink every token resolves
    wrong and the paper the curve is drawn on becomes a hole in the block.

    ⚖️ **THE MASS NEVER MOVES, AND IT IS NOT STATE.** `Mass in the flask ·
    50.0 g` is markup on Design's page and markup here: emitted once, never
    read by the runtime, never recomputed. It is the whole confrontation of
    the lesson — the temperature changes, the picture changes, and the one
    number that could say something was lost does not move — so the renderer
    RAISES on a bench that does not declare it rather than rendering two
    readouts and a gap.

    ⚖️ **EVERY BAND IS DERIVED FROM `keys`.** The five phase boundaries, the
    two shaded plateaus, the flask's melt and boil fractions and the head
    counter's total all come out of the same six breakpoints, so the plateau
    ratio can be corrected in one place and nothing drifts out of step with
    it. Design's page hard-codes the boundaries a second time in `phaseAt`
    (lines 459–466) and a third time in the two flask fractions (574, 592);
    all three had to agree by hand.

    ⚠️ Emit-both-show-one for the phase word and for the five plateau notes.
    Those notes are the science of the lesson and they are never rebuilt in JS
    from an attribute: all five are in the document, four are `hidden`, and
    the runtime toggles which one is shown.
    """
    keys = a.get("keys") or []
    phases = a.get("phases") or []
    labels = a.get("labels") or {}
    graph = a.get("graph") or {}
    flask = a.get("flask") or {}
    alt = a.get("alt") or {}

    if len(keys) < 2 or any(len(k) != 2 for k in keys):
        raise ValueError(
            "heating-bench %r needs keys[] as at least two [x, temperature] "
            "breakpoints." % act_id)
    xs = [k[0] for k in keys]
    if xs != sorted(xs) or len(set(xs)) != len(xs):
        raise ValueError(
            "heating-bench %r has keys[] out of order: x must increase "
            "strictly, got %s." % (act_id, xs))
    if xs[0] != 0 or xs[-1] != 100:
        raise ValueError(
            "heating-bench %r draws a curve from %s to %s; the scrub runs "
            "0–100 and the curve must span it, or the student can drag past "
            "the end of the run." % (act_id, xs[0], xs[-1]))
    if len(phases) != len(keys) - 1:
        raise ValueError(
            "heating-bench %r declares %d phase(s) for %d segment(s). One "
            "band per segment — the bands ARE the segments."
            % (act_id, len(phases), len(keys) - 1))

    segs = _hb_segments(keys)
    plateaus = [i for i, (_x0, t0, _x1, t1) in enumerate(segs) if t0 == t1]
    if not plateaus:
        raise ValueError(
            "heating-bench %r draws no plateau. A curve that only climbs is "
            "not this lesson." % act_id)
    for i, ph in enumerate(phases):
        if ph.get("tone") not in _HB_TONES:
            raise ValueError(
                "heating-bench %r phase %r tone %r; the drawn set is %s."
                % (act_id, ph.get("id"), ph.get("tone"),
                   ", ".join(sorted(_HB_TONES))))
        # A plateau carries the two captions the canvas draws over it; a ramp
        # carries neither, and authoring one on a ramp would paint a stripe
        # over a stretch that is not holding still.
        if (i in plateaus) != bool(ph.get("band")):
            raise ValueError(
                "heating-bench %r phase %r: `band` is the caption over a "
                "SHADED PLATEAU and this segment %s a plateau in keys[]."
                % (act_id, ph.get("id"), "is" if i in plateaus else "is not"))
        if (i in plateaus) != bool(ph.get("banner")):
            raise ValueError(
                "heating-bench %r phase %r: `banner` is the line drawn across "
                "the flask while the state is changing, so it belongs to a "
                "plateau and to nothing else." % (act_id, ph.get("id")))
        if not ph.get("note"):
            raise ValueError(
                "heating-bench %r phase %r has no note. The note is what the "
                "band teaches; a band without one is a colour."
                % (act_id, ph.get("id")))
    if not a.get("mass"):
        raise ValueError(
            "heating-bench %r declares no `mass`. The constant mass readout "
            "IS the confrontation of this lesson — see the module comment."
            % act_id)
    for key in ("scrub", "temperature", "phase", "mass", "unit"):
        if not labels.get(key):
            raise ValueError(
                "heating-bench %r has no labels[%r]; every readout on this "
                "bench is labelled on Design's page." % (act_id, key))
    for jump in a.get("jumps") or []:
        v = jump.get("value")
        if not isinstance(v, int) or v < 0 or v > 100:
            raise ValueError(
                "heating-bench %r jump %r targets %r, which is not a whole "
                "number on the 0–100 scrub." % (act_id, jump.get("label"), v))
    for field, template in (("alt.template", alt.get("template", "")),
                            ("valuetext", a.get("valuetext", ""))):
        if "{t}" not in template or "{phase}" not in template:
            raise ValueError(
                "heating-bench %r %s must carry both {t} and {phase}: it is "
                "the only reading a screen reader gets of a canvas."
                % (act_id, field))

    gate_html, hide = r_bench_gate(a.get("gate"))

    # The resting frame. Every value below is what the page SHOWS before any
    # JS runs, so the document is correct on its own and the first paint is
    # never a wrong number waiting to be corrected.
    start = 0
    t0 = _hb_temp_at(keys, start)
    ph0 = _hb_phase_at(keys, start)
    first = phases[ph0]

    words = "".join(
        '<span class="ks3-hb-phase" data-phase="%s" data-tone="%s"%s>%s</span>'
        % (e(ph.get("id", "")), e(ph.get("tone", "ink")),
           "" if i == ph0 else " hidden", t(ph.get("label", "")))
        for i, ph in enumerate(phases))
    notes = "".join(
        '<p class="ks3-hb-note" data-phase="%s"%s>%s</p>'
        % (e(ph.get("id", "")), "" if i == ph0 else " hidden",
           rich(ph.get("note", "")))
        for i, ph in enumerate(phases))
    jumps = "".join(
        '<button type="button" class="ks3-seg-btn ks3-hb-jump" data-v="%d" '
        'aria-pressed="%s">%s</button>'
        % (j["value"], "true" if abs(start - j["value"]) < 3 else "false",
           t(j.get("label", "")))
        for j in a.get("jumps") or [])

    sid = "ks3-hb-scrub-%s" % act_id
    cfg = {"keys": keys,
           "phases": [{"id": p.get("id", ""), "label": p.get("label", ""),
                       "band": p.get("band", ""), "banner": p.get("banner", "")}
                      for p in phases],
           "graph": graph, "flask": flask, "alt": alt,
           "valuetext": a.get("valuetext", ""), "unit": labels["unit"]}

    return (gate_html
            + '<div class="ks3-hb" data-hb%s data-total="%d" data-cfg="%s">'
              '<div class="ks3-hb-frame">'
              '<canvas class="ks3-hb-canvas" width="%d" height="%d" '
              'role="img" aria-label="%s" data-hb-canvas></canvas>'
              '<div class="ks3-hb-foot">'
              '<label class="ks3-hb-scrub-label" for="%s">%s</label>'
              '<input class="ks3-hb-scrub" id="%s" type="range" min="0" '
              'max="100" step="1" value="%d" aria-valuetext="%s" data-hb-scrub>'
              '<div class="ks3-hb-tiles">'
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value" data-hb-temp>%s</p></div>'
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value">%s</p></div>'
              # ⚠️ NO `data-` hook on the mass tile, deliberately. There is
              # nothing for the runtime to bind to, which is the point.
              '<div class="ks3-hb-tile"><p class="ks3-hb-tile-label">%s</p>'
              '<p class="ks3-hb-tile-value ks3-hb-mass">%s</p></div>'
              '</div>'
              '<div class="ks3-hb-jumps">%s</div>'
              '</div></div>'
              '<div class="ks3-hb-notes" data-hb-notes role="status">%s</div>'
              '</div>'
            % (hide, len(plateaus),
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               _HB_CANVAS[0], _HB_CANVAS[1],
               e(_hb_fill(alt.get("template", ""), t0, first.get("label", ""))),
               e(sid), t(labels["scrub"]), e(sid), start,
               e(_hb_fill(a.get("valuetext", ""), t0, first.get("label", ""))),
               t(labels["temperature"]), t(_hb_degrees(t0, labels["unit"])),
               t(labels["phase"]), words,
               t(labels["mass"]), t(a["mass"]),
               jumps, notes))
# DISPATCH: "keyed-commit": ("ks3-keyed-block", ' data-instrument data-keyedblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "keyed-commit":
#         parts.append(r_keyed_commit(a, act_id))
#
# ⚠️ TWO GUARDS ARE REQUIRED IN `r_activity`, and the component is wrong
# without them. This kind owns its whole body — the option list AND the panel —
# so neither of the shell's generic branches may fire on the same payload:
#
#     if a.get("options") and kind != "keyed-commit":
#         parts.append(r_activity_options(a["options"]))
#     ...
#     if a.get("reveal") and kind != "keyed-commit":
#
# Without the first, `r_activity_options` calls `t()` on a dict and renders its
# repr as four answer buttons under the four real ones. Without the second, a
# lesson that spells the static paragraphs `reveal` gets a SECOND
# `.ks3-reveal-panel` that nothing ever unhides — an invisible duplicate of the
# closing prose, which is the worst of the three failure modes because it looks
# fine.
#
# THE SHARED CONTRACT (c1-03 `#s-bubble` and c1-06 `#s-verdict`), so the two
# lessons author the same shape:
#
#     options:       [{text, reply}] × 4    (or commit_options, same shape)
#     answer_index:  int                    validated here, never marked
#     closing:       [str, …]               static paragraphs, after the reply
#
# ⚠️ As delivered, c1-06 spells the last one `closing` and c1-03 spells it
# `reveal`. Both are read here, because the two lessons landed in parallel and
# refusing one would fail the build over a synonym — but ONE of them should
# win at integration and the other be renamed. `closing` is the better name: it
# is not the shell's `reveal` (which is one gated string), it never gates
# anything on its own, and the collision with the shell's key is exactly what
# makes the second guard above necessary.
#
# Place the function next to `r_evidence_bench`. Needs `e`, `t`, `rich`,
# `_option_li`.


def r_keyed_commit(a, act_id):
    """⊕ c1-06 `#s-verdict` · c1-03 `#s-bubble` — one commit, four answers.

    The nearest shipped shape is the generic `predict`, which carries prompt,
    options and ONE reveal string. Here the first paragraph of the reveal is
    the chosen option's own reply and the paragraphs after it are static, so
    the panel says something different to each of four students and then says
    the same thing to all of them. A single `reveal` cannot express that, and
    branching in code (which is what c1-03's page does — three responses keyed
    on the index) puts science-bearing prose inside the engine.

    ⚖️ PAYLOAD-MAP §6.5.2 ruled the c1-06 shape for both: the reply hangs off
    the option. That is what makes a fifth option a data change rather than a
    fifth branch, and it is why c1-03's `{correct, index_3_special_case, other}`
    is expressed as four replies here.

    ⚠️ R3 — NOTHING MARKS. `answer_index` is read at BUILD TIME only, to check
    it is in range and that the option it names carries a reply. It reaches no
    attribute, no class and no student. An activity option shows that it was
    chosen and nothing else; only the ladder marks correctness.

    Emit-both-show-one: all four replies are in the document, hidden, and one
    is unhidden. No authored sentence is rebuilt in JS, and the em dashes and
    `<em>` survive.

    ⚠️ BOTH DRAWN INSTANCES SIT ON INK. `.ks3-dark p` is (0,1,1) and beats a
    bare instrument class at (0,1,0), so every text rule in the stylesheet is
    scoped `.ks3-dark …`. There is a light fallback beside it; see the CSS.
    """
    opts = a.get("options") or a.get("commit_options") or []
    if not opts:
        raise ValueError("keyed-commit %r declares no options[]." % act_id)
    for i, o in enumerate(opts):
        if not isinstance(o, dict):
            raise ValueError(
                "keyed-commit %r option %d is %r, not a {text, reply} record. "
                "This kind takes an option that carries its own answer — that "
                "is the whole difference from a generic `predict`."
                % (act_id, i, type(o).__name__))
        if not o.get("text") or not o.get("reply"):
            raise ValueError(
                "keyed-commit %r option %d needs both `text` and `reply`; a "
                "reply-less option opens an empty panel."% (act_id, i))

    # ⚠️ Read at build time and nowhere else. It names, for the examiner, the
    # option the lesson is arguing for; a drift in the payload that moved the
    # answer past the end of the list would otherwise be silent.
    ans = a.get("answer_index")
    if ans is not None:
        if not isinstance(ans, int) or isinstance(ans, bool):
            raise ValueError(
                "keyed-commit %r answer_index is %r; it is an index into "
                "options[]." % (act_id, ans))
        if not 0 <= ans < len(opts):
            raise ValueError(
                "keyed-commit %r answer_index %d is out of range for %d "
                "option(s)." % (act_id, ans, len(opts)))

    # `reveal` is c1-03's spelling of the same list. See the header: both are
    # read, one should win at integration, and the shell's own `reveal` branch
    # must be guarded either way.
    closing = a.get("closing") or a.get("reveal") or []
    if isinstance(closing, str):
        closing = [closing]

    buttons = "".join(
        _option_li(i, o["text"], ' aria-pressed="false"')
        for i, o in enumerate(opts))

    replies = "".join(
        '<p class="ks3-keyed-reply" data-reply="%d" hidden>%s</p>'
        % (i, rich(o["reply"])) for i, o in enumerate(opts))

    statics = "".join('<p class="ks3-keyed-static">%s</p>' % rich(p)
                      for p in closing)

    return ('<div class="ks3-keyed" data-keyed>'
            '<ul class="ks3-options ks3-keyed-options" role="list">%s</ul>'
            '<div class="ks3-keyed-reveal" hidden data-reveal>%s%s</div>'
            '</div>' % (buttons, replies, statics))
# DISPATCH: "model-timeline": ("ks3-mtl-block", ' data-instrument data-mtlblock data-stage-done="0"'),
#
# and in `r_activity`, beside the other kind branches:
#     if kind == "model-timeline":
#         parts.append(r_model_timeline(a, act_id))
#
# Place the function next to `r_evidence_bench`. Needs `e`, `t`, `rich`.


def r_model_timeline(a, act_id):
    """⊕ c1-06 `#s-history` — five models, in order, one open at a time.

    ⚠️ A LIGHT `.ks3-block`, and it has NO nearest existing kind. `zoom-ladder`
    is a slider over magnifications with a tick row and an authored next-box;
    `scale-zoom` is two step buttons over five drawings. This is five named
    positions, each with a claim, a body and the evidence that killed it, and
    the step control is a **third control geometry** in the unit — left-aligned,
    `10px 14px`, a two-line stack of mono year over 700 name. It is registered
    as its own thing rather than folded into `seg()`, which is one line and one
    weight, because a year over a name is not a segment label.

    ⚠️ `default_index` IS NOT ZERO, and that is the teaching. The row opens on
    Dalton (index 1), not Democritus: Dalton is the model the student has been
    using all unit, and the point of the row is that it already has a before
    and an after. A component that opened on the first entry would put a
    twenty-century dead end in front of the student as the headline.

    ⚖️ THE RAIL PREDICATE IS A SET, NOT AN INEQUALITY. Design's page ticks this
    stage on `history !== 1`, which unticks the moment a student who has read
    all five comes back to Dalton — a rail that goes backwards. `wireModelTimeline`
    counts a set of visited indices, seeded with the default, and never empties
    it. Same class of defect as c1-04's `Math.max(touched, N)`.

    Emit-all-show-one, the same trick the board and the switch use: five detail
    cards in the document, one shown. Going back to a model finds it exactly as
    it was, no state lives anywhere but the DOM, and the 25 authored strings —
    two of which carry an arrow and a right single quote — are never rebuilt in
    JS from an attribute.
    """
    steps = a.get("steps") or []
    if not steps:
        raise ValueError("model-timeline %r declares no steps[]." % act_id)

    broke_label = a.get("broke_label")
    if not broke_label:
        raise ValueError(
            "model-timeline %r declares no broke_label — the static bold prefix "
            "on the rule-topped line, and the thing that makes the sentence a "
            "cause rather than an aside." % act_id)

    start = int(a.get("default_index") or 0)
    if not 0 <= start < len(steps):
        raise ValueError(
            "model-timeline %r opens on index %d of %d step(s)."
            % (act_id, start, len(steps)))

    for i, s in enumerate(steps):
        missing = [k for k in ("year", "who", "label", "claim", "body", "broke")
                   if not s.get(k)]
        if missing:
            raise ValueError(
                "model-timeline %r step %d (%r) is missing %s. Every one of the "
                "six is drawn, and an empty one renders as a gap in the card."
                % (act_id, i, s.get("who"), ", ".join(missing)))

    btns = "".join(
        '<button type="button" class="ks3-mtl-step" data-step="%d" '
        'aria-pressed="%s">'
        '<span class="ks3-mtl-year">%s</span>'
        '<span class="ks3-mtl-who">%s</span></button>'
        # `t()` on the year, not `e()`: 1913 → now carries U+2192, which none of
        # the five latin woff2 subsets contains. Typed as a character it drops
        # to a system font inside a 12px mono span; `t()` draws it.
        % (i, "true" if i == start else "false", t(s["year"]), t(s["who"]))
        for i, s in enumerate(steps))

    cards = "".join(
        '<div class="ks3-mtl-card" data-step="%d"%s>'
        '<p class="ks3-mtl-label">%s</p>'
        '<p class="ks3-mtl-claim">%s</p>'
        '<p class="ks3-mtl-body">%s</p>'
        '<p class="ks3-mtl-broke"><strong>%s</strong> %s</p></div>'
        % (i, "" if i == start else " hidden",
           t(s["label"]), rich(s["claim"]), rich(s["body"]),
           t(broke_label), rich(s["broke"]))
        for i, s in enumerate(steps))

    return ('<div class="ks3-mtl" data-mtl data-total="%d" data-default="%d">'
            '<div class="ks3-mtl-steps">%s</div>'
            '<div class="ks3-mtl-cards">%s</div></div>'
            % (len(steps), start, btns, cards))
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
# DISPATCH: "random-walk-bench": ("ks3-walk-block", ' data-instrument data-walkblock data-stage-done="0"'),
#
# Goes in ACTIVITY_KIND_RENDERERS beside the C2 entries, plus the two lines
# `r_activity` needs:
#
#     if kind == "random-walk-bench":
#         parts.append(r_random_walk_bench(a, act_id))
#
# Place `_walk_alt` and `r_random_walk_bench` after `r_scale_zoom` in
# build_ks3.py. Needs `json`, `e`, `t`, `rich`, `r_bench_gate` — all already
# in scope there.


def _walk_alt(alt, even, left, right):
    """The tank canvas's aria-label. Composed the same way in JS.

    ⊕ `{left}` and `{right}` are an ADDITION to Design's sentence, and the
    reason is the c1-04 ruling reached by a different route: the half counts
    are DRAWN INSIDE the canvas (page lines 534–535) and appear nowhere in the
    DOM, so without them in the label a screen-reader user is told a bar chart
    exists and never told what it says. Design's own clause is unchanged; one
    sentence is appended.
    """
    return (alt.get("template", "")
            .replace("{state}", alt.get("even" if even else "uneven", ""))
            .replace("{left}", str(left))
            .replace("{right}", str(right)))
def r_random_walk_bench(a, act_id):
    """⊕ c1-05 `#s-walk` — 130 particles, no one steering.

    ⚠️ A LIGHT `.ks3-block`, not a practical. Design draws the tank on cream
    inside a card-ground frame; painting it on ink resolves every text token
    wrong and turns the dye purple-on-black. Same trap the map names for
    c2-01's claim switch.

    ⚖️ **THE TWO CROSSING COUNTERS NEVER RESET WHEN THE TANK EVENS OUT.** They
    are cleared by "Put the drop back" and by nothing else (page lines
    439–440). That is the whole confrontation of `PART-11`: the spreading
    finishes and the moving does not, and a student watching the two numbers
    climb together after "Spread out? Yes" is reading the argument rather than
    being told it. `#s-think`'s reveal then quotes those counters in words. An
    optimisation that zeroed them on `even` would delete the lesson and leave
    an animation.

    ⚠️ THE FOUR NOTES ARE ALL IN THE DOCUMENT AND ONE IS SHOWN. Emit-both-
    show-one, because a note is a science sentence and JS must never rebuild
    one from an attribute — `<em>` would not survive the round trip and a
    string assembled in two places is a string that drifts in one of them.

    ⚠️ The canvas frame here is NOT `_canvas_frame`. That wrapper is the DARK
    one — a 2px `--ks3-on-dark-muted` rule over a `--ks3-dark-panel` foot — and
    this bench is light: a 2px INK rule over a `--ks3-inset` foot. Two grounds,
    two components; reusing the dark one would put an on-dark border on cream.
    """
    n = int(a.get("particles") or 0)
    labels = a.get("labels") or {}
    canvas_labels = a.get("canvas_labels") or {}
    notes = a.get("notes") or {}
    progress = a.get("progress") or {}
    alt = a.get("alt") or {}
    seed = a.get("seed") or {}
    step = a.get("step") or {}
    bounds = a.get("bounds") or {}
    even = a.get("even") or {}

    if n < 2:
        raise ValueError(
            "random-walk-bench %r seeds %d particle(s); the instrument is a "
            "crowd leaving one side and needs a crowd." % (act_id, n))

    need = {
        "labels": (labels, ("cross_right", "cross_left", "even", "even_yes",
                            "even_no", "run_start", "run_pause",
                            "run_continue", "reset", "trace_on", "trace_off",
                            "warm_on", "warm_off")),
        "canvas_labels": (canvas_labels, ("left_half", "right_half",
                                          "profile")),
        # Four branches, and all four are Design's. A missing one would render
        # as an empty panel at exactly the moment the bench has something to
        # say — see `walkNote`, page lines 575–584.
        "notes": (notes, ("idle", "spreading", "even", "tracing")),
        "progress": (progress, ("idle", "spreading", "even")),
        "alt": (alt, ("template", "even", "uneven")),
        "seed": (seed, ("x", "y")),
        "step": (step, ("cool", "warm", "y_scale")),
        "bounds": (bounds, ("x", "y")),
        "even": (even, ("tolerance", "hz")),
    }
    for key, (got, wanted) in sorted(need.items()):
        missing = [k for k in wanted if got.get(k) in (None, "")]
        if missing:
            raise ValueError(
                "random-walk-bench %r is missing %s: %s."
                % (act_id, key, ", ".join(missing)))
    for key in ("trail_max", "bins", "reduced_scale"):
        if not a.get(key):
            raise ValueError(
                "random-walk-bench %r declares no %s." % (act_id, key))

    # ⊕ The block head's readout and `progress.idle` are the SAME WORD in two
    # records — the resting render comes from `head_counter`, the live one from
    # `progress` — so they are checked against each other rather than trusted.
    # Drift here is invisible: the page would open on one word and change to a
    # different one the first time anything is pressed.
    opening = ((a.get("head_counter") or {}).get("start_extra") or {}).get("phase")
    if opening != progress["idle"]:
        raise ValueError(
            "random-walk-bench %r opens its head counter on %r and its live "
            "readout on %r. They are the same readout and must be the same "
            "word." % (act_id, opening, progress["idle"]))

    gate_html, hide = r_bench_gate(a.get("gate"))

    cfg = {"particles": n, "seed": seed, "step": step, "bounds": bounds,
           "even": even, "trail_max": int(a["trail_max"]),
           "bins": int(a["bins"]), "reduced_scale": a["reduced_scale"],
           "canvas_labels": canvas_labels, "alt": alt, "progress": progress}

    def readout(label, inner, extra=""):
        return ('<div class="ks3-walk-readout">'
                '<p class="ks3-walk-readout-label">%s</p>'
                '<p class="ks3-walk-readout-value"%s>%s</p></div>'
                % (t(label), extra, inner))

    # Both words are present and one is hidden — the same rule as the notes.
    # "Yes" and "Not yet" are the answer to the question the gate asked.
    even_words = ('<span data-walk-even-no>%s</span>'
                  '<span data-walk-even-yes hidden>%s</span>'
                  % (t(labels["even_no"]), t(labels["even_yes"])))

    readouts = (readout(labels["cross_right"], "0", " data-walk-cross-right")
                + readout(labels["cross_left"], "0", " data-walk-cross-left")
                + readout(labels["even"], even_words, ' data-walk-even="0"'))

    def swap(attr, pairs, first):
        """A control whose LABEL changes with its state, one span per label."""
        return "".join(
            '<span data-%s="%s"%s>%s</span>'
            % (attr, e(key), "" if key == first else " hidden", t(text))
            for key, text in pairs)

    controls = (
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-run aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-reset>%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-trace aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-sim-seg-btn ks3-walk-btn" '
        'data-walk-warm aria-pressed="false">%s</button>'
        % (swap("run-label", (("start", labels["run_start"]),
                              ("pause", labels["run_pause"]),
                              ("continue", labels["run_continue"])), "start"),
           t(labels["reset"]),
           swap("trace-label", (("on", labels["trace_on"]),
                                ("off", labels["trace_off"])), "on"),
           swap("warm-label", (("on", labels["warm_on"]),
                               ("off", labels["warm_off"])), "on")))

    note_html = "".join(
        '<p data-note="%s"%s>%s</p>'
        % (e(key), "" if key == "idle" else " hidden", rich(notes[key]))
        for key in ("idle", "spreading", "even", "tracing"))

    return (gate_html
            + '<div class="ks3-walk" data-walk%s data-cfg="%s">'
              '<div class="ks3-walk-frame">'
              '<canvas class="ks3-walk-canvas" width="1800" height="640" '
              'role="img" aria-label="%s" data-walk-canvas></canvas>'
              '<div class="ks3-walk-foot">'
              '<div class="ks3-walk-readouts">%s</div>'
              '<div class="ks3-walk-controls">%s</div>'
              '</div></div>'
              # `role="status"` on the note panel, never on the instrument
              # root: the root contains the canvas and the counters, and a live
              # region over a 60 fps drawing announces nothing usable.
              '<div class="ks3-walk-note" data-walk-note role="status">%s</div>'
              '</div>'
            % (hide,
               e(json.dumps(cfg, separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(_walk_alt(alt, False, n, 0)),
               readouts, controls, note_html))
# DISPATCH: "scale-cards": ("ks3-scards-block", " data-instrument data-scalecards"),
#
# NOTE THE ABSENT `data-stage-done`. This kind has no completion contract —
# see the docstring — so it takes the same entry shape as `confrontation`
# rather than the instrument shape. Emitting the attribute would declare a
# contract the section can never discharge, and the stage would sit at 0 for
# ever.
#
# Plus the two lines `r_activity` needs:
#
#     if kind == "scale-cards":
#         parts.append(r_scale_cards(a, act_id))
#
# Place after `r_random_walk_bench` in build_ks3.py. Needs `e`, `t`, `rich`.


def r_scale_cards(a, act_id):
    """⊕ c1-05 `#s-scale` — a distance, a time, and what that costs biology.

    ⚠️ **NOT `reveal-cards`, and this is a build decision with a gate behind
    it.** The nearest existing shape is `r_cards`, and it is wrong three times
    over: these do not flip, there is nothing behind them to reveal, and
    `verify_ks3.py` §5.1.2(a) requires every card grid to ask for a commitment
    in words before the tap. This block asks for nothing — it is the pay-off
    after the bench, not another task — so forcing it into `reveal-cards` would
    either fail that gate or, worse, make somebody write a fake commit prompt
    to satisfy it. A static three-up panel is its own component.

    ⚠️ INK-DARK, so every `<p>` rule in the stylesheet is scoped past
    `.ks3-dark p`, which is (0,1,1) and beats a bare instrument class at
    (0,1,0). The 28px display TIME is the one that would visibly break: it
    would fall back to on-dark BODY colour and read as a caption.

    ⚑ `--ks3-alert` on the distance label is Design's, and the map flags it
    (§5.5.2). Amber on ink is established for CONTROLS since B1; this is amber
    for BODY LABELLING, which is new, and README.txt's "amber is reserved for
    misconceptions" is about blocks rather than either. Reproduced as drawn and
    left flagged — a build is not the place to re-rule a palette question. The
    parity row registers the value, so the day it IS re-ruled the gate says so.
    """
    cards = a.get("scale_cards") or []
    if len(cards) < 2:
        raise ValueError(
            "scale-cards %r draws %d card(s); the panel is a comparison and "
            "needs at least two." % (act_id, len(cards)))
    for i, c in enumerate(cards):
        missing = [k for k in ("distance", "time", "text") if not c.get(k)]
        if missing:
            raise ValueError(
                "scale-cards %r card %d is missing %s. All three lines carry "
                "the comparison — a card with no time says nothing."
                % (act_id, i + 1, ", ".join(missing)))
    if not a.get("close"):
        raise ValueError(
            "scale-cards %r declares no `close`. The closing line is what "
            "turns three numbers into a rule (\"double the distance and "
            "diffusion takes four times as long\"); without it the panel is "
            "three facts and no argument." % act_id)

    grid = "".join(
        '<div class="ks3-scard">'
        '<p class="ks3-scard-distance">%s</p>'
        '<p class="ks3-scard-time">%s</p>'
        '<p class="ks3-scard-text">%s</p></div>'
        % (t(c["distance"]), t(c["time"]), rich(c["text"]))
        for c in cards)

    return ('<div class="ks3-scards">%s</div>'
            '<p class="ks3-scards-close">%s</p>' % (grid, rich(a["close"])))
# DISPATCH: "sort-cards": ("ks3-sortcards-block", ' data-instrument data-sortcardsblock data-stage-done="0"'),
#
# Splice into build_ks3.py beside the other C1 instruments, plus the dispatch
# line in `r_activity`:
#
#     if kind == "sort-cards":
#         parts.append(r_sort_cards(a, act_id))
#
# ⚠️ It renders INSIDE the `misconception` shell (see ks3_data/c1/__init__.py's
# `_INSTRUMENT_SEGMENTS`), so `r_activity` emits the amber head, then
# `r_confrontation`'s quote, then the lede, then this. Nothing about the
# confrontation path changes.


def r_sort_cards(a, act_id):
    """⊕ c1-03 `#s-think` — four things, and the word that fits each one.

    ⚠️ NOT `verdict-cards` and NOT `job-sort`, and the difference is the whole
    mechanism. Both of those are ONE-SHOT: the first press disables the row's
    other options, because their reveal is an answer and a second press would
    be choosing after reading it. Design's sorter stays open — press Melting,
    read why it is not melting, press Dissolving, and the card follows you.
    That is the page as drawn, and it is also what the lede promises: *"the
    sorting is the point, not the score"*. Locking it would make the block a
    test, which is the thing the sentence says it is not.

    ⚠️ **THIS IS THE ONE PLACE IN C1 WHERE A CARD MARKS THE ANSWER**, and it
    is Design's rule as measured (map §3.5.3, page lines 767–770): the card's
    border goes to `--ks3-accent` when the choice matches and `--ks3-ink` when
    it does not, and the note is ink or accent-text to match. It is carried
    because the page wins over the engine, and it is expressed as ONE
    ATTRIBUTE — `data-verdict` on the card — so that if R3 is ever ruled to
    reach this component the change is two lines of CSS and nothing else
    moves. Note that the marking is never the ok/alert family: it cannot be
    confused with the ladder's verdict, and the wrong state takes exactly the
    neutral ink border every decided `job-sort` row already takes.

    ⚠️ Emit-both-show-one. Each card carries BOTH authored notes, one hidden;
    no sentence is ever assembled in JS from an attribute.
    """
    items = a.get("items") or []
    buttons = a.get("buttons") or []
    if not items:
        raise ValueError("sort-cards %r declares no items[]." % act_id)
    if len(buttons) != 2:
        raise ValueError(
            "sort-cards %r offers %d button(s); it is a binary verdict — one "
            "word against the other — and a third column is a different "
            "component." % (act_id, len(buttons)))
    values = [b.get("value") for b in buttons]
    if len(set(values)) != 2 or not all(values):
        raise ValueError(
            "sort-cards %r buttons need two distinct `value`s; got %r."
            % (act_id, values))
    for it in items:
        # ⚠️ ANSWER VALIDATION, unlike `job-sort` and `verdict-cards` — and it
        # is right here for the reason it is wrong there. Those two answer in
        # free sentences that are deliberately not one of the offered options;
        # this one answers with the button's own value, and the value decides
        # which of the two authored notes a student reads. An answer that
        # matches no button would show every card the wrong note, silently.
        if it.get("answer") not in values:
            raise ValueError(
                "sort-cards %r item %r answers %r, which is not one of the "
                "two buttons %r." % (act_id, it.get("id"), it.get("answer"),
                                     values))
        for side in ("right", "wrong"):
            if not it.get(side):
                raise ValueError(
                    "sort-cards %r item %r has no %r note. Both are authored "
                    "on Design's page and both are read: the card answers the "
                    "choice the student actually made."
                    % (act_id, it.get("id"), side))

    cards = []
    for it in items:
        opts = "".join(
            '<button type="button" class="ks3-seg-btn ks3-sortcards-opt" '
            'data-choice="%s" aria-pressed="false">%s</button>'
            % (e(b["value"]), t(b.get("label", "")))
            for b in buttons)
        cards.append(
            '<div class="ks3-sortcards-card" data-card="%s" data-answer="%s">'
            '<p class="ks3-sortcards-text">%s</p>'
            '<div class="ks3-sortcards-opts">%s</div>'
            '<p class="ks3-sortcards-note" data-note="right" hidden>%s</p>'
            '<p class="ks3-sortcards-note" data-note="wrong" hidden>%s</p>'
            '</div>'
            % (e(it.get("id", "")), e(it["answer"]), rich(it.get("text", "")),
               opts, rich(it["right"]), rich(it["wrong"])))

    # The whole-set summary, gated on all four. It is the payoff for sorting
    # rather than reading, so it does not exist in the document's flow until
    # the sorting is done.
    summary = ""
    if a.get("summary"):
        summary = ('<div class="ks3-sortcards-close" hidden '
                   'data-sortcards-close>%s</div>'
                   % "".join("<p>%s</p>" % rich(p) for p in a["summary"]))

    return ('<div class="ks3-sortcards" data-sortcards data-total="%d">'
            '<div class="ks3-sortcards-grid">%s</div>%s</div>'
            % (len(items), "".join(cards), summary))
# DISPATCH: "state-bench": ("ks3-sbench-block", ' data-instrument data-sbenchblock data-stage-done="0"'),
#
# Splice `r_state_bench` into build_ks3.py beside the other C1 instruments, and
# add `if kind == "state-bench": parts.append(r_state_bench(a, act_id))` to
# `r_activity`'s dispatch run.


def r_state_bench(a, act_id):
    """⊕ c1-02 `#s-bench` — one substance, three arrangements, on a canvas.

    ⚠️ A LIGHT `.ks3-block`, not a practical. c1-02 is the only C1 lesson with
    no dark ground but the hook and the keynote (map §2.3), and the particle
    drawing is cream-on-cream: painting the shell ink would resolve every text
    token wrong and put a #FFFDF8 canvas on a #221E1B block.

    ⚖️ THE FIXED-SIZE REFERENCE PARTICLE IS THE LESSON. NOTES §3 flag 3 names
    it non-negotiable, and it is: one particle, the same radius as every
    particle in every state, captioned, drawn under the box in all three states
    and in every setting. It is the visible form of the sentence the whole
    lesson defends — the particles do not change, the spaces do. So
    `reference_particle` is REQUIRED and this raises without it, rather than
    rendering a bench that has quietly lost its argument to a layout tidy-up.

    ⚖️ EIGHT NOTES, ALL IN THE DOCUMENT, SEVEN HIDDEN. squash × 2, paths × 3,
    resting × 3. Emit-both-show-one rather than a `textContent` swap out of an
    attribute: these are the sentences that carry the science, and rebuilding
    one in JS is how an `<em>` gets eaten and how a string ends up living in an
    attribute where nothing reviews it. The two toggle LABELS take the same
    treatment for the same reason — each is a pair of authored words and
    neither is composed.

    ⚠️ NOT `particle-states`. `SIM_ARIA`'s box-of-particles is driven by a
    TEMPERATURE SLIDER and `SIM_CONTROLS` offers temperature / volume /
    particles / medium. Design's bench has no temperature control at all: it has
    three named state buttons, a motion toggle, a path toggle and a squash
    toggle. Rendering it as the sim would hand the student a dial Design did not
    draw and hide three Design did — the MRB-205 failure exactly (map §2.6).

    ⊕ The counter opens at ZERO. Design's `benchProgress` (page line 614) adds
    one for the state the bench is *about* to show, so an untouched page reads
    "1 of 3 states seen" above a bench still behind its gate. `head_counter`
    carries `start: 0`; the gate banks the opening state when it is answered,
    which is the first moment a student has seen anything.
    """
    states = a.get("states") or []
    if not states:
        raise ValueError("state-bench %r declares no states[]." % act_id)
    for s in states:
        missing = [k for k in ("key", "label", "alt") if not s.get(k)]
        if missing:
            raise ValueError(
                "state-bench %r state %r is missing %s. `label` is the button "
                "face AND the caption the canvas prints; `alt` is that state's "
                "whole aria-label, authored as one finished sentence rather "
                "than composed at runtime from the key."
                % (act_id, s.get("key"), ", ".join(missing)))
    keys = [s["key"] for s in states]

    ref = a.get("reference_particle")
    if not ref:
        raise ValueError(
            "state-bench %r authors no `reference_particle`. NOTES §3 flag 3 "
            "makes the fixed-size reference particle and its caption "
            "non-negotiable — it is the drawn form of the claim the lesson "
            "exists to defend, and a bench without it is a picture of three "
            "arrangements with the argument removed." % act_id)

    banner = a.get("squash_banner") or {}
    for k in ("gas", "other"):
        if not banner.get(k):
            raise ValueError(
                "state-bench %r squash_banner is missing %r; the piston prints "
                "one of two authored lines and there is no third." % (act_id, k))

    ctl = a.get("controls") or {}
    pairs = (("motion", "running", "frozen"), ("trails", "shown", "hidden"))
    for name, on_key, off_key in pairs:
        c = ctl.get(name) or {}
        if not (c.get(on_key) and c.get(off_key)):
            raise ValueError(
                "state-bench %r control %r needs both %r and %r. The label is "
                "keyed by the state the control is IN, never by what pressing "
                "it does, so the two can never be swapped by accident."
                % (act_id, name, on_key, off_key))
    if not (ctl.get("squash") or {}).get("label"):
        raise ValueError(
            "state-bench %r control 'squash' needs a `label`." % act_id)

    notes = a.get("notes") or {}
    for k in ("gas", "other"):
        if not (notes.get("squash") or {}).get(k):
            raise ValueError(
                "state-bench %r notes.squash is missing %r." % (act_id, k))
    for group in ("trails", "rest"):
        for k in keys:
            if not (notes.get(group) or {}).get(k):
                raise ValueError(
                    "state-bench %r notes.%s is missing state %r; every state "
                    "answers every instrument." % (act_id, group, k))

    groups = a.get("groups") or {}
    gate_html, hide = r_bench_gate(a.get("gate") or {})
    first = states[0]

    # ── the state row ──
    # `aria-pressed` on the opening state is TRUE because it is where the bench
    # is, and this is a segmented picker rather than an answer: R3 is untouched,
    # nothing here is marked right or wrong. `data-instrument` on the section is
    # what keeps `wirePredictions` off these buttons.
    state_btns = "".join(
        '<button type="button" class="ks3-sbench-seg" data-sbench-state="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(s["key"]), "true" if i == 0 else "false", t(s["label"]))
        for i, s in enumerate(states))

    # ── the instrument row ──
    # ⊕ CORRECTED: `aria-pressed` follows the TINT, not Design's `motionOn`.
    # Design draws the motion button lit when the motion is FROZEN
    # (`motionStyle: this.seg(!s.motion)`, line 711) and announces
    # `aria-pressed="true"` when it is RUNNING (line 709) — so a screen reader
    # hears "pressed" on a control that looks unpressed, and hears nothing
    # change when a student freezes the bench. Its own sibling, the paths
    # toggle, is consistent (lit and pressed both mean "paths are on"). This is
    # a slip rather than an intention, and R2 requires the announced state and
    # the visible state to be the same state, so the announcement is moved onto
    # the tint rather than the tint onto the announcement — the alternative
    # would light the button on page load, before the student has touched it.
    def toggle(name, on_label, off_label, pressed):
        return ('<button type="button" class="ks3-sbench-seg" data-sbench-%s '
                'aria-pressed="%s">'
                '<span data-lbl="on"%s>%s</span>'
                '<span data-lbl="off"%s>%s</span></button>'
                % (name, "true" if pressed else "false",
                   "" if pressed else " hidden", t(on_label),
                   " hidden" if pressed else "", t(off_label)))

    motion = ctl["motion"]
    trails = ctl["trails"]
    # The bench opens with the motion RUNNING and the paths hidden, so the
    # motion button shows "Freeze the motion" unpressed and the paths button
    # shows "Show the paths" unpressed. Nothing is lit until the student acts.
    inst_btns = (
        toggle("motion", motion["frozen"], motion["running"], False)
        + toggle("trails", trails["shown"], trails["hidden"], False)
        + '<button type="button" class="ks3-sbench-seg" data-sbench-squash '
          'aria-pressed="false">%s</button>' % t(ctl["squash"]["label"]))

    # ── the eight notes, all present, seven hidden ──
    # The resting note for the opening state is the one shown, which is what a
    # student reads the instant the gate is answered.
    live = "rest:%s" % first["key"]
    rows = []
    for group in ("squash", "trails", "rest"):
        for k, text in sorted((notes.get(group) or {}).items()):
            nid = "%s:%s" % (group, k)
            rows.append('<p class="ks3-sbench-note-text" data-note="%s"%s>%s</p>'
                        % (e(nid), "" if nid == live else " hidden",
                           rich(text)))

    # ⚠️ `role="status"` on the NOTE, never on the instrument root and never on
    # the gated body. A live region wrapped round the whole bench would
    # re-announce the canvas, both control groups and the note every time a
    # student pressed a toggle; wrapped round the note it announces exactly the
    # sentence that changed. `wireStateBench` therefore opens the gate itself
    # rather than calling `wireBenchGate`, which sets `role="status"` on
    # `[data-benchbody]` — see the wire function.
    note_html = ('<div class="ks3-sbench-note" data-sbench-note role="status">'
                 '%s</div>' % "".join(rows))

    canvas = ('<canvas class="ks3-sbench-canvas" width="1800" height="620" '
              'role="img" aria-label="%s" data-sbench-canvas></canvas>'
              % e(first["alt"]))

    foot = ('<div class="ks3-sbench-foot">'
            '<div class="ks3-sbench-group">'
            '<p class="ks3-sbench-grouplabel">%s</p>'
            '<div class="ks3-sbench-row">%s</div></div>'
            '<div class="ks3-sbench-group">'
            '<p class="ks3-sbench-grouplabel">%s</p>'
            '<div class="ks3-sbench-row">%s</div></div></div>'
            % (t(groups.get("states") or ""), state_btns,
               t(groups.get("instruments") or ""), inst_btns))

    # ⊕ The published state lives on the WRAPPER, which is never hidden, so
    # `state-matrix` can read it whether or not the gate has been answered and
    # whatever order the two instruments happen to wire in. These four
    # attributes are the single source of truth for the bench's settings —
    # nothing keeps a second copy (map §2.5.2's cross-block capability).
    return (gate_html
            + '<div class="ks3-sbench" data-sbench data-state="%s" '
              'data-motion="1" data-trails="0" data-squash="0" '
              'data-states="%s" data-banner-gas="%s" data-banner-other="%s" '
              'data-reference="%s"%s>'
              '<div class="ks3-sbench-body"%s>'
              '<div class="ks3-sbench-frame">%s%s</div>%s</div></div>'
            % (e(first["key"]),
               e(json.dumps([{"key": s["key"], "label": s["label"],
                              "alt": s["alt"]} for s in states],
                            separators=(",", ":"), sort_keys=True,
                            ensure_ascii=False)),
               e(banner["gas"]), e(banner["other"]), e(ref),
               # Design's `benchProgress` reads "all three seen" once every
               # state has been visited, and `_head_counter` has no slot for a
               # bespoke FULL string (it has `zero`, which is the other end).
               # Carried here and written by the wire function, so the sentence
               # is authored exactly once.
               (' data-full="%s"' % e(a["progress_full"]))
               if a.get("progress_full") else "",
               hide, canvas, foot, note_html))
# DISPATCH: "state-matrix": ("ks3-smatrix-block", ' data-instrument data-smatrixblock'),
#
# ⚠️ NO `data-stage-done`. Deliberate, and the same shape as `confrontation`'s
# entry: the attribute declares a completion contract, and `#s-matrix` has
# nothing a student can discharge. See the docstring and the lesson module.
#
# Splice `r_state_matrix` into build_ks3.py beside the other C1 instruments, and
# add `if kind == "state-matrix": parts.append(r_state_matrix(a, act_id))` to
# `r_activity`'s dispatch run.


def r_state_matrix(a, act_id):
    """⊕ c1-02 `#s-matrix` — six properties, three states, one row lit.

    ⚠️ NOT `r_comparison`. That is b1-06's shape: a fixed TWO-column "this one
    against that one" table with a dark header row. This is a four-column
    property matrix with a live-highlighted row, and the highlight is driven by
    a DIFFERENT BLOCK's controls. Rendering it as a comparison would give the
    student two columns for a three-state contrast and drop the mechanism
    entirely (map §2.5.2).

    ⊕ CROSS-BLOCK STATE — the first of it in the key stage. No existing KS3
    component reads another block's state, and the temptation is to give this
    one its own copy of squash/paths and keep the two in step. It does not: the
    bench publishes its settings on `[data-sbench]` and the matrix READS them,
    so there is exactly one place the bench's state lives and no way for a
    second copy to drift. `highlight_from` names the section to look in;
    `highlight` maps a bench condition to a row key.

    ⚖️ IT IS NOT A RAIL STOP, and the lesson module does not list it as one.
    Design's stage 3 ticks on `Object.keys(seen).length >= 3` — stage 2's
    predicate, verbatim (page line 648). MRB-208 ruled the rail carries only
    sections that require the student to do something, and this section emits
    no control, no commit and no field: it is an eyebrow, a heading, a lede, a
    table and a footnote. The nearest thing to a demand of its own is the
    highlight, and that is worked from the BENCH's toggles in the bench's
    section — so a predicate over it would reproduce the same defect one
    control-group to the left. `ks3_parity.check_rail_reachable` names this
    exact case in its own docstring; it passes here because the stop is gone,
    not because a borrowed predicate was left in place.

    ⚑ Three of the six rows — `shape`, `volume`, `pour` — can be reached by no
    bench setting whatever, because the highlight answers squash / paths /
    neither and those three rows answer none of them. All six are authored
    anyway: the table is the lesson's reference and the three unreachable rows
    are three of the six answers a student needs. Reported rather than fixed
    with a control Design did not draw (map §2.5.2).
    """
    rows = a.get("rows") or []
    cols = a.get("columns") or []
    if not rows:
        raise ValueError("state-matrix %r declares no rows[]." % act_id)
    if len(cols) < 2:
        raise ValueError(
            "state-matrix %r declares %d column(s); it needs the property "
            "column and one per state." % (act_id, len(cols)))
    # The three state cells are keyed by name rather than by position, because
    # they are authored against a header the author can also see; this asserts
    # the two agree.
    cells = ("solid", "liquid", "gas")
    for r in rows:
        missing = [k for k in ("key", "label") + cells if not r.get(k)]
        if missing:
            raise ValueError(
                "state-matrix %r row %r is missing %s."
                % (act_id, r.get("key") or r.get("label"), ", ".join(missing)))
    if len(cols) != len(cells) + 1:
        raise ValueError(
            "state-matrix %r has %d columns and %d state cells per row; the "
            "header and the body have to describe the same table."
            % (act_id, len(cols), len(cells)))

    by_key = {r["key"]: r for r in rows}
    hl = a.get("highlight") or {}
    for cond in ("squash", "trails", "rest"):
        if hl.get(cond) not in by_key:
            raise ValueError(
                "state-matrix %r highlight[%r] names row %r, which is not one "
                "of %s. A renamed row must be a build error and never a table "
                "that quietly stops lighting."
                % (act_id, cond, hl.get(cond), ", ".join(sorted(by_key))))
    if not a.get("highlight_from"):
        raise ValueError(
            "state-matrix %r authors no `highlight_from`. The lit row is read "
            "off another block's published state and the matrix has to be told "
            "which section to read." % act_id)

    # The RESTING lit row is emitted lit, at build time, by the same rule the
    # runtime uses — squash first, then paths, then neither, and at rest it is
    # neither. Without this the table renders unlit for the instant before
    # `wireStateMatrix` corrects it, which is a wrong picture on screen and a
    # wrong picture in the HTML a search engine reads.
    lit_at_rest = hl["rest"]

    head = "".join('<th scope="col">%s</th>' % t(c) for c in cols)
    body = []
    for r in rows:
        on = r["key"] == lit_at_rest
        body.append(
            '<tr class="ks3-smatrix-row" data-row="%s" data-lit="%s">'
            # ⊕ `aria-current` is an ADDITION inside a component Design drew.
            # Design signals the lit row with `--ks3-accent-tint` and nothing
            # else, so a student who cannot separate the tint from the card is
            # told nothing at all — and the footnote under the table promises
            # them a highlight. R2 says colour is never the only signal on a
            # state. It costs no pixels and changes nothing Design drew.
            '<th scope="row"%s>%s</th>%s</tr>'
            % (e(r["key"]), "1" if on else "0",
               ' aria-current="true"' if on else "",
               t(r["label"]),
               "".join("<td>%s</td>" % t(r[k]) for k in cells)))

    foot = ('<p class="ks3-smatrix-foot">%s</p>' % t(a["footnote"])
            if a.get("footnote") else "")

    return ('<div class="ks3-smatrix" data-smatrix data-from="%s" '
            'data-lit-squash="%s" data-lit-trails="%s" data-lit-rest="%s">'
            '<div class="ks3-smatrix-scroll">'
            '<table class="ks3-smatrix-table">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s</div>'
            % (e(a["highlight_from"]), e(hl["squash"]), e(hl["trails"]),
               e(hl["rest"]), head, "".join(body), foot))


# ── registrations ────────────────────────────────────────────────────────
KIND_SHELL = {
    'collision-counter': ("ks3-counter-block", ' data-instrument data-counterblock data-stage-done="0"'),
    'evidence-bench': ("ks3-ebench-block", ' data-instrument data-ebenchblock data-stage-done="0"'),
    'gap-test-rig': ("ks3-gap-block", ' data-instrument data-gapblock data-stage-done="0"'),
    'halving-bench': ("ks3-cut-block", ' data-instrument data-cutblock data-stage-done="0"'),
    'heating-bench': ("ks3-hb-block", ' data-instrument data-hbblock data-stage-done="0"'),
    'keyed-commit': ("ks3-keyed-block", ' data-instrument data-keyedblock data-stage-done="0"'),
    'model-timeline': ("ks3-mtl-block", ' data-instrument data-mtlblock data-stage-done="0"'),
    'prediction-stack': ("ks3-predict-block", ' data-instrument data-predictblock data-stage-done="0"'),
    'random-walk-bench': ("ks3-walk-block", ' data-instrument data-walkblock data-stage-done="0"'),
    'scale-cards': ("ks3-scards-block", " data-instrument data-scalecards"),
    'sort-cards': ("ks3-sortcards-block", ' data-instrument data-sortcardsblock data-stage-done="0"'),
    'state-bench': ("ks3-sbench-block", ' data-instrument data-sbenchblock data-stage-done="0"'),
    'state-matrix': ("ks3-smatrix-block", ' data-instrument data-smatrixblock'),
}

KIND_FN = {
    'collision-counter': r_collision_counter,
    'evidence-bench': r_evidence_bench,
    'gap-test-rig': r_gap_test_rig,
    'halving-bench': r_halving_bench,
    'heating-bench': r_heating_bench,
    'keyed-commit': r_keyed_commit,
    'model-timeline': r_model_timeline,
    'prediction-stack': r_prediction_stack,
    'random-walk-bench': r_random_walk_bench,
    'scale-cards': r_scale_cards,
    'sort-cards': r_sort_cards,
    'state-bench': r_state_bench,
    'state-matrix': r_state_matrix,
}
