"""C10 — The Earth and its atmosphere, as one module per lesson.

Authored against Claude Design's approved reference screens in
`docs/ks3/design-reference/c10/`. The shape follows `ks3_data/c9/` exactly.

SIX SLOTS. `structure.py` gives C10 six, in this order, and every one of them
is routable from day one — an unauthored slot renders an honest coming-soon
page (§11 decision 8) rather than 404:

    c10-01 inside-the-earth                     KS3.C.EA.01 + KS3.C.EA.02
    c10-02 three-ways-to-make-a-rock            KS3.C.EA.03a
    c10-03 the-rock-cycle                       KS3.C.EA.03b
    c10-04 a-planet-with-limits                 KS3.C.EA.04
    c10-05 whats-in-the-air                     KS3.C.EA.05
    c10-06 carbon-dioxide-humans-and-climate    KS3.C.EA.06

── ⚖️ RULED · `KS3.C.EA.03` IS CLAUSE-SPLIT (§11.11) ────────────────────

The bullet reads "**the rock cycle and the formation of igneous, sedimentary
and metamorphic rocks**". It carries two ideas that every scheme of work
teaches a week apart, and `structure.py` already reserved two slots for them:
c10-02 makes the three rock types and c10-03 runs the cycle. Under §4.4 rule 3
a statement is owned by exactly one lesson and under §10.2 every lesson has a
non-empty `covers`, so those two rules cannot both hold for c10-02 and c10-03
unless the bullet is split at the grain the lessons are written at. It is:

    KS3.C.EA.03a  the formation of igneous, sedimentary and metamorphic
                  rocks                                          → c10-02
    KS3.C.EA.03b  the rock cycle                                  → c10-03

⚠️ **The mint is made by the lesson that needs it, not here.** Sub-IDs are
permanent once referenced (`ks3_data/substatements.py` rule 4) and are minted
LAZILY, per unit, at authoring time (rule 3). c10-02 and c10-03 are not
authored yet, so `SUBSTATEMENTS` carries no `KS3.C.EA.03` row: writing one now
would reserve two permanent ids against nothing, which is the failure mode
`MATL-04/07/10/14` are recorded in the misconception register for avoiding.
**The ruling is written down here; the rows land with the lessons.**

The other five statements are owned whole and no other sub-ID is needed.
`KS3.C.EA.01` (composition) and `KS3.C.EA.02` (structure) are both c10-01's:
one lesson, two statements, which §4.4 rule 3 permits — what it forbids is one
statement in two lessons.

── ⊖ `c10-07-the-carbon-cycle` IS NOT BUILT, AND MUST NOT BE ────────────

Design's delivery contains a SEVENTH page, `c10-07-the-carbon-cycle.dc.html`,
drawing a lesson on carbon stores and flows with its own `#s-flows` and
`#s-store` instruments. It has **no slot in `structure.py` and no statutory
statement behind it** — the 2014 document's Earth-and-atmosphere strand names
six bullets and the carbon cycle is not one of them.

**THE SKELETON WINS.** `structure.py` declares all 33 units and all 183 lesson
slots, and §8.4 makes a slot's slug and position permanent. Adding a seventh
lesson here would renumber nothing (it would append), but it would put an
unstatutory page into a unit whose six pages are each anchored on a bullet,
and it would make `structure.py` a second-hand copy of whatever the delivery
happens to contain. So the file is IGNORED: not built, not registered, not
added to `structure.py`. It is recorded here rather than deleted, because an
undocumented orphan is indistinguishable from an oversight.

⚠️ It IS in `docs/ks3/rail-manifest.md` — the manifest is regenerated from the
whole delivery folder and records what Design drew, which is the right
behaviour for a reference. A manifest row with no built page is a drawing
nobody used; a built page with no manifest row is the defect the gate exists
for. Only the second is a failure.

── FIVE RAIL STOPS PER LESSON — AND SIX FOR c10-04 ──────────────────────

Measured off Design's own `RAIL` constant on each delivered page, which is
what `ks3_rail_manifest.py` reads and what `ks3_parity.check_rail_matches_
design` checks the built page against:

    c10-01  s-hook s-layers   s-evidence  s-think s-ladder          5
    c10-02  s-hook s-table    s-bench     s-think s-ladder          5   (*)
    c10-03  s-hook s-journey  s-processes s-think s-ladder          5
    c10-04  s-hook s-loop     s-stock     s-words s-think s-ladder  6
    c10-05  s-hook s-mix      s-history   s-think s-ladder          5
    c10-06  s-hook s-how      s-evidence  s-think s-ladder          5

(*) c10-02's `#s-table` is a CONTROLLESS REFERENCE STOP — its done-expression
is `s.hookChoice !== null`, mirroring the hook, which is exactly what MRB-249
licenses and what C9's four reference stops already do. It is a `rule` or
`comparison` block with `mirrors: s-hook` on its rail entry, and it is NOT an
instrument. Do not mint a family for it.

**c10-04 is the only page in the key stage whose vocabulary block takes a rail
stop.** `#s-words` is `class="ks3-block ks3-keywords"` — the EXISTING keyword
block (`build_ks3.py` ~976), authored as the lesson's `vocabulary` list. It is
not a new family either.

── Instrument blocks are ACTIVITIES, not block types ────────────────────

Same argument and mechanism as C3's, C4's, C5's, C7's, C8's and C9's. The
segment each family renders into is MEASURED off Design's class attribute on
the section, not inferred from the family name — §4 of the build contract
records that B1 got two of six shells wrong by inferring them.

Ten of C10's eleven instrument sections are `class="ks3-block"` and nothing
else: light, on the card ground, which is the `check` shell.

⚠️ **c10-04's `#s-loop` is the one INK-DARK instrument in the unit** and takes
the `practical` shell. See the shell note in `ks3_art/c10.py`; the reasoning
is recorded there because that is where the class is emitted.
"""


import importlib
import pkgutil

# Instrument block types seen in authored C10 data, mapped to the §5.1.1
# segment they render as — measured from Design's markup, see the note above.
#
# ⚠️ ALL ELEVEN FAMILIES ARE MAPPED, including the nine whose lessons are not
# written yet. This map is consulted per BLOCK, so a row for a family no block
# uses is inert; what it is not is optional. A lesson author who adds a block
# whose kind is missing from here gets it left in `core` as an unknown block
# type instead of being lifted into `activities[]`, and the failure is silent
# in the direction that looks fine.
_INSTRUMENT_SEGMENTS = {
    # c10-01 · Inside the Earth
    "earth-layers":     "check",
    "depth-evidence":   "check",
    # c10-02 · Three ways to make a rock
    "rock-bench":       "check",
    # c10-03 · The rock cycle
    "grain-journey":    "check",
    "process-arrows":   "check",
    # c10-04 · A planet with limits
    "material-loop":    "practical",   # ⚠️ the unit's one ink-dark block
    "stock-limits":     "check",
    # c10-05 · What's in the air
    "air-mix":          "check",
    "atmos-history":    "check",
    # c10-06 · Carbon dioxide, humans and climate
    "greenhouse-steps": "check",
    "climate-evidence": "check",
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
    """The authored C10 lesson records, in slot order, normalised.

    Modules are discovered by name in sorted order, so `lesson_04_*` sorts
    after `lesson_03_*` and the build is deterministic. A slot with no module
    here renders a coming-soon page (§11 decision 8) rather than 404, which is
    what the five unwritten slots do today.
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
