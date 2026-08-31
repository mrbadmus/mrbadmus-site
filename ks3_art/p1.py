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

import math
import re

from ks3_art.kit import e, rich, t


# ═══ shared P1 primitives ════════════════════════════════════════════════

def _num(v):
    """A number for a data attribute, without a stray trailing `.0`.

    Heat capacities are authored as real J/K figures and some of them are
    fractional (a 30 g steel spoon is 13.5 J/K). `%d` would truncate the
    physics and `%s` on a float would print `840.0` where the author wrote
    `840`, so the integer case is printed as an integer and everything else
    keeps its decimals.
    """
    f = float(v)
    return "%d" % int(f) if f == int(f) else repr(f)


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


# ═══ p1-02 · before-after-tally ══════════════════════════════════════════

def r_before_after_tally(a, act_id):
    """⊕ p1-02 `#s-tally` — two columns, one total, four devices.

    Design's bench. A student commits to where a filament bulb's missing 57 J
    went, which opens the bench; then picks a device and drags a slider that
    splits its input between the job and the surroundings. The teaching point
    is that the TOTAL never moves however the slider is set — the two columns
    are the same energy counted twice.

    ⚖️ **THE SLIDER IS ALLOWED TO BE PHYSICALLY WRONG, AND THAT IS DESIGN'S
    POINT** (her science flag 5). A student can set a filament bulb to 95%
    useful. The sum still balances, because conservation does not care what
    is efficient. The real figure is named only when they land within
    `near` percent of it, so the bench rewards finding it without ever
    refusing a setting.

    ⚖️ **THE BARS ARE DOM, NOT CANVAS.** Design draws hers on a 1800x620
    canvas. Seventeen built KS3 pages carry a `<canvas>` and the bar
    instruments in every other unit are spans, so the bars are spans here:
    the numbers are then real text a screen reader reaches and a phone can
    scale, which a canvas bar is not. The shape, the three readouts, the
    ordering and every string are hers.

    ⚠️ **`total`, `real` AND THE SUM ARE CHECKED AGAINST EACH OTHER.** A
    device whose note quotes a joule figure the slider can never produce
    teaches arithmetic that does not close, and that is exactly the defect
    this unit exists to confront.

    HOOKS: `data-btally` (wrapper, `data-total`) ·
    `data-btally-gate` (the commit panel) · `data-btally-gopt` (its options,
    valued with the index) · `data-btally-bench` (the panel it opens) ·
    `data-btally-dev` (device button, valued with the device id) ·
    `data-btally-slider` · `data-btally-bar` (valued `useful` / `waste`) ·
    `data-btally-out` (valued `in` / `useful` / `waste`) ·
    `data-btally-sum` · `data-btally-note` · `data-btally-progress`.
    """
    devices = a.get("devices") or []
    gate = a.get("gate") or {}
    slider = a.get("slider") or {}

    if len(devices) < 3:
        raise ValueError(
            "before-after-tally %r offers %d device(s). The claim is that the "
            "total holds for ANY transfer, and one or two cases cannot make "
            "it." % (act_id, len(devices)))

    _unique_ids(devices, act_id, "before-after-tally", "device")
    _no_correct_flags(devices, act_id, "before-after-tally")

    for d in devices:
        for key in ("label", "total", "real", "job", "note"):
            if d.get(key) in (None, "", []):
                raise ValueError(
                    "before-after-tally %r device %r has no %r. The label "
                    "names the button, `total` and `real` are the arithmetic, "
                    "`job` is the store being filled, and the note is the "
                    "only place the physics is explained."
                    % (act_id, d.get("id"), key))
        total, real = int(d["total"]), int(d["real"])
        if total <= 0:
            raise ValueError(
                "before-after-tally %r device %r takes in %d J. A transfer "
                "with nothing going in has no columns to balance."
                % (act_id, d["id"], total))
        if not 0 <= real <= 100:
            raise ValueError(
                "before-after-tally %r device %r declares its real figure as "
                "%r. It is a percentage of the input, so it lives in 0-100."
                % (act_id, d["id"], real))

    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "before-after-tally %r has no commit gate, or fewer than three "
            "options in it. Design opens the bench only after the student has "
            "committed, because a bench read before a commitment confirms "
            "whatever the student already believed." % act_id)
    if gate.get("marks") and gate["marks"] not in {d["id"] for d in devices}:
        raise ValueError(
            "before-after-tally %r gate marks %r as seen and no device "
            "carries that id." % (act_id, gate.get("marks")))

    near = int(slider.get("near") or 0)
    if not 1 <= near <= 20:
        raise ValueError(
            "before-after-tally %r calls the real figure found within %r "
            "percent. Too tight and it can never be hit on a phone; too loose "
            "and every setting is congratulated." % (act_id, near))

    opts = "".join(
        '<button type="button" class="ks3-option" data-btally-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    devs = "".join(
        _p1_seg("ks3-btally-dev", d["label"], i == 0, data_btally_dev=d["id"])
        for i, d in enumerate(devices))

    # Every device's note is mounted from load and `shared/ks3.js` swaps which
    # is shown, for the same reason the store audit mounts all five verdicts:
    # a student with JS off reads the physics rather than an empty panel.
    notes = "".join(
        '<p class="ks3-btally-note" data-btally-note="%s"%s>%s</p>'
        % (e(d["id"]), "" if i == 0 else " hidden", rich(d["note"]))
        for i, d in enumerate(devices))

    data = "".join(
        ' data-btally-total-%s="%d" data-btally-real-%s="%d" '
        'data-btally-job-%s="%s"'
        % (e(d["id"]), int(d["total"]), e(d["id"]), int(d["real"]),
           e(d["id"]), e(d["job"]))
        for d in devices)

    def readout(key, label, accent=False):
        return ('<div class="ks3-btally-out%s">'
                '<p class="ks3-btally-outlabel">%s</p>'
                '<p class="ks3-btally-outval" data-btally-out="%s"></p></div>'
                % (" is-accent" if accent else "", t(label), e(key)))

    return ('<div class="ks3-btally" data-btally data-total="%d" '
            'data-near="%d"%s>'
            '<div class="ks3-btally-gate" data-btally-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-btally-bench" data-btally-bench hidden>'
            '<div class="ks3-btally-devs">%s</div>'
            '<div class="ks3-btally-cols">'
            '<div class="ks3-btally-col"><p class="ks3-btally-coltitle">%s</p>'
            '<span class="ks3-btally-bar is-in" data-btally-bar="in"></span>'
            '</div>'
            '<div class="ks3-btally-col"><p class="ks3-btally-coltitle">%s</p>'
            '<span class="ks3-btally-bar is-useful" data-btally-bar="useful">'
            '</span>'
            '<span class="ks3-btally-bar is-waste" data-btally-bar="waste">'
            '</span></div></div>'
            '<label class="ks3-btally-sliderlabel" for="%s-useful" '
            'data-btally-sliderlabel></label>'
            '<input class="ks3-btally-slider" id="%s-useful" type="range" '
            'min="%d" max="%d" step="%d" value="%d" data-btally-slider>'
            '<div class="ks3-btally-outs">%s%s%s</div>'
            '<p class="ks3-btally-sum" data-btally-sum></p>%s</div></div>'
            % (len(devices), near, data,
               t(gate["prompt"]), opts, devs,
               t(a.get("before_title") or "Before"),
               t(a.get("after_title") or "After"),
               e(act_id), e(act_id),
               int(slider.get("min", 0)), int(slider.get("max", 100)),
               int(slider.get("step", 1)), int(slider.get("start", 50)),
               readout("in", "In, from the store"),
               readout("useful", "Doing the job", True),
               readout("waste", "Into the surroundings"),
               notes))


# ═══ p1-02 · waste-sort ══════════════════════════════════════════════════

def r_waste_sort(a, act_id):
    """⊕ p1-02 `#s-waste` — four situations, two verdicts, identical physics.

    Design's block. Each card names a device warming its surroundings and the
    student says whether that is a problem or the entire point. The bulb and
    the heater are the pair the section turns on: the same joules in the same
    store, opposite verdicts, because the verdict is about intent.

    ⚖️ **THE CLOSING PANEL IS WITHHELD UNTIL EVERY CARD IS ANSWERED**, the
    same rule the store/pathway sort uses. It names what all four cards have
    just shown, so it has nothing to say until they have shown it.

    ⚠️ **THE PAYLOAD KEY IS `sort_items`, NEVER `cards`.** `cards` is claimed
    by `r_activity`, which renders it itself with no opt-out, so a payload
    carrying that name gets a second blank flip-card renderer stacked on this
    one and the block ships doubled.

    HOOKS: `data-wsort` (wrapper, `data-total`) · `data-wsort-card` (valued
    with the item id) · `data-wsort-pick` (valued `<id>:<choice index>`) ·
    `data-wsort-note` · `data-wsort-settle`.
    """
    items = a.get("sort_items") or []
    choices = a.get("choices") or []

    if len(items) < 3:
        raise ValueError(
            "waste-sort %r offers %d card(s). The point is made by a PAIR "
            "with identical physics and opposite verdicts, so three is the "
            "fewest that can carry one and still generalise."
            % (act_id, len(items)))
    if len(choices) != 2:
        raise ValueError(
            "waste-sort %r declares %d verdict(s). The sort is binary — "
            "wasted or the point — and a third button is a different "
            "instrument." % (act_id, len(choices)))

    _unique_ids(items, act_id, "waste-sort", "card")
    _no_correct_flags(items, act_id, "waste-sort")

    for it in items:
        for key in ("text", "answer", "right", "wrong"):
            if not it.get(key):
                raise ValueError(
                    "waste-sort %r card %r has no %r. Both notes are needed: "
                    "a card that explains itself only when the student was "
                    "already right teaches nobody who was wrong."
                    % (act_id, it.get("id"), key))
        if it["answer"] not in choices:
            raise ValueError(
                "waste-sort %r card %r answers %r, which is not one of the "
                "two verdicts %r." % (act_id, it["id"], it["answer"], choices))

    if len({it["answer"] for it in items}) < 2:
        raise ValueError(
            "waste-sort %r sorts every card into the same verdict. The whole "
            "lesson is that identical physics gets opposite verdicts, and a "
            "one-sided set teaches the reverse." % act_id)

    cards = "".join(
        '<div class="ks3-wsort-card" data-wsort-card="%s">'
        '<p class="ks3-wsort-text">%s</p>'
        '<div class="ks3-wsort-picks">%s</div>'
        '<p class="ks3-wsort-note" data-wsort-note hidden></p>'
        '<template data-wsort-right>%s</template>'
        '<template data-wsort-wrong>%s</template></div>'
        % (e(it["id"]), t(it["text"]),
           "".join(
               '<button type="button" class="ks3-seg-btn ks3-wsort-pick" '
               'data-wsort-pick="%s:%d" aria-pressed="false">%s</button>'
               % (e(it["id"]), i, t(c)) for i, c in enumerate(choices)),
           rich(it["right"]), rich(it["wrong"]))
        for it in items)

    want = "".join(
        ' data-wsort-want-%s="%d"' % (e(it["id"]), choices.index(it["answer"]))
        for it in items)

    settle = ""
    if a.get("close"):
        settle = ('<div class="ks3-wsort-settle" data-wsort-settle hidden>'
                  '<p>%s</p></div>' % rich(a["close"]))

    return ('<div class="ks3-wsort" data-wsort data-total="%d"%s>'
            '<div class="ks3-wsort-grid">%s</div>%s</div>'
            % (len(items), want, cards, settle))


# ═══ p1-03 · running-total ═══════════════════════════════════════════════

def r_running_total(a, act_id):
    """⊕ p1-03 `#s-bench` — a pendulum, four readouts, one total that holds.

    Design's bench. A student commits to which store is largest at the bottom
    of the swing, then releases the pendulum and watches three stores trade
    while the total never moves. Two switches make the point the other way
    round: friction off, and — the important one — the thermal store HIDDEN.

    ⚖️ **THE HIDE-THERMAL CONTROL DELIBERATELY MAKES THE LAW LOOK FALSE**
    (Design's science flag 7). With the thermal store hidden the bar stops
    reaching the total line, and conservation appears to fail. That IS the
    confrontation of `ENER-12` — the belief that a quantity which stops being
    visible has stopped existing — and it must not be removed as a
    "confusing" control. It is the whole argument of the lesson in one
    button.

    ⚖️ **FRICTION-OFF IS PHYSICALLY IMPOSSIBLE AND SAYS SO** (her flag 8).
    Its note names it as idealised rather than presenting a real pendulum
    that never stops.

    ⚠️ **THE TOTAL IS DERIVED, NEVER STORED.** `grav + kin + therm` is summed
    on every paint and compared against `total`; if the three ever fail to
    make the whole, the bench is asserting the opposite of what the lesson
    claims. The renderer refuses a payload whose notes are missing, because
    a bench that shows the law without ever saying what you are looking at
    teaches nothing to the student who did not already know.

    HOOKS: `data-rtotal` (wrapper, `data-total`) · `data-rtotal-gate` ·
    `data-rtotal-gopt` · `data-rtotal-bench` · `data-rtotal-ctl` (valued with
    the control id) · `data-rtotal-out` (valued with the readout id) ·
    `data-rtotal-bar` (valued with the store id) · `data-rtotal-note`.
    """
    gate = a.get("gate") or {}
    controls = a.get("controls") or []
    readouts = a.get("readouts") or []
    notes = a.get("notes") or {}
    total = int(a.get("total") or 0)

    if total <= 0:
        raise ValueError(
            "running-total %r keeps score on a total of %r. The bench exists "
            "to show a fixed number holding, and it needs one."
            % (act_id, a.get("total")))

    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "running-total %r has no commit gate, or fewer than three "
            "options. A bench read before a commitment confirms whatever the "
            "student already believed." % act_id)

    want_ctl = {"run", "reset", "friction", "hide"}
    have = {c.get("id") for c in controls}
    if want_ctl - have:
        raise ValueError(
            "running-total %r is missing the %s control(s). `hide` in "
            "particular is not optional — it is the confrontation of the "
            "lesson's misconception, and a bench without it only ever shows "
            "the law working." % (act_id, sorted(want_ctl - have)))

    want_out = {"grav", "kin", "therm", "total"}
    if want_out - {r.get("id") for r in readouts}:
        raise ValueError(
            "running-total %r is missing the %s readout(s). The total is one "
            "of them: without it on screen the student is asked to add three "
            "moving numbers in their head."
            % (act_id, sorted(want_out - {r.get("id") for r in readouts})))

    # ⚖️ `fresh` IS REQUIRED, AND IT IS THE P1-9 NOTE. A reset after a
    # completed run puts the bar back to the full total, which is the one
    # moment on this bench where energy appears to come back out of the
    # surroundings. The note is what stops that reading: the room keeps the
    # last run's energy, and the count is starting again. Without it the
    # reset is silent and the student is left to infer the wrong thing.
    for key in ("rest", "running", "stopped", "no_friction", "hidden",
                "fresh"):
        if not notes.get(key):
            raise ValueError(
                "running-total %r has no %r note. Each names what the bench "
                "is showing in that state, the `hidden` one carries the "
                "argument, and the `fresh` one is the only thing that stops "
                "a reset reading as energy coming back." % (act_id, key))

    _unique_ids(controls, act_id, "running-total", "control")
    _unique_ids(readouts, act_id, "running-total", "readout")
    _no_correct_flags(controls, act_id, "running-total")

    # ⚠️ THE COUNT WORD IN THE HEADING MUST MATCH THE BARS DRAWN.
    # Design's heading read "Four stores. One total that never moves." above a
    # bench that draws THREE (`GRAV`, `KIN`, `THERMAL`) plus a Total readout.
    # That is the second count-word/instrument disagreement in P1 — the first
    # is `p1-01`'s "two of them are not stores at all" over a sort with three
    # non-stores. Both were caught by counting rather than reading, so the
    # third one is caught here instead. `total` is a SUM and is excluded from
    # the count on purpose: it is not one of the stores.
    _count_word_agrees(a.get("heading"),
                       len([r for r in readouts if r["id"] != "total"]),
                       act_id, "running-total", "heading")

    opts = "".join(
        '<button type="button" class="ks3-option" data-rtotal-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    ctls = "".join(
        '<button type="button" class="ks3-seg-btn ks3-rtotal-ctl" '
        'data-rtotal-ctl="%s"%s aria-pressed="false">%s</button>'
        % (e(c["id"]),
           (' data-rtotal-alt="%s"' % e(c["alt"])) if c.get("alt") else "",
           t(c["label"]))
        for c in controls)

    outs = "".join(
        '<div class="ks3-rtotal-out%s"><p class="ks3-rtotal-outlabel">%s</p>'
        '<p class="ks3-rtotal-outval" data-rtotal-out="%s"></p></div>'
        % (" is-accent" if r.get("accent") else "", t(r["label"]), e(r["id"]))
        for r in readouts)

    bars = "".join(
        '<span class="ks3-rtotal-bar is-%s" data-rtotal-bar="%s"></span>'
        % (e(r["id"]), e(r["id"]))
        for r in readouts if r["id"] != "total")

    notemarks = "".join(
        '<p class="ks3-rtotal-note" data-rtotal-note="%s"%s>%s</p>'
        % (e(k), "" if k == "rest" else " hidden", rich(v))
        for k, v in (("rest", notes["rest"]), ("running", notes["running"]),
                     ("stopped", notes["stopped"]),
                     ("no_friction", notes["no_friction"]),
                     ("hidden", notes["hidden"]),
                     ("fresh", notes["fresh"])))

    return ('<div class="ks3-rtotal" data-rtotal data-total="%d">'
            '<div class="ks3-rtotal-gate" data-rtotal-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-rtotal-bench" data-rtotal-bench hidden>'
            '<div class="ks3-rtotal-stack">'
            '<span class="ks3-rtotal-line" aria-hidden="true"></span>%s</div>'
            '<div class="ks3-rtotal-outs">%s</div>'
            '<div class="ks3-rtotal-ctls">%s</div>%s</div></div>'
            % (total, t(gate["prompt"]), opts, bars, outs, ctls, notemarks))


# ═══ p1-03 · conservation-beam ═══════════════════════════════════════════

def r_conservation_beam(a, act_id):
    """⊕ p1-03 `#s-balance` — the unit's first formula block, and a BEAM.

    ⚖️ **MRB-204 · BEAM, NOT TRIANGLE, AND DESIGN ARGUES IT ON THE PAGE.**
    Her heading is literally *"Conservation is a balance, not a triangle"*.
    A triangle encodes `A = B × C`; conservation is a SUM on each side of an
    equals sign, and a triangle over it teaches a relationship that does not
    exist. This is the `c2-06` precedent (NOTES-C2 §8 flag 14) applied to
    energy.

    ⚠️ **THE SPLITS ARE CHECKED AGAINST THE TOTAL, EVERY ONE.** A beam whose
    pans do not balance is a beam that lies, and this block's entire claim is
    that they always do. Design's four are 120=120+0+0, 120=62+55+3,
    120=0+114+6 and 120=0+0+120.

    ⊖ **WHY THIS IS AN INSTRUMENT AND NOT THE ENGINE'S `formula` BLOCK.**
    `build_ks3`'s `{"type": "formula"}` supports `figure.shape = "balance"`
    and is the right home for a STATIC rule — it is what `c2-06` uses. Design's
    block here is not static: it carries four configuration buttons and a
    different note under each, and the teaching is watching the beam stay
    level ACROSS them. The static figure cannot express that, so the shape
    she drew is rendered as an instrument. The shape itself is unchanged, and
    it is still a beam over a sum.

    HOOKS: `data-cbeam` (wrapper, `data-total`) · `data-cbeam-split` (valued
    with the split id) · `data-cbeam-pan` (valued `left` / `right`) ·
    `data-cbeam-seg` (valued with the store key) · `data-cbeam-note`.
    """
    splits = a.get("splits") or []
    total = int(a.get("total") or 0)

    if len(splits) < 3:
        raise ValueError(
            "conservation-beam %r offers %d configuration(s). The claim is "
            "that the beam is level in EVERY one, and that needs more than a "
            "before and an after." % (act_id, len(splits)))
    if total <= 0:
        raise ValueError(
            "conservation-beam %r has no total to balance against."
            % act_id)

    _unique_ids(splits, act_id, "conservation-beam", "split")
    _no_correct_flags(splits, act_id, "conservation-beam")

    keys = ("grav", "kin", "therm")
    for s in splits:
        if not s.get("label") or not s.get("note"):
            raise ValueError(
                "conservation-beam %r split %r has no label or no note. The "
                "note is the only place each configuration is explained."
                % (act_id, s.get("id")))
        got = sum(int(s.get(k) or 0) for k in keys)
        if got != total:
            raise ValueError(
                "conservation-beam %r split %r sums to %d and the beam is "
                "drawn against %d. The one thing this block asserts is that "
                "the pans match, so a split that does not add up is the "
                "block contradicting itself."
                % (act_id, s["id"], got, total))

    picks = "".join(
        _p1_seg("ks3-cbeam-split", s["label"], i == 0, data_cbeam_split=s["id"])
        for i, s in enumerate(splits))

    data = "".join(
        "".join(' data-cbeam-%s-%s="%d"' % (e(k), e(s["id"]), int(s.get(k) or 0))
                for k in keys)
        for s in splits)

    segs = "".join(
        '<span class="ks3-cbeam-seg is-%s" data-cbeam-seg="%s"></span>'
        % (e(k), e(k)) for k in keys)

    notes = "".join(
        '<p class="ks3-cbeam-note" data-cbeam-note="%s"%s>%s</p>'
        % (e(s["id"]), "" if i == 0 else " hidden", rich(s["note"]))
        for i, s in enumerate(splits))

    return ('<div class="ks3-cbeam" data-cbeam data-total="%d"%s>'
            '<div class="ks3-cbeam-picks">%s</div>'
            '<div class="ks3-cbeam-rig" role="img" aria-label="%s">'
            '<span class="ks3-cbeam-beam" aria-hidden="true"></span>'
            '<div class="ks3-cbeam-pans">'
            '<div class="ks3-cbeam-pan" data-cbeam-pan="left">'
            '<span class="ks3-cbeam-seg is-whole"></span>'
            '<p class="ks3-cbeam-panlabel">%s J, before</p></div>'
            '<div class="ks3-cbeam-pan" data-cbeam-pan="right">%s'
            '<p class="ks3-cbeam-panlabel">the same %s J, shared out</p>'
            '</div></div>'
            '<p class="ks3-cbeam-caption">always level</p></div>'
            '<p class="ks3-cbeam-ctl">%s</p>%s</div>'
            % (total, data, picks, t(a.get("alt") or ""),
               total, segs, total,
               t(a.get("control_label") or ""), notes))


# ═══ p1-04 · two-quantities ══════════════════════════════════════════════

def r_two_quantities(a, act_id):
    """⊕ p1-04 `#s-two` — two axes, moved one at a time.

    Design's bench. A student sets HOW MUCH there is (a spark, a mug, a bath)
    and HOW FAST its particles move, and watches two readouts respond
    differently: temperature answers only to speed, the thermal store answers
    to both. That asymmetry is the whole lesson and it is why the bench has
    two independent controls rather than one.

    ⚖️ **THE THERMAL BAR IS LOGARITHMIC AND SAYS SO** (Design's science flag
    10). p1-04's bench runs from 0.009 J to 627 MJ, a range of about 10^11 —
    a linear bar leaves the spark at zero pixels and teaches that a spark has
    no energy at all, which is the opposite of the point. The scale note is
    not decoration and the renderer refuses a payload without it: a log axis
    a student has not been told about is a lie told in a picture.

    ⚠️ **`n` IS A HEAT CAPACITY IN J/K, NOT AN INDEX.** The engine prints
    `n × t` as joules, so an authored `n` that is a made-up "particle count"
    prints a made-up energy. It was one once (3 / 22 / 60), and the bench
    then showed a spark out-holding a bath while the paragraph underneath
    said the opposite (MRB-297, finding P1-13). Hence the ordering guard
    below, and hence `n` is emitted as a float — `int()` destroys 0.00045.

    ⚖️ **THE ORDERING GUARD IS THE LESSON.** The biggest amount at the
    COLDEST setting must beat the smallest amount at the HOTTEST setting.
    That inequality is the entire claim the bench exists to demonstrate; a
    payload that breaks it is a bench arguing against its own page.

    ⚠️ **BOTH AXES MUST OFFER AT LEAST THREE SETTINGS.** With two, "moved it
    and the other readout did not follow" is a coincidence a student can
    dismiss; with three it is a pattern.

    HOOKS: `data-twoq` (wrapper) · `data-twoq-amt` (amount button, valued
    with the amount id) · `data-twoq-spd` (speed button, valued with the
    speed id) · `data-twoq-out` (valued `temp` / `store`) ·
    `data-twoq-bar` · `data-twoq-scale` · `data-twoq-close`.
    """
    amounts = a.get("amounts") or []
    speeds = a.get("speeds") or []
    readouts = a.get("readouts") or []

    if len(amounts) < 3 or len(speeds) < 3:
        raise ValueError(
            "two-quantities %r offers %d amount(s) and %d speed(s). The "
            "claim is that one axis moves a readout the other does not, and "
            "two settings make that a coincidence rather than a pattern."
            % (act_id, len(amounts), len(speeds)))

    if not a.get("scale_note"):
        raise ValueError(
            "two-quantities %r has no `scale_note`. The thermal bar is "
            "logarithmic — p1-04's bench spans about 10^11 — and a log "
            "axis the student has not been told about is a lie told in a "
            "picture." % act_id)

    _unique_ids(amounts, act_id, "two-quantities", "amount")
    _unique_ids(speeds, act_id, "two-quantities", "speed")
    _no_correct_flags(amounts, act_id, "two-quantities")
    _no_correct_flags(speeds, act_id, "two-quantities")

    for x in amounts:
        for key in ("label", "n", "tag"):
            if x.get(key) in (None, "", []):
                raise ValueError(
                    "two-quantities %r amount %r has no %r. The tag is what "
                    "makes the amount concrete — “300 g” rather "
                    "than a bar of unknown size."
                    % (act_id, x.get("id"), key))
    for x in speeds:
        if not x.get("label") or x.get("t") in (None, ""):
            raise ValueError(
                "two-quantities %r speed %r has no label or no temperature."
                % (act_id, x.get("id")))

    # ⚖️ THE ORDERING IS THE LESSON — see the docstring. The biggest amount
    # at the coldest setting must hold MORE than the smallest amount at the
    # hottest setting, because that is the sentence the bench is under.
    big = max(amounts, key=lambda x: float(x["n"]))
    small = min(amounts, key=lambda x: float(x["n"]))
    cold = min(speeds, key=lambda x: float(x["t"]))
    hot = max(speeds, key=lambda x: float(x["t"]))
    coldest_big = float(big["n"]) * float(cold["t"])
    hottest_small = float(small["n"]) * float(hot["t"])
    if not coldest_big > hottest_small:
        raise ValueError(
            "two-quantities %r inverts its own lesson: %s at %s (%g J) does "
            "not beat %s at %s (%g J). The bench exists to show that the "
            "coldest large thing holds more than the hottest small one, and "
            "the closing paragraph under it says so in words. `n` is a heat "
            "capacity in joules per kelvin (mass × specific heat capacity) — "
            "if it has been authored as a made-up particle index, the "
            "readout prints a made-up energy and the page argues with "
            "itself."
            % (act_id, big.get("id"), cold.get("id"), coldest_big,
               small.get("id"), hot.get("id"), hottest_small))

    want = {"temp", "store"}
    if want - {r.get("id") for r in readouts}:
        raise ValueError(
            "two-quantities %r is missing the %s readout(s). Both are the "
            "instrument: one of them is what the student thinks the other "
            "one means."
            % (act_id, sorted(want - {r.get("id") for r in readouts})))

    amts = "".join(
        _p1_seg("ks3-twoq-amt", "%s · %s" % (x["label"], x["tag"]), i == 0,
                data_twoq_amt=x["id"])
        for i, x in enumerate(amounts))
    spds = "".join(
        _p1_seg("ks3-twoq-spd", x["label"], i == 1 if len(speeds) > 1 else i == 0,
                data_twoq_spd=x["id"])
        for i, x in enumerate(speeds))

    # ⚠️ FLOAT, NOT `int()`. `n` is a heat capacity in J/K and the spark's is
    # 0.00045 — `int()` rounds it to zero and the spark loses its energy
    # entirely. %.10g keeps every authored digit without exponent notation.
    data = "".join(' data-twoq-n-%s="%.10g"' % (e(x["id"]), float(x["n"]))
                   for x in amounts)
    data += "".join(' data-twoq-t-%s="%d"' % (e(x["id"]), int(x["t"]))
                    for x in speeds)
    # The bench's OWN reachable extremes, so the log bar is normalised over
    # exactly the range this bench can reach rather than a hard-coded factor
    # that saturates somewhere arbitrary.
    data += ' data-twoq-min="%.10g" data-twoq-max="%.10g"' % (
        float(small["n"]) * float(cold["t"]),
        float(big["n"]) * float(hot["t"]))

    outs = "".join(
        '<div class="ks3-twoq-out%s"><p class="ks3-twoq-outlabel">%s</p>'
        '<p class="ks3-twoq-outval" data-twoq-out="%s"></p></div>'
        % (" is-accent" if r.get("accent") else "", t(r["label"]), e(r["id"]))
        for r in readouts)

    close = ""
    if a.get("close"):
        close = ('<p class="ks3-twoq-close" data-twoq-close>%s</p>'
                 % rich(a["close"]))

    return ('<div class="ks3-twoq" data-twoq%s>'
            '<div class="ks3-twoq-axis"><p class="ks3-twoq-axislabel">'
            'How much there is</p><div class="ks3-twoq-btns">%s</div></div>'
            '<div class="ks3-twoq-axis"><p class="ks3-twoq-axislabel">'
            'How fast the particles move</p>'
            '<div class="ks3-twoq-btns">%s</div></div>'
            '<div class="ks3-twoq-outs">%s</div>'
            '<span class="ks3-twoq-bar" data-twoq-bar></span>'
            '<p class="ks3-twoq-scale" data-twoq-scale>%s</p>%s</div>'
            % (data, amts, spds, outs, t(a["scale_note"]), close))


# ═══ p1-04 · one-way-flow ════════════════════════════════════════════════

def r_one_way_flow(a, act_id):
    """⊕ p1-04 `#s-flow` — three pairs, one arrow, and one arrow that isn't.

    Design's bench. Each pair is two objects at stated temperatures; running
    it shows energy crossing from the hotter to the colder until they match.

    ⚖️ **THE ARROW THAT DOES NOT EXIST IS DRAWN, AND LABELLED AS NOT
    EXISTING** (Design's science flag 11). A dashed ghost arrow points the
    wrong way with the caption *no cold travels this way*. Drawing the thing
    that does not happen IS the confrontation of `ENER-14` — a student who
    believes cold flows needs to see that belief on the screen and struck
    out, not merely omitted. It must not be tidied away as a contradictory
    label, and the renderer requires the caption.

    ⚠️ **ONE PAIR MUST START EQUAL.** Thermal equilibrium is not "what
    happens at the end" — it is a state, and the only way to show it is a
    state rather than an ending is to offer a pair that is already in it and
    watch nothing happen. Design's third pair is two blocks at 30 °C and the
    renderer refuses a set without an equal pair, because a bench where every
    run ends in equilibrium teaches equilibrium as an outcome.

    HOOKS: `data-oflow` (wrapper) · `data-oflow-pair` (valued with the pair
    id) · `data-oflow-run` · `data-oflow-arrow` · `data-oflow-ghost` ·
    `data-oflow-temp` (valued `hot` / `cold`) · `data-oflow-note`.
    """
    pairs = a.get("pairs") or []

    if len(pairs) < 3:
        raise ValueError(
            "one-way-flow %r offers %d pair(s). Three is the fewest that can "
            "show a big difference, a small one and none at all."
            % (act_id, len(pairs)))
    if not a.get("ghost_label"):
        raise ValueError(
            "one-way-flow %r has no `ghost_label`. The arrow that does not "
            "exist is drawn and captioned on purpose — it is the "
            "confrontation of the lesson's misconception, and without the "
            "caption it is simply a second arrow pointing the wrong way."
            % act_id)

    _unique_ids(pairs, act_id, "one-way-flow", "pair")
    _no_correct_flags(pairs, act_id, "one-way-flow")

    for p in pairs:
        for key in ("label", "hot_name", "cold_name", "note"):
            if not p.get(key):
                raise ValueError(
                    "one-way-flow %r pair %r has no %r."
                    % (act_id, p.get("id"), key))
        if p.get("hot") is None or p.get("cold") is None:
            raise ValueError(
                "one-way-flow %r pair %r has no temperatures. The direction "
                "of the arrow is derived from them, never authored, so that "
                "a pair cannot be drawn flowing the wrong way."
                % (act_id, p["id"]))
        if int(p["hot"]) < int(p["cold"]):
            raise ValueError(
                "one-way-flow %r pair %r names its colder object as `hot`. "
                "The keys are roles, not labels, and swapping them would "
                "draw the arrow backwards."
                % (act_id, p["id"]))
        # ⚖️ SCIENCE · A PAIR WITHOUT CAPACITIES SETTLES AT THE HALFWAY
        # POINT, WHICH IS ONLY TRUE OF TWO EQUAL BODIES. The bench ran that
        # way once and put a hot spoon and a beaker of water level at 38 °C
        # under a note saying the water barely warms. Where the pair meets
        # is the whole subject of this instrument, so the weighting is
        # required rather than defaulted.
        for key in ("hot_cap", "cold_cap"):
            cap = p.get(key)
            if cap is None or float(cap) <= 0:
                raise ValueError(
                    "one-way-flow %r pair %r has no positive %r. Each body "
                    "needs a heat capacity in J/K: the pair settles at the "
                    "capacity-weighted mean, and without one the bench "
                    "shows every pair meeting halfway, which is true only "
                    "of two identical objects."
                    % (act_id, p["id"], key))

    if not any(int(p["hot"]) == int(p["cold"]) for p in pairs):
        raise ValueError(
            "one-way-flow %r has no pair that starts EQUAL. Equilibrium is a "
            "state, not an ending, and the only way to show that is a pair "
            "already in it where nothing happens. Without one the bench "
            "teaches equilibrium as the outcome of every run."
            % act_id)

    picks = "".join(
        _p1_seg("ks3-oflow-pair", p["label"], i == 0, data_oflow_pair=p["id"])
        for i, p in enumerate(pairs))

    data = "".join(
        ' data-oflow-hot-%s="%d" data-oflow-cold-%s="%d" '
        'data-oflow-hotcap-%s="%s" data-oflow-coldcap-%s="%s" '
        'data-oflow-hotname-%s="%s" data-oflow-coldname-%s="%s"'
        % (e(p["id"]), int(p["hot"]), e(p["id"]), int(p["cold"]),
           e(p["id"]), _num(p["hot_cap"]), e(p["id"]), _num(p["cold_cap"]),
           e(p["id"]), e(p["hot_name"]), e(p["id"]), e(p["cold_name"]))
        for p in pairs)

    notes = "".join(
        '<p class="ks3-oflow-note" data-oflow-note="%s"%s>%s</p>'
        % (e(p["id"]), "" if i == 0 else " hidden", rich(p["note"]))
        for i, p in enumerate(pairs))

    return ('<div class="ks3-oflow" data-oflow%s>'
            '<div class="ks3-oflow-picks">%s</div>'
            '<div class="ks3-oflow-rig">'
            '<div class="ks3-oflow-body is-hot">'
            '<p class="ks3-oflow-name" data-oflow-name="hot"></p>'
            '<p class="ks3-oflow-temp" data-oflow-temp="hot"></p></div>'
            '<div class="ks3-oflow-arrows">'
            '<span class="ks3-oflow-arrow" data-oflow-arrow aria-hidden="true">'
            '</span>'
            '<span class="ks3-oflow-ghost" data-oflow-ghost aria-hidden="true">'
            '</span>'
            '<p class="ks3-oflow-ghostlabel">%s</p></div>'
            '<div class="ks3-oflow-body is-cold">'
            '<p class="ks3-oflow-name" data-oflow-name="cold"></p>'
            '<p class="ks3-oflow-temp" data-oflow-temp="cold"></p></div>'
            '</div>'
            '<button type="button" class="ks3-seg-btn ks3-oflow-run" '
            'data-oflow-run>Run it</button>%s</div>'
            % (data, picks, t(a["ghost_label"]), notes))


# ═══ p1-05 · conduction-bench ════════════════════════════════════════════

def r_conduction_bench(a, act_id):
    """⊕ p1-05 `#s-bar` — four rods, one flame, four very different times.

    Design's bench. A student picks a material, lights the flame and watches
    a wax blob at the far end. The times differ by more than an order of
    magnitude and wood never gets there at all.

    ⚖️ **THE TIMES ARE ILLUSTRATIVE AND THE BENCH SAYS SO** (Design's science
    flag 15). Her own note: *"ratios are right; absolute values need review
    before any claim of realism"*. `model_note` is required rather than
    optional — a bench that quotes seconds without saying what they are worth
    is making a measurement claim nobody has checked.

    ⚖️ **THE HOME-POSITION RINGS ARE REQUIRED** (her flag 13). Grey rings mark
    where each particle started, and every particle stays on its own. Rung 3
    criterion 3 is *"says the particles themselves do not travel along the
    spoon"* — the rings are the evidence for it and are not decoration.

    ⚖️ **FREE ELECTRONS ARE SHOWN ONLY FOR METALS, AND THE CONTROL SAYS SO**
    (her flag 14). Pressing it on a non-metal must produce a SENTENCE, not
    nothing — a control that silently does nothing reads as broken and
    teaches that the page is unreliable rather than that non-metals lack
    free electrons.

    ⚠️ **`wax: None` IS "NEVER", NOT "MISSING".** Wood's far end never
    reaches the wax, and that is the result rather than an absent value. A
    renderer that treated it as 0 would show wood as the fastest.

    HOOKS: `data-cbench` · `data-cbench-mat` · `data-cbench-run` ·
    `data-cbench-elec` · `data-cbench-rod` · `data-cbench-wax` ·
    `data-cbench-clock` · `data-cbench-note` · `data-cbench-elecnote`.
    """
    materials = a.get("materials") or []
    elec = a.get("electrons") or {}

    if len(materials) < 3:
        raise ValueError(
            "conduction-bench %r races %d material(s). The point is an ORDER "
            "across a wide range, and two rods cannot show one."
            % (act_id, len(materials)))
    if not a.get("model_note"):
        raise ValueError(
            "conduction-bench %r has no `model_note`. Its times are "
            "illustrative rather than measured (Design's flag 15), and a "
            "bench that quotes seconds without saying so is making a "
            "measurement claim nobody has checked." % act_id)
    if not a.get("home_ring_note"):
        raise ValueError(
            "conduction-bench %r has no `home_ring_note`. The grey rings are "
            "the evidence for Rung 3's third criterion — that the particles "
            "do not travel — and an unexplained ring teaches nothing."
            % act_id)
    for key in ("label", "alt", "non_metal_note"):
        if not elec.get(key):
            raise ValueError(
                "conduction-bench %r's `electrons` control has no %r. On a "
                "non-metal the control must SAY there is nothing to show; a "
                "button that silently does nothing reads as broken."
                % (act_id, key))

    _unique_ids(materials, act_id, "conduction-bench", "material")
    _no_correct_flags(materials, act_id, "conduction-bench")

    if not any(m.get("metal") for m in materials):
        raise ValueError(
            "conduction-bench %r has no metal in it. The whole lesson is that "
            "metals have a SECOND route, and a bench with nothing to compare "
            "cannot show one." % act_id)
    if not any(not m.get("metal") for m in materials):
        raise ValueError(
            "conduction-bench %r has no non-metal in it, so the free-electron "
            "control can never say what it is for." % act_id)

    for m in materials:
        if not m.get("label") or not m.get("note"):
            raise ValueError(
                "conduction-bench %r material %r has no label or note."
                % (act_id, m.get("id")))
        w = m.get("wax", "missing")
        if w != "missing" and w is not None and int(w) <= 0:
            raise ValueError(
                "conduction-bench %r material %r melts the wax in %r "
                "seconds. Use None for “never”; a zero or negative "
                "time would draw it as the FASTEST rod on the bench."
                % (act_id, m["id"], w))

    _count_word_agrees(a.get("heading"), len(materials), act_id,
                       "conduction-bench", "heading")

    picks = "".join(
        _p1_seg("ks3-cbench-mat", m["label"], i == 0, data_cbench_mat=m["id"])
        for i, m in enumerate(materials))

    data = "".join(
        ' data-cbench-wax-%s="%s" data-cbench-metal-%s="%s"'
        % (e(m["id"]), "never" if m.get("wax") is None else int(m["wax"]),
           e(m["id"]), "1" if m.get("metal") else "0")
        for m in materials)

    notes = "".join(
        '<p class="ks3-cbench-note" data-cbench-note="%s"%s>%s</p>'
        % (e(m["id"]), "" if i == 0 else " hidden", rich(m["note"]))
        for i, m in enumerate(materials))

    return ('<div class="ks3-cbench" data-cbench%s>'
            '<div class="ks3-cbench-picks">%s</div>'
            '<div class="ks3-cbench-rig">'
            '<div class="ks3-cbench-rod" data-cbench-rod>'
            '<span class="ks3-cbench-flame" aria-hidden="true"></span>'
            '<span class="ks3-cbench-wax" data-cbench-wax></span></div>'
            '<p class="ks3-cbench-rings">%s</p></div>'
            '<div class="ks3-cbench-ctls">'
            '<button type="button" class="ks3-seg-btn ks3-cbench-run" '
            'data-cbench-run>Light the flame</button>'
            '<button type="button" class="ks3-seg-btn ks3-cbench-elec" '
            'data-cbench-elec data-alt="%s" aria-pressed="false">%s</button>'
            '<p class="ks3-cbench-clock" data-cbench-clock></p></div>'
            '<p class="ks3-cbench-elecnote" data-cbench-elecnote hidden>%s</p>'
            '%s<p class="ks3-cbench-model">%s</p></div>'
            % (data, picks, t(a["home_ring_note"]),
               e(elec["alt"]), t(elec["label"]), t(elec["non_metal_note"]),
               notes, t(a["model_note"])))


# ═══ p1-06 · three-routes ════════════════════════════════════════════════

def r_three_routes(a, act_id):
    """⊕ p1-06 `#s-routes` — take the routes away one at a time.

    Design's bench. Four scenarios move the detector and remove the air; the
    student watches which of conduction, convection and radiation can still
    deliver anything. Radiation is the only one that survives every setting,
    and the vacuum scenario is the one that proves it.

    ⚖️ **THE FIRST SCENARIO IS THE ONE THAT MISLEADS, AND IT IS FIRST ON
    PURPOSE.** Detector above, in air: convection and radiation both working.
    That is the everyday situation which convinces people heating only goes
    up, and the bench starts there so the student's existing belief is the
    thing being taken apart rather than a strawman.

    ⚠️ **A SCENARIO WITH NO ROUTE AT ALL IS REFUSED.** Every setting must
    leave at least one route delivering, because the claim is about which
    ones survive rather than about switching the bench off.

    ⚠️ **CONVECTION MUST DIE IN A VACUUM.** A payload that leaves `conv` true
    with `vac` set is asserting that a fluid moves where there is no fluid,
    and the bench would teach the opposite of the lesson.

    HOOKS: `data-troute` · `data-troute-sc` · `data-troute-lamp` (valued with
    the route id) · `data-troute-note`.
    """
    scenarios = a.get("scenarios") or []
    routes = a.get("routes") or []

    if len(scenarios) < 3:
        raise ValueError(
            "three-routes %r offers %d scenario(s). Removing one thing at a "
            "time needs at least a baseline, a removal and the vacuum."
            % (act_id, len(scenarios)))
    if {r.get("id") for r in routes} != {"cond", "conv", "rad"}:
        raise ValueError(
            "three-routes %r declares routes %r. The lesson is about exactly "
            "three and each has to be individually visible."
            % (act_id, [r.get("id") for r in routes]))

    _unique_ids(scenarios, act_id, "three-routes", "scenario")
    _unique_ids(routes, act_id, "three-routes", "route")
    _no_correct_flags(scenarios, act_id, "three-routes")

    for sc in scenarios:
        if not sc.get("label") or not sc.get("note"):
            raise ValueError(
                "three-routes %r scenario %r has no label or note."
                % (act_id, sc.get("id")))
        if not (sc.get("cond") or sc.get("conv") or sc.get("rad")):
            raise ValueError(
                "three-routes %r scenario %r has every route off. The bench "
                "shows which routes SURVIVE a change, and a setting that "
                "delivers nothing is the bench switched off rather than a "
                "result." % (act_id, sc["id"]))
        if "vacuum" in (sc.get("label") or "").lower() and sc.get("conv"):
            raise ValueError(
                "three-routes %r scenario %r runs convection in a vacuum. "
                "Convection needs a fluid to move and there is none, so this "
                "would teach the reverse of the lesson."
                % (act_id, sc["id"]))

    if not any(sc.get("rad") for sc in scenarios):
        raise ValueError(
            "three-routes %r never has radiation delivering. It is the route "
            "the lesson exists to establish." % act_id)

    picks = "".join(
        _p1_seg("ks3-troute-sc", sc["label"], i == 0, data_troute_sc=sc["id"])
        for i, sc in enumerate(scenarios))

    data = "".join(
        "".join(' data-troute-%s-%s="%s"'
                % (e(k), e(sc["id"]), "1" if sc.get(k) else "0")
                for k in ("cond", "conv", "rad"))
        for sc in scenarios)

    lamps = "".join(
        '<div class="ks3-troute-lamp" data-troute-lamp="%s">'
        '<span class="ks3-troute-dot" aria-hidden="true"></span>'
        '<p class="ks3-troute-lamplabel">%s</p>'
        '<p class="ks3-troute-lampstate" data-troute-state="%s"></p></div>'
        % (e(r["id"]), t(r["label"]), e(r["id"])) for r in routes)

    notes = "".join(
        '<p class="ks3-troute-note" data-troute-note="%s"%s>%s</p>'
        % (e(sc["id"]), "" if i == 0 else " hidden", rich(sc["note"]))
        for i, sc in enumerate(scenarios))

    return ('<div class="ks3-troute" data-troute%s>'
            '<div class="ks3-troute-picks">%s</div>'
            '<div class="ks3-troute-lamps">%s</div>%s</div>'
            % (data, picks, lamps, notes))


# ═══ p1-07 · insulation-trial ════════════════════════════════════════════

def r_insulation_trial(a, act_id):
    """⊕ p1-07 `#s-trial` — four beakers, one clock, four cooling curves.

    Design's bench. 200 ml at 80 °C in a 20 °C room, four wrappings, a clock
    that can be run or jumped to thirty minutes, and a results table.

    ⚠️ **THE CURVES DO NOT DECIDE ANYTHING, AND THE CLOSING NOTE SAYS SO.**
    Every wrapped beaker stays hotter than the control — which is EXACTLY
    what you would see if the wool were adding warmth. Both accounts fit
    every number in the table. The renderer requires `close` for that reason:
    a trial that quietly implies it has proved something it has not is worse
    than no trial, and `#s-ice` is the section that actually settles it.

    ⚠️ **`k` IS A RATE MULTIPLIER, NOT A TEMPERATURE.** Every beaker starts
    at `start_temp` and decays toward `room_temp`; `k` scales how fast. A
    payload whose `k` for the control is not the largest would draw an
    insulated beaker cooling faster than a bare one.

    HOOKS: `data-itrial` (wrapper, `data-start`, `data-room`) ·
    `data-itrial-run` · `data-itrial-reset` · `data-itrial-jump` ·
    `data-itrial-clock` · `data-itrial-row` (valued with the beaker id) ·
    `data-itrial-now` · `data-itrial-drop` · `data-itrial-close`.
    """
    beakers = a.get("beakers") or []
    start = a.get("start_temp")
    room = a.get("room_temp")

    if len(beakers) < 3:
        raise ValueError(
            "insulation-trial %r runs %d beaker(s). A trial needs a control "
            "and at least two wrappings to compare against it."
            % (act_id, len(beakers)))
    if start is None or room is None or int(start) <= int(room):
        raise ValueError(
            "insulation-trial %r starts at %r in a room at %r. The water has "
            "to be hotter than the room or nothing cools."
            % (act_id, start, room))
    if not a.get("close"):
        raise ValueError(
            "insulation-trial %r has no `close`. Its curves are equally "
            "consistent with insulation ADDING warmth, and a trial that does "
            "not say so implies it has proved something it has not."
            % act_id)

    _unique_ids(beakers, act_id, "insulation-trial", "beaker")
    _no_correct_flags(beakers, act_id, "insulation-trial")

    ks = []
    for b in beakers:
        for key in ("label", "k", "blocks"):
            if b.get(key) in (None, ""):
                raise ValueError(
                    "insulation-trial %r beaker %r has no %r. `blocks` names "
                    "which of the three routes the wrapping stops, which is "
                    "the only reason the row teaches anything."
                    % (act_id, b.get("id"), key))
        ks.append(float(b["k"]))
    if ks[0] != max(ks):
        raise ValueError(
            "insulation-trial %r does not lead with its control. The first "
            "beaker carries k=%r and the fastest cooler is k=%r — a bench "
            "whose control is not the fastest draws insulation making things "
            "cool quicker." % (act_id, ks[0], max(ks)))

    _count_word_agrees(a.get("heading"), len(beakers), act_id,
                       "insulation-trial", "heading")

    data = "".join(' data-itrial-k-%s="%s"' % (e(b["id"]), float(b["k"]))
                   for b in beakers)

    rows = "".join(
        '<tr data-itrial-row="%s"><th scope="row">%s</th>'
        '<td data-itrial-now="%s"></td><td data-itrial-drop="%s"></td>'
        '<td>%s</td></tr>'
        % (e(b["id"]), t(b["label"]), e(b["id"]), e(b["id"]), t(b["blocks"]))
        for b in beakers)

    return ('<div class="ks3-itrial" data-itrial data-start="%d" '
            'data-room="%d" data-jump="%d" data-done="%d"%s>'
            '<div class="ks3-itrial-ctls">'
            '<button type="button" class="ks3-seg-btn ks3-itrial-run" '
            'data-itrial-run>Run the clock</button>'
            '<button type="button" class="ks3-seg-btn" data-itrial-reset>'
            'Reset to %d °C</button>'
            '<button type="button" class="ks3-seg-btn" data-itrial-jump>'
            'Jump to %d minutes</button>'
            '<p class="ks3-itrial-clock" data-itrial-clock></p></div>'
            '<div class="ks3-itrial-tablewrap">'
            '<table class="ks3-itrial-table"><thead><tr>'
            '<th scope="col">Wrapping</th><th scope="col">Now</th>'
            '<th scope="col">Dropped by</th>'
            '<th scope="col">What it blocks</th></tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p class="ks3-itrial-close" data-itrial-close hidden>%s</p>'
            '</div>'
            % (int(start), int(room), int(a.get("jump_to") or 30),
               int(a.get("done_at") or 28), data,
               int(start), int(a.get("jump_to") or 30), rows,
               rich(a["close"])))


# ═══ p1-07 · ice-trial ═══════════════════════════════════════════════════

def r_ice_trial(a, act_id):
    """⊕ p1-07 `#s-ice` — the one trial that can tell the two accounts apart.

    ⚖️ **THIS IS THE DECISIVE EVIDENCE AND IT IS NOT CUT** (Design's science
    flag 18, which is written as an instruction). The hot-water curves in
    `#s-trial` are consistent with insulation adding warmth. Wrapped ice is
    not: if wool warmed things, wrapped ice would melt FASTER, and it lasts
    about four times as long.

    ⚠️ **THE WRAPPED CUBE MUST OUTLAST THE BARE ONE BY A LARGE MARGIN.** The
    renderer refuses a payload where it does not, because the entire
    argument of the lesson is the direction and the size of that difference.
    A margin small enough to look like scatter proves nothing.

    HOOKS: `data-itrial2` (wrapper, `data-bare`, `data-wrapped`) ·
    `data-itrial2-run` · `data-itrial2-reset` · `data-itrial2-clock` ·
    `data-itrial2-cube` (valued `bare` / `wrapped`) · `data-itrial2-note`.
    """
    bare = a.get("bare_minutes")
    wrapped = a.get("wrapped_minutes")
    notes = a.get("notes") or {}

    if bare is None or wrapped is None:
        raise ValueError(
            "ice-trial %r has no melt times. Both are the result."
            % act_id)
    if int(wrapped) < int(bare) * 2:
        raise ValueError(
            "ice-trial %r has the wrapped cube lasting %r minutes against "
            "the bare cube's %r. This trial exists to rule out "
            "“insulation adds warmth”, and a margin that small "
            "reads as scatter rather than as a result."
            % (act_id, wrapped, bare))

    for key in ("rest", "early", "decided", "done"):
        if not notes.get(key):
            raise ValueError(
                "ice-trial %r has no %r note. `done` in particular carries "
                "the conclusion, and without it the trial runs and says "
                "nothing." % (act_id, key))

    notemarks = "".join(
        '<p class="ks3-itrial2-note" data-itrial2-note="%s"%s>%s</p>'
        % (e(k), "" if k == "rest" else " hidden", rich(notes[k]))
        for k in ("rest", "early", "decided", "done"))

    return ('<div class="ks3-itrial2" data-itrial2 data-bare="%d" '
            'data-wrapped="%d">'
            '<div class="ks3-itrial2-cubes">'
            '<div class="ks3-itrial2-col">'
            '<span class="ks3-itrial2-cube" data-itrial2-cube="bare"></span>'
            '<p class="ks3-itrial2-label">In the open air</p></div>'
            '<div class="ks3-itrial2-col">'
            '<span class="ks3-itrial2-cube is-wrapped" '
            'data-itrial2-cube="wrapped"></span>'
            '<p class="ks3-itrial2-label">Wrapped in wool</p></div></div>'
            '<div class="ks3-itrial2-ctls">'
            '<button type="button" class="ks3-seg-btn ks3-itrial2-run" '
            'data-itrial2-run>Start the ice trial</button>'
            '<button type="button" class="ks3-seg-btn" data-itrial2-reset>'
            'Fresh cubes</button>'
            '<p class="ks3-itrial2-clock" data-itrial2-clock></p></div>%s'
            '</div>'
            % (int(bare), int(wrapped), notemarks))


# ═══ p1-08 · lever-bench ═════════════════════════════════════════════════

# The fulcrum slider's reachable positions, as a percentage along the bar.
# ⚠️ THESE THREE ARE WRITTEN INTO THE `<input type="range">` BELOW *AND*
# SWEPT BY `_lever_rows_multiply_out`. They are constants rather than
# literals in two places so that widening the slider also widens the check.
_LEVER_MIN_PCT, _LEVER_MAX_PCT, _LEVER_STEP_PCT = 10, 90, 1


def _js_to_precision(x, p=4):
    """`Number.prototype.toPrecision` for the positive, non-exponential case.

    Python's `%g` strips trailing zeros and JavaScript's `toPrecision` keeps
    them — 0.45 to four figures is `0.4500` in the browser and `0.45` in
    Python. The check below compares against what the STUDENT sees, so it
    has to round the way the browser does.
    """
    ex = math.floor(math.log10(abs(x)))
    return "%.*f" % (max(p - 1 - ex, 0), x)


def _lever_rows_multiply_out(act_id, load, rise, lo, hi):
    """⚖️ SCIENCE · EVERY ROW THE BENCH CAN WRITE MUST SATISFY E = F × d.

    The lesson drills `E = F × d` through two worked examples and then asks
    the student to "read both ends, then multiply". For a while the table
    could not survive that: the friction bias was added to the ENERGY rather
    than to the force it should come from, and the distance was printed to
    three decimals, so 5400 N × 0.006 m came out as 32.4 J against a printed
    30.4 J — 6.6% out, and out in the direction that says the machine lost
    energy.

    Both causes are fixed in `wireLeverBench`, and this is the assertion
    that stops them coming back. It walks EVERY fulcrum position the slider
    can reach, reproduces exactly the two figures the row will print, and
    checks that their product is the third figure to the precision it is
    printed at — and, separately, that the measured input is still strictly
    the larger of the two energies, which is science flag 20.

    ⚠️ THIS MIRRORS `wireLeverBench`'s ARITHMETIC AND MUST BE KEPT WITH IT.
    A change to the record handler that is not made here is a change this
    check no longer describes. The mirroring is the price of asserting a
    runtime table at build time; the alternative is asserting nothing.
    """
    eout = float(load) * float(rise)
    for pct in range(_LEVER_MIN_PCT, _LEVER_MAX_PCT + 1, _LEVER_STEP_PCT):
        load_arm = pct / 100.0
        ratio = load_arm / (1.0 - load_arm)
        effort = float(load) * ratio
        edist = float(rise) / ratio
        frac = ((pct * 37) % 100) / 100.0
        bias = (lo + (hi - lo) * frac) / 100.0
        d_str = _js_to_precision(edist)
        d_val = float(d_str)
        # `Math.round` goes to +infinity on a half; Python's `round` goes to
        # the even neighbour, and the two disagree on exactly the values a
        # student is most likely to check.
        f_shown = math.floor(effort * (1.0 + bias) + 0.5)
        if f_shown * d_val <= eout:
            f_shown += 1
        # ── CHECK 1 · THE PRINTED DISTANCE IS THE REAL ONE.
        # This is P1-25's second cause and the one this sweep genuinely
        # catches: at the far end of the slider the distance is 0.005556 m,
        # and printed to three decimals as 0.006 m the rounding is 8%. The
        # row would still be internally consistent — it would simply be
        # consistent about the wrong lever. A tenth of a per cent is the
        # most a printed figure may lose.
        if abs(d_val - edist) > abs(edist) * 0.001:
            raise ValueError(
                "lever-bench %r would print the effort distance at fulcrum "
                "%d%% as %s m when it is really %.6f m — a rounding of "
                "%.1f%%. The student is asked to multiply the printed "
                "figures, so a printed figure that is not the measurement "
                "makes the equation fail on the page even though it holds "
                "in the physics."
                % (act_id, pct, d_str, edist,
                   100.0 * abs(d_val - edist) / abs(edist)))

        product = f_shown * d_val
        printed = float("%.1f" % product)
        # ── CHECK 2 · THE ROW MULTIPLIES OUT AS PRINTED.
        # The energy is printed to 0.1 J, so a rounding of up to half that
        # is the display and not a defect. Anything beyond it is the row
        # failing its own equation.
        if abs(product - printed) > 0.0501:
            raise ValueError(
                "lever-bench %r would print a row that fails E = F × d. At "
                "fulcrum %d%% the row reads %d N × %s m = %.1f J, but the "
                "printed force and distance multiply to %.4f J. The lesson "
                "asks the student to do that multiplication; a row that "
                "does not close teaches them that the equation does not "
                "work." % (act_id, pct, f_shown, d_str, printed, product))
        # ── CHECK 3 · THE FRICTION STORY SURVIVES THE ROUNDING.
        if printed <= round(eout, 1):
            raise ValueError(
                "lever-bench %r would print a row whose measured input "
                "(%.1f J) is not larger than the energy out (%.1f J) at "
                "fulcrum %d%%. Friction costs energy, so the input is "
                "always the larger — a row that breaks even shows a "
                "frictionless machine, and a row that came out smaller "
                "would show a machine making energy."
                % (act_id, printed, round(eout, 1), pct))


def r_lever_bench(a, act_id):
    """⊕ p1-08 `#s-bench` — move the fulcrum, read both ends, multiply.

    Design's bench. A 600 N load on a 2.4 m bar; sliding the fulcrum trades
    the student's force against the distance their end must travel, and the
    table records the two products side by side.

    ⚖️ **THE MEASURED INPUT SCATTERS UPWARD ONLY** (Design's science flag
    20, ~+0.5% to +3.5%). Friction at the fulcrum costs energy, so the energy
    a student puts in always EXCEEDS the ideal — never falls below it. A
    symmetric scatter would show a machine handing out free energy several
    times a session, which is the exact belief the lesson exists to kill, and
    Rung 3's fifth criterion depends on the asymmetry. The renderer refuses a
    bias that can go negative.

    ⚠️ **THE TWO PRODUCTS ARE COMPUTED, NEVER AUTHORED.** `effort × effort
    distance` and `load × load rise` are both derived from the fulcrum
    position at run time. Authoring either would allow a row where the
    lesson's central claim silently fails to hold.

    HOOKS: `data-lever` (wrapper, `data-load`, `data-rise`, `data-bar`) ·
    `data-lever-gate` · `data-lever-gopt` · `data-lever-bench` ·
    `data-lever-fulcrum` (the slider) · `data-lever-record` ·
    `data-lever-clear` · `data-lever-out` (valued with the column id) ·
    `data-lever-rows` · `data-lever-close`.
    """
    gate = a.get("gate") or {}
    cols = a.get("columns") or []
    bias = a.get("input_bias") or {}
    load = a.get("load")
    rise = a.get("load_rise")
    bar = a.get("bar")

    for name, v in (("load", load), ("load_rise", rise), ("bar", bar)):
        if not v or float(v) <= 0:
            raise ValueError(
                "lever-bench %r has no positive %s. All three are needed to "
                "compute either product." % (act_id, name))
    if float(rise) >= float(bar):
        raise ValueError(
            "lever-bench %r lifts the load %r m on a %r m bar. The rise has "
            "to be small against the bar or the geometry is nonsense."
            % (act_id, rise, bar))

    if not gate.get("prompt") or len(gate.get("options") or []) < 3:
        raise ValueError(
            "lever-bench %r has no commit gate. A bench read before a "
            "commitment confirms whatever the student already believed."
            % act_id)

    want = {"effort", "edist", "ein", "eout"}
    if want - {c.get("id") for c in cols}:
        raise ValueError(
            "lever-bench %r is missing the %s column(s). Both products have "
            "to be on screen together or the student cannot see that they "
            "match." % (act_id, sorted(want - {c.get("id") for c in cols})))

    lo = float(bias.get("min_pct", -1))
    hi = float(bias.get("max_pct", -1))
    if lo <= 0 or hi <= lo:
        raise ValueError(
            "lever-bench %r declares an input bias of %r..%r percent. It must "
            "be strictly POSITIVE: friction costs energy, so a measured input "
            "is always larger than the ideal and never smaller. A bias that "
            "can go negative shows a machine giving energy away for free, "
            "which is the belief this bench exists to kill."
            % (act_id, bias.get("min_pct"), bias.get("max_pct")))

    if not a.get("readout_note"):
        raise ValueError(
            "lever-bench %r has no `readout_note`. The four live readouts "
            "show the IDEAL lever and the recorded rows show a measured one, "
            "so the same fulcrum reads 600 N above the table and 612 N in "
            "it. Unlabelled that is two different answers to one question; "
            "the note is what makes it a distinction." % act_id)

    _unique_ids(cols, act_id, "lever-bench", "column")
    _no_correct_flags(cols, act_id, "lever-bench")
    _lever_rows_multiply_out(act_id, load, rise, lo, hi)

    opts = "".join(
        '<button type="button" class="ks3-option" data-lever-gopt="%d" '
        'aria-pressed="false"><span class="ks3-opt-mark" aria-hidden="true">'
        '%s</span><span class="ks3-opt-label">%s</span></button>'
        % (i, chr(65 + i), t(o)) for i, o in enumerate(gate["options"]))

    heads = "".join("<th scope=\"col\">%s</th>" % t(c["label"]) for c in cols)
    outs = "".join(
        '<div class="ks3-lever-out"><p class="ks3-lever-outlabel">%s</p>'
        '<p class="ks3-lever-outval" data-lever-out="%s"></p></div>'
        % (t(c["label"]), e(c["id"])) for c in cols)

    return ('<div class="ks3-lever" data-lever data-load="%s" data-rise="%s" '
            'data-bar="%s" data-biaslo="%s" data-biashi="%s" '
            'data-target="%d">'
            '<div class="ks3-lever-gate" data-lever-gate>'
            '<p class="ks3-commit">%s</p>'
            '<ul class="ks3-options">%s</ul></div>'
            '<div class="ks3-lever-bench" data-lever-bench hidden>'
            '<div class="ks3-lever-rig">'
            '<span class="ks3-lever-bar" aria-hidden="true"></span>'
            '<span class="ks3-lever-pivot" data-lever-pivot '
            'aria-hidden="true"></span></div>'
            '<label class="ks3-lever-sliderlabel" for="%s-f">'
            'Where the fulcrum sits · drag to set</label>'
            '<input class="ks3-lever-slider" id="%s-f" type="range" '
            'min="%d" max="%d" step="%d" value="50" data-lever-fulcrum>'
            '<div class="ks3-lever-outs">%s</div>'
            # The readouts are the IDEAL lever; the table is a measured one.
            # Reusing `.ks3-lever-sliderlabel` rather than adding a class:
            # it is already the instrument-caption treatment on this bench.
            '<p class="ks3-lever-sliderlabel">%s</p>'
            '<div class="ks3-lever-acts">'
            '<button type="button" class="ks3-seg-btn" data-lever-record>'
            'Lift it and record</button>'
            '<button type="button" class="ks3-seg-btn" data-lever-clear>'
            'Clear the table</button></div>'
            '<div class="ks3-lever-tablewrap">'
            '<table class="ks3-lever-table"><thead><tr>%s</tr></thead>'
            '<tbody data-lever-rows></tbody></table></div>'
            '<p class="ks3-lever-close" data-lever-close hidden>%s</p>'
            '</div></div>'
            % (float(load), float(rise), float(bar), lo, hi,
               int(a.get("runs_to_record") or 3),
               t(gate["prompt"]), opts, e(act_id), e(act_id),
               _LEVER_MIN_PCT, _LEVER_MAX_PCT, _LEVER_STEP_PCT,
               outs, t(a["readout_note"]), heads,
               rich(a.get("close") or "")))


# ═══ registration ════════════════════════════════════════════════════════
#
# ONE ROW PER RENDERER. `ks3_art.check_placements` gate 2 fails a family
# registered and never placed and gate 3 fails one placed and never
# registered, so this list and the lessons agreeing is checkable rather than
# promised. Every family is P1's own — `ks3_art/core.py` is untouched.

KIND_SHELL = {
    'store-audit': ("ks3-saudit-block",
                    ' data-instrument data-sauditblock data-stage-done="0"'),
    'store-pathway-sort': ("ks3-spath-block",
                           ' data-instrument data-spathblock '
                           'data-stage-done="0"'),
    'before-after-tally': ("ks3-btally-block",
                           ' data-instrument data-btallyblock '
                           'data-stage-done="0"'),
    'waste-sort':        ("ks3-wsort-block",
                          ' data-instrument data-wsortblock '
                          'data-stage-done="0"'),
    'running-total': ("ks3-rtotal-block",
                          ' data-instrument data-rtotalblock '
                          'data-stage-done="0"'),
    'conservation-beam': ("ks3-cbeam-block",
                          ' data-instrument data-cbeamblock '
                          'data-stage-done="0"'),
    'two-quantities': ("ks3-twoq-block",
                          ' data-instrument data-twoqblock '
                          'data-stage-done="0"'),
    'one-way-flow': ("ks3-oflow-block",
                          ' data-instrument data-oflowblock '
                          'data-stage-done="0"'),
    'conduction-bench': ("ks3-cbench-block",
                          ' data-instrument data-cbenchblock '
                          'data-stage-done="0"'),
    'touch-test':        ("ks3-touch-block",
                          ' data-instrument data-touchblock '
                          'data-stage-done="0"'),
    'three-routes': ("ks3-troute-block",
                          ' data-instrument data-trouteblock '
                          'data-stage-done="0"'),
    'radiation-word-sort': ("ks3-rword-block",
                          ' data-instrument data-rwordblock '
                          'data-stage-done="0"'),
    'insulation-trial': ("ks3-itrial-block",
                          ' data-instrument data-itrialblock '
                          'data-stage-done="0"'),
    'ice-trial': ("ks3-itrial2-block",
                          ' data-instrument data-itrial2block '
                          'data-stage-done="0"'),
    'plan-the-trial':    ("ks3-plan-block",
                          ' data-instrument data-planblock '
                          'data-stage-done="0"'),
    'lever-bench':       ("ks3-plever-block",
                          ' data-instrument data-pleverblock '
                          'data-stage-done="0"'),
}

KIND_FN = {
    'store-audit': r_store_audit,
    'lever-bench': r_lever_bench,
    'plan-the-trial': r_waste_sort,
    'ice-trial': r_ice_trial,
    'insulation-trial': r_insulation_trial,
    'radiation-word-sort': r_waste_sort,
    'three-routes': r_three_routes,
    'touch-test': r_waste_sort,
    'conduction-bench': r_conduction_bench,
    'one-way-flow': r_one_way_flow,
    'two-quantities': r_two_quantities,
    'conservation-beam': r_conservation_beam,
    'running-total': r_running_total,
    'store-pathway-sort': r_store_pathway_sort,
    'before-after-tally': r_before_after_tally,
    'waste-sort': r_waste_sort,
}
