"""ks3_art.p1 — P1 *Energy transfers*, the first physics unit in the key stage.

Every instrument here is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p1/`. Her page wins outright: a shape that is not in
her drawing is not in this module, and where her NOTES and her drawing disagree
the drawing is measured and the note is reported.

── ⚠️ THE HISTORY THIS MODULE REPLACES ─────────────────────────────────────

An earlier MRB-223 run globbed `docs/ks3/design-reference/*/*.dc.html`, found
no `physics/` folder, concluded Design had drawn nothing, and authored eight
P1 lessons and sixteen instruments from scratch. She had drawn all seventy
physics lessons; they were untracked in the main worktree under
`KS3 P<n> lessons/`, invisible to a lane by relative path because a worktree
shares a `.git` and not a working directory.

That work is preserved, pages and all, at
`docs/ks3/holding/p1-code-authored-2026-08-24/`. It is NOT a starting point
and it is deliberately not reconciled against Design's pages — MRB-205 forbids
an invented shape, and reconciling one against a drawing keeps the invention.

── ⚖️ MRB-204 · TRIANGLE, BEAM, BAR — CHECKED PER BLOCK ────────────────────

P1 carries two formula blocks and they are drawn differently on purpose,
because the arithmetic under them differs:

    p1-03  `#s-balance`   total before = total after       BEAM
           A SUM. Design's own splits are 120 = 62 + 55 + 3, and her page
           argues the point in words: "Conservation is a balance, not a
           triangle." A triangle over a sum teaches a relationship that does
           not exist.

    p1-08  `#s-balance`   F1 x d1 = F2 x d2                BEAM + TRIANGLE/PAN
           Each SIDE is a genuine product, so each pan carries a triangle;
           the equals sign between them is a balance, which no triangle can
           show. Design: "there are four quantities and an equals sign, not
           three quantities and a bar."

Both were checked against the arithmetic before rendering, and again in the
second pass. Arrows inside a formula block are SVG; typed arrows stay in prose.

── ⚠️ RESERVED PAYLOAD KEYS ────────────────────────────────────────────────

`r_activity` renders `cards`, `sim`, `fifa` and `scorecards` itself, and those
four have NO opt-out — an instrument whose payload carries one gets two
renderers and the block ships doubled. Nothing in this module uses any of
them; the sort instrument's items are `sort_items`, never `cards`.

── ⚠️ BAND VALUES ──────────────────────────────────────────────────────────

Where a band appears it is the full word — `standard`, `harder`, `easier`.
Never `s` or `h`.
"""

import re

from ks3_art.kit import e, rich, t


# ═══ shared P1 primitives ════════════════════════════════════════════════

def _p1_seg(cls, label, pressed=False, **attrs):
    """One segmented-control button. No `correct`, ever.

    `pressed` is real state. Design's store audit opens on scenario 1 with its
    text already showing, so that button ships `aria-pressed="true"` and the
    resting HTML agrees with the runtime rather than agreeing one frame later.
    MRB-208 is untouched: what may not be ticked on load is the RAIL STOP, and
    `data-stage-done` still opens at 0.
    """
    extra = "".join(' %s="%s"' % (k.replace("_", "-"), e(v))
                    for k, v in sorted(attrs.items()) if v is not None)
    return ('<button type="button" class="ks3-seg-btn %s"%s '
            'aria-pressed="%s">%s</button>'
            % (e(cls), extra, "true" if pressed else "false", t(label)))


def _unique_ids(rows, act_id, family, what):
    """Ids inside one payload are unique, because they become DOM keys."""
    ids = [r.get("id") for r in rows]
    if not all(ids):
        raise ValueError(
            "%s %r: a %s has no id. The id is half of the `data-*-out` key "
            "that selects its panel, so a missing one silently collapses two "
            "states into one." % (family, act_id, what))
    if len(set(ids)) != len(ids):
        raise ValueError(
            "%s %r repeats a %s id in %s. Two rows with one key means one of "
            "them can never be shown." % (family, act_id, what, ids))
    return ids


def _no_correct_flags(rows, act_id, family):
    """R3: an activity option is CHOSEN, never CORRECT.

    A `correct` key on any row here would put a mark on an activity option,
    and the student then reads the whole page as a test — which is precisely
    what committing-before-revealing exists to avoid. The mastery ladder is
    the only thing on a KS3 page that marks.
    """
    for r in rows:
        if "correct" in r:
            raise ValueError(
                "%s %r row %r carries a `correct` flag. Activity options are "
                "chosen, never marked (R3) — only the ladder marks."
                % (family, act_id, r.get("id")))


_COUNT_WORDS = {
    2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
}


def _count_word_agrees(text, n, act_id, family, where):
    """A number written in words in the prose must match the payload's length.

    Design writes "Two of these four are gases that do nothing" and the like,
    and a payload that grows by one row turns that sentence into a lie that
    nothing else on the page would catch.
    """
    if not text:
        return
    word = _COUNT_WORDS.get(n)
    if not word:
        return
    for m, other in _COUNT_WORDS.items():
        if m == n:
            continue
        if re.search(r"\b%s\b" % other, text, re.I) and not re.search(
                r"\b%s\b" % word, text, re.I):
            raise ValueError(
                "%s %r's %s says %r but the payload holds %d row(s). The "
                "prose counts the instrument, so the two cannot disagree."
                % (family, act_id, where, other, n))


# ═══ p1-01 · store-audit ═════════════════════════════════════════════════

def r_store_audit(a, act_id):
    """⊕ p1-01 `#s-audit` — five scenarios, one ledger, eight stores a side.

    Design's block. A student picks a scenario, ticks which stores hold energy
    at the START and which hold it at the END, and presses Check. The ledger is
    balanced only when BOTH columns match exactly — a superset does not count,
    because the claim being taught is that the count does not go up.

    ⚖️ **THE RAIL STOP TICKS AT THREE OF FIVE, WHICH IS DESIGN'S NUMBER.**
    Her `DONE('s-audit')` is `Object.keys(s.solved).length >= 3` against a set
    of five. It is not a slip: the fifth scenario (the bouncing ball, ticking
    thermal at maximum squash) is the hardest in the unit and is placed last,
    and requiring all five would make the stop a completion badge rather than
    a record of the student having got the idea. `ledgers_to_balance` carries
    it and is checked against the set rather than assumed.

    ⚠️ **THE MARK VOCABULARY IS THREE-VALUED, NOT TWO.** Design distinguishes
    a store ticked that should not be (`not this one`) from a store that
    should have been ticked and was not (`you missed this`). Collapsing those
    into one "wrong" loses the whole diagnostic value of the ledger: the two
    errors mean opposite things about what the student believes.

    ⚠️ **CHECKING IS NOT STICKY.** Touching any chip after a check clears the
    verdict, because a marked ledger the student has since edited is showing
    marks for a state that no longer exists.

    HOOKS: `data-saudit` (wrapper, `data-total`, `data-target`) ·
    `data-saudit-sc` (scenario button, valued with the scenario id) ·
    `data-saudit-text` (the scenario sentence) ·
    `data-saudit-chip` (valued `before:<store>` / `after:<store>`) ·
    `data-saudit-check` · `data-saudit-clear` ·
    `data-saudit-verdict` (the panel) · `data-saudit-vlabel` ·
    `data-saudit-vtext` · `data-saudit-progress`.
    """
    stores = a.get("stores") or []
    scenarios = a.get("scenarios") or []

    if len(stores) < 6:
        raise ValueError(
            "store-audit %r offers %d store(s). The lesson's claim is that "
            "there is a SHORT closed list a student can learn and then use on "
            "anything, and a handful of chips cannot make it."
            % (act_id, len(stores)))
    if len(scenarios) < 3:
        raise ValueError(
            "store-audit %r declares %d scenario(s). The ledger only teaches "
            "anything by being run more than once on different physics."
            % (act_id, len(scenarios)))

    _unique_ids(stores, act_id, "store-audit", "store")
    _unique_ids(scenarios, act_id, "store-audit", "scenario")
    _no_correct_flags(stores, act_id, "store-audit")
    _no_correct_flags(scenarios, act_id, "store-audit")

    known = {s["id"] for s in stores}
    for s in stores:
        if not s.get("label"):
            raise ValueError(
                "store-audit %r store %r has no label. The label is the whole "
                "chip — a store a student cannot read is a store they cannot "
                "learn." % (act_id, s.get("id")))

    for sc in scenarios:
        for key in ("label", "text", "verdict"):
            if not sc.get(key):
                raise ValueError(
                    "store-audit %r scenario %r has no %r. The label names the "
                    "button, the text is the situation being judged, and the "
                    "verdict is the only place the physics is actually "
                    "explained — a missing one leaves a ledger that marks and "
                    "never teaches." % (act_id, sc.get("id"), key))
        for side in ("before", "after"):
            picked = sc.get(side)
            if not picked:
                raise ValueError(
                    "store-audit %r scenario %r has nothing filled %s. A side "
                    "with no store is not a situation energy can be in."
                    % (act_id, sc["id"], side))
            unknown = [p for p in picked if p not in known]
            if unknown:
                raise ValueError(
                    "store-audit %r scenario %r names %s in its %s side, and "
                    "no chip carries that id. The student would be asked for "
                    "a tick they cannot make."
                    % (act_id, sc["id"], unknown, side))
        if set(sc["before"]) == set(sc["after"]):
            raise ValueError(
                "store-audit %r scenario %r fills the same stores before and "
                "after. Nothing transferred, so there is nothing to audit."
                % (act_id, sc["id"]))

    target = int(a.get("ledgers_to_balance") or 0)
    if not 2 <= target <= len(scenarios):
        raise ValueError(
            "store-audit %r ticks its rail stop at %r of %d ledger(s). Two is "
            "the fewest that shows the ledger working on more than one "
            "situation, and more than the set is a stop that can never tick."
            % (act_id, target, len(scenarios)))

    _count_word_agrees(a.get("heading"), len(stores), act_id,
                       "store-audit", "heading")

    picks = "".join(
        _p1_seg("ks3-saudit-sc", sc["label"], i == 0, data_saudit_sc=sc["id"])
        for i, sc in enumerate(scenarios))

    def column(side, title):
        # ⚠️ THE ANSWER LIVES ON THE CHIP, one attribute per scenario, rather
        # than in a table inside `shared/ks3.js`. `wireStoreAudit` reads
        # `data-saudit-want-<scenario>` off the button it is already holding,
        # so the payload stays the single source of what is true and the
        # wiring cannot drift from it by being transcribed twice.
        def wants(store_id):
            return "".join(
                ' data-saudit-want-%s="%s"' % (e(sc["id"]), side)
                for sc in scenarios if store_id in sc[side])

        chips = "".join(
            '<button type="button" class="ks3-saudit-chip" '
            'data-saudit-chip="%s:%s"%s aria-pressed="false">'
            '<span class="ks3-saudit-chip-label">%s</span>'
            '<span class="ks3-saudit-chip-mark" data-saudit-mark></span>'
            '</button>' % (side, e(st["id"]), wants(st["id"]), t(st["label"]))
            for st in stores)
        return ('<div class="ks3-saudit-col">'
                '<p class="ks3-saudit-coltitle">%s</p>'
                '<div class="ks3-saudit-chips">%s</div></div>'
                % (t(title), chips))

    first = scenarios[0]
    # Every scenario's sentence and verdict are in the document from load and
    # `shared/ks3.js` swaps which is shown. Design keeps them all mounted so
    # that a student with JS off still reads the physics rather than an empty
    # panel; the alternative is a block that is blank until it is scripted.
    texts = "".join(
        '<p class="ks3-saudit-text" data-saudit-text="%s"%s>%s</p>'
        % (e(sc["id"]), "" if i == 0 else " hidden", t(sc["text"]))
        for i, sc in enumerate(scenarios))
    verdicts = "".join(
        '<p class="ks3-saudit-vtext" data-saudit-vtext="%s" hidden>%s</p>'
        % (e(sc["id"]), rich(sc["verdict"])) for sc in scenarios)

    return ('<div class="ks3-saudit" data-saudit data-total="%d" '
            'data-target="%d">'
            '<div class="ks3-saudit-picks">%s</div>'
            '<div class="ks3-saudit-panel">%s'
            '<div class="ks3-saudit-cols">%s%s</div>'
            '<div class="ks3-saudit-acts">'
            '<button type="button" class="ks3-seg-btn ks3-saudit-check" '
            'data-saudit-check>%s</button>'
            '<button type="button" class="ks3-seg-btn ks3-saudit-clear" '
            'data-saudit-clear>%s</button></div>'
            '<div class="ks3-saudit-verdict" data-saudit-verdict hidden>'
            '<p class="ks3-saudit-vlabel" data-saudit-vlabel></p>%s</div>'
            '</div></div>'
            % (len(scenarios), target, picks, texts,
               column("before", a.get("before_title") or "Filled at the start"),
               column("after", a.get("after_title") or "Filled at the end"),
               t(a.get("check_label") or "Check the ledger"),
               t(a.get("clear_label") or "Clear it"),
               verdicts))


# ═══ p1-01 · store-pathway-sort ══════════════════════════════════════════

def r_store_pathway_sort(a, act_id):
    """⊕ p1-01 `#s-think` — six words, each a store or a pathway.

    Design's sorter, sitting inside the misconception block whose quote is
    "A torch turns electrical energy into light energy and sound energy." Two
    of the six words in common use are not stores at all, and the sort is
    where the student finds out which.

    ⚠️ **THIS ONE DOES MARK, AND IT IS NOT AN R3 BREACH.** Every other
    activity on a KS3 page is chosen-never-correct. Design marks here because
    the sort IS the confrontation of the misconception — a student who sorts
    `Electrical` as a store and is told nothing has simply recorded the belief
    the block exists to overturn. What she does NOT do is score it: there is
    no tally, no "4 of 6", and the note under each card is an explanation
    rather than a verdict. The `right`/`wrong` note pair is the mechanism, and
    both are written as physics, not as praise or correction.

    ⚠️ **`store` IS A REQUIRED BOOLEAN, NOT A TRUTHY VALUE.** A missing key
    would read as False and silently teach that a store is a pathway.

    ⚠️ **NOT `cards`.** `r_activity` renders a `cards` payload itself with no
    opt-out, so an instrument authoring that key ships two renderers over one
    payload and the block goes blank. These are `sort_items`.

    HOOKS: `data-spath` (wrapper, `data-total`) ·
    `data-spath-item` (one card, valued with the item id) ·
    `data-spath-pick` (valued `<id>:store` / `<id>:path`) ·
    `data-spath-note` (the card's note) ·
    `data-spath-settle` (the closing panel, revealed when all are sorted).
    """
    items = a.get("sort_items") or []

    if len(items) < 4:
        raise ValueError(
            "store-pathway-sort %r declares %d item(s). The distinction only "
            "lands by being made several times over words a student already "
            "uses, and four is the fewest that is not a coin toss."
            % (act_id, len(items)))
    _unique_ids(items, act_id, "store-pathway-sort", "item")

    for it in items:
        if "store" not in it:
            raise ValueError(
                "store-pathway-sort %r item %r does not say whether it is a "
                "store. A missing key reads as False and would teach that a "
                "store is a pathway." % (act_id, it.get("id")))
        if not isinstance(it["store"], bool):
            raise ValueError(
                "store-pathway-sort %r item %r has `store`=%r. It must be a "
                "real boolean — a truthy string is how a store becomes a "
                "pathway by accident." % (act_id, it["id"], it["store"]))
        for key in ("name", "right", "wrong"):
            if not it.get(key):
                raise ValueError(
                    "store-pathway-sort %r item %r has no %r. The name is the "
                    "card, and BOTH notes are the teaching — the `wrong` note "
                    "is the one that does the work, because it is the only "
                    "thing a student who holds the misconception will read."
                    % (act_id, it["id"], key))

    stores = [i for i in items if i["store"]]
    paths = [i for i in items if not i["store"]]
    if not stores or not paths:
        raise ValueError(
            "store-pathway-sort %r is all %s. A sort with one answer is not a "
            "sort — the student can score full marks by pressing the same "
            "button six times."
            % (act_id, "stores" if paths == [] else "pathways"))

    # ⚠️ NOT `_count_word_agrees` ON THE PROMPT. Design's lead sentence counts
    # the NON-STORES among the words she quotes, not the cards in the grid —
    # "three of them are not stores at all" over six cards is correct, and a
    # row-count check would read it as a contradiction. The number that must
    # agree is the count of pathway items, so that is what is checked.
    said = a.get("prompt") or ""
    n_paths = len(paths)
    word = _COUNT_WORDS.get(n_paths)
    if word and not re.search(r"\b%s\b" % word, said, re.I):
        for m, other in _COUNT_WORDS.items():
            if m != n_paths and re.search(r"\b%s\b" % other, said, re.I):
                raise ValueError(
                    "store-pathway-sort %r says %r in its prompt but %d of "
                    "its items are pathways. The lead sentence counts the "
                    "non-stores, and a number that disagrees with the cards "
                    "below it teaches the opposite of the sort."
                    % (act_id, other, n_paths))

    cards = "".join(
        '<div class="ks3-spath-item" data-spath-item="%s">'
        '<p class="ks3-spath-name">%s</p>'
        '<div class="ks3-spath-picks">'
        '<button type="button" class="ks3-seg-btn ks3-spath-pick" '
        'data-spath-pick="%s:store" aria-pressed="false">%s</button>'
        '<button type="button" class="ks3-seg-btn ks3-spath-pick" '
        'data-spath-pick="%s:path" aria-pressed="false">%s</button>'
        '</div>'
        '<p class="ks3-spath-note" data-spath-note hidden></p>'
        '<p class="ks3-spath-src" data-spath-right hidden>%s</p>'
        '<p class="ks3-spath-src" data-spath-wrong hidden>%s</p>'
        '<span data-spath-is="%s" hidden></span>'
        '</div>'
        % (e(it["id"]), t(it["name"]),
           e(it["id"]), t(a.get("store_label") or "A store"),
           e(it["id"]), t(a.get("path_label") or "A pathway"),
           rich(it["right"]), rich(it["wrong"]),
           "store" if it["store"] else "path")
        for it in items)

    settle = ""
    if a.get("settle"):
        settle = ('<div class="ks3-spath-settle" data-spath-settle hidden>%s'
                  '</div>'
                  % "".join("<p>%s</p>" % rich(p) for p in a["settle"]))

    return ('<div class="ks3-spath" data-spath data-total="%d">'
            '<div class="ks3-spath-grid">%s</div>%s</div>'
            % (len(items), cards, settle))


# ═══ registration ════════════════════════════════════════════════════════
#
# TWO ROWS, because two renderers exist. `ks3_art.check_placements` gate 2
# fails a family registered and never placed and gate 3 fails one placed and
# never registered, so this list and the lessons agreeing is checkable rather
# than promised. Every family is P1's own — `ks3_art/core.py` is untouched.

KIND_SHELL = {
    'store-audit': ("ks3-saudit-block",
                    ' data-instrument data-sauditblock data-stage-done="0"'),
    'store-pathway-sort': ("ks3-spath-block",
                           ' data-instrument data-spathblock '
                           'data-stage-done="0"'),
}

KIND_FN = {
    'store-audit': r_store_audit,
    'store-pathway-sort': r_store_pathway_sort,
}
