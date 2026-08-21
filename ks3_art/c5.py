"""ks3_art.c5 — C5's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C5 is *Types of reaction*: 5 lessons and
10 instrument families, all DOM, no canvas anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY. Everything an instrument has to COMPUTE at run time is the JS's
job; this file emits the data it needs (as ``data-`` attributes, or as one
compact JSON payload per instrument) and the RESTING DOM — the state the page
is in before a line of JavaScript has run, which is also the state a crawler
and a no-JS reader see. A resting render that disagrees with the payload is a
wrong number in the bytes, not a flicker.

Two conventions run through every renderer below and both are load-bearing:

  · EMIT-BOTH-SHOW-ONE, wherever a panel has a small closed set of states.
    Every state's text is in the document and one is shown. Nothing is ever
    assembled out of an attribute, so ``<em>``, ``<strong>`` and an ampersand
    survive exactly as the author wrote them, and no sentence is duplicated
    between Python and JS where the two could drift.
  · A JSON ``data-cfg`` ONLY for what genuinely has to be recomputed — a
    number, a colour, a geometry. Never for a sentence.

═══════════════════════════════════════════════════════════════════════════
THE HOOKS ARE AN INTERFACE
═══════════════════════════════════════════════════════════════════════════

Every ``data-`` attribute emitted below is named systematically off the
family's short name and is the contract ``shared/ks3.js`` binds against.
Renaming one here without renaming it there is a silent dead instrument, so
they are documented in each renderer's docstring as well as in the report.

═══════════════════════════════════════════════════════════════════════════
THE RULES THAT BIND THEM ALL
═══════════════════════════════════════════════════════════════════════════

  · Every C5 instrument sits in a LIGHT ``ks3-block``. There is no ink-dark
    practical block anywhere in the unit. The one section drawn on a different
    ground is drawn on AMBER, and amber is a confrontation, not a category.
  · ONLY THE LADDER MARKS. Nothing green and nothing red reaches any control
    in any of these families. A verdict panel says in words what happened; the
    chosen option keeps the ordinary chosen treatment and the unchosen ones
    dim. No ``data-correct`` on any activity option, ever.
  · Every family here ticks a rail stop, so every family carries
    ``data-stage-done="0"``. NOTHING IS TICKED ON LOAD.
  · Author text reaches the page through ``e()`` / ``t()`` / ``rich()``.
    ``e()`` for attribute values — it is the only one safe there, because
    ``t()`` can emit an SVG mark carrying double quotes — ``rich()`` for
    prose, ``t()`` for labels.
  · Arrows inside an equation are DRAWN AS SVG, never the character U+2192.
    The shipped font subsets do not contain it. Typed arrows are prose only.
"""

import json

from ks3_art.kit import (
    _SVG_ACCENT,
    _SVG_ACCENT_TEXT,
    _SVG_ACCENT_TINT,
    _SVG_BAND,
    _SVG_CARD,
    _SVG_DISPLAY,
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_MUTED,
    _SVG_INSET,
    _SVG_RULE,
    _SVG_RULE_STRONG,
    _circle,
    _label,
    _line,
    _mono,
    _path,
    _rect,
    _svg_open,
    _svg_text,
    e,
    option_letter,
    rich,
    t,
)

# ── from art_01.py ─────────────────────────────────────
# ═══ c5-01 · burner-bench + fuel-cards ═══════════════════════════════════
#
# Two families, both DOM, no canvas, no drawn figure. This lesson's picture is
# a readout that changes with two dials, which is what a PARAMETER BENCH draws
# instead of a diagram — and drawing one as well would be a second, frozen copy
# of something the instrument already shows and could disagree with.
#
# Both sit in a LIGHT `ks3-block` (measured off Design's own markup: `#s-burner`
# page line 106 and `#s-fuels` page line 178 both carry `class="ks3-block"` and
# nothing else), both tick a rail stop, so both ship `data-stage-done="0"` and
# NOTHING is ticked on load.
#
# ⚠️ ONLY THE LADDER MARKS. Neither family emits `data-correct`, and nothing
# green and nothing red reaches any control in either of them. A committed dial
# and a committed card option keep the platform's ordinary pressed treatment and
# their spent siblings dim; every verdict on this page is a PANEL OF WORDS, in
# the same voice whichever button was pressed.
#
# ⚑ AMBER, ON ONE CELL, AND IT IS NEITHER A MARK NOR A CATEGORY.
# `--ks3-alert-tint` grounds the bench's prediction gate — which is `REACT-11`'s
# elicitation, a paragraph before the readout confronts it, and is the ruled
# meaning C3's three gates and c4-04's established — and it grounds the "In the
# air around it" cell on exactly the runs where there is carbon monoxide in the
# room. That second one is a HAZARD READING and it is checked as one: the
# renderer raises unless every amber cell sits on a run whose products name
# carbon monoxide, and unless every run whose products name it has one. So the
# amber tracks the poison and not the dial — hydrogen with the hole shut is an
# incomplete run and stays plain, because there is nothing dangerous in its
# products. Amber saying "there is a poison in this air" is the same use as
# `.ks3-readout-where[data-where="absent"]` and `.ks3-fit-badge[data-state=
# "fails"]`, both live. It is never a selection, never a mark and never a
# category hue.
#
# HOOKS, both families:
#   burner-bench  `data-burner` (wrapper, `data-seen-total`) · `data-burner-for`
#                 + `data-burner-val` (a dial button) · `data-burner-track` (a
#                 button on the dial the rail stop watches) ·
#                 `data-burner-predict` (the lettered gate list) ·
#                 `data-burner-panel` (valued with the run key) ·
#                 `data-burner-close`
#   fuel-cards    `data-fcard` (wrapper, `data-total`) · `data-fcard-card`
#                 (valued with the card id, `data-open="0"`) · `data-fcard-opt`
#                 · `data-fcard-reveal`
#
# ⚠️ The prefixes are `burner` and `fcard` and both were grepped against
# `ks3_art/*.py`, `shared/ks3.js` and `shared/ks3.css` before a line was
# written. Neither the family names nor either prefix appears anywhere in the
# build — no `wireBurner…`, no `[data-burner…]`, no `.ks3-fcard…` — so the
# `data-critique` / `data-critiq` trap does not apply here and nothing was
# renamed.


def _burner_arrow():
    """Design's equation arrow, DRAWN, with its spoken word beside it.

    ⚠️ Never the character U+2192. The shipped font subsets do not contain it,
    so a typed arrow drops to a system font mid-line inside a 21px display row.
    Geometry measured off Design's own markup (page line 152): viewBox
    `0 0 44 24`, `M4 12h30M26 5l8 7-8 7`, 2.6px stroke, round caps and joins,
    on `currentColor` so it inherits the ink or the on-dark of whatever panel
    it lands in.
    """
    return ('<svg class="ks3-burner-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" '
            'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>'
            '<span class="ks3-visually-hidden">makes</span>')


def _burner_seg(cls, pressed, label, **attrs):
    """One segmented-control button.

    `.ks3-seg-btn` is the key stage's ONE segmented control (the Drift-4
    ruling), with a family class beside it for layout. R2: the pressed state
    carries `aria-pressed`, a WORD, not colour alone. There is no `correct`
    parameter here and there must never be one.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _burner_lettered(options, hook):
    """A lettered A/B/C commit list inside an instrument.

    The same markup `r_activity_options` emits, because Design draws the SAME
    control for a prediction whether it stands alone in a block or sits inside
    a bench. It gets a hook of its own because the shell's `wirePredictions`
    refuses to touch anything inside `[data-instrument]`: an instrument owns
    every option inside it, which means it also has to wire them.

    Nothing is pressed at rest. MRB-208.
    """
    return ('<ul class="ks3-options" role="list" %s>%s</ul>'
            % (hook,
               "".join(
                   '<li><button type="button" class="ks3-option" data-i="%d" '
                   'aria-pressed="false"><span class="ks3-opt-mark" '
                   'aria-hidden="true">%s</span>'
                   '<span class="ks3-opt-label">%s</span></button></li>'
                   % (i, option_letter(i), t(o))
                   for i, o in enumerate(options))))


# ═══ c5-01 · burner-bench ════════════════════════════════════════════════

def r_burner_bench(a, act_id):
    """⊕ c5-01 `#s-burner` — four fuels, two air settings, eight runs.

    ⚖️ **THE DIAL THAT MATTERS IS THE HOLE IN THE SIDE, AND THAT IS WHY THE
    STOP TICKS ON THE AIR DIAL.** Design's `DONE('s-burner')` is
    `Object.keys(s.seen).length >= 2`, and her `seen` records the AIR setting
    only. The lesson's claim is about the collar: a student who has run one
    fuel both ways has seen the whole argument, and a student who has spun
    through four fuels with the hole open has seen none of it. Which dial the
    stop watches is a property of the PAYLOAD (`tracks_done`) rather than a
    string in this file, so the renderer cannot disagree with the record.

    ⚖️ **THE WHOLE STATE SPACE IS ENUMERATED AND CHECKED (§5A).** Four fuels
    crossed with two air settings is eight runs and all eight are authored.
    Every reachable pair of dial values must have a run and no run may name a
    pair the dials cannot reach: a missing cell would show the previous run's
    readings under the new dial's label, and a surplus one is a run nobody can
    reach and nobody would ever notice was wrong.

    That check is not bookkeeping. Design's page computes five readouts from two
    booleans and three of the eight cells that produces are FALSE — the flame
    note and the verdict for hydrogen with the hole shut both name soot in a
    fuel with no carbon in it, and charcoal with the hole open is given a
    Bunsen's roaring blue flame. Enumerating is what made them visible. See the
    lesson record's `_RUNS` for what each was corrected to and why.

    ⚖️ **EVERY NOTE IS KEYED TO WHICH DIALS ARE SET, NEVER TO HOW MANY.** There
    is no "you have now tried two things" anywhere in this instrument: the flame
    is what it is because of the fuel and the hole, and the panel says so
    whichever route the student took to it. The one sentence that IS about
    having done both is the closing summary, and it says so out loud.

    ⚠️ EMIT-BOTH-SHOW-ONE, AND NOTHING IS COMPUTED. All eight runs' tiles, word
    equations and verdicts are in the document at rest and one is unhidden, so
    `<strong>`, an em dash and a degree sign survive exactly as the author wrote
    them, no sentence exists twice, and the resting render cannot disagree with
    the runtime one. There is no arithmetic here and none in `wireBurnerBench`.

    ⚠️ THE PREDICTION GATE HOLDS THE READOUT (Law 4) AND THEN STAYS ON SCREEN.
    Design's `benchOpen` is `s.predict !== null`, so nothing is readable until
    the student has said what they expect — that part is hers and is reproduced
    exactly. What is NOT reproduced is her `sc-if needPredict`, which removes
    the gate the moment it is answered: that takes the student's own commitment
    off the page at the exact moment the readout arrives to be compared against
    it, which is the comparison Law 4 exists to create. Every gate in C3 and C4
    stays put. This one stays put.

    ⚠️ THE GATE CARRIES A REAL `id`, FROM THE PAYLOAD. `REACT-11`'s `elicited_by`
    is `gate-air-shut` and MRB-244/248 resolve a join against `id="…"` on the
    built page, so the gate has to have one. It comes from `predict.gate_id`
    rather than from a literal here, so a second lesson placing this family
    cannot emit a duplicate id.

    HOOKS: see the module header.
    """
    dials = a.get("dials") or []
    tiles = a.get("tiles") or []
    runs = a.get("runs") or []
    predict = a.get("predict") or {}

    if len(dials) != 2:
        raise ValueError(
            "burner-bench %r declares %d dial(s). The bench is a FUEL crossed "
            "with an AIR SUPPLY and the whole argument is the grid that makes; "
            "with one dial there is nothing to cross." % (act_id, len(dials)))
    if not tiles:
        raise ValueError(
            "burner-bench %r declares no readout tiles. A bench with dials and "
            "nothing to read is a control that does nothing." % act_id)
    if not predict.get("options"):
        raise ValueError(
            "burner-bench %r has no prediction options. Law 4: the readout is "
            "not shown until the student has said what they expect." % act_id)
    if not predict.get("gate_id"):
        raise ValueError(
            "burner-bench %r has no `gate_id` on its prediction. The gate is a "
            "misconception's `elicited_by`, and MRB-244/248 resolve that "
            "against an id on the BUILT PAGE — an unnamed gate cannot be "
            "pointed at." % act_id)

    # ⚠️ EXACTLY ONE DIAL MAY OWN THE RAIL STOP. Two would make the tick depend
    # on which one the JS happened to find first, and none would leave a stop
    # that could never tick — which is the failure MRB-249 forbids and the one
    # that looks fine, because the rail renders either way.
    tracked = [d for d in dials if d.get("tracks_done")]
    if len(tracked) != 1:
        raise ValueError(
            "burner-bench %r has %d dial(s) marked `tracks_done` and needs "
            "exactly one. The rail stop ticks when every option of ONE dial "
            "has been used, and which dial that is is the lesson's claim."
            % (act_id, len(tracked)))
    tracked_id = tracked[0]["id"]
    seen_total = len(tracked[0].get("options") or [])
    if seen_total < 2:
        raise ValueError(
            "burner-bench %r tracks dial %r, which has %d option(s). A stop "
            "that ticks on having used the only setting there is ticks on "
            "load, and MRB-208 rules that nothing does."
            % (act_id, tracked_id, seen_total))

    # ── §5A · the whole state space, enumerated and checked ──────────────
    reachable = []
    for first in dials[0].get("options") or []:
        for second in dials[1].get("options") or []:
            reachable.append("%s:%s" % (first["id"], second["id"]))
    authored = [r["id"] for r in runs]
    missing = [k for k in reachable if k not in authored]
    surplus = [k for k in authored if k not in reachable]
    if missing or surplus:
        raise ValueError(
            "burner-bench %r does not model what it draws. Unreachable run(s): "
            "%s. Dial combination(s) with no run: %s. A dial that is drawn must "
            "be modelled, and a bench with a hole in it shows the last run's "
            "readings under the new run's label."
            % (act_id, surplus or "none", missing or "none"))
    if len(set(authored)) != len(authored):
        raise ValueError(
            "burner-bench %r authors the same run twice. One panel would be "
            "unreachable and no gate would see it." % act_id)

    for r in runs:
        for key in ("eq_left", "eq_right", "verdict"):
            if not r.get(key):
                raise ValueError(
                    "burner-bench %r run %r has no %r. Every run opens a "
                    "readout, an equation and a verdict; a run with nothing to "
                    "report is a control that does nothing."
                    % (act_id, r.get("id"), key))
        cells = r.get("cells") or []
        if len(cells) != len(tiles):
            raise ValueError(
                "burner-bench %r run %r has %d cell(s) for %d tile(s). The "
                "cells are zipped with the tiles in order, so a short run "
                "would silently leave the last tile carrying the label of one "
                "reading and the value of another."
                % (act_id, r.get("id"), len(cells), len(tiles)))
        for i, cell in enumerate(cells):
            for key in ("value", "note"):
                if not cell.get(key):
                    raise ValueError(
                        "burner-bench %r run %r tile %r has no %r. A reading "
                        "with no note is a number nobody said anything about, "
                        "and a note with no reading is a sentence about "
                        "nothing." % (act_id, r.get("id"),
                                      tiles[i].get("id"), key))

        # ⚑ THE CONTENT-TRUTH ASSERTION, AND IT IS ABOUT THE AMBER.
        # Amber on this bench means one thing: there is carbon monoxide in the
        # room. So it must appear on exactly the runs whose products name it,
        # and on no others. That is what stops the tint drifting into "this is
        # the bad setting" — hydrogen with the hole shut is an incomplete run
        # and has no amber, because nothing in its products can hurt anyone.
        alerts = [i for i, c in enumerate(cells) if c.get("alert")]
        makes_co = "carbon monoxide" in r["eq_right"]
        if bool(alerts) != makes_co:
            raise ValueError(
                "burner-bench %r run %r: products %r and %d amber cell(s). "
                "Amber on this bench is a HAZARD reading and means carbon "
                "monoxide is in the air; it is not a mark on the setting. A "
                "run that makes it must carry it and a run that does not must "
                "not."
                % (act_id, r.get("id"), r["eq_right"], len(alerts)))
        if len(alerts) > 1:
            raise ValueError(
                "burner-bench %r run %r paints %d cells amber. One reading is "
                "the hazard; painting the row would make it a verdict on the "
                "run." % (act_id, r.get("id"), len(alerts)))

    # ── the dials ────────────────────────────────────────────────────────
    # The FIRST option of each dial is the resting state — Design's own opening
    # state (`fuel: 'methane', air: 'open'`) expressed as a property of the
    # payload rather than as two strings repeated here and again in the JS.
    dial_html = []
    for d in dials:
        opts = d.get("options") or []
        dial_html.append(
            '<div class="ks3-burner-dial">'
            '<p class="ks3-burner-diallabel">%s</p>'
            '<div class="ks3-burner-dialrow">%s</div></div>'
            % (t(d.get("label", "")),
               "".join(_burner_seg(
                   "ks3-burner-opt", i == 0, o.get("label", ""),
                   data_burner_for=d["id"], data_burner_val=o["id"],
                   data_burner_track="1" if d["id"] == tracked_id else None)
                   for i, o in enumerate(opts))))

    # ── the gate ─────────────────────────────────────────────────────────
    # Visible at rest with nothing pressed, and it stays visible afterwards —
    # see the docstring. `id` is the misconception join's target.
    gate = ('<div class="ks3-burner-gate" id="%s">'
            '<p class="ks3-commit">%s</p>%s</div>'
            % (e(predict["gate_id"]), rich(predict.get("prompt", "")),
               _burner_lettered(predict["options"], "data-burner-predict")))

    # ── the eight run panels, all present, all hidden ────────────────────
    panels = []
    for r in runs:
        cells = []
        for tile, cell in zip(tiles, r["cells"]):
            cells.append(
                '<div class="ks3-burner-tile%s">'
                '<p class="ks3-burner-tilelabel">%s</p>'
                '<p class="ks3-burner-value">%s</p>'
                '<p class="ks3-burner-tilenote">%s</p></div>'
                % (" is-alert" if cell.get("alert") else "",
                   t(tile.get("label", "")), t(cell["value"]),
                   rich(cell["note"])))
        # The word equation for this run. The arrow is drawn; the two halves
        # are authored strings and nothing between them is assembled.
        eq_note = ('<p class="ks3-burner-eqnote">%s</p>' % rich(r["eq_note"])
                   if r.get("eq_note") else "")
        panels.append(
            '<div class="ks3-burner-panel" hidden data-burner-panel="%s">'
            '<div class="ks3-burner-tiles">%s</div>'
            '<div class="ks3-burner-eq">'
            '<p class="ks3-burner-eqlabel">%s</p>'
            '<p class="ks3-burner-eqline"><span>%s</span>%s<span>%s</span></p>'
            '%s</div>'
            '<div class="ks3-burner-note"><p>%s</p></div></div>'
            % (e(r["id"]), "".join(cells),
               t(a.get("eq_label") or "The word equation for this run"),
               t(r["eq_left"]), _burner_arrow(), t(r["eq_right"]),
               eq_note, rich(r["verdict"])))

    close = ('<div class="ks3-burner-close" hidden data-burner-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""

    return ('<div class="ks3-burner" data-burner data-seen-total="%d">'
            '<div class="ks3-burner-dials">%s</div>%s%s%s</div>'
            % (seen_total, "".join(dial_html), gate, "".join(panels), close))


# ═══ c5-01 · fuel-cards ══════════════════════════════════════════════════

def r_fuel_cards(a, act_id):
    """⊕ c5-01 `#s-fuels` — one rule, three fuels, three commitments.

    ⚖️ **THE SAME THREE OPTIONS ON EVERY CARD, AND THE ANSWER MOVES.** That is
    the exercise and it is why the options are authored once on the activity
    rather than three times on the cards: a student who has the rule — carbon
    goes to carbon dioxide, hydrogen goes to water — gets all three, and a
    student pattern-matching the buttons gets one. Three different option sets
    would be three different questions and the rule would never be tested.

    Each commitment is FINAL, which is `c3CommitCards`' contract — the same one
    the purity sorter, the jobs list and c4-03's equation cards take. The reply
    is on screen the instant the card is decided, so a second press would be a
    student choosing an answer they can already read; both siblings disable and
    the ones that were not pressed dim.

    ⚠️ NOTHING HERE MARKS. `answer` reaches no markup at all — the reply names
    the products and says why, in the same voice whichever button was pressed,
    and only the mastery ladder marks. It is read HERE, and only here, so that
    keeping it on the record cannot quietly mean keeping it wrong: an answer
    that is not one of the options offered would be a record that has stopped
    describing its own page.

    HOOKS: see the module header.
    """
    options = a.get("options") or []
    cards = a.get("cards") or []
    if len(options) < 2:
        raise ValueError(
            "fuel-cards %r offers %d option(s). The section asks the same "
            "question of three fuels and one answer is not a question."
            % (act_id, len(options)))
    if len(cards) < 2:
        raise ValueError(
            "fuel-cards %r declares %d card(s). One rule read against one fuel "
            "is an example, not a test of the rule." % (act_id, len(cards)))

    option_ids = [o["id"] for o in options]
    seen = set()
    for c in cards:
        for key in ("id", "name", "made", "eq_left", "eq_right", "why"):
            if not c.get(key):
                raise ValueError(
                    "fuel-cards %r card %r has no %r. The card is a fuel, a "
                    "commitment and a reply; a card missing any of the three "
                    "opens on nothing." % (act_id, c.get("id"), key))
        if c["id"] in seen:
            raise ValueError(
                "fuel-cards %r authors card id %r twice. Two cards with one "
                "name is one unreachable card." % (act_id, c["id"]))
        seen.add(c["id"])
        # See the docstring: `answer` never reaches the page, so this is the
        # only place it can be wrong in a way anything notices.
        if c.get("answer") not in option_ids:
            raise ValueError(
                "fuel-cards %r card %r answers %r, which is not one of the "
                "options %r. The record has to know which products are right "
                "even though the markup never says."
                % (act_id, c["id"], c.get("answer"), option_ids))

    body = []
    for c in cards:
        buttons = "".join(
            _burner_seg("ks3-fcard-opt", False, o.get("label", ""),
                        data_fcard_opt=o["id"])
            for o in options)
        body.append(
            '<div class="ks3-fcard-card" data-fcard-card="%s" data-open="0">'
            '<p class="ks3-fcard-name">%s</p>'
            '<p class="ks3-fcard-made">%s</p>'
            '<div class="ks3-fcard-opts">%s</div>'
            '<div class="ks3-fcard-reveal" hidden data-fcard-reveal>'
            '<p class="ks3-fcard-eq"><span>%s</span>%s<span>%s</span></p>'
            '<p class="ks3-fcard-why">%s</p></div></div>'
            % (e(c["id"]), t(c["name"]), rich(c["made"]), buttons,
               t(c["eq_left"]), _burner_arrow(), t(c["eq_right"]),
               rich(c["why"])))

    return ('<div class="ks3-fcard" data-fcard data-total="%d">%s</div>'
            % (len(cards), "".join(body)))


# ── registrations ────────────────────────────────────────────────────────
#
# Two families, no drawer — c5-01 declares no figure, and the "no row" marker
# is deliberately not written as the word "none" after a REGISTER ART comment:
# a splice once took exactly that as a table row and emitted it into the
# registry, which is a SyntaxError in the generator. A marker that means "no
# row" has to not be the marker.
#
# Both families tick a rail stop, so both carry `data-stage-done="0"` —
# NOTHING IS TICKED ON LOAD (MRB-208). `data-instrument` keeps `wirePredictions`
# out of the bench's own prediction options.
#
# SEGMENTS, measured off Design's own markup and for the commander's
# `_INSTRUMENT_SEGMENTS` map: both sections are a light `ks3-block` with no
# second class, so both are `check`. There is no ink-dark practical block
# anywhere in C5, exactly as there is none in C3 or C4.





# REGISTER SEGMENT: 'burner-bench': "check",
# REGISTER SEGMENT: 'fuel-cards': "check",


# ── from art_02.py ─────────────────────────────────────
# ═══ c5-02 · tube-run, decomp-sort ═══════════════════════════════════════
#
# Two families, both DOM, no canvas, no drawn figure — this lesson's picture
# is a test tube drawn as four stages with three readouts beside it, which is
# what a PROCESS page draws instead of a diagram.
#
# Both sit in a LIGHT `ks3-block` (measured off Design's own markup: `#s-tube`
# and `#s-sort` carry `class="ks3-block"` and nothing else), both tick a rail
# stop, so both ship `data-stage-done="0"` and NOTHING is ticked on load.
#
# ⚠️ ONLY THE LADDER MARKS. Neither family emits `data-correct`, and nothing
# green or red reaches any control in either of them. The cooling gate's three
# options are COMMITMENTS: they take the ordinary pressed treatment, they carry
# no correctness flag, and the answer arrives as the next STAGE OF THE RUN. A
# decided sort card keeps the ordinary pressed treatment, its sibling dims, and
# the verdict is a PANEL OF WORDS in the same voice whichever button was
# pressed.
#
# ⭐ AND THE COOLING GATE IS THE LESSON. NOTES-C5 §2: "a staged run with a
# cooling gate at the end. The gate is the lesson: it does not go back when it
# cools, which is what separates it from a physical change." So it is drawn as
# a BLOCKING panel inside stage 4 — `r_tube_run` hides the advance button while
# the gate is open, and the wiring reproduces Design's `gateNeeded` exactly. A
# student cannot watch the tube cool before saying what they think will happen.
#
# ⚠️ EVERY ARROW INSIDE AN EQUATION IS DRAWN. Design's C4 convention, inherited
# by C5, and a hard one: the shipped font subsets contain no U+2192, so a typed
# arrow is a missing glyph in the middle of the notation. `_tuber_arrow` is the
# ONE definition of that path in this lesson — Design's own 44×24 box,
# `M4 12h30M26 5l8 7-8 7` on `currentColor`, so it inks itself on the ink-dark
# finished panel without a second copy. Its spoken equivalent is "makes", the
# same reading C4 gives it.


def _tuber_arrow():
    """Design's equation arrow (page line 175), drawn, with its spoken word.

    `currentColor` because the only place it appears is the ink-dark finished
    panel, where the text is `--ks3-on-dark`; a named colour here would be a
    second opinion about that panel's ink.
    """
    return ('<svg class="ks3-tuber-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" '
            'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>'
            '<span class="ks3-visually-hidden">makes</span>')


def _tuber_mass(value, act_id, sub_id, which):
    """One mass reading, parsed, so the build can check what it claims.

    Returns `(number, unit)`. A reading the build cannot read is a build
    error rather than a string shown to a student: §5A says a quantity the
    lesson names must be readable as a NUMBER, and a mass tile whose value
    nothing has ever parsed is a number nobody has checked.
    """
    parts = str(value or "").split()
    if len(parts) != 2:
        raise ValueError(
            "tube-run %r substance %r has %s = %r. A mass reading is a number "
            "and a unit — \"4.00 g\" — because the tile is the evidence that "
            "something left the tube, and evidence that cannot be read is an "
            "assertion." % (act_id, sub_id, which, value))
    try:
        return float(parts[0]), parts[1]
    except ValueError:
        raise ValueError(
            "tube-run %r substance %r has %s = %r, whose first word is not a "
            "number." % (act_id, sub_id, which, value))


def r_tube_run(a, act_id):
    """⊕ c5-02 `#s-tube` — one substance in, more than one out, and lighter.

    ⚖️ **THE COOLING GATE IS THE LESSON AND IT BLOCKS.** Design's `showNext`
    is `stage < 4 && !gateNeeded`, so the advance button is not on the page
    while the gate is open. That is the difference between a prediction and a
    caption: a student who can press "Let it cool" first has watched the answer
    and been asked afterwards. The gate is drawn ONCE, inside stage 4, because
    "what happens as it cools?" is not a question about copper — asking it in
    three panels would make it look like one.

    ⚖️ THE SAME METHOD, THREE TIMES. The four stage TITLES are fixed across all
    three substances and are drawn once each; only the four sentences under
    them change. That is the argument of the block — the reaction is the
    reaction whatever is in the tube — and drawing three separate steppers
    would lose it.

    ⚠️ THE MASSES ARE CHECKED AT BUILD TIME, EVERY ONE OF THEM, NOT A SAMPLE.
    `mass1` must be strictly lower than `mass0` and must carry the same unit,
    because "the tube is lighter afterwards" is the evidence the whole lesson
    rests on. Design's three pairs are exact from formula masses (CuCO₃ 123.5 →
    CuO 79.5, CaCO₃ 100 → CaO 56, 2 × NaHCO₃ 168 → Na₂CO₃ 106) and this is
    what keeps a future edit from quietly reversing one.

    ⚠️ AND THE EQUATIONS ARE CHECKED THE SAME WAY. One reactant on the left,
    two or more products on the right — counted off the " + " separators, on
    every substance. That is the definition of thermal decomposition, and it is
    the one thing on this page that could be got wrong in a way no gate and no
    screenshot would show.

    ⚠️ THE RESTING RENDER IS THE FIRST SUBSTANCE AT STAGE 0, NOTHING COMMITTED,
    NOTHING DONE. So: the first tab pressed, its intro shown and the other two
    hidden, every stage closed with the first marked current, no stage text on
    screen, the gate hidden, the tiles reading the first substance's BEFORE
    mass with "clear" limewater and "not yet" heat, the advance button showing
    its first label, both the finished panels and the all-three panel hidden,
    and `data-stage-done="0"`. A resting render that disagrees with any of that
    is a wrong number in the bytes.

    IDS EMITTED, and they are a contract with the misconception register
    (MRB-244/248): `cool-gate` on the commitment panel, and `stage-4-reveal` on
    the container holding the three stage-4 sentences. `REACT-13` names both
    and both resolve here. They are authored in the payload rather than
    composed here, so the register's join and the markup have one source.

    HOOKS: `data-tuber` (wrapper, with `data-total`) · `data-tuber-tab` (a
    substance tab, valued with the substance id) · `data-tuber-tabdone` (its
    completed mark, same value) · `data-tuber-intro` · `data-tuber-stage` (a
    stage row, valued with its index, carrying `data-open` and `data-current`)
    · `data-tuber-text` (valued `<substance>|<stage>`) · `data-tuber-gate` ·
    `data-tuber-gateopt` (valued with the option index) · `data-tuber-mass`
    (valued `<substance>|0` before, `|1` after) · `data-tuber-lime` (valued
    0/1) · `data-tuber-heat` (valued 0/1/2) · `data-tuber-next` /
    `data-tuber-nextlabel` (valued with the stage the label belongs to) ·
    `data-tuber-reset` · `data-tuber-done` (a finished panel, valued with the
    substance id) · `data-tuber-all`.
    """
    subs = a.get("substances") or []
    titles = a.get("stage_titles") or []
    adv = a.get("advance_labels") or []
    tiles = a.get("tiles") or []
    gate = a.get("gate") or {}

    if len(subs) < 2:
        raise ValueError(
            "tube-run %r offers %d substance(s). The block's argument is that "
            "the SAME method gives the same shape whatever is in the tube, and "
            "one substance cannot show a shape." % (act_id, len(subs)))
    if len(titles) != 4:
        raise ValueError(
            "tube-run %r declares %d stage title(s). The run is four moves — "
            "heat it, watch the solid, test the gas, take the flame away — and "
            "the last one is the one the lesson is for."
            % (act_id, len(titles)))
    if len(adv) != len(titles):
        raise ValueError(
            "tube-run %r has %d advance label(s) against %d stages. There is "
            "one label per move and the last of them is the one the gate holds "
            "back." % (act_id, len(adv), len(titles)))
    for key in ("id", "reveal_id", "q"):
        if not gate.get(key):
            raise ValueError(
                "tube-run %r's gate has no %r. The gate is the lesson "
                "(NOTES-C5 §2) and both of its ids are named in the "
                "misconception register, so neither may be composed here."
                % (act_id, key))
    if len(gate.get("options") or []) < 2:
        raise ValueError(
            "tube-run %r's gate offers fewer than two options. A commitment "
            "with one answer is a caption." % act_id)

    kinds = [tl.get("kind") for tl in tiles]
    if kinds != ["mass", "lime", "heat"]:
        raise ValueError(
            "tube-run %r declares tiles %r. Design draws three, in this order "
            "— the mass, the limewater and the heat — and each is driven by a "
            "different part of the run." % (act_id, kinds))
    lime_vals = tiles[1].get("values") or []
    heat_vals = tiles[2].get("values") or []
    if len(lime_vals) != 2 or len(heat_vals) != 3:
        raise ValueError(
            "tube-run %r has %d limewater value(s) and %d heat value(s); they "
            "are two (before and after the gas test) and three (not yet, "
            "while heating, once the flame is off)."
            % (act_id, len(lime_vals), len(heat_vals)))

    # ── THE CONTENT-TRUTH ASSERTION (§5A), WALKING EVERY SUBSTANCE ────────
    #
    # Two claims, and they are the two the lesson makes:
    #
    #   1. IT GETS LIGHTER. `mass1 < mass0`, same unit. "The tube is lighter
    #      afterwards" is in the hook, in the finished panel, in the key note
    #      and in rung 2; a substance whose numbers went the other way would
    #      contradict all four while every page still rendered.
    #   2. ONE IN, MORE THAN ONE OUT. One reactant on the left of the word
    #      equation, two or more products on the right. That is the definition,
    #      and the summary panel states it as the shape "every time".
    #
    # Every substance, not a sample.
    for sub in subs:
        sid = sub.get("id")
        if not sid:
            raise ValueError("tube-run %r has a substance with no id." % act_id)
        if len(sub.get("stages") or []) != len(titles):
            raise ValueError(
                "tube-run %r substance %r has %d stage sentence(s) against %d "
                "titles. Every stage of the run has to say what happened, or a "
                "student presses a button and the panel opens empty."
                % (act_id, sid, len(sub.get("stages") or []), len(titles)))
        before, unit0 = _tuber_mass(sub.get("mass0"), act_id, sid, "mass0")
        after, unit1 = _tuber_mass(sub.get("mass1"), act_id, sid, "mass1")
        if unit0 != unit1:
            raise ValueError(
                "tube-run %r substance %r weighs %s before and %s after. Two "
                "units in one tile is a fall a student cannot read."
                % (act_id, sid, sub.get("mass0"), sub.get("mass1")))
        if not after < before:
            raise ValueError(
                "tube-run %r substance %r goes %s to %s. A thermal "
                "decomposition LOSES mass from the tube, because one of the "
                "products is a gas and it leaves — that is the evidence the "
                "hook, the finished panel, the key note and rung 2 all rest "
                "on." % (act_id, sid, sub.get("mass0"), sub.get("mass1")))
        left = [s for s in str(sub.get("eq_left") or "").split(" + ") if s]
        right = [s for s in str(sub.get("eq_right") or "").split(" + ") if s]
        if len(left) != 1:
            raise ValueError(
                "tube-run %r substance %r puts %d reactants on the left of "
                "its word equation. A decomposition starts with exactly one, "
                "and \"one on the left\" is what the summary panel claims."
                % (act_id, sid, len(left)))
        if len(right) < 2:
            raise ValueError(
                "tube-run %r substance %r puts %d product(s) on the right. "
                "Decomposition is one compound broken into TWO OR MORE; one "
                "product is not this reaction." % (act_id, sid, len(right)))
        if not sub.get("finish"):
            raise ValueError(
                "tube-run %r substance %r has no `finish`. The run ends in a "
                "panel that says what is in the tube and what left it; a run "
                "that finishes with nothing to say is four presses that go "
                "nowhere." % (act_id, sid))

    first = subs[0]["id"]

    # ── the substance dial ───────────────────────────────────────────────
    #
    # The completed mark is a SPAN INSIDE THE BUTTON, hidden at rest, rather
    # than a label the wiring rebuilds. Design writes `SUBS[k].tab + (s.done[k]
    # ? ' ·' : '')`; assembling that in JavaScript would put the tab's name in
    # two languages and make a middot the thing that decides which wins.
    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-tuber-tab" '
        'data-tuber-tab="%s" aria-pressed="%s">%s'
        '<span class="ks3-tuber-tabdone" hidden data-tuber-tabdone="%s"> ·'
        '</span></button>'
        % (e(sub["id"]), "true" if sub["id"] == first else "false",
           t(sub.get("tab", "")), e(sub["id"]))
        for sub in subs)

    intros = "".join(
        '<p class="ks3-tuber-intro"%s data-tuber-intro="%s">%s</p>'
        % ("" if sub["id"] == first else " hidden", e(sub["id"]),
           rich(sub.get("intro", "")))
        for sub in subs)

    # ── the four stages ──────────────────────────────────────────────────
    #
    # `data-open` and `data-current` rather than classes, because both are
    # STATE the wiring moves and the stylesheet reads them as attribute
    # selectors. At rest: nothing open, the first current, every sentence
    # hidden — which is stage 0, before a flame has been lit.
    #
    # ⭐ The gate and the stage-4 sentences are SIBLINGS, not nested. The
    # register names `cool-gate` as REACT-13's elicitation and
    # `stage-4-reveal` as its confrontation, and a confrontation that contains
    # its own elicitation is one element wearing two jobs.
    stages = []
    last = len(titles) - 1
    for i, title in enumerate(titles):
        said = "".join(
            '<p class="ks3-tuber-text" hidden data-tuber-text="%s|%d">%s</p>'
            % (e(sub["id"]), i, rich(sub["stages"][i]))
            for sub in subs)
        gate_html = ""
        if i == last:
            opts = "".join(
                '<li><button type="button" class="ks3-option" '
                'data-tuber-gateopt="%d" aria-pressed="false">'
                '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
                '<span class="ks3-opt-label">%s</span></button></li>'
                % (j, option_letter(j), t(opt))
                for j, opt in enumerate(gate["options"]))
            gate_html = (
                '<div class="ks3-tuber-gate" id="%s" hidden data-tuber-gate>'
                '<p class="ks3-commit">%s</p>'
                '<ul class="ks3-options" role="list">%s</ul></div>'
                % (e(gate["id"]), t(gate["q"]), opts))
        stages.append(
            '<li class="ks3-tuber-stage" data-tuber-stage="%d" data-open="0" '
            'data-current="%s">'
            '<span class="ks3-tuber-num" aria-hidden="true">%d</span>'
            '<div class="ks3-tuber-body">'
            '<p class="ks3-tuber-title">%s</p>'
            '<div class="ks3-tuber-said"%s>%s</div>%s</div></li>'
            % (i, "1" if i == 0 else "0", i + 1, t(title),
               (' id="%s"' % e(gate["reveal_id"])) if i == last else "",
               said, gate_html))

    # ── the three readouts ───────────────────────────────────────────────
    #
    # EMIT-BOTH-SHOW-ONE, all the way down: every value each tile can ever
    # show is in the document from the first byte and the wiring unhides one.
    # Nothing is composed, so "4.00 g" is the author's string and not a number
    # a formatter chose, and §5A's "never hard-code a figure the instrument
    # computes" is satisfied from the other side — the instrument computes
    # nothing, it selects.
    mass_vals = "".join(
        '<span%s data-tuber-mass="%s|%d">%s</span>'
        % ("" if (sub["id"] == first and n == 0) else " hidden",
           e(sub["id"]), n, t(sub["mass0"] if n == 0 else sub["mass1"]))
        for sub in subs for n in (0, 1))
    lime_html = "".join(
        '<span%s data-tuber-lime="%d">%s</span>'
        % ("" if n == 0 else " hidden", n, t(v))
        for n, v in enumerate(lime_vals))
    heat_html = "".join(
        '<span%s data-tuber-heat="%d">%s</span>'
        % ("" if n == 0 else " hidden", n, t(v))
        for n, v in enumerate(heat_vals))

    tile_html = "".join(
        '<div class="ks3-tuber-tile">'
        '<p class="ks3-tuber-tilelabel">%s</p>'
        '<p class="ks3-tuber-tileval">%s</p></div>'
        % (t(tiles[n].get("label", "")), body)
        for n, body in enumerate((mass_vals, lime_html, heat_html)))

    # ── the two controls ─────────────────────────────────────────────────
    # Every label of the advance button is in the document and one is shown,
    # so no label is ever assembled out of an attribute.
    controls = (
        '<div class="ks3-tuber-controls">'
        '<button type="button" class="ks3-reveal-btn ks3-tuber-next" '
        'data-tuber-next>%s</button>'
        '<button type="button" class="ks3-retry ks3-tuber-reset" '
        'data-tuber-reset>%s</button></div>'
        % ("".join('<span%s data-tuber-nextlabel="%d">%s</span>'
                   % ("" if n == 0 else " hidden", n, t(lab))
                   for n, lab in enumerate(adv)),
           t(a.get("reset_label", ""))))

    # ── the finished panel, one per substance ────────────────────────────
    # Ink-dark, which is Design's own treatment (page line 173) and the one
    # place in this block that is not on cream. The arrow inks itself from
    # `currentColor`.
    dones = "".join(
        '<div class="ks3-tuber-done" hidden data-tuber-done="%s">'
        '<p class="ks3-tuber-eq"><span>%s</span>%s<span>%s</span></p>'
        '<p class="ks3-tuber-finish">%s</p></div>'
        % (e(sub["id"]), t(sub["eq_left"]), _tuber_arrow(),
           t(sub["eq_right"]), rich(sub["finish"]))
        for sub in subs)

    summary = ""
    if a.get("summary"):
        summary = ('<div class="ks3-tuber-all" hidden data-tuber-all>'
                   '<p>%s</p></div>' % rich(a["summary"]))

    return ('<div class="ks3-tuber" data-tuber data-total="%d">'
            '<div class="ks3-tuber-dial">'
            '<p class="ks3-tuber-diallabel">%s</p>'
            '<div class="ks3-tuber-tabs">%s</div></div>'
            '%s<ol class="ks3-tuber-stages" role="list">%s</ol>'
            '<div class="ks3-tuber-tiles">%s</div>%s%s%s</div>'
            % (len(subs), t(a.get("dial_label", "")), tabs, intros,
               "".join(stages), tile_html, controls, dones, summary))


# ═══ c5-02 · decomp-sort ═════════════════════════════════════════════════

def r_decomp_sort(a, act_id):
    """⊕ c5-02 `#s-sort` — five changes, and heat is in all five.

    ⚖️ **THE SHARED CLUE IS THE CONSTRUCTION.** Every one of the five involves
    heating something, so "there was a flame" sorts none of them: two are the
    reaction, one is combustion, one is a physical change and one is
    oxidation. The heading says so — "Heat is involved in all five. Only some
    are this reaction" — and that is why the five are drawn as one column of
    equals rather than sorted into two named bins, which would show the answer
    before the question.

    ⚖️ ONE COMMITMENT PER ITEM AND IT IS FINAL. Both buttons on an item
    disable when either is pressed — not to punish a change of mind, but
    because the answer is on screen by then and a second press would be a
    student choosing an option they can already read. Design's own click guard
    does the same (page line 574): the handler re-checks `st.sorts` and
    returns null.

    ⚠️ `yes` IS IN THE PAYLOAD AND IS EMITTED NOWHERE. It is Design's own
    classification of each item and it is the ANSWER; putting it in the
    document — as `data-correct`, as a class, as anything — would let the page
    mark a commitment, and R3 reserves marking for the mastery ladder alone.
    The reveal carries the answer in words, after the commitment, and that is
    the only route it takes.

    That left it as authored correctness data read by nothing, which
    `ks3_key_audit.py` is right to call dead. So it is read HERE, at build
    time, walking EVERY item: an item flagged as this reaction must open its
    answer by naming it, and an item flagged as something else must not. If
    those two ever disagree the page tells a student they were wrong when they
    were right, and nothing else in the build could see it — the flag is
    invisible and the prose is just a string.

    ⚠️ THE RESTING RENDER: five items, nothing pressed, no reveal open, every
    button live, `data-stage-done="0"`.

    HOOKS: `data-dcomp` (wrapper, with `data-total`) · `data-dcomp-item` (an
    item, valued with its id, carrying `data-open`) · `data-dcomp-opt` (a
    verdict button, valued 0/1 to index `options`) · `data-dcomp-reveal`.
    """
    items = a.get("items") or []
    options = a.get("options") or []
    if len(items) < 3:
        raise ValueError(
            "decomp-sort %r offers %d item(s). The block's argument is that a "
            "shared clue sorts nothing, and a clue needs more than two cases "
            "to be shared." % (act_id, len(items)))
    if len(options) != 2:
        raise ValueError(
            "decomp-sort %r offers %d option(s); it is a choice of two — this "
            "reaction or something else — and the whole block is built on "
            "there being exactly those two answers."
            % (act_id, len(options)))

    # ── THE CONTENT-TRUTH ASSERTION (§5A), WALKING EVERY ITEM ─────────────
    #
    # The first two words of `options[0]` are what the answer has to open with
    # when `yes` is true, taken from the payload rather than typed here: a
    # literal "Thermal decomposition" in this file would be a third copy of the
    # phrase and the one nobody would think to change.
    name = " ".join(str(options[0]).split()[:2]).lower()
    for it in items:
        iid = it.get("id")
        for key in ("text", "answer"):
            if not it.get(key):
                raise ValueError(
                    "decomp-sort %r item %r has no %r. Every item opens its "
                    "answer the instant it is decided; an item with nothing to "
                    "reveal is a commitment that goes nowhere."
                    % (act_id, iid, key))
        opens = str(it["answer"]).strip().lower().startswith(name)
        if bool(it.get("yes")) != opens:
            raise ValueError(
                "decomp-sort %r item %r is flagged %s but its answer opens "
                "%r. The flag is the author's intent and the answer is what "
                "the student reads; when they disagree the page tells a "
                "student their commitment was wrong when it was right."
                % (act_id, iid,
                   "as this reaction" if it.get("yes") else "as something else",
                   it["answer"][:48]))

    cards = "".join(
        '<div class="ks3-dcomp-item" data-dcomp-item="%s" data-open="0">'
        '<p class="ks3-dcomp-text">%s</p>'
        '<div class="ks3-dcomp-opts">%s</div>'
        '<div class="ks3-dcomp-reveal" hidden data-dcomp-reveal>'
        '<p>%s</p></div></div>'
        % (e(it.get("id", "")), rich(it["text"]),
           "".join('<button type="button" class="ks3-seg-btn ks3-dcomp-opt" '
                   'data-dcomp-opt="%d" aria-pressed="false">%s</button>'
                   % (j, t(opt)) for j, opt in enumerate(options)),
           rich(it["answer"]))
        for it in items)

    return ('<div class="ks3-dcomp" data-dcomp data-total="%d">%s</div>'
            % (len(items), cards))


# ── registrations for the commander to splice ────────────────────────────
#
# No ART row: this lesson declares no figure. Its picture is the tube run —
# an instrument with a demand, a commitment and a reveal, not a diagram — and
# NOTES-C5 §6 declares no figure anywhere in the unit.
#
# Both families tick a rail stop, so both carry `data-stage-done="0"` and
# NOTHING IS TICKED ON LOAD. `data-instrument` keeps the shell's
# `wirePredictions` out of the cooling gate's options.
#
# ⚠️ PREFIX CHANGED FROM `dsort` TO `dcomp`, AND THE FAMILY NAME IS UNCHANGED.
# The contract's table assigns `decomp-sort` / `dsort`. The family name is
# free, but `ks3-dsort-block` IS ALREADY TAKEN: `ks3_art/b5.py` registers
# `disperse-sort` with exactly that shell class. Two families wearing one class
# means this lesson's stylesheet block lands on b5-06's instrument as well, and
# it would land silently — both pages render, and only a browser on the biology
# page would show it. `dcomp` was grepped across `ks3_art/*.py`,
# `shared/ks3.js` and `shared/ks3.css` and is clear.
#




#
# And in ks3_data/c5/__init__.py's _INSTRUMENT_SEGMENTS — both are LIGHT
# `ks3-block`s on Design's page, measured (`#s-tube` and `#s-sort` carry
# `class="ks3-block"` and nothing else), so both are `check` and neither is
# `practical` or `misconception`:
#     "tube-run":    "check",
#     "decomp-sort": "check",


# ── from art_03.py ─────────────────────────────────────
# ═══ c5-03 · control-tubes and rust-stop ═════════════════════════════════
#
# Two families, one page. `control-tubes` (`#s-rust`) is the flagship and it
# is deliberately NOT A STEPPER (NOTES-C5 §2): four tubes, four commitments,
# and ONE summary that only opens when all four are decided — because the
# conclusion is not available from any three of them. `rust-stop` (`#s-stop`)
# is five real objects and one classification each, with a fifth that the
# rule the student has just learned does not fit.
#
# ── THE PAYLOAD, AND IT IS MEANT TO BE REUSED ───────────────────────────
#
# NOTES-C5 §3 declares `control-tubes` as a shape any later "what does this
# experiment control?" lesson can take. It is documented here because this is
# where the contract is enforced:
#
#     {"tubes": [{"id":   str,          a stable id, the card's hook value
#                 "name": str,          the card's headline
#                 "setup": str,         what was done to this tube
#                 "chips": [{"label": str, "on": bool}],
#                                       the CONTROLLED VARIABLES, one chip per
#                                       factor this tube takes a position on
#                 "rust": bool,         the outcome — ground truth, see below
#                 "result": str,        what was observed, in words
#                 "why":   str}],       what this one tube does for the set
#      "num_format":  "Tube {n}",       the kicker; {n} is 1-based
#      "chip_labels": {"on": …, "off": …},
#      "predict_options": [{"id": str, "label": str}],
#      "summary": {"id", "title", "text",
#                  "equation": {"left", "right"}}}
#
# ⚖️ **THE CONTROL ARGUMENT IS ASSERTED, NOT ASSUMED** (§5A: "every figure
# carries a content-truth assertion walking EVERY element, not a sample").
# `_ctube_control` below DERIVES which factors the set shows to be required —
# a factor is required if some tube removes it and no tube that removes it
# rusts — and then checks EVERY tube's `rust` against that derived rule, and
# checks that every required factor has a tube isolating it. So the summary
# paragraph cannot outlive an edit that breaks the evidence for it: flip a
# chip or a result and the build fails, rather than shipping a conclusion the
# four tubes no longer support.
#
# That is also why `rust` is in the payload at all. Design's own `lessonVals`
# never reads it — the result sentence says what happened — and it reaches no
# markup here either. It is the ground truth the assertion is checked against.
#
# ⚠️ EMIT-BOTH-SHOW-ONE, AT THE CARD LEVEL. Every tube's result and reason,
# every method's answer, and the whole summary are in the document from the
# first paint and are SHOWN, never assembled. So `<strong>` survives as the
# author wrote it, no sentence is duplicated between Python and JS, and a
# no-JS reader gets the lesson rather than four buttons.
#
# ⊖ NO `data-cfg` ON EITHER FAMILY. There is nothing to recompute: no number,
# no colour, no geometry. Both instruments are a commitment and a reveal, and
# `c3CommitCards` needs only the hooks below.
#
# ⚠️ ONLY THE LADDER MARKS. Neither family emits `data-correct`, and nothing
# green and nothing red reaches any control in either of them. A committed
# button keeps the platform's ordinary pressed treatment whichever way it
# went and its spent sibling dims; every verdict is a panel of words in the
# same voice. The chips are not marks either — they state the SETUP, and the
# state is carried by a WORD ("present" / "removed") as well as by a ground.
#
# ⚠️ THE ONE EQUATION ARROW IS DRAWN. Design's C4 convention, inherited by
# C5: the shipped font subsets contain no U+2192, so a typed arrow is a
# missing glyph in the middle of the only equation on the page.
#
# HOOKS (tubes): `data-ctube` (wrapper: `data-total`) · `data-ctube-card`
# (valued with the tube id, carrying `data-open`) · `data-ctube-opt` (valued
# with the option id) · `data-ctube-open` (the result panel) ·
# `data-ctube-summary` (the closer, also `id="four-tube-summary"`).
#
# HOOKS (stop): `data-rstop` (wrapper: `data-total`) · `data-rstop-card`
# (valued with the method id, carrying `data-open`) · `data-rstop-opt`
# (valued with the option id) · `data-rstop-answer`.


def _ctube_arrow():
    """Design's equation arrow, drawn, with its spoken word beside it.

    Her own 44×24 box from page line 146, `M4 12h30M26 5l8 7-8 7` on
    `currentColor` so one path inks itself on whatever ground the panel
    happens to carry. The spoken equivalent is "makes", which is how this
    course reads an arrow everywhere it draws one.
    """
    return ('<svg class="ks3-ctube-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" '
            'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>'
            '<span class="ks3-visually-hidden">makes</span>')


def _c5_seg(cls, hook, value, label):
    """One segmented-control button, in the key stage's ONE segmented control.

    ⚠️ There is no `correct` parameter here and there must never be one.
    Nothing in either of these families marks: a pressed control says it was
    PRESSED, and every verdict is a panel of words.
    """
    return ('<button type="button" class="ks3-seg-btn %s" %s="%s" '
            'aria-pressed="false">%s</button>'
            % (e(cls), hook, e(value), t(label)))


def _c5_options(a, key, act_id, cls, hook):
    """The two-button control every card in both families carries."""
    opts = a.get(key) or []
    if len(opts) != 2:
        raise ValueError(
            "%r offers %d option(s) in %r, and the card draws a PAIR. The "
            "pair IS the question on both of this lesson's instruments — will "
            "it rust or will it not, is it a barrier or is it something else "
            "— and a third button would be a third question."
            % (act_id, len(opts), key))
    for o in opts:
        if not o.get("id") or not o.get("label"):
            raise ValueError(
                "%r has an option in %r with no id or no label. The id is the "
                "hook the wiring reads; the label is what the student presses."
                % (act_id, key))
    return "".join(_c5_seg(cls, hook, o["id"], o["label"]) for o in opts)


def _ctube_control(tubes, act_id):
    """Derive the REQUIRED factors, and prove the set actually shows them.

    This is the assertion the whole lesson rests on, and it walks every tube
    and every chip rather than sampling.

    A factor is REQUIRED if at least one tube removes it and no tube that
    removes it rusts. Salt appears in exactly one tube and is never removed,
    so it can never be derived as required — which is the honest reading of
    the evidence and is precisely why tube 4 is an accelerator rather than a
    fifth requirement. Nothing here is told which factor is which.

    Then, for the set to support the conclusion the summary states:

      · every tube must take a position on every required factor, or
        "present" is a guess rather than a reading;
      · every tube's own `rust` must agree with the derived rule;
      · every required factor must have a tube that ISOLATES it — that
        factor removed and all the others still present. That is what makes
        tubes 2 and 3 controls rather than merely two more tubes;
      · at least two factors must be required, and at least one tube with all
        of them present must rust, or there is no positive result to control
        against.
    """
    off_in = {}
    for tube in tubes:
        for chip in tube.get("chips") or []:
            if not chip.get("label"):
                raise ValueError(
                    "%r: tube %r has a chip with no label. A controlled "
                    "variable a student cannot read the name of is not a "
                    "controlled variable." % (act_id, tube.get("id")))
            if not chip.get("on"):
                off_in.setdefault(chip["label"], []).append(tube)

    required = sorted(name for name, offs in off_in.items()
                      if not any(bool(x.get("rust")) for x in offs))
    if len(required) < 2:
        raise ValueError(
            "%r: the tubes show %d factor(s) to be required, and this "
            "instrument's whole argument is that no single factor is enough. "
            "A set that establishes one requirement is a demonstration, not a "
            "controlled investigation." % (act_id, len(required)))

    positive = 0
    for tube in tubes:
        present = {c["label"] for c in tube.get("chips") or [] if c.get("on")}
        named = {c["label"] for c in tube.get("chips") or []}
        missing = [r for r in required if r not in named]
        if missing:
            raise ValueError(
                "%r: tube %r takes no position on %s, and that factor is one "
                "the set relies on. Every tube has to say whether each "
                "requirement is present or removed, or the reader is guessing "
                "at the setup." % (act_id, tube.get("id"), ", ".join(missing)))
        expected = all(r in present for r in required)
        if bool(tube.get("rust")) != expected:
            raise ValueError(
                "%r: tube %r is recorded as %s, and the factors it carries "
                "say it should be %s — the requirements this set establishes "
                "are %s. One of the chips or the result is wrong, and the "
                "summary would go on claiming a conclusion the tubes no "
                "longer support."
                % (act_id, tube.get("id"),
                   "rusting" if tube.get("rust") else "not rusting",
                   "rusting" if expected else "not rusting",
                   " and ".join(required)))
        if expected:
            positive += 1

    if not positive:
        raise ValueError(
            "%r: no tube has every requirement present, so nothing in the set "
            "rusts and the controls are controlling against nothing."
            % act_id)

    for name in required:
        isolating = [x for x in off_in[name]
                     if all(c.get("on") for c in x.get("chips") or []
                            if c["label"] in required and c["label"] != name)]
        if not isolating:
            raise ValueError(
                "%r: nothing isolates %s — no tube removes it while keeping "
                "every other requirement. Two factors removed at once rules "
                "out neither of them, and that is the single mistake this "
                "instrument exists to teach against." % (act_id, name))
    return required


def r_control_tubes(a, act_id):
    """⊕ c5-03 `#s-rust` — four tubes, and the two in the middle do the work.

    ⚖️ **NOT A STEPPER** (NOTES-C5 §2). There is no order to these four and
    no gate between them: each opens on its own commitment, in whatever order
    the student picks. What is gated is the SUMMARY, and it is gated on all
    four — because "both oxygen and water are needed" is a conclusion no
    three of these tubes can support, and showing it earlier would hand the
    student the finding the set exists to make them assemble.

    ⚠️ THE COMMITMENT IS FINAL, per card. The result is on screen the instant
    a tube is decided, so a second press would be a student choosing an answer
    they can already read. Both buttons disable and the one that was not
    pressed dims — the card still says what was predicted.

    ⚠️ NOTHING HERE MARKS. A tube that was predicted wrong looks exactly like
    a tube that was predicted right: same treatment on the pressed button,
    same ink panel underneath, same two sentences. The correction, where there
    is one, is the result itself.

    ⚑ `data-activity="tube-predictions"` on the section around this (the
    activity id, from the record) and `id="four-tube-summary"` on the panel
    below. Those are `REACT-15`'s two joins and this is where they resolve:
    committing "will rust" on tube 2 or tube 3 IS the belief that air alone or
    water alone is enough, and the summary is the only place on the page that
    reads those two tubes together.
    """
    tubes = a.get("tubes") or []
    if len(tubes) < 3:
        raise ValueError(
            "control-tubes %r declares %d tube(s). One tube is a result, two "
            "are a comparison, and a controlled investigation needs a "
            "positive and a control for each factor it tests."
            % (act_id, len(tubes)))
    summary = a.get("summary") or {}
    for key in ("id", "title", "text"):
        if not summary.get(key):
            raise ValueError(
                "control-tubes %r has no summary.%s. The summary is the whole "
                "point of the shape — four results that mean nothing apart "
                "and something together — and a set of cards with no reading "
                "of them is four disconnected demonstrations."
                % (act_id, key))
    # The content-truth assertion. See `_ctube_control`.
    _ctube_control(tubes, act_id)

    labels = a.get("chip_labels") or {}
    for state in ("on", "off"):
        if not labels.get(state):
            raise ValueError(
                "control-tubes %r has no chip_labels[%r]. A chip has to say "
                "in a WORD whether the factor is there — a background colour "
                "on its own is not a state (R2)." % (act_id, state))
    num_format = a.get("num_format") or ""
    if "{n}" not in num_format:
        raise ValueError(
            "control-tubes %r has a num_format of %r with no {n} in it. The "
            "summary and the ladder both quote tubes by number, and a card "
            "whose kicker does not carry one leaves them pointing at nothing."
            % (act_id, num_format))

    cards = []
    for i, tube in enumerate(tubes):
        chips = "".join(
            '<span class="ks3-ctube-chip" data-on="%s">%s</span>'
            % ("1" if c.get("on") else "0",
               t("%s %s" % (c["label"],
                            labels["on"] if c.get("on") else labels["off"])))
            for c in tube.get("chips") or [])
        cards.append(
            '<div class="ks3-ctube-card" data-ctube-card="%s" data-open="0">'
            '<p class="ks3-ctube-num">%s</p>'
            '<p class="ks3-ctube-name">%s</p>'
            '<p class="ks3-ctube-setup">%s</p>'
            '<div class="ks3-ctube-chips">%s</div>'
            '<div class="ks3-ctube-opts">%s</div>'
            '<div class="ks3-ctube-open" data-ctube-open hidden>'
            '<p class="ks3-ctube-result">%s</p>'
            '<p class="ks3-ctube-why">%s</p></div></div>'
            % (e(tube.get("id", "")),
               t(num_format.replace("{n}", str(i + 1))),
               t(tube.get("name", "")), rich(tube.get("setup", "")), chips,
               _c5_options(a, "predict_options", act_id,
                           "ks3-ctube-opt", "data-ctube-opt"),
               rich(tube.get("result", "")), rich(tube.get("why", ""))))

    eq = summary.get("equation") or {}
    eq_row = ""
    if eq.get("left") and eq.get("right"):
        eq_row = ('<p class="ks3-ctube-eq"><span>%s</span>%s<span>%s</span></p>'
                  % (t(eq["left"]), _ctube_arrow(), t(eq["right"])))

    return ('<div class="ks3-ctube" data-ctube data-total="%d">'
            '<div class="ks3-ctube-grid">%s</div>'
            '<div class="ks3-ctube-summary" id="%s" data-ctube-summary hidden>'
            '<p class="ks3-ctube-sumtitle">%s</p>'
            '<p class="ks3-ctube-sumtext">%s</p>%s</div></div>'
            % (len(tubes), "".join(cards), e(summary["id"]),
               t(summary["title"]), rich(summary["text"]), eq_row))


def r_rust_stop(a, act_id):
    """⊕ c5-03 `#s-stop` — five ways to stop it, and one of them is not.

    ⚖️ **THE FIFTH ONE IS THE LESSON, AND IT IS DELIBERATELY LEFT UNMARKED.**
    Four of these keep the oxygen and the water out; the zinc blocks cover
    nothing at all, and the galvanised gate is both. The block's own lede
    tells the student that one of the five should feel wrong under the rule
    they have just been given, and then declines to say which — because the
    finding is the point and the panel that opens says it in words.

    ⚠️ There is no answer key in this markup and none is needed. The answer
    paragraph is the same paragraph whichever button was pressed, and it
    names the kind rather than the press. `barrier` is in the payload as the
    record's own note of which methods are not simply barriers; it reaches no
    markup, and if it ever did it would be a mark.

    ⚠️ THE COMMITMENT IS FINAL, per card — `c3CommitCards`' contract, the same
    one the tubes above take.
    """
    methods = a.get("methods") or []
    if len(methods) < 2:
        raise ValueError(
            "rust-stop %r declares %d method(s). The section teaches by "
            "contrast across methods, and one method is an example."
            % (act_id, len(methods)))
    seen = set()
    cards = []
    for m in methods:
        if not m.get("id") or m["id"] in seen:
            raise ValueError(
                "rust-stop %r has a method with a missing or repeated id "
                "(%r). The id is the card's hook and two cards wearing one "
                "name would answer each other." % (act_id, m.get("id")))
        seen.add(m["id"])
        if not m.get("answer"):
            raise ValueError(
                "rust-stop %r method %r has no answer. The answer IS the "
                "teaching here — without it the card asks a student to "
                "classify something and then tells them nothing."
                % (act_id, m["id"]))

        # ── THE CONTENT-TRUTH ASSERTION (§5A), AND WHAT `barrier` IS FOR ──
        #
        # `barrier` reaches no markup — it is the answer, and R3 reserves
        # marking for the ladder — which left it as authored correctness data
        # read by nothing, exactly as c4-01's `chemical` was. `ks3_key_audit`
        # is right to call that dead: a key with no read site is an invariant
        # nothing is checking.
        #
        # So it is read HERE, at build time, and what it guards is the one
        # disagreement nothing else in the build could see. `barrier` is what
        # the author MEANT; `answer` is what the student READS. The flag is
        # invisible and the answer is just a string, so if the two ever drift
        # apart the page tells a student that zinc blocks are a barrier — the
        # precise belief this section exists to break, since sacrificial
        # protection is the one method that is NOT a barrier and is why the
        # section has five cards instead of one.
        #
        # Walks EVERY method, not a sample. The test is the answer's OPENING
        # — Design writes each one as a verdict first — and it is THREE-WAY,
        # not two, which is the whole reason the section is worth reading:
        #
        #   barrier=True   opens "A barrier…"        paint, grease, stainless
        #   barrier=False  opens "Not a barrier — …" sacrificial zinc blocks
        #   barrier=False  opens "Both, and …"       galvanising, which is a
        #                                            barrier AND sacrificial
        #
        # So `barrier` does not mean "is a barrier". It means "a barrier is
        # the WHOLE answer", and galvanising is the card that makes the
        # distinction matter. The assertion is therefore that a method
        # claiming the whole answer opens by claiming it, and one that does
        # not never opens with an unqualified "A barrier".
        opening = (m.get("answer") or "").strip().lower()
        whole = opening.startswith("a barrier")
        if bool(m.get("barrier")) != whole:
            raise ValueError(
                "rust-stop %r method %r is flagged barrier=%r but its answer "
                "opens %r. The flag means 'a barrier is the WHOLE answer'; "
                "the answer is what the student reads. When they disagree the "
                "card teaches the opposite of what was meant — and on this "
                "section that means teaching that sacrificial protection is "
                "just a barrier, which is the belief it exists to break."
                % (act_id, m["id"], bool(m.get("barrier")),
                   (m.get("answer") or "")[:48]))
        cards.append(
            '<div class="ks3-rstop-card" data-rstop-card="%s" data-open="0">'
            '<p class="ks3-rstop-name">%s</p>'
            '<p class="ks3-rstop-what">%s</p>'
            '<div class="ks3-rstop-opts">%s</div>'
            '<p class="ks3-rstop-answer" data-rstop-answer hidden>%s</p>'
            '</div>'
            % (e(m["id"]), t(m.get("name", "")), rich(m.get("what", "")),
               _c5_options(a, "verdict_options", act_id,
                           "ks3-rstop-opt", "data-rstop-opt"),
               rich(m["answer"])))
    return ('<div class="ks3-rstop" data-rstop data-total="%d">%s</div>'
            % (len(methods), "".join(cards)))


# No drawer row from this fragment: c5-03 declares no figure, and the marker
# is deliberately not written above with the word "none" after it —
# build_ks3.py records a splice that took exactly that as a table row and
# emitted it into the registry, which is a SyntaxError in the generator. A
# marker that means "no row" has to not be the marker.




# REGISTER SEGMENT: 'control-tubes': "check",
# REGISTER SEGMENT: 'rust-stop': "check",


# ── from art_04.py ─────────────────────────────────────
# ═══ c5-04 · displacement ════════════════════════════════════════════════
#
# ⚠️ REQUIRES IMPORT — six kit names beyond the contract's standing list, all
# of them already in `ks3_art/kit.py`, none of them redefined here (a local
# copy of a kit token is the drift the kit exists to prevent):
#
#     _SVG_ACCENT_TINT  _SVG_ACCENT_TEXT  _SVG_BAND  _SVG_CARD
#     _SVG_RULE         _SVG_DISPLAY
#
# plus the standing ones this fragment uses: `e`, `t`, `rich`, `_svg_open`,
# `_rect`, `_path`, `_label`, `_mono`, `_SVG_INK`, `_SVG_ACCENT`, `_SVG_INSET`
# and `json`. If one is missing the import fails loudly at build, which is the
# safe direction.
#
# Two families, both DOM, plus one drawn figure:
#
#   `reactivity-grid`  #s-grid — a 4×4 grid, sixteen predictions, and every
#                      cell's observation GENERATED from the two metals' data
#                      (NOTES-C5 §3). Adding a fifth metal is a one-line change
#                      in `ks3_data/c5/lesson_04_displacement.py`; C8 and C9
#                      both want this grid with more rows.
#   `reactivity-use`   #s-uses — three consequence cards, one commitment each.
#   `reactivity-series` the reference plate above the grid. NOT an instrument:
#                      no family, no rail stop, no `data-stage-done`, no
#                      wiring. It is drawn here because a `figure` is the one
#                      thing in the closed §5.1.1 vocabulary that can hold
#                      twelve rows AND be checked against the bench below it.
#
# Both families sit in a LIGHT `ks3-block` — measured off Design's own markup
# (page lines 145 and 216, `class="ks3-block"` and nothing else) — and both
# tick a rail stop, so both ship `data-stage-done="0"` and NOTHING is ticked on
# load (MRB-208).
#
# ⚠️ ONLY THE LADDER MARKS. No `data-correct` anywhere in either family. A run
# cell is painted by its RESULT, not by whether the student's prediction
# matched it: `reacts` takes the accent tint and `none` the band, which are the
# two grounds Design draws, and neither is a verdict on the student. The
# prediction itself is never compared to anything — it is a Law 4 gate, and the
# panel that opens says the same thing in the same box whichever button was
# pressed.
#
# ⚠️ EMIT-BOTH-SHOW-ONE, AT SIXTEEN. Every one of the sixteen cells has its
# title, its setup line, its verdict, its explanation and its equation in the
# document from the first byte, and the wiring only chooses which is `hidden`.
# So no sentence is composed at run time, `<strong>` and the em dashes survive
# as authored, and the RESTING DOM — the fe:cu cell selected, nothing run, the
# counter at zero — is the state a crawler and a no-JS reader see.
#
# ⚠️ THE ARROW IS DRAWN, NEVER TYPED. Design's C4 convention, inherited here:
# the shipped font subsets contain no U+2192.


# ── numbers as words, past twelve ───────────────────────────────────────
#
# `kit.NUMBER_WORDS` stops at twelve because nothing before this needed
# thirteen. This grid needs "sixteen" for its own payoff paragraph, and a fifth
# metal needs "twenty-five". A lane may not edit `kit.py` (MRB-271: it is
# shared), so the table is carried on HERE rather than duplicated — the first
# thirteen are still kit's. If a second unit ever needs this, it is a promotion
# into the kit, not a second copy.
_RGRID_TENS = ("thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
               "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
               "twenty-three", "twenty-four", "twenty-five", "twenty-six",
               "twenty-seven", "twenty-eight", "twenty-nine", "thirty",
               "thirty-one", "thirty-two", "thirty-three", "thirty-four",
               "thirty-five", "thirty-six")
_RGRID_UNITS = ("no", "one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve")


def _rgrid_word(n):
    """`n` as the word this page would print, or the numeral past the table."""
    if 0 <= n < len(_RGRID_UNITS):
        return _RGRID_UNITS[n]
    if 13 <= n < 13 + len(_RGRID_TENS):
        return _RGRID_TENS[n - 13]
    return str(n)


def _rgrid_fill(tpl, values, where):
    """Fill `{Name}` placeholders AT BUILD TIME, and refuse a leftover.

    ⚠️ Every sentence this instrument shows is filled HERE, in Python, and then
    emitted as real markup. Nothing is filled in JavaScript and nothing is
    assembled out of an attribute, which is what keeps `<strong>` and the em
    dashes intact and keeps one authored sentence from existing twice.

    A `{` surviving the fill is a typo'd placeholder, and §14 lists
    `{placeholder}` beside `[object Object]` as text that may never reach a
    student. It fails the BUILD instead.
    """
    out = str(tpl)
    for key in sorted(values, key=len, reverse=True):
        out = out.replace("{%s}" % key, str(values[key]))
    if "{" in out or "}" in out:
        raise ValueError(
            "%s left a placeholder unfilled: %r. Known keys here are %s."
            % (where, out, ", ".join(sorted(values))))
    return out


def _c5_cfg(obj):
    """`data-cfg`, deterministically ordered and safe in an attribute.

    ⚠️ A LOCAL COPY ON PURPOSE, and the third one in the key stage —
    `ks3_art/c3.py` has these three lines as `_cfg` and `ks3_art/c4.py` as
    `_c4_cfg`. Reaching across for either would make this module depend on
    another unit's module, and one unit, one file. Promoting it into
    `ks3_art/kit.py` is the right move and is a SHARED-FILE edit, so it is
    reported rather than taken — now with three call sites arguing for it.

    `sort_keys` so two builds of one payload are byte-identical;
    `ensure_ascii=False` so a non-ASCII character stays itself.
    """
    return e(json.dumps(obj, separators=(",", ":"), sort_keys=True,
                        ensure_ascii=False))


def _rgrid_arrow():
    """Design's own 44×24 reaction arrow (page line 194), redrawn not retyped.

    `currentColor` is what lets the one path serve the ink result panel without
    a second copy, and `flex: 0 0 auto` in the stylesheet stops the row
    squeezing it out of shape.
    """
    return ('<svg class="ks3-rgrid-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true"><path d="M4 12h30M26 5l8 7-8 7" '
            'fill="none" stroke="currentColor" stroke-width="2.6" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _rgrid_metals(a, act_id):
    """The bench, checked. Returns the list; raises on anything it cannot draw.

    ⚠️ `order` IS DATA AND IS NEVER INFERRED FROM POSITION (NOTES-C5 §6): C9
    adds metals in the MIDDLE of this list, and a renderer that read reactivity
    off the index would silently re-rank every existing cell the moment it did.
    So the ranks are checked for what they have to be — a complete run of
    0..n-1, each used once — and everything downstream sorts by `order`.
    """
    metals = a.get("metals") or []
    if len(metals) < 2:
        raise ValueError(
            "reactivity-grid %r declares %d metal(s). The grid IS a comparison "
            "of metals against each other's solutions, and one metal compares "
            "with nothing." % (act_id, len(metals)))

    seen = set()
    for m in metals:
        for key in ("id", "name", "solution", "sol_colour", "deposit"):
            if not m.get(key):
                raise ValueError(
                    "reactivity-grid %r metal %r has no %r. Every cell's "
                    "sentence is built from these five, so a missing one is a "
                    "blank in the middle of an observation."
                    % (act_id, m.get("id") or m.get("name"), key))
        if m["id"] in seen:
            raise ValueError(
                "reactivity-grid %r has two metals with id %r. The cell keys "
                "are built from the pair of ids, so a duplicate would give two "
                "cells one panel." % (act_id, m["id"]))
        seen.add(m["id"])
        if not isinstance(m.get("order"), int) or isinstance(m["order"], bool):
            raise ValueError(
                "reactivity-grid %r metal %r has order %r. The reactivity rank "
                "is an integer and it is DATA — it is never read off the "
                "position in the list, because the next unit inserts metals in "
                "the middle." % (act_id, m["id"], m.get("order")))

    ranks = sorted(m["order"] for m in metals)
    if ranks != list(range(len(metals))):
        raise ValueError(
            "reactivity-grid %r has ranks %s for %d metals. They have to be a "
            "complete run from 0, each used once: the whole payoff panel is "
            "the claim that these metals fall in ONE order, and a gap or a "
            "tie would make that sentence false about its own table."
            % (act_id, ranks, len(metals)))
    return metals


def _rgrid_cells(a, act_id, metals):
    """Every pair, in reading order, with its five sentences already filled.

    ⚖️ THE DIAGONAL IS ENUMERATED LIKE ANY OTHER PAIR. A metal in its own
    solution is one of the sixteen, not an exception carved out of the loop —
    §5A is explicit that the whole state space is enumerated and that a state
    is never special-cased away. Design's own lede says the four diagonal cells
    are worth running, and her panel for them explains why nothing could have
    happened. If they were skipped here the lede would be describing four
    buttons that do nothing.
    """
    tpl = a.get("templates") or {}
    for key in ("title", "setup_same", "setup_other", "result_same",
                "result_reacts", "result_none", "why_same", "why_reacts",
                "why_reacts_colourless", "why_none", "eq_left", "eq_right"):
        if not tpl.get(key):
            raise ValueError(
                "reactivity-grid %r has no %r template. Every cell is built "
                "from these twelve shapes and there is no cell text anywhere "
                "else to fall back on." % (act_id, key))

    cells = []
    for m in metals:
        for s in metals:
            same = m["id"] == s["id"]
            # The lesson's own rule, and the ONLY place it is decided.
            # `order` is the rank, so a lower rank is the more reactive metal.
            reacts = (not same) and m["order"] < s["order"]
            deposit = s["deposit"]
            values = {
                "Metal": m["name"], "metal": m["name"].lower(),
                "Other": s["name"], "other": s["name"].lower(),
                "solution": s["solution"], "own_solution": m["solution"],
                "colour": s["sol_colour"],
                "Deposit": deposit[:1].upper() + deposit[1:],
            }
            where = "reactivity-grid %r cell %s:%s" % (act_id, m["id"], s["id"])

            if same:
                setup, result, why = "setup_same", "result_same", "why_same"
            elif reacts:
                setup, result = "setup_other", "result_reacts"
                # ⚑ SCIENCE, and the reason there are two reacting templates.
                # A COLOURLESS SOLUTION CANNOT FADE. Design has one sentence
                # and it opens "The {colour} solution fades…", which is true of
                # five of this bench's six reacting cells and false of
                # magnesium in zinc sulfate. The branch is on the DATA, so it
                # keeps working when the bench changes.
                if s["sol_colour"] == "colourless":
                    if m["sol_colour"] != "colourless":
                        raise ValueError(
                            "%s puts a metal whose own solution is %r into a "
                            "colourless one. Neither reacting template fits: "
                            "one says the colour fades and the other says "
                            "there is no colour to watch, and here a colour "
                            "ARRIVES. Author a third shape rather than "
                            "printing a false observation."
                            % (where, m["sol_colour"]))
                    why = "why_reacts_colourless"
                else:
                    why = "why_reacts"
            else:
                setup, result, why = "setup_other", "result_none", "why_none"

            cells.append({
                "key": "%s:%s" % (m["id"], s["id"]),
                "state": "reacts" if reacts else "none",
                "label": _rgrid_fill(a.get("cell_label") or tpl["title"],
                                     values, where + " label"),
                "title": _rgrid_fill(tpl["title"], values, where + " title"),
                "setup": _rgrid_fill(tpl[setup], values, where + " setup"),
                "result": _rgrid_fill(tpl[result], values, where + " result"),
                "why": _rgrid_fill(tpl[why], values, where + " why"),
                "eq": ((_rgrid_fill(tpl["eq_left"], values, where + " eq"),
                        _rgrid_fill(tpl["eq_right"], values, where + " eq"))
                       if reacts else None),
            })
    return cells


def _rgrid_pattern(a, act_id, metals):
    """The payoff panel, with EVERY figure in it computed from the bench.

    §5A: never hard-code a figure the instrument computes. This panel is
    nothing BUT figures — how many metals, how many tubes, what order they came
    out in, and how many each one displaced — so all four are derived and
    Design's exact sentences fall out of them today. Add a fifth metal and the
    paragraph rewrites itself rather than lying.

    ⭐ `compare` is the paragraph Mide ruled on 18 Aug 2026 (NOTES-C5 §7). It
    used to say "You did not look this up", which stopped being true when the
    reactivity series moved to the top of the page. It now says the tubes
    REPRODUCED the reachable part of a published list — the honest version, and
    the one Design has already made. It is not reverted here.
    """
    p = a.get("pattern") or {}
    for key in ("title", "shape", "row", "order", "compare"):
        if not p.get(key):
            raise ValueError(
                "reactivity-grid %r pattern has no %r. The payoff is the point "
                "of running the grid; a panel missing one of its paragraphs is "
                "a stop that ticks and says nothing." % (act_id, key))

    ranked = sorted(metals, key=lambda m: m["order"])
    n = len(ranked)
    rows = []
    for m in ranked:
        # How many metals this one is above, and so how many it displaces.
        beaten = n - 1 - m["order"]
        if beaten == n - 1:
            tally = p.get("tally_all") or _rgrid_word(beaten)
        elif beaten == 0:
            tally = p.get("tally_none") or _rgrid_word(beaten)
        else:
            tally = _rgrid_word(beaten)
        rows.append(_rgrid_fill(p["row"],
                                {"metal": m["name"].lower(), "tally": tally},
                                "reactivity-grid %r pattern row" % act_id))

    counts = {"count": _rgrid_word(n), "cells": _rgrid_word(n * n),
              "rows": (p.get("rows_join") or ", ").join(rows)}
    order_line = _rgrid_fill(
        p["order"],
        {"order": (p.get("order_join") or " · ").join(
            m["name"].lower() for m in ranked)},
        "reactivity-grid %r pattern order" % act_id)
    return {
        "title": p["title"],
        "shape": _rgrid_fill(p["shape"], counts,
                             "reactivity-grid %r pattern shape" % act_id),
        "order": order_line,
        "compare": _rgrid_fill(p["compare"], counts,
                               "reactivity-grid %r pattern compare" % act_id),
    }


def r_reactivity_grid(a, act_id):
    """⊕ c5-04 `#s-grid` — four metals, four solutions, sixteen predictions.

    ⚖️ **THE SHAPE OF THE COMPLETED TABLE IS THE ARGUMENT.** NOTES-C5 §2: the
    reactivity order "falls out of the shape of the completed table rather than
    being stated". Every reaction is on one side of the diagonal and every
    blank on the other, and that is what an ORDER looks like drawn as a grid.
    Which is why `order` is checked to be a complete run above: a tie or a gap
    would leave a table that could not have that shape, under a paragraph
    saying it does.

    ⚖️ **NOT ONE CELL'S SENTENCE IS WRITTEN DOWN.** Twelve templates, filled
    for all sixteen pairs at build time. NOTES §3 asks for exactly this and
    names the reason: C8 and C9 want this grid with more rows, and a payload of
    sixteen hand-written panels would have to be re-written as twenty-five.

    ⚠️ ONLY THE LADDER MARKS. A cell is painted by its RESULT — accent tint for
    a reaction, band for none, both Design's own grounds — and never by whether
    the prediction matched. The prediction is a Law 4 gate and is compared with
    nothing: both buttons open the same panel, in the same box, in the same
    voice.

    ⊖ ONE DEPARTURE FROM DESIGN'S PROTOTYPE, AND IT IS THE PLATFORM'S SETTLED
    TREATMENT. Her `needPredict` HIDES the predict row once a cell has been
    run, and her `predictButtons` hard-code `pressed: false`, so a commitment
    leaves no trace anywhere. On a grid whose whole shape is "come back to a
    cell", that loses the one thing the student put in. The row therefore
    stays, with both buttons disabled and the chosen one still pressed — which
    is what `c3CommitCards` does on every other commit-once control in the key
    stage, and what MRB-257 3.21 ruled `--ks3-dim-spent` for: "you may not
    press this any more" and "you may not read this" are two different
    sentences. Reported to the commander.

    IDS EMITTED, AND THEY ARE A CONTRACT WITH THE MISCONCEPTION REGISTER
    (MRB-244/248): `grid-predict` on the predict row, which is where a student
    commits to "a reaction happens" about a pair that cannot give one, and
    `grid-reveal` on the results region, where that is taken apart in words.
    `REACT-17` names both and both resolve here. NOTES §5 proposes
    `grid-lower-cells` for the first; the lower cells are six scattered buttons
    rather than one element, and the commitment is not made on the cell at all,
    so the row that carries it is named instead. Reported.

    HOOKS: `data-rgrid` (wrapper, with `data-cfg`) · `data-rgrid-cell` (a cell
    button, valued with the pair key) · `data-rgrid-mark` / `data-rgrid-say`
    (the three printed marks and the three spoken states inside it) ·
    `data-rgrid-setup` · `data-rgrid-predict` · `data-rgrid-opt` ·
    `data-rgrid-result` · `data-rgrid-pattern`.
    """
    metals = _rgrid_metals(a, act_id)
    cells = _rgrid_cells(a, act_id, metals)
    n = len(metals)
    total = n * n

    # ── the head row and the counter say the same numbers as the payload ──
    #
    # §5A: if the lesson names a quantity it must be readable as a number, and
    # the numbers on the page must be the payload's. The block's eyebrow and
    # heading are drawn by the SHELL, before this function runs, so they cannot
    # be filled from here — but they CAN be checked from here, and they are the
    # two places on the page where a fifth metal would leave a stale count
    # behind. "Your turn · sixteen combinations" over a twenty-five cell grid
    # is a wrong number in the bytes.
    for slot, want in (("heading", _rgrid_word(n)),
                       ("eyebrow", _rgrid_word(total))):
        said = (a.get(slot) or "").lower()
        if want not in said:
            raise ValueError(
                "reactivity-grid %r has %d metals and %d cells, so its %s "
                "should say %r. It says %r. The head row is the one place a "
                "count can go stale without anything else on the page moving."
                % (act_id, n, total, slot, want, a.get(slot)))

    # And the live counter's denominator, which the SHELL has already drawn by
    # the time this runs. Left unchecked it fails in the one direction nothing
    # else catches: a missing or wrong `total` ships "0 of 0 run" at the top of
    # the block, and every gate downstream sees a rendered page and passes it.
    hc = a.get("head_counter") or {}
    if hc and hc.get("total") != total:
        raise ValueError(
            "reactivity-grid %r counts to %r in its head row and has %d cells. "
            "The readout is the student's own progress through this grid, so "
            "the denominator is not a number an author gets to choose."
            % (act_id, hc.get("total"), total))

    done_at = a.get("done_at")
    if not isinstance(done_at, int) or isinstance(done_at, bool) \
            or not 1 <= done_at <= total:
        raise ValueError(
            "reactivity-grid %r asks for %r cells before the stop ticks, out "
            "of %d. A threshold larger than the grid is a rail stop that can "
            "never tick, and MRB-249 does not add one of those."
            % (act_id, done_at, total))

    states = a.get("states") or {}
    for key in ("unrun", "reacts", "none"):
        st = states.get(key) or {}
        if not st.get("mark") or not st.get("say"):
            raise ValueError(
                "reactivity-grid %r state %r needs a `mark` (what is printed "
                "in the cell) and a `say` (what a screen reader hears). They "
                "are two elements in the button rather than one aria-label, "
                "because a label rewritten by the wiring is a sentence "
                "composed in JavaScript." % (act_id, key))

    open_at = a.get("open_at") or {}
    open_key = "%s:%s" % (open_at.get("metal"), open_at.get("sol"))
    if open_key not in {c["key"] for c in cells}:
        raise ValueError(
            "reactivity-grid %r opens on %r, which is not one of the %d cells. "
            "The RESTING DOM is that cell's panel shown and every other one "
            "hidden, so a bad key ships a panel with nothing in it."
            % (act_id, open_key, total))

    # ── the table ─────────────────────────────────────────────────────────
    heads = "".join('<th scope="col">%s</th>' % t(m["solution"])
                    for m in metals)
    by_key = {c["key"]: c for c in cells}
    rows = []
    for m in metals:
        tds = []
        for s in metals:
            c = by_key["%s:%s" % (m["id"], s["id"])]
            # EMIT-BOTH-SHOW-ONE, three ways over, inside one button: the
            # printed mark, and the spoken state beside it. The accessible name
            # is therefore ASSEMBLED IN THE DOM — "Iron in copper sulfate" plus
            # ": not yet run" — and the wiring only toggles `hidden`. The colon
            # is punctuation between two authored strings and is the one thing
            # here that is not the author's.
            marks = "".join(
                '<span class="ks3-rgrid-mark" data-rgrid-mark="%s" '
                'aria-hidden="true"%s>%s</span>'
                % (e(k), "" if k == "unrun" else " hidden",
                   t(states[k]["mark"]))
                for k in ("unrun", "reacts", "none"))
            says = "".join(
                '<span class="ks3-sr-only" data-rgrid-say="%s"%s>: %s</span>'
                % (e(k), "" if k == "unrun" else " hidden",
                   t(states[k]["say"]))
                for k in ("unrun", "reacts", "none"))
            # ⚠️ `data-rgrid-outcome` IS NOT A MARK AND IS NOT AN ANSWER KEY.
            # It is what the tube DID, and the wiring needs it to know which of
            # the three marks already in the button to show once the cell is
            # run. It is no more of a disclosure than the panel it belongs to:
            # all sixteen results are in the document from the first byte
            # (EMIT-BOTH-SHOW-ONE), hidden, and this is the classification that
            # picks one. Nothing anywhere compares it with the student's
            # prediction, and no styling keys off it — the paint follows
            # `data-rgrid-state`, which starts at `unrun` for every cell.
            tds.append(
                '<td><button type="button" class="ks3-rgrid-cell" '
                'data-rgrid-cell="%s" data-rgrid-outcome="%s" '
                'data-rgrid-state="unrun" aria-pressed="%s">'
                '<span class="ks3-sr-only">%s</span>%s%s</button></td>'
                % (e(c["key"]), e(c["state"]),
                   "true" if c["key"] == open_key else "false",
                   t(c["label"]), marks, says))
        rows.append('<tr><th scope="row">%s</th>%s</tr>'
                    % (t(m["name"]), "".join(tds)))

    # ⚠️ THE SCROLL REGION IS NOT A NICETY, and it is not a decorative div
    # either. A five-column table does not fit a 390px phone, and a scrollable
    # region reachable only by a finger is unreachable from a keyboard
    # (WCAG 2.1.1). The caption gives that focus stop something to announce, so
    # it does not arrive nameless; it is the block's own heading, sr-only,
    # because Design draws no caption and the heading already says what the
    # table is.
    cap_id = "%s-caption" % act_id
    table = (
        '<div class="ks3-rgrid-scroll" tabindex="0" role="group" '
        'aria-labelledby="%s"><table class="ks3-rgrid-table">'
        '<caption id="%s" class="ks3-sr-only">%s</caption>'
        '<thead><tr><th scope="col">%s</th>%s</tr></thead>'
        '<tbody>%s</tbody></table></div>'
        % (e(cap_id), e(cap_id), t(a.get("heading") or ""),
           t(a.get("column_head") or ""), heads, "".join(rows)))

    # ── the panel: sixteen setups, one predict row, sixteen results ───────
    setups = "".join(
        '<div class="ks3-rgrid-setup" data-rgrid-setup="%s"%s>'
        '<p class="ks3-rgrid-title">%s</p>'
        '<p class="ks3-rgrid-line">%s</p></div>'
        % (e(c["key"]), "" if c["key"] == open_key else " hidden",
           t(c["title"]), rich(c["setup"]))
        for c in cells)

    pred = a.get("predict") or {}
    pred_opts = pred.get("options") or []
    if len(pred_opts) != 2:
        raise ValueError(
            "reactivity-grid %r offers %d prediction(s). It is a choice of "
            "two — something happens or nothing does — and the blank half of "
            "the table is the whole reason there are exactly those two."
            % (act_id, len(pred_opts)))
    buttons = "".join(
        '<button type="button" class="ks3-seg-btn ks3-rgrid-opt" '
        'data-rgrid-opt="%s" aria-pressed="false">%s</button>'
        % (e(o.get("id", "")), t(o.get("label", "")))
        for o in pred_opts)
    predict = ('<div class="ks3-rgrid-predict" id="grid-predict" '
               'data-rgrid-predict><p class="ks3-rgrid-ask">%s</p>'
               '<div class="ks3-rgrid-opts">%s</div></div>'
               % (t(pred.get("prompt") or ""), buttons))

    results = []
    for c in cells:
        eq = ""
        if c["eq"]:
            eq = ('<p class="ks3-rgrid-eq"><span>%s</span>%s<span>%s</span></p>'
                  % (t(c["eq"][0]), _rgrid_arrow(), t(c["eq"][1])))
        results.append(
            '<div class="ks3-rgrid-result" data-rgrid-result="%s" hidden>'
            '<p class="ks3-rgrid-verdict">%s</p>'
            '<p class="ks3-rgrid-why">%s</p>%s</div>'
            % (e(c["key"]), t(c["result"]), rich(c["why"]), eq))

    pattern = _rgrid_pattern(a, act_id, metals)
    payoff = ('<div class="ks3-rgrid-pattern" data-rgrid-pattern hidden>'
              '<p class="ks3-rgrid-pattern-title">%s</p>'
              '<p class="ks3-rgrid-pattern-body">%s</p>'
              '<p class="ks3-rgrid-pattern-order">%s</p>'
              '<p class="ks3-rgrid-pattern-body">%s</p></div>'
              % (t(pattern["title"]), rich(pattern["shape"]),
                 t(pattern["order"]), rich(pattern["compare"])))

    # `data-cfg` carries NUMBERS and nothing else — the threshold the stop
    # ticks at, and the size of the grid. Not one sentence goes through it.
    cfg = _c5_cfg({"doneAt": done_at, "cells": total})
    return ('<div class="ks3-rgrid" data-rgrid data-cfg="%s">%s'
            '<div class="ks3-rgrid-panel">%s%s'
            '<div class="ks3-rgrid-results" id="grid-reveal">%s</div>'
            '</div>%s</div>'
            % (cfg, table, setups, predict, "".join(results), payoff))


# ═══ c5-04 · reactivity-use ══════════════════════════════════════════════

def r_reactivity_use(a, act_id):
    """⊕ c5-04 `#s-uses` — one rule, three places it decides the answer.

    Three cards, one commitment each, and the commitment is FINAL: the answer
    is on screen the instant the card is decided, so a second press would be a
    student choosing something they can already read. Both buttons disable and
    the one that was not pressed dims.

    ⚠️ TWO OPTIONS, AND THAT IS THE QUESTION. Yes or no on a real decision — a
    storage tank, a smelting process, an unknown metal — because the rule the
    lesson teaches gives exactly one of those two every time. There is no
    lettered list here and so no MRB-177 length gate to clear: the options are
    one word each.

    ⚠️ NOTHING HERE MARKS. `correct` reaches NO markup — not as a class, not as
    `data-correct`, not as anything — because R3 reserves marking for the
    mastery ladder. It is read ONCE, here, at build time, as a guard: the
    answer paragraph a student reads has to OPEN with the verdict the card was
    decided by, or the page is telling somebody they were wrong when they were
    right and nothing else in the build could see it. That is the same turn
    c4-01 makes with its unrendered `chemical` flag, and for the same reason —
    it makes an invisible key into a guard on the chemistry rather than dead
    correctness data.
    """
    uses = a.get("uses") or []
    options = a.get("options") or []
    if len(uses) < 2:
        raise ValueError(
            "reactivity-use %r declares %d card(s). The section's own heading "
            "is that ONE rule decides several different questions, and one "
            "card shows nothing of the sort." % (act_id, len(uses)))
    if len(options) != 2:
        raise ValueError(
            "reactivity-use %r offers %d option(s). Every card here is a yes "
            "or a no about a real decision, and a third option would be a "
            "different kind of question." % (act_id, len(options)))
    ids = {o.get("id") for o in options}

    cards = []
    for u in uses:
        for key in ("id", "q", "answer", "correct"):
            if not u.get(key):
                raise ValueError(
                    "reactivity-use %r card %r has no %r. The card opens on "
                    "the commitment and the answer is the whole of what opens."
                    % (act_id, u.get("id"), key))
        if u["correct"] not in ids:
            raise ValueError(
                "reactivity-use %r card %r marks %r correct and the buttons "
                "offer %s. The flag is the author's intent; it has to name one "
                "of the two things a student can actually press."
                % (act_id, u["id"], u["correct"], sorted(ids)))
        # ── THE CONTENT-TRUTH ASSERTION (§5A) ─────────────────────────────
        # The verdict and the prose have to agree. `correct` is invisible and
        # the answer is just a string, so nothing else in the build could catch
        # them disagreeing — and a card whose answer opens "No." while the
        # record says yes marks a right commitment wrong, silently.
        opening = u["answer"].strip().lower()
        if not opening.startswith(str(u["correct"]).lower()):
            raise ValueError(
                "reactivity-use %r card %r is flagged %r but its answer opens "
                "%r. The flag is what the record believes and the answer is "
                "what the student reads; when they disagree the page argues "
                "with itself in front of the student."
                % (act_id, u["id"], u["correct"], u["answer"][:40]))

        btns = "".join(
            '<button type="button" class="ks3-seg-btn ks3-ruse-opt" '
            'data-ruse-opt="%s" aria-pressed="false">%s</button>'
            % (e(o.get("id", "")), t(o.get("label", "")))
            for o in options)
        cards.append(
            '<div class="ks3-ruse-card" data-ruse-card="%s" data-open="0">'
            '<p class="ks3-ruse-q">%s</p>'
            '<div class="ks3-ruse-opts">%s</div>'
            '<p class="ks3-ruse-answer" data-ruse-answer hidden>%s</p></div>'
            % (e(u["id"]), rich(u["q"]), btns, rich(u["answer"])))

    return ('<div class="ks3-ruse" data-ruse data-total="%d">%s</div>'
            % (len(uses), "".join(cards)))


# ═══ c5-04 · the reactivity series (drawn figure, NOT an instrument) ══════

def _series_lines(text, per=15):
    """An authored caption, wrapped for the arrow column. Never re-worded.

    Design's two column captions sit in a 148px box and her CSS wraps them.
    SVG text does not wrap, so the words are broken across lines HERE — the
    string is the author's, unchanged, and only where the line ends is chosen.
    """
    lines, cur = [], ""
    for word in str(text).split():
        nxt = (cur + " " + word).strip()
        if cur and len(nxt) > per:
            lines.append(cur)
            cur = word
        else:
            cur = nxt
    if cur:
        lines.append(cur)
    return lines


def _reactivity_series(fig):
    """⊕ c5-04 — the reference plate, and the guard on everything below it.

    ⚖️ **IT IS A REFERENCE BLOCK, NOT AN INSTRUMENT.** It is absent from
    Design's own `RAIL` and NOTES-C5 §7 gives the reason in as many words: the
    rail ticks ACTIVITIES only, so a stop that could never tick is not added.
    Nothing here carries `data-stage-done`, nothing here is wired, and no
    family is registered for it.

    ⚖️ **THE DRAWING IS CHECKED AGAINST THE BENCH BELOW IT.** Mide ruled on
    18 Aug 2026 that the series is shown UP FRONT, before the grid — so the
    student now checks a published order against their own sixteen tubes. That
    only works if the two agree, and nothing else in the build compares them.
    This drawer walks EVERY row, not a sample, and refuses to draw:

      · a row missing its name or its symbol;
      · a `bench` mark naming a metal the grid does not have, or a grid metal
        the list does not mark;
      · a list whose bench metals do not fall in their `order` — the plate's
        own caption says "most reactive at the top", and a plate that
        contradicts the grid under it is worse than no plate at all;
      · a list that breaks any pair in `must_sit_above`. ⚑ That is science
        flag 17 as an assertion rather than a hope: `USES` item 2 and question
        `h01` both argue from carbon sitting between aluminium and iron, and if
        the list is ever edited so that it does not, the build stops here
        instead of shipping two paragraphs arguing from a drawing that
        contradicts them.

    ⚠️ The `<desc>` is COMPOSED HERE, from what was actually drawn, and
    overrides the record's short fallback (MRB-254): only the drawer knows the
    reading order, the marks and the numbering.
    """
    d = fig.get("data") or {}
    series = d.get("series") or []
    bench = d.get("bench") or []
    if len(series) < 3:
        raise ValueError(
            "reactivity-series figure %r declares %d row(s). It is a LIST — "
            "its whole content is that one thing sits above another — and two "
            "rows do not make an order." % (fig.get("id"), len(series)))

    at = {}
    for i, row in enumerate(series):
        for key in ("name", "symbol"):
            if not row.get(key):
                raise ValueError(
                    "reactivity-series figure %r row %d has no %r. Every row "
                    "is drawn as a number, a name and a symbol chip; a missing "
                    "one renders as an empty badge, which is the same hole as "
                    "`{brace}`." % (fig.get("id"), i + 1, key))
        if row["name"] in at:
            raise ValueError(
                "reactivity-series figure %r names %r twice. A substance in "
                "two places in an order has no place in it."
                % (fig.get("id"), row["name"]))
        at[row["name"]] = i

    # ── the bench marks, both directions ──────────────────────────────────
    marked = [r["name"] for r in series if r.get("bench")]
    want = [m["name"] for m in bench]
    if sorted(marked) != sorted(want):
        raise ValueError(
            "reactivity-series figure %r marks %s and the bench below it uses "
            "%s. The plate says 'the four metals on the bench are marked', and "
            "a mark that names a metal the grid never uses — or a grid metal "
            "the plate leaves plain — makes that sentence false about its own "
            "drawing." % (fig.get("id"), marked, want))

    # ── and the order they are marked in IS the order the grid claims ─────
    ranked = sorted(bench, key=lambda m: m["order"])
    drawn = sorted(want, key=lambda name: at[name])
    if drawn != [m["name"] for m in ranked]:
        raise ValueError(
            "reactivity-series figure %r draws the bench metals as %s, and "
            "their `order` in the grid ranks them %s. The plate's caption says "
            "most reactive at the top, so these two ARE the same claim, and "
            "the sixteen tubes below would be contradicting the list above "
            "them." % (fig.get("id"), drawn, [m["name"] for m in ranked]))

    for above, below in (d.get("must_sit_above") or []):
        if above not in at or below not in at:
            raise ValueError(
                "reactivity-series figure %r asserts %r above %r and one of "
                "them is not in the list at all."
                % (fig.get("id"), above, below))
        if at[above] >= at[below]:
            raise ValueError(
                "reactivity-series figure %r draws %r at position %d and %r at "
                "%d, and the page argues from %r being the more reactive of "
                "the two. Correct the list or drop the argument; do not ship "
                "both." % (fig.get("id"), above, at[above] + 1, below,
                           at[below] + 1, above))

    # ── geometry ──────────────────────────────────────────────────────────
    #
    # One row is 44 units on a 49 pitch, so the drawn positions run strictly
    # DOWN the plate in the same sequence as the list — which is the geometry
    # expressing the claim its caption makes, not merely accompanying it.
    top, pitch, row_h = 12, 49, 44
    width = 660
    height = top + pitch * len(series) - (pitch - row_h) + 15
    note = d.get("note") or ""
    out = [_svg_open(dict(fig, desc=_series_desc(fig, series, bench, d)),
                     width, height)]

    for i, row in enumerate(series):
        y = top + pitch * i
        is_bench = bool(row.get("bench"))
        is_non = bool(row.get("non_metal"))
        ground = (_SVG_ACCENT_TINT if is_bench
                  else _SVG_BAND if is_non else _SVG_INSET)
        edge = _SVG_ACCENT if is_bench else _SVG_RULE
        name_fill = _SVG_ACCENT_TEXT if is_non else _SVG_INK
        out.append(_rect(10, y, 490, row_h, rx=12, fill=ground, stroke=edge,
                         w=2, data_row=row["name"].lower()))
        out.append(_mono(30, y + 29, str(i + 1), size=14, anchor="middle"))
        out.append(_label(52, y + 29, row["name"], size=20,
                          weight="800" if is_bench else "700",
                          anchor="start", family=_SVG_DISPLAY, fill=name_fill))
        if is_non and note:
            # Design sets this in uppercase from CSS; SVG has no
            # `text-transform`, so the case is applied here. The authored
            # lowercase form is what the <desc> uses.
            out.append(_mono(420, y + 28, note.upper(), size=13, anchor="end",
                             fill=_SVG_ACCENT_TEXT, spacing=".05em"))
        out.append(_rect(432, y + 8, 56, 28, rx=8, fill=_SVG_CARD,
                         stroke=_SVG_RULE, w=1))
        out.append(_mono(460, y + 27, row["symbol"], size=15, weight="600",
                         anchor="middle",
                         fill=_SVG_ACCENT_TEXT if is_non else _SVG_INK))

    # ── the arrow column ──────────────────────────────────────────────────
    #
    # Design draws a bar with a head at BOTH ends — up at the top, down at the
    # bottom — because it marks the two ends of a range rather than pointing
    # one way. Redrawn, not retyped, and the two captions are her words with
    # only the line breaks chosen here.
    cx, a_top, a_bot = 580, 84, 522
    lines = _series_lines(d.get("top") or "")
    for j, line in enumerate(lines):
        out.append(_mono(cx, 30 + 18 * j, line, size=13, anchor="middle",
                         spacing=".06em"))
    out.append(_path("M%d %d L%d %d L%d %d Z"
                     % (cx, a_top, cx + 12, a_top + 17, cx - 12, a_top + 17),
                     fill=_SVG_ACCENT))
    out.append(_rect(cx - 5, a_top + 17, 10, a_bot - a_top - 34,
                     fill=_SVG_ACCENT))
    out.append(_path("M%d %d L%d %d L%d %d Z"
                     % (cx, a_bot, cx - 12, a_bot - 17, cx + 12, a_bot - 17),
                     fill=_SVG_ACCENT))
    for j, line in enumerate(_series_lines(d.get("bottom") or "")):
        out.append(_mono(cx, 556 + 18 * j, line, size=13, anchor="middle",
                         spacing=".06em"))

    out.append("</svg>")
    return "".join(out)


def _series_desc(fig, series, bench, d):
    """The description a reader who cannot see the plate gets, walked in
    reading order and built from what is actually drawn (MRB-254)."""
    rows = ", ".join("%d %s (%s)%s"
                     % (i + 1, r["name"].lower(), r["symbol"],
                        ", %s" % (d.get("note") or "") if r.get("non_metal")
                        else "")
                     for i, r in enumerate(series))
    names = [m["name"].lower() for m in sorted(bench, key=lambda x: x["order"])]
    marked = ", ".join(names[:-1]) + " and " + names[-1] if len(names) > 1 \
        else (names[0] if names else "")
    return ("A numbered list of %s substances in order of reactivity, drawn "
            "from the most reactive at the top to the least reactive at the "
            "bottom: %s. Highlighted on the list are %s, the metals used on "
            "the bench in this lesson. A bar beside the list carries an "
            "arrowhead at each end, labelled “%s” and “%s”."
            % (_rgrid_word(len(series)), rows, marked,
               d.get("top") or "", d.get("bottom") or ""))


# The five registration rows this fragment needs, and nothing else.
#
# ⊖ NO `KIND_HEAD_TOTAL` ROW. The grid's denominator is authored in the lesson
# record and checked by `r_reactivity_grid`, for the reason written beside it
# there: the shell draws the counter before this renderer runs, so a derivation
# would put the number where the instrument's own guard cannot see it, and a
# derivation that is simply never spliced ships "0 of 0 run" in silence.
#
# ⊖ AND `#s-series` APPEARS IN NONE OF THEM. It is a `figure` block placed by
# the lesson record — no family, no shell, no wiring, no rail stop — so its
# only registration in the whole system is the drawer row at the top.





# REGISTER SEGMENT: 'reactivity-grid': "check",   (already in ks3_data/c5/__init__.py)
# REGISTER SEGMENT: 'reactivity-use': "check",    (already in ks3_data/c5/__init__.py)


# ── from art_05.py ─────────────────────────────────────
# ═══ c5-05 · type-sorter, rule-write ═════════════════════════════════════
#
# The unit's assessment in disguise. Two families, both DOM, no canvas, and no
# drawn figure — deliberately: this lesson's whole claim is that what a
# reaction LOOKS like is not what names it, so a diagram here would be the
# drama the page is arguing against. Eight reactions in words, with the same
# five buttons under every one.
#
# Both sit in a LIGHT `ks3-block` (measured off Design's own markup: `#s-sort`
# and `#s-rule` carry `class="ks3-block"` and nothing else), both tick a rail
# stop, so both ship `data-stage-done="0"` and NOTHING is ticked on load
# (MRB-208). `data-instrument` keeps the shell's `wirePredictions` out of the
# options inside them.
#
# ⚠️ ONLY THE LADDER MARKS. Neither family emits `data-correct`, and nothing
# green or red reaches any control in either of them. A committed reaction
# keeps the ordinary pressed treatment and its four spent siblings dim; the
# answer is a PANEL OF WORDS, in the same voice whichever button was pressed.


def _tsort_seg(label, index):
    """One of the five type buttons.

    `.ks3-seg-btn` is the key stage's ONE segmented control (the Drift-4
    ruling), with a family class beside it for layout. `aria-pressed` is a
    WORD, not colour alone (R2).

    ⚠️ `data-tsort-opt` is the button's INDEX INTO `options`, exactly as
    `data-cpair-opt` is — never the type id it names, and never anything the
    card's own answer could be recovered from. There is no `correct`
    parameter here and there must never be one (R3).
    """
    return ('<button type="button" class="ks3-seg-btn ks3-tsort-opt" '
            'data-tsort-opt="%s" aria-pressed="false">%s</button>'
            % (e(str(index)), t(label)))


def r_type_sorter(a, act_id):
    """⊕ c5-05 `#s-sort` — eight reactions, five buttons, one question.

    ⚖️ **THE SHARED OPTION LIST IS THE INSTRUMENT.** NOTES-C5 §2: four
    PROCESS lessons teach the four types one at a time, and "naming four types
    is not the same as telling them apart". So all five buttons stand under
    every reaction from the first card, including "None of the four" — a fifth
    button produced only at the eighth reaction would have told the student the
    answer through the interface. It is offered eight times and is right once.

    ⚖️ ONE COMMITMENT PER REACTION AND IT IS FINAL. All five buttons disable
    when any one is pressed — not to punish a change of mind, but because the
    answer is on screen by then and a second press would be a student choosing
    something they can already read. Design's own click guard does the same
    (page line 480): the handler re-checks `st.picks` and returns null.

    ⚠️ `type` IS IN THE PAYLOAD AND IS EMITTED NOWHERE. It is the authored
    classification of each reaction and it is THE ANSWER; putting it in the
    document — as `data-correct`, as a class, as the value of a button — would
    let the page mark a commitment, and R3 reserves marking for the mastery
    ladder alone. The reveal panel carries the answer in words, after the
    commitment, and that is the only route it takes.

    ── THE CONTENT-TRUTH ASSERTIONS (§5A), AND WHAT `type` IS FOR ─────────

    Read HERE, at build time, so `type` is a guard on the chemistry rather
    than dead correctness data. All four walk EVERY reaction and EVERY option,
    not a sample:

      1. EVERY BUTTON IS SOMEBODY'S ANSWER. If any of the five were never the
         answer to any reaction, it would be a button on screen eight times
         that nothing on the page ever justifies — which is what a trick
         option is, and this lesson's fifth button is the opposite of one.
      2. EXACTLY ONE REACTION ANSWERS "none", AND IT IS THE LAST. The lede
         above the cards says "the eighth is not any of the four". A payload
         edit that moved it, dropped it or added a second would leave that
         sentence on the page saying something false about the cards under it.
      3. THE FLAG AND THE ANSWER LINE AGREE. `type` is what the author meant;
         `answer` is what the student reads. If those disagree the page tells
         a student they were wrong when they were right, and nothing else in
         the build could see it — the flag is invisible and the answer is just
         a string.
      4. THE COUNTER'S DENOMINATOR IS THE NUMBER OF REACTIONS. `setCount`
         clamps to `data-total`, so a head row promising eight where there are
         nine sticks at "8 of 8 named" for ever while a card sits undecided.

    IDS EMITTED, and they are a contract with the misconception register
    (MRB-244/248): none. `REACT-18` is elicited and confronted in `#s-think`,
    which is the shell's own activity — see the lesson record. This instrument
    names no register entry and emits no join target.

    HOOKS: `data-tsort` (wrapper, with `data-total`) · `data-tsort-card` (one
    reaction, valued with its id) · `data-tsort-opt` (a type button, valued
    0–4 to index `options`) · `data-tsort-reveal` · `data-tsort-close`. The
    head tally is the SHELL's `[data-count]`, rendered by `_head_counter` from
    `head_counter`.
    """
    reactions = a.get("reactions") or []
    options = a.get("options") or []
    if not reactions:
        raise ValueError("type-sorter %r declares no reactions[]." % act_id)
    if len(options) < 3:
        raise ValueError(
            "type-sorter %r offers %d option(s). The whole lesson is a choice "
            "between the four named types and the honest fifth answer, and a "
            "shorter list is a different lesson." % (act_id, len(options)))

    labels = {}
    for o in options:
        if not o.get("id") or not o.get("label"):
            raise ValueError(
                "type-sorter %r has an option with no id or no label: %r. The "
                "id is what every reaction's `type` names and the label is "
                "what the student reads." % (act_id, o))
        labels[o["id"]] = o["label"]

    # ── assertion 4 — the head row's denominator ────────────────────────
    hc = a.get("head_counter") or {}
    if hc.get("total") is not None and int(hc["total"]) != len(reactions):
        raise ValueError(
            "type-sorter %r draws %d reaction(s) under a head counter that "
            "says %s. `setCount` clamps to the denominator, so the readout "
            "would stop moving while a card was still undecided — and the "
            "rail stop that ticks with it would still be right, which is what "
            "makes it invisible."
            % (act_id, len(reactions), hc["total"]))

    seen = []
    for r in reactions:
        for key in ("id", "type", "level", "text", "answer", "why"):
            if not r.get(key):
                raise ValueError(
                    "type-sorter %r reaction %r has no %r. Every card opens "
                    "an answer the instant it is decided; a card with nothing "
                    "to reveal is a commitment that goes nowhere."
                    % (act_id, r.get("id"), key))
        if r["type"] not in labels:
            raise ValueError(
                "type-sorter %r reaction %r is classified %r, and no button "
                "on the card offers it. The student would be asked to name a "
                "type they cannot pick."
                % (act_id, r.get("id"), r["type"]))
        # ── assertion 3 — the flag and the sentence say the same thing ──
        want = labels[r["type"]]
        if not r["answer"].strip().startswith(want):
            raise ValueError(
                "type-sorter %r reaction %r is flagged %r but its answer line "
                "opens %r. The flag is the author's intent and the answer is "
                "what the student reads; when they disagree the page marks a "
                "correct commitment wrong."
                % (act_id, r.get("id"), want, r["answer"]))
        seen.append(r["type"])

    # ── assertion 1 — every button is somebody's answer ─────────────────
    unused = [o["id"] for o in options if o["id"] not in seen]
    if unused:
        raise ValueError(
            "type-sorter %r offers %s under every reaction and no reaction "
            "answers %s. A button that is never right is a button a student "
            "learns to ignore, and the fifth one here is the opposite of a "
            "trick — it is the lesson."
            % (act_id, ", ".join(sorted(labels[u] for u in unused)),
               "it" if len(unused) == 1 else "them"))

    # ── assertion 2 — one edge case, and it is the last one ─────────────
    edges = [i for i, r in enumerate(reactions) if r["type"] == "none"]
    if len(edges) != 1 or edges[0] != len(reactions) - 1:
        raise ValueError(
            "type-sorter %r has %d reaction(s) answering \"none of the four\" "
            "at position(s) %s. The lede above the cards says the EIGHTH is "
            "not any of the four, and it is a sentence about these cards "
            "rather than a general remark."
            % (act_id, len(edges), [i + 1 for i in edges]))

    label_tpl = a.get("reaction_label") or "Reaction {n}"
    cards = []
    for i, r in enumerate(reactions):
        btns = "".join(_tsort_seg(o["label"], j)
                       for j, o in enumerate(options))
        cards.append(
            '<div class="ks3-tsort-card" data-tsort-card="%s">'
            '<div class="ks3-tsort-head">'
            '<p class="ks3-tsort-num">%s</p>'
            '<p class="ks3-tsort-level">%s</p></div>'
            '<p class="ks3-tsort-text">%s</p>'
            '<div class="ks3-tsort-opts">%s</div>'
            '<div class="ks3-tsort-reveal" hidden data-tsort-reveal>'
            '<p class="ks3-tsort-answer">%s</p>'
            '<p class="ks3-tsort-why">%s</p></div></div>'
            % (e(r["id"]),
               t(label_tpl.replace("{n}", str(i + 1))),
               t(r["level"]), rich(r["text"]), btns,
               t(r["answer"]), rich(r["why"])))

    # ⚠️ The closing panel is INSIDE the wrapper, not a sibling of it.
    # `c3CommitCards` resolves `sel.close` with `wrap.querySelector(...)`, so
    # a panel outside `[data-tsort]` is a panel that never opens — and it
    # would fail silently, because all eight cards would still work.
    close = ('<div class="ks3-tsort-close" hidden data-tsort-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""
    return ('<div class="ks3-tsort" data-tsort data-total="%d">'
            '<div class="ks3-tsort-list">%s</div>%s</div>'
            % (len(reactions), "".join(cards), close))


# ═══ c5-05 · rule-write ══════════════════════════════════════════════════

def r_rule_write(a, act_id):
    """⊕ c5-05 `#s-rule` — write the four rules, then read four to compare.

    ⚖️ THE ONE ACTIVITY ON THE PAGE THAT NOTHING MARKS, and that is the point
    of it: a CLASSIFY lesson ends with the rule stated in the student's own
    words, and a rule you can only recognise is not a rule you have. The
    panel underneath is offered as a COMPARISON, never as the answer — the
    closing line says so, and it says the student's worse English is the more
    useful version.

    ⚖️ **THE SIXTY-CHARACTER UNLOCK, AND NO COPY ABOUT IT.** The button ships
    `disabled` and `shared/ks3.js` releases it once the box holds 60
    characters — the engine's own number, settled across 58 live lessons
    (Mide's ruling, 19 Aug 2026, R8's missing half). Nothing reads what was
    written: no keywords, no parsing, no judgement. It is the COMMITMENT that
    is required, not the correctness, because a model answer that arrives
    before a word has been typed IS the answer.

    ⚠️ §8.10 — NO "write at least 60 characters", no counter, no nag. The
    control is simply not active yet and looks the way an inactive control
    looks. `.ks3-check-btn[disabled]` already carries that treatment, measured
    (`--ks3-dim-spent`, hover cancelled), so nothing is drawn here for it.

    ⚠️ IT SHIPS DISABLED IN THE RESTING DOM rather than being disabled by JS
    on load — the engine's own self-marked rung does exactly this, for exactly
    this reason: the attribute in the bytes means the control is never briefly
    live in the window while a deferred script is still arriving.

    ⚠️ THE SHARED FIELD CLASSES ARE REUSED AND THE SHARED HOOKS ARE NOT.
    `.ks3-answer-label`, `.ks3-answer` and `.ks3-check-btn` are the key
    stage's one written-answer control and this is that control, so it takes
    them and adds no fourth copy of the same box. But the ladder's `data-answer`
    and `data-check` are NOT reused: `wireSelf` walks `.ks3-rung` inside the
    ladder section, and a shared hook is how one instrument ends up wired to
    another's handler (the `data-critique` / `data-critiq` trap).

    HOOKS: `data-rwrite` (wrapper) · `data-rwrite-field` (the textarea) ·
    `data-rwrite-show` (the button) · `data-rwrite-reveal`.
    """
    model = a.get("model") or []
    if not model:
        raise ValueError(
            "rule-write %r offers no model[] to compare with. The button "
            "promises a version to compare with, and a panel that opens on "
            "nothing is a promise the block does not keep." % act_id)
    if not a.get("button"):
        raise ValueError(
            "rule-write %r has no `button` label. The control is the only "
            "thing between a written answer and the comparison, and an "
            "unlabelled button says nothing about what pressing it does."
            % act_id)

    fid = "%s-field" % act_id
    items = "".join('<li class="ks3-rwrite-item">%s</li>' % rich(m)
                    for m in model)
    close = ('<p class="ks3-rwrite-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")
    return ('<div class="ks3-rwrite" data-rwrite>'
            '<label class="ks3-answer-label" for="%s">%s</label>'
            '<textarea class="ks3-answer" id="%s" rows="6" data-rwrite-field'
            '%s></textarea>'
            '<button type="button" class="ks3-check-btn" data-rwrite-show '
            'aria-expanded="false" disabled>%s</button>'
            '<div class="ks3-rwrite-reveal" hidden data-rwrite-reveal>'
            '<ul class="ks3-rwrite-list" role="list">%s</ul>'
            '%s</div></div>'
            % (e(fid), t(a.get("field_label") or "Write your answer"),
               e(fid),
               (' placeholder="%s"' % e(a["placeholder"])
                if a.get("placeholder") else ""),
               t(a["button"]), items, close))


# ── registrations for the commander to splice ────────────────────────────
#
# No drawer: this lesson declares no figures, so there is no ART row. Both
# families sit in a LIGHT `ks3-block` — measured off Design's own markup, and
# there is no ink-dark practical block anywhere in C4 or C5 — so both take the
# `check` segment. Neither is a confrontation, so neither takes amber:
# `#s-think` is the shell's own `misconception` block and is authored in
# `activities[]`, not here.
#





# REGISTER SEGMENT: 'type-sorter': "check",
# REGISTER SEGMENT: 'rule-write': "check",


ART = {
    'reactivity-series': _reactivity_series,
}

KIND_SHELL = {
    'burner-bench': ("ks3-burner-block", ' data-instrument data-burnerblock data-stage-done="0"'),
    'fuel-cards': ("ks3-fcard-block", ' data-instrument data-fcardblock data-stage-done="0"'),
    'tube-run': ("ks3-tuber-block", ' data-instrument data-tuberblock data-stage-done="0"'),
    'decomp-sort': ("ks3-dcomp-block", ' data-instrument data-dcompblock data-stage-done="0"'),
    'control-tubes': ("ks3-ctube-block", ' data-instrument data-ctubeblock data-stage-done="0"'),
    'rust-stop': ("ks3-rstop-block", ' data-instrument data-rstopblock data-stage-done="0"'),
    'reactivity-grid': ("ks3-rgrid-block", ' data-instrument data-rgridblock data-stage-done="0"'),
    'reactivity-use': ("ks3-ruse-block", ' data-instrument data-ruseblock data-stage-done="0"'),
    'type-sorter': ("ks3-tsort-block", ' data-instrument data-tsortblock data-stage-done="0"'),
    'rule-write': ("ks3-rwrite-block", ' data-instrument data-rwriteblock data-stage-done="0"'),
}

KIND_FN = {
    'burner-bench': r_burner_bench,
    'fuel-cards': r_fuel_cards,
    'tube-run': r_tube_run,
    'decomp-sort': r_decomp_sort,
    'control-tubes': r_control_tubes,
    'rust-stop': r_rust_stop,
    'reactivity-grid': r_reactivity_grid,
    'reactivity-use': r_reactivity_use,
    'type-sorter': r_type_sorter,
    'rule-write': r_rule_write,
}
