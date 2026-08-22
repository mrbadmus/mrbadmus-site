"""ks3_art.c9 — C9's instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. C9 is *Metals and materials*: four
lessons, FOUR instrument families and NO drawn figure, all DOM, no canvas and
no animation loop anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY, on C7's and C8's conventions and for their reasons.

  · EMIT-BOTH-SHOW-ONE wherever a panel has a small closed set of states. This
    unit leans on it hardest of any so far: the route bench alone carries
    TWENTY-FOUR authored verdicts and not one of them is composed here.
  · NUMBERS ARE DERIVED, NEVER AUTHORED TWICE.
  · ONLY THE LADDER MARKS. Every bench below gives its verdict in WORDS.
  · Every family ticks a rail stop, so every family carries
    `data-stage-done="0"`. NOTHING IS TICKED ON LOAD (MRB-208).
  · Arrows are drawn as SVG by `t()`, never typed as U+2192.
  · CONTAINMENT, NOT CLIPPING: the two matrices carry `position: relative` on
    their scrollers.

═══════════════════════════════════════════════════════════════════════════
⚖️ RULED: `reaction-audit` IS ITS OWN FAMILY, NOT `reactivity-grid`
═══════════════════════════════════════════════════════════════════════════

`NOTES-C8.md` §4 expected C9's series to be `reactivity-grid`'s FOURTH use and
its first with more than four rows. `NOTES-C9.md` §3 then declined to use it
and asked for a ruling either way. **Kept separate**, for three reasons and in
that order:

1. **Folding requires editing `ks3_art/c5.py`**, which owns `reactivity-grid`.
   A content lane may not edit another unit's module (`docs/ks3/worktrees.md`
   §1), and generalising c5's renderer would rebuild C5's pages out of a C9
   content change. This alone settles it.
2. **The payloads do not convert**, which is Design's own §7 note. A
   `reactivity-grid` cell is reaction / no-reaction. A `reaction-audit` cell
   carries an observation, an optional word equation, an optional apparatus
   line, and a fourth state — *unavailable* — that the grid has no room for.
3. It would be the third metals grid in the chemistry sequence, which is §6's
   adjacency warning arriving as a default rather than as a need.

⚖️ **WHAT DOES CARRY FROM C5 IS THE RULING ABOUT THE DATA, AND THIS IS THE
FIRST INSTRUMENT WHERE IT IS TESTED PAST FOUR ROWS.** Order is `rank` and
never array position; `_audit_order()` is the only place the order is derived,
and `r_reaction_audit` checks the authored BANDS against it. Six rows, twelve
cells, and re-sorting the payload cannot change a single verdict or move a
single metal between bands.

═══════════════════════════════════════════════════════════════════════════
⊖ `unit-nav` IS NOT REGISTERED, AND MUST NOT BE
═══════════════════════════════════════════════════════════════════════════

`NOTES-C9.md` §7 registers `unit-nav` as C9's fifth family: a four-row `UNIT`
array on each page from which prev/next is derived. Design needs it because
her pages are standalone files that have to link to each other.

**The engine already owns this.** `build_ks3.py` generates endmatter prev/next
from unit order (§8.10 / audit law 16), for every lesson in the key stage,
from `structure.py`. Registering a family here would put a SECOND source of
the same links in the build, and the two would drift the first time a slot
moved. So it is dropped, and `SLUG`/`UNIT` are not carried into any lesson
record.

⊕ This also resolves `NOTES-C9.md` §2b, which asks what `c9-01` should do
about having no predecessor: C8's `metal-and-non-metal-oxides` slot EXISTS
since MRB-281 and renders as a routable coming-soon page, so the generated
back-link resolves and the question does not arise.

═══════════════════════════════════════════════════════════════════════════
⊖ AND `extraction-route` AND `spec-bench` STAY TWO FAMILIES
═══════════════════════════════════════════════════════════════════════════

§7 notes both are "choose a tool, be told what it costs you" and offers to
fold them. They are kept apart on Design's own grounds: `extraction-route`'s
verdicts are AUTHORED per (ore, method) pair — twenty-four of them, including
"works and is the wrong tool", which is a judgement no tag set produces — while
`spec-bench`'s are DERIVED from requirement tags. One is a table of rulings and
the other is a computation. They do not convert.

═══════════════════════════════════════════════════════════════════════════
THE HOOKS ARE AN INTERFACE
═══════════════════════════════════════════════════════════════════════════

Named off each family's short name — raud / pdeck / xroute / specb — and the
contract `shared/ks3.js` binds against. Shell classes checked free against
every `KIND_SHELL` value in `ks3_art` before minting (MRB-279):
`ks3-raudit-block`, `ks3-pdeck-block`, `ks3-xroute-block`, `ks3-specb-block`.
"""

from ks3_art.kit import e, rich, t


# ═══ shared inside C9 ════════════════════════════════════════════════════

def _c9_seg(cls, label, **attrs):
    """One segmented-control button, unpressed at rest. No `correct`, ever."""
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="false">%s</button>'
            % (e(cls), extra, t(label)))


def _counter_agrees(a, act_id, n, what):
    """The block-head counter's denominator must be the number of things."""
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
    """The payoff panel: title, paragraphs, an optional authored `id`."""
    paras = a.get("close") or []
    if not paras:
        return ""
    ident = (' id="%s"' % e(a["close_id"])) if a.get("close_id") else ""
    title = (('<p class="%s-closetitle">%s</p>' % (cls, t(a["close_title"])))
             if a.get("close_title") else "")
    return ('<div class="%s-close"%s hidden %s>%s%s</div>'
            % (cls, ident, hook, title,
               "".join("<p>%s</p>" % rich(p) for p in paras)))


def _no_correct_flags(rows, act_id, family):
    """Refuse a `correct` key on any commit option, anywhere in C9."""
    for row in rows:
        for opt in (row.get("options") or []):
            if isinstance(opt, dict) and ("correct" in opt or
                                          "correction" in opt):
                raise ValueError(
                    "%s %r: option %r carries a marking key. Nothing outside "
                    "the mastery ladder marks in C9 — every bench gives its "
                    "verdict in words."
                    % (family, act_id, opt.get("id") or opt.get("label")))


def _ranks_are_dense(rows, act_id, family, field="rank"):
    """Ranks are 0..n-1, no gap and no tie. ORDER IS DATA (the C5 ruling).

    ⚖️ THE ASSERTION THIS UNIT IS BUILT ON, AND THE FIRST TIME IT IS TESTED
    PAST FOUR ROWS. Every verdict on the audit and every outcome on the deck is
    decided by comparing these numbers. A TIE is two subjects the page cannot
    put in order while claiming to have derived one; a GAP is an order with a
    hole in it that still sorts correctly, which is worse, because it looks
    right.
    """
    ranks = []
    for row in rows:
        if row.get(field) is None:
            raise ValueError(
                "%s %r: %r has no %r. ORDER IS DATA — the order is read off "
                "this field and never off the position of the row in the "
                "array, so a payload re-sorted for layout cannot silently "
                "re-teach the series."
                % (family, act_id, row.get("id") or row.get("name"), field))
        ranks.append(int(row[field]))
    if sorted(ranks) != list(range(len(ranks))):
        raise ValueError(
            "%s %r ranks its %d row(s) %s. Ranks are 0..n-1 with no gap and "
            "no tie: a tie is two things the page cannot order while claiming "
            "to have derived an order, and a gap looks correct while being "
            "wrong." % (family, act_id, len(ranks), sorted(ranks)))
    return ranks


# ═══ c9-01 · reaction-audit ══════════════════════════════════════════════

def _audit_order(metals):
    """THE ONLY PLACE THE DERIVED ORDER IS PRODUCED, AND IT IS FROM `rank`."""
    return [m["id"] for m in sorted(metals, key=lambda m: int(m["rank"]))]


def r_reaction_audit(a, act_id):
    """⊕ c9-01 `#s-bench` — six metals down, two liquids across, twelve cells.

    Every cell is predict-then-read. A cell may be UNAVAILABLE — readable,
    with a reason, and no prediction taken — which is potassium in dilute
    acid: violent with water alone, and dilute acid is mostly water. That
    fourth state is why this is not `reactivity-grid` (see the header).

    ⚖️ **THE BANDS ARE CHECKED AGAINST THE CELLS, EVERY METAL, BOTH WAYS.**
    The synthesis panel sorts the six into three bands and then states the
    order it has just derived, so the bands are a CLAIM about the twelve cells
    above them:

      · a metal in the water band must actually react in cold water;
      · a metal in the acid band must do NOTHING worth watching in water and
        react in acid — that is the whole meaning of the label;
      · a metal in the neither band must react in neither.

    Without this, a page can sort a metal into "needs acid before much
    happens" while the cell above says it fizzed in water, and both halves
    render perfectly.

    ⚖️ **AND THE BANDS MUST BE IN RANK ORDER AND NONE MAY BE EMPTY.** An empty
    band is a heading over nothing; bands out of order would have the panel
    claim a series that its own grouping contradicts.

    ⚖️ **A CELL THAT DOES NOT HAPPEN CARRIES NO EQUATION.** Writing products
    for a reaction that never happens is the error `#s-think` is about.

    HOOKS: `data-raud` (wrapper, `data-total`) · `data-raud-cell` (valued
    `metal:reagent`) · `data-raud-opt` · `data-raud-out` · `data-raud-close`.
    """
    metals = a.get("metals") or []
    reagents = a.get("reagents") or []
    bands = a.get("bands") or []
    if len(metals) < 4 or len(reagents) < 2:
        raise ValueError(
            "reaction-audit %r has %d metal(s) and %d reagent(s). The order "
            "is derived from the pattern of results, and a pattern needs more "
            "than one liquid and more than three metals."
            % (act_id, len(metals), len(reagents)))
    _ranks_are_dense(metals, act_id, "reaction-audit")

    band_ids = [b["id"] for b in bands]
    if len(set(band_ids)) != len(band_ids):
        raise ValueError("reaction-audit %r repeats a band id." % act_id)
    for b in bands:
        if not b.get("label") or not b.get("note"):
            raise ValueError(
                "reaction-audit %r band %r has no label or no note. The band "
                "is a heading over a claim." % (act_id, b.get("id")))

    water_id = reagents[0]["id"]
    n_cells = 0
    by_band = {}
    for m in sorted(metals, key=lambda m: int(m["rank"])):
        for key in ("id", "name", "band", "form"):
            if not m.get(key):
                raise ValueError(
                    "reaction-audit %r metal %r has no %r."
                    % (act_id, m.get("id"), key))
        if m["band"] not in band_ids:
            raise ValueError(
                "reaction-audit %r sorts %r into band %r, which is not one of "
                "%s. The synthesis panel prints the band's own label."
                % (act_id, m["id"], m["band"], band_ids))
        by_band.setdefault(m["band"], []).append(m["id"])

        for rg in reagents:
            cell = m.get(rg["id"])
            if not cell:
                raise ValueError(
                    "reaction-audit %r has no cell for %r in %r. Twelve "
                    "tubes means twelve — a hole is a comparison the student "
                    "is invited to make and then cannot."
                    % (act_id, m["id"], rg["id"]))
            n_cells += 1
            if not cell.get("obs"):
                raise ValueError(
                    "reaction-audit %r cell %s:%s records no observation. "
                    "Reading the cell IS the activity."
                    % (act_id, m["id"], rg["id"]))
            if cell.get("skipped"):
                if cell.get("happens") or cell.get("eq"):
                    raise ValueError(
                        "reaction-audit %r cell %s:%s is skipped AND carries "
                        "a result. A cell that is not done has no result — "
                        "the note is the teaching."
                        % (act_id, m["id"], rg["id"]))
                continue
            if not cell.get("happens") and cell.get("eq"):
                raise ValueError(
                    "reaction-audit %r cell %s:%s does not react and carries "
                    "a word equation. Writing products for a reaction that "
                    "never happens is what `#s-think` is about."
                    % (act_id, m["id"], rg["id"]))
            if cell.get("happens") and not cell.get("eq"):
                raise ValueError(
                    "reaction-audit %r cell %s:%s reacts and carries no word "
                    "equation." % (act_id, m["id"], rg["id"]))

        # ── the band assertion, per metal, on the cells above it ─────────
        w = m.get(water_id) or {}
        in_water = bool(w.get("happens")) and not w.get("skipped")
        others = [m.get(rg["id"]) or {} for rg in reagents[1:]]
        in_other = any(bool(c.get("happens")) and not c.get("skipped")
                       for c in others)
        want = ("water" if in_water else ("acid" if in_other else "neither"))
        if m["band"] != want:
            raise ValueError(
                "reaction-audit %r sorts %r into band %r and its own twelve "
                "cells say %r (%s in %s; %s in the rest). The panel groups "
                "the metals the student has just read, so a band that "
                "disagrees with the cells above it is the page contradicting "
                "itself in front of them."
                % (act_id, m["id"], m["band"], want,
                   "reacts" if in_water else "does not react", water_id,
                   "reacts" if in_other else "does not react"))

    empty = [b for b in band_ids if b not in by_band]
    if empty:
        raise ValueError(
            "reaction-audit %r declares band(s) %s that no metal falls into. "
            "The synthesis panel opens when every cell has been read, so an "
            "empty band is a heading over nothing." % (act_id, empty))
    order = _audit_order(metals)
    pos = dict((mid, i) for i, mid in enumerate(order))
    seen_band_order = [b for b in band_ids if b in by_band]
    tops = [min(pos[x] for x in by_band[b]) for b in seen_band_order]
    if tops != sorted(tops):
        raise ValueError(
            "reaction-audit %r lists its bands %s, and by rank the metals in "
            "them run %s. The panel states the derived ORDER immediately "
            "under the bands, so bands out of order contradict it."
            % (act_id, seen_band_order, tops))

    claim = a.get("order_claim")
    if claim is not None and list(claim) != order:
        raise ValueError(
            "reaction-audit %r states the order %s and its ranks give %s. "
            "That sentence is the conclusion of the whole bench."
            % (act_id, list(claim), order))
    _counter_agrees(a, act_id, n_cells, "cell(s)")
    _no_correct_flags([{"options": a.get("predict_options") or []}],
                      act_id, "reaction-audit")

    heads = "".join('<th scope="col">%s</th>' % t(rg["label"])
                    for rg in reagents)
    body, outs = [], []
    for m in sorted(metals, key=lambda m: int(m["rank"])):
        tds = []
        for rg in reagents:
            key = "%s:%s" % (m["id"], rg["id"])
            cell = m[rg["id"]]
            tds.append(
                '<td class="ks3-raud-td"><button type="button" '
                'class="ks3-raud-cell" data-raud-cell="%s" '
                'aria-pressed="false"><span class="ks3-raud-mark">%s</span>'
                '</button></td>' % (e(key), t(a.get("resting_mark") or "?")))
            care = (('<p class="ks3-raud-care">%s</p>' % rich(cell["care"]))
                    if cell.get("care") else "")
            eq = (('<p class="ks3-raud-eq">%s</p>'
                   % t("%s → %s" % (cell["eq"][0], cell["eq"][1])))
                  if cell.get("eq") else "")
            # ⚑ `vigour` IS AUTHORED PER CELL AND IS RENDERED. Design gives
            # every reacting cell a word — violent, vigorous, steady — and the
            # first cut of this renderer dropped it on the floor, which
            # `ks3_key_audit.py` reported as a key "read by nothing". It was
            # exactly that: authored content that reached no student. It goes
            # into the verdict line, which is the one place on the cell where
            # a single word does work, and it is the difference between
            # "it reacts" for potassium and for iron.
            verdict = a.get("verdict_skipped") if cell.get("skipped") else (
                a.get("verdict_yes") if cell.get("happens")
                else a.get("verdict_no"))
            if cell.get("vigour") and cell.get("happens") \
                    and not cell.get("skipped"):
                verdict = "%s %s." % (verdict, cell["vigour"].capitalize())
            outs.append(
                '<div class="ks3-raud-one" data-raud-out="%s" hidden>'
                '<p class="ks3-raud-title">%s</p>'
                '<p class="ks3-raud-verdict">%s</p>'
                '<p class="ks3-raud-obs">%s</p>%s%s</div>'
                % (e(key),
                   t("%s in %s" % (m["name"], rg["phrase"])),
                   t(verdict or ""), rich(cell["obs"]), eq, care))
        body.append('<tr><th scope="row"><span class="ks3-raud-mname">%s</span>'
                    '<span class="ks3-raud-mform">%s</span></th>%s</tr>'
                    % (t(m["name"]), t(m["form"]), "".join(tds)))

    band_html = "".join(
        '<div class="ks3-raud-band"><p class="ks3-raud-blabel">%s</p>'
        '<p class="ks3-raud-bmembers">%s</p>'
        '<p class="ks3-raud-bnote">%s</p></div>'
        % (t(b["label"]),
           t(", ".join(next(m["name"] for m in metals if m["id"] == x)
                       for x in by_band[b["id"]])),
           rich(b["note"]))
        for b in bands if b["id"] in by_band)

    predict = ""
    if a.get("predict_options"):
        predict = ('<div class="ks3-raud-predict">'
                   '<p class="ks3-raud-prompt">%s</p>%s</div>'
                   % (rich(a.get("predict_prompt") or ""),
                      "".join(_c9_seg("ks3-raud-opt", o["label"],
                                      data_raud_opt=o["id"])
                              for o in a["predict_options"])))

    close = _close_panel(a, "ks3-raud", "data-raud-close")
    return ('<div class="ks3-raud" data-raud data-total="%d">'
            '<div class="ks3-raud-scroll"><table class="ks3-raud-table">'
            '<thead><tr><th scope="col" class="ks3-raud-corner">'
            '<span class="ks3-sr">Metal</span></th>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>%s'
            '<div class="ks3-raud-readout" data-raud-readout>'
            '<p class="ks3-raud-rest">%s</p>%s</div>'
            '<div class="ks3-raud-bands" hidden data-raud-bands>%s</div>'
            '%s</div>'
            % (n_cells, heads, "".join(body), predict,
               t(a.get("resting") or "Pick a tube."), "".join(outs),
               band_html, close))


# ═══ c9-02 · prediction-deck ═════════════════════════════════════════════

def _deck_happens(added, inside):
    """THE ONLY PLACE A CARD'S OUTCOME IS DECIDED, AND IT IS FROM `rank`.

    A displacement happens when the element ADDED is more reactive than the
    one already in the compound — a lower rank. Never stored per card, so a
    card cannot be authored to contradict the series it is drawn from.
    """
    return int(added["rank"]) < int(inside["rank"])


def r_prediction_deck(a, act_id):
    """⊕ c9-02 `#s-deck` — eight proposals, one commitment each.

    ⚖️ **NO CARD STORES ITS OWN OUTCOME.** Every card names what is ADDED and
    what is INSIDE the compound, and `_deck_happens` decides from the ranked
    strip. That is the instrument's whole argument — the rule is the only
    thing left standing when the deck is sorted — and a per-card `happens`
    flag would let a card be authored against the series printed beside it.

    ⚖️ **THE AUTHORED OBSERVATION IS CHECKED AGAINST THE DERIVED OUTCOME.** A
    card that resolves to "nothing happens" whose observation describes a
    colour change is a page arguing with itself, and nothing else could see it.

    ⚖️ **BOTH OUTCOMES MUST OCCUR, AND THE LEAD'S COUNT IS DERIVED.** A deck
    where everything happens has no rule in it, only examples; and "five of
    the eight happen" is a number the student reads before committing to any
    of them.

    HOOKS: `data-pdeck` (wrapper, `data-total`) · `data-pdeck-card` ·
    `data-pdeck-opt` · `data-pdeck-reveal` · `data-pdeck-close`.
    """
    strip = a.get("strip") or []
    cards = a.get("proposals") or []
    if len(strip) < 3 or len(cards) < 4:
        raise ValueError(
            "prediction-deck %r has %d strip entr(ies) and %d card(s)."
            % (act_id, len(strip), len(cards)))
    _ranks_are_dense(strip, act_id, "prediction-deck")
    by_name = dict((s["name"], s) for s in strip)
    if len(by_name) != len(strip):
        raise ValueError("prediction-deck %r repeats a strip name." % act_id)
    _no_correct_flags(cards, act_id, "prediction-deck")

    n_yes = 0
    html = []
    seen = set()
    for c in cards:
        for key in ("id", "added", "inside", "label", "setup", "obs"):
            if not c.get(key):
                raise ValueError(
                    "prediction-deck %r card %r has no %r."
                    % (act_id, c.get("id"), key))
        if c["id"] in seen:
            raise ValueError(
                "prediction-deck %r authors the card id %r twice."
                % (act_id, c["id"]))
        seen.add(c["id"])
        if "happens" in c:
            raise ValueError(
                "prediction-deck %r card %r stores its own outcome. The "
                "outcome is DERIVED from the ranked strip — a stored flag can "
                "be authored against the series printed beside it."
                % (act_id, c["id"]))
        for side in ("added", "inside"):
            if c[side] not in by_name:
                raise ValueError(
                    "prediction-deck %r card %r names %r as %s, which is not "
                    "on the strip. Every card is decided by comparing two "
                    "strip entries." % (act_id, c["id"], c[side], side))
        happens = _deck_happens(by_name[c["added"]], by_name[c["inside"]])
        n_yes += 1 if happens else 0
        if bool(c.get("eq")) != happens:
            raise ValueError(
                "prediction-deck %r card %r resolves to %r and %s a word "
                "equation. Products belong to reactions that happen."
                % (act_id, c["id"], happens,
                   "carries" if c.get("eq") else "carries no"))

        # ── the content-truth assertion, per card ────────────────────────
        low = c["obs"].lower()
        NEG = ("no change", "nothing", "no reaction", "unchanged",
               "stays", "remains", "does not")
        looks_negative = any(k in low for k in NEG)
        if happens and looks_negative and "but" not in low:
            raise ValueError(
                "prediction-deck %r card %r resolves to a reaction and its "
                "observation reads as a null result: %r. The verdict and the "
                "observation are read together."
                % (act_id, c["id"], c["obs"][:60]))
        if not happens and not looks_negative:
            raise ValueError(
                "prediction-deck %r card %r resolves to NO reaction and its "
                "observation never says so: %r. A student reads the "
                "observation, not the rank."
                % (act_id, c["id"], c["obs"][:60]))

        opts = "".join(
            _c9_seg("ks3-pdeck-opt", o["label"], data_pdeck_opt=o["id"])
            for o in (c.get("options") or a.get("options") or []))
        eq = (('<p class="ks3-pdeck-eq">%s</p>' % t(c["eq"]))
              if c.get("eq") else "")
        html.append(
            '<div class="ks3-pdeck-card" data-pdeck-card="%s" data-open="0">'
            '<p class="ks3-pdeck-label">%s</p>'
            '<p class="ks3-pdeck-setup">%s</p>'
            '<div class="ks3-pdeck-opts">%s</div>'
            '<div class="ks3-pdeck-reveal" hidden data-pdeck-reveal>'
            '<p class="ks3-pdeck-verdict">%s</p>'
            '<p class="ks3-pdeck-obs">%s</p>%s</div></div>'
            % (e(c["id"]), t(c["label"]), rich(c["setup"]), opts,
               t((a.get("verdict_yes") if happens else a.get("verdict_no"))
                 or ""), rich(c["obs"]), eq))

    if not n_yes or n_yes == len(cards):
        raise ValueError(
            "prediction-deck %r resolves to %d of %d happening. A deck where "
            "everything happens, or nothing does, has no rule in it."
            % (act_id, n_yes, len(cards)))
    claim = a.get("happens_claim")
    if claim is not None and int(claim) != n_yes:
        raise ValueError(
            "prediction-deck %r says %s of the cards happen and the ranks "
            "give %d. The lead is read BEFORE anything is committed to."
            % (act_id, claim, n_yes))
    _counter_agrees(a, act_id, len(cards), "card(s)")

    strip_html = "".join(
        '<li class="ks3-pdeck-strip-item"%s><span class="ks3-pdeck-sname">%s'
        '</span>%s</li>'
        % (' data-tag="1"' if s.get("tag") else "", t(s["name"]),
           ('<span class="ks3-pdeck-stag">%s</span>' % t(s["tag"]))
           if s.get("tag") else "")
        for s in sorted(strip, key=lambda s: int(s["rank"])))

    close = _close_panel(a, "ks3-pdeck", "data-pdeck-close")
    return ('<div class="ks3-pdeck" data-pdeck data-total="%d">'
            '<ol class="ks3-pdeck-strip">%s</ol>'
            '<div class="ks3-pdeck-cards">%s</div>%s</div>'
            % (len(cards), strip_html, "".join(html), close))


# ═══ c9-03 · extraction-route ════════════════════════════════════════════

def r_extraction_route(a, act_id):
    """⊕ c9-03 `#s-bench` — six deliveries, four methods, 24 authored verdicts.

    ⚖️ **THREE VERDICTS, NOT TWO, AND THE THIRD IS THE LESSON.** A method can
    WORK, can NOT WORK, or can work and be THE WRONG TOOL — heating silver
    oxide works and so does electrolysis, and a works would not pay for the
    second. A two-state bench cannot say that, and saying it is the whole
    point of asking a student to choose.

    ⚖️ **EVERY PAIR IS AUTHORED — 24 OF THEM — AND NONE IS COMPOSED.** The C6
    `acid-metal-grid` precedent: composing a verdict from the ore's name and
    the method's would make several cells literally the same paragraph and
    make `<strong>` impossible.

    ⚖️ **EACH ORE'S `route` MUST NAME A METHOD THAT ACTUALLY WORKS FOR IT.**
    The synthesis groups the ores by their best route and prints it. An ore
    whose declared route is a method its own verdict says fails is the panel
    recommending something the bench has just refused.

    ⚖️ **AND AT LEAST ONE ORE MUST DEFEAT CARBON.** Aluminium oxide is why
    `MATL-09` exists — "any oxide gives up its oxygen to carbon if the furnace
    is hot enough" — and without a single ore that carbon cannot free, the
    bench teaches that carbon always works.

    HOOKS: `data-xroute` (wrapper, `data-total`) · `data-xroute-ore` ·
    `data-xroute-method` · `data-xroute-out` · `data-xroute-close`.
    """
    ores = a.get("ores") or []
    methods = a.get("methods") or []
    groups = a.get("route_groups") or []
    if len(ores) < 4 or len(methods) < 3:
        raise ValueError(
            "extraction-route %r has %d ore(s) and %d method(s)."
            % (act_id, len(ores), len(methods)))
    method_ids = [m["id"] for m in methods]
    group_ids = [g["id"] for g in groups]
    carbon = a.get("carbon_method")
    n_pairs, carbon_fails = 0, 0
    by_group = {}

    for o in ores:
        for key in ("id", "name", "metal", "route", "setup", "line"):
            if not o.get(key):
                raise ValueError(
                    "extraction-route %r ore %r has no %r."
                    % (act_id, o.get("id"), key))
        verdicts = o.get("verdicts") or {}
        missing = [m for m in method_ids if m not in verdicts]
        if missing:
            raise ValueError(
                "extraction-route %r ore %r has no verdict for %s. Every ore "
                "is offered every method, so a missing verdict is a choice "
                "the student can make and get nothing back from."
                % (act_id, o["id"], missing))
        surplus = sorted(set(verdicts) - set(method_ids))
        if surplus:
            raise ValueError(
                "extraction-route %r ore %r authors verdict(s) for %s, which "
                "are not methods on this bench." % (act_id, o["id"], surplus))
        for mid in method_ids:
            v = verdicts[mid]
            n_pairs += 1
            for key in ("title", "why"):
                if not v.get(key):
                    raise ValueError(
                        "extraction-route %r verdict %s:%s has no %r."
                        % (act_id, o["id"], mid, key))
            if not v.get("works") and v.get("eq"):
                raise ValueError(
                    "extraction-route %r verdict %s:%s does not work and "
                    "carries an equation." % (act_id, o["id"], mid))
        if o["route"] not in method_ids:
            raise ValueError(
                "extraction-route %r ore %r declares route %r, which is not a "
                "method on this bench." % (act_id, o["id"], o["route"]))
        if not verdicts[o["route"]].get("works"):
            raise ValueError(
                "extraction-route %r ore %r declares its route as %r and its "
                "own verdict for that method says it does NOT work. The "
                "synthesis panel prints this route as the answer."
                % (act_id, o["id"], o["route"]))
        if carbon and not verdicts.get(carbon, {}).get("works"):
            carbon_fails += 1
        # ⊕ THE GROUP DEFAULTS TO THE ROUTE, because that is what the panel
        # groups by: "ores by their best route". Design's `ROUTE_GROUPS` ids
        # ARE the method ids, and her ores carry no separate `group` key.
        # Defaulting rather than requiring one keeps the two from drifting —
        # an ore whose route moved would otherwise stay in its old group.
        grp = o.get("group") or o.get("route")
        if grp is not None:
            if grp not in group_ids:
                raise ValueError(
                    "extraction-route %r ore %r is in group %r, which is not "
                    "declared." % (act_id, o["id"], grp))
            by_group.setdefault(grp, []).append(o["id"])

    if carbon and not carbon_fails:
        raise ValueError(
            "extraction-route %r: carbon frees every ore on the bench. "
            "`MATL-09` is the belief that any oxide gives up its oxygen to "
            "carbon if the furnace is hot enough, and a bench with no "
            "counter-example teaches it rather than confronting it."
            % act_id)
    for g in groups:
        if not g.get("label") or not g.get("note"):
            raise ValueError(
                "extraction-route %r group %r has no label or note."
                % (act_id, g.get("id")))
        if by_group and g["id"] not in by_group:
            raise ValueError(
                "extraction-route %r declares group %r that no ore falls "
                "into." % (act_id, g["id"]))
    _counter_agrees(a, act_id, len(ores), "route(s) found")
    _no_correct_flags([{"options": a.get("predict_options") or []}],
                      act_id, "extraction-route")

    picker = "".join(_c9_seg("ks3-xroute-ore", o["name"],
                             data_xroute_ore=o["id"]) for o in ores)
    mpick = "".join(_c9_seg("ks3-xroute-method", m["label"],
                            data_xroute_method=m["id"]) for m in methods)
    outs = []
    for o in ores:
        for mid in method_ids:
            v = o["verdicts"][mid]
            eq = (('<p class="ks3-xroute-eq">%s</p>' % t(v["eq"]))
                  if v.get("eq") else "")
            # ⚠️ `data-works` IS EMITTED SO THE SHELL NEVER HAS TO DECIDE.
            # The rail stop ticks when the student has FOUND a route, and
            # "found" means they opened a verdict that works. Deriving that in
            # JS would put the works/does-not-work judgement in two places —
            # here, where it is authored, and there, where it would be
            # re-inferred from the words. One source.
            outs.append(
                '<div class="ks3-xroute-one" data-xroute-out="%s" '
                'data-works="%d" data-ore="%s" hidden>'
                '<p class="ks3-xroute-setup">%s</p>'
                '<p class="ks3-xroute-title">%s</p>'
                '<p class="ks3-xroute-why">%s</p>%s</div>'
                % (e("%s:%s" % (o["id"], mid)), 1 if v.get("works") else 0,
                   e(o["id"]), rich(o["setup"]),
                   t(v["title"]), rich(v["why"]), eq))
    group_html = "".join(
        '<div class="ks3-xroute-group"><p class="ks3-xroute-glabel">%s</p>'
        '<p class="ks3-xroute-gmembers">%s</p>'
        '<p class="ks3-xroute-gnote">%s</p></div>'
        % (t(g["label"]),
           t(", ".join(next(o["name"] for o in ores if o["id"] == x)
                       for x in by_group.get(g["id"], []))),
           rich(g["note"]))
        for g in groups if g["id"] in by_group)

    close = _close_panel(a, "ks3-xroute", "data-xroute-close")
    return ('<div class="ks3-xroute" data-xroute data-total="%d" '
            'data-pairs="%d">'
            '<div class="ks3-xroute-pickers">'
            '<div class="ks3-xroute-ores">%s</div>'
            '<div class="ks3-xroute-methods">%s</div></div>'
            '<div class="ks3-xroute-readout" data-xroute-readout>'
            '<p class="ks3-xroute-rest">%s</p>%s</div>'
            '<div class="ks3-xroute-groups" hidden data-xroute-groups>%s</div>'
            '%s</div>'
            % (len(ores), n_pairs, picker, mpick,
               t(a.get("resting") or "Pick a delivery, then pick a method."),
               "".join(outs), group_html, close))


# ═══ c9-04 · spec-bench ══════════════════════════════════════════════════

def r_spec_bench(a, act_id):
    """⊕ c9-04 `#s-bench` — four jobs, six materials, one match each.

    ⚖️ **EXACTLY ONE MATERIAL SATISFIES EACH JOB, AND IT IS COMPUTED.** The
    match is derived from the requirement tag sets, never authored, so a job
    cannot be given an answer its own requirements do not select. Two matches
    means the job does not discriminate; none means it cannot be done.

    ⚖️ **A REJECTION IS REPORTED AS THE NAMED REQUIREMENT IT FAILS, NEVER AS
    A COUNT.** "Fails 2 of 4" teaches nothing; "it passes carbon dioxide, so
    the drink goes flat" teaches the lesson. So every material must carry a
    REASON for every requirement it does not meet, and a material whose
    `meets` and `fails` do not partition the requirements it is judged on is
    refused — that gap is exactly where a silent "no reason given" comes from.

    HOOKS: `data-specb` (wrapper, `data-total`) · `data-specb-job` ·
    `data-specb-mat` · `data-specb-out` · `data-specb-close`.
    """
    reqs = a.get("reqs") or {}
    mats = a.get("materials") or []
    jobs = a.get("jobs") or []
    if not reqs or len(mats) < 3 or len(jobs) < 2:
        raise ValueError(
            "spec-bench %r has %d requirement(s), %d material(s) and %d "
            "job(s)." % (act_id, len(reqs), len(mats), len(jobs)))

    for m in mats:
        for key in ("id", "name", "cls"):
            if not m.get(key):
                raise ValueError(
                    "spec-bench %r material %r has no %r."
                    % (act_id, m.get("id"), key))
        meets = set(m.get("meets") or [])
        fails = dict(m.get("fails") or {})
        unknown = sorted((meets | set(fails)) - set(reqs))
        if unknown:
            raise ValueError(
                "spec-bench %r material %r names requirement(s) %s that are "
                "not declared." % (act_id, m["id"], unknown))
        both = sorted(meets & set(fails))
        if both:
            raise ValueError(
                "spec-bench %r material %r both meets and fails %s."
                % (act_id, m["id"], both))
        for rid, reason in fails.items():
            if not reason:
                raise ValueError(
                    "spec-bench %r material %r fails %r with no reason. A "
                    "rejection is reported as the requirement it fails and "
                    "WHY — never as a count." % (act_id, m["id"], rid))

    n_pairs = 0
    for j in jobs:
        for key in ("id", "name", "setup", "praise"):
            if not j.get(key):
                raise ValueError(
                    "spec-bench %r job %r has no %r." % (act_id, j.get("id"), key))
        want = list(j.get("reqs") or [])
        if not want:
            raise ValueError(
                "spec-bench %r job %r asks for no requirements, so every "
                "material matches it." % (act_id, j["id"]))
        unknown = sorted(set(want) - set(reqs))
        if unknown:
            raise ValueError(
                "spec-bench %r job %r names requirement(s) %s that are not "
                "declared." % (act_id, j["id"], unknown))
        winners = []
        for m in mats:
            n_pairs += 1
            meets = set(m.get("meets") or [])
            fails = dict(m.get("fails") or {})
            missing = [r for r in want if r not in meets]
            unexplained = [r for r in missing if r not in fails]
            if unexplained:
                raise ValueError(
                    "spec-bench %r: material %r is judged against job %r and "
                    "neither meets nor explains %s. `meets` and `fails` must "
                    "partition every requirement a material is judged on, or "
                    "the bench rejects it with nothing to say."
                    % (act_id, m["id"], j["id"], unexplained))
            if not missing:
                winners.append(m["id"])
        if len(winners) != 1:
            raise ValueError(
                "spec-bench %r job %r is satisfied by %d material(s) (%s) and "
                "must be satisfied by exactly one. Two means the job does not "
                "discriminate; none means it cannot be done."
                % (act_id, j["id"], len(winners), winners or "nothing"))
        if j.get("answer") and j["answer"] != winners[0]:
            raise ValueError(
                "spec-bench %r job %r declares the answer %r and its own "
                "requirements select %r."
                % (act_id, j["id"], j["answer"], winners[0]))
    _counter_agrees(a, act_id, len(jobs), "job(s) matched")

    # ⚠️ THE JOB CARD IS A REAL <button>, NOT A DIV WITH A HANDLER. Picking a
    # job is the first half of every choice on this bench, so it has to be
    # reachable by keyboard and announce itself as a control. `aria-pressed`
    # carries the state as a word rather than as the presence of a class (R2).
    jobs_html = "".join(
        '<div class="ks3-specb-job" data-specb-job="%s" data-open="0">'
        '<button type="button" class="ks3-specb-jbtn" data-specb-jbtn '
        'aria-pressed="false">'
        '<span class="ks3-specb-jname">%s</span>'
        '<span class="ks3-specb-setup">%s</span>'
        '<span class="ks3-specb-reqs">%s</span></button></div>'
        % (e(j["id"]), t(j["name"]), rich(j["setup"]),
           "".join('<span class="ks3-specb-req">%s</span>' % t(reqs[r])
                   for r in j["reqs"]))
        for j in jobs)
    mats_html = "".join(
        _c9_seg("ks3-specb-mat", m["name"], data_specb_mat=m["id"])
        for m in mats)

    outs = []
    for j in jobs:
        for m in mats:
            meets = set(m.get("meets") or [])
            fails = dict(m.get("fails") or {})
            missing = [r for r in j["reqs"] if r not in meets]
            if missing:
                body = "".join(
                    '<li><span class="ks3-specb-rname">%s</span>'
                    '<span class="ks3-specb-rwhy">%s</span></li>'
                    % (t(reqs[r]), rich(fails[r])) for r in missing)
                inner = ('<p class="ks3-specb-verdict">%s</p>'
                         '<ul class="ks3-specb-fails">%s</ul>'
                         % (t(a.get("verdict_no") or ""), body))
            else:
                inner = ('<p class="ks3-specb-verdict">%s</p>'
                         '<p class="ks3-specb-praise">%s</p>'
                         % (t(a.get("verdict_yes") or ""), rich(j["praise"])))
            # ⚠️ `data-fit` for the same reason as `data-works` above: the
            # match is COMPUTED here, from the requirement tag sets, and the
            # shell reads the answer rather than recomputing it.
            outs.append('<div class="ks3-specb-one" data-specb-out="%s" '
                        'data-fit="%d" data-job="%s" hidden>'
                        '<p class="ks3-specb-head">%s</p>%s</div>'
                        % (e("%s:%s" % (j["id"], m["id"])),
                           0 if missing else 1, e(j["id"]),
                           t("%s for the %s" % (m["name"], j["name"])), inner))

    close = _close_panel(a, "ks3-specb", "data-specb-close")
    return ('<div class="ks3-specb" data-specb data-total="%d" '
            'data-pairs="%d">'
            '<div class="ks3-specb-jobs">%s</div>'
            '<div class="ks3-specb-shelf">%s</div>'
            '<div class="ks3-specb-readout" data-specb-readout>'
            '<p class="ks3-specb-rest">%s</p>%s</div>%s</div>'
            % (len(jobs), n_pairs, jobs_html, mats_html,
               t(a.get("resting") or "Pick a job, then pick a material."),
               "".join(outs), close))


# ═══ registration ════════════════════════════════════════════════════════

KIND_SHELL = {
    'reaction-audit': ("ks3-raudit-block",
                       ' data-instrument data-raudblock data-stage-done="0"'),
    'prediction-deck': ("ks3-pdeck-block",
                        ' data-instrument data-pdeckblock '
                        'data-stage-done="0"'),
    'extraction-route': ("ks3-xroute-block",
                         ' data-instrument data-xrouteblock '
                         'data-stage-done="0"'),
    'spec-bench': ("ks3-specb-block",
                   ' data-instrument data-specbblock data-stage-done="0"'),
}

KIND_FN = {
    'reaction-audit': r_reaction_audit,
    'prediction-deck': r_prediction_deck,
    'extraction-route': r_extraction_route,
    'spec-bench': r_spec_bench,
}
