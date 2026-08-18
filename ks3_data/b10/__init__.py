"""B10 — Inheritance and DNA. Five lessons, Biology.

One module per lesson, authored against Claude Design's approved pages in
`docs/ks3/design-reference/b10/`, her `NOTES-B10.md`, and the payload schema written
before dispatch at `docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md`, under the MRB-220
build contract.

    L1 variation-continuous-and-discontinuous  variation-plotter  #s-bench
    L2 chromosomes-genes-and-dna               zoom-bench         #s-bench
    L3 how-we-worked-out-dna                   model-builder      #s-bench
    L4 passing-it-on-heredity                  pea-cross          #s-bench
    L5 what-makes-a-species                    species-cases      #s-bench

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

> ⊗ **A title divergence recorded here on 18 Aug 2026 DOES NOT EXIST, and this
> is the correction.** This paragraph claimed `structure.py` names L3 *"How we
> worked out DNA's structure"* while Design's page titles it *"How we worked out
> DNA"*. Measured: the page's `<title>` and its `<h1>` both read **How we worked
> out DNA's structure**, character for character identical to `structure.py`.
> There is nothing to reconcile.
>
> The claim came from `docs/ks3/design-reference/b10/README.txt`, whose contents table
> lists the lesson as *"How we worked out DNA"* — a short LABEL in a fixed-width
> column, not a title. Reading a delivery's index as if it were the artefact is
> how a divergence gets invented, and it was nearly handed to an authoring pass
> as something to reconcile. Kept in place and marked rather than deleted,
> because the next reader of that README will make the same mistake.
>
> Found by the b10-02 authoring pass, which measured the page rather than
> trusting this file. The slug is `how-we-worked-out-dna` in both, and slugs are
> the thing that may not differ (§8.4).

── THE FORWARD REFERENCE THIS UNIT RESOLVES ────────────────────────────────

`b9-06 sampling-an-ecosystem` carries a `references` edge at
`{"unit": "B10", "lesson": "variation-continuous-and-discontinuous"}`, authored
as a reference rather than a `requires` precisely so that it could ship before
this unit existed: an unknown `requires` target fails the build, while an unbuilt
reference renders as "… (Inheritance and DNA — coming soon)". L1 landing here
resolves it, and nothing in b9-06 changes.

── FOUR RAIL STOPS, ALL FOUR TICK (MRB-249) ────────────────────────────────

Design draws four stops on all five pages. The third is the BAND section —
`s-two`, `s-model`, `s-who`, `s-steps`, `s-test` — which renders as a static
`ks3-rule` and carries none of the DOM signals `doneByDom()` reads, because
Design completes it on the INSTRUMENT's predicate instead, in a rail-level
`isDone()`.

`docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §8 originally told this unit to author
three stops and drop the band. That instruction is REVERSED and the section now
says so at the top: MRB-205 binds and is not re-argued — Design draws, we
render, and the page wins over the engine. The band holds this lesson's KEY
FACT; it is teaching, not a spacer.

So every lesson declares FOUR stops, and the band stop carries `mirrors` naming
the section it borrows its completion from. `shared/ks3.js` resolves it in
`wireRail`'s `paint()`, at rail level, which is the level Design resolves it at.
`ks3_parity.check_rail_matches_design` fails the build if a page ships three,
checked against `docs/ks3/rail-manifest.md`.

── `#s-think` is a `confrontation` on all five pages, and on NO rail ───────

Measured on all five: `#s-think` holds two `.ks3-mis-quote` runs with a rule
between them, and no options, no commit, no gated reveal, no `sc-if`. Contract
R1 makes `#s-think` a rail stop only where it asks for a commitment and then
reveals, which is B2, C1 and C2's shape, not this one's. None of the five rails
lists `s-think`, which is the independent confirmation.

── "Data from one year group" IS ALLOWED. Ruled 18 Aug 2026 ────────────────

b10-01's bench prompt opens *"Data from one year group."* — the only occurrence
of the word "year" anywhere in this unit, and the authoring pass was right to
raise it rather than assume.

**It stays.** The rule it looks like it breaks is *sequence is data*: a lesson
page may not encode where it sits in a scheme of work, which is why we write
"a student your age" and never "a Year 7". That rule exists so a school can
teach these lessons in its own order without the page contradicting the
timetable. This sentence does none of that. It names no year, pins the lesson
to no point in any sequence, and describes the **sample** rather than the
lesson: sixty people of roughly one age, which is exactly why the height data
has the spread it has and is doing real teaching work in a lesson about
variation. Cut it and the student loses the reason the numbers look like that.

The test to apply, and it is a discernment test rather than a word list — the
same shape as §8.10's: does the sentence tell a student WHERE THIS LESSON SITS,
or does it tell them something about the science in front of them? "Year 9
should already know this" is the first. "Data from one year group" is the
second.

⚠️ **Nothing in `verify_ks3.py` gates this rule.** Grepped: there is no
assertion anywhere that a lesson page's bytes are free of a year or a half-term.
It has been contract law since MRB-220 and has been kept by authors reading it,
which is exactly the arrangement that holds until the first pass that has not
read it. Raised for the gate to be built; when it is, it must pass the sentence
above and fail "Year 9", which is the discernment the test names.

── MISCONCEPTION IDS ARE PRE-ALLOCATED, INCLUDING SPARES ───────────────────

`GENE-01`…`GENE-10`, two per lesson, plus one named spare per lesson,
`GENE-11`…`GENE-15`. The range is fixed in schema §12 BEFORE any author starts,
because five authors working five files at once cannot see each other: an author
who mints "the next free id" mints the same one as everybody else. An unclaimed
spare stays permanently unused, like `DRUG-07`. Ids are permanent and a spare is
never re-pointed.

⚠️ `GENE-06` is a nature-of-science belief, and a `NOS` family now exists —
`NOS-04` was minted by b9-06. Whether `GENE-06` should be a `NOS` id is a
decision that must be taken before publish, because ids are permanent. Flagged,
not taken here.
"""
import importlib
import pkgutil

# Instrument block types seen in authored B9 data, mapped to the §5.1.1 segment
# they render as — MEASURED from Design's own class attribute on all five pages
# (`ks3-block ks3-dark ks3-practical`), never inferred from the kind name.
# Contract §4 records that B1 got two of six wrong by inferring it.
#
# ⚠️ Written in ONE pass, by the engine pass, deliberately. Five authors work
# this unit in parallel and this dict is the one file they would all have had to
# edit; parallel writes to a single dict lose entries silently, and a lost entry
# here does not fail the build — it renders the instrument as an unlifted block
# and the page ships a bare list past a green kinds gate.
_INSTRUMENT_SEGMENTS = {
    "variation-plotter": "practical",
    "zoom-bench":        "practical",
    "model-builder":     "practical",
    "pea-cross":         "practical",
    "species-cases":     "practical",
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
    """The authored B10 lesson records, in slot order, normalised.

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
