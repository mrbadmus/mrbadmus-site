"""P12 — *Space*, as one module per lesson.

Six lessons, a complete unit. The package layout follows `ks3_data/p9/`
exactly.

Every lesson is authored against Claude Design's delivered pages in
`docs/ks3/design-reference/p12/`. Her page wins outright, and where her
NOTES and her drawing disagree the DRAWING IS MEASURED and the note is
reported in `docs/ks3/design-reference/p12/DEPARTURES-P12.md`.

── ⚖️ THE OWNERSHIP MAP — FOUR STATEMENTS OVER SIX SLOTS ─────────────

    p12-01  gravity-and-weight          SPACE.01a  the force of gravity, and
                                                   weight = mass × g with
                                                   g = 10 N/kg on Earth
    p12-02  mass-vs-weight              SPACE.01b  g, and so weight, differs
                                                   elsewhere while mass does
                                                   not
    p12-03  gravity-earth-moon-and-sun  SPACE.01c  Earth–Moon and Earth–Sun
                                                   gravity, qualitatively
    p12-04  the-sun-stars-and-galaxies  SPACE.02   whole
    p12-05  seasons-and-the-tilt        SPACE.03   whole
    p12-06  how-far-is-a-light-year     SPACE.04   whole

`KS3.P.SPACE.01` is compound — it carries the definition, the variation and
the two named pairs in one bullet — so it is split at the clause under the
rule `ks3_data/substatements.py` already carries. This is the fifth physics
unit in the run to use it.

── ⚖️ FOUR RAIL STOPS ON EVERY PAGE, AND THE THIRD ONE FORKS ─────────

Measured off Design's own `RAIL` and `DONE` on each page, and matching
`docs/ks3/rail-manifest.md` row for row:

    p12-01  s-hook  s-bench  s-formula  s-ladder
    p12-02  s-hook  s-bench  s-formula  s-ladder
    p12-03  s-hook  s-bench  s-think    s-ladder
    p12-04  s-hook  s-bench  s-think    s-ladder
    p12-05  s-hook  s-bench  s-think    s-ladder
    p12-06  s-hook  s-bench  s-formula  s-ladder

Her `DONE`, on all six:

    s-hook     s.hookChoice !== null
    s-bench    s.gate !== null && s.touched
    s-formula  !!s.cfifaOpen                          (p12-01/02/06)
    s-think    s.answers.r1 !== null || s.hookChoice !== null   (p12-03/04/05)
    s-ladder   both marked rungs answered and both self rungs checked

⚠️ **`#s-think` IS A RAIL STOP ON THREE PAGES, AND IT IS NOT A MIRROR.**
`ks3_rail_manifest` derives the mirror map by comparing her `isDone()`
expressions for EQUALITY, and `s.answers.r1 !== null || s.hookChoice !== null`
is not `s.gate !== null && s.touched`. So the manifest records no mirror for
any P12 lesson — the mirrors column reads `—` on all six rows — and a
declared `mirrors` would fail `check_rail_matches_design` outright.

It is not `band_anchor` / `band_at` either, which is how P4, P6 and P9 tick a
sibling: those tick the section BESIDE the bench, from the bench. Her
predicate here is satisfied by the HOOK, which is above the bench, or by
LADDER RUNG 1, which is below it — so a student can complete this stop
without touching the bench at all, and the bench cannot honestly claim it.

The section therefore takes P12's OWN family `space-think`, whose renderer
draws nothing and whose only job is the shell declaration
(`data-instrument data-stage-done="0"`, which `check_nothing_ticks_on_load`
requires of a rail anchor), plus a wire function that listens to the hook's
options and to ladder rung 1. `ks3_art/core.py`'s shared `confrontation`
shell emits the marker without the declaration, and that file is shared by
ten units.

That parallels the open flag raised at `p9-01` — *Think-again as a rail
stop* — and it is the same ruling reaching a different predicate. It is
noted in `docs/ks3/misconception-register.md` and NOT re-raised.

`p12-01`, `p12-02` and `p12-06` keep the ordinary `predict` kind on their
`#s-think`, because on those three pages the third stop is `#s-formula` and
the confrontation is off the rail exactly as everywhere else in the key
stage.

── ⚖️ SCIENCE RULINGS ALREADY MADE, APPLIED AND NOT RE-ASKED ─────────

1. **`p12-03`'s forces stand in `10^20` notation, as drawn.** Her NOTES §6
   asks whether scientific notation is too early for KS3. It is not: the
   figures are READOUTS the bench computes, rung 2 asks for equality rather
   than arithmetic, and standard form is KS3 maths.
2. **`p12-04`'s star counts stand.** "About 200 billion", "about a trillion"
   and "around two trillion galaxies" are hers, hedged in her own words, and
   her legal line records that galaxy star counts are estimates with wide
   error bars.
3. **`p12-05`'s model stands with its legal line.** Declination, the sunrise
   equation, `90 − |lat − dec|` and `sin(altitude)` are real astronomy, and
   the legal line names what the model leaves out.
4. **`g = 10 N/kg` is statutory** and is the figure used throughout. Each
   page's legal line records that Earth's true mean value is 9.81 N/kg.
5. **No Childline block on any P12 page.** Nothing here asks a student to
   disclose anything.

── ⚠️ ONE BENCH FAMILY, SIX MODELS ──────────────────────────────────

Design ships `Bench.dc.html` — ONE shared child component mounted by all six
pages with `<dc-import name="Bench" …>` — so `space-bench` is one family and
one drawer, and the six pages differ only in the `model` their payload
names. See `ks3_art/p12.py`.
"""

import importlib
import pkgutil

_INSTRUMENT_SEGMENTS = {
    # Design's bench section is `ks3-block ks3-dark ks3-practical` on all six
    # pages — measured off her markup, not inferred from the kind name, which
    # is how B1 got two of six shells wrong.
    "space-bench": "practical",
}

# ⚠️ `space-think` AND `p12-attempt` ARE NOT IN THE TABLE ABOVE, and must not
# be. `space-think` is the shell of a `misconception` BLOCK, which `r_activity`
# already renders through its own block type; lifting it here would put it in a
# `check` shell and lose Design's `ks3-misconception` ground and her amber
# rule. `p12-attempt` is authored on a `check` block directly, exactly as P7's
# `p7-attempt` is.

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
    """The authored P12 lesson records, in slot order, normalised."""
    found = []
    for mod in sorted(m.name for m in pkgutil.iter_modules(__path__)):
        if not mod.startswith("lesson_"):
            continue
        m = importlib.import_module("%s.%s" % (__name__, mod))
        record = getattr(m, "LESSON", None)
        if record is not None:
            found.append(_normalise(dict(record)))
    return found
