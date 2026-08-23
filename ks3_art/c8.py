"""ks3_art.c8 — C8's instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C8 is *The periodic table*: seven authored
lessons, EIGHT instrument families and NO drawn figure, all DOM, no canvas and
no animation loop anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY, on C7's conventions and for C7's reasons. Everything an
instrument COMPUTES at run time is the JS's job; this file emits the data it
needs and the RESTING DOM — the state the page is in before a line of
JavaScript has run, which is also the state a crawler and a no-JS reader see.

  · EMIT-BOTH-SHOW-ONE wherever a panel has a small closed set of states, so
    ``<em>``, ``<strong>``, ``<sub>`` and an ampersand survive exactly as the
    author wrote them and no sentence is duplicated between Python and JS.
  · NUMBERS ARE DERIVED, NEVER AUTHORED TWICE. Every count a block's lead
    claims is computed here from the payload and cross-checked against the
    authored claim. Where the two disagree the build fails.
  · ONLY THE LADDER MARKS. Nothing green and nothing red reaches any control
    in any of these seven. A verdict panel says in words what happened. No
    ``data-correct`` on any activity option, ever.
  · Every family here ticks a rail stop, so every family carries
    ``data-stage-done="0"``. NOTHING IS TICKED ON LOAD (MRB-208).
  · Author text reaches the page through ``e()`` / ``t()`` / ``rich()``.
  · Arrows are DRAWN AS SVG, never the character U+2192 — ``t()`` does that
    substitution, and the word equations on c8-04 rely on it.
  · CONTAINMENT, NOT CLIPPING. The one horizontal scroller in this unit is
    the periodic table on c8-03, and it carries ``position: relative`` so the
    period labels inside it cannot escape and widen the document.

═══════════════════════════════════════════════════════════════════════════
⚠️ `halogen-grid`, NOT `reactivity-grid` — AND THIS IS THE THIRD TIME
═══════════════════════════════════════════════════════════════════════════

``NOTES-C8.md`` §4 names c8-05's instrument ``reactivity-grid``, "``from C5-04
with halogens substituted``", and counts it as that family's third use.

That name and its shell class ``ks3-rgrid-block`` are OWNED by
``ks3_art/c5.py``. Re-registering it here raises on the duplicate-family gate;
wearing its shell class raises on MRB-279's; and EDITING c5.py to generalise it
would be this lane reaching into another unit's module, which
``docs/ks3/worktrees.md`` §1 forbids and which would rebuild C5's pages out of
a C8 content change.

So C8 registers its own ``halogen-grid`` / ``ks3-hgrid-block`` / ``hgrid``.
Same SHAPE, own family, and c5's is neither reused nor edited — which is
exactly the call ``ks3_art/c6.py`` made for ``acid-metal-grid`` and
``ks3_art/c7.py`` made for ``rig-plan-critique``. A family name is an OWNER,
not a description.

⚖️ **The C5 ruling that DOES carry is the one about the data.** ORDER IS DATA:
whether a cell reacts is decided by comparing ``rank``, never by comparing
positions in the array. ``_hgrid_reacts()`` below is the only place that
decision is made, it is made from ``rank``, and ``r_halogen_grid`` asserts that
every authored cell agrees with it. Reordering the payload therefore cannot
change a single verdict — which is the property C5 asked for and the reason the
grid can be re-sorted for layout without re-teaching the chemistry.

═══════════════════════════════════════════════════════════════════════════
FIVE CARD BLOCKS, ONE FAMILY — `predict-cards`
═══════════════════════════════════════════════════════════════════════════

Design draws a commit-then-reveal card block on FIVE anchored sections across
four lessons:

    c8-02  #s-rules   three decisions taken against the table in the 1870s
    c8-03  #s-read    four addresses read off the table
    c8-04  #s-predict three predictions about rubidium
    c8-06  #s-file    four unknown elements to place from the model
    c8-06  #s-uses    three real uses of the noble gases to judge

Measured off her own payloads, all five are ``{id, q, options[], answer}`` —
a question, a set of commitments carrying no correct flag, and one answer
paragraph that opens whichever button was pressed. ``#s-file``'s cards add a
``tag`` (the unknown's address) and nothing else.

That is ONE instrument placed five times, not five families that look alike,
and it is registered as one for the reason ``ks3_art/c7.py`` gives for
``energy-uses``: five copies of one renderer is five chances to drift, and §6's
warning is against an identical block LINEUP arriving as a DEFAULT, not against
Design deliberately using one move repeatedly.

⊖ ``NOTES-C8.md`` §4 lists ``unknown-file`` as a family of its own. It is
folded into ``predict-cards`` with ``tag`` optional — a refinement inside the
shape Design drew, not a shape she did not draw (MRB-205). Reported.

⚖️ **NO OPTION ON ANY CARD CARRIES A CORRECT FLAG, AND THAT IS ASSERTED.**
These are commitments. The answer paragraph opens the same way whichever
button was pressed, because only the ladder marks. A ``correct`` key arriving
in a payload here would turn a commitment into a test and is refused.

═══════════════════════════════════════════════════════════════════════════
THE HOOKS ARE AN INTERFACE
═══════════════════════════════════════════════════════════════════════════

Every ``data-`` attribute below is named off the family's short name — prop /
gapf / pcard / tread / trough / hgrid / shel / oxb — and is the contract
``shared/ks3.js`` binds against. Renaming one here without renaming it there is
a silent dead instrument.

Checked free before minting, against every KIND_SHELL value in ``ks3_art`` and
against ``shared/ks3.js`` and ``shared/ks3.css``:
``ks3-prop-block``, ``ks3-gapfill-block``, ``ks3-pcards-block``,
``ks3-tread-block``, ``ks3-trough-block``, ``ks3-hgrid-block``,
``ks3-shell-block``, ``ks3-oxb-block``. Note ``ks3-gap-block`` (c1) and
``ks3-psort-block`` (c3) are TAKEN and are deliberately not what any of these
is called.

═══════════════════════════════════════════════════════════════════════════
THE pH RAMP IS COPIED, NOT IMPORTED — AND THAT IS THE `halogen-grid` RULING
═══════════════════════════════════════════════════════════════════════════

``PH_COLOURS`` below is byte-identical to ``ks3_art/c6.py``'s, which is
byte-identical to Design's own ``PH_COLOURS`` in c6-02, c6-03 **and in her
c8-07 script, where she re-declares the whole fifteen-value array rather than
referencing c6's**. That re-declaration is the measurement: Design treats the
ramp as data each page carries.

Importing c6's would be this module reading another unit's module, which the
header above forbids in both directions and which ``docs/ks3/worktrees.md`` §1
forbids for the same reason ``halogen-grid`` is not ``reactivity-grid``. The
values are the printed universal-indicator chart — scientific data, not brand
colour — so two copies cannot drift without one of them becoming factually
wrong, which is a different and much louder failure than a palette drifting.

⚠️ AND IDENTITY IS NEVER HUE-ONLY HERE EITHER. Every beaker prints its pH as a
NUMBER at 48px, says the indicator colour in WORDS, and describes what is left
on the bottom in a sentence. ``r_oxide_bench`` refuses a payload that cannot.
"""

import re

from ks3_art.kit import e, option_letter, rich, t


# ═══ shared inside C8 ════════════════════════════════════════════════════

def _c8_seg(cls, label, **attrs):
    """One segmented-control button, unpressed at rest.

    `.ks3-seg-btn` is the key stage's ONE segmented control (the Drift-4
    ruling), with a family class beside it for layout. There is no `pressed`
    parameter and no `correct` parameter, and there must never be one of
    either: nothing in C8 is pressed on load (MRB-208) and nothing outside the
    ladder is marked.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="false">%s</button>'
            % (e(cls), extra, t(label)))


def _c8_lettered(options, hook):
    """A lettered A/B/C commit list inside an instrument.

    The same markup `r_activity_options` emits, because Design draws the SAME
    control for a prediction whether it stands alone in a block or sits inside
    a bench. It gets a hook of its own because the shell's `wirePredictions`
    refuses to touch anything inside `[data-instrument]`: an instrument owns
    every option inside it, which means it also has to wire them.
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


def _counter_agrees(a, act_id, n, what):
    """The block-head counter's denominator must be the number of things.

    ⚖️ THE SMALLEST §5A ASSERTION IN THE UNIT AND THE ONE THAT WOULD SHIP
    SILENTLY. `head_counter.total` is authored beside the payload, not derived
    from it, so a seventh card under a counter that still says six produces a
    page reading "7 of 6" — clamped by `setCount` to "6 of 6", which ticks a
    rail stop the student has not finished and lies in the direction that
    looks fine.
    """
    hc = a.get("head_counter") or {}
    if not hc:
        return
    total = hc.get("total")
    if total is not None and int(total) != int(n):
        raise ValueError(
            "%s: the block-head counter says %s of %s and the payload holds "
            "%d %s. The denominator is a claim about the instrument under it."
            % (act_id, "{n}", total, n, what))


def _close_panel(a, cls, hook):
    """The payoff panel: title, paragraphs, an optional `id`, always hidden.

    The `id` is AUTHORED (`close_id`) rather than composed here, because on
    four of C8's six pages it is a misconception's `confronted_by` and MRB-244
    resolves that against the BUILT page. A name composed in a renderer is a
    name the register cannot be checked against.
    """
    paras = a.get("close") or []
    if not paras:
        return ""
    ident = (' id="%s"' % e(a["close_id"])) if a.get("close_id") else ""
    title = (('<p class="%s-closetitle">%s</p>' % (cls, t(a["close_title"])))
             if a.get("close_title") else "")
    return ('<div class="%s-close"%s hidden %s>%s%s</div>'
            % (cls, ident, hook, title,
               "".join("<p>%s</p>" % rich(p) for p in paras)))


def _words(s):
    """Lowercase, punctuation stripped, whitespace collapsed.

    Used for comparing an authored reveal against the option labels it is
    supposed to name. Meaning-bearing words only — see `r_predict_cards`.
    """
    return " ".join(re.sub(r"[^0-9a-z ]+", " ", s.lower()).split())


def _no_correct_flags(rows, act_id, family):
    """Refuse a `correct` key on any commit option, anywhere in C8.

    ⚖️ §5A, and the rule it protects is R2 rather than a number. Every option
    control in this unit outside the ladder is a COMMITMENT: the reveal opens
    the same way whichever button was pressed, and the chosen button keeps the
    ordinary chosen treatment. A `correct` flag arriving in a payload would
    make the renderer able to mark, and the next author to add one would get a
    page that marks in a unit whose whole convention is that it does not.
    """
    for row in rows:
        for opt in (row.get("options") or []):
            if not isinstance(opt, dict):
                continue
            if "correct" in opt or "correction" in opt:
                raise ValueError(
                    "%s %r: option %r carries a %r key. Nothing outside the "
                    "mastery ladder marks in C8 — the reveal opens whichever "
                    "button was pressed. Only the ladder marks (R2)."
                    % (family, act_id, opt.get("id") or opt.get("label"),
                       "correct" if "correct" in opt else "correction"))


def _cards_markup(cards, cls, hook_card, hook_opt, hook_reveal):
    """The shared commit-then-reveal card list. Used by `predict-cards`.

    Every card emits its answer paragraph into the document at build time and
    hides it — emit-both-show-one — so the markup a student's reader reaches is
    the author's, not a string JS assembled.
    """
    out = []
    for row in cards:
        tag = (('<p class="%s-tag">%s</p>' % (cls, t(row["tag"])))
               if row.get("tag") else "")
        opts = "".join(
            _c8_seg("%s-opt" % cls, o["label"], **{hook_opt: o["id"]})
            for o in row["options"])
        out.append(
            '<div class="%s-card" %s="%s" data-open="0">%s'
            '<p class="%s-q">%s</p>'
            '<div class="%s-opts">%s</div>'
            '<p class="%s-answer" hidden %s>%s</p></div>'
            % (cls, hook_card, e(row["id"]), tag,
               cls, rich(row["q"]),
               cls, opts,
               cls, hook_reveal, rich(row["answer"])))
    return "".join(out)


# ═══ c8-01 · property-sorter ═════════════════════════════════════════════

def r_property_sorter(a, act_id):
    """⊕ c8-01 `#s-bench` — six unlabelled samples, metal or non-metal.

    ⚖️ **THE RULE-BREAKERS ARE THE INSTRUMENT'S ARGUMENT AND THEY ARE
    COUNTED.** The closing panel says "Three of those broke a rule and were
    still what they were" and then names mercury, graphite and sodium. That is
    a number in a sentence a student reads AFTER sorting, about the cards they
    just sorted. It is derived from the payload's `breaks` flags and checked
    against the authored claim, so a flag flipped in a later edit fails the
    build rather than shipping a panel that contradicts the bench above it.

    ⚖️ **AND EVERY NAMED BREAKER MUST BE ON THE BENCH.** The panel names its
    three by name. A name that is not a sample id is a panel talking about a
    card that is not there.

    ⚖️ **BOTH VERDICTS MUST OCCUR.** A bench on which every sample is a metal
    teaches sorting nothing — there is no discrimination to make, and the
    student scores full marks by pressing one button six times.

    ⚠️ EACH `why` IS CHECKED TO NAME ITS OWN VERDICT FIRST. A card whose reason
    opens by saying "non-metal" under a verdict that says metal is a page
    arguing with itself in front of a student, and nothing else in the build
    could see it. This is C7's `energy-sorter` assertion, and it is here
    because c8-01's whole lesson is that the reason and the verdict are read
    together.

    HOOKS: `data-prop` (wrapper, `data-total`) · `data-prop-item` (valued with
    the sample id) · `data-prop-opt` (valued with the option id) ·
    `data-prop-reveal` · `data-prop-close`.
    """
    samples = a.get("samples") or []
    options = a.get("options") or []
    if len(samples) < 4:
        raise ValueError(
            "property-sorter %r declares %d sample(s). The lesson's claim is "
            "that several samples BREAK a rule and are still what they are, "
            "and that is not visible in three." % (act_id, len(samples)))
    if len(options) != 2:
        raise ValueError(
            "property-sorter %r offers %d option(s). Every element is one of "
            "two things here, and a third option would be a different "
            "question." % (act_id, len(options)))
    _counter_agrees(a, act_id, len(samples), "sample(s)")
    _no_correct_flags([{"options": options}], act_id, "property-sorter")

    opt_ids = [o["id"] for o in options]
    by_id, breakers, seen_answers = {}, [], set()
    cards = []
    for row in samples:
        for key in ("id", "code", "state", "answer", "why"):
            if not row.get(key):
                raise ValueError(
                    "property-sorter %r sample %r has no %r. A sample with no "
                    "state is data a student cannot judge, and one with no "
                    "reason reveals nothing when it opens."
                    % (act_id, row.get("id"), key))
        if row["id"] in by_id:
            raise ValueError(
                "property-sorter %r authors the sample id %r twice."
                % (act_id, row["id"]))
        if row["answer"] not in opt_ids:
            raise ValueError(
                "property-sorter %r sample %r answers %r, which is not one of "
                "the two options %s. The verdict panel is chosen by this "
                "value." % (act_id, row["id"], row["answer"], opt_ids))
        facts = row.get("facts") or []
        if len(facts) < 3:
            raise ValueError(
                "property-sorter %r sample %r carries %d fact(s). The lesson's "
                "rule is that ONE property is a clue and several agreeing "
                "properties are an identification — a sample offering fewer "
                "than three cannot be judged the way the page asks."
                % (act_id, row["id"], len(facts)))
        by_id[row["id"]] = row
        seen_answers.add(row["answer"])
        if row.get("breaks"):
            breakers.append(row["id"])

        # ── the content-truth assertion, per card ────────────────────────
        verdict = dict((o["id"], o["label"]) for o in options)[row["answer"]]
        low = row["why"].lower()
        want = verdict.lower()
        other = [o["label"].lower() for o in options if o["id"] != row["answer"]][0]
        at_want, at_other = low.find(want), low.find(other)
        # "non-metal" contains "metal", so the longer label is looked for first
        # and the shorter one only counts where it is not part of the longer.
        if len(other) > len(want) and at_other >= 0 and at_other <= at_want:
            at_want = low.find(want, at_other + len(other))
        if at_want < 0 or (0 <= at_other < at_want and len(other) > len(want)
                           and at_other != low.find(want)):
            pass  # resolved below by the plain check
        if at_want < 0:
            raise ValueError(
                "property-sorter %r sample %r is answered %r, so its verdict "
                "will read %r — but its reason never names it. The verdict "
                "and the reason are read together."
                % (act_id, row["id"], row["answer"], verdict))

        cards.append(
            '<div class="ks3-prop-item" data-prop-item="%s" data-open="0">'
            '<div class="ks3-prop-head">'
            '<p class="ks3-prop-code">%s</p>'
            '<p class="ks3-prop-state">%s</p></div>'
            '<ul class="ks3-prop-facts">%s</ul>'
            '<div class="ks3-prop-opts">%s</div>'
            '<div class="ks3-prop-reveal" hidden data-prop-reveal>'
            '<p class="ks3-prop-verdict">%s</p>'
            '<p class="ks3-prop-why">%s</p></div></div>'
            % (e(row["id"]), t(row["code"]), t(row["state"]),
               "".join("<li>%s</li>" % rich(f) for f in facts),
               "".join(_c8_seg("ks3-prop-opt", o["label"], data_prop_opt=o["id"])
                       for o in options),
               t(verdict), rich(row["why"])))

    if len(seen_answers) < 2:
        raise ValueError(
            "property-sorter %r answers every sample %r. A bench with one "
            "answer teaches no sorting: pressing the same button six times "
            "scores full marks without reading a fact."
            % (act_id, sorted(seen_answers)[0]))

    claim = a.get("breaks_claim")
    if claim is not None and int(claim) != len(breakers):
        raise ValueError(
            "property-sorter %r says %s of the samples break a rule and "
            "flags %d. That number is in the closing panel, which the student "
            "reads immediately after sorting the cards it counts."
            % (act_id, claim, len(breakers)))
    for name in (a.get("breaks_named") or []):
        if name not in by_id:
            raise ValueError(
                "property-sorter %r closing panel names %r as a rule-breaker "
                "and no sample has that id. The panel names its three by name."
                % (act_id, name))
        if not by_id[name].get("breaks"):
            raise ValueError(
                "property-sorter %r closing panel names %r as a rule-breaker "
                "but the sample is not flagged `breaks`. The panel and the "
                "card disagree about the same sample."
                % (act_id, name))

    close = _close_panel(a, "ks3-prop", "data-prop-close")
    return ('<div class="ks3-prop" data-prop data-total="%d">%s%s</div>'
            % (len(samples), "".join(cards), close))


# ═══ c8-02 · gap-filler ══════════════════════════════════════════════════

def r_gap_filler(a, act_id):
    """⊕ c8-02 `#s-gap` — a neighbour grid with a hole, and what filled it.

    Three parts, one instrument, one rail stop: a 3 × 3 grid of neighbours
    with exactly ONE dashed empty square; three predictions made from the
    squares around it; then Mendeleev's 1871 figures beside the 1886
    measurements in one table.

    ⚖️ **EXACTLY ONE BLANK, AND IT IS ASSERTED.** The lesson is that a gap is
    a PREDICTION rather than a weakness (`PTAB-04`). Two blanks and the
    neighbours no longer determine what belongs; none and the instrument is a
    table. Neither would look broken.

    ⚖️ **THE BLANK MUST HAVE NEIGHBOURS ON BOTH AXES.** A hole in a corner of
    the grid can be read from two sides; Mendeleev read germanium's properties
    off FOUR. The grid is asserted rectangular and the blank asserted to be
    interior on at least one axis, because a prediction made from one
    neighbour is a guess and the page claims it is not.

    ⚖️ **EVERY `predicted` MUST HAVE ITS `actual`.** The table's whole force is
    the pairing — 72 against 72.6, 5.5 against 5.32. A row with one side
    missing is a claim with no check under it, which is precisely the shape of
    the thing the lesson is arguing against.

    HOOKS: `data-gapf` (wrapper) · `data-gapf-cell` · `data-gapf-card` ·
    `data-gapf-opt` · `data-gapf-reveal` · `data-gapf-close`.
    """
    grid = a.get("grid") or []
    cards = a.get("predictions") or []
    table = a.get("table") or []
    cols = int(a.get("cols") or 3)

    if not grid or len(grid) % cols:
        raise ValueError(
            "gap-filler %r holds %d cell(s) in rows of %d, which is not "
            "rectangular. The neighbours are read across AND down, so a "
            "ragged grid has cells with no address."
            % (act_id, len(grid), cols))
    # ⚠️ TWO KINDS OF EMPTY CELL, AND THEY ARE NOT THE SAME THING.
    # `blank` is THE GAP — the dashed square carrying the question mark, the
    # one the lesson is about, and there is exactly one. `empty` is a SPACER:
    # a corner of the 3 x 3 that holds no element because the neighbour grid
    # is a plus-shape cut out of a table, and it renders as nothing at all.
    # Conflating them would either put four question marks on the page or
    # make the gap indistinguishable from a corner.
    blanks = [i for i, c in enumerate(grid) if c.get("blank")]
    if len(blanks) != 1:
        raise ValueError(
            "gap-filler %r marks %d cell(s) blank. Exactly one: the lesson is "
            "that a GAP is a prediction rather than a weakness, and two gaps "
            "leave the neighbours unable to determine what belongs in either. "
            "A corner that holds no element is `empty`, not `blank`."
            % (act_id, len(blanks)))
    for cell in grid:
        if cell.get("blank") and cell.get("empty"):
            raise ValueError(
                "gap-filler %r marks one cell both `blank` and `empty`. The "
                "gap is the subject of the lesson; a spacer is furniture."
                % act_id)
    pos = blanks[0]
    rows_n = len(grid) // cols
    r, c = divmod(pos, cols)
    if not ((0 < r < rows_n - 1) or (0 < c < cols - 1)):
        raise ValueError(
            "gap-filler %r puts its blank at row %d column %d of a %d x %d "
            "grid, where it has neighbours on one side only. The page claims "
            "the missing element's properties were read off the squares "
            "AROUND it, and a corner does not support that claim."
            % (act_id, r, c, rows_n, cols))
    n_real = 0
    for cell in grid:
        if cell.get("blank") or cell.get("empty"):
            continue
        n_real += 1
        for key in ("symbol", "name", "data"):
            if not cell.get(key):
                raise ValueError(
                    "gap-filler %r cell %r has no %r. A neighbour with no "
                    "data is a square a prediction cannot be made from."
                    % (act_id, cell.get("symbol") or cell.get("name"), key))
    if n_real < 2:
        raise ValueError(
            "gap-filler %r surrounds its gap with %d element(s) carrying "
            "data. Mendeleev read germanium off FOUR neighbours, and a "
            "prediction made from one is a guess the page claims is not."
            % (act_id, n_real))

    _no_correct_flags(cards, act_id, "gap-filler")
    for row in cards:
        for key in ("id", "q", "answer"):
            if not row.get(key):
                raise ValueError(
                    "gap-filler %r prediction %r has no %r."
                    % (act_id, row.get("id"), key))
        if len(row.get("options") or []) < 2:
            raise ValueError(
                "gap-filler %r prediction %r offers fewer than two options. "
                "A prediction with one answer is a statement."
                % (act_id, row["id"]))

    for row in table:
        for key in ("prop", "predicted", "actual"):
            if not row.get(key):
                raise ValueError(
                    "gap-filler %r table row %r has no %r. The table's whole "
                    "force is the PAIRING of what was predicted in 1871 with "
                    "what was measured in 1886; a row with one side missing "
                    "is a claim with no check under it."
                    % (act_id, row.get("prop"), key))
    _counter_agrees(a, act_id, len(cards), "prediction(s)")

    cells = "".join(
        ('<div class="ks3-gapf-cell ks3-gapf-blank" data-gapf-cell="blank" '
         'aria-label="%s"><span class="ks3-gapf-qm" aria-hidden="true">?'
         '</span></div>' % e(a.get("blank_label") or "the missing element"))
        if cell.get("blank") else
        ('<div class="ks3-gapf-spacer" aria-hidden="true"></div>')
        if cell.get("empty") else
        ('<div class="ks3-gapf-cell" data-gapf-cell="%s">'
         '<p class="ks3-gapf-sym">%s</p><p class="ks3-gapf-name">%s</p>'
         '<p class="ks3-gapf-data">%s</p></div>'
         % (e(cell["symbol"]), t(cell["symbol"]), t(cell["name"]),
            t(cell["data"])))
        for cell in grid)

    rows_html = "".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>'
        % (t(row["prop"]), t(row["predicted"]), t(row["actual"]))
        for row in table)
    table_html = ("" if not table else
                  '<div class="ks3-gapf-tablewrap">'
                  '<table class="ks3-gapf-table"><caption>%s</caption>'
                  '<thead><tr><th scope="col">Property</th>'
                  '<th scope="col">%s</th><th scope="col">%s</th></tr></thead>'
                  '<tbody>%s</tbody></table></div>'
                  % (t(a.get("table_caption") or ""),
                     t(a.get("predicted_head") or "Predicted"),
                     t(a.get("actual_head") or "Measured"), rows_html))

    close = _close_panel(a, "ks3-gapf", "data-gapf-close")
    return ('<div class="ks3-gapf" data-gapf data-cols="%d" data-total="%d">'
            '<div class="ks3-gapf-grid" style="--gapf-cols:%d">%s</div>'
            '<div class="ks3-gapf-cards">%s</div>%s%s</div>'
            % (cols, len(cards), cols, cells,
               _cards_markup(cards, "ks3-gapf", "data-gapf-card",
                             "data_gapf_opt", "data-gapf-reveal"),
               table_html, close))


# ═══ c8-02, c8-03, c8-04, c8-06 (x2) · predict-cards ═════════════════════

def r_predict_cards(a, act_id):
    """⊕ ONE FAMILY, FIVE PLACEMENTS. See this module's header for the ruling.

    A list of commit-then-reveal cards: a question, a set of buttons carrying
    NO correct flag, and one answer paragraph that opens whichever button was
    pressed. `#s-file`'s cards add a `tag` — the unknown element's address —
    and nothing else differs across the five.

    ⚖️ **NOT ONE OPTION MAY CARRY A CORRECT FLAG, AND IT IS ASSERTED.** These
    are commitments, not questions with a right button. The reveal opens the
    same way either way and the chosen button keeps the ordinary chosen
    treatment. Only the ladder marks (R2). See `_no_correct_flags`.

    ⚖️ **EVERY CARD NEEDS AT LEAST TWO OPTIONS.** A card with one is a
    statement wearing a button, and a student who presses it has committed to
    nothing.

    ⚖️ **AND THE ANSWER MUST NAME ONE OF THE OPTIONS.** Every one of Design's
    fifteen cards opens its answer paragraph with the option it is about
    ("Softer.", "Magnesium.", "A violent reaction, and worse than
    potassium's"). A reveal that names none of the things the student could
    have chosen has stopped answering the question it was asked.

    HOOKS: `data-pcard` (wrapper, `data-total`) · `data-pcard-card` (valued
    with the card id) · `data-pcard-opt` (valued with the option id) ·
    `data-pcard-reveal` · `data-pcard-close`.
    """
    # ⚠️ THE PAYLOAD KEY IS `items`, NOT `cards`, AND THAT IS NOT COSMETIC.
    # `cards` is RESERVED by the shell: `r_activity` draws its own flip-card
    # list from `a["cards"]` in the vocabulary shape, so a predict-cards
    # payload using that name got BOTH renderers — this one, correctly, and
    # the shell's, which emitted one blank flip-card per item with an empty
    # front and an empty definition. Seventeen of them shipped across four
    # pages: real buttons, reachable by keyboard, announcing nothing.
    #
    # Caught by verify_ks3's "every reveal-card grid asks for a commitment"
    # gate, which found a `ks3-cards` list with no prompt in front of it — a
    # gate looking for a missing sentence found a whole phantom instrument.
    cards = a.get("items") or []
    if not cards:
        raise ValueError(
            "predict-cards %r holds no items. (The key is `items`: `cards` is "
            "reserved by the shell and would draw a second, blank flip-card "
            "list beside this one.)" % act_id)
    if a.get("cards"):
        raise ValueError(
            "predict-cards %r authors a `cards` key. That name is reserved by "
            "`r_activity`, which would draw a blank vocabulary flip-card for "
            "every entry. Use `items`." % act_id)
    _no_correct_flags(cards, act_id, "predict-cards")

    seen = set()
    for row in cards:
        for key in ("id", "q", "answer"):
            if not row.get(key):
                raise ValueError(
                    "predict-cards %r card %r has no %r. A card with no "
                    "question asks nothing; one with no answer reveals "
                    "nothing when it opens." % (act_id, row.get("id"), key))
        if row["id"] in seen:
            raise ValueError(
                "predict-cards %r authors the card id %r twice. The id is "
                "what the reveal is keyed on, so the second card would open "
                "the first one's paragraph." % (act_id, row["id"]))
        seen.add(row["id"])
        opts = row.get("options") or []
        if len(opts) < 2:
            raise ValueError(
                "predict-cards %r card %r offers %d option(s). A card with "
                "one is a statement wearing a button and the student has "
                "committed to nothing." % (act_id, row["id"], len(opts)))
        ids = [o.get("id") for o in opts]
        if len(set(ids)) != len(ids):
            raise ValueError(
                "predict-cards %r card %r repeats an option id in %s."
                % (act_id, row["id"], ids))
        # ⚠️ COMPARED ON WORDS, NOT ON PUNCTUATION. The first cut matched the
        # option label as a raw substring and fired on a card whose option
        # reads "An oxide; the solution is alkaline" against an answer opening
        # "An oxide, and the solution is alkaline" — the same commitment, in
        # the same words, with a semicolon swapped for a comma. The property
        # worth asserting is that the reveal NAMES one of the choices; a
        # punctuation-sensitive test measures typography instead, and would
        # push the next author to write stilted answers to satisfy it.
        low = _words(row["answer"])
        if not any(_words(o.get("label", "")) in low for o in opts):
            raise ValueError(
                "predict-cards %r card %r reveals an answer that names none "
                "of its own options %s. The reveal is read directly under the "
                "buttons it is about."
                % (act_id, row["id"],
                   [o.get("label") for o in opts]))
    _counter_agrees(a, act_id, len(cards), "card(s)")

    lead = ('<p class="ks3-pcards-lead">%s</p>' % rich(a["lead"])) \
        if a.get("lead") else ""
    close = _close_panel(a, "ks3-pcards", "data-pcard-close")
    return ('<div class="ks3-pcards" data-pcard data-total="%d">%s%s%s</div>'
            % (len(cards), lead,
               _cards_markup(cards, "ks3-pcards", "data-pcard-card",
                             "data_pcard_opt", "data-pcard-reveal"),
               close))


# ═══ c8-03 · table-reader ════════════════════════════════════════════════

def r_table_reader(a, act_id):
    """⊕ c8-03 `#s-table` — twenty elements, four periods, eight groups.

    ⚠️ **LAYOUT IS SEPARATE FROM ELEMENT DATA, DELIBERATELY, AND IT MUST
    STAY SO.** The payload is `EL` (what each element IS) plus `LAYOUT` (where
    the squares GO) plus `FAMILIES` (what each column is called). NOTES-C8 §4
    asks for this explicitly so the same twenty elements can be redrawn as a
    long-form table without touching a single note, and says C9 and any KS4
    table lesson want the same one. DO NOT FORK IT and do not merge the two.

    ⚠️ **`null` CELLS ARE DRAWN, NOT SKIPPED, AND THE PERIOD-1 ROW STAYS
    MOSTLY EMPTY.** An empty cell renders as a dashed transparent box.
    NOTES-C8 §7: the SHAPE OF THE GAP is part of what the table teaches —
    hydrogen and helium sit at opposite ends of a row with six holes between
    them, and collapsing that row to two squares would teach that they are
    neighbours. Do not tidy it.

    ⚖️ **EVERY KEY IN LAYOUT MUST EXIST IN EL, AND EVERY ELEMENT IN EL MUST BE
    PLACED.** A key with no element is a square that renders blank where the
    author meant an element; an element with no square is a note no student can
    reach, and neither is visible on the built page.

    ⚖️ **AND EVERY ELEMENT'S OWN `group` MUST MATCH THE COLUMN IT IS PLACED
    IN.** The instrument's entire demand is "read an address off the table",
    and the address is printed from the element's own `group` and `period`
    while the POSITION comes from LAYOUT. If those two disagree, the readout
    tells the student a different address from the one they just counted to,
    and the lesson marks them wrong for being right.

    HOOKS: `data-tread` (wrapper) · `data-tread-cell` (valued with the element
    key) · `data-tread-out` · `data-tread-close`.
    """
    el = a.get("elements") or {}
    layout = a.get("layout") or []
    families = a.get("families") or {}
    if not el or not layout:
        raise ValueError(
            "table-reader %r needs both `elements` and `layout`. They are "
            "separate on purpose — see this renderer's docstring." % act_id)

    # ⚠️ THE LAST COLUMN IS GROUP 0, NOT GROUP 8, AND THAT IS WHY THE CHECK
    # GOES THROUGH `group_heads` RATHER THAN THROUGH THE COLUMN INDEX.
    # The table's columns are headed 1 2 3 4 5 6 7 0 — the noble gases close
    # the row rather than continuing the count. Comparing an element's `group`
    # against its 1-based position would fail every noble gas and, worse,
    # would have been "fixed" by renumbering group 0 to group 8, which is the
    # one thing on this page a student must not be taught.
    heads_list = list(a.get("group_heads") or [])
    if not heads_list:
        raise ValueError(
            "table-reader %r declares no `group_heads`. The column headings "
            "ARE the group numbers and the address readout is checked "
            "against them." % act_id)
    widths = {len(r.get("cells") or []) for r in layout}
    if widths != {len(heads_list)}:
        raise ValueError(
            "table-reader %r heads %d column(s) and holds rows of width %s. "
            "Every row spans the whole table — a short row would silently "
            "shift every element in it into the wrong group."
            % (act_id, len(heads_list), sorted(widths)))

    placed, seen_cols = [], {}
    for row in layout:
        cells = row.get("cells")
        if cells is None:
            raise ValueError(
                "table-reader %r row %r has no `cells`."
                % (act_id, row.get("label")))
        for col, key in enumerate(cells, 1):
            if key is None:
                continue
            if key not in el:
                raise ValueError(
                    "table-reader %r places %r in row %r, and `elements` has "
                    "no such key. That square would render blank where an "
                    "element was meant."
                    % (act_id, key, row.get("label")))
            placed.append(key)
            seen_cols[key] = col

    missing = sorted(set(el) - set(placed))
    if missing:
        raise ValueError(
            "table-reader %r declares %s in `elements` and places none of "
            "them. An element with no square carries a note no student can "
            "reach." % (act_id, missing))
    dupes = sorted(k for k in set(placed) if placed.count(k) > 1)
    if dupes:
        raise ValueError(
            "table-reader %r places %s more than once. One element, one "
            "square." % (act_id, dupes))

    for key, col in sorted(seen_cols.items()):
        rec = el[key]
        for field in ("sym", "name", "num", "group", "period", "kind"):
            if rec.get(field) in (None, ""):
                raise ValueError(
                    "table-reader %r element %r has no %r. The address "
                    "readout prints every one of these."
                    % (act_id, key, field))
        want_group = heads_list[col - 1]
        if str(rec["group"]) != str(want_group):
            raise ValueError(
                "table-reader %r places %r under the column headed %r and the "
                "element's own `group` says %s. The student COUNTS to the "
                "column and the readout PRINTS the group, so a disagreement "
                "tells them a different address from the one they just "
                "counted to." % (act_id, key, want_group, rec["group"]))
    for row in layout:
        for key in (row.get("cells") or []):
            if key is None:
                continue
            want = row.get("period")
            if want is not None and int(el[key]["period"]) != int(want):
                raise ValueError(
                    "table-reader %r puts %r in the row labelled period %s "
                    "and the element's own `period` says %s."
                    % (act_id, key, want, el[key]["period"]))
    # ── ⊕ §5A · A PROSE CLAIM ABOUT DISTANCE IS CHECKED AGAINST THE TABLE
    #
    # THIS ASSERTION EXISTS BECAUSE THE DEFECT WAS REAL AND WAS SHIPPED IN THE
    # DELIVERY. Design's c8-03 says sodium and chlorine are "seven squares
    # apart" at `#s-think` and "three squares apart" on the apply rung. They
    # are SIX columns apart — Na heads period 3 and Cl is the seventh square
    # of it — so the two sentences disagree with each other AND both disagree
    # with the table drawn directly above them, which a student can count.
    #
    # The build law is that where prose and instrument disagree the INSTRUMENT
    # is the measurement and the prose changes, so both sentences were
    # corrected. This turns the corrected number into something the build
    # checks rather than something the next author has to remember: a
    # `separation_claims` entry names two elements and the gap the prose
    # claims between them, and it is measured off LAYOUT.
    for claim in (a.get("separation_claims") or []):
        one, two, gap = claim["a"], claim["b"], int(claim["columns"])
        for k in (one, two):
            if k not in seen_cols:
                raise ValueError(
                    "table-reader %r claims a separation involving %r, which "
                    "is not placed on this table." % (act_id, k))
        if int(el[one]["period"]) != int(el[two]["period"]):
            raise ValueError(
                "table-reader %r claims %r and %r are %d column(s) apart, and "
                "they are in different periods. A distance along a row is "
                "only meaningful inside one row."
                % (act_id, one, two, gap))
        real = abs(seen_cols[one] - seen_cols[two])
        if real != gap:
            raise ValueError(
                "table-reader %r: the prose claims %r and %r are %d square(s) "
                "apart and the table places them %d apart. The table is drawn "
                "directly above the sentence and a student can count it."
                % (act_id, one, two, gap, real))

    for gnum in sorted(families):
        if not families[gnum]:
            raise ValueError(
                "table-reader %r declares an empty family line for group %r. "
                "The family line is what the square says it BELONGS to."
                % (act_id, gnum))

    heads = "".join('<th scope="col" class="ks3-tread-gh">%s</th>' % t(str(g))
                    for g in (a.get("group_heads") or []))
    body = []
    for row in layout:
        squares = []
        for key in (row.get("cells") or []):
            if key is None:
                squares.append('<td class="ks3-tread-empty" aria-hidden="true">'
                               '</td>')
                continue
            rec = el[key]
            squares.append(
                '<td class="ks3-tread-td"><button type="button" '
                'class="ks3-tread-cell" data-tread-cell="%s" '
                'aria-pressed="false" data-kind="%s">'
                '<span class="ks3-tread-num">%s</span>'
                '<span class="ks3-tread-sym">%s</span>'
                '<span class="ks3-tread-nm">%s</span></button></td>'
                % (e(key), e(rec["kind"]), t(str(rec["num"])), t(rec["sym"]),
                   t(rec["name"])))
        body.append('<tr><th scope="row" class="ks3-tread-ph">%s</th>%s</tr>'
                    % (t(row.get("label") or ""), "".join(squares)))

    # emit-both-show-one: every square's readout is in the document already.
    outs = "".join(
        '<div class="ks3-tread-one" data-tread-out="%s" hidden>'
        '<p class="ks3-tread-addr">%s</p><p class="ks3-tread-fam">%s</p>'
        '<p class="ks3-tread-note">%s</p></div>'
        % (e(key), t(a.get("address_fmt", "Group %(group)s, period %(period)s")
                     % el[key]),
           t(families.get(el[key]["group"], "")
             or families.get(str(el[key]["group"]), "")),
           rich(el[key].get("note") or ""))
        for key in sorted(seen_cols))

    close = _close_panel(a, "ks3-tread", "data-tread-close")
    return ('<div class="ks3-tread" data-tread data-total="%d">'
            '<div class="ks3-tread-scroll">'
            '<table class="ks3-tread-table"><thead><tr>'
            '<th scope="col" class="ks3-tread-corner"><span class="ks3-sr">'
            'Period</span></th>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<div class="ks3-tread-readout" data-tread-readout>'
            '<p class="ks3-tread-rest">%s</p>%s</div>%s</div>'
            % (len(seen_cols), heads, "".join(body),
               t(a.get("resting") or "Tap any element."), outs, close))


# ═══ c8-04 · water-trough ════════════════════════════════════════════════

def r_water_trough(a, act_id):
    """⊕ c8-04 `#s-trough` — three metals, one trough, one at a time.

    ⚖️ **THE TREND IS DATA AND IT IS ASSERTED MONOTONIC.** Lithium, sodium,
    potassium are authored with a `rank`, and the whole point of the lesson —
    and of c8-05, which exists to break it — is that vigour rises with rank
    going down the group. The order is read off `rank`, never off the array,
    so re-sorting the payload for layout cannot re-teach the chemistry (the C5
    ruling, carried).

    ⚠️ **NO SENTENCE HERE MAY IMPLY A DENSITY TREND, AND THAT IS ASSERTED
    RATHER THAN LEFT TO CARE.** Lithium 0.53, sodium 0.97, potassium 0.86 is
    NOT monotonic, so "denser as you go down" is false and "less dense as you
    go down" is equally false. The lesson says only that they all float.
    Design's NOTES-C8 §5 flag 11 asked for the omission to be confirmed; the
    commander's ruling (MRB-281, R4 flag 11) UPGRADED it from an omission to a
    positive instruction, so it is a check rather than a habit: any
    observation or headline pairing a density word with a direction word fails
    the build.

    HOOKS: `data-trough` (wrapper, `data-total`) · `data-trough-metal` (valued
    with the metal id) · `data-trough-opt` · `data-trough-run` ·
    `data-trough-close`.
    """
    metals = a.get("metals") or []
    if len(metals) < 3:
        raise ValueError(
            "water-trough %r runs %d metal(s). A trend needs three points; "
            "two is a pair and one is an anecdote." % (act_id, len(metals)))
    _counter_agrees(a, act_id, len(metals), "metal(s)")

    ranks = []
    for row in metals:
        for key in ("id", "name", "data", "headline"):
            if not row.get(key):
                raise ValueError(
                    "water-trough %r metal %r has no %r."
                    % (act_id, row.get("id"), key))
        if row.get("rank") is None:
            raise ValueError(
                "water-trough %r metal %r has no `rank`. ORDER IS DATA: the "
                "trend is read off rank and never off the position of the "
                "metal in the array, so a payload re-sorted for layout cannot "
                "silently re-teach the group." % (act_id, row["id"]))
        ranks.append(int(row["rank"]))
        if not (row.get("obs") or []):
            raise ValueError(
                "water-trough %r metal %r records no observations. The run IS "
                "the observations." % (act_id, row["id"]))
    if sorted(ranks) != list(range(len(ranks))):
        raise ValueError(
            "water-trough %r ranks its metals %s. Ranks are 0..n-1 with no "
            "gap and no tie: the trend the next lesson breaks is stated as an "
            "ORDER, and a tie means two metals the page cannot put in order."
            % (act_id, sorted(ranks)))

    # ── the density assertion (R4 flag 11) ───────────────────────────────
    #
    # ⚠️ MATCHED ON WORD BOUNDARIES, NEVER AS SUBSTRINGS. The first cut of
    # this check used `"light" in sentence` and fired on potassium's own
    # observation — "hot enough to set its own hydrogen **alight**" — which is
    # a sentence about a flame with no density claim anywhere in it. A gate
    # that cries wolf on true content gets weakened by the next author, which
    # is how a real check stops being one. `\b` costs nothing and makes the
    # gate mean what it says.
    _DENSITY = r"\b(dense|density|denser|heavier|lighter|heavy|light)\b"
    _DIRECTION = (r"\b(down the group|going down|further down|down the "
                  r"column|up the group|going up|each one below|as you go "
                  r"down|further up)\b")
    # Checked SENTENCE BY SENTENCE, not blob by blob. "They all float" and
    # "reactivity increases down the group" are both true and may sit in one
    # paragraph; it is only their appearance in ONE SENTENCE that asserts a
    # density trend. A blob-level check would forbid the honest paragraph.
    blobs = [a.get("lead") or ""] + list(a.get("close") or [])
    for row in metals:
        blobs += [row.get("headline") or ""] + list(row.get("obs") or [])
    for blob in blobs:
        for sentence in re.split(r"(?<=[.!?;])\s+", blob):
            low = sentence.lower()
            if re.search(_DENSITY, low) and re.search(_DIRECTION, low):
                raise ValueError(
                    "water-trough %r: %r pairs a density word with a "
                    "direction in one sentence. Li 0.53, Na 0.97, K 0.86 is "
                    "NOT monotonic, so there is no density trend to state in "
                    "either direction — the lesson says only that they all "
                    "float (R4 flag 11)." % (act_id, sentence[:70]))

    order = sorted(metals, key=lambda m: int(m["rank"]))
    picker = "".join(
        _c8_seg("ks3-trough-pick", m["name"], data_trough_metal=m["id"])
        for m in order)

    runs = []
    for m in order:
        eq = ""
        if m.get("eq_right"):
            eq = ('<p class="ks3-trough-eq">%s</p>'
                  % t("%s + water → %s"
                      % (m["name"], m["eq_right"])))
        runs.append(
            '<div class="ks3-trough-run" data-trough-run="%s" hidden>'
            '<p class="ks3-trough-headline">%s</p>'
            '<p class="ks3-trough-data">%s</p>'
            '<ul class="ks3-trough-obs">%s</ul>%s</div>'
            % (e(m["id"]), t(m["headline"]), t(m["data"]),
               "".join("<li>%s</li>" % rich(o) for o in m["obs"]), eq))

    predict = ""
    if a.get("predict_prompt"):
        predict = ('<div class="ks3-trough-predict">'
                   '<p class="ks3-trough-prompt">%s</p>%s</div>'
                   % (rich(a["predict_prompt"]),
                      "".join(_c8_seg("ks3-trough-opt", o["label"],
                                      data_trough_opt=o["id"])
                              for o in (a.get("predict_options") or []))))
        _no_correct_flags([{"options": a.get("predict_options") or []}],
                          act_id, "water-trough")

    close = _close_panel(a, "ks3-trough", "data-trough-close")
    return ('<div class="ks3-trough" data-trough data-total="%d">'
            '<div class="ks3-trough-picker">%s</div>%s'
            '<div class="ks3-trough-stage">'
            '<p class="ks3-trough-rest">%s</p>%s</div>%s</div>'
            % (len(metals), picker, predict,
               t(a.get("resting") or "Choose a metal."), "".join(runs), close))


# ═══ c8-05 · halogen-grid ════════════════════════════════════════════════

def _hgrid_reacts(hal, salt):
    """THE ONLY PLACE THE VERDICT IS DECIDED, AND IT IS DECIDED FROM `rank`.

    A halogen displaces a halide when it is MORE reactive than the halogen in
    the salt, and in group 7 more reactive means HIGHER UP, which is the lower
    rank. Same element on both sides is not a displacement.

    Position in the payload array is never consulted. That is C5's ruling and
    the reason the grid can be re-sorted for layout without re-teaching the
    chemistry.
    """
    if hal["id"] == salt["id"]:
        return False
    return int(hal["rank"]) < int(salt["rank"])


def r_halogen_grid(a, act_id):
    """⊕ c8-05 `#s-grid` — three halogens against three halide solutions.

    ⚠️ `halogen-grid`, NOT `reactivity-grid`. See this module's header.

    ⚖️ **EVERY CELL IS AUTHORED, NONE IS COMPOSED.** Design's page builds each
    cell's title and setup sentence at run time out of the halogen's name and
    the salt's ending. Reproducing that would put an element's name into a
    sentence by string surgery, make three "no reaction" cells literally the
    same paragraph, and make `<strong>` impossible. All nine are authored, on
    the C6 `acid-metal-grid` precedent.

    ⚖️ **AND EVERY AUTHORED CELL IS CHECKED AGAINST `_hgrid_reacts`.** This is
    the assertion the unit turns on. `PTAB-08` — "reactivity always increases
    going down a group" — exists ONLY because c8-04 builds that trend and this
    grid breaks it, so a single cell authored the wrong way round does not
    merely misinform: it removes the surprise the lesson is built to produce,
    and it does so on a page that still renders perfectly.

    ⚖️ **THE GRID MUST BE SQUARE AND COMPLETE.** Every halogen appears as a
    row and as a column, nine cells, no hole and no surplus. A missing cell is
    a comparison the student cannot make, and the diagonal — an element with
    its own salt — is what shows them that "nothing happened" is a real result
    rather than a broken one.

    ⚖️ **AND BOTH OUTCOMES MUST OCCUR.** A grid where everything reacts, or
    nothing does, has no pattern in it to reverse.

    HOOKS: `data-hgrid` (wrapper) · `data-hgrid-cell` (valued `hal:salt`) ·
    `data-hgrid-opt` · `data-hgrid-out` · `data-hgrid-close`.
    """
    hals = a.get("halogens") or []
    cells = a.get("cells") or {}
    if len(hals) < 3:
        raise ValueError(
            "halogen-grid %r declares %d halogen(s). The reversal is not "
            "visible in two." % (act_id, len(hals)))

    ranks = sorted(int(h["rank"]) for h in hals)
    if ranks != list(range(len(hals))):
        raise ValueError(
            "halogen-grid %r ranks its halogens %s. Ranks are 0..n-1, no gap "
            "and no tie — the verdict in every cell is decided by comparing "
            "them, so a tie is a cell with no answer." % (act_id, ranks))
    for h in hals:
        for key in ("id", "name", "salt", "colour"):
            if not h.get(key):
                raise ValueError(
                    "halogen-grid %r halogen %r has no %r."
                    % (act_id, h.get("id"), key))

    by_id = dict((h["id"], h) for h in hals)
    if len(by_id) != len(hals):
        raise ValueError("halogen-grid %r repeats a halogen id." % act_id)

    want_keys = set()
    n_react = n_none = 0
    for hal in hals:
        for salt in hals:
            key = "%s:%s" % (hal["id"], salt["id"])
            want_keys.add(key)
            if key not in cells:
                raise ValueError(
                    "halogen-grid %r has no cell for %r. The grid is %d x %d "
                    "and every pair is a comparison the student is invited to "
                    "make — including an element with its own salt, which is "
                    "what shows them that 'nothing happened' is a result."
                    % (act_id, key, len(hals), len(hals)))
            cell = cells[key]
            truth = _hgrid_reacts(hal, salt)
            if bool(cell.get("reacts")) != truth:
                raise ValueError(
                    "halogen-grid %r cell %r is authored reacts=%r and the "
                    "ranks say %r (%s rank %s against %s rank %s). "
                    "`PTAB-08` exists ONLY because c8-04 builds a trend and "
                    "this grid breaks it — a cell the wrong way round removes "
                    "the surprise the lesson is built to produce, on a page "
                    "that still renders."
                    % (act_id, key, bool(cell.get("reacts")), truth,
                       hal["name"], hal["rank"], salt["name"], salt["rank"]))
            for field in ("title", "setup", "obs"):
                if not cell.get(field):
                    raise ValueError(
                        "halogen-grid %r cell %r has no %r. Every cell is "
                        "AUTHORED — none is composed from the element names "
                        "at run time (the C6 precedent)."
                        % (act_id, key, field))
            if truth:
                n_react += 1
                if not cell.get("eq"):
                    raise ValueError(
                        "halogen-grid %r cell %r reacts and carries no word "
                        "equation. A displacement that happens has products."
                        % (act_id, key))
            else:
                n_none += 1
                if cell.get("eq"):
                    raise ValueError(
                        "halogen-grid %r cell %r does NOT react and carries a "
                        "word equation %r. Writing products for a reaction "
                        "that never happens is the error the grid exists to "
                        "correct." % (act_id, key, cell["eq"]))
    surplus = sorted(set(cells) - want_keys)
    if surplus:
        raise ValueError(
            "halogen-grid %r authors %s, which is not a halogen against a "
            "halide on this grid." % (act_id, surplus))
    if not n_react or not n_none:
        raise ValueError(
            "halogen-grid %r resolves to %d reacting and %d not. A grid where "
            "everything reacts, or nothing does, has no pattern in it to "
            "reverse." % (act_id, n_react, n_none))

    order = sorted(hals, key=lambda h: int(h["rank"]))
    heads = "".join('<th scope="col">%s</th>'
                    % t(a.get("col_fmt", "potassium %(salt)s") % h)
                    for h in order)
    body = []
    for hal in order:
        tds = []
        for salt in order:
            key = "%s:%s" % (hal["id"], salt["id"])
            tds.append(
                '<td class="ks3-hgrid-td"><button type="button" '
                'class="ks3-hgrid-cell" data-hgrid-cell="%s" '
                'aria-pressed="false"><span class="ks3-hgrid-mark">%s</span>'
                '</button></td>'
                % (e(key), t(a.get("resting_mark") or "?")))
        body.append('<tr><th scope="row">%s</th>%s</tr>'
                    % (t(a.get("row_fmt", "%(name)s water") % hal),
                       "".join(tds)))

    outs = []
    for hal in order:
        for salt in order:
            key = "%s:%s" % (hal["id"], salt["id"])
            cell = cells[key]
            eq = ('<p class="ks3-hgrid-eq">%s</p>' % t(cell["eq"])) \
                if cell.get("eq") else ""
            outs.append(
                '<div class="ks3-hgrid-one" data-hgrid-out="%s" hidden>'
                '<p class="ks3-hgrid-title">%s</p>'
                '<p class="ks3-hgrid-setup">%s</p>'
                '<p class="ks3-hgrid-verdict">%s</p>'
                '<p class="ks3-hgrid-obs">%s</p>%s</div>'
                % (e(key), t(cell["title"]), rich(cell["setup"]),
                   t(a.get("verdict_yes" if cell.get("reacts")
                           else "verdict_no") or ""),
                   rich(cell["obs"]), eq))

    predict = ""
    if a.get("predict_options"):
        _no_correct_flags([{"options": a["predict_options"]}], act_id,
                          "halogen-grid")
        predict = ('<div class="ks3-hgrid-predict">'
                   '<p class="ks3-hgrid-prompt">%s</p>%s</div>'
                   % (rich(a.get("predict_prompt") or ""),
                      "".join(_c8_seg("ks3-hgrid-opt", o["label"],
                                      data_hgrid_opt=o["id"])
                              for o in a["predict_options"])))

    close = _close_panel(a, "ks3-hgrid", "data-hgrid-close")
    return ('<div class="ks3-hgrid" data-hgrid data-total="%d">'
            '<div class="ks3-hgrid-scroll"><table class="ks3-hgrid-table">'
            '<thead><tr><th scope="col" class="ks3-hgrid-corner">'
            '<span class="ks3-sr">Added to</span></th>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>%s'
            '<div class="ks3-hgrid-readout" data-hgrid-readout>'
            '<p class="ks3-hgrid-rest">%s</p>%s</div>%s</div>'
            % (len(hals) * len(hals), heads, "".join(body), predict,
               t(a.get("resting") or "Tap a cell."), "".join(outs), close))


# ═══ c8-06 · shell-strip ═════════════════════════════════════════════════

def r_shell_strip(a, act_id):
    """⊕ c8-06 `#s-shells` — eight dots a row, `n` of them filled.

    The only place in the chemistry sequence where electron count is shown
    visually. ⚠️ **IT STOPS SHORT OF SHELLS-WITHIN-SHELLS DELIBERATELY AND IS
    TO BE LEFT THERE** (NOTES-C8 §4). One row is one OUTER shell. Adding inner
    shells would make the drawing right and the lesson unreadable, and group
    number = outer electrons is the whole of what c8-03 and c8-06 claim.

    ⚖️ **`n` MUST FIT THE ROW, AND THE DRAWN GEOMETRY MUST EXPRESS THE NUMBER
    IT CLAIMS.** The strip draws `slots` dots and fills `n`. A row claiming
    nine electrons in eight dots would silently draw eight and the page would
    then say "the outer shell is full" beside a picture that is merely full to
    the edge of the drawing.

    ⚖️ **HELIUM IS THE AUTHORED EXCEPTION AND MUST DECLARE ITSELF.** Its outer
    shell is full at TWO, not eight. A row whose `full` flag disagrees with
    `n == slots` must carry a `detail` saying why, or the page shows two dots
    filled out of eight beside the word "full" and the student is right to
    disbelieve it.

    HOOKS: `data-shel` (wrapper) · `data-shel-row` (valued with the row id) ·
    `data-shel-detail` · `data-shel-close`.
    """
    rows = a.get("rows") or []
    slots = int(a.get("slots") or 8)
    if len(rows) < 2:
        raise ValueError(
            "shell-strip %r draws %d row(s). The strip exists to be COMPARED "
            "down a column." % (act_id, len(rows)))
    _counter_agrees(a, act_id, len(rows), "row(s)")

    out = []
    for row in rows:
        for key in ("id", "title", "summary"):
            if not row.get(key):
                raise ValueError(
                    "shell-strip %r row %r has no %r."
                    % (act_id, row.get("id"), key))
        n = row.get("n")
        if n is None:
            raise ValueError(
                "shell-strip %r row %r has no `n`. The number of filled dots "
                "is the whole content of the row." % (act_id, row["id"]))
        n = int(n)
        if not (0 <= n <= slots):
            raise ValueError(
                "shell-strip %r row %r claims %d electron(s) in a strip of %d "
                "dots. The drawing would show %d and the text would say %d, "
                "and the drawn geometry must express the number it claims."
                % (act_id, row["id"], n, slots, min(n, slots), n))
        if row.get("full") and n != slots and not row.get("detail"):
            raise ValueError(
                "shell-strip %r row %r is flagged `full` with %d of %d dots "
                "filled and carries no `detail`. Helium is the authored "
                "exception and has to say so on the row — otherwise the page "
                "shows two dots out of eight beside the word 'full'."
                % (act_id, row["id"], n, slots))
        dots = "".join(
            '<span class="ks3-shel-dot" data-on="%d" aria-hidden="true">'
            '</span>' % (1 if i < n else 0) for i in range(slots))
        detail = (('<p class="ks3-shel-detail" hidden data-shel-detail>%s</p>'
                   % rich(row["detail"])) if row.get("detail") else "")
        # ⚠️ THE ROW IS A REAL <button>, NOT A DIV WITH A HANDLER. The strip
        # is tappable — "tap a row to see what it forces the element to do" —
        # so the control has to be reachable by keyboard and announce itself
        # as a control. `aria-expanded` carries the state as a WORD rather
        # than as the presence of a class (R2).
        out.append(
            '<div class="ks3-shel-row" data-shel-row="%s" data-open="0">'
            '<button type="button" class="ks3-shel-toggle" '
            'data-shel-toggle aria-expanded="false">'
            '<span class="ks3-shel-head"><span class="ks3-shel-title">%s'
            '</span><span class="ks3-shel-tag">%s</span></span>'
            '<span class="ks3-shel-dots" role="img" aria-label="%s">%s</span>'
            '<span class="ks3-shel-summary">%s</span></button>%s</div>'
            % (e(row["id"]), t(row["title"]), t(row.get("tag") or ""),
               e("%d of %d outer-shell places filled" % (n, slots)), dots,
               t(row["summary"]), detail))

    close = _close_panel(a, "ks3-shel", "data-shel-close")
    return ('<div class="ks3-shel" data-shel data-slots="%d" data-total="%d">'
            '%s%s</div>' % (slots, len(rows), "".join(out), close))


# ═══ c8-07 · oxide-bench ═════════════════════════════════════════════════
#
# THE FIFTEEN VALUES ARE SCIENTIFIC DATA. See the note in this module's
# header. Index IS the pH.
PH_COLOURS = [
    "#C1272D", "#D2382B", "#E04A22", "#EA6A1E", "#EE8C1B",
    "#EFB120", "#D7CA2A", "#4FA352", "#3E9C86", "#2F8DA8",
    "#2A6FA8", "#2E4E96", "#453C8E", "#553191", "#5E2483",
]

# What is left on the bottom of the beaker, and how much of it. Design's own
# `{ thin: 11, heap: 28 }` and `residue === 'heap' ? '#1A1714' : '#EFE7D6'`.
#
# ⚠️ THESE TWO HEX VALUES ARE OBSERVATION, NOT PALETTE, exactly as the ramp
# above is. Copper oxide is a black powder and magnesium oxide is a white one;
# routing either through `--ks3-accent` would make the drawing wrong in order
# to make the stylesheet tidy. Neither is ever the only channel — every panel
# says in a sentence what is on the bottom and what colour it is.
RESIDUE_DEPTH = {"thin": 11, "heap": 28}
RESIDUE_DARK = "#1A1714"
RESIDUE_PALE = "#EFE7D6"

OXIDE_KINDS = ("metal", "non-metal")


def _ph_word(ph):
    """The universal-indicator colour at a whole-number pH, in WORDS.

    Design's `uiWord()`, ported unchanged. It exists so that the beaker's
    reading is announced rather than merely painted: the ramp above is the only
    non-token colour in the unit and it is allowed to be one precisely because
    nothing on this page is identified by hue alone.
    """
    if ph <= 4:
        return "red"
    if ph <= 6:
        return "orange"
    if ph == 7:
        return "green"
    if ph <= 9:
        return "blue-green"
    if ph <= 11:
        return "blue"
    return "purple"


def _cap(s):
    return s[:1].upper() + s[1:]


def _oxide_compare(a, b):
    """The side-by-side sentence, BUILT FROM THE TWO READINGS ON THE BENCH.

    ⚖️ §5A — A COMPARATIVE LABEL IS DERIVED, NEVER STORED PER PAIR. Thirty
    ordered pairs are reachable and every one of their sentences comes out of
    here, from `ph`, `kind` and `insoluble` and from nothing else. Storing
    thirty sentences beside the payload would be thirty chances for one of them
    to disagree with the number printed six inches above it, and the one that
    disagreed would look exactly like the twenty-nine that did not.

    Design's own six branches, ported unchanged:

      equal · acidic against alkaline · acidic against neutral ·
      neutral against alkaline · both alkaline · both acidic

    ⚠️ THE EQUAL BRANCH IS NOT AN EDGE CASE ON THIS BENCH, IT IS THE LESSON.
    Copper oxide and water both read 7 and mean completely different things by
    it, so the tail below says which of the two readings is not a verdict —
    and it says it about whichever chip is the insoluble one, in either order.
    """
    hi, lo = (a, b) if a["ph"] >= b["ph"] else (b, a)
    if a["ph"] == b["ph"]:
        head = ("%s and %s both read pH %d."
                % (_cap(a["name"]), b["name"], a["ph"]))
    elif lo["ph"] < 7 and hi["ph"] > 7:
        head = ("%s read pH %d, which is acidic. %s read pH %d, which is "
                "alkaline."
                % (_cap(lo["name"]), lo["ph"], _cap(hi["name"]), hi["ph"]))
    elif lo["ph"] < 7 and hi["ph"] == 7:
        head = ("%s took the reading down to %d. %s left it at 7."
                % (_cap(lo["name"]), lo["ph"], _cap(hi["name"])))
    elif lo["ph"] == 7 and hi["ph"] > 7:
        head = ("%s took the reading up to %d. %s left it at 7."
                % (_cap(hi["name"]), hi["ph"], _cap(lo["name"])))
    elif lo["ph"] > 7:
        head = ("Both readings are above 7. %s at pH %d is the more alkaline "
                "of the two." % (_cap(hi["name"]), hi["ph"]))
    else:
        head = ("Both readings are below 7. %s at pH %d is the more acidic of "
                "the two." % (_cap(lo["name"]), lo["ph"]))

    kinds = (" Both are %s oxides." % a["kind"]
             if a["kind"] == b["kind"]
             else " One of them is a metal oxide and one is not.")

    tail = ""
    if a.get("insoluble") or b.get("insoluble"):
        which = a if a.get("insoluble") else b
        tail = (" The 7 beside %s is not a verdict on it: almost none of it "
                "dissolved, so the water had nothing to report." % which["name"])
    elif a["ph"] == b["ph"]:
        tail = " Nothing on this test separates them."
    return head + kinds + tail


def _oxide_beaker(a, o, slot):
    """One beaker panel: the glass, the fill, the solid, and the reading.

    ⚠️ Z-ORDER IS FIXED AND IS PART OF THE DRAWING (NOTES-C8 §8): body, then
    the water fill, then the undissolved solid, then the pH numeral OUTSIDE the
    glass. The solid is emitted after the water so it sits on top of it — a
    heap drawn under the fill would be a heap that dissolved, which is the one
    thing the copper-oxide case must not show.

    ⚠️ CONTAINMENT, NOT CLIPPING. Both spans are absolutely positioned and the
    glass carries `position: relative` in the stylesheet, so neither can escape
    and widen the document. The glass is the only positioned box this
    instrument draws.
    """
    ph = o["ph"] if o else 7
    depth = RESIDUE_DEPTH.get((o or {}).get("residue"), 0) if o else 0
    water = ('<span class="ks3-oxb-water" aria-hidden="true" '
             'style="background:%s"></span>' % e(PH_COLOURS[ph]))
    solid = ""
    if depth:
        solid = ('<span class="ks3-oxb-solid" aria-hidden="true" '
                 'data-solid="%s" style="height:%dpx;background:%s"></span>'
                 % (e(o["residue"]), depth,
                    e(RESIDUE_DARK if o["residue"] == "heap"
                      else RESIDUE_PALE)))
    # DERIVED, never authored (§5A). The label is a description of what is
    # actually drawn — the fill's colour and whether a solid is on the bottom —
    # so an authored one would be a second statement of the same two facts and
    # the copy that went stale would be the one nobody can see.
    alt = ("A beaker of water with the indicator %s, and %s on the bottom."
           % (_ph_word(ph), "undissolved solid" if depth else "nothing"))
    note = (('<p class="ks3-oxb-note">%s</p>' % rich(o["note"]))
            if o and o.get("note") else "")
    return (
        '<div class="ks3-oxb-panel" data-oxb-panel="%d:%s"%s>'
        '<div class="ks3-oxb-head">'
        '<p class="ks3-oxb-slot">%s</p><p class="ks3-oxb-kind">%s</p></div>'
        '<p class="ks3-oxb-title">%s</p>'
        '<div class="ks3-oxb-row">'
        '<div class="ks3-oxb-glass" role="img" aria-label="%s">%s%s</div>'
        '<div class="ks3-oxb-readout">'
        '<p class="ks3-oxb-phlabel">%s</p>'
        '<p class="ks3-oxb-ph">%d</p>'
        '<p class="ks3-oxb-ui">%s %s.</p></div></div>'
        '<p class="ks3-oxb-residue">%s</p>%s</div>'
        % (slot, e(o["id"]) if o else "empty",
           "" if o is None else " hidden",
           t((a.get("slot_fmt") or "Beaker %d") % (slot + 1)),
           t("%s oxide" % o["kind"] if o else (a.get("empty_kind")
                                              or "water only")),
           t(o["title"] if o else (a.get("empty_title")
                                   or "Water, nothing added")),
           e(alt), water, solid,
           t(a.get("ph_label") or "pH of the solution"), ph,
           t(a.get("indicator_label") or "Universal indicator:"),
           t(_ph_word(ph)),
           t(o["residue_line"] if o else (a.get("empty_line") or "")),
           note))


def r_oxide_bench(a, act_id):
    """⊕ c8-07 `#s-bench` — six oxides, two beakers of the same water.

    THIRTY-SEVEN REACHABLE STATES, AND EVERY ONE OF THEM IS IN THE DOCUMENT AT
    REST. One empty, six with a single oxide in beaker 1, and thirty ordered
    pairs — ordered because the sentence names the LEFT reading first, so
    calcium-then-carbon and carbon-then-calcium are two different sentences.
    `[null, y]` is unreachable: taking a chip out slides the other one left,
    which is Design's own `pick()` and is why the count is 37 and not 49.

    Fourteen beaker panels and thirty comparison sentences are emitted here and
    hidden — emit-both-show-one — so every pH, every indicator word and every
    comparative is BYTES a crawler and a no-JS reader get, not a string
    JavaScript assembles.

    ⚖️ **BOTH DISCRIMINATING CASES ARE ASSERTED ON THE INSTRUMENT, NOT TRUSTED
    TO THE PROSE.** The famous version of this lesson's rule — metal oxide
    means alkaline water, non-metal oxide means acid — is wrong twice, and
    NOTES-C8 §8 puts both counter-cases on the bench rather than in a footnote:

      1. AN INSOLUBLE METAL OXIDE THAT READS 7. Copper oxide is a base and the
         water does not move, because almost none of it dissolves. The bench
         has to SHOW that: an oxide flagged `insoluble` must read pH 7 AND draw
         a residue with real depth, so the student sees undissolved solid
         sitting under an unmoved number. An insoluble oxide that dissolved
         away in the drawing would make the reading look like a refutation of
         the rule, which is the exact misbelief `PTAB-11` exists to confront.
      2. A NEUTRAL NON-METAL OXIDE. Water is hydrogen oxide and it reads 7.
         Without it on the tray, "non-metal oxides are acidic" ships as a rule
         with no exception a student can reach.

    ⚖️ **AND THE RULE ITSELF MUST BE ON THE BENCH TOO** — at least one metal
    oxide above 7 and at least one non-metal oxide below it. Two exceptions and
    no pattern is not a contrast lesson, it is a page of special cases.

    ⚖️ **THE CLOSING PANEL'S COUNTS ARE DERIVED FROM THE READINGS.** It says
    "Two went above 7. Two went below. Two did not move at all." and then names
    all six by name. Both halves are checked: the three counts against
    `pattern_claim`, and every name in the paragraph against the tray. A pH
    edited later fails the build rather than shipping a panel that contradicts
    the six numbers directly above it.

    ⚖️ **EVERY NAMED QUANTITY IS READABLE AS A NUMBER** (§5A). `ph` is a whole
    number 0..14, it is printed as a numeral, and the indicator colour is said
    in words beside it.

    HOOKS: `data-oxb` (wrapper, `data-total`) · `data-oxb-chip` (valued with
    the oxide id) · `data-oxb-name` · `data-oxb-panel` (valued `slot:id`, or
    `slot:empty`) · `data-oxb-compare` · `data-oxb-cmp` (valued `left:right`) ·
    `data-oxb-clear` · `data-oxb-untested` / `data-oxb-untested-list` /
    `data-oxb-alltested` · `data-oxb-close`.
    """
    oxides = a.get("oxides") or []
    if len(oxides) < 4:
        raise ValueError(
            "oxide-bench %r puts %d oxide(s) on the tray. The lesson's claim is "
            "that the SIDE OF THE TABLE decides the direction, and that is not "
            "visible without several of each kind." % (act_id, len(oxides)))
    if a.get("pairs") or a.get("comparisons"):
        raise ValueError(
            "oxide-bench %r authors a stored comparison. Every side-by-side "
            "sentence is DERIVED at render from the two readings (§5A) — a "
            "stored one is a sentence free to disagree with the numbers "
            "printed above it." % act_id)
    if a.get("cards"):
        raise ValueError(
            "oxide-bench %r authors a `cards` key. That name is reserved by "
            "`r_activity`, which would draw a blank vocabulary flip-card for "
            "every entry beside this bench. Use `oxides`." % act_id)
    _counter_agrees(a, act_id, len(oxides), "oxide(s)")

    seen = set()
    for o in oxides:
        for key in ("id", "name", "formula", "kind", "title", "residue",
                    "residue_line", "note"):
            if not o.get(key):
                raise ValueError(
                    "oxide-bench %r oxide %r has no %r. A chip with no name is "
                    "unpickable, one with no reading is unreadable, and one "
                    "with no note opens on a gap."
                    % (act_id, o.get("id"), key))
        if o["id"] in seen:
            raise ValueError(
                "oxide-bench %r authors the oxide id %r twice. The id keys the "
                "beaker panel AND both halves of every comparison, so the "
                "second chip would show the first one's beaker."
                % (act_id, o["id"]))
        seen.add(o["id"])
        if o["kind"] not in OXIDE_KINDS:
            raise ValueError(
                "oxide-bench %r oxide %r is a %r. The whole instrument is a "
                "sort into %s, and the comparison sentence says 'Both are %%s "
                "oxides' out of this word."
                % (act_id, o["id"], o["kind"], " and ".join(OXIDE_KINDS)))
        ph = o.get("ph")
        if not isinstance(ph, int) or isinstance(ph, bool) or not 0 <= ph <= 14:
            raise ValueError(
                "oxide-bench %r oxide %r reads pH %r. §5A: a named quantity is "
                "readable as a NUMBER, the chart it is read against runs 0 to "
                "14, and the numeral is printed at 48px."
                % (act_id, o["id"], ph))
        if o["residue"] not in RESIDUE_DEPTH and o["residue"] not in (
                "clear", "self", "gas"):
            raise ValueError(
                "oxide-bench %r oxide %r has residue %r. The drawing knows "
                "%s (a heap with depth) and clear / self / gas (nothing on the "
                "bottom); anything else would draw as nothing and the sentence "
                "beside it would still describe a solid."
                % (act_id, o["id"], o["residue"],
                   " and ".join(sorted(RESIDUE_DEPTH))))
        # ── discriminating case 1, asserted at the drawing ────────────────
        if o.get("insoluble"):
            if ph != 7:
                raise ValueError(
                    "oxide-bench %r flags %r insoluble and reads it at pH %d. "
                    "The whole point of that chip is that the reading DOES NOT "
                    "MOVE — a base the water cannot report. A moved reading "
                    "makes it an ordinary alkali and removes the case."
                    % (act_id, o["id"], ph))
            if not RESIDUE_DEPTH.get(o["residue"]):
                raise ValueError(
                    "oxide-bench %r flags %r insoluble and draws no residue "
                    "with depth. The student has to SEE the solid sitting "
                    "under an unmoved number: an insoluble oxide drawn as a "
                    "clear beaker is a page saying one thing and showing the "
                    "opposite." % (act_id, o["id"]))
        elif RESIDUE_DEPTH.get(o["residue"]) and ph == 7:
            raise ValueError(
                "oxide-bench %r draws %r as a heap on the bottom at pH 7 and "
                "does not flag it insoluble. That is the copper-oxide case "
                "unlabelled, and the comparison sentence would leave the 7 "
                "standing as a verdict." % (act_id, o["id"]))

    metals = [o for o in oxides if o["kind"] == "metal"]
    nons = [o for o in oxides if o["kind"] == "non-metal"]
    if not metals or not nons:
        raise ValueError(
            "oxide-bench %r puts %d metal oxide(s) and %d non-metal oxide(s) "
            "on the tray. The bench IS the contrast; one side of it alone "
            "teaches no discrimination."
            % (act_id, len(metals), len(nons)))
    if not any(o["ph"] > 7 for o in metals):
        raise ValueError(
            "oxide-bench %r has no metal oxide that takes the water above 7. "
            "The rule has to be on the bench as well as its exceptions, or the "
            "page is a list of special cases." % act_id)
    if not any(o["ph"] < 7 for o in nons):
        raise ValueError(
            "oxide-bench %r has no non-metal oxide that takes the water below "
            "7." % act_id)
    # ── discriminating case 1 and 2, asserted as PRESENT ──────────────────
    if not any(o["kind"] == "metal" and o.get("insoluble") for o in oxides):
        raise ValueError(
            "oxide-bench %r has no insoluble METAL oxide. `PTAB-11` — "
            "alkaline and basic are the same word — is elicited by a base that "
            "leaves the pH at 7, and without that chip the lesson's central "
            "distinction is a claim in a paragraph rather than a reading a "
            "student produced." % act_id)
    if not any(o["kind"] == "non-metal" and o["ph"] == 7 for o in oxides):
        raise ValueError(
            "oxide-bench %r has no NEUTRAL non-metal oxide. Water is hydrogen "
            "oxide and it reads 7; without it 'non-metal oxides are acidic' "
            "ships as a rule with no exception a student can reach." % act_id)
    if len({o["ph"] for o in oxides}) == len(oxides):
        raise ValueError(
            "oxide-bench %r gives every oxide a different pH, so the EQUAL "
            "branch of the comparison is unreachable. Two readings that match "
            "and mean different things is what this bench is for (NOTES-C8 "
            "§8)." % act_id)

    # ── the closing panel, checked against the readings under it ──────────
    claim = a.get("pattern_claim")
    if claim is not None:
        got = {"above": sum(1 for o in oxides if o["ph"] > 7),
               "below": sum(1 for o in oxides if o["ph"] < 7),
               "same": sum(1 for o in oxides if o["ph"] == 7)}
        if {k: int(v) for k, v in claim.items()} != got:
            raise ValueError(
                "oxide-bench %r closes by claiming %r and the six readings on "
                "the bench are %r. The student reads that sentence immediately "
                "after producing the numbers it counts."
                % (act_id, claim, got))
    close_prose = " ".join([a.get("close_title") or ""]
                           + list(a.get("close") or []))
    if close_prose.strip():
        low = _words(close_prose)
        for o in oxides:
            if _words(o["name"]) not in low:
                raise ValueError(
                    "oxide-bench %r closing panel never names %r, which is on "
                    "the tray. The panel reads the WHOLE bench — an oxide it "
                    "leaves out is one the student tested and the payoff "
                    "ignores." % (act_id, o["name"]))

    # ── the tray ──────────────────────────────────────────────────────────
    chips = "".join(
        '<button type="button" class="ks3-seg-btn ks3-oxb-chip" '
        'data-oxb-chip="%s" data-oxb-name="%s" aria-pressed="false">'
        '<span class="ks3-oxb-chipname">%s</span>'
        '<span class="ks3-oxb-chipformula">%s</span></button>'
        % (e(o["id"]), e(o["name"]), t(o["name"]), t(o["formula"]))
        for o in oxides)

    # ── fourteen beaker panels: the empty one shown, thirteen hidden ──────
    beakers = "".join(
        '<div class="ks3-oxb-beaker" data-oxb-slot="%d">%s%s</div>'
        % (slot, _oxide_beaker(a, None, slot),
           "".join(_oxide_beaker(a, o, slot) for o in oxides))
        for slot in (0, 1))

    # ── thirty ordered pairs, every sentence derived ──────────────────────
    cmps = "".join(
        '<p class="ks3-oxb-cmp" data-oxb-cmp="%s:%s" hidden>%s</p>'
        % (e(left["id"]), e(right["id"]), t(_oxide_compare(left, right)))
        for left in oxides for right in oxides if left["id"] != right["id"])

    untested = ", ".join(o["name"] for o in oxides)
    close = _close_panel(a, "ks3-oxb", "data-oxb-close")
    return (
        '<div class="ks3-oxb" data-oxb data-total="%d">'
        '<div class="ks3-oxb-tray">%s</div>'
        '<div class="ks3-oxb-beakers">%s</div>'
        '<div class="ks3-oxb-compare" data-oxb-compare hidden>'
        '<p class="ks3-oxb-cmp-eyebrow">%s</p>%s</div>'
        '<div class="ks3-oxb-controls">'
        '<button type="button" class="ks3-oxb-clear" data-oxb-clear disabled>'
        '%s</button>'
        '<p class="ks3-oxb-untested" data-oxb-untested>'
        '<span class="ks3-oxb-untested-lead">%s</span> '
        '<span data-oxb-untested-list>%s.</span></p>'
        '<p class="ks3-oxb-untested" data-oxb-alltested hidden>%s</p>'
        '</div>%s</div>'
        % (len(oxides), chips, beakers,
           t(a.get("compare_eyebrow") or "Side by side"), cmps,
           t(a.get("clear_label") or "Empty both beakers"),
           t(a.get("untested_lead") or "Not yet in a beaker:"), t(untested),
           t(a.get("all_tested") or "All of them have been in a beaker."),
           close))


# ═══ registration ════════════════════════════════════════════════════════

KIND_SHELL = {
    'property-sorter': ("ks3-prop-block",
                        ' data-instrument data-propblock '
                        'data-stage-done="0"'),
    'gap-filler': ("ks3-gapfill-block",
                   ' data-instrument data-gapfblock data-stage-done="0"'),
    'predict-cards': ("ks3-pcards-block",
                      ' data-instrument data-pcardblock '
                      'data-stage-done="0"'),
    'table-reader': ("ks3-tread-block",
                     ' data-instrument data-treadblock data-stage-done="0"'),
    'water-trough': ("ks3-trough-block",
                     ' data-instrument data-troughblock '
                     'data-stage-done="0"'),
    'halogen-grid': ("ks3-hgrid-block",
                     ' data-instrument data-hgridblock data-stage-done="0"'),
    'shell-strip': ("ks3-shell-block",
                    ' data-instrument data-shelblock data-stage-done="0"'),
    'oxide-bench': ("ks3-oxb-block",
                    ' data-instrument data-oxbblock data-stage-done="0"'),
}

KIND_FN = {
    'property-sorter': r_property_sorter,
    'gap-filler': r_gap_filler,
    'predict-cards': r_predict_cards,
    'table-reader': r_table_reader,
    'water-trough': r_water_trough,
    'halogen-grid': r_halogen_grid,
    'shell-strip': r_shell_strip,
    'oxide-bench': r_oxide_bench,
}
