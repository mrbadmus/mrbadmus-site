"""B6 — Health and drugs, as one module per lesson.

Authored against Claude Design's approved reference screens in
`KS3 B6 lessons/` and under the MRB-220 build contract. Shape follows
`ks3_data/b4/`: each module exports a single `LESSON` dict and this file
collects them.

Every student-facing string is lifted byte-identical from the approved page.
On this unit that is a safeguarding rule as much as an accuracy one.

── `KS3.B.HLTH.01` is SPLIT three ways ──────────────────────────────────

Minted in `ks3_data/substatements.py` for this unit. The bullet reads *"the
effects of recreational drugs (including substance misuse) on behaviour, health
and life processes"* — one statement across three lessons, which the register's
own coverage table flagged as `B6 | 1 | 3 | 0.33 ⚠️`.

    HLTH.01a  what a drug is, and how one acts once in the blood   `what-drugs-do-to-the-body`
    HLTH.01b  the effects of alcohol and of tobacco smoke          `alcohol-and-smoking`
    HLTH.01c  substance misuse, and judging a claim as evidence    `substance-misuse-and-decisions`

⚑ **This split is a CURRICULUM-MAPPING CALL and the weakest-provenance mint in
`substatements.py`** — flagged for Mide there and here. The bullet names
"recreational drugs" and "substance misuse" but does not itself name alcohol or
tobacco; clause `b` is justified by them being the two the statement's own words
bite hardest on at this age, not by the document naming them. The alternative is
a two-way split with b6-01 and b6-02 sharing clause `a`, which §4.4 rule 3
forbids.

── ⚠️ TONE IS A GATE ON EVERY PAGE OF THIS UNIT ─────────────────────────

Design's register is ruled and consistent with b3-04, b4-04 and B5: clinical,
no scare copy, no euphemism, and **no doses, thresholds or methods anywhere**.
A student reading this unit may be living with someone else's addiction, or
their own. The tone is not decoration on the science; it is what makes the
science readable by the student who most needs it.

Two things are settled and must not be re-opened by an authoring pass:

- **Flag 9, the vape paragraph, is APPROVED BY MIDE and ships exactly as
  written.** No tar, no carbon monoxide, the same or stronger nicotine
  dependence, very likely less harmful than cigarettes, **not known to be
  safe**, nothing to gain for a non-smoker, illegal under 18. Every clause in
  that list is load-bearing and the paragraph is balanced as a whole; trimming
  any one of them tips it into either advertisement or scare copy.
- **Flag 4, paracetamol and the liver** — a large dose damages cells, the damage
  is permanent, and **the person may feel fine for a day or two**. That last
  clause is deliberately included at KS3 because it is the one that saves a
  life. It is not softened.

Each lesson also carries a `ks3-layer ks3-support` referral block. Design points
at "the services listed in your school's PSHE materials" rather than naming a
helpline, because a named helpline goes stale and naming one is a safeguarding
decision rather than an authoring one. Carry it as drawn; Mide may override.

── The `DRUG` misconception family opens here ───────────────────────────

Six entries, two per lesson, minted `DRUG-01` … `DRUG-06`. The ranges are
PRE-ALLOCATED per lesson in each author's brief and in the register, because
B4's five parallel authors collided twice on `BREATH` ids and the fix — open the
family before the lessons are written — had been recorded after B3 and never
applied. `DRUG-01` is cited by all three lessons and confronted in b6-01; the
register's reappears note carries that rather than minting three near-duplicates.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Measured from Design's own markup on all three pages, not inherited:

    b6-01 #s-dose    ks3-block ks3-dark ks3-practical  dark → practical
    b6-02 #s-clock   ks3-block ks3-dark ks3-practical  dark → practical
    b6-03 #s-claims  ks3-block ks3-dark ks3-practical  dark → practical

⚠️ ALL THREE ARE ON INK. `.ks3-dark p` is (0,1,1) and beats a bare instrument
class at (0,1,0). This has now bitten five builds; on B4 it shipped a chain
label at 1.21:1 — invisible — past a green build, a green kinds gate and a green
key audit, and only a browser caught it. Scope every instrument text rule to at
least (0,2,0), and re-measure the colour you chose on the ground it lands on:
B4 also proved the cascade bug can MASK a wrong token, so fixing specificity
alone can turn a passing element into a failing one.

── No figures ──────────────────────────────────────────────────────────

NOTES-B6 flag 14: this unit names no diagram slots anywhere and draws none. Its
visuals are the three instruments. That is measured, not an omission — nothing
is declared and nothing is invented.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B6 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the table above.
#
# ⚠️ Written in ONE pass, by the commander. Three authors work this unit in
# parallel and this dict is the one file they would all have had to edit;
# parallel writes to a single dict lose entries silently, and a lost entry does
# not fail the build — it renders the instrument as an unlifted block.
_INSTRUMENT_SEGMENTS = {
    "route-tracer":    "practical",
    "clearance-clock": "practical",
    "claim-check":     "practical",
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
    """The authored B6 lesson records, in slot order, normalised.

    A slot with no module here renders an honest coming-soon page — that is the
    structure-first guarantee (§11 decision 8) and not a gap to be apologised
    for. B6 is expected to reach three of three.
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
