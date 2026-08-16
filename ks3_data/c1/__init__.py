"""C1 — Particles and their behaviour, as one module per lesson.

⚠️ **This unit is a REBUILD over six pages that are already live.** The
superseded bodies were inline in `ks3_data/chemistry_c1_particles.py`, which
becomes a thin wrapper exactly as `biology_b1_cells.py` did. They stay
reachable in git history — that is the record, and nothing is deleted to tidy
up.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c1/` and the measured specification in
`docs/ks3/c1-inventory/PAYLOAD-MAP.md`, under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). Shape follows `ks3_data/c2/`, which
follows `ks3_data/b2/` and `ks3_data/b1/`.

Every student-facing string is lifted byte-identical from the approved page via
`node tools/extract_design_payload.js` for the top-level constants, and from
the payload map's recorded line ranges for the strings that live inside
`renderVals()`. The second half matters more here than anywhere: c1-03's
`PHASE` (the five plateau paragraphs — the science core of that lesson),
c1-04's shared wrong-answer note and c1-06's `VERDICTS` are all authored INSIDE
`renderVals`, so a lift of the top-level constants alone loses them silently.

── Slugs do not move ────────────────────────────────────────────────────

All six slugs, titles and families are identical live vs Design and match
`ks3_data/structure.py:156–164` character for character. No URL breaks, no
`requires` repointing, no redirects, no scheme-of-work row moves. Verified
rather than assumed — PAYLOAD-MAP §7.1.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as B1, B2 and C2. §5.1.1's block vocabulary is
CLOSED and MRB-203's registry fails the build on a block type with no
registered component, so an instrument is authored inline in `core` — where its
position in the document is obvious — and `_normalise()` lifts it into
`activities[]`, leaving the right SHELL behind it.

⚠️ The segment decides the SHELL and it is a real decision, not a label:
`practical` is ink-dark, `check` is a plain light `ks3-block`. Measured from
Design's own markup, page by page (PAYLOAD-MAP §1.3, §2.3, §3.3, §4.3, §5.3,
§6.3), because the contract's own roster says to follow the measurement and not
the table where they disagree:

    c1-01 #s-cut      ks3-block                        light  → check
    c1-01 #s-gap      ks3-block ks3-dark ks3-practical dark   → practical
    c1-02 #s-bench    ks3-block                        light  → check
    c1-02 #s-matrix   ks3-block                        light  → check
    c1-03 #s-curve    ks3-block                        light  → check
    c1-03 #s-bubble   ks3-block ks3-dark ks3-practical dark   → practical
    c1-03 #s-think    ks3-block ks3-misconception      amber  → misconception
    c1-04 #s-bench    ks3-block                        light  → check
    c1-04 #s-predict  ks3-block ks3-dark ks3-practical dark   → practical
    c1-05 #s-walk     ks3-block                        light  → check
    c1-05 #s-scale    ks3-block ks3-dark ks3-practical dark   → practical
    c1-06 #s-bench    ks3-block                        light  → check
    c1-06 #s-verdict  ks3-block ks3-dark ks3-practical dark   → practical
    c1-06 #s-history  ks3-block                        light  → check

⚠️ `sort-cards` is the one instrument that is NOT its own block. It lives
inside c1-03's `#s-think`, which is a misconception shell — so the sorter is
the misconception's mechanism rather than a bench of its own, and its segment
is `misconception` accordingly. Mapping it to `check` would paint c1-03's
confrontation on the wrong ground and lose the amber that says "a wrong idea is
being handled here".

⚠️ `keyed-commit` is shared by c1-03 (`#s-bubble`) and c1-06 (`#s-verdict`).
It takes the **c1-06 shape** — the reply attached per option — because that is
the shape that generalises; c1-03's identical behaviour is branched in code on
the approved page and is expressed here in the same per-option form.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C1 data, mapped to the §5.1.1 segment
# they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "halving-bench":      "check",
    "gap-test-rig":       "practical",
    "state-bench":        "check",
    "state-matrix":       "check",
    "heating-bench":      "check",
    "keyed-commit":       "practical",
    "sort-cards":         "misconception",
    "collision-counter":  "check",
    "prediction-stack":   "practical",
    "random-walk-bench":  "check",
    "scale-cards":        "practical",
    "evidence-bench":     "check",
    "model-timeline":     "check",
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
    """The authored C1 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. C1 is expected to reach six of six.
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
