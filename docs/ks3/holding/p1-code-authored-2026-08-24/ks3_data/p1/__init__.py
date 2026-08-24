"""P1 — Energy transfers, as one module per lesson.

The first physics unit ever built. The shape follows `ks3_data/c10/` exactly;
nothing about the package layout is new, and nothing about it is physics.

EIGHT SLOTS. `structure.py` gives P1 eight, in this order, and all eight are
authored by this unit — the first KS3 unit to be authored complete on the run
that opened it:

    p1-01 energy-stores                        KS3.P.CIS.02a
    p1-02 energy-transfers-before-and-after    KS3.P.CIS.02b + KS3.P.ECT.03
    p1-03 conservation-of-energy               KS3.P.CIS.01  + KS3.P.CIS.03
    p1-04 heating-and-thermal-equilibrium      KS3.P.ECT.02a
    p1-05 conduction                           KS3.P.ECT.02b
    p1-06 radiation                            KS3.P.ECT.02c
    p1-07 insulation                           KS3.P.ECT.02d
    p1-08 simple-machines                      KS3.P.ECT.01

── ⚖️ RULED · THE OWNERSHIP MAP, AND WHY IT IS THIS ONE ─────────────────

Six statements, eight lessons. §10.2 wants every lesson's `covers` non-empty
and §4.4 rule 3 wants every statement owned exactly once, so two of the six
split. Both mints are in `ks3_data/substatements.py` with the bullets quoted
in full; the reasoning that chose the seams is there and is not repeated here.

What IS decided here is which lesson takes which clause, and two of those are
judgement calls worth writing down:

**`KS3.P.ECT.03` goes to p1-02, not to p1-01.** The bullet is a list of
transfer PROCESSES — "changing motion, dropping an object, completing an
electrical circuit, stretching a spring, metabolism of food, burning fuels" —
and every one of them is a before-and-after situation. p1-01 names the stores;
p1-02 is where a student says which one went down and which went up, and the
six named processes are literally its bench. Putting the list on p1-01 would
have the stores lesson teach six transfers before the word transfer has been
defined.

**`KS3.P.CIS.03` goes to p1-03, with `KS3.P.CIS.01`.** The bullet says to use
physical processes and mechanisms, RATHER THAN ENERGY, to explain the
intermediate steps. That instruction only becomes reasonable once a student
knows the total never changes: if energy is conserved, it cannot have been
consumed, and a quantity that is never consumed can never be the reason
anything happened. Conservation is the premise and "name the mechanism" is
the conclusion, so they are one lesson. p1-03 teaches them in that order and
`#s-why` is where the student does it.

── ⚖️ RULED · TRIANGLE, BEAM, BAR — CHECKED PER BLOCK ───────────────────

MRB-204 as amended 15 Aug 2026: TRIANGLE for products (`A = B x C`),
BALANCE-BEAM and part-whole BAR for sums and conservation statements. Physics
gets this wrong more easily than chemistry did, because a physics unit has
several formulas rather than one, and they are not all the same shape.

P1 carries three formula blocks and they are deliberately not all drawn alike:

    p1-03  total energy before = total energy after      BEAM  + BAR
           the bar splits the after side into the useful transfer and the
           part that warmed the surroundings. Whole = part + part: a SUM.
    p1-08  work done = force x distance                  TRIANGLE
           a genuine product, and the only triangle in the unit.
    p1-08  work in = work out                            BEAM
           a conservation statement about a product, which is NOT itself a
           product. Two equal wholes, so a level beam and no bar: there are
           no parts to split.

⚠️ The third of those is the one a careless pass draws as a triangle, because
the quantities on both sides are products and a triangle is what a product
gets. It is not a product; it is an EQUALITY BETWEEN two products, and a
triangle would tell a student that work-in is work-out multiplied by
something. Checked against the arithmetic, per block, not against the topic.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as C10's. The segment each family renders into is
MEASURED against the ground the instrument needs, not inferred from its name:
`practical` is ink-dark and is for a bench a student runs; `check` is the
plain light `ks3-block` and is for a discrimination they make.

⚠️ `fifa-pick` is in the map below and is NOT a P1 family. It is registered by
`ks3_art/c2.py` and P1 PLACES it without editing that module — MRB-204 part 4
needs it on both formula lessons, the payload fits `r_fifa_pick` with no
change, and generalising another lane's renderer is exactly what
`docs/ks3/worktrees.md` §1 forbids. The coupling is recorded in
`ks3_art/p1.py`'s header so it is visible from the physics side too.
"""


import importlib
import pkgutil

# Instrument block types seen in authored P1 data, mapped to the §5.1.1
# segment they render as.
#
# ⚠️ This map is consulted per BLOCK, so a row for a family no block uses is
# inert; what it is not is optional. A lesson author who adds a block whose
# kind is missing from here gets it left in `core` as an unknown block type
# instead of being lifted into `activities[]`, and the failure is silent in
# the direction that looks fine.
_INSTRUMENT_SEGMENTS = {
    # p1-01 · Energy stores
    "store-audit":         "check",
    "store-or-pathway":    "check",
    # p1-02 · Energy transfers: before and after
    "before-after-bench":  "practical",
    # p1-03 · Conservation of energy
    "energy-audit":        "practical",
    "mechanism-or-energy": "check",
    # p1-04 · Heating and thermal equilibrium
    "equilibrium-bench":   "practical",
    # p1-05 · Conduction
    "conduction-race":     "practical",
    "particle-relay":      "check",
    # p1-06 · Radiation
    "radiation-cube":      "practical",
    "across-the-gap":      "check",
    # p1-07 · Keeping energy in: insulation
    "lagging-bench":       "practical",
    # p1-08 · Simple machines
    "machine-bench":       "practical",
    # ⚠️ NOT a P1 family — C2's, placed here. See the header.
    "fifa-pick":           "check",
}

# Keys that stay on the BLOCK when an instrument is lifted, because they
# describe where the block sits in the document rather than what the
# instrument does.
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

        # The anchor is the only stable name an inline instrument has, and it
        # is already unique within the lesson because it is a DOM id.
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
    """The authored P1 lesson records, in slot order, normalised.

    Modules are discovered by name in sorted order, so `lesson_04_*` sorts
    after `lesson_03_*` and the build is deterministic.
    """
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
