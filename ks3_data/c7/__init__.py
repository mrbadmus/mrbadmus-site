"""C7 — Energy changes in reactions, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c7/` under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/c5/`
exactly, which follows `ks3_data/c4/` and `ks3_data/c3/`: each module exports a
single `LESSON` dict, and this file collects them.

Every student-facing string is lifted byte-identical from the approved page
via `node tools/extract_design_payload.js` for the top-level constants, and by
reading `lessonVals()` for the strings that live inside it — which is where
most of a lesson's words live, and which a lift of the top-level constants
alone silently loses. Where a string moves it is marked ⚑ in the lesson file
and reported to the commander.

── TWO STATUTORY BULLETS, FOUR LESSONS ──────────────────────────────────

`KS3.C.ENER.01` (energy changes on changes of state) is one bullet and one
lesson, so `c7-01` owns the parent whole.

`KS3.C.ENER.02` (exothermic and endothermic chemical reactions) is ONE bullet
claimed by THREE lessons, so its clauses are minted in
`ks3_data/substatements.py` on exactly the pattern C5 used for `CR.03a–e`:

    c7-02 exothermic-reactions           KS3.C.ENER.02a
    c7-03 endothermic-reactions          KS3.C.ENER.02b
    c7-04 measuring-a-temperature-change KS3.C.ENER.02c

Clause `c` is a commander's ruling and is not a phrase of its own bullet. The
full reasoning is written against `KS3.C.ENER.02` in that file; the short
version is that "(qualitative)" is the word in the bullet that makes the
measurement lesson statutory rather than off-spec, because a temperature
change is how a KS3 student decides which of the two a reaction is.

── THE HEATING CURVE'S DATA WAS REBUILT, AND THE RULING SAYS WHY ────────

⭐ **Ruled by the commander, 21 Aug 2026, on Design's NOTES-C7 §4 flag 2.**
Design's `CURVE` drew the melting plateau and the boiling plateau the SAME
length — four readings each — while her note at index 10 says "The boiling
step is longer than the melting step". The prose is right and the drawing is
wrong: the specific latent heat of fusion of water is 334 kJ/kg and of
vaporisation 2260 kJ/kg, so at constant power boiling takes about 6.8× the
energy of melting.

The standing build law is *where prose and instrument disagree, the instrument
is the measurement*. That law exists so nobody fudges DATA to rescue a
SENTENCE. Here the data is the error, so it is the data that changed:

    melting plateau   3 minutes flat at 0 °C     (Design's own, unchanged)
    boiling plateau   8 minutes flat at 100 °C   (2.67× as drawn)

and `c7-01` states IN WORDS that the curve is schematic and that boiling really
takes about seven times the energy of melting. Nothing on the page implies the
drawing is to scale. See `lesson_01_energy_and_changes_of_state.py` for the
point-by-point arithmetic.

⭐ **Ruled at the same time: the equal-slope claim is deleted, not reversed.**
Design's note at `CURVE` index 6 said the liquid climbs "at the same rate as it
climbed through the ice". That is false — ice has a specific heat capacity of
about 2.1 kJ/kg/K against liquid water's 4.18 — and it contradicts her own
drawn slopes. It is REMOVED rather than corrected, because the drawn slopes
cannot carry all four rate relationships truthfully on one tappable curve:
water spans 100 °C and ice only 20 °C, so any usable step count makes water's
drawn slope the steeper one. The teachable content of a heating curve is the
PLATEAUS, and no slope comparison is made anywhere in the lesson.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as C3's, C4's and C5's, and the same mechanism. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component. C7's instruments are interactive tasks with a
demand, a commitment and a reveal, which is what §5.5's activity record is for.
Each lesson authors its instrument inline in `core`, where its position in the
document is obvious, and `_normalise()` lifts it into `activities[]` leaving
the right SHELL behind it.

⚠️ THE SEGMENT IS A MEASUREMENT, AND IN THIS UNIT IT IS UNIFORM. Measured from
Design's own markup, every anchored instrument section in all four lessons
carries `class="ks3-block"` and nothing else:

    c7-01 #s-curve    ks3-block   light  → check
    c7-01 #s-uses     ks3-block   light  → check
    c7-02 #s-bench    ks3-block   light  → check
    c7-02 #s-uses     ks3-block   light  → check
    c7-03 #s-compare  ks3-block   light  → check
    c7-03 #s-uses     ks3-block   light  → check
    c7-04 #s-plan     ks3-block   light  → check
    c7-04 #s-bench    ks3-block   light  → check

There is no ink-dark practical block anywhere in C7, exactly as there is none
in C3, C4 or C5. The only dark sections are the hook and the closing key note,
both of which the engine emits itself. The ink panels INSIDE `#s-bench` on
c7-02 and c7-04 are readouts nested in a light block, which is a different
thing and is styled as one.

── SIX FAMILIES, NOT FIVE, AND THE SIXTH IS PLACED THREE TIMES ──────────

Design draws a "Three judgements" block on c7-01, c7-02 AND c7-03 — three
cards, one commitment each, an answer paragraph on the card that opens. It is
the same instrument three times, so it is ONE family (`energy-uses`) placed
three times, not three families that happen to look alike.

That is the opposite call from the one §6 warns about, and deliberately: §6's
warning is against an identical block LINEUP arriving as a default. Here the
repetition is Design's own and it is load-bearing — the three judgement blocks
are the same move (take the rule off the bench and use it on something real)
made three lessons running, and giving each its own family would be three
copies of one renderer with three chances to drift.

The unit's four FLAGSHIPS are all different, which is where §6's warning
actually bites: a minute-by-minute stepper, a five-beaker predict-then-run
bench, an eight-item sorter, and a plan critique followed by a three-dial rig
builder. A later pass that harmonises those four would be undoing what makes
them four lessons.

⚠️ `rig-plan-critique`, NOT `plan-critique`. `ks3_art/c3.py` already registers
`plan-critique` for c3-07, with the shell class `ks3-critique-block`. C7's is
the same SHAPE with a different plan in it, and Design's NOTES-C7 §3 says so —
but a family name is an owner, not a description, and a lane may not edit
another unit's module. So C7 registers its own, and the two live side by side.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C7 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "heating-curve":     "check",
    "temp-bench":        "check",
    "energy-sorter":     "check",
    "energy-uses":       "check",
    "rig-plan-critique": "check",
    "rig-builder":       "check",
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
    """The authored C7 lesson records, in slot order, normalised.

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
