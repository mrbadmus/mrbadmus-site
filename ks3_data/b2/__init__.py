"""B2 — Movement: skeleton and muscles, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/b2/` and the measured specification in
`docs/ks3/b2-inventory/PAYLOAD-MAP.md`, under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/b1/`
exactly, which is the current pattern and supersedes the single-file one:
each module exports a single `LESSON` dict, and this file collects them.

Every student-facing string is lifted byte-identical from the approved page
via `node tools/extract_design_payload.js`. Nothing science-bearing is
retyped — a typo in retyped prose is invisible and crosses the examiner gate.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as B1's, and the same mechanism. §5.1.1's block vocabulary is
CLOSED and MRB-203's registry fails the build on a block type with no
registered component. The four B2 instruments are interactive tasks with a
demand, a commitment and a reveal, which is what §5.5's activity record is
for; admitting each as a page-level segment would grow the vocabulary by four
for no gain and put an instrument on the same footing as `hook` and `summary`.

So each lesson authors its instrument inline in `core`, where its position in
the document is obvious, and `_normalise()` lifts it into `activities[]`
leaving the right SHELL behind it.

⚠️ The segment decides the SHELL and it is a real decision, not a label:
`practical` is ink-dark, `check` is a plain light `ks3-block`. B1 got two of
six wrong and it took a layer-C assertion to say so — a whole instrument
painted on the wrong ground. Measured from Design's own markup, page by page:

    b2-01 #s-switch  ks3-block                        light  → check
    b2-01 #s-sort    ks3-block (inset ground)         light  → check
    b2-02 #s-bench   ks3-block ks3-dark ks3-practical dark   → practical
    b2-02 #s-cases   ks3-block (inset ground)         light  → check
    b2-03 #s-bench   ks3-block ks3-dark ks3-practical dark   → practical
    b2-03 #s-pairs   ks3-block (inset ground)         light  → check
    b2-04 #s-bench   ks3-block ks3-dark ks3-practical dark   → practical
    b2-04 #s-build   ks3-block (inset ground)         light  → check
    b2-04 #s-meters  ks3-block (default ground)       light  → check

The inset ground is authored per block (`ground: "inset"`), because it is a
property of the block Design drew and not of the instrument inside it — the
same `job-sort` sits on inset in all three lessons and would sit on a card
anywhere else.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B2 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "system-switch": "check",
    "job-sort":      "check",
    "joint-bench":   "practical",
    "muscle-pair":   "practical",
    # ⊕ b2-04. `arm-lever` is the only one of the three that inverts: Design
    # paints the rig on ink like the other two benches, and paints both of
    # b2-04's other instruments on a light block. `#s-meters` takes the
    # DEFAULT card ground rather than the inset one `#s-build` takes, so it
    # authors no `ground` at all.
    "arm-lever":     "practical",
    "lever-steps":   "check",
    "meter-compare": "check",
}

# Keys that stay on the BLOCK when an instrument is lifted, because they
# describe where the block sits in the document rather than what the
# instrument does. `ground` is one of them: it paints the section, and the
# section is what `r_activity` emits.
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
    """The authored B2 lesson records, in slot order, normalised.

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
