"""C6 — Acids and alkalis. Seven lessons, Year 8 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c6/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c6/`) under MRB-220.

── SEVEN LESSONS AGAINST SEVEN SLOTS AND SEVEN DRAWINGS ────────────────

⊖ **SUPERSEDED 23 Aug 2026 (MRB-281).** The retirement ruling below is kept
rather than deleted, because it is a ruling and because the paragraph that
replaces it only makes sense beside it.

> ⚠️ **SIX LESSONS AGAINST SEVEN SLOTS AND SEVEN DRAWINGS, AND THE GAP IS A
> RULING.** `structure.py`'s fifth C6 slot is `acid-plus-alkali`; Design drew
> `c6-05-acids-and-carbonates` there instead and flagged the divergence
> herself in NOTES-C6 §2 with "Ruling wanted" — her case being that acid +
> carbonate is the third of the three acid reaction families and carries the
> limewater test, her case against being that it is not in §7 and owns no
> statutory statement.
>
> The commander ruled: build the six slots where the drawing and the skeleton
> agree, author nothing for the seventh. `structure.py` is not edited by a
> unit module and was not edited by this one, and the unauthored slot renders
> an honest coming-soon page — the structure-first guarantee (§11 decision 8).
>
> If the ruling is ever revisited, the limewater test needs a home; NOTES-C6
> §2 suggests C10-02.

**Mide overrode it on 23 Aug 2026: `acids-and-carbonates` is built, in this
unit, and the limewater test lives here rather than in C10-02.** Design's case
carried — it is the third of the three acid reaction families, and without it
the unit teaches two reactions of acids and calls it a set.

Three things about HOW it was built, because each is easy to get wrong:

  · **The fifth slot was RENAMED in place**, from `acid-plus-alkali` /
    "Acid + alkali: making a salt" to `acids-and-carbonates` / "Acids and
    carbonates". No eighth tuple was inserted. `acid-plus-alkali` could never
    legally have been authored — its topic is owned twice already by
    `neutralisation` (`CR.07a`) and `making-a-pure-dry-salt` (`CR.07b`) — so
    keeping it alongside would have left an un-fillable coming-soon ghost at
    position 5 permanently.
  · **Nothing below it moved and the key stage is still 185 slots.** Positions
    6 and 7 were already `making-a-pure-dry-salt` and `catalysts`; the phantom
    was already counted. Renaming an unauthored slot to something real does
    not add a slot.
  · **It owns no statutory statement and mints none.** See the next section.

── FIVE BULLETS, SEVEN LESSONS, ONE MINTED PAIR AND ONE EXEMPTION ──────

C6 owns `KS3.C.CR.04` through `CR.08`:

    CR.04  defining acids and alkalis in terms of neutralisation reactions
    CR.05  the pH scale for measuring acidity/alkalinity; and indicators
    CR.06  reactions of acids with metals to produce a salt plus hydrogen
    CR.07  reactions of acids with alkalis to produce a salt plus water
    CR.08  what catalysts do

Five into six does not go, and `validate()` binds from both sides: rule 3 fails
an authored lesson with an empty `covers`, rule 4 fails a statement owned twice.
The architecture's mechanism for exactly this is `substatements.py` — the same
one that turned `KS3.C.CR.03` into five clauses for C5 and `KS3.C.ENER.02` into
three for C7 — and Design's own NOTES-C6 §1 already describes the split it
needs: *"`CR.07` is split across two lessons on purpose: `neutralisation`
establishes the equation and the pH curve, `making-a-salt` turns it into a
preparation with a filtration step."*

So the allocation is:

    acids-and-alkalis            CR.04
    the-ph-scale-and-indicators  CR.05
    neutralisation               CR.07a   (+ touches CR.04)
    acid-plus-metal              CR.06
    acids-and-carbonates         none — beyond_statutory (see below)
    making-a-pure-dry-salt       CR.07b
    catalysts                    CR.08

⚠️ **`acids-and-carbonates` MINTS NOTHING, AND MUST NOT.** None of C6's five
statements mentions carbonates, carbon dioxide, or the reaction of an acid
with either — `CR.06` is metals and hydrogen, `CR.07` is alkalis and water.
`CR.07a`/`CR.07b` are legitimate because they split `CR.07`'s OWN text across
two lessons that are both about acid + alkali; a `CR.06c` or `CR.07c` here
would be different in kind, because acid + carbonate is chemically neither of
its parents. The clause would misstate the National Curriculum, and a statutory
id is permanent — "an ID never changes meaning ... a re-mint is a breaking
change" (`docs/ks3/statutory-register.md`). Design's own §2 agrees: "it owns no
statutory statement."

So it takes §7.6's OTHER legal shape, all three legs enforced by
`validate()` rule 3: `beyond_statutory: True`, `covers: []`, `ks4_links`
non-empty (`chemistry/chemical-changes/reactions-of-acids`, which resolves).
Nothing enters the coverage register and `docs/ks3/statutory-register.md`
gains no row — it is generated from the DfE source and is never hand-edited.

⚑ This revives a pattern Mide closed under MRB-199, where two off-spec B1
lessons were REMOVED rather than kept as `beyond_statutory`. That gate is
scoped to B1 and does not bind here, and the product call to keep this lesson
in this unit is his own and freshly made; the tension is recorded in full in
`ks3_data/c6/lesson_05_acids_and_carbonates.py`'s docstring rather than
buried.

⚠️ **`CR.07a` AND `CR.07b` DO NOT EXIST IN `ks3_data/substatements.py` YET.**
The commander's brief for this unit forbade minting clauses and that file is
the commander's, so the block that mints them is written out for splicing
rather than applied here. Without it the build fails naming both ids; with it,
both rules pass. See `making-a-pure-dry-salt`'s docstring for the full
reasoning and for why the two legal alternatives — an empty `covers`, or a
`beyond_statutory` declaration — are respectively a worse failure and a false
statement.

**Repetition across lessons is right and is NOT the same as double ownership.**
`neutralisation` teaches the definition `CR.04` is about and says so in
`touches`, which is not an ownership claim and is not gated. `CR.04` is owned
once, by the lesson that defines the two words.

── TEN INSTRUMENT FAMILIES, ONE DRAWN FIGURE, SIXTEEN PLACEMENTS ───────

    bottle-sorter     c6-01 #s-bench
    acid-judgements   c6-01 #s-hazard · c6-02 #s-choose · c6-03 #s-uses ·
                      c6-04 #s-test · c6-05 #s-world · c6-07 #s-uses
    ph-strip (ART)    c6-02 #s-scale
    ph-bench          c6-02 #s-bench
    titration-dial    c6-03 #s-titrate
    acid-metal-grid   c6-04 #s-bench
    step-rig          c6-05 #s-rig
    solid-sorter      c6-05 #s-bench
    salt-namer        c6-06 #s-name
    method-order      c6-06 #s-method
    catalyst-bench    c6-07 #s-bench

`acid-judgements` is one family placed six times, because Design draws the
identical component on six of the seven pages: a question, a small set of
options, one commitment, one answer. §6's warning about repeated block lineups
is answered the way C5 answered it — the FLAGSHIP of every page is different,
and this is the small second instrument beside each of them.

⚠️ `acid-metal-grid` is NOT `reactivity-grid`. Design's NOTES-C6 §4 reuses
C5-04's name and `ks3_art/c5.py` owns it, together with the shell class
`ks3-rgrid-block`. Two families wearing one shell class puts one unit's
stylesheet on the other unit's instrument, silently, which is what MRB-279's
gate exists to catch.

── THE UNIT ASSUMES C5 THROUGHOUT ──────────────────────────────────────

Every reaction here is written as a word equation, `acid-plus-metal` argues from
the reactivity series, and `catalysts` closes on a reaction that cannot be sped
up because it cannot happen. A student who has not met `displacement` can read
the pages; a student who has not met "a reaction makes new substances" cannot.
"""

from .c6 import lessons as _c6_lessons

UNIT = {
    "code":            "C6",
    "slug":            "acids-and-alkalis",
    "title":           "Acids and alkalis",
    "discipline":      "chemistry",
    "statutory_area":  "Chemical reactions",
    "typical_year":    8,
    "split_rationale": "Eight statutory bullets spanning representation, "
                       "reaction types and acid chemistry; universally taught "
                       "as separate units and too large to schedule as one.",
    "intro":           "An acid and an alkali are not things you can see, "
                       "weigh or smell. They are things a substance does — to "
                       "a dye, to a metal, to each other — and this unit is "
                       "about reading those behaviours, predicting them, and "
                       "using them on purpose.",
    "lessons": _c6_lessons(),
}
