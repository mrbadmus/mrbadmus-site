"""C8 — The periodic table, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c8/` and her author's notes `NOTES-C8.md`. The shape
follows `ks3_data/c7/` exactly, which follows `ks3_data/c5/` and `c4/` and
`c3/`: each module exports a single `LESSON` dict, and this file collects them.

═══════════════════════════════════════════════════════════════════════════
SEVEN SLOTS, SEVEN AUTHORED — AND `KS3.C.PT.06` IS CLOSED
═══════════════════════════════════════════════════════════════════════════

`ks3_data/structure.py` carries SEVEN C8 slots since MRB-281, and all seven are
authored here. The seventh — `metal-and-non-metal-oxides`, which owns
`KS3.C.PT.06` — landed on **23 August 2026**.

⊕ **`KS3.C.PT.06` WAS THE ONLY UNCOVERED STATUTORY STATEMENT IN C1–C8, AND IT
IS NOW COVERED.** This block used to record that hole in the curriculum and say
"it is not fixed by this run". It is fixed. The statement is owned solely by
`lesson_07_metal_and_non_metal_oxides.py`; every statutory statement in C1–C8
now has exactly one owner. The unit ships no coming-soon page.

⚠️ c8-06 still **touches** `PT.06` in one prediction card and that is still
correct and still ungated. Touching is not owning: `covers` is what the register
counts, and nothing in c8-06's record changed when this one arrived.

⊖ **c8-06 NO LONGER LINKS FORWARD TO IT** (MRB-281, R2). Design's page carried
a sentence in the lesson body pointing at `c8-07-metal-and-non-metal-oxides`,
which did not exist at the time. MRB-257 ruled that a placeholder is the build's
backlog printed to a twelve-year-old, and a sentence pointing at a lesson that
is not there is exactly that. The unit index already carries unbuilt slots as
coming-soon rows; that convention needs no help from prose and it resolves on
its own the day c8-07 ships. **That day was 23 August 2026, and it resolved
exactly as predicted — the generated prev/next now reaches a real lesson and no
prose had to be added or removed to make it.** The R2 decision stands as
written; do not "restore" a forward-link sentence now that the target exists.
c8-01's BACK link to `c7-04` is untouched — that page exists.

═══════════════════════════════════════════════════════════════════════════
SIX STATUTORY BULLETS, SEVEN LESSONS, AND TWO BULLETS SPLIT
═══════════════════════════════════════════════════════════════════════════

Under §4.4 rule 3 every statement is owned by exactly one lesson. Design's
`NOTES-C8.md` §1 assigns `PT.03` to TWO lessons and `PT.04` to THREE, so both
are minted at clause grain in `ks3_data/substatements.py` — the CR.03a–e and
ENER.02a–c pattern:

    c8-01 metals-and-non-metals      PT.01, PT.03b, PT.05
    c8-02 mendeleev                  PT.02
    c8-03 groups-and-periods         PT.03a
    c8-04 group-1-the-alkali-metals  PT.04a
    c8-05 group-7-the-halogens       PT.04b
    c8-06 group-0-and-why-groups...  PT.04c
    c8-07 metal-and-non-metal-oxides PT.06

⚖️ **Minting is about OWNERSHIP, not about what a lesson may TEACH.** Those
are different fields and the distinction is what the last run got backwards.
Repetition across these lessons is CORRECT — group number and outer electrons
are said on three pages, and the trend mechanism on three — and repetition is
carried by `touches`, which is ungated, not by a second `covers` entry, which
`validate()` refuses. A lesson may touch a statement any number of times.

═══════════════════════════════════════════════════════════════════════════
Instrument blocks are ACTIVITIES, not block types
═══════════════════════════════════════════════════════════════════════════

Same argument as C3's, C4's, C5's and C7's, and the same mechanism. §5.1.1's
block vocabulary is CLOSED and MRB-203's registry fails the build on a block
type with no registered component. C8's instruments are interactive tasks with
a demand, a commitment and a reveal, which is what §5.5's activity record is
for. Each lesson authors its instrument inline in `core`, where its position in
the document is obvious, and `_normalise()` lifts it into `activities[]`
leaving the right SHELL behind it.

⚠️ THE SEGMENT IS A MEASUREMENT, AND IN THIS UNIT IT IS UNIFORM. Measured from
Design's own markup, every anchored instrument section in all seven lessons
carries `class="ks3-block"` and nothing else — light, never ink-dark. The only
dark sections are the hook and the closing key note, both of which the engine
emits itself. There is no ink-dark practical block anywhere in C8, exactly as
there is none in C3, C4, C5 or C7.

⊕ c8-07's `#s-bench` is the same light `ks3-block`. It does draw ONE ink-dark
PANEL inside itself — the side-by-side comparison, `background: var(--ks3-ink)`
in Design's own markup — which is the same shape as the closing panels every
other C8 instrument carries and does not make the section dark. It is also the
only place `--ks3-data` is spent in the whole unit, because it is the only
on-ink surface C8 has.

The two CONTROLLESS reference sections — c8-01 `#s-table` (the two property
lists) and c8-05 `#s-family` (the four halogens) — are `comparison` blocks, not
instruments. They are rail stops that carry no control, ticked by the hook's
commitment, which is what MRB-249 licenses.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C8 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the note above.
_INSTRUMENT_SEGMENTS = {
    "property-sorter": "check",
    "gap-filler":      "check",
    "predict-cards":   "check",
    "table-reader":    "check",
    "water-trough":    "check",
    "halogen-grid":    "check",
    "shell-strip":     "check",
    "oxide-bench":     "check",
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
    """The authored C8 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is
    the structure-first guarantee (§11 decision 8) and not a gap to be
    apologised for. ⊕ As of 23 August 2026 C8 has no such slot: all seven are
    authored, and `metal-and-non-metal-oxides` — which was that slot — is
    `lesson_07_metal_and_non_metal_oxides.py`.
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
