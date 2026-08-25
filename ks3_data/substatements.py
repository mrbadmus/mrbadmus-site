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
    # Minted for B8 (2026-08-17, MRB-248). The bullet reads:
    #   "the process of anaerobic respiration in humans and micro-organisms,
    #    including fermentation, and a word summary for anaerobic respiration"
    # It names TWO organisms' worth of the same process, and B8 is written at
    # that grain because the two are not the same lesson: the human clause is
    # about a body that has run out of oxygen and must pay it back, and the
    # micro-organism clause is about a process we deliberately RUN — in a
    # brewery, a yoghurt maker and an industrial fermenter — with no debt to
    # repay at all. Teaching them together makes fermentation look like a
    # failure state, which is exactly the misconception b8-04's bench exists to
    # confront (its open, stirred yeast vessel is not an error message, it is
    # how yeast is manufactured).
    #
    # The word summary named at the end of the bullet is not a third clause —
    # it is the product of the process, and it lands with (a), where the
    # equation is first written.
    "KS3.B.RESP.03": [
        ("a", "Anaerobic respiration in humans: what a muscle does when the "
              "oxygen supply cannot keep up, and a word summary for it.",
         "B8"),
        ("b", "Anaerobic respiration in micro-organisms, including "
              "fermentation and what we use it for.", "B8"),
    ],
    # Minted for B9 (2026-08-17, MRB-248). The bullet reads:
    #   "the interdependence of organisms in an ecosystem, including food webs
    #    and insect pollinated crops"
    # It names one idea and two worked examples of it, and B9 spends four of its
    # six lessons on them. Splitting three ways would have been tidier and would
    # have DROPPED a clause the bullet names out loud — "insect pollinated
    # crops" — so it splits four.
    #
    # The seam between (b) and (c) is worth naming because it is not obvious.
    # (b) is two populations that each change the other, which is a relationship
    # a student can hold in one hand. (c) is what happens when a species is
    # taken OUT, and its whole point is that the effect does not stop at the
    # links you can draw — b9-03's bench puts bees in the web with no feeding
    # line at all and removing them still empties it. That is a different claim
    # about interdependence, not a longer version of the same one.
    "KS3.B.ECO.01": [
        ("a", "Interdependence shown as food chains and food webs: who eats "
              "whom, and what happens to the energy along the way.", "B9"),
        ("b", "Interdependence between a predator and its prey: two "
              "populations that each change the other.", "B9"),
        ("c", "What interdependence means when a web is disturbed: removing "
              "one species reaches further than the links it feeds along.",
         "B9"),
        ("d", "Insect pollinated crops as a case of interdependence.", "B9"),
    ],
    # Minted for B10 (2026-08-17, MRB-248). The bullet reads:
    #   "a simple model of chromosomes, genes and DNA in heredity, including
    #    the part played by Watson, Crick, Wilkins and Franklin in the
    #    development of the DNA model"
    # A MODEL and the HISTORY OF ARRIVING AT IT are two lessons in every scheme
    # of work, and B10 writes them as two: b10-02 nests person → cell → nucleus
    # → chromosome → gene → bases, and b10-03 rebuilds the 1952 argument from
    # four pieces of evidence with the bench opening on Pauling's wrong triple
    # helix.
    #
    # ⚑ (b) is the only statutory clause in the key stage that names PEOPLE.
    # That is why b10-03 can mark a rung on writing a fairer acknowledgement —
    # the statutory language is "the part played by", and who played what part
    # is the thing being assessed. Flagged for Mide in the unit wrapper; it is
    # a values judgement inside a science mark and it is arguable.
    "KS3.B.INH.02": [
        ("a", "A simple model of chromosomes, genes and DNA in heredity, and "
              "how the four nest inside one another.", "B10"),
        ("b", "The part played by Watson, Crick, Wilkins and Franklin in "
              "developing the DNA model, and how the evidence settled it.",
         "B10"),
    ],
    # Minted for B11 (2026-08-17, MRB-248). The bullet reads:
    #   "the variation between species and between individuals of the same
    #    species meaning some organisms compete more successfully, which can
    #    drive natural selection"
    # The bullet's own "which can drive" is the seam: everything before it is a
    # statement about a POPULATION AT ONE MOMENT — these individuals differ, and
    # some of them do better here. Everything after it is a statement about that
    # repeating over GENERATIONS until the population itself changes. b11-01
    # teaches the first with a bench whose ranking REVERSES between
    # environments; b11-02 teaches the second with a deterministic runner.
    #
    # Teaching them in one sitting is what produces the belief that an
    # individual adapts during its own life, which is the single most expensive
    # misconception in this unit.
    "KS3.B.INH.05": [
        ("a", "Variation between and within species meaning some organisms "
              "compete more successfully — and that which variation helps "
              "depends on where the organism is.", "B11"),
        ("b", "How that difference in competitive success, repeated over "
              "generations, drives natural selection.", "B11"),
    ],
    # Minted for C4 (2026-08-20, MRB-246). The bullet reads:
    #   "conservation of mass changes of state and chemical reactions"
    # ⚖️ RULED (MRB-246), answering NOTES-C4 §1's referencing question. Design
    # asked whether `c4-04 mass-in-a-reaction` may REFERENCE a statement C2
    # already owns, without double-counting. It may not — validate() rule 3
    # requires non-empty `covers` on every authored lesson, so "reference and
    # own nothing" is not a shape this build has. The alternative Design
    # offered was folding the lesson into C2 and losing the four-part
    # quantitative treatment, which is the worse trade: MRB-204's treatment is
    # the point of a QUANTITATIVE lesson, and mass in a REACTION belongs in the
    # reactions unit.
    #
    # So the bullet is split instead, and it splits cleanly, because it names
    # its two contexts out loud: changes of state, and chemical reactions.
    # `c2-06 conservation-of-mass` establishes the principle where nothing new
    # is made — clause `a`. `c4-04 mass-in-a-reaction` carries it into the case
    # where something is — clause `b` — and weighs it.
    #
    # ⚠️ c2-06's `covers` NARROWED from the parent to clause `a` as part of this
    # ruling. It is the only edit this unit makes to another unit's lesson, and
    # it changes no student-facing byte: c2-06 still teaches both contexts, as
    # it always did. `covers` records which lesson is ANSWERABLE for a clause,
    # never which lesson is allowed to mention it.
    "KS3.C.AEC.04": [
        ("a", "Conservation of mass in changes of state: melting, boiling, "
              "freezing and condensing rearrange particles without changing "
              "how much matter there is.", "C2"),
        ("b", "Conservation of mass in chemical reactions: the total mass of "
              "the products equals the total mass of the reactants, including "
              "when a gas escapes or joins from the air.", "C4"),
    ],
    # Minted for C3 (2026-08-20, MRB-272). The bullet reads:
    #   "mixtures, including dissolving"
    # The bullet's own "including" is the seam, and it is the same seam
    # NOTES-C3 §1 splits on: what a mixture IS, and then the one kind of
    # mixture the statutory wording singles out. Teaching both in one sitting
    # is what produces students who think dissolving is the definition of
    # mixing — a student who has only met sugar in tea does not recognise air,
    # sea water or a rock as mixtures at all.
    "KS3.C.PIS.02": [
        ("a", "Mixtures: two or more substances together but not chemically "
              "joined, in any proportion, and separable again without a "
              "reaction.", "C3"),
        ("b", "Dissolving, and what a solution is — the kind of mixture the "
              "bullet names.", "C3"),
    ],
    # Minted for C3 (2026-08-20, MRB-272). The bullet reads:
    #   "simple techniques for separating mixtures: filtration, evaporation,
    #    distillation and chromatography"
    # ⚠️ THIS BULLET NAMES ITS OWN CLAUSES, IN ORDER, AND C3 GIVES EACH ONE A
    # LESSON. The sub-IDs are allocated in the order the bullet prints them,
    # which is also the order the unit teaches them.
    #
    # The alternative — one "separating mixtures" lesson owning the parent —
    # is what §4.2 calls two lessons wearing one title, and here it would be
    # four. Each technique has its own apparatus, its own failure modes and
    # its own answer to "what can this one separate that the last one could
    # not", which is the thread the unit is actually built on.
    #
    # These four are minted for the BOOKKEEPING, not to make a claim about
    # what may be repeated: a fact taught in four lessons is taught four
    # times on purpose. What `covers` records is which lesson is answerable
    # for a clause, and four techniques have four answerable lessons.
    "KS3.C.PIS.04": [
        ("a", "Filtration: separating an insoluble solid from a liquid.",
         "C3"),
        ("b", "Evaporation and crystallisation: recovering a dissolved solid "
              "from its solution.", "C3"),
        ("c", "Distillation: recovering the solvent, or separating liquids "
              "by boiling point.", "C3"),
        ("d", "Chromatography: separating substances dissolved in the same "
              "solvent from each other.", "C3"),
    ],
    # Minted for C4 (2026-08-20, MRB-246). The bullet reads:
    #   "chemical reactions as the rearrangement of atoms"
    # Two teachable ideas, and NOTES-C4 §1 splits on the seam between them:
    # deciding whether a change is a reaction AT ALL, and then what a reaction
    # turns out to be underneath. A student who meets both in one sitting
    # learns "chemical change = irreversible", which is the misconception
    # `REACT-01` exists to break — the recognition half has to be taught, and
    # taught wrong-first, before the rearrangement half can land.
    "KS3.C.CR.01": [
        ("a", "What counts as a chemical reaction: a change that makes one or "
              "more new substances, as distinct from a physical change, which "
              "does not.", "C4"),
        ("b", "Chemical reactions as the rearrangement of atoms: the atoms "
              "present afterwards are the same atoms, regrouped — none is "
              "made, destroyed or turned into another kind.", "C4"),
    ],
    # Minted for C4 (2026-08-20, MRB-246). The bullet reads:
    #   "representing chemical reactions using formulae and using equations"
    # The bullet's own "and" is the seam. NOTES-C4 §1 splits it the way AEC.03
    # was split and for the same reason: a word equation is a SENTENCE, and a
    # symbol equation is a MODEL WITH NUMBERS IN IT. The students who meet them
    # together learn that a formula is a longer name.
    #
    # ⚠️ The formula-writing half of "using formulae" is C2's `KS3.C.AEC.03b`
    # and is NOT re-owned here. What clause `b` owns is representing a
    # REACTION with them — the equation, and the balancing that makes it one.
    "KS3.C.CR.02": [
        ("a", "Representing a chemical reaction as a word equation: reactants, "
              "an arrow that means 'becomes', and products.", "C4"),
        ("b", "Representing a chemical reaction with formulae, as a balanced "
              "symbol equation.", "C4"),
    ],
    # Minted for C5 (2026-08-20, MRB-246). The bullet reads:
    #   "combustion, thermal decomposition, oxidation and displacement
    #    reactions"
    # ⚠️ THIS BULLET NAMES ITS OWN CLAUSES, IN ORDER, exactly as PIS.04 does,
    # and C5 gives each one a lesson. Clauses a–d are allocated in the order
    # the bullet prints them.
    #
    # ⚖️ CLAUSE `e` IS A COMMANDER'S RULING (MRB-246) AND IT IS THE ONE ENTRY
    # IN THIS FILE THAT IS NOT A PHRASE OF ITS BULLET. It is minted because
    # `c5-05 which-reaction-is-this` teaches the bullet as a SET rather than
    # any member of it, and the three legal alternatives were all worse:
    #
    #   · Own the parent alongside a–d — forbidden by validate() rule 5, and
    #     rightly: a parent and its clause both owned double-counts.
    #   · Own one of a–d jointly with that type's own lesson — forbidden by
    #     rule 4, and it would make one of the four answerable twice while the
    #     discrimination lesson is answerable for nothing.
    #   · Declare it `beyond_statutory` — FALSE. §7.6 means off-spec content,
    #     and telling the four apart is not off-spec; it is what the bullet
    #     actually demands and what an exam actually asks.
    #
    # NOTES-C5 §1 makes the argument and it is ratified here: naming four types
    # is not the same as telling them apart, and four lessons that each never
    # meet the other three do not add up to the bullet. The clause is worded as
    # the bullet's integrative demand, not as a fifth reaction type — there is
    # no fifth type, and clause `e` must never be read as claiming one.
    "KS3.C.CR.03": [
        ("a", "Combustion: a substance reacting with oxygen, releasing energy, "
              "and what changes when the oxygen supply is limited.", "C5"),
        ("b", "Thermal decomposition: one substance broken down by heating "
              "into two or more, and not reassembling on cooling.", "C5"),
        ("c", "Oxidation: a substance gaining oxygen, including corrosion, and "
              "the conditions it needs.", "C5"),
        ("d", "Displacement: a more reactive metal taking the place of a less "
              "reactive one in its compound.", "C5"),
        ("e", "Telling the four named types apart: deciding, for a given "
              "reaction, which of them it is — including where more than one "
              "name is right, and where none of the four applies.", "C5"),
    ],
    # Minted for C6 (2026-08-21, MRB-272). The bullet reads:
    #   "reactions of acids with alkalis to produce a salt plus water"
    # ONE bullet with two demands in it, and the seam is the word "produce".
    # Design's NOTES-C6 §1 splits on exactly that seam: `neutralisation`
    # establishes the reaction and the point at which it is complete;
    # `making-a-pure-dry-salt` turns it into a preparation with an excess, a
    # filtration and a crystallisation.
    #
    # ⚖️ Clause `b` is minted on the same reasoning that minted `KS3.C.CR.03e`
    # and `KS3.C.ENER.02c`: the lesson teaches a demand of the bullet that is
    # not the reaction itself, and all three legal alternatives are worse.
    # Owning the parent alongside `a` is forbidden by `validate()` rule 5;
    # sharing `a` with `c6-03` is forbidden by rule 4; and `beyond_statutory`
    # is simply false — "to produce" is a word in the bullet, and getting a
    # pure dry sample out of the beaker is what it asks for.
    #
    # ⚠️ Clause `b` must never be read as a second reaction. There is one
    # reaction and clause `a` owns it. `b` is the preparation, and `c6-06`'s
    # six-step method is the bullet's "produce" made into something a student
    # can be assessed on.
    "KS3.C.CR.07": [
        ("a", "Neutralisation as the reaction of an acid with a base: the "
              "word equation, the salt and water it always makes, and the "
              "single point at which the acid is exactly used up.", "C6"),
        ("b", "PRODUCING a named salt as a pure, dry solid: reacting the acid "
              "with an excess of an insoluble base, filtering off what is "
              "left, and crystallising rather than drying.", "C6"),
    ],
    # Minted for C7 (2026-08-21, MRB-272). The bullet reads:
    #   "exothermic and endothermic chemical reactions (qualitative)"
    # ONE bullet naming TWO opposite behaviours, claimed by THREE lessons.
    # Design's NOTES-C7 §1 gives the split and the reason: "the split into a
    # PROCESS lesson and a CONTRAST lesson is the only way to give the
    # endothermic case a hook of its own — otherwise it arrives as a footnote
    # to exothermic and stays one."
    #
    # ⚖️ Clauses `a` and `b` are the bullet's own two phrases. Clause `c` is
    # NOT, and it is minted on exactly the reasoning that minted `KS3.C.CR.03e`
    # above: `c7-04` teaches the bullet as a MEASUREMENT rather than as either
    # member of it, and all three legal alternatives are worse. Owning the
    # parent alongside a and b is forbidden by `validate()` rule 5; sharing a
    # clause with `c7-02` or `c7-03` is forbidden by rule 4; and
    # `beyond_statutory` is simply false — "(qualitative)" is the word in the
    # bullet that MAKES the measurement lesson statutory rather than off-spec.
    # A temperature change is how a KS3 student decides which of the two a
    # reaction is, and a lesson on reading it is the bullet's own demand.
    #
    # ⚠️ Clause `c` must never be read as a THIRD kind of energy change. There
    # are two. It is the bullet's evidential demand: how the decision between
    # a and b is actually made, and how badly a leaking beaker can make it.
    # ── C8, minted 21 Aug 2026 (MRB-281) ────────────────────────────────
    #
    # `KS3.C.PT.03` prints TWO ideas separated by a semicolon and every scheme
    # teaches them as two lessons: where a square IS, and what KIND of thing
    # sits in it. Clause order is the bullet's own printed order.
    "KS3.C.PT.03": [
        ("a", "The table's address system: periods run across and groups run "
              "down, an element's position is read off both, and elements in "
              "one group are a family that behaves alike.", "C8"),
        ("b", "The metal / non-metal divide as the table's other partition, "
              "and where the line between them falls.", "C8"),
    ],

    # `KS3.C.PT.04` is ONE sentence and is split anyway, which needs saying.
    #
    # It is not split by EXAMPLE — "group 1, group 7, group 0" would be three
    # instances of one idea, and rule 1 would not license that. It is split by
    # the PREDICTIVE MOVE, and the three are genuinely different skills that a
    # student can hold any one of without the others:
    #
    #   a  read a trend off a group and extend it to a member you have not met
    #   b  recognise that the DIRECTION of a group's trend is a property of the
    #      group, not of the table, and that it can run the other way
    #   c  predict from structure rather than from a trend at all — a full
    #      outer shell explains behaviour with no series to extrapolate along
    #
    # ⚖️ The arithmetic forced the question and the reading answered it. Three
    # lessons each need non-empty `covers` (§10.2) and PT.04 is the only
    # statement any of them teaches, so ownership had to reach clause grain.
    # But a split that could only be justified by the arithmetic would be a
    # split by example wearing clause clothes, and it would be `touches` —
    # the ungated field — that was really wanted. These three survive without
    # the arithmetic, which is why they are minted rather than fudged.
    "KS3.C.PT.04": [
        ("a", "Reading a trend off a group and extending it to a member of "
              "that group you have not met, using the position of the outer "
              "electron to say why the trend runs the way it does.", "C8"),
        ("b", "That the DIRECTION of a group's trend belongs to the group and "
              "not to the table: a second group whose reactivity runs the "
              "opposite way, and the same mechanism explaining both.", "C8"),
        ("c", "Predicting from structure rather than from a trend: a full "
              "outer shell accounting for behaviour where there is no series "
              "to extrapolate along, and placing an unknown element from its "
              "address alone.", "C8"),
    ],

    # ── C10, minted 22 Aug 2026 (MRB-281) ───────────────────────────────
    #
    # The bullet reads "the rock cycle and the formation of igneous,
    # sedimentary and metamorphic rocks". It carries two ideas that every
    # scheme of work teaches a week apart, and `structure.py` reserved two
    # slots for them long before either was authored: `c10-02` makes the three
    # rock types and `c10-03` runs the cycle. The ruling is recorded in full
    # in `ks3_data/c10/__init__.py`; these are the rows it said would land
    # with the lessons.
    #
    # ⚠️ BOTH CLAUSES ARE MINTED IN ONE PASS, and only `a` has a lesson today.
    # Rule 3 is about not big-banging a whole register ahead of any need, not
    # about splitting one bullet in half twice: a bullet split at `a` alone
    # would leave the parent partly owned and partly not, which rule 2 is
    # written to prevent. `b` is registered ahead of `the-rock-cycle` in
    # exactly the sense `CELL-09`–`12` are registered ahead of their lesson,
    # and no gate treats an unowned clause as a failure.
    "KS3.C.EA.03": [
        ("a", "The formation of igneous, sedimentary and metamorphic rocks: "
              "the three routes by which rock is made, and the evidence in a "
              "sample that says which route it took.", "C10"),
        ("b", "The rock cycle: the processes that carry material from one of "
              "those three groups into another, and the fact that the route "
              "has no beginning and no end.", "C10"),
    ],

    "KS3.C.ENER.02": [
        ("a", "Exothermic changes: energy transferred out to the "
              "surroundings, so the temperature of the mixture rises, and the "
              "energy was stored in the chemicals beforehand.", "C7"),
        ("b", "Endothermic changes: energy taken in from the surroundings, so "
              "the temperature falls — and reversing a change reverses the "
              "direction of the transfer.", "C7"),
        ("c", "Deciding which of the two a reaction is by MEASURING the "
              "temperature change: what to record, what to keep the same, and "
              "what heat loss does to the number you end up with.", "C7"),
    ],
    # Minted for P1 (2026-08-24). The bullet reads:
    #   "comparing the starting with the final conditions of a system and
    #    describing increases and decreases in the amounts of energy
    #    associated with movements, temperatures, changes in positions in a
    #    field, in elastic distortions and in chemical compositions"
    # Two separable teaching ideas, and Design draws them as two lessons: the
    # LIST of places energy can sit, then the COMPARISON of one moment with
    # another. `p1-01` cannot teach the comparison, because the word transfer
    # is not defined until `p1-02`.
    "KS3.P.CIS.02": [
        ("a", "The set of energy stores: movement, temperature, position in "
              "a field, elastic distortion and chemical composition — "
              "what a store is, and which situations fill which.", "P1"),
        ("b", "Comparing the starting with the final conditions of a system, "
              "and describing which stores increased and which decreased.",
         "P1"),
    ],
    # Minted for P1 (2026-08-24). The bullet reads:
    #   "heating and thermal equilibrium: temperature difference between 2
    #    objects leading to energy transfer from the hotter to the cooler
    #    one, through contact (conduction) or radiation; such transfers
    #    tending to reduce the temperature difference; use of insulators"
    # This is the compound bullet named in this file's own opening paragraph
    # as the example of the problem — four genuinely separable ideas, taught
    # as four lessons by every scheme of work and by Design's delivery.
    "KS3.P.ECT.02": [
        ("a", "Heating and thermal equilibrium: a temperature difference "
              "drives energy from the hotter object to the cooler one, and "
              "the transfer tends to reduce the difference until it "
              "stops.", "P1"),
        ("b", "Transfer through contact — conduction.", "P1"),
        ("c", "Transfer by radiation, including across a vacuum.", "P1"),
        ("d", "The use of insulators to slow a transfer down.", "P1"),
    ],
    # ── Minted for P4 (2026-08-24, MRB-223) ───────────────────────────────
    #
    # ⚑ THIS IS THE NOTATION DESIGN'S `NOTES-P4-P6.md` FLAG 1 ASKS FOR, AND
    # IT ALREADY EXISTED. Her flag reads: *"the register records ownership per
    # statement, per unit … Either the register needs `.a` / `.b` sub-IDs or
    # lesson records need a `covers_partial` field. Until then a build gate
    # counting statements per lesson will read `FORCES.04` as claimed three
    # times."*
    #
    # She was right about the defect and right about the fix, and she could
    # not see that the fix was already in the tree — her access was read-only
    # and this file is not in the reference set she was given. The gate did
    # read FORCES.02 as double-owned and FORCES.04 as triple-owned on the
    # first P4 build, exactly as she predicted. **No new mechanism was
    # invented; rule 3 above was followed — mint lazily, per unit, at
    # authoring time.**
    #
    # The bullet reads:
    #   "using force arrows in diagrams, adding forces in 1 dimension,
    #    balanced and unbalanced forces"
    # Three clauses, and P4 teaches them as two lessons: p4-02 owns the
    # drawing and the adding, p4-03 owns the balanced/unbalanced contrast.
    "KS3.P.FORCES.02": [
        ("a", "Using force arrows in diagrams: an arrow's start, direction "
              "and length as the record of a force.", "P4"),
        ("b", "Adding forces in one dimension to give a resultant.", "P4"),
        ("c", "Balanced and unbalanced forces.", "P4"),
    ],
    # The bullet reads:
    #   "forces: associated with deforming objects; stretching and squashing
    #    – springs; with rubbing and friction between surfaces, with pushing
    #    things out of the way; resistance to motion of air and water"
    # Four genuinely separate practicals, and P4 is written at that grain:
    # p4-05 owns friction, p4-06 owns resistance, p4-08 owns deformation.
    # This is the bullet the gate read as claimed three times.
    "KS3.P.FORCES.04": [
        ("a", "Forces associated with deforming objects: stretching and "
              "squashing, springs.", "P4"),
        ("b", "Forces with rubbing and friction between surfaces.", "P4"),
        ("c", "Forces with pushing things out of the way: resistance to "
              "motion of air and water.", "P4"),
    ],
    # The bullet reads:
    #   "forces measured in newtons, measurements of stretch or compression
    #    as force is changed"
    # Two ideas taught weeks apart: the UNIT, which p4-03 needs the moment it
    # says a table pushes back with 8 N, and the MEASUREMENT SERIES, which is
    # p4-08's whole investigation.
    "KS3.P.FORCES.05": [
        ("a", "Forces measured in newtons.", "P4"),
        ("b", "Measurements of stretch or compression as force is changed.",
         "P4"),
    ],
    # ── Minted for P5 (2026-08-24, MRB-223) ───────────────────────────────
    #
    # The bullet reads:
    #   "pressure in liquids, increasing with depth; upthrust effects,
    #    floating and sinking"
    # Two different physical ideas in one line, and P5 is written at that
    # grain: p5-02 owns what depth does to the pressure, p5-03 owns what the
    # pressure difference does to an object in it. Design's own note says the
    # split "has to be", and it is the only one of P5's three bullets that
    # needs one — the unit has four slots for three statements, so nothing
    # else is under pressure to divide.
    "KS3.P.PRES.02": [
        ("a", "Pressure in liquids, increasing with depth.", "P5"),
        ("b", "Upthrust effects, floating and sinking.", "P5"),
    ],
    # ── P6 · Waves and sound ────────────────────────────────────────────
    #
    # Three of P6's six statements are compound and are split at the clause;
    # SND.02, SND.04 and EAW.01 are whole and take no sub-IDs. Minted lazily,
    # per unit, at authoring time — rule 3 above — and for the same reason
    # P4's were: nine lessons over six statements is the surplus case, and
    # without the split the coverage gate reads three of them as claimed
    # twice.
    #
    # The bullet reads:
    #   "waves on water as undulations which travel through water with
    #    transverse motion; these waves can be reflected, and add or cancel
    #    – superposition"
    # Three clauses, and P6 teaches them as two lessons: p6-01 owns what a
    # wave IS, p6-02 owns what two of them do when they meet.
    "KS3.P.OBW.01": [
        ("a", "Waves on water as undulations which travel through water "
              "with transverse motion.", "P6"),
        ("b", "These waves can be reflected.", "P6"),
        ("c", "These waves add or cancel — superposition.", "P6"),
    ],
    # The bullet reads:
    #   "frequencies of sound waves, measured in hertz (Hz); echoes,
    #    reflection and absorption of sound"
    # Two clauses that are four lessons apart in any scheme of work: p6-05
    # owns the hertz, p6-07 owns the echo.
    "KS3.P.SND.01": [
        ("a", "Frequencies of sound waves, measured in hertz (Hz).", "P6"),
        ("b", "Echoes, reflection and absorption of sound.", "P6"),
    ],
    # The bullet reads:
    #   "sound produced by vibrations of objects, in loudspeakers, detected
    #    by their effects on microphone diaphragm and the ear drum; sound
    #    waves are longitudinal"
    # Production, detection and longitudinality are three separate lessons'
    # worth. p6-03 owns the first two — they are one chain and teaching them
    # apart would break it — and p6-04 owns the third.
    "KS3.P.SND.03": [
        ("a", "Sound produced by vibrations of objects, and in "
              "loudspeakers.", "P6"),
        ("b", "Sound detected by its effects on a microphone diaphragm and "
              "on the ear drum.", "P6"),
        ("c", "Sound waves are longitudinal.", "P6"),
    ],
    # ── P7 · Light ──────────────────────────────────────────────────────
    #
    # Six statements over seven slots (ratio 0.86) — the surplus case again,
    # and the reason three of the six are split is Design's own §2 table:
    # `LGT.04` alone is claimed by FOUR lessons, which without a notation the
    # coverage gate reads as one statement owned four times. `LGT.01`,
    # `LGT.02` and `LGT.05` are whole and take no sub-IDs.
    #
    # The bullet reads:
    #   "the transmission of light through materials: absorption, diffuse
    #    scattering and specular reflection at a surface"
    # Two clauses, and P7 teaches them two lessons apart: p7-02 owns what a
    # surface does to the light it sends BACK, p7-07 owns what it does to the
    # light it keeps. The clause order here follows the split rather than the
    # bullet's own word order, because scattering and specular reflection are
    # one lesson's idea and absorption is another's.
    "KS3.P.LGT.03": [
        ("a", "The transmission of light through materials: diffuse "
              "scattering and specular reflection at a surface.", "P7"),
        ("b", "Absorption of light at a surface.", "P7"),
    ],
    # The bullet reads:
    #   "use of ray model to explain imaging in mirrors, the pinhole camera,
    #    the refraction of light and action of convex lens in focusing
    #    (qualitative); the human eye"
    # Four separate lessons' worth, and the widest split in the key stage:
    # p7-02 owns the mirror, p7-03 owns refraction, p7-04 owns the pinhole and
    # the convex lens together — they are one argument, the bargain and the
    # thing that refuses it — and p7-05 owns the eye.
    "KS3.P.LGT.04": [
        ("a", "Use of the ray model to explain imaging in mirrors.", "P7"),
        ("b", "The refraction of light.", "P7"),
        ("c", "The pinhole camera, and the action of a convex lens in "
              "focusing (qualitative).", "P7"),
        ("d", "The human eye.", "P7"),
    ],
    # The bullet reads:
    #   "colours and the different frequencies of light, white light and
    #    prisms (qualitative only); differential colour effects in absorption
    #    and diffuse reflection"
    # Two clauses and two lessons: p7-06 establishes that white light is a
    # mixture sorted by frequency, p7-07 uses that to explain what a coloured
    # surface does. Design's §4 records that neither depends on the other.
    "KS3.P.LGT.06": [
        ("a", "Colours and the different frequencies of light; white light "
              "and prisms (qualitative only).", "P7"),
        ("b", "Differential colour effects in absorption and diffuse "
              "reflection.", "P7"),
    ],
    # ── P8 · Electric circuits ──────────────────────────────────────────
    #
    # P8 is the most surplus-slot unit in physics: THREE statements over
    # SEVEN lessons, a ratio of 0.43. Design's `NOTES-P8-P9.md` FLAG 1 is the
    # third repeat of the flag P4 and P6 already answered — *"a gate counting
    # statements per lesson will read `CUR.01` as claimed three times"* — and
    # she is right that it would. She could not see that the notation exists,
    # because this file is not in the read-only reference set she works from.
    #
    # Minted lazily, per unit, at authoring time (rule 3 above). `CUR.03` is
    # whole and takes no sub-IDs; `p8-07` owns no subject-content clause at
    # all (her FLAG 2) and claims a Working Scientifically statement instead,
    # which §5.7 exempts from the exactly-once rule.
    #
    # The bullet reads:
    #   "electric current, measured in amperes, in circuits, series and
    #    parallel circuits, currents add where branches meet and current as
    #    flow of charge"
    # Three clauses, and P8 teaches them as three lessons: p8-01 owns what a
    # current IS and the loop it needs, p8-02 owns the two arrangements,
    # p8-03 owns what happens where branches meet.
    "KS3.P.CUR.01": [
        ("a", "Electric current, measured in amperes, in circuits; current "
              "as a flow of charge.", "P8"),
        ("b", "Series and parallel circuits.", "P8"),
        ("c", "Currents add where branches meet.", "P8"),
    ],
    # The bullet reads:
    #   "potential difference, measured in volts, battery and bulb ratings;
    #    resistance, measured in ohms, as the ratio of potential difference
    #    (p.d.) to current"
    # Two clauses and two lessons. The semicolon in the source is doing the
    # dividing: what a p.d. IS and what a rating means is p8-04's, and the
    # RATIO that defines resistance is p8-05's whole subject.
    "KS3.P.CUR.02": [
        ("a", "Potential difference, measured in volts; battery and bulb "
              "ratings.", "P8"),
        ("b", "Resistance, measured in ohms, as the ratio of potential "
              "difference (p.d.) to current.", "P8"),
    ],
    # ── P9 · Static electricity ─────────────────────────────────────────
    #
    # P9 owns two statements over three slots (ratio 0.67) — the surplus case
    # again, and Design's own §2 table splits the compound one at the clause.
    # `STAT.02` is whole and takes no sub-ID: *the idea of* an electric field
    # is one lesson's worth and `p9-03` owns all of it.
    #
    # ⚑ Her `NOTES-P8-P9.md` FLAG 1 asks for this notation for the third time
    # in the physics run ("the register needs `.a` / `.b` sub-IDs, or lesson
    # records need `covers_partial`"). It already existed, and she could not
    # see it: her access is read-only and this file is not in the reference
    # set she was given. Same answer as P4's and P6's — mint lazily, per unit,
    # at authoring time.
    #
    # The bullet reads:
    #   "separation of positive or negative charges when objects are rubbed
    #    together: transfer of electrons, forces between charged objects"
    # Two clauses and two lessons: `p9-01` owns HOW an object becomes charged,
    # `p9-02` owns what two charged objects then do to each other. Splitting
    # them is not a convenience — a page that taught both would have to teach
    # induction as an aside, and induction is the whole second half of
    # `p9-02`.
    "KS3.P.STAT.01": [
        ("a", "Separation of positive or negative charges when objects are "
              "rubbed together: transfer of electrons.", "P9"),
        ("b", "Forces between charged objects.", "P9"),
    ],
    # Minted for P10 (MRB-223, 2026-08-25). The bullet reads:
    #   "the magnetic effect of a current, electromagnets, D.C. motors
    #    (principles only)"
    # Three clauses and two lessons, and the split falls at the second comma
    # because the first two clauses are one idea: a current makes a field, and
    # an electromagnet is what you build out of that. The motor is a different
    # fact — the field pushing BACK on a current — and it needs nothing from
    # the electromagnet lesson except the sentence `a current makes a field`,
    # which `p10-05` restates in one clause of its own so a school running the
    # unit in another order strands nobody.
    #
    # ⚑ Minted because Design's NOTES §1 claims `MAG.04` for `p10-04` AND for
    # `p10-05` and records that as needing no notation. Under §4.4 rule 3 it
    # does: `covers` is exactly-once across the key stage and `verify_ks3`
    # asserts it, so a second claim on the parent is a build failure rather
    # than a duplicate. This is the compound-bullet case this file exists for
    # and it needs no ruling from Mide — the two lessons are already in
    # `structure.py` as separate slots.
    "KS3.P.MAG.04": [
        ("a", "The magnetic effect of a current, and electromagnets.", "P10"),
        ("b", "D.C. motors, principles only.", "P10"),
    ],
    # ── P12 · Space ─────────────────────────────────────────────────────
    #
    # P12 owns four statements over six slots (ratio 1.5) — the surplus case
    # at its widest in physics, and the compound bullet is the one that has
    # to give. `SPACE.02`, `.03` and `.04` are whole and take no sub-ID: the
    # Sun/stars/galaxies, the seasons and the light year are one lesson's
    # worth each and `p12-04`, `p12-05` and `p12-06` own all of them.
    #
    # The bullet reads:
    #   "gravity force, weight = mass x gravitational field strength (g), on
    #    Earth g=10 N/kg, different on other planets and stars; gravity forces
    #    between Earth and Moon, and between Earth and sun (qualitative only)"
    #
    # THREE clauses, and they are three lessons in every scheme of work:
    #
    #   a  what weight IS and how it is calculated where you are standing;
    #   b  that g — and so weight — travels while mass does not;
    #   c  gravity between bodies nobody is standing on, qualitatively.
    #
    # Splitting them is not a convenience. A page that carried (a) and (b)
    # together would have to introduce the mass/weight contrast as an aside,
    # and that contrast IS `p12-02` — Design's own README calls the
    # gram-to-kilogram trap "where the distinction between mass and weight is
    # actually lost". And (c) is qualitative where the first two are
    # quantitative, so it takes no formula block at all; folding it into
    # either would put a calculation beside a statement the bullet marks
    # "qualitative only".
    "KS3.P.SPACE.01": [
        ("a", "The force of gravity, and weight = mass × gravitational field "
              "strength with g = 10 N/kg on Earth.", "P12"),
        ("b", "g, and so weight, differs on other planets and stars while "
              "mass does not.", "P12"),
        ("c", "Gravity forces between Earth and Moon, and between Earth and "
              "Sun, qualitatively.", "P12"),
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
