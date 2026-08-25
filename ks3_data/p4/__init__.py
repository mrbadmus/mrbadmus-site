"""P4 — *Forces*, as one module per lesson.

Nine lessons, a complete unit. The package layout follows `ks3_data/p3/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p4/`. Her page wins outright.

── ⚖️ THE OWNERSHIP MAP — ELEVEN STATEMENTS OVER NINE SLOTS ───────────

P4 owns eleven statements and has nine slots, so three of the compound
bullets are split at the CLAUSE. Every clause is claimed exactly once and
no clause is claimed twice:

    p4-01  what-a-force-is             FORCES.01 whole
    p4-02  drawing-and-adding-forces   FORCES.02 "force arrows" + "adding
                                       forces in 1 dimension"
    p4-03  balanced-and-unbalanced     FORCES.02 "balanced and unbalanced";
                                       FORCES.05 "forces measured in newtons"
    p4-04  what-forces-do-to-motion    (no statement of its own — it is the
                                       bridge FORCES.02 needs to be about
                                       anything, carried as `touches`)
    p4-05  friction                    FORCES.04 "rubbing and friction
                                       between surfaces"
    p4-06  air-and-water-resistance    FORCES.04 "pushing things out of the
                                       way; resistance to motion of air and
                                       water"
    p4-07  moments                     FORCES.03 whole
    p4-08  springs-and-hookes-law      FORCES.04 "deforming objects;
                                       stretching and squashing – springs";
                                       FORCES.05 "measurements of stretch or
                                       compression as force is changed";
                                       FORCES.06 whole; FORCES.07 whole
    p4-09  non-contact-forces          FORCES.08 whole

⚠️ **DESIGN'S FLAG 1 STANDS OPEN AND IS NOT RESOLVED HERE.** The register
records ownership per STATEMENT, per UNIT, and has no sub-index for a
clause, so a gate counting statements per lesson will read `FORCES.04` as
claimed three times. Her note asks for `.a` / `.b` sub-IDs or a
`covers_partial` field on the lesson record. **That is a data-model
question and it is Mide's**, so nothing here invents a notation: each
lesson `covers` the statements it genuinely carries a clause of, and the
overlap is declared honestly rather than hidden by giving three lessons
three different made-up ids.

── ⚖️ `FORCE` CONTINUES FROM `FORCE-12`, AS THE REGISTER SAYS ─────────

`docs/ks3/misconception-register.md` opens `FORCE` under P3 and closes the
ruling with the sentence *"P4 continues from `FORCE-12`."* It does.
`FORCE-12` … `FORCE-35` are minted by these nine lessons.

⚠️ **DESIGN'S PROPOSED IDS ARE NOT THE ONES USED, AND COULD NOT BE.** Her
`NOTES-P4-P6.md` §6 reserves `FORCE-01` … `FORCE-36`, four per lesson,
starting `p4-01` at `FORCE-01`. Those numbers were already spent: P3 took
`FORCE-01` … `FORCE-11` on 24 Aug and `FORCE-01` there is *"whichever one
gets there first is going faster"*. Her ranges are a reservation made
without sight of the register, which she says in as many words — *"access
here is read-only, so no id is cited on any page"*. The STATEMENTS are
hers; the numbers are the register's.

── ⚠️ HER NOTES PREDATE HER DRAWING, AND THE DRAWING WAS MEASURED ─────

`NOTES-P4-P6.md` §3 describes a FOUR-step FIFA. Her own
`PHYSICS-AUDIT-2026-08-23.md` then records the rebuild: CFIFA — five
steps, with a Convert line — became the standing shape, and every
quantitative lesson in this group was rebuilt on to the shared
`Cfifa.dc.html` component. **The delivered pages carry the five-step
shape**, and that is what is built. Measured, not inferred; reported, not
escalated.

── FOUR RAIL STOPS PER LESSON ────────────────────────────────────────

Measured off Design's own `RAIL` constant on each page:

    p4-01  s-hook s-bench s-pairs   s-ladder
    p4-02  s-hook s-bench s-formula s-ladder
    p4-03  s-hook s-bench s-formula s-ladder
    p4-04  s-hook s-bench s-three   s-ladder
    p4-05  s-hook s-bench s-rules   s-ladder
    p4-06  s-hook s-bench s-stages  s-ladder
    p4-07  s-hook s-bench s-formula s-ladder
    p4-08  s-hook s-bench s-formula s-ladder
    p4-09  s-hook s-bench s-three   s-ladder

⚠️ Every lesson also carries a `#s-think` that is NOT on the rail, and
`#s-keynote` likewise. Both keep their `id`.

⚠️ **NO STOP IN THIS UNIT IS A MIRROR.** On five of the nine pages Design's
own `DONE(id, s)` gives the band stop a LOWER threshold than the bench —
`s-pairs` at one case opened against `s-bench` at three, `s-three` at the
gate alone against `s-bench` at the gate AND a control touched. MRB-249's
`mirrors` ties two stops together and would make the band stop tick LATE.
Each bench therefore marks its own band sibling, at Design's threshold,
through `band_anchor` / `band_at`.

── ⚠️ MRB-208 · THE RAIL STOP GOES ON THE BLOCK THAT CAN TICK ────────

Design draws the statement, the figure and the CFIFA inside one
`#s-formula`. A `formula` block carries no demand and emits no
`data-stage-done`, so anchoring the stop to it makes a stop that can never
become true. On the four `#s-formula` lessons the id goes on the FIRST
worked example, which is what Design's own `s.buildOpen` is set by.

── ⚠️ THE KEY FACT IS A TOP-LEVEL BLOCK, AS IT IS IN P1–P3 ───────────

Design draws `[data-key-fact]` INSIDE the band or formula section. The
engine's `key-fact` is a top-level block type and there is no way to nest
one inside an instrument without giving every instrument a key-fact slot.
It is emitted immediately after the section it belongs to, so the reading
order is unchanged and only the box's parent differs. This is the same
shape P1, P2 and P3 shipped; it is engine geometry, not content, and it
carries no departure row.

── ⚠️ SHELLS ARE MEASURED, NOT INFERRED ──────────────────────────────

Bare band section → `check`. `ks3-block ks3-dark ks3-practical` →
`practical`. `ks3-block ks3-misconception` → `misconception`.
"""

import importlib
import pkgutil

# Instrument block types seen in authored P4 data, mapped to the §5.1.1
# segment they render as — measured from Design's `class` attribute.
_INSTRUMENT_SEGMENTS = {
    # Every P4 bench is `ks3-block ks3-dark ks3-practical`.
    "interaction-board": "practical",
    "resultant-bench":   "practical",
    "support-rig":       "practical",
    "gate-run":          "practical",
    "drag-lane":         "practical",
    "fall-balance":      "practical",
    "spanner-rig":       "practical",
    "spring-plot":       "practical",
    "force-sorter":      "practical",
    # The band sections carry no class of their own on Design's pages — they
    # are a `--ks3-band` card with a 3px rule — which is the bare `check`.
    "force-band":        "check",
}

# ⚠️ `p4-attempt` IS NOT IN THE TABLE ABOVE, AND THAT IS DELIBERATE. The
# table lifts an INLINE block into `activities[]`; the attempt panel is
# already authored there, beside the two worked examples it belongs with, and
# is placed in `core` as a `check` naming its id — the same shape a
# `worked-example` uses. Adding it here would make `_normalise` try to lift a
# block whose id is already taken, which is the collision it raises on.

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
    """The authored P4 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
