"""C9 — Metals and materials, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c9/` and her author's notes `NOTES-C9.md`. The shape
follows `ks3_data/c8/` exactly.

FOUR SLOTS, FOUR AUTHORED. `structure.py` gives C9 four and all four are here,
so this unit has no coming-soon page.

    c9-01 the-reactivity-series             KS3.C.MATS.01
    c9-02 predicting-displacement           KS3.WS.EXP.02
    c9-03 getting-metals-out-of-rocks       KS3.C.MATS.02
    c9-04 ceramics-polymers-and-composites  KS3.C.MATS.03

**No sub-IDs are minted.** All three subject statements are owned exactly once
and whole. `MATS.01` names "metals and carbon", and carbon's position is
established in lesson 1 rather than split with lesson 3 — §11.11 allows a
clause split and this statement does not need one, and a mint is permanent
once referenced.

⚑ **`predicting-displacement` anchors on WS, and the anchor is `KS3.WS.EXP.02`
— "make predictions using scientific knowledge and understanding".** NOTES-C9
§1 asks whether `KS3.WS.ANA.03` (identifying patterns) would be better. It
would not: ANA.03 describes what the SYNTHESIS PANEL does once the deck is
sorted, which is one moment at the end, while EXP.02 describes what the
student does EIGHT TIMES, one card at a time, before anything runs. The
archetype is what the student does. WS statements are exempt from
exactly-once ownership (§5.7), so nothing else is displaced by the choice.

── FIVE RAIL STOPS PER LESSON, NOT FOUR ─────────────────────────────────

`NOTES-C9.md` §10 records a correction to four. Design's own `RAIL` constant
draws FIVE on all four pages and `docs/ks3/rail-manifest.md` already records
them with the reference stop mirroring the hook. Where prose and instrument
disagree, the instrument is the measurement. Written out in
`lesson_01_the_reactivity_series.py`.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as C3's, C4's, C5's, C7's and C8's. Measured off
Design's markup, every anchored instrument section in all four lessons carries
`class="ks3-block"` and nothing else — light, never ink-dark. The four
CONTROLLESS reference sections (`#s-series`, `#s-rule`, `#s-line`,
`#s-classes`) are `rule` or `comparison` blocks, not instruments: rail stops
carrying no control, ticked by the hook, which is what MRB-249 licenses.
"""


import importlib
import pkgutil

# Instrument block types seen in authored C8 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the note above.
_INSTRUMENT_SEGMENTS = {
    "reaction-audit":   "check",
    "prediction-deck":  "check",
    "extraction-route": "check",
    "spec-bench":       "check",
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
    """The authored C9 lesson records, in slot order, normalised.

    C9 has four slots and four modules, so this unit produces no coming-soon
    page. A slot with no module here would render one honestly (§11 decision
    8) rather than 404.
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
