"""C6 L4 — Acid + metal (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-04-acids-and-metals.dc.html` (648 lines), and
her author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §1, §3, §4, §5
flags 11 and 12, §6 (`ACID-07`) and §7.

⚠️ THE TITLE AND SLUG ARE `structure.py`'s, NOT THE PAGE'S. Design's page is
headed "Acids and metals"; the skeleton's slot is `acid-plus-metal` / "Acid +
metal". The slug is permanent (§8.4) and the title is what every index,
breadcrumb and rail link already prints. Nothing else moves.

── THE FAMILY IS `acid-metal-grid`, NOT `reactivity-grid` ──────────────

NOTES-C6 §4 names this instrument `reactivity-grid`, reusing C5-04's. That name
and its shell class `ks3-rgrid-block` are OWNED by `ks3_art/c5.py`, and
MRB-279's gate exists because two families wearing one shell class puts one
unit's stylesheet on the other unit's instrument and does it silently — both
pages still render and only a browser open on the other page would show it. So
C6 registers its own `acid-metal-grid` / `ks3-amgrid-block` / `amgrid`. Same
shape, own family, and c5's is neither reused nor edited.

── EIGHT CELLS, ALL AUTHORED, NONE COMPOSED ────────────────────────────

Design's page builds every cell's explanation at run time out of the metal's
name and the acid's salt ending — one sentence serving six cells, plus a
hard-coded copper paragraph for the other two. Reproducing that would put a
metal's name into a sentence by string surgery, make the two copper cells
literally the same paragraph, and make `<strong>` impossible.

All eight are authored instead, and `r_acid_metal_grid` checks the rule the
generator encoded, on every one of them (§5A — enumerate the whole state space,
and carry a content-truth assertion walking every element rather than a sample):

  · the eight cells cover metals x acids exactly, with no hole and no surplus;
  · WHETHER A METAL REACTS IS A PROPERTY OF THE METAL, so a metal's two cells
    must agree — one that fizzed in hydrochloric acid and sat still in sulfuric
    would contradict the reactivity series the whole page argues from;
  · at least one metal does nothing at all, because without a negative row
    there is no rule, only six examples;
  · a reacting cell's products name that acid's own salt ending AND name
    hydrogen — `acid + metal makes salt + hydrogen`, asserted rather than
    stated once and hoped for;
  · a non-reacting cell carries no equation, because writing products for a
    reaction that never happens is exactly what rung 2 is about.

── SCIENCE FLAGS ───────────────────────────────────────────────────────

⚑ Flag 11 — iron chloride and iron sulfate left unspecified as to oxidation
state. KEPT, matching the C5 flag-11 convention. "Iron chloride" is what a KS3
student writes and the number in brackets is a GCSE distinction; naming it here
would introduce a notation the page never explains.

⚑ Flag 12 — copper with acid gives no reaction, justified by the reactivity
series from C5-04. KEPT, and the cross-reference is deliberate: `references`
names `displacement`, and the closing panel says the order the grid produces IS
the reactivity series arrived at by a different route.

⚑ THE THIRD JUDGEMENT IS A REAL HAZARD, NOT A TRICK. Holding a lit splint over
a tube that is still producing hydrogen is a bang rather than a squeak, and
Design's own lead says so before the student commits. Kept whole, and it is
also what the `safety_note` at the foot points at.

── CONTAINMENT ─────────────────────────────────────────────────────────

The grid scrolls sideways at 390px. Every cell button's accessible name is an
`aria-label` ATTRIBUTE rather than a visually-hidden span, so there is not one
absolutely positioned element inside that scroller — which is the exact defect
that widened five C5 pages by 140px. See `r_acid_metal_grid`'s docstring.
"""

# ── the four metals and the two acids (Design's `METALS` and `ACIDS`) ───
#
# In her order, which is the reactivity order and is the order the grid is
# meant to be READ down: magnesium, zinc, iron, copper. Copper is last because
# it is the row that proves the rule.
_METALS = [
    {"id": "mg", "name": "Magnesium"},
    {"id": "zn", "name": "Zinc"},
    {"id": "fe", "name": "Iron"},
    {"id": "cu", "name": "Copper"},
]

# ⚑ Flag 11: the salt endings carry no oxidation state. "Iron chloride" is the
# KS3 name and the bracketed number is a GCSE distinction the page does not
# explain.
_ACIDS = [
    {"id": "hcl", "name": "hydrochloric acid", "salt": "chloride"},
    {"id": "h2so4", "name": "sulfuric acid", "salt": "sulfate"},
]

# ── the eight tubes, every one authored ─────────────────────────────────
#
# ⚠️ `aria` IS THE TUBE'S IDENTITY AND NOTHING ELSE. Design's page composes an
# aria-label that changes with the cell's state — "…: reaction", "…: not yet
# run" — which is a sentence assembled in JavaScript and a second copy of what
# the panel below already says. The accessible NAME of a button is what the
# button IS; the RESULT is announced in the readout, which is where a screen
# reader is taken next. So the label is constant and the panel does the
# reporting.
#
# `mark` is what the cell reads once it has been run. Nothing marks: "fizzes"
# and "none" are observations, not verdicts, and neither carries a colour that
# means right or wrong.
_CELLS = [
    {"id": "mg:hcl", "reacts": True, "mark": "fizzes",
     "aria": "Magnesium in hydrochloric acid",
     "title": "Magnesium in hydrochloric acid",
     "setup": "A measured strip of magnesium dropped into 10 cm³ of dilute "
              "hydrochloric acid at room temperature.",
     "result": "Vigorous. Bubbles stream off and the tube becomes hot to "
               "hold. Over in under a minute.",
     "why": "Magnesium is high above hydrogen in the reactivity series, so it "
            "takes the hydrogen's place in the acid without hesitating. The "
            "hydrogen is pushed out as a gas and the magnesium ends up "
            "dissolved as magnesium chloride — which is why the strip "
            "disappears and the liquid stays clear.",
     "eq_left": "hydrochloric acid + magnesium",
     "eq_right": "magnesium chloride + hydrogen"},
    {"id": "mg:h2so4", "reacts": True, "mark": "fizzes",
     "aria": "Magnesium in sulfuric acid",
     "title": "Magnesium in sulfuric acid",
     "setup": "A measured strip of magnesium dropped into 10 cm³ of dilute "
              "sulfuric acid at room temperature.",
     "result": "Vigorous again, and just as fast. The tube warms and the "
               "strip is gone within the minute.",
     "why": "The same metal doing the same thing, because the reactivity "
            "series does not care which acid the hydrogen came out of. What "
            "changes is the salt left behind: sulfuric acid gives a sulfate, "
            "so this tube ends up holding magnesium sulfate.",
     "eq_left": "sulfuric acid + magnesium",
     "eq_right": "magnesium sulfate + hydrogen"},
    {"id": "zn:hcl", "reacts": True, "mark": "fizzes",
     "aria": "Zinc in hydrochloric acid",
     "title": "Zinc in hydrochloric acid",
     "setup": "Measured zinc granules dropped into 10 cm³ of dilute "
              "hydrochloric acid at room temperature.",
     "result": "Steady. A constant stream of small bubbles and a tube that "
               "warms gently over several minutes.",
     "why": "Zinc is above hydrogen too, but not as far above it as magnesium "
            "— so the same reaction runs at a pace you can watch rather than "
            "one you have to catch. The salt is zinc chloride.",
     "eq_left": "hydrochloric acid + zinc",
     "eq_right": "zinc chloride + hydrogen"},
    {"id": "zn:h2so4", "reacts": True, "mark": "fizzes",
     "aria": "Zinc in sulfuric acid",
     "title": "Zinc in sulfuric acid",
     "setup": "Measured zinc granules dropped into 10 cm³ of dilute sulfuric "
              "acid at room temperature.",
     "result": "Steady, the same as with the other acid. Small bubbles, "
               "several minutes, a tube that warms.",
     "why": "This is the tube a school uses when it wants a jar of hydrogen: "
            "fast enough to fill one and slow enough to control. The salt is "
            "zinc sulfate, and it is the same zinc sulfate whether you make "
            "it from the metal or from zinc oxide.",
     "eq_left": "sulfuric acid + zinc",
     "eq_right": "zinc sulfate + hydrogen"},
    {"id": "fe:hcl", "reacts": True, "mark": "fizzes",
     "aria": "Iron in hydrochloric acid",
     "title": "Iron in hydrochloric acid",
     "setup": "Measured iron filings dropped into 10 cm³ of dilute "
              "hydrochloric acid at room temperature.",
     "result": "Slow. A few bubbles clinging to the filings, and it takes "
               "most of a lesson to see much change.",
     "why": "Iron is only just above hydrogen, so it does displace it — but "
            "barely, and you need patience to see it. That narrow margin is "
            "the whole reason iron rusts away in wet air over years rather "
            "than in minutes.",
     "eq_left": "hydrochloric acid + iron",
     "eq_right": "iron chloride + hydrogen"},
    {"id": "fe:h2so4", "reacts": True, "mark": "fizzes",
     "aria": "Iron in sulfuric acid",
     "title": "Iron in sulfuric acid",
     "setup": "Measured iron filings dropped into 10 cm³ of dilute sulfuric "
              "acid at room temperature.",
     "result": "Slow again, and the liquid turns a pale green as the filings "
               "go into solution.",
     "why": "Slowest of the three that work, in either acid, which places "
            "iron at the bottom of the reacting metals here. The pale green "
            "is the iron sulfate dissolving — the metal has not vanished, it "
            "has changed into something that dissolves.",
     "eq_left": "sulfuric acid + iron",
     "eq_right": "iron sulfate + hydrogen"},
    # ⚑ Flag 12. The two copper tubes are two DIFFERENT paragraphs rather than
    # one repeated, because the second is where the argument gets made: nothing
    # about the acid is the reason, so changing the acid cannot help.
    {"id": "cu:hcl", "reacts": False, "mark": "none",
     "aria": "Copper in hydrochloric acid",
     "title": "Copper in hydrochloric acid",
     "setup": "Measured copper turnings dropped into 10 cm³ of dilute "
              "hydrochloric acid at room temperature.",
     "result": "Nothing. Not in twenty minutes, not in a week.",
     "why": "Copper sits BELOW hydrogen in the reactivity series, so it "
            "cannot push hydrogen out of an acid. There is no slow reaction "
            "here to wait for — there is no reaction at all, and warming it, "
            "stirring it or leaving it out overnight all give the same "
            "result.",
     "eq_left": "", "eq_right": ""},
    {"id": "cu:h2so4", "reacts": False, "mark": "none",
     "aria": "Copper in sulfuric acid",
     "title": "Copper in sulfuric acid",
     "setup": "Measured copper turnings dropped into 10 cm³ of dilute "
              "sulfuric acid at room temperature.",
     "result": "Nothing again. The turnings are as bright at the end as they "
              "were at the start.",
     "why": "Changing the acid changes nothing, and that is the point of "
            "running the second copper tube at all. What decides this is "
            "where copper sits relative to hydrogen, and that is a fact about "
            "copper — so no acid you could reach for on this bench would give "
            "a different answer.",
     "eq_left": "", "eq_right": ""},
]

# ── the three judgements (Design's `JUDGEMENTS`) ────────────────────────
#
# Yes/no on all three. ⭐ The third is the one that matters most: it asks
# whether a test that reports nothing has failed, and the answer is that a
# correct negative IS a result — which is the same idea `c5-03`'s control tubes
# teach and the idea the copper row of the grid has just demonstrated.
_JUDGEMENTS = [
    {"id": "t1",
     "q": "A tube of gas from magnesium and acid is tested with a lit splint "
          "and squeaks. Does that prove the gas is hydrogen?",
     "options": [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
     "answer": "yes",
     "reply": "Yes — the squeaky pop is the standard test for hydrogen, and "
              "no other gas you will meet at this level does it. The squeak "
              "is the sound of the hydrogen burning explosively with the "
              "oxygen in the tube, making water."},
    {"id": "t2",
     "q": "A student holds the splint to the mouth of the tube while it is "
          "still fizzing hard. Is that a good idea?",
     "options": [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
     "answer": "no",
     "reply": "No. The tube needs to be collected and stoppered first, and "
              "tested away from the reaction. Holding a flame over a vessel "
              "that is actively producing hydrogen means the flame can run "
              "back down into it — and a tube of hydrogen mixed with air does "
              "not squeak, it bangs."},
    {"id": "t3",
     "q": "The same test is tried on the gas from copper and acid, and "
          "nothing pops. Does that mean the test failed?",
     "options": [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
     "answer": "no",
     "reply": "No — it means there was no gas to test. Copper sits below "
              "hydrogen in the reactivity series, so it cannot displace "
              "hydrogen from an acid. A test that correctly reports nothing "
              "is not a failed test, and this one has just told you where "
              "copper sits."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 227 character for character.
    "slug":        "acid-plus-metal",
    "title":       "Acid + metal",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.CR.06` is "reactions of acids with metals to produce a salt plus
    # hydrogen", and this lesson owns the whole of it: the grid produces the
    # salts, the gas test identifies the hydrogen, and the copper row is where
    # the "reactive enough" qualifier gets taught.
    "covers":      ["KS3.C.CR.06"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires":    ["neutralisation"],
    "assumes":     [],
    # ⚑ Flag 12's cross-reference, declared rather than assumed. The copper row
    # is justified by the reactivity series, which is C5-04's content.
    #
    # ⚠️ THE DICT FORM, because this crosses a unit boundary. A bare string is
    # read as "a lesson in THIS unit" and the href would be composed from C6 —
    # the MRB-248 repair. Naming C5 says what is true.
    "references":  [{"unit": "C5", "lesson": "displacement"}],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Drop magnesium into acid and the tube fizzes hard enough "
                    "to warm your hand. Drop copper in and nothing happens at "
                    "all — for a week.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`. `done_when` restates her own `DONE()`: the
    # hook on a commitment, the grid when six of the eight tubes have been run,
    # the gas test when all three judgements are decided, `#s-think` on a
    # commitment, and the ladder when every rung is answered.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The squeak", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "TUBES",
         "label": "Eight tubes", "done_when": "six_run"},
        {"anchor": "s-test",   "short": "TEST",
         "label": "Testing the gas", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "What the bubbles are", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK GIVES THE EVIDENCE THAT DECIDES IT AND DOES NOT SAY WHAT IT
    # DECIDES. "Hold a lit splint to it, and it goes off with a squeak" is the
    # identification of the gas, sitting in plain sight, and the commitment is
    # about where it CAME FROM, which the squeak does not answer.
    "phenomenon": {
        "kind": "narrative",
        "title": "A strip of magnesium goes into dilute hydrochloric acid. "
                 "The tube fills with bubbles and the metal disappears.",
        "prompt": "The tube gets warm. Within a minute the magnesium is gone "
                  "and the liquid is clear. Collect the gas coming off, hold "
                  "a lit splint to it, and it goes off with a squeak.",
        "commit": "Where did the gas come from?",
        # MRB-177: 5, 8, 6, 6 words. The correct option is index 2 and is not
        # the longest — B is. Design's set, unchanged.
        "options": [
            "The magnesium turned into gas",
            "It was air trapped in the metal strip",
            "The hydrogen came out of the acid",
            "The water in the acid boiled",
        ],
        "reveal": "From the acid. Every acid contains hydrogen — that is what "
                  "makes it an acid — and a reactive metal takes the acid "
                  "apart and lets the hydrogen go. The magnesium has not "
                  "turned into gas; it has gone into the solution as a salt, "
                  "invisible and dissolved. Boil the liquid dry and it is "
                  "waiting for you as white crystals of magnesium chloride.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⊖ `think-reveal-hydrogen` cannot be emitted from a lane — the `#s-think`
    # reveal panel is drawn by the shared `r_activity` with no id. `ACID-07`
    # names the activity that holds both its commitment and its answer, which
    # is the `c5-02` / `c4-01` reconciliation and what satisfies Law 3.
    "misconceptions": [
        {"id": "ACID-07",
         "statement": "The bubbles are the metal turning into gas.",
         "elicited_by": "think-commit-fizz",
         "confronted_by": "think-commit-fizz"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A reactive metal reacts with an acid, and there are always "
                 "two products."},

        # ⭐ THE WORD EQUATION, DRAWN — see `neutralisation`'s note for why an
        # `explainer` cannot carry an inline SVG and why `r_equation` is the
        # component that can. No triangle and no part-whole bar: MRB-204 as
        # amended gives the triangle to `A = B x C` and the bar to a sum, and a
        # word equation is neither.
        {"type": "rule", "id": "salt-plus-hydrogen",
         "eyebrow": "The rule",
         "statement": "A reactive metal and an acid always make the same two "
                      "things.",
         "equation": {"reactants": "acid + metal",
                      "arrow": "makes",
                      "products": "salt + hydrogen",
                      # Commentary, not a condition on the arrow (b8-01's
                      # shape). This is ACID-07 said in the one place a
                      # student looks when they are writing the equation out.
                      "condition": "the hydrogen comes out of the acid, "
                                   "not the metal"},
         "close": "Which salt depends on the acid. Hydrochloric acid makes "
                  "<strong>chlorides</strong>, sulfuric acid makes "
                  "<strong>sulfates</strong>, nitric acid makes "
                  "<strong>nitrates</strong>. The first word of the salt's "
                  "name is the metal; the second comes from the acid."},

        {"type": "explainer",
         "text": "And it only happens if the metal is reactive enough. The "
                 "reactivity series decides which tubes fizz and which sit "
                 "there doing nothing."},

        # #s-bench — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ THE LEAD IS NOT A NARRATION OF THE CONTROLS. Design's line is "N
        # of 8 run. The copper row is worth running as well — a tube that does
        # nothing is telling you something precise." The count is the block
        # head's counter; the sentence that follows it is an argument about
        # negative evidence and is the reason the copper row exists, so it is
        # kept whole.
        {"type": "acid-metal-grid", "id": "grid-eight", "anchor": "s-bench",
         "eyebrow": "Your turn · eight tubes",
         "heading": "Four metals, two acids. Pick a tube, predict, then run "
                    "it.",
         "prompt": "The copper row is worth running as well — a tube that "
                   "does nothing is telling you something precise.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} run", "start": 0},
         "metals": _METALS,
         "acids": _ACIDS,
         "cells": _CELLS,
         "corner_label": "Metal added to",
         "table_label": "Four metals crossed with two acids",
         "unrun_mark": "?",
         "predict_prompt": "Predict before you run it.",
         "predict_options": [{"id": "fast", "label": "Fizzes hard"},
                             {"id": "slow", "label": "Fizzes slowly"},
                             {"id": "none", "label": "Nothing happens"}],
         # Design's own threshold. Six of the eight is enough to have met the
         # copper row, which is the row that proves the rule, and it leaves the
         # stop reachable without demanding a completed grid.
         "done_at": 6,
         "close": {"id": "grid-pattern",
                   "title": "Two patterns, not one.",
                   "paras": [
                       "Read down the columns and the speed falls in the "
                       "order magnesium, zinc, iron, copper — the reactivity "
                       "series again, arrived at by a different route. Read "
                       "across the rows and the metal decides the first word "
                       "of the salt while the acid decides the second: "
                       "chloride from hydrochloric, sulfate from sulfuric.",
                       "Copper is the row that proves the rule. It is below "
                       "hydrogen in the reactivity series, so it cannot push "
                       "hydrogen out of an acid — and no amount of waiting "
                       "will change that.",
                   ]}},

        {"type": "key-fact", "ref": "out-of-the-acid"},

        # #s-test — three judgements. Light `ks3-block` → `check`.
        {"type": "acid-judgements", "id": "test-three", "anchor": "s-test",
         "eyebrow": "Three judgements · testing the gas",
         "heading": "A squeak, a lit splint and a stoppered tube",
         "prompt": "Commit to each before reading. The third one is a genuine "
                   "hazard, not a trick question.",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "items": _JUDGEMENTS},

        {"type": "misconception", "id": "think-commit-fizz",
         "anchor": "s-think", "targets": "ACID-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. The grid IS the picture — four metals crossed with two acids, with
    # a readout beside it — and a frozen drawing of the reactivity series would
    # be C5-04's figure reproduced here, where the point is that the grid
    # produces the order rather than consults it.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # ⚑ "makes" rather than a typed arrow — Design's own 21 Aug font-law pass.
    "key_facts": [
        {"id": "out-of-the-acid",
         "text": "acid + metal makes salt + hydrogen. The hydrogen comes out "
                 "of the acid, not the metal, and a lit splint gives a "
                 "squeaky pop.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-fizz",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-07",
         "prompt": "The magnesium does vanish, and bubbles do come off. "
                   "Commit before you read on.",
         # MRB-177: 8, 16, 9, 11 words. The correct option is index 1 and is
         # strictly the longest by five words at 1.45x — the construct §13
         # measures. The three distractors are re-authored at its own length
         # and in its own shape; Design's B is untouched and the answer has not
         # moved.
         "options": [
             "Right — the metal boils away as bubbles, which is why the strip "
             "disappears from the tube",
             "Wrong — the bubbles are hydrogen from the acid; the metal is "
             "dissolved as a salt",
             "Right, because the metal is gone at the end and the gas is the "
             "only thing that left",
             "Wrong — the bubbles are air that was pushed out of the liquid "
             "as the strip sank into it",
         ],
         "reveal": [
             "Two different things are happening and they are easy to run "
             "together. The <strong>bubbles</strong> are hydrogen, which came "
             "out of the acid. The <strong>metal</strong> has gone into "
             "solution as a salt — dissolved, invisible, and still every atom "
             "present.",
             "You can prove both halves. The gas pops with a lit splint, "
             "which magnesium vapour would not do. And evaporating the liquid "
             "leaves white magnesium chloride crystals, which were not there "
             "when you started. <strong>The metal did not become the gas — it "
             "swapped places with the hydrogen in the acid.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        # Design's options, untouched; the answer moves to index 3 (MRB-278).
        # MRB-177: all four are four words, so there is no length tell in
        # either direction.
        "recall": {
            "q": "Zinc is added to sulfuric acid. What are the products?",
            "options": [
                "Zinc chloride and hydrogen",
                "Zinc sulfate and water",
                "Zinc oxide and hydrogen",
                "Zinc sulfate and hydrogen",
            ],
            "answer": 3,
            "feedback": {
                0: "Chlorides come from hydrochloric acid. Sulfuric acid "
                   "gives sulfates.",
                1: "Water is what you get when an acid meets an alkali. With "
                   "a metal, the second product is hydrogen gas.",
                2: "No oxide forms here — the metal ends up joined to the "
                   "part of the acid left behind, which is the sulfate.",
            }},
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 15 words against 9, 5 and 5:
        # strictly the longest by six and at 1.67x. Each now states a WRONG
        # RULE in the correct answer's own "X, so Y" shape and at its own
        # length: 14, 15, 15 against 15. Every one of Design's corrections is
        # unchanged and still answers its own option — the dilution argument,
        # the "not really a metal" argument, and the time argument.
        "apply": {
            "q": "Copper is left in dilute hydrochloric acid for a week and "
                 "nothing happens. What is the reason?",
            "options": [
                "Copper is below hydrogen in the reactivity series, so it "
                "cannot displace it from the acid",
                "The acid was too dilute to attack copper, so a concentrated "
                "one would have worked",
                "Copper is not really a metal but a mixture, so it has no "
                "reaction with any acid",
                "A week is not long enough for a reaction this slow, so it "
                "simply needs to be left longer",
            ],
            "answer": 0,
            "feedback": {
                1: "Concentration changes how fast a possible reaction goes. "
                   "This one cannot happen at any concentration of dilute "
                   "hydrochloric acid.",
                2: "Copper is very much a metal. It is simply an unreactive "
                   "one.",
                3: "Time cannot make an impossible reaction happen. A year "
                   "would look exactly the same.",
            }},
        "explain": {
            "q": "Magnesium is dropped into hydrochloric acid. Describe what "
                 "you would see, name both products, and explain where the "
                 "gas comes from.",
            "field_label": "Your explanation",
            "placeholder": "The magnesium…",
            "success": [
                "Says bubbles of gas are given off rapidly and the metal "
                "disappears.",
                "Says the tube gets warm.",
                "Names the products as magnesium chloride and hydrogen.",
                "Says the hydrogen comes from the acid, not from the metal.",
                "Says the magnesium is still present, dissolved as a salt.",
            ]},
        "produce": {
            "q": "You are given four unlabelled metals and a bottle of dilute "
                 "hydrochloric acid. Explain how you would put the metals in "
                 "order of reactivity, and what you would do to make it a "
                 "fair comparison.",
            "field_label": "Your plan",
            "placeholder": "I would put an equal-sized piece of each metal "
                           "into…",
            "success": [
                "Adds an equal-sized piece of each metal to the same volume "
                "of the same acid.",
                "Keeps the acid concentration and temperature the same for "
                "each.",
                "Compares how quickly bubbles are produced.",
                "Says the fastest is the most reactive and any that does "
                "nothing is the least.",
                "Says a metal that does not react at all must be below "
                "hydrogen in the series.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A metal above hydrogen in the reactivity series reacts with "
                "an acid to give a salt and hydrogen gas. The more reactive "
                "the metal, the faster the fizzing. Hydrochloric acid gives "
                "chlorides, sulfuric acid gives sulfates. Hydrogen is tested "
                "with a lit splint: it burns with a squeaky pop.",

    # ── the stretch layer (§5.6) ────────────────────────────────────────────
    "stretch": [
        {"type": "explainer", "id": "sacrificial-anodes",
         "text": "This reaction is why the hulls of ships are fitted with "
                 "slabs of zinc bolted to the steel below the waterline. "
                 "Seawater is mildly acidic and full of dissolved salt, and "
                 "it attacks iron steadily. Bolt on something more reactive "
                 "and the seawater attacks that instead: the zinc corrodes "
                 "away and the hull does not. The slabs are called "
                 "sacrificial anodes, and replacing them is routine dry-dock "
                 "work."},
        {"type": "explainer", "id": "why-acid-is-not-stored-in-metal",
         "text": "It is also the reason nobody stores acid in a metal can. "
                 "Concentrated acids arrive in glass or plastic, and the "
                 "tanker lorries that carry sulfuric acid are lined — because "
                 "a steel tank full of acid is a hydrogen generator, and "
                 "hydrogen and air together only need a spark. The gas that "
                 "gives a tidy squeak from a test tube is the same gas that "
                 "took down the Hindenburg."},
    ],

    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Salt",
         "definition": "The compound made when a metal takes the place of the "
                       "hydrogen in an acid. Its first word is the metal and "
                       "its second comes from the acid."},
        {"term": "Reactivity series",
         "definition": "The order of metals from most reactive to least. A "
                       "metal above hydrogen in it will push hydrogen out of "
                       "an acid; one below it will not."},
        {"term": "Displace",
         "definition": "To take the place of something else in a compound. A "
                       "reactive metal displaces the hydrogen in an acid and "
                       "the hydrogen leaves as a gas."},
        {"term": "Squeaky pop",
         "definition": "The test for hydrogen. A lit splint held in a tube of "
                       "hydrogen makes a sharp squeak as the gas burns.",
         "note": "The tube is stoppered and moved away from the reaction "
                 "before it is tested."},
        {"term": "Chloride",
         "definition": "A salt made by hydrochloric acid. Sulfuric acid makes "
                       "sulfates and nitric acid makes nitrates."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚑ NEW PROSE. ⊖ No safeguarding block — lab safety. It names the hazard
    # the third judgement is about and does not retract the method: the page is
    # about collecting and testing hydrogen, and this says how it is done.
    "safety_note": "Hydrogen mixed with air explodes rather than squeaking. "
                   "The gas is collected in a tube, stoppered, and carried "
                   "away from the fizzing flask before a lit splint goes near "
                   "it — never tested at the mouth of a tube that is still "
                   "reacting.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why copper does nothing?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Redox: the metal loses electrons and hydrogen ions gain "
                   "them, plus rates of reaction measured by the volume of "
                   "gas collected.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    "review_state": "draft",
}
