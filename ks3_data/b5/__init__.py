"""B5 — Reproduction, as one module per lesson.

Authored against Claude Design's approved reference screens in
`KS3 B5 lessons/` and under the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`). Shape follows `ks3_data/b4/`, which
follows `ks3_data/b3/`, `ks3_data/c1/`, `ks3_data/c2/`, `ks3_data/b2/` and
`ks3_data/b1/`: each module exports a single `LESSON` dict and this file
collects them.

Every student-facing string is lifted byte-identical from the approved page.
That rule is not a style preference anywhere, and on this unit it is a
safeguarding one — see the tone note below.

── BOTH statutory statements are SPLIT ──────────────────────────────────

Minted in `ks3_data/substatements.py` for this unit. Neither split needed
interpreting: both bullets print their own clause lists, and B5's eight
lessons are those lists in that order.

    REP.01a  male and female reproductive systems  `human-reproductive-systems`
    REP.01b  gametes and fertilisation             `gametes-and-fertilisation`
    REP.01c  the menstrual cycle, no hormones      `the-menstrual-cycle`
    REP.01d  gestation and birth                   `gestation-placenta-and-birth`
    REP.01e  maternal lifestyle via the placenta   `lifestyle-and-the-developing-foetus`
    REP.02a  flower structure and pollination      `flowers-and-pollination`
    REP.02b  fertilisation, seed and fruit         `fertilisation-seeds-and-fruit`
    REP.02c  seed dispersal                        `seed-dispersal`

── ⚑ A STATUTORY GAP IS OPEN IN THIS UNIT, AND IT IS RULED ──────────────

`KS3.B.REP.02` asks for a *"quantitative investigation of some dispersal
mechanisms"*. Design's `seed-dispersal` is a CLASSIFY lesson in which the
student measures nothing — eight specimens sorted by observable structure into
five methods, and no number taken anywhere on the page. Design's own NOTES-B5
flag 43 raises it. Ruled not to block this build (MRB-244); Design patches it
later.

`REP.02c` is deliberately minted at the bullet's FULL width, quantitative words
included, rather than narrowed to the classifying that is actually taught. A
narrowed clause would make the register read as fully covered and the gap would
vanish from every gate that reads it. It is meant to read covered-with-a-gap.

── ⚠️ TONE IS A GATE ON THIS UNIT, AND DESIGN'S TREATMENT STANDS ────────

Confirmed 16 Aug 2026 (MRB-244). Five of these eight lessons are human
reproduction and are read by 12- and 13-year-olds, some of whom are pregnant in
their families, some of whom are not living with the parents who conceived
them. Design's register is the ruled one and it is not to be softened,
sharpened, or annotated by an authoring pass:

- clinical and function-first; anatomical names plain, no euphemism
- no sexual detail beyond the statutory clause list
- no normative language about family structure; RSE and PSHE own that
- sex and gender are not conflated — "male system" and "female system" are
  properties of organs, never claims about a reader's identity
- third person throughout: "a person's cycle", never "your cycle"

`lifestyle-and-the-developing-foetus` carries the load-bearing case. Its whole
architecture is the placenta as a NEUTRAL surface governed by size and
solubility — which is what makes its second confrontation, the belief that
anything that goes wrong is the mother's fault, answerable at all. That
refutation and the lesson's legal line are safeguarding copy. They are lifted
whole or not at all.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as B1, B2, B3, B4, C1 and C2. §5.1.1's block
vocabulary is CLOSED and MRB-203's registry fails the build on a block type
with no registered component, so an instrument is authored inline in `core` —
where its position in the document is obvious — and `_normalise()` lifts it
into `activities[]`, leaving the right SHELL behind it.

⚠️ Measured from Design's own markup across all eight pages, not inherited:

    b5-01 #s-jobs     ks3-block ks3-dark ks3-practical  dark → practical
    b5-02 #s-compare  ks3-block ks3-dark ks3-practical  dark → practical
    b5-03 #s-dial     ks3-block ks3-dark ks3-practical  dark → practical
    b5-04 #s-cross    ks3-block ks3-dark ks3-practical  dark → practical
    b5-05 #s-cross    ks3-block ks3-dark ks3-practical  dark → practical
    b5-06 #s-parts    ks3-block ks3-dark ks3-practical  dark → practical
    b5-07 #s-becomes  ks3-block ks3-dark ks3-practical  dark → practical
    b5-08 #s-sort     ks3-block ks3-dark ks3-practical  dark → practical

⚠️ EVERY ONE OF THESE IS ON INK, and B4 proved the cost. `.ks3-dark p` is
(0,1,1) and beats a bare instrument class at (0,1,0), so every text rule in
every B5 instrument must be scoped to at least (0,2,0). This has now bitten
FIVE builds; on B4 it shipped a chain label at 1.21:1 — invisible — past a
green kinds gate, and only a browser found it. On eight ink-dark lessons it
would bite the whole unit.

── Figures are declared and NOT drawn ───────────────────────────────────

Design's legal lines name diagram slots across this unit that have no artwork —
more than any unit so far, because anatomy is where a labelled drawing does
work no prose can. They are declared at `status: "needed"` rather than dropped,
so `docs/ks3/diagram-manifest.md` counts them as sourcing tasks (§4.10, not a
build blocker). Nothing is invented to fill a slot.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B5 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
#
# ⚠️ Written in ONE pass, by the commander, deliberately. Eight authors work
# this unit in parallel and this dict is the one file they would all have had
# to edit; parallel writes to a single dict lose entries silently, and a lost
# entry here does not fail the build — it renders the instrument as an unlifted
# block and the page ships a bare list past a green kinds gate.
_INSTRUMENT_SEGMENTS = {
    "job-match":       "practical",
    "gamete-compare":  "practical",
    "cycle-dial":      "practical",
    "crossing-bench":  "practical",
    "crosses-panel":   "practical",
    "flower-jobs":     "practical",
    "what-it-becomes": "practical",
    "disperse-sort":   "practical",
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

        shell = {"type": segment, "id": act_id, "anchor": block.get("anchor")}
        # `ground` is a property of the BLOCK Design drew, not of the
        # instrument inside it, so it stays on the shell.
        if block.get("ground"):
            shell["ground"] = block["ground"]
        out.append(shell)

    lesson["core"] = out
    lesson["activities"] = acts
    return lesson


def lessons():
    """The authored B5 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. B5 is expected to reach eight of eight.
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
