# DISPATCH: "gut-journey": ("ks3-gut-block", ' data-instrument data-gutblock data-stage-done="0"'),
#
# and in `ACTIVITY_KIND_FN`, beside the other B3 rows:
#     "gut-journey":            r_gut_journey,
#
# Place `r_gut_journey` beside `r_clinic_cases`. Needs `e`, `t` and `rich`.
#
# ⚠️ THE THREE TILE LABELS AND THE NOTE LABEL ARE AUTHORED, not literals here.
# They are student-facing copy ("Molecules broken here", "Worth knowing:") and
# the same argument that keeps a reveal's sentences out of the engine keeps
# these out of it: a label that lives in Python cannot be corrected by the
# person who owns the science.


def r_gut_journey(a, act_id):
    """⊕ b3-05 `#s-journey` — seven stops, and a time chart that argues.

    ⚖️ THE CHART IS THE ARGUMENT, NOT A DECORATION, and it is why this is not
    `job-sort`, `verdict-cards` or the board. Those are runs of judgements;
    this is one journey with a quantity attached to each leg, and the quantity
    contradicts the intuition — the stomach, which every student names first,
    holds the meal about four hours, and the small intestine holds it sixteen.
    A tabbed panel set with no chart under it would teach the seven organs and
    lose the only thing the lesson is built to overturn.

    ⚖️ EVERY BAR COMES OUT OF `hours`, AT BUILD TIME. The widths are a pure
    function of the authored numbers against the longest of them, so the bar
    and the printed figure beside it cannot disagree — Design's page computes
    the width in one place and the printed string in another, from the same
    field, which is two chances for one number. Nothing in the wiring builds a
    width; the runtime moves the HIGHLIGHT and nothing else.

    ⚠️ `chart_name` AND `chart_hours` ARE AUTHORED, and Design derives both.
    Its chart name is `label.split(',')[0]` — which turns "Pancreas, liver,
    gall bladder" into "Pancreas" and would silently truncate any future stop
    whose label carries a comma for a different reason. Its hours string is a
    three-branch expression (`0 → '—'`, `<1 → '<1 h'`, else `n + ' h'`), which
    is a sentence about the data assembled in JS. Both are strings a student
    reads; both are authored once, here, where the science owner can see them.

    ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument class at
    (0,1,0), so every colour rule in the stylesheet is scoped `.ks3-dark …`.
    The tiles are what would visibly break: three labels and three values in
    one undifferentiated on-dark body colour is a panel that has lost its
    structure, and it looks tidy.

    Emit-all-show-one: seven stop panels are in the document and one is shown.
    Going back to a stop finds it exactly as it was, no state lives anywhere
    but the DOM, and none of the fourteen authored sentences — several of which
    carry em dashes, a right single quote and a superscript ² — is ever rebuilt
    in JS from an attribute.
    """
    stops = a.get("stops") or []
    if len(stops) < 2:
        raise ValueError(
            "gut-journey %r declares %d stop(s). The block is a journey and "
            "one stop is a destination." % (act_id, len(stops)))

    tiles = a.get("tile_labels") or {}
    for key in ("time", "breaks", "absorbs"):
        if not tiles.get(key):
            raise ValueError(
                "gut-journey %r tile_labels is missing %r. All three tiles are "
                "drawn on every stop and an unlabelled one renders as a bare "
                "value with nothing saying what it is." % (act_id, key))

    chart = a.get("chart") or {}
    for key in ("label", "close"):
        if not chart.get(key):
            raise ValueError(
                "gut-journey %r chart is missing %r. Without the closing line "
                "the chart is seven bars and no argument." % (act_id, key))

    for s in stops:
        missing = [k for k in ("id", "label", "name", "kind", "time", "breaks",
                               "absorbs", "what", "note", "chart_name",
                               "chart_hours")
                   if not s.get(k)]
        if missing:
            raise ValueError(
                "gut-journey %r stop %r is missing %s. Every one is drawn, and "
                "an empty one renders as a gap in the panel."
                % (act_id, s.get("id"), ", ".join(missing)))
        if "hours" not in s:
            raise ValueError(
                "gut-journey %r stop %r declares no `hours`. The bar widths "
                "are derived from it; a stop with none has no place on the "
                "chart the block is built around." % (act_id, s["id"]))

    # ⚖️ ONE scale for all seven, taken from the data rather than authored, so
    # a corrected transit time re-scales the whole chart in one edit.
    longest = max(float(s["hours"]) for s in stops) or 1.0

    tabs = "".join(
        '<li><button type="button" class="ks3-gut-tab" data-stop="%s" '
        'aria-pressed="%s">'
        '<span class="ks3-gut-tabnum">%s</span>'
        '<span class="ks3-gut-tablabel">%s</span></button></li>'
        % (e(s["id"]), "true" if i == 0 else "false",
           t("%02d" % (i + 1)), t(s["label"]))
        for i, s in enumerate(stops))

    panels = []
    for i, s in enumerate(stops):
        cells = "".join(
            '<div class="ks3-gut-tile" data-tile="%s">'
            '<p class="ks3-gut-tilelabel">%s</p>'
            '<p class="ks3-gut-tilevalue">%s</p></div>'
            % (key, t(tiles[key]), t(s[val]))
            for key, val in (("time", "time"), ("breaks", "breaks"),
                             ("absorbs", "absorbs")))
        panels.append(
            '<div class="ks3-gut-stop" data-stop="%s"%s>'
            '<div class="ks3-gut-stophead" role="status">'
            '<p class="ks3-gut-name">%s</p>'
            '<p class="ks3-gut-kind">%s</p></div>'
            '<p class="ks3-gut-what">%s</p>'
            '<div class="ks3-gut-tiles">%s</div>'
            '<p class="ks3-gut-note"><strong>%s</strong> %s</p></div>'
            % (e(s["id"]), "" if i == 0 else " hidden",
               t(s["name"]), t(s["kind"]), rich(s["what"]), cells,
               t(a.get("note_label") or "Worth knowing:"), rich(s["note"])))

    rows = "".join(
        '<li class="ks3-gut-row" data-stop="%s"%s>'
        '<span class="ks3-gut-rowname">%s</span>'
        '<span class="ks3-gut-track">'
        '<span class="ks3-gut-bar" style="width:%s%%"></span></span>'
        '<span class="ks3-gut-rowhours">%s</span></li>'
        % (e(s["id"]), ' data-lit="1"' if i == 0 else "",
           t(s["chart_name"]),
           ("%.1f" % (float(s["hours"]) / longest * 100)),
           t(s["chart_hours"]))
        for i, s in enumerate(stops))

    return ('<div class="ks3-gut" data-gut data-total="%d">'
            '<ol class="ks3-gut-tabs">%s</ol>'
            '<div class="ks3-gut-stops">%s</div>'
            '<div class="ks3-gut-chart">'
            '<p class="ks3-gut-chartlabel">%s</p>'
            '<ul class="ks3-gut-rows">%s</ul>'
            '<p class="ks3-gut-chartclose">%s</p></div></div>'
            % (len(stops), tabs, "".join(panels),
               t(chart["label"]), rows, rich(chart["close"])))
