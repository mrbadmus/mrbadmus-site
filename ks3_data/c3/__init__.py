"""C3 — Mixtures and separation, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c3/` under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/c2/`
exactly, which follows `ks3_data/b1/`: each module exports a single `LESSON`
dict, and this file collects them.

Every student-facing string is lifted byte-identical from the approved page
via `node tools/extract_design_payload.js` for the top-level constants, and by
reading `lessonVals()` for the strings that live inside it — which is where
between 240 and 900 words per lesson live, and which a lift of the top-level
constants alone silently loses.

⊕ The extractor gained a fix for this unit. `c3-01` builds every sample's
particle strip through a page-local `dots()` helper, so `SAMPLES` — the whole
eight-sample payload of the unit's flagship — could not be evaluated and came
back as `dots is not defined`. Top-level `function` declarations are now
hoisted into the sandbox before the constants are evaluated. Measured across
all 140 frozen reference pages, that fix changes exactly two results: `c3-01`
7→8 constants and `c4-05` 3→4. Nothing else moved.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as B1's, B2's and C2's, and the same mechanism. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component. C3's seven instruments are interactive tasks
with a demand, a commitment and a reveal, which is what §5.5's activity record
is for. Each lesson authors its instrument inline in `core`, where its
position in the document is obvious, and `_normalise()` lifts it into
`activities[]` leaving the right SHELL behind it.

⚠️ THE SEGMENT IS A MEASUREMENT, AND IN THIS UNIT THE MEASUREMENT IS UNIFORM.
`practical` is ink-dark; `check` is a plain light `ks3-block`. C2 got four of
its nine instruments on ink and the map had to be read block by block to find
out which. C3 does not: measured from Design's own markup, every instrument
section in all seven lessons carries `class="ks3-block"` and nothing else.

    c3-01 #s-sorter    ks3-block   light  → check
    c3-02 #s-lab       ks3-block   light  → check
    c3-03 #s-steps     ks3-block   light  → check
    c3-03 #s-build     ks3-block   light  → check
    c3-04 #s-bench     ks3-block   light  → check
    c3-04 #s-jobs      ks3-block   light  → check
    c3-05 #s-still     ks3-block   light  → check
    c3-06 #s-lab       ks3-block   light  → check
    c3-07 #s-critique  ks3-block   light  → check
    c3-07 #s-bench     ks3-block   light  → check

There is no ink-dark practical block anywhere in C3. The only dark sections in
the unit are the hook (`ks3-block ks3-dark ks3-hook`) and the closing key note
(`ks3-block ks3-dark ks3-keynote`), both of which the engine emits itself.
That is a fact about the unit worth stating out loud rather than leaving to be
re-derived: a future pass that "restores" a practical shell here would be
painting an instrument on a ground Design did not draw it on, and resolving
every text token inside it wrong.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C3 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "purity-sorter":       "check",
    "dissolve-lab":        "check",
    "sequence-rebuild":    "check",
    "crystal-bench":       "check",
    "still-run":           "check",
    "chroma-run":          "check",
    "melting-point-bench": "check",
    # ⊕ Two more, and they are NOT the unit's seven flagships. Design draws a
    # second, smaller instrument on two pages — `#s-jobs` on c3-04 (three
    # real jobs, pick the method for each) and `#s-critique` on c3-07 (four
    # steps of somebody else's plan, judged before the student writes their
    # own). Both are light `ks3-block`s, measured like the rest.
    #
    # ⚖️ REGISTERED AS C3's OWN, NOT REUSED. Both are the drawn shape of a
    # family another unit already owns — `verdict-cards` in `ks3_art/c2.py`,
    # `critique-steps` in a biology module — and reuse was the obvious move.
    # It was not taken. Reuse here means either depending on another unit's
    # module or promoting a family into `ks3_art/core.py`, and `core.py` is a
    # SHARED file: a lane that edits it stops being a lane. The payloads
    # differ anyway (C3's jobs carry a task, an answer and a why; C2's cards
    # carry a headline and a layout), so the reuse would have been a rename
    # plus a widened payload, which is a new family wearing an old name.
    #
    # One unit, one module, nine families. That is what MRB-271 bought.
    "method-choice":       "check",
    "plan-critique":       "check",
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
    """The authored C3 lesson records, in slot order, normalised.

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
