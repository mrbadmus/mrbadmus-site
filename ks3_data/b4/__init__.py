"""B4 — Breathing and gas exchange, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b4/` and under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). Shape follows `ks3_data/b3/`, which
follows `ks3_data/c1/`, `ks3_data/c2/`, `ks3_data/b2/` and `ks3_data/b1/`: each
module exports a single `LESSON` dict and this file collects them.

Every student-facing string is lifted byte-identical from the approved page.

── `KS3.B.GAS.01` is SPLIT ──────────────────────────────────────────────

Minted in `ks3_data/substatements.py` for this unit. The bullet reads *"the
structure and functions of the gas exchange system in humans, including
adaptations to function"*, and its own "including" is the seam:

    GAS.01a  the parts air passes through and what each does
                                            `the-gas-exchange-system`
    GAS.01b  adaptations of the exchange surface to its function
                                            `alveoli-built-for-exchange`

Teaching adaptation before the student knows what the parts ARE is the order
that makes adaptation sound like decoration. `GAS.02`, `GAS.03` and `GAS.04`
are owned whole, one lesson each.

── ⚑ A STATUTORY GAP IS OPEN IN THIS UNIT, AND IT IS RULED ──────────────

`KS3.B.GAS.02` asks for *"simple measurements of lung volume"*. Design's
`how-breathing-works` contains none — the bell-jar is a pressure model with
volume READOUTS, not a measurement the student takes. Ruled not to block this
build (MRB-244); Design patches it later.

The clause is deliberately NOT narrowed to hide this. `GAS.02` is owned whole
by `how-breathing-works` at the bullet's full width, so what is missing stays
legible against what is claimed. Splitting it to give the measurement clause
its own sub-ID would need an owner, and there is no lesson to own it — a
sub-ID minted with no owner fails §4.4 rule 3's exactly-once check, which is
the correct failure for a gap nobody has agreed to leave open, and the wrong
one for a gap Mide has ruled on.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as B1, B2, B3, C1 and C2. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component, so an instrument is authored inline in `core` —
where its position in the document is obvious — and `_normalise()` lifts it
into `activities[]`, leaving the right SHELL behind it.

⚠️ The segment decides the SHELL and it is a real decision, not a label.
Measured from Design's own markup across all five pages: like B3, B4 is
uniform — every lesson carries exactly one flagship instrument and every one
sits on `ks3-block ks3-dark ks3-practical`. That uniformity is a finding, not
an assumption; a second instrument on a lighter ground would be `check` and
must be measured, never inherited from the flagship beside it.

    b4-01 #s-air      ks3-block ks3-dark ks3-practical  dark → practical
    b4-02 #s-model    ks3-block ks3-dark ks3-practical  dark → practical
    b4-03 #s-gradient ks3-block ks3-dark ks3-practical  dark → practical
    b4-04 #s-bench    ks3-block ks3-dark ks3-practical  dark → practical
    b4-05 #s-ledger   ks3-block ks3-dark ks3-practical  dark → practical

⚠️ EVERY ONE OF THESE IS ON INK. `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0), so every text rule in every B4 instrument has to
be scoped to at least (0,2,0) or it renders in the block's own colour rather
than its own. This has now bitten four separate builds; on this unit it would
bite all five lessons at once.

── Figures are declared and NOT drawn ───────────────────────────────────

Design's pages name figure slots in their legal lines that no artwork exists
for. They are declared here at `status: "needed"` rather than dropped, because
a declared figure is a tracked sourcing task in `docs/ks3/diagram-manifest.md`
and a dropped one is invisible. `needed` is not a build blocker (§4.10).
Nothing is invented to fill a slot.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B4 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
#
# ⚠️ Written in ONE pass, by the commander, deliberately. B3's eight
# instruments were authored by three agents in parallel and this dict is the
# one file they would all have had to edit; parallel writes to a single dict
# lose entries silently, and a lost entry here does not fail the build — it
# renders the instrument as an unlifted block and the page ships a bare list.
_INSTRUMENT_SEGMENTS = {
    "gas-compare":        "practical",
    "bell-jar":           "practical",
    "crossing-counter":   "practical",
    "fault-bench":        "practical",
    "two-process-ledger": "practical",
}

# Keys that stay on the BLOCK when an instrument is lifted, because they
# describe where the block sits in the document rather than what the
# instrument does.
_BLOCK_KEYS = ("type", "anchor", "id", "ground")


def _normalise(lesson):
    """Lift inline instrument blocks into `activities[]`. Returns the lesson."""
    core = lesson.get("core") or []
    acts = list(lesson.get("activities") or [])
    known = {a.get("id") for a in acts}
    out = []

    for block in core:
        kind = block.get("type")
        segment = _INSTRUMENT_SEGMENTS.get(kind)
        if not segment:
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

        shell = {"type": segment, "id": act_id, "anchor": block.get("anchor")}
        # `ground` is a property of the BLOCK Design drew, not of the
        # instrument inside it, so it stays on the shell.
        if block.get("ground"):
            shell["ground"] = block["ground"]
        out.append(shell)

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The authored B4 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. B4 is expected to reach five of five.
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
