"""ks3_art.b6 — B6's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing
here may be added to any other unit's module. Moved verbatim out of
``build_ks3.py`` by MRB-271 so that two content lanes can build two
units at once without editing the same file.
"""

import re
from ks3_art.kit import (
    e,
    option_letter,
    rich,
    t,
)


# renderers: ═══ END B4 ═══


# renderers: ═══ BEGIN B6 ═══
#
# Three lessons, three instruments, and every one of them on ink.
#
# ⚠️ SAME TRAP AS B4, SAME COUNT OF PAGES IT WOULD TAKE. All three B6
# practicals are `ks3-block ks3-dark ks3-practical` — measured off Design's
# markup on all three pages — so `.ks3-dark p` at (0,1,1) beats a bare
# instrument class at (0,1,0) on every one of them at once. Every colour rule
# these three hang on is scoped `.ks3-dark …` in `shared/ks3.css`, and the
# ELEMENTS that invert to the cream ground inside the ink block are listed
# there by element rather than by panel. B4 counted panels and shipped a label
# inside a listed panel at 1.21:1.
#
# ⚠️ NOTHING IN B6 ANIMATES, NOTHING USES A TIMER, AND NOTHING DRAWS A CANVAS.
# NOTES-B6 §4 says it of the unit and it is true of the engine: all three are
# pure functions of their controls' state. There is no rAF loop here to test
# `prefers-reduced-motion` inside, and the stylesheet's platform-wide
# reduced-motion block already removes every transition these three carry.
#
# ⚠️ TONE IS A GATE ON THIS UNIT AND IT REACHES INTO THE ENGINE. No renderer
# below computes, formats, rounds or scales a quantity of any substance. There
# is no dose in B6, no threshold, no method, and the one instrument that counts
# anything counts HOURS OF WAITING. If a future pass finds itself writing a
# number-formatting helper in this section, that is the signal to stop.


def r_route_tracer(a, act_id):
    """⊕ b6-01 `#s-dose` — one dose, five stages, and stage 3 is the lesson.

    ⚖️ STAGE 3 IS THE INSTRUMENT. *Once round the whole body* is the stage that
    kills `DRUG-02` — the belief that a painkiller travels to the part that
    hurts — and NOTES-B6 §2.1 says so in as many words: "do not let a future
    revision collapse stages 2 and 3 to save space." Stage 2 says the drug is
    dissolved in plasma with no address on it; stage 3 says every organ is then
    offered it. Merged, the sentence that remains is a fact about blood rather
    than an argument about side effects, and stage 5's *and everywhere else*
    panel loses the thing it is the consequence of. This renderer therefore
    accepts exactly five stages and raises on any other number, which is a
    weaker guarantee than the one the lesson needs — nothing here can read
    prose — but it is the one that makes the collapse a build failure rather
    than an edit nobody notices.

    ⚖️ ONLY TWO OF THE FIVE STAGES BELONG TO THE DRUG, and that is the argument
    rather than an economy. Stage 1 is the drug's own `entry` and stage 4 its
    own `target`; stages 2, 3 and 5 are the SAME SENTENCES for caffeine,
    paracetamol, nicotine and alcohol, because the middle of the journey does
    not depend on which molecule is making it. A student who tabs between four
    drugs and watches the two ends change while the middle stays word-for-word
    identical has been shown the generalisation, not told it. `body_from` is
    what keeps that sharing declared: a stage either carries one `body` for
    every drug or names the per-drug key it takes.

    ⚠️ CHANGING DRUG RESETS TO STAGE 0, and the reset is Design's own
    (`onClick: this.setState({ drug: d.id, step: 0 })`). Without it a student
    who reached the end on caffeine would tap Nicotine and be shown nicotine's
    *where else the same dose went* panel having followed none of nicotine's
    route — the payoff handed over with the argument skipped, which is the one
    thing the block is built to prevent.

    ⚠️ NO DOSE, NO THRESHOLD, NO TIMING, AND NO NUMBER AT ALL. The only
    numerals this renderer emits are the five stage ordinals. NOTES-B6 §1 makes
    that a gate on the unit and §2.1 records that the tracer "deliberately
    shows a route without a quantity"; there is nothing here to format one
    with, and adding one would be a content decision made in the generator.
    """
    drugs = a.get("drugs") or []
    if len(drugs) < 2:
        raise ValueError(
            "route-tracer %r declares %d drug(s). The block's argument is that "
            "four different molecules take the SAME route and differ only at "
            "the two ends of it, and one drug cannot make that argument — "
            "there would be nothing to tab between and nothing held constant."
            % (act_id, len(drugs)))

    seen = []
    for d in drugs:
        for key in ("id", "label", "name", "klass", "where", "verdict"):
            if not d.get(key):
                raise ValueError(
                    "route-tracer %r drug %r is missing %r. `klass` is the "
                    "mono line beside the name (“Stimulant”, "
                    "“Depressant”) and `verdict` is the cream panel "
                    "that closes the journey; neither has a default, because "
                    "both are science."
                    % (act_id, d.get("id"), key))
        if d["id"] in seen:
            raise ValueError(
                "route-tracer %r declares drug id %r twice. The id is what the "
                "tab, the stage list and the closing panel are matched on, so "
                "a duplicate shows two drugs' text at once."
                % (act_id, d["id"]))
        seen.append(d["id"])

        elsewhere = d.get("elsewhere") or []
        if not elsewhere:
            raise ValueError(
                "route-tracer %r drug %r declares no `elsewhere` rows. That "
                "panel IS stage 5 — it is where the same dose went, and a "
                "drug that reaches the end of the route with nothing to show "
                "there has demonstrated that a drug goes to one place."
                % (act_id, d["id"]))
        for row in elsewhere:
            if not (row.get("organ") and row.get("effect")):
                raise ValueError(
                    "route-tracer %r drug %r has an `elsewhere` row missing "
                    "`organ` or `effect`." % (act_id, d["id"]))

    stages = a.get("stages") or []
    if len(stages) != 5:
        raise ValueError(
            "route-tracer %r declares %d stage(s), not 5. The five are: in → "
            "into the blood → once round the whole body → it acts where it "
            "fits → and everywhere else it reached. STAGE 3 IS THE POINT OF "
            "THE INSTRUMENT (NOTES-B6 §2.1) and it is the one a tidy-up "
            "reaches for, because on its own it reads like a restatement of "
            "stage 2. It is not: stage 2 says the molecule has no address, "
            "stage 3 says every organ is offered it anyway, and only the "
            "second of those makes stage 5 a consequence rather than a list."
            % (act_id, len(stages)))

    for i, st in enumerate(stages):
        if not st.get("title"):
            raise ValueError(
                "route-tracer %r stage %d has no `title`. The title is visible "
                "before the stage is reached — it is the map of the journey a "
                "student reads at step 0 — so a blank one is a numbered row "
                "with nothing in it." % (act_id, i + 1))
        has_body = bool(st.get("body"))
        has_from = bool(st.get("body_from"))
        if has_body == has_from:
            raise ValueError(
                "route-tracer %r stage %d needs exactly one of `body` (the "
                "same sentence for every drug) and `body_from` (the name of "
                "the per-drug key it takes). It declares %s. The distinction "
                "is the block's argument: stages 2, 3 and 5 are shared "
                "BECAUSE the middle of the route does not depend on the "
                "molecule, and a stage that quietly carried both would let "
                "one of them win silently."
                % (act_id, i + 1, "both" if has_body else "neither"))
        if has_from:
            for d in drugs:
                if not d.get(st["body_from"]):
                    raise ValueError(
                        "route-tracer %r stage %d takes its body from %r and "
                        "drug %r has no such key. The stage would be reached "
                        "with nothing under it for that drug alone, which is "
                        "the hardest kind of gap to see: three tabs correct "
                        "and the fourth silently short."
                        % (act_id, i + 1, st["body_from"], d["id"]))

    titles = [st["title"] for st in stages]
    if len(set(titles)) != len(titles):
        raise ValueError(
            "route-tracer %r declares two stages with the same title. The five "
            "titles are the map of the journey and a repeated one reads as the "
            "student not having advanced." % act_id)

    for key in ("dose_label", "elsewhere_label", "reset_label"):
        if not a.get(key):
            raise ValueError(
                "route-tracer %r declares no %r." % (act_id, key))

    nxt = a.get("next_labels") or {}
    missing = sorted({"start", "more", "done"} - set(nxt))
    if missing:
        raise ValueError(
            "route-tracer %r next_labels is missing %s. The advance button "
            "says three different things — take the dose, next stage, journey "
            "complete — and the first of the three is the only instruction a "
            "student gets at step 0. A button with no words is not a control."
            % (act_id, ", ".join(missing)))

    start = a.get("start_drug") or drugs[0]["id"]
    if start not in seen:
        raise ValueError(
            "route-tracer %r opens on start_drug %r, which is not one of %s."
            % (act_id, start, seen))

    def switched(tag, cls, value_of, attr="data-for"):
        """Emit every drug's variant, show the one the block opens on."""
        return "".join(
            '<%s class="%s" %s="%s"%s>%s</%s>'
            % (tag, cls, attr, e(d["id"]),
               "" if d["id"] == start else " hidden", value_of(d), tag)
            for d in drugs)

    tabs = "".join(
        '<button type="button" class="ks3-route-tab" data-pick="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(d["id"]), "true" if d["id"] == start else "false", t(d["label"]))
        for d in drugs)

    def body_of(d, st):
        return st["body"] if st.get("body") else d[st["body_from"]]

    steplists = "".join(
        '<ol class="ks3-route-steps" data-for="%s"%s>%s</ol>'
        % (e(d["id"]), "" if d["id"] == start else " hidden",
           "".join(
               '<li class="ks3-route-step" data-step="%d">'
               '<span class="ks3-route-num" aria-hidden="true">%d</span>'
               '<span class="ks3-route-stepmain">'
               '<span class="ks3-route-steptitle">%s</span>'
               '<span class="ks3-route-stepbody" hidden>%s</span>'
               '</span></li>'
               % (i + 1, i + 1, t(st["title"]), rich(body_of(d, st)))
               for i, st in enumerate(stages)))
        for d in drugs)

    elses = "".join(
        '<div class="ks3-route-else" data-else="%s" hidden>'
        '<p class="ks3-route-elselabel">%s</p>'
        '<ul class="ks3-route-organs" role="list">%s</ul>'
        '<p class="ks3-route-verdict">%s</p></div>'
        % (e(d["id"]), t(a["elsewhere_label"]),
           "".join(
               '<li class="ks3-route-organrow">'
               '<p class="ks3-route-organ">%s</p>'
               '<p class="ks3-route-effect">%s</p></li>'
               % (t(row["organ"]), rich(row["effect"]))
               for row in d["elsewhere"]),
           rich(d["verdict"]))
        for d in drugs)

    return ('<div class="ks3-route" data-route data-drug="%s" data-step="0" '
            'data-total="%d">'
            '<div class="ks3-route-dose">'
            '<p class="ks3-route-doselabel">%s</p>'
            '<div class="ks3-route-tabs">%s</div></div>'
            '<div class="ks3-route-panel">'
            '<div class="ks3-route-head">%s%s</div>%s%s'
            '<div class="ks3-route-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-route-next" '
            'data-route-next data-label-start="%s" data-label-more="%s" '
            'data-label-done="%s">%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-route-reset" '
            'data-route-reset>%s</button></div></div>%s</div>'
            % (e(start), len(stages), t(a["dose_label"]), tabs,
               switched("p", "ks3-route-name", lambda d: t(d["name"])),
               switched("p", "ks3-route-class", lambda d: t(d["klass"])),
               switched("p", "ks3-route-where", lambda d: rich(d["where"])),
               steplists,
               e(nxt["start"]), e(nxt["more"]), e(nxt["done"]),
               t(nxt["start"]), t(a["reset_label"]), elses))
# ── the B6 plural rule, shared by `clearance-clock`'s eight templates ─────
#
# ⚖️ `{s}` IS THE PLURAL SUFFIX OF THE NUMBER PLACEHOLDER IMMEDIATELY BEFORE
# IT, and that rule is Design's sentences read back rather than an invention.
# Two of the eight templates carry two numbers and two `{s}`, and the pairing
# is crossed between them:
#
#     "{h} hour{s} elapsed · {r} unit{s} left"      → h, then r
#     "{r} unit{s} still in the blood after {h} hour{s}."  → r, then h
#
# A single global plural would print "1 units left" on one of them whichever
# number it chose, and named suffixes (`{hs}`, `{rs}`) would make the author
# write the pairing twice and keep the two in step by hand. Left-to-right, the
# suffix belongs to the number it just followed — which is exactly how the
# sentence is read, and it cannot fall out of step with the words around it.
#
# ⚠️ A `{s}` WITH NO NUMBER BEFORE IT IS A BUILD ERROR, not a silent "s". It
# means the author moved a number and left its suffix behind, which is a
# sentence that will read wrong for one value in every ten.
_B6_TOKEN = re.compile(r"\{(n|r|h|s)\}")
def _plural_fill(tpl, vals, where):
    """Fill `{n}` / `{r}` / `{h}`, with `{s}` pluralising the last of them."""
    state = {"last": None}

    def sub(m):
        key = m.group(1)
        if key == "s":
            if state["last"] is None:
                raise ValueError(
                    "%s: template %r has a `{s}` with no number before it. "
                    "The plural suffix belongs to the number it follows, so "
                    "one with nothing to agree with is a suffix left behind "
                    "when its number moved." % (where, tpl))
            return "" if state["last"] == 1 else "s"
        if key not in vals:
            raise ValueError(
                "%s: template %r uses `{%s}`, which this readout does not "
                "carry. It has %s." % (where, tpl, key, sorted(vals)))
        state["last"] = vals[key]
        return str(vals[key])

    out = _B6_TOKEN.sub(sub, tpl)
    # ⚠️ AND NOTHING IN BRACES SURVIVES. `_B6_TOKEN` only matches the four
    # names it knows, so a typo — `{q}`, `{units}`, `{hours}` — passed straight
    # through and shipped the braces to a student, silently, with every other
    # gate green. An unknown placeholder is an author asking for a number the
    # readout does not carry, and it has to be a build error rather than a
    # curly brace in a sentence about how drunk somebody is.
    left = re.search(r"\{[^}]*\}", out)
    if left:
        raise ValueError(
            "%s: template %r still contains %s after filling. The placeholders "
            "this readout carries are %s, plus `{s}` for the plural of "
            "whichever of them came last."
            % (where, tpl, left.group(0), sorted(vals)))
    return out
def r_clearance_clock(a, act_id):
    """⊕ b6-02 `#s-clock` — six ways to sober up, and none of them is one.

    ⚖️ THE INSTRUMENT IS THAT NO INTERVENTION CHANGES THE NUMBER OF HOURS.
    Not "the interventions are mostly ineffective" — none of them moves the
    clock, and the block exists so that a student discovers that by trying to
    beat it. NOTES-B6 §2.2 states it as a design note; here it is a property of
    the code, and it is enforced by ARCHITECTURE rather than by care: the
    chosen fix reaches exactly one thing in this renderer and in
    `wireClearanceClock` — the note that is showing — and reaches no arithmetic
    anywhere. There is no rate key on the payload for a future pass to make
    conditional, and `fixes[]` carries no numeric field at all, so there is
    nothing to multiply the clock by even if someone tried.

    ⚖️ THE ONE HONEST EXCEPTION IS A SENTENCE, NOT A BRANCH. *A big meal first*
    genuinely changes something — it lowers the PEAK and not the clock — and
    Design handles that entirely in that fix's own `note`: "The total amount to
    break down has not changed, so the hours have not changed." Implementing it
    as a special case would put a second behaviour into the instrument and
    would teach that one trick does work, which is the belief the block is
    built to remove.

    ⚖️ HOURS = UNITS, AND THE RATE IS NOT A PAYLOAD KEY. One unit an hour is
    the lesson's own figure, stated in six places on b6-02 including the key
    fact and the legal line, and NOTES-B6 flag 5 has it as a science-review
    item. It is deliberately NOT a dial here: a `hours_per_unit` key is a
    number a later pass can make depend on the fix, and this arithmetic is the
    single claim the whole block rests on. If the science gate moves the rate,
    it moves here, in one place, in a reviewed commit.

    ⚠️ THE BAR IS A FRACTION OF WHAT WAS DRUNK, NOT OF THE MAXIMUM. Design's
    `bloodBarStyle` is `remaining / units`, so two units and twelve units both
    open full and both empty at the same visual rate — the bar reads *how far
    through this evening's clearance you are*, and the hours readout beside it
    is the only thing that says how long that evening is. Scaling it against
    `max_units` instead would make a small evening look nearly clear from the
    first hour.

    ⚠️ A DRINK RESETS THE ELAPSED CLOCK, and that is Design's own
    (`{ units: …, hour: 0 }`). Pouring another drink at 2am does not un-drink
    the first, but it does mean the clock is now measuring a different
    evening — and leaving `hour` where it was would credit the new units with
    hours that passed before they existed.
    """
    drinks = a.get("drinks") or []
    if not drinks:
        raise ValueError(
            "clearance-clock %r declares no drinks. The units are what the "
            "hours are, so a bench with nothing to pour has no clock."
            % act_id)
    drink_ids = []
    for d in drinks:
        if not (d.get("id") and d.get("label")):
            raise ValueError(
                "clearance-clock %r drink %r needs `id` and `label`."
                % (act_id, d.get("id")))
        if d["id"] in drink_ids:
            raise ValueError(
                "clearance-clock %r declares drink id %r twice."
                % (act_id, d["id"]))
        drink_ids.append(d["id"])
        u = d.get("units")
        if not isinstance(u, int) or isinstance(u, bool) or u < 1:
            raise ValueError(
                "clearance-clock %r drink %r has units=%r. A drink adds a "
                "whole number of units and at least one — the unit values are "
                "science (NOTES-B6 flag 6) and a drink worth nothing is a "
                "control that does nothing when pressed."
                % (act_id, d["id"], u))

    fixes = a.get("fixes") or []
    if len(fixes) < 2:
        raise ValueError(
            "clearance-clock %r declares %d fix(es). The block's whole "
            "argument is that SEVERAL different things people believe in all "
            "give the same number of hours, and one of them cannot make that "
            "argument — with a single fix there is nothing to compare it "
            "against and the clock looks like it was never going to move."
            % (act_id, len(fixes)))
    fix_ids = []
    for f in fixes:
        for key in ("id", "label", "note"):
            if not f.get(key):
                raise ValueError(
                    "clearance-clock %r fix %r is missing %r. The note is the "
                    "whole of what a fix does: it is where the student is told "
                    "why the number did not move, and *a big meal first* is "
                    "where the one honest exception is drawn."
                    % (act_id, f.get("id"), key))
        if f["id"] in fix_ids:
            raise ValueError(
                "clearance-clock %r declares fix id %r twice."
                % (act_id, f["id"]))
        fix_ids.append(f["id"])
        # ⚠️ THE GATE THAT KEEPS THE INSTRUMENT AN INSTRUMENT. A fix carrying a
        # number is a fix that is about to be multiplied into the clock.
        for key, v in sorted(f.items()):
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                raise ValueError(
                    "clearance-clock %r fix %r carries a numeric key %r=%r. "
                    "No intervention on this bench changes the number of "
                    "hours — that IS the instrument (NOTES-B6 §2.2) — so a "
                    "fix has nothing to contribute a number to, and one that "
                    "carries one is a rate waiting to be applied."
                    % (act_id, f["id"], key, v))

    max_units = a.get("max_units")
    if not isinstance(max_units, int) or isinstance(max_units, bool) or max_units < 1:
        raise ValueError(
            "clearance-clock %r max_units is %r; it is the cap on the glass "
            "and must be a positive whole number." % (act_id, max_units))
    biggest = max(d["units"] for d in drinks)
    if max_units < biggest:
        raise ValueError(
            "clearance-clock %r caps the glass at %d units and offers a drink "
            "worth %d. Pressing it on an empty glass would add less than the "
            "drink says it is, which is a readout that disagrees with the "
            "button that produced it." % (act_id, max_units, biggest))

    start_units = a.get("start_units", 0)
    if (not isinstance(start_units, int) or isinstance(start_units, bool)
            or not 0 <= start_units <= max_units):
        raise ValueError(
            "clearance-clock %r start_units is %r; it is a whole number of "
            "units between 0 and max_units (%d)."
            % (act_id, start_units, max_units))

    start_fix = a.get("start_fix") or fixes[0]["id"]
    if start_fix not in fix_ids:
        raise ValueError(
            "clearance-clock %r opens on start_fix %r, which is not one of %s."
            % (act_id, start_fix, fix_ids))

    for key in ("add_label", "fix_label", "units_label", "hours_label",
                "hours_none", "blood_label", "remaining_label", "wait_label",
                "clear_label", "reset_label"):
        if not a.get(key):
            raise ValueError(
                "clearance-clock %r declares no %r." % (act_id, key))

    verdicts = a.get("verdicts") or {}
    missing = sorted({"empty", "clear", "running"} - set(verdicts))
    if missing:
        raise ValueError(
            "clearance-clock %r verdicts is missing %s. All three are "
            "reachable from the controls — an empty glass, a glass still "
            "clearing, and a glass that has cleared — and the third of them is "
            "the one that says the hours matched the units whatever route was "
            "tried." % (act_id, ", ".join(missing)))

    # Every template is filled once here, at build time, which validates its
    # placeholders before a browser ever sees it.
    where = "clearance-clock %r" % act_id
    remaining0 = start_units
    fmt = {
        "units": _plural_fill(a["units_label"], {"n": start_units}, where),
        "hours": (a["hours_none"] if start_units == 0
                  else _plural_fill(a["hours_label"], {"n": start_units}, where)),
        "remaining": _plural_fill(a["remaining_label"],
                                  {"h": 0, "r": remaining0}, where),
    }
    for branch in ("empty", "clear", "running"):
        _plural_fill(verdicts[branch],
                     {"n": start_units, "h": 0, "r": remaining0}, where)

    drink_html = "".join(
        '<button type="button" class="ks3-clock-drink" data-add="%d">%s</button>'
        % (d["units"], t("%s · %d" % (d["label"], d["units"])))
        for d in drinks)

    fix_html = "".join(
        '<button type="button" class="ks3-clock-fix" data-fix="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(f["id"]), "true" if f["id"] == start_fix else "false",
           t(f["label"]))
        for f in fixes)

    notes = "".join(
        '<p class="ks3-clock-note" data-fixnote="%s"%s>%s</p>'
        % (e(f["id"]), "" if f["id"] == start_fix else " hidden",
           rich(f["note"]))
        for f in fixes)

    width = 0.0 if start_units == 0 else remaining0 / float(start_units) * 100

    return ('<div class="ks3-clock" data-clearance data-units="%d" '
            'data-hour="0" data-max="%d" data-fix="%s" '
            'data-units-label="%s" data-hours-label="%s" data-hours-none="%s" '
            'data-remaining-label="%s" data-wait-label="%s" '
            'data-clear-label="%s" data-verdict-empty="%s" '
            'data-verdict-clear="%s" data-verdict-running="%s">'
            '<div class="ks3-clock-group">'
            '<p class="ks3-clock-grouplabel">%s</p>'
            '<div class="ks3-clock-btns">%s</div></div>'
            '<div class="ks3-clock-group">'
            '<p class="ks3-clock-grouplabel">%s</p>'
            '<div class="ks3-clock-btns">%s</div></div>'
            '<div class="ks3-clock-panel">'
            '<div class="ks3-clock-head">'
            '<p class="ks3-clock-units" data-clock-units>%s</p>'
            '<p class="ks3-clock-hours" data-clock-hours>%s</p></div>'
            '<p class="ks3-clock-bloodlabel">%s</p>'
            '<span class="ks3-clock-track">'
            '<span class="ks3-clock-fill" data-clock-fill style="width:%.1f%%">'
            '</span></span>'
            '<p class="ks3-clock-remaining" data-clock-remaining>%s</p>%s'
            '<div class="ks3-clock-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-clock-wait" '
            'data-clock-wait%s>%s</button>'
            '<button type="button" class="ks3-reveal-btn ks3-clock-reset" '
            'data-clock-reset>%s</button></div>'
            '<p class="ks3-clock-verdict" data-clock-verdict hidden></p>'
            '</div></div>'
            % (start_units, max_units, e(start_fix),
               e(a["units_label"]), e(a["hours_label"]), e(a["hours_none"]),
               e(a["remaining_label"]), e(a["wait_label"]), e(a["clear_label"]),
               e(verdicts["empty"]), e(verdicts["clear"]),
               e(verdicts["running"]),
               t(a["add_label"]), drink_html,
               t(a["fix_label"]), fix_html,
               fmt["units"], fmt["hours"], t(a["blood_label"]), width,
               fmt["remaining"], notes,
               " disabled" if start_units == 0 else "",
               t(a["clear_label"] if start_units == 0 else a["wait_label"]),
               t(a["reset_label"])))
def r_claim_check(a, act_id):
    """⊕ b6-03 `#s-claims` — five claims, five faults, and no invented wrong ones.

    ⚖️ THE POOL IS A BIJECTION AND THE RENDERER PROVES IT. Five faults, five
    claims, and each fault is the right answer for exactly one of them — which
    is what makes every wrong pick still a TRUE statement about evidence, and
    what the prompt promises the student in as many words: "a wrong answer
    still teaches you something about the claim you picked it for." Add one
    invented distractor and that promise becomes false; drop one and a claim
    becomes unanswerable. NOTES-B6 §2.3 makes it the rule, and this raises
    unless the mapping is one-to-one and onto.

    ⚖️ THE BENCH DOES NOT MARK RIGHT AND WRONG (MRB-208 R10, and Design's own
    comment on the page). A fault button shows that it was CHOSEN — alert
    border, alert letter — and takes no verdict class, no green, no red, ever,
    open or not. What happens at the check is not marking either: the
    unchosen buttons dim, and a separate cream panel NAMES the fault in a
    sentence. Only the mastery ladder marks correctness.

    ⚠️ THE ANSWER LINE IS THE CORRECT FAULT'S TEXT, NOT THE CHOSEN ONE. Design
    reads `FAULTS.find(f => f.id === claim.answer).text`, so a student who
    picked wrongly is shown the right fault named in full rather than being
    told only that they were wrong. That is the entire reason the reveal is not
    withheld for a wrong answer.

    ⚠️ EVERY CLAIM KEEPS ITS OWN PICK AND ITS OWN CHECKED FLAG. Five tabs over
    ONE shared fault list, so the picks live in the wiring and are re-applied
    on every tab change — `fault-bench`'s arrangement, for `fault-bench`'s
    reason: a student who checks claim 1 and moves to claim 2 must find claim 2
    uncommitted and claim 1 exactly as they left it.
    """
    claims = a.get("claims") or []
    if len(claims) < 2:
        raise ValueError(
            "claim-check %r declares %d claim(s). The fault pool is shared "
            "across the claims and each fault answers exactly one of them, so "
            "a single claim has no pool — only one option that is true and "
            "four that are about nothing." % (act_id, len(claims)))

    faults = a.get("faults") or []
    if len(faults) < 2:
        raise ValueError(
            "claim-check %r declares %d fault(s). Locating a fault needs "
            "somewhere else it could have been." % (act_id, len(faults)))
    fault_ids = []
    for f in faults:
        if not (f.get("id") and f.get("text")):
            raise ValueError(
                "claim-check %r fault %r needs `id` and `text`. The text is "
                "read twice — once as the option a student picks and again as "
                "the answer line naming the fault — so it has to be a "
                "sentence that stands on its own."
                % (act_id, f.get("id")))
        if f["id"] in fault_ids:
            raise ValueError(
                "claim-check %r declares fault id %r twice." % (act_id, f["id"]))
        fault_ids.append(f["id"])

    claim_ids = []
    answers = []
    for c in claims:
        for key in ("id", "label", "text", "evidence", "answer", "why",
                    "settle"):
            if not c.get(key):
                raise ValueError(
                    "claim-check %r claim %r is missing %r. `why` is the "
                    "reasoning and `settle` is what would actually decide it; "
                    "a claim with a verdict and no `settle` teaches that bad "
                    "evidence is a thing to spot rather than a thing to "
                    "replace." % (act_id, c.get("id"), key))
        if c["id"] in claim_ids:
            raise ValueError(
                "claim-check %r declares claim id %r twice." % (act_id, c["id"]))
        claim_ids.append(c["id"])
        if c["answer"] not in fault_ids:
            raise ValueError(
                "claim-check %r claim %r answers %r, which is not one of the "
                "offered faults %s. Every option would read as the wrong one "
                "and the claim would be unanswerable."
                % (act_id, c["id"], c["answer"], fault_ids))
        answers.append(c["answer"])

    # ⚖️ ONE-TO-ONE AND ONTO. Both halves are load-bearing and they fail
    # differently, so they are reported differently.
    if len(faults) != len(claims):
        raise ValueError(
            "claim-check %r offers %d faults for %d claims. The pool is "
            "one-to-one (NOTES-B6 §2.3): each fault is the right answer for "
            "exactly one claim, which is what makes every WRONG pick still a "
            "true statement about evidence — and it is what the block's own "
            "prompt promises the student. A spare fault is an invented "
            "distractor; a missing one leaves a claim with no answer."
            % (act_id, len(faults), len(claims)))
    duplicated = sorted({x for x in answers if answers.count(x) > 1})
    if duplicated:
        raise ValueError(
            "claim-check %r has fault(s) %s answering more than one claim. "
            "With five faults and five claims that also means at least one "
            "fault answers none of them — a option that is true of nothing on "
            "the bench, which is exactly the invented distractor the pool "
            "exists to avoid." % (act_id, ", ".join(map(repr, duplicated))))

    labels = a.get("labels") or {}
    missing = sorted({"claims", "evidence", "faults", "settle"} - set(labels))
    if missing:
        raise ValueError(
            "claim-check %r labels is missing %s. `evidence` captions the "
            "quoted evidence and `settle` introduces the last line of the "
            "reveal; an uncaptioned evidence panel reads as part of the claim "
            "rather than as the case made for it."
            % (act_id, ", ".join(missing)))

    verdicts = a.get("verdicts") or {}
    vmissing = sorted({"right", "wrong"} - set(verdicts))
    if vmissing:
        raise ValueError(
            "claim-check %r verdicts is missing %s. Both are eyebrows on the "
            "cream panel and neither is a mark: the reveal opens either way."
            % (act_id, ", ".join(vmissing)))

    tally = a.get("tally") or {}
    if not (tally.get("format") and tally.get("done")):
        raise ValueError(
            "claim-check %r needs both `tally.format` and `tally.done`. The "
            "line beside the button counts DOWN — how many claims are still "
            "to check — and the last one is a sentence rather than “0 "
            "still to check”." % act_id)

    for key in ("check_label", "checked_label"):
        if not a.get(key):
            raise ValueError(
                "claim-check %r declares no %r." % (act_id, key))

    start = a.get("start_claim") or claims[0]["id"]
    if start not in claim_ids:
        raise ValueError(
            "claim-check %r opens on start_claim %r, which is not one of %s."
            % (act_id, start, claim_ids))

    fault_text = {f["id"]: f["text"] for f in faults}

    tabs = "".join(
        '<button type="button" class="ks3-ccheck-tab" data-pick="%s" '
        'aria-pressed="%s">%s</button>'
        % (e(c["id"]), "true" if c["id"] == start else "false", t(c["label"]))
        for c in claims)

    texts = "".join(
        '<p class="ks3-ccheck-claim" data-for="%s"%s>%s</p>'
        % (e(c["id"]), "" if c["id"] == start else " hidden", t(c["text"]))
        for c in claims)

    evidence = "".join(
        '<p class="ks3-ccheck-evidence" data-for="%s"%s>'
        '<span class="ks3-ccheck-evlabel">%s</span>%s</p>'
        % (e(c["id"]), "" if c["id"] == start else " hidden",
           t(labels["evidence"]), rich(c["evidence"]))
        for c in claims)

    options = "".join(
        '<li><button type="button" class="ks3-ccheck-fault" data-fault="%s" '
        'aria-pressed="false">'
        '<span class="ks3-ccheck-mark" aria-hidden="true">%s</span>'
        '<span class="ks3-ccheck-faulttext">%s</span></button></li>'
        % (e(f["id"]), t(option_letter(i)), t(f["text"]))
        for i, f in enumerate(faults))

    reveals = "".join(
        '<div class="ks3-ccheck-verdict" data-verdict="%s" data-answer="%s" '
        'hidden><p class="ks3-ccheck-word">'
        '<span data-word="right" hidden>%s</span>'
        '<span data-word="wrong" hidden>%s</span></p>'
        '<p class="ks3-ccheck-answer">%s</p>'
        '<p class="ks3-ccheck-why">%s</p>'
        '<p class="ks3-ccheck-settle"><strong>%s</strong> %s</p></div>'
        % (e(c["id"]), e(c["answer"]), t(verdicts["right"]),
           t(verdicts["wrong"]), t(fault_text[c["answer"]]), rich(c["why"]),
           t(labels["settle"]), rich(c["settle"]))
        for c in claims)

    return ('<div class="ks3-ccheck" data-ccheck data-total="%d" '
            'data-claim="%s" data-check-label="%s" data-checked-label="%s" '
            'data-tally="%s" data-tally-done="%s">'
            '<div class="ks3-ccheck-tabsgroup">'
            '<p class="ks3-ccheck-tabslabel">%s</p>'
            '<div class="ks3-ccheck-tabs">%s</div></div>'
            '<div class="ks3-ccheck-panel">%s%s'
            '<p class="ks3-ccheck-ask">%s</p>'
            '<ul class="ks3-ccheck-faults" role="list">%s</ul>'
            '<div class="ks3-ccheck-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-ccheck-check" '
            'data-ccheck-open disabled>%s</button>'
            '<span class="ks3-ccheck-tally" data-ccheck-tally role="status">%s'
            '</span></div>%s</div></div>'
            % (len(claims), e(start), e(a["check_label"]),
               e(a["checked_label"]), e(tally["format"]), e(tally["done"]),
               t(labels["claims"]), tabs, texts, evidence,
               t(labels["faults"]), options, t(a["check_label"]),
               t(tally["format"].replace("{n}", str(len(claims)))
                 .replace("{total}", str(len(claims)))),
               reveals))


# ── registrations ────────────────────────────────────────────────────────
KIND_SHELL = {
    'route-tracer': ("ks3-route-block", ' data-instrument data-routeblock data-stage-done="0"'),
    'clearance-clock': ("ks3-clock-block", ' data-instrument data-clearblock data-stage-done="0"'),
    'claim-check': ("ks3-ccheck-block", ' data-instrument data-ccheckblock data-stage-done="0"'),
}

KIND_FN = {
    'route-tracer': r_route_tracer,
    'clearance-clock': r_clearance_clock,
    'claim-check': r_claim_check,
}
