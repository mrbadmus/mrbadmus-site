"""P5 — *Pressure*, as one module per lesson.

Four lessons, a complete unit. The package layout follows `ks3_data/p4/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p5/`. Her page wins outright.

── ⚖️ THE OWNERSHIP MAP — THREE STATEMENTS OVER FOUR SLOTS ────────────

P5 is the SURPLUS-SLOT case: three statutory statements and four lessons.
Only `PRES.02` is split, and it has to be — it names two different physical
ideas in one line:

    p5-01  pressure-force-over-area      KS3.P.PRES.03 whole
    p5-02  pressure-in-liquids           KS3.P.PRES.02a "pressure in
                                         liquids, increasing with depth"
    p5-03  upthrust-floating-and-sinking KS3.P.PRES.02b "upthrust effects,
                                         floating and sinking"
    p5-04  atmospheric-pressure          KS3.P.PRES.01 whole

The `.a` / `.b` sub-IDs are minted in `ks3_data/substatements.py` under the
rule that file already carries — mint lazily, per unit, at authoring time.
See the P4 package note: **the notation Design's FLAG 1 asks for already
existed**, and this is the second unit to use it.

── ⊖ DESIGN'S FLAG 9 · THE MISSING `hydraulics` SLOT — ANSWERED ───────

Her flag: `misconception-register.md` routes a force-multiplication belief
to *"P4 `moments`, P5 `hydraulics`"*, and `structure.py` gives P5 four slots
with no hydraulics among them. She resolved it by confronting the belief in
`p5-01`'s *Going further* — the hydraulic jack, with the distance traded
explicitly against the force — *"rather than leaving the register pointing
at nothing"*, and asked for the register to be re-pointed or a fifth slot
added.

**Her resolution is kept and NOTHING IS RE-POINTED HERE.** The register
entry she names is `ENERGY-11`, and there is no `ENERGY` family: it was
discharged into `ENER` on 21 Aug and the belief now lives as `ENER-19` —
*"a machine that multiplies force gives you energy for free"* — owned by
`p1-08 simple-machines` and confronted by its lever bench. So the register
does not point at nothing; it points at P1, and always did. `p5-01`'s
*Going further* re-confronts it in a second situation and mints nothing,
exactly as this register asks. **Adding a fifth slot to `structure.py` is a
scope decision and is Mide's, not a lane's**, and nothing here needs it.

── ⚠️ HER NOTES PREDATE HER DRAWING, AND THE DRAWING WAS MEASURED ─────

`NOTES-P4-P6.md` §3 describes a FOUR-step FIFA. Her own 23 Aug audit
records the rebuild to CFIFA — five steps, with a Convert line — and the
delivered pages carry the five-step shape.

── FOUR RAIL STOPS PER LESSON, AND ALL FOUR PAGES ARE THE SAME SHAPE ──

    s-hook · s-bench · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the ATTEMPT PANEL on all four,
because Design's own `DONE` reads `if (id === 's-formula') return
s.buildOpen`, and `buildOpen` is set by the CFIFA's Check. A `formula` block
carries no demand and emits no `data-stage-done`.

⚠️ **NO STOP IN THIS UNIT IS A MIRROR AND NONE NEEDS A BAND SIBLING.**
Unlike P4, every P5 rail stop sits on a block that carries its own control.

── ⚖️ THE `PRESS` FAMILY OPENS HERE ──────────────────────────────────

See the ruling in `docs/ks3/misconception-register.md`. `PRESS-01` …
`PRESS-16` are minted by these four lessons.

── ⚠️ SHELLS ARE MEASURED, NOT INFERRED ──────────────────────────────

Every P5 bench is `ks3-block ks3-dark ks3-practical` → `practical`. Every
`#s-think` is `ks3-block ks3-misconception` → `misconception`. The
attempt panel sits inside a classless `#s-formula` → `check`.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    "block-on-sand":   "practical",
    "depth-probe":     "practical",
    "float-tank":      "practical",
    "altitude-column": "practical",
}

# ⚠️ `p5-attempt` IS NOT IN THE TABLE ABOVE, for the same reason `p4-attempt`
# is not in P4's: it is authored in `activities[]` beside the two worked
# examples it belongs with, and placed in `core` as a `check` naming its id.

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
    """The authored P5 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
