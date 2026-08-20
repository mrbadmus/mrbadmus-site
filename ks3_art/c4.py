"""ks3_art.c4 — C4's drawers, instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C4 is *Chemical reactions*: 5 lessons and
12 instrument families, all DOM, no canvas anywhere in the unit.

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

  · Every C4 instrument sits in a LIGHT ``ks3-block``. There is no ink-dark
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
    _SVG_INK,
    _SVG_INK_BODY,
    _SVG_INK_MUTED,
    _SVG_INSET,
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
# ═══ c4-01 · change-pairs, chain-build ═══════════════════════════════════
#
# Two families, both DOM, no canvas, no drawn figure — this lesson's picture
# is six cards of words either side of a line, which is what a CONTRAST page
# draws instead of a diagram.
#
# Both sit in a LIGHT `ks3-block` (measured off Design's own markup: `#s-pairs`
# and `#s-chain` carry `class="ks3-block"` and nothing else), both tick a rail
# stop, so both ship `data-stage-done="0"` and NOTHING is ticked on load.
#
# ⚠️ ONLY THE LADDER MARKS. Neither family emits `data-correct`, and nothing
# green or red reaches any control in either of them. A committed side keeps
# the ordinary pressed treatment and its spent sibling dims; the verdict is a
# PANEL OF WORDS, in the same voice whichever button was pressed.


def _cpair_seg(label, hook, value):
    """One verdict button — Physical / Chemical.

    `.ks3-seg-btn` is the key stage's ONE segmented control (the Drift-4
    ruling), with a family class beside it for layout. `aria-pressed` is a
    WORD, not colour alone (R2), and there is no `correct` parameter here and
    must never be one (R3).
    """
    return ('<button type="button" class="ks3-seg-btn ks3-cpair-opt" '
            '%s="%s" aria-pressed="false">%s</button>'
            % (hook, e(value), t(label)))


def r_change_pairs(a, act_id):
    """⊕ c4-01 `#s-pairs` — three pairs, six commitments, one question.

    ⚖️ **THE PAIRING IS THE ARGUMENT AND IT IS LOAD-BEARING IN THE MARKUP.**
    NOTES-C4 §2: each pair is chosen so the *visible* clue appears on BOTH
    sides — heat twice, a solid vanishing into a liquid twice, colour twice.
    So this is three PAIR panels of two sides each, never six independent
    cards in one grid: a student who can see the two halves of a pair beside
    each other is being shown that the clue they share settles nothing, and a
    six-up grid loses exactly that.

    ⚖️ ONE COMMITMENT PER SIDE AND IT IS FINAL. Both buttons on a side disable
    when either is pressed — not to punish a change of mind, but because the
    evidence and the verdict are on screen by then and a second press would be
    a student choosing an answer they can already read. Design's own click
    guard does the same (page line 566): the handler re-checks `st.verdicts`
    and returns null.

    ⚠️ `chemical` IS IN THE PAYLOAD AND IS EMITTED NOWHERE. It is Design's own
    classification of each side and it is the ANSWER; putting it in the
    document — as `data-correct`, as a class, as anything — would let the page
    mark a commitment, and R3 reserves marking for the mastery ladder alone.
    The verdict panel carries the answer in words, after the commitment, and
    that is the only route it takes.

    ⚠️ THE ORDER OF THE THREE EVIDENCE LINES IS THE ARGUMENT TOO — does it
    come back, has it new properties, what happened to the mass — so they are
    rendered in the authored order and never sorted or filtered.

    IDS EMITTED, and they are a contract with the misconception register
    (MRB-244/248): `pair-{n}-commit` on the pair's sides row, which is where
    the student commits on both halves of that pair, and
    `pair-{n}-reveal-{side}` on each side's opened panel. `REACT-02` names
    `pair-2-commit` and `pair-2-reveal-marble`, and both resolve here.

    HOOKS: `data-cpair` (wrapper, with `data-total`) · `data-cpair-side` (a
    side card, valued with the side id) · `data-cpair-opt` (a verdict button,
    valued 0/1 to index `options`) · `data-cpair-reveal` · `data-cpair-close`.
    """
    pairs = a.get("pairs") or []
    options = a.get("options") or []
    if not pairs:
        raise ValueError("change-pairs %r declares no pairs[]." % act_id)
    if len(options) != 2:
        raise ValueError(
            "change-pairs %r offers %d option(s); it is a choice of two — "
            "physical or chemical — and the whole lesson is built on there "
            "being exactly those two answers." % (act_id, len(options)))

    total = 0
    blocks = []
    for n, pair in enumerate(pairs, start=1):
        sides = pair.get("sides") or []
        if len(sides) != 2:
            raise ValueError(
                "change-pairs %r pair %r has %d side(s). A pair is two, and "
                "the shared clue it exists to show cannot appear on both "
                "sides of one." % (act_id, pair.get("id"), len(sides)))

        # ── THE CONTENT-TRUTH ASSERTION (§5A), AND WHAT `chemical` IS FOR ──
        #
        # `chemical` is emitted NOWHERE — see the docstring; it is the answer
        # and R3 reserves marking for the ladder. That left it as authored
        # correctness data read by nothing, which `ks3_key_audit.py` is right
        # to call dead: a key with no read site is content that never reaches
        # a student AND an invariant nothing is checking.
        #
        # So it is read HERE, at build time, and it guards the two things the
        # instrument's whole argument rests on. It walks EVERY side, not a
        # sample:
        #
        #   1. A PAIR IS ONE OF EACH. If both sides of a pair were chemical,
        #      the pair would no longer show that a shared clue settles
        #      nothing — it would show two reactions that look alike, which is
        #      a different lesson and a true sentence about a false page.
        #   2. THE FLAG AND THE PROSE AGREE. `verdict` is what the student
        #      reads after committing; `chemical` is what the author meant.
        #      If those two ever disagree the page tells a student they were
        #      wrong when they were right, and nothing else in the build could
        #      see it — the flag is invisible and the prose is just a string.
        #
        # This is what turns Design's unrendered classification from dead
        # correctness data into a guard on the chemistry. It fails the BUILD,
        # loudly, rather than failing a student quietly.
        flags = [bool(sd.get("chemical")) for sd in sides]
        if sorted(flags) != [False, True]:
            raise ValueError(
                "change-pairs %r pair %r has both sides marked %s. Every pair "
                "is one reaction and one non-reaction — that contrast IS the "
                "instrument, and a pair of two alike shows nothing."
                % (act_id, pair.get("id"),
                   "chemical" if flags[0] else "physical"))
        for sd in sides:
            said = (sd.get("verdict") or "").strip().lower()
            want = "chemical" if sd.get("chemical") else "physical"
            if not said.startswith(want):
                raise ValueError(
                    "change-pairs %r side %r is flagged %s but its verdict "
                    "opens %r. The flag is the author's intent and the verdict "
                    "is what the student reads; when they disagree the page "
                    "marks a correct commitment wrong."
                    % (act_id, sd.get("id"), want, sd.get("verdict")))

        cards = []
        for side in sides:
            for key in ("name", "what", "verdict", "why"):
                if not side.get(key):
                    raise ValueError(
                        "change-pairs %r side %r has no %r. Every side opens "
                        "a verdict the instant it is decided; a side with "
                        "nothing to reveal is a commitment that goes "
                        "nowhere." % (act_id, side.get("id"), key))
            if not side.get("evidence"):
                raise ValueError(
                    "change-pairs %r side %r carries no evidence[]. The three "
                    "tests ARE the answer to 'how would you know', and a "
                    "verdict with no evidence under it is an assertion."
                    % (act_id, side.get("id")))
            total += 1

            tests = "".join(
                '<li class="ks3-cpair-test">'
                '<p class="ks3-cpair-testname">%s</p>'
                '<p class="ks3-cpair-testresult">%s</p></li>'
                % (t(ev.get("test", "")), rich(ev.get("result", "")))
                for ev in side["evidence"])
            btns = "".join(_cpair_seg(opt, "data-cpair-opt", str(j))
                           for j, opt in enumerate(options))
            cards.append(
                '<div class="ks3-cpair-side" data-cpair-side="%s">'
                '<p class="ks3-cpair-name">%s</p>'
                '<p class="ks3-cpair-what">%s</p>'
                '<div class="ks3-cpair-opts">%s</div>'
                '<div class="ks3-cpair-reveal" id="%s" hidden data-cpair-reveal>'
                '<ul class="ks3-cpair-tests" role="list">%s</ul>'
                '<div class="ks3-cpair-verdict">'
                '<p class="ks3-cpair-verdict-head">%s</p>'
                '<p class="ks3-cpair-why">%s</p></div></div></div>'
                % (e(side.get("id", "")), t(side["name"]),
                   rich(side["what"]), btns,
                   e("pair-%d-reveal-%s" % (n, side.get("id", ""))),
                   tests, t(side["verdict"]), rich(side["why"])))

        blocks.append(
            '<div class="ks3-cpair-pair" data-cpair-pair="%s">'
            '<p class="ks3-cpair-label">%s</p>'
            '<div class="ks3-cpair-sides" id="%s">%s</div></div>'
            % (e(pair.get("id", "")), t(pair.get("label", "")),
               e("pair-%d-commit" % n), "".join(cards)))

    # ⚠️ The closing panel is INSIDE the wrapper, not a sibling of it.
    # `c3CommitCards` resolves `sel.close` with `wrap.querySelector(...)`, so
    # a panel outside `[data-cpair]` is a panel that never opens — and it
    # would fail silently, because the six cards would all work.
    close = ('<div class="ks3-cpair-close" hidden data-cpair-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""
    return ('<div class="ks3-cpair" data-cpair data-total="%d">'
            '<div class="ks3-cpair-pairs">%s</div>%s</div>'
            % (total, "".join(blocks), close))


# ═══ c4-01 · chain-build ═════════════════════════════════════════════════

def _chain_lettered(options, hook, value):
    """A lettered A/B/C clause list, inside an instrument.

    The same markup the shell's `r_activity_options` emits — `.ks3-options` /
    `.ks3-option` with the letter as the resting mark — because Design draws
    the SAME control for a clause choice as for a prediction.

    ⚠️ It gets a hook of its own because the shell's `wirePredictions` refuses
    to touch anything inside `[data-instrument]`. An instrument owns every
    option inside it, which means it also has to wire them.
    """
    return ('<ul class="ks3-options" role="list" %s="%s">%s</ul>'
            % (hook, e(value),
               "".join(
                   '<li><button type="button" class="ks3-option" '
                   'data-i="%d" aria-pressed="false">'
                   '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
                   '<span class="ks3-opt-label">%s</span></button></li>'
                   % (i, option_letter(i), t(o))
                   for i, o in enumerate(options))))


def r_chain_build(a, act_id):
    """⊕ c4-01 `#s-chain` — the CONTRAST family's linked-comparison step.

    NOTES-C4 §2: this is "the one place in the unit where the model answer is
    shown in full". Two slots of three clauses; every one of the nine
    combinations is legal and none of them is wrong, which is the teaching.
    The note that follows branches on whether the two halves are LINKED — not
    on whether they are true — because the marks are for the comparison and
    every clause on offer is a true statement about wax.

    ⚖️ EMIT BOTH NOTES, SHOW ONE. Design's `chainNote` is a ternary over two
    long paragraphs; both are in the document from the first byte and the
    wiring unhides one. Nothing is assembled out of an attribute, so the
    `<strong>`, the quotation marks and the em dashes survive exactly as they
    were authored, and neither paragraph exists twice in two languages.

    ⚖️ THE SENTENCE IS READ OFF THE BUTTONS, NEVER OUT OF AN ATTRIBUTE. The
    two chosen clauses are already on the page, in the `.ks3-opt-label` of the
    pressed option, so `wireChainBuild` joins those two strings. That is the
    only version in which no clause is written down twice.

    ⚠️ AND THE SLOTS DO NOT LOCK. Design's handler sets the index and nothing
    else (page line 585), so a student may re-pick either half and watch the
    sentence and the note change. The rail stop ratchets — `markStage` never
    goes back — so re-picking cannot untick a stop that has been earned.

    ⚠️ `data-chain-ideal` is INDICES, not a sentence: it is the one thing the
    wiring has to recompute, and it is the pair of clause numbers that make
    the linked comparison. It is not a mark: no option is ticked, crossed,
    dimmed or coloured by it — it chooses which of the two authored notes is
    shown, and both notes are on the same ground in the same panel.

    HOOKS: `data-chain` (wrapper, with `data-chain-ideal`) · `data-chain-slot`
    (a clause list, valued with the slot id) · `data-chain-reveal` ·
    `data-chain-sentence` · `data-chain-note` (valued `ideal` / `other`).
    """
    slots = a.get("slots") or []
    if len(slots) != 2:
        raise ValueError(
            "chain-build %r has %d slot(s). It builds ONE sentence out of two "
            "halves, and the whole point is that the second half answers the "
            "first." % (act_id, len(slots)))
    if not a.get("model"):
        raise ValueError(
            "chain-build %r shows no model sentence. NOTES-C4 §2 makes this "
            "the one place in the unit where the full-marks answer is shown "
            "whole; without it the block asks for a comparison and never "
            "shows one." % act_id)
    notes = a.get("notes") or {}
    for key in ("ideal", "other"):
        if not notes.get(key):
            raise ValueError(
                "chain-build %r has no %r note. Both states are reachable on "
                "the first click, and a state with nothing to say is a reveal "
                "that opens empty." % (act_id, key))

    ideal = a.get("ideal") or {}
    rows = "".join(
        '<div class="ks3-chain-slot"><p class="ks3-chain-slotlabel">%s</p>'
        '%s</div>'
        % (t(s.get("label", "")),
           _chain_lettered(s.get("options") or [], "data-chain-slot",
                           s.get("id", "")))
        for s in slots)

    return ('<div class="ks3-chain-wrap" data-chain data-chain-ideal="%s">'
            '<div class="ks3-chain-slots">%s</div>'
            '<div class="ks3-chain-reveal" hidden data-chain-reveal>'
            '<p class="ks3-chain-eyebrow">%s</p>'
            '<p class="ks3-chain-sentence" data-chain-sentence></p>'
            '<p class="ks3-chain-note" hidden data-chain-note="ideal">%s</p>'
            '<p class="ks3-chain-note" hidden data-chain-note="other">%s</p>'
            '<p class="ks3-chain-modelhead">%s</p>'
            '<p class="ks3-chain-model">%s</p>'
            '</div></div>'
            % (e(",".join("%s:%s" % (s.get("id", ""),
                                     ideal.get(s.get("id"), -1))
                          for s in slots)),
               rows,
               t(a.get("sentence_label", "")),
               rich(notes["ideal"]), rich(notes["other"]),
               t(a.get("model_label", "")), rich(a["model"])))


# ── registrations for the commander to splice ────────────────────────────
#
# No drawer: this lesson has no figure, so there is no ART row.
#


# ── from art_02.py ─────────────────────────────────────
# ═══ c4-02 · atom-rearranger + impossible-ask ════════════════════════════
#
# Two families, both DOM, no canvas, both in a LIGHT `ks3-block` (measured off
# Design's markup: `class="ks3-block"` and nothing else on both sections).
# Between them they are the flagship of C4: the first shows a reaction taking
# atoms apart and putting them back, the second asks it for something the atoms
# cannot spell and is refused.
#
# ⚠️ NOTHING HERE COMPUTES A PICTURE AT RUN TIME. Every one of the nine stage
# views (3 reactions × 3 stages) and every one of the four verdict panels is
# rendered HERE, in full, and the JS does nothing but show one and hide the
# rest. That is EMIT-BOTH-SHOW-ONE taken to its end, and it buys three things:
# `<sub>` and `<strong>` and the em dashes survive exactly as authored; no
# sentence and no colour is duplicated between Python and JavaScript where the
# two could drift; and the RESTING DOM — what a crawler and a no-JS reader see
# — is the real stage 0 of the real first reaction rather than an empty box.
#
# There is consequently NO `data-cfg` on either family. Neither instrument has
# a number, a colour or a geometry that has to be recomputed, so neither gets a
# JSON payload; the only thing the JS reads is which reaction and which stage,
# and it reads those off the attributes below.


def _arr_formula(parts):
    """`[("H", 2), ("O", 1)]` -> `H<sub>2</sub>O`.

    A REAL `<sub>`, never a Unicode subscript — Design's C4 convention (NOTES
    §3) and the reason `rich()` admitted the tag on 20 Aug. The `1` is never
    printed, because nobody writes `H`₁.

    `t()` on the symbol, not `rich()`: a symbol is a label, and letting rich
    markup through here would let a formula carry emphasis.
    """
    out = []
    for sym, n in parts:
        out.append(t(sym))
        if int(n) > 1:
            out.append("<sub>%s</sub>" % t(n))
    return "".join(out)


def _arr_expand(parts):
    """`[("H", 2), ("O", 1)]` -> `["H", "H", "O"]`. The formula's own claim
    about which atoms are in the particle, in the order it makes it."""
    out = []
    for sym, n in parts:
        out.extend([sym] * int(n))
    return out


def _arr_tally(groups):
    """Every atom in a list of particles, counted. Returns `{symbol: n}`."""
    counts = {}
    for g in groups:
        for sym in g.get("atoms") or []:
            counts[sym] = counts.get(sym, 0) + 1
    return counts


def _arr_check(act_id, elements, reactions):
    """THE CONTENT-TRUTH ASSERTION, and it walks every particle and every
    element rather than sampling.

    ⚖️ CONSERVATION OF ATOMS *IS* THIS LESSON. A payload in which the products
    quietly held one more oxygen than the reactants would draw a picture that
    contradicts the key fact directly above it, and it would look completely
    normal — three coloured circles either way. So four things are checked
    here and the build stops on any of them:

      1. every particle's `formula` expands to exactly its own `atoms`, in
         order — so the caption under a picture cannot drift from the picture;
      2. every symbol used anywhere is in the element table, so no atom can be
         drawn in a fallback colour;
      3. the reactant tally equals the product tally, element by element, in
         BOTH directions — so a substance cannot appear or vanish;
      4. `counts[]` — which is what the table on the page prints — names every
         element that is actually present, once, with the number the tally
         gives, and names no element that is not.

    Rule 4 is the one that earns its keep. The table is the only place on the
    page where the numbers are readable AS NUMBERS (§5A), and it is authored
    separately from the atoms it describes.
    """
    if not reactions:
        raise ValueError(
            "atom-rearranger %r declares no reactions[]." % act_id)
    names = {}
    for sym, spec in (elements or {}).items():
        names[spec.get("name") or sym] = sym
    for rx in reactions:
        rid = rx.get("id")
        for side in ("reactants", "products"):
            groups = rx.get(side) or []
            if not groups:
                raise ValueError(
                    "atom-rearranger %r reaction %r has no %s."
                    % (act_id, rid, side))
            for g in groups:
                atoms = list(g.get("atoms") or [])
                spelled = _arr_expand(g.get("formula") or [])
                if spelled != atoms:
                    raise ValueError(
                        "atom-rearranger %r reaction %r: the formula %r "
                        "spells %s and the picture draws %s. The caption and "
                        "the circles under it are the same claim, and this is "
                        "the one place they can disagree."
                        % (act_id, rid, g.get("formula"), spelled, atoms))
                for sym in atoms:
                    if sym not in (elements or {}):
                        raise ValueError(
                            "atom-rearranger %r reaction %r draws a %r atom, "
                            "which is not in the element table — it would be "
                            "drawn in no colour at all."
                            % (act_id, rid, sym))
        before = _arr_tally(rx.get("reactants") or [])
        after = _arr_tally(rx.get("products") or [])
        if before != after:
            raise ValueError(
                "atom-rearranger %r reaction %r does not conserve atoms: "
                "before %s, after %s. This instrument exists to show that "
                "those two are always the same."
                % (act_id, rid, sorted(before.items()), sorted(after.items())))
        rows = rx.get("counts") or []
        seen = set()
        for row in rows:
            sym = names.get(row.get("el"))
            if sym is None:
                raise ValueError(
                    "atom-rearranger %r reaction %r counts %r, which is not "
                    "the name of any element in the table."
                    % (act_id, rid, row.get("el")))
            if sym in seen:
                raise ValueError(
                    "atom-rearranger %r reaction %r counts %r twice."
                    % (act_id, rid, row.get("el")))
            seen.add(sym)
            if int(row.get("n", -1)) != before.get(sym):
                raise ValueError(
                    "atom-rearranger %r reaction %r says %s %s and the "
                    "picture draws %s of them."
                    % (act_id, rid, row.get("n"), row.get("el"),
                       before.get(sym)))
        missing = sorted(set(before) - seen)
        if missing:
            raise ValueError(
                "atom-rearranger %r reaction %r draws %s and the atom-count "
                "table never mentions %s. Every element on the bench is in "
                "the count, or the count is not the budget."
                % (act_id, rid, sorted(before), missing))


def _arr_atom(elements, sym, small):
    """One labelled circle.

    ⚠️ THE COLOUR IS THE ONLY THING INLINE. Design composes the whole
    declaration in `atomSpan()` — size, radius, hairline, mono, weight — and
    all of that is identical for every atom on the page, so it belongs to
    `.ks3-arr-atom` in the stylesheet and the small variant to
    `.ks3-arr-atom.is-small`. What genuinely varies per atom is the fill and
    the ink on it, and those come from the ONE element table (NOTES §3).

    `e()` on both, because this is an attribute value and `t()` may emit an
    SVG mark carrying double quotes.
    """
    spec = elements[sym]
    return ('<span class="ks3-arr-atom%s" style="background:%s;color:%s">'
            '%s</span>'
            % (" is-small" if small else "",
               e(spec["colour"]), e(spec["ink"]), t(sym)))


def _arr_lettered(options, hook, name):
    """A lettered A/B/C commit list inside an instrument.

    The same markup `r_activity_options` emits, because Design draws the SAME
    control for a prediction whether it stands alone in a block or sits inside
    a bench.

    ⚠️ It needs a hook of its own: the shell's `wirePredictions` refuses to
    touch anything inside `[data-instrument]`, so an instrument that owns
    options also has to wire them.

    ⚠️ NO `data-correct`, HERE OR ANYWHERE. These gates are commitments. The
    answer arrives as the next stage of the picture, not as a mark.
    """
    return ('<ul class="ks3-options" role="list" %s>%s</ul>'
            % (hook,
               "".join(
                   '<li><button type="button" class="ks3-option" '
                   'data-%s="%d" aria-pressed="false">'
                   '<span class="ks3-opt-mark" aria-hidden="true">%s</span>'
                   '<span class="ks3-opt-label">%s</span></button></li>'
                   % (e(name), i, option_letter(i), t(o))
                   for i, o in enumerate(options))))


def r_atom_rearranger(a, act_id):
    """⊕ c4-02 `#s-rearr` — break the joins, count the atoms, make new ones.

    Three reactions × three stages, and the middle stage is the reason the
    instrument exists.

    ⚖️ **THE LOOSE-ATOM STAGE SAYS OUT LOUD THAT IT IS NOT REAL, AND THAT
    SENTENCE STAYS.** "Every join has been broken and nothing else has been
    done. This stage is not real — no chemist ever sees it — but it is the
    honest way to see what a reaction has to work with." A model that admits
    what it is is worth more than a tidier one that does not, and this is the
    only view in which the atom budget is a countable set of objects on a
    table. Shortening it to "the joins are broken" would buy a smoother read
    at the cost of the one true thing the picture is for.

    ⚖️ THE GATE IS A COMMITMENT, NOT A MARKED QUESTION. It stands between
    stage 1 and stage 2 — after the atoms are loose and countable, before the
    products exist — and it is answered by the products themselves. No option
    carries a correctness flag, nothing green or red reaches one, and the
    verdict is `product_text`: a panel of words saying what was actually
    built. ONLY THE LADDER MARKS.

    ⚠️ AMBER, AND WHY IT IS RIGHT HERE. Design grounds the gate in
    `--ks3-alert-tint`. That is amber carrying its ruled meaning: every wrong
    option in it is a wrong idea about how many atoms there are ("Four — one
    for each hydrogen"), offered a beat before the next stage takes it apart.
    It is not a category, not a selection and not a reading.

    ⚠️ THE `role="img"` LABEL IS PER VIEW, NOT PER PLATE. Design puts one
    `aria-label` on the outer box and recomposes it in `lessonVals`. Here each
    of the nine views carries its own, written at build time from the payload's
    own template with the PARTICLE COUNT filled in — so the label can never
    describe a stage other than the one on screen, the stage heading above it
    stops being swallowed by the image role, and no sentence has to survive a
    trip through a `data-` attribute.

    ⚠️ THE "AFTER" COLUMN EMITS BOTH READINGS AND SHOWS ONE. An em dash while
    there are no products, the tallied number once there are. Neither is
    composed at run time, so the accent-text treatment on the number is a
    stylesheet rule on a class rather than a colour assembled in JavaScript.

    HOOKS: `data-arr` (wrapper, with `data-total`) · `data-arr-tab` (a
    reaction button, valued with its id) · `data-arr-words` (the word equation,
    valued with the reaction id) · `data-arr-stagename` (valued 0/1/2) ·
    `data-arr-groups` (a stage view, valued `<rx>|<stage>`) ·
    `data-arr-counts` (a `<tbody>`, valued with the reaction id) ·
    `data-arr-pending` / `data-arr-num` (the two readings of one After cell) ·
    `data-arr-stagetext` (valued `0`, `1` or `2|<rx>`) · `data-arr-gate`
    (valued with the reaction id) · `data-arr-gateopts` / `data-arr-gateopt` ·
    `data-arr-advance` with `data-arr-adv` on its two labels ·
    `data-arr-reset` · `data-arr-done`.
    """
    elements = a.get("elements") or {}
    reactions = a.get("reactions") or []
    _arr_check(act_id, elements, reactions)

    stage = int(a.get("stage") or 0)
    if stage != 0:
        raise ValueError(
            "atom-rearranger %r opens at stage %d. It opens at 0 or the "
            "resting page shows a reaction half taken apart that nobody asked "
            "to take apart — and MRB-208's ratchet starts from nothing done."
            % (act_id, stage))

    names = a.get("stage_names") or []
    texts = a.get("stage_texts") or []
    labels = a.get("stage_labels") or []
    if len(names) != 3 or len(labels) != 3 or len(texts) != 2:
        raise ValueError(
            "atom-rearranger %r needs three `stage_names`, three "
            "`stage_labels` and two `stage_texts` — the third stage's text is "
            "each reaction's own `product_text`, and there is no fallback for "
            "a reaction that has none." % act_id)
    adv = a.get("advance_labels") or []
    if len(adv) != 2:
        raise ValueError(
            "atom-rearranger %r needs two `advance_labels`, one per move."
            % act_id)
    heads = a.get("count_headings") or {}
    first = reactions[0]["id"]

    # ── the reaction dial ────────────────────────────────────────────────
    tabs = "".join(
        '<button type="button" class="ks3-seg-btn ks3-arr-tab" '
        'data-arr-tab="%s" aria-pressed="%s">%s</button>'
        % (e(rx["id"]), "true" if rx["id"] == first else "false",
           t(rx.get("tab", "")))
        for rx in reactions)

    # ── the word equation, one per reaction ──────────────────────────────
    words = "".join(
        '<p class="ks3-arr-words"%s data-arr-words="%s">%s</p>'
        % ("" if rx["id"] == first else " hidden", e(rx["id"]),
           rich(rx.get("words", "")))
        for rx in reactions)

    # ── the plate: three stage headings and nine views ───────────────────
    stagenames = "".join(
        '<p class="ks3-arr-stagename"%s data-arr-stagename="%d">%s</p>'
        % ("" if i == 0 else " hidden", i, t(name))
        for i, name in enumerate(names))

    views = []
    for rx in reactions:
        for st in (0, 1, 2):
            groups = rx["products"] if st == 2 else rx["reactants"]
            if st == 1:
                # Every join broken: the PARTICLES are gone and only atoms are
                # left, so the outlines and the captions go with them. That is
                # what "loose" means, and drawing a box round a single atom
                # would be putting a join back.
                boxes = "".join(
                    '<div class="ks3-arr-group is-loose">'
                    '<span class="ks3-arr-atoms">%s</span></div>'
                    % _arr_atom(elements, sym, True)
                    for g in groups for sym in (g.get("atoms") or []))
            else:
                cls = " is-product" if st == 2 else ""
                boxes = "".join(
                    '<div class="ks3-arr-group%s">'
                    '<span class="ks3-arr-atoms">%s</span>'
                    '<p class="ks3-arr-label">%s</p></div>'
                    % (cls,
                       "".join(_arr_atom(elements, sym, False)
                               for sym in (g.get("atoms") or [])),
                       _arr_formula(g.get("formula") or []))
                    for g in groups)

            # §5A: the count in the label is DERIVED. Design writes
            # `rx.reactants.length` and `rx.products.length`; hard-coding
            # either would be a figure the instrument computes, typed by hand.
            label = labels[st].replace("{n}", str(len(groups)))
            views.append(
                '<div class="ks3-arr-view"%s role="img" aria-label="%s" '
                'data-arr-groups="%s|%d"><div class="ks3-arr-row">%s</div>'
                '</div>'
                % ("" if (rx["id"] == first and st == 0) else " hidden",
                   e(label), e(rx["id"]), st, boxes))

    # ── the atom-count table ─────────────────────────────────────────────
    bodies = []
    for rx in reactions:
        rows = "".join(
            '<tr><th scope="row" class="ks3-arr-el">%s</th>'
            '<td class="ks3-arr-before">%s</td>'
            '<td class="ks3-arr-after">'
            '<span class="ks3-arr-pending" data-arr-pending>%s</span>'
            '<span class="ks3-arr-num" hidden data-arr-num>%s</span>'
            '</td></tr>'
            % (t(row.get("el", "")), t(row.get("n", "")),
               t(a.get("count_pending", "—")), t(row.get("n", "")))
            for row in (rx.get("counts") or []))
        bodies.append('<tbody%s data-arr-counts="%s">%s</tbody>'
                      % ("" if rx["id"] == first else " hidden",
                         e(rx["id"]), rows))

    table = ('<table class="ks3-arr-table"><thead><tr>'
             '<th scope="col">%s</th><th scope="col">%s</th>'
             '<th scope="col">%s</th></tr></thead>%s</table>'
             % (t(heads.get("atom", "")), t(heads.get("before", "")),
                t(heads.get("after", "")), "".join(bodies)))

    # ── the stage commentary ─────────────────────────────────────────────
    # Stages 0 and 1 are the same sentence whichever reaction is loaded, so
    # they are in the document once. Stage 2 is the reaction's own
    # `product_text`, so there is one per reaction and none is a template.
    stagetexts = ['<p class="ks3-arr-stagetext"%s data-arr-stagetext="%d">%s</p>'
                  % ("" if i == 0 else " hidden", i, rich(txt))
                  for i, txt in enumerate(texts)]
    for rx in reactions:
        if not rx.get("product_text"):
            raise ValueError(
                "atom-rearranger %r reaction %r has no `product_text`. Stage "
                "2 is where the gate above it gets its answer; a reaction "
                "that reaches its products with nothing to say is a "
                "commitment that goes nowhere." % (act_id, rx.get("id")))
        stagetexts.append(
            '<p class="ks3-arr-stagetext" hidden data-arr-stagetext="2|%s">'
            '%s</p>' % (e(rx["id"]), rich(rx["product_text"])))

    # ── the gates, one per reaction, all closed at rest ──────────────────
    gates = []
    for rx in reactions:
        gate = rx.get("gate") or {}
        if not gate.get("q") or not gate.get("options"):
            raise ValueError(
                "atom-rearranger %r reaction %r has no gate. The commitment "
                "belongs between the loose atoms and the products, and "
                "without it the student watches instead of predicting."
                % (act_id, rx.get("id")))
        gates.append(
            '<div class="ks3-arr-gate" hidden data-arr-gate="%s">'
            '<p class="ks3-commit">%s</p>%s</div>'
            % (e(rx["id"]), t(gate["q"]),
               _arr_lettered(gate["options"],
                             'data-arr-gateopts="%s"' % e(rx["id"]),
                             "arr-gateopt")))

    # ── the two controls ─────────────────────────────────────────────────
    # Both labels of the advance button are in the document and one is shown,
    # so no label is ever assembled out of an attribute.
    controls = (
        '<div class="ks3-arr-controls">'
        '<button type="button" class="ks3-reveal-btn ks3-arr-advance" '
        'data-arr-advance>'
        '<span data-arr-adv="0">%s</span>'
        '<span hidden data-arr-adv="1">%s</span></button>'
        '<button type="button" class="ks3-retry ks3-arr-reset" data-arr-reset>'
        '%s</button></div>'
        % (t(adv[0]), t(adv[1]), t(a.get("reset_label", ""))))

    summary = ""
    if a.get("summary"):
        summary = ('<div class="ks3-arr-summary" hidden data-arr-done>'
                   '<p>%s</p></div>' % rich(a["summary"]))

    return ('<div class="ks3-arr" data-arr data-total="%d">'
            '<div class="ks3-arr-dial">'
            '<p class="ks3-arr-diallabel">%s</p>'
            '<div class="ks3-arr-tabs">%s</div></div>'
            '%s'
            '<div class="ks3-arr-plate">%s%s</div>'
            '<div class="ks3-arr-panels">'
            '<div class="ks3-arr-panel">'
            '<p class="ks3-arr-panelhead">%s</p>%s</div>'
            '<div class="ks3-arr-panel ks3-arr-say">%s</div>'
            '</div>%s%s%s</div>'
            % (len(reactions), t(a.get("tabs_label", "")), tabs, words,
               stagenames, "".join(views),
               t(a.get("count_label", "")), table,
               "".join(stagetexts), "".join(gates), controls, summary))


def r_impossible_ask(a, act_id):
    """⊕ c4-02 `#s-impossible` — ask for a product the atoms cannot spell.

    ⚖️ **THE REFUSAL BRANCHES ON WHICH ATOMS ARE PRESENT, AND ON NOTHING
    ELSE.** Design's payload carries a `possible: true/false` per ask. That
    flag is a PROXY — the answer written down beside the question — and §5A
    forbids branching on one. So it is not authored and it is not read here.
    Each ask declares the elements its product is BUILT FROM, and the verdict
    is `set(needs) <= set(table)`: ammonia is refused because there is no
    nitrogen on the table, gold because there is no gold. Two refusals, one
    test, different atoms — which is the sentence the lesson wants left
    behind, and the sentence balancing is built on three lessons later.

    ⚖️ THE DERIVATION NAMES THE PANEL. A possible ask renders
    `id="ask-<id>-verdict"`; a refused one renders `id="ask-<id>-refusal"`.
    The suffix is therefore evidence of what the atoms produced rather than a
    label somebody typed — and because `REACT-04` is joined to
    `ask-gold-refusal`, a payload edit that put gold within reach would rename
    that element and turn the MRB-244 join gate RED. The misconception
    register is doing duty as a guard on the chemistry, which is the strongest
    use it has had.

    ⚠️ FOUR ASKS, FIVE STATES. Nothing is open on load and nothing is ticked
    on load; that is the fifth state and it is the one a resting page is in.
    The rail stop ticks on ANY ask, refused or built, because the thing being
    credited is having asked and read what came back.

    ⚠️ THE VERDICT PANEL IS INK-DARK ON A LIGHT BLOCK, which is the one
    nesting Design draws in this unit. Its text takes `--ks3-on-dark` and
    `--ks3-on-dark-body` and never `--ks3-accent-text`, and every rule for it
    is self-scoped at (0,2,0) so a generic on-dark type rule cannot win.

    HOOKS: `data-iask` (wrapper) · `data-iask-ask` (an ask button, valued with
    its id, and carrying `id="ask-<id>"`) · `data-iask-verdict` (a panel,
    valued with the ask's id).
    """
    asks = a.get("asks") or []
    table = list(a.get("table") or [])
    if not asks or not table:
        raise ValueError(
            "impossible-ask %r needs asks[] and a table[] of the atoms "
            "actually on the bench." % act_id)
    have = set(table)

    buttons, panels, possible, refused = [], [], 0, 0
    for ask in asks:
        aid = ask.get("id")
        needs = list(ask.get("needs") or [])
        if not aid or not needs:
            raise ValueError(
                "impossible-ask %r has an ask with no id or no `needs`. "
                "`needs` is what the verdict is computed from; an ask without "
                "it is an ask nothing can answer." % act_id)
        for key in ("label", "title", "text"):
            if not ask.get(key):
                raise ValueError(
                    "impossible-ask %r ask %r has no %r."
                    % (act_id, aid, key))
        can = set(needs) <= have
        if can:
            possible += 1
        else:
            refused += 1
        buttons.append(
            '<button type="button" class="ks3-seg-btn ks3-iask-ask" '
            'id="ask-%s" data-iask-ask="%s" aria-pressed="false">%s</button>'
            % (e(aid), e(aid), t(ask["label"])))
        panels.append(
            '<div class="ks3-iask-verdict" hidden id="ask-%s-%s" '
            'data-iask-verdict="%s">'
            '<p class="ks3-iask-title">%s</p>'
            '<p class="ks3-iask-text">%s</p></div>'
            % (e(aid), "verdict" if can else "refusal", e(aid),
               rich(ask["title"]), rich(ask["text"])))

    if not possible or not refused:
        raise ValueError(
            "impossible-ask %r derives %d possible and %d refused ask(s) from "
            "the atoms on the table. The instrument teaches a CONTRAST — the "
            "rule has teeth only when something gets through it — so one of "
            "each is the floor." % (act_id, possible, refused))

    return ('<div class="ks3-iask" data-iask>'
            '<div class="ks3-iask-asks">%s</div>%s</div>'
            % ("".join(buttons), "".join(panels)))


# ── registrations for the commander to splice ────────────────────────────
#
# No ART row: this lesson declares no figure. Its particle pictures are the
# rearranger's own stages — an instrument with a demand and a commitment, not
# a diagram — and authoring them again as a `drawn` figure would put the same
# atoms on the page twice.
#
# Both families tick a rail stop, so both carry `data-stage-done="0"` and
# NOTHING IS TICKED ON LOAD. `data-instrument` keeps the shell's
# `wirePredictions` out of the rearranger's own gate options.
#




#
# And in ks3_data/c4/__init__.py's _INSTRUMENT_SEGMENTS — both are LIGHT
# `ks3-block`s on Design's page, measured, so both are `check` and neither is
# `practical`:
#     "atom-rearranger": "check",
#     "impossible-ask":  "check",


# ── from art_03.py ─────────────────────────────────────
# ═══ c4-03 · equation-builder and equation-read ══════════════════════════
#
# Two families, one page. `equation-builder` (`#s-builder`) is the flagship:
# three real cases, a bench that offers more than belongs in the equation, and
# a check that names the wrong RULE rather than the wrong answer.
# `equation-read` (`#s-read`) is the other direction — the equation is given
# and the student says what it claims.
#
# ⚠️ EVERY ARROW INSIDE AN EQUATION IS DRAWN. Design's C4 convention, and a
# hard one: the shipped font subsets contain no U+2192, so a typed arrow is a
# missing glyph in the middle of the notation the lesson teaches. `_eqb_arrow`
# is the ONE definition of that path in this unit — Design's own 44×24 box,
# `M4 12h30M26 5l8 7-8 7` on `currentColor`, so it inks itself on cream and on
# the ink-dark check panel without a second copy.
#
# It also carries the spoken equivalent, and the word is "makes" rather than
# `appendAuthored`'s "to". That is this lesson's own reading of the arrow —
# the explainer, the key fact, the key note and rung 1 all say so — and a
# screen reader that hears "zinc and copper sulfate to zinc sulfate and
# copper" has been given the arithmetic reading the page exists to refuse.
#
# HOOKS (builder): `data-eqb` (wrapper: `data-eqb-total`, `data-eqb-cfg`) ·
# `data-eqb-tab` (a case tab, valued with the case id) · `data-eqb-story` /
# `data-eqb-bank` / `data-eqb-eq` / `data-eqb-checkpanel` (one per case, valued
# with the case id, all but the opening one hidden) · `data-eqb-row` (a bank
# row, valued with the substance name) · `data-eqb-chip` · `data-eqb-place`
# (a row button, valued `left` / `right` / `out`) · `data-eqb-sidebox` /
# `data-eqb-ghost` (valued `left` / `right`) · `data-eqb-store` (the hidden
# pool the term nodes rest in) · `data-eqb-term` (a term node, valued with the
# name) · `data-eqb-plus` · `data-eqb-check` / `data-eqb-clear` (the two
# buttons) · `data-eqb-branch` (a verdict branch, valued `perfect` /
# `distractor` / `side` / `missing`) · `data-eqb-why` (a distractor's own
# sentence, valued with the name) · `data-eqb-sidetitle` /
# `data-eqb-sidetext` / `data-eqb-missingtext` (the three composed nodes).
#
# HOOKS (read): `data-eqr` (wrapper: `data-total`) · `data-eqr-card` (valued
# with the reading id, carrying `data-open`) · `data-eqr-opt` (valued with the
# option index) · `data-eqr-reply`.


def _eqb_cfg(obj):
    """One JSON payload, deterministically ordered, safe in an attribute."""
    return e(json.dumps(obj, separators=(",", ":"), sort_keys=True,
                        ensure_ascii=False))


def _eqb_arrow():
    """Design's equation arrow, drawn, with its spoken word beside it."""
    return ('<svg class="ks3-eqb-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" '
            'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>'
            '<span class="ks3-visually-hidden">makes</span>')


def _eqb_seg(cls, pressed, label, **attrs):
    """One segmented-control button, in the key stage's ONE segmented control.

    ⚠️ There is no `data-correct` parameter here and there must never be one.
    Nothing in either of these two instruments marks: a pressed control says
    it was PRESSED, and every verdict is a panel of words.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _eqb_names(case):
    """Every name on this case's bench, in Design's own bank order.

    Reactants, then products, then the distractors — her `names`, unshuffled.
    The real substances are never last and the distractors are never marked
    out by position; what tells them apart is the story, and nothing else.
    """
    return ([n for n in case.get("reactants") or []]
            + [n for n in case.get("products") or []]
            + [n for n, _why in case.get("distractors") or []])


def r_equation_builder(a, act_id):
    """⊕ c4-03 `#s-builder` — three cases, one bench, and five wrong rules.

    ⚖️ **THE DISTRACTORS ARE THE LESSON** (NOTES §2). Heat, energy, a flame,
    limewater from a different test tube, and "bubbles" instead of the gas's
    name. Each is offered in the same list, with the same two buttons, as the
    substances that really do belong — so nothing about the CONTROL says which
    is which, and a student who wants to know has to read the story. Each is
    answered by a sentence naming the wrong RULE it embodies, never by "no".

    ⚠️ EMIT-BOTH-SHOW-ONE, AT THE CASE LEVEL. All three cases are in the
    document — story, bench, equation and check panel — and one is shown. Each
    case therefore keeps its own progress with no state to store: the DOM is
    the state, and coming back to a case that was already checked shows it
    exactly as it was left. It is also why not one authored sentence — six
    distractor corrections, three model equations, four verdict branches — is
    ever assembled out of an attribute.

    ⚠️ THE RESTING STATE HAS "LEAVE IT OUT" PRESSED ON EVERY ROW, and that is
    Design's, not a default: her `pressed` is `(place[n] || null) === b.id`
    and the third button's id is `null`, so on first paint every substance is
    already out of the equation and both sides read "nothing yet". A resting
    render with three unpressed buttons per row would be a different opening
    state from the one she drew.

    ⚠️ `data-eqb-cfg` CARRIES NO SENTENCE THAT IS NOT A TEMPLATE. The names
    and the two answer lists are there because the verdict has to be
    recomputed from them; the two wrong-side templates and the missing-list
    template are there because a substance name has to be substituted into
    them. Everything else — every correction, every fixed title, every model
    equation — is real markup, emitted once and shown.

    ⚑ `id="builder-distractor"` is on the bench panel and `data-activity=
    "builder-check"` on the section around it (the activity id, from the
    record). Those are `REACT-06`'s two joins and this is where they resolve:
    the bench is where a student can commit to heat being a reactant, and the
    check is where that is taken apart.
    """
    cases = a.get("cases") or []
    if len(cases) < 2:
        raise ValueError(
            "equation-builder %r declares %d case(s). The instrument teaches "
            "by contrast across cases — one case is a worked example, not a "
            "bench." % (act_id, len(cases)))
    verdict = a.get("verdict") or {}
    for key in ("perfect_title", "perfect_text", "distractor_title",
                "side_title", "side_product", "side_reactant",
                "missing_title", "missing_text"):
        if not verdict.get(key):
            raise ValueError(
                "equation-builder %r has no verdict.%s. Every branch a "
                "student can reach has to say something: a right equation, a "
                "thing that does not belong, a substance on the wrong side "
                "and a substance left out are four different findings."
                % (act_id, key))
    for c in cases:
        if not c.get("reactants") or not c.get("products"):
            raise ValueError(
                "equation-builder %r case %r has no reactants or no products. "
                "A word equation with an empty side is not an equation."
                % (act_id, c.get("id")))
        names = _eqb_names(c)
        if len(set(names)) != len(names):
            raise ValueError(
                "equation-builder %r case %r names %r twice. One chip, one "
                "place — a name on the bench twice can be a reactant and a "
                "distractor at the same time."
                % (act_id, c.get("id"),
                   [n for n in names if names.count(n) > 1][0]))
        for n, why in c.get("distractors") or []:
            if not why:
                raise ValueError(
                    "equation-builder %r case %r offers %r with no reason. "
                    "The reason IS the teaching — without it the only thing "
                    "left to say is that the student was wrong."
                    % (act_id, c.get("id"), n))

    labels = a.get("place_labels") or {}
    for side in ("left", "right", "out"):
        if not labels.get(side):
            raise ValueError(
                "equation-builder %r has no place_labels[%r]. All three "
                "buttons are drawn on every row." % (act_id, side))

    cfg = {"cases": [{"id": c.get("id"),
                      "names": _eqb_names(c),
                      "reactants": list(c.get("reactants") or []),
                      "products": list(c.get("products") or []),
                      "distractors": [n for n, _w in c.get("distractors")
                                      or []]}
                     for c in cases],
           "verdict": {k: verdict[k] for k in
                       ("side_title", "side_product", "side_reactant",
                        "missing_text")},
           "missing_join": verdict.get("missing_join") or " and "}

    tabs = "".join(
        _eqb_seg("ks3-eqb-tab", i == 0, c.get("tab", ""),
                 data_eqb_tab=c.get("id", ""))
        for i, c in enumerate(cases))

    stories = "".join(
        '<p class="ks3-eqb-story" data-eqb-story="%s"%s>%s</p>'
        % (e(c.get("id", "")), "" if i == 0 else " hidden",
           rich(c.get("story", "")))
        for i, c in enumerate(cases))

    banks = []
    for i, c in enumerate(cases):
        rows = []
        for n in _eqb_names(c):
            btns = "".join(
                _eqb_seg("ks3-eqb-place", side == "out", labels[side],
                         data_eqb_place=side)
                for side in ("left", "right", "out"))
            rows.append(
                '<div class="ks3-eqb-row" data-eqb-row="%s">'
                '<span class="ks3-eqb-chip" data-eqb-chip>%s</span>'
                '<span class="ks3-eqb-rowbtns">%s</span></div>'
                % (e(n), t(n), btns))
        banks.append('<div class="ks3-eqb-bank" data-eqb-bank="%s"%s>%s</div>'
                     % (e(c.get("id", "")), "" if i == 0 else " hidden",
                        "".join(rows)))

    eqs = []
    for i, c in enumerate(cases):
        # The term nodes rest in the store and are MOVED, never rewritten, so
        # a name never round-trips through an attribute and the plus signs are
        # real markup that the runtime only shows or hides.
        store = "".join(
            '<span class="ks3-eqb-term" data-eqb-term="%s">'
            '<span class="ks3-eqb-plus" data-eqb-plus aria-hidden="true" '
            'hidden>+</span><span class="ks3-eqb-name">%s</span></span>'
            % (e(n), t(n)) for n in _eqb_names(c))
        eqs.append(
            '<div class="ks3-eqb-eq" data-eqb-eq="%s"%s>'
            '<p class="ks3-eqb-eqlabel">%s</p>'
            '<p class="ks3-eqb-line">'
            '<span class="ks3-eqb-side" data-eqb-sidebox="left"></span>'
            '<span class="ks3-eqb-ghost" data-eqb-ghost="left">%s</span>'
            '%s'
            '<span class="ks3-eqb-side" data-eqb-sidebox="right"></span>'
            '<span class="ks3-eqb-ghost" data-eqb-ghost="right">%s</span>'
            '</p>'
            '<span class="ks3-eqb-store" data-eqb-store hidden>%s</span>'
            '</div>'
            % (e(c.get("id", "")), "" if i == 0 else " hidden",
               t(a.get("equation_label") or ""),
               t(a.get("empty_label") or ""), _eqb_arrow(),
               t(a.get("empty_label") or ""), store))

    checks = []
    for c in cases:
        whys = "".join(
            '<p class="ks3-eqb-checktext" data-eqb-why="%s" hidden>%s</p>'
            % (e(n), rich(why)) for n, why in c.get("distractors") or [])
        model = ('<p class="ks3-eqb-model"><span>%s</span>%s<span>%s</span></p>'
                 % (t(" + ".join(c.get("reactants") or [])), _eqb_arrow(),
                    t(" + ".join(c.get("products") or []))))
        checks.append(
            '<div class="ks3-eqb-check" data-eqb-checkpanel="%s" hidden>'
            '<div data-eqb-branch="perfect" hidden>'
            '<p class="ks3-eqb-checktitle">%s</p>'
            '<p class="ks3-eqb-checktext">%s</p></div>'
            '<div data-eqb-branch="distractor" hidden>'
            '<p class="ks3-eqb-checktitle">%s</p>%s</div>'
            '<div data-eqb-branch="side" hidden>'
            '<p class="ks3-eqb-checktitle" data-eqb-sidetitle></p>'
            '<p class="ks3-eqb-checktext" data-eqb-sidetext></p></div>'
            '<div data-eqb-branch="missing" hidden>'
            '<p class="ks3-eqb-checktitle">%s</p>'
            '<p class="ks3-eqb-checktext" data-eqb-missingtext></p></div>'
            '%s</div>'
            % (e(c.get("id", "")), t(verdict["perfect_title"]),
               rich(verdict["perfect_text"]), t(verdict["distractor_title"]),
               whys, t(verdict["missing_title"]), model))

    return ('<div class="ks3-eqb" data-eqb data-eqb-total="%d" '
            'data-eqb-cfg="%s">'
            '<div class="ks3-eqb-tabs">%s</div>'
            '<div class="ks3-eqb-stories">%s</div>'
            '<div class="ks3-eqb-bench" id="builder-distractor">'
            '<p class="ks3-eqb-benchlabel">%s</p>%s</div>'
            '<div class="ks3-eqb-eqs">%s</div>'
            '<div class="ks3-eqb-btns">'
            '<button type="button" class="ks3-reveal-btn ks3-eqb-checkbtn" '
            'data-eqb-check hidden>%s</button>'
            '<button type="button" class="ks3-retry ks3-eqb-clear" '
            'data-eqb-clear>%s</button></div>'
            '<div class="ks3-eqb-checks">%s</div></div>'
            % (len(cases), _eqb_cfg(cfg), tabs, stories,
               t(a.get("bench_label") or ""), "".join(banks), "".join(eqs),
               t(a.get("check_label") or ""), t(a.get("clear_label") or ""),
               "".join(checks)))


def r_equation_read(a, act_id):
    """⊕ c4-03 `#s-read` — the equation is given; what does it CLAIM?

    Three cards, one commitment each, and the commitment is FINAL: the reply
    is on screen the instant the card is decided, so a second press would be a
    student choosing an answer they can already read. Both buttons disable and
    the one that was not pressed dims — the card still says what was chosen.

    ⚠️ TWO OPTIONS, AND THAT IS THE QUESTION. Design draws a pair on every
    card, not a lettered list of four, because each pair is a single
    distinction — "and/makes" against "plus/equals", one substance breaking
    apart against two joining, a compound against a mixture. A third option
    would be a third distinction and a different exercise. The MRB-177 length
    gate skips a set of two by construction, so the pairs are measured by the
    thing that matters here instead: neither reading is longer or shorter than
    the other by enough to be pickable without reading it.

    ⚠️ NOTHING HERE MARKS. The chosen button keeps the ordinary pressed
    treatment whichever way it went, and the reply says in words what the
    equation is saying. `answer` never reaches the markup at all — it is not
    needed: the reply is the same paragraph either way, and it names the
    reading that is right.
    """
    readings = a.get("readings") or []
    if len(readings) < 2:
        raise ValueError(
            "equation-read %r declares %d reading(s). The section is a set of "
            "contrasts and one card is not a set." % (act_id, len(readings)))
    cards = []
    for r in readings:
        opts = r.get("options") or []
        if len(opts) != 2:
            raise ValueError(
                "equation-read %r card %r offers %d option(s). Design draws a "
                "PAIR on every card — the pair is the distinction being made, "
                "and a third option is a second distinction."
                % (act_id, r.get("id"), len(opts)))
        if not r.get("reply"):
            raise ValueError(
                "equation-read %r card %r has no reply. The card opens on the "
                "commitment and the reply is the whole of what opens."
                % (act_id, r.get("id")))
        # `answer` reaches no markup — the reply names the reading that is
        # right, and only the ladder marks — so this is the one place it is
        # read. It is Design's own `correct`, kept because the record should
        # say which reading is right even where the page does not need to,
        # and checked here so that "kept" cannot quietly mean "wrong".
        if r.get("answer") not in (0, 1):
            raise ValueError(
                "equation-read %r card %r marks option %r correct, and there "
                "are two. The record has to know which reading is the right "
                "one even though the markup never says."
                % (act_id, r.get("id"), r.get("answer")))
        buttons = "".join(
            _eqb_seg("ks3-eqr-opt", False, o, data_eqr_opt=str(i))
            for i, o in enumerate(opts))
        cards.append(
            '<div class="ks3-eqr-card" data-eqr-card="%s" data-open="0">'
            '<p class="ks3-eqr-eq"><span>%s</span>%s<span>%s</span></p>'
            '<div class="ks3-eqr-opts">%s</div>'
            '<p class="ks3-eqr-reply" data-eqr-reply hidden>%s</p></div>'
            % (e(r.get("id", "")), t(r.get("left", "")), _eqb_arrow(),
               t(r.get("right", "")), buttons, rich(r["reply"])))
    return ('<div class="ks3-eqr" data-eqr data-total="%d">%s</div>'
            % (len(readings), "".join(cards)))


# No drawer row from this fragment: c4-03 declares no figure, and the
# marker is deliberately not written above with the word "none" after
# it — build_ks3.py records a splice that took exactly that as a table
# row and emitted it into the registry, which is a SyntaxError in the
# generator. A marker that means "no row" has to not be the marker.


# ── from art_04.py ─────────────────────────────────────
# ═══ c4-04 · mass-in-a-reaction ══════════════════════════════════════════
#
# Four families, one lesson: `mass-bench`, `mass-cover`, `mass-worked` and
# `mass-check`. All DOM, no canvas, no animation, no timer. Every one of the
# four sits in a LIGHT `ks3-block` — measured off Design's own markup, page
# lines 105, 169, 230 and 259 — and every one ticks a rail stop, so every one
# carries `data-stage-done="0"` and NOTHING is ticked on load.
#
# ⚖️ **`mass-cover` IS DELIBERATELY NOT `r_cover_bar`, AND MUST NOT BE
# "FIXED" INTO IT.** There is a comment in `build_ks3.py` (around line 2022)
# stating that `cover-triangle` is not an activity kind, that its bar variant
# is a `formula` block sub-key, that it has no `data-stage-done`, and that
# "the block is read, not done, and MRB-208 keeps it off the rail". That
# comment is TRUE OF C2's READ-ONLY VARIANT and it does not govern this page.
#
# Design's own reference settles it. `RAIL` (page line 449) contains `s-cover`,
# and `DONE()` (page line 553) reads:
#
#     if (id === 's-cover') return s.cover !== null;
#
# — it ticks when the student has PRESSED A COVER BUTTON. That is a
# commitment with a real completion signal, so MRB-249 requires the stop and
# the section is an ACTIVITY with `data-stage-done="0"`. Turning it back into
# a `formula` block's `cover` key would silently cost this lesson one of its
# seven rail stops, and the rail would look fine while a stop could never tick.
#
# ⚠️ The FAMILY NAME is `mass-cover` and the prefix is `mcov`, not `cover-bar`
# / `cbar`. `r_cover_bar` already exists in `build_ks3.py` for C2, and two
# different components called cover-bar in one build is exactly the
# `data-critique` / `data-critiq` trap — a shared selector wiring one
# instrument to another's handler, which fails as a silently dead instrument
# rather than as an error. It is still a BAR: the name and the status changed,
# the drawing did not.
#
# ⚠️ AND THE BENCH IS `mass-bench`, NOT THE CONTRACT'S `balance-bench`. That
# family is ALREADY REGISTERED — `ks3_art/c2.py`, for c2-06's `#s-balance`,
# which is very nearly this instrument one unit earlier. `ks3_art.load()` fails
# loudly on a duplicate family across modules and it is RIGHT to: a silent
# last-one-wins would draw this bench with C2's renderer, under C2's payload
# shape, and tell nobody. §8's own rule decides it — a family is registered as
# THIS unit's own even where another unit has one that looks like it, because
# reuse means depending on another unit's module or promoting into the shared
# `ks3_art/core.py`. The assigned `bbench` prefix was already collision-free
# and is kept; only the family name moved. Same correction as `cover-bar`.
#
# ⚖️ AND IT STAYS A BAR. MRB-204 as ruled at MRB-246: a triangle is for
# `A = B × C`; a beam or a part–whole bar is for SUMS and conservation
# statements. Conservation of mass is a sum. A triangle here would teach a
# student that two masses can be multiplied together, which is not a thing.
#
# HOOKS, all four families:
#   mass-bench     `data-bbench` (wrapper, `data-total`) · `data-bbench-for` +
#                  `data-bbench-val` (a dial button) · `data-bbench-predict`
#                  (the lettered gate list) · `data-bbench-run` ·
#                  `data-bbench-panel` (valued with the run key) ·
#                  `data-bbench-close`
#   mass-cover     `data-mcov` (wrapper) · `data-mcov-for` (a cover button) ·
#                  `data-mcov-plate` (valued with the cell id) ·
#                  `data-mcov-out` · `data-mcov-result` (valued with the id)
#   mass-worked    `data-mwork` (wrapper, `data-total`) · `data-mwork-step` ·
#                  `data-mwork-open` · `data-mwork-next` · `data-mwork-label`
#   mass-check     `data-mchk` (wrapper, `data-total`) · `data-mchk-step` ·
#                  `data-mchk-open` · `data-mchk-btn`
#
# ⚠️ NO `data-correct` ON ANY OPTION IN ANY OF THE FOUR, and nothing green and
# nothing red reaches a control. The bench's prediction has no right answer to
# mark — the answer depends on which flask you chose — and every verdict on
# this page is a PANEL OF WORDS. Only the mastery ladder marks.


def _c4_seg(cls, pressed, label, **attrs):
    """One segmented-control button.

    `.ks3-seg-btn` is the system's ONE segmented control (the Drift-4 ruling),
    with a family class beside it for layout. R2: the pressed state carries
    `aria-pressed`, a WORD, not colour alone. There is no `data-correct`
    parameter and there must never be one.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _c4_lettered(options, hook):
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


# ═══ c4-04 · mass-bench ═══════════════════════════════════════════════

def r_mass_bench(a, act_id):
    """⊕ c4-04 `#s-bench` — two dials, four runs, and one thing they prove.

    ⚖️ **THE FOUR RUNS ARE THE ARGUMENT, WHICH IS WHY ALL FOUR MUST BE RUN
    BEFORE THE STOP TICKS.** Design's `DONE('s-bench')` is
    `Object.keys(s.ran).length >= 4`, not "has run one". Two runs of the same
    reaction in two flasks say the lid matters; two reactions in the same flask
    say direction varies. Only all four say *the reaction never changes the
    mass, and the lid decides whether the balance can see it* — which is the
    closing panel, and it is the sentence the whole lesson turns on.

    ⚖️ THE VERDICT BRANCHES ON THE VESSEL, NOT ON A PROXY. Each run's note is
    keyed to WHICH dials are set — the reaction and the flask — and never to
    how many runs have happened. The state space is enumerated in full below
    and the renderer refuses to build a bench with a hole in it: every
    reachable pair of dial values must have an authored run, because a bench
    that silently shows the last run's numbers for an unauthored combination is
    a wrong number in the bytes.

    ⚠️ EMIT-BOTH-SHOW-ONE, AND NOTHING IS COMPUTED. All four runs' tiles and
    notes are in the document at rest and one is unhidden. So the deltas in
    Design's own reveal sentences — "fell by 2.20 g", "rose by 1.60 g" — are
    AUTHORED prose, not a figure this instrument works out and could then
    contradict. There is no arithmetic in this renderer and none in
    `wireMassBench`.

    ⚠️ THE THIRD TILE IS "not measured — you work it out" ON BOTH OPEN RUNS,
    AND THAT IS THE LESSON. An open flask never gives you the mass of the gas;
    it gives you two readings and leaves the subtraction to the student, three
    sections later. On the sealed runs the honest value is `0.00 g`, which is a
    READING rather than an absence, and the tile keeps its dashed border either
    way so the two are visibly the same slot.

    ⚠️ THE PREDICTION GATE HOLDS THE RUN BUTTON. Design's `canRun` is
    `s.predict !== null && !ran`, so the button is not in the document's
    resting state at all: Law 4, and the reading is not shown until the student
    has said what they expect. Changing a dial withdraws it again, because the
    prediction was about the flask they have just left.

    ⚑ AMBER ON THE GATE, AND IT CARRIES ITS RULED MEANING. `--ks3-alert-tint`
    grounds this panel exactly as it grounds c3-03's, c3-04's and c3-05's
    predict gates: it is the WRONG IDEA being elicited a few sections before
    the page confronts it. Here that idea is `REACT-07` — a student who thinks
    a gas has no mass predicts "go down" for the sealed flask too. It is never
    a selection and never a reading; every live value on this bench is
    `--ks3-accent-text`, which is what Design paints them.

    HOOKS: see the module header.
    """
    dials = a.get("dials") or []
    runs = a.get("runs") or []
    tiles = a.get("tiles") or []
    predict = a.get("predict") or {}
    if len(dials) != 2:
        raise ValueError(
            "mass-bench %r declares %d dial(s). The bench is a REACTION "
            "crossed with a FLASK and the whole argument is the four cells "
            "that makes; with one dial there is nothing to cross."
            % (act_id, len(dials)))
    if len(tiles) != 3:
        raise ValueError(
            "mass-bench %r declares %d tile(s); the readout is before, "
            "after and the mass of gas." % (act_id, len(tiles)))
    if not predict.get("options"):
        raise ValueError(
            "mass-bench %r has no prediction options. Law 4: the reading "
            "is not shown until the student has said what they expect."
            % act_id)

    # ⚠️ THE WHOLE STATE SPACE, ENUMERATED AND CHECKED (§5A). Every reachable
    # pair of dial values must have an authored run, and no run may name a pair
    # the dials cannot reach. A missing cell would show the previous run's
    # numbers under the new dial's label; a surplus one is a run nobody can get
    # to and nobody would ever notice was wrong.
    reachable = []
    for first in dials[0].get("options") or []:
        for second in dials[1].get("options") or []:
            reachable.append("%s:%s" % (first["id"], second["id"]))
    authored = [r["id"] for r in runs]
    missing = [k for k in reachable if k not in authored]
    surplus = [k for k in authored if k not in reachable]
    if missing or surplus:
        raise ValueError(
            "mass-bench %r does not model what it draws. Unreachable "
            "run(s): %s. Dial combination(s) with no run: %s. A dial that is "
            "drawn must be modelled, and a bench with a hole in it shows the "
            "last run's numbers under the new run's label."
            % (act_id, surplus or "none", missing or "none"))
    for r in runs:
        for key in ("before", "after", "third", "third_note", "note"):
            if not r.get(key):
                raise ValueError(
                    "mass-bench %r run %r has no %r. Every run opens a "
                    "readout and a verdict; a run with nothing to report is a "
                    "control that does nothing." % (act_id, r.get("id"), key))

    # ── the dials ────────────────────────────────────────────────────────
    # The FIRST option of each dial is the resting state, which is Design's
    # own opening state (`reaction: 'marble', vessel: 'open'`) expressed as a
    # property of the payload rather than as two strings repeated here.
    dial_html = []
    for d in dials:
        opts = d.get("options") or []
        dial_html.append(
            '<div class="ks3-bbench-dial">'
            '<p class="ks3-bbench-diallabel">%s</p>'
            '<div class="ks3-bbench-dialrow">%s</div></div>'
            % (t(d.get("label", "")),
               "".join(_c4_seg("ks3-bbench-opt", i == 0, o.get("label", ""),
                               data_bbench_for=d["id"],
                               data_bbench_val=o["id"])
                       for i, o in enumerate(opts))))

    # ── the gate ─────────────────────────────────────────────────────────
    # The Run button is emitted `hidden`: `canRun` is false at rest, and the
    # RESTING DOM must be the state the page is in before a line of JS runs.
    gate = ('<div class="ks3-bbench-gate">'
            '<p class="ks3-commit">%s</p>%s'
            '<button type="button" class="ks3-reveal-btn ks3-bbench-run" '
            'hidden data-bbench-run>%s</button></div>'
            % (rich(predict.get("prompt", "")),
               _c4_lettered(predict["options"], "data-bbench-predict"),
               t(predict.get("run_label") or "Run the reaction")))

    # ── the four run panels, all present, all hidden ─────────────────────
    panels = []
    for r in runs:
        cells = []
        values = (r["before"], r["after"], r["third"])
        for tile, value in zip(tiles, values):
            gas = tile.get("id") == "gas"
            note = r["third_note"] if gas else tile.get("note", "")
            cells.append(
                '<div class="ks3-bbench-tile%s">'
                '<p class="ks3-bbench-tilelabel">%s</p>'
                '<p class="ks3-bbench-value%s">%s</p>'
                '<p class="ks3-bbench-tilenote">%s</p></div>'
                % (" is-gas" if gas else "", t(tile.get("label", "")),
                   " is-soft" if gas else "", t(value), rich(note)))
        panels.append(
            '<div class="ks3-bbench-panel" hidden data-bbench-panel="%s">'
            '<div class="ks3-bbench-tiles">%s</div>'
            '<div class="ks3-bbench-note"><p>%s</p></div></div>'
            % (e(r["id"]), "".join(cells), rich(r["note"])))

    close = ('<div class="ks3-bbench-close" hidden data-bbench-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""

    return ('<div class="ks3-bbench" data-bbench data-total="%d">'
            '<div class="ks3-bbench-dials">%s</div>%s%s%s</div>'
            % (len(reachable), "".join(dial_html), gate,
               "".join(panels), close))


# ═══ c4-04 · mass-cover ══════════════════════════════════════════════════

def r_mass_cover(a, act_id):
    """⊕ c4-04 `#s-cover` — MRB-204 part 2, the rule DRAWN as a part–whole bar.

    ⚖️ **A BAR, NEVER A TRIANGLE, AND THIS IS THE RULED SHAPE.** MRB-204 as
    amended at MRB-246: a triangle encodes `A = B × C`; a beam or a part–whole
    bar encodes a SUM. Conservation of mass is a sum. Drawing it as a triangle
    would tell a student that two of these masses multiply together to give the
    third, which is not a relationship that exists. Design drew a bar, the bar
    is correct, and a later pass that "restores the triangle" would be teaching
    a false relationship to make a rule fit. Do not redraw it.

    ⚖️ AND IT IS AN ACTIVITY, NOT `r_cover_bar`. See the module header for the
    full reasoning and for why the `build_ks3.py` comment about `cover-triangle`
    does not govern this page: Design's own `RAIL` and `DONE()` both name
    `s-cover`, so it ticks a stop.

    ⚠️ RADIO, NEVER A TOGGLE, AND IT OPENS UNCOVERED. Design's `cover` starts
    `null`, so the resting DOM has every plate hidden and the result panel
    empty — unlike c2-06's bar, which opens with the gas already covered. The
    stop ticks on the FIRST press and `markStage` is a ratchet, so changing
    which cell is covered never withdraws the credit.

    ⚠️ THE PLATE'S "?" IS `--ks3-data`, NOT `--ks3-alert`. Design paints it
    amber. MRB-252 ruled amber for WARNING AND CONFRONTATION — the `#s-think`
    register, genuine caution and loss — and moved CATEGORY AND SELECTION to
    `--ks3-data`. A plate that says *this is the cell you covered, this is the
    unknown you are solving for* is selection, not warning; it is neither a
    caution nor a loss, and spending amber on it wears the meaning away one
    panel at a time. The plate's ground is `--ks3-ink` at .9, which is exactly
    the on-ink use `--ks3-data` was measured for, and the glyph is 26px display
    so the large-text floor is met with room to spare. The `?` is
    `aria-hidden`: the cell's own label is real text underneath it.

    ⚠️ **THE CELL WIDTHS ARE DESIGN'S 68 / 32 AND THEY ARE NOT THE RATIO OF
    THE MASSES.** 2.20 g is one part in about seventy of 152.00 g. Drawn true,
    the gas cell would be a six-pixel sliver carrying a 24px number, and at
    390px nothing in the bar would be readable at all. §5A requires drawn
    geometry to express the ratio its label claims, so the honest resolution is
    neither to lie about it nor to shrink the cell into illegibility: the bar
    keeps Design's readable proportions and SAYS SO, in a line that turns the
    disclaimer into a quantity a student can read. The `aria_label` says the
    same thing, because a reader who cannot see the bar must not be told it is
    to scale either.

    The weights are DERIVED from the payload rather than written into the
    stylesheet, so the two cells are one authored ratio in one place — a flex
    row with the numbers hard-coded in CSS is a bar model whose halves are free
    to drift from the labels above them.

    HOOKS: see the module header.
    """
    whole = a.get("whole") or {}
    parts = a.get("parts") or []
    results = a.get("results") or {}
    if len(parts) < 2:
        raise ValueError(
            "mass-cover %r declares %d part(s). A part–whole bar needs at "
            "least two, or there is no sum to see." % (act_id, len(parts)))
    cells = [whole] + list(parts)
    ids = [c.get("id") for c in cells]
    if not all(ids):
        raise ValueError(
            "mass-cover %r has a cell with no id; the id is what a cover "
            "button, a plate and a result are joined by." % act_id)
    gaps = [i for i in ids if i not in results]
    if gaps:
        raise ValueError(
            "mass-cover %r offers cover button(s) for %s and no result for "
            "them. Every cover is a press that must open an arrangement, or "
            "it is a control that does nothing." % (act_id, gaps))
    for i in ids:
        for key in ("result", "sentence"):
            if not (results[i] or {}).get(key):
                raise ValueError(
                    "mass-cover %r cover %r has no %r. The result is the "
                    "arrangement that falls out and the sentence NAMES THE "
                    "OPERATION; NOTES-C4 §4 asks for both, and the sentence "
                    "is where the addition or the subtraction is said out "
                    "loud." % (act_id, i, key))
        if not (cells[ids.index(i)].get("label")
                and cells[ids.index(i)].get("value")):
            raise ValueError(
                "mass-cover %r cell %r has no label or no value. §5A: if the "
                "lesson names a quantity it must be readable as a NUMBER."
                % (act_id, i))

    def cell(c, extra_style=""):
        return ('<div class="ks3-mcov-cell"%s>'
                '<p class="ks3-mcov-celllabel">%s</p>'
                '<p class="ks3-mcov-cellvalue">%s</p>'
                '<span class="ks3-mcov-plate" aria-hidden="true" hidden '
                'data-mcov-plate="%s">?</span></div>'
                % (extra_style, t(c.get("label", "")), t(c.get("value", "")),
                   e(c["id"])))

    total_weight = sum(float(p.get("weight") or 0) for p in parts) or len(parts)
    part_cells = "".join(
        cell(p, ' style="flex:%s 1 0"' % ("%g" % (100.0 * float(
            p.get("weight") or 0) / total_weight)))
        for p in parts)

    bar = ('<div class="ks3-mcov-bar" role="img" aria-label="%s">'
           '%s<div class="ks3-mcov-parts">%s</div></div>'
           % (e(a.get("aria_label", "")), cell(whole), part_cells))

    scale = ('<p class="ks3-mcov-scale">%s</p>' % rich(a["scale_note"])
             if a.get("scale_note") else "")

    btns = "".join(
        _c4_seg("ks3-mcov-btn", False, c.get("button", ""),
                data_mcov_for=c["id"])
        for c in cells)

    # EMIT-BOTH-SHOW-ONE: all three arrangements are in the document and one is
    # unhidden. Nothing is assembled out of an attribute, so the minus signs
    # and the ampersand-free arithmetic survive as authored and no sentence is
    # duplicated between Python and JS.
    outs = "".join(
        '<div class="ks3-mcov-outcome" hidden data-mcov-result="%s">'
        '<p class="ks3-mcov-result">%s</p>'
        '<p class="ks3-mcov-sentence">%s</p></div>'
        % (e(i), rich(results[i]["result"]), rich(results[i]["sentence"]))
        for i in ids)

    close = ('<p class="ks3-mcov-close">%s</p>' % rich(a["close"])
             if a.get("close") else "")

    # The unit rows. The pill is the unit and the line beside it is the
    # quantity: the unit belongs to the answer, which is what the worked
    # example's Answer step says once more three sections later.
    units = ""
    if a.get("units"):
        units = ('<div class="ks3-mcov-units">%s</div>'
                 % "".join('<div class="ks3-mcov-unitrow">'
                           '<span class="ks3-mcov-quantity">%s</span>'
                           '<span class="ks3-mcov-unit">%s</span></div>'
                           % (t(u.get("quantity", "")), t(u.get("unit", "")))
                           for u in a["units"]))

    # Design draws the plain-English restatement in a bordered card at the top
    # of the section, ABOVE the eyebrow. The activity shell emits its eyebrow
    # and <h2> first, so the card is this instrument's opening element and
    # lands one row lower than on the reference. Reported; the alternative was
    # a CSS `order` that would have put the DOM and the reading order at odds
    # for a screen reader, to save one row for a sighted one.
    rule = ('<div class="ks3-mcov-rule"><p>%s</p></div>' % rich(a["rule"])
            if a.get("rule") else "")

    return ('<div class="ks3-mcov" data-mcov>%s%s%s'
            '<div class="ks3-mcov-btns">%s</div>'
            '<div class="ks3-mcov-out" hidden data-mcov-out>%s</div>'
            '%s%s</div>'
            % (rule, bar, scale, btns, outs, close, units))


# ═══ c4-04 · mass-worked ═════════════════════════════════════════════════

def _c4_steps(ns, steps, act_id, with_prompt):
    """The four F / I / F / A step boxes, shared by `mass-worked` and
    `mass-check`.

    ONE FUNCTION, because the thing that must not drift between parts 3 and 4
    of MRB-204's treatment is precisely that they are the SAME FOUR STEPS. A
    student who sees a different badge, a different name or a different box on
    the second one has been shown a second method, which is the opposite of
    what the scaffolding is for. The two families differ in what opens a step
    — one button walking down the list, or a compare button per step — and in
    nothing else, so that is the only thing the two renderers do separately.

    `data-open` and `data-next` carry the state; the badge fill and the box
    ground are CSS on those attributes rather than inline styles, so there is
    one definition of "an open step" instead of one per language.

    ⚠️ THE LETTER IS `aria-hidden`. Each step's real name — Formula, Insert,
    Fine-tune, Answer — is real text beside it, so the badge is reinforcement
    for a sighted reader and never the only route to which step this is.
    """
    if len(steps) != 4:
        raise ValueError(
            "%s %r has %d step(s). FIFA is four steps and the badges spell it; "
            "three or five is a different method wearing the same name."
            % (ns, act_id, len(steps)))
    out = []
    for i, s in enumerate(steps):
        needed = ("letter", "name", "maths", "note")
        # ⚠️ The scaffolded half needs a `prompt` on EVERY step, and a missing
        # one is a step the student is asked to do with nothing telling them
        # what to do — which reads as an empty box rather than as an error.
        if with_prompt:
            needed += ("prompt",)
        for key in needed:
            if not s.get(key):
                raise ValueError("%s %r step %d has no %r." % (ns, act_id, i,
                                                               key))
        prompt = ('<p class="ks3-%s-prompt">%s</p>' % (ns, rich(s["prompt"]))
                  if with_prompt else "")
        out.append(
            '<li class="ks3-%s-step" data-%s-step="%d" data-open="0" '
            'data-next="%s">'
            '<span class="ks3-%s-badge" aria-hidden="true">%s</span>'
            '<div class="ks3-%s-body">'
            '<p class="ks3-%s-name">%s</p>%s'
            '<div class="ks3-%s-open" hidden data-%s-open>'
            '<p class="ks3-%s-maths">%s</p>'
            '<p class="ks3-%s-note">%s</p></div>'
            '{extra%d}</div></li>'
            % (ns, ns, i, "1" if i == 0 else "0",
               ns, t(s["letter"]),
               ns, ns, t(s["name"]), prompt,
               ns, ns, ns, rich(s["maths"]), ns, rich(s["note"]), i))
    return out


def r_mass_worked(a, act_id):
    """⊕ c4-04 `#s-worked` — MRB-204 part 3, the worked example one step at a
    time with the F / I / F / A badges visible on each step.

    ⚖️ ONE-WAY, AND ONE CONTROL AT A TIME. There is no collapse: unshowing a
    step teaches nothing and gives a student a way to lose their place. And the
    stepper offers exactly one button — the next step's — because the point of
    the pause is that the reader tries the next line before reading it. A page
    that shows all four at once is a page a student scrolls past.

    ⚠️ THE BUTTON'S TWO LABELS ARE BOTH IN THE DOCUMENT AND ONE IS SHOWN
    (EMIT-BOTH-SHOW-ONE). "Show the first step" and "Show the next step" are
    authored sentences, and §6 forbids a sentence living in a `data-` attribute
    for JS to read back out. Two spans, one hidden, nothing composed.

    ⚠️ NOTHING GREEN AND NOTHING RED. An opened step is opened, not correct:
    the badge takes the accent fill Design paints it and the box takes the
    inset ground. There is no marking anywhere in this instrument, because the
    student has not answered anything — they have watched.

    HOOKS: see the module header.
    """
    steps = a.get("steps") or []
    boxes = _c4_steps("mwork", steps, act_id, with_prompt=False)
    # No per-step control on the watched half: one button walks the list.
    body = "".join(b.replace("{extra%d}" % i, "")
                   for i, b in enumerate(boxes))
    return ('<div class="ks3-mwork" data-mwork data-total="%d">'
            '<ol class="ks3-mwork-steps" role="list">%s</ol>'
            '<button type="button" class="ks3-reveal-btn ks3-mwork-next" '
            'data-mwork-next>'
            '<span data-mwork-label="first">%s</span>'
            '<span data-mwork-label="next" hidden>%s</span>'
            '</button></div>'
            % (len(steps), body,
               t(a.get("first_label") or "Show the first step"),
               t(a.get("next_label") or "Show the next step")))


# ═══ c4-04 · mass-check ══════════════════════════════════════════════════

def r_mass_check(a, act_id):
    """⊕ c4-04 `#s-check` — MRB-204 part 4, the same four steps done by the
    STUDENT, with a compare button PER STEP.

    ⚖️ **A COMPARE BUTTON PER STEP IS THE WHOLE DIFFERENCE FROM `#s-worked`,
    AND IT IS NOT A CONVENIENCE.** One reveal at the end lets a student write
    four lines, read four lines and mark themselves; a button on each line
    catches them at the step they got wrong, while it still matters and before
    the error has been carried into the next three. NOTES-C4 §4 asks for it in
    those words, and it is the reason this section costs a rail stop of its own
    rather than sharing `#s-worked`'s.

    ⚠️ EACH STEP'S PROMPT IS ON THE PAGE FROM THE START, AND ITS ANSWER IS NOT.
    That is the difference between scaffolding and a solution: the student is
    told what to do at every line and shown what it looks like only after they
    have done it. `prompt` is authored per step for exactly that.

    ⚠️ THE BUTTON LABEL IS A TEMPLATE, `Compare step {n}`, AND `{n}` IS THE
    INSTRUMENT'S. §5A forbids hard-coding a figure the instrument computes;
    four authored labels reading "Compare step 1" … "Compare step 4" would be
    the step number written down four times in a place nothing checks against
    the step it sits on. Filled here, at render, from the step's own index.

    ⚠️ ONE BUTTON VISIBLE AT A TIME, and it is the next unopened step's — the
    same discipline as `#s-worked`, so the two halves of the treatment behave
    identically. Every button is in the document; three of the four are hidden
    at rest.

    HOOKS: see the module header.
    """
    steps = a.get("steps") or []
    tpl = a.get("compare_label") or "Compare step {n}"
    if "{n}" not in tpl:
        raise ValueError(
            "mass-check %r's compare label %r has no {n}. The step number is "
            "the instrument's and must not be written out four times."
            % (act_id, tpl))
    boxes = _c4_steps("mchk", steps, act_id, with_prompt=True)
    body = []
    for i, box in enumerate(boxes):
        btn = ('<button type="button" class="ks3-reveal-btn ks3-mchk-btn"%s '
               'data-mchk-btn="%d">%s</button>'
               % ("" if i == 0 else " hidden", i,
                  t(tpl.replace("{n}", str(i + 1)))))
        body.append(box.replace("{extra%d}" % i, btn))
    close = ('<div class="ks3-mchk-close" hidden data-mchk-close>'
             '<p>%s</p></div>' % rich(a["close"])) if a.get("close") else ""
    return ('<div class="ks3-mchk" data-mchk data-total="%d">'
            '<ol class="ks3-mchk-steps" role="list">%s</ol>%s</div>'
            % (len(steps), "".join(body), close))


# ── registrations ────────────────────────────────────────────────────────
#
# Four families, no drawer. All four tick a rail stop, so all four carry
# `data-stage-done="0"` — NOTHING IS TICKED ON LOAD (MRB-208). `data-instrument`
# keeps `wirePredictions` out of the bench's own prediction options.
#
# ⚠️ `mass-cover` IS REGISTERED AS A FAMILY ON PURPOSE. It is not
# `cover-triangle`'s bar variant and it is not a `formula` block's `cover` key;
# see the module header. Its shell carries `data-stage-done="0"` because
# Design's own `DONE()` ticks it.


# ── from art_05.py ─────────────────────────────────────
# ═══ c4-05 · coefficient-balancer + forbidden-move ═══════════════════════
#
# Fragment for `ks3_art/c4.py`. Markup only: everything that has to be
# RECOMPUTED as the student presses a control is `js_05.js`'s job, and this
# file emits the data it needs plus the RESTING DOM — the state the page is in
# before a line of JavaScript has run, which is also what a crawler and a
# no-JS reader see. A resting render that disagrees with the payload is a
# wrong number in the bytes, not a flicker.
#
# ─── THE SUBSCRIPT CONVENTION. THIS UNIT STANDARDISES IT AND OWNS IT. ─────
#
# ⚖️ **EVERY FORMULA ON THIS PAGE IS BUILT FROM `parts: [{sym, sub}]`, AND A
# SUBSCRIPT IS A REAL `<sub>` ELEMENT.** Never a Unicode subscript character,
# never a styled span, never a bare digit sitting at full size. `_cbal_parts`
# below is the ONE place it happens and every downstream chemistry unit
# inherits it, so it is worth stating why rather than leaving it to be
# re-derived:
#
#   · It is SEMANTIC. The 2 in H₂O is part of how the substance is spelled,
#     and this whole lesson turns on the difference between that 2 and the
#     one in front. A reader who loses the distinction loses the lesson.
#   · THE UNICODE ROUTE DOES NOT EXIST for the general case. There is no
#     subscript glyph for every character chemistry needs, the shipped latin
#     woff2 subsets carry none of them, and c3-06's `R<sub>f</sub>` already
#     proved the point (there is no U+2093-style subscript `f`). Mixing real
#     subscripts for some formulae and characters for others would be two
#     conventions.
#   · IT IS ADMITTED TO `rich()` FOR EXACTLY THIS. C2 flag 13 ruled the
#     convention for the course and `kit._RICH_OK` gained `sub` under
#     MRB-272 to serve it, on the two-part test the allow-list is drawn at:
#     `<sub>` is semantic rather than styling, and it carries no attributes,
#     so it is neither an injection hole nor a styling backdoor.
#
# ⚠️ AND IT DOES NOT REACH THE LADDER. `_rung_marked` escapes a marked rung's
# question and options with `t()` and escapes its per-option correction into a
# `data-feedback` ATTRIBUTE, so a `<sub>` in any of those ships as visible
# angle brackets — the escape-as-visible defect, on the page's assessment.
# Design writes every ladder formula flat (`H2O2`, `2Mg + O2`) and the lesson
# record keeps them flat. The split is deliberate and is documented at both
# ends.
#
# ⚠️ AN EMPTY `sub` EMITS NO ELEMENT. Design's own template writes
# `<sub>{{p.sub}}</sub>` unconditionally, which puts an empty `<sub></sub>`
# after every Mg, Na and Cl on the page. Visually identical, semantically
# noise, and it makes a `<sub>` in the built bytes stop meaning "there is a
# subscript here" — which is the one thing a grep over these pages will want
# to ask. Omitted.
#
# ─── THE TWO CONVENTIONS THAT RUN THROUGH BOTH RENDERERS ─────────────────
#
#   · EMIT-BOTH-SHOW-ONE. Four equations, four `words` paragraphs, three
#     counter-state sentences per counter, two forbidden-move verdicts and
#     two products are ALL in the document, with one of each shown. Nothing
#     is ever assembled out of an attribute, so `<em>`, `<strong>`, `<sub>`
#     and an ampersand survive exactly as the author wrote them and no
#     sentence is duplicated between Python and JS where the two could drift.
#   · A JSON `data-cfg` ONLY for what genuinely has to be recomputed — the
#     atom counts, the targets, the bounds. NEVER for a sentence.
#
# ─── §5A, AND WHERE EACH RULE IS DISCHARGED ──────────────────────────────
#
#   · never narrate the controls — the coefficient cap (NOTES §5 flag 15) is
#     a property of the STEPPER and is never written down as a rule of
#     chemistry. At the bound the button takes `aria-disabled` and stops
#     responding. There is no sentence about it anywhere on the page.
#   · never hard-code a figure the instrument computes — every counter is
#     derived from `atoms` × the live coefficients, in `_cbal_counts`, in
#     both languages, with the same arithmetic.
#   · comparative labels DERIVED at render, and the equal state driven —
#     `_cbal_assert` walks the WHOLE reachable state space of every equation
#     (at most 4⁴ = 256 vectors each), drives the target, and checks the
#     counters agree.
#   · enumerate the whole state space including the on-load state and every
#     zero — done, and the assertion proves there IS no zero: every
#     coefficient is at least `min` and every term carries at least one atom
#     of each element it contributes, so "Too few on the left/right" is
#     always a real shortfall.
#   · if the lesson names a quantity it must be readable as a NUMBER — the
#     per-element counts are printed as numerals in their own spans.
#   · branch verdicts on the thing the lesson teaches — `solved` branches on
#     the TARGET and the "Balanced." panel branches on the COUNTS, and those
#     are two different tests. See `_cbal_assert`.
#
# ⚖️ ONLY THE LADDER MARKS. Nothing green and nothing red reaches any control
# here. A matched counter is a READING and takes the blue reading treatment,
# never `--ks3-ok` — see `css_05.css`, where the reason is written out: on
# this page of all pages, painting "the counts match" in the colour the page
# uses for "you got it right" would be `REACT-09` rendered in CSS.


# ── one JSON payload, and the only one ───────────────────────────────────

def _c4_cfg(obj):
    """`data-cfg`, deterministically ordered and safe in an attribute.

    ⚠️ A LOCAL COPY ON PURPOSE. `ks3_art/c3.py` has the same three lines under
    the name `_cfg`, and reaching across for it would make this module depend
    on another unit's module — one unit, one file, and a lane that imports
    another lane's file stops being a lane. Promoting it into `ks3_art/kit.py`
    is the right long-term move and is a SHARED-FILE edit, so it is reported
    rather than taken.

    `sort_keys` so two builds of the same payload are byte-identical;
    `ensure_ascii=False` so a non-ASCII character stays itself rather than
    becoming six characters of escape inside an attribute nobody reads.
    """
    return e(json.dumps(obj, separators=(",", ":"), sort_keys=True,
                        ensure_ascii=False))


# ── formulae ─────────────────────────────────────────────────────────────

def _cbal_parts(parts):
    """`[{sym, sub}]` → `H<sub>2</sub>O`. THE convention (see the header).

    `t()` on both halves: a symbol and a subscript are LABELS, and neither is
    an attribute value. An absent or empty `sub` emits no element at all.
    """
    out = []
    for p in parts or []:
        sym = p.get("sym", "")
        sub = p.get("sub", "")
        out.append("<span class=\"ks3-cbal-sym\">%s%s</span>"
                   % (t(sym), ("<sub>%s</sub>" % t(sub)) if sub != "" else ""))
    return "".join(out)


def _cbal_arrow():
    """Design's own equation arrow, at her geometry (page line 145).

    ⚠️ NOT `MARK_ARROW`. That one is `1em` of whatever text it sits in and is
    right inside a sentence; this is the arrow of a DISPLAY EQUATION, drawn at
    Design's 44×24 on a 2.6 stroke so it reads at the 26px display size the
    formulae are set in. A typed `→` is for prose only — the shipped font
    subsets contain no glyph for U+2192 — which is why both arrows are drawn.
    """
    return ('<svg class="ks3-cbal-arrow" viewBox="0 0 44 24" width="44" '
            'height="24" aria-hidden="true" focusable="false">'
            '<path d="M4 12h30M26 5l8 7-8 7" fill="none" stroke="currentColor"'
            ' stroke-width="2.6" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>')


# ── the arithmetic, in Python, once ──────────────────────────────────────

def _cbal_terms(eq):
    """Left then right, in document order. The coefficient index IS this order."""
    return list(eq.get("left") or []) + list(eq.get("right") or [])


def _cbal_els(eq):
    """Every element in the equation, in first-appearance order.

    The SAME order Design's page derives (`Object.keys` over each term's
    `atoms`, in term order), so the counter tiles read left to right in the
    order the formulae introduce their elements — C then H then O on methane,
    not alphabetically.
    """
    els = []
    for tm in _cbal_terms(eq):
        for el in (tm.get("atoms") or {}):
            if el not in els:
                els.append(el)
    return els


def _cbal_counts(eq, coeffs):
    """(element, atoms on the left, atoms on the right) — DERIVED, always.

    ⚖️ This function and `c4Counts` in `js_05.js` are the same arithmetic and
    there is no other. Nothing anywhere prints a count that did not come out
    of one of them.
    """
    left = eq.get("left") or []
    nl = len(left)
    out = []
    for el in _cbal_els(eq):
        lo = sum((tm.get("atoms") or {}).get(el, 0) * coeffs[i]
                 for i, tm in enumerate(left))
        hi = sum((tm.get("atoms") or {}).get(el, 0) * coeffs[nl + j]
                 for j, tm in enumerate(eq.get("right") or []))
        out.append((el, lo, hi))
    return out


def _cbal_vectors(n, lo, hi):
    """Every coefficient vector the stepper can reach. At most 4⁴ = 256."""
    vecs = [[]]
    for _ in range(n):
        vecs = [v + [k] for v in vecs for k in range(lo, hi + 1)]
    return vecs


def _cbal_assert(eq, lo, hi, act_id):
    """⚖️ THE CONTENT-TRUTH ASSERTION, WALKING THE WHOLE STATE SPACE.

    Not a sample and not the target alone. Every reachable coefficient vector
    is driven and its counters are read, and five properties are checked. Each
    one is a sentence somewhere on the page that would otherwise be able to
    become false without anything failing:

      1. `target` has one entry per term and every entry is inside the
         stepper's bounds — otherwise the equation cannot be solved at all and
         `#s-balance` becomes a rail stop that can never tick. This is
         NOTES §5 flag 15's "every target is reachable", checked rather than
         asserted in a comment.
      2. The target BALANCES. `solved` branches on the target and the
         "Balanced." panel branches on the counts; they are two different
         tests and the lesson is only coherent while the first implies the
         second. (It does not go the other way — see 4.)
      3. NO COUNT IS EVER ZERO anywhere in the space, so "Too few on the
         left" / "Too few on the right" is always a real shortfall on a side
         that has something on it, never an empty side.
      4. EVERY OTHER BALANCED STATE IS A WHOLE MULTIPLE OF THE TARGET, k ≥ 2.
         This is what `multiple_note` says out loud, and it is the property
         that makes the sentence true: at 4H₂ + 2O₂ → 4H₂O the counts match,
         the equation is genuinely balanced, and it is not the answer. If a
         future equation had a balanced state that was NOT a multiple of its
         target, that sentence would be a lie and this raises instead.
      5. The target is therefore the SMALLEST balanced state, which is the
         convention the stretch layer teaches.

    Cheap — 256 vectors at the very worst — and it runs on every build.
    """
    terms = _cbal_terms(eq)
    target = list(eq.get("target") or [])
    eid = eq.get("id")
    if len(target) != len(terms):
        raise ValueError(
            "coefficient-balancer %r equation %r has %d term(s) and a target "
            "of %d. The target IS the coefficient vector, one number per "
            "term." % (act_id, eid, len(terms), len(target)))
    for tm in terms:
        if not tm.get("parts"):
            raise ValueError(
                "coefficient-balancer %r equation %r has a term with no "
                "`parts`. Formulae are drawn from parts so subscripts are "
                "real elements; a term with none renders as nothing at all."
                % (act_id, eid))
        if not tm.get("atoms"):
            raise ValueError(
                "coefficient-balancer %r equation %r has a term with no "
                "`atoms`. The counters are derived from `atoms` and from "
                "nothing else, so a term without them is invisible to the "
                "very thing this instrument measures." % (act_id, eid))
    out_of_range = [v for v in target if v < lo or v > hi]
    if out_of_range:
        raise ValueError(
            "coefficient-balancer %r equation %r needs coefficient(s) %s, "
            "which the stepper's %d–%d range cannot reach. The stop could "
            "never tick." % (act_id, eid, out_of_range, lo, hi))
    if any(l != r for _el, l, r in _cbal_counts(eq, target)):
        raise ValueError(
            "coefficient-balancer %r equation %r declares target %s, and at "
            "that target the counters do NOT agree: %s. The target is what "
            "the instrument credits; an unbalanced one credits a wrong answer."
            % (act_id, eid, target,
               ", ".join("%s %d/%d" % c for c in _cbal_counts(eq, target))))

    multiples = []
    for vec in _cbal_vectors(len(terms), lo, hi):
        counts = _cbal_counts(eq, vec)
        for el, l, r in counts:
            if l == 0 or r == 0:
                raise ValueError(
                    "coefficient-balancer %r equation %r reaches a state "
                    "(%s) with zero %s atoms on a side. 'Too few on the "
                    "left/right' would be describing an empty side."
                    % (act_id, eid, vec, el))
        if any(l != r for _el, l, r in counts) or vec == target:
            continue
        ratios = set()
        for got, want in zip(vec, target):
            if got % want:
                raise ValueError(
                    "coefficient-balancer %r equation %r balances at %s, "
                    "which is not a whole multiple of its target %s. "
                    "`multiple_note` tells the student every number is k "
                    "times bigger than it needs to be, and at this state "
                    "that sentence is false." % (act_id, eid, vec, target))
            ratios.add(got // want)
        if len(ratios) != 1:
            raise ValueError(
                "coefficient-balancer %r equation %r balances at %s, whose "
                "terms are different multiples %s of the target %s. There is "
                "no single k to print." % (act_id, eid, vec, sorted(ratios),
                                           target))
        multiples.append(ratios.pop())
    return sorted(set(multiples))


# ── c4-05 · coefficient-balancer ═════════════════════════════════════════

def r_coefficient_balancer(a, act_id):
    """⊕ c4-05 `#s-balance` — four equations, two controls each, live counters.

    ⚖️ **THE STUDENT MAY CHANGE ONE KIND OF NUMBER AND THE INSTRUMENT OFFERS
    NO OTHER.** There is a `+` and a `−` in front of every formula and there
    is nothing at all attached to a subscript, because the whole lesson is
    which number is theirs. The forbidden move is not disabled here; it is a
    SEPARATE SECTION with a button of its own (`r_forbidden_move`), so that a
    student who wants to make it can, and is then shown what they wrote.

    ⚖️ `solved` IS THE TARGET AND `balanced` IS THE COUNTS, AND THEY ARE NOT
    THE SAME TEST. Every equation here has exactly two balanced states inside
    the cap — its target and the target doubled — and only the target ticks
    the tab. At the doubled state the panel still says "Balanced.", because it
    is, and the note beside it changes to the one that says it is not in its
    smallest numbers. That is the "Going further" paragraph's own case
    ("4H₂ + 2O₂ makes 4H₂O is balanced and would still be marked down"),
    reached at the moment the student produces it instead of praised now and
    marked down four sections later — which §14 forbids.

    ⚠️ THE RESTING DOM IS THE HOOK'S OWN STATE. First equation, every
    coefficient at 1: hydrogen already matches at 2 and 2, oxygen reads 2 on
    the left against 1 on the right. That is exactly the equation the hook
    opens with, and it is in the shipped bytes rather than painted on load.

    ⚠️ THE CAP IS A PROPERTY OF THE CONTROL AND IS NEVER NARRATED (§11, and
    NOTES §5 flag 15 — the cap is a help, and an uncapped stepper turns a
    chemistry lesson into a number puzzle). At the bound the button takes
    `aria-disabled="true"`, which dims it and makes the handler return early.
    Deliberately NOT `disabled`: a real `disabled` attribute drops keyboard
    focus the instant the student steps to 4 with the `+` key, and losing
    focus to the document body is a worse defect than a dimmed control.

    HOOKS: `data-cbal` (wrapper, with `data-cfg`) · `data-cbal-tab` (a tab,
    valued with the equation id) · `data-cbal-tick` (its solved dot) ·
    `data-cbal-eq` (one equation's whole block) · `data-cbal-coeff` (a
    coefficient span, valued with its term index, plus `data-cbal-lit`) ·
    `data-cbal-for` + `data-cbal-delta` (a stepper button) ·
    `data-cbal-counter` (a counter tile, valued with its element, plus
    `data-cbal-match`) · `data-cbal-left` / `data-cbal-right` (its two
    numbers) · `data-cbal-st` (one of its three state sentences) ·
    `data-cbal-balanced` (the panel) · `data-cbal-note` (`target` or
    `multiple`) · `data-cbal-k` · `data-cbal-reset` · `data-cbal-summary`.
    """
    eqs = a.get("equations") or []
    if not eqs:
        raise ValueError(
            "coefficient-balancer %r declares no equations[]." % act_id)
    lo = int(a.get("min", 1))
    hi = int(a.get("max", 4))
    if hi <= lo:
        raise ValueError(
            "coefficient-balancer %r has a stepper range of %d–%d, which is "
            "not a range." % (act_id, lo, hi))
    states = a.get("counter_states") or {}
    for key in ("matched", "short_right", "short_left"):
        if not states.get(key):
            raise ValueError(
                "coefficient-balancer %r has no `counter_states[%r]`. Every "
                "counter carries a WORD as well as a treatment (R2), and all "
                "three states are reachable on every equation." % (act_id, key))
    multiple_note = a.get("multiple_note") or ""
    if "{k}" not in multiple_note:
        raise ValueError(
            "coefficient-balancer %r's `multiple_note` does not contain "
            "`{k}`. The multiple is DERIVED from the coefficients and the "
            "target and is never written down as a number." % act_id)
    # ⚠️ SPLIT IN PYTHON, NOT FILLED IN JS. The sentence is authored once and
    # reaches the page in two halves either side of the span that holds the
    # number, so no template ever lives in the wiring and no `{k}` can survive
    # to a student if the runtime never runs.
    note_head, _, note_tail = multiple_note.partition("{k}")

    cfg_eqs = []
    tabs = []
    blocks = []
    for i, eq in enumerate(eqs):
        eid = eq.get("id") or "eq%d" % i
        multiples = _cbal_assert(eq, lo, hi, act_id)
        terms = _cbal_terms(eq)
        left = eq.get("left") or []
        nl = len(left)
        rest = [lo] * len(terms)
        first = (i == 0)

        cfg_eqs.append({
            "id": eid,
            "nl": nl,
            "els": _cbal_els(eq),
            "atoms": [dict(tm.get("atoms") or {}) for tm in terms],
            "target": list(eq.get("target") or []),
        })

        # ── the tab ──────────────────────────────────────────────────────
        # The solved dot is Design's (`e.tab + (solved ? ' ·' : '')`). It is
        # aria-hidden and carries a word beside it in the clipped span, so a
        # screen reader gets "done" rather than a middle dot read as
        # punctuation or skipped entirely (R2 again: the mark is never the
        # only signal).
        tabs.append(
            '<button type="button" class="ks3-seg-btn ks3-cbal-tab" '
            'data-cbal-tab="%s" aria-pressed="%s">%s'
            '<span class="ks3-cbal-tick" data-cbal-tick="%s" hidden>'
            '<span aria-hidden="true"> ·</span>'
            '<span class="ks3-sr-only"> solved</span></span></button>'
            % (e(eid), "true" if first else "false", t(eq.get("tab", "")),
               e(eid)))

        # ── the terms ────────────────────────────────────────────────────
        def _side(items, offset):
            out = []
            for j, tm in enumerate(items):
                idx = offset + j
                if j:
                    out.append('<span class="ks3-cbal-plus" '
                               'aria-hidden="true">+</span>')
                out.append(
                    '<div class="ks3-cbal-term">'
                    '<p class="ks3-cbal-formula">'
                    '<span class="ks3-cbal-coeff" data-cbal-coeff="%d" '
                    'data-cbal-lit="%s">%d</span>%s</p>'
                    '<div class="ks3-cbal-steps">'
                    '<button type="button" class="ks3-cbal-step" '
                    'data-cbal-for="%d" data-cbal-delta="-1" '
                    'aria-label="%s" aria-disabled="%s">−</button>'
                    '<button type="button" class="ks3-cbal-step" '
                    'data-cbal-for="%d" data-cbal-delta="1" '
                    'aria-label="%s" aria-disabled="%s">+</button>'
                    '</div></div>'
                    % (idx, "1" if rest[idx] > lo else "0", rest[idx],
                       _cbal_parts(tm.get("parts")),
                       idx, e("Decrease the number in front"),
                       "true" if rest[idx] <= lo else "false",
                       idx, e("Increase the number in front"),
                       "true" if rest[idx] >= hi else "false"))
            return "".join(out)

        # ── the counters, DERIVED from the resting coefficients ──────────
        counters = []
        for el, l, r in _cbal_counts(eq, rest):
            key = ("matched" if l == r
                   else "short_right" if l > r else "short_left")
            counters.append(
                '<div class="ks3-cbal-counter" data-cbal-counter="%s" '
                'data-cbal-match="%s">'
                '<p class="ks3-cbal-el">%s atoms</p>'
                '<p class="ks3-cbal-line">'
                '<span data-cbal-left>%d</span> left · '
                '<span data-cbal-right>%d</span> right</p>'
                '<p class="ks3-cbal-state">%s</p></div>'
                % (e(el), "1" if l == r else "0", t(el), l, r,
                   "".join('<span data-cbal-st="%s"%s>%s</span>'
                           % (e(k), "" if k == key else " hidden",
                              rich(states[k]))
                           for k in ("matched", "short_right", "short_left"))))

        # ── the "Balanced." panel ────────────────────────────────────────
        # ⚠️ DERIVED FROM THE RESTING COUNTS, NOT ASSUMED HIDDEN. Every
        # target in this unit is something other than "1 in front of
        # everything", so the panel is in fact closed on load — but that is a
        # property of the DATA and reading it off the counts is what keeps
        # the resting bytes right if a later equation happens to balance at
        # its opening state.
        #
        # ⚠️ THE MULTIPLE PARAGRAPH IS ONLY DRAWN IF IT IS REACHABLE. An
        # equation whose only balanced state inside the cap is its target has
        # no second note to show, and drawing one would be drawing a panel
        # that is not modelled (§5A). Its resting number is the SMALLEST
        # multiple the enumeration actually found, never a literal 2.
        rest_counts = _cbal_counts(eq, rest)
        rest_balanced = all(l == r for _el, l, r in rest_counts)
        rest_target = (rest == list(eq.get("target") or []))
        show_multiple = rest_balanced and not rest_target
        note = (
            '<p class="ks3-cbal-note" data-cbal-note="target"%s>%s</p>'
            % (" hidden" if show_multiple else "", rich(eq.get("note", ""))))
        if multiples:
            note += (
                '<p class="ks3-cbal-note" data-cbal-note="multiple"%s>'
                '%s<span data-cbal-k>%d</span>%s</p>'
                % ("" if show_multiple else " hidden",
                   rich(note_head), multiples[0], rich(note_tail)))

        blocks.append(
            '<div class="ks3-cbal-eq" data-cbal-eq="%s"%s>'
            '<p class="ks3-cbal-words">%s</p>'
            '<div class="ks3-cbal-panel">'
            '<div class="ks3-cbal-side">%s</div>%s'
            '<div class="ks3-cbal-side">%s</div></div>'
            '<div class="ks3-cbal-counters">%s</div>'
            '<div class="ks3-cbal-balanced"%s data-cbal-balanced>'
            '<p class="ks3-cbal-balanced-h">%s</p>%s</div>'
            '</div>'
            % (e(eid), "" if first else " hidden",
               rich(eq.get("words", "")),
               _side(left, 0), _cbal_arrow(),
               _side(eq.get("right") or [], nl),
               "".join(counters),
               "" if rest_balanced else " hidden",
               t(a.get("balanced_label") or "Balanced."), note))

    cfg = {"floor": lo, "cap": hi, "start": cfg_eqs[0]["id"], "eqs": cfg_eqs}

    # The resting summary follows the same rule: nothing is solved on load,
    # because `solved` is per-equation state a student has to reach.
    return ('<div class="ks3-cbal" data-cbal data-cfg="%s">'
            '<div class="ks3-cbal-tabs">%s</div>'
            '<div class="ks3-cbal-eqs">%s</div>'
            '<div class="ks3-cbal-foot">'
            '<button type="button" class="ks3-retry" data-cbal-reset>%s'
            '</button></div>'
            '<div class="ks3-cbal-summary" hidden data-cbal-summary>'
            '<p>%s</p></div></div>'
            % (_c4_cfg(cfg), "".join(tabs), "".join(blocks),
               t(a.get("reset_label") or "Set them all back to 1"),
               rich(a.get("summary", ""))))


# ── c4-05 · forbidden-move ═══════════════════════════════════════════════

def r_forbidden_move(a, act_id):
    """⊕ c4-05 `#s-forbidden` — THE FORBIDDEN MOVE IS A BUTTON, NOT A WARNING.

    ⚖️ **THE STUDENT IS ALLOWED TO MAKE THE MOVE.** This is the cleverest
    thing in the unit (NOTES §2) and the whole of it is that nothing stops
    them: adding a small 2 to the water balances the equation, and the
    equation that comes back says the reaction makes bleach. There is no
    refusal, no confirmation, no red and no warning dialog — the move is
    offered as an ordinary segmented button beside the legal one, and the
    panel that opens shows WHAT THEY ACTUALLY WROTE.

    ⚖️ AND BOTH BUTTONS STAY PRESSABLE. The point is the comparison, so a
    student who has seen one is meant to be able to see the other; neither is
    a commitment and neither is spent. What is refused is only a re-press of
    the button that is already open, which would move focus to a panel that
    has not changed.

    ⚑ `REACT-08` — "an equation can be balanced by changing the small numbers
    in a formula" — is elicited by `id="forbidden-small-2"` and confronted by
    `id="forbidden-reveal"`, and BOTH ids are emitted here, by name, because
    MRB-244 requires every join to resolve against the built page. They are
    the register's own handles and must not be renamed without renaming the
    register entry in the same edit.

    ⚑ It is `ATOM-09` in its balancing costume, and the confrontation is
    DELIBERATELY the same substance — H₂O₂ — so c2's lesson and this one
    reinforce each other (NOTES §6). Cross-referenced, never re-minted.

    ⚠️ THE PRODUCTS ARE DRAWN FROM `parts`, NOT PRINTED FROM A STRING.
    Design's page carries `forbiddenProduct` as the flat literals `'H2O2'` and
    `'2H2O'`, which would ship a page whose hook writes H<sub>2</sub>O with a
    real subscript and whose forbidden panel writes H2O2 without one — two
    conventions, forty lines apart, in the lesson that exists to teach the
    difference between a small number and a big one. Both products are built
    through `_cbal_parts` like every other formula on the page.

    HOOKS: `data-forbid` (wrapper) · `data-forbid-move` (a move button,
    valued `small`/`big`) · `data-forbid-reveal` (the panel) ·
    `data-forbid-product` · `data-forbid-text`.
    """
    moves = a.get("moves") or []
    if len(moves) != 2:
        raise ValueError(
            "forbidden-move %r offers %d move(s). It is a comparison of "
            "exactly two — the small number and the big one — and it is the "
            "comparison that teaches." % (act_id, len(moves)))
    for m in moves:
        for key in ("id", "value", "label", "product", "text"):
            if not m.get(key):
                raise ValueError(
                    "forbidden-move %r move %r has no %r. Every move needs a "
                    "button, an equation to draw and a verdict to open; one "
                    "without them is a control that goes nowhere."
                    % (act_id, m.get("value") or m.get("id"), key))
    reveal_id = a.get("reveal_id")
    if not reveal_id:
        raise ValueError(
            "forbidden-move %r declares no `reveal_id`. The panel is what "
            "REACT-08's `confronted_by` names, and a confrontation that is "
            "not addressable cannot be joined to the register." % act_id)

    btns = "".join(
        '<button type="button" id="%s" class="ks3-seg-btn ks3-forbid-btn" '
        'data-forbid-move="%s" aria-pressed="false">%s</button>'
        % (e(m["id"]), e(m["value"]), t(m["label"])) for m in moves)

    # EMIT-BOTH-SHOW-ONE: both products and both verdicts are in the
    # document, both hidden, and the panel above them is hidden too — so the
    # resting page offers the choice and gives away neither answer.
    products = "".join(
        '<span class="ks3-forbid-product" data-forbid-product="%s" hidden>'
        '%s%s</span>'
        % (e(m["value"]),
           ('<span class="ks3-cbal-coeff" data-cbal-lit="1">%s</span>'
            % t(m["coeff"])) if m.get("coeff") else "",
           _cbal_parts(m["product"]))
        for m in moves)
    texts = "".join(
        '<p class="ks3-forbid-text" data-forbid-text="%s" hidden>%s</p>'
        % (e(m["value"]), rich(m["text"])) for m in moves)

    left = "".join(
        ('<span class="ks3-cbal-plus" aria-hidden="true">+</span>'
         if j else "") + _cbal_parts(tm.get("parts"))
        for j, tm in enumerate(a.get("left") or []))

    return ('<div class="ks3-forbid" data-forbid>'
            '<div class="ks3-forbid-btns">%s</div>'
            '<div class="ks3-forbid-reveal" id="%s" hidden data-forbid-reveal>'
            '<p class="ks3-forbid-eq">%s%s%s</p>%s</div></div>'
            % (btns, e(reveal_id), left, _cbal_arrow(), products, texts))


# ── registrations ────────────────────────────────────────────────────────
#
# ⚠️⚠️ **THE PREFIX IS `cbal`, NOT `bal`, AND THAT IS A CORRECTION TO THE
# ASSIGNMENT TABLE — READ THIS BEFORE SPLICING.**
#
# The build contract §8 assigns `coefficient-balancer` the prefix `bal`,
# `data-balblock` and `data-bal`, on the stated grounds that "prefixes are
# chosen to avoid live selector collisions". That one does not: `data-bal`,
# `data-balblock` and six `data-bal-*` hooks are ALREADY LIVE, taken by C2's
# `balance-bench` (`ks3_art/c2.py` lines 551–566, registered at 856), and
# `shared/ks3.js` line 18613 already reads
#
#     each(root.querySelectorAll("[data-balblock]"), wireBalanceBench);
#
# Emitted as assigned, this instrument's section would match that selector,
# `wireBalanceBench` would run against it, parse this payload as its own
# `data-cfg` and hunt for a `[data-bal-canvas]` that is not there. It is the
# `data-critiq` case exactly — the one §8 itself cites as the precedent — and
# it is silent: nothing throws, and the instrument that gets wired twice is
# the one nobody looks at again.
#
# `cbal` and `forbid` are both measured free across `shared/ks3.js`,
# `shared/ks3.css` and every `ks3_art/*.py`. `forbid` is the contract's own
# assignment and is unchanged. Reported to the commander rather than changed
# quietly.
#
# ⚠️ SEPARATELY, AND NOT THIS LESSON'S TO FIX: §8 assigns c4-04 the FAMILY
# NAME `balance-bench`, which C2 already registers. The registry fails loudly
# on a duplicate family name across modules, so c4-04 will refuse to build
# under the assigned name. Flagged in the report.
#
# Both families tick a rail stop, so both carry `data-stage-done="0"` and
# NOTHING IS TICKED ON LOAD (MRB-208). `data-instrument` keeps the shell's
# `wirePredictions` out of the options inside them — `forbidden-move` owns its
# two buttons and `coefficient-balancer` owns every control in it.
#
# ⚠️ `forbidden-move`'s SEGMENT IS `misconception`, NOT `check`. Design draws
# `#s-forbidden` as `ks3-block ks3-misconception` — light, with the `!` badge
# and the amber eyebrow — and it is a wrong IDEA being confronted, which is
# the one meaning amber is reserved for (MRB-252). `#s-balance` is a plain
# light `ks3-block` and takes `check`. Neither is ink-dark: there is no
# ink-dark practical block anywhere in C4 or C5.
#





# REGISTER SEGMENT: 'coefficient-balancer': "check",
# REGISTER SEGMENT: 'forbidden-move': "misconception",


ART = {}

KIND_SHELL = {
    'change-pairs': ("ks3-cpair-block", ' data-instrument data-cpairblock data-stage-done="0"'),
    'chain-build': ("ks3-chain-block", ' data-instrument data-chainblock data-stage-done="0"'),
    'atom-rearranger': ("ks3-arr-block", ' data-instrument data-arrblock data-stage-done="0"'),
    'impossible-ask': ("ks3-iask-block", ' data-instrument data-iaskblock data-stage-done="0"'),
    'equation-builder': ("ks3-eqb-block", ' data-instrument data-eqbblock data-stage-done="0"'),
    'equation-read': ("ks3-eqr-block", ' data-instrument data-eqrblock data-stage-done="0"'),
    'mass-bench': ("ks3-bbench-block", ' data-instrument data-bbenchblock data-stage-done="0"'),
    'mass-cover': ("ks3-mcov-block", ' data-instrument data-mcovblock data-stage-done="0"'),
    'mass-worked': ("ks3-mwork-block", ' data-instrument data-mworkblock data-stage-done="0"'),
    'mass-check': ("ks3-mchk-block", ' data-instrument data-mchkblock data-stage-done="0"'),
    'coefficient-balancer': ("ks3-cbal-block", ' data-instrument data-cbalblock data-stage-done="0"'),
    'forbidden-move': ("ks3-forbid-block", ' data-instrument data-forbidblock data-stage-done="0"'),
}

KIND_FN = {
    'change-pairs': r_change_pairs,
    'chain-build': r_chain_build,
    'atom-rearranger': r_atom_rearranger,
    'impossible-ask': r_impossible_ask,
    'equation-builder': r_equation_builder,
    'equation-read': r_equation_read,
    'mass-bench': r_mass_bench,
    'mass-cover': r_mass_cover,
    'mass-worked': r_mass_worked,
    'mass-check': r_mass_check,
    'coefficient-balancer': r_coefficient_balancer,
    'forbidden-move': r_forbidden_move,
}
