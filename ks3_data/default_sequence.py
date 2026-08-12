"""MrBadmusAI default sequence v1 — the published default ordering of KS3.

**Source: architecture.md §7's `typical_year` column**, adopted as the published
default by Mide's ruling of 2026-07-26.

    "The platform must be school-agnostic. Rainford's SOW is reference
     evidence, never a template."

This map earns the default because of *how it was derived*: from the **statutory
programme of study and the prerequisite graph** — what has to be true before the
next idea can be taught — and not from any one school's timetable. A default is
what a school gets before it has told us anything about itself, so it must not
carry another school's local constraints, staffing, lab availability or option
blocks. Those are real, but they are that school's, and §4.5 is how a school
says so.

**This is DATA, never structure** (§4.5). A school reorders KS3 by changing a
scheme-of-work row: it writes rows into ``scheme_of_work_overrides`` and they
win over the global default in ``scheme_of_work_entries``. Nothing rebuilds, no
URL contains a year, and no page moves. If honouring a different order ever
costs more than a data change, the invariant has failed and we want to know
immediately.

**§7's column is no longer a "fallback".** It IS the default. There is no second
layer to consult and no precedence question to get wrong: this dict and
``structure.py``'s ``typical_year`` are the same mapping, and the assertion at
the bottom of this module fails the import if they ever drift apart. It is
written out in full here anyway, because **the published default is an artifact**
— a person should be able to read the whole of it in one place without
reconstructing it from 33 tuples.

---

**Reversal, 2026-07-26.** This reverses the joint ruling made earlier the same
day on architecture.md **§11 decision 5 and conflict 1d**, which had adopted
MRB-103's locked Rainford year map as "MrBadmusAI default sequence v1" and
demoted §7's column to an advisory fallback. Mide reversed it: a real school's
real sequence is excellent *evidence*, and is exactly the wrong thing to publish
as a *platform* default.

Rainford's map has moved to ``ks3_data/school_schemes.py``, where it is one
school's configured sequence — and, being 16 units divergent from this map, the
live test that the override mechanism costs nothing (§4.5, §8.9).

Nothing about the reversal was expensive, which is itself the evidence: swapping
the platform's entire published default was a data change in one dict.
"""

from . import structure

# ═══════════════════════════════════════════════════════════════════════════
# The published default — 33 units, 183 lessons
# ═══════════════════════════════════════════════════════════════════════════
#
# Y7   9 units,  53 lessons
# Y8  13 units,  79 lessons
# Y9  11 units,  51 lessons
#
# Year 8 is the heavy year, and §7 states that rather than shading it: it
# carries four of the five physics units a school would rather not meet in
# Year 7. A school that finds it heavy moves a unit — which is a data change.

DEFAULT_SEQUENCE_V1 = {
    # ── Year 7 ──────────────────────────────────────────────────────────
    # Bio: cells and the organisation of life first, because every later
    #      biology idea is stated in terms of cells; then the two body
    #      systems that need nothing but cells to make sense.
    "B1": 7, "B2": 7, "B3": 7,
    # Chem: the particle model first — states, then what particles ARE, then
    #       what you can do with a mixture of them. Nothing here needs a
    #       reaction, and everything after it does.
    "C1": 7, "C2": 7, "C3": 7,
    # Phys: motion before forces, forces before everything; and the particle
    #       model's physics half (density, Brownian motion) alongside C1,
    #       which owns the chemistry half (§4.6).
    "P3": 7, "P4": 7, "P11": 7,

    # ── Year 8 ──────────────────────────────────────────────────────────
    # Bio: gas exchange and reproduction as whole-organism systems, then
    #      bioenergetics — photosynthesis and respiration both require the
    #      cell and the reaction, so neither can precede Y7 chemistry.
    "B4": 8, "B5": 8, "B7": 8, "B8": 8,
    # Chem: reactions, now that atoms and elements exist to rearrange —
    #       what a reaction is, the types, acids, and the table that
    #       predicts.
    "C4": 8, "C5": 8, "C6": 8, "C8": 8,
    # Phys: energy, then pressure (needs forces from P4), then the two wave
    #       units, then circuits.
    "P1": 8, "P5": 8, "P6": 8, "P7": 8, "P8": 8,

    # ── Year 9 ──────────────────────────────────────────────────────────
    # Bio: health, ecosystems, inheritance and evolution — the units that
    #      read as consequences of everything above them.
    "B6": 9, "B9": 9, "B10": 9, "B11": 9,
    # Chem: energetics (needs reactions), metals (needs the reactivity
    #       series), and the Earth as one system.
    "C7": 9, "C9": 9, "C10": 9,
    # Phys: energy at home (quantitative, needs P1), the two electricity
    #       units that follow circuits, and space.
    "P2": 9, "P9": 9, "P10": 9, "P12": 9,
}


# ═══════════════════════════════════════════════════════════════════════════
# Drift guard
# ═══════════════════════════════════════════════════════════════════════════
# The dict above is written out in full for legibility — the published default
# should be readable in one place. The cost of writing it twice is that the two
# copies can disagree, so they are not allowed to: this fails the import, at
# module load, naming the exact units that diverged.
#
# There is no "which one wins" rule on purpose. A divergence here is not a
# precedence question, it is a transcription bug, and it should stop the build.

def _assert_agrees_with_structure():
    declared = {code: u["typical_year"]
                for code, u in structure.unit_index().items()}

    missing = sorted(set(declared) - set(DEFAULT_SEQUENCE_V1),
                     key=lambda c: (c[0], int(c[1:])))
    extra = sorted(set(DEFAULT_SEQUENCE_V1) - set(declared),
                   key=lambda c: (c[0], int(c[1:])))
    differ = sorted(
        ((c, DEFAULT_SEQUENCE_V1[c], declared[c])
         for c in set(declared) & set(DEFAULT_SEQUENCE_V1)
         if DEFAULT_SEQUENCE_V1[c] != declared[c]),
        key=lambda t: (t[0][0], int(t[0][1:])))

    if missing or extra or differ:
        parts = []
        if missing:
            parts.append("units in structure.py but not in the default: %s"
                         % ", ".join(missing))
        if extra:
            parts.append("units in the default but not in structure.py: %s"
                         % ", ".join(extra))
        if differ:
            parts.append("year disagrees for: %s"
                         % ", ".join("%s (default Y%d, structure.py Y%d)" % d
                                     for d in differ))
        raise ValueError(
            "DEFAULT_SEQUENCE_V1 has drifted from structure.py's typical_year. "
            "They are the same mapping by construction (architecture.md §7, "
            "ruled 2026-07-26) — %s. Fix the transcription; do not pick a "
            "winner." % "; ".join(parts))


_assert_agrees_with_structure()


def year_of(unit_code, fallback=None):
    """Default year for a unit.

    ``fallback`` is vestigial: the assertion above guarantees every one of the
    33 units is present, so it is only ever returned for a code that is not a
    KS3 unit at all.
    """
    return DEFAULT_SEQUENCE_V1.get(unit_code, fallback)


def by_year():
    out = {7: [], 8: [], 9: []}
    for code, yr in DEFAULT_SEQUENCE_V1.items():
        out[yr].append(code)
    for yr in out:
        out[yr].sort(key=lambda c: (c[0], int(c[1:])))
    return out
