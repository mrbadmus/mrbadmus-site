"""C2 — Atoms, elements and compounds, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c2/` and the measured specification in
`docs/ks3/c2-inventory/PAYLOAD-MAP.md`, under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/b2/`
exactly, which follows `ks3_data/b1/`: each module exports a single `LESSON`
dict, and this file collects them.

Every student-facing string is lifted byte-identical from the approved page
via `node tools/extract_design_payload.js` for the top-level constants, and
from the payload map's recorded line ranges for the strings that live inside
`renderVals()` — which is where between 240 and 900 words per lesson live,
and which a lift of the top-level constants alone silently loses.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as B1's and B2's, and the same mechanism. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component. C2's nine instruments are interactive tasks
with a demand, a commitment and a reveal, which is what §5.5's activity record
is for. Each lesson authors its instrument inline in `core`, where its
position in the document is obvious, and `_normalise()` lifts it into
`activities[]` leaving the right SHELL behind it.

⚠️ The segment decides the SHELL and it is a real decision, not a label:
`practical` is ink-dark, `check` is a plain light `ks3-block`. Measured from
Design's own markup, page by page (PAYLOAD-MAP §2.3, §3.3, §4.3, §5.3, §6.3,
§7.3):

    c2-01 #s-model    ks3-block                        light  → check
    c2-01 #s-scale    ks3-block ks3-dark ks3-practical dark   → practical
    c2-02 #s-bench    ks3-block                        light  → check
    c2-03 #s-bench    ks3-block ks3-dark ks3-practical dark   → practical
    c2-03 #s-sort     ks3-block (inset ground)         light  → check
    c2-04 #s-sort     ks3-block                        light  → check
    c2-04 #s-read     ks3-block (inset ground)         light  → check
    c2-05 #s-builder  ks3-block ks3-dark ks3-practical dark   → practical
    c2-05 #s-limit    ks3-block (inset ground)         light  → check
    c2-06 #s-balance  ks3-block ks3-dark ks3-practical dark   → practical
    c2-06 #s-build    ks3-block (inset ground)         light  → check

⚠️ `#s-model` is the trap the map calls out by name: it LOOKS like the
flagship of a MODEL lesson and it is a light block. Mapping it to `practical`
would paint the whole instrument on ink and resolve every text token wrong.

The inset ground is authored per block (`ground: "inset"`), because it is a
property of the block Design drew and not of the instrument inside it.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C2 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "claim-switch":           "check",
    "scale-zoom":             "practical",
    "test-budget-bench":      "check",
    "mixture-compound-dish":  "practical",
    "verdict-cards":          "check",
    "origin-grid":            "check",
    "formula-builder":        "practical",
    "model-limit":            "check",
    "balance-bench":          "practical",
    "fifa-pick":              "check",
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
        out.append({"type": segment, "id": act_id,
                    "anchor": block.get("anchor")})

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The authored C2 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is
    the structure-first guarantee (§11 decision 8) and not a gap to be
    apologised for.
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
