"""ks3_art.b11 — B11's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import re
from ks3_art.kit import (
    _SVG_BAND,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_MONO,
    _SVG_RULE_STRONG,
    _b10_suffix,
    _b7_need,
    _b8_plain,
    _b9_json,
    _pctnum,
    _svg_open,
    _svg_text,
    e,
    t,
)


# ── the peppered moth pair (b11-02) ──────────────────────────────────────

# ⚖️ TWO BARKS, AND THEY DIFFER BY PATTERN AS WELL AS BY TONE. That is the
# whole reason this is a closed set of two drawn textures rather than a colour
# an author picks: lichen is scattered rounded MOTTLE and soot is vertical
# STREAKS, so a reader who cannot separate the two tones can still see that
# these are two different surfaces. Colour-alone would make the diagram work
# for most readers and fail exactly the ones it is drawn for.
#
# The coordinates are hardcoded and deterministic — B11 has no randomness
# anywhere (schema §0.2), and a mottle that moved between builds would make
# every byte-identical-output gate in the build meaningless.
_B11_MOTH_LICHEN = (
    # x, y, rx, ry — panel-local, kept inside the frame by construction so no
    # clip path (and therefore no generated id) is needed.
    (48, 38, 26, 17), (118, 22, 15, 11), (196, 44, 21, 13), (272, 26, 17, 12),
    (28, 104, 18, 12), (104, 128, 24, 15), (186, 112, 14, 10),
    (258, 132, 22, 14), (312, 78, 16, 11), (72, 168, 20, 12),
    (168, 172, 15, 10), (240, 176, 19, 12), (306, 148, 13, 9),
)
_B11_MOTH_SOOT = (
    # x, width — full-height vertical streaks, which is a different KIND of
    # mark from a blob and reads as one at any tone.
    (26, 7), (44, 3), (78, 11), (100, 4), (132, 6), (150, 3), (186, 9),
    (208, 4), (238, 7), (256, 3), (286, 10), (312, 4), (332, 6),
)
# The two barks the drawer knows how to paint, and the two moth tones. Closed
# sets, so a typo raises instead of drawing a blank panel or an invisible moth.
_B11_MOTH_BARKS = ("lichen", "soot")
_B11_MOTH_TONES = ("pale", "dark")
def _moth(cx, cy, tone, fill, stroke, scale=1.0):
    """One moth, wings out, seen from above. Drawn, not lettered.

    A triangle would have done the job of "something is resting here", but the
    shape a student is being asked to FIND has to look like a moth or the
    exercise is not the exercise. Two swept forewings, two smaller hindwings, a
    body and two antennae — the minimum that reads as a moth at 120px.

    ⚠️ PAINT GOES IN `style`, NEVER IN `fill="var(--ks3-…)"`. A custom property
    is only substituted inside a CSS declaration; as an SVG presentation
    attribute `var(--ks3-ink)` is not a valid <paint>, the attribute is
    silently dropped, and the element renders opaque BLACK while every token
    grep stays clean. `_svg_text` carries the same warning and it cost four
    rebuilds on the first drawer.
    """
    s = scale
    st = ' style="fill:%s;stroke:%s" stroke-width="1.5"' % (fill, stroke)
    # A group with a class and its tone on it, so a parity row can read the
    # RESOLVED fill of a moth in the browser. That is the assertion that
    # catches the `fill="var(…)"` failure — a dropped paint renders opaque
    # black while every token grep in the repo stays clean.
    parts = ['<g class="ks3-moth" data-moth-tone="%s">' % e(tone)]
    # Forewings, mirrored: a swept triangle with a curved trailing edge.
    for sign in (-1, 1):
        parts.append(
            '<path d="M %.1f %.1f L %.1f %.1f Q %.1f %.1f %.1f %.1f Z"%s/>'
            % (cx, cy - 26 * s,
               cx + sign * 62 * s, cy + 6 * s,
               cx + sign * 34 * s, cy + 30 * s, cx, cy + 16 * s, st))
        # Hindwings, smaller and lower, so the outline is not one flat kite.
        parts.append(
            '<path d="M %.1f %.1f L %.1f %.1f Q %.1f %.1f %.1f %.1f Z"%s/>'
            % (cx, cy + 2 * s,
               cx + sign * 40 * s, cy + 26 * s,
               cx + sign * 18 * s, cy + 40 * s, cx, cy + 30 * s, st))
    # Body.
    parts.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"%s/>'
                 % (cx, cy + 2 * s, 7 * s, 30 * s, st))
    # Antennae.
    for sign in (-1, 1):
        parts.append(
            '<path d="M %.1f %.1f Q %.1f %.1f %.1f %.1f" fill="none" '
            'style="stroke:%s" stroke-width="1.5"/>'
            % (cx, cy - 26 * s, cx + sign * 10 * s, cy - 40 * s,
               cx + sign * 22 * s, cy - 42 * s, stroke))
    parts.append('</g>')
    return "".join(parts)
def _moth_pair(fig):
    """The same two moths on two barks, and only the background changed.

    ⚖️ WHY THIS LESSON GETS A DIAGRAM WHEN THE REST OF B11 DOES NOT (schema
    §14, flag 16, ruled 18 Aug 2026). Camouflage is the one idea in the unit
    that is genuinely and irreducibly visual: the claim is about whether a bird
    can pick a moth out against a background, and no sentence does what two
    panels do. `selection-runner` on the same page shows the PROPORTION
    changing over generations — which is the consequence — and never shows the
    thing the consequence follows from.

    ⚖️ THE TWO BARKS DIFFER BY PATTERN AS WELL AS BY TONE, and that is a
    requirement rather than a flourish. Lichen is scattered rounded mottle;
    soot is vertical streaks. A reader who cannot separate the tones can still
    see two different surfaces, and — more to the point — can still see that
    the MOTH did not change and the BARK did, which is the entire argument of
    the lesson beside it.

    ⚖️ AND EVERY MOTH IS LABELLED, twice: with its name and with a written note
    saying how easy it is to see there. A leader line runs from the label to
    the moth, so the camouflaged one can always be FOUND even when it cannot be
    picked out — which is the honest way to draw camouflage in a diagram that
    also has to be usable. The fill is the camouflage; the hairline outline and
    the leader are the diagram's convention, and they are drawn on all four
    moths so they never mark one of them out as the special case.

    ⛔ THE SAME TWO MOTHS APPEAR ON BOTH BARKS, once each, and the drawer
    refuses anything else. "Individuals do not change — populations do" is this
    lesson's KEY FACT, and a pair of panels showing three moths on one bark and
    one on the other would be drawing a different claim.
    """
    d = fig.get("data") or {}
    panels = d.get("panels") or []
    if len(panels) != 2:
        raise ValueError(
            "moth-pair figure %r declares %d panel(s). It is a PAIR: the whole "
            "argument is one background against another, and a single panel "
            "shows a moth on some bark and claims nothing."
            % (fig.get("id"), len(panels)))

    barks = [p.get("bark") for p in panels]
    for b in barks:
        if b not in _B11_MOTH_BARKS:
            raise ValueError(
                "moth-pair figure %r asks for bark %r. The drawer paints %s — "
                "and they are a closed set because the two must differ by "
                "PATTERN as well as by tone (mottle against streaks), which is "
                "what makes the drawing work for a reader who cannot separate "
                "the tones." % (fig.get("id"), b, " and ".join(_B11_MOTH_BARKS)))
    if barks[0] == barks[1]:
        raise ValueError(
            "moth-pair figure %r draws %r twice. Both panels on the same bark "
            "is the same photograph printed alongside itself: the thing that "
            "changes between them is the whole diagram."
            % (fig.get("id"), barks[0]))

    for p in panels:
        if not p.get("label"):
            raise ValueError(
                "moth-pair figure %r has a panel with no `label`. The label is "
                "what says WHICH bark this is, in words — without it the two "
                "panels are told apart by their texture alone."
                % fig.get("id"))
        moths = p.get("moths") or []
        tones = [m.get("tone") for m in moths]
        if sorted(tones) != sorted(_B11_MOTH_TONES):
            raise ValueError(
                "moth-pair figure %r puts %r on the %s bark. Both panels carry "
                "the same two moths, once each — the pale one and the dark one "
                "— because the claim is that NOTHING ABOUT THE MOTHS CHANGED "
                "and only the background did."
                % (fig.get("id"), tones, p.get("bark")))
        for m in moths:
            for k in ("label", "note"):
                if not m.get(k):
                    raise ValueError(
                        "moth-pair figure %r has a %s moth on the %s bark with "
                        "no %r. `label` names it and `note` says how easy it is "
                        "to see there — the drawing must never be readable by "
                        "colour alone, and those two words are what make it "
                        "readable without any."
                        % (fig.get("id"), m.get("tone"), p.get("bark"), k))

    PW, PH, GAP, X0, PY = 352, 196, 40, 8, 46
    W = X0 * 2 + PW * 2 + GAP
    H = PY + PH + 106

    out = [_svg_open(fig, W, H)]
    for i, p in enumerate(panels):
        px = X0 + i * (PW + GAP)
        lichen = p["bark"] == "lichen"
        ground = _SVG_BAND if lichen else _SVG_INK
        # ⚖️ THE MOTH OUTLINE AND THE LEADER TAKE THEIR TONE FROM THE BARK, not
        # from the moth. On lichen a hairline is dark; on soot it is light.
        # Both moths in a panel get the same one, so the convention never
        # singles out the camouflaged one — which would give the answer away
        # and delete the exercise.
        line = _SVG_INK_MUTED if lichen else "var(--ks3-on-dark-muted)"

        out.append(_svg_text(px, 26, p["label"], size=13,
                             fill=_SVG_INK_BODY, weight="700", anchor="start",
                             family=_SVG_MONO, spacing="0.06em"))
        out.append('<rect class="ks3-moth-bark" data-bark="%s" x="%d" y="%d" '
                   'width="%d" height="%d" rx="14" '
                   'style="fill:%s;stroke:%s" stroke-width="2"/>'
                   % (e(p["bark"]), px, PY, PW, PH, ground, _SVG_INK))

        # The texture. Mottle against streaks — a different KIND of mark, not a
        # different shade of the same one.
        if lichen:
            for bx, by, rx, ry in _B11_MOTH_LICHEN:
                out.append('<ellipse class="ks3-moth-mottle" cx="%d" cy="%d" '
                           'rx="%d" ry="%d" style="fill:%s"/>'
                           % (px + bx, PY + by, rx, ry, _SVG_INSET))
        else:
            for bx, bw in _B11_MOTH_SOOT:
                out.append('<rect class="ks3-moth-streak" x="%d" y="%d" '
                           'width="%d" height="%d" rx="3" style="fill:%s"/>'
                           % (px + bx, PY + 10, bw, PH - 20, _SVG_INK_BODY))

        for j, m in enumerate(sorted(p["moths"],
                                     key=lambda x: _B11_MOTH_TONES.index(x["tone"]))):
            cx = px + (PW * 0.29 if j == 0 else PW * 0.71)
            cy = PY + 78
            fill = _SVG_BAND if m["tone"] == "pale" else _SVG_INK
            out.append(_moth(cx, cy, m["tone"], fill, line, scale=0.92))
            # The leader, so a camouflaged moth can be FOUND even when it
            # cannot be picked out. Drawn on all four.
            out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                       'style="stroke:%s" stroke-width="1.5" '
                       'stroke-dasharray="3 3"/>'
                       % (cx, cy + 46, cx, PY + PH + 10, line))
            out.append(_svg_text(cx, PY + PH + 32, m["label"], size=14,
                                 fill=_SVG_INK, weight="700",
                                 cls="ks3-moth-label"))
            out.append(_svg_text(cx, PY + PH + 52, m["note"], size=13,
                                 fill=_SVG_INK_MUTED, weight="600",
                                 family=_SVG_MONO, cls="ks3-moth-note"))

    ly = PY + PH + 76
    out.append('<line x1="0" y1="%d" x2="%d" y2="%d" style="stroke:%s" '
               'stroke-width="2"/>' % (ly, W, ly, _SVG_RULE_STRONG))
    out.append(_svg_text(X0, ly + 22,
                         d.get("key")
                         or "the same two moths on both barks — only the "
                            "background changed",
                         size=13, fill=_SVG_INK_BODY, weight="600",
                         anchor="start"))
    out.append('</svg>')
    return "".join(out)
# renderers: ═══ END B10 ═══


# renderers: ═══ BEGIN B11 ═══
# B11 · Evolution, extinction and biodiversity (⊕ MRB-248)
#
# KS3 Biology's last unit. Four instruments, four lessons, and one drawn
# diagram. All four benches are DOM-only and all four are on
# `ks3-block ks3-dark ks3-practical`, measured off Design's own `#s-bench`
# class attribute on all four delivered pages (schema §0.3).
#
# ⚑ AND NOT ONE OF THEM CONTAINS A RANDOM NUMBER, which is load-bearing rather
# than incidental (schema §0.2). B11 teaches a process people wrongly imagine
# to be directed; a stochastic bench lets a student watch a run go "the wrong
# way" and conclude the model is broken, or watch a lucky one and conclude
# selection is a lottery. `selection-runner` is a closed-form recurrence.
# Nothing below calls `random`, and nothing below asks the runtime to.


# ── b11-01 `#s-bench` · advantage-bench ──────────────────────────────────

# ⚖️ DESIGN'S OWN THRESHOLD, AND IT IS READ TWICE. `isDone()` on b11-01 is
# `n >= 3` for `s-bench` AND for `s-three` — the band stop mirrors the bench
# (MRB-249, schema §8) — so this number is not a tuning choice. Three of five
# is the point at which a student has switched the world twice and can have
# seen the same animal at the top and at the bottom of the column, which is
# the whole argument of the lesson.
_B11_AB_THRESHOLD = 3
# Chassis, not content. Design composes the figure as
# `c + '% survive' + (isBest ? ' · best here' : …)`; the schema names the two
# suffixes (`best_suffix`, `worst_suffix`) and names nothing for the middle,
# because the middle is the instrument saying what the number IS. Authoring it
# would let one environment's column read "% survive" and another's read
# "% chance" about the same five animals. Contract R5 cuts both ways: do not
# read a key the schema does not name.
_B11_AB_CHANCE = "% survive"
def _b11_ab_extremes(chances, ids, act_id, env_id):
    """Which subject is best in one column, which is worst — or NEITHER.

    ⛔ THIS IS THE FIX FOR THE `disease` PANEL, and it is the one place in the
    unit where the port departs from Design's own renderer (schema §2). Her
    `isBest` is `c === Math.max(...)`, and `disease` is
    `{big: 45, thick: 45, fast: 45, bold: 30, pale: 45}` — so FOUR of the five
    mice carry `45% survive · best here`, in green, at once, underneath a
    verdict that reads *"None of the visible variations helps."* A panel that
    says no variation helps while painting four green winners teaches the
    opposite of its own sentence, and that panel is the one that sets up rung 4
    and hands off to b11-04.

    ⚖️ SO A COLUMN MARKS NOTHING UNLESS BOTH ENDS ARE UNIQUE. Schema §2 rules
    the tie by suppressing *both* suffixes and *both* colours and leaving every
    bar muted, and this implements exactly that: the trigger it names is a
    non-unique maximum, and a non-unique minimum is the same defect read the
    other way round — two bars sharing an amber "worst here" is as false as
    four sharing a green "best here". Requiring both ends narrows nothing on
    the measured matrix: winter, drought, owl and crowded each have a unique
    maximum AND a unique minimum, and `disease` has neither a unique maximum
    nor a spare reading under which it would acquire one.

    ⚠️ AND IT IS COMPUTED HERE, AT BUILD TIME, not in the browser. Every
    column is a fixed set of authored integers, so the marking is a fact about
    the payload and belongs in the bytes — which also means no science-bearing
    string is ever assigned to `textContent`, and a reader with JS off sees the
    same five rankings a reader with JS on does.
    """
    vals = [int(chances[i]) for i in ids]
    hi, lo = max(vals), min(vals)
    if hi == lo or vals.count(hi) != 1 or vals.count(lo) != 1:
        return None, None
    return ids[vals.index(hi)], ids[vals.index(lo)]
def r_advantage_bench(a, act_id):
    """⊕ b11-01 `#s-bench` — change the world, not the mice.

    ⚖️ THE SAME FIVE ANIMALS IN EVERY PANEL, IN THE SAME ORDER, AND THAT IS
    THE INSTRUMENT. `subjects` is one list read by every environment, so the
    student's eye tracks one row down the bench while the world changes
    underneath it. Design's `MICE` is a top-level constant and each `ENV`
    carries only the numbers; a per-environment roster would let two panels
    disagree about which animals are on the bench, and the reversal rung 3 asks
    about — thick coat 90 in winter, 25 in the drought — would become a
    comparison between two different lists.

    ⚖️ THERE IS NO RUN BUTTON AND NO RESET. Switching *is* the experiment:
    five tabs, each of which sets the environment and records that it has been
    seen. `seen` never shrinks, which is MRB-208's rail rule (the rail records
    participation) and also the honest reading — a student who has looked at
    the drought has looked at the drought.

    ⚠️ EVERY ENVIRONMENT'S PANEL IS IN THE DOCUMENT, hidden, so the shipped
    bytes carry all five verdicts and all twenty-five per-mouse rationales
    rather than having them written in by the runtime. Twenty-five
    individually-written sentences is the largest single body of authored prose
    in this unit and none of it goes through an attribute.

    ⛔ AND THE BENCH MARKS NOTHING (schema §0.7). `best here` and `worst here`
    are the instrument reporting a COLUMN, in words as well as in colour, and
    the student has committed to nothing on this bench — there is no
    prediction here to be right or wrong about. No option button takes a
    verdict class.
    """
    _b7_need(a, act_id, ("tabs_label", "progress_suffix", "best_suffix",
                         "worst_suffix", "subjects", "envs"))

    subjects = a["subjects"]
    # ⚖️ TWO IS THE FLOOR AND IT IS NOT A FORMALITY. `best here` and `worst
    # here` are the ends of a column; a bench of one animal has a column with
    # no ends, and `_b11_ab_extremes` would mark nothing on every environment
    # for ever while the page looked entirely normal.
    if len(subjects) < 2:
        raise ValueError(
            "advantage-bench %r puts %d subject(s) on the bench. The whole "
            "instrument is a RANKING that reshuffles when the world changes, "
            "and a column of one has no top and no bottom to reshuffle."
            % (act_id, len(subjects)))
    sids, seen_s = [], set()
    for s in subjects:
        for f in ("id", "name"):
            if not s.get(f):
                raise ValueError(
                    "advantage-bench %r subject %r declares no %r."
                    % (act_id, s.get("id"), f))
        if s["id"] in seen_s:
            raise ValueError("advantage-bench %r declares subject id %r twice."
                             % (act_id, s["id"]))
        seen_s.add(s["id"])
        sids.append(s["id"])

    envs = a["envs"]
    # ⚖️ THE MIRROR STOP NEEDS THREE (MRB-249, schema §8). Design's `isDone()`
    # for BOTH `s-bench` and `s-three` is `n >= 3` seen, so a bench with fewer
    # than three environments ships two rail stops that can never tick.
    if len(envs) < _B11_AB_THRESHOLD:
        raise ValueError(
            "advantage-bench %r declares %d environment(s). The bench's stage "
            "predicate is %d seen and the `s-three` band stop MIRRORS it "
            "(MRB-249), so a shorter bench ships two rail stops that no "
            "student can ever tick." % (act_id, len(envs), _B11_AB_THRESHOLD))

    tabs, panels, seen_e = [], [], set()
    for i, env in enumerate(envs):
        for f in ("id", "label", "name", "note", "chances", "whys", "verdict"):
            if not env.get(f):
                raise ValueError(
                    "advantage-bench %r environment %r declares no %r. "
                    "`label` is the tab and `name` is the panel headline and "
                    "they are NOT the same string — Design's tab reads 'A hard "
                    "winter' where the panel reads 'A hard winter, snow for "
                    "eight weeks'. `verdict` is the only place this bench says "
                    "what just happened, in words, on cream."
                    % (act_id, env.get("id"), f))
        if env["id"] in seen_e:
            raise ValueError("advantage-bench %r declares environment id %r "
                             "twice." % (act_id, env["id"]))
        seen_e.add(env["id"])

        # ⚠️ MAPS KEYED BY SUBJECT ID, EXACTLY AND IN BOTH DIRECTIONS (schema
        # §1). A MISSING key is a mouse with no survival number; an EXTRA key
        # is a rationale written for an animal that is not on the bench, which
        # is what a rename or a reorder leaves behind and which no rendered
        # page would ever show. Both are checked, because the second is the one
        # that survives review.
        for field in ("chances", "whys"):
            got = set(env[field])
            if got != set(sids):
                raise ValueError(
                    "advantage-bench %r environment %r %s covers %r and the "
                    "bench holds %r. It is a MAP KEYED BY SUBJECT ID, never a "
                    "parallel array, and it is required for every subject: a "
                    "missing key is an animal with no entry in this column, "
                    "and a spare key is a sentence written for an animal that "
                    "is not on the bench and that nothing will ever draw."
                    % (act_id, env["id"], field, sorted(got), sorted(sids)))
        for sid in sids:
            c = env["chances"][sid]
            if not isinstance(c, int) or isinstance(c, bool):
                raise ValueError(
                    "advantage-bench %r environment %r gives %r a survival "
                    "chance of %r. It is a whole percentage — the number is "
                    "printed and it is also the WIDTH of the bar, so a string "
                    "or a fraction draws a plausible row with an impossible "
                    "bar." % (act_id, env["id"], sid, c))
            if not 0 <= c <= 100:
                raise ValueError(
                    "advantage-bench %r environment %r gives %r %d%%. A "
                    "survival chance is 0–100; the bar's width is this number "
                    "as a percentage of its track."
                    % (act_id, env["id"], sid, c))
            if not env["whys"][sid]:
                raise ValueError(
                    "advantage-bench %r environment %r has an empty `why` for "
                    "%r. The sentence under the bar is what makes the number "
                    "mean something — without it the row is a percentage with "
                    "no reason, which is the one thing this bench must never "
                    "teach." % (act_id, env["id"], sid))

        best, worst = _b11_ab_extremes(env["chances"], sids, act_id, env["id"])
        first = i == 0
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-ab-tab" '
            'data-ab-env="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(env["id"]), "true" if first else "false", t(env["label"])))

        rows = []
        for s in subjects:
            sid = s["id"]
            c = int(env["chances"][sid])
            rank = "best" if sid == best else ("worst" if sid == worst else "")
            sfx = (a["best_suffix"] if rank == "best"
                   else a["worst_suffix"] if rank == "worst" else "")
            mark = (' data-ab-rank="%s"' % rank) if rank else ""
            rows.append(
                '<li class="ks3-ab-row">'
                '<div class="ks3-ab-rowhead">'
                '<p class="ks3-ab-name">%s</p>'
                '<p class="ks3-ab-chance"%s>%s</p></div>'
                '<span class="ks3-ab-track">'
                '<span class="ks3-ab-bar"%s style="width:%d%%"></span></span>'
                '<p class="ks3-ab-why">%s</p></li>'
                % (t(s["name"]), mark,
                   t("%d%s%s" % (c, _B11_AB_CHANCE, sfx)), mark, c,
                   t(env["whys"][sid])))

        panels.append(
            '<div class="ks3-ab-env" data-ab-envpanel="%s"%s>'
            '<p class="ks3-ab-envname">%s</p>'
            '<p class="ks3-ab-envnote">%s</p>'
            '<ul class="ks3-ab-rows" role="list">%s</ul>'
            '<p class="ks3-ab-verdict">%s</p></div>'
            % (e(env["id"]), "" if first else " hidden",
               t(env["name"]), t(env["note"]), "".join(rows),
               t(env["verdict"])))

    return ('<div class="ks3-ab" data-ab data-threshold="%d">'
            '<div class="ks3-ab-tabsgroup">'
            '<p class="ks3-ab-tabslabel" id="%s-envs">%s</p>'
            '<ul class="ks3-options ks3-ab-tabs" role="list" '
            'aria-labelledby="%s-envs">%s</ul></div>'
            '<div class="ks3-ab-panel">%s</div></div>'
            % (_B11_AB_THRESHOLD, e(act_id), t(a["tabs_label"]), e(act_id),
               "".join(tabs), "".join(panels)))
# ── b11-02 `#s-bench` · selection-runner ─────────────────────────────────

# ⚖️ DESIGN'S OWN THRESHOLD, READ TWICE. `isDone()` on b11-02 is `gen >= 10`
# for `s-bench` AND for `s-steps` — the band stop mirrors the bench (MRB-249,
# schema §8). Ten is also exactly one press of *Ten generations*, which is the
# point: a student who presses the big button once has seen the thing the
# lesson is about, and `notes.moving` says so in words ("how little changes in
# any single generation and how much has changed after ten").
_B11_NR_THRESHOLD = 10
# ⛔ THE BENCH OPENS ON THE SOOTY BARK, AND THAT IS A TEACHING CHOICE THE
# PAYLOAD DOES NOT CARRY. Design's state is `bark: 'sooty'`, which is
# `BARKS[1]` — the SECOND entry, not the first — and schema §0.4 forbids
# authoring runtime state, so no author writes it down. It is here because it
# has to be somewhere, and it is an ID rather than an index because an index is
# a fact about list order and this is a fact about teaching: the lesson opens
# in industrial Britain, where the population is 90% pale on black bark and one
# press of *Ten generations* shows the sweep this lesson exists to show. Open
# it on clean bark and the same press shows a pale population getting slightly
# paler, which is the same mechanism and none of the point.
#
# ⚠️ A rename fails the build loudly rather than falling back to `barks[0]`,
# which is the whole reason this is not `barks[1]`: a silent fallback opens the
# lesson on the wrong world and nothing anywhere says a word.
_B11_NR_OPENS_ON = "sooty"
def _b11_nr_control(bark):
    """Is this bark THE CONTROL? Measured from the rates, never from the id.

    ⚑ THE CONTROL IS DEFINED BY `pale_surv == dark_surv` AND BY NOTHING ELSE.
    Design tests `s.bark === 'mixed'`, which is the id of the bark that happens
    to carry equal rates on this bench; the property that makes it a control is
    the equality, and `notes.control` says exactly that — *"Neither colour has
    an advantage on patchy bark … without a difference in survival there is no
    selection."* Keying the branch to the id would let a later edit give
    `mixed` unequal rates and go on printing the control's sentence over a
    population that was quietly moving.
    """
    return float(bark["pale_surv"]) == float(bark["dark_surv"])
def _b11_sr_axis_format(a, act_id):
    """`axis_format` — the axis caption, as a template over the DRAWN window.

    MRB-257 (5.40). The chart holds `history` columns and `advance()` shifts
    older entries off the left, so the authored caption's "oldest on the left"
    is true only until generation `history`. After five presses of "Ten
    generations" the head read "generation 50" while column 0 carried a pale
    fraction of 0.9987 — it was generation 27, and generation 0 (at 0.9) had
    gone. Nothing on screen said so, which is the whole change the lesson is
    about disappearing silently.

    ⚠️ Widening the window is NOT the fix available here. `ks3_parity.py`
    asserts that after sixty generations EVERY drawn column equals the
    control's fraction, and that holds only because the window has flushed the
    selecting bark's run — keeping generation 0 on screen turns that gate red.
    Moving both is one coordinated change across two files. Naming the window
    costs nothing and makes the chart honest about what it is showing, which
    is the part that was missing.
    """
    fmt = a.get("axis_format")
    if not fmt:
        raise ValueError(
            "selection-runner %r declares no `axis_format`. The chart is a "
            "sliding window, so a caption that does not name which "
            "generations are on screen is false from generation %s onwards "
            "(5.40)." % (act_id, a.get("history")))
    for slot in ("{from}", "{to}"):
        if slot not in fmt:
            raise ValueError(
                "selection-runner %r `axis_format` %r carries no %s. Both ends "
                "of the window have to be named, or the caption is describing "
                "a window it cannot see." % (act_id, fmt, slot))
    return fmt
def r_selection_runner(a, act_id):
    """⊕ b11-02 `#s-bench` — run the generations, and no moth changes colour.

    ⚖️⚖️ THE MODEL IS A CLOSED-FORM RECURRENCE AND THERE IS NO RANDOMNESS IN
    IT (schema §0.2, §3). Per generation, with pale fraction `p`:

        survivors_pale = p · pale_surv
        survivors_dark = (1 − p) · dark_surv
        p′             = survivors_pale / (survivors_pale + survivors_dark)

    — equivalently the ODDS `p/(1−p)` multiplied by a constant per bark. No
    sampling, no drift, no mutation, no migration. That is load-bearing rather
    than incidental: this lesson teaches a process people wrongly imagine to be
    directed, and a stochastic bench lets a student watch a run go the wrong
    way and conclude the model is broken, or watch a lucky one and conclude
    selection is a lottery. Population size is not modelled at all — only the
    fraction is carried, which is what the page's legal line already says.

    ⚖️ THE THIRD BARK IS THE CONTROL AND IT MUST NOT CREEP. Equal survival
    rates make `p′ = p`, and the runtime short-circuits to exactly that rather
    than dividing — because `p·0.7 / (p·0.7 + (1−p)·0.7)` is NOT bit-for-bit
    `p` in floating point (at p = 0.9 it lands on 0.9000000000000001), and over
    fifty generations a control that drifts in the sixteenth decimal is a
    control that has to be argued for rather than shown. The bench asserts
    exactly one such bark exists: without it there is no panel showing
    selection NOT happening, and that panel is what proves the other two are
    showing selection rather than an animation.

    ⚖️ AND THE BARK TABS DO NOT RESET THE POPULATION. That is Design's, and it
    is the best thing on the bench: run it sooty until the population is 99%
    dark, switch to clean, run it again, and watch it come back — with
    `notes.pale_high` saying in words that selection has no memory and no
    direction. A tab that reset the population would delete that.

    ⛔ THE GEN-0 NOTE IS GATED ON THE POPULATION, NOT ON THE GENERATION
    (schema §3). Design shows `notes.start` — *"Nine moths in ten are pale"* —
    whenever `gen === 0`, and her own reset sets `pale: 0.5, gen: 0`. So
    pressing *Start again at fifty-fifty* displays a fifty-fifty population
    under a sentence saying nine in ten are pale. The port gates `start` on
    `gen === 0 && pale === start_pale` and authors a sixth branch, `reset`, for
    `gen === 0 && pale === reset_pale`.

    ⛔ AND NOTHING HERE MARKS A STUDENT (schema §0.7). The six notes are
    descriptions of a population, not judgements; there is no prediction on
    this bench to be right or wrong about, and no button takes a verdict class.
    """
    _b7_need(a, act_id, ("tabs_label", "barks", "start_pale", "reset_pale",
                         "history_len", "pale_label", "dark_label",
                         "axis_note", "one_label", "ten_label", "reset_label",
                         "notes", "gen_label", "gen_zero_label"))

    barks, ids, controls = a["barks"], [], []
    for b in barks:
        for f in ("id", "label", "note"):
            if not b.get(f):
                raise ValueError(
                    "selection-runner %r bark %r declares no %r. `note` is the "
                    "line at the top of the panel that says what this bark IS "
                    "— soot from coal-burning factories, lichen returning — "
                    "and it is the only place the history behind the numbers "
                    "is stated." % (act_id, b.get("id"), f))
        if b["id"] in ids:
            raise ValueError("selection-runner %r declares bark id %r twice."
                             % (act_id, b["id"]))
        ids.append(b["id"])
        for f in ("pale_surv", "dark_surv"):
            v = b.get(f)
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                raise ValueError(
                    "selection-runner %r bark %r declares %s = %r. The two "
                    "survival rates are the ONLY numbers in the model — the "
                    "whole recurrence is the odds multiplied by "
                    "`pale_surv / dark_surv` — so a missing or non-numeric one "
                    "is not a missing label, it is a bench with no physics."
                    % (act_id, b["id"], f, v))
            if not 0 < float(v) <= 1:
                raise ValueError(
                    "selection-runner %r bark %r has %s = %r. A survival rate "
                    "is a fraction in (0, 1]; at zero every moth of that "
                    "colour dies in one generation and the division below "
                    "loses its denominator the moment the other colour reaches "
                    "fixation." % (act_id, b["id"], f, v))
        if _b11_nr_control(b):
            controls.append(b["id"])

    # ⚖️ EXACTLY ONE CONTROL. Not a formality: the patchy bark is the panel
    # that shows selection NOT happening, and it is what proves the other two
    # are showing selection rather than an animation. With none, every bark
    # moves and a student has nothing to compare a moving population to; with
    # two, "this is the control" is a sentence the bench contradicts by
    # printing it twice about two different worlds.
    if len(controls) != 1:
        raise ValueError(
            "selection-runner %r has %d bark(s) where `pale_surv` equals "
            "`dark_surv` (%r). Exactly one is the CONTROL: equal rates make "
            "the proportion sit exactly where it already was, which is the one "
            "panel showing selection NOT happening — and that panel is what "
            "proves the other two are showing selection rather than an "
            "animation." % (act_id, len(controls), controls))

    if _B11_NR_OPENS_ON not in ids:
        raise ValueError(
            "selection-runner %r declares barks %r and the bench opens on %r, "
            "which is not one of them. The opening bark is a TEACHING CHOICE "
            "the payload does not carry (schema §0.4 forbids authoring runtime "
            "state), so it lives in the renderer — and it raises here rather "
            "than falling back to the first bark, because a silent fallback "
            "opens the lesson in the wrong world and nothing anywhere says a "
            "word." % (act_id, ids, _B11_NR_OPENS_ON))

    # The two opening fractions, and they may not be the same number: they are
    # the DISCRIMINATOR between `notes.start` and `notes.reset`, which is the
    # whole of the gen-0 fix. Equal, the bench would print one of the two
    # sentences for ever and the other would be unreachable.
    for f in ("start_pale", "reset_pale"):
        v = a[f]
        if not isinstance(v, (int, float)) or isinstance(v, bool) \
                or not 0 < float(v) < 1:
            raise ValueError(
                "selection-runner %r declares %s = %r. It is the pale fraction "
                "the bench opens on, strictly between 0 and 1 — at either end "
                "one colour is already extinct and no survival difference can "
                "bring it back." % (act_id, f, v))
    if float(a["start_pale"]) == float(a["reset_pale"]):
        raise ValueError(
            "selection-runner %r opens at %r and resets to the same fraction. "
            "The two numbers are what tell `notes.start` from `notes.reset` "
            "(schema §3) — identical, one of the two sentences can never be "
            "reached and the other is printed over both populations, which is "
            "the defect this port exists to fix."
            % (act_id, a["start_pale"]))

    hist_len = a["history_len"]
    if not isinstance(hist_len, int) or isinstance(hist_len, bool) \
            or hist_len <= _B11_NR_THRESHOLD:
        raise ValueError(
            "selection-runner %r keeps %r columns of history. One press of "
            "*Ten generations* adds %d columns to the opening one, so a "
            "history shorter than that loses the start of the run the student "
            "just watched — and the stage predicate is that same %d."
            % (act_id, hist_len, _B11_NR_THRESHOLD, _B11_NR_THRESHOLD))

    notes = a["notes"]
    for k in ("start", "reset", "control", "dark_high", "pale_high", "moving"):
        if not notes.get(k):
            raise ValueError(
                "selection-runner %r notes declares no %r. Six branches, first "
                "match wins, and the line under the readout is the ONLY place "
                "this bench says anything at all — a missing branch is a "
                "population on screen with nothing said about it. `reset` is "
                "the sixth and it does not exist in Design's delivered bytes: "
                "her reset shows a fifty-fifty population under a sentence "
                "reading 'Nine moths in ten are pale' (schema §3)."
                % (act_id, k))

    tabs = []
    for b in barks:
        on = b["id"] == _B11_NR_OPENS_ON
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-nr-tab" '
            'data-nr-bark="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(b["id"]), "true" if on else "false", t(b["label"])))

    # ⚠️ EVERY BARK'S NOTE IS IN THE DOCUMENT, hidden, rather than written in
    # by the runtime — the same rule the whole unit follows. Nothing
    # science-bearing rides a `data-` attribute or a `textContent` assignment.
    bark_notes = "".join(
        '<p class="ks3-nr-barknote" data-nr-barknote="%s"%s>%s</p>'
        % (e(b["id"]), "" if b["id"] == _B11_NR_OPENS_ON else " hidden",
           t(b["note"])) for b in barks)

    # ⚠️ AND SO IS EVERY NOTE BRANCH. Six paragraphs, one shown.
    note_ps = "".join(
        '<p class="ks3-nr-note" data-nr-note="%s"%s>%s</p>'
        % (e(k), "" if k == "start" else " hidden", t(notes[k]))
        for k in ("start", "reset", "control", "dark_high", "pale_high",
                  "moving"))

    # ⚖️ THE CHART'S COLUMNS ARE DRAWN, ALL `history_len` OF THEM, and the
    # runtime unhides and resizes rather than creating elements. The bench
    # opens on one column at `start_pale` — which is the population before any
    # generation has run, and it is on screen from the first paint so a student
    # can see what the run is starting from.
    start = float(a["start_pale"])
    cols = []
    for i in range(hist_len):
        live = i == 0
        cols.append(
            '<span class="ks3-nr-col" data-nr-col="%d"%s>'
            '<span class="ks3-nr-pale" style="height:%s%%"></span>'
            '<span class="ks3-nr-dark" style="height:%s%%"></span></span>'
            % (i, "" if live else " hidden",
               e(_pctnum(start * 100.0)), e(_pctnum((1.0 - start) * 100.0))))

    model = {"barks": {b["id"]: {"pale": float(b["pale_surv"]),
                                 "dark": float(b["dark_surv"]),
                                 "control": _b11_nr_control(b),
                                 "pale_favoured":
                                     float(b["pale_surv"])
                                     > float(b["dark_surv"])}
                       for b in barks},
             "start": start, "reset": float(a["reset_pale"]),
             "history": hist_len, "opens_on": _B11_NR_OPENS_ON}

    pale_pct = int(round(start * 100))
    return ('<div class="ks3-nr" data-nr data-model="%s" data-threshold="%d">'
            '<div class="ks3-nr-tabsgroup">'
            '<p class="ks3-nr-tabslabel" id="%s-barks">%s</p>'
            '<ul class="ks3-options ks3-nr-tabs" role="list" '
            'aria-labelledby="%s-barks">%s</ul></div>'
            '<div class="ks3-nr-panel">%s'
            '<div class="ks3-nr-chart" data-nr-chart>%s</div>'
            # ⊕ MRB-257 (5.40) — the axis names the WINDOW it is drawing.
            # The chart is a sliding window `history` columns wide, so past
            # generation 23 "oldest on the left" stopped being true: at
            # generation 50 column 0 was generation 27, and the whole change
            # the lesson is about had scrolled off silently. `axis_format`
            # carries {from} and {to}, filled by `wireNaturalRun` on every
            # draw; `axis_note` remains the static half.
            '<p class="ks3-nr-axis" data-nr-axis data-format="%s">%s</p>'
            '<div class="ks3-nr-live">'
            '<p class="ks3-nr-figure" data-nr-series="pale" '
            'data-label="%s">%s</p>'
            '<p class="ks3-nr-figure" data-nr-series="dark" '
            'data-label="%s">%s</p></div>'
            '<div class="ks3-nr-notes" data-nr-notes>%s</div>'
            '<div class="ks3-nr-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-nr-one" '
            'data-nr-run="1">%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-nr-ten" '
            'data-nr-run="%d">%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-nr-reset" '
            'data-nr-reset>%s</button></div></div></div>'
            % (_b9_json(model), _B11_NR_THRESHOLD,
               e(act_id), t(a["tabs_label"]), e(act_id), "".join(tabs),
               bark_notes, "".join(cols),
               e(_b11_sr_axis_format(a, act_id)), t(a["axis_note"]),
               e(_b8_plain(a["pale_label"], act_id, "`pale_label`")),
               t("%s %d%%" % (a["pale_label"], pale_pct)),
               e(_b8_plain(a["dark_label"], act_id, "`dark_label`")),
               t("%s %d%%" % (a["dark_label"], 100 - pale_pct)),
               note_ps,
               t(a["one_label"]), _B11_NR_THRESHOLD, t(a["ten_label"]),
               t(a["reset_label"])))
# ── b11-03 `#s-bench` · pressure-bench ───────────────────────────────────

# ⚖️ DESIGN'S OWN THRESHOLD, READ TWICE. `isDone()` on b11-03 is `n >= 4` for
# `s-bench` AND for `s-risk` — the band stop mirrors the bench (MRB-249, schema
# §8). Four combinations is two moves off the opening pair, which is the least
# that can show the point: a species that shrugs one pressure off and is
# destroyed by another.
_B11_PB_THRESHOLD = 4
# ⛔ THE BENCH OPENS ON THE DORMOUSE UNDER HABITAT LOSS, AND NEITHER IS FIRST
# IN ITS LIST FOR THE SPECIES. Design's state is
# `species: 'dormouse', pressure: 'habitat'`; the dormouse is `SPECIES[1]`.
# Schema §0.4 forbids authoring runtime state, so this lives here — as ids
# rather than indices, because a rename should fail the build rather than
# quietly open the lesson on the brown rat, whose row is green in all five
# columns and teaches nothing on arrival. Habitat loss IS the first pressure,
# and it is named anyway so the opening PAIR is stated in one place: the pair
# is the thing that is seen, and a half-stated pair is how the two drift apart.
_B11_PB_OPENS_SPECIES = "dormouse"
_B11_PB_OPENS_PRESSURE = "habitat"
# The four traits, in Design's order, and the reason `trait_labels` is a list
# rather than a map: the ORDER is the argument. Diet and breeding rate first
# (what the animal does), then range and genetic variation (what it has left to
# fall back on) — which is the order the KEY FACT names them in.
_B11_PB_TRAIT_KEYS = ("diet", "breeding", "range", "variation")
def _b11_plural(suffix, act_id, kind):
    """`"combination(s) tried"` → the singular and the plural, split once.

    ⚠️ THE ENGINE OWNS THE PLURALISATION AND THE AUTHOR OWNS THE NOUN. Design
    writes it inline — `n + ' combination' + (n === 1 ? '' : 's') + ' tried'` —
    and schema §4 and §5 record the authored key as the `(s)` form, which is
    what both authors wrote. Unsplit, the page reads "2 combination(s) tried":
    visible to anyone who opens it and invisible to every gate that does not.

    Splitting here rather than asking for two keys keeps the noun authored
    exactly once, which is the same reason `progress_suffix` exists at all.
    B10's `pea-cross` did this inside its own wire function for "1 seed grown";
    `head_counter`'s `format_one` is that solution generalised, and this is the
    other half of it.
    """
    s = _b8_plain(suffix, act_id, "`progress_suffix`")
    if "(s)" not in s:
        raise ValueError(
            "%s %r declares progress_suffix %r, which carries no `(s)`. This "
            "bench's readout agrees its noun with its count — Design writes "
            "`' combination' + (n === 1 ? '' : 's') + ' tried'` — and the "
            "author writes the noun once, in the `(s)` form the schema "
            "records. Without the marker the singular and the plural are the "
            "same string and the bench reads '1 combinations tried'."
            % (kind, act_id, s))
    return s.replace("(s)", ""), s.replace("(s)", "s")
def _b11_pb_band(score, bands):
    """Which of the three bands a fifty-year outcome falls in.

    ⚑ AMBER IS THE BOTTOM BAND AND IT IS DATA, NOT A MARK. There is no
    prediction on this bench and nothing a student can be wrong about; the
    colour means "this population is in trouble", and the sentence underneath
    says which trouble. Design's thresholds, `bands`, authored rather than
    inlined because they are the line between "coping" and "in trouble" and
    that is a teaching judgement.
    """
    if score >= bands["ok"]:
        return "ok"
    return "mid" if score >= bands["mid"] else "bad"
def r_pressure_bench(a, act_id):
    """⊕ b11-03 `#s-bench` — who survives what.

    ⚖️ TWO AXES, AND THE COMBINATION IS THE UNIT. The student picks a species
    and a pressure independently, and what is recorded as `seen` is the PAIR —
    Design's `seen[species + '-' + pressure]`. That matters: the lesson is not
    "four species" or "five pressures", it is that resilience is a property of
    a species AGAINST a particular pressure, and a bench that counted axis
    presses would tick its stage on a student who had looked at four species
    under one pressure and never seen a row change.

    ⚖️ THE FOUR TRAITS ARE THE EXPLANATION AND THEY ARE ON SCREEN BEFORE THE
    OUTCOME. Diet, breeding rate, range, genetic variation — the same four for
    every species, in the same order, above the divider. The number below the
    divider is then something to be explained rather than something to be
    read, which is what rung 3 asks for.

    ⚠️ ALL TWENTY OUTCOME TEXTS ARE IN THE DOCUMENT, hidden. They are twenty
    individually-written sentences (schema §4) — nothing is generated,
    concatenated or templated, and a paraphrase would be a science edit. None
    of them reaches the page through a `data-` attribute.

    ⚑ THE NOTES' "every species is vulnerable to at least one pressure" DOES
    NOT HOLD, and the numbers are authored as measured anyway (schema §4). The
    brown rat scores 65 or above in all five columns and the herring gull never
    falls below 60, so neither has a cell in the bottom band. That is not a
    defect in the bench: the two generalists are on it BECAUSE they shrug
    almost everything off, and the dormouse/panda contrast is the lesson. It is
    the NOTES sentence that overstates it, and no cell is invented here to make
    the claim true.

    ⛔ AND THE BENCH MARKS NOTHING (schema §0.7). The band colours describe a
    population fifty years on; the student has predicted nothing. No option
    button takes a verdict class.
    """
    _b7_need(a, act_id, ("species_label", "pressure_label", "progress_suffix",
                         "trait_labels", "species", "pressures", "outcomes",
                         "outcome_label", "outcome_suffix", "bands"))

    _b11_plural(a["progress_suffix"], act_id, "pressure-bench")

    labels = a["trait_labels"]
    if len(labels) != len(_B11_PB_TRAIT_KEYS):
        raise ValueError(
            "pressure-bench %r declares %d trait label(s) and every species "
            "carries %d — %s. The list is ORDERED and the order is the "
            "argument: what the animal does, then what it has left to fall "
            "back on, which is the order the KEY FACT names them in."
            % (act_id, len(labels), len(_B11_PB_TRAIT_KEYS),
               ", ".join(_B11_PB_TRAIT_KEYS)))

    bands = a["bands"]
    for k in ("ok", "mid"):
        if not isinstance(bands.get(k), int) or isinstance(bands[k], bool):
            raise ValueError(
                "pressure-bench %r bands declares no integer %r. The two "
                "thresholds are the line between coping and being in trouble, "
                "and they decide the colour of every one of the twenty cells."
                % (act_id, k))
    if not 0 < bands["mid"] < bands["ok"] <= 100:
        raise ValueError(
            "pressure-bench %r declares bands ok=%r, mid=%r. They must satisfy "
            "0 < mid < ok ≤ 100 — inverted, every cell falls in one band and "
            "the bench draws twenty rows in one colour."
            % (act_id, bands["ok"], bands["mid"]))

    pressures, pids = a["pressures"], []
    for pr in pressures:
        for f in ("id", "label", "name", "note"):
            if not pr.get(f):
                raise ValueError(
                    "pressure-bench %r pressure %r declares no %r. `label` is "
                    "the tab and `name` is the headline and they are NOT the "
                    "same string — Design's tab reads 'Habitat loss' where the "
                    "headline reads 'Half the habitat is cleared'."
                    % (act_id, pr.get("id"), f))
        if pr["id"] in pids:
            raise ValueError("pressure-bench %r declares pressure id %r twice."
                             % (act_id, pr["id"]))
        pids.append(pr["id"])

    species, sids = a["species"], []
    for sp in species:
        for f in ("id", "name") + _B11_PB_TRAIT_KEYS:
            if not sp.get(f):
                raise ValueError(
                    "pressure-bench %r species %r declares no %r. The four "
                    "traits are the EXPLANATION of the number below the "
                    "divider, and a blank one is the one thing on this bench a "
                    "student would read as 'nothing is known here'."
                    % (act_id, sp.get("id"), f))
        if sp["id"] in sids:
            raise ValueError("pressure-bench %r declares species id %r twice."
                             % (act_id, sp["id"]))
        sids.append(sp["id"])
        # ⚠️ SCORES ARE A MAP KEYED BY PRESSURE ID, checked in BOTH directions
        # (schema §1). A missing key is a cell with no number; a spare key is a
        # score for a pressure that is not on the bench, which is what a rename
        # leaves behind and which nothing on any page would ever draw.
        if set(sp.get("scores") or {}) != set(pids):
            raise ValueError(
                "pressure-bench %r species %r scores %r and the bench applies "
                "%r. It is a MAP KEYED BY PRESSURE ID, never a parallel array, "
                "and every pressure is required: a parallel array silently "
                "pairs a species with another pressure's number the moment "
                "anyone reorders the list."
                % (act_id, sp["id"], sorted(sp.get("scores") or {}),
                   sorted(pids)))
        for pid in pids:
            v = sp["scores"][pid]
            if not isinstance(v, int) or isinstance(v, bool) \
                    or not 0 <= v <= 100:
                raise ValueError(
                    "pressure-bench %r species %r scores %r under %r. It is a "
                    "whole percentage of the original population 0–100, and it "
                    "is also the WIDTH of the bar."
                    % (act_id, sp["id"], v, pid))

    # ⚠️ TWENTY TEXTS, AND ALL TWENTY ARE REQUIRED. Design's `OUTCOMES` is a
    # full 4 × 5 object literal with nothing shared and nothing templated
    # (schema §4). A missing one is a cell that draws a number and a bar with
    # nothing under them saying what happened — which is the only part of the
    # cell that teaches.
    outcomes = a["outcomes"]
    if set(outcomes) != set(sids):
        raise ValueError(
            "pressure-bench %r writes outcomes for %r and the bench holds %r."
            % (act_id, sorted(outcomes), sorted(sids)))
    for sid in sids:
        if set(outcomes[sid]) != set(pids):
            raise ValueError(
                "pressure-bench %r writes %r's outcomes for %r and the bench "
                "applies %r. All %d are individually written; nothing here is "
                "generated or templated, so a gap cannot be filled in by the "
                "renderer." % (act_id, sid, sorted(outcomes[sid]),
                               sorted(pids), len(sids) * len(pids)))
        for pid in pids:
            if not outcomes[sid][pid]:
                raise ValueError(
                    "pressure-bench %r has an empty outcome for %r under %r."
                    % (act_id, sid, pid))

    for want, got in ((_B11_PB_OPENS_SPECIES, sids),
                      (_B11_PB_OPENS_PRESSURE, pids)):
        if want not in got:
            raise ValueError(
                "pressure-bench %r opens on %r and the bench offers %r. The "
                "opening PAIR is a teaching choice the payload does not carry "
                "(schema §0.4), so it lives in the renderer — and it raises "
                "rather than falling back to the first entry, because the "
                "first species is the brown rat, whose row is in the top band "
                "in all five columns and teaches nothing on arrival."
                % (act_id, want, got))

    sp_tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-pb-tab" '
        'data-pb-species="%s" aria-pressed="%s">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(sp["id"]), "true" if sp["id"] == _B11_PB_OPENS_SPECIES else "false",
           t(sp["name"])) for sp in species)
    pr_tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-pb-tab" '
        'data-pb-pressure="%s" aria-pressed="%s">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(pr["id"]),
           "true" if pr["id"] == _B11_PB_OPENS_PRESSURE else "false",
           t(pr["label"])) for pr in pressures)

    sp_panels = []
    for sp in species:
        traits = "".join(
            '<li class="ks3-pb-trait">'
            '<span class="ks3-pb-traitlabel">%s</span>%s</li>'
            % (t(labels[i]), t(sp[k]))
            for i, k in enumerate(_B11_PB_TRAIT_KEYS))
        sp_panels.append(
            '<div class="ks3-pb-species" data-pb-speciespanel="%s"%s>'
            '<p class="ks3-pb-name">%s</p>'
            '<ul class="ks3-pb-traits" role="list">%s</ul></div>'
            % (e(sp["id"]),
               "" if sp["id"] == _B11_PB_OPENS_SPECIES else " hidden",
               t(sp["name"]), traits))

    pr_panels = "".join(
        '<div class="ks3-pb-pressure" data-pb-pressurepanel="%s"%s>'
        '<p class="ks3-pb-pname">%s</p>'
        '<p class="ks3-pb-pnote">%s</p></div>'
        % (e(pr["id"]),
           "" if pr["id"] == _B11_PB_OPENS_PRESSURE else " hidden",
           t(pr["name"]), t(pr["note"])) for pr in pressures)

    cells = []
    for sp in species:
        for pr in pressures:
            score = int(sp["scores"][pr["id"]])
            band = _b11_pb_band(score, bands)
            live = (sp["id"] == _B11_PB_OPENS_SPECIES
                    and pr["id"] == _B11_PB_OPENS_PRESSURE)
            cells.append(
                '<div class="ks3-pb-cell" data-pb-cell="%s|%s"%s>'
                '<div class="ks3-pb-outrow">'
                '<p class="ks3-pb-outlabel">%s</p>'
                '<p class="ks3-pb-outpct" data-pb-band="%s">%s</p></div>'
                '<span class="ks3-pb-track">'
                '<span class="ks3-pb-bar" data-pb-band="%s" '
                'style="width:%d%%"></span></span>'
                '<p class="ks3-pb-why">%s</p></div>'
                % (e(sp["id"]), e(pr["id"]), "" if live else " hidden",
                   t(a["outcome_label"]), e(band),
                   t("%d%s" % (score, a["outcome_suffix"])), e(band), score,
                   t(outcomes[sp["id"]][pr["id"]])))

    return ('<div class="ks3-pb" data-pb data-threshold="%d" '
            'data-opens-on="%s|%s">'
            '<div class="ks3-pb-tabsets">'
            '<div class="ks3-pb-tabsgroup">'
            '<p class="ks3-pb-tabslabel" id="%s-species">%s</p>'
            '<ul class="ks3-options ks3-pb-tabs" role="list" '
            'aria-labelledby="%s-species">%s</ul></div>'
            '<div class="ks3-pb-tabsgroup">'
            '<p class="ks3-pb-tabslabel" id="%s-pressures">%s</p>'
            '<ul class="ks3-options ks3-pb-tabs" role="list" '
            'aria-labelledby="%s-pressures">%s</ul></div></div>'
            '<div class="ks3-pb-panel">%s'
            '<div class="ks3-pb-under">%s%s</div></div></div>'
            % (_B11_PB_THRESHOLD, e(_B11_PB_OPENS_SPECIES),
               e(_B11_PB_OPENS_PRESSURE),
               e(act_id), t(a["species_label"]), e(act_id), sp_tabs,
               e(act_id), t(a["pressure_label"]), e(act_id), pr_tabs,
               "".join(sp_panels), pr_panels, "".join(cells)))
# ── b11-04 `#s-bench` · blight-bench ─────────────────────────────────────

# ⚖️ DESIGN'S OWN THRESHOLD, READ TWICE. `isDone()` on b11-04 is `n >= 2` for
# `s-bench` AND for `s-banks` — the band stop mirrors the bench (MRB-249,
# schema §8). Two fields is the least that makes a comparison, and the
# comparison is the lesson: one field where nothing survives, and one where
# something does.
_B11_BB_THRESHOLD = 2
# ⛔ THE BENCH OPENS ON THE CLONE FIELD, which IS the first entry — Design's
# `field: 'clone'`. Named rather than left to list order for the same reason
# the other three opening states are: the choice is a teaching one. The clone
# is the field where nothing survives, and opening on it means the student's
# first press of *Release the blight* is the one that returns exactly zero.
_B11_BB_OPENS_ON = "clone"
# ⚖️ THE SURVIVOR BAND, AND IT IS NOT AUTHORED. Design's rule is
# `pct === 0 ? alert : (pct >= 50 ? ok : muted)` — three bands with a bespoke
# ZERO at the bottom, which is the whole point of the clone field: it does not
# do badly, it returns nothing. A `bands` key here would let a record ship a
# clone field painted muted, and the one number this lesson exists to show
# would stop being special.
_B11_BB_OK_PCT = 50
def _b11_bb_band(pct):
    """The survivor row's band. Zero is its own band, not the bottom of one."""
    if pct == 0:
        return "none"
    return "ok" if pct >= _B11_BB_OK_PCT else "mid"
def r_blight_bench(a, act_id):
    """⊕ b11-04 `#s-bench` — plant it, then release the blight.

    ⚖️⚖️ THE CLONE FIELD RETURNS EXACTLY ZERO, BY CONSTRUCTION AND NOT BY
    ROUNDING (schema §5). `survivors = round(total × resistant / varieties)`
    with `resistant: 0` over `varieties: 1` is zero along every arithmetic
    path — there is no route to a single survivor. That number is the payoff of
    the whole lesson, and the renderer asserts it rather than trusting it: a
    field with no resistant variety must come out at zero, and the bench must
    hold one.

    ⚖️ THE TRADE-OFF IS THE SECOND BAR RUNNING AGAINST THE THIRD. Variation
    9 → 36 → 90 → 100 against yield 100 → 85 → 85 → 55: monotone opposite at
    the two ends and deliberately TIED in the middle, because the trade-off
    bites at the extremes rather than smoothly across the range. Both bars are
    authored per field rather than derived from the id — Design derives them
    with `f.id === 'clone' ? … : (f.id === 'landrace' ? … : …)`, so a fifth
    field would fall silently into her `else` and be drawn as "good / 85".

    ⚖️ SWITCHING FIELD RE-ARMS THE BLIGHT AND *Clear the field* DOES NOT
    UNTICK ANYTHING. `released` is cleared by both; `tried` is cleared by
    neither. That is MRB-208 in the instrument: a student who has released the
    blight on two fields has done it, and clearing a field is using the bench.

    ⚠️ BOTH STATES OF EVERY FIELD ARE IN THE DOCUMENT, hidden — the harvest
    before the blight (a thousand of a thousand) and after it — so the shipped
    bytes carry all four verdicts and both survivor rows for each field, and
    nothing science-bearing is written in by the runtime.

    ⛔ AND THE BENCH MARKS NOTHING (schema §0.7). The amber on a zero-survivor
    bar means "nothing came through", not "you were wrong"; the student has
    predicted nothing here. No option button takes a verdict class.
    """
    _b7_need(a, act_id, ("tabs_label", "progress_suffix", "progress_zero",
                         "total", "fields", "bar_labels", "bar_label_before",
                         "run_label",
                         "ran_label", "reset_label", "verdicts"))

    _b11_plural(a["progress_suffix"], act_id, "blight-bench")

    total = a["total"]
    if not isinstance(total, int) or isinstance(total, bool) or total <= 0:
        raise ValueError(
            "blight-bench %r plants %r. The total is the denominator of every "
            "survivor count and the '%s of %s' the row prints, so it is a "
            "whole number of plants." % (act_id, total, total, total))

    labels = a["bar_labels"]
    if len(labels) != 3:
        raise ValueError(
            "blight-bench %r declares %d bar label(s) and the field draws "
            "three — what survived, how much variation was in the ground, and "
            "what the field yields in a year with no blight. The third is the "
            "COST, and a bench that drops it teaches that variation is free."
            % (act_id, len(labels)))
    # MRB-257 (5.41) — the survivor row's BEFORE label. The row is drawn in
    # both states and only one of them is about survival; sharing one string
    # made the resting page report a thousand plants surviving a blight that
    # had not been released.
    before_label = a.get("bar_label_before")
    if not before_label:
        raise ValueError(
            "blight-bench %r declares no `bar_label_before`. The survivor row "
            "is drawn before the blight as well as after it, and before it "
            "the number is a count of what was PLANTED — labelling it "
            "'%s' says a thousand plants survived something that has not "
            "happened (5.41)." % (act_id, labels[0]))

    fields, fids, zeroes = a["fields"], [], []
    for f in fields:
        for k in ("id", "label", "name", "note", "variation_word",
                  "yield_word"):
            if not f.get(k):
                raise ValueError(
                    "blight-bench %r field %r declares no %r. `variation_word` "
                    "and `yield_word` are AUTHORED PER FIELD (schema §5) "
                    "because Design derives them from the id with a ternary "
                    "chain — a fifth field falls into her `else` and is drawn "
                    "as 'good / 85' with nothing raised."
                    % (act_id, f.get("id"), k))
        if f["id"] in fids:
            raise ValueError("blight-bench %r declares field id %r twice."
                             % (act_id, f["id"]))
        fids.append(f["id"])
        for k in ("varieties", "resistant", "variation_bar", "yield_bar"):
            v = f.get(k)
            if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                raise ValueError(
                    "blight-bench %r field %r declares %s = %r. All four are "
                    "whole non-negative numbers: two of them are counts of "
                    "plants and two of them are bar widths."
                    % (act_id, f["id"], k, v))
        if f["varieties"] < 1:
            raise ValueError(
                "blight-bench %r field %r plants %d varieties. It is the "
                "DIVISOR in `total × resistant / varieties`."
                % (act_id, f["id"], f["varieties"]))
        if f["resistant"] > f["varieties"]:
            raise ValueError(
                "blight-bench %r field %r plants %d varieties and %d of them "
                "resist. More resistant varieties than varieties is a survivor "
                "count above the total and a bar wider than its track."
                % (act_id, f["id"], f["varieties"], f["resistant"]))
        for k in ("variation_bar", "yield_bar"):
            if not 0 <= f[k] <= 100:
                raise ValueError(
                    "blight-bench %r field %r declares %s = %d. It is a "
                    "percentage of the track." % (act_id, f["id"], k, f[k]))
        if f["resistant"] == 0:
            zeroes.append(f["id"])

    # ⚖️ ONE FIELD WHERE NOTHING SURVIVES, AND THE BENCH MUST HOLD ONE. It is
    # the payoff of the lesson and the thing every other field is compared
    # against; a bench of four fields that all return something teaches that
    # monoculture is a bad bet rather than that it is a total loss.
    if not zeroes:
        raise ValueError(
            "blight-bench %r has no field where every plant dies. `resistant: "
            "0` over `varieties: 1` returns EXACTLY zero by construction, and "
            "that zero is the payoff of this lesson — the Irish potato crop, "
            "the Gros Michel. Without it the bench shows four different bad "
            "harvests and nothing that is a total loss." % (act_id))

    verdicts = a["verdicts"]
    if set(verdicts) != set(fids):
        raise ValueError(
            "blight-bench %r writes verdicts for %r and plants %r. It is keyed "
            "BY FIELD ID with every field written out (schema §5), even where "
            "two fields carry identical text — Design has one shared `else` "
            "for the middle two, and a fifth field would inherit a verdict "
            "written for somebody else."
            % (act_id, sorted(verdicts), sorted(fids)))

    if _B11_BB_OPENS_ON not in fids:
        raise ValueError(
            "blight-bench %r plants %r and the bench opens on %r. The opening "
            "field is a teaching choice the payload does not carry (schema "
            "§0.4): it is the field where NOTHING survives, so the student's "
            "first release is the one that returns zero."
            % (act_id, fids, _B11_BB_OPENS_ON))

    tabs, panels = [], []
    for f in fields:
        first = f["id"] == _B11_BB_OPENS_ON
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-bb-tab" '
            'data-bb-field="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(f["id"]), "true" if first else "false", t(f["label"])))

        survivors = int(round(total * (f["resistant"] / float(f["varieties"]))))
        pct = int(round(survivors / float(total) * 100))
        if f["resistant"] == 0 and survivors != 0:
            raise ValueError(
                "blight-bench %r field %r has no resistant variety and %d "
                "plants survived. Zero over anything is zero along every "
                "arithmetic path, so this is the rounding having been given "
                "something to round." % (act_id, f["id"], survivors))

        # ⚠️ `{pct}` IS SUBSTITUTED HERE, AT BUILD TIME, because the number is
        # a property of the field and not of the run — the same field always
        # returns the same percentage. Design interpolates it in her shared
        # `else` branch, which is why the two middle fields already print
        # different sentences from identical templates. A verdict that still
        # carries a brace after this has named a placeholder nothing fills, and
        # would ship the brace to the page.
        verdict = verdicts[f["id"]].replace("{pct}", str(pct))
        if "{" in verdict:
            raise ValueError(
                "blight-bench %r field %r's verdict still carries a "
                "placeholder after substitution: %r. The only one this bench "
                "fills is `{pct}`." % (act_id, f["id"], verdict))

        # ⚖️ THE SURVIVOR ROW HAS TWO STATES AND BOTH ARE DRAWN. Before the
        # blight every plant is standing — Design's `s.released ? … : TOTAL` —
        # and the row reads a full green bar at "1000 of 1000". That is what
        # makes the release mean something: the student watches a full field
        # become an empty one rather than watching an empty one appear.
        # ⊕ MRB-257 (5.41) — THE TWO STATES NEED TWO LABELS. Both rows shipped
        # `bar_labels[0]`, so on load — with nothing released — the bench read
        # "Plants surviving the blight — 1000 of 1000" under a full green bar,
        # about a blight that had not happened. The before row is a count of
        # what was planted; only the after row is a count of survivors.
        rows = []
        row_labels = {"before": before_label, "after": labels[0]}
        for state, n in (("before", total), ("after", survivors)):
            p = int(round(n / float(total) * 100))
            band = _b11_bb_band(p)
            rows.append(
                '<li class="ks3-bb-row" data-bb-surv="%s"%s>'
                '<div class="ks3-bb-rowhead">'
                '<p class="ks3-bb-barname">%s</p>'
                '<p class="ks3-bb-value" data-bb-band="%s">%s</p></div>'
                '<span class="ks3-bb-track">'
                '<span class="ks3-bb-bar" data-bb-band="%s" '
                'style="width:%d%%"></span></span></li>'
                % (e(state), "" if state == "before" else " hidden",
                   t(row_labels[state]), e(band),
                   t("%d of %d" % (n, total)), e(band), p))

        # The other two bars never move: how much variation went into the
        # ground, and what the field yields in a year with no blight. They are
        # facts about what was PLANTED, and the blight does not change them —
        # which is exactly why the trade-off is legible.
        for i, (word, width, tone) in enumerate((
                (f["variation_word"], f["variation_bar"], "muted"),
                (f["yield_word"], f["yield_bar"], "cost"))):
            rows.append(
                '<li class="ks3-bb-row">'
                '<div class="ks3-bb-rowhead">'
                '<p class="ks3-bb-barname">%s</p>'
                '<p class="ks3-bb-value">%s</p></div>'
                '<span class="ks3-bb-track">'
                '<span class="ks3-bb-bar" data-bb-tone="%s" '
                'style="width:%d%%"></span></span></li>'
                % (t(labels[i + 1]), t(word), e(tone), width))

        panels.append(
            '<div class="ks3-bb-field" data-bb-fieldpanel="%s"%s>'
            '<p class="ks3-bb-name">%s</p>'
            '<p class="ks3-bb-note">%s</p>'
            '<ul class="ks3-bb-rows" role="list">%s</ul>'
            '<p class="ks3-bb-verdict" data-bb-verdict hidden>%s</p></div>'
            % (e(f["id"]), "" if first else " hidden", t(f["name"]),
               t(f["note"]), "".join(rows), t(verdict)))

    # ⚠️ THE RELEASE BUTTON SHIPS LIVE and the verdict ships hidden: the
    # resting page is a planted field that has not met the blight yet. Design
    # disables the button only once it has been pressed.
    return ('<div class="ks3-bb" data-bb data-threshold="%d" '
            'data-run-label="%s" data-ran-label="%s">'
            '<div class="ks3-bb-tabsgroup">'
            '<p class="ks3-bb-tabslabel" id="%s-fields">%s</p>'
            '<ul class="ks3-options ks3-bb-tabs" role="list" '
            'aria-labelledby="%s-fields">%s</ul></div>'
            '<div class="ks3-bb-panel">%s'
            '<div class="ks3-bb-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-bb-run" '
            'data-bb-run>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-bb-clear" '
            'data-bb-clear>%s</button></div></div></div>'
            % (_B11_BB_THRESHOLD,
               e(_b8_plain(a["run_label"], act_id, "`run_label`")),
               e(_b8_plain(a["ran_label"], act_id, "`ran_label`")),
               e(act_id), t(a["tabs_label"]), e(act_id), "".join(tabs),
               "".join(panels), t(a["run_label"]), t(a["reset_label"])))


# ── registrations ────────────────────────────────────────────────────────
ART = {
    'moth-pair': _moth_pair,
}

KIND_SHELL = {
    'advantage-bench': ("ks3-ab-block",
                        ' data-instrument data-abblock data-stage-done="0"'),
    'selection-runner': ("ks3-nr-block",
                         ' data-instrument data-nrblock data-stage-done="0"'),
    'pressure-bench': ("ks3-pb-block",
                        ' data-instrument data-pbblock data-stage-done="0"'),
    'blight-bench': ("ks3-bb-block",
                        ' data-instrument data-bbblock data-stage-done="0"'),
}

KIND_FN = {
    'advantage-bench': r_advantage_bench,
    'selection-runner': r_selection_runner,
    'pressure-bench': r_pressure_bench,
    'blight-bench': r_blight_bench,
}

KIND_HEAD_START = {
    'advantage-bench': 1,
}

KIND_HEAD_TOTAL = {
    'advantage-bench': lambda a: len(a.get("envs") or []),
}

KIND_HEAD_FROM = {
    'advantage-bench': lambda a: {
        "format": "{n} of {total} %s" % _b10_suffix(a, "advantage-bench")},
    'selection-runner': lambda a: {
        "format": "%s{n}" % _b8_plain(a.get("gen_label") or "", a.get("id")
                                      or "?", "`gen_label`"),
        "zero": a.get("gen_zero_label") or "", "start": 0},
    'pressure-bench': lambda a: (lambda one, many: {
        "format": "{n} %s" % many, "format_one": "{n} %s" % one, "start": 1})(
            *_b11_plural(a.get("progress_suffix") or "",
                         a.get("id") or "?", "pressure-bench")),
    'blight-bench': lambda a: (lambda one, many: {
        "format": "{n} %s" % many, "format_one": "{n} %s" % one,
        "zero": a.get("progress_zero") or "", "start": 0})(
            *_b11_plural(a.get("progress_suffix") or "",
                         a.get("id") or "?", "blight-bench")),
}
