"""P11 — *Matter and the particle model*, as one module per lesson.

Four lessons, a complete unit. The package layout follows `ks3_data/p9/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p11/`. Her page wins outright, and where her
NOTES and her drawing disagree the DRAWING IS MEASURED and the note is
reported in `docs/ks3/design-reference/p11/DEPARTURES-P11.md`.

── ⚖️ A REFERENCING UNIT — FOUR OWNED SLOTS, TWO BORROWED STRANDS ─────

`structure.REFERENCING_UNITS` lists P11 as pulling coverage from C1 and
C4. It owns four slots and five statements, and no more:

    p11-01  density                          KS3.P.PHYC.02
    p11-02  brownian-motion                  KS3.P.PHYC.03
    p11-03  temperature-and-internal-energy  KS3.P.EIM.01, KS3.P.EIM.02
    p11-04  why-ice-floats                   KS3.P.PMOD.01

`KS3.P.PHYC.01` (conservation through changes of state) and
`KS3.P.PHYC.04` (diffusion) are **C1's** and are not restated here. States
of matter, changes of state, diffusion and gas pressure all stay in C1, and
every lesson's `references` links out to them rather than teaching them
again. No sub-IDs are minted: all five statements are taken whole.

── ⚖️ FOUR RAIL STOPS, AND THREE PAGES PUT `#s-think` ON ONE ─────────

Measured off Design's own `RAIL` and `DONE` on each page, and identical to
`docs/ks3/rail-manifest.md` rows 188–191:

    p11-01  s-hook  s-bench  s-formula  s-ladder
    p11-02  s-hook  s-bench  s-think    s-ladder
    p11-03  s-hook  s-bench  s-think    s-ladder
    p11-04  s-hook  s-bench  s-think    s-ladder

On all four, `#s-bench` ticks at `s.gate !== null && s.touched`. On
`p11-01` the third stop is the CFIFA block and ticks at `!!s.cfifaOpen`,
which is `attempt_checked` — the same seam P7 uses, because her `Cfifa`
component calls `onOpen` from the Check button and from nowhere else.

On the other three the third stop is `#s-think`, and her predicate is

    if (id === 's-think') return s.answers.r1 !== null || s.hookChoice !== null;

⚠️ That is a PAGE-LEVEL predicate — the hook, or ladder rung 1 — and not a
sibling of the bench, so `band_anchor` / `band_at` is the wrong mechanism
here and `mirrors` is refused outright: `ks3_rail_manifest` derives the
mirror map from her `isDone()`, this expression matches no other stop's,
and the manifest's `mirrors` column reads `—` on all four rows. The
section takes P11's own `matter-think` shell so it declares
`data-stage-done="0"` in the shipped bytes, and `wireMatterThink` watches
exactly the two things her predicate names. See `ks3_art/p11.py`.

⊕ **THE "THINK-AGAIN AS A RAIL STOP" QUESTION IS ALREADY OPEN AND IS NOT
RE-RAISED.** `p9-01` is the first lesson in the key stage whose rail
includes `#s-think` and its package note parks the design question for
Mide. Three more lessons arrive at it here from Design's own `DONE`. The
count is noted beside the P11 entries in
`docs/ks3/misconception-register.md` so one decision covers all four; the
flag is not re-raised.

── ⚖️ ONE FORMULA BLOCK IN THE UNIT ──────────────────────────────────

`p11-01` is the unit's only QUANTITATIVE lesson. It carries the formula
statement, the triangle (`m` on top, `d × V` below — MRB-204's shape for a
PRODUCT), two staged worked examples and two write-it-out attempts.
`p11-02`, `p11-03` and `p11-04` carry no formula block and none is
missing: Design's audit says *"the rule is not to invent a calculation to
fill the block"*, and all three are MODEL or CONTRAST lessons.

── ⚖️ MISCONCEPTIONS — NO NEW FAMILY ─────────────────────────────────

Particle-model beliefs go to `PART`, whose domain line is widened here to
name density as what the model explains. `p11-03`'s temperature and
internal-energy beliefs go to `ENER`. Both families continue from the next
free number measured from the register; `PART-12` and `PART-13` are
permanent gaps and are never reissued.

── ⚖️ SCIENCE RULINGS APPLIED, NOT RE-ASKED ──────────────────────────

1. **`p11-02`'s speeds stand; her legal line's wording does not.** 500 m/s
   for air and 590 m/s for water at 20 °C are both real figures, and her
   legal line calls both "root-mean-square" — which is true of the air
   figure only (590 m/s is the MEAN speed of a water molecule; the rms is
   about 640). Instrument wins, prose changes (5A.1): the line now reads
   *typical molecular speeds*. Registered.
2. **Weight is not in this unit.** Nothing here is measured in newtons and
   nothing asks for `W = m × g`; that is P12's.
3. **Densities are g/cm³ with the Latin-1 superscript**, per her §5. Powers
   of ten, where any arise, are typed `10^25`.

── ⚠️ NO CHILDLINE BLOCK ON ANY P11 PAGE ─────────────────────────────

Design places one on `p10-01` and on no other page in P10–P12. Nothing in
this unit asks a student to disclose a risk in their own home.

── ⚠️ NO DRAFT MARKINGS ANYWHERE ─────────────────────────────────────

Every delivered page carries `showDraft` and a `ks3-review-flag`. None of
it is ported; `verify_ks3` asserts its absence.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    # Measured from Design's own markup: every `#s-bench` on all four pages
    # is `<section class="ks3-block ks3-dark ks3-practical">`.
    "matter-bench": "practical",
}

# ⚠️ `matter-think` IS NOT IN THE TABLE ABOVE, and must not be. It is the
# shell of a `misconception` BLOCK, which `r_activity` already renders
# through its own block type; lifting it here would put it in a `check`
# shell and lose Design's `ks3-misconception` ground and her amber divider.
# It is authored in `activities[]` directly, exactly as `p9-01`'s
# `charge-think` is.
#
# ⚠️ `p11-attempt` is not here either, for the P7 reason: its core block is
# a `check`, authored as one, because Design's `#s-formula` is the light
# band ground and not an ink-dark practical.

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
    """The authored P11 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
