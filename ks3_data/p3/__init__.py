"""P3 — *Describing motion*, as one module per lesson.

Three lessons, a complete unit. The package layout follows `ks3_data/p2/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p3/`. Her page wins outright.

── ⚖️ THE OWNERSHIP MAP — 1:1, NO SPLITS NEEDED ───────────────────────

Three statutory statements, three lessons, one for one:

    p3-01  speed                 KS3.P.MOT.01
    p3-02  distance-time-graphs  KS3.P.MOT.02  (+ KS3.WS.ANA.02 as `touches`)
    p3-03  relative-motion       KS3.P.MOT.03

All three MOT statements are covered, none twice, and nothing outside MOT
is taught as core.

── ⚖️ RULED · THE FAMILY IS `FORCE`, AND IT OPENS HERE ────────────────

Design's `NOTES-P3.md` §4 asks for a ruling: open `FORCE` for kinematics,
or mint a separate `MOT` family and leave `FORCE` for P4? **`FORCE` opens
here**, and it is the register's own table that decides it — the family
is listed as *"`FORCE` (forces and motion)"*, so motion is inside the
family as declared, and a lane meeting a motion misconception adds to it
rather than opening a second one beside it.

That is the SAME ruling the register already made for `ENER` against
`ENERGY`, in the same words: the reservation is discharged into the family
that exists rather than left standing beside it. Applying it consistently
is the point — a lane that mints `MOT` here would leave the next lane
with two plausible families and no rule.

P4 continues from `FORCE-12`.

── ⚠️ HER NOTES PREDATE HER DRAWING, AND THE DRAWING WAS MEASURED ─────

`NOTES-P3.md` is dated 15 Aug and describes a FOUR-step FIFA, five or six
rail stops per lesson, and a `#s-compare` stop on `p3-01`. Her own
`PHYSICS-AUDIT-2026-08-23.md` then records both changes: CFIFA (five steps,
with a Convert line) became the standing shape, and P1–P3 were cut to four
rail stops — *"p3-01 drops COMPARE and THINK"*. The drawings carry the
23 Aug shape. Measured, not inferred; reported, not escalated.

── FOUR RAIL STOPS PER LESSON ────────────────────────────────────────

Measured off Design's own `RAIL` constant on each page:

    p3-01  s-hook s-track  s-build s-ladder   4
    p3-02  s-hook s-plot   s-match s-ladder   4
    p3-03  s-hook s-frames s-pass  s-ladder   4

⚠️ Every lesson also carries a `#s-think` that is NOT on the rail, and
`p3-01` carries `#s-compare` as well. All keep their `id`: `p3-01`'s
tutor link points at `#s-build`, `p3-02`'s at `#s-plot` and `p3-03`'s at
`#s-pass`.

── ⚖️ MRB-204 · ONE TRIANGLE IN THE UNIT, AND NO BEAM ────────────────

    p3-01  s = d ÷ t     a genuine relationship   TRIANGLE
    p3-02  no formula figure — the gradient IS the speed, and it is
           read off a graph rather than computed from a rule
    p3-03  no formula figure — and this one matters

`p3-03`'s arithmetic is `30 + 30 = 60` and `25 − 20 = 5`: SUMS and
DIFFERENCES, not products. **A triangle over a relative speed would teach
a relationship that does not exist**, and Design draws none — the word
"triangle" appears zero times on that page. Checked against her drawing
and against the arithmetic, twice.

── ⚠️ SHELLS ARE MEASURED, NOT INFERRED ──────────────────────────────

Bare `ks3-block` → `check`. `ks3-block ks3-dark ks3-practical` →
`practical`. `ks3-block ks3-misconception` → `misconception`.
"""

import importlib
import pkgutil

# Instrument block types seen in authored P3 data, mapped to the §5.1.1
# segment they render as — measured from Design's `class` attribute.
_INSTRUMENT_SEGMENTS = {
    # p3-01 · Speed        #s-track is dark+practical; #s-compare is bare
    "light-gates":    "practical",
    "compare-pairs":  "check",
    # p3-02 · Distance-time graphs   #s-plot bare; #s-match dark+practical
    "graph-plot":     "check",
    "journey-match":  "practical",
    # p3-03 · Relative motion        #s-frames dark+practical; #s-pass bare
    "relative-frames": "practical",
    "passing-speeds":  "check",
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
    return lesson


def lessons():
    """The authored P3 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
