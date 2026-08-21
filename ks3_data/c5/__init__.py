"""C5 — Types of reaction, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c5/` under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/c4/`
exactly, which follows `ks3_data/c3/`: each module exports a single `LESSON`
dict, and this file collects them.

Every student-facing string is lifted byte-identical from the approved page
via `node tools/extract_design_payload.js` for the top-level constants, and by
reading `lessonVals()` for the strings that live inside it — which is where
most of a lesson's words live, and which a lift of the top-level constants
alone silently loses.

── ONE STATUTORY BULLET, FIVE LESSONS ───────────────────────────────────

`KS3.C.CR.03` names four reaction types in a single bullet and this unit gives
each one a lesson, exactly as C3 does with `PIS.04`'s four techniques. The
fifth lesson exists because NAMING four types is not the same as TELLING THEM
APART, which is what an exam asks and what §5.8 rung 2 is for.

⚠️ FOUR CONSECUTIVE `PROCESS` LESSONS IS A RISK, NOT AN ACCIDENT. §6 warns
that identical block lineups should be a coincidence of need and never a
default, and four PROCESS lessons in a row is precisely the shape that
produces one. Design's answer was to give each a DIFFERENT flagship — a
parameter bench, a staged run with a cooling gate, a four-tube controlled
investigation, and a 4x4 grid — and that difference is load-bearing. A future
pass that "harmonises" these four into one repeated instrument would be
undoing the thing that makes them four lessons.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as C3's and C4's, and the same mechanism. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component. C5's ten instruments are interactive tasks with
a demand, a commitment and a reveal, which is what §5.5's activity record is
for. Each lesson authors its instrument inline in `core`, where its position
in the document is obvious, and `_normalise()` lifts it into `activities[]`
leaving the right SHELL behind it.

⚠️ THE SEGMENT IS A MEASUREMENT, AND IN THIS UNIT IT IS UNIFORM. Measured from
Design's own markup, every anchored instrument section in all five lessons
carries `class="ks3-block"` and nothing else:

    c5-01 #s-burner   ks3-block   light  → check
    c5-01 #s-fuels    ks3-block   light  → check
    c5-02 #s-tube     ks3-block   light  → check
    c5-02 #s-sort     ks3-block   light  → check
    c5-03 #s-rust     ks3-block   light  → check
    c5-03 #s-stop     ks3-block   light  → check
    c5-04 #s-grid     ks3-block   light  → check
    c5-04 #s-uses     ks3-block   light  → check
    c5-05 #s-sort     ks3-block   light  → check
    c5-05 #s-rule     ks3-block   light  → check

There is no ink-dark practical block anywhere in C5, exactly as there is none
in C3 or C4. The only dark sections are the hook and the closing key note,
both of which the engine emits itself.

── `#s-series` IS NOT IN THIS TABLE, AND THAT IS THE POINT ──────────────

c5-04 draws an eleventh light `ks3-block`, `#s-series`, carrying the full KS3
reactivity series. It is NOT an instrument, has NO family here, and takes NO
rail stop — it is absent from Design's own `RAIL`, and NOTES-C5 §7 gives the
reason: the rail ticks ACTIVITIES only, so a stop that could never tick is not
added. It is authored from the closed block vocabulary like any other
reference section.

⭐ Ruled by Mide, 18 Aug 2026 (NOTES-C5 §7), overriding Design's original
discovery framing: the series is shown UP FRONT, before the grid, rather than
withheld until twelve cells have been run. The grid's payoff paragraph changed
with it — it now says the sixteen tubes REPRODUCED the part of the published
list the bench can reach, which is the honest version of the same point and
arguably the better one: the student checks a published order against their own
data rather than being handed a conclusion.

⚠️ The cost of that ruling is recorded here because it is easy to lose. A
student who consults the list can complete sixteen predictions without
reasoning from evidence at all, so `c5-04`'s rung 4 — design an investigation
to place an unknown metal — is now the ONLY place the derivation is actually
assessed. That rung is load-bearing in a way it was not when the series was
withheld.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C5 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "burner-bench":     "check",
    "fuel-cards":       "check",
    "tube-run":         "check",
    "decomp-sort":      "check",
    "control-tubes":    "check",
    "rust-stop":        "check",
    "reactivity-grid":  "check",
    "reactivity-use":   "check",
    "type-sorter":      "check",
    "rule-write":       "check",
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
    """The authored C5 lesson records, in slot order, normalised.

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
