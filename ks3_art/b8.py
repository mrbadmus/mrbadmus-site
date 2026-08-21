"""ks3_art.b8 — B8's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import json
import re
from ks3_art.kit import (
    _attr_safe,
    _dial_block,
    _dials,
    _group_digits,
    _js_round,
    _need,
    _pctnum,
    _self_check,
    _verdict_ids,
    _with_suffix,
    e,
    rich,
    t,
)


def _b8_mass(x, unit, dp_below):
    """Design's own printing rule: round at or above `dp_below`, else one place.

    ⚠️ THE THRESHOLD IS PER VALUE, NOT PER AMOUNT. At 90 g of glucose the same
    panel prints `132 g` beside `54.0 g`, and that is the rule applied honestly.
    Tidying it to one form would change the printed totals a student is being
    asked to compare, which is the one thing on this bench that must not move.
    """
    x = float(x)
    return ("%d" % _js_round(x) if x >= float(dp_below) else "%.1f" % x) + unit
# ── b8-01 `#s-bench` · mass-ledger ───────────────────────────────────────

def r_mass_ledger(a, act_id):
    """⊕ b8-01 `#s-bench` — weigh both sides, and watch the energy stay out.

    ⚖️ THE LEDGER IS RATIOS, NOT A TABLE OF FOUR ANSWERS. Every printed figure
    is derived from one per-gram model, which is *why* the two totals match at
    every amount rather than at the four the author happened to check. 180 g
    glucose + 192 g oxygen → 264 g CO₂ + 108 g H₂O is the balanced equation by
    mass (180 + 6×32 = 372; 6×44 + 6×18 = 372), so per gram of glucose both
    sides come to 2.0667 and the totals are equal by construction, before any
    rounding. That is asserted below rather than trusted: a ledger about
    conservation that does not balance is the lesson teaching its own
    misconception.

    ⚖️ THE ENERGY FIGURE SITS OUTSIDE BOTH TOTALS, ON THE SAME ROW, IN ALERT.
    That is not decoration and it is not an oversight to be tidied: it is the
    visual form of the argument that energy is not a substance. Rung 2 — where
    10 kg of fat has gone — and the second `#s-think` paragraph both depend on
    the student having seen it sitting apart from the two columns. Folding it
    into a total would make mass and energy the same kind of quantity on the
    one page in the key stage that exists to separate them. `r_mass_ledger`
    refuses a payload that puts an energy row in either column.

    ⚠️ ONE ROW CARRIES NO PER-GRAM FACTOR AND THAT ROW IS THE GLUCOSE. It is
    the amount itself — the number the student picked — so its factor is 1 by
    definition rather than by authoring. Asserted to be exactly one row, and to
    be the first row of the `in` column, because a second unfactored row would
    silently weigh one gram per gram and balance nothing.
    """
    _need(a, act_id, ("options_label", "amounts", "start", "per_gram",
                         "columns", "rows_in", "rows_out", "totals", "units",
                         "run_label", "ran_label", "exits_label", "exits",
                         "close"))

    amounts = a["amounts"]
    if len(amounts) < 2:
        raise ValueError(
            "mass-ledger %r declares %d amount(s). The bench's argument is that "
            "the two totals match AT EVERY amount, which needs more than one."
            % (act_id, len(amounts)))
    seen = set()
    for m in amounts:
        for f in ("id", "label", "name", "grams", "note"):
            if not m.get(f):
                raise ValueError(
                    "mass-ledger %r amount %r declares no %r. `name` is the "
                    "panel's heading and `label` is the tab — Design writes "
                    "them differently on two of the four, so neither can stand "
                    "in for the other." % (act_id, m.get("id"), f))
        if m["id"] in seen:
            raise ValueError("mass-ledger %r declares amount id %r twice."
                             % (act_id, m["id"]))
        seen.add(m["id"])
        if float(m["grams"]) <= 0:
            raise ValueError(
                "mass-ledger %r amount %r weighs %r g. An amount of no glucose "
                "prints a ledger of zeroes that balances trivially."
                % (act_id, m["id"], m["grams"]))
    if a["start"] not in seen:
        raise ValueError(
            "mass-ledger %r opens on amount %r, which it does not offer."
            % (act_id, a["start"]))

    per_gram = dict(a["per_gram"])
    if not per_gram.get("kj"):
        raise ValueError(
            "mass-ledger %r's per_gram declares no `kj`. The energy figure is "
            "the row the lesson turns on." % act_id)
    energy_per_g = float(per_gram.pop("kj"))

    units = a["units"]
    for f in ("mass", "energy", "dp_below"):
        if not units.get(f):
            raise ValueError("mass-ledger %r units declares no %r."
                             % (act_id, f))
    group = bool(units.get("group_thousands"))

    for f in ("in", "out"):
        if not a["columns"].get(f):
            raise ValueError("mass-ledger %r columns declares no %r."
                             % (act_id, f))
    for f in ("in", "out", "energy"):
        if not a["totals"].get(f):
            raise ValueError(
                "mass-ledger %r totals declares no %r. All three are on screen "
                "on the same row, and the third is on it precisely because it "
                "is not part of the other two." % (act_id, f))

    # The factor map. A row with no `per_gram` entry is the glucose — the amount
    # itself, factor 1 by definition — and there may be exactly one of them.
    factors, unfactored, rows = {}, [], []
    for side in ("rows_in", "rows_out"):
        if not a[side]:
            raise ValueError("mass-ledger %r declares no %s." % (act_id, side))
        for r in a[side]:
            if not (r.get("id") and r.get("name")):
                raise ValueError(
                    "mass-ledger %r %s has a row missing `id` or `name`."
                    % (act_id, side))
            if r["id"] in factors:
                raise ValueError("mass-ledger %r declares row id %r twice."
                                 % (act_id, r["id"]))
            if r["id"] == "kj" or r["id"] in ("energy", "kilojoules"):
                raise ValueError(
                    "mass-ledger %r puts row %r in the %s column. ENERGY IS NOT "
                    "A SUBSTANCE and it is not in either total — that placement "
                    "is the argument rung 2 and the second `#s-think` paragraph "
                    "both rest on." % (act_id, r["id"], side))
            if r["id"] in per_gram:
                factors[r["id"]] = float(per_gram[r["id"]])
            else:
                factors[r["id"]] = 1.0
                unfactored.append((side, r["id"]))
            rows.append((side, r))
    if len(unfactored) != 1 or unfactored[0][0] != "rows_in":
        raise ValueError(
            "mass-ledger %r has %d row(s) with no per-gram factor (%s). Exactly "
            "one row is the glucose — the amount the student picked, factor 1 by "
            "definition — and it is the first row of the `in` column. A second "
            "unfactored row weighs one gram per gram of glucose and balances "
            "nothing." % (act_id, len(unfactored),
                          ", ".join(r for _, r in unfactored) or "none"))
    if a["rows_in"][0]["id"] != unfactored[0][1]:
        raise ValueError(
            "mass-ledger %r's unfactored row %r is not the first row of the "
            "`in` column. The glucose is what the student chose; it is read "
            "first." % (act_id, unfactored[0][1]))
    spare = sorted(set(per_gram) - set(factors))
    if spare:
        raise ValueError(
            "mass-ledger %r's per_gram declares %s, which no row prints. A "
            "factor nothing reads is a substance the ledger accounts for and "
            "never shows." % (act_id, ", ".join(map(repr, spare))))

    # ⚖️ THE BALANCE, ASSERTED. Per gram of glucose the two sides must come to
    # the same number, exactly — that is what makes the printed totals match at
    # every amount rather than at the four somebody checked.
    total_in = sum(factors[r["id"]] for r in a["rows_in"])
    total_out = sum(factors[r["id"]] for r in a["rows_out"])
    if abs(total_in - total_out) > 1e-9:
        raise ValueError(
            "mass-ledger %r does not balance: %.6f g in against %.6f g out, per "
            "gram of glucose. The two totals are printed side by side under a "
            "legal line that says they are equal, and rung 2 asks the student "
            "to trust it." % (act_id, total_in, total_out))

    exits = a["exits"]
    if len(exits) < 2:
        raise ValueError(
            "mass-ledger %r declares %d exit(s). The reveal's argument is that "
            "two of them have mass and one does not." % (act_id, len(exits)))
    for x in exits:
        if not (x.get("name") and x.get("route")):
            raise ValueError(
                "mass-ledger %r has an exit missing `name` or `route`."
                % act_id)

    start = next(m for m in amounts if m["id"] == a["start"])
    grams = float(start["grams"])
    mass_u, dp = units["mass"], units["dp_below"]

    tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-ml-tab" '
        'data-ml-amount="%s" data-grams="%s" data-name="%s" data-note="%s" '
        'aria-pressed="%s"><span class="ks3-opt-label">%s</span>'
        '</button></li>'
        % (e(m["id"]), e(_pctnum(m["grams"])),
           e(_attr_safe(m["name"], act_id, "amount %r `name`" % m["id"])),
           e(_attr_safe(m["note"], act_id, "amount %r `note`" % m["id"])),
           "true" if m["id"] == a["start"] else "false", t(m["label"]))
        for m in amounts)

    def column(side, key):
        return ('<div class="ks3-ml-col">'
                '<p class="ks3-ml-colhead">%s</p>'
                '<ul class="ks3-ml-rows" role="list">%s</ul></div>'
                % (t(a["columns"][key]),
                   "".join(
                       '<li class="ks3-ml-row">'
                       '<span class="ks3-ml-rowname">%s</span>'
                       '<span class="ks3-ml-rowvalue" data-ml-row="%s" '
                       'data-ml-side="%s">%s</span></li>'
                       % (t(r["name"]), e(r["id"]), e(key),
                          t(_b8_mass(grams * factors[r["id"]], mass_u, dp)))
                       for r in a[side])))

    return ('<div class="ks3-ml" data-ml data-factors="%s" data-kj="%s" '
            'data-mass-unit="%s" data-energy-unit="%s" data-dp="%s" '
            'data-group="%s" data-run-label="%s" data-ran-label="%s">'
            '<div class="ks3-ml-tabsgroup">'
            '<p class="ks3-ml-tabslabel" id="%s-amounts">%s</p>'
            '<ul class="ks3-options ks3-ml-tabs" role="list" '
            'aria-labelledby="%s-amounts">%s</ul></div>'
            '<div class="ks3-ml-panel">'
            '<p class="ks3-ml-name" data-ml-name>%s</p>'
            '<p class="ks3-ml-note" data-ml-note>%s</p>'
            '<div class="ks3-ml-cols">%s%s</div>'
            '<div class="ks3-ml-totals">'
            '<p class="ks3-ml-total"><span class="ks3-ml-totallabel">%s</span> '
            '<span data-ml-total="in">%s</span></p>'
            '<p class="ks3-ml-total"><span class="ks3-ml-totallabel">%s</span> '
            '<span data-ml-total="out">%s</span></p>'
            '<p class="ks3-ml-energy"><span class="ks3-ml-totallabel">%s</span> '
            '<span data-ml-energy>%s</span></p></div>'
            '<div class="ks3-ml-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ml-run" '
            'data-ml-run>%s</button></div>'
            '<div class="ks3-ml-exits" data-ml-exitspanel hidden>'
            '<p class="ks3-ml-exitslabel">%s</p>'
            '<ul class="ks3-ml-exitlist" role="list">%s</ul>'
            '<p class="ks3-ml-close">%s</p></div></div></div>'
            % (e(json.dumps(factors, separators=(",", ":"), sort_keys=True)),
               e(_pctnum(energy_per_g)), e(mass_u), e(units["energy"]),
               e(_pctnum(dp)), "1" if group else "",
               e(_attr_safe(a["run_label"], act_id, "`run_label`")),
               e(_attr_safe(a["ran_label"], act_id, "`ran_label`")),
               e(act_id), t(a["options_label"]), e(act_id), tabs,
               t(start["name"]), t(start["note"]),
               column("rows_in", "in"), column("rows_out", "out"),
               t(a["totals"]["in"]),
               t(_b8_mass(grams * total_in, mass_u, dp)),
               t(a["totals"]["out"]),
               t(_b8_mass(grams * total_out, mass_u, dp)),
               t(a["totals"]["energy"]),
               t(_group_digits(_js_round(grams * energy_per_g), group)
                 + units["energy"]),
               t(a["run_label"]), t(a["exits_label"]),
               "".join(
                   '<li class="ks3-ml-exit">'
                   '<p class="ks3-ml-exitname">%s</p>'
                   '<p class="ks3-ml-exitroute">%s</p></li>'
                   % (t(x["name"]), rich(x["route"])) for x in exits),
               rich(a["close"])))
# ── b8-02 `#s-bench` · cell-demand ───────────────────────────────────────

def r_cell_demand(a, act_id):
    """⊕ b8-02 `#s-bench` — five very different cells, one reaction.

    ⚖️ THE CUT IS PER CELL AND ONE-WAY, and that is what makes the bench an
    argument rather than a demonstration. Switching tabs does not un-reveal a
    cell already cut; coming back to it shows its `fails` line still open. The
    student accumulates five failures that are all the same failure, which is
    the sentence `RESP-03` needs and which one cell could never make.

    ⚖️ THE ROOT HAIR CELL IS THE REASON THIS BENCH EXISTS. It is the only plant
    cell among the five, and its `fails` line — mineral uptake stops, osmosis
    does not, so the plant goes short of minerals long before it goes short of
    water — is what sets up rung 4 on waterlogged soil and b8-05's `root` case.
    A bench of five animal cells would teach that respiration is an animal
    thing, which is precisely the belief it is here to kill. So the renderer
    refuses a payload whose cells all share one `origin`: the contrast is
    structural, not decorative.

    ⚠️ EVERY CELL'S PANEL IS IN THE DOCUMENT and only one is shown. The DOM is
    the state, so a cell's cut survives a tab switch with nothing to remember,
    and a reader with JS off gets the opening cell whole rather than an empty
    shell.

    ⚑ THE PERCENTAGES ARE ILLUSTRATIVE AND THE PAGE'S LEGAL LINE SAYS SO. They
    are asserted to sum to 100 because a spend breakdown that does not is a
    reading error waiting to happen, not because the individual figures are
    measurements. NOTES-B8 flag 8 offers to replace them with ranked words;
    that is Mide's to rule on and the shape survives either way, since ranked
    words would still need an order.
    """
    _need(a, act_id, ("options_label", "spend_label", "mito_label", "cells",
                         "start", "run_label", "ran_label", "done_after"))

    cells = a["cells"]
    if len(cells) < 3:
        raise ValueError(
            "cell-demand %r declares %d cell(s). The block's argument is that "
            "five very different cells run the SAME reaction, which needs "
            "enough of them to be different." % (act_id, len(cells)))

    seen, origins = set(), set()
    for c in cells:
        for f in ("id", "label", "name", "origin", "job", "spend", "mito",
                  "fails"):
            if not c.get(f):
                raise ValueError(
                    "cell-demand %r cell %r declares no %r. `fails` is the "
                    "whole reveal — a cell whose oxygen can be cut with nothing "
                    "to report is a button that does nothing."
                    % (act_id, c.get("id"), f))
        if c["id"] in seen:
            raise ValueError("cell-demand %r declares cell id %r twice."
                             % (act_id, c["id"]))
        seen.add(c["id"])
        origins.add(c["origin"])
        total = 0
        for p in c["spend"]:
            if not (p.get("name") and p.get("pct") is not None):
                raise ValueError(
                    "cell-demand %r cell %r has a spend row missing `name` or "
                    "`pct`." % (act_id, c["id"]))
            total += float(p["pct"])
        if abs(total - 100.0) > 1e-9:
            raise ValueError(
                "cell-demand %r cell %r spends %g%% of its energy. The rows are "
                "shares of one budget and are drawn as bars against a common "
                "track, so a column that does not come to 100 draws a cell with "
                "energy left over or borrowed." % (act_id, c["id"], total))

    if len(origins) < 2:
        raise ValueError(
            "cell-demand %r draws %d cell(s) and every one of them is %r. The "
            "bench exists to show that respiration is not an animal thing — the "
            "root hair cell is the only plant cell among the five and it is what "
            "makes that unarguable. One origin teaches the misconception."
            % (act_id, len(cells), sorted(origins)[0]))

    if a["start"] not in seen:
        raise ValueError("cell-demand %r opens on cell %r, which it does not "
                         "offer." % (act_id, a["start"]))
    after = int(a["done_after"])
    if not 1 <= after <= len(cells):
        raise ValueError(
            "cell-demand %r completes after %d cell(s) of %d. A threshold above "
            "the number of cells is a stop that can never tick; one at or below "
            "zero is a stop that ticks on load."
            % (act_id, after, len(cells)))

    tabs, panels = [], []
    for c in cells:
        first = c["id"] == a["start"]
        tabs.append(
            '<li><button type="button" class="ks3-option ks3-cd-tab" '
            'data-cd-cell="%s" aria-pressed="%s">'
            '<span class="ks3-opt-label">%s</span></button></li>'
            % (e(c["id"]), "true" if first else "false", t(c["label"])))
        panels.append(
            '<div class="ks3-cd-cell" data-cd-panel="%s"%s>'
            '<div class="ks3-cd-headrow">'
            '<p class="ks3-cd-name">%s</p>'
            '<p class="ks3-cd-origin">%s</p></div>'
            '<p class="ks3-cd-job">%s</p>'
            '<p class="ks3-cd-spendlabel">%s</p>'
            '<ul class="ks3-cd-spend" role="list">%s</ul>'
            '<div class="ks3-cd-mito">'
            '<p class="ks3-cd-mitorow">'
            '<span class="ks3-cd-mitolabel">%s</span>%s</p></div>'
            '<div class="ks3-cd-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-cd-cut" '
            'data-cd-cut="%s">%s</button></div>'
            '<p class="ks3-cd-fails" data-cd-fails hidden>%s</p></div>'
            % (e(c["id"]), "" if first else " hidden",
               t(c["name"]), t(c["origin"]), t(c["job"]), t(a["spend_label"]),
               "".join(
                   '<li class="ks3-cd-spendrow">'
                   '<div class="ks3-cd-spendhead">'
                   '<p class="ks3-cd-spendname">%s</p>'
                   '<p class="ks3-cd-spendpct">%s%%</p></div>'
                   '<span class="ks3-cd-track"><span class="ks3-cd-fill" '
                   'style="width:%s%%"></span></span></li>'
                   % (t(p["name"]), t(_pctnum(p["pct"])), e(_pctnum(p["pct"])))
                   for p in c["spend"]),
               t(a["mito_label"]), rich(c["mito"]),
               e(c["id"]), t(a["run_label"]), rich(c["fails"])))

    return ('<div class="ks3-cd" data-cd data-total="%d" data-done-after="%d" '
            'data-run-label="%s" data-ran-label="%s">'
            '<div class="ks3-cd-tabsgroup">'
            '<p class="ks3-cd-tabslabel" id="%s-cells">%s</p>'
            '<ul class="ks3-options ks3-cd-tabs" role="list" '
            'aria-labelledby="%s-cells">%s</ul></div>'
            '<div class="ks3-cd-panel">%s</div></div>'
            % (len(cells), after,
               e(_attr_safe(a["run_label"], act_id, "`run_label`")),
               e(_attr_safe(a["ran_label"], act_id, "`ran_label`")),
               e(act_id), t(a["options_label"]), e(act_id),
               "".join(tabs), "".join(panels)))
# ── b8-03 `#s-bench` · oxygen-debt ───────────────────────────────────────
#
# ⚖️ THE BREATHING BAR IS DRIVEN BY LACTATE, NOT BY PACE, AND THAT IS THE WHOLE
# LESSON. Design's own line, measured off page line 438:
#
#     breathing = min(100, round(20 + supply × 0.6 + lactate × 0.5))
#
# `pace` does not appear in it. Neither does `demand`. Nothing about the
# runner's effort reaches the breathing bar except through `supply`, which
# decays slowly, and `lactate`, which is what the recovery is for. Traced
# through Design's own numbers from a flat-out sprint:
#
#   press            supply  lactate  demand shown  breathing
#   (opening)          25       0         25          35%
#   Run 10 s           43      59        150          75%
#   Run 10 s           61     100        150         100%
#   Stop 30 s          51      78         25          90%   ← the lesson
#   Stop 30 s          41      56         25          73%
#   Stop 30 s          31      34         25          56%
#   Stop 30 s          25      12         25          41%
#   Stop 30 s          25       0         25          35%   ← ever_recovered
#
# The row marked is the point of the page. THE DEMAND BAR COLLAPSES FROM 150 TO
# 25 THE INSTANT THE RUNNER STOPS, AND THE BREATHING BAR STAYS AT 90%. A
# breathing bar that fell when the runner stopped would teach the opposite of
# the lesson, so `_od_trace` below simulates exactly that sequence at build time
# and refuses to draw the bench if it does not happen.


def _od_step(model, pace_demand, st, running):
    """One press. Design's own arithmetic, and the only copy of it in Python.

    Returned state is a fresh dict so the caller can keep the previous one — the
    assertion below needs to compare a press against the press before it.
    """
    supply, lactate = st["supply"], st["lactate"]
    if running:
        supply = min(model["supply_max"], supply + model["supply_step"])
        gap = max(0, pace_demand - supply)
        lactate = min(model["lactate_max"],
                      lactate + gap * model["lactate_factor"])
        phase, secs = "running", st["seconds"] + model["run_seconds"]
    else:
        lactate = max(0, lactate - model["recover_clear"])
        supply = (max(model["supply_rest"], supply - model["supply_decay"])
                  if lactate > 0 else model["supply_rest"])
        phase, secs = "recovering", st["seconds"] + model["recover_seconds"]
    return {"supply": supply, "lactate": lactate, "seconds": secs,
            "phase": phase,
            "ever_recovered": st["ever_recovered"] or
                              (not running and lactate == 0)}
def _od_read(model, paces, pace_id, st):
    """The four bar values and the shortfall, for a state. Design's own reads."""
    demand = (model["recover_demand"] if st["phase"] == "recovering"
              else (model["supply_rest"] if st["phase"] == "ready"
                    else next(p["demand"] for p in paces if p["id"] == pace_id)))
    b = model["breathing"]
    return {
        "demand": demand,
        "aerobic": min(st["supply"], demand),
        "lactate": _js_round(st["lactate"]),
        "breathing": min(b["max"],
                         _js_round(b["base"] + st["supply"] * b["per_supply"]
                                   + st["lactate"] * b["per_lactate"])),
        "shortfall": max(0, demand - st["supply"]),
    }
def r_oxygen_debt(a, act_id):
    """⊕ b8-03 `#s-bench` — run it, then stop, and watch what does not stop.

    ⚖️ THE ASSERTION BELOW IS THE LESSON, WRITTEN AS A TEST. The bench is
    simulated at build time at its hardest pace: two running presses, then one
    stop. If the demand bar does not collapse on that stop, or if the breathing
    bar falls with it, the build fails — because a page where breathing drops
    the moment the runner stops teaches precisely the belief `RESP-05` exists
    to break, and it would look completely normal to anyone reading the payload.

    ⚖️ RECOVERY LOWERS `supply` TOO, and that term is load-bearing. Without it
    breathing would fall on the supply half as well and the effect would be
    muddied; with it, the only thing holding breathing up after a stop is the
    lactate term. Design's `max(supply_rest, supply − 10)` while lactate
    remains, and a snap back to rest once it is gone.

    ⚖️ AND THE STOP ONLY TICKS WHEN LACTATE REACHES ZERO. A student who presses
    once and leaves has watched breathing fall from 100% to 90%, which is the
    wrong story — the debt is not repaid, it has barely been touched. Five
    presses at a sprint, and that is not padding.

    ⚠️ TWO DEAD KEYS IN DESIGN'S PAYLOAD ARE NOT CARRIED. `runDisabled: false`
    and `runStyle: ''` are constants on page lines 506–507, read for nothing, and
    would fail the key audit under R5. `stopDisabled`/`stopStyle` are real and
    are computed from `phase`, so the stop button ships `disabled` at rest and
    the runtime clears it.
    """
    _need(a, act_id, ("options_label", "paces", "start", "model", "bars",
                         "clock", "phases", "shortfall", "notes", "run_label",
                         "running_label", "stop_label", "recovering_label",
                         "reset_label"))

    paces = a["paces"]
    if len(paces) < 2:
        raise ValueError(
            "oxygen-debt %r declares %d pace(s). The bench's argument is a "
            "CONTRAST — a pace the oxygen supply covers against one it cannot — "
            "and one pace makes no contrast." % (act_id, len(paces)))
    seen = set()
    for p in paces:
        for f in ("id", "label", "demand"):
            if not p.get(f):
                raise ValueError("oxygen-debt %r pace %r declares no %r."
                                 % (act_id, p.get("id"), f))
        if p["id"] in seen:
            raise ValueError("oxygen-debt %r declares pace id %r twice."
                             % (act_id, p["id"]))
        seen.add(p["id"])
    if a["start"] not in seen:
        raise ValueError("oxygen-debt %r opens on pace %r, which it does not "
                         "offer." % (act_id, a["start"]))

    model = dict(a["model"])
    # MRB-257 (5.15) — `demand_rest` is REQUIRED. `read()` fell back to
    # `supply_rest` when it was absent, which made standing on the line cost
    # 25 units against walking's 20: the bench said standing still is more
    # expensive than walking. A fallback that produces a false reading is not
    # a fallback, so the payload has to carry it.
    for f in ("supply_rest", "demand_rest", "supply_max", "supply_step",
              "supply_decay", "recover_demand", "recover_clear",
              "lactate_factor", "lactate_max", "breathing", "run_seconds",
              "recover_seconds", "bar_divisor"):
        if model.get(f) is None:
            raise ValueError("oxygen-debt %r model declares no %r."
                             % (act_id, f))
    # ⚖️ THE BREATHING MODEL'S KEYS ARE THE STRUCTURAL FORM OF "NOT DRIVEN BY
    # PACE". If a `per_pace` or `per_demand` term ever appears here the whole
    # argument of the lesson has quietly changed, and it would still compute a
    # plausible-looking number.
    b = model["breathing"]
    if sorted(b) != ["base", "max", "per_lactate", "per_supply"]:
        raise ValueError(
            "oxygen-debt %r's breathing model declares %s. It is `base`, `max`, "
            "`per_supply` and `per_lactate` and nothing else — the entire "
            "teaching point of this lesson is that neither pace nor demand "
            "reaches the breathing bar." % (act_id, sorted(b)))
    if not b["per_lactate"] > 0:
        raise ValueError(
            "oxygen-debt %r's breathing model has `per_lactate` at %r. Lactate "
            "is the ONLY thing holding breathing up after the runner stops; at "
            "zero the bar falls with the demand and the page teaches the "
            "opposite of the lesson." % (act_id, b["per_lactate"]))

    hardest = max(paces, key=lambda p: float(p["demand"]))
    if float(hardest["demand"]) <= float(model["supply_max"]):
        raise ValueError(
            "oxygen-debt %r's hardest pace demands %g against an aerobic ceiling "
            "of %g, so no pace can ever open a shortfall and no lactic acid can "
            "ever be made. The anaerobic half of the bench is unreachable."
            % (act_id, float(hardest["demand"]), float(model["supply_max"])))
    if not any(float(p["demand"]) <= float(model["supply_max"]) for p in paces):
        raise ValueError(
            "oxygen-debt %r offers no pace inside the aerobic ceiling. The bench "
            "must be able to show the AEROBIC case or the contrast is "
            "untestable, and `notes.within` is the string for it." % act_id)

    bars = a["bars"]
    ids = [x.get("id") for x in bars]
    if sorted(ids) != ["aerobic", "breathing", "demand", "lactate"]:
        raise ValueError(
            "oxygen-debt %r draws bars %s. The four are `demand`, `aerobic`, "
            "`lactate` and `breathing` — the renderer keys each bar's value and "
            "its width off its own id, and the lesson is what the fourth does "
            "when the first collapses." % (act_id, sorted(ids)))
    for x in bars:
        for f in ("id", "name", "suffix", "tone"):
            if not x.get(f):
                raise ValueError("oxygen-debt %r bar %r declares no %r."
                                 % (act_id, x.get("id"), f))

    for f in ("zero", "suffix", "recovering"):
        if not a["clock"].get(f):
            raise ValueError("oxygen-debt %r clock declares no %r."
                             % (act_id, f))
    for f in ("ready", "recovering"):
        if not a["phases"].get(f):
            raise ValueError("oxygen-debt %r phases declares no %r."
                             % (act_id, f))
    for f in ("aerobic", "repaying", "borrowed"):
        if not a["shortfall"].get(f):
            raise ValueError("oxygen-debt %r shortfall declares no %r."
                             % (act_id, f))
    if "{n}" not in a["shortfall"]["borrowed"]:
        raise ValueError(
            "oxygen-debt %r's shortfall.borrowed names no {n}. How many units "
            "are being borrowed is the one number that line is for." % act_id)
    # MRB-257 (5.13 / 5.14) — SEVEN NOTES, NOT FIVE. `nothing_to_repay` is the
    # state where the runner never went anaerobic, which `cleared` was claiming
    # ("the debt is paid" over an acid bar that read 0 throughout);
    # `within_with_lactate` is the state where supply has caught up but the
    # acid already made is still there, which `within` was denying ("nothing is
    # building up" over a bar reading 4 units). Both are reachable in three
    # presses and both had the engine falling back to a note that is false of
    # them, so both are required rather than optional.
    for f in ("rest", "within", "within_with_lactate", "shortfall", "debt",
              "cleared", "nothing_to_repay"):
        if not a["notes"].get(f):
            raise ValueError(
                "oxygen-debt %r notes declares no %r. All seven are reachable "
                "states of the bench, and a state with no note of its own "
                "falls back to one that is false of it."
                % (act_id, f))
    if "{n}" not in a["notes"]["shortfall"]:
        raise ValueError(
            "oxygen-debt %r's notes.shortfall names no {n}. The size of the gap "
            "is what that note is telling the student." % act_id)

    # MRB-257 (5.15) — and it must be BELOW the resting supply, or "at rest"
    # is not what the bars are showing; and below every pace, or standing
    # still is not the cheapest thing on the list.
    if float(model["demand_rest"]) >= float(model["supply_rest"]):
        raise ValueError(
            "oxygen-debt %r has demand_rest %g against supply_rest %g. At rest "
            "the supply has to comfortably exceed the demand — that is what "
            "'at rest' means, and the bars say so."
            % (act_id, float(model["demand_rest"]), float(model["supply_rest"])))
    cheapest = min(float(p["demand"]) for p in paces)
    if float(model["demand_rest"]) >= cheapest:
        raise ValueError(
            "oxygen-debt %r has demand_rest %g against a cheapest pace of %g, "
            "so the bench says standing on the line costs at least as much as "
            "moving (5.15)." % (act_id, float(model["demand_rest"]), cheapest))

    # ── the assertion that IS the lesson ──────────────────────────────────
    rest = {"supply": float(model["supply_rest"]), "lactate": 0.0,
            "seconds": 0, "phase": "ready", "ever_recovered": False}
    hard = float(hardest["demand"])
    st = _od_step(model, hard, _od_step(model, hard, rest, True), True)
    running = _od_read(model, paces, hardest["id"], st)
    st_stopped = _od_step(model, hard, st, False)
    stopped = _od_read(model, paces, hardest["id"], st_stopped)
    at_rest = _od_read(model, paces, hardest["id"], rest)

    if not stopped["demand"] < running["demand"]:
        raise ValueError(
            "oxygen-debt %r: stopping does not drop the demand bar (%g running, "
            "%g stopped). The student is asked to watch one bar collapse while "
            "another does not, and there is nothing to see."
            % (act_id, running["demand"], stopped["demand"]))
    if not stopped["breathing"] > at_rest["breathing"]:
        raise ValueError(
            "oxygen-debt %r: breathing after stopping is %g%%, at rest it is "
            "%g%%. The whole page asks why you keep breathing hard AFTER you "
            "stop; if the bar has already come home there is no question."
            % (act_id, stopped["breathing"], at_rest["breathing"]))
    if stopped["breathing"] < 0.8 * running["breathing"]:
        raise ValueError(
            "oxygen-debt %r: breathing falls from %g%% to %g%% on the first "
            "stop — it follows the demand down. THE BREATHING BAR IS DRIVEN BY "
            "LACTATE, NOT BY PACE. A bar that drops when the runner stops "
            "teaches the opposite of this lesson."
            % (act_id, running["breathing"], stopped["breathing"]))

    # ...and that the stop can actually be reached, in a bounded number of
    # presses, from the hardest pace — the state that takes the longest.
    walk, presses = st, 0
    while not walk["ever_recovered"] and presses < 50:
        walk = _od_step(model, hard, walk, False)
        presses += 1
    if not walk["ever_recovered"]:
        raise ValueError(
            "oxygen-debt %r never clears its lactate, so `ever_recovered` is "
            "unreachable and the rail stop can never tick." % act_id)

    # ⚠️ EVERY ONE OF THESE REACHES THE PAGE AS `textContent`, NOT AS MARKUP.
    # The phase label, the shortfall line, the five notes and the four button
    # labels are all written in by the runtime, so `t()` never sees them and a
    # drawn mark typed into one would ship as tofu. See `_attr_safe`.
    for f, v in sorted(a["phases"].items()):
        _attr_safe(v, act_id, "phases.%s" % f)
    for f, v in sorted(a["shortfall"].items()):
        _attr_safe(v, act_id, "shortfall.%s" % f)
    for f, v in sorted(a["notes"].items()):
        _attr_safe(v, act_id, "notes.%s" % f)
    for f in ("run_label", "running_label", "stop_label", "recovering_label"):
        _attr_safe(a[f], act_id, "`%s`" % f)
    for p in paces:
        _attr_safe(p["label"], act_id, "pace %r `label`" % p["id"])
    for x in bars:
        _attr_safe(x["suffix"], act_id, "bar %r `suffix`" % x["id"])

    div = float(model["bar_divisor"])
    lact_max = float(model["lactate_max"])

    def width(bar_id, v):
        """How full each bar draws. ⚠️ THREE RULES, NOT ONE.

        `bar_divisor` APPLIES TO `demand` AND `aerobic` ONLY. Those two are in
        arbitrary energy units running past the 100-mark — a flat-out sprint
        demands 150 — so they are scaled to fit the track. The other two are
        already on their own 0–100 scales and are drawn at their own value.

        Dividing all four by 1.6 would render a maxed breathing bar at 62% and
        cost the lesson its punchline: a breathing bar that visibly TOPS OUT,
        and stays there after the runner stops, is the evidence the student is
        meant to read. Design's own arithmetic, and the reason it looks
        inconsistent is that the four bars are not in the same units.
        """
        if bar_id == "breathing":
            return min(100.0, float(v))
        if bar_id == "lactate":
            return min(100.0, float(v) * 100.0 / lact_max)
        return min(100.0, float(v) / div)

    open_read = at_rest
    rows = "".join(
        '<li class="ks3-od-bar" data-tone="%s">'
        '<div class="ks3-od-barhead">'
        '<p class="ks3-od-barname">%s</p>'
        '<p class="ks3-od-barvalue" data-od-bar="%s" data-suffix="%s">%s</p>'
        '</div>'
        '<span class="ks3-od-track"><span class="ks3-od-fill" '
        'data-od-fill="%s" style="width:%s%%"></span></span></li>'
        % (e(x["tone"]), t(x["name"]), e(x["id"]), e(x["suffix"]),
           t(_with_suffix(open_read[x["id"]], x["suffix"])), e(x["id"]),
           _pctnum(width(x["id"], open_read[x["id"]])))
        for x in bars)

    tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-od-tab" '
        'data-od-pace="%s" data-demand="%s" data-label="%s" aria-pressed="%s">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(p["id"]), e(_pctnum(p["demand"])), e(p["label"]),
           "true" if p["id"] == a["start"] else "false", t(p["label"]))
        for p in paces)

    return ('<div class="ks3-od" data-od data-model="%s" data-labels="%s" '
            'data-phases="%s" data-shortfall="%s" data-notes="%s" '
            'data-lactate-max="%s" data-bar-divisor="%s">'
            '<div class="ks3-od-tabsgroup">'
            '<p class="ks3-od-tabslabel" id="%s-paces">%s</p>'
            '<ul class="ks3-options ks3-od-tabs" role="list" '
            'aria-labelledby="%s-paces">%s</ul></div>'
            '<div class="ks3-od-panel">'
            '<div class="ks3-od-headrow">'
            '<p class="ks3-od-phase" data-od-phase>%s</p>'
            '<p class="ks3-od-shortfall" data-od-shortfall>%s</p></div>'
            '<ul class="ks3-od-bars" role="list">%s</ul>'
            '<p class="ks3-od-note" data-od-note>%s</p>'
            '<div class="ks3-od-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-od-run" '
            'data-od-run>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-od-stop" '
            'data-od-stop disabled>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-od-reset" '
            'data-od-reset>%s</button></div></div></div>'
            % (e(json.dumps(model, separators=(",", ":"), sort_keys=True)),
               e(json.dumps({"run": a["run_label"],
                             "running": a["running_label"],
                             "stop": a["stop_label"],
                             "recovering": a["recovering_label"]},
                            separators=(",", ":"), sort_keys=True)),
               e(json.dumps(a["phases"], separators=(",", ":"),
                            sort_keys=True)),
               e(json.dumps(a["shortfall"], separators=(",", ":"),
                            sort_keys=True)),
               e(json.dumps(a["notes"], separators=(",", ":"), sort_keys=True)),
               e(_pctnum(lact_max)), e(_pctnum(div)),
               e(act_id), t(a["options_label"]), e(act_id), tabs,
               t(a["phases"]["ready"]), t(a["shortfall"]["aerobic"]), rows,
               rich(a["notes"]["rest"]),
               t(a["run_label"]), t(a["stop_label"]), t(a["reset_label"])))
# ── b8-04 `#s-bench` · fermenter ─────────────────────────────────────────
#
# ⛔ `products` IS AUTHORED PER BRANCH AND IS NEVER DERIVED FROM `line`.
#
# This is the whole shape of the renderer and it exists because of a real
# defect on the approved page. Design computes which product list to show with
#
#     const aerobic = out.line.indexOf('oxygen') >= 0;      // page line 478
#
# — a string sniff on the reaction text — and it is wrong on one live branch.
# Yoghurt bacteria in an OPEN, STIRRED vessel take `line = "contaminated"`,
# which contains no `"oxygen"`, so the sniff falls through to the anaerobic
# bacteria list and the bench prints **"Lactic acid 100 units"** underneath its
# own heading *"Poor conditions for these bacteria"*. The panel contradicts
# itself, and it contradicts the chemistry: lactic acid is what the FERMENTATION
# route makes, and that route is the one that runs when oxygen is absent.
#
# Reading `products` off the record removes the sniff and the defect with it.
# The guard below then makes the defect unreachable by a later edit rather than
# merely absent today — contract §1 (MRB-205, *page wins over engine*) yielding
# to fact, which is the one direction it yields in.
#
# ⚖️ AND THE YEAST OPEN-AND-STIRRED BRANCH IS NOT A FAILURE STATE. It is how
# yeast is manufactured, in open stirred tanks, and it is the branch that
# teaches why a brewer seals the vessel. Its rate is 100, it takes no error
# treatment, no amber, no alert border — it is drawn exactly like every other
# outcome. Nothing in this renderer or its stylesheet may single it out.

# Products of the fermentation route and of nothing else at this key stage.
# Named here because the assertion below is a statement about CHEMISTRY rather
# than about b8-04: whatever the branch is called, an organism supplied with
# oxygen in a stirred vessel is not running the route that makes these.
_FM_ANAEROBIC_ONLY = ("ethanol", "lactic acid")
def _fm_matches(when, dials_state):
    """Design's own first-match-wins: a branch fires when every pin agrees."""
    for dial, option in when.items():
        if dials_state.get(dial) != option:
            return False
    return True
def r_fermenter(a, act_id):
    """⊕ b8-04 `#s-bench` — one vessel, four dials, ten branches, eight texts.

    ⚖️ THE PRECEDENCE IS ORDERED AND THE ORDER IS THE PEDAGOGY. Design's own
    comment reads *"Order matters: killed beats starved beats aerobic beats
    fermenting."* A dead culture is dead whatever else is set; a culture with no
    sugar has nothing to respire however perfect the other three dials are. Read
    from the authored list and never from a dict, so re-sorting a literal cannot
    silently change which outcome a student reaches.

    ⚖️ EVERY BRANCH IS DRAWN IN FULL AND HIDDEN, rather than being written in by
    the runtime. That is not a style preference: the reaction lines carry `→`,
    which is a DRAWN mark — `t()` swaps it for an `<svg>` because no shipped font
    subset contains the codepoint. A line routed through a data attribute and
    assigned to `textContent` would ship the raw codepoint and render as tofu in
    the middle of an equation. Static markup keeps `t()` in the path. See
    `_attr_safe`, which fences the attribute routes this deliberately avoids.

    ⚠️ EXHAUSTIVE AND REACHABLE, BOTH ASSERTED. Every combination of the dials
    must match some branch — an unmatched one is a bench that goes blank in a
    student's hands — and every branch must be the FIRST match for at least one
    combination, because Design's copy is lifted byte-identical and an
    unreachable branch is a paragraph of hers that no student will ever read.
    """
    dials = _dials(a, act_id, ())
    _need(a, act_id, ("start", "presets", "rate_label", "outcome_label",
                         "branches", "done_after"))

    dial_ids = [d["id"] for d in dials]
    opts_of = {d["id"]: [o["id"] for o in d["options"]] for d in dials}

    def check_setting(name, mapping):
        if sorted(mapping) != sorted(dial_ids):
            raise ValueError(
                "fermenter %r's %s sets %s but the bench has dials %s. A "
                "setting that misses a dial leaves it wherever it was, and one "
                "naming a dial that is not there is a position nothing can "
                "apply." % (act_id, name, sorted(mapping), sorted(dial_ids)))
        for d, o in sorted(mapping.items()):
            if o not in opts_of[d]:
                raise ValueError(
                    "fermenter %r's %s sets dial %r to %r, which is not one of "
                    "its settings." % (act_id, name, d, o))

    check_setting("`start`", a["start"])
    for p in a["presets"]:
        for f in ("id", "label", "dials"):
            if not p.get(f):
                raise ValueError("fermenter %r preset %r declares no %r."
                                 % (act_id, p.get("id"), f))
        check_setting("preset %r" % p["id"], p["dials"])

    if "{n}" not in a["rate_label"]:
        raise ValueError(
            "fermenter %r's rate_label names no {n}. The rate is the number "
            "that line is for." % act_id)

    branches = list(a["branches"])
    if len(branches) < 2:
        raise ValueError(
            "fermenter %r declares %d branch(es). The bench's argument is that "
            "the same four dials give different products."
            % (act_id, len(branches)))

    seen = set()
    for br in branches:
        for f in ("id", "when", "rate", "line", "title", "body", "products"):
            if br.get(f) is None or br.get(f) == "":
                raise ValueError(
                    "fermenter %r branch %r declares no %r. ⛔ `products` is "
                    "authored per branch and is NEVER derived from `line` — "
                    "that string sniff is the defect this renderer exists to "
                    "make unreachable." % (act_id, br.get("id"), f))
        if br["id"] in seen:
            raise ValueError("fermenter %r declares branch id %r twice."
                             % (act_id, br["id"]))
        seen.add(br["id"])
        for d, o in sorted(br["when"].items()):
            if d not in opts_of:
                raise ValueError(
                    "fermenter %r branch %r pins dial %r, which the bench does "
                    "not have." % (act_id, br["id"], d))
            if o not in opts_of[d]:
                raise ValueError(
                    "fermenter %r branch %r pins dial %r to %r, which is not "
                    "one of its settings." % (act_id, br["id"], d, o))
        rate = float(br["rate"])
        if not 0 <= rate <= 100:
            raise ValueError("fermenter %r branch %r has rate %g, outside "
                             "0–100." % (act_id, br["id"], rate))

        for pr in br["products"]:
            if not pr.get("name") or not pr.get("tone"):
                raise ValueError(
                    "fermenter %r branch %r has a product missing `name` or "
                    "`tone`." % (act_id, br["id"]))
            has_v, has_n = bool(pr.get("value")), bool(pr.get("none_text"))
            if has_v == has_n:
                raise ValueError(
                    "fermenter %r branch %r product %r declares %s `value` and "
                    "`none_text`. Exactly one: a product either has a reading "
                    "or it has the words that say why it has none."
                    % (act_id, br["id"], pr["name"],
                       "both" if has_v else "neither"))
            if rate == 0 and has_v:
                raise ValueError(
                    "fermenter %r branch %r runs at rate 0 but prints a reading "
                    "for %r. Nothing is being made on this branch, so every "
                    "product says so in words."
                    % (act_id, br["id"], pr["name"]))

        # ⛔ THE CORRECTION, MADE UNREACHABLE RATHER THAN MERELY ABSENT.
        #
        # An aerobic branch produces no ethanol and no lactic acid. Both are
        # fermentation products — the route that makes them is the one that runs
        # when oxygen is absent — so a branch the student reached by OPENING the
        # vessel cannot report either of them as a positive reading. This is the
        # exact defect Design's `line.indexOf('oxygen')` sniff produced.
        #
        # A branch is aerobic on either of two authored signals: its `id` names
        # it so, or its `when` pins a dial to the `open` setting. The union is
        # deliberate — renaming the branch does not disarm the check, and neither
        # does rewording the reaction line. Both are false-NEGATIVE risks only;
        # neither can fail a correct payload.
        aerobic = (str(br["id"]).startswith("aerobic")
                   or "open" in br["when"].values())
        if aerobic:
            for pr in br["products"]:
                if (pr.get("value")
                        and pr["name"].strip().lower() in _FM_ANAEROBIC_ONLY):
                    raise ValueError(
                        "fermenter %r branch %r is aerobic and reports %r as a "
                        "positive reading. An aerobic branch produces no %s: "
                        "that is a fermentation product, and fermentation is "
                        "the route that runs when oxygen is ABSENT. This is the "
                        "defect Design's `line.indexOf('oxygen')` sniff "
                        "produced — the bench printed \"Lactic acid 100 units\" "
                        "under the words \"Poor conditions for these bacteria\"."
                        % (act_id, br["id"], pr["name"], pr["name"].lower()))

    # ── exhaustive, and every branch reachable ────────────────────────────
    combos, stack = [{}], list(dials)
    for d in stack:
        combos = [dict(c, **{d["id"]: o}) for c in combos
                  for o in opts_of[d["id"]]]
    hit = set()
    for c in combos:
        for br in branches:
            if _fm_matches(br["when"], c):
                hit.add(br["id"])
                break
        else:
            raise ValueError(
                "fermenter %r has no branch for %s. The bench would go blank in "
                "a student's hands, with every dial legally set."
                % (act_id, sorted(c.items())))
    dead = [br["id"] for br in branches if br["id"] not in hit]
    if dead:
        raise ValueError(
            "fermenter %r declares branch(es) %s that no setting of the dials "
            "reaches first. Design's copy is lifted byte-identical, so an "
            "unreachable branch is a paragraph of hers no student will read."
            % (act_id, ", ".join(map(repr, dead))))

    after = int(a["done_after"])
    if not 1 <= after <= len(combos):
        raise ValueError(
            "fermenter %r completes after %d set-up(s). A threshold at or below "
            "zero ticks the stop on load." % (act_id, after))

    # ⚠️ Attribute paths only. The reaction lines, titles and bodies are drawn
    # into static markup below, where `t()` can draw the arrow.
    for p in a["presets"]:
        _attr_safe(p["label"], act_id, "preset %r `label`" % p["id"])

    def branch_block(br, shown):
        rate = float(br["rate"])
        return (
            '<div class="ks3-fm-branch" data-fm-branch="%s"%s>'
            '<div class="ks3-fm-headrow">'
            '<p class="ks3-fm-line">%s</p>'
            '<p class="ks3-fm-rate">%s</p></div>'
            '<ul class="ks3-fm-products" role="list">%s</ul>'
            '<div class="ks3-fm-outcome">'
            '<p class="ks3-fm-outcomelabel">%s</p>'
            '<p class="ks3-fm-title">%s</p>'
            '<p class="ks3-fm-body">%s</p></div></div>'
            % (e(br["id"]), "" if shown else " hidden",
               t(br["line"]),
               t(a["rate_label"].replace("{n}", _pctnum(rate))),
               "".join(
                   '<li class="ks3-fm-product" data-tone="%s">'
                   '<div class="ks3-fm-prodhead">'
                   '<p class="ks3-fm-prodname">%s</p>'
                   '<p class="ks3-fm-prodvalue">%s</p></div>'
                   '<span class="ks3-fm-track"><span class="ks3-fm-fill" '
                   'style="width:%s%%"></span></span></li>'
                   % (e(pr["tone"]), t(pr["name"]),
                      t(pr.get("value") or pr.get("none_text")),
                      _pctnum(rate if pr.get("value") else 0))
                   for pr in br["products"]),
               t(a["outcome_label"]), t(br["title"]), rich(br["body"])))

    opening = next(br for br in branches if _fm_matches(br["when"], a["start"]))

    return ('<div class="ks3-fm" data-fm data-branches="%s" data-start="%s" '
            'data-done-after="%d">%s'
            '<div class="ks3-fm-panel">%s'
            '<div class="ks3-fm-foot">%s</div></div></div>'
            % (e(json.dumps([{"id": br["id"], "when": br["when"]}
                             for br in branches],
                            separators=(",", ":"), sort_keys=True)),
               e(json.dumps(a["start"], separators=(",", ":"), sort_keys=True)),
               after,
               _dial_block("fm", act_id, dials, a["start"],
                              lambda d, o: ""),
               "".join(branch_block(br, br["id"] == opening["id"])
                       for br in branches),
               "".join(
                   '<button type="button" class="ks3-reveal-btn ks3-fm-preset" '
                   'data-fm-preset="%s">%s</button>'
                   % (e(json.dumps(p["dials"], separators=(",", ":"),
                                   sort_keys=True)), t(p["label"]))
                   for p in a["presets"])))
# ── b8-05 `#s-bench` · route-decider ─────────────────────────────────────
#
# ⚖️ THE MARATHON IS THE INSTRUMENT, AND THIS RENDERER'S JOB IS TO PROTECT IT.
# Four of the five cases fall out of asking "is the oxygen supply keeping up?".
# The marathon is the one where "is the runner working hard?" answers the
# opposite way, and it is the case the lesson is built on. A student must
# therefore be given NOTHING that lets them read a case's route before they
# commit to it: `answer` travels in the block's JSON and is never written into
# a tab label, an `aria-label` or a `title`. The lesson record's docstring
# makes that promise and this is where it is kept.
#
# ⚠️ NO GREEN, NO RED, NOTHING ON AN OPTION BUTTON — the house rule, and
# MRB-196 R10 for a CONTRAST lesson. Only the ladder marks correctness. A
# settled case's route button looks exactly like any other pressed option
# whether the student had it or not; `verdicts` carries two WORDS and they are
# the entire marking surface. There is deliberately no tone key for a renderer
# to reach for later.
def r_route_decider(a, act_id):
    """b8-05's five-case bench: commit to a route, check it, read a verdict."""
    _need(a, act_id,
             ("cases_label", "options_label", "routes", "cases", "progress",
              "tally", "run_label", "ran_label", "done_after"),
             "Payload schema §6 names it; the block cannot render without it.")

    routes, cases = a["routes"], a["cases"]

    route_ids = []
    for r in routes:
        for k in ("id", "text"):
            if not r.get(k):
                raise ValueError("route-decider %r has a route with no %r."
                                 % (act_id, k))
        if r["id"] in route_ids:
            raise ValueError("route-decider %r declares route id %r twice."
                             % (act_id, r["id"]))
        route_ids.append(r["id"])
    if len(route_ids) < 2:
        raise ValueError(
            "route-decider %r offers %d route(s). A bench that asks for a "
            "commitment needs something to commit BETWEEN."
            % (act_id, len(route_ids)))

    seen = []
    for c in cases:
        for k in ("id", "label", "text", "answer", "why"):
            if not c.get(k):
                raise ValueError("route-decider %r case %r declares no %r. "
                                 "`why` is the verdict panel's whole content — "
                                 "without it the bench settles a case and then "
                                 "says nothing about it."
                                 % (act_id, c.get("id"), k))
        if c["id"] in seen:
            raise ValueError("route-decider %r declares case id %r twice."
                             % (act_id, c["id"]))
        seen.append(c["id"])
        if c["answer"] not in route_ids:
            raise ValueError(
                "route-decider %r case %r answers %r, which is not one of the "
                "routes %s. The verdict would name a button that is not on the "
                "page." % (act_id, c["id"], c["answer"], route_ids))

    if int(a["done_after"]) != len(cases):
        raise ValueError(
            "route-decider %r completes after %s of %d case(s). The bench's "
            "argument is that one case catches almost everybody, so a stop "
            "that ticks early lets a student leave before meeting it."
            % (act_id, a["done_after"], len(cases)))

    for token in ("{n}", "{total}"):
        if token not in a["progress"]:
            raise ValueError("route-decider %r's progress names no %s."
                             % (act_id, token))
    tally = a["tally"]
    for k in ("remaining", "all"):
        if not tally.get(k):
            raise ValueError("route-decider %r's tally declares no %r."
                             % (act_id, k))
    if "{n}" not in tally["remaining"]:
        raise ValueError("route-decider %r's tally.remaining names no {n}."
                         % act_id)

    verdicts = _verdict_ids(
        a, act_id, ("right", "wrong"),
        "The verdict panel is the only place a case's route is named, and it "
        "has to be able to say both things in words.")

    # ⚠️ `answer` and `why` are NOT written into the tab. See the section note.
    tabs = "".join(
        '<li><button type="button" class="ks3-option ks3-rd-case" '
        'data-rd-case="%s" aria-pressed="%s">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(c["id"]), "true" if i == 0 else "false", t(c["label"]))
        for i, c in enumerate(cases))

    opts = "".join(
        '<li><button type="button" class="ks3-option ks3-rd-route" '
        'data-rd-route="%s" aria-pressed="false">'
        '<span class="ks3-opt-label">%s</span></button></li>'
        % (e(r["id"]), t(r["text"])) for r in routes)

    return ('<div class="ks3-rd" data-rd data-cases="%s" data-verdicts="%s" '
            'data-progress="%s" data-tally="%s" data-labels="%s" '
            'data-done-after="%d">'
            '<div class="ks3-rd-casesgroup">'
            '<p class="ks3-rd-caseslabel" id="%s-cases">%s</p>'
            '<ul class="ks3-options ks3-rd-cases" role="list" '
            'aria-labelledby="%s-cases">%s</ul></div>'
            '<div class="ks3-rd-panel">'
            '<p class="ks3-rd-text" data-rd-text>%s</p>'
            '<p class="ks3-rd-routeslabel" id="%s-routes">%s</p>'
            '<ul class="ks3-options ks3-rd-routes" role="list" '
            'aria-labelledby="%s-routes">%s</ul>'
            '<div class="ks3-rd-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-rd-run" '
            'data-rd-run disabled>%s</button>'
            '<p class="ks3-rd-progress" data-rd-progress>%s</p></div>'
            '<div class="ks3-rd-verdict" data-rd-verdict hidden>'
            '<p class="ks3-rd-word" data-rd-word></p>'
            '<p class="ks3-rd-why" data-rd-why></p></div>'
            '<p class="ks3-rd-tally" data-rd-tally>%s</p></div>%s</div>'
            % (e(json.dumps([{"id": c["id"], "text": c["text"],
                              "answer": c["answer"], "why": c["why"]}
                             for c in cases],
                            separators=(",", ":"), sort_keys=True)),
               e(json.dumps(verdicts, separators=(",", ":"), sort_keys=True)),
               e(a["progress"]),
               e(json.dumps(tally, separators=(",", ":"), sort_keys=True)),
               e(json.dumps({"run": a["run_label"], "ran": a["ran_label"]},
                            separators=(",", ":"), sort_keys=True)),
               int(a["done_after"]),
               e(act_id), t(a["cases_label"]), e(act_id), tabs,
               rich(cases[0]["text"]),
               e(act_id), t(a["options_label"]), e(act_id), opts,
               t(a["run_label"]),
               t(a["progress"].replace("{n}", "0")
                              .replace("{total}", str(len(cases)))),
               t(tally["remaining"].replace("{n}", str(len(cases)))),
               _self_check(a, act_id)))


# ── registrations ────────────────────────────────────────────────────────
KIND_SHELL = {
    'mass-ledger': ("ks3-ml-block",
                      ' data-instrument data-mlblock data-stage-done="0"'),
    'cell-demand': ("ks3-cd-block",
                      ' data-instrument data-cdblock data-stage-done="0"'),
    'oxygen-debt': ("ks3-od-block",
                      ' data-instrument data-odblock data-stage-done="0"'),
    'fermenter': ("ks3-fm-block",
                      ' data-instrument data-fmblock data-stage-done="0"'),
    'route-decider': ("ks3-rd-block",
                      ' data-instrument data-rdblock data-stage-done="0"'),
}

KIND_FN = {
    'mass-ledger': r_mass_ledger,
    'cell-demand': r_cell_demand,
    'oxygen-debt': r_oxygen_debt,
    'fermenter': r_fermenter,
    'route-decider': r_route_decider,
}

KIND_HEAD_TOTAL = {
    'route-decider': lambda a: len(a.get("cases") or []),
}

KIND_HEAD_FROM = {
    'oxygen-debt': lambda a: {
        "zero": (a.get("clock") or {}).get("zero") or "",
        "running": "{n}%s" % ((a.get("clock") or {}).get("suffix") or ""),
        "recovering": "{n}%s%s" % ((a.get("clock") or {}).get("suffix") or "",
                                   (a.get("clock") or {}).get("recovering")
                                   or ""),
    },
}
