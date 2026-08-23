"""C6 L6 — Making a pure dry salt (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-06-making-a-salt.dc.html` (650 lines), and her
author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §1, §3, §4, §6
(`ACID-09`) and §7.

⚠️ THE TITLE AND SLUG ARE `structure.py`'s, NOT THE PAGE'S. Design's page is
headed "Making a salt"; the skeleton's slot is `making-a-pure-dry-salt` /
"Making a pure dry salt". The slug is permanent (§8.4). The skeleton's title is
also the better one here: PURE and DRY are the two words the whole lesson is
about, and "making a salt" is the easy half that the hook dispatches in one
sentence.

⊖ **SUPERSEDED 23 Aug 2026 (MRB-281). `lesson_05_acids_and_carbonates.py`
EXISTS.** The paragraph below is kept because it is a statement that the file
is deliberately absent, and acting on it now would delete a shipped lesson.

> ⚠️ **THERE IS NO `lesson_05_` IN THIS PACKAGE AND THAT IS A RULING, NOT AN
> OVERSIGHT.** See `ks3_data/c6/__init__.py`. Design drew
> `c6-05-acids-and-carbonates` in `structure.py`'s `acid-plus-alkali` slot and
> flagged the divergence herself; the commander ruled that the slot stays
> unauthored and renders an honest coming-soon page. This lesson's "Before
> this lesson" link on Design's page points at that page; the generator's own
> `lesson_neighbours` skips unauthored slots, so the built page links back to
> `acid-plus-metal` instead and nothing points at a page that does not exist.

Mide overrode the retirement and the slot was renamed in place to
`acids-and-carbonates` and authored. `lesson_neighbours` therefore resolves
this lesson's "Before this lesson" to `acids-and-carbonates.html`, which is
what Design's own page draws — verified on the built page rather than assumed,
and nothing here was hand-wired to make it happen.

════════════════════════════════════════════════════════════════════════
⚠️ AN UNRESOLVED GATE CONFLICT, REPORTED RATHER THAN WORKED AROUND
════════════════════════════════════════════════════════════════════════

C6 owns FIVE statutory bullets — `KS3.C.CR.04` through `CR.08` — and builds SIX
lessons. `validate()` rule 3 fails an authored lesson with an empty `covers`;
rule 4 fails a statement owned by two lessons. Five into six does not go, and
there is no allocation of the five bullets that satisfies both rules.

The mechanism the architecture provides for exactly this is `substatements.py`,
which is how `KS3.C.CR.03` became five clauses for C5's five lessons and how
`KS3.C.ENER.02` became three for C7's four. The commander's brief for this unit
says explicitly **not** to mint clauses, and `substatements.py` is the
commander's file.

So this lesson declares `covers: ["KS3.C.CR.07b"]` and `neutralisation`
declares `["KS3.C.CR.07a"]`, and the two clauses they name **do not exist
yet**. The block that mints them is written out for the commander at
`<scratch>/c6-substatements-block.py` rather than spliced into
`ks3_data/substatements.py` here.

  · WITH that splice, the unit builds and both rules pass.
  · WITHOUT it, the build fails naming `KS3.C.CR.07a` and `KS3.C.CR.07b`.

That is a loud failure rather than a quiet one, which is the right direction:
the alternative was `covers: []` here, which fails rule 3 with a less
informative message, or `beyond_statutory: True`, which would be a lie — making
a pure dry salt is what "reactions of acids with alkalis to produce a salt plus
water" demands, not off-spec content.

The split itself is Design's own, from NOTES-C6 §1: "`CR.07` is split across
two lessons on purpose: `neutralisation` establishes the equation and the pH
curve, `making-a-salt` turns it into a preparation with a filtration step."

════════════════════════════════════════════════════════════════════════

── THE HOOK IS THE WHOLE INVESTIGATION IN ONE DECISION ─────────────────

"How much copper oxide should you add?" is not a warm-up. The answer — MORE
than you need — is counter-intuitive, it is the reason the method has a
filtration step in it, and it is the difference between a pure product and one
contaminated with leftover acid. Everything after it is the consequence:
`#s-name` is why the salt is called what it is called, `#s-method` is the six
decisions in order, and `#s-think` is the last one that can still ruin it after
everything else has gone right.

── TWO INSTRUMENTS, AND THE SECOND HAS NO CHEMISTRY IN IT ──────────────

`salt-namer` runs a rule — the metal names the salt, the acid names its ending
— across twelve combinations. `r_salt_namer` runs the SAME rule at build time
and refuses any mix whose authored name disagrees with it, refuses a duplicate
option, and refuses a carbonate whose products forget the carbon dioxide.

`method-order` is generic: `{steps: [{id, text, why}], shuffled: [id…]}` and no
chemistry anywhere in the renderer. NOTES-C6 §4 flags it as the obvious
instrument for any "put the method in order" task in any subject, and C10-03's
rock cycle journey is already named as its second placement.
"""

# ── the three acids and the four bases (Design's `ACIDS` and `BASES`) ───
#
# `ending` and `metal` are the two halves of the rule the bench teaches, and
# `r_salt_namer` composes them at BUILD time and checks the answer against the
# result. `kind` and `soluble` drive the note under each equation: a carbonate
# also gives carbon dioxide, and a base that dissolves cannot be filtered off.
_ACIDS = [
    {"id": "hcl",   "label": "Hydrochloric", "name": "hydrochloric acid",
     "ending": "chloride"},
    {"id": "h2so4", "label": "Sulfuric",     "name": "sulfuric acid",
     "ending": "sulfate"},
    {"id": "hno3",  "label": "Nitric",       "name": "nitric acid",
     "ending": "nitrate"},
]

_BASES = [
    {"id": "cuo",   "label": "Copper oxide",       "name": "copper oxide",
     "metal": "copper",    "kind": "oxide",     "soluble": False},
    {"id": "mgo",   "label": "Magnesium oxide",    "name": "magnesium oxide",
     "metal": "magnesium", "kind": "oxide",     "soluble": False},
    {"id": "naoh",  "label": "Sodium hydroxide",   "name": "sodium hydroxide",
     "metal": "sodium",    "kind": "hydroxide", "soluble": True},
    {"id": "caco3", "label": "Calcium carbonate",  "name": "calcium carbonate",
     "metal": "calcium",   "kind": "carbonate", "soluble": False},
]

# The two notes, written once. Design composes both at run time out of the
# base's own fields; they are constants and they are constants HERE, so the
# twelve mixes below carry the sentence rather than a recipe for it.
_FIZZES = ("A carbonate gives carbon dioxide as well, so this one fizzes "
           "while it reacts. ")
_SOLUBLE = ("Sodium hydroxide dissolves, so excess cannot be filtered off — "
            "this salt has to be made by titration instead.")


def _insoluble(name):
    return ("%s is insoluble, so you can add it in excess and filter off what "
            "is left." % name)


# ── the twelve combinations, every one authored ─────────────────────────
#
# ⚠️ **THE ANSWER IS NOT ALWAYS THE FIRST BUTTON.** Design's generator puts the
# correct name at index 0 on all twelve, which makes "press the left-hand one"
# beat knowing the rule on every combination in the bench. The twelve are
# authored level at four apiece across indices 0, 1 and 2, and `r_salt_namer`
# both derives the correct name from the rule AND asserts that `answer` points
# at it — so the position can be balanced without the key drifting from the
# options beside it.
#
# The two wrong names on each card are Design's own two shapes: the right metal
# with the wrong ending, and the wrong metal with the right ending. Between
# them they catch the two halves of the rule separately.
_MIXES = [
    {"id": "hcl:cuo", "title": "Hydrochloric acid + copper oxide",
     "salt": "copper chloride",
     "options": ["Copper chloride", "Copper sulfate", "Sodium chloride"],
     "answer": 0,
     "eq_left": "hydrochloric acid + copper oxide",
     "eq_right": "copper chloride + water",
     "note": _insoluble("Copper oxide")},
    {"id": "hcl:mgo", "title": "Hydrochloric acid + magnesium oxide",
     "salt": "magnesium chloride",
     "options": ["Magnesium sulfate", "Magnesium chloride", "Copper chloride"],
     "answer": 1,
     "eq_left": "hydrochloric acid + magnesium oxide",
     "eq_right": "magnesium chloride + water",
     "note": _insoluble("Magnesium oxide")},
    {"id": "hcl:naoh", "title": "Hydrochloric acid + sodium hydroxide",
     "salt": "sodium chloride",
     "options": ["Sodium sulfate", "Copper chloride", "Sodium chloride"],
     "answer": 2,
     "eq_left": "hydrochloric acid + sodium hydroxide",
     "eq_right": "sodium chloride + water",
     "note": _SOLUBLE},
    {"id": "hcl:caco3", "title": "Hydrochloric acid + calcium carbonate",
     "salt": "calcium chloride",
     "options": ["Calcium chloride", "Calcium sulfate", "Copper chloride"],
     "answer": 0,
     "eq_left": "hydrochloric acid + calcium carbonate",
     "eq_right": "calcium chloride + water + carbon dioxide",
     "note": _FIZZES + _insoluble("Calcium carbonate")},

    {"id": "h2so4:cuo", "title": "Sulfuric acid + copper oxide",
     "salt": "copper sulfate",
     "options": ["Copper chloride", "Copper sulfate", "Sodium sulfate"],
     "answer": 1,
     "eq_left": "sulfuric acid + copper oxide",
     "eq_right": "copper sulfate + water",
     "note": _insoluble("Copper oxide")},
    {"id": "h2so4:mgo", "title": "Sulfuric acid + magnesium oxide",
     "salt": "magnesium sulfate",
     "options": ["Magnesium chloride", "Copper sulfate", "Magnesium sulfate"],
     "answer": 2,
     "eq_left": "sulfuric acid + magnesium oxide",
     "eq_right": "magnesium sulfate + water",
     "note": _insoluble("Magnesium oxide")},
    {"id": "h2so4:naoh", "title": "Sulfuric acid + sodium hydroxide",
     "salt": "sodium sulfate",
     "options": ["Sodium sulfate", "Sodium chloride", "Copper sulfate"],
     "answer": 0,
     "eq_left": "sulfuric acid + sodium hydroxide",
     "eq_right": "sodium sulfate + water",
     "note": _SOLUBLE},
    {"id": "h2so4:caco3", "title": "Sulfuric acid + calcium carbonate",
     "salt": "calcium sulfate",
     "options": ["Calcium chloride", "Calcium sulfate", "Copper sulfate"],
     "answer": 1,
     "eq_left": "sulfuric acid + calcium carbonate",
     "eq_right": "calcium sulfate + water + carbon dioxide",
     "note": _FIZZES + _insoluble("Calcium carbonate")},

    {"id": "hno3:cuo", "title": "Nitric acid + copper oxide",
     "salt": "copper nitrate",
     "options": ["Copper chloride", "Sodium nitrate", "Copper nitrate"],
     "answer": 2,
     "eq_left": "nitric acid + copper oxide",
     "eq_right": "copper nitrate + water",
     "note": _insoluble("Copper oxide")},
    {"id": "hno3:mgo", "title": "Nitric acid + magnesium oxide",
     "salt": "magnesium nitrate",
     "options": ["Magnesium nitrate", "Magnesium chloride", "Copper nitrate"],
     "answer": 0,
     "eq_left": "nitric acid + magnesium oxide",
     "eq_right": "magnesium nitrate + water",
     "note": _insoluble("Magnesium oxide")},
    {"id": "hno3:naoh", "title": "Nitric acid + sodium hydroxide",
     "salt": "sodium nitrate",
     "options": ["Sodium chloride", "Sodium nitrate", "Copper nitrate"],
     "answer": 1,
     "eq_left": "nitric acid + sodium hydroxide",
     "eq_right": "sodium nitrate + water",
     "note": _SOLUBLE},
    {"id": "hno3:caco3", "title": "Nitric acid + calcium carbonate",
     "salt": "calcium nitrate",
     "options": ["Calcium chloride", "Copper nitrate", "Calcium nitrate"],
     "answer": 2,
     "eq_left": "nitric acid + calcium carbonate",
     "eq_right": "calcium nitrate + water + carbon dioxide",
     "note": _FIZZES + _insoluble("Calcium carbonate")},
]

# ── the six steps, in the order that works (Design's `METHOD`) ──────────
#
# The `why` on each is the block's real payoff and it is shown WHETHER OR NOT
# the order came out right — see `r_method_order`. Three of the six carry a
# decision that could ruin the preparation: m2 (excess on purpose), m4 (stop
# while there is still liquid) and m5 (slow cooling).
_METHOD = [
    {"id": "m1", "text": "Warm the acid gently in a beaker.",
     "why": "Warming speeds the reaction up. It is not boiled — that would "
            "drive acid off before it has reacted with anything."},
    {"id": "m2",
     "text": "Add the copper oxide a spatula at a time, stirring, until no "
             "more will dissolve.",
     "why": "Excess is deliberate. The black powder settling out means every "
            "last bit of acid has been used up, which is the only way to be "
            "sure none is left in your product."},
    {"id": "m3", "text": "Filter the mixture to remove the leftover copper "
                         "oxide.",
     "why": "The excess base is insoluble, so it stays on the filter paper "
            "while the blue copper sulfate solution passes through. This is "
            "the step that pays for adding too much."},
    {"id": "m4", "text": "Heat the filtrate to evaporate about half the "
                         "water.",
     "why": "Concentrating the solution, not drying it. You stop while there "
            "is still plenty of liquid — the test is a drop on a cold glass "
            "rod forming crystals."},
    {"id": "m5", "text": "Leave the concentrated solution to cool slowly.",
     "why": "Slow cooling is what grows large, regular crystals. Fast cooling "
            "gives a mass of tiny ones, and boiling to dryness gives powder."},
    {"id": "m6", "text": "Pat the crystals dry between filter papers.",
     "why": "The last of the mother liquor is dissolved salt, and it would "
            "dry as a crust on the surface. Patting rather than rubbing keeps "
            "the crystals whole."},
]

# Design's own `SHUFFLED`, unchanged. `r_method_order` asserts it is a real
# permutation AND that it is not already the correct order — a shuffle that
# happened to equal the answer would be a task finished before the student
# touched it, and it would look entirely normal in the source.
_SHUFFLED = ["m3", "m5", "m1", "m6", "m2", "m4"]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 229 character for character.
    "slug":        "making-a-pure-dry-salt",
    "title":       "Making a pure dry salt",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚠️ `KS3.C.CR.07b` DOES NOT EXIST YET. See the module docstring: five
    # bullets against six lessons is a genuine arithmetic conflict between
    # `validate()` rules 3 and 4, the mechanism for it is a minted clause, and
    # minting is the commander's call. The block is written out for splicing
    # and this lesson names the clause it needs.
    "covers":      ["KS3.C.CR.07b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "measurement-and-uncertainty", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires":    ["neutralisation"],
    "assumes":     [],
    # Crystallisation is C3's technique, used here rather than taught here —
    # this lesson's own claim is about WHY this order of steps, and `#s-think`
    # says outright that slow cooling is "the same rule you met when you
    # crystallised salt from solution".
    #
    # ⚠️ THE DICT FORM, because this crosses a unit boundary (MRB-248).
    "references":  [{"unit": "C3",
                     "lesson": "evaporation-and-crystallisation"}],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Blue crystals big enough to hold, grown from a beaker of "
                    "clear acid and a spoonful of black powder. Every step of "
                    "getting there is a decision you can get wrong.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`. `done_when` restates her own `DONE()`: the
    # hook on a commitment, the naming bench when three combinations have been
    # named, the method when all six steps are placed, `#s-think` on a
    # commitment, and the ladder when every rung is answered.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Blue crystals", "done_when": "committed"},
        {"anchor": "s-name",   "short": "NAME",
         "label": "Naming bench", "done_when": "three_named"},
        {"anchor": "s-method", "short": "METHOD",
         "label": "Build the method", "done_when": "all_six_placed"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Boiling dry", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK NAMES THE HARD PART BEFORE ASKING THE QUESTION. "The reaction
    # itself is easy… The hard part is what comes after" is what stops the
    # commitment being read as a question about chemistry: it is a question
    # about purity, and the answer is a method decision.
    "phenomenon": {
        "kind": "narrative",
        "title": "You are asked for a jar of pure copper sulfate crystals. "
                 "You are given sulfuric acid and black copper oxide powder.",
        "prompt": "The reaction itself is easy — the acid neutralises the "
                  "oxide and the solution turns blue. The hard part is what "
                  "comes after: getting a pure, dry, crystalline solid out of "
                  "a beaker of blue liquid, with no leftover acid and no "
                  "black powder in it.",
        "commit": "How much copper oxide should you add?",
        # MRB-177: 8, 9, 8, 8 words. The correct option is index 2 and is
        # joint-shortest. Design's set, unchanged.
        "options": [
            "Exactly the amount the equation says, weighed out",
            "A little less than you need, to be safe",
            "More than you need, until no more will react",
            "It makes no difference how much you add",
        ],
        "reveal": "More than you need, and then stop when no more will "
                  "dissolve. Copper oxide is a base that does not dissolve in "
                  "water, so the excess just sits on the bottom where you can "
                  "<strong>filter it off</strong>. Leftover acid could not be "
                  "removed like that — it would be dissolved in with your "
                  "product. Adding too much of the insoluble one is a problem "
                  "with a solution; adding too much acid is not.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⊖ `think-reveal-slow-cooling` cannot be emitted from a lane — the
    # `#s-think` reveal panel is drawn by the shared `r_activity` with no id.
    # `ACID-09` names the activity that holds both its commitment and its
    # answer, which is the `c5-02` reconciliation and what satisfies Law 3.
    "misconceptions": [
        {"id": "ACID-09",
         "statement": "Boiling a solution dry gives the best crystals.",
         "elicited_by": "think-commit-boil",
         "confronted_by": "think-commit-boil"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every neutralisation makes a salt, and the salt's name is "
                 "built from the two things that made it. The "
                 "<strong>metal</strong> gives the first word. The "
                 "<strong>acid</strong> gives the second: hydrochloric makes "
                 "chlorides, sulfuric makes sulfates, nitric makes nitrates."},
        {"type": "explainer",
         "text": "So the name tells you the recipe backwards. Copper sulfate "
                 "had to come from copper — as the metal, its oxide, its "
                 "hydroxide or its carbonate — and sulfuric acid. Nothing "
                 "else could have made it."},

        # #s-name — the naming bench. Light `ks3-block` → `check`.
        #
        # ⚠️ THE LEAD IS THE HALF OF DESIGN'S SENTENCE THAT TEACHES. Her line
        # is "N combinations named. Twelve are possible — three is enough to
        # see the rule." She draws no block-head counter on this section, so
        # the count is dropped rather than invented and the argument is kept.
        {"type": "salt-namer", "id": "namer-twelve", "anchor": "s-name",
         "eyebrow": "Your turn · the naming bench",
         "heading": "Pick an acid and a base. Name the salt before you check.",
         "prompt": "Twelve are possible — three is enough to see the rule.",
         "demand": "construct",
         "acid_label": "The acid",
         "base_label": "The base",
         "ask_prompt": "Which salt does this make?",
         "acids": _ACIDS,
         "bases": _BASES,
         "mixes": _MIXES,
         # Design's own `DONE`: three of the twelve.
         "done_at": 3},

        # #s-method — the method builder. Light `ks3-block` → `check`.
        #
        # ⚠️ NO NARRATION. Design's lead is a live count — "N of 6 placed" —
        # and at zero it reads "Tap them in the order you would carry them out.
        # Nothing is marked until all six are placed", which is the controls
        # read aloud plus platform self-explanation. §5A forbids the first and
        # §8.10 the second. The heading already says what to do ("Six steps,
        # shuffled. Put them in the order you would do them"), so the lead
        # carries the thing the heading cannot: what the ordering is FOR.
        {"type": "method-order", "id": "method-six", "anchor": "s-method",
         "eyebrow": "Your turn · build the method",
         "heading": "Six steps, shuffled. Put them in the order you would do "
                    "them.",
         "prompt": "Three of the six carry a decision that could ruin the "
                   "crystals, and the order is what makes each of them "
                   "possible.",
         "demand": "construct",
         "steps": _METHOD,
         "shuffled": _SHUFFLED,
         "clear_label": "Start the order again",
         "why_join": "—",
         # ⚠️ BOTH VERDICTS INTRODUCE THE SAME SIX REASONS, and neither is a
         # mark: no green, no red, no per-step tick. The six explanations are
         # the point of the block whether the order came out right or not.
         "verdicts": {
             "right": "That is the order, and every step earns its place.",
             "wrong": "Not the order that works. Here is the sequence and "
                      "what each step is for.",
         }},

        {"type": "key-fact", "ref": "excess-then-filter"},

        {"type": "misconception", "id": "think-commit-boil",
         "anchor": "s-think", "targets": "ACID-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page — the two instruments are the
    # pictures — and §5.4 allows an empty list where it does not allow an
    # absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "excess-then-filter",
         "text": "The metal names the salt and the acid names its ending. Use "
                 "excess insoluble base, filter it off, then crystallise — "
                 "because excess solid can be removed and excess acid cannot.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-boil",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-09",
         "prompt": "You do get a solid, and quickly. Commit before you read "
                   "on.",
         # MRB-177: 8, 12, 9, 9 words. The correct option is index 1 and is
         # longest by three words at 1.33x, which is inside both thresholds.
         # The distractors are lengthened to Design's own shape rather than
         # left at 6, 6 and 6; her B is untouched and the answer has not moved.
         "options": [
             "Right — heat gets the water off quickest, so the crystals come "
             "sooner",
             "Wrong — boiling dry gives a caked powder; crystals need slow "
             "cooling",
             "Right, because the crystals cannot boil away once the water has "
             "gone",
             "Wrong — the salt itself would be destroyed by the heat of "
             "boiling",
         ],
         "reveal": [
             "You get a solid, but not crystals. Boiling to dryness throws "
             "thousands of tiny crystals out of solution at once and leaves a "
             "caked powder, with whatever else was dissolved in the water "
             "trapped in it. Crystals need time: heat the solution until it "
             "is concentrated, stop while there is still liquid, and let it "
             "cool slowly.",
             "This is the same rule you met when you crystallised salt from "
             "solution — fast drying gives powder, slow cooling gives "
             "crystals. <strong>Big clean crystals are a product of patience, "
             "not heat.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        # Design's options, untouched; the answer moves to index 2 (MRB-278).
        # MRB-177: 2, 2, 3, 2 words — nothing here is a length tell.
        "recall": {
            "q": "Nitric acid is neutralised with magnesium oxide. What salt "
                 "is made?",
            "options": [
                "Magnesium sulfate",
                "Nitrogen magnesate",
                "Magnesium nitrate",
                "Magnesium oxide nitrate",
            ],
            "answer": 2,
            "feedback": {
                0: "Sulfates come from sulfuric acid. Nitric acid gives "
                   "nitrates.",
                1: "The metal always comes first and the acid supplies the "
                   "ending. There is no such compound.",
                3: "The oxide is used up in the reaction — its oxygen leaves "
                   "as part of the water.",
            }},
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 12 words against 7, 5 and 6:
        # strictly the longest by five and at 1.71x. Each now states a WRONG
        # RULE at the correct answer's own length — 13, 12, 12 against 12 — and
        # every one of Design's corrections is unchanged and still answers its
        # own option: the yield argument, the cost argument, the catalyst
        # argument.
        "apply": {
            "q": "Why is excess copper oxide added rather than an exactly "
                 "measured amount?",
            "options": [
                "Because more copper oxide makes more salt, so the yield goes "
                "up with it",
                "Because copper oxide is cheap, so wasting some of it costs "
                "almost nothing",
                "Because the reaction needs a catalyst and the extra oxide "
                "acts as one",
                "Because leftover solid can be filtered out, while leftover "
                "acid could not be",
            ],
            "answer": 3,
            "feedback": {
                0: "Once the acid is used up, extra base makes nothing. The "
                   "yield is set by the acid.",
                1: "Cost is not the reason. The reason is that the excess can "
                   "be removed and acid could not.",
                2: "No catalyst is involved — the excess is simply insurance "
                   "that no acid survives.",
            }},
        "explain": {
            "q": "Describe how you would make pure, dry crystals of magnesium "
                 "sulfate from sulfuric acid and magnesium oxide, and explain "
                 "the reason behind each of the three decisions that could "
                 "ruin it.",
            "field_label": "Your method",
            "placeholder": "I would warm the acid and then…",
            "success": [
                "Adds magnesium oxide in excess to warm sulfuric acid, "
                "stirring.",
                "Filters to remove the unreacted magnesium oxide.",
                "Evaporates some of the water rather than boiling to dryness.",
                "Leaves the solution to cool slowly so crystals grow.",
                "Explains that excess is used because the solid can be "
                "filtered off but excess acid could not.",
            ]},
        "produce": {
            "q": "A student needs to make sodium chloride crystals from "
                 "hydrochloric acid and sodium hydroxide. Explain why the "
                 "method above will not work, and what they must do instead.",
            "field_label": "Your answer",
            "placeholder": "Sodium hydroxide is different because…",
            "success": [
                "Says sodium hydroxide is soluble, so excess cannot be "
                "filtered off.",
                "Says there is no visible sign of when enough has been added.",
                "Says an indicator is used to find the exact volume that "
                "neutralises the acid.",
                "Says the experiment is then repeated with the same volumes "
                "and no indicator.",
                "Says the solution is then evaporated and cooled slowly to "
                "crystallise, as before.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A salt is named after the metal and the acid that made it: "
                "sulfuric acid gives sulfates, hydrochloric gives chlorides, "
                "nitric gives nitrates. To make a pure sample, react the acid "
                "with excess insoluble base, filter off what is left over, "
                "then evaporate part of the water and let the solution cool "
                "slowly so crystals grow.",

    # ── the stretch layer (§5.6) ────────────────────────────────────────────
    "stretch": [
        {"type": "explainer", "id": "the-soluble-case",
         "text": "Making a salt with a soluble alkali instead of an insoluble "
                 "base is a much harder job, and it is worth knowing why. "
                 "Sodium hydroxide dissolves, so excess cannot be filtered off "
                 "— there is no way to see when you have added enough. The "
                 "answer is to do the reaction twice: once with indicator to "
                 "find the exact volume that neutralises the acid, then again "
                 "with the same volumes and no indicator, so the crystals are "
                 "not stained with dye."},
        {"type": "explainer", "id": "salts-are-not-curiosities",
         "text": "Salts are not laboratory curiosities. Ammonium nitrate and "
                 "ammonium sulfate, made by neutralising acids with ammonia, "
                 "are the fertilisers that feed a large fraction of the "
                 "world; the process that makes the ammonia consumes about "
                 "one per cent of all energy generated on Earth. Copper "
                 "sulfate goes on vines as a fungicide, calcium sulfate is "
                 "plasterboard, and sodium chloride is on the table."},
    ],

    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Salt",
         "definition": "The compound made when an acid reacts with a base. "
                       "The metal names it and the acid gives it its ending."},
        {"term": "Excess",
         "definition": "More than enough. Adding an insoluble base in excess "
                       "guarantees no acid is left, and what is left over can "
                       "be filtered out."},
        {"term": "Insoluble",
         "definition": "Will not dissolve. An insoluble base sits on the "
                       "bottom of the beaker once the acid is used up, which "
                       "is how you know to stop."},
        {"term": "Filtrate",
         "definition": "The liquid that passes through the filter paper. Here "
                       "it is the salt solution, with the leftover solid left "
                       "behind."},
        {"term": "Crystallise",
         "definition": "To grow crystals out of a solution by concentrating "
                       "it and letting it cool slowly.",
         "note": "Boiling to dryness is not crystallising — it gives powder."},
        {"term": "Soluble",
         "definition": "Will dissolve. A soluble base cannot be added in "
                       "excess, because there would be no way to remove what "
                       "was left over."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚑ NEW PROSE. ⊖ No safeguarding block — lab safety. It adds the two things
    # the six steps assume rather than withdrawing any of them.
    "safety_note": "Copper compounds are harmful if swallowed and the warm "
                   "acid stage spits if it is allowed to boil. Eye protection "
                   "throughout, the crystals are never tasted, and the "
                   "evaporating basin is left to cool before it is handled.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why you add too much of the base on "
                      "purpose?",
              "cta": "Ask about this lesson",
              "anchor": "s-method"},

    "ks4_becomes": "Preparing soluble salts by titration, calculating "
                   "percentage yield, and predicting solubility from the "
                   "rules.",

    "ws": ["experimental-skills-and-investigations", "measurement"],

    "review_state": "draft",
}
