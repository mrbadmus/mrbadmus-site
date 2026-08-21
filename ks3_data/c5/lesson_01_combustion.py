"""C5 L1 — Combustion (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c5/c5-01-combustion.dc.html` (703 lines), and her
author's notes `docs/ks3/design-reference/c5/NOTES-C5.md` §1, §2 (the parameter
bench), §3, §4 flags 1–6, §5 (`REACT-10`, `REACT-11`) and §6.

Every student-facing string is byte-identical to the approved page except where
a line is marked ⚠️ RE-AUTHORED below, and every one of those is in the report
with its reason. `RAIL`, `FUELS`, `AIRS`, `CARDS`, `RUNGS` and `SELF_RUNGS` came
out of the node extractor; the hook options and reveal, the two explainer
paragraphs, the bench's dials, its prediction gate, its four readout tiles and
both verdicts, the key fact, the `#s-fuels` lede, the `#s-think` options and
both reveal paragraphs, the fire-triangle reference cards, the key note and both
"Going further" paragraphs were lifted from `lessonVals(s)` and from the markup
— which is where most of this lesson's words live, and where a lift of the
top-level constants alone silently loses them.

── THE SHAPE: A PARAMETER BENCH, AND §5A APPLIED HARD ──────────────────

NOTES-C5 §2: `c5-01` is a **parameter bench** — fuel × air supply — and the dial
that matters is a hole in the side of a burner. Four fuels crossed with two air
settings is EIGHT runs, and all eight are authored below, in full, as separate
records.

⚖️ **THAT IS NOT TIDINESS. DESIGN'S PAGE COMPUTES FIVE READOUTS FROM TWO
BOOLEANS, AND THREE OF THE EIGHT CELLS THAT PRODUCES ARE FALSE.**
`lessonVals()` branches on `complete` (the air hole) and `hasCarbon`, and then
uses `complete` alone for the flame note, the verdict and the soot note. So:

  * **hydrogen, air hole shut** — the flame note reads *"The brightness is
    glowing soot."* on the same row as a soot readout saying *"None — there is
    no carbon in the fuel"*. One panel contradicting itself.
  * **hydrogen, air hole shut** — the verdict reads *"some carbon stopped at
    carbon monoxide, some never reacted at all and came out as soot"*, of a
    fuel with no carbon in it.
  * **charcoal, air hole open** — the flame reads *"Blue, roaring, around
    1500 °C"*. Burning charcoal glows; it does not give a roaring blue flame,
    and a teacher would mark that wrong.

§5A's rule is exactly this: **branch on the thing the lesson teaches — how much
oxygen reaches the flame, and what the fuel is made of — never on a proxy.**
`complete` is a proxy for "there is soot in this flame", and on a carbon-free
fuel the proxy is simply wrong. Enumerating all eight and authoring each one is
what made the three visible; they are corrected here and reported.

⚠️ EMIT-BOTH-SHOW-ONE, AND NOTHING IS COMPUTED. All eight runs' tiles, word
equations and verdicts are in the document at rest and one is unhidden, so no
sentence exists twice and the resting render cannot disagree with the runtime
one. There is no arithmetic in the renderer and none in `wireBurnerBench`.

⚑ SCIENCE FLAGS — NOTES-C5 §4, all six answered in the authoring brief:

  * **flag 1 — blue ≈ 1500 °C, yellow ≈ 1000 °C.** CONFIRMED roughly right for
    a Bunsen. Both figures KEPT, with Design's own "around" / "roughly" hedge,
    on the bench and in the `#s-think` reveal and rung 2's correction.
  * **flag 2 — the yellow flame's brightness is glowing soot.** CORRECT and
    KEPT PLAINLY. That it contradicts the intuition `#s-think` then attacks is
    the POINT: `REACT-10` is precisely "brighter means hotter".
  * **flag 3 — incomplete combustion gives carbon monoxide + carbon + water.**
    CORRECT. Named together rather than staged, exactly as Design wrote it.
  * **flag 4 — charcoal as carbon.** CONFIRMED as a KS3 simplification, and
    ⚠️ THE PAGE NOW SAYS "mostly carbon", NOT "carbon". Design hedges it on the
    fuel card ("Almost pure carbon") and NOT on the bench, where a dial reading
    `Charcoal` sits over a word equation reading `carbon + oxygen`. The two
    charcoal runs carry an `eq_note` saying so; see `_RUNS`.
  * **flag 5 — carbon monoxide and haemoglobin.** CONFIRMED — it binds far more
    strongly than oxygen and does not readily let go. KEPT, and ⚠️ the
    cross-reference to the breathing unit is now NAMED: "The gas exchange
    system", by its title. Never a unit code (§14, no sequence leaks).
  * **flag 6 — hydrogen clean at the flame, not necessarily clean as a fuel.**
    CORRECT TODAY and THE QUALIFICATION IS KEPT WHOLE. MRB-225: teach the
    version that is TRUE, not the famous one. "Hydrogen is clean" is the
    famous one.

⚑ AND ONE FLAG DESIGN DID NOT RAISE, RULED HERE (§18): **the page contradicted
itself about the yellow flame.** The bench's closing panel said "There is no
situation in which you want a yellow flame from a burner", and the `#s-think`
reveal — two sections later — says "The safety flame is yellow so you can see
the burner is lit", which is a situation in which you want one. §14 forbids a
sentence in a lesson body being retracted by a later one in the same lesson.
Fixed at the ABSOLUTE, not at the true statement: see `_BENCH_CLOSE`.

── SAFETY, AND WHY THERE IS A `safety_note` BUT NO CHILDLINE BLOCK ─────

⚖️ **NO CHILDLINE BLOCK, and the reasoning matters more than the answer.** §16's
trigger is a lesson about a student's OWN body, health or circumstances, where a
student might recognise themselves in the page and need a route to help —
reproduction, diet, drugs, smoking. The carbon monoxide paragraph here is a
MECHANISM OF TOXICITY inside a lesson about burning: the same kind of fact as
"pure sodium will set fire to your hand". It invites no disclosure and has no
"if this is about you" shape, so a Childline block would be a safeguarding
signal attached to a chemistry fact — which teaches a student that the signal
means nothing.

⚖️ **A `safety_note` IS A DIFFERENT THING AND THIS LESSON DOES EARN ONE.** It is
the only lesson in C5 with a burner on it, and the page describes two things a
student can repeat at a bench: holding a beaker in a flame until it blacks, and
opening the collar. The note is scoped to exactly those two and to nothing else.
A blanket "never light anything" would retract the lesson's own content, which
is the self-retraction §14 forbids; and it is a foot-of-page line beside the
standing legal one, NOT a callout.
"""

# ── the burner bench: FOUR FUELS × TWO AIR SETTINGS = EIGHT RUNS ────────
#
# §5A, enumerated in full. Every reachable pair of dial values has an authored
# run and no run names a pair the dials cannot reach; `r_burner_bench` refuses
# to build a bench with a hole in it, because a bench with a hole shows the last
# run's numbers under the new run's label.
#
# ⚠️ EVERY NOTE IS KEYED TO WHICH DIALS ARE SET, NEVER TO HOW MANY. There is no
# "you have now tried two things" anywhere in this payload: the flame is what it
# is because of the fuel and the hole, and the panel says so whichever run the
# student reached it by.
#
# The cells are in tile order — flame, energy, beaker, air — and each is
# `{"value", "note"}`. `alert` is the amber ground and it appears on exactly one
# cell, the air one, and only where there is carbon monoxide in the room: see
# the note on it below.
#
# ⚠️ RE-AUTHORED, and every instance is marked. Three kinds:
#   ⚠️1 the four incomplete CARBON runs' energy value, Design's "Less than half
#      wasted as unburnt fuel";
#   ⚠️2 both CHARCOAL runs' flame value and note, Design's Bunsen description;
#   ⚠️3 the HYDROGEN SHUT run's flame note and verdict, Design's `complete`
#      branch, which is false of a fuel with no carbon in it.

# The two verdicts Design writes, byte-identical, used by the six runs they are
# true of. Authored once and referenced so a correction cannot be applied to one
# copy and not another.
_V_COMPLETE = ("Complete combustion. Enough oxygen arrived for every atom in "
               "the fuel to finish reacting, so all of the available energy "
               "came out and nothing was left over.")
_V_INCOMPLETE = ("Incomplete combustion. The fuel still reacted and it did not "
                 "finish: some carbon stopped at carbon monoxide, some never "
                 "reacted at all and came out as soot, and the energy you "
                 "wanted stayed locked in both of them.")

# ⚠️3 NEW PROSE, and it exists because Design's `_V_INCOMPLETE` is FALSE of a
# fuel with no carbon in it — it names soot and carbon monoxide, and hydrogen
# can make neither. Written in the lesson's own logic rather than as an
# exception to it: less oxygen still means less finishes, and the reason there
# is nothing worse in the products is the reason the whole page gives, which is
# that there is no carbon to stop half way.
_V_INCOMPLETE_NO_CARBON = (
    "Incomplete combustion, and without carbon in the fuel it looks quite "
    "different. Less oxygen still means less of the hydrogen finishes "
    "reacting, so less energy comes out — but there is no carbon to stop half "
    "way, so there is no soot and no carbon monoxide. The only product is "
    "still water.")

# ⚠️1 RE-AUTHORED. Design's value is "Less than half wasted as unburnt fuel",
# under a tile labelled "Energy released", and it is wrong twice over.
#
#   * It READS BACKWARDS. Beside a complete run whose value is "All of it",
#     "Less than half wasted" says a minority is lost, which is the opposite of
#     what the tile is reporting and the opposite of what the lesson teaches.
#   * The FRACTION IS FALSE. Burning methane to carbon monoxide and water
#     releases roughly two thirds of what burning it to carbon dioxide does,
#     and stopping at soot roughly a half — so "less than half" overstates the
#     loss even in the worst case, and a real safety flame is nowhere near it.
#
# Both are fixed by removing the number rather than by replacing it with
# another one: the lesson never asks for a figure here and §5A only requires a
# number where the lesson NAMES a quantity. "Wasted as unburnt fuel" is not
# lost — Design's own verdict says it better, in the clause about the energy
# staying locked in the soot and the carbon monoxide.
_E_INCOMPLETE = "Less than the fuel could give"

_RUNS = [
    # ── methane, the Bunsen case, and the one every other run is read against
    {"id": "methane:open",
     "eq_left": "methane + oxygen",
     "eq_right": "carbon dioxide + water",
     "cells": [
         {"value": "Blue, roaring, around 1500 °C",
          "note": "Nothing solid in it to glow."},
         {"value": "All of it", "note": "The reaction finished."},
         {"value": "None — the beaker stays clean",
          "note": "Carbon that never made it to carbon dioxide."},
         {"value": "Nothing harmful from this reaction",
          "note": "No carbon monoxide. Every carbon atom reached carbon "
                  "dioxide."},
     ],
     "verdict": _V_COMPLETE},
    {"id": "methane:shut",
     "eq_left": "methane + oxygen",
     "eq_right": "carbon monoxide + carbon + water",
     "cells": [
         {"value": "Yellow, lazy, around 1000 °C",
          "note": "The brightness is glowing soot."},
         {"value": _E_INCOMPLETE,
          "note": "Unfinished reactions release less."},
         {"value": "Black deposit on the beaker within seconds",
          "note": "Carbon that never made it to carbon dioxide."},
         {"value": "Carbon monoxide", "alert": True,
          "note": "Carbon monoxide: colourless, odourless, and it stops your "
                  "blood carrying oxygen."},
     ],
     "verdict": _V_INCOMPLETE},

    # ── candle wax, the same chemistry in a fuel nobody calls a gas ────────
    {"id": "wax:open",
     "eq_left": "candle wax + oxygen",
     "eq_right": "carbon dioxide + water",
     "cells": [
         {"value": "Blue, roaring, around 1500 °C",
          "note": "Nothing solid in it to glow."},
         {"value": "All of it", "note": "The reaction finished."},
         {"value": "None — the beaker stays clean",
          "note": "Carbon that never made it to carbon dioxide."},
         {"value": "Nothing harmful from this reaction",
          "note": "No carbon monoxide. Every carbon atom reached carbon "
                  "dioxide."},
     ],
     "verdict": _V_COMPLETE},
    {"id": "wax:shut",
     "eq_left": "candle wax + oxygen",
     "eq_right": "carbon monoxide + carbon + water",
     "cells": [
         {"value": "Yellow, lazy, around 1000 °C",
          "note": "The brightness is glowing soot."},
         {"value": _E_INCOMPLETE,
          "note": "Unfinished reactions release less."},
         {"value": "Black deposit on the beaker within seconds",
          "note": "Carbon that never made it to carbon dioxide."},
         {"value": "Carbon monoxide", "alert": True,
          "note": "Carbon monoxide: colourless, odourless, and it stops your "
                  "blood carrying oxygen."},
     ],
     "verdict": _V_INCOMPLETE},

    # ── charcoal, the fuel with no hydrogen in it ──────────────────────────
    #
    # ⚑ FLAG 4, AND THE HEDGE THE BRIEF REQUIRES. The dial says `Charcoal` and
    # the word equation says `carbon + oxygen`; between them they assert that
    # charcoal IS carbon, which it is not. Design hedges this on the fuel card
    # ("Almost pure carbon") and nowhere on the bench, which comes FIRST in the
    # document. `eq_note` is the hedge, said where the claim is made.
    #
    # ⚠️2 RE-AUTHORED FLAME. Design's page gives every carbon fuel with the hole
    # open "Blue, roaring, around 1500 °C" — a Bunsen description, applied to
    # burning charcoal by a branch that only knows `hasCarbon`. Charcoal glows
    # rather than flames, which is a thing a student has SEEN on a barbecue, and
    # printing a roaring blue flame there teaches something false about a fuel
    # the very next section uses as its most dangerous example. No temperature
    # is given because none is claimed: a charcoal fire's temperature depends
    # entirely on the draught, and inventing a figure to fill the slot is the
    # kind of number §5A exists to keep off a page.
    {"id": "charcoal:open",
     "eq_left": "carbon + oxygen",
     "eq_right": "carbon dioxide",
     "eq_note": "Charcoal is mostly carbon, with a little ash and other "
                "substances in it, so the equation is written for the carbon.",
     "cells": [
         {"value": "Orange glow, hardly any flame",
          "note": "The solid itself is glowing, not a gas above it."},
         {"value": "All of it", "note": "The reaction finished."},
         {"value": "None — the beaker stays clean",
          "note": "Carbon that never made it to carbon dioxide."},
         {"value": "Nothing harmful from this reaction",
          "note": "No carbon monoxide. Every carbon atom reached carbon "
                  "dioxide."},
     ],
     "verdict": _V_COMPLETE},
    {"id": "charcoal:shut",
     "eq_left": "carbon + oxygen",
     "eq_right": "carbon monoxide + carbon",
     "eq_note": "Charcoal is mostly carbon, with a little ash and other "
                "substances in it, so the equation is written for the carbon.",
     "cells": [
         {"value": "A dull, dark glow",
          "note": "Less oxygen reaching it means less of it burning."},
         {"value": _E_INCOMPLETE,
          "note": "Unfinished reactions release less."},
         {"value": "Black deposit on the beaker within seconds",
          "note": "Carbon that never made it to carbon dioxide."},
         {"value": "Carbon monoxide", "alert": True,
          "note": "Carbon monoxide: colourless, odourless, and it stops your "
                  "blood carrying oxygen."},
     ],
     "verdict": _V_INCOMPLETE},

    # ── hydrogen, the fuel that breaks the pattern ─────────────────────────
    #
    # ⚠️3 The shut run is where Design's `complete` branch fails outright. Both
    # the flame note and the verdict are re-authored; the flame VALUE, the
    # energy value and note, the beaker value and the air value and note are
    # Design's own no-carbon branch and are byte-identical.
    #
    # ⚠️ THE BEAKER NOTE IS PER-RUN AND NOT FIXED. Design's is the same sentence
    # on all eight — "Carbon that never made it to carbon dioxide" — which under
    # a reading of "None, there is no carbon in the fuel" describes something
    # the fuel does not contain.
    {"id": "hydrogen:open",
     "eq_left": "hydrogen + oxygen",
     "eq_right": "water",
     "cells": [
         {"value": "Almost invisible, very hot",
          "note": "Nothing solid in it to glow."},
         {"value": "All of it", "note": "The reaction finished."},
         {"value": "None — there is no carbon in the fuel",
          "note": "There is no carbon in this fuel to leave behind."},
         {"value": "Nothing harmful from this reaction",
          "note": "No carbon monoxide is possible, whatever the air supply."},
     ],
     "verdict": _V_COMPLETE},
    {"id": "hydrogen:shut",
     "eq_left": "hydrogen + oxygen",
     "eq_right": "water",
     "cells": [
         {"value": "Pale and quiet",
          "note": "Nothing solid in it to glow."},
         {"value": "Nearly all of it",
          "note": "Unfinished reactions release less."},
         {"value": "None — there is no carbon in the fuel",
          "note": "There is no carbon in this fuel to leave behind."},
         {"value": "Nothing harmful from this reaction",
          "note": "No carbon monoxide is possible, whatever the air supply."},
     ],
     "verdict": _V_INCOMPLETE_NO_CARBON},
]

# ⚠️ RE-AUTHORED LAST SENTENCE, AND ONLY THE LAST SENTENCE (§14).
#
# Design's closing panel ends "There is no situation in which you want a yellow
# flame from a burner." Two sections later the `#s-think` reveal says "The
# safety flame is yellow so you can see the burner is lit" — which names a
# situation in which you want exactly that. §14: nothing in a lesson body may be
# retracted by a later sentence in the same lesson.
#
# The absolute is the sentence that changes, not the true one, because the
# safety flame's purpose is real and is the reason a burner has a collar at all.
# The replacement keeps the force and drops only the over-claim: a yellow flame
# is never the flame you HEAT with, and that is what the whole bench has just
# shown. The seam lands as a whole sentence, not a raw string delete.
_BENCH_CLOSE = ("Same fuel, both air settings. Shutting the air off did not "
                "stop the reaction and did not make it hotter — it made "
                "it <strong>unfinished</strong>. Less energy out, soot on the "
                "glass, and carbon monoxide in the room. A yellow flame is "
                "never the flame you heat something with.")

# ── the three fuel cards (Design's `CARDS`, byte-identical) ─────────────
#
# ⚠️ THE OPTIONS ARE THE SAME THREE ON EVERY CARD AND THE ANSWER MOVES. That is
# the exercise: one rule read against three different fuels, so a student who
# has the rule gets all three and a student pattern-matching the buttons gets
# one. MRB-177 measured on the set: 4 / 3 / 2 tokens, correct at 4 on card one
# and 3 and 2 on the other two. Card one is the only set where the correct
# option is longest, by one token and a ratio of 1.33 — inside both thresholds,
# so nothing is re-authored here.
#
# ⚠️ NOTHING MARKS. `answer` reaches no markup: the reply names the products and
# says why, in the same voice whichever button was pressed. It is kept on the
# record so the data knows which reading is right even where the page does not
# need to, and `r_fuel_cards` checks it against the options so that "kept"
# cannot quietly mean "wrong".
_FUEL_OPTIONS = [
    {"id": "both", "label": "Carbon dioxide + water"},
    {"id": "co2", "label": "Carbon dioxide only"},
    {"id": "water", "label": "Water only"},
]

_CARDS = [
    {"id": "f1",
     "name": "Propane, in a camping stove",
     "made": "Made of carbon and hydrogen only. Burned with plenty of air.",
     "answer": "both",
     "eq_left": "propane + oxygen",
     "eq_right": "carbon dioxide + water",
     "why": "Carbon and hydrogen in the fuel, so carbon dioxide and water out. "
            "Every hydrocarbon burned completely gives these two products and "
            "no others."},
    {"id": "f2",
     "name": "Charcoal, on a barbecue",
     "made": "Almost pure carbon. No hydrogen in it at all.",
     "answer": "co2",
     "eq_left": "carbon + oxygen",
     "eq_right": "carbon dioxide",
     "why": "No hydrogen means no water. One product only — which is why "
            "a charcoal barbecue in an enclosed space is so dangerous when the "
            "air runs short and that product becomes carbon monoxide instead."},
    # ⚠️ RE-AUTHORED NAME, TWO WORDS. Design's is "Hydrogen, in a fuel cell
    # bus". A fuel cell is not combustion — it is the same overall reaction run
    # electrochemically, with no flame — and this card sits under a heading
    # reading "Complete combustion, plenty of oxygen", so as drawn the section
    # tells a student that a fuel cell burns its hydrogen. Every product claim
    # on the card is correct and the concrete example is the best one there is,
    # so what changed is the two words that made the claim, and nothing else.
    {"id": "f3",
     "name": "Hydrogen, in a hydrogen-powered bus",
     "made": "No carbon anywhere in the fuel.",
     "answer": "water",
     "eq_left": "hydrogen + oxygen",
     "eq_right": "water",
     "why": "No carbon means no carbon dioxide and no soot. The exhaust is "
            "water. This is the reason hydrogen is interesting, and the reason "
            "the argument about it happens elsewhere — in how the "
            "hydrogen was made."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 216 character for character.
    "slug":        "combustion",
    "title":       "Combustion",
    "discipline":  "chemistry",
    "unit":        "types-of-reaction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.CR.03` names four reaction types in one bullet and the bullet's own
    # order is the clause order; combustion is the first. The full reasoning is
    # written against `KS3.C.CR.03` in `ks3_data/substatements.py` and is not
    # restated or edited here.
    "covers":      ["KS3.C.CR.03a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 4},
                    {"id": "energy", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ `requires` IS THE ARGUMENT'S EDGE, NOT THE PAGE ORDER. Design's "Before
    # this lesson" card links to `symbol-equations-and-balancing`, which is
    # simply the lesson before this one; the real dependency is `word-equations`
    # — every readout on the bench and every fuel card is a word equation, and a
    # student who cannot read reactants, an arrow and products has nothing to
    # read them with. Nothing is lost by saying so: the endmatter renders both
    # neighbours from the unit order, so the symbol-equations lesson is still
    # one click away as "Previous".
    #
    # ⚑ THE BIOLOGY EDGE IS REAL AND IS DECLARED. The stretch layer's first
    # paragraph is a mechanism from the breathing unit, named by its title, and
    # §4.6 requires the dict form the moment an edge crosses a unit boundary.
    #
    # ⚠️ `unit` IS THE UNIT CODE, NOT ITS SLUG. `build_ks3.py:4143` compares the
    # authored value against the target's own `_unit`, which is `"B4"`, and
    # RAISES on a disagreement rather than quietly correcting the href — an
    # authored unit that is wrong is a false statement about where a lesson
    # lives, not a routing detail. The slug there would have failed the build.
    #
    # ⚠️ `why` IS STUDENT-FACING PROSE, NOT AN AUTHORING NOTE. It renders as a
    # `<p>` under the endmatter link (`build_ks3.py:4157`), so it is written as
    # a line for a reader — short, and saying what they would go there for.
    "requires":    ["word-equations"],
    "assumes":     ["chemical-vs-physical-change"],
    "references":  ["symbol-equations-and-balancing",
                    {"unit": "B4",
                     "lesson": "the-gas-exchange-system",
                     "why": "Where carbon monoxide does its harm."}],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A collar of metal at the bottom of a burner decides "
                    "whether the flame is clean and hot or dirty, cool and "
                    "poisonous. Why should a hole in the side matter that "
                    "much?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops, Design's `RAIL` in her order with her ids and her `short`
    # labels. `done_when` restates her own `DONE()` (page lines 452–459) rather
    # than guessing:
    #
    #     s-hook    s.hookChoice !== null
    #     s-burner  Object.keys(s.seen).length >= 2
    #     s-fuels   Object.keys(s.fuelChoices).length >= CARDS.length
    #     s-think   s.thinkChoice !== null
    #     s-ladder  every rung answered and both self-marked rungs checked
    #
    # ⚠️ ONE DEPARTURE, ON `s-burner`, AND IT IS WHY THE VALUE READS "read"
    # RATHER THAN "used". Design's `sawBoth` is `Object.keys(s.seen).length >= 2`
    # and is INDEPENDENT of the prediction gate, so a student who presses both
    # air buttons without ever committing gets the closing summary — "Same
    # fuel, both air settings…" — having read no readout at all, and ticks the
    # stop for it. `wireBurnerBench` requires the prediction as well, so the
    # signal is a student who has READ both runs rather than one who has
    # pressed two buttons. That is what MRB-208 wants a stop to mean.
    #
    # ⚠️ `s-burner` TICKS ON BOTH AIR SETTINGS HAVING BEEN USED, NOT ON EIGHT
    # RUNS. Design's `seen` records the AIR dial only, and she is right: the
    # lesson's claim is about the hole, and a student who has seen one fuel both
    # ways has seen the whole argument. The fuel dial is there so the argument
    # can be tested on a fuel with no hydrogen in it and on a fuel with no
    # carbon at all — which is a different question, and `#s-fuels` is where it
    # is asked and marked.
    #
    # ⚠️ THE FIRE TRIANGLE IS A REFERENCE BLOCK AND GETS NO STOP. It is not in
    # Design's `RAIL` and there is nothing in it a student does, so a stop there
    # could never tick. NOTES-C5 §7 names it as the precedent for exactly this.
    #
    # MRB-208: credit is a RATCHET and nothing is ticked on load. Both
    # instruments ship `data-stage-done="0"`.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two flames",       "done_when": "committed"},
        {"anchor": "s-burner", "short": "BENCH",
         "label": "The burner bench", "done_when": "both_air_settings_read"},
        {"anchor": "s-fuels",  "short": "FUELS",
         "label": "Three fuels",      "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Which is hotter?", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Design's set, byte-identical. MRB-177 measured in the gate's own tokens:
    # 6 / 11 / 7 / 8, correct at 11 against a longest distractor of 8. That is
    # a gap of 3 (the threshold is 4) and a ratio of 1.375 (the threshold is
    # 1.4), so it passes on both and nothing is re-authored. It is the tightest
    # set on the page and the margin is a tenth of a token: anyone shortening
    # option D later must lengthen it again somewhere else.
    #
    # All three distractors are wrong RULES in the correct answer's shape — a
    # thing the collar changes. A (the gas), C (the temperature going in) and D
    # (nothing chemical) are the three answers a class actually gives.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two flames on the same burner. One is clean and roaring. One "
                 "is lazy, yellow and quietly making a poison.",
        "prompt": "Same gas, same tap, same room. The only thing that changed "
                  "was a metal collar at the bottom of the burner. Hold a "
                  "beaker over the yellow one and it comes away black; hold it "
                  "over the blue one and it stays clean.",
        "commit": "What is the collar changing?",
        "options": [
            "How much gas reaches the flame",
            "How much air, and so how much oxygen, reaches the gas",
            "The temperature of the gas going in",
            "Nothing chemical — only the shape of the flame",
        ],
        "reveal": "How much <strong>air</strong> — and therefore how much "
                  "oxygen — reaches the gas. With plenty of oxygen every "
                  "carbon atom in the fuel ends up in carbon dioxide. With too "
                  "little, some of them end up as soot and some as "
                  "<strong>carbon monoxide</strong>, which is colourless, has "
                  "no smell, and is the reason gas boilers are serviced by law.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ ALL FOUR JOINS RESOLVE TO SOMETHING THE PAGE ACTUALLY EMITS
    # (MRB-244/248). Checked against the emitted markup, not against intent:
    #
    #   REACT-10  elicited_by   "think-commit-yellow"  → the `#s-think`
    #             confronted_by "think-commit-yellow"    activity's own id,
    #                                                    emitted as
    #                                                    data-activity="think-commit-yellow"
    #   REACT-11  elicited_by   "gate-air-shut"        → id="gate-air-shut" on
    #                                                    the bench's prediction
    #                                                    gate, emitted by
    #                                                    `r_burner_bench` from
    #                                                    `predict.gate_id`
    #             confronted_by "shut-hole-run"        → the burner bench's
    #                                                    activity id, emitted as
    #                                                    data-activity="shut-hole-run"
    #
    # ⚠️ `REACT-10` NAMES ONE ACTIVITY TWICE, DELIBERATELY, AND NOT AS A
    # SHORTCUT. NOTES-C5 §5 proposes `think-commit-yellow` / `think-reveal-soot`.
    # `build_ks3.py` emits a confrontation's reveal as
    # `<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>` with NO
    # `id`, so a `think-reveal-*` name has nothing on the page to point at and
    # CANNOT be made to resolve from inside a content lane. The register's own
    # note under `REACT` says so and records the engine fix as open. So the join
    # names the ACTIVITY that owns both the commitment and the reveal, which is
    # what c3-03's `MIX-06` and c4-01's `REACT-01` do and what satisfies Law 3.
    #
    # ⚠️ `REACT-11`'s `confronted_by` IS `shut-hole-run`, NOT NOTES' `burner-bench`.
    # `burner-bench` is the FAMILY name — what the renderer is — and the
    # activity is named for what it DOES to the belief, exactly as c4-04's bench
    # is `sealed-flask-run` rather than `mass-bench`. Running the same fuel with
    # the hole shut and reading a COOLER flame, less energy and a poison is the
    # confrontation, and it is a real activity id, which Law 3 requires of at
    # least one entry. Reported to the commander as a divergence from NOTES.
    #
    # ⚠️ `statement` IS THE LINE THE PAGE QUOTES for `REACT-10` (page line 216),
    # not the register's shorter handle — `r_confrontation` prints `statement`
    # and Design's is the one a student says out loud. `REACT-11` is quoted
    # nowhere on the page, so it keeps the register's wording.
    "misconceptions": [
        {"id": "REACT-10",
         "statement": "The big yellow flame is hotter — you can see more "
                      "fire.",
         "elicited_by": "think-commit-yellow",
         "confronted_by": "think-commit-yellow"},
        {"id": "REACT-11",
         "statement": "Shutting the air off makes a flame burn hotter or more "
                      "fiercely.",
         "elicited_by": "gate-air-shut",
         "confronted_by": "shut-hole-run"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 100–103 — the two definitions the rest of the lesson uses.
        # Two paragraphs, so two blocks: `r_explainer` draws one <p>.
        {"type": "explainer",
         "text": "<strong>Combustion</strong> is a fuel reacting with oxygen "
                 "and giving out energy. Nothing burns without oxygen, which "
                 "is why a jar over a candle puts it out — and why a "
                 "rocket leaving the atmosphere has to carry its own oxygen "
                 "with it."},
        {"type": "explainer",
         "text": "When there is enough oxygen for the reaction to finish, it "
                 "is <strong>complete combustion</strong>. When there is not, "
                 "it is <strong>incomplete combustion</strong>, and the "
                 "products are different — worse in every way."},

        # ── #s-burner — the flagship. Light `ks3-block` → `check`. ─────────
        #
        # Measured off Design's own markup (page line 106):
        # `class="ks3-block"` and nothing else. There is no ink-dark practical
        # block anywhere in C5, exactly as there is none in C3 or C4.
        #
        # Its ACTIVITY id is `shut-hole-run`; see the misconception note.
        {"type": "burner-bench", "id": "shut-hole-run", "anchor": "s-burner",
         "eyebrow": "Your turn · the burner bench",
         "heading": "Pick a fuel, set the air supply, and see what comes out",
         "demand": "investigate",
         # ⚠️ THE FIRST OPTION OF EACH DIAL IS THE RESTING STATE, which is
         # Design's own opening state (`fuel: 'methane', air: 'open'`) expressed
         # as a property of the payload rather than as two strings written down
         # a second time in the renderer and a third time in the JS.
         #
         # ⚠️ `tracks_done` MARKS THE DIAL THE RAIL STOP WATCHES. Design's
         # `seen` records air settings only, so the stop ticks when both of THIS
         # dial's options have been used. Saying which dial rather than counting
         # presses is §5A's "key to WHICH controls are active, never how many".
         "dials": [
             {"id": "fuel", "label": "The fuel",
              "options": [{"id": "methane", "label": "Methane"},
                          {"id": "wax", "label": "Candle wax"},
                          {"id": "charcoal", "label": "Charcoal"},
                          {"id": "hydrogen", "label": "Hydrogen"}]},
             {"id": "air", "label": "The air supply", "tracks_done": True,
              "options": [{"id": "open", "label": "Air hole open"},
                          {"id": "shut", "label": "Air hole shut"}]},
         ],
         # Law 4: the readouts are not shown until the student has said what
         # they expect. The gate is asked ONCE, about the shut hole, because
         # that is the one prediction the whole bench exists to test.
         #
         # ⚠️ `gate_id` IS `REACT-11`'s `elicited_by` AND IT IS EMITTED AS A REAL
         # `id`. It is authored here rather than written into the renderer so a
         # second lesson using this family cannot emit a duplicate id.
         #
         # ⚠️ TWO DISTRACTORS RE-AUTHORED FOR LENGTH PARITY (MRB-177 / §13).
         # Design's set ran 6 / 9 / 5 tokens with the correct answer at 9 —
         # 1.8× the shortest and 1.5× the longest distractor, which fails the
         # gate's ratio threshold and is a set a student can score without
         # reading. **Fixed AT THE DISTRACTOR, exactly as the ruling requires**:
         # the correct option is byte-identical to Design's, and A and C were
         # rewritten as WRONG RULES IN ITS OWN SHAPE — a product clause, then a
         # clause about the flame. All three now run 9 / 9 / 9.
         #
         # Both rewrites carry `REACT-11` on purpose, from its two sides: A is
         # the student who thinks shutting the air only turns the heat down, C
         # is the student who thinks it concentrates the gas and burns hotter.
         # This gate is `REACT-11`'s elicitation, so its distractors should be
         # the belief rather than filler.
         "predict": {
             "gate_id": "gate-air-shut",
             "prompt": "Before you light it: with the air hole shut, what will "
                       "be in the products that was not there before?",
             "options": [
                 "Nothing new, and a flame that gives less heat",
                 "Soot, and a gas that is colourless and poisonous",
                 "More carbon dioxide, and a flame that burns hotter",
             ]},
         # The four readout tiles, in Design's order. Only `label` is fixed —
         # every value and every note is the RUN's, because a note that is the
         # same sentence on all eight runs is a note describing something other
         # than what is on screen. See the hydrogen runs.
         "tiles": [
             {"id": "flame", "label": "The flame"},
             {"id": "energy", "label": "Energy released"},
             {"id": "soot", "label": "Beaker held over the flame"},
             {"id": "air", "label": "In the air around it"},
         ],
         "eq_label": "The word equation for this run",
         "runs": _RUNS,
         "close": _BENCH_CLOSE},

        # ⚑ THE KEY FACT, AND ITS MIDDLE SENTENCE IS RE-AUTHORED (§14, §18).
        #
        # Design's reads "With enough oxygen the products are carbon dioxide and
        # water." The very next section shows two fuels for which that is false
        # — charcoal gives carbon dioxide and nothing else, hydrogen gives water
        # and nothing else — so the photographable line would be contradicted by
        # the page under it, which is the retraction §14 forbids.
        #
        # The fix is not a hedge, it is the rule the lesson actually teaches,
        # and it is already on the page twice: it is the key note's own wording
        # and it is the `#s-fuels` lede word for word ("every carbon atom in the
        # fuel ends up in carbon dioxide, and every hydrogen atom ends up in
        # water"). Written this way it is true of all four fuels on the bench,
        # and the three sections now agree instead of two of them disagreeing.
        {"type": "key-fact", "ref": "what-the-air-hole-decides"},

        # ── #s-fuels — one rule, three fuels. Light `ks3-block` → `check`. ──
        {"type": "fuel-cards", "id": "three-fuels", "anchor": "s-fuels",
         "eyebrow": "Three fuels · predict the products",
         "heading": "Complete combustion, plenty of oxygen. What comes out?",
         "demand": "construct",
         "prompt": "One rule does all three: every carbon atom in the fuel "
                   "ends up in carbon dioxide, and every hydrogen atom ends up "
                   "in water. Read the fuel, commit, then check.",
         "options": _FUEL_OPTIONS,
         "cards": _CARDS},

        # ── #s-think — REACT-10. The misconception shell, amber. ───────────
        {"type": "misconception", "id": "think-commit-yellow",
         "anchor": "s-think", "targets": "REACT-10"},

        # ── the fire triangle. A REFERENCE BLOCK, so NO anchor and NO stop. ──
        #
        # ⚠️ RENDERED AS A `rule` BLOCK, AND THAT IS A MAPPING RATHER THAN A
        # REDESIGN. Design draws three inset cards in a grid under an eyebrow
        # and an <h2>, with one closing paragraph. The §5.1.1 vocabulary is
        # CLOSED, `comparison` takes exactly two columns and raises on a third,
        # and a third instrument family is not what this is — nothing in it is
        # done, so nothing in it could tick. `rule` is the block that has
        # exactly this shape: eyebrow, a statement, a card grid, a closing line.
        # Every string is Design's and the structure is hers; what changes is
        # that the heading becomes the panel's statement and is set larger.
        {"type": "rule", "id": "three-things-a-fire-needs",
         "eyebrow": "Reference · three things a fire needs",
         "statement": "Take away any one of them and it stops",
         "cards": [
             {"term": "Fuel",
              "gloss": "A firebreak clears the fuel out of the way so a "
                       "wildfire has nothing to reach."},
             {"term": "Oxygen",
              "gloss": "A fire blanket, a pan lid or a carbon dioxide "
                       "extinguisher cuts the air off."},
             {"term": "Heat",
              "gloss": "Water cools the fuel below the temperature at which "
                       "it can keep going."},
         ],
         "close": "Never water on a chip-pan fire or on an electrical fire: "
                  "hot oil throws burning droplets everywhere, and water "
                  "conducts. Cutting off the oxygen is the move in both cases."},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None, and not by omission. NOTES-C5 §6 is explicit that all five C5
    # instruments are DOM with no canvas, and this page draws no diagram: the
    # fire triangle is three cards of words, and the flame comparison is a
    # READOUT that changes with the dials, so drawing it would be a second,
    # frozen copy of something the instrument already shows and could disagree
    # with. A figure invented here would be a picture Design did not draw
    # carrying an assertion nothing checks against the bench.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "what-the-air-hole-decides",
         "text": "Combustion is a fuel reacting with oxygen and giving out "
                 "energy. With enough oxygen the carbon in the fuel ends up as "
                 "carbon dioxide and the hydrogen ends up as water. With too "
                 "little, some carbon comes out as soot and some as carbon "
                 "monoxide, and less energy is released.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instruments are lifted out of `core` into this
    # list by `_normalise()` and are never authored here.
    #
    # ⚠️ THREE DISTRACTORS RE-AUTHORED FOR LENGTH PARITY (MRB-177 / §13).
    # Design's set ran 6 / 13 / 7 / 8 tokens with the correct answer at 13 —
    # strictly longest by 5 words and by 1.6×, which fails the gate on both
    # thresholds. **Fixed AT THE DISTRACTOR**: the correct option is
    # byte-identical to Design's, and A, C and D were rewritten as WRONG RULES
    # IN ITS OWN SHAPE — a verdict, then a claim about which flame is hotter,
    # then a claim about what the brightness is. They now run 14 / 13 / 12 / 13,
    # so the correct answer is not the longest at all.
    #
    # Each rewrite is a rule a real student holds. A is `REACT-10` itself, said
    # in full. C is the physics-flavoured version, and it is wrong twice over —
    # blue light carries MORE energy per photon than yellow, not less. D is
    # Design's own "they are the same temperature, only the size changed".
    "activities": [
        {"id": "think-commit-yellow",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-10",
         "prompt": "It is taller, brighter and looks far more like a fire. "
                   "Commit before you read on.",
         "options": [
             "Right — the yellow flame is hotter; the brightness is heat "
             "you can see",
             "Wrong — the blue flame is hotter; the yellow glow is "
             "glowing soot",
             "Right — yellow light carries more energy; the colour is the "
             "temperature",
             "Wrong — both flames are the same temperature; only the size "
             "has changed",
         ],
         # ⚑ Flags 1 and 2 are both in the first paragraph and both are KEPT
         # PLAINLY, with Design's own "around" and "roughly". That the second
         # sentence contradicts the intuition the block is attacking is the
         # point of the block.
         "reveal": [
             "The blue flame is the hot one — around 1500 °C at its "
             "tip, against roughly 1000 °C for the yellow. What you can "
             "see in the yellow flame is <strong>glowing soot</strong>: "
             "unburnt carbon, hot enough to give off light but not burning. "
             "The brightness is the fuel being wasted, and the soot lands on "
             "whatever you were trying to heat.",
             "Which is why the blue flame is almost invisible. There is "
             "nothing solid left in it to glow — every carbon atom has "
             "already made it to carbon dioxide. <strong>In a flame, visible "
             "is not the same as hot.</strong> The safety flame is yellow so "
             "you can see the burner is lit; the working flame is blue because "
             "it is finishing the job.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce.
    #
    # All four of her headings are the engine's own defaults character for
    # character — "Recall", "The one that catches people", "Explain", "Take it
    # somewhere new" — so none of the four authors a `title`.
    #
    # ⚠️ Length measured on both marked rungs (MRB-177), in the gate's own
    # tokens. Rung 1: 4 / 4 / 3 / 4, correct at 4 and TIED with two distractors,
    # so it is not strictly longest and the set passes. Rung 2: 10 / 16 / 15 /
    # 13, correct is the SHORTEST. Neither needed a distractor rewritten and
    # both are Design's byte for byte.
    #
    # Rung 2 is `REACT-10` and `REACT-11` asked as an exam would ask them: its
    # option C is the misconception the `#s-think` block has just confronted,
    # and its option B is the other half — the belief that the gas tap and the
    # collar do the same job.
    "ladder": {
        "recall": {
            "q": "What are the products of the complete combustion of a fuel "
                 "containing carbon and hydrogen?",
            "options": [
                "Carbon dioxide and water",
                "Carbon monoxide and water",
                "Carbon dioxide only",
                "Soot and water vapour",
            ],
            "answer": 0,
            "feedback": {
                1: "Carbon monoxide is a product of incomplete combustion, "
                   "when the oxygen supply is short.",
                2: "The hydrogen in the fuel has to go somewhere, and it goes "
                   "into water.",
                3: "Soot means carbon that never finished reacting. With "
                   "enough oxygen there is none.",
            }},
        "apply": {
            "q": "A Bunsen burner is giving a tall yellow flame. What does "
                 "that tell you?",
            "options": [
                "Not enough air is getting in, so combustion is incomplete",
                "Turning the gas up makes the flame taller, so the colour "
                "follows the amount of fuel",
                "A bigger, brighter flame is a hotter flame, so the yellow one "
                "is burning more fiercely",
                "Yellow means the gas supply is contaminated, so the colour "
                "comes from the impurity",
            ],
            "answer": 0,
            "feedback": {
                1: "The gas tap changes the size of the flame. The colour is "
                   "about air, and yellow means too little of it.",
                2: "The blue flame is hotter, at around 1500 °C. The "
                   "yellow glow is soot, and soot is wasted fuel.",
                3: "Same gas, both flames. Open the air hole and the yellow "
                   "flame becomes blue immediately.",
            }},
        "explain": {
            "q": "A gas fire is burning with a yellow flame and there is black "
                 "marking on the wall above it. Explain what is going wrong "
                 "chemically, why it is dangerous, and why the danger cannot "
                 "be detected by smell.",
            "field_label": "Your explanation",
            "placeholder": "The yellow flame shows that…",
            "success": [
                "Says the yellow flame and soot show incomplete combustion.",
                "Says there is not enough oxygen for all the carbon to become "
                "carbon dioxide.",
                "Names carbon monoxide as a product of incomplete combustion.",
                "Says carbon monoxide is colourless and has no smell, so it "
                "gives no warning.",
                "Says less energy is released as well, so the fire is also "
                "wasting fuel.",
            ]},
        "produce": {
            "q": "A rocket has to burn its fuel hundreds of kilometres above "
                 "the Earth, where there is effectively no air. A candle in a "
                 "sealed jar goes out within seconds. Use the same idea to "
                 "explain both, and say what a rocket must therefore carry.",
            "field_label": "Your answer",
            "placeholder": "Combustion needs…",
            "success": [
                "Says combustion needs oxygen as a reactant, not just fuel.",
                "Explains the candle: the oxygen in the sealed jar is used up, "
                "so the reaction stops.",
                "Says there is no oxygen in space for a rocket to react with.",
                "Says the rocket must carry its own supply of oxygen, or "
                "another oxidiser.",
                "Notes that this is why the fuel alone is not enough, however "
                "much of it there is.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Design's, byte-identical. It is also the wording the key fact above was
    # corrected TO, so the two cannot disagree.
    "key_note": "Combustion is a fuel reacting with oxygen, giving out energy. "
                "Complete combustion — plenty of oxygen — turns the "
                "carbon in the fuel into carbon dioxide and the hydrogen into "
                "water, and releases all the available energy. Incomplete "
                "combustion, with too little oxygen, leaves soot and produces "
                "carbon monoxide, and releases less. A yellow flame is the "
                "visible warning; the poison is not visible at all.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ FLAG 5 is the first paragraph and it is KEPT. Carbon monoxide binds to
    # haemoglobin far more strongly than oxygen does and does not readily let
    # go, which is exactly what Design wrote.
    #
    # ⚠️ ONE CLAUSE ADDED, AND IT IS THE CROSS-REFERENCE THE BRIEF REQUIRES.
    # Design's paragraph says the reason "belongs to biology" and then never
    # says where. The breathing lesson is named BY ITS TITLE — "The gas exchange
    # system" — and never by a unit code: §14 forbids a sequence leak in
    # student-facing prose, and "B4" is exactly that.
    #
    # ⚑ FLAG 6 is the second paragraph and THE QUALIFICATION IS KEPT WHOLE.
    # MRB-225: teach the version that is TRUE, not the famous one. "Hydrogen is
    # clean" is the famous one, and the honest version — clean at the flame, not
    # necessarily clean as a fuel, because most of it is made from natural gas —
    # is both correct today and the more useful thing to know. Byte-identical.
    "stretch": [
        {"type": "explainer", "id": "carbon-monoxide-and-blood",
         "text": "Carbon monoxide is dangerous for a reason that belongs to "
                 "biology, and you meet it properly in <em>The gas exchange "
                 "system</em>. It sticks to the haemoglobin in your red blood "
                 "cells far more strongly than oxygen does, and it does not "
                 "let go — so the blood keeps circulating while carrying "
                 "less and less oxygen. There is no smell and no taste, and "
                 "the early symptoms are a headache and tiredness, which is "
                 "exactly what you would ignore. A boiler burning with a "
                 "yellow flame instead of a blue one is producing it, which is "
                 "why the servicing is a legal requirement rather than a "
                 "suggestion."},
        {"type": "explainer", "id": "a-clean-flame-is-not-a-clean-fuel",
         "text": "Hydrogen is the fuel that breaks the pattern: it contains no "
                 "carbon at all, so complete combustion gives water and "
                 "nothing else — no carbon dioxide, no soot, no carbon "
                 "monoxide. That is the whole appeal of a hydrogen car. The "
                 "catch is not in the burning; it is that hydrogen has to be "
                 "made first, and most of it today is made from natural gas, "
                 "which releases carbon dioxide somewhere else. A clean flame "
                 "is not the same as a clean fuel, and knowing where to look "
                 "is the difference."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent. Design
    # draws no "Need a hand?" layer on this page, and the scaffolding a
    # struggling student needs is already the lesson's spine: the bench lets the
    # same fuel be run both ways as many times as they like, and `#s-fuels`
    # states the rule in full immediately above the three cards it is used on.
    "support": [],

    # ── vocabulary (§10.2, §12) ─────────────────────────────────────────────
    # ⚠️ `definition` + `note`, not `gloss`. The build contract's §12 names the
    # key `gloss`; the SHIPPED schema is `{"term", "definition", "note"}` — that
    # is what `r_cards` reads (build_ks3.py:922) and what every live lesson
    # authors. Authored to the shipped spelling so the terms reach the unit
    # page's "Words this unit gives you" chips and the reading-age gate's
    # exclusion list.
    #
    # Design draws no keyword block on this page, so none of these definitions
    # reaches the lesson body — the list is the lesson's term record.
    #
    # `Hydrocarbon` is here because the page uses it once, in fuel card one's
    # reply, without ever defining it: "Every hydrocarbon burned completely
    # gives these two products and no others."
    "vocabulary": [
        {"term": "Combustion",
         "definition": "A reaction in which a fuel reacts with oxygen and "
                       "gives out energy.",
         "note": "Burning is the everyday word for it. Nothing burns without "
                 "oxygen."},
        {"term": "Fuel",
         "definition": "A substance burned to release energy.",
         "note": None},
        {"term": "Complete combustion",
         "definition": "Combustion with enough oxygen for the reaction to "
                       "finish, so all the available energy is released.",
         "note": "The carbon in the fuel ends up as carbon dioxide and the "
                 "hydrogen ends up as water."},
        {"term": "Incomplete combustion",
         "definition": "Combustion with too little oxygen, so the reaction "
                       "does not finish.",
         "note": "It makes soot and carbon monoxide and releases less energy. "
                 "A yellow flame from a burner is the warning sign."},
        {"term": "Carbon monoxide",
         "definition": "A colourless, odourless, poisonous gas made when a "
                       "fuel containing carbon burns without enough oxygen.",
         "note": "It stops the blood carrying oxygen, and there is nothing to "
                 "smell."},
        {"term": "Soot",
         "definition": "Carbon from a fuel that never finished reacting, left "
                       "behind as a black solid.",
         "note": "It is what makes a yellow flame bright, and it is wasted "
                 "fuel."},
        {"term": "Hydrocarbon",
         "definition": "A compound made of carbon and hydrogen only.",
         "note": "Methane, propane and candle wax are all hydrocarbons, which "
                 "is why all three burn to the same two products."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚖️ EARNED, AND SCOPED TO THE TWO THINGS THE PAGE DESCRIBES A STUDENT
    # DOING. This is the only lesson in C5 with a burner on it, and the page
    # describes holding a beaker in a flame until it blacks and opening the
    # collar — both of which a student repeats at a bench that week.
    #
    # ⚠️ IT DOES NOT RETRACT THE LESSON. A blanket "never light anything" would
    # take back the page's own content, which is the self-retraction §14
    # forbids; and it says the yellow flame HAS a job, which is what the
    # `#s-think` reveal says and what the bench's closing line was corrected to
    # agree with. Small, at the foot, beside the standing legal line, and not a
    # callout — a safety note is a different thing from a safeguarding block
    # (§16), and the reasoning for there being no safeguarding block on this
    # lesson is in the module docstring.
    "safety_note": "Anything held in a flame stays hot long after it stops "
                   "looking it, and glass shows nothing at all — the "
                   "sooted beaker is moved with tongs and left to cool. Open "
                   "the collar only while you are actually heating something, "
                   "and turn the burner back to the yellow flame as soon as "
                   "you stop, so that everyone can see it is lit.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the blue flame is the hot one?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Fuels, the atmosphere and pollutants, and combustion as an "
                   "exothermic reaction with a reaction profile.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `experimental-skills-and-investigations` because the bench is a two-dial
    # controlled comparison — the same fuel, one thing changed — and
    # `analysis-and-evaluation` because what the student reads off it is four
    # observations that only mean something read against the other run.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
