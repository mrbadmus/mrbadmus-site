"""B9 — Ecosystems and interdependence. Six lessons, Biology.

One module per lesson, authored against Claude Design's approved pages in
`KS3 B9 lessons/`, her `NOTES-B9.md`, and the payload schema written before
dispatch at `docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md`, under the MRB-220 build
contract.

    L1 food-chains-and-food-webs        chain-ledger       #s-bench
    L2 predator-and-prey                cycle-runner       #s-bench
    L3 disturbing-a-food-web            remove-a-species   #s-bench
    L4 pollinators-and-food-security    supermarket-shelf  #s-bench
    L5 toxic-build-up-in-a-food-chain   bioaccumulation    #s-bench
    L6 sampling-an-ecosystem            quadrat-bench      #s-bench

**Slugs match `ks3_data/structure.py` character for character.** They are the
join for scheme-of-work rows, progress records and every `requires` edge, and
they are permanent (§8.4).

── B9 OWNS TROPHIC 10:1 FOR THE WHOLE KEY STAGE ────────────────────────────

The one-tenth-per-level figure is this unit's to teach, and `chain-ledger` is
where a student meets it as a measurement rather than as a stated fact. It
leaked forward into B7 earlier than its owner once already. No other unit
re-declares it, in the same way MRB-210 gives the microscope depth-of-field
table one home.

── FOUR RAIL STOPS, ALL FOUR TICK (MRB-249) ────────────────────────────────

Design draws four stops on all six pages. The third is the BAND section —
`s-roles`, `s-cycle`, `s-rules`, `s-who`, `s-two`, `s-rules` — which renders as
a static `ks3-rule` and carries none of the five DOM signals `doneByDom()`
reads, because Design completes it on the INSTRUMENT's predicate instead:

    if (id === 's-bench') return s.everTopped;
    if (id === 's-roles') return s.everTopped;

`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §4 originally told this unit to author
three stops and drop the band. That instruction is REVERSED — MRB-205 binds and
is not re-argued: Design draws, we render, and the page wins over the engine. A
band holding three fact cards and a KEY FACT is teaching, not a spacer.

So every lesson declares FOUR stops, and the band stop carries `mirrors` naming
the section it borrows its completion from:

    {"anchor": "s-roles", "short": "ROLES", "label": "Producer, consumer, …",
     "mirrors": "s-bench", "done_when": "chain_topped"},

`shared/ks3.js` resolves it in `wireRail`'s `paint()`, at rail level, which is
the level Design resolves it at. `ks3_parity.check_rail_matches_design` fails
the build if a page ships three, checked against `docs/ks3/rail-manifest.md`.

── `#s-think` and `#s-keynote` are on NO rail, and that is correct ─────────

Neither is a stop on Design's own page. `#s-keynote` is the KEY FACT band and
asks nothing; `#s-think` on these six pages is a `confrontation` — two quotes
and two bodies, static, with no commitment to make. Contract R1 makes `#s-think`
a stop only where it asks for a commitment and then reveals, which is B2, C1
and C2's shape, not B9's.
"""

import importlib
import pkgutil

# Instrument block types seen in authored B9 data, mapped to the §5.1.1 segment
# they render as — MEASURED from Design's own class attribute on all six pages
# (`ks3-block ks3-dark ks3-practical`), never inferred from the kind name.
# Contract §4 records that B1 got two of six wrong by inferring it.
#
# ⚠️ Written in ONE pass, by the engine pass, deliberately. Six authors work
# this unit in parallel and this dict is the one file they would all have had to
# edit; parallel writes to a single dict lose entries silently, and a lost entry
# here does not fail the build — it renders the instrument as an unlifted block
# and the page ships a bare list past a green kinds gate.
_INSTRUMENT_SEGMENTS = {
    "chain-ledger":      "practical",
    "cycle-runner":      "practical",
    "remove-a-species":  "practical",
    "supermarket-shelf": "practical",
    "bioaccumulation":   "practical",
    "quadrat-bench":     "practical",
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
    """The authored B9 lesson records, in slot order, normalised.

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
