"""P10 — *Magnetism and electromagnetism*, as one module per lesson.

Five lessons, a complete unit. The package layout follows `ks3_data/p9/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p10/`. Her page wins outright, and where her NOTES
and her drawing disagree the DRAWING IS MEASURED and the note is reported in
`docs/ks3/design-reference/p10/DEPARTURES-P10.md`.

── ⚖️ THE OWNERSHIP MAP — FOUR STATEMENTS OVER FIVE SLOTS ─────────────

    p10-01  magnets-and-poles       MAG.01  magnetic poles, attraction and
                                            repulsion
    p10-02  magnetic-fields         MAG.02  magnetic fields by plotting with a
                                            compass, representation by field
                                            lines
    p10-03  the-earth-is-a-magnet   MAG.03  the Earth's magnetism, compass and
                                            navigation
    p10-04  electromagnets          MAG.04a the magnetic effect of a current,
                                            and electromagnets
    p10-05  how-a-motor-works       MAG.04b D.C. motors, principles only

⚠️ **DESIGN'S §1 CLAIMS TWO STATEMENTS TWICE AND SAYS SO IS FINE.** Her table
gives `MAG.02` to `p10-02`, again to `p10-03` and again to `p10-05`, and
`MAG.04` to both `p10-04` and `p10-05`, with the note *"That is correct and
needs no notation."* It is not how this register works: architecture.md §4.4
rule 3 makes `covers` exactly-once across the key stage and `verify_ks3`
asserts it, so a second claim would fail the build. `MAG.04` is split at its
own clause boundary into `.04a` and `.04b` — the bullet reads *"the magnetic
effect of a current, electromagnets, DC motors (principles only)"* and the
comma is where a scheme of work splits it too — and `p10-03`'s reading of
`MAG.02` is carried as a `touches`, which is what the register has for a
statement a lesson uses without owning. `p10-05` carries neither: it draws a
field between two magnets but it never plots one with a compass, which is what
`MAG.02` actually names. One register line in `DEPARTURES-P10.md`.

── ⚖️ FOUR RAIL STOPS, AND THE THIRD IS THE FIGURE BESIDE THE BENCH ───

Measured off Design's own `RAIL` and `DONE` on each page, and matching
`docs/ks3/rail-manifest.md` row for row:

    p10-01  s-hook  s-bench  s-proof  s-ladder
    p10-02  s-hook  s-bench  s-rules  s-ladder
    p10-03  s-hook  s-bench  s-earth  s-ladder
    p10-04  s-hook  s-bench  s-uses   s-ladder
    p10-05  s-hook  s-bench  s-parts  s-ladder

On all five pages the THIRD stop ticks at `s.gate !== null` while the bench
beside it needs the gate AND a control touched. That is the `band_anchor` /
`band_at` shape exactly, as in P4, P6 and P9: each bench marks its own sibling
through `markSibling` at Design's own earlier threshold. MRB-249's `mirrors`
is NOT used and would be wrong twice over — it would tick the stop late, and
`ks3_rail_manifest` derives the mirror map from her `isDone()`, which returns
two DIFFERENT expressions here, so a declared mirror fails
`check_rail_matches_design` outright. The manifest carries `—` in the mirrors
column for all five rows.

⚠️ **`#s-think` IS OFF THE RAIL ON ALL FIVE PAGES**, which is the ordinary
arrangement everywhere in the key stage except `p9-01`. So P10 needs no
shell-only confrontation family: every `#s-think` here is a plain `predict`.

── ⚖️ RULINGS APPLIED, NOT RE-ASKED ───────────────────────────────────

Design's §9, all five standing as drawn:

1. **No formula block anywhere in P10, and no worked example.** Her §2 and her
   own audit; KS3 magnetism names no quantity a student can calculate.
2. **Relative scales, never invented units.** No tesla, no newton, no newton
   metre, anywhere in the unit — tiles, notes, legal lines, rungs or bank.
   Each relative figure names its reference in the readout, in words.
3. **`p10-03` uses a centred dipole aligned with the spin axis**, giving
   `tan(dip) = 2 tan(latitude)` and a sideways pull going as `cos(latitude)`.
   Disclosed in the legal line, including the eleven-degree tilt it leaves out.
4. **`p10-04` models the plastic former as identical to no core**, and says so
   on the face of the bench.
5. **`p10-05` freezes the coil horizontal.** Disclosed, with the reason real
   motors use several coils given in *Going further*.

── ⚖️ THE `MAG` FAMILY OPENS HERE ─────────────────────────────────────

See the ruling in `docs/ks3/misconception-register.md`. `MAG-01` … `MAG-20`
are minted by these five lessons. Design's §6 pre-allocated four per lesson
and authored fifteen, leaving the last of each four as a named spare; all five
spares are minted here from real page content — a gate distractor or a rung
distractor with its own correction — rather than left reserved, which is the
register's own rule.

── ⚠️ CHILDLINE IS ON `p10-01` AND ON NO OTHER PAGE ───────────────────

Her §5, ruled. `p10-01`'s *Going further* names neodymium magnets and magnet
ingestion, which is a risk to a student's own body and one that lives in their
home rather than in a lab. The other four carry none: nothing on them touches
a student's own body or health, and `p10-04`'s MRI paragraph is information
about a hazard in a hospital rather than a risk the student is being asked to
disclose.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    # The five benches are `ks3-block ks3-dark ks3-practical`.
    "track-pair":     "practical",
    "compass-plot":   "practical",
    "dip-circle":     "practical",
    "solenoid-bench": "practical",
    "motor-coil":     "practical",
    # The five band figures are bare `ks3-block` on the band ground.
    "mag-band":       "check",
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
    """The authored P10 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
