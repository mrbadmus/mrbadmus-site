"""P9 — *Static electricity*, as one module per lesson.

Three lessons, a complete unit. The package layout follows `ks3_data/p6/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p9/`. Her page wins outright, and where her
NOTES and her drawing disagree the DRAWING IS MEASURED and the note is
reported in `docs/ks3/design-reference/p9/DEPARTURES-P9.md`.

── ⚖️ THE OWNERSHIP MAP — TWO STATEMENTS OVER THREE SLOTS ─────────────

    p9-01  charging-by-rubbing     STAT.01a "separation of positive or
                                   negative charges when objects are
                                   rubbed together: transfer of electrons"
    p9-02  forces-between-charges  STAT.01b "forces between charged
                                   objects"
    p9-03  electric-fields         STAT.02 whole

The `.a` / `.b` sub-IDs are minted in `ks3_data/substatements.py` under the
rule that file already carries. This is the fourth physics unit in the run
to use it; see the P4 package note for why Design's FLAG 1 asks for a
notation that already existed.

── ⚖️ FOUR RAIL STOPS, AND `p9-01`'s THIRD ONE IS THE CONFRONTATION ───

Measured off Design's own `RAIL` and `DONE` on each page:

    p9-01  s-hook  s-rub      s-think   s-ladder
    p9-02  s-hook  s-spheres  s-matrix  s-ladder
    p9-03  s-hook  s-field    s-reach   s-ladder

On all three pages the THIRD stop ticks at `s.gate !== null` while the
bench beside it needs the gate AND a control touched. That is the
`band_anchor` / `band_at` shape exactly, as in P4 and P6: each bench marks
its own sibling through `markSibling` at Design's own earlier threshold.
MRB-249's `mirrors` is NOT used and would be wrong twice over — it would
tick the stop late, and `ks3_rail_manifest` derives the mirror map from her
`isDone()`, which returns two DIFFERENT expressions here, so a declared
mirror fails `check_rail_matches_design` outright.

⚠️ **`p9-01`'s THIRD STOP IS `#s-think`, WHICH IS A MISCONCEPTION BLOCK,
AND NO OTHER PAGE IN THE KEY STAGE PUTS ONE ON THE RAIL.** `ks3_parity`'s
own note records that "`#s-think` is on no rail on any page" — it was true
of the first 137 lessons and it is not true of this one, because Design's
`DONE` says otherwise and her page wins.

Two gates read that section and both need something from it:

  * `check_rail_reachable` (R2) needs the section to carry a signal
    `doneByDom()` reads. A `predict` block carries none — no options, no
    reveal, no rungs, no declaration.
  * `check_nothing_ticks_on_load` needs any `data-instrument` section that
    IS a rail anchor to declare `data-stage-done="0"` in the SHIPPED
    BYTES, because the rail's first paint runs before the instruments
    wire and a reader with JavaScript off would otherwise get a rail
    claiming work nobody did.

`ks3_art/core.py`'s shared `confrontation` shell satisfies neither — it
emits `data-instrument` and no declaration, so routing through it would
fail the second gate. Rather than widen a file ten units share, `p9-01`'s
confrontation carries P9's OWN family `charge-think`, whose only job is the
shell declaration. See `ks3_art/p9.py` for the whole of it; `p9-02` and
`p9-03` keep the plain `predict` kind, because their `#s-think` is off the
rail exactly as everywhere else.

── ⚖️ MIDE'S RULINGS, 21 Aug 2026 — APPLIED, NOT RE-ASKED ────────────

1. **The charge ceiling is REAL and it is hers.** Her FLAG 8 says `p9-01`'s
   model has no ceiling. Her page has `STROKE_CEIL = 26.3` and
   `STROKE_TAU = 14`, and its legal line says the stroke term levels off
   because charge leaks away and the air breaks down. Measured, ported
   exactly, and logged as a notes-versus-drawing contradiction rather than
   a change.
2. **Induced attraction is relative words only, never newtons.** Accepted
   coefficient, no absolute force anywhere on `p9-02`. Her page already
   holds that line and nothing moved.
3. **`p9-01` carries no formula block and keeps BOTH readouts.**
4. **No Childline block anywhere in P9.**

── ⚖️ THE `CHRG` FAMILY OPENS HERE ────────────────────────────────────

See the ruling in `docs/ks3/misconception-register.md`. `CHRG-01` …
`CHRG-12` are minted by these three lessons. Design proposed the prefix
`STAT`; the commander chose `CHRG`, because `STAT` collides in a reader's
eye with the statutory ids `KS3.P.STAT.01` / `.02` printed on the same
pages. Her NUMBERS are kept one for one.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    # The three benches are `ks3-block ks3-dark ks3-practical`.
    "transfer-pair": "practical",
    "charge-pair":   "practical",
    "field-grid":    "practical",
    # The three fixed figures are bare `ks3-block` on the band ground.
    "charge-band":   "check",
}

# ⚠️ `charge-think` IS NOT IN THE TABLE ABOVE, and must not be. It is the
# shell of a `misconception` BLOCK, which `r_activity` already renders
# through its own block type; lifting it here would put it in a `check`
# shell and lose Design's `ks3-misconception` ground and her amber divider.
# It is authored in `activities[]` directly, exactly as `p6-attempt` is.

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
    """The authored P9 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
