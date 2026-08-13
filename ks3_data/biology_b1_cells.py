"""B1 — Cells and organisation. Six lessons, Year 7 Biology.

⊖ **Authored as eight; six survive.** `stem-cells-and-meristems` and
`enzymes-and-rate` were removed on 2026-08-12 under MRB-199, ruled by Mide as
examiner: neither owned a statutory statement. The catalyst clause enzymes would
have carried, `KS3.B.NUT.04`, is already owned by B3's `enzymes-in-digestion`
slot, so the slot was dropped outright rather than moved — two lessons competing
for one ownable statement is the defect MRB-199 exists to close. Enzyme *rate*
(optimum temperature, denaturing, the shape of the curve) has no KS3 statutory
home at all and belongs in §7.6's Year 9 bridge unit when that is built.

Both authored bodies survive in git history on `design/b1-content`. The prose
below still describes the unit as eight lessons in places, and the ⚑ flags for
L7 and L8 still stand as written; that text is a record of what was authored and
reviewed, not a description of what this file now emits, and it is deliberately
left intact rather than rewritten to make the ledger agree retroactively.

Authored against the ten laws (§5.0), the segment vocabulary (§5.1.1), the
family grammar (§6) and the per-lesson done-list (§10.2). Same shape as
`chemistry_c1_particles.py`, which is the only worked example that existed when
this was written.

**Why this unit, and what it is a pattern for.** Two of its families — `SYSTEM`
and `CLASSIFY` — had never been rendered with real content anywhere in the
course. Between them they carry 47 of the 185 lessons. The shapes chosen here
are therefore not local decisions; they are the first draft of the pattern for
all 47, and they are called out as such below.

**review_state is `draft` on every lesson.** Mide is the sole science gate
(§5.10). Every ⚑ below is a science or scope call for him, raised here rather
than hedged in the prose where he would have to guess whether it was meant.

──────────────────────────────────────────────────────────────────────────
STATUTORY ALLOCATION — six statements, eight lessons
──────────────────────────────────────────────────────────────────────────

    L1 life-processes            KS3.B.CELLS.01a
    L2 using-a-microscope        KS3.WS.EXP.05 + KS3.B.CELLS.01b
    L3 animal-and-plant-cells    KS3.B.CELLS.02, KS3.B.CELLS.03
    L4 specialised-cells         KS3.B.CELLS.04
    L5 levels-of-organisation    KS3.B.CELLS.06
    L6 unicellular-organisms     KS3.B.CELLS.05
    L7 stem-cells-and-meristems  — none. beyond_statutory: True
    L8 enzymes-and-rate          — none. beyond_statutory: True

Every subject clause is owned exactly once (§4.4). One bullet needed splitting;
nothing else did.

**The `KS3.B.CELLS.01` split** (§11 decision 11, minted lazily per rule 3 of
`substatements.py`). The bullet reads *"cells as the fundamental unit of living
organisms, including how to observe, interpret and record cell structure using
a light microscope"* — two genuinely separable teaching ideas which every scheme
of work teaches a week apart. Add to `SUBSTATEMENTS`:

    "KS3.B.CELLS.01": [
        ("a", "Cells as the fundamental unit of living organisms: everything "
              "alive is built from cells, and nothing else is.", "B1"),
        ("b", "How to observe, interpret and record cell structure using a "
              "light microscope.", "B1"),
    ],

`KS3.B.CELLS.06` was NOT split. It was tempting to give `specialised-cells` a
clause of it ("cells specialised for a job, as the base of the hierarchy") so
that every lesson held a statement of its own, but the hierarchy bullet is one
idea and `levels-of-organisation` teaches all of it. Splitting a bullet to
relieve an allocation squeeze is how a register stops meaning anything.

⚑ **FLAG 1 — L2 owns a subject statement as well as a WS one.** §5.7.1 says an
INVESTIGATION lesson "usually owns none" and adds one "only if the lesson
genuinely owns it and no other lesson does". `KS3.B.CELLS.01b` is *how to
observe, interpret and record cell structure using a light microscope* — that is
the entire lesson, and no other lesson in KS3 teaches it. Both halves of the
rule are met, but this is the first INVESTIGATION lesson to use clause 3 and it
should be confirmed rather than assumed.

⚑ **FLAG 2 — B1 contains two lessons with no statutory home, and this needs a
ruling.** `stem-cells-and-meristems` and `enzymes-and-rate` are in §7's topic
map and in `structure.py`, and neither teaches anything in the 2014 programme of
study. Stem cells appear nowhere in KS3. Enzymes appear once, parenthetically,
inside `KS3.B.NUT.04` — *"(enzymes simply as biological catalysts)"* — which B3
owns and needs, and B3 is already short of statements for its lesson count.

§10.2 leaves exactly two legal shapes: `covers` non-empty, or
`beyond_statutory: True` with `covers` empty and `ks4_links` non-empty. The
second is the honest one, so both lessons are authored that way and both point
at real, resolving KS4 pages. Note that §7.6 *already assumes B1 teaches enzyme
rate* — XB1's bridge lesson is justified by "B1 teaches enzyme rate
descriptively; GCSE wants the model and the pH/temperature curve" — so this is a
gap in the coverage record, not a scope change.

Two consequences for Mide, both mechanical:

1. Under §7.6 rule 5 these become the **first two entries in
   `docs/ks3/bridge-register.md`**, which does not exist yet. They are not in a
   bridge *unit*: their URLs are `/ks3/biology/cells-and-organisation/…` and say
   nothing about a bridge, which §7.6's URL rule assumes they would. Recommend
   the register gains a column distinguishing *bridge-unit lesson* from
   *beyond-statutory lesson inside a KS3 unit*, rather than moving the lessons —
   moving them would change the 185-lesson scope, which is not an authoring
   decision.
2. Both are placed **last in the unit**, after every statutory lesson, so a
   school that stops at the statutory content loses nothing and nothing earlier
   depends on them.

⚑ **FLAG 3 — `beyond_statutory` is absent from every C1 lesson.** §4.8 lists it
as a canonical field and §10.2 says "absent is a defect". It is present and
explicit on all eight lessons here, including the six where it is `False`. C1
predates the field; worth a sweep.

──────────────────────────────────────────────────────────────────────────
MISCONCEPTIONS — two families opened, one existing ID re-used
──────────────────────────────────────────────────────────────────────────

Fifteen new entries, plus one re-use. Register rows are in
`docs/ks3/b1-review-pack.md` ready to paste; they are not invented here and
then left for someone else to transcribe.

- **`LIFE`** — what counts as living, and the life processes. `LIFE-01` … `-03`.
- **`CELL`** — cells, microscopy and the organisation of living things.
  `CELL-01` … `-12`.

**`PART-10` is re-used, not re-minted.** L4's second misconception is *"something
has to push the particles along"* wearing a biological costume: students write
"the heart pushes the oxygen into the muscle cell". The register already
predicted this reappearance (it names B1 under `PART-10`/`PART-11`), so the ID
travels with the idea and L4 says out loud that this is the same wrong answer
they met in chemistry. The `statement` field is copied **verbatim** from the
register; only `elicited_by` and `confronted_by` are local.

The register predicted the reappearance in `animal-and-plant-cells`. It lands in
`specialised-cells` instead, because that is where `KS3.B.CELLS.04` is owned and
where diffusion does visible work. `reappears_in` needs that one-word edit.

⚑ **FLAG 4 — `CELL-11` and `CELL-12` are enzyme misconceptions parked in a cell
family**, exactly as `PART-12`/`PART-13` are nature-of-science misconceptions
parked in a particle family. Opening an `ENZ` family for two entries in a
beyond-statutory lesson would be worse. If B3 `enzymes-in-digestion` and C6
`catalysts` later want one, the ruling on `PART-12`/`PART-13` applies unchanged:
these two do not move, and the register carries a cross-reference.

──────────────────────────────────────────────────────────────────────────
INSTRUMENTS — two new kinds, one re-used across a discipline boundary
──────────────────────────────────────────────────────────────────────────

`build_ks3.py:r_sim()` **fails the build** on an unknown sim kind, so declaring
one is a hard dependency, not a wish. Two are declared, and both are used more
than once — a bespoke instrument per lesson is not a plan that survives 185
lessons.

**Both are now MRB-198**, ticketed 10 Aug 2026, and the contract is the one
specced in `B1 Instrument Spec` — controls, readouts, payload shape, aria-labels
and locked/reduced-motion states. These eight lessons are authored against that
contract as built.

    lesson                     flagship              mid-size
    L1 life-processes          classify drill        —            (no new build)
    L2 using-a-microscope      microscope   ⊕NEW     Law 5 pair
    L3 animal-and-plant-cells  system-parts ⊕NEW     reveal-cards
    L4 specialised-cells       system-parts ⊕NEW     diffusion  ← C1's, re-used
    L5 levels-of-organisation  system-parts ⊕NEW     classify drill
    L6 unicellular-organisms   microscope   ⊕NEW     reveal-cards
    L7 stem-cells-and-meristems  Law 5 pair          investigation (no new build)
    L8 enzymes-and-rate        Law 5 pair            investigation (no new build)

**`diffusion` is re-used from C1 with no changes at all** — same component, same
controls, and the dashed centre line reads as the cell membrane. A Year 7 meets
the identical instrument in chemistry and then in biology, which is the whole
argument of the misconception register made visible.

**⊕ NEW `microscope`** — L2 flagship, L6 flagship. What it must do:

    controls   specimen · magnification · focus
    readouts   total magnification · field of view · what you can see
    payload    "specimens": [...]  — the slides this lesson offers, in order

    Turning the magnification up shrinks the field of view and throws the image
    out of focus until focus is corrected: that is the entire teaching point of
    L2 and it cannot be a frame swap (Law 9). Focus racks through the depth of
    the specimen, so a thick slide can never be sharp all at once.

    aria-label (the canvas is a blank rectangle to a screen reader — this is the
    only description a non-sighted student gets, so it narrates the mechanism):
    "Animation: the view down a light microscope. Turning the magnification up
    makes everything larger but shows a smaller circle of the slide, and the
    image blurs until the focus is corrected. Turning the focus moves down
    through the thickness of the specimen, so different layers come sharp in
    turn. The readout below the animation gives the total magnification and the
    width of the field of view in words."

**⊕ NEW `system-parts`** — L3, L4, L5. The `SYSTEM` family's flagship is
perturbation, never labelling (§6), and there was no instrument for it. This is
the one that matters most: it is the pattern for all 47 SYSTEM and CLASSIFY
lessons, so it is authored as a **payload-driven** component rather than three
bespoke ones.

    controls   part            — a part selector, not a slider
    readouts   what still works · what has stopped
    payload    "parts": [{"id", "name", "job", "needs": [ids]}, ...]

    Switching a part off animates the failure propagating along the `needs`
    edges, one step at a time, so the student watches the knock-on rather than
    reading it. Reduced motion (R6): the end state is drawn immediately and the
    written readout carries the whole result.

    aria-label:
    "Animation: a set of labelled parts that work together. Switching one part
    off makes every part that depends on it stop in turn, spreading outwards
    from the part that was switched off. The readout below the animation lists
    what still works and what has stopped, in words."

⚑ **FLAG 5 — `SIM_CONTROLS` needs four new names, and it is part of MRB-198.**
It is currently `("temperature", "volume", "particles", "medium")` and `r_sim()`
validates against it, so `specimen`, `magnification`, `focus` and `part` must be
added there and given labels in `shared/ks3.js:CONTROL_LABELS`. Five of the eight
lessons will not render until they are. Recorded here so the constant is not
forgotten behind the two components — it is the cheap half of the ticket and the
half that fails loudest.

⚑ **FLAG 6 — no `rate-curve` instrument was declared, and L8 wants one.** A
MODEL lesson should have a flagship parameter instrument (§6) and
`enzymes-and-rate` is the one lesson here that does not. It leans on a declared
graph figure plus a Law 5 read-the-curve pair instead. Two blocking components
is already the limit for one unit, and the same instrument would serve B7
`rate-of-photosynthesis`, C6 `catalysts` and C7 `measuring-a-temperature-change`
— so it is worth designing once, for a unit that needs it more, rather than
bolting it on here.

⚑ **FLAG 7 — the schema has nowhere to put a stepper's steps.** §6 says a
PROCESS lesson leads with a "worked stepper with predict-gates", and the only
authored `worked-example` in the course (C1's `mass-fifa`) is a calculation, so
`fifa` carried it. L7's mechanism is not a calculation. Its steps are numbered
inside the `prompt`, which renders correctly today; a `steps` field would render
better and every PROCESS lesson after this one will want it. Recommended, not
assumed — nothing here depends on it.

──────────────────────────────────────────────────────────────────────────
FIGURES — 21 declared, all `needed`, and a new kind
──────────────────────────────────────────────────────────────────────────

MRB-103's anatomical-diagram gap is this unit, and it is declared rather than
written around: cells, specialised cells and levels of organisation all want real
diagrams and none exist. Thirteen schematics, five micrographs, two apparatus,
one graph — and the diagram manifest goes from 11 figures to 32.

⚑ **FLAG 8 — a new figure kind, `micrograph`, and it is NOT the photography
ticket.** Five figures here are photographs taken down a microscope. The
manifest's existing kinds are `schematic`, `apparatus` and `graph`, and its
standing warning is that a photograph does not substitute for a schematic. This
is the inverse case and it is worth being explicit about: **a schematic does not
substitute for a micrograph either.** L2's entire lesson is that the real view is
disappointing — perfect circles that turn out to be air bubbles — and a tidy
drawing of onion cells would destroy it. These are also **not** the Platform
Backlog photography ticket: that ticket is real-life photography of apparatus and
context; these are photographs through an objective lens, of named specimens, at
stated magnifications. Three sourcing efforts, not two, and none substitutes for
another.

──────────────────────────────────────────────────────────────────────────
SCIENCE FLAGS — every claim Mide should look at twice
──────────────────────────────────────────────────────────────────────────

⚑ 9  **"All seven life processes, with no exceptions" (L1).** The KS3 rule is
      taught as an all-or-nothing test, because a test that accepts "most of
      them" cannot exclude a candle flame. The confrontation is worded so the
      rule survives the obvious objections — a resting seed, a mule — by saying a
      living thing has the *equipment* for all seven even when it is not using
      it. Confirm that wording.
⚑ 10 **Numbers used as facts.** "About thirty trillion cells" (unit intro),
      "about four months" for a red blood cell and "two million new ones every
      second" (L4), "×10 eyepiece × ×40 objective = ×400" (L2). All are standard,
      all are checkable, none is decorative.
⚑ 11 **Osmosis is deliberately never named** (L3 vacuole, L6 contractile
      vacuole, L4 root hair cell). It is not in the KS3 programme of study. Water
      movement is described — "water seeps in and the vacuole squeezes it back
      out", "root hair cells take in water and minerals" — without naming the
      mechanism, and the root hair cell is never given as an example of
      diffusion, because it is not one.
⚑ 12 **Bacteria have no nucleus** (L6 stretch). Standard KS3 practice and needed
      to make `KS3.B.CELLS.05`'s "structural adaptations" honest, but the words
      prokaryote and eukaryote are KS4 and are not used.
⚑ 13 **"Warmer particles meet more often"** (L8). This is collision theory in
      Year 7 clothing, and collision theory is an XC1 bridge lesson. It is said
      in one sentence, without the name, because the upward half of the enzyme
      curve is otherwise magic. Cut it if you would rather it waited.
⚑ 14 **Enzyme shape** (L8, `b1-enzyme-shape`). "The enzyme has a shape that fits
      what it works on; heat changes that shape permanently" — the KS3 treatment,
      stopping short of lock-and-key, which XB1 owns.
⚑ 15 **A virus does one life process and only inside another cell** (L1
      stretch). Genuinely beyond the programme of study, in an opt-in stretch
      block, and it is the question every Year 7 asks the moment they meet the
      seven processes. Ruling wanted, not a quiet ship.
⚑ 16 **Bone marrow, and why a cut heals but a finger does not regrow** (L7).
      Beyond the programme of study, inside a beyond-statutory lesson.

Prose runs 137–242 words per lesson against the 450 ceiling (§5.2); the first
commitment in every lesson lands inside the opening ~90 words (Law 2), and no
single explainer exceeds 91.
"""

UNIT = {
    "code":            "B1",
    "slug":            "cells-and-organisation",
    "title":           "Cells and organisation",
    "discipline":      "biology",
    "statutory_area":  "Structure and function of living organisms",
    "split_rationale": None,
    "intro":           "You are built from about thirty trillion cells, and not "
                       "one of them knows you exist. This unit starts by asking "
                       "what makes something alive at all, goes down to a single "
                       "cell, and comes back up to a whole organism.",
    "lessons": [

# ══════════════════════════════════════════════════════════════════════════
# L1 — Life processes and what living things are made of (CLASSIFY)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "life-processes",
    "title":       "Life processes and what living things are made of",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "CLASSIFY",

    "covers":      ["KS3.B.CELLS.01a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    "requires":    [],
    "assumes":     [],
    "references":  [],
    # Deliberately empty (§10.2). The seven life processes are assumed
    # knowledge at GCSE rather than taught anywhere, so there is no KS4 page
    # to point at. Naming one that only half-fits would be worse than none.
    "ks4_links":   [],

    "big_question": "What makes something alive?",

    "phenomenon": {
        "kind": "demo",
        "title": "Three dishes on the bench",
        "prompt": "Dish one holds a dry seed. It has not moved or changed in a "
                  "year. Dish two holds a crystal sitting in salty water: it is "
                  "growing, and it is making more shapes exactly like itself. "
                  "Dish three holds yeast in warm sugar water, frothing hard.",
        "commit": "One of these three is not alive. Which one?",
    },

    "misconceptions": [
        {"id": "LIFE-01",
         "statement": "If something moves on its own it must be alive, and if it "
                      "never moves it must not be.",
         "elicited_by": "three-dishes-vote",
         "confronted_by": "seed-or-crystal"},
        {"id": "LIFE-02",
         "statement": "Doing one of the life processes is enough to count as "
                      "alive — if it grows on its own, it is alive.",
         "elicited_by": "crystal-check",
         "confronted_by": "seven-out-of-seven"},
    ],

    "vocabulary": [
        {"term": "organism",
         "definition": "A single living thing.",
         "note": "One organism can be one cell, or trillions of them working "
                 "together. You will meet both in this unit."},
        {"term": "cell",
         "definition": "The smallest living unit, and the thing every living "
                       "thing is built from.",
         "note": None},
        {"term": "life process",
         "definition": "One of the seven jobs that every living thing does.",
         "note": "The seven are movement, respiration, sensitivity, growth, "
                 "reproduction, excretion and nutrition. Many people remember "
                 "them by the first letters: MRS GREN."},
    ],

    "figures": [
        {"id": "b1-three-dishes", "kind": "apparatus",
         "caption": "Three dishes side by side: a dry seed, a crystal growing in "
                    "salty water, and yeast frothing in sugar water.",
         "status": "needed"},
        {"id": "b1-everything-is-cells", "kind": "micrograph",
         "caption": "Three specimens at the same magnification — a leaf, human "
                    "skin and pond water — each one made of cells.",
         "status": "needed"},
    ],

    # CLASSIFY rhythm (§6): lead → decision instrument (commit, then watch it
    # resolve) → the reference table → classification drills at rising stakes →
    # ladder, ending with the rule in the student's own words. The hook is
    # wagered on at block 2 and answered at block 3.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "three-dishes-vote"},
        {"type": "explainer", "id": "why-the-crystal-is-out",
         "text": "Here is the answer. The crystal is the one that is not alive. "
                 "It grows, and it does make more shapes like itself, so it "
                 "passes two of the tests. It never feeds, it never senses "
                 "anything, and it never gets rid of waste. Living things pass "
                 "all seven tests, not two. The seed is alive but resting — its "
                 "life processes have slowed almost to nothing, and water starts "
                 "them again. The yeast is alive and busy. The froth is a waste "
                 "gas it is giving off."},
        {"type": "figure", "ref": "b1-three-dishes"},
        {"type": "misconception", "id": "seed-or-crystal", "targets": "LIFE-01"},
        {"type": "check", "id": "crystal-check"},
        {"type": "misconception", "id": "seven-out-of-seven", "targets": "LIFE-02"},
        {"type": "keyword", "terms": ["organism", "cell", "life process"]},
        {"type": "check", "id": "mrs-gren-cards"},
        {"type": "practical", "id": "living-sorter"},
        {"type": "explainer", "id": "made-of-cells",
         "text": "So the seven tests sort the living from the rest. Now the "
                 "other half of the question: what are living things actually "
                 "made of? Cut a leaf thin enough, put it under a microscope, "
                 "and you find boxes. Do the same with your own skin. Do the "
                 "same with a drop of pond water. Every time, boxes. We call "
                 "them cells. Everything alive is built from them, and nothing "
                 "else is. That is the real reason the crystal was never in the "
                 "running."},
        {"type": "figure", "ref": "b1-everything-is-cells"},
        {"type": "check", "id": "flame-explain"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "the-argument-about-viruses",
         "text": "One thing does not fit the test, and scientists still argue "
                 "about it. A virus does exactly one of the seven processes — it "
                 "reproduces — and it can only do that inside somebody else's "
                 "cell. On its own it does nothing at all. It is not made of "
                 "cells either. So most scientists say a virus is not alive, and "
                 "some say the test is the thing that needs changing."},
        {"type": "check", "id": "virus-verdict"},
    ],

    "support": [],   # slot present, content deferred — §11 decision 4

    "activities": [
        {"id": "three-dishes-vote", "kind": "predict",
         "demand": "elicit LIFE-01 by forcing a commitment on the hook",
         "prompt": "Commit before anyone explains it. Which of the three is not "
                   "alive?",
         "options": ["The seed — it has not moved or changed all year",
                     "The crystal — it grows, but only in the salty water",
                     "The yeast — froth is a chemical reaction, not a life sign"],
         "answer": 1,
         "reveal": "The crystal. Both the others are alive — and the reason the "
                   "crystal is out has nothing to do with whether it moves. The "
                   "next block gives the real test.",
         "targets": "LIFE-01"},
        {"id": "seed-or-crystal", "kind": "confrontation",
         "demand": "make the wrongness of LIFE-01 visible",
         "prompt": "Here is the idea to kill, in the words students really "
                   "write: 'the seed is dead because it never moves.' Put the "
                   "seed and the crystal next to each other. The crystal is the "
                   "one that moved, grew and copied itself. The seed did "
                   "nothing at all.",
         "reveal": "And the crystal is the dead one. Movement is one test out of "
                   "seven, and it is the least useful of them. A seed is alive, "
                   "sitting still, with everything it needs to do all seven the "
                   "moment it gets water. Plenty of living things stay still for "
                   "months. Plenty of dead things move.",
         "targets": "LIFE-01"},
        {"id": "crystal-check", "kind": "predict",
         "demand": "elicit LIFE-02",
         "prompt": "The crystal grew, and it made more shapes just like itself. "
                   "That is two of the seven. So how many does something have to "
                   "do before we call it alive?",
         "options": ["One is enough — growing on its own is the sign of life",
                     "Most of them — five or six of the seven will do",
                     "All seven, every one, with no exceptions"],
         "answer": 2,
         "reveal": "All seven. That is what makes the list a test instead of a "
                   "hint.",
         "targets": "LIFE-02"},
        {"id": "seven-out-of-seven", "kind": "confrontation",
         "demand": "make the wrongness of LIFE-02 visible",
         "prompt": "Say the wrong idea out loud: 'it grows by itself, so it must "
                   "be alive.' Now score the crystal on all seven. Movement: "
                   "yes, it spreads. Growth: yes. Reproduction: it makes more "
                   "shapes like itself, so call that a yes too. Nutrition: no. "
                   "Respiration: no. Sensitivity: no. Excretion: no.",
         "reveal": "Three out of seven, and it is not alive. If three were "
                   "enough, a growing crystal, a spreading fire and a rusting "
                   "nail would all be living things. That is why the test is all "
                   "seven and not most. One thing to be careful of: a living "
                   "thing counts if it has what it needs for all seven, even "
                   "when it is not using them. A resting seed is alive. A mule "
                   "that never breeds is alive. A crystal has never had the "
                   "equipment at all.",
         "targets": "LIFE-02"},
        {"id": "mrs-gren-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Seven processes, seven cards. Say the word out loud before "
                   "you tap each card — no peeking first.",
         "cards": [
             {"front": "Changing position, or moving part of yourself",
              "back": "Movement"},
             {"front": "Releasing energy from food, inside your cells",
              "back": "Respiration"},
             {"front": "Noticing a change and responding to it",
              "back": "Sensitivity"},
             {"front": "Getting permanently bigger",
              "back": "Growth"},
             {"front": "Making more of your own kind",
              "back": "Reproduction"},
             {"front": "Getting rid of the waste your own body makes",
              "back": "Excretion"},
             {"front": "Taking in the food you need",
              "back": "Nutrition"},
         ]},
        {"id": "living-sorter", "kind": "classify",
         "demand": "classify, at rising stakes",
         "prompt": "Six candidates, getting harder. For each one decide alive, "
                   "never alive, or once alive — and name the process that "
                   "settles it. A mushroom · a candle flame · a river · a coral "
                   "reef · a wooden chair · frozen bacteria in Antarctic ice.",
         "options": ["Alive", "Never alive", "Once alive"],
         "reveal": "Mushroom and coral: alive, and both catch people out because "
                   "they do not move about. The flame and the river move, grow "
                   "and even 'feed' — never alive, and never made of cells. The "
                   "chair was once alive: it is made of cells, but a tree's. The "
                   "frozen bacteria are alive and resting, exactly like the seed."},
        {"id": "flame-explain", "kind": "construct",
         "demand": "produce the rule, in the student's own words",
         "prompt": "Now say the rule yourself, on the hardest case on the list. "
                   "A candle flame moves, gets bigger, uses fuel and gives off "
                   "gas. Write the reply you would give someone who says a flame "
                   "is alive.",
         "success": ["Names at least two life processes a flame does not do",
                     "Says a living thing must do all seven, not some",
                     "Says a flame is not made of cells",
                     "Does not argue only from 'it isn't natural'"]},
        {"id": "virus-verdict", "kind": "construct",
         "demand": "transfer the rule to a case the rule struggles with",
         "prompt": "Use the test on the case that breaks it. A virus reproduces, "
                   "but only inside another living cell, and it is not made of "
                   "cells itself. Decide whether it is alive and justify your "
                   "decision against the seven.",
         "success": ["Uses the seven processes as the test, not a feeling",
                     "Notices a virus does only one of them",
                     "Notices it is not made of cells",
                     "Gives a decision and defends it, either way"]},
    ],

    "ladder": {
        "recall": {
            "q": "What is the smallest unit that every living thing is built "
                 "from?",
            "options": ["A cell", "An organ", "A tissue", "A molecule"],
            "answer": 0,
            "feedback": {
                1: "An organ is made of many cells. The cell is the smaller "
                   "unit.",
                2: "A tissue is made of many cells too. Keep going down.",
                3: "Non-living things are made of molecules as well, so that "
                   "cannot be the unit of life.",
            }},
        "apply": {
            "q": "A candle flame moves, gets bigger, takes in fuel and gives off "
                 "gas. Why is it not alive?",
            "options": ["It is far too hot for anything to be living",
                        "It was lit by a person, so it cannot be natural",
                        "It is not made of cells and it does not do all seven",
                        "It does not move about the room on its own"],
            "answer": 2,
            "feedback": {
                0: "Some organisms live in hot springs above 80 °C. "
                   "Temperature is not the test.",
                1: "Plenty of living things are started by people — every "
                   "seed a farmer sows. (LIFE-02)",
                3: "Movement is one test out of seven, and a flame does move. "
                   "(LIFE-01)",
            }},
        "explain": {
            "q": "Explain why a crystal growing in salty water is not alive, "
                 "even though it gets bigger and makes more shapes like itself.",
            "success": ["Says a living thing must do all seven life processes",
                        "Names at least two the crystal does not do",
                        "Says the crystal is not made of cells",
                        "Does not rely on 'it isn't moving' as the reason"]},
        "produce": {
            "q": "A friend says: 'my phone is alive — it takes in energy, it "
                 "responds when I touch it, and it gets hot.' Write a reply that "
                 "settles it.",
            "success": ["Agrees the phone does do one or two of the seven",
                        "Names processes it cannot do, such as growth or "
                        "reproduction",
                        "Says all seven are needed, not some",
                        "Says the phone is not made of cells"]},
    },

    "key_note": "Living things are made of cells and carry out all seven life "
                "processes: movement, respiration, sensitivity, growth, "
                "reproduction, excretion, nutrition. Two or three is not enough. "
                "A crystal grows and is still not alive; a seed sits still for a "
                "year and is alive the whole time.",

    "ws": ["scientific-attitudes"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L2 — Using a microscope (INVESTIGATION)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "using-a-microscope",
    "title":       "Using a microscope",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "INVESTIGATION",

    # WS-anchored per §5.7.1, plus one subject clause this lesson genuinely
    # owns and no other lesson teaches — see FLAG 1 in the module docstring.
    "covers":      ["KS3.WS.EXP.05", "KS3.B.CELLS.01b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 50,

    "requires":    ["life-processes"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["biology/cell-biology/microscopy"],

    "big_question": "Why does almost everybody's first slide show nothing at "
                    "all?",

    "phenomenon": {
        "kind": "data",
        # "Year 7" reworded at MRB-198 integration: R13 forbids a lesson
        # page from naming a year, and the parity gate caught these in the
        # rendered bytes. Same meaning, no year.
        "title": "A real student's slide",
        "prompt": "This is an onion slide made by a student your age, "
                  "photographed down the microscope. It is covered in perfect "
                  "round circles with thick black rims. Beside it is the drawing "
                  "they made from it, in biro, shaded in, with twelve circles "
                  "labelled 'cells'.",
        "commit": "They drew twelve cells. How many cells are actually in that "
                  "photograph?",
    },

    "misconceptions": [
        {"id": "CELL-01",
         "statement": "Those neat round circles in the field of view are the "
                      "cells.",
         "elicited_by": "count-the-cells",
         "confronted_by": "bubble-or-cell"},
        {"id": "CELL-02",
         "statement": "The highest magnification is always the best one to use, "
                      "because it shows you the most.",
         "elicited_by": "pick-a-lens",
         "confronted_by": "microscope-lab"},
    ],

    "vocabulary": [
        {"term": "specimen",
         "definition": "The thing you are looking at under the microscope.",
         "note": "It has to be thin enough for light to get through it. That is "
                 "why onion skin works and a whole onion does not."},
        {"term": "coverslip",
         "definition": "The thin square of glass laid over a specimen.",
         "note": "Lower it slowly, at an angle. Dropping it flat is what traps "
                 "the air bubbles this lesson opens with."},
        {"term": "magnification",
         "definition": "How many times bigger than real life something looks.",
         "note": "Total magnification = eyepiece × objective. A ×10 eyepiece "
                 "with a ×40 objective gives ×400."},
        {"term": "field of view",
         "definition": "The circle of the specimen you can see down the "
                       "microscope at one time.",
         "note": "Turn to a higher magnification and the field of view gets "
                 "smaller. You see more detail of less."},
    ],

    "figures": [
        {"id": "b1-bubbles-vs-cells", "kind": "micrograph",
         "caption": "The same onion slide twice: a field full of air bubbles "
                    "with thick dark rims, and a field of onion cells packed in "
                    "a brick-wall pattern.",
         "status": "needed"},
        {"id": "b1-microscope-labelled", "kind": "schematic",
         "caption": "A light microscope with the eyepiece, objective lenses, "
                    "stage, clips, light source and both focus wheels labelled.",
         "status": "needed"},
        {"id": "b1-drawing-standards", "kind": "schematic",
         "caption": "Two drawings of the same onion cells: one shaded, in biro, "
                    "with crossing label lines; one in sharp pencil with straight "
                    "ruled labels and no shading.",
         "status": "needed"},
    ],

    # INVESTIGATION rhythm (§6): lead with a flawed piece of work → critique
    # before construct → run it and get an awkward result → analyse → ladder
    # ending in a method the student writes. The hook is wagered at block 2 and
    # answered at block 3.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "count-the-cells"},
        {"type": "explainer", "id": "bubbles-not-cells",
         "text": "None. Not one circle in that photograph is a cell. Every one "
                 "of them is an air bubble. A bubble is perfectly round, has a "
                 "thick dark rim, and sits on its own with space around it. An "
                 "onion cell is a brick with straight sides, and cells are "
                 "packed together in rows with no gaps at all. Bubbles get under "
                 "the coverslip when it is dropped flat instead of lowered "
                 "slowly at an angle. So the first skill here is not looking. It "
                 "is making a slide worth looking at."},
        {"type": "figure", "ref": "b1-bubbles-vs-cells"},
        {"type": "misconception", "id": "bubble-or-cell", "targets": "CELL-01"},
        {"type": "keyword", "terms": ["specimen", "coverslip", "magnification",
                                      "field of view"]},
        {"type": "figure", "ref": "b1-microscope-labelled"},
        {"type": "check", "id": "pick-a-lens"},
        {"type": "practical", "id": "microscope-lab"},
        {"type": "explainer", "id": "what-magnification-costs",
         "text": "So a higher magnification never shows you more. It shows you "
                 "more detail of less. Every step up shrinks the circle you can "
                 "see and throws the picture out of focus until you correct it. "
                 "That is why you always start on the lowest lens, find "
                 "something worth looking at, put it in the middle, and only "
                 "then turn up. Start on the highest and you are hunting for a "
                 "cell through a keyhole."},
        {"type": "worked-example", "id": "magnification-fifa"},
        {"type": "check", "id": "magnification-fifa-do"},
        {"type": "check", "id": "critique-the-drawing"},
        {"type": "figure", "ref": "b1-drawing-standards"},
        {"type": "check", "id": "draw-your-own"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "how-small-is-a-cell",
         "text": "You can work out how big a cell is without any special "
                 "equipment. Measure the field of view once, then count how many "
                 "cells fit across it. Six onion cells across a field 1.8 mm "
                 "wide makes each cell about 0.3 mm. A cheek cell is around "
                 "0.06 mm — five times smaller. A bacterium is smaller again, "
                 "and a school microscope will never show you one properly."},
        {"type": "check", "id": "estimate-cell-size"},
    ],

    "support": [],

    "activities": [
        {"id": "count-the-cells", "kind": "predict",
         "demand": "elicit CELL-01 by forcing a commitment on the hook",
         "prompt": "Commit to a number before you read on. How many onion cells "
                   "are in that photograph?",
         "options": ["Twelve — the twelve circles they drew and labelled",
                     "About thirty — the twelve circles and the fainter ones",
                     "None — not one of those circles is a cell"],
         "answer": 2,
         "reveal": "None of them. The next block says what they actually are, "
                   "and how to tell in one second.",
         "targets": "CELL-01"},
        {"id": "bubble-or-cell", "kind": "confrontation",
         "demand": "make the wrongness of CELL-01 visible",
         "prompt": "The wrong idea, in the words students really write: 'the "
                   "cells are the round circles.' So test it. Onion cells are "
                   "packed together in rows, like bricks in a wall, with no gaps "
                   "between them. Look at the photograph again and ask what is "
                   "in the gaps between the circles.",
         "reveal": "Nothing is, because they are not packed at all — they are "
                   "floating separately with clear space around them, and real "
                   "cells never do that. Perfectly round, thick dark rim, "
                   "floating alone: air bubble. Straight sides, packed in rows, "
                   "thin outline: cell. Once you have seen the difference once "
                   "you cannot unsee it.",
         "targets": "CELL-01"},
        {"id": "pick-a-lens", "kind": "predict",
         "demand": "elicit CELL-02",
         "prompt": "You have a good field of onion cells at ×100. You turn the "
                   "nosepiece round to the ×40 objective, giving ×400. Predict "
                   "what you will see.",
         "options": ["The same cells, four times bigger, all still in view",
                     "A much smaller piece of the slide, and it will need "
                     "refocusing",
                     "Nothing at all — ×400 is too high for onion cells"],
         "answer": 1,
         "reveal": "A much smaller piece, and it goes blurry until you correct "
                   "the focus. Run it yourself in the lab below before you "
                   "believe it.",
         "targets": "CELL-02"},
        {"id": "microscope-lab", "kind": "lab",
         "demand": "investigate",
         "prompt": "The wrong idea, out loud first: 'use the highest lens, it "
                   "shows you the most.' Predict before you run it — you are "
                   "hunting for one cell on a slide you have not seen before. "
                   "Which lens should you start on?",
         "options": ["The highest — it shows the most detail straight away",
                     "The lowest — the widest circle of slide is in view",
                     "It makes no difference which one you start on"],
         "answer": 1,
         "sim": {"kind": "microscope",
                 "controls": ["specimen", "magnification", "focus"],
                 "readouts": ["total magnification", "field of view",
                              "what you can see"],
                 "specimens": ["onion skin — well made",
                               "onion skin — coverslip dropped flat",
                               "human cheek cells"],
                 "caption": "Three slides, two of them onion. Start on the "
                            "lowest lens and turn up. Watch the field of view "
                            "reading as you do."},
         "reveal": "The lowest. At ×40 the whole slide is nearly in view and you "
                   "can find something in seconds; at ×400 you are looking "
                   "through a keyhole and could miss a cell by a hair. Now put "
                   "the badly made slide on and compare the two onion slides at "
                   "the same magnification — same onion, same lens, and only one "
                   "of them shows you a cell.",
         "targets": "CELL-02"},
        {"id": "magnification-fifa", "kind": "worked-example",
         "demand": "model the calculation before asking for it (Law 5)",
         "prompt": "Watch this one set out in full, because you do the next one. "
                   "A microscope has a ×10 eyepiece. The objective lens in use "
                   "is ×40. What is the total magnification?",
         "fifa": {
             "formula": "total magnification = eyepiece × objective",
             "insert":  "total magnification = 10 × 40",
             "fix":     "both numbers are magnifications, so the answer has no "
                        "unit — it is written with a ×",
             "answer":  "×400"}},
        {"id": "magnification-fifa-do", "kind": "construct",
         "demand": "the same artifact, produced by the student (Law 5)",
         "prompt": "Your turn, same four steps. The eyepiece is ×10 and the "
                   "student switches to the ×4 objective to find their specimen. "
                   "What is the total magnification now? Set it out as Formula, "
                   "Insert, Fix, Answer.",
         "success": ["Formula: eyepiece × objective",
                     "Inserts 10 × 4",
                     "Answer ×40",
                     "Writes it with a × and no other unit"]},
        {"id": "critique-the-drawing", "kind": "investigation",
         "demand": "critique before construct — judge someone else's work first",
         "prompt": "Before you draw anything, mark theirs. Here are the rules "
                   "for a biological drawing: sharp pencil, clear single lines, "
                   "no shading and no colouring in, labels outside the drawing "
                   "with straight lines that do not cross, and a title saying "
                   "what it is and at what magnification. Find every rule the "
                   "biro drawing breaks, and say what each one costs the reader.",
         "success": ["Finds at least four broken rules",
                     "Says shading hides the outline you are trying to show",
                     "Says crossing label lines make labels ambiguous",
                     "Notices the drawing has no magnification on it",
                     "Judges the drawing, not the student"]},
        {"id": "draw-your-own", "kind": "construct",
         "demand": "produce the same artifact you just judged",
         "prompt": "Now do it properly. Draw four onion cells from the lab "
                   "above, following every rule you just used on somebody else.",
         "success": ["Sharp pencil, single clear lines, no shading",
                     "Cells drawn packed together, not floating apart",
                     "Labels outside, ruled, not crossing",
                     "Title names the specimen and the magnification"]},
        {"id": "estimate-cell-size", "kind": "construct",
         "demand": "transfer the measurement method to a new specimen",
         "prompt": "Use the counting method on a different slide. A field of "
                   "view is 1.8 mm across. Thirty cheek cells fit across it. "
                   "Work out roughly how wide one cheek cell is, and say why the "
                   "answer is only rough.",
         "success": ["Divides 1.8 mm by 30 to get about 0.06 mm",
                     "Gives the unit with the answer",
                     "Says the cells are not all the same size",
                     "Says counting across the middle is a judgement, not a "
                     "measurement"]},
    ],

    "ladder": {
        "recall": {
            "q": "A microscope has a ×10 eyepiece and a ×40 objective lens. What "
                 "is the total magnification?",
            "options": ["×50", "×400", "×4", "×4000"],
            "answer": 1,
            "feedback": {
                0: "The two magnifications multiply, they do not add.",
                2: "That is the objective divided by the eyepiece. Multiply "
                   "them instead.",
                3: "Check the multiplication: 10 × 40 is 400.",
            }},
        "apply": {
            "q": "A student can see a whole onion cell at ×100. At ×400 they can "
                 "find almost nothing. What is the best explanation?",
            "options": ["The stronger lens has damaged the specimen",
                        "The field of view is smaller, so less slide is in it",
                        "The higher lens makes the specimen look smaller",
                        "Onion cells are too small to see at ×400"],
            "answer": 1,
            "feedback": {
                0: "A lens does not damage a specimen. Nothing has changed on "
                   "the slide.",
                2: "It makes things look bigger, not smaller — that is what "
                   "magnification means. (CELL-02)",
                3: "They are easily big enough at ×400. Finding them is the "
                   "problem, not seeing them. (CELL-02)",
            }},
        "explain": {
            "q": "A slide shows a field full of perfectly round circles with "
                 "thick dark rims, floating apart from each other. Explain why "
                 "these are almost certainly not cells, and what went wrong.",
            "success": ["Says real cells are packed together with no gaps",
                        "Says the circles are air bubbles",
                        "Says the coverslip was dropped flat instead of lowered "
                        "at an angle",
                        "Says what to do differently next time"]},
        "produce": {
            "q": "Write a method for making and viewing an onion slide that "
                 "another student could follow with no help. Say what each "
                 "step is for, not just what to do.",
            "success": ["Specimen must be thin enough for light to pass through",
                        "Coverslip lowered slowly at an angle, and says why",
                        "Start on the lowest objective, and says why",
                        "Focus using the coarse wheel first, then the fine one",
                        "Steps are in an order that would actually work"]},
    },

    "key_note": "A slide has to be thin, and the coverslip goes down slowly at "
                "an angle or you get air bubbles — round, dark-rimmed, floating "
                "apart. Real cells are packed together in rows. Total "
                "magnification = eyepiece × objective. Always start on the "
                "lowest lens: a higher one shows more detail of less.",

    "ws": ["experimental-skills-and-investigations", "measurement",
           "analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L3 — Animal and plant cells (MODEL)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "animal-and-plant-cells",
    "title":       "Animal and plant cells",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "MODEL",

    "covers":      ["KS3.B.CELLS.02", "KS3.B.CELLS.03"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 45,

    "requires":    ["using-a-microscope"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["biology/cell-biology/animal-plant-cells"],

    "big_question": "What is inside a cell, and what is each part for?",

    "phenomenon": {
        "kind": "demo",
        "title": "Two slides at the same magnification",
        "prompt": "Onion cells on the left, cheek cells on the right, both at "
                  "×400. The onion cells are five times bigger, sit in straight "
                  "rows, and have a hard straight edge you could rule. The cheek "
                  "cells are floppy, rounded and no two are the same shape.",
        "commit": "One of these came from something that stands up without a "
                  "skeleton. Which one — and what is holding it up?",
    },

    "misconceptions": [
        {"id": "CELL-03",
         "statement": "Every plant cell is green, because plants are green.",
         "elicited_by": "plant-extras",
         "confronted_by": "not-all-green"},
        {"id": "CELL-04",
         "statement": "The cell membrane and the cell wall are the same thing — "
                      "animal cells have a wall, it is just called a membrane.",
         "elicited_by": "whats-holding-it-up",
         "confronted_by": "wall-or-membrane"},
    ],

    "vocabulary": [
        {"term": "cell membrane",
         "definition": "A thin skin around every cell that controls what gets in "
                       "and out.",
         "note": "Every cell has one — plant, animal and every other kind."},
        {"term": "cytoplasm",
         "definition": "The jelly that fills the cell, where most of its "
                       "chemical reactions happen.",
         "note": None},
        {"term": "nucleus",
         "definition": "The control centre. It holds the instructions for "
                       "everything the cell does.",
         "note": "Usually one per cell. You will meet a cell with none at all in "
                 "the next lesson."},
        {"term": "mitochondria",
         "definition": "Tiny structures where energy is released from food.",
         "note": "One is a mitochondrion; several are mitochondria. A muscle "
                 "cell is packed with them."},
        {"term": "cell wall",
         "definition": "A stiff layer outside the membrane of a plant cell, "
                       "which gives the cell its shape.",
         "note": "A wall is stiff and on the outside; a membrane is thin and "
                 "underneath it. An animal cell has the membrane only."},
        {"term": "vacuole",
         "definition": "A large space in a plant cell, filled with cell sap, "
                       "which pushes outwards and keeps the cell firm.",
         "note": "When a plant is short of water the vacuoles stop pushing, and "
                 "the whole plant wilts."},
        {"term": "chloroplast",
         "definition": "The green part of a plant cell, where light is used to "
                       "make food.",
         "note": "Only the cells that get light have them. Roots are not green."},
    ],

    "figures": [
        {"id": "b1-cheek-onion-micrograph", "kind": "micrograph",
         "caption": "Cheek cells and onion cells side by side at the same "
                    "magnification.",
         "status": "needed"},
        {"id": "b1-animal-cell-labelled", "kind": "schematic",
         "caption": "An animal cell with the membrane, cytoplasm, nucleus and "
                    "mitochondria labelled.",
         "status": "needed"},
        {"id": "b1-plant-cell-labelled", "kind": "schematic",
         "caption": "A plant cell with all seven parts labelled, drawn beside an "
                    "animal cell at the same scale.",
         "status": "needed"},
    ],

    # MODEL rhythm (§6): lead → the model instrument at the centre of gravity,
    # predict-gated → property blocks anchored back to it → ladder. The hook is
    # wagered at block 2 and answered at block 3; the parts are met as answers
    # to "what is failing?", never as a labelled diagram to copy.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "whats-holding-it-up"},
        {"type": "explainer", "id": "the-wall-and-the-membrane",
         "text": "The onion. A plant stands up without a skeleton because every "
                 "one of its cells is a stiff box. Outside the membrane of a "
                 "plant cell there is a cell wall — a hard layer that will not "
                 "bend, which is why onion cells have straight sides and sit in "
                 "rows. An animal cell has no wall. It has the thin, floppy "
                 "membrane and nothing else outside it, so it takes whatever "
                 "shape it is pushed into. That is the whole difference you can "
                 "see down a microscope."},
        {"type": "figure", "ref": "b1-cheek-onion-micrograph"},
        {"type": "misconception", "id": "wall-or-membrane", "targets": "CELL-04"},
        {"type": "explainer", "id": "the-four-in-every-cell",
         "text": "Underneath that, both cells are built the same way. Four parts "
                 "are in every cell there is. The membrane controls what gets in "
                 "and out. The cytoplasm is the jelly where the cell's reactions "
                 "happen. The nucleus holds the instructions. The mitochondria "
                 "release energy from food, which is what pays for everything "
                 "else. Take any one of those away and something the cell does "
                 "stops. The lab below is where you find out what."},
        {"type": "figure", "ref": "b1-animal-cell-labelled"},
        {"type": "practical", "id": "cell-parts-lab"},
        {"type": "check", "id": "plant-extras"},
        {"type": "misconception", "id": "not-all-green", "targets": "CELL-03"},
        {"type": "figure", "ref": "b1-plant-cell-labelled"},
        {"type": "keyword", "terms": ["cell membrane", "cytoplasm", "nucleus",
                                      "mitochondria", "cell wall", "vacuole",
                                      "chloroplast"]},
        {"type": "check", "id": "part-job-cards"},
        {"type": "check", "id": "compare-two-cells"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "why-so-many-mitochondria",
         "text": "Cells do not all carry the same number of each part. A muscle "
                 "cell in your leg holds thousands of mitochondria, because "
                 "contracting costs energy every single time. A fat cell, which "
                 "mostly sits still and stores, holds very few. Count the "
                 "mitochondria in a cell and you can make a decent guess at how "
                 "hard it works."},
        {"type": "check", "id": "count-mitochondria"},
    ],

    "support": [],

    "activities": [
        {"id": "whats-holding-it-up", "kind": "predict",
         "demand": "elicit CELL-04 by forcing a commitment on the hook",
         "prompt": "Commit before you read on. A plant has no skeleton, yet it "
                   "stands up. What is holding each of its cells in shape?",
         "options": ["A stiff wall outside the cell membrane",
                     "The cell membrane, which is stiff in plants",
                     "Nothing — plant cells are just packed in tightly"],
         "answer": 0,
         "reveal": "A stiff wall, outside the membrane. Plants have both; "
                   "animals have the membrane only. The next block is the whole "
                   "difference in five lines.",
         "targets": "CELL-04"},
        {"id": "wall-or-membrane", "kind": "confrontation",
         "demand": "make the wrongness of CELL-04 visible",
         "prompt": "Name the idea first, in the words students really write: "
                   "'animal cells have a wall too, it's just called a "
                   "membrane.' If the membrane were the wall, an animal cell "
                   "would keep its shape as stubbornly as an onion cell does. "
                   "Look at the cheek cells again.",
         "reveal": "No two of them are the same shape. They are floppy, and they "
                   "have been squashed into whatever room they were given. A "
                   "wall and a membrane are two different things doing two "
                   "different jobs: the wall is stiff, on the outside, and holds "
                   "the shape; the membrane is thin, underneath, and controls "
                   "what goes through. A plant cell has both. An animal cell has "
                   "one.",
         "targets": "CELL-04"},
        {"id": "cell-parts-lab", "kind": "lab",
         "demand": "investigate",
         "prompt": "Switch one part off at a time and watch what stops. Predict "
                   "first, before you touch anything: switch off the nucleus of "
                   "a cell. What happens?",
         "options": ["The cell bursts open straight away",
                     "The cell loses its instructions and cannot make new parts "
                     "or divide",
                     "Nothing at all — the nucleus only matters when the cell "
                     "reproduces"],
         "answer": 1,
         "sim": {"kind": "system-parts",
                 "controls": ["part"],
                 "readouts": ["what still works", "what has stopped"],
                 "parts": [
                     {"id": "membrane", "name": "Cell membrane",
                      "job": "Controls what gets in and out",
                      "needs": []},
                     {"id": "cytoplasm", "name": "Cytoplasm",
                      "job": "Where the cell's reactions happen",
                      "needs": ["membrane"]},
                     {"id": "nucleus", "name": "Nucleus",
                      "job": "Holds the instructions for everything",
                      "needs": ["cytoplasm"]},
                     {"id": "mitochondria", "name": "Mitochondria",
                      "job": "Release energy from food",
                      "needs": ["cytoplasm", "membrane"]},
                     {"id": "wall", "name": "Cell wall (plant only)",
                      "job": "Keeps the cell's box shape",
                      "needs": []},
                     {"id": "vacuole", "name": "Vacuole (plant only)",
                      "job": "Pushes outwards and keeps the cell firm",
                      "needs": ["wall", "membrane"]},
                     {"id": "chloroplast", "name": "Chloroplasts (plant only)",
                      "job": "Use light to make food",
                      "needs": ["cytoplasm"]},
                 ],
                 "caption": "Switch off one part and watch what else stops, in "
                            "order. Switch it back on before you try the next "
                            "one."},
         "reveal": "It loses its instructions. Nothing bursts and nothing "
                   "happens immediately — the cell carries on for a while, then "
                   "cannot replace anything that wears out and cannot divide. "
                   "Now try the membrane, and watch how much goes down with it: "
                   "everything inside depends on something being kept in."},
        {"id": "plant-extras", "kind": "predict",
         "demand": "elicit CELL-03",
         "prompt": "Plants have three parts animals do not: the wall, a large "
                   "vacuole, and chloroplasts. Chloroplasts are the green ones. "
                   "Which plant cells have them?",
         "options": ["All of them — that is why plants are green",
                     "Only the cells that light actually reaches",
                     "Only the cells in the flower and the fruit"],
         "answer": 1,
         "reveal": "Only the cells light reaches. Dig up a root and look at it: "
                   "it is white.",
         "targets": "CELL-03"},
        {"id": "not-all-green", "kind": "confrontation",
         "demand": "make the wrongness of CELL-03 visible",
         "prompt": "Say the wrong idea out loud: 'every plant cell is green, "
                   "because plants are green.' Now pull up a dandelion and look "
                   "at the root. Then look at the potato in the cupboard, and "
                   "the onion you have been staring at all lesson.",
         "reveal": "All three are white, and all three are plant. A chloroplast "
                   "is only worth having where light arrives, so a plant builds "
                   "them in its leaves and in the parts of the stem that catch "
                   "the sun, and nowhere else. Leaving a potato on a windowsill "
                   "until it goes green is the same rule working in front of "
                   "you. Green is a job, not a plant's colour.",
         "targets": "CELL-03"},
        {"id": "part-job-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Seven parts, seven jobs. Say the name of the part out loud "
                   "before you tap each card.",
         "cards": [
             {"front": "Controls what gets in and out of the cell",
              "back": "Cell membrane — in every cell there is"},
             {"front": "The jelly where the cell's reactions happen",
              "back": "Cytoplasm — in every cell"},
             {"front": "Holds the instructions for everything the cell does",
              "back": "Nucleus — in every cell in this unit"},
             {"front": "Releases energy from food",
              "back": "Mitochondria — in every cell, most of all in busy ones"},
             {"front": "Stiff layer outside the membrane, holding the shape",
              "back": "Cell wall — plant cells only"},
             {"front": "Big sap-filled space that pushes out and keeps the cell "
                       "firm",
              "back": "Vacuole — plant cells only"},
             {"front": "Uses light to make food, and is green",
              "back": "Chloroplast — plant cells that get light"},
         ]},
        {"id": "compare-two-cells", "kind": "construct",
         "demand": "force the linked comparison, not two separate lists",
         "prompt": "One job left, and it is the one people lose marks on for "
                   "years: a comparison has to mention both sides. Complete this "
                   "sentence properly: 'A plant cell can make its own food but "
                   "an animal cell cannot, because …'",
         "success": ["Mentions BOTH cells, not just the plant",
                     "Says the plant cell has chloroplasts",
                     "Says the animal cell has none",
                     "Links chloroplasts to using light to make food"]},
        {"id": "count-mitochondria", "kind": "construct",
         "demand": "transfer the parts idea to an unseen cell",
         "prompt": "Use the idea on cells you have not met. Put these three in "
                   "order of how many mitochondria you would expect, most "
                   "first, and justify the order: a heart muscle cell, a fat "
                   "storage cell, a cell just under the skin of a leaf.",
         "success": ["Heart muscle cell first",
                     "Justifies by how much energy the cell's job needs",
                     "Says mitochondria release energy from food",
                     "Does not order them by size"]},
    ],

    "ladder": {
        "recall": {
            "q": "Which part of a cell controls what enters and leaves it?",
            "options": ["The cell wall", "The cell membrane", "The cytoplasm",
                        "The nucleus"],
            "answer": 1,
            "feedback": {
                0: "The wall is stiff and holds the shape. It is not a filter, "
                   "and animal cells manage without one. (CELL-04)",
                2: "The cytoplasm is where reactions happen, inside the "
                   "membrane.",
                3: "The nucleus holds the instructions; it does not touch the "
                   "outside of the cell.",
            }},
        "apply": {
            "q": "A cell from a garden plant has a nucleus, mitochondria and a "
                 "cell wall, but no chloroplasts. Where in the plant did it come "
                 "from?",
            "options": ["A root, where no light reaches",
                        "A leaf, where light reaches easily",
                        "Nowhere — every plant cell has chloroplasts",
                        "Nowhere — plant cells never have mitochondria"],
            "answer": 0,
            "feedback": {
                1: "A leaf cell in the light is exactly where chloroplasts are "
                   "worth having, so it would have them.",
                2: "Only the cells that get light have them. Roots are white. "
                   "(CELL-03)",
                3: "Every cell has mitochondria — plants release energy from "
                   "food too.",
            }},
        "explain": {
            "q": "Explain why an onion cell keeps a straight-sided box shape but "
                 "a cheek cell does not.",
            "success": ["Says the onion cell has a cell wall",
                        "Says the wall is stiff and sits outside the membrane",
                        "Says the cheek cell has a membrane only",
                        "Says the membrane is thin and flexible, so the cell "
                        "takes the shape it is given"]},
        "produce": {
            "q": "A student writes: 'animal cells have a wall to hold them "
                 "together.' Write a correction another student would "
                 "understand.",
            "success": ["Says animal cells have no cell wall",
                        "Says what they do have — a membrane",
                        "Says what each of the two actually does",
                        "Says which cells do have a wall"]},
    },

    "key_note": "Every cell has a membrane, cytoplasm, a nucleus and "
                "mitochondria. Plant cells add three more: a stiff cell wall, a "
                "large vacuole and chloroplasts. The wall is outside and holds "
                "the shape; the membrane is underneath and controls what goes "
                "through. Only the plant cells that get light are green.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L4 — Specialised cells (SYSTEM)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "specialised-cells",
    "title":       "Specialised cells",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "SYSTEM",

    "covers":      ["KS3.B.CELLS.04"],
    "touches":     ["KS3.B.CELLS.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "structure-function", "level": 2},
                    {"id": "cells-and-systems", "level": 2},
                    {"id": "particles", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 45,

    "requires":    ["animal-and-plant-cells"],
    "assumes":     ["KS3.C.PIS.03"],   # diffusion, owned by C1 L5
    # ⊖ §8.10 — `why` RENDERS to the student, in the "Connects to" card. It read
    #   "Diffusion is owned by C1 (§7.4 ordering: …) … and must render gracefully
    #   whether or not C1 has been taught first", which is the platform
    #   explaining its own build order to a twelve-year-old who did not ask.
    #   Rewritten to say what the connection IS. The authoring rationale it used
    #   to carry is not lost — it is what `assumes` and the reference edge encode.
    "references":  [{"unit": "C1", "lesson": "diffusion",
                     "why": "Oxygen gets into a red blood cell by diffusion — "
                            "the same spreading out you meet with particles in "
                            "chemistry, happening here across a living "
                            "membrane."}],
    "ks4_links":   ["biology/cell-biology/cell-specialisation",
                    "biology/cell-biology/transport-in-cells"],

    "big_question": "Why is a red blood cell shaped like a squashed doughnut?",

    "phenomenon": {
        "kind": "data",
        "title": "Six cells, none of them tidy",
        "prompt": "Six human and plant cells, photographed at the same "
                  "magnification: a red blood cell, a nerve cell almost a metre "
                  "long, a sperm cell with a tail, a root hair cell, a palisade "
                  "cell, a muscle fibre. Not one of them looks like the neat "
                  "labelled blob you drew last lesson.",
        "commit": "One of these six has no nucleus at all. Which one — and why "
                  "would a cell give up its control centre?",
    },

    "misconceptions": [
        {"id": "CELL-05",
         "statement": "Every cell in your body has a nucleus.",
         "elicited_by": "which-has-no-nucleus",
         "confronted_by": "no-nucleus-reveal"},
        # Re-used, not re-minted. Same wrong idea as C1 L5, in a biological
        # costume: "the heart pushes the oxygen into the muscle cell". The
        # `statement` is copied verbatim from the register; only the activities
        # are local. See the module docstring.
        {"id": "PART-10",
         "statement": "Diffusion needs a draught, a current, or someone to waft "
                      "it — something has to push the particles along.",
         "elicited_by": "how-does-oxygen-get-in",
         "confronted_by": "membrane-diffusion-lab"},
    ],

    "vocabulary": [
        {"term": "specialised",
         "definition": "Built to do one particular job very well.",
         "note": "The price is that a specialised cell is usually no good at "
                 "anything else."},
        {"term": "adaptation",
         "definition": "A feature that helps something do its job.",
         "note": "Here the adaptation is a feature of one single cell. Later you "
                 "will meet adaptations of whole organisms."},
        {"term": "diffusion",
         "definition": "The spreading out of particles from where there are many "
                       "to where there are few, caused by their own random "
                       "movement.",
         "note": "You met this in chemistry, with a smell crossing a still room. "
                 "Same process, same rules — now doing a job inside you."},
        {"term": "surface area",
         "definition": "The total amount of outside surface something has.",
         "note": "Squash a cell flat, or grow it a long thin hair, and its "
                 "surface area goes up without much more inside to supply."},
    ],

    "figures": [
        {"id": "b1-red-blood-cell-section", "kind": "schematic",
         "caption": "A red blood cell face on and in section, with the dip in "
                    "the middle marked and arrows showing oxygen crossing the "
                    "membrane.",
         "status": "needed"},
        {"id": "b1-diffusion-distance", "kind": "schematic",
         "caption": "A small cell and a large cell side by side, with the "
                    "distance from the surface to the centre marked on each.",
         "status": "needed"},
        {"id": "b1-specialised-cells-set", "kind": "schematic",
         "caption": "Six specialised cells drawn to the same scale, each "
                    "labelled with the one feature that fits its job: red blood "
                    "cell, nerve cell, sperm cell, root hair cell, palisade "
                    "cell, muscle fibre.",
         "status": "needed"},
    ],

    # SYSTEM rhythm (§6): lead → the system assembled part by part, each part
    # earning its place → PERTURBATION as the flagship, never labelling →
    # ladder. The characteristic KS3 error is knowing the parts and not the
    # interaction, so the flagship (block 11) breaks a cell on purpose. The
    # mid-size instrument at block 8 is C1's diffusion lab, unchanged, because
    # the mechanism it teaches is the mechanism this lesson runs on.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "which-has-no-nucleus"},
        {"type": "explainer", "id": "room-for-the-cargo",
         "text": "The red blood cell. It pushes its nucleus out as it is made, "
                 "and that is not a fault — it is the point. The space where the "
                 "nucleus would sit is filled with haemoglobin instead, the red "
                 "chemical that carries oxygen. No nucleus means more cargo. It "
                 "also means the cell cannot repair itself or divide, so it "
                 "wears out in about four months. Your body makes around two "
                 "million new ones every second to keep up."},
        {"type": "figure", "ref": "b1-red-blood-cell-section"},
        {"type": "misconception", "id": "no-nucleus-reveal", "targets": "CELL-05"},
        {"type": "check", "id": "how-does-oxygen-get-in"},
        {"type": "practical", "id": "membrane-diffusion-lab"},
        {"type": "explainer", "id": "why-cells-stay-small",
         "text": "So nothing pushes oxygen into a cell. It arrives by diffusion, "
                 "and diffusion has one weakness: it is quick over a tiny "
                 "distance and hopeless over a large one. Double the width of a "
                 "cell and the middle waits far longer than twice as long. That "
                 "is why almost every cell is microscopic, and why the ones that "
                 "have to move materials fast are flattened, or dented, or grown "
                 "out into a long thin hair. Shape is how a cell cheats the "
                 "distance."},
        {"type": "figure", "ref": "b1-diffusion-distance"},
        {"type": "practical", "id": "knock-out-the-shape"},
        {"type": "figure", "ref": "b1-specialised-cells-set"},
        {"type": "keyword", "terms": ["specialised", "adaptation", "diffusion",
                                      "surface area"]},
        {"type": "check", "id": "shape-job-cards"},
        {"type": "check", "id": "design-a-cell"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "the-longest-cell",
         "text": "Cells stay small in every direction but one. A nerve cell "
                 "running from your big toe to the base of your spine is a "
                 "single cell, close to a metre long — and it is still "
                 "microscopically thin. Thin is what matters. Length costs it "
                 "nothing, because nothing has to diffuse from one end of it to "
                 "the other."},
        {"type": "check", "id": "nerve-cell-explain"},
    ],

    "support": [],

    "activities": [
        {"id": "which-has-no-nucleus", "kind": "predict",
         "demand": "elicit CELL-05 by forcing a commitment on the hook",
         "prompt": "Commit before you read on. Which of the six has no nucleus?",
         "options": ["The nerve cell — it is far too thin to fit one in",
                     "The red blood cell — it is packed with something else",
                     "None of them — every cell has to have a nucleus"],
         "answer": 1,
         "reveal": "The red blood cell, and it gives up its nucleus on purpose. "
                   "The next block says what it gets in return.",
         "targets": "CELL-05"},
        {"id": "no-nucleus-reveal", "kind": "confrontation",
         "demand": "make the wrongness of CELL-05 visible",
         "prompt": "The idea to kill, in the words students really write: 'every "
                   "cell has a nucleus, it's the control centre.' A red blood "
                   "cell has none. So ask what it would cost to put one back in.",
         "reveal": "Room. The nucleus would take up space that is currently full "
                   "of haemoglobin, so the cell would carry less oxygen on every "
                   "single trip — and carrying oxygen is the only reason it "
                   "exists. It pays a real price for that: with no instructions "
                   "it cannot repair itself, so it wears out and has to be "
                   "replaced. The rule is not 'every cell has a nucleus'. The "
                   "rule is that a specialised cell keeps whatever helps it do "
                   "its job and loses what gets in the way.",
         "targets": "CELL-05"},
        {"id": "how-does-oxygen-get-in", "kind": "predict",
         "demand": "elicit PART-10 in its biological form",
         "prompt": "So the red blood cell arrives at a working muscle loaded "
                   "with oxygen. Commit before you read on: what actually gets "
                   "the oxygen out of the blood and into the muscle cell?",
         "options": ["The heart pushes it in — that is what blood pressure is "
                     "for",
                     "The muscle cell pulls it in when it needs it",
                     "Nothing pushes or pulls it — it moves by diffusion"],
         "answer": 2,
         "reveal": "Nothing pushes it. This is the same wrong answer you met in "
                   "chemistry, wearing a lab coat: 'something has to move the "
                   "particles'. Run the lab and watch.",
         "targets": "PART-10"},
        {"id": "membrane-diffusion-lab", "kind": "lab",
         "demand": "investigate",
         "prompt": "The wrong idea in students' own words: 'the heart pushes "
                   "the oxygen into the muscle cell.' This is the diffusion lab "
                   "from chemistry, unchanged — except that the dashed line down "
                   "the middle is now a cell membrane, with oxygen crowded on "
                   "the blood side. Predict before you count: over ten seconds, "
                   "which way do oxygen particles cross the membrane?",
         "options": ["Only from the blood into the cell, where it is needed",
                     "Both ways, but more from the blood side",
                     "Both ways, in exactly equal numbers"],
         "answer": 1,
         "sim": {"kind": "diffusion",
                 "controls": ["temperature"],
                 "readouts": ["crossings left to right",
                              "crossings right to left",
                              "concentration on each side"],
                 "caption": "The dashed line is the cell membrane. Nothing in "
                            "this lab pushes, pumps or aims anything."},
         "reveal": "Both counters climb, the whole time. Particles cross in both "
                   "directions, and more cross into the cell only because more "
                   "of them started on the blood side. Nothing pushed them and "
                   "nothing was aiming for the muscle. Warm it up and everything "
                   "happens faster, which is one reason your body is held at "
                   "37 °C.",
         "targets": "PART-10"},
        {"id": "knock-out-the-shape", "kind": "lab",
         "demand": "investigate",
         "prompt": "Now break the cells on purpose. Change one feature at a time "
                   "and watch what the cell can no longer do. Predict first: "
                   "give the red blood cell its nucleus back. What happens to "
                   "the oxygen it delivers?",
         "options": ["Nothing — the nucleus does not touch the oxygen",
                     "It carries less, because there is less room for "
                     "haemoglobin",
                     "It carries more, because the nucleus controls the loading"],
         "answer": 1,
         "sim": {"kind": "system-parts",
                 "controls": ["part"],
                 "readouts": ["what still works", "what has stopped"],
                 "parts": [
                     {"id": "no-nucleus", "name": "No nucleus",
                      "job": "Leaves room for haemoglobin",
                      "needs": []},
                     {"id": "haemoglobin", "name": "Packed with haemoglobin",
                      "job": "Holds the oxygen for the journey",
                      "needs": ["no-nucleus"]},
                     {"id": "dimple", "name": "Dented on both sides",
                      "job": "Large surface area, short distance to the middle",
                      "needs": []},
                     {"id": "small", "name": "Very small",
                      "job": "Fits through the narrowest blood vessels",
                      "needs": []},
                     {"id": "flexible", "name": "Flexible membrane",
                      "job": "Squeezes through and springs back",
                      "needs": ["small"]},
                     {"id": "delivery", "name": "Oxygen delivered to a muscle",
                      "job": "The job the whole cell exists for",
                      "needs": ["haemoglobin", "dimple", "flexible"]},
                 ],
                 "caption": "Switch one feature off and watch the delivery "
                            "chain. Every feature here is either cargo, "
                            "distance, or getting there."},
         "reveal": "It carries less. Everything in this cell is either about how "
                   "much oxygen it can hold, how fast that oxygen can cross the "
                   "membrane, or whether the cell can reach the muscle at all — "
                   "and switching off any one of the three stops the delivery. "
                   "Now try the dent: without it the middle of the cell is "
                   "further from the surface, and oxygen has further to diffuse."},
        {"id": "shape-job-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Six cells, six jobs. Say what the shape is for before you "
                   "tap each card.",
         "cards": [
             {"front": "Dented disc, no nucleus, packed with haemoglobin",
              "back": "Red blood cell — maximum oxygen, minimum distance to the "
                      "middle"},
             {"front": "Almost a metre long, and microscopically thin",
              "back": "Nerve cell — carries a signal from one end of you to the "
                      "other"},
             {"front": "A long tail, and a head full of mitochondria",
              "back": "Sperm cell — swims, and carries its own energy supply"},
             {"front": "One long thin hair pushed out into the soil",
              "back": "Root hair cell — huge surface area for taking in water "
                      "and minerals"},
             {"front": "Tall box near the top of a leaf, stuffed with "
                       "chloroplasts",
              "back": "Palisade cell — catches as much light as possible"},
             {"front": "Long fibre that can shorten, full of mitochondria",
              "back": "Muscle cell — pulls, and pays for it with a lot of "
                      "energy"},
         ]},
        {"id": "design-a-cell", "kind": "construct",
         "demand": "produce an adaptation for a job the lesson never showed",
         "prompt": "Now design one. A fish takes in oxygen from water through "
                   "its gills, where the water is on one side and the blood is "
                   "on the other. Design the cell that lines a gill, and justify "
                   "every feature you give it.",
         "success": ["Says the cell should be very thin, so the distance is "
                     "short",
                     "Says the surface should be large — flat, folded or "
                     "hair-like",
                     "Says oxygen crosses by diffusion",
                     "Justifies each feature by the job, not by how it looks"]},
        {"id": "nerve-cell-explain", "kind": "construct",
         "demand": "transfer the diffusion-distance rule to an odd case",
         "prompt": "Apply the rule to the cell that seems to break it. A nerve "
                   "cell is a metre long. Explain why that does not slow its "
                   "oxygen supply down, when a cell twice as wide would be in "
                   "trouble.",
         "success": ["Says diffusion is slow across a large distance",
                     "Says the nerve cell is thin in every direction that "
                     "matters",
                     "Says nothing has to diffuse along its length",
                     "Uses width, not length, as the thing that counts"]},
    ],

    "ladder": {
        "recall": {
            "q": "Which of these cells has no nucleus?",
            "options": ["The red blood cell", "The nerve cell",
                        "The root hair cell", "The muscle cell"],
            "answer": 0,
            "feedback": {
                1: "A nerve cell has a nucleus, in the wider part at one end. "
                   "(CELL-05)",
                2: "A root hair cell has a nucleus like other plant cells. "
                   "(CELL-05)",
                3: "Muscle cells keep their nuclei — and they are busy cells. "
                   "(CELL-05)",
            }},
        "apply": {
            "q": "A root hair cell has one long, thin hair pushed out into the "
                 "soil. What does that shape give it?",
            "options": ["A large surface area for taking in water and minerals",
                        "A firm anchor that holds the plant against the wind",
                        "A short path for light to reach the chloroplasts",
                        "A store of food to last the plant through winter"],
            "answer": 0,
            "feedback": {
                1: "Anchoring is the job of the whole root, not of one cell's "
                   "hair.",
                2: "Root cells are underground and have no chloroplasts. "
                   "(CELL-03)",
                3: "Storage happens elsewhere in the root, and would want a fat "
                   "cell, not a thin hair.",
            }},
        "explain": {
            "q": "Explain how oxygen gets from the blood into a muscle cell, "
                 "using the word diffusion.",
            "success": ["Says there is more oxygen in the blood than in the "
                        "muscle cell",
                        "Says particles move randomly, in both directions",
                        "Says more move into the cell because more start "
                        "outside it",
                        "Does not say the blood pushes or forces the oxygen in"]},
        "produce": {
            "q": "A student says: 'a bigger cell would be better, because it can "
                 "hold more.' Using diffusion, explain why almost every cell is "
                 "tiny instead.",
            "success": ["Says materials get in and out by diffusion",
                        "Says diffusion is slow across a large distance",
                        "Says the middle of a large cell would be badly supplied",
                        "Gives an example of a shape that beats the problem, "
                        "such as flat, dented or hair-like"]},
    },

    "key_note": "A specialised cell's shape is its job. A red blood cell drops "
                "its nucleus to carry more oxygen and is dented so nothing is "
                "far from the surface; a root hair cell grows a long hair for "
                "surface area. Materials cross the membrane by diffusion — "
                "random, both ways, never pushed — and diffusion is slow over "
                "distance, which is why cells stay small.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L5 — Levels of organisation (SYSTEM)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "levels-of-organisation",
    "title":       "Levels of organisation",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "SYSTEM",

    "covers":      ["KS3.B.CELLS.06"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 3},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 45,

    "requires":    ["specialised-cells"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["biology/organisation/principles-of-organisation",
                    "biology/organisation/plant-tissues"],

    "big_question": "How do you get from one cell to a whole animal?",

    "phenomenon": {
        "kind": "demo",
        "title": "Pulling a piece of steak apart",
        "prompt": "Take a piece of cooked steak and pull it apart with two "
                  "forks. It splits into strands. Pull a strand apart and you "
                  "get finer strands. Keep going, put the last one under a "
                  "microscope, and you reach single muscle cells.",
        "commit": "What is the smallest piece you could take and still call it "
                  "muscle?",
    },

    "misconceptions": [
        {"id": "CELL-06",
         "statement": "The levels are just about size: small things are cells, "
                      "medium things are tissues and big things are organs.",
         "elicited_by": "size-trap",
         "confronted_by": "not-about-size"},
        {"id": "CELL-07",
         "statement": "Blood is not a tissue, because a tissue is solid and "
                      "blood is a liquid.",
         "elicited_by": "blood-check",
         "confronted_by": "blood-is-a-tissue"},
    ],

    "vocabulary": [
        {"term": "tissue",
         "definition": "A group of similar cells working together to do one job.",
         "note": None},
        {"term": "organ",
         "definition": "A group of different tissues working together to do one "
                       "job.",
         "note": "A stomach is an organ. So is a leaf — plants have them too."},
        {"term": "organ system",
         "definition": "A group of organs working together to do one big job.",
         "note": "Your digestive system is a chain of organs, from your mouth to "
                 "your intestines."},
    ],

    "figures": [
        {"id": "b1-organisation-ladder", "kind": "schematic",
         "caption": "One example carried up all five levels: muscle cell → "
                    "muscle tissue → stomach → digestive system → human.",
         "status": "needed"},
        {"id": "b1-stomach-wall-layers", "kind": "micrograph",
         "caption": "A section through the stomach wall showing three different "
                    "tissue layers stacked on each other.",
         "status": "needed"},
        {"id": "b1-plant-organisation", "kind": "schematic",
         "caption": "The same five levels in a plant: palisade cell → palisade "
                    "tissue → leaf → shoot system → whole plant.",
         "status": "needed"},
    ],

    # SYSTEM rhythm (§6) again, and deliberately NOT the same lineup as L4:
    # this one builds the ladder first and breaks it last. The flagship at
    # block 12 is a perturbation that travels UP the levels, which is the only
    # way to show that the levels are a chain of dependencies rather than a
    # list of sizes — the exact error CELL-06 names.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "smallest-piece"},
        {"type": "explainer", "id": "you-stop-at-the-cell",
         "text": "You stop at one muscle cell. Split that and you have the "
                 "inside of a cell, which is not muscle any more. So the cell is "
                 "the bottom of the ladder — and everything above it is cells "
                 "grouped up. Similar cells working together make a tissue. "
                 "Different tissues working together make an organ. Organs "
                 "working together make an organ system. Systems working "
                 "together make you."},
        {"type": "figure", "ref": "b1-organisation-ladder"},
        {"type": "keyword", "terms": ["tissue", "organ", "organ system"]},
        {"type": "check", "id": "size-trap"},
        {"type": "misconception", "id": "not-about-size", "targets": "CELL-06"},
        {"type": "practical", "id": "level-sorter"},
        {"type": "check", "id": "blood-check"},
        {"type": "misconception", "id": "blood-is-a-tissue", "targets": "CELL-07"},
        {"type": "figure", "ref": "b1-stomach-wall-layers"},
        {"type": "practical", "id": "break-the-chain"},
        {"type": "explainer", "id": "one-failure-travels-up",
         "text": "That is what the levels are really for. Each one can do "
                 "something the level below cannot: one muscle cell twitches, a "
                 "sheet of them squeezes a stomach. And it runs the other way "
                 "too. A problem in one tissue does not stay in that tissue — it "
                 "stops the organ doing its job, which stops the system, which "
                 "the whole organism then feels. Nothing in a body fails on its "
                 "own."},
        {"type": "figure", "ref": "b1-plant-organisation"},
        {"type": "check", "id": "plant-ladder"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "lab-grown-tissue",
         "text": "The levels explain something hospitals can and cannot do. "
                 "Growing a sheet of skin tissue for a burns patient is "
                 "difficult but it is done: one kind of cell, grown into one "
                 "layer. Growing a whole organ is a far harder problem, because "
                 "an organ is several different tissues arranged in exactly the "
                 "right places, with a blood supply running through all of them."},
        {"type": "check", "id": "why-organs-are-harder"},
    ],

    "support": [],

    "activities": [
        {"id": "smallest-piece", "kind": "predict",
         "demand": "elicit the bottom of the ladder from the hook",
         "prompt": "Commit before you read on. What is the smallest piece you "
                   "could pull off and still call it muscle?",
         "options": ["A strand you can just see without a microscope",
                     "One single muscle cell",
                     "The nucleus inside a muscle cell"],
         "answer": 1,
         "reveal": "One muscle cell. Go smaller and you are inside a cell, "
                   "looking at parts that are not muscle at all.",
         "targets": None},
        {"id": "size-trap", "kind": "predict",
         "demand": "elicit CELL-06",
         "prompt": "Now the trap. A nerve running down your leg is long enough "
                   "to see. A piece of bone is big, hard and solid. Which level "
                   "is bone at?",
         "options": ["An organ — it is big, solid and you can hold it",
                     "A tissue — it is one kind of material doing one job",
                     "An organ system — a skeleton is a system of bones"],
         "answer": 1,
         "reveal": "A tissue. Bone is one kind of material with one job, no "
                   "matter how big the piece is.",
         "targets": "CELL-06"},
        {"id": "not-about-size", "kind": "confrontation",
         "demand": "make the wrongness of CELL-06 visible",
         "prompt": "Say the wrong idea out loud: 'small things are cells, big "
                   "things are organs.' Now put these two next to each other. "
                   "Bone: big, hard, heavy — and a tissue. The pituitary gland "
                   "in your head: the size of a pea — and an organ.",
         "reveal": "The pea beats the leg bone. Size decides nothing here. What "
                   "decides is how many kinds of thing are working together: one "
                   "kind of cell is a tissue, several kinds of tissue arranged "
                   "together is an organ, several organs in a chain is a system. "
                   "Ask 'what is working with what', never 'how big is it'.",
         "targets": "CELL-06"},
        {"id": "level-sorter", "kind": "classify",
         "demand": "classify, at rising stakes",
         "prompt": "Eight to sort, getting harder. Name the level for each and "
                   "say what settled it: a root hair cell · skin · the heart · "
                   "a leaf · bone · the small intestine · muscle · the digestive "
                   "system.",
         "options": ["Cell", "Tissue", "Organ", "Organ system"],
         "reveal": "Cell: root hair cell. Tissue: bone, muscle. Organ: the "
                   "heart, a leaf, the small intestine — and skin, which catches "
                   "almost everyone, because it is several tissues layered "
                   "together and is the largest organ you have. System: the "
                   "digestive system."},
        {"id": "blood-check", "kind": "predict",
         "demand": "elicit CELL-07",
         "prompt": "One case tests the definition harder than any other. Blood "
                   "is liquid, and it holds red cells, white cells and platelets "
                   "— more than one kind of cell. Which level is blood?",
         "options": ["Not a level at all — blood is a liquid, not a body part",
                     "A tissue — its cells work together on one job",
                     "An organ — it contains several different kinds of cell"],
         "answer": 1,
         "reveal": "A tissue, and it is the case that shows what the definition "
                   "actually rests on.",
         "targets": "CELL-07"},
        {"id": "blood-is-a-tissue", "kind": "confrontation",
         "demand": "make the wrongness of CELL-07 visible",
         "prompt": "The wrong idea, said plainly: 'blood can't be a tissue, a "
                   "tissue is solid.' So check what the definition of a tissue "
                   "actually says. Cells working together to do one job. Read it "
                   "again — it says nothing about being solid, and nothing about "
                   "being tidy.",
         "reveal": "Blood is a tissue. Its cells all work on one job between "
                   "them — transport and defence — and that shared job is the "
                   "whole test. Being liquid is not a disqualification, and nor "
                   "is having more than one kind of cell in it. What makes a "
                   "tissue is what its cells are for, never what it feels like "
                   "in your hand.",
         "targets": "CELL-07"},
        {"id": "break-the-chain", "kind": "lab",
         "demand": "investigate",
         "prompt": "Now break one level and watch what happens to the rest. "
                   "Predict first: switch off the muscle tissue in the stomach "
                   "wall, leaving every other tissue working. What is the "
                   "furthest the damage reaches?",
         "options": ["Only that tissue — the other tissues carry on as normal",
                     "The stomach stops churning, and the whole organism gets "
                     "less from its food",
                     "Nothing at all — the stomach's job is acid, not movement"],
         "answer": 1,
         "sim": {"kind": "system-parts",
                 "controls": ["part"],
                 "readouts": ["what still works", "what has stopped"],
                 "parts": [
                     # `one_of_many` added at MRB-198 integration: the reveal
                     # below teaches that switching off ONE muscle cell does
                     # almost nothing because a tissue is thousands of them —
                     # but the payload shape {id, name, job, needs} cannot say
                     # so, and a bare needs-edge would cascade a single cell's
                     # failure to the whole organism, contradicting the reveal.
                     # The flag marks a part as one instance of a large
                     # population; the engine absorbs its failure and the
                     # readout says why. The cascade stays derived from data.
                     {"id": "muscle-cell", "name": "Muscle cell",
                      "job": "Shortens when it is told to",
                      "needs": [], "one_of_many": True},
                     {"id": "gland-cell", "name": "Gland cell",
                      "job": "Makes acid and digestive juice",
                      "needs": [], "one_of_many": True},
                     {"id": "muscle-tissue", "name": "Muscle tissue",
                      "job": "Squeezes and churns the food",
                      "needs": ["muscle-cell"]},
                     {"id": "gland-tissue", "name": "Glandular tissue",
                      "job": "Releases the juice into the stomach",
                      "needs": ["gland-cell"]},
                     {"id": "lining", "name": "Lining tissue",
                      "job": "Protects the stomach from its own acid",
                      "needs": []},
                     {"id": "stomach", "name": "Stomach (organ)",
                      "job": "Breaks food down, physically and chemically",
                      "needs": ["muscle-tissue", "gland-tissue", "lining"]},
                     {"id": "digestive", "name": "Digestive system",
                      "job": "Gets food into the blood",
                      "needs": ["stomach"]},
                     {"id": "organism", "name": "The organism",
                      "job": "Stays supplied with everything it needs",
                      "needs": ["digestive"]},
                 ],
                 "caption": "Switch off one part and watch the failure climb "
                            "the levels. Try a cell, then a tissue, then the "
                            "organ."},
         "reveal": "It reaches all the way to the organism. One tissue stops, so "
                   "the organ can only do half its job, so the system delivers "
                   "less, so the whole animal is short of what it needs. Now try "
                   "switching off a single muscle cell instead: almost nothing "
                   "happens, because a tissue is thousands of them and the rest "
                   "cover for it. That difference is what having levels buys you."},
        {"id": "plant-ladder", "kind": "construct",
         "demand": "produce the same ladder for a case nobody demonstrated",
         "prompt": "Build the ladder yourself, for a plant this time. Start at a "
                   "palisade cell in a leaf and climb all five levels to the "
                   "whole plant, naming each level as you go.",
         "success": ["Cell: palisade cell",
                     "Tissue: palisade tissue, or a layer of similar cells",
                     "Organ: the leaf",
                     "System: the shoot, or the leaves and stem together",
                     "Organism: the whole plant"]},
        {"id": "why-organs-are-harder", "kind": "construct",
         "demand": "transfer the level difference to a real problem",
         "prompt": "Use the levels to explain a real difficulty. Scientists can "
                   "grow a sheet of skin tissue in a laboratory, but growing a "
                   "whole working kidney is far harder. Explain the difference "
                   "using the levels.",
         "success": ["Says a tissue is one kind of cell doing one job",
                     "Says an organ is several tissues arranged together",
                     "Says the arrangement matters, not just the cells",
                     "Mentions that an organ needs a blood supply through it"]},
    ],

    "ladder": {
        "recall": {
            "q": "What is a tissue?",
            "options": ["A group of similar cells working together on one job",
                        "A group of different organs working together",
                        "A single cell that has one particular job",
                        "The liquid that surrounds the organs in the body"],
            "answer": 0,
            "feedback": {
                1: "That is an organ system — one level higher than an organ.",
                2: "One cell on its own is a cell, however specialised it is.",
                3: "There is no such level. Blood is liquid and is a tissue. "
                   "(CELL-07)",
            }},
        "apply": {
            "q": "Blood contains red cells, white cells and platelets, all "
                 "working together to carry things and defend the body. Which "
                 "level is blood?",
            "options": ["A cell", "A tissue", "An organ", "An organ system"],
            "answer": 1,
            "feedback": {
                0: "Blood contains cells; it is not one cell.",
                2: "An organ is several tissues arranged together. Blood is one "
                   "tissue.",
                3: "A system is organs in a chain, like the digestive system.",
            }},
        "explain": {
            "q": "Explain how damage to one tissue in the stomach can affect the "
                 "whole organism.",
            "success": ["Names the tissue and the job it does",
                        "Says the organ can then only do part of its job",
                        "Says the organ system delivers less as a result",
                        "Says the organism is left short of something it needs"]},
        "produce": {
            "q": "A student says: 'the heart is a tissue, because it's all "
                 "muscle.' Write a reply that puts the heart at the right level "
                 "and says how you can tell.",
            "success": ["Says the heart is an organ",
                        "Says it contains more than one kind of tissue",
                        "Names at least one tissue in it other than muscle",
                        "States the test: one kind of cell is a tissue, several "
                        "tissues together is an organ"]},
    },

    "key_note": "Cells → tissues → organs → organ systems → organism. A tissue "
                "is similar cells with one job; an organ is different tissues "
                "with one job; a system is organs in a chain. It is about what "
                "works with what, never about size — a pea-sized gland is an "
                "organ and a leg bone is a tissue. Blood is a tissue.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
},

# ══════════════════════════════════════════════════════════════════════════
# L6 — Unicellular organisms (CONTRAST)
# ══════════════════════════════════════════════════════════════════════════
{
    "slug":        "unicellular-organisms",
    "title":       "Unicellular organisms",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "CONTRAST",

    "covers":      ["KS3.B.CELLS.05"],
    "touches":     ["KS3.B.CELLS.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 3},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 45,

    "requires":    ["life-processes", "animal-and-plant-cells"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["biology/cell-biology/eukaryotes-prokaryotes"],

    "big_question": "How can one single cell be a whole living thing?",

    "phenomenon": {
        "kind": "demo",
        "title": "One drop of pond water",
        "prompt": "A drop of pond water under the microscope. A Euglena swims "
                  "past, driven by a whip at one end. An Amoeba flows around a "
                  "piece of food and swallows it whole. A Paramecium hurtles "
                  "across the view covered in tiny beating hairs. Every one of "
                  "them is a single cell, and every one is a whole organism.",
        "commit": "With no mouth, no legs, no lungs and no brain, how many of "
                  "the seven life processes can one cell manage?",
    },

    "misconceptions": [
        {"id": "LIFE-03",
         "statement": "A single cell cannot be a whole living thing — it must be "
                      "part of something bigger.",
         "elicited_by": "how-many-processes",
         "confronted_by": "one-cell-does-all-seven"},
        {"id": "CELL-08",
         "statement": "A single-celled organism is just a simpler version of one "
                      "of our cells — the same parts, doing less.",
         "elicited_by": "same-or-extra",
         "confronted_by": "more-not-fewer"},
    ],

    "vocabulary": [
        {"term": "unicellular",
         "definition": "Made of one single cell, which is the whole organism.",
         "note": None},
        {"term": "multicellular",
         "definition": "Made of many cells, which are usually specialised.",
         "note": "You are multicellular. So is every plant and animal you can "
                 "see without a microscope."},
        {"term": "flagellum",
         "definition": "A long whip that a cell beats in order to swim.",
         "note": "One is a flagellum, several are flagella. You have already met "
                 "one: the tail of a sperm cell."},
        {"term": "cilia",
         "definition": "Short hairs covering a cell's surface, which beat "
                       "together like tiny oars.",
         "note": "One is a cilium. Cilia line your airways too, sweeping dust "
                 "back up out of your lungs."},
    ],

    "figures": [
        {"id": "b1-pond-water-micrograph", "kind": "micrograph",
         "caption": "A field of pond water at ×100 with a Euglena, an Amoeba and "
                    "a Paramecium in view at once.",
         "status": "needed"},
        {"id": "b1-unicellular-adaptations", "kind": "schematic",
         "caption": "Euglena, Amoeba, Paramecium and a bacterium drawn to the "
                    "same scale, each labelled with its structural adaptations.",
         "status": "needed"},
    ],

    # CONTRAST rhythm (§6): lead → predict-gated A/B instrument → parallel
    # compare-cards as static reference → an explanation-chain builder forcing
    # the LINKED comparison → ladder. The A/B is the microscope's specimen
    # control: pond water and human cheek cells, same lens, same lesson —
    # one organism per cell, or one organism made of billions.
    "core": [
        {"type": "hook", "ref": "phenomenon"},
        {"type": "check", "id": "how-many-processes"},
        {"type": "explainer", "id": "all-seven-in-one-cell",
         "text": "All seven. That one cell moves, feeds, senses light, grows, "
                 "gets rid of its waste, reproduces and releases energy from its "
                 "food — with nothing to help it and nothing to specialise into. "
                 "You do all seven as well, but you use billions of cells and "
                 "dozens of organs to manage it. A Paramecium does the lot with "
                 "one cell and some very good equipment."},
        {"type": "misconception", "id": "one-cell-does-all-seven",
         "targets": "LIFE-03"},
        {"type": "practical", "id": "pond-water-lab"},
        {"type": "figure", "ref": "b1-pond-water-micrograph"},
        {"type": "check", "id": "same-or-extra"},
        {"type": "misconception", "id": "more-not-fewer", "targets": "CELL-08"},
        {"type": "figure", "ref": "b1-unicellular-adaptations"},
        {"type": "keyword", "terms": ["unicellular", "multicellular",
                                      "flagellum", "cilia"]},
        {"type": "check", "id": "adaptation-cards"},
        {"type": "check", "id": "one-cell-vs-many"},
        {"type": "quiz", "ref": "ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "stretch": [
        {"type": "explainer", "id": "bacteria-are-different",
         "text": "One group in that drop is built differently again. A bacterium "
                 "has a membrane, cytoplasm and a cell wall — but no nucleus at "
                 "all. Its instructions sit in a loop, floating loose in the "
                 "cytoplasm. It is smaller than everything else on the slide, it "
                 "is far more common than everything else on the slide, and "
                 "there are more bacteria in a teaspoon of soil than there are "
                 "people on Earth."},
        {"type": "check", "id": "bacteria-verdict"},
    ],

    "support": [],

    "activities": [
        {"id": "how-many-processes", "kind": "predict",
         "demand": "elicit LIFE-03 by forcing a commitment on the hook",
         "prompt": "Commit before you read on. How many of the seven life "
                   "processes can a single cell carry out on its own?",
         "options": ["Two or three — one cell cannot possibly do them all",
                     "Six — everything except reproducing",
                     "All seven, in that one cell"],
         "answer": 2,
         "reveal": "All seven. That is what makes it an organism and not just a "
                   "cell.",
         "targets": "LIFE-03"},
        {"id": "one-cell-does-all-seven", "kind": "confrontation",
         "demand": "make the wrongness of LIFE-03 visible",
         "prompt": "The wrong idea, in the words students really write: 'it's "
                   "only one cell, so it must be part of something bigger.' Take "
                   "one of your own cells out and put it in pond water beside "
                   "the Amoeba. Watch both.",
         "reveal": "Your cell dies. It has no way to feed itself, no way to move "
                   "and nothing to sense with, because it has always had the "
                   "rest of you doing those jobs. The Amoeba carries on hunting. "
                   "That is the difference: your cells are specialists that only "
                   "work as a team, and a unicellular organism is a whole "
                   "living thing that happens to be one cell.",
         "targets": "LIFE-03"},
        {"id": "pond-water-lab", "kind": "lab",
         "demand": "investigate",
         "prompt": "Same microscope, two slides. Predict first: you have three "
                   "organisms in view at ×100 and you turn up to ×400. What "
                   "happens to the Paramecium?",
         "options": ["It fills the view and is easier to watch",
                     "It shoots out of view and is very hard to follow",
                     "It stops moving, because the light is stronger"],
         "answer": 1,
         "sim": {"kind": "microscope",
                 "controls": ["specimen", "magnification", "focus"],
                 "readouts": ["total magnification", "field of view",
                              "what you can see"],
                 "specimens": ["pond water", "human cheek cells"],
                 "caption": "Two slides at the same magnifications. One holds "
                            "several whole organisms. The other holds part of "
                            "one."},
         "reveal": "It shoots straight out of view. The field of view is "
                   "smaller, so the same speed crosses it far faster — which is "
                   "exactly what you found with the onion. Now switch to the "
                   "cheek cells at the same magnification and compare. One slide "
                   "has three complete organisms on it. The other has a few "
                   "cells off the inside of somebody's mouth, and none of them "
                   "could live for an hour on their own.",
         "targets": None},
        {"id": "same-or-extra", "kind": "predict",
         "demand": "elicit CELL-08",
         "prompt": "So how does a Euglena compare with one of your cells? "
                   "Commit: does it have fewer parts than yours, the same, or "
                   "more?",
         "options": ["Fewer — it is a simpler, more basic kind of cell",
                     "The same parts, just arranged a bit differently",
                     "More — it has everything yours has, and extra equipment"],
         "answer": 2,
         "reveal": "More. It has a nucleus, cytoplasm and a membrane like yours, "
                   "plus chloroplasts, plus a whip to swim with, plus an eyespot "
                   "to find the light.",
         "targets": "CELL-08"},
        {"id": "more-not-fewer", "kind": "confrontation",
         "demand": "make the wrongness of CELL-08 visible",
         "prompt": "Name the idea out loud: 'single-celled organisms are simple "
                   "— they're basic cells that do less.' Now list what a Euglena "
                   "carries that one of your cells does not: a flagellum, an "
                   "eyespot, chloroplasts. Then list what one of your cells "
                   "carries that a Euglena does not.",
         "reveal": "The second list is empty. Fewer cells does not mean a "
                   "simpler cell — it means the opposite, because everything the "
                   "organism needs has to fit inside that one cell. Your cells "
                   "can afford to be simple. They have thirty trillion "
                   "colleagues.",
         "targets": "CELL-08"},
        {"id": "adaptation-cards", "kind": "reveal-cards",
         "demand": "recall",
         "prompt": "Four organisms, four sets of equipment. Say what the "
                   "structure is for before you tap each card.",
         "cards": [
             {"front": "Euglena · a long whip and a red eyespot",
              "back": "Swims with the flagellum, and steers towards light so its "
                      "chloroplasts can work"},
             {"front": "Amoeba · a shape that flows and changes",
              "back": "Pushes out a false foot to crawl, and wraps the same way "
                      "around its food to swallow it"},
             {"front": "Paramecium · thousands of tiny beating hairs",
              "back": "Cilia row it along fast, and sweep food down a groove "
                      "into the cell"},
             {"front": "Amoeba and Paramecium · a space that swells then empties",
              "back": "A contractile vacuole. Water seeps in all the time, and "
                      "this squeezes it back out again"},
             {"front": "Bacterium · a wall, a loop of instructions, no nucleus",
              "back": "The wall holds its shape; the instructions sit loose in "
                      "the cytoplasm"},
         ]},
        {"id": "one-cell-vs-many", "kind": "construct",
         "demand": "force the linked comparison, not two separate descriptions",
         "prompt": "The hardest job on the page, and it is the one this whole "
                   "lesson is for: a comparison has to say both sides. Complete "
                   "it properly. 'A Paramecium takes in its food using …, but a "
                   "human needs …, because …'",
         "success": ["Says the Paramecium uses cilia and a groove, in one cell",
                     "Says a human needs a whole digestive system of organs",
                     "Says why: the Paramecium is one cell and does everything "
                     "itself",
                     "Mentions BOTH sides in the final clause, not just one"]},
        {"id": "bacteria-verdict", "kind": "construct",
         "demand": "transfer the seven-process test to an unfamiliar organism",
         "prompt": "Use L1's test on something that looks like it might fail it. "
                   "A bacterium has no nucleus, no chloroplasts and no whip, and "
                   "is far too small to see with a school microscope. Decide "
                   "whether it is alive, and justify it against the seven.",
         "success": ["Uses the seven life processes as the test",
                     "Says it feeds, grows, reproduces and gets rid of waste",
                     "Says it is made of a cell — one cell",
                     "Does not use size or having no nucleus as a reason "
                     "against"]},
    ],

    "ladder": {
        "recall": {
            "q": "What does unicellular mean?",
            "options": ["Made of one single cell", "Made of many cells",
                        "Living in water", "Having no nucleus"],
            "answer": 0,
            "feedback": {
                1: "That is multicellular — you, and every plant and animal you "
                   "can see.",
                2: "Plenty of unicellular organisms live in water, but so do "
                   "fish. It is not what the word means.",
                3: "Bacteria have no nucleus, but a Euglena is unicellular and "
                   "has one. (CELL-08)",
            }},
        "apply": {
            "q": "A Euglena has chloroplasts and a flagellum. What can it do "
                 "that an Amoeba cannot?",
            "options": ["Make its own food using light, and swim with a whip",
                        "Change its shape and flow around a piece of food",
                        "Reproduce by dividing itself into two new cells",
                        "Get rid of the waste water that seeps into it"],
            "answer": 0,
            "feedback": {
                1: "That is the Amoeba's own method — a false foot, not a whip.",
                2: "Both of them do that. It is one of the seven processes.",
                3: "Both do that too — the Amoeba has a contractile vacuole as "
                   "well.",
            }},
        "explain": {
            "q": "Explain how one single cell can be a complete living thing, "
                 "when one of your cells could not survive on its own for an "
                 "hour.",
            "success": ["Says the unicellular organism carries out all seven "
                        "life processes itself",
                        "Names at least two structures that let it do so",
                        "Says your cells are specialised for one job each",
                        "Says your cells depend on the rest of the body, and "
                        "mentions both sides of the comparison"]},
        "produce": {
            "q": "A student writes: 'single-celled organisms are simple, because "
                 "they've only got one cell.' Rewrite it so it is correct, and "
                 "say what was wrong with the original.",
            "success": ["Removes 'simple' as a consequence of being one cell",
                        "Says the single cell must do everything itself",
                        "Gives an example of extra equipment it carries",
                        "Identifies the mistake: fewer cells was treated as "
                        "less complicated"]},
    },

    "key_note": "A unicellular organism is one cell that does all seven life "
                "processes by itself, so it carries equipment your cells never "
                "need: a flagellum or cilia to move, a false foot to feed, a "
                "contractile vacuole to bail out water. Fewer cells does not "
                "mean simpler. It means everything has to fit in one.",

    "ws": ["experimental-skills-and-investigations"],
    "review_state": "draft",
},


    ],
}
