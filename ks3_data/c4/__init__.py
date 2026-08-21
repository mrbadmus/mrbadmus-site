"""C4 — Chemical reactions, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c4/` under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/c3/`
exactly, which follows `ks3_data/c2/`: each module exports a single `LESSON`
dict, and this file collects them.

Every student-facing string is lifted byte-identical from the approved page
via `node tools/extract_design_payload.js` for the top-level constants, and by
reading `lessonVals()` for the strings that live inside it — which is where
most of a lesson's words live, and which a lift of the top-level constants
alone silently loses.

⊕ `c4-05`'s `EQS` is one of the two payloads the extractor could not see until
the hoisting fix landed (MRB-272 measured it: `c3-01` 7→8 constants and
`c4-05` 3→4, nothing else in 140 pages moved). It was confirmed present and
intact before this unit was authored — four equations, each carrying `left`,
`right`, `target` and its own `note`. A future pass that finds `EQS` empty is
looking at a regressed extractor, not at a page that never had it.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as C3's, and the same mechanism. §5.1.1's block vocabulary is
CLOSED and MRB-203's registry fails the build on a block type with no
registered component. C4's twelve instruments are interactive tasks with a
demand, a commitment and a reveal, which is what §5.5's activity record is
for. Each lesson authors its instrument inline in `core`, where its position
in the document is obvious, and `_normalise()` lifts it into `activities[]`
leaving the right SHELL behind it.

⚠️ THE SEGMENT IS A MEASUREMENT, AND IN THIS UNIT IT IS NOT QUITE UNIFORM.
Measured from Design's own markup, every anchored instrument section in C4
carries `class="ks3-block"` — light — with exactly two carrying a second
class, and the second class is the measurement:

    c4-01 #s-pairs       ks3-block                  light  → check
    c4-01 #s-chain       ks3-block                  light  → check
    c4-02 #s-rearr       ks3-block                  light  → check
    c4-02 #s-impossible  ks3-block                  light  → check
    c4-03 #s-builder     ks3-block                  light  → check
    c4-03 #s-read        ks3-block                  light  → check
    c4-04 #s-bench       ks3-block                  light  → check
    c4-04 #s-cover       ks3-block                  light  → check
    c4-04 #s-worked      ks3-block                  light  → check
    c4-04 #s-check       ks3-block ks3-check        light  → check
    c4-05 #s-balance     ks3-block                  light  → check
    c4-05 #s-forbidden   ks3-block ks3-misconception light → misconception

There is no ink-dark practical block anywhere in C4, exactly as there is none
in C3. The only dark sections in the unit are the hook
(`ks3-block ks3-dark ks3-hook`) and the closing key note
(`ks3-block ks3-dark ks3-keynote`), both of which the engine emits itself.

⚖️ `forbidden-move` IS DRAWN ON A MISCONCEPTION GROUND AND IS MAPPED THAT WAY.
It would have been easy to send all twelve to `check` and let the amber ground
be the one thing that quietly went missing — the block confronts `REACT-08`
("an equation can be balanced by changing the small numbers in a formula") and
Design gives it the amber treatment every confrontation in the course gets.
Mapping it to `check` would repaint a confrontation as an ordinary exercise
and resolve every token inside it wrong. Amber warns a wrong IDEA; that is
precisely what this block is for.

── `mass-cover` is an ACTIVITY, and that is deliberate ──────────────────

⚠️ There is a comment at `build_ks3.py:2022` saying `cover-triangle` is NOT an
activity kind, carries no `data-stage-done`, and that "MRB-208 keeps it off
the rail". That is TRUE OF THE READ-ONLY BAR VARIANT `r_cover_bar()` that
c2-06 ships, and it does NOT govern this unit.

Design's own page settles c4-04: `s-cover` is in her `RAIL`, and her `DONE()`
reads `if (id === 's-cover') return s.cover !== null` — it ticks when the
student has PRESSED a cover button. A press is a commitment, so the stop has a
real completion signal and MRB-249 requires it. `mass-cover` is therefore a
registered instrument with `data-stage-done="0"`, and it is deliberately NOT
named `cover-bar`: `r_cover_bar` already exists in `build_ks3.py` and two
things wearing one name is the `data-critique`/`data-critiq` trap.

It is still drawn as a PART-WHOLE BAR. Conservation of mass is a SUM, and
MRB-204 gives a sum a beam and never a triangle.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C4 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "change-pairs":         "check",
    "chain-build":          "check",
    "atom-rearranger":      "check",
    "impossible-ask":       "check",
    "equation-builder":     "check",
    "equation-read":        "check",
    "mass-bench":           "check",
    "mass-cover":           "check",
    "mass-worked":          "check",
    "mass-check":           "check",
    "coefficient-balancer": "check",
    # Measured amber. See the ruling in the docstring above.
    "forbidden-move":       "misconception",
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
    """The authored C4 lesson records, in slot order, normalised.

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
