"""Real schools' configured KS3 sequences — SEED DATA, never the default.

**These are reference evidence and seed data. They are not a template, and no
school scheme in this file is ever the platform's published default.** The
published default lives in ``default_sequence.py`` and is derived from the
statutory spine and the prerequisite graph, not from anybody's timetable.

Mide's ruling of 2026-07-26 (reversing the earlier ruling of the same day on
architecture.md §11 decision 5 / conflict 1d):

    "Rainford's SOW is reference evidence, never a template — the platform must
     be school-agnostic."

So MRB-103's locked Rainford year map, which had briefly been adopted as
"MrBadmusAI default sequence v1", moved here. It is now what it always should
have been: **one school's configured sequence**, and the proof that the override
mechanism in §4.5 works.

---

**Why this file exists at all.** §4.5 makes a binding promise:

    "Reordering a school's entire KS3 curriculum must require zero content
     changes and zero regeneration — it is a data change in that school's
     scheme of work."

A promise nobody has ever tested is a wish. Rainford's map diverges from the
platform default on 16 of the 33 units, and ``verify_ks3.py`` applies the whole
of it over the default and rebuilds, asserting that not one page path and not
one page byte changes. That is the gate §4.5 lives or dies on.

**Where these rows land in the database.** Not in ``scheme_of_work_entries`` —
that table is GLOBAL and holds the platform default. School schemes go in
``scheme_of_work_overrides``, which carries a ``school_id``. Both tables needed
the same three KS3 constraint fixes (§8.7); see migrations
``20260726120000_ks3_scheme_of_work_entries.sql`` and
``20260726180000_ks3_scheme_of_work_overrides.sql``. The seed SQL for this file
is generated, never hand-written — run ``python3 ks3_seed_sow.py``.

**Adding a second school.** Drop another key into ``SCHOOL_SCHEMES`` with the
same shape. Nothing else changes: the generator, the divergence helper and the
verification gate all iterate the dict. No refactor, which is the point.
"""

from .default_sequence import DEFAULT_SEQUENCE_V1

# ═══════════════════════════════════════════════════════════════════════════
# The schemes
# ═══════════════════════════════════════════════════════════════════════════
#
# Shape of one entry:
#
#     "school-slug": {
#         "name":             human name, as it appears in public.schools.name
#         "source":           where the map came from, and who ruled on it
#         "units":            unit code → year group.  The scheme itself.
#         "notes":            unit code → why this school's choice differs
#         "beyond_statutory": topics this school teaches that KS3 statute
#                             does not require — recorded, never units
#         "deepening_pairs":  spirals this school teaches as two halves
#     }
#
# `units` is the only key the seed generator and the §4.5 gate consume. The
# other three are commentary about the school and must never render on a
# platform page.

SCHOOL_SCHEMES = {
    "rainford-high": {
        "name": "Rainford High School",
        "source": (
            "MRB-103 locked year map, ratification comment 6 Jul 2026, by Ayo; "
            "ruled against Rainford's actual scheme of work."
        ),

        # unit code → year, transcribed from MRB-103's locked map.
        "units": {
            # ── Year 7 ──────────────────────────────────────────────────
            # Bio: Cells & organisation (incl. skeleton/muscles), Diet &
            #      digestion, Reproduction.
            "B1": 7, "B2": 7, "B3": 7, "B5": 7,
            # Chem: States of matter (particles + separation), Chemical
            #       reactions (incl. exo/endo, combustion), Materials &
            #       reactivity.
            "C1": 7, "C3": 7, "C4": 7, "C5": 7, "C7": 7, "C9": 7,
            # Phys: Forces & motion (incl. speed), Electricity & magnetism,
            #       Space.
            "P3": 7, "P4": 7, "P8": 7, "P9": 7, "P10": 7, "P12": 7,

            # ── Year 8 ──────────────────────────────────────────────────
            # Bio: Bioenergetics (photosynthesis, respiration, gas exchange),
            #      Genetics & evolution, Ecosystems.
            "B4": 8, "B7": 8, "B8": 8, "B9": 8, "B10": 8, "B11": 8,
            # Chem: Atoms/elements/compounds (incl. periodic table + groups),
            #       Acids & alkalis, Earth & atmosphere.
            "C2": 8, "C6": 8, "C8": 8, "C10": 8,
            # Phys: Energy, Waves, Energy in matter (particle model, pressure,
            #       heating).
            "P1": 8, "P2": 8, "P5": 8, "P6": 8, "P7": 8, "P11": 8,

            # ── Year 9 (short, part-year, then GCSE bridge) ──────────────
            # Bio: Health & disease.  Chem: rate of reaction → beyond statutory.
            # Phys: exploring space (fusion, star life cycle) → beyond statutory.
            "B6": 9,
        },

        # Energy was ruled Y8 on strict Rainford, against the Y7 consensus of Ark
        # and both Opus passes. MRB-103 flags it as revisable precisely because
        # year_band is soft. Recorded so the divergence is not mistaken for an
        # error.
        "notes": {
            "P1": "Energy ruled Y8 on strict Rainford, against the Y7 consensus "
                  "of Ark and both Opus 4.8 passes. Revisable — year is soft "
                  "(§4.5).",
        },

        # Named in Rainford's map, deliberately NOT units and NOT in any `covers`
        # list. architecture.md §11 conflict 1g, ruled 2026-07-26.
        "beyond_statutory": {
            "circulation":                ("biology",   8, "KS4 content; not in the 2014 KS3 programme of study."),
            "rate-of-reaction":           ("chemistry", 9, "KS4 content; not in the 2014 KS3 programme of study."),
            "fusion-and-star-life-cycle": ("physics",   9, "KS4 content; not in the 2014 KS3 programme of study."),
        },

        # Deepening pairs — MRB-103: "spirals to model as deepening pairs, not
        # one topic". Both halves are separate units; the thread tags (§4.7)
        # carry the spiral.
        "deepening_pairs": [
            ("particle model", "C1", 7, "P11", 8),
            ("space",          "P12", 7, None, 9),   # Y9 half is beyond-statutory
        ],
    },

    # ── SLOT: Westleigh ─────────────────────────────────────────────────────
    # "westleigh": pending — Mide holds the map; requested 2026-07-26.
    #
    # Leave this slot open and fill it as soon as the map arrives. One divergent
    # school proves the override mechanism runs; TWO divergent real schemes,
    # teaching the *identical* 185 lessons in two different orders off one
    # unchanged build, is the demonstration §4.5 actually exists for. Until the
    # second one lands, "year is metadata, never structure" is a claim supported
    # by a single example.
    #
    # Adding it is a dict entry and nothing else — no refactor, no new code
    # path, no rebuild. If it ever turns out to need more than that, §4.5 has
    # failed and that is the finding.
}


# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════

def scheme(school_key):
    """One school's record. Raises with the known keys rather than KeyError."""
    try:
        return SCHOOL_SCHEMES[school_key]
    except KeyError:
        raise KeyError(
            "No school scheme %r. Known schools: %s. School schemes are seed "
            "data (see this module's docstring) — a school with no scheme "
            "configured gets the platform default, which is correct behaviour, "
            "not a missing row." % (school_key, sorted(SCHOOL_SCHEMES)))


def divergence_from_default(school_key):
    """Units where this school differs from the published default.

    Returns ``[(unit_code, default_year, school_year), ...]`` in unit-code
    order. This is the size of the §4.5 test: every tuple here is a unit the
    school teaches in a different year from the platform default, and the
    invariant says all of them together cost zero page changes.

    A unit the school does not list at all is not a divergence — an unlisted
    unit simply falls through to the default.
    """
    units = scheme(school_key)["units"]
    out = []
    for code in sorted(DEFAULT_SEQUENCE_V1,
                       key=lambda c: (c[0], int(c[1:]))):
        school_year = units.get(code)
        if school_year is not None and school_year != DEFAULT_SEQUENCE_V1[code]:
            out.append((code, DEFAULT_SEQUENCE_V1[code], school_year))
    return out


def effective_sequence(school_key):
    """The full 33-unit map this school actually teaches.

    The school's configured units laid over the platform default, which is
    exactly what the database does: ``scheme_of_work_overrides`` rows win over
    ``scheme_of_work_entries`` rows, and anything a school has not configured
    keeps the default. Used by ``verify_ks3.py`` to apply a real school's real
    sequence over a real build.
    """
    out = dict(DEFAULT_SEQUENCE_V1)
    out.update(scheme(school_key)["units"])
    return out


def by_year(school_key):
    """year → sorted unit codes, for one school's effective sequence."""
    out = {7: [], 8: [], 9: []}
    for code, yr in effective_sequence(school_key).items():
        out[yr].append(code)
    for yr in out:
        out[yr].sort(key=lambda c: (c[0], int(c[1:])))
    return out
