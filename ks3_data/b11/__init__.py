"""B11 — Evolution, extinction and biodiversity. Four lessons, Biology.

One module per lesson, authored against Claude Design's approved pages in
`docs/ks3/design-reference/b11/`, her `NOTES-B11.md`, and the payload schema written
before dispatch at `docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md`, under the MRB-220
build contract.

    L1 variation-and-competitive-success           advantage-bench   #s-bench
    L2 natural-selection                           selection-runner  #s-bench
    L3 when-the-environment-changes-extinction      pressure-bench    #s-bench
    L4 biodiversity-and-gene-banks                 blight-bench      #s-bench

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

── THE FORWARD REFERENCE THIS UNIT RESOLVES ────────────────────────────────

`b9-03 disturbing-a-food-web` carries a `references` edge at
`{"unit": "B11", "lesson": "when-the-environment-changes-extinction"}`. L3
landing here resolves it, and nothing in b9-03 changes.

── FOUR RAIL STOPS, ALL FOUR TICK (MRB-249) ────────────────────────────────

Design draws four on all four pages; the third is the band — `s-three`,
`s-steps`, `s-risk`, `s-banks` — and is a mirror of the bench. Schema §8 left
this as "the commander's call" between a rail of three and a mirror; the call is
made and recorded there: **the mirror.** A rail of three is not available,
because MRB-205 binds and dropping a stop Design drew is not rendering what she
drew — and the panel is where each lesson's KEY FACT lives.

── THE PEPPERED MOTH IS TAUGHT PLAINLY, WITH NO HEDGE IN THE BODY ─────────

Ruled 16 Aug: the conclusion is sound, so teach it flatly and put the method
criticism in *Going further*. Verified in the delivered bytes (schema §10) —
every moth-bearing sentence outside *Going further* already states the science
without qualification. Do not add a hedge back.

── MISCONCEPTION IDS ARE PRE-ALLOCATED, INCLUDING SPARES ───────────────────

`EVOL-01`…`EVOL-08`, two per lesson, plus `EVOL-09`…`EVOL-12`, one named spare
each. `EVOL` is a new prefix. An unclaimed spare stays permanently unused and is
never re-pointed.

⚠️ `DRUG-06` is a SOCIAL-NORM belief, not a nature-of-science one. `NOTES-B11`
mis-cites it as a NOS misconception. That citation is not reintroduced anywhere
in this unit.
"""
import importlib
import pkgutil

# Instrument block types seen in authored B9 data, mapped to the §5.1.1 segment
# they render as — MEASURED from Design's own class attribute on all four pages
# (`ks3-block ks3-dark ks3-practical`), never inferred from the kind name.
# Contract §4 records that B1 got two of six wrong by inferring it.
#
# ⚠️ Written in ONE pass, by the engine pass, deliberately. Four authors work
# this unit in parallel and this dict is the one file they would all have had to
# edit; parallel writes to a single dict lose entries silently, and a lost entry
# here does not fail the build — it renders the instrument as an unlifted block
# and the page ships a bare list past a green kinds gate.
_INSTRUMENT_SEGMENTS = {
    "advantage-bench":   "practical",
    "selection-runner":  "practical",
    "pressure-bench":    "practical",
    "blight-bench":      "practical",
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
    """The authored B11 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for.
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
