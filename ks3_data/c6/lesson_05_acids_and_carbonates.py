"""C6 L5 — Acids and carbonates (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-05-acids-and-carbonates.dc.html` (645 lines),
and her author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §2, §3, §4,
§5 flag 10, §6 (`ACID-08`) and §7.

── THE SLOT WAS RENAMED, NOT ADDED ─────────────────────────────────────

⊕ MRB-281, 23 Aug 2026. `structure.py`'s fifth C6 slot used to read
`acid-plus-alkali` / "Acid + alkali: making a salt". It had never been
authored and never could be: acid + alkali is owned twice over already, by
`neutralisation` (`CR.07a`, the equation and the curve) and by
`making-a-pure-dry-salt` (`CR.07b`, the preparation), so a third lesson under
that name would double-own `CR.07` and fail `validate()`'s rule 4. The slot
was a permanent coming-soon page with no legal way to fill it.

Design drew `c6-05-acids-and-carbonates` at that position instead and flagged
the divergence herself (NOTES-C6 §2, "Ruling wanted"). The first ruling left
the slot dead. **Mide overrode that on 23 Aug 2026 and this lesson is the
result.** The slot was RENAMED in place rather than an eighth tuple inserted,
so `making-a-pure-dry-salt` and `catalysts` do not move, no slug changes, no
URL changes, and the key stage stays at 185 slots.

── IT OWNS NO STATUTORY STATEMENT, AND SAYS SO THE LEGAL WAY ───────────

⚠️ **NOTHING IS MINTED FOR THIS LESSON AND NOTHING MAY BE.** C6 owns
`KS3.C.CR.04`–`CR.08`, and none of the five mentions carbonates, carbon
dioxide, or the reaction of an acid with either:

    CR.06  reactions of acids with metals to produce a salt plus hydrogen
    CR.07  reactions of acids with alkalis to produce a salt plus water

`CR.07a` / `CR.07b` are legitimate because they split `CR.07`'s OWN text
across two lessons that are both about acid + alkali. A `CR.06c` or `CR.07c`
here would be different in kind: acid + carbonate is chemically neither of its
parents, so the clause would misstate what the National Curriculum says. A
statutory id is permanent — `docs/ks3/statutory-register.md`: "an ID never
changes meaning ... a re-mint is a breaking change" — so a wrong mint is not
quietly fixable afterwards. Design's own §2 says it outright: "it owns no
statutory statement."

So this lesson takes §7.6's OTHER legal shape, all three legs:

    beyond_statutory: True     covers: []     ks4_links: non-empty

enforced by `build_ks3.validate()` rule 3 and reported by `verify_ks3.py`
§10.2. Nothing enters the coverage register and
`docs/ks3/statutory-register.md` gains no row.

⚑ **THIS REVIVES A PATTERN MIDE CLOSED ONCE BEFORE, AND THE TENSION IS
RECORDED RATHER THAN HIDDEN.** Under MRB-199 (12 Aug 2026) he ruled, as
examiner, that off-spec KS3 content should not live inside a statutory unit as
`beyond_statutory` — it should wait for the §7.6 Year 9 GCSE-bridge group —
and two B1 lessons were REMOVED rather than kept that way. `verify_ks3.py`
line 184 still gates that, scoped to B1. It does not bind on C6, so this is
legal; it is nevertheless the same shape he closed. It is used here because
the alternative is worse — a minted clause would be a false statement about
the National Curriculum, permanently — and because the product call to keep
the lesson in this unit is Mide's own and was made on 23 Aug 2026. The only
remaining job was to wire that decision up honestly, and this is the one
honest mechanism the codebase has for it.

── TWO NEW FAMILIES, AND WHY THE THIRD IS NOT NEW ──────────────────────

NOTES-C6 §4 names `step-rig` + `solid-sorter` for this page, and both are
registered here for the first time — `ks3_art/c6.py`, C6's own module, with
their own shell classes and their own prefixes. The comment in that file
saying they are deliberately unregistered is replaced: its premise was that
`structure.py` had no slot for this lesson, and that stopped being true above.

`#s-world` is NOT a third new family. Design's "three consequences" section is
a question, three options, one commitment and one answer — `acid-judgements`,
already placed on five C6 pages and drawn identically on all of them. This is
its sixth placement, and inventing a `uses-cards` family for the same markup
would be the drift MRB-279's gate exists to catch, one level up.

── WHAT MOVED FROM DESIGN'S DRAWING, AND WHY ───────────────────────────

⚑ **THE TWO LIVE COUNTS GO TO THE BLOCK HEAD.** Design draws `#s-rig`'s
"{n} of 5 revealed" as a mono line beside the reveal button, and folds
`#s-bench`'s count into the lead sentence ("N of 4 decided. Three of these
look almost identical..."). Both are the block head's `head_counter` here —
mono, uppercase, right-aligned on the eyebrow row, which is the same component
in Design's own treatment — and the sentence that FOLLOWS the count stays as
the block's prompt, because it is an argument about the bench rather than a
narration of the controls. Identical to what `acid-plus-metal` did with the
same shape.

⚑ **THE FOUR BENCH VERDICTS ARE AUTHORED, NOT COMPOSED.** Design builds each
from `row.isCarb ? 'It fizzes — this one is a carbonate.' : 'No fizzing. Not a
carbonate.'`, which makes the three positive verdicts literally one string and
puts a flag into a sentence by ternary. All four are authored, and
`r_solid_sorter` checks the rule the ternary encoded on every one of them —
see its docstring for the five content-truth assertions.

── SCIENCE FLAGS ───────────────────────────────────────────────────────

⚑ Flag 10 — limewater going clear again with excess carbon dioxide, step 5.
KEPT, and Design's own note says why: it is honest apparatus behaviour and
most textbooks omit it. MRB-225 is satisfied because the step does not retract
the test — it says when to READ it ("the test is the change to milky, so read
it when it happens rather than at the end"), which is the difference between
an honest instrument and a trick.

⚑ Sodium hydrogencarbonate, named in full on the bench and described as "a
carbonate with hydrogen in it". Design's own wording. It is the KS3 name and
it is what is on the tub in a kitchen; the hydrogencarbonate/carbonate
distinction is a GCSE one and the page does not open it.

⚑ Copper carbonate is green, and the bench says so in a section headed "four
white solids". That is deliberate and Design's: "The only one on the bench
that is not white — and it fizzes hard ... Carbonates are a family, not a
single substance." The heading is about what the student is looking at, and
the fourth bottle is the one that breaks the look-alike rule.

⚑ **NO SAFEGUARDING BLOCK.** ⊖ The gas test and the dilute acid are LAB
safety, which is what `safety_note` is for: eye protection, a boiling tube
rather than a test tube, a bung fitted at arm's length. A Childline-style line
belongs where a student's own body, health or risk is the subject, and nothing
on this page is. Same call as `acid-plus-metal`'s.

── MRB-177 · WHAT WAS RE-AUTHORED AT THE DISTRACTOR ────────────────────

⚠️ Rung 1's four options are Design's IDEAS at Design's lengths, but three of
them are re-authored. Her set ran the correct answer at six tokens against
three, three and three — strictly longest at 2.0x, which is a tell a student
can score on without reading. Under MRB-177 as ruled (17 Aug 2026) the fix is
at the DISTRACTOR, never at the correct option: each wrong option now states a
wrong three-product rule in the correct answer's own shape and at its own
length, and every one of Design's corrections still answers its own option.
The correct option is untouched.

Rung 2 measured clean and is Design's, verbatim. Both rungs' ANSWERS move —
index 2 and index 1 — because Design puts both at index 0 and MRB-278 gates
position across the unit. The option TEXT does not move with them.
"""

# ── the five steps of the limewater test (Design's `STEPS`) ─────────────
#
# Her order, which is the order of the method, and each `why` is a way the
# test is got wrong rather than a reason it is done. That is the whole lead:
# "Each step has a reason, and each reason is a way this test can be got
# wrong."
_STEPS = [
    {"id": "st1",
     "what": "Put the carbonate in a boiling tube and add the acid.",
     "why": "A boiling tube, not a test tube — the fizzing throws liquid up "
            "the sides, and a tube that is too small delivers acid spray to "
            "whoever is holding it."},
    {"id": "st2",
     "what": "Fit a bung with a delivery tube straight away.",
     "why": "Carbon dioxide is produced from the first second. Anything that "
            "escapes before the bung goes in is gas you cannot test, and the "
            "fastest fizzing happens at the start."},
    {"id": "st3",
     "what": "Run the delivery tube into a second tube of clear limewater.",
     "why": "The end of the tube must be under the surface of the limewater. "
            "Above it, the gas bubbles into the air and the limewater never "
            "meets it."},
    {"id": "st4",
     "what": "Watch the limewater, not the reaction.",
     "why": "The interesting tube is the second one. Clear limewater turning "
            "milky white is the positive result — a fine white solid forming "
            "in what was a clear liquid."},
    # ⚑ Flag 10. Kept whole. It does not retract the test; it says when to
    # read it.
    {"id": "st5",
     "what": "Keep bubbling and it goes clear again.",
     "why": "Not a mistake, and not a failed test. Excess carbon dioxide "
            "dissolves the white solid back into something colourless. The "
            "test is the change to milky, so read it when it happens rather "
            "than at the end."},
]

# ── the four white solids (Design's `BENCH`) ────────────────────────────
#
# ⚠️ `answer` IS EMITTED NOWHERE AND IS READ AT BUILD TIME, on every row. Only
# the ladder marks; the verdict is one authored sentence naming what the solid
# IS, the same sentence whichever button was pressed. `r_solid_sorter` walks
# all four and checks that the flag, the verdict and the equation agree — see
# its docstring.
#
# Table salt is the row that makes the bench a bench. Without a solid that
# does nothing there is no rule, only three examples, and "white powder" would
# be doing the identifying instead of the acid.
_SOLIDS = [
    {"id": "w1", "name": "Marble chips", "looks": "hard white lumps",
     "answer": "fizz",
     "verdict": "It fizzes — this one is a carbonate.",
     "why": "Calcium carbonate. Steady fizzing from every surface, and the "
            "limewater goes milky within seconds.",
     "eq_left": "hydrochloric acid + calcium carbonate",
     "eq_right": "calcium chloride + water + carbon dioxide"},
    {"id": "w2", "name": "Baking soda", "looks": "fine white powder",
     "answer": "fizz",
     "verdict": "It fizzes — this one is a carbonate.",
     "why": "Sodium hydrogencarbonate — a carbonate with hydrogen in it, and "
            "it behaves the same way. Violent fizzing because the powder has "
            "an enormous surface area.",
     "eq_left": "hydrochloric acid + sodium hydrogencarbonate",
     "eq_right": "sodium chloride + water + carbon dioxide"},
    {"id": "w3", "name": "Table salt", "looks": "white crystals",
     "answer": "no",
     "verdict": "No fizzing. Not a carbonate.",
     "why": "Sodium chloride. Nothing happens at all: it is already a salt, "
            "and there is no carbonate in it for the acid to break open. It "
            "just dissolves.",
     "eq_left": "", "eq_right": ""},
    {"id": "w4", "name": "Copper carbonate", "looks": "green powder",
     "answer": "fizz",
     "verdict": "It fizzes — this one is a carbonate.",
     "why": "The only one on the bench that is not white — and it fizzes "
            "hard, giving a blue-green solution of copper chloride. "
            "Carbonates are a family, not a single substance.",
     "eq_left": "hydrochloric acid + copper carbonate",
     "eq_right": "copper chloride + water + carbon dioxide"},
]

# ── the three consequences (Design's `USES`) ────────────────────────────
#
# `acid-judgements`' sixth placement. Design's questions, options and answer
# paragraphs, unchanged; `answer` names the option id and is checked at build
# time against the set, because only the ladder marks.
_USES = [
    {"id": "u1",
     "q": "Why do old gravestones made of limestone go unreadable while "
          "granite ones stay sharp?",
     "options": [{"id": "a", "label": "Limestone is softer"},
                 {"id": "b", "label": "Rain reacts with the carbonate in "
                                      "limestone"},
                 {"id": "c", "label": "Granite is polished"}],
     "answer": "b",
     "reply": "Because rain is slightly acidic and limestone is calcium "
              "carbonate, so the stone is slowly reacted away — letters "
              "first, since they are the thinnest part. Granite contains no "
              "carbonate, so the same rain runs off it and does nothing. "
              "Hardness is a side issue; this is a chemical difference, not a "
              "physical one."},
    {"id": "u2",
     "q": "A fizzy indigestion tablet contains a carbonate and a solid acid. "
          "Why does it only fizz when dropped in water?",
     "options": [{"id": "a", "label": "Water is an acid"},
                 {"id": "b", "label": "The two solids cannot react until they "
                                      "dissolve"},
                 {"id": "c", "label": "The water heats them up"}],
     "answer": "b",
     "reply": "Both ingredients sit dry in the tablet doing nothing, because "
              "their particles cannot move past each other. Water dissolves "
              "them, the particles mix, and the reaction starts — giving "
              "carbon dioxide, which is the fizz. The carbonate then goes on "
              "to neutralise the acid in the stomach."},
    {"id": "u3",
     "q": "A farmer wants to know whether a field of soil contains chalk. "
          "What is the two-minute test?",
     "options": [{"id": "a", "label": "Add acid and watch for fizzing"},
                 {"id": "b", "label": "Add water and see if it dissolves"},
                 {"id": "c", "label": "Weigh a sample before and after "
                                      "drying"}],
     "answer": "a",
     "reply": "Drip dilute acid on it. Fizzing means a carbonate is present, "
              "and in soil that means chalk or limestone. Collecting the gas "
              "and turning limewater milky would confirm it. Geologists carry "
              "a small bottle of acid in the field for exactly this."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches `ks3_data/structure.py`'s renamed fifth C6 tuple character for
    # character. Design's page title and the skeleton's now agree, which is
    # the first C6 lesson of which that is true.
    "slug":        "acids-and-carbonates",
    "title":       "Acids and carbonates",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # §7.6's declared exemption, all three legs. See the module docstring for
    # why a minted clause would have been a false statement rather than a
    # tidier answer.
    "covers":      [],
    "beyond_statutory": True,
    "ks4_links":   ["chemistry/chemical-changes/reactions-of-acids"],
    "touches":     [],
    "threads":     [{"id": "substances-and-reactions", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    # The third acid reaction family lands after the second. A student who has
    # not met `acid-plus-metal` has no set for this to complete and no reason
    # the gas being something other than hydrogen is a surprise.
    "requires":    ["acid-plus-metal"],
    "assumes":     [],
    "references":  [],
    "connects_heading": "Next in this unit",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A cathedral has stood for eight hundred years and the "
                    "faces on its statues have gone. Nobody touched them — "
                    "the rain did it, one reaction at a time.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Six stops, Design's `RAIL`, and `done_when` restates her own `DONE()`:
    # the hook on a commitment, the rig when all five steps are open, the
    # bench when all four solids are decided, the consequences when all three
    # are decided, `#s-think` on a commitment, the ladder when every rung is
    # answered. No stop mirrors another — every one of her six expressions is
    # different — so no `mirrors` key, which is what
    # `check_rail_matches_design` compares against.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Rock that fizzes", "done_when": "committed"},
        {"anchor": "s-rig",    "short": "RIG",
         "label": "The limewater test", "done_when": "all_five_revealed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Four white solids", "done_when": "all_four_decided"},
        {"anchor": "s-world",  "short": "USES",
         "label": "Three consequences", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "What a test proves", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK GIVES THE EVIDENCE AND DOES NOT NAME THE GAS. Both results
    # are in plain sight — the splint goes out, the limewater goes milky — and
    # the commitment is what they add up to. A student who reads "the splint
    # went out" as the identification is exactly the student `#s-think` is
    # waiting for, four sections later.
    "phenomenon": {
        "kind": "narrative",
        "title": "Drop a marble chip into acid and it fizzes like a tablet in "
                 "water. Marble is rock.",
        "prompt": "The chip shrinks and streams bubbles from every surface. "
                  "The gas is not hydrogen — a lit splint held to it goes out "
                  "instead of squeaking. Bubble the gas through clear "
                  "limewater and the limewater turns milky white.",
        "commit": "What is the gas?",
        # MRB-177: 7, 4, 8, 5 words. The correct option is index 2 and is
        # longest by one word at 1.14x — inside §13's bar in both directions.
        # Design's set, unchanged.
        "options": [
            "Hydrogen, the same as with a metal",
            "Oxygen from the acid",
            "Carbon dioxide, which came out of the rock",
            "Steam from the warm tube",
        ],
        "reveal": "Carbon dioxide. Turning limewater milky is the test for "
                  "it, and nothing else you will meet does that. Marble is "
                  "calcium <strong>carbonate</strong> — the carbon and the "
                  "oxygen were locked into the rock, and the acid has taken "
                  "them out and let them go as gas. Chalk, limestone and "
                  "eggshell are the same compound and all do the same thing.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # `ACID-08` was minted by Design in NOTES-C6 §6 and has sat unused since
    # 21 Aug, deliberately, because the lesson that elicits it was not built.
    # It is built now and the id means exactly what she said it means.
    #
    # ⊖ `think-reveal-specificity` cannot be emitted from a lane — the
    # `#s-think` reveal panel is drawn by the shared `r_activity` with no id —
    # so both joins name the activity that holds the commitment AND the two
    # confronting paragraphs. Same repair as `ACID-01`, `03`, `05`, `07`,
    # `09` and `10`.
    "misconceptions": [
        {"id": "ACID-08",
         "statement": "A gas that puts out a splint is carbon dioxide.",
         "elicited_by": "think-commit-splint",
         "confronted_by": "think-commit-splint"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>carbonate</strong> is any compound containing a "
                 "carbonate group — calcium carbonate, sodium carbonate, "
                 "copper carbonate. Every one of them reacts with acid the "
                 "same way, and there are three products, not two."},

        # ⭐ THE WORD EQUATION, DRAWN. Design's line ends in a colon and runs
        # straight into the equation; the rule panel intervenes here, as it
        # does on `acid-plus-metal` for the same reason, so the colon becomes
        # a full stop. No triangle and no part-whole bar: MRB-204 as amended
        # gives the triangle to `A = B x C` and the bar to a sum, and a word
        # equation is neither.
        {"type": "rule", "id": "salt-water-and-gas",
         "eyebrow": "The rule",
         "statement": "An acid and a carbonate always make the same three "
                      "things.",
         "equation": {"reactants": "acid + carbonate",
                      "arrow": "makes",
                      "products": "salt + water + carbon dioxide",
                      # Commentary on the equation, not a condition on the
                      # arrow — the b8-01 shape, and the same slot
                      # `acid-plus-metal` uses to say where the hydrogen came
                      # from. This is the sentence a student needs while they
                      # are writing the products out.
                      "condition": "the carbon dioxide comes out of the "
                                   "carbonate, not the acid"},
         "close": "The carbon dioxide is the giveaway. It is the fizz, and it "
                  "is what limewater detects."},

        # #s-rig — five steps, revealed one at a time. Light `ks3-block` →
        # `check`.
        #
        # ⚠️ THE LEAD IS NOT A NARRATION OF THE CONTROL. "Reveal them one at a
        # time" is Design's own sentence and it is the third clause of an
        # argument — each step has a reason, and each reason is a way the test
        # is got wrong. Cutting it would leave the block with no reason to be
        # staged at all.
        {"type": "step-rig", "id": "rig-limewater", "anchor": "s-rig",
         "eyebrow": "Watched first · five steps",
         "heading": "The limewater test",
         "prompt": "Each step has a reason, and each reason is a way this "
                   "test can be got wrong. Reveal them one at a time.",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} revealed", "start": 0},
         "steps": _STEPS,
         # Design's three button labels, emitted together and shown one at a
         # time. `all` is the disabled resting state at the end.
         "labels": {"first": "Reveal the first step",
                    "next": "Reveal the next step",
                    "all": "All five shown"}},

        # #s-bench — the flagship. Light `ks3-block` → `check`.
        {"type": "solid-sorter", "id": "bench-four-solids", "anchor": "s-bench",
         "eyebrow": "Your turn · four white solids",
         "heading": "Which of these are carbonates? Only the acid can tell "
                    "you.",
         "prompt": "Three of these look almost identical in the bottle, which "
                   "is the point.",
         "demand": "investigate",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         # ⚠️ `reacts` NAMES WHICH BUTTON IS THE REACTING ONE, and it is read
         # at build time only. Without it the renderer cannot tell an
         # equation that is missing from one that is correctly absent, and
         # "carbonates fizz" would be a claim nothing checks.
         "options": [{"id": "fizz", "label": "It will fizz", "reacts": True},
                     {"id": "no", "label": "No reaction"}],
         "solids": _SOLIDS},

        {"type": "key-fact", "ref": "limewater-is-the-test"},

        # #s-world — `acid-judgements`, sixth placement. Light `ks3-block` →
        # `check`.
        {"type": "acid-judgements", "id": "uses-three", "anchor": "s-world",
         "eyebrow": "Three consequences",
         "heading": "One reaction, three places it decides the outcome",
         "prompt": "Commit to each before reading. None of the three is about "
                   "a laboratory.",
         "demand": "explain",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "items": _USES},

        {"type": "misconception", "id": "think-commit-splint",
         "anchor": "s-think", "targets": "ACID-08"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None, and Design draws none. The rig is five sentences a student reveals
    # rather than an apparatus diagram, on purpose: a drawing of a boiling
    # tube with a delivery tube in it shows the arrangement and hides every
    # reason the arrangement is that way, which is the whole content of the
    # section.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # ⚑ "makes" rather than a typed arrow — Design's own 21 Aug font-law pass.
    "key_facts": [
        {"id": "limewater-is-the-test",
         "text": "acid + carbonate makes salt + water + carbon dioxide. "
                 "Limewater turning milky is the test for that gas — and "
                 "nothing else turns it milky.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-splint",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-08",
         "prompt": "The splint did go out. Commit before you read on.",
         # MRB-177: 12, 13, 8, 9 words. The correct option is index 1 and is
         # longest by one word at 1.08x. Design's set, unchanged.
         "options": [
             "Right — putting a splint out is the test for carbon dioxide",
             "Wrong — most gases put a splint out; only limewater identifies "
             "carbon dioxide",
             "Right, because carbon dioxide is heavier than air",
             "Wrong — carbon dioxide makes a splint burn brighter",
         ],
         "reveal": [
             "Almost every gas puts a splint out. Nitrogen does, argon does, "
             "and so does a tube of nothing much at all — a flame needs "
             "oxygen, and anything that is not oxygen will smother it. “The "
             "splint went out” narrows the answer to <em>not oxygen</em>, "
             "which is barely a clue.",
             "Limewater is different: it goes milky for carbon dioxide and "
             "for nothing else on your bench. <strong>A good test has one "
             "answer. A test that dozens of substances could pass is not "
             "evidence.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 6 tokens against 3, 3 and 3:
        # strictly longest at 2.0x, which a student can score on by picking
        # the long one. Each distractor now states a WRONG THREE-PRODUCT RULE
        # in the correct answer's own shape and at its own length — 6, 5, 5
        # against 6 — and every one of Design's corrections still answers its
        # own option. The answer moves to index 2 (MRB-278).
        "recall": {
            "q": "Complete: acid + carbonate makes what?",
            "options": [
                "salt + hydrogen + carbon dioxide",
                "salt + water + hydrogen",
                "salt + water + carbon dioxide",
                "carbon dioxide + water only",
            ],
            "answer": 2,
            "feedback": {
                0: "Hydrogen is what a metal gives with an acid. A carbonate "
                   "gives carbon dioxide, and water as well — and no hydrogen "
                   "at all.",
                1: "That pair is what an acid gives with a metal. The "
                   "carbonate brings carbon and oxygen with it, and they "
                   "leave as carbon dioxide.",
                3: "The metal from the carbonate has to end up somewhere — it "
                   "becomes the salt, dissolved in the water that is also "
                   "formed.",
            }},
        # Design's set, verbatim: 6 tokens against 5, 4 and 4, so the correct
        # answer is longest by one and at 1.2x — inside §13's bar. The answer
        # moves to index 1 (MRB-278); the option text does not move with it.
        "apply": {
            "q": "A gas is bubbled through limewater and the limewater stays "
                 "clear. What can you conclude?",
            "options": [
                "The gas is hydrogen",
                "The gas is not carbon dioxide",
                "The limewater has gone off",
                "No gas was produced",
            ],
            "answer": 1,
            "feedback": {
                0: "It rules carbon dioxide out but does not identify what it "
                   "is. Hydrogen would need its own test.",
                2: "Possible in principle, but the honest conclusion from a "
                   "clear result is that the gas is not carbon dioxide.",
                3: "Gas was bubbled through. A negative result is a result "
                   "about the gas, not about whether there was one.",
            }},
        "explain": {
            "q": "Marble chips are dropped into dilute hydrochloric acid. "
                 "Describe what you would see, name all three products, and "
                 "explain how you would prove the gas is carbon dioxide.",
            "field_label": "Your explanation",
            "placeholder": "The chips…",
            "success": [
                "Says the chips fizz and get smaller.",
                "Names the products as calcium chloride, water and carbon "
                "dioxide.",
                "Says the gas is collected through a delivery tube into "
                "limewater.",
                "Says limewater turning milky shows carbon dioxide.",
                "Says the delivery tube must be below the surface of the "
                "limewater.",
            ]},
        "produce": {
            "q": "Two white powders are on the bench: one is a carbonate and "
                 "one is not, and you may not taste or touch either. Design a "
                 "test that would tell them apart, and explain what result "
                 "would settle it.",
            "field_label": "Your plan",
            "placeholder": "I would add dilute acid to a small sample of…",
            "success": [
                "Adds dilute acid to a small sample of each powder.",
                "Uses the same amount of the same acid for both.",
                "Says the carbonate fizzes and the other does not.",
                "Collects the gas and tests it with limewater to confirm.",
                "Says limewater turning milky proves the fizzing was carbon "
                "dioxide.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Acids react with carbonates to give a salt, water and carbon "
                "dioxide. The fizzing is the carbon dioxide leaving, and it "
                "is identified by bubbling it through limewater, which turns "
                "milky. Calcium carbonate is chalk, limestone and marble — "
                "which is why acid rain damages buildings and statues made of "
                "them.",

    # ── the stretch layer (§5.6) ────────────────────────────────────────────
    "stretch": [
        {"type": "explainer", "id": "limestone-landscapes",
         "text": "Whole landscapes are made by this reaction. Rain is "
                 "slightly acidic before it picks up any pollution at all, "
                 "and where it falls on limestone it dissolves it — slowly, "
                 "along cracks, for thousands of years. The result is "
                 "limestone pavement above ground and cave systems below it, "
                 "and every stalactite is the same reaction running backwards "
                 "as the water dries and leaves the calcium carbonate "
                 "behind."},
        {"type": "explainer", "id": "the-same-chemistry-in-the-ocean",
         "text": "The same chemistry sits in the ocean. Carbon dioxide "
                 "dissolving into seawater makes it very slightly more "
                 "acidic, and shells and coral skeletons are calcium "
                 "carbonate. A change of a few tenths of a pH unit across an "
                 "ocean is not a laboratory abstraction — it is the "
                 "difference between a shell that thickens and one that "
                 "thins."},
    ],

    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Carbonate",
         "definition": "Any compound containing a carbonate group. Every one "
                       "of them reacts with an acid to give a salt, water and "
                       "carbon dioxide."},
        {"term": "Limewater",
         "definition": "A clear solution used to test for carbon dioxide. It "
                       "turns milky white when the gas is bubbled through it, "
                       "and nothing else on a school bench does that.",
         "note": "Keep bubbling past the milky stage and it clears again. "
                 "The change to milky is the result, not the end state."},
        {"term": "Calcium carbonate",
         "definition": "The compound that chalk, limestone and marble are all "
                       "made of. It is why acid rain damages statues and why "
                       "a drop of acid on soil tells a farmer there is chalk "
                       "in it."},
        {"term": "Delivery tube",
         "definition": "The tube that carries gas from the reaction to "
                       "wherever it is being tested. Its far end goes under "
                       "the surface of the liquid, or the gas escapes into "
                       "the air instead."},
        {"term": "Specific test",
         "definition": "A test only one substance can pass. A splint going "
                       "out is not one — most gases do that — and limewater "
                       "going milky is."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚑ NEW PROSE. ⊖ No safeguarding block — lab safety, and nothing on this
    # page is about a student's own body or health. It names the two real
    # hazards the rig has and does not retract the method: the page is about
    # collecting and testing a gas, and this says how it is done safely.
    "safety_note": "Eye protection throughout. Dilute acid on a carbonate "
                   "fizzes hard enough to throw liquid up the tube, which is "
                   "why the reaction goes in a boiling tube rather than a "
                   "test tube and why the bung is fitted from the side rather "
                   "than over the mouth. Limewater is an alkali: wash it off "
                   "skin, and off the bench.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why limewater goes cloudy?",
              "cta": "Ask about this lesson",
              "anchor": "s-rig"},

    "ks4_becomes": "Testing for carbonates and gases as part of qualitative "
                   "analysis, and the thermal decomposition of carbonates in "
                   "the lime kiln.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    "review_state": "draft",
}
