"""ks3_art.p2 — P2 *Energy at home*, the unit where energy becomes a bill.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p2/`. Her page wins outright: a shape that is not
in her drawing is not in this module, and where her NOTES and her drawing
disagree the drawing is measured and the note is reported.

── ⚠️ ONE OF HER FIVE PAGES HIDES ITS MARKUP ──────────────────────────────

`p2-02-power-ratings-in-watts.dc.html` is a 697 KB `__bundler` container —
the only file in the whole P1/P2/P3 tree carrying that signature. What is and
is not readable in it was MEASURED rather than assumed, because the first
version of this note overstated it:

    readable as plain text   `const RAIL`, `SORT_CARDS`, `RUNGS`,
                             `cfifaExamples` — the whole `data-dc-script`
                             block sits in the outer file unencoded, which is
                             why `ks3_rail_manifest.py` reads this lesson's
                             four rail stops correctly with no special case
    NOT readable             every line of MARKUP. The page body is a JSON
                             string literal inside
                             `<script type="__bundler/template">`, on ONE
                             line, with every quote escaped

So `grep 'id="s-'` returns 0 (the file has `id=\"s-`), and any per-occurrence
count of a class name collapses to 1 because `grep -c` counts LINES and the
whole body is one line. Both look like findings about the lesson and are
really artefacts of the container.

It was unpacked; the decoded page is committed as
`p2-02-power-ratings-in-watts.DECODED.html` and is what this module measured
for markup. ⚠️ The manifest glob is `*/*.dc.html`, so the decoded file takes
no manifest row of its own and none of the counts double.

── ⚖️ MRB-204 · TRIANGLE, BEAM — CHECKED PER BLOCK ────────────────────────

P2 carries four formula blocks and they are NOT all the same shape, because
the arithmetic under them is not the same:

    p2-01  E = e × m                         a PRODUCT   TRIANGLE
    p2-02  E = P × t                         a PRODUCT   TRIANGLE
    p2-03  E = P × t                         a PRODUCT   TRIANGLE
    p2-04  one row = P × t                   a PRODUCT   TRIANGLE (on the pan)
           amount due = Σ rows + standing    a SUM       BALANCE BEAM

`p2-04` is the one that makes the rule visibly necessary rather than
pedantic: a product and a sum inside a single calculation, and Design draws
both, captioning her own beam *"A SUM OF PRODUCTS — TRIANGLE FOR ONE ROW,
BALANCE FOR THE TOTAL"*. A triangle over the bill's total would teach a
relationship that does not exist.

`p2-05` has no calculable relationship at its centre and carries no formula
figure at all. That is a measurement of her page, not an omission.

Arrows inside a formula block are SVG. Typed arrows stay in prose.

── ⚠️ RESERVED PAYLOAD KEYS ───────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` itself and those
four have NO opt-out — an instrument whose payload carries one gets two
renderers and the block ships doubled. Nothing here uses `cards`, `sim` or
`scorecards`; `fifa` appears ONLY on `worked-example` activities, which is
the kind that branch exists to draw. The sorters' items are `sort_items` and
the bill's rows are `rows`, never `cards`.

── ⚠️ BAND VALUES ─────────────────────────────────────────────────────────

Where a band appears it is the full word — `easier`, `standard`, `harder`.
Never `s` or `h`.

── ⚠️ Ω IS U+03A9 ─────────────────────────────────────────────────────────

Not U+2126. No ohms arise in P2, but the rule is stated here because P8 will
inherit this module's conventions.
"""

import re

from ks3_art.kit import e, rich, t


# ═══ shared P2 primitives ════════════════════════════════════════════════

def _p2_seg(cls, label, pressed=False, **attrs):
    """A segmented-control button, the shape every P2 bench picks from."""
    bits = "".join(' %s="%s"' % (k.replace("_", "-"), e(str(v)))
                   for k, v in sorted(attrs.items()))
    return ('<button type="button" class="%s" aria-pressed="%s"%s>%s</button>'
            % (e(cls), "true" if pressed else "false", bits, t(label)))


def _unique_ids(rows, act_id, family, what):
    """Two rows sharing an id makes one of them unreachable, silently."""
    seen, dupes = set(), []
    for r in rows:
        rid = r.get("id")
        if rid in seen:
            dupes.append(rid)
        seen.add(rid)
    if dupes:
        raise ValueError(
            "%s %r has two %ss with id %s. The second is unreachable and the "
            "failure is silent." % (family, act_id, what, sorted(set(dupes))))


def _no_correct_flags(rows, act_id, family):
    """A `correct` key on a bench row is an answer key in a payload."""
    for r in rows:
        if "correct" in r:
            raise ValueError(
                "%s %r carries a `correct` flag on row %r. A bench measures; "
                "it does not mark." % (family, act_id, r.get("id")))


# ═══ p2-01 · #s-burn · the calorimeter ═══════════════════════════════════

def r_calorimeter(a, act_id):
    """⊕ p2-01 `#s-burn` — burn a weighed sample, watch 20 g of water.

    Design's bench. Four foods, a mass slider, a burn that consumes the
    sample a step at a time, and a table that records what each run
    measured — deliberately well below the label.

    ⚖️ **THE CAPTURE FRACTIONS ARE THE LESSON.** 0.30 to 0.42, so the bench
    reads 30–42% of the packet figure. Rung 3's fifth criterion — that
    repeating a measurement does nothing about a systematic leak — can
    only be answered by a student who has watched their own value come out
    low. The renderer refuses a capture fraction of 1.0 for that reason.

    ⊕ MRB-297 · 1 Sep 2026 — this said "AND THEY ARE HERS, UNCHANGED. 0.30
    to 0.46, so the bench reads 30–46%". Three of the four are still hers
    and unchanged; the 0.46 was the peanut's, and the peanut was ruled out
    of the practical on 30 Aug 2026. The cheese puff that replaced it
    carries 0.38, so the set is 0.30, 0.34, 0.38, 0.42 and the range closes
    at 0.42. See D-P2-02.

    ⚖️ **THE MEASURED PER-GRAM VALUE IS COMPUTED, NEVER AUTHORED.**
    `measured = (rise × water × shc / 1000) ÷ consumed`, which reduces to
    `kJ/g × capture × scatter`. Authoring it would allow a row where the
    lesson's central claim silently fails to hold.

    ⚠️ **THE SAMPLE MASS IS THE ONE DEPARTURE IN THIS UNIT — D-P2-01.**
    Design's slider runs 5 g to 30 g against 20 g of water. Her own
    arithmetic then puts the thermometer between 295 °C and 4469 °C, in
    EVERY state the instrument can reach, including its minimum; and her own
    canvas draws warmth as `min(1, rise / 60)`, so the drawing is built for
    rises up to 60 °C while the readout says 1618. The range is 0.10–0.50 g
    here. Nothing else moves, and because the measured per-gram value is
    independent of the mass, no teaching number moves either. Full row in
    `docs/ks3/design-reference/p2/DEPARTURES-P2.md`.

    HOOKS: `data-calor` (wrapper, `data-water`, `data-shc`, `data-target`) ·
    `data-calor-gate` · `data-calor-gopt` · `data-calor-bench` ·
    `data-calor-food` (valued with the food index) · `data-calor-mass` (the
    slider) · `data-calor-masslabel` · `data-calor-burn` ·
    `data-calor-fresh` · `data-calor-record` · `data-calor-out` (valued with
    the readout id) · `data-calor-rows` · `data-calor-note` ·
    `data-calor-close`.
    """
    gate = a.get("gate") or {}
    foods = a.get("foods") or []
    cols = a.get("columns") or []
    water = float(a.get("water_g") or 0)
    shc = float(a.get("shc") or 0)

    if water <= 0 or shc <= 0:
        raise ValueError(
            "calorimeter %r needs a positive water mass and specific heat "
            "capacity; the temperature rise is computed from both."
            % act_id)

    if len(foods) < 3:
        raise ValueError(
            "calorimeter %r offers %d food(s). The bench's claim is a "
            "COMPARISON between foods, which needs at least three."
            % (act_id, len(foods)))

    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "calorimeter %r has no commit gate. A bench read before a "
            "commitment confirms whatever the student already believed."
            % act_id)

    _unique_ids(foods, act_id, "calorimeter", "food")
    _no_correct_flags(foods, act_id, "calorimeter")

    lo = float(a.get("mass_min") or 0)
    hi = float(a.get("mass_max") or 0)
    step = float(a.get("mass_step") or 0)
    start = float(a.get("mass_start") or 0)
    if not (0 < lo < hi) or step <= 0 or not (lo <= start <= hi):
        raise ValueError(
            "calorimeter %r has an unusable mass range %r..%r step %r start "
            "%r." % (act_id, lo, hi, step, start))

    # ⚖️ THE PHYSICS GATE. Every reachable state must leave the water liquid.
    # This is the assertion that would have caught D-P2-01 on Design's own
    # numbers before a page was written, and it is here so that a later edit
    # to a capture fraction or a mass range cannot quietly reintroduce it.
    SCATTER_MAX = 1.1
    START_C = 20.0
    worst = max(float(f["kj_per_g"]) * float(f["capture"]) for f in foods)
    worst_rise = hi * worst * SCATTER_MAX * 1000.0 / (water * shc)
    if START_C + worst_rise >= 100.0:
        raise ValueError(
            "calorimeter %r can drive %g g of water to %.0f °C — burning "
            "%g g of its densest food. Liquid water in a boiling tube does "
            "not reach that, and the canvas draws warmth as rise/60. Reduce "
            "the sample mass or raise the water mass."
            % (act_id, water, START_C + worst_rise, hi))

    for f in foods:
        if float(f.get("capture") or 0) >= 1.0:
            raise ValueError(
                "calorimeter %r gives %r a capture fraction of %r. A "
                "calorimeter that catches everything the flame releases "
                "agrees with the packet, and the gap between the two IS this "
                "lesson." % (act_id, f.get("id"), f.get("capture")))

    want = {"temp", "rise", "left"}
    have = {c.get("id") for c in (a.get("readouts") or [])} or want
    if want - have:
        raise ValueError(
            "calorimeter %r is missing the %s readout(s)."
            % (act_id, sorted(want - have)))

    opts = "".join(
        '<button type="button" class="ks3-option" data-calor-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    picks = "".join(
        _p2_seg("ks3-seg-btn", f["label"],
                pressed=(i == int(a.get("start_food") or 0)),
                data_calor_food=i,
                data_kjg=f["kj_per_g"], data_capture=f["capture"],
                data_note=f.get("note", ""))
        for i, f in enumerate(foods))

    outs = "".join(
        '<div class="ks3-calor-out"><p class="ks3-calor-outlabel">%s</p>'
        '<p class="ks3-calor-outval" data-calor-out="%s"></p></div>'
        % (t(lbl), oid)
        for oid, lbl in (("temp", "Water temperature"),
                         ("rise", "Rise"),
                         ("left", "Sample left")))

    heads = "".join('<th scope="col">%s</th>' % t(c) for c in cols)

    return ('<div class="ks3-calor" data-calor data-water="%s" data-shc="%s" '
            'data-target="%d" data-start="%s">'
            '<div class="ks3-calor-gate" data-calor-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-calor-bench" data-calor-bench hidden>'
            '<div class="ks3-calor-picks">%s</div>'
            '<div class="ks3-calor-rig" role="img" aria-label="%s">'
            '<span class="ks3-calor-tube" aria-hidden="true">'
            '<span class="ks3-calor-water" data-calor-water></span></span>'
            '<span class="ks3-calor-flame" data-calor-flame '
            'aria-hidden="true"></span>'
            '<span class="ks3-calor-escape" aria-hidden="true"></span>'
            '</div>'
            '<label class="ks3-calor-sliderlabel" for="%s-m">'
            'Mass of sample · <span data-calor-masslabel></span></label>'
            '<input class="ks3-calor-slider" id="%s-m" type="range" '
            'min="%s" max="%s" step="%s" value="%s" data-calor-mass>'
            '<div class="ks3-calor-outs">%s</div>'
            '<div class="ks3-calor-acts">'
            '<button type="button" class="ks3-seg-btn" data-calor-burn>'
            '%s</button>'
            '<button type="button" class="ks3-seg-btn" data-calor-fresh>'
            '%s</button>'
            '<button type="button" class="ks3-seg-btn" data-calor-record '
            'disabled>%s</button></div>'
            '<div class="ks3-calor-tablewrap">'
            '<table class="ks3-calor-table"><thead><tr>%s</tr></thead>'
            '<tbody data-calor-rows></tbody></table></div>'
            '<p class="ks3-calor-note" data-calor-note></p>'
            '<p class="ks3-calor-close" data-calor-close hidden>%s</p>'
            '</div></div>'
            % (water, shc, int(a.get("runs_to_record") or 3), START_C,
               t(gate["prompt"]), opts, picks, e(a.get("alt", "")),
               e(act_id), e(act_id), lo, hi, step, start, outs,
               t(a.get("burn_label") or "Light the sample"),
               t(a.get("fresh_label") or "Fresh sample"),
               t(a.get("record_label") or "Record this run"),
               heads, rich(a.get("close") or "")))


# ═══ p2-02 · #s-bench · the power bench ══════════════════════════════════

def r_power_bench(a, act_id):
    """⊕ p2-02 `#s-bench` — race a 2000 W kettle against a 15 W router.

    Design's bench. Two appliances side by side; a TALL bar for power, which
    never moves, and a FILLING bar for the running total, which does. The
    whole lesson is in the fact that the short bar wins.

    ⊕ MRB-297 · 1 Sep 2026 — THE APPLIANCE IS A ROUTER. This docstring
    said "charger" in four places, and is corrected in place rather than
    marked line by line because the word is the NAME of a thing the bench
    draws, not a claim about it. The ruling and its reasoning are P2-09,
    written up in `ks3_data/p2/lesson_02_power_ratings_in_watts.py`: a
    charger does not draw its rating for eight hours, so the page credited
    the wrong answer for the appliance it named. A router does, and not one
    number moved in the swap. The old name is kept in this sentence so the
    change is still findable.

    ⚖️ **THE CROSSOVER IS COMPUTED, NEVER AUTHORED.** It is the moment the
    router's running total passes the kettle's finished total, i.e.
    `kettle_watts x kettle_runs_for / router_watts` = 2000 x 180 / 15 =
    24 000 s = 6 h 40 min. Authoring "6.67 h" as a constant would let a
    later edit to a wattage leave the marker pointing at a time that is no
    longer the crossover, and the page would go on claiming it was.

    ⚖️ **A POWER BAR IS A HEIGHT AND AN ENERGY BAR IS AN AREA.** They are
    drawn as two different bars on purpose — the kettle's power bar is
    133 times the router's and its energy bar ends up SHORTER. Drawing both
    quantities in one bar would hide exactly the thing the lesson is for.

    HOOKS: `data-pbench` (wrapper, `data-cross`, `data-maxt`) ·
    `data-pbench-gate` · `data-pbench-gopt` · `data-pbench-bench` ·
    `data-pbench-run` · `data-pbench-reset` · `data-pbench-jump` (valued
    with the time in seconds) · `data-pbench-out` (valued with the readout
    id) · `data-pbench-pow` / `data-pbench-nrg` (valued with the appliance
    id) · `data-pbench-note` · `data-pbench-close`.
    """
    gate = a.get("gate") or {}
    apps = a.get("appliances") or []
    jumps = a.get("jumps") or []
    outs_spec = a.get("readouts") or []

    if len(apps) != 2:
        raise ValueError(
            "power-bench %r has %d appliance(s). The bench's whole claim is "
            "a RACE between exactly two, one high-power and one long-running."
            % (act_id, len(apps)))
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "power-bench %r has no commit gate. A bench read before a "
            "commitment confirms whatever the student already believed."
            % act_id)

    _unique_ids(apps, act_id, "power-bench", "appliance")
    _unique_ids(jumps, act_id, "power-bench", "jump")
    _no_correct_flags(apps, act_id, "power-bench")

    for ap in apps:
        if float(ap.get("watts") or 0) <= 0 or float(ap.get("runs_for_s") or 0) <= 0:
            raise ValueError(
                "power-bench %r appliance %r needs a positive wattage and a "
                "positive running time; both products are computed from them."
                % (act_id, ap.get("id")))

    hi, lo = sorted(apps, key=lambda x: -float(x["watts"]))
    if float(hi["watts"]) * float(hi["runs_for_s"]) >= \
            float(lo["watts"]) * float(lo["runs_for_s"]):
        raise ValueError(
            "power-bench %r: the HIGHER-power appliance also transfers more "
            "energy (%g J vs %g J). Then the bench agrees with the wrong idea "
            "it exists to kill, and the hook's answer is false."
            % (act_id,
               float(hi["watts"]) * float(hi["runs_for_s"]),
               float(lo["watts"]) * float(lo["runs_for_s"])))

    # The crossover, derived. See the ruling above.
    cross = float(hi["watts"]) * float(hi["runs_for_s"]) / float(lo["watts"])
    maxt = max(float(x["runs_for_s"]) for x in apps)

    opts = "".join(
        '<button type="button" class="ks3-option" data-pbench-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    top = max(float(x["watts"]) for x in apps)
    rigs = "".join(
        '<div class="ks3-pbench-app">'
        '<p class="ks3-pbench-name">%s</p>'
        '<div class="ks3-pbench-bars">'
        '<div class="ks3-pbench-col"><span class="ks3-pbench-pow" '
        'data-pbench-pow="%s" data-w="%s" data-runs="%s" '
        'style="--h:%s"></span>'
        '<p class="ks3-pbench-cap">%s W</p></div>'
        '<div class="ks3-pbench-col"><span class="ks3-pbench-nrg" '
        'data-pbench-nrg="%s" style="--h:0"></span>'
        '<p class="ks3-pbench-cap">total</p></div>'
        '</div></div>'
        % (t(ap["label"]), e(ap["id"]),
           float(ap["watts"]), float(ap["runs_for_s"]),
           round(float(ap["watts"]) / top, 4), t(str(ap["watts"])),
           e(ap["id"]))
        for ap in apps)

    jbtns = "".join(
        _p2_seg("ks3-seg-btn", j["label"],
                data_pbench_jump=(cross if j.get("at") == "crossover"
                                  else float(j.get("at_s") or 0)))
        for j in jumps)

    outs = "".join(
        '<div class="ks3-pbench-out"><p class="ks3-pbench-outlabel">%s</p>'
        '<p class="ks3-pbench-outval" data-pbench-out="%s"></p></div>'
        % (t(o["label"]), e(o["id"])) for o in outs_spec)

    return ('<div class="ks3-pbench" data-pbench data-cross="%s" '
            'data-maxt="%s">'
            '<div class="ks3-pbench-gate" data-pbench-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-pbench-bench" data-pbench-bench hidden>'
            '<div class="ks3-pbench-rig" role="img" aria-label="%s">%s</div>'
            '<div class="ks3-pbench-outs">%s</div>'
            '<div class="ks3-pbench-acts">'
            '<button type="button" class="ks3-seg-btn" data-pbench-run '
            'aria-pressed="false">%s</button>'
            '<button type="button" class="ks3-seg-btn" data-pbench-reset>'
            '%s</button>%s</div>'
            '<p class="ks3-pbench-note" data-pbench-note></p>'
            '<p class="ks3-pbench-close" data-pbench-close hidden>%s</p>'
            '</div></div>'
            % (cross, maxt, t(gate["prompt"]), opts, e(a.get("alt", "")),
               rigs, outs,
               t(a.get("run_label") or "Run the day"),
               t(a.get("reset_label") or "Back to zero"), jbtns,
               rich(a.get("close") or "")))


# ═══ p2-02 · #s-sort · power or energy ═══════════════════════════════════

def r_power_energy_sort(a, act_id):
    """⊕ p2-02 `#s-sort` — six units and sentences, each one quantity.

    ⚖️ **THE TWO BUTTONS STAY ENABLED AFTER AN ANSWER.** R3: an activity
    control shows that it was CHOSEN, never whether it was right, and a
    student may change their mind. The note that appears underneath is a
    STATEMENT about the item, not a mark — Design writes two, one for
    each choice, and neither is green or red.

    ⚠️ **`sort_items`, NOT `cards`.** `cards` is claimed by `r_activity`
    and has no opt-out: an instrument authoring it gets two renderers and
    ships the block doubled and blank.

    HOOKS: `data-pwsort` (wrapper, `data-target`) · `data-pwsort-item`
    (valued with the item id) · `data-pwsort-btn` (valued `power`/`energy`) ·
    `data-pwsort-note`.
    """
    items = a.get("sort_items") or []
    if len(items) < 4:
        raise ValueError(
            "power-energy-sort %r has %d item(s). The sort is a claim that "
            "the distinction holds across units AND sentences, which needs "
            "both kinds present and several of each." % (act_id, len(items)))

    _unique_ids(items, act_id, "power-energy-sort", "item")

    if "cards" in a:
        raise ValueError(
            "power-energy-sort %r carries a `cards` key. `cards` is rendered "
            "by r_activity itself with NO opt-out, so the block would ship "
            "twice. The key is `sort_items`." % act_id)

    n_pow = sum(1 for i in items if i.get("is_power"))
    if n_pow == 0 or n_pow == len(items):
        raise ValueError(
            "power-energy-sort %r has every item on one side. A sort with "
            "one answer teaches the answer, not the distinction." % act_id)

    for it in items:
        if not it.get("right") or not it.get("wrong"):
            raise ValueError(
                "power-energy-sort %r item %r is missing one of its two "
                "notes. Design writes one for each choice, so the student "
                "who picks wrongly is told what the thing IS rather than "
                "just that they missed." % (act_id, it.get("id")))

    plab = a.get("power_label") or "Power"
    elab = a.get("energy_label") or "Energy"

    cards = "".join(
        '<li class="ks3-pwsort-item" data-pwsort-item="%s" '
        'data-ispower="%d" data-right="%s" data-wrong="%s">'
        '<p class="ks3-pwsort-text">%s</p>'
        '<div class="ks3-pwsort-btns">'
        '<button type="button" class="ks3-seg-btn" data-pwsort-btn="power" '
        'aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-seg-btn" data-pwsort-btn="energy" '
        'aria-pressed="false">%s</button></div>'
        '<p class="ks3-pwsort-note" data-pwsort-note hidden></p></li>'
        % (e(it["id"]), 1 if it.get("is_power") else 0,
           e(it["right"]), e(it["wrong"]), t(it["text"]), t(plab), t(elab))
        for it in items)

    return ('<div class="ks3-pwsort" data-pwsort data-target="%d">'
            '<ul class="ks3-pwsort-grid" role="list">%s</ul></div>'
            % (len(items), cards))


# ═══ p2-03 · #s-bench · the appliance bench ══════════════════════════════

def r_appliance_bench(a, act_id):
    """⊕ p2-03 `#s-bench` — one energy, shown in both legal unit pairings.

    Design's bench. Five appliances, a time slider running from one minute
    to a full day, and the same energy printed twice — in joules and in
    kilowatt-hours — with the cost beside it.

    ⚖️ **BOTH FIGURES ARE ONE CALCULATION SHOWN TWICE, NOT TWO
    CALCULATIONS.** `E = P x t` in watts and seconds gives the joules;
    dividing by 3 600 000 gives the kilowatt-hours. That is the lesson: two
    legal pairings, one quantity. If the two readouts were computed
    independently they could disagree, and a bench that disagrees with
    itself teaches that the pairings are different quantities.

    ⚖️ **THE FRIDGE MUST BE ABLE TO OUTRANK THE OVEN.** 90 W for 24 h beats
    2200 W for 45 min, and that inversion is `ENER-21` from `p2-02` paying
    off on real appliances. The renderer asserts that at least one
    lower-rated appliance overtakes a higher-rated one at their typical
    times — otherwise the bench quietly agrees with the belief it is
    here to kill.

    ⚠️ **THE PRICE IS ONE NAMED CONSTANT.** Design isolated it for exactly
    this reason: it is a plausible mid-2020s tariff, it will date, and when
    it does it changes in one place.

    HOOKS: `data-abench` (wrapper, `data-price`, `data-target`) ·
    `data-abench-gate` · `data-abench-gopt` · `data-abench-bench` ·
    `data-abench-app` (valued with the appliance index, carrying `data-w`) ·
    `data-abench-mins` (the slider) · `data-abench-timelabel` ·
    `data-abench-preset` (carrying `data-app` and `data-mins`) ·
    `data-abench-out` (valued with the readout id) · `data-abench-note` ·
    `data-abench-close`.
    """
    gate = a.get("gate") or {}
    apps = a.get("appliances") or []
    outs_spec = a.get("readouts") or []
    price = float(a.get("price_per_kwh") or 0)

    if len(apps) < 4:
        raise ValueError(
            "appliance-bench %r has %d appliance(s). The bench's claim is "
            "that the ORDER changes with the time setting, which needs "
            "enough of them to reorder." % (act_id, len(apps)))
    if price <= 0:
        raise ValueError(
            "appliance-bench %r has no price per kWh, so the cost readout "
            "would print nothing." % act_id)
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "appliance-bench %r has no commit gate." % act_id)

    _unique_ids(apps, act_id, "appliance-bench", "appliance")
    _no_correct_flags(apps, act_id, "appliance-bench")

    for ap in apps:
        if float(ap.get("watts") or 0) <= 0 or float(ap.get("typical_min") or 0) <= 0:
            raise ValueError(
                "appliance-bench %r appliance %r needs a positive wattage "
                "and typical time." % (act_id, ap.get("id")))

    # ⚖️ The inversion has to be reachable. See the ruling above.
    inverted = any(
        float(lo["watts"]) < float(hi["watts"])
        and float(lo["watts"]) * float(lo["typical_min"])
        > float(hi["watts"]) * float(hi["typical_min"])
        for hi in apps for lo in apps)
    if not inverted:
        raise ValueError(
            "appliance-bench %r: at their typical times, every appliance "
            "ranks in the same order as its rating. Then the bench agrees "
            "that a bigger rating means more energy, which is the belief "
            "p2-02 spent a whole lesson killing." % act_id)

    want = {"joules", "kwh", "cost"}
    have = {o.get("id") for o in outs_spec}
    if want - have:
        raise ValueError(
            "appliance-bench %r is missing the %s readout(s). Both unit "
            "pairings have to be on screen together or the student cannot "
            "see they are one quantity."
            % (act_id, sorted(want - have)))

    opts = "".join(
        '<button type="button" class="ks3-option" data-abench-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    picks = "".join(
        _p2_seg("ks3-seg-btn", ap["label"], pressed=(i == 0),
                data_abench_app=i, data_w=float(ap["watts"]))
        for i, ap in enumerate(apps))

    n_preset = int(a.get("appliances_to_price") or 3)
    presets = "".join(
        _p2_seg("ks3-seg-btn", "%s: %s" % (ap["label"], ap["tnote"]),
                data_abench_preset=i, data_app=i,
                data_mins=float(ap["typical_min"]))
        for i, ap in enumerate(apps[:n_preset]))

    outs = "".join(
        '<div class="ks3-abench-out"><p class="ks3-abench-outlabel">%s</p>'
        '<p class="ks3-abench-outval" data-abench-out="%s"></p></div>'
        % (t(o["label"]), e(o["id"])) for o in outs_spec)

    return ('<div class="ks3-abench" data-abench data-price="%s" '
            'data-target="%d">'
            '<div class="ks3-abench-gate" data-abench-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-abench-bench" data-abench-bench hidden>'
            '<div class="ks3-abench-picks" role="group" '
            'aria-label="Appliance">%s</div>'
            '<label class="ks3-abench-sliderlabel" for="%s-t">'
            'How long it runs · <span data-abench-timelabel></span></label>'
            '<input class="ks3-abench-slider" id="%s-t" type="range" '
            'min="%d" max="%d" step="1" value="%d" data-abench-mins>'
            '<div class="ks3-abench-presets">%s</div>'
            '<div class="ks3-abench-outs" aria-label="%s">%s</div>'
            '<p class="ks3-abench-note" data-abench-note></p>'
            '<p class="ks3-abench-close" data-abench-close hidden>%s</p>'
            '</div></div>'
            % (price, n_preset, t(gate["prompt"]), opts, picks,
               e(act_id), e(act_id),
               int(a.get("mins_min") or 1), int(a.get("mins_max") or 1440),
               int(a.get("mins_start") or 3), presets,
               e(a.get("alt", "")), outs, rich(a.get("close") or "")))


# ═══ p2-04 · #s-kwh · one kilowatt-hour, four ways ═══════════════════════

def r_kwh_rectangles(a, act_id):
    """⊕ p2-04 `#s-kwh` — four rectangles, four shapes, ONE area.

    ⚖️ **EQUAL AREA IS THE ENTIRE CLAIM, SO IT IS ASSERTED AND THEN
    DERIVED.** Every way must enclose exactly 1 kWh: `watts x hours / 1000
    == 1`. The renderer checks each one and refuses the block otherwise,
    because a set of "equal-area" rectangles whose areas differ is a picture
    that contradicts its own caption — and it would do so silently, since
    nothing about a drawn rectangle says what its area is meant to be.

    The widths and heights are DERIVED from the power and the time rather
    than laid out by flex, for the same reason `r_cover_bar` derives its
    parts: a flex row would make each rectangle whatever the container
    allowed, and rectangles that do not actually have equal area are a bar
    model that lies.

    ⚠️ The 9 W LED for 111 hours is the one that lands, and it is also the
    one whose aspect ratio is extreme (12 000:1 in the raw quantities). The
    drawing uses a LOG width so all four remain visible; the readout beside
    each says the true product, so nothing is hidden by the compression and
    the number a student quotes is the real one.

    HOOKS: `data-kwh` (wrapper, `data-target`) · `data-kwh-way` (valued with
    the way id, carrying `data-w`, `data-h`, `data-note`) ·
    `data-kwh-rect` · `data-kwh-note` · `data-kwh-close`.
    """
    ways = a.get("ways") or []
    if len(ways) < 3:
        raise ValueError(
            "kwh-rectangles %r has %d way(s). The claim is that MANY "
            "different shapes have one area, which needs several."
            % (act_id, len(ways)))
    _unique_ids(ways, act_id, "kwh-rectangles", "way")
    _no_correct_flags(ways, act_id, "kwh-rectangles")

    import math
    for w in ways:
        kwh = float(w["watts"]) * float(w["hours"]) / 1000.0
        if abs(kwh - 1.0) > 0.005:
            raise ValueError(
                "kwh-rectangles %r way %r encloses %.4f kWh, not 1. Every "
                "rectangle in this block is captioned as one unit, and one "
                "that is not makes the picture contradict its own caption "
                "— silently, because nothing about a drawn rectangle "
                "says what its area is supposed to be."
                % (act_id, w.get("id"), kwh))

    # Log widths so the 9 W / 111 h case stays visible beside the 2 kW /
    # 0.5 h one. The heights follow, so area on screen stays constant.
    lo = min(math.log10(float(w["hours"])) for w in ways)
    hi = max(math.log10(float(w["hours"])) for w in ways)
    span = (hi - lo) or 1.0

    cells = []
    for w in ways:
        frac = (math.log10(float(w["hours"])) - lo) / span
        wid = 18 + frac * 64          # per cent of the track
        cells.append(
            '<li class="ks3-kwh-way"><button type="button" '
            'class="ks3-kwh-btn" data-kwh-way="%s" data-w="%s" '
            'data-h="%s" data-note="%s" aria-pressed="false">'
            '<span class="ks3-kwh-rect" data-kwh-rect '
            'style="--w:%.2f%%;--h:%.2f%%" aria-hidden="true"></span>'
            '<span class="ks3-kwh-label">%s</span></button></li>'
            % (e(w["id"]), float(w["watts"]), float(w["hours"]),
               e(w.get("note", "")), wid, 100.0 - frac * 64.0,
               t(w["label"])))

    return ('<div class="ks3-kwh" data-kwh data-target="%d" role="img" '
            'aria-label="%s">'
            '<ul class="ks3-kwh-grid" role="list">%s</ul>'
            '<p class="ks3-kwh-note" data-kwh-note></p>'
            '<p class="ks3-kwh-close" data-kwh-close hidden>%s</p>'
            '</div>'
            % (len(ways), e(a.get("alt", "")), "".join(cells),
               rich(a.get("close") or "")))


# ═══ p2-04 · #s-bill · the bill builder ══════════════════════════════════

def r_bill_builder(a, act_id):
    """⊕ p2-04 `#s-bill` — five sliders, five products, one sum.

    ⚖️ **EVERY ROW AND THE TOTAL ARE COMPUTED.** A row is
    `watts/1000 x hours/day x days`; the total is those rows added, PLUS a
    standing charge that no slider reaches. Authoring any of them would let
    a bill that does not add up ship looking finished, and this block exists
    to show a student that it does add up.

    ⚖️ **THE STANDING CHARGE IS A ROW THAT NO CONTROL CAN MOVE, AND THAT IS
    THE TEACHING.** `ENER-26` — "switch everything off and the bill goes
    to zero" — dies when a student drags every slider to zero and the
    total does not reach zero. So the renderer requires a positive standing
    charge: without one the instrument would quietly agree with the belief.

    HOOKS: `data-bill` (wrapper, `data-price`, `data-standing`,
    `data-days`, `data-target`) · `data-bill-gate` · `data-bill-gopt` ·
    `data-bill-panel` · `data-bill-slider` (valued with the row id,
    carrying `data-w`, `data-perhour`) · `data-bill-hours` ·
    `data-bill-cell` (valued `<rowid>:<column>`) · `data-bill-units` ·
    `data-bill-cost` · `data-bill-standing` · `data-bill-close`.
    """
    gate = a.get("gate") or {}
    rows = a.get("rows") or []
    cols = a.get("columns") or []
    price = float(a.get("price_per_kwh") or 0)
    standing = float(a.get("standing_per_day") or 0)
    days = int(a.get("days") or 0)

    if len(rows) < 3:
        raise ValueError(
            "bill-builder %r has %d row(s). The bottom line is a SUM, and a "
            "sum of one or two terms does not look like one."
            % (act_id, len(rows)))
    if price <= 0 or days <= 0:
        raise ValueError(
            "bill-builder %r needs a positive price per unit and a positive "
            "number of days." % act_id)
    if standing <= 0:
        raise ValueError(
            "bill-builder %r has no standing charge. Dragging every slider "
            "to zero would then take the total to zero, and the instrument "
            "would agree with ENER-26 — the belief the lesson is here "
            "to kill." % act_id)
    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError("bill-builder %r has no commit gate." % act_id)

    _unique_ids(rows, act_id, "bill-builder", "row")
    _no_correct_flags(rows, act_id, "bill-builder")

    for r in rows:
        if float(r.get("watts") or 0) <= 0 or float(r.get("per_hour") or 0) <= 0:
            raise ValueError(
                "bill-builder %r row %r needs a positive wattage and a "
                "positive `per_hour` divisor (60 for a min/day slider, 1 "
                "for an h/day one)." % (act_id, r.get("id")))

    opts = "".join(
        '<button type="button" class="ks3-option" data-bill-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    sliders = "".join(
        '<div class="ks3-bill-slider">'
        '<label for="%s-%s">%s · <span data-bill-hours="%s"></span></label>'
        '<input id="%s-%s" type="range" min="%s" max="%s" step="1" '
        'value="%s" data-bill-slider="%s" data-w="%s" data-perhour="%s" '
        'data-unit="%s"></div>'
        % (e(act_id), e(r["id"]), t(r["name"]), e(r["id"]),
           e(act_id), e(r["id"]), r.get("min", 0), r.get("max", 24),
           r.get("start", 0), e(r["id"]), float(r["watts"]),
           float(r["per_hour"]), e(r.get("unit", "")))
        for r in rows)

    heads = "".join('<th scope="col">%s</th>' % t(c) for c in cols)
    body = "".join(
        '<tr><th scope="row">%s</th>'
        '<td>%s W</td>'
        '<td data-bill-cell="%s:hours"></td>'
        '<td data-bill-cell="%s:units"></td>'
        '<td data-bill-cell="%s:cost"></td></tr>'
        % (t(r["name"]), t(str(int(float(r["watts"])))),
           e(r["id"]), e(r["id"]), e(r["id"]))
        for r in rows)

    return ('<div class="ks3-bill" data-bill data-price="%s" '
            'data-standing="%s" data-days="%d" data-target="%d">'
            '<div class="ks3-bill-gate" data-bill-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-bill-panel" data-bill-panel hidden>'
            '<div class="ks3-bill-sliders">%s</div>'
            '<div class="ks3-bill-tablewrap" role="img" aria-label="%s">'
            '<table class="ks3-bill-table"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody>'
            '<tfoot>'
            '<tr><th scope="row" colspan="3">Standing charge · %d days</th>'
            '<td></td><td data-bill-standing></td></tr>'
            '<tr><th scope="row" colspan="3">Amount due</th>'
            '<td data-bill-units></td><td data-bill-cost></td></tr>'
            '</tfoot></table></div>'
            '<p class="ks3-bill-close" data-bill-close hidden>%s</p>'
            '</div></div>'
            % (price, standing, days, len(rows), t(gate["prompt"]), opts,
               sliders, e(a.get("alt", "")), heads, body, days,
               rich(a.get("close") or "")))


# ═══ p2-05 · #s-sort · will it run out ══════════════════════════════════

def r_renewable_sort(a, act_id):
    """⊕ p2-05 `#s-sort` — eight resources, ONE question, deliberately.

    ⚖️ **THE FIRST PASS ASKS ONE QUESTION AND REFUSES THE SECOND.** Design
    separates the two questions across two sections on purpose: a student
    who sorts on "will it run out?" while already thinking about pollution
    never finds out that the two answers disagree. The prompt says so, and
    nothing in this block mentions carbon.

    ⚠️ `sort_items`, NOT `cards` — `cards` is claimed by `r_activity`
    with no opt-out and would render the block twice.

    HOOKS: `data-rsort` (wrapper, `data-target`) · `data-rsort-item`
    (valued with the id, carrying `data-renew`, `data-note`) ·
    `data-rsort-btn` (valued `renew`/`finite`) · `data-rsort-note`.
    """
    items = a.get("sort_items") or []
    if len(items) < 6:
        raise ValueError(
            "renewable-sort %r has %d resource(s). The grid in the next "
            "section needs enough of them for BOTH \"impossible\" corners "
            "to be occupied." % (act_id, len(items)))
    if "cards" in a:
        raise ValueError(
            "renewable-sort %r carries a `cards` key, which r_activity "
            "renders itself with no opt-out. The key is `sort_items`."
            % act_id)
    _unique_ids(items, act_id, "renewable-sort", "resource")
    _no_correct_flags(items, act_id, "renewable-sort")

    n_renew = sum(1 for i in items if i.get("renewable"))
    if n_renew == 0 or n_renew == len(items):
        raise ValueError(
            "renewable-sort %r has every resource on one side." % act_id)

    rlab = a.get("renew_label") or "Renewable"
    flab = a.get("finite_label") or "Finite"

    cells = "".join(
        '<li class="ks3-rsort-item" data-rsort-item="%s" data-renew="%d" '
        'data-note="%s">'
        '<p class="ks3-rsort-name">%s</p>'
        '<p class="ks3-rsort-store">%s</p>'
        '<div class="ks3-rsort-btns">'
        '<button type="button" class="ks3-seg-btn" data-rsort-btn="renew" '
        'aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-seg-btn" data-rsort-btn="finite" '
        'aria-pressed="false">%s</button></div>'
        '<p class="ks3-rsort-note" data-rsort-note hidden></p></li>'
        % (e(it["id"]), 1 if it.get("renewable") else 0,
           e(it.get("note", "")), t(it["text"]), t(it.get("store", "")),
           t(rlab), t(flab))
        for it in items)

    return ('<div class="ks3-rsort" data-rsort data-target="%d">'
            '<ul class="ks3-rsort-grid" role="list">%s</ul></div>'
            % (len(items), cells))


# ═══ p2-05 · #s-grid · the two-axis grid ════════════════════════════════

def r_two_axis_grid(a, act_id):
    """⊕ p2-05 `#s-grid` — renewability against one other axis at a time.

    ⚖️ **BOTH \"IMPOSSIBLE\" CORNERS MUST BE OCCUPIED ON THE CARBON
    AXIS, AND THE RENDERER CHECKS IT.** The belief being killed is that
    renewable and clean are one question, and the ONLY evidence that kills
    it is a low-carbon finite resource (nuclear) and a high-carbon renewable
    one (wood). If a later edit softened either, the grid would have an
    empty corner, the misconception would survive the lesson, and Rung 2
    would have no answer — silently, because the grid would still draw.

    ⚖️ **EVERY AXIS MUST REORDER THE RANKING.** The lesson's claim is that
    there is no single best resource; that is only shown if the orderings
    genuinely disagree. Two axes that ranked identically would be one axis
    drawn twice.

    ⚠️ **THE VALUES ARE POSITIONS, NOT MEASUREMENTS** (Design's flag 17).
    They carry an ORDERING and nothing else, and the page's legal line says
    so. They are 0-1 and are never printed as figures.

    HOOKS: `data-grid2` (wrapper, `data-target`) · `data-grid2-axis`
    (valued with the axis id, carrying `data-note`) · `data-grid2-plot` ·
    `data-grid2-dot` (valued with the resource id, carrying `data-x`,
    `data-y`) · `data-grid2-axislabel` · `data-grid2-lo` / `data-grid2-hi` ·
    `data-grid2-note` · `data-grid2-close`.
    """
    axes = a.get("axes") or []
    if len(axes) < 2:
        raise ValueError(
            "two-axis-grid %r has %d axis/axes. The lesson's claim is that "
            "the ranking RESHUFFLES, which needs at least two to compare."
            % (act_id, len(axes)))
    _unique_ids(axes, act_id, "two-axis-grid", "axis")

    # ⚖️ WHICH COLUMN EACH RESOURCE SITS IN. Authored here as `resources`
    # AND cross-checked against `#s-sort`'s own list by
    # `ks3_data/p2/__init__.py`, which sees the whole lesson — so the
    # two blocks cannot disagree about whether wood is renewable.
    res = a.get("resources") or []
    if not res:
        raise ValueError(
            "two-axis-grid %r has no `resources`, so no dot knows which "
            "column it belongs in." % act_id)
    _unique_ids(res, act_id, "two-axis-grid", "resource")
    renew = {r["id"]: bool(r.get("renewable")) for r in res}

    carbon = None
    for ax in axes:
        if ax.get("id") == "carbon":
            carbon = ax
    if carbon is None:
        raise ValueError(
            "two-axis-grid %r has no `carbon` axis. It is the axis on which "
            "the renewable/clean belief is confronted." % act_id)

    # ⚖️ BOTH "IMPOSSIBLE" CORNERS MUST BE OCCUPIED. See the ruling above.
    cv = carbon.get("values") or {}
    LOWC, HIGHC = 0.25, 0.5
    clean_finite = [k for k, v in cv.items()
                    if not renew.get(k) and float(v) <= LOWC]
    dirty_renew = [k for k, v in cv.items()
                   if renew.get(k) and float(v) >= HIGHC]
    if not clean_finite or not dirty_renew:
        raise ValueError(
            "two-axis-grid %r leaves a corner of the carbon axis EMPTY "
            "(low-carbon finite: %s · high-carbon renewable: %s). Those two "
            "cells are the whole evidence that renewable and clean are "
            "different questions: with either empty the misconception "
            "survives the lesson and Rung 2 has no answer — and the "
            "grid still draws, so nothing would say so."
            % (act_id, clean_finite or "NONE", dirty_renew or "NONE"))

    for ax in axes:
        vals = ax.get("values") or {}
        if not vals:
            raise ValueError(
                "two-axis-grid %r axis %r has no values, so nothing would "
                "plot." % (act_id, ax.get("id")))
        for k, v in vals.items():
            if not (0.0 <= float(v) <= 1.0):
                raise ValueError(
                    "two-axis-grid %r axis %r gives %r a value of %r. These "
                    "are relative POSITIONS on 0-1, not measurements."
                    % (act_id, ax.get("id"), k, v))

    # ⚖️ Every axis must produce a different ordering. See the ruling above.
    orders = {}
    for ax in axes:
        vals = ax["values"]
        orders[ax["id"]] = tuple(sorted(vals, key=lambda k: vals[k]))
    seen = {}
    for aid, order in orders.items():
        if order in seen:
            raise ValueError(
                "two-axis-grid %r: axes %r and %r rank the resources in the "
                "SAME order. Two axes that agree are one axis drawn twice, "
                "and the lesson's claim is that they disagree."
                % (act_id, seen[order], aid))
        seen[order] = aid

    tabs = "".join(
        _p2_seg("ks3-seg-btn", ax["label"], pressed=(i == 0),
                data_grid2_axis=ax["id"], data_note=ax.get("note", ""),
                data_lo=ax.get("low", ""), data_hi=ax.get("high", ""))
        for i, ax in enumerate(axes))

    first = axes[0]
    label_of = {r["id"]: r.get("label", r["id"]) for r in res}
    dots = "".join(
        '<span class="ks3-grid2-dot" data-grid2-dot="%s" %s '
        'data-renew="%d" style="--x:%s;--y:%s">'
        '<span class="ks3-grid2-tag">%s</span></span>'
        % (e(r["id"]),
           " ".join('data-v-%s="%s"' % (e(ax["id"]),
                                        float(ax["values"].get(r["id"], 0)))
                    for ax in axes),
           1 if renew.get(r["id"]) else 0,
           0.78 if renew.get(r["id"]) else 0.22,
           float(first["values"].get(r["id"], 0)),
           t(label_of[r["id"]]))
        for r in res)

    return ('<div class="ks3-grid2" data-grid2 data-target="%d" role="img" '
            'aria-label="%s">'
            '<div class="ks3-grid2-tabs" role="group" '
            'aria-label="Second question">%s</div>'
            '<p class="ks3-grid2-axislabel" data-grid2-axislabel></p>'
            '<div class="ks3-grid2-plot" data-grid2-plot>'
            '<span class="ks3-grid2-hi" data-grid2-hi></span>'
            '<span class="ks3-grid2-lo" data-grid2-lo></span>'
            '<span class="ks3-grid2-xlab">%s</span>%s</div>'
            '<p class="ks3-grid2-note" data-grid2-note></p>'
            '<p class="ks3-grid2-close" data-grid2-close hidden>%s</p>'
            '</div>'
            % (len(axes), e(a.get("alt", "")), tabs,
               t(a.get("renew_axis_label") or "Will it run out?"), dots,
               rich(a.get("close") or "")))


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. `ks3_art.check_placements` gate 2 fails a family
# registered and never placed and gate 3 fails one placed and never
# registered, so this list and the lessons agreeing is checkable rather than
# promised. Every family is P2's own — `ks3_art/core.py` is untouched.
#
# ⚠️ SHELL CLASSES ARE UNIQUE ACROSS THE WHOLE REGISTRY. `ks3_art.load()`
# asserts it since MRB-279, because two families wearing one class puts one
# unit's stylesheet block on another unit's instrument and does it silently.
# Every class below is prefixed `ks3-` and carries a P2-only stem.

KIND_SHELL = {
    'calorimeter':       ("ks3-calor-block",
                          ' data-instrument data-calorblock '
                          'data-stage-done="0"'),
    'power-bench':       ("ks3-pbench-block",
                          ' data-instrument data-pbenchblock '
                          'data-stage-done="0"'),
    'power-energy-sort': ("ks3-pwsort-block",
                          ' data-instrument data-pwsortblock '
                          'data-stage-done="0"'),
    'appliance-bench':   ("ks3-abench-block",
                          ' data-instrument data-abenchblock '
                          'data-stage-done="0"'),
    'kwh-rectangles':    ("ks3-kwh-block",
                          ' data-instrument data-kwhblock '
                          'data-stage-done="0"'),
    'bill-builder':      ("ks3-bill-block",
                          ' data-instrument data-billblock '
                          'data-stage-done="0"'),
    'renewable-sort':    ("ks3-rsort-block",
                          ' data-instrument data-rsortblock '
                          'data-stage-done="0"'),
    'two-axis-grid':     ("ks3-grid2-block",
                          ' data-instrument data-grid2block '
                          'data-stage-done="0"'),
}

KIND_FN = {
    'calorimeter':       r_calorimeter,
    'power-bench':       r_power_bench,
    'power-energy-sort': r_power_energy_sort,
    'appliance-bench':   r_appliance_bench,
    'kwh-rectangles':    r_kwh_rectangles,
    'bill-builder':      r_bill_builder,
    'renewable-sort':    r_renewable_sort,
    'two-axis-grid':     r_two_axis_grid,
}
