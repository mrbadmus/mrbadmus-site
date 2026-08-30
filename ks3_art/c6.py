"""ks3_art.c6 — C6's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may be
added to any other unit's module. C6 is *Acids and alkalis*: seven authored
lessons, ten instrument families and one drawn figure, all DOM, no canvas
anywhere in the unit.

⊕ MRB-281, 23 Aug 2026. This used to read "six authored lessons, eight
instrument families". `acids-and-carbonates` was built into the renamed fifth
slot and brought `step-rig` and `solid-sorter` with it — see
`ks3_data/c6/lesson_05_acids_and_carbonates.py` for the ruling, and the
registrations block at the foot of this file for why the comment there that
said those two families would never be registered is now rewritten.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY, on the same two conventions C5 established and for the same
reasons:

  · EMIT-BOTH-SHOW-ONE wherever a panel has a small closed set of states.
    Every state's text is in the document and one is shown, so ``<strong>``,
    an em dash and a degree sign survive exactly as the author wrote them, no
    sentence exists twice, and the resting render cannot disagree with the
    runtime one.
  · A JSON ``data-cfg`` ONLY for what genuinely has to be recomputed — a
    number, a colour, a geometry. Never for a sentence.

Design's C6 pages compose a great deal in ``lessonVals()`` — c6-04 builds every
cell's explanation out of the metal's name and the acid's salt ending, c6-06
builds twelve salt names out of ``base.metal + acid.ending``, and c6-02 builds
its verdict out of a chain of ternaries on the pH. **None of that composition
is reproduced.** Every one of those states is enumerated in the lesson record
and CHECKED here against the rule it was generated from, so the sentence a
student reads is an authored sentence and the rule that generated it is an
assertion rather than a hope.

═══════════════════════════════════════════════════════════════════════════
THE HOOKS ARE AN INTERFACE
═══════════════════════════════════════════════════════════════════════════

Every ``data-`` attribute emitted below is named systematically off the
family's short prefix and is the contract ``shared/ks3.js`` binds against.
Renaming one here without renaming it there is a silent dead instrument.

    bottle-sorter      bottle     acid-judgements    ajudge
    ph-bench           phbench    titration-dial     titr
    acid-metal-grid    amgrid     salt-namer         namer
    method-order       morder     catalyst-bench     catb
    step-rig           srig       solid-sorter       solid

All ten family names, all ten shell classes and all ten prefixes were
grepped across ``ks3_art/*.py``, ``shared/ks3.js`` and ``shared/ks3.css``
before a line was written, and every one was free. ⚠️ ``acid-metal-grid`` is
NOT ``reactivity-grid``: Design's NOTES-C6 §4 reuses C5-04's name, and
``ks3_art/c5.py`` already owns it together with ``ks3-rgrid-block``. Same
shape, own family — see MRB-279's shell-class gate, which exists precisely
because two families wearing one class fails silently.

═══════════════════════════════════════════════════════════════════════════
THE RULES THAT BIND THEM ALL
═══════════════════════════════════════════════════════════════════════════

  · Every C6 instrument sits in a LIGHT ``ks3-block``. Measured off Design's
    own markup: `#s-bench`, `#s-hazard`, `#s-scale`, `#s-choose`, `#s-titrate`,
    `#s-uses`, `#s-test`, `#s-name`, `#s-method` are each ``class="ks3-block"``
    and nothing else. There is no ink-dark practical block anywhere in C6,
    exactly as there is none in C3, C4 or C5.
  · ONLY THE LADDER MARKS. Nothing green and nothing red reaches any control
    in any of these families. A verdict panel says in words what is true; the
    chosen option keeps the ordinary chosen treatment and the unchosen ones
    dim. No ``data-correct`` on any activity option, ever.

    ⚑ THIS IS THE ONE PLACE C6 REFINES DESIGN'S DRAWING, and it is worth
    stating because it looks like a subtraction. c6-01's bench composes its
    verdict headline as ``chosen === row.answer ? 'You said ' + chosen + ' —
    that is what it is.' : 'It is ' + row.answer + '.'`` — a MARK, assembled
    in JavaScript, in two voices. The refinement is inside the shape she drew
    (a card, a commitment, a two-paragraph reveal): the headline becomes one
    authored sentence naming what the bottle IS, the same sentence whichever
    button was pressed. The `answer` key stays in the payload and is read
    HERE, at build time, so keeping it on the record cannot quietly mean
    keeping it wrong.
  · Every family here ticks a rail stop, so every family carries
    ``data-stage-done="0"``. NOTHING IS TICKED ON LOAD (MRB-208).
  · Author text reaches the page through ``e()`` / ``t()`` / ``rich()``.
    ``e()`` for attribute values — it is the only one safe there, because
    ``t()`` can emit an SVG mark carrying double quotes — ``rich()`` for
    prose, ``t()`` for labels.
  · Arrows inside an equation are DRAWN AS SVG, never the character U+2192.
    The shipped font subsets do not contain it. Typed arrows are prose only.

═══════════════════════════════════════════════════════════════════════════
CONTAINMENT, NOT CLIPPING — AND WHY NOTHING HERE IS ABSOLUTELY POSITIONED
═══════════════════════════════════════════════════════════════════════════

C5 shipped 65 visually-hidden screen-reader labels inside a horizontal
scroller and widened the page by 140px at 390px, because an absolutely
positioned child escapes a scroller that is not itself ``position: relative``
and ``overflow: hidden`` does not fix it.

C6 has two sections of exactly that shape — c6-04's 4x2 grid, which scrolls
sideways, and c6-02's fifteen-cell pH strip. Neither contains a single
absolutely positioned element:

  · THE GRID'S ACCESSIBLE NAME IS AN ``aria-label`` ATTRIBUTE, not a hidden
    span. An attribute has no box and cannot escape anything.
  · THE pH STRIP IS A DRAWN SVG FIGURE rather than fifteen flex divs. It goes
    through ``.ks3-figure-scroll``, which the platform already sizes, measures
    and fades, and an SVG's children are inside its own viewBox by
    construction.

The stylesheet still declares ``position: relative`` on the grid's scroller,
as a belt: the day someone adds a hidden label to a cell, it is contained.
"""

import json
import re

from ks3_art.kit import (
    _SVG_INK,
    _SVG_INK_MUTED,
    _label,
    _mono,
    _rect,
    _svg_open,
    e,
    rich,
    t,
)


# ═══════════════════════════════════════════════════════════════════════════
# THE pH COLOUR RAMP — FIFTEEN LITERAL HEX VALUES, AND THE REASON
# ═══════════════════════════════════════════════════════════════════════════
#
# ⚑ NOTES-C6 §7 flags this as the only non-token colour in C1–C8 and asks for
# a ruling. RULED AND KEPT, and the reason is written here rather than in a
# commit message because this is the file a future tidy-up would open:
#
#   THESE ARE SCIENTIFIC DATA, NOT BRAND COLOUR. The ramp is the printed
#   universal-indicator chart. A student holds a wet strip against a picture
#   of it and reads a number off the match, so the fifteen values ARE the
#   instrument — they are no more substitutable for `--ks3-accent` and
#   `--ks3-data` than the numbers 0 to 14 are. Routing them through brand
#   tokens would make the chart wrong in order to make the palette tidy.
#
# ⚠️ AND THEREFORE: IDENTITY IS NEVER HUE-ONLY. Every cell of the strip and
# every reading the bench prints carries its NUMBER, in text, beside or on the
# colour — `_ph_strip` refuses to draw a cell without one and `r_ph_bench`
# refuses a sample whose chip does not print its pH. A colour-blind student
# reads exactly the same instrument, which is also what the lesson's own prose
# says: "the numbers matter more than the colours".
#
# Byte-identical to Design's `PH_COLOURS` in c6-02 and c6-03. Index IS the pH.
PH_COLOURS = [
    "#C1272D", "#D2382B", "#E04A22", "#EA6A1E", "#EE8C1B",
    "#EFB120", "#D7CA2A", "#4FA352", "#3E9C86", "#2F8DA8",
    "#2A6FA8", "#2E4E96", "#453C8E", "#553191", "#5E2483",
]

# The ink the numbers take ON the ramp. Design's own `#FFFDF8`, and it is not
# a brand token for the same reason the ramp is not: it is the one near-white
# that stays legible on all fifteen, including the yellow at pH 6.
PH_ON_COLOUR = "#FFFDF8"


def _c6_arrow(cls):
    """Design's equation arrow, DRAWN, with its spoken word beside it.

    ⚠️ Never the character U+2192. The shipped font subsets do not contain it,
    so a typed arrow drops to a system font mid-line inside a display row.
    Geometry is Design's own, unchanged from `c4-05` and reused verbatim in
    every C6 formula line she draws: viewBox `0 0 44 24`,
    `M4 12h30M26 5l8 7-8 7`, 2.6px stroke, round caps and joins, on
    `currentColor` so it inherits the ink or the on-dark of whatever panel it
    lands in.

    The spoken equivalent is "makes", which is the reading C4 gave it and the
    word Design's own key facts and rung questions use in prose.
    """
    return ('<svg class="%s" viewBox="0 0 44 24" width="44" height="24" '
            'aria-hidden="true">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" '
            'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>'
            '<span class="ks3-visually-hidden">makes</span>' % e(cls))


def _c6_seg(cls, pressed, label, **attrs):
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


def _c6_need(a, act_id, kind, keys, why):
    """Every one of `keys` present on `a`, or a build error naming the gap."""
    for key in keys:
        if not a.get(key):
            raise ValueError("%s %r has no %r. %s" % (kind, act_id, key, why))


# ═══ c6-01 · bottle-sorter (#s-bench) ═════════════════════════════════════

def r_bottle_sorter(a, act_id):
    """⊕ c6-01 `#s-bench` — eight bottles, three answers, one reveal each.

    ⚖️ **THE PAYOFF IS THAT THE MOST DANGEROUS BOTTLE IS AN ALKALI**, and the
    bench is built to produce it rather than to assert it. Eight bottles, four
    of them things a student eats or drinks, and the where-it-lives tag on each
    is doing real work: the acids turn up in the food cupboard and the stomach,
    the alkalis in the cleaning cupboard and the shed. The closing panel is the
    only place the point is stated, and it only opens when all eight are
    decided, because seven bottles cannot show a distribution.

    ⚖️ ONE COMMITMENT PER BOTTLE AND IT IS FINAL — `c3CommitCards`' contract,
    the same one the purity sorter, the fuel cards and c5-02's sorter take. The
    reply is on screen the instant the bottle is decided, so a second press
    would be a student choosing an answer they can already read.

    ⚠️ NOTHING HERE MARKS, AND THE VERDICT IS ONE SENTENCE. Design's page
    composes `'You said ' + chosen + ' — that is what it is.'` against
    `'It is ' + row.answer + '.'`; that is a mark, in two voices, assembled in
    JavaScript. The refinement is inside her shape: `verdict` is one authored
    sentence naming what the bottle IS, identical whichever button was pressed,
    and `why` is her paragraph unchanged underneath it. See the module header.

    ⚠️ `answer` IS EMITTED NOWHERE AND IS READ HERE, WALKING EVERY BOTTLE.
    Two assertions, both content-truth (§5A):

      1. Every bottle's `answer` names one of the options actually offered. An
         answer outside the option set is a record that has stopped describing
         its own page.
      2. Every bottle's `verdict` NAMES that answer. The flag is the author's
         intent and the verdict is what the student reads; when they disagree
         the page tells a student the wrong thing and nothing else in the build
         could see it, because the flag reaches no markup and the verdict is
         just a string.

    And one about the SET rather than an item: every option offered must be the
    answer to at least one bottle. A third button nothing is ever an example of
    is a control that does nothing, and on this bench "neutral" is the one a
    lazy set would drop.

    ⚠️ THE RESTING RENDER: eight bottles, nothing pressed, no reveal open, the
    closing panel hidden, the head counter reading zero, `data-stage-done="0"`.

    HOOKS: `data-bottle` (wrapper, with `data-total`) · `data-bottle-card` (a
    bottle, valued with its id, carrying `data-open`) · `data-bottle-opt`
    (valued with the option id) · `data-bottle-reveal` · `data-bottle-close`.
    """
    options = a.get("options") or []
    bottles = a.get("bottles") or []
    pattern = a.get("pattern") or {}

    if len(options) < 3:
        raise ValueError(
            "bottle-sorter %r offers %d option(s). The bench sorts into acid, "
            "alkali and NEUTRAL, and the third is the one that stops the page "
            "reading as a binary — pure water and salt solution are on it for "
            "exactly that reason." % (act_id, len(options)))
    if len(bottles) < 6:
        raise ValueError(
            "bottle-sorter %r declares %d bottle(s). The closing panel claims "
            "a distribution — acids in the food cupboard, alkalis in the "
            "cleaning cupboard — and a handful of bottles cannot show one."
            % (act_id, len(bottles)))
    if not pattern.get("id") or not pattern.get("text"):
        raise ValueError(
            "bottle-sorter %r has no closing panel with an `id` and a `text`. "
            "The panel is where the lesson's claim is made, and its id is a "
            "misconception join (MRB-244/248), so neither may be composed "
            "here." % act_id)

    option_ids = [o["id"] for o in options]
    labels = dict((o["id"], str(o.get("label", ""))) for o in options)
    seen_ids, answered = set(), set()
    for b in bottles:
        _c6_need(b, b.get("id"), "bottle-sorter bottle",
                 ("id", "name", "where", "answer", "verdict", "why"),
                 "A bottle is a name, a place it lives, a commitment and a "
                 "reply; a bottle missing any of them opens on nothing.")
        if b["id"] in seen_ids:
            raise ValueError(
                "bottle-sorter %r authors bottle id %r twice. Two bottles "
                "with one name is one unreachable bottle." % (act_id, b["id"]))
        seen_ids.add(b["id"])
        if b["answer"] not in option_ids:
            raise ValueError(
                "bottle-sorter %r bottle %r answers %r, which is not one of "
                "the options %r. The record has to know which answer is right "
                "even though the markup never says."
                % (act_id, b["id"], b["answer"], option_ids))
        answered.add(b["answer"])
        # ── THE CONTENT-TRUTH ASSERTION, WALKING EVERY BOTTLE ─────────────
        word = labels[b["answer"]].lower()
        if word not in str(b["verdict"]).lower():
            raise ValueError(
                "bottle-sorter %r bottle %r is flagged %r but its verdict "
                "reads %r, which never says the word. The flag is the "
                "author's intent and the verdict is what the student reads; "
                "when they disagree the page states the wrong classification "
                "and nothing else in the build can see it."
                % (act_id, b["id"], word, b["verdict"]))

    missing = [i for i in option_ids if i not in answered]
    if missing:
        raise ValueError(
            "bottle-sorter %r offers option(s) %s that no bottle is an "
            "example of. A button that is never the answer is a control that "
            "does nothing, and it is learnable in one lesson."
            % (act_id, missing))

    cards = []
    for b in bottles:
        buttons = "".join(
            _c6_seg("ks3-bottle-opt", False, o.get("label", ""),
                    data_bottle_opt=o["id"])
            for o in options)
        cards.append(
            '<div class="ks3-bottle-card" data-bottle-card="%s" '
            'data-open="0">'
            '<div class="ks3-bottle-head">'
            '<p class="ks3-bottle-name">%s</p>'
            '<p class="ks3-bottle-where">%s</p></div>'
            '<div class="ks3-bottle-opts">%s</div>'
            '<div class="ks3-bottle-reveal" hidden data-bottle-reveal>'
            '<p class="ks3-bottle-verdict">%s</p>'
            '<p class="ks3-bottle-why">%s</p></div></div>'
            % (e(b["id"]), t(b["name"]), t(b["where"]), buttons,
               rich(b["verdict"]), rich(b["why"])))

    close = ('<div class="ks3-bottle-close" id="%s" hidden data-bottle-close>'
             '<p class="ks3-bottle-closetitle">%s</p>'
             '<p class="ks3-bottle-closebody">%s</p></div>'
             % (e(pattern["id"]), t(pattern.get("title", "")),
                rich(pattern["text"])))

    return ('<div class="ks3-bottle" data-bottle data-total="%d">'
            '<div class="ks3-bottle-cards">%s</div>%s</div>'
            % (len(bottles), "".join(cards), close))


# ═══ c6-01 · c6-02 · c6-03 · c6-04 · c6-07 — acid-judgements ══════════════

def r_acid_judgements(a, act_id):
    """⊕ the five judgement blocks — a question, a commitment, an answer.

    ⭐ **ONE FAMILY, FIVE PLACEMENTS, AND THAT IS DELIBERATE.** Design draws
    the identical component on five of the six pages — `#s-hazard` (three
    judgements about danger), `#s-choose` (three jobs, pick the indicator),
    `#s-uses` (four problems for neutralisation), `#s-test` (three judgements
    about the gas test) and `#s-uses` again on the catalyst page. Same markup,
    same handler, same `c3CommitCards` contract; only the questions and the
    number of options change. C3's `sequence-rebuild` set the precedent for
    one family placed more than once, and the alternative here is five
    near-identical renderers that would drift apart within a unit.

    §6's warning about repeated block lineups is answered the way C5 answered
    it: the FLAGSHIP of each page is different every time — a bottle bench, a
    pH bench, a titration dial, a 4x2 grid, a naming bench, a five-flask
    comparison — and this is the small second instrument beside each of them,
    not the thing the page is.

    ⚠️ THE NUMBER OF OPTIONS IS A PROPERTY OF THE ITEM, NOT OF THE BLOCK. Two
    of the five ask yes/no and three ask a three-way choice, and one page mixes
    lengths inside a block. Options are therefore authored per item.

    ⚠️ `answer` IS EMITTED NOWHERE AND IS READ HERE. R3 reserves marking for
    the mastery ladder, so the reply is a paragraph in the same voice whichever
    button was pressed. It is checked at build time against the item's own
    option set, for the same reason `fuel-cards` checks its cards: authored
    correctness data with no read site is content that never reaches a student
    AND an invariant nothing is watching.

    ⭐ AN ITEM MAY CARRY A REAL `id`, AND ONE OF THEM HAS TO. MRB-244/248
    resolve a misconception join against `id="…"` or `data-activity="…"` on the
    BUILT PAGE, and `data-ajudge-card` is neither. `dom_id` puts the
    commitment's name on the card and `reveal_id` puts the confrontation's name
    on the panel underneath it; both come from the payload rather than being
    composed here, so the register's join and the markup have one source and a
    second placement of this family cannot emit a duplicate id.

    HOOKS: `data-ajudge` (wrapper, with `data-total`) · `data-ajudge-card`
    (valued with the item id, carrying `data-open`) · `data-ajudge-opt` (valued
    with the option id) · `data-ajudge-reveal`.
    """
    items = a.get("items") or []
    if len(items) < 2:
        raise ValueError(
            "acid-judgements %r declares %d item(s). One judgement is an "
            "example; the block's whole shape is the same question asked of "
            "several situations." % (act_id, len(items)))

    seen = set()
    for it in items:
        _c6_need(it, it.get("id"), "acid-judgements item",
                 ("id", "q", "answer", "reply"),
                 "Every item is a question, a commitment and a reply; an item "
                 "missing any of them is a button that goes nowhere.")
        if it["id"] in seen:
            raise ValueError(
                "acid-judgements %r authors item id %r twice." % (act_id, it["id"]))
        seen.add(it["id"])
        opts = it.get("options") or []
        if len(opts) < 2:
            raise ValueError(
                "acid-judgements %r item %r offers %d option(s). A commitment "
                "with one answer is a caption." % (act_id, it["id"], len(opts)))
        ids = [o["id"] for o in opts]
        if len(set(ids)) != len(ids):
            raise ValueError(
                "acid-judgements %r item %r repeats an option id: %r. Two "
                "buttons with one name is one unreachable button."
                % (act_id, it["id"], ids))
        if it["answer"] not in ids:
            raise ValueError(
                "acid-judgements %r item %r answers %r, which is not one of "
                "%r. The record has to know which answer is right even though "
                "the markup never says." % (act_id, it["id"], it["answer"], ids))

    cards = "".join(
        '<div class="ks3-ajudge-card"%s data-ajudge-card="%s" data-open="0">'
        '<p class="ks3-ajudge-q">%s</p>'
        '<div class="ks3-ajudge-opts">%s</div>'
        '<div class="ks3-ajudge-reveal"%s hidden data-ajudge-reveal>'
        '<p>%s</p></div></div>'
        % ((' id="%s"' % e(it["dom_id"])) if it.get("dom_id") else "",
           e(it["id"]), rich(it["q"]),
           "".join(_c6_seg("ks3-ajudge-opt", False, o.get("label", ""),
                           data_ajudge_opt=o["id"])
                   for o in it["options"]),
           (' id="%s"' % e(it["reveal_id"])) if it.get("reveal_id") else "",
           rich(it["reply"]))
        for it in items)

    return ('<div class="ks3-ajudge" data-ajudge data-total="%d">%s</div>'
            % (len(items), cards))


# ═══ c6-02 · the pH strip, drawn (ART) ════════════════════════════════════

def _ph_strip(fig):
    """⊕ c6-02 `#s-scale` — the printed universal-indicator chart.

    ⚖️ **DRAWN, NOT BUILT OUT OF FIFTEEN FLEX DIVS**, and the reason is the
    C5 defect. Design's own markup is a row of `div`s in an `overflow-x: auto`
    box; anything absolutely positioned inside such a box escapes it unless the
    box is `position: relative`, and `overflow: hidden` does not fix it — that
    is what widened five C5 pages by 140px at 390px. An SVG's children are
    inside its viewBox by construction, and `.ks3-figure-scroll` is the
    platform's own already-measured, already-faded scroll region (MRB-254).

    ⚖️ **EVERY CELL CARRIES ITS NUMBER, AND THAT IS ENFORCED HERE.** NOTES-C6
    §7's ruling on the fifteen literal hex values is conditional on it: the
    ramp is scientific data and may be non-token, PROVIDED identity is never
    hue-only. So this walks all fifteen cells and refuses to draw one without
    its printed pH — the assertion covers EVERY element rather than a sample,
    which is §5A's requirement for a figure's content-truth check.

    ⚑ AND THE NEUTRAL POINT IS ASSERTED. The lesson, the key fact, the key note
    and three ladder rungs all rest on 7 being the middle; the drawing has to
    agree, and here it has to agree by construction rather than by counting the
    cells and hoping.
    """
    data = fig.get("data") or {}
    colours = data.get("colours") or []
    neutral = data.get("neutral_at")

    if len(colours) != 15:
        raise ValueError(
            "figure %r draws %d pH cell(s). The scale is 0 to 14 inclusive, "
            "which is fifteen whole numbers, and the page says so in words."
            % (fig.get("id"), len(colours)))
    if neutral != 7:
        raise ValueError(
            "figure %r puts neutral at %r. Every claim on this page — the key "
            "fact, the key note, both marked rungs — rests on 7, and a "
            "drawing that disagrees with the prose beside it is the failure "
            "§5A's content-truth assertion exists for." % (fig.get("id"), neutral))
    for key in ("acid_end", "neutral_label", "alkali_end", "note"):
        if not data.get(key):
            raise ValueError(
                "figure %r has no %r. The strip's three captions and its note "
                "are what turn a row of colours into a scale." % (fig.get("id"), key))

    # Geometry. 15 cells at 52 wide with a 4 gutter is 836, plus 12 either
    # side: 860, which is the width the biology kit settled on and the width
    # `.ks3-figure-scroll` is already sized around.
    pad, cell, gap, top, high = 12, 52, 4, 46, 88
    width = pad * 2 + cell * 15 + gap * 14
    height = top + high + 66

    out = [_svg_open(fig, width, height)]

    # The three mono captions ABOVE the ramp, so a narrow reader meets the
    # orientation before the colours rather than after them.
    out.append(_mono(pad, 24, data["acid_end"], size=13,
                     fill=_SVG_INK_MUTED, anchor="start"))
    out.append(_mono(width / 2.0, 24, data["neutral_label"], size=13,
                     fill=_SVG_INK_MUTED, anchor="middle"))
    out.append(_mono(width - pad, 24, data["alkali_end"], size=13,
                     fill=_SVG_INK_MUTED, anchor="end"))

    for i, colour in enumerate(colours):
        x = pad + i * (cell + gap)
        out.append(_rect(x, top, cell, high, rx=10, fill=colour,
                         stroke=_SVG_INK, w=2,
                         data_ph_cell=str(i)))
        # ⚠️ THE NUMBER IS THE IDENTITY. `_label` refuses an empty string, so
        # a cell can never ship as a bare colour: `str(i)` is always a
        # character, and this is the line NOTES-C6 §7's ruling is conditional
        # on. It is drawn ON the cell in the one near-white that clears every
        # one of the fifteen grounds, including the yellow at pH 6.
        out.append(_label(x + cell / 2.0, top + high - 14, str(i), size=17,
                          fill=PH_ON_COLOUR, weight="700", anchor="middle",
                          data_ph_num=str(i)))
        # The neutral cell gets a printed word as well as a number, because
        # "7 is neutral" is the single fact the whole strip exists to place.
        if i == neutral:
            out.append(_label(x + cell / 2.0, top - 10, "neutral", size=13,
                              fill=_SVG_INK, weight="700", anchor="middle"))

    out.append(_label(pad, top + high + 34, data["note"], size=15,
                      fill=_SVG_INK_MUTED, weight="500", anchor="start"))
    out.append("</svg>")
    return "".join(out)


# ═══ c6-02 · ph-bench (#s-bench) ══════════════════════════════════════════

_PH_BANDS_MSG = (
    "The bands are the guess the student commits to before the indicator goes "
    "in, so every sample has to fall in exactly one of them and every band has "
    "to be reachable.")


def r_ph_bench(a, act_id):
    """⊕ c6-02 `#s-bench` — pick a sample, BAND THE GUESS, then test it.

    ⚖️ **THE GUESS IS THE GATE (Law 4).** Nothing about a sample is readable
    until the student has said which band they expect, and Design's own
    `needGuess` does exactly this. What is NOT reproduced is the disappearance:
    her `sc-if needGuess` removes the band buttons the moment one is pressed,
    which takes the student's own commitment off the page at the exact moment
    the reading arrives to be compared against it. Every gate in C3, C4 and C5
    stays put. This one stays put, and the pressed band stays pressed.

    ⚖️ **THE VERDICT IS DERIVED FROM THE pH, NOT AUTHORED BESIDE IT** (§5A:
    comparative labels are derived at render, and a branch is taken on the
    thing the lesson teaches rather than on a proxy). Design writes a chain of
    ternaries on `sample.ph`; the bands are authored once, with their ranges,
    and every sample's band and verdict are LOOKED UP from its pH here. So a
    sample cannot be filed under a band its own number contradicts, and adding
    a seventh sample cannot forget to update a verdict.

    ⚠️ THE WHOLE STATE SPACE IS ENUMERATED AND CHECKED. Every band must contain
    at least one sample, or the bench draws a button that is never the answer;
    the ranges must tile 0 to 14 with no gap and no overlap, or a sample can
    fall through; and pH 7 must be a band of its own, because "neutral is a
    single point you cross" is the claim c6-03 is about to make.

    ⚠️ THE COLOUR CHIP CARRIES ITS NUMBER. See `PH_COLOURS` at the top of this
    file: the ramp is scientific data and is allowed to be non-token exactly
    because nothing on this page is identified by hue alone.

    ⚖️ CREDIT IS FOR TESTING FOUR OF THE SIX, which is Design's own
    `DONE('s-bench')` (`Object.keys(s.tested).length >= 4`). Four is enough to
    have met both ends of the scale and the middle; six would make the stop a
    completion bar rather than a record of participation.

    HOOKS: `data-phbench` (wrapper, with `data-total` and `data-done-at`) ·
    `data-phbench-tab` (valued with the sample id) · `data-phbench-name` /
    `data-phbench-setup` (valued with the sample id) · `data-phbench-guess`
    (valued with the band id) · `data-phbench-result` (valued with the sample
    id) · `data-phbench-guessrow`.
    """
    samples = a.get("samples") or []
    bands = a.get("bands") or []
    done_at = a.get("done_at")

    if len(samples) < 4:
        raise ValueError(
            "ph-bench %r offers %d sample(s). The bench has to reach both ends "
            "of the scale and the middle, or the strip beside it is a picture "
            "of somewhere the student never goes." % (act_id, len(samples)))
    if len(bands) < 3:
        raise ValueError(
            "ph-bench %r offers %d band(s). %s" % (act_id, len(bands), _PH_BANDS_MSG))
    if not isinstance(done_at, int) or not 2 <= done_at <= len(samples):
        raise ValueError(
            "ph-bench %r has done_at=%r against %d samples. The rail stop "
            "ticks when that many have been tested; one would tick on the "
            "first press and more than there are could never tick."
            % (act_id, done_at, len(samples)))

    # ── the bands must tile 0..14 exactly once ───────────────────────────
    covered = {}
    for band in bands:
        _c6_need(band, band.get("id"), "ph-bench band",
                 ("id", "label", "verdict"),
                 "A band is a button the student presses and a verdict the "
                 "reading is reported in; neither may be missing.")
        lo, hi = band.get("lo"), band.get("hi")
        if not isinstance(lo, int) or not isinstance(hi, int) or lo > hi:
            raise ValueError(
                "ph-bench %r band %r has range %r..%r. %s"
                % (act_id, band["id"], lo, hi, _PH_BANDS_MSG))
        for n in range(lo, hi + 1):
            if n in covered:
                raise ValueError(
                    "ph-bench %r: pH %d is in band %r AND band %r. A reading "
                    "in two bands is a guess that cannot be wrong."
                    % (act_id, n, covered[n], band["id"]))
            covered[n] = band["id"]
    holes = [n for n in range(15) if n not in covered]
    if holes:
        raise ValueError(
            "ph-bench %r leaves pH %s in no band at all. %s"
            % (act_id, holes, _PH_BANDS_MSG))
    if covered[7] == covered.get(6) or covered[7] == covered.get(8):
        raise ValueError(
            "ph-bench %r puts pH 7 in a band with its neighbours. Neutral is a "
            "single point, which is the claim c6-03's titration cliff is built "
            "on, and a band that spans 6 to 8 teaches the opposite." % act_id)

    by_id = dict((b["id"], b) for b in bands)

    # ── every sample, checked against the bands rather than against itself ─
    used = set()
    seen = set()
    for s in samples:
        _c6_need(s, s.get("id"), "ph-bench sample",
                 ("id", "label", "setup", "litmus", "why"),
                 "A sample is a name, a setup, a litmus reading and an "
                 "explanation; a sample missing any of them opens on a gap.")
        if s["id"] in seen:
            raise ValueError(
                "ph-bench %r authors sample id %r twice." % (act_id, s["id"]))
        seen.add(s["id"])
        ph = s.get("ph")
        if not isinstance(ph, int) or not 0 <= ph <= 14:
            raise ValueError(
                "ph-bench %r sample %r reads pH %r. §5A: if the lesson names a "
                "quantity it must be readable as a NUMBER, and the chart this "
                "bench reads against runs 0 to 14."
                % (act_id, s["id"], ph))
        want = covered[ph]
        if s.get("band") != want:
            raise ValueError(
                "ph-bench %r sample %r is filed under band %r but reads pH %d, "
                "which is band %r. The band is DERIVED from the number; a "
                "sample filed against its own reading would print a verdict "
                "the chip beside it contradicts."
                % (act_id, s["id"], s.get("band"), ph, want))
        used.add(want)

    unused = [b["id"] for b in bands if b["id"] not in used]
    if unused:
        raise ValueError(
            "ph-bench %r draws band button(s) %s that no sample lands in. A "
            "guess that is never right is learnable in one bench."
            % (act_id, unused))

    first = samples[0]["id"]

    tabs = "".join(
        _c6_seg("ks3-phbench-tab", s["id"] == first, s.get("label", ""),
                data_phbench_tab=s["id"])
        for s in samples)

    names = "".join(
        '<p class="ks3-phbench-name"%s data-phbench-name="%s">%s</p>'
        % ("" if s["id"] == first else " hidden", e(s["id"]), t(s["label"]))
        for s in samples)
    setups = "".join(
        '<p class="ks3-phbench-setup"%s data-phbench-setup="%s">%s</p>'
        % ("" if s["id"] == first else " hidden", e(s["id"]), rich(s["setup"]))
        for s in samples)

    guesses = ('<div class="ks3-phbench-guess" data-phbench-guessrow>'
               '<p class="ks3-commit">%s</p>'
               '<div class="ks3-phbench-bands">%s</div></div>'
               % (t(a.get("guess_prompt", "")),
                  "".join(_c6_seg("ks3-phbench-band", False,
                                  b.get("label", ""), data_phbench_guess=b["id"])
                          for b in bands)))

    # ── the results, all present, all hidden ─────────────────────────────
    #
    # EMIT-BOTH-SHOW-ONE. Six results in the document at rest and one unhidden
    # once its guess is in, so the chip's colour, its number, the derived
    # verdict and the litmus line are all bytes rather than a paint.
    results = []
    for s in samples:
        band = by_id[covered[s["ph"]]]
        results.append(
            '<div class="ks3-phbench-result" hidden data-phbench-result="%s">'
            '<div class="ks3-phbench-row">'
            '<span class="ks3-phbench-chip" style="background:%s">pH %d</span>'
            '<div><p class="ks3-phbench-verdict">%s</p>'
            '<p class="ks3-phbench-litmus">%s %s</p></div></div>'
            '<p class="ks3-phbench-why">%s</p></div>'
            % (e(s["id"]), e(PH_COLOURS[s["ph"]]), s["ph"],
               t(band["verdict"]), t(a.get("litmus_label", "Litmus:")),
               t(s["litmus"]), rich(s["why"])))

    return ('<div class="ks3-phbench" data-phbench data-total="%d" '
            'data-done-at="%d">'
            '<div class="ks3-phbench-tabs">%s</div>'
            '<div class="ks3-phbench-panel">%s%s%s%s</div></div>'
            % (len(samples), done_at, tabs, names, setups, guesses,
               "".join(results)))


# ═══ c6-03 · titration-dial (#s-titrate) ══════════════════════════════════

def r_titration_dial(a, act_id):
    """⊕ c6-03 `#s-titrate` — twenty drops, and one of them is a cliff.

    ⭐ **THE INSTRUMENT IS THE LESSON.** NOTES-C6 §3: "a drop-by-drop titration
    with a live pH readout and a bar trace. The instrument is the lesson: the
    trace makes the cliff visible." Everything below exists to make one shape
    visible — flat, cliff, flat — and to make it visible as something the
    student produced rather than as a claim in a paragraph.

    ⚖️ **NOT ONE NUMBER ON THIS PAGE IS HARD-CODED. EVERY ONE IS DERIVED FROM
    THE CURVE** (§5A). The equivalence point, the drop the cliff happens at,
    the height of all twenty-one bars, the colour of the beaker at every
    position, the state label at every position, and the drop count at which
    the rail stop ticks — all of them are read off `curve` here, at build time.
    Design's own page hard-codes "the first nine drops", "the tenth" and
    `seenJump: next >= 11` in three separate places; re-point the curve at a
    different acid and all three go quietly wrong. Here, re-pointing the curve
    is one line and everything follows it.

    ⚑ SCIENCE FLAG 6, RULED AND KEPT EXACTLY: 1,1,1,1,2,2,2,2,3,3,7,11,11,12,
    12,12,13,13,13,13,13 — integers, equivalence at drop 10, shaped correctly
    for a strong acid with a strong alkali. It is not smoothed, and the
    assertions below are what stop a later pass smoothing it: a curve with no
    single 7, or with a gentle climb through it, fails the build rather than
    shipping a page whose payoff paragraph describes a shape that is no longer
    on screen.

    ⚠️ THE FOUR ASSERTIONS, AND EACH IS ONE OF THE LESSON'S CLAIMS:

      1. THE CURVE ONLY RISES. Adding alkali to acid never lowers the pH, and
         a curve that dipped would be a page teaching that it can.
      2. THERE IS EXACTLY ONE READING OF 7. "Neutral is not a region you drift
         into. It is a single point you cross" is the payoff sentence, and two
         sevens would make it a region.
      3. THE STEP ACROSS THAT POINT IS A CLIFF. At least four pH units in one
         drop — Design's is eight. A curve that climbed to 7 in ones would
         still satisfy 1 and 2 and would teach the opposite of the lesson.
      4. THE STATE LABELS ARE DERIVED AND CHECKED. Each authored state names
         the drop positions it covers; those sets must tile 0..N exactly once,
         and every position's authored verdict must agree with what its own pH
         says — acidic below 7, neutral at 7, alkaline above.

    ⚠️ EMIT-BOTH-SHOW-ONE for the pH label, the state label and the note; the
    bar heights and the beaker colours are a `data-cfg`, because they are
    geometry and colour and are exactly what that hatch is for.

    HOOKS: `data-titr` (wrapper, carrying `data-cfg` and `data-done-at`) ·
    `data-titr-beaker` · `data-titr-ph` (valued with the pH) · `data-titr-count`
    (with `data-format`) · `data-titr-state` (valued with the state id) ·
    `data-titr-note` (valued with the state id) · `data-titr-bar` (valued with
    its drop index) · `data-titr-add` (valued with how many drops it adds) ·
    `data-titr-reset` · `data-titr-close`.
    """
    curve = a.get("curve") or []
    states = a.get("states") or []
    adds = a.get("add_buttons") or []
    close = a.get("close") or {}

    if len(curve) < 6:
        raise ValueError(
            "titration-dial %r has a %d-point curve. The shape the lesson is "
            "for is flat, cliff, flat, and it needs room on both sides of the "
            "cliff to be a shape at all." % (act_id, len(curve)))
    for n in curve:
        if not isinstance(n, int) or not 0 <= n <= 14:
            raise ValueError(
                "titration-dial %r has curve value %r. The readings are whole "
                "pH numbers on a 0-to-14 scale — flag 6's ruling — and the "
                "chart the beaker is coloured from has fifteen entries."
                % (act_id, n))

    # ── 1 · monotonic ────────────────────────────────────────────────────
    for i in range(1, len(curve)):
        if curve[i] < curve[i - 1]:
            raise ValueError(
                "titration-dial %r drops from pH %d to pH %d at drop %d. "
                "Adding alkali to acid never sends the reading back down; a "
                "curve that dips teaches that it can."
                % (act_id, curve[i - 1], curve[i], i))

    # ── 2 · exactly one equivalence point ────────────────────────────────
    sevens = [i for i, n in enumerate(curve) if n == 7]
    if len(sevens) != 1:
        raise ValueError(
            "titration-dial %r reads pH 7 at drop(s) %s. The payoff paragraph "
            "says neutral is a single point you cross rather than a region you "
            "drift into, and %d of them makes it a region."
            % (act_id, sevens, len(sevens)))
    equiv = sevens[0]
    if equiv in (0, len(curve) - 1):
        raise ValueError(
            "titration-dial %r puts the equivalence point at the end of the "
            "run (drop %d of %d). The trace has to show flat, cliff, flat."
            % (act_id, equiv, len(curve) - 1))

    # ── 3 · it is a cliff, not a climb ───────────────────────────────────
    jump = max(curve[equiv] - curve[equiv - 1], curve[equiv + 1] - curve[equiv])
    if jump < 4:
        raise ValueError(
            "titration-dial %r moves at most %d pH unit(s) across the "
            "equivalence point. That is a climb, and the whole block exists to "
            "show a cliff — 'one single drop takes the reading from 3 to 11' "
            "is the sentence the trace has to earn." % (act_id, jump))

    # The first position past neutral is where the payoff panel opens: the
    # student has SEEN the jump by then and not before. Derived, so Design's
    # `seenJump: next >= 11` cannot drift from her own curve.
    jump_at = next(i for i, n in enumerate(curve) if n > 7)
    done_at = jump_at + 1
    if done_at >= len(curve):
        done_at = len(curve) - 1

    # ── 4 · the states tile the run, and each agrees with its own pH ─────
    where = {}
    for st in states:
        _c6_need(st, st.get("id"), "titration-dial state",
                 ("id", "label", "note", "side"),
                 "A state is a verdict, a note and which side of neutral it "
                 "is on; the side is what the build checks the verdict "
                 "against.")
        if st["side"] not in ("acid", "neutral", "alkali"):
            raise ValueError(
                "titration-dial %r state %r declares side %r. The three sides "
                "are the three the pH scale has." % (act_id, st["id"], st["side"]))
        for i in st.get("at") or []:
            if not isinstance(i, int) or not 0 <= i < len(curve):
                raise ValueError(
                    "titration-dial %r state %r covers drop %r, which is not "
                    "on a %d-drop run." % (act_id, st["id"], i, len(curve)))
            if i in where:
                raise ValueError(
                    "titration-dial %r: drop %d is covered by state %r AND "
                    "state %r. Two notes for one reading is a panel that shows "
                    "whichever the browser found first."
                    % (act_id, i, where[i], st["id"]))
            where[i] = st["id"]
            # THE CONTENT-TRUTH ASSERTION, WALKING EVERY DROP.
            side = ("neutral" if curve[i] == 7
                    else "acid" if curve[i] < 7 else "alkali")
            if st["side"] != side:
                raise ValueError(
                    "titration-dial %r state %r calls drop %d %r, but the "
                    "reading there is pH %d, which is %r. The verdict branches "
                    "on the thing the lesson teaches — which side of 7 the "
                    "beaker is on — and it may not disagree with the number "
                    "printed beside it."
                    % (act_id, st["id"], i, st["side"], curve[i], side))
    uncovered = [i for i in range(len(curve)) if i not in where]
    if uncovered:
        raise ValueError(
            "titration-dial %r has no state for drop(s) %s, including the "
            "resting one if 0 is in that list. A student presses a button and "
            "the panel goes blank." % (act_id, uncovered))

    if not adds:
        raise ValueError(
            "titration-dial %r has no add buttons. A titration with no way to "
            "add a drop is a picture of one." % act_id)
    for b in adds:
        if not isinstance(b.get("n"), int) or b["n"] < 1:
            raise ValueError(
                "titration-dial %r add button %r adds %r drops."
                % (act_id, b.get("label"), b.get("n")))
    if not close.get("id") or not close.get("paras"):
        raise ValueError(
            "titration-dial %r has no closing panel with an `id` and its "
            "paragraphs. The panel is where the cliff is explained and its id "
            "is a misconception join." % act_id)

    # ── the readout ──────────────────────────────────────────────────────
    ph_vals = sorted(set(curve))
    ph_html = "".join(
        '<span%s data-titr-ph="%d">pH %d</span>'
        % ("" if n == curve[0] else " hidden", n, n) for n in ph_vals)
    state_html = "".join(
        '<p class="ks3-titr-state"%s data-titr-state="%s">%s</p>'
        % ("" if st["id"] == where[0] else " hidden", e(st["id"]), t(st["label"]))
        for st in states)
    note_html = "".join(
        '<p class="ks3-titr-note"%s data-titr-note="%s">%s</p>'
        % ("" if st["id"] == where[0] else " hidden", e(st["id"]), rich(st["note"]))
        for st in states)

    # ── the trace ────────────────────────────────────────────────────────
    #
    # Height and colour are the one thing here that IS a `data-cfg`: they are
    # geometry and paint, recomputed on every press, and no sentence is
    # involved. The resting render draws bar 0 lit and the other twenty
    # dormant, which is the state a page is in before anybody touches it.
    top = float(max(curve) + 1)
    bars = "".join(
        '<span class="ks3-titr-bar" data-titr-bar="%d" data-on="%s" '
        'style="height:%.0f%%"></span>'
        % (i, "1" if i == 0 else "0", 100.0 * n / top)
        for i, n in enumerate(curve))

    cfg = json.dumps({"curve": curve, "colours": PH_COLOURS,
                      "where": [where[i] for i in range(len(curve))]},
                     separators=(",", ":"), sort_keys=True)

    controls = "".join(
        _c6_seg("ks3-titr-add", False, b.get("label", ""),
                data_titr_add=str(b["n"]))
        for b in adds)

    closer = ('<div class="ks3-titr-close" id="%s" hidden data-titr-close>'
              '<p class="ks3-titr-closetitle">%s</p>%s</div>'
              % (e(close["id"]), t(close.get("title", "")),
                 "".join("<p>%s</p>" % rich(p) for p in close["paras"])))

    return ('<div class="ks3-titr" data-titr data-done-at="%d" '
            'data-cfg="%s">'
            '<div class="ks3-titr-grid">'
            '<div class="ks3-titr-beakerpanel">'
            '<div class="ks3-titr-row">'
            '<span class="ks3-titr-beaker" data-titr-beaker '
            'style="background:%s" aria-hidden="true"></span>'
            '<div><p class="ks3-titr-ph">%s</p>'
            '<p class="ks3-titr-count" data-titr-count data-format="%s">%s</p>'
            '%s</div></div>%s'
            '<div class="ks3-titr-controls">%s'
            '<button type="button" class="ks3-retry ks3-titr-reset" '
            'data-titr-reset>%s</button></div></div>'
            '<div class="ks3-titr-tracepanel">'
            '<p class="ks3-titr-tracelabel">%s</p>'
            '<div class="ks3-titr-trace">%s</div>'
            '<p class="ks3-titr-axis">%s</p></div></div>%s</div>'
            % (done_at, e(cfg), e(PH_COLOURS[curve[0]]), ph_html,
               e(a.get("count_format", "{n} drops of alkali added")),
               t(a.get("count_zero", "0 drops of alkali added")),
               state_html, note_html, controls,
               t(a.get("reset_label", "Start again")),
               t(a.get("trace_label", "")), bars,
               t(a.get("axis_label", "")), closer))


# ═══ c6-04 · acid-metal-grid (#s-bench) ═══════════════════════════════════

def r_acid_metal_grid(a, act_id):
    """⊕ c6-04 `#s-bench` — four metals, two acids, eight tubes.

    ⚠️ **THIS IS NOT `reactivity-grid`.** `ks3_art/c5.py` owns that family name
    and the shell class `ks3-rgrid-block`; NOTES-C6 §4 proposes reusing both
    and MRB-279's gate is what stops it. Same shape, own family, own class, own
    prefix — two families wearing one class puts one unit's stylesheet on the
    other unit's instrument and does it silently.

    ⚖️ **TWO PATTERNS, AND THE GRID HAS TO SHOW BOTH.** Read down a column and
    the speed falls in reactivity order; read across a row and the acid decides
    the salt's second word. The closing panel claims exactly that, and it only
    opens when six of the eight have been run — Design's own threshold, and the
    honest one: six is enough to have met the copper row, which is the row that
    proves the rule.

    ⚖️ **REACTING IS A PROPERTY OF THE METAL, AND IT IS ASSERTED AS ONE.** A
    metal that fizzes in hydrochloric acid and sits still in sulfuric would
    contradict the reactivity series the whole lesson argues from. The build
    checks every metal's cells agree with each other, and that at least one
    metal does nothing at all — without a negative row there is no rule, only
    four examples.

    ⚠️ AND EVERY EQUATION IS CHECKED AGAINST THE ACID IT CAME FROM. A reacting
    cell's products must name that acid's own salt ending and must name
    hydrogen; a non-reacting cell must carry no equation at all, because there
    is no reaction to write one for. That is `acid + metal makes salt +
    hydrogen` asserted against all eight cells rather than stated once in a key
    fact and hoped for.

    ⚠️ NOTHING IS COMPOSED. Design builds `cellWhy` out of the metal's name and
    the acid's salt ending and produces one sentence for seven cells and a
    hard-coded copper paragraph for the eighth. All eight are authored, so
    "magnesium" is not a substring surgically inserted into a sentence, the
    copper cells are two different sentences rather than one repeated, and
    `<strong>` survives.

    ⚠️ CONTAINMENT: the accessible name of every cell button is an `aria-label`
    ATTRIBUTE, not a visually-hidden span. An attribute has no box, so it
    cannot escape the horizontal scroller the table sits in — which is the
    exact defect that widened five C5 pages by 140px at 390px.

    HOOKS: `data-amgrid` (wrapper, with `data-total` and `data-done-at`) ·
    `data-amgrid-cell` (valued `<metal>:<acid>`) · `data-amgrid-title` /
    `data-amgrid-setup` (same value) · `data-amgrid-predict` (valued with the
    prediction id) · `data-amgrid-result` (same cell value) ·
    `data-amgrid-predictrow` · `data-amgrid-close`.
    """
    metals = a.get("metals") or []
    acids = a.get("acids") or []
    cells = a.get("cells") or []
    predicts = a.get("predict_options") or []
    close = a.get("close") or {}
    done_at = a.get("done_at")

    if len(metals) < 3 or len(acids) < 2:
        raise ValueError(
            "acid-metal-grid %r crosses %d metal(s) with %d acid(s). The block "
            "reads down for reactivity and across for the salt's name, and it "
            "needs both directions to have something in them."
            % (act_id, len(metals), len(acids)))
    if len(predicts) < 2:
        raise ValueError(
            "acid-metal-grid %r has %d prediction option(s). Law 4: the "
            "readout is not shown until the student has said what they expect."
            % (act_id, len(predicts)))

    reachable = ["%s:%s" % (m["id"], x["id"]) for m in metals for x in acids]
    authored = [c["id"] for c in cells]
    missing = [k for k in reachable if k not in authored]
    surplus = [k for k in authored if k not in reachable]
    if missing or surplus:
        raise ValueError(
            "acid-metal-grid %r does not model what it draws. Cell(s) with no "
            "tube: %s. Tube(s) for no cell: %s. A hole in the grid shows the "
            "last cell's readings under the new cell's label."
            % (act_id, missing or "none", surplus or "none"))
    if len(set(authored)) != len(authored):
        raise ValueError(
            "acid-metal-grid %r authors the same tube twice." % act_id)

    if not isinstance(done_at, int) or not 2 <= done_at <= len(cells):
        raise ValueError(
            "acid-metal-grid %r has done_at=%r against %d tubes. The closing "
            "panel claims two patterns; it has to open on enough of the grid "
            "to show them, and it has to be reachable."
            % (act_id, done_at, len(cells)))

    by_id = dict((c["id"], c) for c in cells)
    salt_of = dict((x["id"], str(x.get("salt", ""))) for x in acids)

    # ── reacting is a property of the METAL ──────────────────────────────
    inert = []
    for m in metals:
        verdicts = set()
        for x in acids:
            c = by_id["%s:%s" % (m["id"], x["id"])]
            verdicts.add(bool(c.get("reacts")))
        if len(verdicts) != 1:
            raise ValueError(
                "acid-metal-grid %r has %s reacting with one acid and not the "
                "other. Whether a metal displaces hydrogen is decided by where "
                "it sits in the reactivity series, which is the same wherever "
                "the hydrogen came from — and the closing panel argues exactly "
                "that." % (act_id, m.get("name")))
        if not verdicts.pop():
            inert.append(m.get("name"))
    if not inert:
        raise ValueError(
            "acid-metal-grid %r has every metal reacting. The row that does "
            "nothing is the row that proves the rule — 'copper is below "
            "hydrogen, so it cannot push hydrogen out of an acid' is the "
            "lesson's second pattern and it needs a negative case." % act_id)
    if len(inert) == len(metals):
        raise ValueError(
            "acid-metal-grid %r has no metal reacting at all." % act_id)

    # ── and every equation is checked against its own acid ───────────────
    for c in cells:
        _c6_need(c, c.get("id"), "acid-metal-grid cell",
                 ("id", "title", "setup", "mark", "aria", "result", "why"),
                 "Every tube carries a label, a setup, what the grid cell "
                 "reads after it is run, and what happened; a tube missing "
                 "one opens on a blank.")
        acid_id = c["id"].split(":")[1]
        if c.get("reacts"):
            for key in ("eq_left", "eq_right"):
                if not c.get(key):
                    raise ValueError(
                        "acid-metal-grid %r cell %r reacts but has no %r. A "
                        "reaction the page will not write down is a reaction "
                        "the student cannot check." % (act_id, c["id"], key))
            right = str(c["eq_right"]).lower()
            if salt_of[acid_id] not in right:
                raise ValueError(
                    "acid-metal-grid %r cell %r is run in an acid that makes "
                    "%ss, and its products read %r. The acid names the second "
                    "word of the salt — that is one of the block's two "
                    "patterns, and the equation may not contradict it."
                    % (act_id, c["id"], salt_of[acid_id], c["eq_right"]))
            if "hydrogen" not in right:
                raise ValueError(
                    "acid-metal-grid %r cell %r reacts and its products read "
                    "%r, which never names hydrogen. `acid + metal makes salt "
                    "+ hydrogen` is the key fact this grid is the evidence "
                    "for." % (act_id, c["id"], c["eq_right"]))
        elif c.get("eq_left") or c.get("eq_right"):
            raise ValueError(
                "acid-metal-grid %r cell %r does not react and carries an "
                "equation anyway. Writing products for a reaction that never "
                "happens is the exact thing rung 2 is about."
                % (act_id, c["id"]))

    first = cells[0]["id"]

    # ── the table ────────────────────────────────────────────────────────
    head = ('<tr><th scope="col" class="ks3-amgrid-corner">%s</th>%s</tr>'
            % (t(a.get("corner_label", "")),
               "".join('<th scope="col">%s</th>' % t(x.get("name", ""))
                       for x in acids)))
    rows = []
    for m in metals:
        tds = []
        for x in acids:
            key = "%s:%s" % (m["id"], x["id"])
            c = by_id[key]
            # EMIT-BOTH-SHOW-ONE, down to a single word. The unrun mark and
            # the run mark are both in the document and the wiring unhides
            # one; neither is ever written into the button out of an
            # attribute, so a cell cannot end up showing a value composed at
            # run time from a string this file also has to be right about.
            tds.append(
                '<td><button type="button" class="ks3-amgrid-cell" '
                'data-amgrid-cell="%s" data-run="0" aria-pressed="%s" '
                'aria-label="%s">'
                '<span data-amgrid-unrun>%s</span>'
                '<span hidden data-amgrid-mark>%s</span></button></td>'
                % (e(key), "true" if key == first else "false",
                   e(c["aria"]), t(a.get("unrun_mark", "?")), t(c["mark"])))
        rows.append('<tr><th scope="row">%s</th>%s</tr>'
                    % (t(m.get("name", "")), "".join(tds)))

    table = ('<div class="ks3-amgrid-scroll" tabindex="0" role="group" '
             'aria-label="%s"><table class="ks3-amgrid-table">'
             '<thead>%s</thead><tbody>%s</tbody></table></div>'
             % (e(a.get("table_label", "Metals crossed with acids")),
                head, "".join(rows)))

    titles = "".join(
        '<p class="ks3-amgrid-title"%s data-amgrid-title="%s">%s</p>'
        % ("" if c["id"] == first else " hidden", e(c["id"]), t(c["title"]))
        for c in cells)
    setups = "".join(
        '<p class="ks3-amgrid-setup"%s data-amgrid-setup="%s">%s</p>'
        % ("" if c["id"] == first else " hidden", e(c["id"]), rich(c["setup"]))
        for c in cells)

    predict = ('<div class="ks3-amgrid-predict" data-amgrid-predictrow>'
               '<p class="ks3-commit">%s</p>'
               '<div class="ks3-amgrid-predictopts">%s</div></div>'
               % (t(a.get("predict_prompt", "")),
                  "".join(_c6_seg("ks3-amgrid-predictopt", False,
                                  p.get("label", ""),
                                  data_amgrid_predict=p["id"])
                          for p in predicts)))

    results = []
    for c in cells:
        eq = ""
        if c.get("reacts"):
            eq = ('<p class="ks3-amgrid-eq"><span>%s</span>%s<span>%s</span></p>'
                  % (t(c["eq_left"]), _c6_arrow("ks3-amgrid-arrow"),
                     t(c["eq_right"])))
        results.append(
            '<div class="ks3-amgrid-result" hidden data-amgrid-result="%s">'
            '<p class="ks3-amgrid-verdict">%s</p>'
            '<p class="ks3-amgrid-why">%s</p>%s</div>'
            % (e(c["id"]), rich(c["result"]), rich(c["why"]), eq))

    closer = ""
    if close.get("id") and close.get("paras"):
        closer = ('<div class="ks3-amgrid-close" id="%s" hidden '
                  'data-amgrid-close><p class="ks3-amgrid-closetitle">%s</p>%s'
                  '</div>'
                  % (e(close["id"]), t(close.get("title", "")),
                     "".join("<p>%s</p>" % rich(p) for p in close["paras"])))

    return ('<div class="ks3-amgrid" data-amgrid data-total="%d" '
            'data-done-at="%d">%s'
            '<div class="ks3-amgrid-panel">%s%s%s%s</div>%s</div>'
            % (len(cells), done_at, table, titles, setups, predict,
               "".join(results), closer))


# ═══ c6-06 · salt-namer (#s-name) ═════════════════════════════════════════

def r_salt_namer(a, act_id):
    """⊕ c6-06 `#s-name` — three acids, four bases, twelve salts.

    ⚖️ **THE NAME IS GENERATED BY A RULE, AND HERE THE RULE IS THE ASSERTION.**
    NOTES-C6 §4: "`salt-namer` generates the salt name from `base.metal +
    acid.ending`, so adding a fourth acid is a one-line change." Design's page
    runs that rule at RUN time and prints whatever it produces. This runs it at
    BUILD time and checks it against the twelve authored names, which is the
    same one-line change with one difference: a base whose metal is wrong, or
    an acid filed under the wrong ending, stops the build instead of teaching
    twelve students a wrong name apiece.

    ⚠️ AND THE OPTIONS ARE CHECKED THE SAME WAY. Each mix offers three names
    and exactly one of them must be the derived salt; the other two must be
    different from it and from each other. Design's generator produces a
    duplicate for any base whose metal is the one her `wrongB` falls back to,
    which is a wrong answer offered twice — the kind of thing that is invisible
    on the two combinations anyone opens by hand.

    ⚠️ AND THE PRODUCTS. A carbonate base gives carbon dioxide as well as salt
    and water, and nothing else does. That is checked on every one of the
    twelve, because it is the one place this bench touches the reaction rather
    than the naming, and it is the fact `c6-05` would have taught if it had
    been built.

    ⚖️ CREDIT IS FOR NAMING THREE, which is Design's own `DONE` and her own
    sentence: "Twelve are possible — three is enough to see the rule." Twelve
    would make the stop a completion bar.

    ⚠️ ANSWER POSITION. The correct name is NOT index 0 on all twelve — see the
    lesson record, where the twelve option orders are authored level. Design's
    generator always puts it first, and "press the left-hand button" would
    otherwise beat knowing the rule on every combination.

    HOOKS: `data-namer` (wrapper, with `data-total` and `data-done-at`) ·
    `data-namer-acid` / `data-namer-base` (valued with the id) ·
    `data-namer-title` (valued `<acid>:<base>`) · `data-namer-opt` (valued
    `<acid>:<base>|<index>`) · `data-namer-result` (valued `<acid>:<base>`) ·
    `data-namer-askrow`.
    """
    acids = a.get("acids") or []
    bases = a.get("bases") or []
    mixes = a.get("mixes") or []
    done_at = a.get("done_at")

    if len(acids) < 2 or len(bases) < 2:
        raise ValueError(
            "salt-namer %r crosses %d acid(s) with %d base(s). The rule is "
            "that the metal names the salt and the acid names its ending, and "
            "one of either cannot show a rule." % (act_id, len(acids), len(bases)))

    reachable = ["%s:%s" % (x["id"], b["id"]) for x in acids for b in bases]
    authored = [m["id"] for m in mixes]
    missing = [k for k in reachable if k not in authored]
    surplus = [k for k in authored if k not in reachable]
    if missing or surplus:
        raise ValueError(
            "salt-namer %r does not model what it draws. Combination(s) with "
            "no mix: %s. Mix(es) for no combination: %s. A hole in the bench "
            "shows the previous salt's name under the new pair's label."
            % (act_id, missing or "none", surplus or "none"))
    if not isinstance(done_at, int) or not 2 <= done_at <= len(mixes):
        raise ValueError(
            "salt-namer %r has done_at=%r against %d combinations."
            % (act_id, done_at, len(mixes)))

    acid_by = dict((x["id"], x) for x in acids)
    base_by = dict((b["id"], b) for b in bases)

    for m in mixes:
        _c6_need(m, m.get("id"), "salt-namer mix",
                 ("id", "title", "salt", "eq_left", "eq_right", "note"),
                 "A mix is a pair, a salt name, a word equation and a note on "
                 "what that base does to the method.")
        acid = acid_by[m["id"].split(":")[0]]
        base = base_by[m["id"].split(":")[1]]

        # ── THE RULE, RUN AT BUILD TIME ───────────────────────────────────
        want = "%s %s" % (base.get("metal", ""), acid.get("ending", ""))
        if str(m["salt"]).strip().lower() != want:
            raise ValueError(
                "salt-namer %r mix %r is named %r. The rule the whole bench "
                "teaches — the metal names the salt, the acid names its ending "
                "— gives %r. When the bench's own rule and its answer key "
                "disagree, the page marks a student wrong for applying what it "
                "just taught." % (act_id, m["id"], m["salt"], want))

        opts = m.get("options") or []
        if len(opts) < 3:
            raise ValueError(
                "salt-namer %r mix %r offers %d name(s). Two is a coin toss "
                "and one is a caption." % (act_id, m["id"], len(opts)))
        low = [str(o).strip().lower() for o in opts]
        if len(set(low)) != len(low):
            raise ValueError(
                "salt-namer %r mix %r offers the same name twice: %r. A wrong "
                "answer offered twice is a three-option question a student can "
                "answer as a two-option one." % (act_id, m["id"], opts))
        if low.count(want) != 1:
            raise ValueError(
                "salt-namer %r mix %r offers the correct name %r %d time(s)."
                % (act_id, m["id"], want, low.count(want)))
        if m.get("answer") != low.index(want):
            raise ValueError(
                "salt-namer %r mix %r declares answer index %r; the correct "
                "name sits at %d. The index is authored so the position can be "
                "kept level across the twelve, and it is checked so it cannot "
                "drift from the options beside it."
                % (act_id, m["id"], m.get("answer"), low.index(want)))

        # ── AND THE PRODUCTS ──────────────────────────────────────────────
        right = str(m["eq_right"]).lower()
        if not right.startswith(want):
            raise ValueError(
                "salt-namer %r mix %r writes products %r, which does not open "
                "with the salt %r that this pair makes."
                % (act_id, m["id"], m["eq_right"], want))
        carbonate = base.get("kind") == "carbonate"
        makes_co2 = "carbon dioxide" in right
        if carbonate != makes_co2:
            raise ValueError(
                "salt-namer %r mix %r uses a %s and its products read %r. A "
                "carbonate gives carbon dioxide as well as salt and water; "
                "nothing else does, and the note beside this equation says so."
                % (act_id, m["id"], base.get("kind"), m["eq_right"]))

    # ── answer position, across the whole bench ──────────────────────────
    #
    # Not the ladder's gate and not the bank's — this is an instrument, and
    # neither corpus measures it. It is checked anyway, on the same principle:
    # a position that holds more than half of twelve is a button that beats
    # reading, and Design's generator holds all twelve.
    spread = {}
    for m in mixes:
        spread[m["answer"]] = spread.get(m["answer"], 0) + 1
    if spread and max(spread.values()) * 2 > len(mixes):
        worst = max(spread, key=lambda k: spread[k])
        raise ValueError(
            "salt-namer %r puts the correct name at position %d on %d of %d "
            "combinations. More than half means pressing that button beats "
            "knowing the rule." % (act_id, worst, spread[worst], len(mixes)))

    first_acid, first_base = acids[0]["id"], bases[0]["id"]
    first = "%s:%s" % (first_acid, first_base)

    acid_row = "".join(
        _c6_seg("ks3-namer-acid", x["id"] == first_acid, x.get("label", ""),
                data_namer_acid=x["id"]) for x in acids)
    base_row = "".join(
        _c6_seg("ks3-namer-base", b["id"] == first_base, b.get("label", ""),
                data_namer_base=b["id"]) for b in bases)

    titles = "".join(
        '<p class="ks3-namer-title"%s data-namer-title="%s">%s</p>'
        % ("" if m["id"] == first else " hidden", e(m["id"]), t(m["title"]))
        for m in mixes)

    asks = "".join(
        '<div class="ks3-namer-opts"%s data-namer-optrow="%s">%s</div>'
        % ("" if m["id"] == first else " hidden", e(m["id"]),
           "".join(_c6_seg("ks3-namer-opt", False, o,
                           data_namer_opt="%s|%d" % (m["id"], i))
                   for i, o in enumerate(m["options"])))
        for m in mixes)

    results = "".join(
        '<div class="ks3-namer-result" hidden data-namer-result="%s">'
        '<p class="ks3-namer-salt">%s</p>'
        '<p class="ks3-namer-eq"><span>%s</span>%s<span>%s</span></p>'
        '<p class="ks3-namer-note">%s</p></div>'
        % (e(m["id"]), t(m["options"][m["answer"]]), t(m["eq_left"]),
           _c6_arrow("ks3-namer-arrow"), t(m["eq_right"]), rich(m["note"]))
        for m in mixes)

    return ('<div class="ks3-namer" data-namer data-total="%d" '
            'data-done-at="%d">'
            '<div class="ks3-namer-dials">'
            '<div class="ks3-namer-dial"><p class="ks3-namer-diallabel">%s</p>'
            '<div class="ks3-namer-dialrow">%s</div></div>'
            '<div class="ks3-namer-dial"><p class="ks3-namer-diallabel">%s</p>'
            '<div class="ks3-namer-dialrow">%s</div></div></div>'
            '<div class="ks3-namer-panel">%s'
            '<div class="ks3-namer-ask" data-namer-askrow>'
            '<p class="ks3-commit">%s</p>%s</div>%s</div></div>'
            % (len(mixes), done_at, t(a.get("acid_label", "")), acid_row,
               t(a.get("base_label", "")), base_row, titles,
               t(a.get("ask_prompt", "")), asks, results))


# ═══ c6-06 · method-order (#s-method) ═════════════════════════════════════

def r_method_order(a, act_id):
    """⊕ c6-06 `#s-method` — six steps, shuffled, put them in order.

    ⚖️ **NO CHEMISTRY IN THIS FAMILY AT ALL**, and NOTES-C6 §4 says so: the
    payload is `{steps: [{id, text, why}], shuffled: [id…]}` and it is the
    obvious instrument for any "put the method in order" task in any subject.
    Nothing below mentions an acid.

    ⚖️ **THE VERDICT IS A SENTENCE, NOT A MARK, AND THE ANSWER ARRIVES EITHER
    WAY.** Design draws two closing lines — "That is the order, and every step
    earns its place" against "Not the order that works. Here is the sequence
    and what each step is for" — followed by the same six-item explanation
    both times. That is kept exactly: no green, no red, no per-step tick, and
    the six reasons are the point of the block whether the order came out right
    or not. Only the mastery ladder marks.

    ⚠️ THE SHUFFLE IS AUTHORED AND IS CHECKED TO BE A REAL SHUFFLE. A
    `shuffled` list that happens to equal the correct order is a task that is
    complete before it starts, and it would look completely normal in the
    source. It is also checked to be a PERMUTATION — a shuffle that drops a
    step makes the answer unreachable and a shuffle that repeats one makes two
    buttons the same button.

    ⚠️ THE RESTING RENDER: six steps in the shuffled order, none placed, no
    badge showing a number, the answer panel hidden, both verdicts hidden,
    `data-stage-done="0"`.

    HOOKS: `data-morder` (wrapper, carrying `data-total` and `data-morder-key`
    — NOT `data-correct`: R3 reserves that name for the ladder, and this is an
    ordering key, not a mark) ·
    `data-morder-step` (valued with the step id, carrying `data-placed`) ·
    `data-morder-badge` (same value) · `data-morder-clear` ·
    `data-morder-verdict` (valued `right` / `wrong`) · `data-morder-answer`.
    """
    steps = a.get("steps") or []
    shuffled = a.get("shuffled") or []
    verdicts = a.get("verdicts") or {}

    if len(steps) < 4:
        raise ValueError(
            "method-order %r has %d step(s). A sequence a student can hold in "
            "one glance is not a sequence they have to reason about."
            % (act_id, len(steps)))
    ids = [s["id"] for s in steps]
    if len(set(ids)) != len(ids):
        raise ValueError(
            "method-order %r repeats a step id: %r." % (act_id, ids))
    for s in steps:
        _c6_need(s, s.get("id"), "method-order step", ("id", "text", "why"),
                 "Every step is what you do and why it is there; the reasons "
                 "are the block's payoff and they are shown whether the order "
                 "came out right or not.")
    if sorted(shuffled) != sorted(ids):
        raise ValueError(
            "method-order %r shuffles %r against steps %r. The shuffle has to "
            "be a permutation: one that drops a step makes the answer "
            "unreachable, and one that repeats a step draws the same button "
            "twice." % (act_id, shuffled, ids))
    if list(shuffled) == list(ids):
        raise ValueError(
            "method-order %r's shuffled order IS the correct order. The task "
            "would be finished before the student touched it, and it would "
            "look entirely normal in the source." % act_id)
    for key in ("right", "wrong"):
        if not verdicts.get(key):
            raise ValueError(
                "method-order %r has no %r verdict. Both are sentences and "
                "both introduce the same six reasons; a missing one is a "
                "finished task with nothing said about it." % (act_id, key))

    by_id = dict((s["id"], s) for s in steps)

    choices = "".join(
        '<li><button type="button" class="ks3-morder-step" '
        'data-morder-step="%s" data-placed="0">'
        '<span class="ks3-morder-badge" data-morder-badge="%s" '
        'aria-hidden="true"></span>'
        '<span class="ks3-morder-text">%s</span></button></li>'
        % (e(sid), e(sid), t(by_id[sid]["text"]))
        for sid in shuffled)

    answer = "".join(
        '<li><strong>%s</strong> %s %s</li>'
        % (t(s["text"]), t(a.get("why_join", "—")), rich(s["why"]))
        for s in steps)

    verdict_html = "".join(
        '<p class="ks3-morder-verdict" hidden data-morder-verdict="%s">%s</p>'
        % (key, rich(verdicts[key])) for key in ("right", "wrong"))

    return ('<div class="ks3-morder" data-morder data-total="%d" '
            'data-morder-key="%s">'
            '<ol class="ks3-morder-list" role="list">%s</ol>'
            '<div class="ks3-morder-controls">'
            '<button type="button" class="ks3-retry ks3-morder-clear" '
            'data-morder-clear>%s</button></div>'
            '<div class="ks3-morder-answerpanel" hidden data-morder-answer>'
            '%s<ol class="ks3-morder-answer">%s</ol></div></div>'
            % (len(steps),
               e(json.dumps(ids, separators=(",", ":"))),
               choices, t(a.get("clear_label", "Start the order again")),
               verdict_html, answer))


# ═══ c6-07 · catalyst-bench (#s-bench) ════════════════════════════════════

def _catb_volume(value, act_id, trial_id):
    """The oxygen reading, parsed, so the build can compare the trials.

    A reading the build cannot read is a build error rather than a string shown
    to a student: §5A says a quantity the lesson names must be readable as a
    NUMBER, and this bench's entire argument is a comparison between numbers.
    """
    parts = str(value or "").split()
    if len(parts) != 2:
        raise ValueError(
            "catalyst-bench %r trial %r reports %r. A gas reading is a number "
            "and a unit — \"48 cm³\" — because the whole block is one trial "
            "measured against another." % (act_id, trial_id, value))
    try:
        return float(parts[0]), parts[1]
    except ValueError:
        raise ValueError(
            "catalyst-bench %r trial %r reports %r, whose first word is not a "
            "number." % (act_id, trial_id, value))


def r_catalyst_bench(a, act_id):
    """⊕ c6-07 `#s-bench` — five flasks, two controls, and one that catches you.

    ⚖️ **THE DISCRIMINATING TRIAL IS THE LESSON, AND IT IS ASSERTED.** Four
    flasks would teach "a catalyst makes it faster". The fifth — dilute acid,
    faster and consumed — is what makes the definition have two halves, and
    NOTES-C6 §5 flag 15 keeps it deliberately. So the build DERIVES which
    trials were faster (by comparing every reading against the control's) and
    then asserts:

      · every trial flagged as a catalyst was faster AND came back unchanged;
      · at least one trial was faster and is NOT a catalyst, or the bench
        teaches that speeding a reaction up is sufficient;
      · at least one trial changed nothing at all, or there is no control and
        "faster" is measured against nothing.

    §5A's rule is that a comparative label is derived at render rather than
    typed beside the thing it describes. "Faster" is exactly such a label here,
    and deriving it means a later edit that lowers the manganese dioxide figure
    below the control's cannot leave a page calling it a catalyst.

    ⚑ SCIENCE FLAGS 13, 15 AND 16, RULED. The volumes are ILLUSTRATIVE and the
    page has to say so where it reports them: `figures_note` is required
    whenever any trial reports a volume, and it is rendered directly under the
    two readouts rather than in a footnote. The dilute-acid trial stays. The
    "nine tenths of manufactured chemicals" claim is replaced by a range in the
    lesson's stretch layer, where it lives.

    ⚖️ CREDIT IS FOR RUNNING ALL FIVE, which is Design's own `DONE`. Here it is
    right: the argument is a comparison across the set and four flasks cannot
    make it — whichever four you leave out, one of the three assertions above
    has no evidence.

    ⚠️ EMIT-BOTH-SHOW-ONE throughout, and no number is composed: each trial's
    volume and recovered mass are authored strings sitting in the document from
    the first byte.

    HOOKS: `data-catb` (wrapper, with `data-total`) · `data-catb-tab` (valued
    with the trial id) · `data-catb-title` / `data-catb-setup` (same value) ·
    `data-catb-predict` (valued with the prediction id) · `data-catb-result`
    (same trial value) · `data-catb-predictrow` · `data-catb-close`.
    """
    trials = a.get("trials") or []
    predicts = a.get("predict_options") or []
    close = a.get("close") or {}

    if len(trials) < 4:
        raise ValueError(
            "catalyst-bench %r declares %d trial(s). The argument needs a "
            "control, a second control that is a solid and does nothing, at "
            "least one catalyst, and the one that is faster without "
            "qualifying." % (act_id, len(trials)))
    if len(predicts) < 2:
        raise ValueError(
            "catalyst-bench %r has %d prediction option(s). Law 4."
            % (act_id, len(predicts)))
    if not a.get("figures_note"):
        raise ValueError(
            "catalyst-bench %r reports volumes with no `figures_note`. "
            "NOTES-C6 §5 flags 13 and 16: these are illustrative figures, not "
            "measurements from one run, and the lesson has to say so where it "
            "reports them rather than let a student quote 48 cm³ as data."
            % act_id)

    seen = set()
    for tr in trials:
        _c6_need(tr, tr.get("id"), "catalyst-bench trial",
                 ("id", "label", "setup", "result", "volume", "mass", "why"),
                 "A trial is what was added, what happened, how much oxygen "
                 "came off, what was recovered and why it counts or does not.")
        if tr["id"] in seen:
            raise ValueError(
                "catalyst-bench %r authors trial id %r twice." % (act_id, tr["id"]))
        seen.add(tr["id"])

    # ── the comparison, DERIVED ──────────────────────────────────────────
    control = trials[0]
    base, unit = _catb_volume(control.get("volume"), act_id, control["id"])
    if control.get("catalyst"):
        raise ValueError(
            "catalyst-bench %r opens on a trial flagged as a catalyst. The "
            "first flask is the control every other reading is compared "
            "against, and a control that speeds the reaction up measures "
            "nothing." % act_id)

    faster, unchanged_speed = [], []
    for tr in trials:
        vol, this_unit = _catb_volume(tr["volume"], act_id, tr["id"])
        if this_unit != unit:
            raise ValueError(
                "catalyst-bench %r trial %r reports %s against the control's "
                "%s. Two units in one comparison is a difference a student "
                "cannot read." % (act_id, tr["id"], tr["volume"], control["volume"]))
        if vol > base:
            faster.append(tr["id"])
        else:
            unchanged_speed.append(tr["id"])

        if tr.get("catalyst"):
            if vol <= base:
                raise ValueError(
                    "catalyst-bench %r flags trial %r as a catalyst but it "
                    "gives %s against the control's %s. A catalyst speeds the "
                    "reaction up; that is half the definition and this bench "
                    "is the evidence for it."
                    % (act_id, tr["id"], tr["volume"], control["volume"]))
            if not tr.get("recovered"):
                raise ValueError(
                    "catalyst-bench %r flags trial %r as a catalyst but does "
                    "not declare it recovered. Coming back unchanged is the "
                    "OTHER half of the definition, and it is the half the "
                    "dilute acid fails." % (act_id, tr["id"]))

    if not faster:
        raise ValueError(
            "catalyst-bench %r has nothing faster than the control. There is "
            "no catalyst on the bench and no reaction to explain." % act_id)
    if len(unchanged_speed) < 2:
        raise ValueError(
            "catalyst-bench %r has %d trial(s) that change nothing. Two are "
            "needed and Design draws two: the empty flask, and the SAND — a "
            "solid with a large surface area that does nothing, which is what "
            "stops the student concluding that adding a powder is the thing "
            "that matters." % (act_id, len(unchanged_speed)))

    # ── ⊕ MRB-281 · THE MASS READOUT MUST NOT CONTRADICT THE FLAG ───────
    #
    # Found by mutation-testing this renderer at source: `recovered` was
    # asserted in ONE direction only — a catalyst had to declare it — so a
    # trial could be flagged recovered while its own mass readout said it had
    # been consumed, and nothing here would object. That readout is the
    # EVIDENCE for "a catalyst is not used up"; it is the number a student
    # reads, and a number that contradicts its own label teaches the
    # misconception the lesson exists to confront (`ACID-10`).
    for tr in trials:
        mass = str(tr.get("mass", ""))
        lost = re.match(r"\s*([\d.]+)\s*g\s+of\s+([\d.]+)\s*g\s*$", mass)
        spent = any(w in mass.lower() for w in ("consumed", "used up", "lost"))
        if tr.get("recovered"):
            if spent:
                raise ValueError(
                    "catalyst-bench %r declares trial %r recovered and reports "
                    "its mass as %r. Recovered means it came back unchanged; "
                    "a readout that says otherwise is the lesson's own claim "
                    "contradicted on the same row."
                    % (act_id, tr["id"], mass))
            if lost and lost.group(1) != lost.group(2):
                raise ValueError(
                    "catalyst-bench %r declares trial %r recovered but reports "
                    "%s recovered of %s added. Coming back UNCHANGED is the "
                    "half of the definition this bench is the evidence for, "
                    "and %s is not %s."
                    % (act_id, tr["id"], lost.group(1), lost.group(2),
                       lost.group(1), lost.group(2)))

    ringers = [i for i in faster
               if not next(x for x in trials if x["id"] == i).get("catalyst")]
    # ⊕ MRB-281 — and a ringer must NOT be recovered. Being consumed is the
    # whole reason a faster-but-not-a-catalyst flask is not a catalyst; a
    # ringer that also comes back unchanged meets both halves of the
    # definition and IS a catalyst, which makes such an item
    # indistinguishable from the thing it exists to be distinguished from.
    # Found by mutation at source. This still stands for any bench that
    # authors a ringer — it is only no longer compulsory to author one.
    for i in ringers:
        tr = next(x for x in trials if x["id"] == i)
        if tr.get("recovered"):
            raise ValueError(
                "catalyst-bench %r has trial %r faster than the control, not "
                "flagged a catalyst, and yet declared recovered. Faster AND "
                "unchanged IS the definition — so either it is a catalyst or "
                "it is not recovered, and the bench cannot say both."
                % (act_id, tr["id"]))

    # ⊕ RULED 28 Aug 2026 (MRB-295, C6-11). THIS GUARD USED TO REQUIRE A
    # RINGER — a trial faster than the control and still not a catalyst —
    # and it named the dilute-acid flask as the item NOTES-C6 §5 flag 15
    # kept in order to prevent the bench teaching that speed alone is
    # sufficient. The requirement is retired because the only flask that
    # ever satisfied it did so on INVENTED CHEMISTRY: dilute acid does not
    # accelerate hydrogen peroxide decomposition, it stabilises it. Mide
    # ruled the flask honest rather than keeping the shape, so a bench that
    # tells the truth about acid cannot contain a ringer at all, and a guard
    # demanding one would have forced the invented result back.
    #
    # ⚠️ This is NOT the protection being dropped. It is the protection being
    # re-expressed against what the bench now has to do. The pedagogical risk
    # the old guard named — a student concluding that adding something, or
    # speeding something up, is what makes a catalyst — is now carried by
    # requiring TWO flasks that had something added and did nothing: the sand
    # (a solid) and the acid (a liquid). That is a strictly harder condition
    # to satisfy by accident than "one trial is faster and uncatalysed", and
    # it is the point the ruling put in the lesson's mouth.
    inert = [tr for tr in trials[1:]
             if not tr.get("catalyst") and tr["id"] not in faster]
    if len(inert) < 2:
        raise ValueError(
            "catalyst-bench %r has %d flask(s) that had something added and "
            "changed nothing. Two are needed. Without a second one the bench "
            "lets a student conclude that adding something is what makes a "
            "catalyst — and the two have to be different KINDS of thing "
            "(Design draws a solid and a liquid), so that the conclusion "
            "cannot survive as 'adding a powder is what matters' either."
            % (act_id, len(inert)))

    first = trials[0]["id"]

    tabs = "".join(
        _c6_seg("ks3-catb-tab", tr["id"] == first, tr.get("label", ""),
                data_catb_tab=tr["id"]) for tr in trials)
    titles = "".join(
        '<p class="ks3-catb-title"%s data-catb-title="%s">%s</p>'
        % ("" if tr["id"] == first else " hidden", e(tr["id"]), t(tr["label"]))
        for tr in trials)
    setups = "".join(
        '<p class="ks3-catb-setup"%s data-catb-setup="%s">%s</p>'
        % ("" if tr["id"] == first else " hidden", e(tr["id"]), rich(tr["setup"]))
        for tr in trials)

    predict = ('<div class="ks3-catb-predict" data-catb-predictrow>'
               '<p class="ks3-commit">%s</p>'
               '<div class="ks3-catb-predictopts">%s</div></div>'
               % (t(a.get("predict_prompt", "")),
                  "".join(_c6_seg("ks3-catb-predictopt", False,
                                  p.get("label", ""), data_catb_predict=p["id"])
                          for p in predicts)))

    results = "".join(
        '<div class="ks3-catb-result" hidden data-catb-result="%s">'
        '<p class="ks3-catb-verdict">%s</p>'
        '<div class="ks3-catb-tiles">'
        '<div class="ks3-catb-tile"><p class="ks3-catb-tilelabel">%s</p>'
        '<p class="ks3-catb-value">%s</p></div>'
        '<div class="ks3-catb-tile"><p class="ks3-catb-tilelabel">%s</p>'
        '<p class="ks3-catb-value">%s</p></div></div>'
        '<p class="ks3-catb-figsnote">%s</p>'
        '<p class="ks3-catb-why">%s</p></div>'
        % (e(tr["id"]), rich(tr["result"]),
           t(a.get("volume_label", "")), t(tr["volume"]),
           t(a.get("mass_label", "")), t(tr["mass"]),
           rich(a["figures_note"]), rich(tr["why"]))
        for tr in trials)

    closer = ""
    if close.get("id") and close.get("paras"):
        closer = ('<div class="ks3-catb-close" id="%s" hidden data-catb-close>'
                  '<p class="ks3-catb-closetitle">%s</p>%s</div>'
                  % (e(close["id"]), t(close.get("title", "")),
                     "".join("<p>%s</p>" % rich(p) for p in close["paras"])))

    return ('<div class="ks3-catb" data-catb data-total="%d">'
            '<div class="ks3-catb-tabs">%s</div>'
            '<div class="ks3-catb-panel">%s%s%s%s</div>%s</div>'
            % (len(trials), tabs, titles, setups, predict, results, closer))


# ═══ c6-05 · step-rig (#s-rig) ════════════════════════════════════════════

def r_step_rig(a, act_id):
    """⊕ c6-05 `#s-rig` — five steps of a method, revealed one at a time.

    ⚖️ **THE STAGING IS THE TEACHING, NOT A FLOURISH.** Design's own lead says
    what the block is for: "Each step has a reason, and each reason is a way
    this test can be got wrong." A method printed whole is a recipe a student
    copies; a method that arrives one reason at a time is five chances to
    predict the reason before reading it. The `what` of every step is on the
    page from the start — nothing is hidden that a student needs in order to
    follow the sequence — and only the `why` is staged.

    ⚖️ ONE-WAY, AND THERE IS NO COLLAPSE. `r_fifa`'s ruling, for its reason:
    unshowing a step teaches nothing and gives a student a way to lose their
    place.

    ⚠️ THE BUTTON'S THREE LABELS ARE EMITTED TOGETHER AND ONE IS SHOWN. Design
    composes them — `s.stepsOpen >= STEPS.length ? 'All five shown' :
    (s.stepsOpen === 0 ? 'Reveal the first step' : 'Reveal the next step')` —
    which is three authored sentences assembled by ternary. Emit-both-show-one
    keeps all three as authored strings, so the resting render cannot disagree
    with the runtime one and an em dash or a `<strong>` would survive.

    ⚑ THE COUNT IS THE BLOCK HEAD'S. Design draws "N of 5 revealed" as a mono
    uppercase line beside the button; the block head's `head_counter` is that
    same component in Design's own treatment, right-aligned on the eyebrow
    row, and routing it there is what every live count in C6 already does. The
    denominator comes from the payload (`KIND_HEAD_TOTAL`), never from a
    number an author types twice.

    ⚠️ NOTHING HERE MARKS. There is no right answer in this block — it is a
    method, not a question — so there is no `data-correct`, no colour that
    means anything, and the only state a step carries is `data-open`, which
    says "you have been here".

    ── THE CONTENT-TRUTH ASSERTIONS (§5A) ───────────────────────────────

    Walked over every step rather than sampled:

      1. Every step is a `what` AND a `why`. A step with no reason is the
         recipe this block exists not to be.
      2. No two steps share a `what`, and no two share a `why`. Design's page
         composes nothing here, but the failure this catches is a copy-paste
         during authoring: two steps with one reason is a button that appears
         to do nothing when it is pressed, and it reads as normal in the
         source.
      3. The three labels are all present and all DIFFERENT. Two identical
         labels means a student presses the button and cannot tell whether it
         worked.

    ⚠️ THE RESTING RENDER: five steps, every `what` visible, every `why`
    hidden, the button carrying the FIRST label, the head counter reading
    zero, `data-stage-done="0"`.

    HOOKS: `data-srig` (wrapper, with `data-total`) · `data-srig-step`
    (valued with the step id, carrying `data-open`) · `data-srig-why` ·
    `data-srig-reveal` (the button) · `data-srig-label` (valued
    `first` / `next` / `all`).
    """
    steps = a.get("steps") or []
    labels = a.get("labels") or {}

    if len(steps) < 4:
        raise ValueError(
            "step-rig %r has %d step(s). A method a student can hold in one "
            "glance does not need staging, and staging it would be a "
            "flourish rather than five predictions." % (act_id, len(steps)))

    seen, whats, whys = set(), {}, {}
    for st in steps:
        _c6_need(st, st.get("id"), "step-rig step", ("id", "what", "why"),
                 "Every step is what you do and why it is there; the reasons "
                 "are the whole block, and a step with none is a line of a "
                 "recipe.")
        if st["id"] in seen:
            raise ValueError(
                "step-rig %r authors step id %r twice. Two steps with one "
                "name is one unreachable step." % (act_id, st["id"]))
        seen.add(st["id"])
        for field, bag in (("what", whats), ("why", whys)):
            text = str(st[field]).strip()
            if text in bag:
                raise ValueError(
                    "step-rig %r gives steps %r and %r the same %r. A "
                    "repeated reason is a press that appears to do nothing, "
                    "and it reads as entirely normal in the source."
                    % (act_id, bag[text], st["id"], field))
            bag[text] = st["id"]

    want = ("first", "next", "all")
    for key in want:
        if not labels.get(key):
            raise ValueError(
                "step-rig %r has no %r label. The button says three different "
                "things across its life and all three are authored sentences, "
                "not one composed by ternary." % (act_id, key))
    if len({str(labels[k]) for k in want}) != len(want):
        raise ValueError(
            "step-rig %r repeats a button label: %r. A button whose words do "
            "not change when it is pressed cannot tell a student it worked."
            % (act_id, [labels[k] for k in want]))

    items = "".join(
        '<li class="ks3-srig-step" data-srig-step="%s" data-open="0">'
        '<div class="ks3-srig-head">'
        '<span class="ks3-srig-num" aria-hidden="true">%d</span>'
        '<p class="ks3-srig-what">%s</p></div>'
        '<p class="ks3-srig-why" hidden data-srig-why>%s</p></li>'
        % (e(st["id"]), i + 1, rich(st["what"]), rich(st["why"]))
        for i, st in enumerate(steps))

    button = ('<button type="button" class="ks3-seg-btn ks3-srig-reveal" '
              'data-srig-reveal>%s</button>'
              % "".join('<span class="ks3-srig-label"%s data-srig-label="%s">'
                        '%s</span>'
                        % ("" if key == "first" else " hidden", key,
                           t(labels[key]))
                        for key in want))

    return ('<div class="ks3-srig" data-srig data-total="%d">'
            '<ol class="ks3-srig-list" role="list">%s</ol>'
            '<div class="ks3-srig-controls">%s</div></div>'
            % (len(steps), items, button))


# ═══ c6-05 · solid-sorter (#s-bench) ══════════════════════════════════════

def r_solid_sorter(a, act_id):
    """⊕ c6-05 `#s-bench` — four white solids, and only the acid can tell.

    ⚖️ **THE BENCH IS AN ARGUMENT ABOUT EVIDENCE, NOT A QUIZ ABOUT
    CARBONATES.** Three of the four look the same in the bottle and one of
    them does nothing; the fourth is green and fizzes hardest. So neither
    "white powder" nor "looks like a rock" survives the bench, and what is
    left is the test. The `looks` tag on every row is doing that work and is
    not decoration.

    ⚖️ ONE COMMITMENT PER SOLID AND IT IS FINAL — `c3CommitCards`' contract,
    the same one `bottle-sorter` takes four sections earlier in the same unit.
    The reply is on screen the instant the solid is decided, so a second press
    would be a student choosing an answer they can already read.

    ⚠️ NOTHING HERE MARKS. Design composes the verdict headline as
    `row.isCarb ? 'It fizzes — this one is a carbonate.' : 'No fizzing. Not a
    carbonate.'`, which makes three of the four verdicts literally one string
    and puts a flag into a sentence by ternary. All four are authored, the
    same sentence whichever button was pressed, and `answer` reaches no
    markup at all — it is read HERE, so keeping the flag on the record cannot
    quietly mean keeping it wrong.

    ── THE CONTENT-TRUTH ASSERTIONS (§5A) ───────────────────────────────

    Five, walked over every solid rather than sampled, because the rule the
    page argues — *acid + carbonate makes salt + water and CARBON DIOXIDE* —
    is stated once in a key fact and demonstrated four times here, and nothing
    else in the build could see the two disagree:

      1. Every `answer` names one of the options actually offered.
      2. Every option offered is the answer to at least one solid. Without a
         solid that does nothing there is no rule, only three examples, and
         the "No reaction" button would be a control nothing is ever an
         example of.
      3. A REACTING solid carries an equation and a non-reacting one carries
         none. Writing products for a reaction that never happens is the
         error `#s-think` and rung 2 are both about.
      4. Every reacting solid's products name WATER and CARBON DIOXIDE, and
         its reactants name an ACID. Three products, not two, asserted on
         every row rather than stated once in the key fact and hoped for.
      5. Every verdict agrees with its flag: a non-reacting solid's verdict
         says it is not a carbonate, and a reacting solid's does not. The flag
         is the author's intent and the verdict is what the student reads;
         when they disagree the page states the wrong classification.

    ⚠️ THE RESTING RENDER: four solids, nothing pressed, no reveal open, the
    head counter reading zero, `data-stage-done="0"`.

    HOOKS: `data-solid` (wrapper, with `data-total`) · `data-solid-card`
    (valued with the solid id, carrying `data-open`) · `data-solid-opt`
    (valued with the option id) · `data-solid-reveal`.
    """
    options = a.get("options") or []
    solids = a.get("solids") or []

    if len(options) < 2:
        raise ValueError(
            "solid-sorter %r offers %d option(s). The bench asks whether the "
            "acid will do anything, and a question with one answer is a "
            "caption." % (act_id, len(options)))
    if len(solids) < 3:
        raise ValueError(
            "solid-sorter %r declares %d solid(s). The block's whole shape is "
            "several things that look alike being told apart by one test, and "
            "two of them cannot look alike as a group." % (act_id, len(solids)))

    option_ids = [o["id"] for o in options]
    reacting = [o["id"] for o in options if o.get("reacts")]
    if len(reacting) != 1:
        raise ValueError(
            "solid-sorter %r flags %d option(s) as the reacting one: %r. "
            "Exactly one has to be, or the build cannot tell an equation that "
            "is MISSING from one that is correctly absent."
            % (act_id, len(reacting), reacting))
    reacts = reacting[0]

    seen, answered, negatives = set(), set(), 0
    for s in solids:
        _c6_need(s, s.get("id"), "solid-sorter solid",
                 ("id", "name", "looks", "answer", "verdict", "why"),
                 "A solid is a name, what it looks like, a commitment and a "
                 "reply; one missing any of them opens on nothing.")
        if s["id"] in seen:
            raise ValueError(
                "solid-sorter %r authors solid id %r twice. Two solids with "
                "one name is one unreachable solid." % (act_id, s["id"]))
        seen.add(s["id"])
        if s["answer"] not in option_ids:
            raise ValueError(
                "solid-sorter %r solid %r answers %r, which is not one of the "
                "options %r. The record has to know which answer is right "
                "even though the markup never says."
                % (act_id, s["id"], s["answer"], option_ids))
        answered.add(s["answer"])

        left = str(s.get("eq_left") or "").strip()
        right = str(s.get("eq_right") or "").strip()
        verdict = str(s["verdict"]).lower()

        if s["answer"] == reacts:
            if not (left and right):
                raise ValueError(
                    "solid-sorter %r solid %r reacts but carries no equation. "
                    "The bench's four rows are where the rule is "
                    "demonstrated; a reacting row with nothing written is the "
                    "claim made and not shown." % (act_id, s["id"]))
            for want in ("water", "carbon dioxide"):
                if want not in right.lower():
                    raise ValueError(
                        "solid-sorter %r solid %r gives products %r, which "
                        "never say %r. The page's rule is THREE products, not "
                        "two, and this row is one of the four places it is "
                        "shown rather than asserted."
                        % (act_id, s["id"], right, want))
            if "acid" not in left.lower():
                raise ValueError(
                    "solid-sorter %r solid %r names reactants %r with no acid "
                    "in them. Every row on this bench is a carbonate meeting "
                    "an acid." % (act_id, s["id"], left))
            if "not a carbonate" in verdict:
                raise ValueError(
                    "solid-sorter %r solid %r is flagged as reacting and its "
                    "verdict reads %r. The flag is the author's intent and "
                    "the verdict is what the student reads; when they "
                    "disagree the page states the wrong classification and "
                    "nothing else in the build can see it."
                    % (act_id, s["id"], s["verdict"]))
        else:
            negatives += 1
            if left or right:
                raise ValueError(
                    "solid-sorter %r solid %r does not react and carries an "
                    "equation anyway (%r / %r). Writing products for a "
                    "reaction that never happens is exactly what rung 2 is "
                    "about." % (act_id, s["id"], left, right))
            if "not a carbonate" not in verdict:
                raise ValueError(
                    "solid-sorter %r solid %r is flagged as doing nothing but "
                    "its verdict reads %r, which never says it is not a "
                    "carbonate. A negative row that does not say so is the "
                    "one row on this bench a student cannot read."
                    % (act_id, s["id"], s["verdict"]))

    missing = [i for i in option_ids if i not in answered]
    if missing:
        raise ValueError(
            "solid-sorter %r offers option(s) %s that no solid is an example "
            "of. A button that is never the answer is a control that does "
            "nothing." % (act_id, missing))
    if not negatives:
        raise ValueError(
            "solid-sorter %r has no solid that does nothing. Without a "
            "negative row there is no rule, only examples, and 'white powder' "
            "would still be doing the identifying." % act_id)

    cards = []
    for s in solids:
        buttons = "".join(
            _c6_seg("ks3-solid-opt", False, o.get("label", ""),
                    data_solid_opt=o["id"])
            for o in options)
        eq = ""
        if s["answer"] == reacts:
            eq = ('<p class="ks3-solid-eq">'
                  '<span>%s</span>%s<span>%s</span></p>'
                  % (t(s["eq_left"]), _c6_arrow("ks3-solid-arrow"),
                     t(s["eq_right"])))
        cards.append(
            '<div class="ks3-solid-card" data-solid-card="%s" data-open="0">'
            '<div class="ks3-solid-head">'
            '<p class="ks3-solid-name">%s</p>'
            '<p class="ks3-solid-looks">%s</p></div>'
            '<div class="ks3-solid-opts">%s</div>'
            '<div class="ks3-solid-reveal" hidden data-solid-reveal>'
            '<p class="ks3-solid-verdict">%s</p>'
            '<p class="ks3-solid-why">%s</p>%s</div></div>'
            % (e(s["id"]), t(s["name"]), t(s["looks"]), buttons,
               rich(s["verdict"]), rich(s["why"]), eq))

    return ('<div class="ks3-solid" data-solid data-total="%d">'
            '<div class="ks3-solid-cards">%s</div></div>'
            % (len(solids), "".join(cards)))


# ── registrations ────────────────────────────────────────────────────────
#
# Ten instrument families and ONE drawn figure. Every family below is placed
# by at least one C6 lesson and every kind those lessons place is registered
# here — the two halves of `check_placements`' gates 2 and 3.
#
# `acid-judgements` is ONE family placed SIX times, on c6-01 `#s-hazard`,
# c6-02 `#s-choose`, c6-03 `#s-uses`, c6-04 `#s-test`, c6-05 `#s-world` and
# c6-07 `#s-uses`. See its docstring: Design draws the identical component on
# six of the seven pages, and C3's `sequence-rebuild` is the precedent for one
# family placed more than once.
#
# ⊕ MRB-281, 23 Aug 2026 — `step-rig` AND `solid-sorter` ARE NOW REGISTERED.
# This comment used to say the opposite, and it is rewritten rather than
# deleted because its reasoning was correct and its PREMISE stopped being
# true: they belong to Design's `c6-05 acids-and-carbonates`, and
# `structure.py` had no slot for it. It has one now — the dead
# `acid-plus-alkali` slot was renamed in place — the lesson is authored, and
# both families are placed. Registering a family nothing places is still gate
# 2, and gate 2 is still right.
#
# Every family ticks a rail stop, so every one carries `data-stage-done="0"` —
# NOTHING IS TICKED ON LOAD (MRB-208). `data-instrument` keeps the shell's
# `wirePredictions` out of the benches' own prediction and guess options.
#
# SEGMENTS, measured off Design's own markup and for the commander's
# `_INSTRUMENT_SEGMENTS` map: every anchored instrument section in all seven
# lessons is a light `ks3-block` with no second class, so every one of them is
# `check`. There is no ink-dark practical block anywhere in C6.

ART = {
    'ph-strip': _ph_strip,
}

KIND_SHELL = {
    'bottle-sorter': ("ks3-bottle-block", ' data-instrument data-bottleblock data-stage-done="0"'),
    'acid-judgements': ("ks3-ajudge-block", ' data-instrument data-ajudgeblock data-stage-done="0"'),
    'ph-bench': ("ks3-phbench-block", ' data-instrument data-phbenchblock data-stage-done="0"'),
    'titration-dial': ("ks3-titr-block", ' data-instrument data-titrblock data-stage-done="0"'),
    'acid-metal-grid': ("ks3-amgrid-block", ' data-instrument data-amgridblock data-stage-done="0"'),
    'salt-namer': ("ks3-namer-block", ' data-instrument data-namerblock data-stage-done="0"'),
    'method-order': ("ks3-morder-block", ' data-instrument data-morderblock data-stage-done="0"'),
    'catalyst-bench': ("ks3-catb-block", ' data-instrument data-catbblock data-stage-done="0"'),
    'step-rig': ("ks3-srig-block", ' data-instrument data-srigblock data-stage-done="0"'),
    'solid-sorter': ("ks3-solid-block", ' data-instrument data-solidblock data-stage-done="0"'),
}

KIND_FN = {
    'bottle-sorter': r_bottle_sorter,
    'acid-judgements': r_acid_judgements,
    'ph-bench': r_ph_bench,
    'titration-dial': r_titration_dial,
    'acid-metal-grid': r_acid_metal_grid,
    'salt-namer': r_salt_namer,
    'method-order': r_method_order,
    'catalyst-bench': r_catalyst_bench,
    'step-rig': r_step_rig,
    'solid-sorter': r_solid_sorter,
}

# The head counter's denominator comes from the PAYLOAD rather than from a
# number an author types twice. Six of the ten draw one; the pH bench, the
# titration dial, the naming bench and the method builder do not — Design
# draws a live lead sentence on the first three and a placed-count on the
# fourth, and both are inside the instrument rather than in the block head.
KIND_HEAD_TOTAL = {
    'bottle-sorter': lambda a: len(a.get("bottles") or []),
    'acid-judgements': lambda a: len(a.get("items") or []),
    'acid-metal-grid': lambda a: len(a.get("cells") or []),
    'catalyst-bench': lambda a: len(a.get("trials") or []),
    'step-rig': lambda a: len(a.get("steps") or []),
    'solid-sorter': lambda a: len(a.get("solids") or []),
}
