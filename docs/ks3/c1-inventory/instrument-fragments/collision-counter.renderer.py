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
_COUNTER_GROUPS = (
    ("temps", "speed_multiplier", "temperature", "temp"),
    ("vols", "scale", "volume", "vol"),
    ("counts", "n", "particles", "count"),
)


def _counter_alt(alt, temps, vols, counts, temp, vol, count, hits):
    """The bench canvas's aria-label. Same composition in Python and in JS.

    ⊕ CORRECTION (PAYLOAD-MAP §4.6). Design's label (page 705–706) names the
    temperature, the container and the particle count and stops — it does not
    say how many wall hits there were, which is the one number the lesson is
    about and the one a sighted student is reading in 58px type. Every readout
    on this bench is drawn INSIDE the canvas, so `aria-label` is the only route
    to any of it. Design's sentence is carried byte-identical and the count is
    added as a second sentence after it.
    """
    return (alt.get("template", "")
            .replace("{temp}", (temps[temp].get("label") or "").lower())
            .replace("{vol}", (vols[vol].get("label") or "").lower())
            .replace("{n}", str(counts[count].get("n", "")))
            .replace("{hits}", str(hits)))


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

    ⚑ NOTES flag 6 — pressure is a COUNT and a BAR, never a pascal. The bar
    fills to `min(1, hits / pressure_full)` and carries no number and no unit.

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

    for token in ("{temp}", "{vol}", "{n}", "{hits}"):
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
        "window_ms": a.get("window_ms", 1000),
        "flash_ms": a.get("flash_ms", 420),
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
                              groups["counts"], temp0, vol0, count0, 0)),
               "".join(group_html), bump_btn, t(bumps["caption"]),
               note_html))
