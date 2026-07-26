"""MrBadmusAI default sequence v1 — the published default ordering of KS3.

**Source: MRB-103's locked year map** (ratification comment, 6 Jul 2026, by Ayo),
adopted as the published default by Mide's ruling of 2026-07-26 — architecture.md
§11 decision 5 and conflict 1d, ruled jointly.

    "Adopt MRB-103's locked map as the published default, because it is a real
     school's real sequence and Ayo already ruled on it, and treat §7's column
     as the advisory fallback."

**This is DATA, never structure** (§4.5). A school reorders KS3 by changing a
scheme-of-work row; nothing rebuilds, no URL contains a year, and no page moves.
If honouring a different order ever costs more than a data change, the invariant
has failed and we want to know immediately.

`typical_year` on the lesson record (§4.8) remains the §7 advisory fallback and
is consulted only where this map is silent. Where the two differ, this map wins.

---

Rainford's map names some topics that are **not in the statutory programme of
study** and which conflict 1g deliberately excludes from coverage: circulation
(Y8 Bio), rate of reaction (Y9 Chem), and fusion / star life cycle (Y9 Phys).
They are recorded in ``BEYOND_STATUTORY`` below so the omission stays visible and
deliberate rather than looking like a transcription slip. They are NOT units, and
nothing `covers` them.
"""

# unit code → year, transcribed from MRB-103's locked map.
DEFAULT_SEQUENCE_V1 = {
    # ── Year 7 ──────────────────────────────────────────────────────────
    # Bio: Cells & organisation (incl. skeleton/muscles), Diet & digestion,
    #      Reproduction.
    "B1": 7, "B2": 7, "B3": 7, "B5": 7,
    # Chem: States of matter (particles + separation), Chemical reactions
    #       (incl. exo/endo, combustion), Materials & reactivity.
    "C1": 7, "C3": 7, "C4": 7, "C5": 7, "C7": 7, "C9": 7,
    # Phys: Forces & motion (incl. speed), Electricity & magnetism, Space.
    "P3": 7, "P4": 7, "P8": 7, "P9": 7, "P10": 7, "P12": 7,

    # ── Year 8 ──────────────────────────────────────────────────────────
    # Bio: Bioenergetics (photosynthesis, respiration, gas exchange),
    #      Genetics & evolution, Ecosystems.
    "B4": 8, "B7": 8, "B8": 8, "B9": 8, "B10": 8, "B11": 8,
    # Chem: Atoms/elements/compounds (incl. periodic table + groups),
    #       Acids & alkalis, Earth & atmosphere.
    "C2": 8, "C6": 8, "C8": 8, "C10": 8,
    # Phys: Energy, Waves, Energy in matter (particle model, pressure, heating).
    "P1": 8, "P2": 8, "P5": 8, "P6": 8, "P7": 8, "P11": 8,

    # ── Year 9 (short, part-year, then GCSE bridge) ──────────────────────
    # Bio: Health & disease.  Chem: rate of reaction → beyond statutory.
    # Phys: exploring space (fusion, star life cycle) → beyond statutory.
    "B6": 9,
}

# Deepening pairs — MRB-103: "spirals to model as deepening pairs, not one topic".
# Both halves are separate units; the thread tags (§4.7) carry the spiral.
DEEPENING_PAIRS = [
    ("particle model", "C1", 7, "P11", 8),
    ("space",          "P12", 7, None, 9),   # Y9 half is beyond-statutory — see below
]

# Named in Rainford's map, deliberately NOT units and NOT in any `covers` list.
# architecture.md §11 conflict 1g, ruled 2026-07-26.
BEYOND_STATUTORY = {
    "circulation":              ("biology",   8, "KS4 content; not in the 2014 KS3 programme of study."),
    "rate-of-reaction":         ("chemistry", 9, "KS4 content; not in the 2014 KS3 programme of study."),
    "fusion-and-star-life-cycle": ("physics", 9, "KS4 content; not in the 2014 KS3 programme of study."),
}

# Energy was ruled Y8 on strict Rainford, against the Y7 consensus of Ark and
# both Opus passes. MRB-103 flags it as revisable precisely because year_band is
# soft. Recorded so the divergence is not mistaken for an error.
NOTES = {
    "P1": "Energy ruled Y8 on strict Rainford, against the Y7 consensus of Ark "
          "and both Opus 4.8 passes. Revisable — year is soft (§4.5).",
}


def year_of(unit_code, fallback=None):
    """Default year for a unit. Falls back to §7's advisory column."""
    return DEFAULT_SEQUENCE_V1.get(unit_code, fallback)


def by_year():
    out = {7: [], 8: [], 9: []}
    for code, yr in DEFAULT_SEQUENCE_V1.items():
        out[yr].append(code)
    for yr in out:
        out[yr].sort(key=lambda c: (c[0], int(c[1:])))
    return out
