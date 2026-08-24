"""ks3_art.p1 — P1's instruments and registrations.

ONE UNIT, ONE FILE. Nothing here is read by any other unit; nothing here may
be added to any other unit's module. P1 is *Energy transfers*: eight lessons,
TWELVE instrument families, no drawn figure, all DOM and inline SVG, no canvas
and no animation loop anywhere in the unit.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS FILE IS RESPONSIBLE FOR, AND WHAT IT IS NOT
═══════════════════════════════════════════════════════════════════════════

MARKUP ONLY, on C9's and C10's conventions and for their reasons.

  · EMIT-BOTH-SHOW-ONE wherever a panel has a small closed set of states. The
    equilibrium bench alone carries THIRTY-SIX authored-or-derived states and
    not one of them is composed in the browser.
  · NUMBERS ARE DERIVED, NEVER AUTHORED TWICE. The machine bench authors one
    multiplier per set-up and computes both forces, both distances and both
    products from it. The lagging bench authors one final temperature per cell
    and computes every drop and every comparison with the control.
  · ONLY THE LADDER MARKS. Every bench below gives its verdict in WORDS, and
    `_no_correct_flags` refuses a payload carrying a marking key.
  · Every family ticks a rail stop, so every family carries
    `data-stage-done="0"`. NOTHING IS TICKED ON LOAD (MRB-208).
  · Arrows are drawn as SVG by `t()`, never typed as U+2192. No P1 payload
    contains one; direction is carried by words and by a drawn chevron.
  · CONTAINMENT, NOT CLIPPING: every horizontally scrolling row below carries
    `position: relative` on the scroller itself, so an absolutely positioned
    child cannot widen the document on a phone.

═══════════════════════════════════════════════════════════════════════════
⚖️ RULED · A COMPARATIVE LABEL IS COMPUTED, AND ITS EQUAL STATE IS REACHABLE
═══════════════════════════════════════════════════════════════════════════

Two instruments here carry a label that compares two values — the equilibrium
bench ("which one is hotter") and the machine bench ("less force, further").
MRB-257 §5A.1 rules that such a label is DERIVED from the values and never
authored beside them, because an authored comparative ships a false statement
the moment the two values are equal.

Both derive it, and both have the equal state ON THE BENCH rather than as a
theoretical possibility:

  `equilibrium-bench`   the fourth pair starts at 40 and 40 and never moves,
                        so the equal branch is the FIRST FRAME of a reachable
                        state rather than the eighth step of a slider. Every
                        other pair also ends there.
  `machine-bench`       two of the nine set-ups have a multiplier of 1 — an
                        equal-armed lever and a single fixed pulley — so the
                        "this machine gives you nothing" branch is a real
                        machine a student can pick, not a guard clause.

⚠️ This is the alveoli defect exactly (audit 5A.4), and it is worth naming:
the state a load sweep never reaches is the state the literal fix gets wrong.

═══════════════════════════════════════════════════════════════════════════
⊖ `fifa-pick` IS NOT REGISTERED HERE, AND MUST NOT BE
═══════════════════════════════════════════════════════════════════════════

p1-03 and p1-08 both place `fifa-pick`, which MRB-204 part 4 requires of every
formula lesson. It is registered by `ks3_art/c2.py` and P1 uses it AS IT
STANDS: the payloads fit `r_fifa_pick` with no change to that module, so
nothing is edited and no family is registered twice.

Registering it again here would fail `ks3_art.load()`'s duplicate-family gate,
which is the correct outcome — one family, one owner. Generalising C2's
renderer instead would mean editing another lane's module, which
`docs/ks3/worktrees.md` §1 forbids outright and which the C9 ruling settled
for the same reason.

⚠️ THE COUPLING IS REAL AND IS RECORDED HERE SO IT IS VISIBLE FROM THE
PHYSICS SIDE. A change to `r_fifa_pick` changes two P1 pages. What P1 depends
on is exactly: two pick ladders, a numeric field with a units select whose
placeholder carries an empty value, an n-step reveal, and the `{answer}` /
`{unit}` close template. Nothing else.

═══════════════════════════════════════════════════════════════════════════
⊖ NO DRAWN FIGURE IN THE WHOLE UNIT, AND THAT IS A DECISION
═══════════════════════════════════════════════════════════════════════════

`ART` is empty. Every picture P1 could want is either an instrument the
student operates — which is a better version of the same drawing — or a
picture of a situation the words already carry. `docs/ks3/diagram-manifest.md`
gains no P1 rows, and every question in the bank is `figure=None`.

The two DRAWN relationships in the unit are the formula triangle and the
balance beam, and both belong to the engine (`r_cover_triangle`, `_BEAM` in
`build_ks3.py`) rather than to this file. They are Design's drawings, reached
through `r_formula`, and P1 authors payloads for them rather than redrawing
them.
"""

from ks3_art.kit import e, rich, t


# ═══ shared inside P1 ════════════════════════════════════════════════════

def _seg(cls, label, pressed=False, **attrs):
    """One segmented-control button. No `correct` key, ever, anywhere."""
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _counter_agrees(a, act_id, n, what):
    """The block-head counter's denominator must be the number of things.

    The denominator is a CLAIM about the instrument underneath it, and a
    wrong one is the shape of defect that renders perfectly: "3 of 6 read"
    over a bench with eight cells is a student who can never finish.
    """
    hc = a.get("head_counter") or {}
    total = hc.get("total")
    if total is not None and int(total) != int(n):
        raise ValueError(
            "%s: the block-head counter says %s of %s and the payload holds "
            "%d %s. The denominator is a claim about the instrument under it."
            % (act_id, "{n}", total, n, what))


def _no_correct_flags(rows, act_id, family):
    """Refuse a `correct` key on any commit option, anywhere in P1.

    Only the mastery ladder marks (MRB-208 / contract §1). Every bench in
    this unit gives its verdict in words, and a `correct` on an option would
    make the whole page read as a test — at which point committing before
    revealing stops being worth doing.
    """
    for row in rows:
        for opt in (row.get("options") or []):
            if isinstance(opt, dict) and ("correct" in opt or
                                          "correction" in opt):
                raise ValueError(
                    "%s %r: option %r carries a marking key. Nothing outside "
                    "the mastery ladder marks in P1 — every bench gives its "
                    "verdict in words."
                    % (family, act_id, opt.get("id") or opt.get("label")))


def _ranks_are_dense(rows, act_id, family, field="rank"):
    """Ranks are 0..n-1, no gap and no tie. ORDER IS DATA (the C5/C9 ruling).

    Three benches in this unit state an order they claim to have derived —
    the conduction race, the Leslie's cube and the lagging bench. A TIE is
    two rows the page cannot put in order while claiming to have done so; a
    GAP is an order with a hole in it that still sorts correctly, which is
    worse, because it looks right.
    """
    ranks = []
    for row in rows:
        if row.get(field) is None:
            raise ValueError(
                "%s %r: %r has no %r. ORDER IS DATA — the order is read off "
                "this field and never off the position of the row in the "
                "array, so a payload re-sorted for layout cannot silently "
                "re-teach the result."
                % (family, act_id, row.get("id") or row.get("name"), field))
        ranks.append(int(row[field]))
    if sorted(ranks) != list(range(len(ranks))):
        raise ValueError(
            "%s %r ranks its %d row(s) %s. Ranks are 0..n-1 with no gap and "
            "no tie." % (family, act_id, len(ranks), sorted(ranks)))
    return ranks


def _check_order_claim(a, act_id, family, ordered_ids):
    """The closing sentence names the order. It must be the derived one."""
    claim = a.get("order_claim")
    if claim is None:
        return
    if list(claim) != list(ordered_ids):
        raise ValueError(
            "%s %r states the order %s and its own data gives %s. That "
            "sentence is the conclusion of the whole bench, and a panel that "
            "contradicts the cells above it is the page arguing with itself "
            "in front of the student."
            % (family, act_id, list(claim), list(ordered_ids)))


def _close_panel(a, cls, hook):
    """The payoff panel: an optional title, then paragraphs. Emitted hidden."""
    paras = a.get("close") or []
    if not paras:
        return ""
    title = (('<p class="%s-closetitle">%s</p>' % (cls, t(a["close_title"])))
             if a.get("close_title") else "")
    return ('<div class="%s-close" hidden %s>%s%s</div>'
            % (cls, hook, title,
               "".join("<p>%s</p>" % rich(p) for p in paras)))


def _num(v, dp=0):
    """A number formatted for a readout, with no trailing `.0` at dp=0."""
    if dp <= 0:
        return "%d" % int(round(float(v)))
    return ("%." + str(dp) + "f") % float(v)


def _need(a, act_id, keys, family):
    missing = [k for k in keys if not a.get(k)]
    if missing:
        raise ValueError(
            "%s %r has no %s." % (family, act_id, ", ".join(repr(k)
                                                           for k in missing)))


# ═══ p1-01 · store-audit ═════════════════════════════════════════════════

def r_store_audit(a, act_id):
    """⊕ p1-01 `#s-stores` — five store cards, opened one at a time.

    A REFERENCE instrument, not a sorter: the student is reading, and the
    next block is where they decide. Five tabs, five panels, one shown, and
    the head counter records how many have been opened.

    ⚖️ **EVERY CARD CARRIES `belongs`, AND IT IS THE ONE LINE THAT MATTERS
    MOST.** A store is a property of a SITUATION, and the gravitational card
    is the only place in the key stage that says so before p1-02 needs it.
    Without that line `ENER-10` has nowhere to have come from and nothing to
    be corrected against.

    HOOKS: `data-saud` (wrapper, `data-total`) · `data-saud-tab` (valued by
    store id) · `data-saud-panel` · `data-saud-rest` · `data-saud-close`.
    """
    stores = a.get("stores") or []
    if len(stores) < 3:
        raise ValueError(
            "store-audit %r has %d store(s). The block is a set held against "
            "each other and a set of two is a comparison, which is a "
            "different block." % (act_id, len(stores)))
    for s in stores:
        for key in ("id", "name", "sub", "belongs", "fills", "empties",
                    "example", "watch"):
            if not s.get(key):
                raise ValueError(
                    "store-audit %r card %r has no %r. Every card answers "
                    "the same six questions; a card missing one is a hole a "
                    "student meets only after opening it."
                    % (act_id, s.get("id"), key))
    ids = [s["id"] for s in stores]
    if len(set(ids)) != len(ids):
        raise ValueError("store-audit %r repeats a store id." % act_id)
    _counter_agrees(a, act_id, len(stores), "store(s)")

    tabs = "".join(
        _seg("ks3-saud-tab", s["name"], data_saud_tab=s["id"])
        for s in stores)

    panels = "".join(
        '<div class="ks3-saud-panel" data-saud-panel="%s" hidden>'
        '<p class="ks3-saud-name">%s<span class="ks3-saud-sub">%s</span></p>'
        '<dl class="ks3-saud-lines">'
        '<div class="ks3-saud-line"><dt>Fills when</dt><dd>%s</dd></div>'
        '<div class="ks3-saud-line"><dt>Empties when</dt><dd>%s</dd></div>'
        '<div class="ks3-saud-line"><dt>Belongs to</dt><dd>%s</dd></div>'
        '</dl>'
        '<p class="ks3-saud-example">%s</p>'
        '<p class="ks3-saud-watch">%s</p></div>'
        % (e(s["id"]), t(s["name"]), t(s["sub"]), t(s["fills"]),
           t(s["empties"]), t(s["belongs"]), rich(s["example"]),
           rich(s["watch"]))
        for s in stores)

    return ('<div class="ks3-saud" data-saud data-total="%d">'
            '<div class="ks3-saud-tabs">%s</div>'
            '<div class="ks3-saud-body">'
            '<p class="ks3-saud-rest" data-saud-rest>%s</p>%s</div>%s</div>'
            % (len(stores), tabs,
               t(a.get("resting") or "Pick a store to open it."),
               panels, _close_panel(a, "ks3-saud", "data-saud-close")))


# ═══ p1-01 · store-or-pathway ════════════════════════════════════════════

def r_store_or_pathway(a, act_id):
    """⊕ p1-01 `#s-sort` — the CLASSIFY sort, with MRB-196 R10's self-check.

    Eight items, two bins, one chip pressed per row. NOTHING on any chip is
    green, red, or marked in any way: the sorter reveals the reasons when
    every row has been sorted and then asks the student how many of their own
    judgements matched. Only the student knows, which is exactly why the
    self-check carries no answer key — `_self_check` in `ks3_art/kit.py`
    raises if one is authored.

    ⚖️ **THE `why` LINE IS EMITTED FOR EVERY ITEM AND REVEALED FOR ALL OF
    THEM AT ONCE.** Revealing per row would make the eighth chip a formality
    and would put a verdict beside a choice, which is a mark in everything
    but colour.

    HOOKS: `data-spath` (wrapper, `data-total`) · `data-spath-row` ·
    `data-spath-chip` (valued `item:bin`) · `data-spath-why` ·
    `data-spath-progress` · `data-spath-close`.
    """
    bins = a.get("bins") or []
    items = a.get("items") or []
    if len(bins) != 2:
        raise ValueError(
            "store-or-pathway %r declares %d bin(s); the discrimination is "
            "between two." % (act_id, len(bins)))
    bin_ids = [b["id"] for b in bins]
    if len(set(bin_ids)) != 2:
        raise ValueError("store-or-pathway %r repeats a bin id." % act_id)
    if len(items) < 4:
        raise ValueError(
            "store-or-pathway %r sorts %d item(s). Fewer than four cannot "
            "show a pattern." % (act_id, len(items)))

    seen = set()
    for it in items:
        for key in ("id", "label", "bin", "why"):
            if not it.get(key):
                raise ValueError(
                    "store-or-pathway %r item %r has no %r."
                    % (act_id, it.get("id") or it.get("label"), key))
        if it["bin"] not in bin_ids:
            raise ValueError(
                "store-or-pathway %r puts %r in bin %r, which is not one of "
                "%s." % (act_id, it["id"], it["bin"], bin_ids))
        if it["id"] in seen:
            raise ValueError(
                "store-or-pathway %r repeats item id %r." % (act_id, it["id"]))
        seen.add(it["id"])

    # ⚖️ NEITHER BIN MAY BE EMPTY, AND NEITHER MAY HOLD EVERYTHING BUT ONE.
    # A sort whose answer is "nearly all of them go left" is a sort a student
    # can pass by pressing left, which is MRB-278's property applied to a
    # corpus MRB-278 does not reach.
    per_bin = {}
    for it in items:
        per_bin.setdefault(it["bin"], []).append(it["id"])
    for b in bin_ids:
        n = len(per_bin.get(b, []))
        if n == 0:
            raise ValueError(
                "store-or-pathway %r has an empty bin (%r). A bin nothing "
                "goes in is a heading over nothing." % (act_id, b))
        if n * 4 < len(items):
            raise ValueError(
                "store-or-pathway %r puts only %d of %d items in bin %r. A "
                "sort a student can pass by pressing one chip every time is "
                "not a sort." % (act_id, n, len(items), b))
    _counter_agrees(a, act_id, len(items), "item(s)")

    heads = "".join('<span class="ks3-spath-binhead">%s'
                    '<span class="ks3-spath-gloss">%s</span></span>'
                    % (t(b.get("label", "")), t(b.get("gloss", "")))
                    for b in bins)

    rows = []
    for it in items:
        chips = "".join(
            '<button type="button" class="ks3-spath-chip" '
            'data-spath-chip="%s" data-row="%s" aria-pressed="false">%s'
            '</button>'
            % (e("%s:%s" % (it["id"], b["id"])), e(it["id"]),
               t(b.get("label", "")))
            for b in bins)
        rows.append(
            '<li class="ks3-spath-row" data-spath-row="%s" data-sorted="0">'
            '<span class="ks3-spath-item">%s</span>'
            '<span class="ks3-spath-chips">%s</span>'
            '<p class="ks3-spath-why" data-spath-why="%s" hidden>%s</p></li>'
            % (e(it["id"]), t(it["label"]), chips, e(it["id"]),
               rich(it["why"])))

    from ks3_art.kit import _self_check
    return ('<div class="ks3-spath" data-spath data-total="%d">'
            '<div class="ks3-spath-heads" aria-hidden="true">'
            '<span class="ks3-spath-item"></span>%s</div>'
            '<ul class="ks3-spath-rows" role="list">%s</ul>'
            '<p class="ks3-spath-progress" data-spath-progress>%s</p>'
            '%s%s</div>'
            % (len(items), heads, "".join(rows),
               # ⚖️ NOT A COUNT. The block head already counts, and two
               # readouts of one number is two sources for one fact. This
               # line says what finishing buys, and the wiring replaces it
               # with the announcement when it has been earned.
               t(a.get("sorting_hint")
                 or "Sort every row, and the reasons open underneath."),
               _self_check(a, act_id),
               _close_panel(a, "ks3-spath", "data-spath-close")))


# ═══ p1-02 · before-after-bench ══════════════════════════════════════════

def r_before_after_bench(a, act_id):
    """⊕ p1-02 `#s-ba` — six changes, a BEFORE column and an AFTER column.

    `KS3.P.ECT.03`'s own six processes, in the bullet's own order. One
    commitment per change — which store empties — then the account opens.

    ⚖️ **THERE IS NO MIDDLE COLUMN, AND THAT IS THE DESIGN.** `KS3.P.CIS.02`
    asks for the starting conditions compared with the final conditions and
    nothing else. The story of what happened in between is where "the energy
    turns into" gets in, and this block has nowhere to put one.

    ⚖️ **`down` AND `up` MUST NAME DECLARED STORES AND MUST DIFFER.** A change
    whose store went down and up is not a change; a change naming a store the
    chip row does not offer is a commitment the student cannot make.

    HOOKS: `data-baben` (wrapper, `data-total`) · `data-baben-tab` ·
    `data-baben-panel` · `data-baben-opt` (valued `change:store`) ·
    `data-baben-out` · `data-baben-rest` · `data-baben-close`.
    """
    from ks3_art.kit import r_bench_gate
    changes = a.get("changes") or []
    stores = a.get("stores") or []
    if len(changes) < 3:
        raise ValueError(
            "before-after-bench %r has %d change(s)." % (act_id, len(changes)))
    store_ids = [s["id"] for s in stores]
    if len(set(store_ids)) != len(store_ids) or len(store_ids) < 3:
        raise ValueError(
            "before-after-bench %r offers %d store chip(s), repeated or too "
            "few." % (act_id, len(store_ids)))

    seen = set()
    for c in changes:
        for key in ("id", "label", "scene", "before", "after", "down", "up",
                    "by", "note"):
            if not c.get(key):
                raise ValueError(
                    "before-after-bench %r change %r has no %r."
                    % (act_id, c.get("id"), key))
        if c["id"] in seen:
            raise ValueError(
                "before-after-bench %r repeats change id %r."
                % (act_id, c["id"]))
        seen.add(c["id"])
        for slot in ("down", "up"):
            if c[slot] not in store_ids:
                raise ValueError(
                    "before-after-bench %r change %r names %r as the store "
                    "that went %s, and the chip row offers %s. A student "
                    "cannot commit to a store that is not on the bench."
                    % (act_id, c["id"], c[slot], slot, store_ids))
        if c["down"] == c["up"]:
            raise ValueError(
                "before-after-bench %r change %r has the same store going "
                "down and up. That is not a transfer."
                % (act_id, c["id"]))
    _counter_agrees(a, act_id, len(changes), "change(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "before-after-bench")

    lab = a.get("labels") or {}
    by_id = dict((s["id"], s.get("label", s["id"])) for s in stores)

    tabs = "".join(_seg("ks3-baben-tab", c["label"], data_baben_tab=c["id"])
                   for c in changes)

    panels, outs = [], []
    for c in changes:
        chips = "".join(
            '<button type="button" class="ks3-seg-btn ks3-baben-opt" '
            'data-baben-opt="%s" data-change="%s" aria-pressed="false">%s'
            '</button>'
            % (e("%s:%s" % (c["id"], s["id"])), e(c["id"]),
               t(s.get("label", "")))
            for s in stores)
        panels.append(
            '<div class="ks3-baben-panel" data-baben-panel="%s" hidden>'
            '<p class="ks3-baben-scene">%s</p>'
            '<div class="ks3-baben-two">'
            '<div class="ks3-baben-half"><p class="ks3-baben-tag">%s</p>'
            '<p>%s</p></div>'
            '<div class="ks3-baben-half"><p class="ks3-baben-tag">%s</p>'
            '<p>%s</p></div></div>'
            '<p class="ks3-baben-commit">%s</p>'
            '<div class="ks3-baben-chips">%s</div></div>'
            % (e(c["id"]), t(c["scene"]),
               t(lab.get("before", "BEFORE")), t(c["before"]),
               t(lab.get("after", "AFTER")), t(c["after"]),
               t(a.get("commit_prompt") or "Which store empties?"), chips))
        # ⚖️ The account is a THIRD panel, shown only after the commitment,
        # and it is composed here so nothing about it is built in the browser.
        outs.append(
            '<div class="ks3-baben-out" data-baben-out="%s" hidden>'
            '<dl class="ks3-baben-acct">'
            '<div class="ks3-baben-acctrow"><dt>%s</dt><dd>%s</dd></div>'
            '<div class="ks3-baben-acctrow"><dt>%s</dt><dd>%s</dd></div>'
            '<div class="ks3-baben-acctrow"><dt>%s</dt><dd>%s</dd></div>'
            '</dl><p class="ks3-baben-note">%s</p></div>'
            % (e(c["id"]),
               t(lab.get("down", "The store that emptied")),
               t(by_id[c["down"]]),
               t(lab.get("up", "The store that filled")), t(by_id[c["up"]]),
               t(lab.get("by", "Carried by")), t(c["by"]),
               rich(c["note"])))

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-baben" data-baben data-total="%d"%s>'
            '<div class="ks3-baben-tabs">%s</div>'
            '<div class="ks3-baben-body">'
            '<p class="ks3-baben-rest" data-baben-rest>%s</p>%s%s</div>%s</div>'
            % (gate_html, len(changes), body_attr, tabs,
               t(a.get("resting") or "Pick a change to read it."),
               "".join(panels), "".join(outs),
               _close_panel(a, "ks3-baben", "data-baben-close")))


# ═══ p1-03 · energy-audit ════════════════════════════════════════════════

def r_energy_audit(a, act_id):
    """⊕ p1-03 `#s-count` — five machines, one hundred joules each.

    ⚖️ **THE WASTE FIGURE IS DERIVED AND IS NEVER AUTHORED.** Each machine
    authors one number — how much of the hundred did the job — and everything
    else on the readout comes out of it: the waste, the total, the two bar
    widths and the percentage. The lesson is that the two columns add to the
    whole, and a payload that authored both halves could put a row on the
    page whose halves did not.

    ⚖️ **AND THE BAR IS DRAWN FROM THE SAME TWO NUMBERS.** Its two segments
    are `useful` and `total - useful` as percentages of the bar's width, so a
    bar that looked wrong would be a bar whose numbers were wrong. A flex row
    would make the two segments whatever the container allowed, which is a
    bar model that lies — the same ruling as `r_cover_bar`'s.

    HOOKS: `data-eaud` (wrapper, `data-total`) · `data-eaud-tab` ·
    `data-eaud-guess` (valued `machine:index`) · `data-eaud-out` ·
    `data-eaud-rest` · `data-eaud-close`.
    """
    from ks3_art.kit import r_bench_gate
    machines = a.get("machines") or []
    total_in = a.get("total_in")
    guesses = a.get("guesses") or []
    if not machines:
        raise ValueError("energy-audit %r has no machines[]." % act_id)
    if not isinstance(total_in, (int, float)) or total_in <= 0:
        raise ValueError(
            "energy-audit %r has no positive `total_in`. Every row is a "
            "split of the same total and there is nothing to split without "
            "one." % act_id)
    if len(guesses) < 3:
        raise ValueError(
            "energy-audit %r offers %d guess(es); the commitment needs a "
            "real choice." % (act_id, len(guesses)))

    seen = set()
    for m in machines:
        for key in ("id", "name", "job", "note"):
            if not m.get(key):
                raise ValueError(
                    "energy-audit %r machine %r has no %r."
                    % (act_id, m.get("id"), key))
        if m["id"] in seen:
            raise ValueError(
                "energy-audit %r repeats machine id %r." % (act_id, m["id"]))
        seen.add(m["id"])
        u = m.get("useful")
        if not isinstance(u, (int, float)) or not 0 < u < total_in:
            raise ValueError(
                "energy-audit %r machine %r does %r of %r joules of useful "
                "work. It has to be more than none and less than all of it: "
                "a machine that wastes nothing does not exist and a machine "
                "that does nothing is not on this bench."
                % (act_id, m["id"], u, total_in))
    _counter_agrees(a, act_id, len(machines), "machine(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "energy-audit")

    lab = a.get("labels") or {}
    unit = a.get("unit") or "J"
    tabs = "".join(_seg("ks3-eaud-tab", m["name"], data_eaud_tab=m["id"])
                   for m in machines)
    picks = "".join(
        '<button type="button" class="ks3-seg-btn ks3-eaud-guess" '
        'data-eaud-guess="%d" aria-pressed="false">%s</button>'
        % (i, t(g)) for i, g in enumerate(guesses))

    outs = []
    for m in machines:
        useful = float(m["useful"])
        waste = float(total_in) - useful
        pct = 100.0 * useful / float(total_in)
        outs.append(
            '<div class="ks3-eaud-out" data-eaud-out="%s" '
            'data-useful="%s" data-waste="%s" hidden>'
            '<p class="ks3-eaud-name">%s</p>'
            '<dl class="ks3-eaud-tiles">'
            '<div class="ks3-eaud-tile"><dt>%s</dt><dd>%s %s</dd></div>'
            '<div class="ks3-eaud-tile"><dt>%s</dt><dd>%s %s</dd></div>'
            '<div class="ks3-eaud-tile"><dt>%s</dt><dd>%s %s</dd></div>'
            '<div class="ks3-eaud-tile"><dt>%s</dt><dd>%s %s</dd></div>'
            '</dl>'
            '<div class="ks3-eaud-bar" role="img" aria-label="%s">'
            '<span class="ks3-eaud-seg ks3-eaud-useful" style="width:%.2f%%">'
            '</span>'
            '<span class="ks3-eaud-seg ks3-eaud-waste" style="width:%.2f%%">'
            '</span></div>'
            '<p class="ks3-eaud-split">%s</p>'
            '<p class="ks3-eaud-note">%s</p></div>'
            % (e(m["id"]), e(_num(useful)), e(_num(waste)), t(m["name"]),
               t(lab.get("in", "Given to it")), _num(total_in), t(unit),
               t(lab.get("useful", "Did the job")), _num(useful), t(unit),
               t(lab.get("waste", "Warmed the surroundings")), _num(waste),
               t(unit),
               t(lab.get("total", "Total out")), _num(useful + waste), t(unit),
               e("A bar of %s joules, split into %s that did the job and %s "
                 "that warmed the surroundings."
                 % (_num(total_in), _num(useful), _num(waste))),
               pct, 100.0 - pct,
               # ⚖️ DERIVED, and it is the sentence the whole bench exists
               # for: the two parts are printed adding up to the whole, in
               # the same numbers the tiles above already show.
               t("%s joules into %s, %s joules warming the surroundings. "
                 "%s plus %s is %s."
                 % (_num(useful), m["job"], _num(waste), _num(useful),
                    _num(waste), _num(useful + waste))),
               rich(m["note"])))

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-eaud" data-eaud data-total="%d"%s>'
            '<div class="ks3-eaud-tabs">%s</div>'
            '<div class="ks3-eaud-guesses" data-eaud-guessrow hidden>'
            '<p class="ks3-eaud-commit">%s</p>'
            '<div class="ks3-eaud-picks">%s</div></div>'
            '<div class="ks3-eaud-body">'
            '<p class="ks3-eaud-rest" data-eaud-rest>%s</p>%s</div>%s</div>'
            % (gate_html, len(machines), body_attr, tabs,
               t("How much of the hundred does the job?"), picks,
               t(a.get("resting") or "Pick a machine to read it."),
               "".join(outs),
               _close_panel(a, "ks3-eaud", "data-eaud-close")))


# ═══ p1-03 · mechanism-or-energy ═════════════════════════════════════════

def r_mechanism_or_energy(a, act_id):
    """⊕ p1-03 `#s-why` — `KS3.P.CIS.03`, made into a decision.

    Five questions, each with two true answers offered: an energy account and
    a mechanism. The student picks which one answers THAT question.

    ⚖️ **THE ANSWER IS NOT ALWAYS THE MECHANISM, AND THE RENDERER ENFORCES
    IT.** A block whose answer is the same every time is a block a student
    passes without reading — MRB-278's property, applied to a corpus the gate
    itself cannot see because these options are not a marked ladder. So the
    check is made here, at build time: neither tool may answer fewer than a
    quarter of the cases.

    ⚖️ **NOTHING MARKS.** `answers` decides which tool the NOTE argues for; it
    never becomes a `data-correct`, never colours a button and never disables
    one. The note is the teaching and it concedes in its first clause that
    both answers are true.

    HOOKS: `data-mech` (wrapper, `data-total`) · `data-mech-tab` ·
    `data-mech-panel` · `data-mech-opt` (valued `case:tool`) ·
    `data-mech-out` · `data-mech-rest` · `data-mech-close`.
    """
    cases = a.get("cases") or []
    tools = a.get("tools") or []
    if len(tools) != 2:
        raise ValueError(
            "mechanism-or-energy %r declares %d tool(s); the choice is "
            "between two." % (act_id, len(tools)))
    tool_ids = [x["id"] for x in tools]
    if len(set(tool_ids)) != 2:
        raise ValueError("mechanism-or-energy %r repeats a tool id." % act_id)
    if len(cases) < 4:
        raise ValueError(
            "mechanism-or-energy %r has %d case(s)." % (act_id, len(cases)))

    seen, tally = set(), {}
    for c in cases:
        for key in ("id", "question", "account", "mechanism", "answers",
                    "note"):
            if not c.get(key):
                raise ValueError(
                    "mechanism-or-energy %r case %r has no %r."
                    % (act_id, c.get("id"), key))
        if c["id"] in seen:
            raise ValueError(
                "mechanism-or-energy %r repeats case id %r."
                % (act_id, c["id"]))
        seen.add(c["id"])
        if c["answers"] not in tool_ids:
            raise ValueError(
                "mechanism-or-energy %r case %r is answered by %r, which is "
                "not one of %s." % (act_id, c["id"], c["answers"], tool_ids))
        tally[c["answers"]] = tally.get(c["answers"], 0) + 1

    for tid in tool_ids:
        n = tally.get(tid, 0)
        if n * 4 < len(cases):
            raise ValueError(
                "mechanism-or-energy %r: only %d of %d cases are answered by "
                "%r. A block whose answer is nearly always the same tool is "
                "one a student gets right without reading the question, and "
                "the whole point is the discrimination."
                % (act_id, n, len(cases), tid))
    _counter_agrees(a, act_id, len(cases), "case(s)")

    tabs = "".join(
        _seg("ks3-mech-tab", "Q%d" % (i + 1), data_mech_tab=c["id"])
        for i, c in enumerate(cases))

    panels, outs = [], []
    for c in cases:
        opts = "".join(
            '<button type="button" class="ks3-mech-opt" data-mech-opt="%s" '
            'data-case="%s" aria-pressed="false">'
            '<span class="ks3-mech-tool">%s</span>'
            '<span class="ks3-mech-claim">%s</span></button>'
            % (e("%s:%s" % (c["id"], x["id"])), e(c["id"]),
               t(x.get("label", "")), t(c[x["id"]]))
            for x in tools)
        panels.append(
            '<div class="ks3-mech-panel" data-mech-panel="%s" hidden>'
            '<p class="ks3-mech-q">%s</p>'
            '<div class="ks3-mech-opts">%s</div></div>'
            % (e(c["id"]), t(c["question"]), opts))
        outs.append(
            '<div class="ks3-mech-out" data-mech-out="%s" hidden>%s</div>'
            % (e(c["id"]), "<p>%s</p>" % rich(c["note"])))

    return ('<div class="ks3-mech" data-mech data-total="%d">'
            '<div class="ks3-mech-tabs">%s</div>'
            '<div class="ks3-mech-body">'
            '<p class="ks3-mech-rest" data-mech-rest>%s</p>%s%s</div>%s</div>'
            % (len(cases), tabs,
               t(a.get("resting") or "Pick a question to open it."),
               "".join(panels), "".join(outs),
               _close_panel(a, "ks3-mech", "data-mech-close")))


# ═══ p1-04 · equilibrium-bench ═══════════════════════════════════════════

# Each step closes this fraction of whatever gap is left. Fast at the start
# and slow at the end, which is what a real cooling curve does and what the
# lesson's own argument predicts: the transfer runs on the gap and spends the
# gap as it runs.
# ⚠️ 0.60 AND NOT LESS, AND THE FIGURE IS LOAD-BEARING. Eight steps have
# to leave a gap that rounds to 0.0 at the bench's own one-decimal
# resolution, or the last frame of every run reads a difference under a
# lesson that says it settles. At 0.40 the widest pair finished 1.0
# degrees apart; at 0.60 it finishes 0.04 apart, which prints as 0.0.
_EQUIL_CLOSE = 0.60


def _equil_states(pair, steps):
    """Every (step -> left, right, gap) for one pair. Computed ONCE, here.

    Two identical blocks, so the finishing temperature is the plain mean.
    Specific heat capacity is KS4 and is not needed to make this point;
    unequal blocks would need it and would put a number on the page that
    nothing in this lesson can justify.
    """
    left0, right0 = float(pair["left"]), float(pair["right"])
    mid = (left0 + right0) / 2.0
    out = []
    for k in range(steps + 1):
        f = (1.0 - _EQUIL_CLOSE) ** k
        # ⚖️ THE GAP IS DERIVED FROM THE ROUNDED READOUTS, NOT FROM THE
        # UNROUNDED ONES. Both blocks print to one decimal, and a gap
        # computed behind that resolution disagrees with them: at step 7
        # of the wide pair both blocks read 50.0 and the true gap is
        # 0.098, which printed as a gap of 0.1 beside two identical
        # numbers. Deriving it from what is actually on screen makes the
        # two agree at every step of every pair by construction.
        left = round(mid + (left0 - mid) * f, 1)
        right = round(mid + (right0 - mid) * f, 1)
        out.append((k, left, right, round(abs(left - right), 1)))
    return out


def r_equilibrium_bench(a, act_id):
    """⊕ p1-04 `#s-equil` — two identical blocks, four pairs, eight steps.

    ⚖️ **THE COMPARATIVE LABEL IS COMPUTED FROM THE TWO TEMPERATURES, AT
    EVERY ONE OF THE THIRTY-SIX STATES.** MRB-257 §5A.1: an authored
    comparative is a second source for a fact the numbers already carry, and
    the two drift the moment a state is added. Here the drift would be worse
    than usual, because the state the bench ENDS in is the equal one — an
    authored "the left one is hotter" would be false on the last frame of
    every single run.

    Three branches, and all three are reachable:

        left hotter   ->  energy goes left to right
        right hotter  ->  energy goes right to left
        equal         ->  nothing either way, and it has stopped

    ⚠️ **THE EQUAL BRANCH IS DRIVEN FROM TWO DIRECTIONS IN REVIEW**: as the
    last step of any pair that starts apart, and as the FIRST FRAME of the
    fourth pair, which starts at 40 and 40 and never moves. A branch that can
    only be reached after eight drags of a slider is a branch nobody tested.

    ⚖️ **AND THE GAP IS DERIVED TOO.** It is the difference of the two
    readouts, computed in the same expression that produced them, so a gap of
    zero and a sentence saying "the same temperature" cannot disagree.

    HOOKS: `data-equil` (wrapper, `data-total`) · `data-equil-pair` ·
    `data-equil-time` (range) · `data-equil-state` (valued `pair:step`) ·
    `data-equil-note` · `data-equil-close`.
    """
    from ks3_art.kit import r_bench_gate
    pairs = a.get("pairs") or []
    steps = int(a.get("time_steps") or 0)
    if len(pairs) < 2:
        raise ValueError(
            "equilibrium-bench %r has %d pair(s)." % (act_id, len(pairs)))
    if steps < 2:
        raise ValueError(
            "equilibrium-bench %r runs %d step(s); the settling has to be "
            "watchable." % (act_id, steps))

    seen, has_equal = set(), False
    for p in pairs:
        for key in ("id", "label", "note"):
            if not p.get(key):
                raise ValueError(
                    "equilibrium-bench %r pair %r has no %r."
                    % (act_id, p.get("id"), key))
        for key in ("left", "right"):
            if not isinstance(p.get(key), (int, float)):
                raise ValueError(
                    "equilibrium-bench %r pair %r has no numeric %r."
                    % (act_id, p["id"], key))
        if p["id"] in seen:
            raise ValueError(
                "equilibrium-bench %r repeats pair id %r." % (act_id, p["id"]))
        seen.add(p["id"])
        if float(p["left"]) == float(p["right"]):
            has_equal = True

    # ⚖️ THE EQUAL PAIR IS REQUIRED, NOT OPTIONAL. Without one the third
    # branch of the derived label is only ever reached at the end of a slider
    # drag, and a branch reached only at the end of a drag is a branch that
    # ships untested. It is also the state that teaches the rule: no gap, no
    # transfer, whatever the two temperatures actually are.
    if not has_equal:
        raise ValueError(
            "equilibrium-bench %r has no pair that starts equal. The equal "
            "state is where every run ENDS and is the state the lesson is "
            "about; a bench that can only arrive at it after eight steps "
            "never shows a student what it looks like from the start."
            % act_id)
    _counter_agrees(a, act_id, len(pairs), "pair(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "equilibrium-bench")

    lab = a.get("labels") or {}
    bl = a.get("block_labels") or {}
    unit = lab.get("unit", "°C")
    left_name = bl.get("left", "Block A")
    right_name = bl.get("right", "Block B")

    picks = "".join(_seg("ks3-equil-pair", p["label"], data_equil_pair=p["id"])
                    for p in pairs)

    states = []
    for p in pairs:
        for k, left, right, gap in _equil_states(p, steps):
            # ⚖️ THE SENTENCE, DERIVED. Three branches, in the same expression
            # that produced the two numbers above it.
            if gap == 0.0:
                direction, sentence = "none", (
                    "Both at %s %s. There is no difference between them, so "
                    "nothing is going either way and nothing will."
                    % (_num(left, 1), unit))
            elif left > right:
                direction, sentence = "lr", (
                    "%s is the hotter one, by %s %s. Energy is going from %s "
                    "to %s." % (left_name, _num(gap, 1), unit, left_name,
                                right_name))
            else:
                direction, sentence = "rl", (
                    "%s is the hotter one, by %s %s. Energy is going from %s "
                    "to %s." % (right_name, _num(gap, 1), unit, right_name,
                                left_name))
            states.append(
                '<div class="ks3-equil-state" data-equil-state="%s" '
                'data-dir="%s" data-gap="%s" hidden>'
                '<div class="ks3-equil-blocks">'
                '<div class="ks3-equil-block"><p class="ks3-equil-bname">%s</p>'
                '<p class="ks3-equil-temp">%s <span>%s</span></p></div>'
                '<div class="ks3-equil-arrow" data-dir="%s" aria-hidden="true">'
                '</div>'
                '<div class="ks3-equil-block"><p class="ks3-equil-bname">%s</p>'
                '<p class="ks3-equil-temp">%s <span>%s</span></p></div></div>'
                '<p class="ks3-equil-gap">%s: <strong>%s %s</strong></p>'
                '<p class="ks3-equil-says">%s</p></div>'
                % (e("%s:%d" % (p["id"], k)), e(direction), e(_num(gap, 1)),
                   t(left_name), _num(left, 1), t(unit),
                   e(direction),
                   t(right_name), _num(right, 1), t(unit),
                   t(lab.get("gap", "The gap between them")), _num(gap, 1),
                   t(unit), t(sentence)))

    notes = "".join(
        '<p class="ks3-equil-note" data-equil-note="%s" hidden>%s</p>'
        % (e(p["id"]), rich(p["note"])) for p in pairs)

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-equil" data-equil data-total="%d" '
            'data-steps="%d"%s>'
            '<div class="ks3-equil-pairs">%s</div>'
            '<div class="ks3-equil-stage">%s</div>'
            '<div class="ks3-equil-timerow">'
            '<label class="ks3-equil-timelabel" for="%s">%s</label>'
            '<input class="ks3-equil-time" id="%s" type="range" min="0" '
            'max="%d" step="1" value="0" data-equil-time disabled>'
            '<span class="ks3-equil-clock" data-equil-clock>0 %s</span></div>'
            '%s%s</div>'
            % (gate_html, len(pairs), steps, body_attr, picks,
               "".join(states),
               e("%s-time" % act_id), t(lab.get("time", "Time")),
               e("%s-time" % act_id), steps, t(a.get("time_unit") or "min"),
               notes, _close_panel(a, "ks3-equil", "data-equil-close")))


# ═══ p1-05 · conduction-race ═════════════════════════════════════════════

def r_conduction_race(a, act_id):
    """⊕ p1-05 `#s-race` — five rods, four wax blobs each, sixty seconds.

    ⚖️ **THE ORDER IS DERIVED FROM `rank` AND CHECKED AGAINST THE TIMES.**
    C9's ruling, and this is where it earns its keep: the closing panel states
    a conductivity order, and that sentence is the conclusion of the bench. A
    rod ranked above another whose blobs fell later or fewer would have the
    page contradict itself in front of the student, and both halves would
    render perfectly.

    So two assertions, both ways:
      · ranks are dense, 0..n-1, no tie and no gap;
      · a rod ranked better must drop at least as many blobs, and must drop
        each shared blob at least as early.

    ⚖️ **A `None` TIME IS A BLOB THAT DID NOT FALL, AND IT IS DATA.** The wood
    rod drops none, and that row is the most important on the bench. It is
    rendered as the authored `still` label rather than as a blank cell,
    because a blank cell reads as a measurement nobody took.

    HOOKS: `data-crace` (wrapper, `data-total`) · `data-crace-rod` ·
    `data-crace-run` · `data-crace-out` · `data-crace-rest` ·
    `data-crace-close`.
    """
    from ks3_art.kit import r_bench_gate
    rods = a.get("rods") or []
    positions = a.get("blob_positions") or []
    if len(rods) < 3:
        raise ValueError(
            "conduction-race %r has %d rod(s)." % (act_id, len(rods)))
    if len(positions) < 2:
        raise ValueError(
            "conduction-race %r marks %d position(s); one blob measures a "
            "yes or no rather than a rate." % (act_id, len(positions)))
    if list(positions) != sorted(positions):
        raise ValueError(
            "conduction-race %r lists its blob positions %s out of order. "
            "They are distances along one rod." % (act_id, list(positions)))

    seen = set()
    for r in rods:
        for key in ("id", "name", "note"):
            if not r.get(key):
                raise ValueError(
                    "conduction-race %r rod %r has no %r."
                    % (act_id, r.get("id"), key))
        if r["id"] in seen:
            raise ValueError(
                "conduction-race %r repeats rod id %r." % (act_id, r["id"]))
        seen.add(r["id"])
        times = r.get("times")
        if not isinstance(times, (list, tuple)) or len(times) != len(positions):
            raise ValueError(
                "conduction-race %r rod %r gives %r times for %d blob "
                "positions. Every rod is marked the same way or the rods are "
                "not comparable."
                % (act_id, r["id"], times, len(positions)))
        prev = None
        fell_after_gap = False
        for i, tm in enumerate(times):
            if tm is None:
                fell_after_gap = True
                continue
            if fell_after_gap:
                raise ValueError(
                    "conduction-race %r rod %r has blob %d falling after an "
                    "earlier blob did not. The blobs are in order along the "
                    "rod, so a nearer one cannot survive a further one."
                    % (act_id, r["id"], i + 1))
            if a.get("duration") and tm > a["duration"]:
                raise ValueError(
                    "conduction-race %r rod %r drops blob %d at %s s, after "
                    "the run ends at %s s."
                    % (act_id, r["id"], i + 1, tm, a["duration"]))
            if prev is not None and tm <= prev:
                raise ValueError(
                    "conduction-race %r rod %r drops blob %d at %s s, no "
                    "later than the one before it. The vibration reaches the "
                    "near blob first."
                    % (act_id, r["id"], i + 1, tm))
            prev = tm

    _ranks_are_dense(rods, act_id, "conduction-race")
    ordered = sorted(rods, key=lambda r: int(r["rank"]))

    # ⚖️ THE RANKING IS CHECKED AGAINST THE CELLS, EVERY ADJACENT PAIR.
    for better, worse in zip(ordered, ordered[1:]):
        nb = sum(1 for x in better["times"] if x is not None)
        nw = sum(1 for x in worse["times"] if x is not None)
        if nb < nw:
            raise ValueError(
                "conduction-race %r ranks %r above %r and %r dropped %d "
                "blobs against %r's %d. The rank is a claim about these "
                "readings."
                % (act_id, better["id"], worse["id"], better["id"], nb,
                   worse["id"], nw))
        for i, (tb, tw) in enumerate(zip(better["times"], worse["times"])):
            if tb is not None and tw is not None and tb > tw:
                raise ValueError(
                    "conduction-race %r ranks %r above %r and %r drops blob "
                    "%d LATER (%s s against %s s)."
                    % (act_id, better["id"], worse["id"], better["id"],
                       i + 1, tb, tw))
    _check_order_claim(a, act_id, "conduction-race",
                       [r["id"] for r in ordered])
    _counter_agrees(a, act_id, len(rods), "rod(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "conduction-race")

    lab = a.get("labels") or {}
    runl = a.get("run_labels") or {}
    punit = a.get("position_unit") or "cm"
    tunit = lab.get("unit", "s")

    picks = "".join(_seg("ks3-crace-rod", r["name"], data_crace_rod=r["id"])
                    for r in rods)

    outs = []
    for r in rods:
        fell = sum(1 for x in r["times"] if x is not None)
        blobs = "".join(
            '<li class="ks3-crace-blob" data-fell="%d">'
            '<span class="ks3-crace-at">%s %s</span>'
            '<span class="ks3-crace-time">%s</span></li>'
            % (1 if tm is not None else 0, _num(pos), t(punit),
               (("%s %s" % (_num(tm), tunit)) if tm is not None
                else t(lab.get("still", "still there"))))
            for pos, tm in zip(positions, r["times"]))
        outs.append(
            '<div class="ks3-crace-out" data-crace-out="%s" data-fell="%d" '
            'hidden><p class="ks3-crace-name">%s</p>'
            '<p class="ks3-crace-count">%s: <strong>%d of %d</strong></p>'
            '<ul class="ks3-crace-blobs" role="list">%s</ul>'
            '<p class="ks3-crace-note">%s</p></div>'
            % (e(r["id"]), fell, t(r["name"]),
               t(lab.get("fell", "Blobs that fell")), fell, len(positions),
               blobs, rich(r["note"])))

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-crace" data-crace data-total="%d"%s>'
            '<div class="ks3-crace-rods">%s</div>'
            '<div class="ks3-crace-runrow">'
            '<button type="button" class="ks3-crace-run" data-crace-run '
            'data-idle="%s" data-done="%s" disabled>%s</button></div>'
            '<div class="ks3-crace-body">'
            '<p class="ks3-crace-rest" data-crace-rest>%s</p>%s</div>%s</div>'
            % (gate_html, len(rods), body_attr, picks,
               e(runl.get("idle", "Run")), e(runl.get("done", "Run finished")),
               t(runl.get("idle", "Run")),
               t(a.get("resting") or "Pick a rod and run it."),
               "".join(outs),
               _close_panel(a, "ks3-crace", "data-crace-close")))


# ═══ p1-05 · particle-relay ══════════════════════════════════════════════

_RELAY_N = 12          # particles drawn in the strip
_RELAY_W, _RELAY_H = 640, 118


def _relay_svg(step, idx):
    """One stage of the strip. Every stage is drawn; the wiring shows one.

    ⚖️ **THE PARTICLES ARE AT THE SAME x IN EVERY STAGE, TO THE PIXEL.** That
    is the claim the drawing makes and it is the claim the lesson is about: in
    conduction the particles stay put and the vibration travels. A drawing
    whose dots crept rightwards stage by stage would teach the misconception
    the lesson exists to kill, and it would look livelier doing it.
    """
    reach = int(step.get("reach") or 0)
    gap = (_RELAY_W - 80) / float(_RELAY_N - 1)
    parts = []
    for i in range(_RELAY_N):
        cx = 40 + gap * i
        hot = i < reach
        # The vibration is drawn as an amplitude — a pair of ticks either side
        # of a particle that has been set going — never as a displacement.
        if hot:
            parts.append(
                '<line class="ks3-prel-amp" x1="%.1f" y1="60" x2="%.1f" '
                'y2="60"></line>' % (cx - 11, cx + 11))
        parts.append(
            '<circle class="ks3-prel-dot" data-hot="%d" cx="%.1f" cy="60" '
            'r="9"></circle>' % (1 if hot else 0, cx))
    if step.get("electrons"):
        # Free electrons: small marks BETWEEN the particles, running the whole
        # length. They are the only thing in the drawing that travels.
        for i in range(_RELAY_N - 1):
            cx = 40 + gap * i + gap / 2.0
            parts.append(
                '<circle class="ks3-prel-el" cx="%.1f" cy="36" r="3.4">'
                '</circle>' % cx)
        parts.append(
            '<line class="ks3-prel-elpath" x1="34" y1="36" x2="%.1f" y2="36">'
            '</line>' % (_RELAY_W - 34))
    return ('<svg class="ks3-prel-svg" viewBox="0 0 %d %d" role="img" '
            'aria-label="%s">'
            '<rect class="ks3-prel-rod" x="16" y="30" width="%d" height="60" '
            'rx="14"></rect>'
            '<line class="ks3-prel-flame" x1="16" y1="30" x2="16" y2="90">'
            '</line>%s</svg>'
            % (_RELAY_W, _RELAY_H,
               e("Step %d. A row of %d particles at fixed positions in a rod, "
                 "heated from the left. %d of them have been set vibrating. %s"
                 % (idx + 1, _RELAY_N, reach,
                    "Free electrons run the whole length of the rod."
                    if step.get("electrons")
                    else "No electrons are drawn.")),
               _RELAY_W - 32, "".join(parts)))


def r_particle_relay(a, act_id):
    """⊕ p1-05 `#s-model` — the mechanism, in four stages, one-way.

    `KS3.P.CIS.03` in practice: the whole block describes physical steps and
    never once says how much. Staged, on tap, and one-way — unshowing a step
    teaches nothing and gives a student a way to lose their place.

    ⚖️ **THE REACH MUST GROW AND MUST END AT THE FAR END.** A relay whose last
    stage stopped short would draw a rod whose far end never gets hot, under a
    lesson whose hook is a spoon handle that does.

    HOOKS: `data-prel` (wrapper, `data-total`) · `data-prel-stage` ·
    `data-prel-next` · `data-prel-close`.
    """
    steps = a.get("steps") or []
    if len(steps) < 3:
        raise ValueError(
            "particle-relay %r has %d step(s)." % (act_id, len(steps)))
    prev = -1
    for i, s in enumerate(steps):
        for key in ("id", "title", "text"):
            if not s.get(key):
                raise ValueError(
                    "particle-relay %r step %r has no %r."
                    % (act_id, s.get("id"), key))
        reach = s.get("reach")
        if not isinstance(reach, int) or not 0 < reach <= _RELAY_N:
            raise ValueError(
                "particle-relay %r step %r reaches %r of %d particles."
                % (act_id, s["id"], reach, _RELAY_N))
        if reach <= prev:
            raise ValueError(
                "particle-relay %r step %r reaches %d, no further than the "
                "step before it. The relay runs one way."
                % (act_id, s["id"], reach))
        prev = reach
    if steps[-1]["reach"] != _RELAY_N:
        raise ValueError(
            "particle-relay %r ends with the vibration reaching %d of %d "
            "particles. The far end of the spoon handle gets hot, which is "
            "the lesson's own hook."
            % (act_id, steps[-1]["reach"], _RELAY_N))
    _counter_agrees(a, act_id, len(steps), "step(s)")

    btns = a.get("buttons") or {}
    stages = "".join(
        '<div class="ks3-prel-stage" data-prel-stage="%d" hidden>'
        '<p class="ks3-prel-title">%s</p>%s'
        '<p class="ks3-prel-text">%s</p></div>'
        % (i, t(s["title"]), _relay_svg(s, i), rich(s["text"]))
        for i, s in enumerate(steps))

    return ('<div class="ks3-prel" data-prel data-total="%d">'
            '<p class="ks3-prel-caption">%s</p>%s'
            '<div class="ks3-prel-foot">'
            '<button type="button" class="ks3-reveal-btn ks3-prel-next" '
            'data-prel-next data-next="%s" data-done="%s">%s</button></div>'
            '%s</div>'
            % (len(steps),
               t(a.get("strip_label") or ""), stages,
               e(btns.get("next", "Show the next step")),
               e(btns.get("done", "All shown")),
               t(btns.get("first", "Show the first step")),
               _close_panel(a, "ks3-prel", "data-prel-close")))


# ═══ p1-06 · radiation-cube ══════════════════════════════════════════════

def r_radiation_cube(a, act_id):
    """⊕ p1-06 `#s-surface` — a Leslie's cube and four cans, two modes.

    ⚖️ **THE TWO MODES MUST AGREE ON THE ORDER, AND THE RENDERER CHECKS IT.**
    A good emitter is a good absorber — they are one property seen from two
    sides — and the closing panel says so. A payload whose emission ranking
    and absorption ranking disagreed would put that sentence over two columns
    that contradict it, and both columns would render.

    ⚖️ **THE FOUR FACES ARE CHOSEN TO CONTRADICT THE FOLK VERSION, AND THE
    NUMBERS ARE THE ARGUMENT.** Matt white at 92 against matt black's 100, and
    two silver faces of the SAME metal eight points apart at one end and
    twenty-two at the other. Shiny against matt is what decides it; colour is
    a small effect on top. See the lesson's docstring for the full ruling and
    for where the black-car case is answered.

    HOOKS: `data-rcube` (wrapper, `data-total`) · `data-rcube-mode` ·
    `data-rcube-face` · `data-rcube-out` (valued `face:mode`) ·
    `data-rcube-rest` · `data-rcube-close`.
    """
    from ks3_art.kit import r_bench_gate
    faces = a.get("faces") or []
    modes = a.get("modes") or []
    if len(faces) < 3:
        raise ValueError(
            "radiation-cube %r has %d face(s)." % (act_id, len(faces)))
    if len(modes) != 2:
        raise ValueError(
            "radiation-cube %r declares %d mode(s); giving off and taking in "
            "are the pair the law is about." % (act_id, len(modes)))
    mode_ids = [m["id"] for m in modes]
    if sorted(mode_ids) != ["absorb", "emit"]:
        raise ValueError(
            "radiation-cube %r names its modes %s; they are `emit` and "
            "`absorb`." % (act_id, mode_ids))

    seen = set()
    for f in faces:
        for key in ("id", "name", "note"):
            if not f.get(key):
                raise ValueError(
                    "radiation-cube %r face %r has no %r."
                    % (act_id, f.get("id"), key))
        if f["id"] in seen:
            raise ValueError(
                "radiation-cube %r repeats face id %r." % (act_id, f["id"]))
        seen.add(f["id"])
        for m in mode_ids:
            if not isinstance(f.get(m), (int, float)) or f[m] <= 0:
                raise ValueError(
                    "radiation-cube %r face %r has no positive %r reading. "
                    "Every face is measured both ways or the two columns "
                    "cannot be compared." % (act_id, f["id"], m))

    _ranks_are_dense(faces, act_id, "radiation-cube")
    ordered = sorted(faces, key=lambda f: int(f["rank"]))

    # ⚖️ ONE PROPERTY, TWO SIDES. Both columns must fall in rank order, and
    # strictly: two faces reading the same in one mode would be two faces the
    # bench cannot order while printing an order.
    for mid in mode_ids:
        vals = [float(f[mid]) for f in ordered]
        if vals != sorted(vals, reverse=True):
            raise ValueError(
                "radiation-cube %r ranks its faces %s and the %r column runs "
                "%s. A good emitter is a good absorber: the closing panel "
                "says so, and these two columns are the evidence for it."
                % (act_id, [f["id"] for f in ordered], mid, vals))
        if len(set(vals)) != len(vals):
            raise ValueError(
                "radiation-cube %r has two faces with the same %r reading. "
                "The bench prints an order it claims to have measured."
                % (act_id, mid))
    _check_order_claim(a, act_id, "radiation-cube", [f["id"] for f in ordered])
    _counter_agrees(a, act_id, len(faces), "face(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "radiation-cube")

    mode_btns = "".join(
        _seg("ks3-rcube-mode", m.get("label", ""), pressed=(i == 0),
             data_rcube_mode=m["id"])
        for i, m in enumerate(modes))
    caps = "".join(
        '<p class="ks3-rcube-caption" data-rcube-caption="%s"%s>%s</p>'
        % (e(m["id"]), "" if i == 0 else " hidden", t(m.get("caption", "")))
        for i, m in enumerate(modes))
    face_btns = "".join(
        _seg("ks3-rcube-face", f["name"], data_rcube_face=f["id"])
        for f in faces)

    outs = []
    for f in faces:
        for m in modes:
            outs.append(
                '<div class="ks3-rcube-out" data-rcube-out="%s" hidden>'
                '<p class="ks3-rcube-name">%s</p>'
                '<p class="ks3-rcube-read"><span class="ks3-rcube-what">%s'
                '</span><span class="ks3-rcube-val">%s</span>'
                '<span class="ks3-rcube-unit">%s</span></p>'
                '<p class="ks3-rcube-note">%s</p></div>'
                % (e("%s:%s" % (f["id"], m["id"])), t(f["name"]),
                   t(m.get("readout", "")),
                   _num(f[m["id"]], 1 if m["id"] == "absorb" else 0),
                   t(m.get("unit", "")), rich(f["note"])))

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-rcube" data-rcube data-total="%d"%s>'
            '<div class="ks3-rcube-modes">%s</div>%s'
            '<div class="ks3-rcube-faces">%s</div>'
            '<div class="ks3-rcube-body">'
            '<p class="ks3-rcube-rest" data-rcube-rest>%s</p>%s</div>%s</div>'
            % (gate_html, len(faces), body_attr, mode_btns, caps, face_btns,
               t(a.get("resting") or "Pick a face to read it."),
               "".join(outs),
               _close_panel(a, "ks3-rcube", "data-rcube-close")))


# ═══ p1-06 · across-the-gap ══════════════════════════════════════════════

def r_across_the_gap(a, act_id):
    """⊕ p1-06 `#s-gap` — three gaps down, two routes across, six cells.

    The block that kills `ENER-14`. Read across the radiation row and it is
    the same in all three gaps; read across the conduction row and it goes
    full, almost none, none.

    ⚖️ **EVERY CELL IS PRESENT OR THE BUILD FAILS.** A hole in a matrix is a
    comparison the student is invited to make and then cannot, and this
    matrix's whole teaching is one row read against the other.

    ⚠️ **THE MATRIX SCROLLS SIDEWAYS ON A NARROW SCREEN AND ITS SCROLLER
    CARRIES `position: relative`** (audit law: an absolutely positioned child
    inside a scroller that is not positioned widens the document instead of
    the scroller, and it does it only on a phone).

    HOOKS: `data-agap` (wrapper, `data-total`) · `data-agap-cell` (valued
    `route:gap`) · `data-agap-out` · `data-agap-rest` · `data-agap-close`.
    """
    gaps = a.get("gaps") or []
    routes = a.get("routes") or []
    cells = a.get("cells") or {}
    if len(gaps) < 2 or len(routes) < 2:
        raise ValueError(
            "across-the-gap %r has %d gap(s) and %d route(s); the block is a "
            "matrix." % (act_id, len(gaps), len(routes)))

    n = 0
    for r in routes:
        for g in gaps:
            key = "%s:%s" % (r["id"], g["id"])
            cell = cells.get(key)
            if not cell:
                raise ValueError(
                    "across-the-gap %r has no cell for %r. A hole in the "
                    "matrix is a comparison the student is invited to make "
                    "and then cannot." % (act_id, key))
            for k in ("verdict", "obs"):
                if not cell.get(k):
                    raise ValueError(
                        "across-the-gap %r cell %r has no %r."
                        % (act_id, key, k))
            lvl = cell.get("level")
            if not isinstance(lvl, int) or not 0 <= lvl <= 3:
                raise ValueError(
                    "across-the-gap %r cell %r has level %r; it is 0 to 3 "
                    "and it is what paints the cell." % (act_id, key, lvl))
            n += 1

    # ⚖️ THE POINT OF THE BLOCK, ASSERTED. Radiation must read the same
    # through every gap and conduction must not — otherwise the two rows say
    # nothing when read against each other, which is the only thing this
    # block is for.
    def _levels(route_id):
        return [cells["%s:%s" % (route_id, g["id"])]["level"] for g in gaps]

    rad = [r["id"] for r in routes if r["id"] == "radiation"]
    con = [r["id"] for r in routes if r["id"] == "conduction"]
    if rad and con:
        rl, cl = _levels(rad[0]), _levels(con[0])
        if len(set(rl)) == len(rl) and len(rl) > 1:
            raise ValueError(
                "across-the-gap %r gives radiation a different level in every "
                "gap (%s). The block exists to show that radiation is "
                "unaffected by what is in the gap." % (act_id, rl))
        if len(set(cl)) < 2:
            raise ValueError(
                "across-the-gap %r gives conduction the same level in every "
                "gap (%s). The contrast with radiation is the whole block."
                % (act_id, cl))
        if 0 not in cl:
            raise ValueError(
                "across-the-gap %r never gives conduction a level of 0. The "
                "vacuum cell is the one that settles ENER-14, and 'almost "
                "none' is not the same claim as 'none'." % act_id)
    _counter_agrees(a, act_id, n, "cell(s)")

    heads = "".join('<th scope="col">%s</th>' % t(g.get("label", ""))
                    for g in gaps)
    body, outs = [], []
    for r in routes:
        tds = []
        for g in gaps:
            key = "%s:%s" % (r["id"], g["id"])
            cell = cells[key]
            # ⚖️ THE PIPS ARE THE VISUAL ENCODING AND THEY ARE DERIVED
            # FROM `level`, THREE OF THEM, FILLED FROM THE LEFT. The word is
            # the primary channel — colour is never the only one — and the
            # pips let a student read the whole matrix down a column without
            # opening every cell, which is the comparison the block is for.
            pips = "".join(
                '<i data-on="%d"></i>' % (1 if k < cell["level"] else 0)
                for k in range(3))
            tds.append(
                '<td><button type="button" class="ks3-agap-cell" '
                'data-agap-cell="%s" data-level="%d" aria-pressed="false">'
                '<span class="ks3-agap-word">%s</span>'
                '<span class="ks3-agap-pips" aria-hidden="true">%s</span>'
                '</button></td>'
                % (e(key), cell["level"], t(cell["verdict"]), pips))
            outs.append(
                '<div class="ks3-agap-out" data-agap-out="%s" data-level="%d" '
                'hidden><p class="ks3-agap-head">%s</p>'
                '<p class="ks3-agap-verdict">%s</p>'
                '<p class="ks3-agap-obs">%s</p></div>'
                % (e(key), cell["level"],
                   t("%s across %s" % (r.get("label", ""),
                                       g.get("label", "").lower())),
                   t(cell["verdict"]), rich(cell["obs"])))
        body.append('<tr><th scope="row">%s</th>%s</tr>'
                    % (t(r.get("label", "")), "".join(tds)))

    return ('<div class="ks3-agap" data-agap data-total="%d">'
            '<div class="ks3-agap-scroll">'
            '<table class="ks3-agap-table"><thead><tr><td></td>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<div class="ks3-agap-readout">'
            '<p class="ks3-agap-rest" data-agap-rest>%s</p>%s</div>%s</div>'
            % (n, heads, "".join(body),
               t(a.get("resting") or "Pick a cell to read it."),
               "".join(outs),
               _close_panel(a, "ks3-agap", "data-agap-close")))


# ═══ p1-07 · lagging-bench ═══════════════════════════════════════════════

def r_lagging_bench(a, act_id):
    """⊕ p1-07 `#s-lag` — four materials, two thicknesses, one bare beaker.

    TWO DIALS, and both are MODELLED. MRB-257 §5A.1: a dial that is drawn and
    not modelled marks a student's own prediction correct while showing them
    nothing, and `gas-pressure` shipped exactly that. Here every one of the
    eight cells has its own reading and its own derived comparison.

    ⚖️ **EVERY NUMBER EXCEPT THE FINAL TEMPERATURE IS DERIVED.** The drop, the
    margin over the bare beaker and the sentence beside them all come out of
    `after`, `start_temp` and `control_after`. Authoring a drop as well would
    be the same fact in two places, and the two would disagree the first time
    a temperature moved.

    ⚖️ **THE CONTROL IS ON SCREEN AT ALL TIMES**, not behind a tab. Without it
    "62.7 degrees" is a number with nothing to be better than, and the whole
    investigation is eight unrelated readings.

    ⚖️ **THE ORDER IS DERIVED FROM `rank` AND CHECKED AT BOTH THICKNESSES.**
    The closing panel claims the order is the same at one layer and at three,
    which is a claim about eight readings; the renderer checks it against all
    eight before it will draw the panel.

    ⚠️ **EVERY BEAKER MUST STILL COOL.** A cell whose final temperature was
    the starting temperature would say insulation stops a transfer, which is
    the opposite of `ENER-15`'s correction and of the lesson's key fact.

    HOOKS: `data-lagb` (wrapper, `data-total`) · `data-lagb-mat` ·
    `data-lagb-thick` · `data-lagb-run` · `data-lagb-out` (valued
    `material:thickness`) · `data-lagb-rest` · `data-lagb-close`.
    """
    from ks3_art.kit import r_bench_gate
    mats = a.get("materials") or []
    thicks = a.get("thicknesses") or []
    start = a.get("start_temp")
    room = a.get("room_temp")
    control = a.get("control_after")
    if len(mats) < 3 or len(thicks) < 2:
        raise ValueError(
            "lagging-bench %r has %d material(s) and %d thickness(es); two "
            "dials is the point of the block."
            % (act_id, len(mats), len(thicks)))
    for name, v in (("start_temp", start), ("room_temp", room),
                    ("control_after", control)):
        if not isinstance(v, (int, float)):
            raise ValueError(
                "lagging-bench %r has no numeric %r." % (act_id, name))
    if not room < control < start:
        raise ValueError(
            "lagging-bench %r has the bare beaker finishing at %s, outside "
            "the room temperature %s and the start %s. The control is the "
            "worst case and it still cannot pass either end."
            % (act_id, control, room, start))

    tids = [x["id"] for x in thicks]
    if len(set(tids)) != len(tids):
        raise ValueError("lagging-bench %r repeats a thickness id." % act_id)

    seen = set()
    for m in mats:
        for key in ("id", "name", "note"):
            if not m.get(key):
                raise ValueError(
                    "lagging-bench %r material %r has no %r."
                    % (act_id, m.get("id"), key))
        if m["id"] in seen:
            raise ValueError(
                "lagging-bench %r repeats material id %r." % (act_id, m["id"]))
        seen.add(m["id"])
        after = m.get("after") or {}
        for tid in tids:
            v = after.get(tid)
            if not isinstance(v, (int, float)):
                raise ValueError(
                    "lagging-bench %r material %r has no reading at "
                    "thickness %r. Eight cells means eight."
                    % (act_id, m["id"], tid))
            if not room < v < start:
                raise ValueError(
                    "lagging-bench %r material %r at %r finishes at %s. Every "
                    "beaker cools and none of them reaches the room, which "
                    "is the lesson's own key fact: insulation slows a "
                    "transfer and never stops one."
                    % (act_id, m["id"], tid, v))
            if v <= control:
                raise ValueError(
                    "lagging-bench %r material %r at %r finishes at %s, no "
                    "better than the bare beaker at %s. A lagging that does "
                    "nothing is not on this bench."
                    % (act_id, m["id"], tid, v, control))
        # More layers must do better, or the thickness dial is drawn and not
        # modelled — which is the defect this comment exists to prevent.
        vals = [after[tid] for tid in tids]
        if vals != sorted(vals):
            raise ValueError(
                "lagging-bench %r material %r reads %s across %s. More "
                "layers hold more still air, so a thicker one cannot finish "
                "cooler." % (act_id, m["id"], vals, tids))

    _ranks_are_dense(mats, act_id, "lagging-bench")
    ordered = sorted(mats, key=lambda m: int(m["rank"]))
    for tid in tids:
        vals = [float(m["after"][tid]) for m in ordered]
        if vals != sorted(vals, reverse=True):
            raise ValueError(
                "lagging-bench %r ranks its materials %s and at thickness %r "
                "the readings run %s. The closing panel claims the order is "
                "the same at every thickness."
                % (act_id, [m["id"] for m in ordered], tid, vals))
    _check_order_claim(a, act_id, "lagging-bench", [m["id"] for m in ordered])
    _counter_agrees(a, act_id, len(mats) * len(thicks), "combination(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "lagging-bench")

    lab = a.get("labels") or {}
    runl = a.get("run_labels") or {}
    unit = a.get("unit") or "°C"

    mat_btns = "".join(_seg("ks3-lagb-mat", m["name"], data_lagb_mat=m["id"])
                       for m in mats)
    thick_btns = "".join(_seg("ks3-lagb-thick", x.get("label", ""),
                              data_lagb_thick=x["id"]) for x in thicks)

    outs = []
    for m in mats:
        for x in thicks:
            after = float(m["after"][x["id"]])
            drop = float(start) - after
            margin = after - float(control)
            outs.append(
                '<div class="ks3-lagb-out" data-lagb-out="%s" hidden>'
                '<p class="ks3-lagb-name">%s, %s</p>'
                '<dl class="ks3-lagb-tiles">'
                '<div class="ks3-lagb-tile"><dt>%s</dt><dd>%s %s</dd></div>'
                '<div class="ks3-lagb-tile"><dt>%s</dt><dd>%s %s</dd></div>'
                '</dl>'
                '<p class="ks3-lagb-margin">%s</p>'
                '<p class="ks3-lagb-note">%s</p></div>'
                % (e("%s:%s" % (m["id"], x["id"])), t(m["name"]),
                   t(x.get("label", "")),
                   t(lab.get("after", "After")), _num(after, 1), t(unit),
                   t(lab.get("drop", "Temperature drop")), _num(drop, 1),
                   t(unit),
                   # ⚖️ DERIVED against the control, every cell.
                   t("%s %s %s — and it still cooled by %s %s."
                     % (_num(margin, 1), unit,
                        lab.get("better", "above the bare beaker"),
                        _num(drop, 1), unit)),
                   rich(m["note"])))

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-lagb" data-lagb data-total="%d"%s>'
            '<div class="ks3-lagb-control">'
            '<p class="ks3-lagb-clabel">%s</p>'
            '<p class="ks3-lagb-cval">%s %s</p>'
            '<p class="ks3-lagb-cdrop">cooled by %s %s in %s minutes</p>'
            '</div>'
            '<div class="ks3-lagb-dials">'
            '<div class="ks3-lagb-dial"><p class="ks3-lagb-dlabel">%s</p>'
            '<div class="ks3-lagb-dbtns">%s</div></div>'
            '<div class="ks3-lagb-dial"><p class="ks3-lagb-dlabel">%s</p>'
            '<div class="ks3-lagb-dbtns">%s</div></div></div>'
            '<div class="ks3-lagb-runrow">'
            '<button type="button" class="ks3-lagb-run" data-lagb-run '
            'data-idle="%s" data-done="%s" disabled>%s</button></div>'
            '<div class="ks3-lagb-body">'
            '<p class="ks3-lagb-rest" data-lagb-rest>%s</p>%s</div>%s</div>'
            % (gate_html, len(mats) * len(thicks), body_attr,
               t(lab.get("control", "Bare beaker")), _num(control, 1), t(unit),
               _num(float(start) - float(control), 1), t(unit),
               _num(a.get("minutes") or 0),
               t(lab.get("material", "Material")), mat_btns,
               t(lab.get("thickness", "Thickness")), thick_btns,
               e(runl.get("idle", "Run")), e(runl.get("done", "Run finished")),
               t(runl.get("idle", "Run")),
               t(a.get("resting") or "Pick a material and a thickness."),
               "".join(outs),
               _close_panel(a, "ks3-lagb", "data-lagb-close")))


# ═══ p1-08 · machine-bench ═══════════════════════════════════════════════

def r_machine_bench(a, act_id):
    """⊕ p1-08 `#s-machine` — one load, three machines, nine set-ups.

    ⚖️ **ONE AUTHORED NUMBER PER SET-UP, AND EVERYTHING ELSE IS COMPUTED.**
    The payload gives a `multiplier`; the load and the height are the block's
    and never change. From those three:

        force on the load  = load
        distance it rises  = height
        force you apply    = load / multiplier
        distance you move  = height * multiplier
        work in            = force you apply * distance you move
        work out           = load * height

    and the renderer REFUSES a row whose two products differ. The identity is
    the entire lesson (`KS3.P.ECT.01`: "product of force and displacement
    unchanged"), and a row that quietly broke it would render perfectly and
    teach the opposite.

    ⚖️ **THE COMPARATIVE IS DERIVED AND HAS AN EQUAL BRANCH.** MRB-257 §5A.1.
    Two of the nine set-ups have a multiplier of 1 — an equal-armed lever and
    a single fixed pulley — so "this machine gives you nothing and charges
    you nothing" is a state a student can select, not a guard clause. The
    renderer requires at least one, for the same reason the equilibrium bench
    requires an equal pair.

    ⚠️ **NO SET-UP MAY HAVE A MULTIPLIER BELOW 1 ON THIS BENCH.** A machine
    used the other way round — trading force for speed, as a bicycle gear
    does — is real and is `(and vice versa)` in the bullet, but the bench's
    readout is written round "you push with less and move further" and a
    multiplier under one would print that sentence over numbers that say the
    opposite. It is named in the close instead of half-drawn here.

    HOOKS: `data-mbench` (wrapper, `data-total`) · `data-mbench-machine` ·
    `data-mbench-setting` (valued `machine:setting`) · `data-mbench-out` ·
    `data-mbench-rest` · `data-mbench-close`.
    """
    from ks3_art.kit import r_bench_gate
    machines = a.get("machines") or []
    load = a.get("load")
    height = a.get("height")
    if len(machines) < 2:
        raise ValueError(
            "machine-bench %r has %d machine(s)." % (act_id, len(machines)))
    if not isinstance(load, (int, float)) or load <= 0:
        raise ValueError("machine-bench %r has no positive `load`." % act_id)
    if not isinstance(height, (int, float)) or height <= 0:
        raise ValueError("machine-bench %r has no positive `height`." % act_id)

    w_out = float(load) * float(height)
    n, has_unit_mult, seen = 0, False, set()
    for m in machines:
        for key in ("id", "name", "how"):
            if not m.get(key):
                raise ValueError(
                    "machine-bench %r machine %r has no %r."
                    % (act_id, m.get("id"), key))
        if m["id"] in seen:
            raise ValueError(
                "machine-bench %r repeats machine id %r." % (act_id, m["id"]))
        seen.add(m["id"])
        settings = m.get("settings") or []
        if len(settings) < 2:
            raise ValueError(
                "machine-bench %r machine %r has %d setting(s); the bench is "
                "about what changes when the setting does."
                % (act_id, m["id"], len(settings)))
        sids = set()
        for s in settings:
            for key in ("id", "label", "detail"):
                if not s.get(key):
                    raise ValueError(
                        "machine-bench %r setting %r on %r has no %r."
                        % (act_id, s.get("id"), m["id"], key))
            if s["id"] in sids:
                raise ValueError(
                    "machine-bench %r machine %r repeats setting id %r."
                    % (act_id, m["id"], s["id"]))
            sids.add(s["id"])
            mult = s.get("multiplier")
            if not isinstance(mult, (int, float)) or mult < 1:
                raise ValueError(
                    "machine-bench %r setting %r on %r has multiplier %r. It "
                    "is at least 1 on this bench — see the docstring for why "
                    "the vice-versa case is named rather than half-drawn."
                    % (act_id, s["id"], m["id"], mult))
            if float(mult) == 1.0:
                has_unit_mult = True
            # THE IDENTITY, CHECKED. Both products, from the same three
            # numbers, before anything is drawn.
            f_in = float(load) / float(mult)
            d_in = float(height) * float(mult)
            if abs(f_in * d_in - w_out) > 1e-9:
                raise ValueError(
                    "machine-bench %r setting %r on %r gives %s J in and %s J "
                    "out. `KS3.P.ECT.01` is that these are the same number."
                    % (act_id, s["id"], m["id"], f_in * d_in, w_out))
            n += 1

    if not has_unit_mult:
        raise ValueError(
            "machine-bench %r has no set-up with a multiplier of 1. That is "
            "the state where the derived comparative has to say 'this "
            "machine gives you nothing', and a branch no set-up reaches is a "
            "branch that ships untested — the alveoli defect exactly."
            % act_id)
    _counter_agrees(a, act_id, n, "set-up(s)")
    _no_correct_flags([{"options": (a.get("gate") or {}).get("options") or []}],
                      act_id, "machine-bench")

    lab = a.get("labels") or {}
    un = a.get("units") or {}
    uf, ud, uw = (un.get("force", "N"), un.get("distance", "m"),
                  un.get("work", "J"))

    mach_btns = "".join(
        _seg("ks3-mbench-machine", m["name"], data_mbench_machine=m["id"])
        for m in machines)
    hows = "".join(
        '<p class="ks3-mbench-how" data-mbench-how="%s" hidden>%s</p>'
        % (e(m["id"]), t(m["how"])) for m in machines)
    setrows = "".join(
        '<div class="ks3-mbench-setrow" data-mbench-setrow="%s" hidden>%s'
        '</div>'
        % (e(m["id"]),
           "".join(_seg("ks3-mbench-setting", s["label"],
                        data_mbench_setting="%s:%s" % (m["id"], s["id"]))
                   for s in m["settings"]))
        for m in machines)

    outs = []
    for m in machines:
        for s in m["settings"]:
            mult = float(s["multiplier"])
            f_in = float(load) / mult
            d_in = float(height) * mult
            if mult == 1.0:
                says = ("You pull with the whole %s %s and move it the whole "
                        "%s %s. This machine gives you nothing and charges "
                        "you nothing — what it changes is the direction you "
                        "pull in."
                        % (_num(load), uf, _num(height, 2), ud))
            else:
                says = ("You pull with %s %s instead of %s %s — %s times less "
                        "force — and you move it %s %s instead of %s %s, "
                        "which is %s times further."
                        % (_num(f_in), uf, _num(load), uf, _num(mult),
                           _num(d_in, 2), ud, _num(height, 2), ud,
                           _num(mult)))
            outs.append(
                '<div class="ks3-mbench-out" data-mbench-out="%s" '
                'data-mult="%s" hidden>'
                '<p class="ks3-mbench-name">%s · %s</p>'
                '<p class="ks3-mbench-detail">%s</p>'
                '<dl class="ks3-mbench-tiles">'
                '<div class="ks3-mbench-tile"><dt>%s</dt><dd>%s %s</dd></div>'
                '<div class="ks3-mbench-tile"><dt>%s</dt><dd>%s %s</dd></div>'
                '<div class="ks3-mbench-tile"><dt>%s</dt><dd>%s %s</dd></div>'
                '<div class="ks3-mbench-tile"><dt>%s</dt><dd>%s %s</dd></div>'
                '</dl>'
                '<div class="ks3-mbench-work">'
                '<p class="ks3-mbench-wtile"><span>%s</span>'
                '<strong>%s %s</strong></p>'
                '<p class="ks3-mbench-eq" aria-hidden="true">=</p>'
                '<p class="ks3-mbench-wtile"><span>%s</span>'
                '<strong>%s %s</strong></p></div>'
                '<p class="ks3-mbench-says">%s</p></div>'
                % (e("%s:%s" % (m["id"], s["id"])), e(_num(mult)),
                   t(m["name"]), t(s["label"]), t(s["detail"]),
                   t(lab.get("fin", "Force you apply")), _num(f_in), t(uf),
                   t(lab.get("din", "Distance you move it")), _num(d_in, 2),
                   t(ud),
                   t(lab.get("fout", "Force on the load")), _num(load), t(uf),
                   t(lab.get("dout", "Distance it rises")), _num(height, 2),
                   t(ud),
                   t(lab.get("win", "Work you do")), _num(f_in * d_in), t(uw),
                   t(lab.get("wout", "Work done on the load")), _num(w_out),
                   t(uw),
                   t(says)))

    gate_html, body_attr = r_bench_gate(a.get("gate"))
    return ('%s<div class="ks3-mbench" data-mbench data-total="%d"%s>'
            '<div class="ks3-mbench-machines">'
            '<p class="ks3-mbench-dlabel">%s</p>%s</div>%s'
            '<div class="ks3-mbench-settings">'
            '<p class="ks3-mbench-dlabel">%s</p>%s</div>'
            '<div class="ks3-mbench-body">'
            '<p class="ks3-mbench-rest" data-mbench-rest>%s</p>%s</div>%s</div>'
            % (gate_html, n, body_attr,
               t(lab.get("machine", "Machine")), mach_btns, hows,
               t(lab.get("setting", "Setting")), setrows,
               t(a.get("resting") or "Pick a machine and a setting."),
               "".join(outs),
               _close_panel(a, "ks3-mbench", "data-mbench-close")))


# ═══ registration ════════════════════════════════════════════════════════
#
# ⚠️ `fifa-pick` IS NOT HERE. It is C2's, and P1 places it without
# registering it — see the module header for the full reasoning and for
# exactly what P1 depends on.

KIND_SHELL = {
    'store-audit': ("ks3-saudit-block",
                    ' data-instrument data-sauditblock data-stage-done="0"'),
    'store-or-pathway': ("ks3-spath-block",
                         ' data-instrument data-spathblock '
                         'data-stage-done="0"'),
    'before-after-bench': ("ks3-baben-block",
                           ' data-instrument data-babenblock '
                           'data-stage-done="0"'),
    'energy-audit': ("ks3-eaudit-block",
                     ' data-instrument data-eauditblock data-stage-done="0"'),
    'mechanism-or-energy': ("ks3-mech-block",
                            ' data-instrument data-mechblock '
                            'data-stage-done="0"'),
    'equilibrium-bench': ("ks3-equil-block",
                          ' data-instrument data-equilblock '
                          'data-stage-done="0"'),
    'conduction-race': ("ks3-crace-block",
                        ' data-instrument data-craceblock '
                        'data-stage-done="0"'),
    'particle-relay': ("ks3-prelay-block",
                       ' data-instrument data-prelayblock '
                       'data-stage-done="0"'),
    'radiation-cube': ("ks3-rcube-block",
                       ' data-instrument data-rcubeblock data-stage-done="0"'),
    'across-the-gap': ("ks3-agap-block",
                       ' data-instrument data-agapblock data-stage-done="0"'),
    'lagging-bench': ("ks3-lagb-block",
                      ' data-instrument data-lagbblock data-stage-done="0"'),
    'machine-bench': ("ks3-mbench-block",
                      ' data-instrument data-mbenchblock '
                      'data-stage-done="0"'),
}

KIND_FN = {
    'store-audit': r_store_audit,
    'store-or-pathway': r_store_or_pathway,
    'before-after-bench': r_before_after_bench,
    'energy-audit': r_energy_audit,
    'mechanism-or-energy': r_mechanism_or_energy,
    'equilibrium-bench': r_equilibrium_bench,
    'conduction-race': r_conduction_race,
    'particle-relay': r_particle_relay,
    'radiation-cube': r_radiation_cube,
    'across-the-gap': r_across_the_gap,
    'lagging-bench': r_lagging_bench,
    'machine-bench': r_machine_bench,
}
