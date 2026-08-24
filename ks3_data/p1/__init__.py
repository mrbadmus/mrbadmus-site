"""P1 — *Energy transfers*, as one module per lesson.

The first physics unit in the key stage. The package layout follows
`ks3_data/c10/` exactly; nothing about it is new and nothing about it is
physics.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p1/`. Her page wins outright.

── ⚠️ THE RUN THIS UNIT REPLACES ───────────────────────────────────────

An earlier MRB-223 run authored eight P1 lessons believing Design had drawn
nothing, having globbed one folder and found no `physics/` in it. She had
drawn all seventy physics lessons, untracked in the main worktree under
`KS3 P<n> lessons/`. That work is kept at
`docs/ks3/holding/p1-code-authored-2026-08-24/` and is deliberately NOT used
as a starting point: MRB-205 forbids an invented shape, and reconciling one
against a drawing keeps the invention.

── ⚖️ RULED · THE OWNERSHIP MAP ────────────────────────────────────────

Six statutory statements, eight lessons. §10.2 wants every lesson's `covers`
non-empty and §4.4 rule 3 wants every statement owned exactly once, so two of
the six split at the grain Design actually teaches them:

    p1-01  energy-stores                      KS3.P.CIS.02a
    p1-02  energy-transfers-before-and-after  KS3.P.CIS.02b + KS3.P.ECT.03
    p1-03  conservation-of-energy             KS3.P.CIS.01  + KS3.P.CIS.03
    p1-04  heating-and-thermal-equilibrium    KS3.P.ECT.02a
    p1-05  conduction                         KS3.P.ECT.02b
    p1-06  radiation                          KS3.P.ECT.02c
    p1-07  insulation                         KS3.P.ECT.02d
    p1-08  simple-machines                    KS3.P.ECT.01

Both mints are in `ks3_data/substatements.py` with the parent bullets quoted
in full. Two of the allocations are judgement calls worth writing down:

**`KS3.P.ECT.03` goes to p1-02, not to p1-01.** The bullet is a list of
transfer PROCESSES — "changing motion, dropping an object, completing an
electrical circuit, stretching a spring, metabolism of food, burning fuels" —
and every one is a before-and-after situation. p1-01 names the stores; p1-02
is where a student says which went down and which went up, and Design's
`DEVICES` bench is literally that list. Putting it on p1-01 would have the
stores lesson teach six transfers before the word *transfer* is defined.

**`KS3.P.CIS.03` goes to p1-03, with `KS3.P.CIS.01`.** The bullet says to use
physical processes and mechanisms, RATHER THAN ENERGY, to explain the
intermediate steps. That instruction only becomes reasonable once a student
knows the total never changes: if energy is conserved it cannot have been
consumed, and a quantity that is never consumed can never be why anything
happened. Conservation is the premise and "name the mechanism" is the
conclusion, so they are one lesson — which is how Design draws it, with
`#s-think` doing exactly that work.

── FOUR RAIL STOPS PER LESSON ──────────────────────────────────────────

Measured off Design's own `RAIL` constant on each delivered page, which is
what `ks3_rail_manifest.py` reads and what `ks3_parity.check_rail_matches_
design` checks the built page against:

    p1-01  s-hook s-audit  s-think   s-ladder   4
    p1-02  s-hook s-tally  s-waste   s-ladder   4
    p1-03  s-hook s-bench  s-balance s-ladder   4
    p1-04  s-hook s-two    s-flow    s-ladder   4
    p1-05  s-hook s-bar    s-touch   s-ladder   4
    p1-06  s-hook s-routes s-word    s-ladder   4
    p1-07  s-hook s-plan   s-trial   s-ladder   4
    p1-08  s-hook s-bench  s-worked  s-ladder   4

⚠️ **A SECTION IS NOT A STOP.** `p1-02`–`p1-08` all carry a `#s-think`
section that is NOT on the rail, and `p1-07` and `p1-08` each carry a second
one (`#s-ice`, `#s-balance`). Design's audit records the cut and the
`NOTES-C9` §10 correction behind it: the misconception block loses its stop
where the lesson has a fuller third section. Every section keeps its `id`, so
in-page anchors and the tutor link are untouched.

`p1-01` is the exception and it is not an oversight — its `#s-think` holds
the store/pathway sort, six items a student completes, so it IS the fuller
section and it keeps the stop. Counted off the drawing, not inferred.

── ⚠️ SHELLS ARE MEASURED, NOT INFERRED ────────────────────────────────

The segment each family renders into is measured off Design's `class`
attribute on the section — §4 of the build contract records that B1 got two
of six shells wrong by inferring them from family names.

Bare `ks3-block` → `check`. `ks3-block ks3-dark ks3-practical` →
`practical`. `ks3-block ks3-misconception` → `misconception`.
"""

import importlib
import pkgutil

# Instrument block types seen in authored P1 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the note above.
#
# ⚠️ ROWS EXIST FOR FAMILIES WHOSE LESSONS ARE NOT WRITTEN YET. This map is
# consulted per BLOCK, so a row for a family no block uses is inert; what it
# is not is optional. A lesson author who adds a block whose kind is missing
# from here gets it left in `core` as an unknown block type instead of being
# lifted into `activities[]`, and the failure is silent in the direction that
# looks fine (MRB-244).
_INSTRUMENT_SEGMENTS = {
    # p1-01 · Energy stores
    "store-audit":         "check",
    "store-pathway-sort":  "misconception",
    # p1-02 · Energy transfers: before and after
    #   `#s-tally` is bare `ks3-block`                       → check
    #   `#s-waste` is `ks3-block ks3-dark ks3-practical`     → practical
    "before-after-tally":  "check",
    "waste-sort":          "practical",
    "running-total":         "check",
    "conservation-beam":     "check",
    "two-quantities":        "check",
    "one-way-flow":          "practical",
    "conduction-bench":      "check",
    "touch-test":            "practical",
    "three-routes":          "check",
    "radiation-word-sort":   "practical",
    "insulation-trial":      "check",
    "ice-trial":             "practical",
    "plan-the-trial":        "check",
    "lever-bench":           "check",
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

    Modules are discovered by name in sorted order, so `lesson_02_*` sorts
    after `lesson_01_*` and the build is deterministic. A slot with no module
    here renders a coming-soon page (§11 decision 8) rather than 404.
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
