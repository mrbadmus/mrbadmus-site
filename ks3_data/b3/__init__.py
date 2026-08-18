"""B3 — Nutrition and digestion, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b3/` and under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). Shape follows `ks3_data/c1/`, which
follows `ks3_data/c2/`, `ks3_data/b2/` and `ks3_data/b1/`: each module exports
a single `LESSON` dict and this file collects them.

Every student-facing string is lifted byte-identical from the approved page.

── `KS3.B.NUT.02` is SPLIT, and B3 owns half of it ──────────────────────

Ruled by Mide on 16 Aug 2026 (MRB-232). The statement was claimed by both this
unit and Physics P2, and §7.4 had given the whole of it to P2 with B3 holding a
reference slot that generated no page at all. It is two lessons wearing one
bullet and it splits at that seam:

    B3  what you need and why — requirements, imbalance, and what follows
        from getting it wrong.                  `energy-in-food-and-what-you-need`
    P2  comparing energy values from food labels in kJ — the arithmetic
        and the units.                          `energy-in-food`

P2's link back here is a `references` EDGE, never prose, so neither page
repeats the other and §4.6's single-source rule holds. The full ruling, and why
it must not be re-opened from one file, is in `docs/ks3/statutory-register.md`.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as B1, B2, C1 and C2. §5.1.1's block vocabulary is
CLOSED and MRB-203's registry fails the build on a block type with no
registered component, so an instrument is authored inline in `core` — where its
position in the document is obvious — and `_normalise()` lifts it into
`activities[]`, leaving the right SHELL behind it.

⚠️ The segment decides the SHELL and it is a real decision, not a label.
Measured from Design's own markup across all eight pages: B3 is unusually
uniform — every lesson carries exactly one flagship instrument and every one of
them sits on `ks3-block ks3-dark ks3-practical`, so every flagship is
`practical`. That uniformity is the finding, not an assumption; a second
instrument on a lighter ground would be `check` and must be measured, not
inherited from the flagship beside it.

    b3-01 #s-plate    ks3-block ks3-dark ks3-practical  dark → practical
    b3-02 #s-bench    ks3-block ks3-dark ks3-practical  dark → practical
    b3-03 #s-ledger   ks3-block ks3-dark ks3-practical  dark → practical
    b3-04 #s-cases    ks3-block ks3-dark ks3-practical  dark → practical
    b3-05 #s-journey  ks3-block ks3-dark ks3-practical  dark → practical
    b3-06 #s-bench    ks3-block ks3-dark ks3-practical  dark → practical
    b3-07 #s-fold     ks3-block ks3-dark ks3-practical  dark → practical
    b3-08 #s-jobs     ks3-block ks3-dark ks3-practical  dark → practical

⚠️ EVERY ONE OF THESE IS ON INK. `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0), so every text rule in every B3 instrument has to
be scoped to at least (0,2,0) or it renders in the block's own colour rather
than its own. This has bitten three separate builds; on this unit it would bite
all eight lessons at once.

── Enzyme rate is NOT owned content ─────────────────────────────────────

MRB-199: `enzymes-in-digestion` owns the CATALYST clause of `KS3.B.NUT.04`
("enzymes simply as biological catalysts"). Enzyme RATE — the temperature and
pH curves, the optimum, denaturing — has no KS3 statutory statement and belongs
in the Year 9 bridge. Design's b3-06 teaches it in full, and the page is built
as drawn because MRB-205 says the approved page is what renders; what does NOT
happen is the rate material being CLAIMED under a statutory statement. See the
lesson module for the `covers` it declares and the note beside it.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B3 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "band-commit":   "practical",
    "test-bench":    "practical",
    "person-ledger": "practical",
    "clinic-cases":  "practical",
    "gut-journey":   "practical",
    "enzyme-run":    "practical",
    "fold-builder":  "practical",
    "job-switch":    "practical",
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
    """The authored B3 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. B3 is expected to reach eight of eight.
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
