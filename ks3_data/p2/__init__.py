"""P2 — *Energy at home*, as one module per lesson.

Five lessons, four of them QUANTITATIVE — the highest concentration of
calculation anywhere in KS3. The package layout follows `ks3_data/p1/`
exactly; nothing about it is new.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p2/`. Her page wins outright.

── ⚠️ ONE FILE IN THIS DELIVERY HIDES ITS MARKUP ───────────────────────

`p2-02-power-ratings-in-watts.dc.html` is 697 KB and carries a
`__bundler/manifest` signature — the only file in the whole P1/P2/P3
tree that does. What is and is not readable in it was MEASURED:

  · the `data-dc-script` block is PLAIN TEXT in the outer file, so
    `const RAIL`, `SORT_CARDS`, `RUNGS` and `cfifaExamples` all read
    normally — which is why `ks3_rail_manifest.py` picks this lesson's
    four rail stops up with no special case at all;
  · the MARKUP does not. The page body is a JSON string literal inside
    `<script type="__bundler/template">`, on one line, every quote escaped.
    `grep 'id="s-'` therefore returns 0 (the file holds `id=\"s-`), and a
    per-occurrence count of any class collapses to 1 because `grep -c`
    counts lines and the body is one line.

Both artefacts read like findings about the lesson. It was unpacked, and
the decoded page is committed beside the original as
`p2-02-power-ratings-in-watts.DECODED.html` so the next lane measures
markup rather than a container. The manifest glob is `*/*.dc.html`, so the
decoded copy takes no row of its own.

Decoded, it is an ordinary lesson: six sections, four rail stops, one
`dc-import name="Cfifa"`, and a formula triangle over `E = P × t`.

── ⚖️ THE OWNERSHIP MAP — 1:1, NO SPLITS NEEDED ────────────────────────

Five statutory statements, five lessons, and they line up one-for-one, so
unlike P1 this unit mints no substatements at all:

    p2-01  energy-in-food                  KS3.P.FUEL.01
    p2-02  power-ratings-in-watts          KS3.P.FUEL.02
    p2-03  calculating-energy-transferred  KS3.P.FUEL.03
    p2-04  reading-a-fuel-bill             KS3.P.FUEL.04
    p2-05  fuels-and-energy-resources      KS3.P.FUEL.05

`p2-01` is the OWNER of the food-energy figures under §4.6. Biology B3's
`a-balanced-diet` references this lesson and must not restate them.

── FOUR RAIL STOPS PER LESSON ──────────────────────────────────────────

Measured off Design's own `RAIL` constant on each delivered page — for
`p2-02`, off the DECODED page, because the original has no readable one:

    p2-01  s-hook s-burn  s-worked s-ladder   4
    p2-02  s-hook s-bench s-cfifa  s-ladder   4
    p2-03  s-hook s-bench s-worked s-ladder   4
    p2-04  s-hook s-bill  s-cfifa  s-ladder   4
    p2-05  s-hook s-sort  s-grid   s-ladder   4

⚠️ **A SECTION IS NOT A STOP.** Every lesson here carries a `#s-think`
that is NOT on the rail, and `p2-03` (`#s-tri`), `p2-04` (`#s-kwh`,
`#s-shape`) and `p2-02` (`#s-sort`) each carry more. Design's audit records
the cut: "p2-02 drops SORT and THINK · p2-03 drops TRIANGLE and THINK ·
p2-04 drops UNIT, SHAPE and THINK". Every section keeps its `id`, so
in-page anchors and the tutor link are untouched.

── ⚖️ MRB-204 · CHECKED PER BLOCK, AGAINST THE ARITHMETIC ──────────────

    p2-01  E = e × m          product   TRIANGLE
    p2-02  E = P × t          product   TRIANGLE
    p2-03  E = P × t          product   TRIANGLE
    p2-04  one row = P × t    product   TRIANGLE (drawn on the beam's pan)
           amount due = Σ rows + standing charge   A SUM   BALANCE BEAM
    p2-05  no calculable relationship — no formula figure at all

`p2-04` is the lesson that makes MRB-204 visibly necessary rather than
pedantic: it is the only place in KS3 where a product and a sum sit inside
one calculation, and Design draws both, with the beam's own caption reading
"A SUM OF PRODUCTS — TRIANGLE FOR ONE ROW, BALANCE FOR THE TOTAL".

── ⚠️ SHELLS ARE MEASURED, NOT INFERRED ────────────────────────────────

Bare `ks3-block` → `check`. `ks3-block ks3-dark ks3-practical` →
`practical`. `ks3-block ks3-misconception` → `misconception`.
"""

import importlib
import pkgutil

# Instrument block types seen in authored P2 data, mapped to the §5.1.1
# segment they render as — measured from Design's `class` attribute on the
# section, never inferred from the family name.
_INSTRUMENT_SEGMENTS = {
    # p2-01 · Energy in food        #s-burn  is bare `ks3-block`
    "calorimeter":        "check",
    # p2-02 · Power ratings         #s-bench bare; #s-sort is dark+practical
    "power-bench":        "check",
    "power-energy-sort":  "practical",
    # p2-03 · Calculating energy transferred
    "appliance-bench":    "check",
    # p2-04 · Reading a fuel bill
    "kwh-rectangles":     "check",
    "bill-builder":       "check",
    # p2-05 · Fuels and energy resources
    "renewable-sort":     "check",
    "two-axis-grid":      "check",
}

_BLOCK_KEYS = ("type", "anchor", "id")


def _normalise(lesson):
    """Lift inline instrument blocks into `activities[]`. Returns the lesson."""
    core = lesson.get("core") or []
    acts = list(lesson.get("activities") or [])
    known = {a.get("id") for a in acts}
    out = []

    for block in core:
        kind = block.get("type")
        segment = _INSTRUMENT_SEGMENTS.get(kind)
        if segment is None:
            out.append(block)
            continue

        act_id = block.get("id") or block.get("anchor") or kind
        if act_id in known:
            raise ValueError(
                "%s: instrument %r collides with an existing activity id"
                % (lesson.get("slug"), act_id))
        known.add(act_id)

        payload = {k: v for k, v in block.items() if k not in _BLOCK_KEYS}
        payload.update({"id": act_id, "kind": kind})
        payload.setdefault("demand", "investigate")
        acts.append(payload)
        out.append({"type": segment, "id": act_id,
                    "anchor": block.get("anchor")})

    lesson["core"] = out
    lesson["activities"] = acts
    _check_sort_grid_agree(lesson)
    return lesson


def _check_sort_grid_agree(lesson):
    """⚖️ `p2-05`'s two blocks must agree about which resources renew.

    `#s-sort` sorts eight resources on "will it run out?"; `#s-grid` then
    plots the same eight with renewability as its x-axis. The two carry
    separate lists, because they are separate instruments — and if they
    ever disagreed, BOTH WOULD STILL DRAW. A student would sort wood as
    renewable and then find it in the finite column two paragraphs later,
    and nothing in the build would have said so.

    The check is here rather than in either renderer because only the
    lesson record sees both blocks at once.
    """
    sort = grid = None
    for a in lesson.get("activities") or []:
        if a.get("kind") == "renewable-sort":
            sort = a
        elif a.get("kind") == "two-axis-grid":
            grid = a
    if not sort or not grid:
        return

    left = {i["id"]: bool(i.get("renewable"))
            for i in (sort.get("sort_items") or [])}
    right = {r["id"]: bool(r.get("renewable"))
             for r in (grid.get("resources") or [])}

    if set(left) != set(right):
        raise ValueError(
            "%s: #s-sort and #s-grid disagree about WHICH resources exist "
            "(only in the sort: %s · only in the grid: %s). A resource in "
            "one and not the other is either an unplottable sort card or a "
            "dot for something the student never sorted."
            % (lesson.get("slug"), sorted(set(left) - set(right)),
               sorted(set(right) - set(left))))

    clash = sorted(k for k in left if left[k] != right[k])
    if clash:
        raise ValueError(
            "%s: #s-sort and #s-grid disagree about whether %s renew(s). "
            "Both blocks would still draw, and the student would sort a "
            "resource into one column and then find it in the other."
            % (lesson.get("slug"), clash))


def lessons():
    """The authored P2 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
