"""C6 — Acids and alkalis. Six lessons, Year 8 Chemistry.

The thin unit wrapper. The lesson records live one per module under
`ks3_data/c6/`, authored against Claude Design's approved reference screens
(`docs/ks3/design-reference/c6/`) under MRB-220.

⚠️ **SIX LESSONS AGAINST SEVEN SLOTS AND SEVEN DRAWINGS, AND THE GAP IS A
RULING.** `structure.py`'s fifth C6 slot is `acid-plus-alkali`; Design drew
`c6-05-acids-and-carbonates` there instead and flagged the divergence herself in
NOTES-C6 §2 with "Ruling wanted" — her case being that acid + carbonate is the
third of the three acid reaction families and carries the limewater test, her
case against being that it is not in §7 and owns no statutory statement.

The commander ruled: build the six slots where the drawing and the skeleton
agree, author nothing for the seventh. `structure.py` is not edited by a unit
module and was not edited by this one, and the unauthored slot renders an
honest coming-soon page — the structure-first guarantee (§11 decision 8).

If the ruling is ever revisited, the limewater test needs a home; NOTES-C6 §2
suggests C10-02.

── FIVE BULLETS, SIX LESSONS, AND ONE MINTED PAIR ──────────────────────

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
    making-a-pure-dry-salt       CR.07b
    catalysts                    CR.08

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

── EIGHT INSTRUMENT FAMILIES, ONE DRAWN FIGURE, THIRTEEN PLACEMENTS ────

    bottle-sorter     c6-01 #s-bench
    acid-judgements   c6-01 #s-hazard · c6-02 #s-choose · c6-03 #s-uses ·
                      c6-04 #s-test · c6-07 #s-uses
    ph-strip (ART)    c6-02 #s-scale
    ph-bench          c6-02 #s-bench
    titration-dial    c6-03 #s-titrate
    acid-metal-grid   c6-04 #s-bench
    salt-namer        c6-06 #s-name
    method-order      c6-06 #s-method
    catalyst-bench    c6-07 #s-bench

`acid-judgements` is one family placed five times, because Design draws the
identical component on five of the six pages: a question, a small set of
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
