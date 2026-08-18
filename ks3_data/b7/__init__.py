"""B7 — Photosynthesis, as one module per lesson.

Authored against Claude Design's approved reference screens in
`KS3 B7 lessons/`, under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`) and the payload schema written for this
run at `docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`. Shape follows `ks3_data/b5/`,
which follows B4, B3, C1, C2, B2 and B1: each module exports a single `LESSON`
dict and this file collects them.

Every student-facing string is lifted byte-identical from the approved page.

── Statutory position: all three PHOT statements covered, by three lessons ──

    B.PHOT.01  reactants, products, word summary   `the-photosynthesis-reaction`
    B.PHOT.03  adaptations of leaves               `leaves-built-for-the-job`
    B.PHOT.02  dependence of almost all life       `why-almost-all-life-depends-on-it`

`B.NUT.06` (carbohydrates made in leaves; minerals and water from the soil) is
covered by b7-01's van Helmont treatment.

`testing-a-leaf-for-starch` claims **no subject statement**. It is the practical
the other three are argued from, which is why it sits third rather than second.
Its `covers` is anchored on `KS3.WS.*` per §5.7.1 — every INVESTIGATION lesson
does this, §10.2 requires `covers` non-empty, and WS ids are exempt from the
exactly-once ownership check in `build_ks3.validate()`.

── ⊕ DESIGN DRAWS FOUR RAIL STOPS PER PAGE. ALL FOUR TICK. ───────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This heading used to read "THREE CAN
TICK", and all four B7 authoring passes reached that call independently — which
is why it was recorded here once rather than four times, and why the reversal
is recorded here once too.

On every B7 page, one rail stop is anchored to a section whose completion
predicate is Design's own, stated a second time for the instrument one section
to its left — `s.everTested` on b7-01 `#s-summary`, `s.moved` on b7-02
`#s-features`, `s.everRan` on b7-03 `#s-method`, `s.everArrived` on b7-04
`#s-jobs`. Each of those sections is static cards: no control, no commitment,
no field.

The old argument: `ks3_parity.check_rail_reachable()` requires the anchored
section to contain one of five literal DOM signals — `data-stage-done`,
`class="ks3-rung`, `data-reveal`, `ks3-reveal-btn`, `class="ks3-option` — these
four carry none, so a stop on them could never tick and would FAIL the build.
Hence three stops per page, anchors kept.

Two things overrule it.

MRB-205 binds and is not re-argued: Design draws, we render; no invented and no
dropped page structure; page wins over engine. A gate that cannot express what
Design drew is the thing that gives way, and it has.

And the repeated predicate is Design stating the tick condition, in a
rail-level `isDone()`. Each of those static sections is the PAYOFF of the
instrument beside it, carrying no control precisely because the instrument
already took the student's commitment. That relationship is a MIRROR:
`build_ks3.py` serialises a `mirrors` key into `data-rail-stages`, and
`wireRail`'s `paint()` in `shared/ks3.js` resolves it at rail level rather than
searching the section for a signal. `ks3_parity.check_rail_matches_design`
gates the built rail against `docs/ks3/rail-manifest.md`.

So: FOUR stops per page, anchors unchanged, hash links and `elicited_by` values
resolving exactly as before. b4-03 `#s-built`, b5-06 `#s-designs`, b6-03
`#s-four`, c1-02 `#s-matrix` and the rest are restored the same way. NOTES-B7
§3's "four in all four" is followed, not reported.

⚠️ **`#s-tuner` is the one stop that depends on the RENDERER, not the record.**
The signal test is a plain substring search over the built page's STATIC markup.
Design builds her dial buttons in JavaScript as `let cls = 'ks3-option'`, which
does **not** match the signal `class="ks3-option` — the attribute prefix is part
of it. If `r_leaf_tuner` emits its dials only from JS, that stop ships unable to
ever tick. Emit them as static `<button class="ks3-option" aria-pressed=…>`
inside `<ul class="ks3-options">`; that also puts them under the existing
`.ks3-dark .ks3-option` tone rules, which is where an ink-dark bench belongs.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as B1–B6, C1 and C2. §5.1.1's block vocabulary is
CLOSED and MRB-203's registry fails the build on a block type with no registered
component, so an instrument is authored inline in `core` — where its position in
the document is obvious — and `_normalise()` lifts it into `activities[]`,
leaving the right SHELL behind it.

⚠️ Measured from Design's own markup on all four pages, not inherited:

    b7-01 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical
    b7-02 #s-tuner   ks3-block ks3-dark ks3-practical   dark → practical
    b7-03 #s-bench   ks3-block ks3-dark ks3-practical   dark → practical
    b7-04 #s-trace   ks3-block ks3-dark ks3-practical   dark → practical

⚠️ ALL FOUR ARE ON INK. `.ks3-dark p` is (0,1,1) and beats a bare instrument
class at (0,1,0), so every text rule in every B7 instrument must be scoped to at
least (0,2,0). This trap has now bitten ten builds. ⊕ **As of MRB-245 it is
GATED** — `ks3_parity.check_dark_text_specificity()` resolves the real cascade
winner on every element on every ink ground and fails when a generic
`.ks3-dark <type>` rule beats a component's own colour. Scoping is no longer a
thing to remember; forgetting it is now a red build.

── Figures: EMPTY ON ALL FOUR, and that is measured, not an omission ─────

No B7 page draws an `<img>`, a `<figure>` or a placeholder — checked on all
four. §4.10 allows an empty `figures` for a lesson carried by its interactives.
NOTES-B7 flag 12 names a leaf cross-section as the obvious candidate, records
that it is **not in `docs/ks3/diagram-manifest.md`**, and that Design taught the
internal structure in b7-02's five feature cards instead. Nothing is declared,
because declaring a slot means writing a caption and a caption would pre-empt
the ruling flag 12 asks for. Mide's to rule on; the flag is not dropped.

── Misconceptions: the `PLANT` family, opened by this unit ──────────────

`PLANT-01`..`PLANT-08`, two per lesson, written into
`docs/ks3/misconception-register.md`. `PLANT-09`..`PLANT-12` were pre-allocated
one per lesson as spares, none was claimed, and they stay **permanently
unused** — the same discipline as `DRUG-07` and `REPRO-17`/`20`/`21`/`23`.

⚑ NOTES-B7 §4 states these eight were already written into the register with a
new prefix row. They were not; `PLANT` was still listed among the families *not
yet opened*. They were written from the four authored pages during MRB-245.
`NOTES-B5` made the same claim about `REPRO`. Second occurrence, one process
note rather than eight.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B7 data, mapped to the §5.1.1 segment
# they render as — measured from Design's markup, see the table above.
#
# ⚠️ Written in ONE pass, by the commander, deliberately. Four authors worked
# this unit in parallel and this dict is the one file they would all have had to
# edit; parallel writes to a single dict lose entries silently, and a lost entry
# here does not fail the build — it renders the instrument as an unlifted block
# and the page ships a bare list past a green kinds gate.
_INSTRUMENT_SEGMENTS = {
    "reactant-remover": "practical",
    "leaf-tuner":       "practical",
    "method-breaker":   "practical",
    "trace-it-back":    "practical",
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

        # The anchor is the only stable name an inline instrument has, and it is
        # already unique within the lesson because it is a DOM id.
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
        # `ground` is a property of the BLOCK Design drew, not of the instrument
        # inside it, so it stays on the shell.
        if block.get("ground"):
            shell["ground"] = block["ground"]
        out.append(shell)

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The authored B7 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. B7 reaches four of four.
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
