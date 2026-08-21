"""C6 — Acids and alkalis, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c6/` under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). The shape follows `ks3_data/c5/`
exactly, which follows `ks3_data/c4/` and `ks3_data/c3/`: each module exports a
single `LESSON` dict, and this file collects them.

Every student-facing string is lifted from the approved page — by
`node tools/extract_design_payload.js` for the top-level constants, and by
READING `lessonVals()` for the rest, which is where most of a lesson's words
live and which a lift of the top-level constants alone silently loses.

── SIX LESSONS, SEVEN DRAWINGS, AND THERE IS NO `lesson_05_` ────────────

⚠️ **THE MAPPING IS NOT 1:1 AND THE GAP IS DELIBERATE. Do not "fix" it by
adding a fifth module.**

`ks3_data/structure.py`'s fifth C6 slot is `acid-plus-alkali` ("Acid + alkali:
making a salt", PROCESS). Design drew `c6-05-acids-and-carbonates` there
instead and flagged the divergence herself in NOTES-C6 §2 with "Ruling
wanted": her case is that acid + carbonate is the third of the three acid
reaction families and carries the limewater test, and her case against is that
it is not in §7 and owns no statutory statement.

**The commander ruled: build the six slots where Design's drawing and
`structure.py` agree, and author nothing for the seventh.** The slug is
permanent (§8.4), `structure.py` is not edited by a unit module and was not
edited by this one, and the unauthored slot renders an honest coming-soon page
— the structure-first guarantee (§11 decision 8), which is a supported state
rather than a gap to be apologised for.

So the modules here are numbered 01, 02, 03, 04, 06, 07 against the slot
positions in `structure.py`, and the missing 05 is a record of the ruling
rather than an oversight. `lessons()` globs, so the gap costs nothing.

── THE TITLE AND THE SLUG COME FROM `structure.py`, THE WORDS FROM DESIGN ──

Three of Design's page titles differ from the skeleton's, and the skeleton
wins on both slug and title because the slug is permanent and the title is the
thing every index, breadcrumb and rail link already prints:

    c6-02  "Indicators and the pH scale"  →  `the-ph-scale-and-indicators`
                                             "The pH scale and indicators"
    c6-04  "Acids and metals"             →  `acid-plus-metal`
                                             "Acid + metal"
    c6-06  "Making a salt"                →  `making-a-pure-dry-salt`
                                             "Making a pure dry salt"

Nothing else moves. The teaching content, the instruments and the words are
Design's.

⚠️ **`docs/ks3/rail-manifest.md` KEYS ON THE BUILT SLUG AND DERIVES IT FROM
DESIGN'S FILENAME**, so those three lessons have no manifest row under the
name they will actually build as, and `ks3_parity.check_rail_matches_design`
fails a rail-bearing page with no row. That is a real gate finding and it is
reported to the commander rather than worked around here; the fix is a rename
map in `ks3_rail_manifest._slug` plus the three rows, and it is an engine
change, not a content one.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument as C3's, C4's and C5's, and the same mechanism. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component. C6's thirteen instrument placements are
interactive tasks with a demand, a commitment and a reveal, which is what
§5.5's activity record is for. Each lesson authors its instrument inline in
`core`, where its position in the document is obvious, and `_normalise()`
lifts it into `activities[]` leaving the right SHELL behind it.

⚠️ THE SEGMENT IS A MEASUREMENT, AND IN THIS UNIT IT IS UNIFORM. Measured from
Design's own markup, every anchored instrument section in all six lessons
carries `class="ks3-block"` and nothing else:

    c6-01 #s-bench    ks3-block  light  → check
    c6-01 #s-hazard   ks3-block  light  → check
    c6-02 #s-bench    ks3-block  light  → check
    c6-02 #s-choose   ks3-block  light  → check
    c6-03 #s-titrate  ks3-block  light  → check
    c6-03 #s-uses     ks3-block  light  → check
    c6-04 #s-bench    ks3-block  light  → check
    c6-04 #s-test     ks3-block  light  → check
    c6-06 #s-name     ks3-block  light  → check
    c6-06 #s-method   ks3-block  light  → check
    c6-07 #s-bench    ks3-block  light  → check
    c6-07 #s-uses     ks3-block  light  → check

There is no ink-dark practical block anywhere in C6, exactly as there is none
in C3, C4 or C5. The only dark sections are the hook and the closing key note,
both of which the engine emits itself.

── `#s-scale` IS NOT IN THAT TABLE, BECAUSE IT IS A FIGURE ──────────────

c6-02 draws a thirteenth section, `#s-scale`, carrying the fifteen-cell pH
chart. It is NOT an instrument — it has no commitment and takes no decision —
and Design's own `DONE('s-scale')` returns `s.hookChoice !== null`, the SAME
expression as `s-hook`. That is a MIRROR in MRB-249's sense, it is on her rail,
and it is kept: the stop is authored with `mirrors: "s-hook"` and the rail
resolves it against the hook's state.

It is authored as a `figure` block with an `anchor`, which C3 (MRB-272) made
legal, and drawn by `ks3_art.c6._ph_strip`. Drawn rather than built out of
fifteen flex divs on purpose — see that function's docstring for the
containment argument, which is the C5 defect that widened five pages by 140px
at 390px.
"""

import importlib
import pkgutil

# Instrument block types seen in authored C6 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
_INSTRUMENT_SEGMENTS = {
    "bottle-sorter":    "check",
    "acid-judgements":  "check",
    "ph-bench":         "check",
    "titration-dial":   "check",
    "acid-metal-grid":  "check",
    "salt-namer":       "check",
    "method-order":     "check",
    "catalyst-bench":   "check",
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
    """The authored C6 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is
    the structure-first guarantee (§11 decision 8) and not a gap to be
    apologised for. `acid-plus-alkali` is that slot, on purpose; see the module
    docstring.
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
