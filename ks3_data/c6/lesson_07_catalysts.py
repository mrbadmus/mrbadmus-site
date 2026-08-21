"""C6 L7 — Catalysts (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-07-catalysts.dc.html` (621 lines), and her
author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §1, §3, §5 flags 13,
14, 15, 16, §6 (`ACID-10`) and §7.

── THE FIFTH FLASK IS THE LESSON ───────────────────────────────────────

Four flasks would teach "a catalyst makes a reaction faster", and a student who
learned only that would call dilute acid a catalyst, which is the fifth flask
and is wrong. The definition has TWO halves — faster AND not consumed — and the
bench is built so that the second half has to be used.

NOTES-C6 §5 flag 15 keeps that trial deliberately, and `r_catalyst_bench`
asserts the shape rather than trusting it (§5A — a comparative label is DERIVED
at render, and every element is checked rather than a sample):

  · every reading is parsed as a NUMBER and compared against the control's, so
    "faster" is derived rather than typed beside the thing it describes;
  · every trial flagged as a catalyst must be faster AND declared recovered;
  · at least one trial must be faster and NOT a catalyst, or the bench teaches
    that speeding a reaction up is sufficient;
  · at least two trials must change nothing, because the second control — sand,
    a solid with a large surface area that does nothing — is what stops the
    student concluding that adding a powder is the thing that matters.

An edit that lowered the manganese dioxide figure below the control's would
fail the build rather than leave a page calling it a catalyst.

── SCIENCE FLAGS ───────────────────────────────────────────────────────

⚑ Flags 13 and 16 — THE FIGURES ARE ILLUSTRATIVE AND THE PAGE SAYS SO WHERE IT
REPORTS THEM. 48 cm³ in 60 s for manganese dioxide and 55 cm³ for liver are
plausible classroom values, not measurements from one run, and quoting them
without saying so invites a student to cite them as data. `figures_note` is
rendered directly under the two readouts on every trial, and
`r_catalyst_bench` refuses a bench that reports volumes without one.

⚑ Flag 16 — THE "NINE TENTHS" CLAIM IS REPLACED BY A RANGE. Design's stretch
says "roughly nine tenths of everything manufactured by the chemical industry
passes over a catalyst". The figure is widely quoted and not sourced, and the
commander ruled for a range: "the great majority". Nothing else in that
paragraph changes, because the ARGUMENT — that the saving is energy and money,
every hour, for the life of the plant — does not depend on the precise
fraction.

⚑ Flag 14 — CATALASE NAMED, AND THE BOILED-LIVER CONTROL DESCRIBED. KEPT. It
is the cross-link to B8 and it is what makes the fourth flask more than a
curiosity: an enzyme with the wrong shape is no longer a catalyst, which is the
same "blocked, not consumed" idea `#s-think` is about, arriving from the other
direction.

⚑ Flag 15 — THE DILUTE-ACID TRIAL. KEPT, and stated at KS3 precisely: faster,
consumed as it goes, and therefore not a catalyst. The page does not claim to
explain the acid's mechanism, and `why` says what is observable — the rate
falls away and you cannot recover what you added — rather than a story about
what the acid is doing.

── MRB-225: NOTHING HERE IS RETRACTED BY A LATER SENTENCE ──────────────

The two claims that could have contradicted each other are made in one place
each and the instrument is the evidence for both. "A catalyst is not used up"
is the bench's recovered-mass readout; "catalytic converters do stop working"
is `#s-think`, and it resolves as POISONED rather than consumed rather than
softening the first claim. The key note states both.
"""

# ── the five flasks (Design's `TRIALS`) ─────────────────────────────────
#
# ⚠️ THE FIRST TRIAL IS THE CONTROL, AND `r_catalyst_bench` READS IT AS ONE.
# Every other reading is compared against its 2 cm³ to derive whether that
# trial was faster; a bench that opened on a catalyst would be measuring
# against something that already changed the answer, and the renderer refuses
# it.
#
# `catalyst` and `recovered` reach NO markup. They are the ground truth the
# derived comparison is checked against — the same job `rust` does in c5-03's
# control tubes — and the student meets the verdict as a paragraph of words
# after the trial has been run.
_TRIALS = [
    {"id": "t1", "label": "Nothing added", "catalyst": False,
     "recovered": False, "volume": "2 cm³", "mass": "none added",
     "setup": "50 cm³ of hydrogen peroxide solution in a conical flask, with "
              "a delivery tube to a gas syringe. Nothing else.",
     "result": "A few bubbles. Almost nothing in a minute.",
     "why": "The control, and the one that proves the reaction was always "
            "happening. Hydrogen peroxide decomposes into water and oxygen on "
            "its own — it is simply too slow to watch. Everything that "
            "follows is a comparison against this flask."},
    # ⭐ THE SECOND CONTROL, AND IT IS THE IMPORTANT ONE. Without it the bench
    # would let a student conclude that adding a powder is what matters.
    {"id": "t2", "label": "Sand", "catalyst": False, "recovered": False,
     "volume": "2 cm³", "mass": "1.00 g of 1.00 g",
     "setup": "The same peroxide, with one spatula of clean dry sand stirred "
              "in.",
     "result": "No change. The same few bubbles as the empty flask.",
     "why": "The second control, and the important one. Sand is a solid, it "
            "is insoluble, it has a large surface area — and it does nothing. "
            "Adding a powder is not what makes a catalyst; being the right "
            "powder is."},
    {"id": "t3", "label": "Manganese dioxide", "catalyst": True,
     "recovered": True, "volume": "48 cm³", "mass": "1.00 g of 1.00 g",
     "setup": "The same peroxide, with one spatula of black manganese dioxide "
              "stirred in.",
     "result": "Immediate vigorous frothing. The syringe fills in under a "
               "minute.",
     "why": "A catalyst. The reaction is the same reaction giving the same "
            "products — the oxygen relights a glowing splint either way — but "
            "it is finished in a minute rather than a year. Filter, dry and "
            "weigh the powder and every milligram is still there."},
    # ⚑ Flag 14 lives in this trial's `why` and is kept whole: catalase named,
    # and the boiled-liver control described. It is B8's content arriving here
    # as the reason a lump of liver behaves like a chemical.
    {"id": "t4", "label": "Fresh liver", "catalyst": True, "recovered": True,
     "volume": "55 cm³", "mass": "unchanged",
     "setup": "The same peroxide, with a small piece of fresh liver dropped "
              "in.",
     "result": "Violent frothing, faster than the manganese dioxide, and the "
               "foam climbs the flask.",
     "why": "Also a catalyst, and a biological one. Liver is full of "
            "catalase, an enzyme that exists to destroy hydrogen peroxide "
            "inside cells. Boil the liver first and it does nothing at all — "
            "heat destroys the enzyme's shape, and the shape is what does the "
            "work."},
    # ⭐ ⚑ FLAG 15. THE DISCRIMINATING ITEM. Faster, and still not a catalyst.
    {"id": "t5", "label": "Dilute acid", "catalyst": False, "recovered": False,
     "volume": "19 cm³", "mass": "partly consumed",
     "setup": "The same peroxide, with 5 cm³ of dilute acid added.",
     "result": "A noticeable increase in bubbling, then it tails off.",
     "why": "Faster, but not a catalyst. The acid is consumed as it goes, "
            "which is why the rate falls away and why you cannot recover what "
            "you added. Changing the speed is not sufficient — a catalyst "
            "must also come out unchanged."},
]

# ── the three judgements (Design's `USES`) ──────────────────────────────
#
# ⭐ THE THIRD IS THE LIMIT OF THE IDEA, and it reaches back to `acid-plus-
# metal`: a catalyst cannot make copper react with acid, because there is no
# reaction to speed up. That is the same claim rung 1's third distractor makes
# and it is the boundary the whole lesson needs — without it "catalyst" drifts
# into "makes things happen".
_USES = [
    {"id": "u1",
     "q": "A catalytic converter in a car exhaust contains platinum and "
          "rhodium — expensive metals. Why is the cost tolerable?",
     "options": [{"id": "a", "label": "Only a tiny amount is needed and it is "
                                      "not used up"},
                 {"id": "b", "label": "They are cheap in bulk"},
                 {"id": "c", "label": "They are replaced every service"}],
     "answer": "a",
     "reply": "Because a catalyst is not consumed, a few grams coating a "
              "honeycomb can process the exhaust of a car for its entire "
              "life. If the metal were a reactant it would need topping up "
              "like fuel, and no car would be affordable. The converter turns "
              "carbon monoxide and unburnt fuel into carbon dioxide and water "
              "on the way out of the engine."},
    {"id": "u2",
     "q": "A factory reaction runs at 450 °C without a catalyst and 250 °C "
          "with one, producing the same amount of product. Which matters more "
          "to the company?",
     "options": [{"id": "a", "label": "The temperature saving"},
                 {"id": "b", "label": "The amount of product"},
                 {"id": "c", "label": "Neither"}],
     "answer": "a",
     "reply": "The temperature. The yield is the same either way, so the "
              "catalyst is not making more of anything — it is making the "
              "same amount for less fuel, every hour, for decades. Two "
              "hundred degrees across an industrial plant is an enormous "
              "quantity of energy, which is why almost every large-scale "
              "process is catalysed."},
    {"id": "u3",
     "q": "Would adding a catalyst make copper react with dilute hydrochloric "
          "acid?",
     "options": [{"id": "a", "label": "Yes, that is what catalysts are for"},
                 {"id": "b", "label": "No — a catalyst only speeds up a "
                                      "reaction that can already happen"},
                 {"id": "c", "label": "Only with enough catalyst"}],
     "answer": "b",
     "reply": "No, and this is the limit of what a catalyst is. Copper is "
              "below hydrogen in the reactivity series, so there is no "
              "reaction to speed up. A catalyst shortens the time a possible "
              "reaction takes; it cannot make an impossible one occur, "
              "however much you add."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 230 character for character.
    "slug":        "catalysts",
    "title":       "Catalysts",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.CR.08` is "what catalysts do", and this lesson owns all of it: the
    # bench establishes both halves of the definition, `#s-uses` says why
    # anybody cares, and `#s-think` draws the line between blocked and
    # consumed.
    "covers":      ["KS3.C.CR.08"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "energy", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires":    ["making-a-pure-dry-salt"],
    "assumes":     [],
    # `#s-uses` item 3 argues from where copper sits relative to hydrogen,
    # which is `acid-plus-metal`'s content and is declared rather than assumed.
    "references":  ["acid-plus-metal"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A spatula of black powder turns a bottle that has been "
                    "sitting still for a year into a reaction that is over in "
                    "twenty seconds. Weigh the powder afterwards and none of "
                    "it has gone.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`. `done_when` restates her own `DONE()`: the
    # hook on a commitment, the bench when ALL FIVE flasks have been run — the
    # argument is a comparison across the set and four cannot make it — the
    # judgements when all three are decided, `#s-think` on a commitment, and
    # the ladder when every rung is answered.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The black powder", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Five flasks", "done_when": "all_five_run"},
        {"anchor": "s-uses",   "short": "USES",
         "label": "Three judgements", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Used up or blocked", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK CLOSES THREE DOORS BEFORE IT ASKS. "A black powder that is
    # not one of the reactants and not one of the products" rules out A and C;
    # "hydrogen peroxide slowly falls apart… left alone, a bottle takes about a
    # year" rules out D. What is left is the thing the lesson is for, and a
    # student still has to notice that the powder came back weighing the same.
    "phenomenon": {
        "kind": "narrative",
        "title": "Hydrogen peroxide slowly falls apart into water and oxygen. "
                 "Left alone, a bottle takes about a year.",
        "prompt": "Tip in a spatula of manganese dioxide — a black powder "
                  "that is not one of the reactants and not one of the "
                  "products — and the same bottle froths over in seconds, "
                  "giving off enough oxygen to relight a glowing splint. "
                  "Filter the mixture afterwards and the black powder is "
                  "still there, all of it, dry and weighing exactly what it "
                  "did.",
        "commit": "What did the black powder do?",
        # MRB-177: 6, 9, 5, 11 words. The correct option is index 1 and is not
        # the longest — D is. Design's set, unchanged.
        "options": [
            "It reacted with the hydrogen peroxide",
            "It made the reaction go faster without taking part",
            "It produced the oxygen itself",
            "It made a reaction happen that could not otherwise occur",
        ],
        "reveal": "It made the reaction go faster, and took no part in it. "
                  "The reaction was always going to happen — hydrogen "
                  "peroxide decomposes on its own — and the powder only "
                  "changed how long it took. Nothing was added to the "
                  "products, nothing was consumed, and the powder can be "
                  "dried and used again tomorrow. That is a "
                  "<strong>catalyst</strong>.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⊖ `think-reveal-poisoning` cannot be emitted from a lane — the `#s-think`
    # reveal panel is drawn by the shared `r_activity` with no id. `ACID-10`
    # names the activity that holds both its commitment and its answer, which
    # is the `c5-02` reconciliation and what satisfies Law 3.
    "misconceptions": [
        {"id": "ACID-10",
         "statement": "A catalyst is used up slowly, which is why it wears "
                      "out.",
         "elicited_by": "think-commit-consumed",
         "confronted_by": "think-commit-consumed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>catalyst</strong> is a substance that speeds up a "
                 "chemical reaction without being used up by it. At the end "
                 "there is exactly as much catalyst as there was at the "
                 "start, and it can be recovered and reused."},
        {"type": "explainer",
         "text": "A catalyst does not make an impossible reaction happen, and "
                 "it does not change what the products are. It changes one "
                 "thing only: <strong>how fast</strong>."},

        # #s-bench — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ THE LEAD IS THE ARGUMENT, NOT THE COUNT. Design's line is "N of 5
        # run. Two of the five are catalysts, two are controls, and one speeds
        # the reaction up and still does not qualify." The count is the block
        # head's counter; the rest is the whole construction of the bench said
        # out loud before the student starts, and it is kept — a student who
        # knows one of them is a ringer reads the fifth flask properly.
        {"type": "catalyst-bench", "id": "bench-five", "anchor": "s-bench",
         "eyebrow": "Your turn · five flasks",
         "heading": "Same hydrogen peroxide in every flask. One spatula of "
                    "something added to each.",
         "prompt": "Two of the five are catalysts, two are controls, and one "
                   "speeds the reaction up and still does not qualify.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} run", "start": 0},
         "trials": _TRIALS,
         "volume_label": "Oxygen after 60 s",
         "mass_label": "Solid recovered",
         # ⚑ FLAGS 13 AND 16. The figures are illustrative and the page says
         # so where it reports them, on every trial, directly under the two
         # readouts. `r_catalyst_bench` refuses a bench that reports volumes
         # without this note.
         "figures_note": "These volumes are illustrative of what the five "
                         "flasks show against each other, not measurements "
                         "from one run.",
         "predict_prompt": "Predict before you run it.",
         "predict_options": [{"id": "fast", "label": "Much faster"},
                             {"id": "same", "label": "No real change"},
                             {"id": "slow", "label": "Slower"}],
         "close": {"id": "bench-pattern",
                   "title": "Two of the five were catalysts, and one of those "
                            "was alive.",
                   "paras": [
                       "The sand did nothing, which is the control: adding a "
                       "solid is not enough on its own. The acid changed the "
                       "speed too, but it was consumed doing it — so it is a "
                       "reactant, not a catalyst. Manganese dioxide and liver "
                       "both sped the reaction up and both came back weighing "
                       "the same.",
                       "Note the total oxygen. Every flask that was left long "
                       "enough produced the same amount in the end. <strong>A "
                       "catalyst changes when the reaction finishes, not how "
                       "much it makes.</strong>",
                   ]}},

        {"type": "key-fact", "ref": "faster-and-unchanged"},

        # #s-uses — three judgements. Light `ks3-block` → `check`.
        #
        # ⚠️ NO `prompt`. Design draws the eyebrow and the h2 and goes straight
        # to the three cards on this one — unlike her other four judgement
        # blocks — and §5A forbids narrating the controls. "Why anybody cares"
        # IS the ask.
        {"type": "acid-judgements", "id": "uses-three", "anchor": "s-uses",
         "eyebrow": "Three judgements",
         "heading": "Why anybody cares",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "items": _USES},

        {"type": "misconception", "id": "think-commit-consumed",
         "anchor": "s-think", "targets": "ACID-10"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. The bench IS the picture — five flasks with two readouts each —
    # and a drawn reaction profile would be KS4's diagram arriving three years
    # early to explain a mechanism this page deliberately does not claim.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "faster-and-unchanged",
         "text": "A catalyst speeds up a reaction and is not used up by it. "
                 "The mass of catalyst at the end equals the mass at the "
                 "start, and the products are unchanged.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-consumed",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-10",
         "prompt": "Catalytic converters really do have to be replaced "
                   "eventually. Commit before you read on.",
         # MRB-177: 13, 15, 12, 13 words. The correct option is index 1 and is
         # longest by two words at 1.15x, which is inside both thresholds. The
         # distractors are lengthened to Design's own shape rather than left at
         # 11, 5 and 5; her B is untouched and the answer has not moved.
         "options": [
             "Right — it is consumed slowly, which is why a converter "
             "eventually stops working",
             "Wrong — the mass is unchanged; catalysts fail by being coated "
             "or damaged, not consumed",
             "Right, because nothing lasts forever and every part of a car "
             "wears out in the end",
             "Wrong — catalysts never stop working, so a converter that fails "
             "was faulty to begin with",
         ],
         "reveal": [
             "The balance settles it. Weigh the manganese dioxide before, "
             "filter it out afterwards, dry it and weigh it again: the mass "
             "is the same, and the same spatula of powder will run the "
             "reaction again tomorrow. Nothing is being slowly consumed.",
             "Catalysts do fail in the real world, but not by being used up. "
             "They get <strong>poisoned</strong> — coated by something else "
             "that sticks to the surface and blocks it — or physically "
             "clogged, or damaged by heat. That is why leaded petrol destroys "
             "a catalytic converter: the lead covers the surface the reaction "
             "needs. <strong>Blocked is not the same as consumed.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        # Design's options, untouched; the answer moves to index 1 (MRB-278).
        # MRB-177: 6, 8, 7, 8 words — the correct option is joint-longest and
        # nothing here is a tell.
        "recall": {
            "q": "What does a catalyst do?",
            "options": [
                "Makes a reaction produce more product",
                "Speeds up a reaction without being used up",
                "Starts reactions that could not otherwise happen",
                "Is used up gradually as the reaction proceeds",
            ],
            "answer": 1,
            "feedback": {
                0: "The amount of product is unchanged. Only the time taken "
                   "is different.",
                2: "A catalyst can only speed up a reaction that is already "
                   "possible.",
                3: "That would make it a reactant. A catalyst weighs the same "
                   "at the end as at the start.",
            }},
        # Design's options, untouched; the answer moves to index 0 (MRB-278).
        # MRB-177: 12, 6, 12, 7 words — the correct option is JOINT longest
        # with option C, which is inside both thresholds, and it is the shape
        # §13 wants: the two long options are the two that state a rule and a
        # student has to choose between them on the chemistry.
        "apply": {
            "q": "Two flasks of hydrogen peroxide are left until the reaction "
                 "is completely finished. One had a catalyst, one did not. "
                 "How do the volumes of oxygen compare?",
            "options": [
                "They are the same — the catalyst changed the speed, not the "
                "amount",
                "The catalysed flask produces more oxygen",
                "The catalysed flask produces less, because some is used by "
                "the catalyst",
                "It depends how much catalyst was added",
            ],
            "answer": 0,
            "feedback": {
                1: "The same peroxide can only give the same oxygen. What "
                   "changed was how long it took.",
                2: "The catalyst consumes nothing. Filter it out at the end "
                   "and it is all still there.",
                3: "More catalyst goes faster still, but the final volume is "
                   "set by the amount of peroxide.",
            }},
        "explain": {
            "q": "Describe an experiment that would prove a black powder is "
                 "acting as a catalyst in the decomposition of hydrogen "
                 "peroxide, and say what results would settle it.",
            "field_label": "Your method",
            "placeholder": "I would run the reaction with and without…",
            "success": [
                "Runs the reaction with and without the powder, keeping "
                "everything else the same.",
                "Measures the volume of gas produced against time, or the "
                "time taken.",
                "Says the reaction is faster with the powder present.",
                "Weighs the powder before, then filters, dries and weighs it "
                "afterwards.",
                "Says an unchanged mass, plus a faster rate, shows it is a "
                "catalyst.",
            ]},
        "produce": {
            "q": "Catalytic converters stop working if a car runs on leaded "
                 "petrol, but the platinum inside has not been consumed. "
                 "Explain how a catalyst can fail without being used up, and "
                 "what that tells you about how catalysts work.",
            "field_label": "Your answer",
            "placeholder": "The platinum is still there, but…",
            "success": [
                "Says the platinum is still present and has not been "
                "consumed.",
                "Says the lead coats or sticks to the platinum.",
                "Says the reacting substances can no longer reach the "
                "catalyst.",
                "Concludes that the reaction must happen on the surface of "
                "the catalyst.",
                "Says this is why catalysts are made with a very large "
                "surface area.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A catalyst speeds up a chemical reaction without being used "
                "up. It can be filtered out at the end, weighs the same as it "
                "did at the start, and can be used again. It does not change "
                "the products and it does not make impossible reactions "
                "happen — it only changes the rate. Enzymes are the catalysts "
                "living things use.",

    # ── the stretch layer (§5.6) ────────────────────────────────────────────
    # ⚑ FLAG 16, RULED: "roughly nine tenths of everything manufactured" is
    # replaced by "the great majority". The figure is widely quoted and not
    # sourced, and the paragraph's argument — that the saving is energy and
    # money, every hour, for the life of the plant — does not depend on the
    # precise fraction. Nothing else in it moves.
    #
    # ⚑ FLAG 14 lives in the second paragraph and is kept whole: catalase
    # named, the boiled-liver control described, and the shape argument made.
    "stretch": [
        {"type": "explainer", "id": "money-and-energy",
         "text": "The great majority of everything manufactured by the "
                 "chemical industry passes over a catalyst at some point. The "
                 "reason is money and energy: a reaction that needs 400 °C "
                 "without a catalyst and 200 °C with one costs half as much "
                 "to run, every hour, for the life of the plant. The ammonia "
                 "process that makes the world's fertiliser runs over iron, "
                 "and the catalyst is the difference between a reaction that "
                 "is possible and a reaction that is worth doing."},
        {"type": "explainer", "id": "enzymes",
         "text": "Your own body is running thousands of catalysed reactions "
                 "at this moment, at 37 °C, which is a temperature at which "
                 "almost none of them would otherwise proceed usefully. The "
                 "catalysts are enzymes — large protein molecules, each "
                 "shaped to fit one particular reaction. The liver in the "
                 "flask worked because it is full of catalase, an enzyme "
                 "whose job is to destroy hydrogen peroxide before it damages "
                 "cells. Boil the liver first and nothing happens: heat "
                 "wrecks the shape, and an enzyme with the wrong shape is no "
                 "longer a catalyst."},
    ],

    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Catalyst",
         "definition": "A substance that speeds up a chemical reaction "
                       "without being used up by it. It weighs the same at "
                       "the end as it did at the start."},
        {"term": "Rate",
         "definition": "How fast a reaction goes. A catalyst changes the rate "
                       "and nothing else — not the products, and not how much "
                       "is made."},
        {"term": "Enzyme",
         "definition": "A catalyst made by a living thing. Catalase, in "
                       "liver, is the one that breaks hydrogen peroxide down.",
         "note": "Heat destroys an enzyme's shape, and the shape is what does "
                 "the work."},
        {"term": "Poisoned",
         "definition": "A catalyst that has been coated by something that "
                       "blocks its surface. It is still all there — it just "
                       "cannot be reached."},
        {"term": "Control",
         "definition": "A trial run with the thing you are testing left out, "
                       "so you know what would have happened anyway."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚑ NEW PROSE. ⊖ No safeguarding block — lab safety, and it names the two
    # hazards this exact bench has rather than issuing a general warning.
    "safety_note": "Hydrogen peroxide at the strength used here bleaches skin "
                   "and damages eyes, and the liver flask froths over: it is "
                   "run in a large flask standing in a tray, with eye "
                   "protection on. Manganese dioxide is harmful if swallowed "
                   "and the recovered powder is not handled with bare hands.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure how something can change a reaction and "
                      "not take part?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Catalysts lowering activation energy, reaction profiles "
                   "with and without one, and enzymes as biological catalysts "
                   "with optimum temperatures and pH.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    "review_state": "draft",
}
