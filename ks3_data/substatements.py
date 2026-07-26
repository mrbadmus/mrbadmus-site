"""Clause-level sub-IDs — architecture.md §11 decision 11, ruled option (a).

Some statutory bullets are **compound**: one bullet carries several ideas that
any sane scheme of work teaches as separate lessons. `KS3.P.ECT.02` alone
contains thermal equilibrium, conduction, radiation *and* insulators.

Under §4.4 rule 3 every statement is owned by exactly one lesson, and under
§10.2 every lesson has non-empty `covers`. With 137 statements and 185 lessons
those two rules cannot both hold — unless the compound bullets are split at the
grain lessons are actually written at. That is what this file does.

**The four operative rules** (ruled 2026-07-26):

1. **The parent ID and its verbatim text are never touched.** This file lives
   *outside* ``statutory-register.md`` precisely so the register stays a faithful
   copy of the source document and Mide's transcription gate keeps working. A
   sub-ID is an additional, finer handle on a clause *of* the parent.
2. **Exactly-once bites at sub-ID grain.** Where a bullet is split, its clauses
   are owned exactly once each, so the parent is covered exactly once by
   construction. Where a bullet is not split, the parent is owned exactly once as
   before.
3. **Mint lazily — per unit, at authoring time. Never big-bang.** A sub-ID
   appears here only because a real lesson needed it. Most bullets will never be
   split.
4. **Sub-IDs are permanent once referenced**, exactly as parent IDs are. Lazy
   minting is about *when* an ID is created, never about whether it can later be
   renumbered. It cannot.

Form: parent ID + a lowercase letter, allocated in the clause order the bullet
prints.
"""

# parent statement ID → [(sub-id suffix, clause text, minted-for unit), ...]
#
# `clause` is a plain-English statement of the clause. It is NOT a quotation of
# the statutory document — the verbatim text lives in statutory-register.md
# against the parent, and is deliberately not duplicated here.

SUBSTATEMENTS = {
    # Minted for C1 (Phase 1, 2026-07-26). The bullet reads:
    #   "the properties of the different states of matter (solid, liquid and
    #    gas) in terms of the particle model, including gas pressure"
    # Three genuinely separable teaching ideas, and C1 teaches them as three
    # lessons: the model itself, the three states' properties, and gas pressure.
    "KS3.C.PNM.01": [
        ("a", "The particle model itself: matter is made of tiny particles, "
              "which are always moving, with empty space between them.", "C1"),
        ("b", "The properties of the different states of matter (solid, liquid "
              "and gas), explained by the particle model.", "C1"),
        ("c", "Gas pressure, explained by the particle model.", "C1"),
    ],
}


def sub_ids(parent):
    """All minted sub-IDs for a parent statement, in clause order."""
    return ["%s%s" % (parent, suf) for suf, _, _ in SUBSTATEMENTS.get(parent, [])]


def all_sub_ids():
    out = {}
    for parent, clauses in SUBSTATEMENTS.items():
        for suf, text, unit in clauses:
            out["%s%s" % (parent, suf)] = {
                "parent": parent, "clause": text, "minted_for": unit,
            }
    return out


def parent_of(statement_id):
    """`KS3.C.PNM.01a` → `KS3.C.PNM.01`. A parent ID returns itself."""
    if statement_id and statement_id[-1].islower():
        return statement_id[:-1]
    return statement_id
