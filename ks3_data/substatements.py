"""Clause-level sub-IDs — architecture.md §11 decision 11, ruled option (a).

Some statutory bullets are **compound**: one bullet carries several ideas that
any sane scheme of work teaches as separate lessons. `KS3.P.ECT.02` alone
contains thermal equilibrium, conduction, radiation *and* insulators.

Under §4.4 rule 3 every statement is owned by exactly one lesson, and under
§10.2 every lesson has non-empty `covers`. With 137 statements and 183 lessons
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
    # Minted for B1 (2026-08-09). The bullet reads:
    #   "cells as the fundamental unit of living organisms, including how to
    #    observe, interpret and record cell structure using a light microscope"
    # Two separable teaching ideas, taught a week apart by every scheme of work.
    "KS3.B.CELLS.01": [
        ("a", "Cells as the fundamental unit of living organisms: everything "
              "alive is built from cells, and nothing else is.", "B1"),
        ("b", "How to observe, interpret and record cell structure using a "
              "light microscope.", "B1"),
    ],
    # Minted for B2 (2026-08-16, MRB-220). The bullet reads:
    #   "the structure and functions of the human skeleton, to include
    #    support, protection, movement and making blood cells"
    # It names TWO things — a structure and a set of functions — and B2 is
    # written at that grain: `what-the-skeleton-does` owns the four functions,
    # `joints` owns the structure at the places bones meet.
    #
    # ⚑ Minted because §10.2 (non-empty `covers`) and §4.4 rule 3 (owned
    # exactly once) cannot both hold for `joints` otherwise. Design's NOTES §1
    # says so in as many words: "the 2014 document does not name joints, but
    # it names movement, and a movement lesson that never mentions how a bone
    # can move at all is not teachable." That is exactly the compound-bullet
    # case this file exists for. **Flagged for Mide** in
    # `ks3_data/biology_b2_movement.py` — it is a curriculum-mapping call,
    # and the alternative NOTES offers is merging the two lesson slots.
    "KS3.B.SKEL.01": [
        ("a", "The functions of the human skeleton: support, protection, "
              "movement, and making blood cells.", "B2"),
        ("b", "The structure of the human skeleton at the places bones meet: "
              "the types of joint, and what each one allows and refuses.",
         "B2"),
    ],
    # Minted for C2 (2026-08-16, MRB-220). The bullet reads:
    #   "differences between atoms, elements and compounds"
    # Two ideas, and C2 teaches them as two lessons a week apart: what makes
    # something an element (and why nothing about how it looks will tell you),
    # then what a compound is and how it differs from a mixture.
    "KS3.C.AEC.02": [
        ("a", "What an element is: one kind of atom, and not separable into "
              "anything simpler by chemistry.", "C2"),
        ("b", "What a compound is, and how it differs from a mixture: fixed "
              "proportion, joined in a reaction, new properties.", "C2"),
    ],
    # Minted for C2 (2026-08-16, MRB-220). The bullet reads:
    #   "chemical symbols and formulae for elements and compounds"
    # The bullet itself prints two things joined by "and", and Design's NOTES
    # §1 gives the pedagogic reason for keeping them apart: "symbols are a
    # notation to be read, formulae are a model of what is in a particle, and
    # teaching them in one sitting is what makes students think a formula is
    # just a longer symbol."
    "KS3.C.AEC.03": [
        ("a", "Chemical symbols for the elements: one capital starts one "
              "element, and the case of a second letter is not a style choice.",
         "C2"),
        ("b", "Formulae for compounds: which elements are present and how many "
              "atoms of each.", "C2"),
    ],
    # Minted for B3 (2026-08-16, MRB-228), and this one splits ACROSS UNITS.
    # The bullet reads:
    #   "calculations of energy requirements in a healthy daily diet"
    # It was claimed by Biology B3 and Physics P2 at once, and §7.4 had given
    # the whole of it to P2 with B3 holding a reference slot that generated no
    # page at all. **Ruled by Mide on 16 Aug 2026 (MRB-232):** it is two
    # lessons wearing one bullet and it splits at that seam.
    #
    # The seam is worth naming, because it is not the obvious one. It is not
    # "biology does the food and physics does the sums" — it is that a
    # REQUIREMENT is a fact about a body and a kJ VALUE is a measurement of a
    # substance, and only the second is what a joule is for. P2's link back to
    # B3 is a `references` EDGE, never prose, so neither page repeats the
    # other. Full ruling in `docs/ks3/statutory-register.md`.
    "KS3.B.NUT.02": [
        ("a", "What you need and why: that the energy a person needs varies "
              "with who they are and what they do, and what follows from "
              "taking in more or less than that.", "B3"),
        ("b", "Comparing energy values from food labels in kJ: the arithmetic "
              "and the units.", "P2"),
    ],
    # Minted for B3 (2026-08-16, MRB-228). The bullet reads:
    #   "the tissues and organs of the human digestive system, including
    #    adaptations to function and how the digestive system digests food
    #    (enzymes simply as biological catalysts)"
    # The longest statement in the strand, and it prints its own three clauses:
    # the organs, what they do to food, and how their structure fits the job.
    # B3 teaches them as three lessons and no scheme of work teaches them as
    # one.
    #
    # ⚠️ `b` is the CATALYST clause and it is exactly as wide as the bullet's
    # own parenthesis: enzymes simply as biological catalysts. Enzyme RATE —
    # the temperature and pH curves, the optimum, denaturing — has no KS3
    # statutory statement anywhere and belongs in the Year 9 bridge (MRB-199).
    # Design's b3-06 teaches rate in full and the page renders as drawn, but
    # none of that material is CLAIMED here. Widening `b` to cover it would
    # mint a statement the national curriculum does not contain.
    "KS3.B.NUT.04": [
        ("a", "The tissues and organs of the human digestive system.", "B3"),
        ("b", "How the digestive system digests food, with enzymes simply as "
              "biological catalysts.", "B3"),
        ("c", "Adaptations of the digestive system to its function.", "B3"),
    ],
    # Minted for B4 (2026-08-16, MRB-244). The bullet reads:
    #   "the structure and functions of the gas exchange system in humans,
    #    including adaptations to function"
    # The bullet's own "including" is the seam, and B4 is written across it:
    # `the-gas-exchange-system` walks the six parts and what each does, and
    # `alveoli-built-for-exchange` is entirely about why the exchange surface
    # has the shape it has. Teaching adaptation before the student knows what
    # the parts ARE is the order that makes adaptation sound like decoration.
    "KS3.B.GAS.01": [
        ("a", "The structure and functions of the human gas exchange system: "
              "the parts air passes through, and what each one does.", "B4"),
        ("b", "Adaptations of the gas exchange surface to its function: why "
              "the alveoli have the surface, thinness and blood supply they "
              "have.", "B4"),
    ],
    # Minted for B5 (2026-08-16, MRB-244). The bullet reads:
    #   "reproduction in humans (as an example of a mammal), including the
    #    structure and function of the male and female reproductive systems,
    #    menstrual cycle (without details of hormones), gametes, fertilisation,
    #    gestation and birth, to include the effect of maternal lifestyle on
    #    the foetus through the placenta"
    # The longest bullet in the KS3 biology spine. It does not need
    # interpreting to split — it prints its own clause list, and B5's five
    # human lessons are that list in that order.
    "KS3.B.REP.01": [
        ("a", "The structure and function of the male and female reproductive "
              "systems.", "B5"),
        ("b", "Gametes and fertilisation.", "B5"),
        ("c", "The menstrual cycle, without details of hormones.", "B5"),
        ("d", "Gestation and birth.", "B5"),
        ("e", "The effect of maternal lifestyle on the foetus through the "
              "placenta.", "B5"),
    ],
    # Minted for B5 (2026-08-16, MRB-244). The bullet reads:
    #   "reproduction in plants, including flower structure, wind and insect
    #    pollination, fertilisation, seed and fruit formation and dispersal,
    #    including quantitative investigation of some dispersal mechanisms"
    # Three lessons, and again the bullet prints the seams itself.
    #
    # ⚑ FLAGGED FOR MIDE — the STATUTORY GAP is inside clause `c`, and it is
    # recorded here rather than hidden by the split. The bullet asks for a
    # "quantitative investigation of some dispersal mechanisms"; Design's
    # `seed-dispersal` is a CLASSIFY lesson in which the student measures
    # nothing. The clause is deliberately minted at the bullet's full width —
    # including the quantitative words — so that what is missing is legible
    # against what is claimed. Narrowing `c` to drop those words would make
    # the register read as fully covered and the gap would vanish from every
    # gate that reads it. Ruled NOT to block this build (MRB-244); Design
    # patches it later.
    "KS3.B.REP.02": [
        ("a", "Flower structure, and wind and insect pollination.", "B5"),
        ("b", "Fertilisation in plants, and seed and fruit formation.", "B5"),
        ("c", "Seed dispersal, including quantitative investigation of some "
              "dispersal mechanisms.", "B5"),
    ],
    # Minted for B6 (2026-08-16, MRB-244). The bullet reads:
    #   "the effects of recreational drugs (including substance misuse) on
    #    behaviour, health and life processes"
    # One bullet, three lessons, and B6 previously showed in the register's
    # own coverage table as 1 statement across 3 lessons (0.33 ⚠️) — the
    # warning this file exists to answer.
    #
    # ⚑ FLAGGED FOR MIDE — this split is a CURRICULUM-MAPPING CALL, not a
    # reading of the bullet's punctuation, and it is the weakest-provenance
    # mint in this file. The bullet names "recreational drugs" and "substance
    # misuse" but does not itself name alcohol or tobacco; clause `b` is
    # justified by them being the two drugs the statement's own words
    # ("behaviour, health and life processes") bite hardest on at this age,
    # not by the document naming them. The alternative is a two-way split with
    # b6-01 and b6-02 sharing clause `a`, which §4.4 rule 3 forbids.
    "KS3.B.HLTH.01": [
        ("a", "What a recreational drug is, and how one acts on behaviour, "
              "health and life processes once it is in the blood.", "B6"),
        ("b", "The effects of alcohol and of tobacco smoke on behaviour, "
              "health and life processes.", "B6"),
        ("c", "Substance misuse: its effects, and how a claim made about a "
              "drug is judged as evidence.", "B6"),
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
