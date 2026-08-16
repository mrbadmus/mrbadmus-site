"""B2 — Movement: skeleton and muscles. Four lessons, Year 7 Biology.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/b2/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/b2/`) and the measured payload map
(`docs/ks3/b2-inventory/PAYLOAD-MAP.md`) under MRB-220.

⚑ **Statutory coverage needed a clause split, and it is flagged for Mide.**
Design's NOTES §1 records that `joints` "has no statement of its own: the 2014
document does not name joints, but it names movement, and a movement lesson
that never mentions how a bone can move at all is not teachable." Two standing
rules meet there and cannot both hold as written: §10.2 requires every
authored lesson to have non-empty `covers`, and §4.4 rule 3 requires every
subject-content statement to be owned exactly once.

`ks3_data/substatements.py` is the platform's own answer to precisely that
collision, and its rule 3 says to mint lazily, per unit, at authoring time. So
`KS3.B.SKEL.01` is split at the grain the bullet itself prints — it names a
*structure* and it names *functions* — giving `01a` to `what-the-skeleton-does`
and `01b` to `joints`. Nothing about the parent statement or its verbatim text
moves.

**This is a curriculum-mapping judgement, not a rendering one, and it is
Mide's to confirm or reverse.** The alternative NOTES offers is merging the two
lessons, which is a `structure.py` change rather than a content one. Reversing
the split costs two `covers` lines and one dict entry.
"""

from .b2 import lessons as _b2_lessons

UNIT = {
    "code":            "B2",
    "slug":            "movement-skeleton-and-muscles",
    "title":           "Movement: skeleton and muscles",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "Bone is not the dead scaffolding it looks like in the "
                       "corner of a lab. It is living tissue that rebuilds "
                       "itself around the forces you put through it, it makes "
                       "your blood, and it is the only thing your muscles have "
                       "to pull against.",
    "lessons": _b2_lessons(),
}
