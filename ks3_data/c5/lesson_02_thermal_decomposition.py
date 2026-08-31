"""C5 L2 — Thermal decomposition (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c5/c5-02-thermal-decomposition.dc.html` (696 lines),
and her author's notes `docs/ks3/design-reference/c5/NOTES-C5.md` §1, §2, §3,
§4 flags 7–10, §5 (`REACT-12`, `REACT-13`) and §6.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`SUBS`, `SORTS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the
hook options and reveal, the two explainer paragraphs, the tube block's
eyebrow / heading / dial label / stage titles / tile labels / button labels,
the cooling gate's question and its three options, the all-three panel, the
key fact, the sort block's eyebrow and heading, the `#s-think` options and its
two reveal paragraphs, the key note and both "Going further" paragraphs were
lifted from `lessonVals(s)` and from the markup, which is where most of this
lesson's words live and where a lift of the top-level constants alone silently
loses them.

── THE COOLING GATE IS THE LESSON ──────────────────────────────────────

NOTES-C5 §2 says it outright: this is "a staged run with a cooling gate at the
end. The gate is the lesson: it does not go back when it cools, which is what
separates it from a physical change." So the gate is not a formality bolted to
the last stage — it is the payoff of `c4-01` (a change is chemical when it
makes a new substance) and of `c5-01` (burning joins things together), and it
is the one commitment on this page that the student cannot get from watching.

Three things follow, and all three are load-bearing:

  · THE GATE BLOCKS THE LAST STAGE. `showNext` is false while the gate is
    open, so a student cannot watch the tube cool before saying what they
    think will happen. Design's own `gateNeeded` does this and the wiring
    reproduces it exactly.
  · THE ANSWER ARRIVES AS THE NEXT STAGE OF THE RUN, not as a verdict. Stage 4
    for each of the three substances says the same thing in its own words —
    the powder stays black, the quicklime is not what went in, the cake does
    not become batter — and nothing on the page marks the commitment.
  · THE GATE IS THE SAME GATE FOR ALL THREE SUBSTANCES, so it is drawn once.
    "What happens as it cools?" is not a question about copper, and asking it
    three times in three panels would make it look like one.

── The three substances are one payload, and the numbers are the evidence ──

⚑ Science flag 7, RULED and KEPT WHOLE: 4.00 g → 2.58 g (copper carbonate),
→ 2.24 g (calcium carbonate), → 2.52 g (sodium hydrogencarbonate). All three
re-derived from formula masses and exact (CuCO₃ 123.5 → CuO 79.5; CaCO₃ 100 →
CaO 56; 2 × NaHCO₃ 168 → Na₂CO₃ 106). Design's NOTES asks whether numbers are
wanted at all given no calculation: they are. A decomposition that visibly
loses mass is the EVIDENCE that something left, and a number makes that
checkable rather than assertable.

`r_tube_run` reads all six masses at BUILD time and refuses to draw a
substance whose after-mass is not lower than its before-mass, and refuses one
whose equation does not put a single reactant on the left and two or more
products on the right. That is the lesson's whole claim — one in, more than
one out, and lighter — asserted against every substance rather than a sample,
so a future edit that breaks it fails the build instead of a student.

⚑ Science flag 8, CONFIRMED and KEPT: limestone at "around 900 °C", "a roaring
blue flame and patience, or an industrial kiln". The hedge is honest and it is
what explains why this one is a demonstration rather than a class practical.

⚑ Science flag 9, CONFIRMED and KEPT with Design's own hedge: cement at
"something like 8% of the world's carbon dioxide emissions".

⚑ Science flag 10, CONFIRMED and KEPT: the airbag. Design's sentence already
times the INFLATION rather than the reaction — "why an airbag can inflate in
thirty milliseconds" — which is the reading the figure supports. Unchanged.

⚑ And one distractor set re-authored under MRB-177, at the distractors:

  * RUNG 1's four options ran 11, 6, 7 and 7 words. The correct answer was
    strictly the longest and cleared the field by four, which is exactly the
    construct §13 measures: the right answer states a RULE (one compound, into
    two or more, by heat) and each distractor stated a short wrong REASON. The
    three DISTRACTORS are re-authored as wrong RULES in the correct answer's
    own three-part shape and at its own length — 11, 11, 11 against 11. The
    correct option is Design's, untouched, and still index 0; every one of her
    corrections still answers the option it is attached to, because each
    distractor still names the same wrong reaction type it always named.

── The `#s-sort` block's `yes` flag is the answer and is emitted nowhere ──

Same rule as `c4-01`'s `chemical`, and the same fix: `r_decomp_sort` reads it
at BUILD time and asserts, for all five items, that a `yes` item's answer
opens by naming thermal decomposition and a `no` item's does not. Otherwise it
would be authored correctness data with no read site — content that never
reaches a student AND an invariant nothing is checking.
"""

# ── the three substances (Design's `SUBS`) ──────────────────────────────
#
# One object, in her key order — copper, calcium, bicarb — which is the order
# the tabs are drawn in and the order the run gets harder in: the one a school
# Bunsen does easily, the one it does not, and the one in a kitchen cupboard.
#
# `stages` is FOUR strings against the four fixed stage titles below, and the
# fourth is the one `REACT-13` is confronted by: each says, in its own words,
# that the change did not go back. `mass0` / `mass1` are the before and after
# readings of the tile the run drives; `eqLeft` / `eqRight` are the word
# equation the finished panel draws with an SVG arrow between them.
_SUBS = [
    {"id": "copper",
     "tab": "Copper carbonate",
     "mass0": "4.00 g",
     "mass1": "2.58 g",
     "intro": "A green powder. It decomposes at a temperature an ordinary "
              "Bunsen burner reaches easily, which is why it is the school "
              "version of this reaction.",
     "stages": [
         "The flame goes under the tube. Nothing happens for a few seconds "
         "while the powder heats through.",
         "The green darkens from the bottom upwards and becomes black. The "
         "colour change spreads as the heat does — the part not yet hot "
         "enough is still green.",
         "The gas is bubbled through limewater, which turns milky. That is "
         "the test for carbon dioxide, and only carbon dioxide passes it.",
         "The flame comes off. The powder stays black as it cools, and it "
         "stays black tomorrow.",
     ],
     "eq_left": "copper carbonate",
     "eq_right": "copper oxide + carbon dioxide",
     "finish": "Black copper oxide left in the tube, carbon dioxide gone into "
               "the limewater. The tube is lighter by exactly the mass of the "
               "gas that left."},

    # ⚑ Science flag 8 is this substance's `intro` and its first stage, both
    # KEPT WHOLE. "Far more heat than the copper carbonate did" and "a roaring
    # blue flame and patience, or an industrial kiln" are the honest version,
    # and they are what tells a reader why nobody is handing them a lump of
    # limestone and a Bunsen.
    {"id": "calcium",
     "tab": "Limestone",
     "mass0": "4.00 g",
     "mass1": "2.24 g",
     "intro": "Calcium carbonate — limestone, chalk and marble are all the "
              "same compound. It needs a much higher temperature than the "
              "copper one: a roaring blue flame and patience, or an "
              "industrial kiln.",
     "stages": [
         "The flame goes under the lump. Nothing visible happens for a long "
         "time — this reaction needs far more heat than the copper carbonate "
         "did.",
         "The lump glows and crumbles slightly, and it stays white. There is "
         "no colour change to watch, which makes this a good reminder that a "
         "colour change is a clue and not a requirement.",
         "The gas turns limewater milky: carbon dioxide again. This is the "
         "only evidence that anything has happened at all.",
         "It cools as a white solid — calcium oxide, quicklime — and it is "
         "not the same substance that went in. Drop water on it and it hisses "
         "and gets hot.",
     ],
     "eq_left": "calcium carbonate",
     "eq_right": "calcium oxide + carbon dioxide",
     "finish": "Quicklime in the tube and carbon dioxide gone. This is the "
               "reaction that makes cement possible, run in kilns the size of "
               "buildings."},

    {"id": "bicarb",
     "tab": "Baking soda",
     "mass0": "4.00 g",
     "mass1": "2.52 g",
     "intro": "Sodium hydrogencarbonate — the raising agent in a cake. It "
              "decomposes at oven temperatures, which is the entire reason it "
              "is in the recipe.",
     "stages": [
         "Gentle heating. The white powder starts to fizz and shift as gas "
         "works its way out of it.",
         "It stays white and loses volume. Water vapour condenses in the cool "
         "upper part of the tube — this decomposition gives two gases, not "
         "one.",
         "The gas turns limewater milky, so carbon dioxide is among the "
         "products. In a cake, this gas is what makes it rise.",
         "It cools to a white powder — sodium carbonate — and does not turn "
         "back. A cake does not become batter again as it cools either.",
     ],
     "eq_left": "sodium hydrogencarbonate",
     "eq_right": "sodium carbonate + carbon dioxide + water",
     "finish": "Three products from one reactant. The carbon dioxide is the "
               "point in baking, and the water vapour is why a cake steams as "
               "it comes out of the oven."},
]

# ── the five changes to sort (Design's `SORTS`) ─────────────────────────
#
# ⚠️ `yes` IS THE ANSWER AND IS EMITTED NOWHERE. It is read at build time by
# `r_decomp_sort`, which asserts against `answer`; see the docstring. Heat is
# involved in ALL FIVE, which is the whole construction: two are the reaction,
# one is combustion, one is a physical change and one is oxidation, so "there
# was a flame" sorts none of them.
_SORTS = [
    {"id": "s1", "yes": True,
     "text": "Green copper carbonate is heated and turns black, giving off "
             "carbon dioxide.",
     "answer": "Thermal decomposition. One compound in, two substances out, "
               "using heat and nothing else."},
    {"id": "s2", "yes": False,
     "text": "A candle is lit and the wax burns away.",
     "answer": "Combustion, not decomposition. Two reactants — wax and oxygen "
               "— and the reaction releases heat rather than needing it."},
    # The physical-change item, and the one the cooling gate has just prepared
    # the student for: it reverses on cooling, and nothing new was made.
    {"id": "s3", "yes": False,
     "text": "Ice in a beaker is heated and melts to water.",
     "answer": "A physical change. One substance in and the same substance "
               "out, and it reverses on cooling. No new substance was made at "
               "all."},
    {"id": "s4", "yes": True,
     "text": "Baking soda in a cake mixture is heated and the cake rises.",
     "answer": "Thermal decomposition. The sodium hydrogencarbonate breaks "
               "down and the carbon dioxide it releases is trapped in the "
               "mixture."},
    {"id": "s5", "yes": False,
     "text": "Magnesium ribbon is heated in air and leaves a white powder.",
     "answer": "Oxidation — two reactants joining, not one coming apart. The "
               "mass goes up here; in a decomposition it goes down."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 217 character for character.
    "slug":        "thermal-decomposition",
    "title":       "Thermal decomposition",
    "discipline":  "chemistry",
    "unit":        "types-of-reaction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1 gives all five C5 lessons `KS3.C.CR.03`, a bullet that names
    # four reaction types in one sentence. `validate()` rule 4 owns a statement
    # exactly once, so the clauses are minted in `ks3_data/substatements.py`
    # (the commander's file). This lesson is clause `b`: one substance broken
    # down by heating into two or more, and not reassembling on cooling.
    "covers":      ["KS3.C.CR.03b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "energy", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to c5-01. The explainer, the
    # `#s-think` reveal and sort item s2 all argue AGAINST combustion, so this
    # lesson cannot be read by anyone for whom burning does not already mean
    # something specific. The cooling gate is c4-01's distinction being cashed
    # in, which is why that lesson is referenced.
    "requires":    ["combustion"],
    "assumes":     [],
    "references":  ["chemical-vs-physical-change"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Every reaction so far has joined things together. What "
                    "kind of reaction takes one substance and gives you two?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, in her order with her ids and her short
    # labels. `done_when` restates her own `DONE()`: the hook on a commitment,
    # the tube when all three substances have been carried to the end
    # (`Object.keys(s.done).length >= 3`), the sort when every one of the five
    # is decided (`>= SORTS.length`), `#s-think` on a commitment, and the
    # ladder when every rung is answered and both self-marked rungs checked.
    #
    # MRB-208: nothing is ticked on load and credit is a ratchet.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "One in, two out", "done_when": "committed"},
        {"anchor": "s-tube",   "short": "TUBE",
         "label": "The test tube", "done_when": "all_three_run"},
        {"anchor": "s-sort",   "short": "SORT",
         "label": "Five changes", "done_when": "all_five_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Did it burn?", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is unread by the generator (it dispatches on which media key is
    # present) and is authored for consistency with C1–C4.
    #
    # ⚠️ THE HOOK CLOSES THE ONE DOOR THE LESSON NEEDS SHUT. "Nothing is added
    # to it — no acid, no other chemical, and the tube is not open to much air"
    # is what makes `REACT-12` answerable at all: without it, "something in the
    # air reacted with it" is not a wrong answer, it is an untested one.
    "phenomenon": {
        "kind": "narrative",
        "title": "One substance went into the tube. Two came out.",
        "prompt": "A green powder is heated in a test tube. Nothing is added "
                  "to it — no acid, no other chemical, and the tube is not "
                  "open to much air. It turns black, a gas comes off that "
                  "turns limewater cloudy, and the tube is lighter "
                  "afterwards.",
        "commit": "Every reaction so far had two or more reactants. What has "
                  "happened here?",
        "options": [
            "Something in the air reacted with the powder",
            "The heat broke the compound apart into two new substances",
            "The powder melted and changed colour",
            "The gas was trapped in the powder and escaped",
        ],
        "reveal": "The compound has been <strong>broken apart by heat</strong>. "
                  "Copper carbonate is copper, carbon and oxygen joined "
                  "together; heating supplies enough energy to break those "
                  "joins, and the pieces reassemble as two new substances — "
                  "black copper oxide, which stays, and carbon dioxide, which "
                  "leaves. One reactant, two products. Nothing arrived from "
                  "outside.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS RESOLVE AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248), and
    # the universe of legal names is exactly `id="…"` and `data-activity="…"`.
    #
    # ⊖ NOTES §5 proposes `think-commit-black` / `think-reveal-copper-oxide`
    # for REACT-12. NO `think-reveal-*` ID CAN BE EMITTED FROM A LANE: the
    # `#s-think` reveal panel is drawn by `build_ks3.py`'s shared `r_activity`,
    # which emits `<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>`
    # and NO id, and `build_ks3.py` is not a file this lane may touch. The two
    # confronting paragraphs are INSIDE the activity whose `data-activity` is
    # `think-commit-black`, so that is what the join names — the same
    # reconciliation `c4-01` made for REACT-01 and `c3-03` for MIX-06. It is
    # also what satisfies Law 3, which requires at least one `confronted_by`
    # to be a real ACTIVITY id.
    #
    # ⊕ REACT-13's two names are NOTES' own and BOTH ARE EMITTED HERE, by
    # `r_tube_run`: `id="cool-gate"` on the commitment panel inside stage 4,
    # and `id="stage-4-reveal"` on the container holding the three stage-4
    # sentences — one element, whichever substance is loaded, because "what
    # happens as it cools" is one question and gets one answer.
    #
    # `statement` is the line the PAGE quotes when the page quotes one.
    # REACT-12's is quoted, in `.ks3-mis-quote`, and `r_confrontation` prints
    # `statement` there, so Design's line is the one that must render.
    # REACT-13 is never quoted on the page — it is elicited by a button, not by
    # a quotation — so it keeps the register's own wording.
    "misconceptions": [
        {"id": "REACT-12",
         "statement": "It went black, so the copper carbonate burnt.",
         "elicited_by": "think-commit-black",
         "confronted_by": "think-commit-black"},
        {"id": "REACT-13",
         "statement": "A decomposition reverses when it cools.",
         "elicited_by": "cool-gate",
         "confronted_by": "stage-4-reveal"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 106–107 — the definition, and the sentence that separates
        # this reaction from the one before it. Two paragraphs, so two blocks:
        # `r_explainer` draws one <p>.
        {"type": "explainer",
         "text": "<strong>Thermal decomposition</strong> is one compound "
                 "being broken down into two or more substances using heat. "
                 "It is the only reaction type you will meet that runs "
                 "<em>backwards</em> compared with the others: instead of "
                 "substances joining, one comes apart."},
        {"type": "explainer",
         "text": "It also needs the heat continuously. Take the flame away "
                 "and the reaction stops — which is the opposite of burning, "
                 "where the reaction supplies its own heat once it has "
                 "started."},

        # #s-tube — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ NO `prompt`. Design draws the eyebrow, the h2 and then the dial
        # label, with no line of instruction between them, and §5A forbids
        # narrating the controls: "press Light the Bunsen, then press Keep
        # heating" is the instrument read aloud. The stage titles and the
        # button labels ARE the instruction.
        {"type": "tube-run", "id": "tube-heat", "anchor": "s-tube",
         "eyebrow": "Your turn · the test tube",
         "heading": "Heat it, test the gas, then let it cool",
         "demand": "investigate",
         "dial_label": "In the tube",
         "substances": _SUBS,
         # The four stage titles, fixed across all three substances, because
         # the METHOD is the same method whatever is in the tube — which is
         # the point of running it three times.
         "stage_titles": ["Heat it", "Watch the solid", "Test the gas",
                          "Take the flame away"],
         # ⭐ THE COOLING GATE. One panel, drawn once, blocking the last
         # stage. `id` is REACT-13's elicitation site and `reveal_id` is its
         # confrontation site; both are named here rather than composed in the
         # renderer, so the register's join and the markup have one source.
         "gate": {"id": "cool-gate",
                  "reveal_id": "stage-4-reveal",
                  "q": "Before you take the flame away: what happens as it "
                       "cools?",
                  "options": [
                      "It changes back as it cools",
                      "It stays as it is — the change does not reverse",
                      "It changes back only if you add the gas again",
                  ]},
         # The three live readouts. `mass` takes each substance's own two
         # values, so it is authored as a NAME rather than as a value; `lime`
         # and `heat` are the same for every substance and their values are
         # authored in the order the run reaches them.
         "tiles": [
             {"kind": "mass", "label": "Mass in the tube"},
             {"kind": "lime", "label": "Limewater",
              "values": ["clear", "milky"]},
             {"kind": "heat", "label": "Heat needed",
              "values": ["not yet", "continuously", "flame removed"]},
         ],
         # One label per move, and the last of them is the one the gate holds
         # back. Four labels for four moves: 0→1, 1→2, 2→3, 3→4.
         "advance_labels": ["Light the Bunsen", "Keep heating", "Test the gas",
                            "Let it cool"],
         "reset_label": "Fresh tube",
         "summary": "Three different substances, three word equations, and "
                    "the same shape every time: <strong>one on the left, more "
                    "than one on the right.</strong> None of them needed "
                    "anything added, all of them needed the flame kept on, "
                    "and not one of them came back on cooling."},

        {"type": "key-fact", "ref": "one-in-more-out"},

        # #s-sort — five changes, all of them involving heat. Light
        # `ks3-block` → `check`.
        #
        # ⚠️ NO `prompt` here either, and for the same reason: Design draws the
        # eyebrow and the h2 and goes straight to the five cards. The heading
        # IS the ask — "Heat is involved in all five. Only some are this
        # reaction" — and it is a better one than any instruction under it.
        {"type": "decomp-sort", "id": "sort-five", "anchor": "s-sort",
         "eyebrow": "Five changes · which are decomposition?",
         "heading": "Heat is involved in all five. Only some are this "
                    "reaction",
         "demand": "classify",
         "options": ["Thermal decomposition", "Something else"],
         "items": _SORTS},

        {"type": "misconception", "id": "think-commit-black",
         "anchor": "s-think", "targets": "REACT-12"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page — the instrument IS the
    # picture, a tube with four stages and three readouts beside it — and
    # NOTES §6 declares no figure for the unit. §5.4 allows an empty list where
    # it does not allow an absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "one-in-more-out",
         "text": "Thermal decomposition breaks one compound into two or more "
                 "substances using heat. One reactant, several products, "
                 "nothing added — and it does not reverse when it cools.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-commit-black",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-12",
         "prompt": "Things that go black in a flame usually have burnt. "
                   "Commit before you read on.",
         # MRB-177: 10, 10, 8, 11 words. The correct option is index 1 and is
         # not the longest — D is. Design's set, unchanged.
         "options": [
             "Right — heating something until it goes black is burning",
             "Wrong — nothing burnt; the black solid is copper oxide",
             "Right, because oxygen from the air joined in",
             "Wrong — the powder only looks black while it is hot",
         ],
         "reveal": [
             "Burning needs oxygen as a reactant. Do this reaction in a tube "
             "with no air in it and it works exactly the same — so nothing "
             "was burnt. The black is not soot and it is not charring: it is "
             "<strong>copper oxide</strong>, which is black because that is "
             "what copper oxide looks like.",
             "The two reaction types point in opposite directions. In "
             "combustion, a substance <strong>joins with</strong> oxygen and "
             "the reaction releases energy. In thermal decomposition, a "
             "compound <strong>comes apart</strong> and the reaction absorbs "
             "energy for as long as you supply it. Both involve heat and a "
             "Bunsen burner, and that is the whole of their resemblance.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her rung
    # labels are the engine's own defaults character for character ("Recall",
    # "The one that catches people", "Explain", "Take it somewhere new"), so no
    # rung authors a `title`. `feedback` is keyed by the INT index of each
    # wrong option, which is what `_rung_marked` reads.
    "ladder": {
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 11 words against 6, 7 and 7:
        # strictly the longest and clear of the field by four, which is the
        # construct §13 measures — the answer states a RULE (one compound,
        # into two or more, by heat) and each distractor stated a short wrong
        # REASON. Each now states a WRONG RULE in the same three-part shape and
        # at the same length: 11, 11, 11, 11. Every distractor still names the
        # reaction type it always named — joining, melting, oxidation — so
        # every one of Design's corrections still answers its own option.
        "recall": {
            "q": "What is thermal decomposition?",
            "options": [
                "Two or more substances joined together into one compound by "
                "heat",
                "One substance turned from a solid into a liquid by heat",
                "One substance joined with the oxygen in the air by heat",
                "One compound broken down into two or more substances by heat",
            ],
            "answer": 3,
            "feedback": {
                0: "That is the shape of combustion and oxidation. "
                   "Decomposition goes the other way: one reactant, several "
                   "products.",
                1: "Melting is a physical change — same substance, different "
                   "state, and it reverses on cooling.",
                2: "That is oxidation. Decomposition needs no other reactant "
                   "at all, and works in a tube with no air in it.",
            }},
        # The one that catches people, and it is the mass claim at the ladder:
        # a balance can only weigh what stayed. The correct option is 10 words
        # and index 3 is 10 as well, so nothing here is longest. Design's set,
        # unchanged.
        "apply": {
            "q": "A tube of copper carbonate is weighed, heated until the "
                 "colour change is complete, and weighed again. What has "
                 "happened to the mass, and why?",
            "options": [
                "It has risen, because oxygen joined the copper",
                "It has fallen, because the carbon dioxide left the tube",
                "It is unchanged, because mass is always conserved",
                "It has fallen, because some of the solid was destroyed",
            ],
            "answer": 1,
            "feedback": {
                0: "Nothing joined. No oxygen was needed — the reaction works "
                   "in a tube with no air, and the oxygen in the copper oxide "
                   "came from the carbonate itself.",
                2: "Mass is conserved, and one of the products left the tube. "
                   "The balance can only weigh what stayed.",
                3: "Nothing is destroyed. Collect the gas and weigh it and "
                   "the total comes out exactly the same.",
            }},
        "explain": {
            "q": "A student heats copper carbonate and says \"it burnt, that "
                 "is why it went black\". Give two pieces of evidence from "
                 "this lesson that show they are wrong, and say what the black "
                 "solid actually is.",
            "field_label": "Your explanation",
            "placeholder": "Burning needs oxygen, and…",
            "success": [
                "Says burning needs oxygen as a reactant.",
                "Gives the evidence that the reaction works with no air in "
                "the tube.",
                "Says the mass went down, whereas things that react with "
                "oxygen gain mass.",
                "Identifies the black solid as copper oxide, a product of the "
                "decomposition.",
                "Says the gas given off was carbon dioxide, shown by the "
                "limewater turning milky.",
            ]},
        "produce": {
            "q": "Cement is made by decomposing limestone in kilns. Explain "
                 "why this process releases carbon dioxide even if the kiln "
                 "were heated with electricity from wind turbines, and why "
                 "that makes the emissions hard to remove.",
            "field_label": "Your answer",
            "placeholder": "The decomposition itself produces…",
            "success": [
                "Says the decomposition of calcium carbonate itself produces "
                "carbon dioxide.",
                "Says that gas comes from the limestone, not from the fuel.",
                "Says changing the heat source removes the fuel emissions "
                "only.",
                "Says the reaction is required to make the product, so it "
                "cannot simply be left out.",
                "Suggests what would be needed instead — capturing the gas, "
                "or a different material altogether.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Byte-identical. It is the only sentence on the page that states all four
    # of the lesson's claims at once: one reactant, nothing added, energy in
    # for as long as you supply it, and no way back on cooling.
    "key_note": "Thermal decomposition breaks one compound down into two or "
                "more substances using heat. One reactant, several products, "
                "and nothing added — so it works even where there is no air. "
                "It absorbs energy for as long as you supply it, the mass "
                "left behind falls because a gas escapes, and it does not "
                "reverse on cooling.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Science flags 9 and 10 live here and both are KEPT byte-identical.
    #   * flag 9 — "something like 8% of the world's carbon dioxide emissions"
    #     keeps Design's own hedge, which is what makes a widely quoted figure
    #     honest rather than precise.
    #   * flag 10 — the airbag sentence already times the INFLATION ("why an
    #     airbag can inflate in thirty milliseconds") rather than the reaction,
    #     which is the reading the figure supports. Nothing moved.
    "stretch": [
        {"type": "explainer", "id": "cement",
         "text": "One thermal decomposition is carried out on an industrial "
                 "scale that dwarfs everything else in this unit. Limestone "
                 "is heated in kilns to around 900 °C to make calcium oxide "
                 "— quicklime — which is the basis of cement. The reaction "
                 "is unavoidable and it releases carbon dioxide from the rock "
                 "itself, before you count the fuel used to heat the kiln. "
                 "Cement production is responsible for something like 8% of "
                 "the world's carbon dioxide emissions, and the chemistry "
                 "means you cannot fix it by changing the fuel alone."},
        {"type": "explainer", "id": "cakes-and-airbags",
         "text": "The same reaction type is why cakes rise, and why an airbag "
                 "can inflate in thirty milliseconds. Sodium "
                 "hydrogencarbonate in baking powder decomposes in the oven "
                 "and the carbon dioxide it releases is trapped as bubbles in "
                 "the batter. An airbag holds a solid, sodium azide, which "
                 "decomposes to nitrogen gas fast enough to fill a bag before "
                 "your head arrives — a reaction chosen precisely because one "
                 "solid becomes an enormous volume of gas, on command."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The key is `definition`, NOT `gloss` — `build_ks3.py:939` hard-indexes
    # `v["definition"]`. Every technical term the lesson introduces, glossed at
    # the reading age the lesson is written for.
    "vocabulary": [
        {"term": "thermal decomposition",
         "definition": "Breaking one compound down into two or more "
                       "substances using heat. Nothing else is added, and it "
                       "does not go back when it cools."},
        {"term": "compound",
         "definition": "A substance made of two or more different kinds of "
                       "atom joined together. Copper carbonate is copper, "
                       "carbon and oxygen joined."},
        {"term": "reactant",
         "definition": "A substance you start with. A decomposition has only "
                       "one, which is what makes it unusual."},
        {"term": "product",
         "definition": "A substance you end up with. A decomposition makes "
                       "two or more of them from a single reactant."},
        {"term": "limewater",
         "definition": "A clear liquid used to test a gas. It turns milky "
                       "when carbon dioxide is bubbled through it, and for "
                       "nothing else.",
         "note": "Milky and cloudy mean the same thing here."},
        {"term": "quicklime",
         "definition": "The everyday name for calcium oxide, the white solid "
                       "left when limestone is decomposed. It is the basis of "
                       "cement."},
        {"term": "absorbs energy",
         "definition": "Takes energy in rather than giving it out. A "
                       "decomposition absorbs energy for as long as you keep "
                       "heating it, which is why it stops when the flame "
                       "comes off."},
    ],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⚑ NEW PROSE, and the only new prose in this file. Reported to the
    # commander (contract §16) rather than added silently.
    #
    # ⊖ NO SAFEGUARDING BLOCK, and that is the right call: this is a substance
    # lesson and nothing on it touches a student's own body, health or
    # circumstances. C3 and C4 carried none for the same reason.
    #
    # ⊕ A `safety_note` IS earned, and it is a different thing — small, at the
    # foot, beside the standing legal line, NOT a callout. Two of the three
    # substances on this page are things a twelve-year-old could plausibly get
    # hold of and heat: baking soda is in a kitchen cupboard and the page says
    # so twice, and the copper carbonate run is described as "the school
    # version" of the reaction. The specific hazard is the one this exact
    # apparatus has and no other: a tube of gas bubbling into limewater, with
    # the flame about to come off at stage 4. Cold liquid drawn back into hot
    # glass cracks it.
    #
    # Scoped so it does not retract the lesson's own content. It does not say
    # "never heat anything" — the whole page is about heating things — and it
    # does not contradict stage 4, which says the flame comes off; it names the
    # step that belongs immediately before it. §7 forbids a lesson retracting
    # itself later on the same page, and this adds to the method rather than
    # withdrawing it.
    "safety_note": "These are demonstrations, not things to try at home. Take "
                   "the tube carrying the gas out of the limewater before the "
                   "flame comes off, or cold liquid is drawn back into the "
                   "hot test tube and cracks it.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why nothing burnt in the tube?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Endothermic reactions and reaction profiles, and thermal "
                   "decomposition in the extraction of metals and the making "
                   "of cement.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
