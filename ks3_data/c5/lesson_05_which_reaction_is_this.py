"""C5 L5 — Which reaction is this? (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c5/c5-05-which-reaction-is-this.dc.html`
(608 lines), and her author's notes `docs/ks3/design-reference/c5/NOTES-C5.md`
§1, §2, §4 flags 15/16/18, §5 (`REACT-18`) and §6.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`TYPES`, `ITEMS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook's headline, prompt, commit and reveal, the two explainer paragraphs,
the decision-rule block's eyebrow / heading / four numbered rules / mass
close, the sorter's eyebrow / heading / tally / lede / close, the key fact,
`#s-rule`'s heading, lede, field label, placeholder, button and four model
rules, the `#s-think` options and its two reveal paragraphs, the key note and
both "Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup, which is where most of this lesson's words live and where a lift of
the top-level constants alone silently loses them.

── THIS LESSON IS THE UNIT'S ASSESSMENT IN DISGUISE ──────────────────────

NOTES-C5 §2: four PROCESS lessons teach the four types one at a time, and
"naming four types is not the same as telling them apart". So the flagship is
eight reactions at rising stakes with the SAME five buttons under every one —
the discrimination is the whole task, and a student who has to choose between
five names eight times is doing what an exam asks and what four separate
lessons never can.

⚠️ NOTHING IN THE INSTRUMENT MARKS. `type` is in `_REACTIONS` below because
it is the authored classification of each reaction, and it is emitted
NOWHERE — no `data-correct`, no green, no red. The reveal panel says in words
what the answer is whichever button was pressed, and only the mastery ladder
marks correctness. What `type` is FOR is two build-time assertions in
`r_type_sorter`, and they are the chemistry's guard rather than a mark:

  1. Every one of the five buttons is the answer to at least one reaction.
     A fifth button nothing ever justifies is a button that reads as a trick.
  2. Every reaction's `answer` line OPENS with the label of the button that
     answers it. The flag is what the author meant; the answer line is what
     the student reads, and when the two disagree the page tells a student
     they were wrong when they were right.

── THE CURRICULUM POSITION, and why clause `e` exists ────────────────────

⚖️ `KS3.C.CR.03e` IS A COMMANDER'S RULING (MRB-246) and it is the one clause
in `ks3_data/substatements.py` that is not a phrase of its own bullet. CR.03
names four reaction types; this lesson teaches the bullet as a SET rather
than any member of it. The full reasoning is at `KS3.C.CR.03` in that file
and it rejects all three alternatives: owning the parent alongside a–d is
forbidden by `validate()` rule 5, sharing one of a–d is forbidden by rule 4,
and `beyond_statutory` is simply false — telling the four apart is what the
bullet demands and what an exam asks.

⚠️ CLAUSE `e` IS NOT A FIFTH REACTION TYPE and must never be read or written
as one. There are four types. The clause is the bullet's integrative demand.

⚑ For Mide's science gate — the NOTES §4 flags this page carries:

  * flag 18 — ITEM 8 ANSWERS "NONE OF THE FOUR". RULED KEEP (commander), and
    it is the honest payoff of the `covers` clause above: the lesson is about
    the SET, and a set has edges. Marble in acid is a neutralisation — two
    reactants, neither of them oxygen, no metal displacing another — so none
    of the four names fits, and a classification question whose honest answer
    is that the classification does not cover it is exactly what a real
    scientist meets.

    ⚑ THE ANSWER LINE AND THE REVEAL ARE STRENGTHENED, and that is the one
    condition the ruling came with. Design's answer line was "None of the
    four." alone, which a teacher skim-reading the answers could read as a
    slip. It now says in its own words that it is the correct answer, and the
    reveal says in plain words that this is not a gap in what the student
    knows and not a trick: the four are a useful set, not a complete one, and
    this reaction has its own name. Design's sentences are otherwise intact.

  * flag 15 — RESPIRATION AS AN OXIDATION (item 7). CONFIRMED CORRECT and
    KEPT byte-identical, including the deliberate biology cross-link: the
    same reactants and the same products as burning glucose, at 37 °C and
    with no flame.

  * flag 16 — THERMITE AT "around 2500 °C" (item 6). CONFIRMED and KEPT.
    Design's item says "It reaches 2500 °C", which is the figure the flag
    quotes.

  * flag 8, restated here — LIMESTONE IN A KILN AT 900 °C (item 5).
    Consistent with `c5-02`'s own figure and correct: calcium carbonate
    decomposes at around that temperature industrially, and the white solid
    left is calcium oxide, which does hiss when water is dropped on it.

⚑ And one correction of the author's own, under the contract's §18:

  * ITEM 4 SAID RUSTING IS "the same reaction as burning", one sentence after
    saying rusting needs water as well. Burning iron and rusting iron are both
    OXIDATIONS of iron and they are not the same reaction: they make different
    oxides and only one of them needs water, which the same `why` had just
    said. That is a lesson body retracted by its own next clause (MRB-225), on
    the item whose job is to separate oxidation from combustion. RE-AUTHORED
    to claim the thing that is true — the same GAIN OF OXYGEN — and the
    teaching it carries (oxidation is the general case, combustion is the fast
    one) is unchanged. `h04`'s distractor in the questions file corrects the
    same wrong idea from the other side.

⚑ And two distractor sets re-authored under MRB-177, both AT THE DISTRACTOR:

  * THE HOOK ran 4, 9, 5 and 5 words with the CORRECT one longest by four —
    the gate's exact threshold, on the set that opens the lesson. It carries
    no `answer` so the gate skips it, which makes it worse rather than safer:
    this is the commitment `#s-think` and the whole sorter are built on, and a
    visibly-longest right answer means the student never commits to a wrong
    sorting rule at all. Index 1 is Design's, unchanged and still index 1; the
    three distractors are re-authored as the three WRONG sorting rules this
    lesson exists to break — sort by colour, sort by heat, sort by the gas —
    each in the correct option's own two-part shape.
  * RUNG 1 AND RUNG 2 both failed measurably. See the `ladder` comments.

⚠️ `#s-think`'s four options were MEASURED AND LEFT ALONE: 8 / 13 / 10 / 9
words with the correct one at 13 against a longest distractor of 10 — inside
both thresholds (gap 3, ratio 1.3). Design's set, unchanged.
"""

# ── the five buttons under every reaction (Design's `TYPES`) ────────────
#
# ⚠️ ONE OPTION LIST FOR ALL EIGHT, and that is the instrument's argument.
# The fifth button is on screen from the first reaction, not produced at the
# eighth: a student who meets "None of the four" only when it is the answer
# has been told the answer by the interface. It is offered eight times and is
# right once.
_TYPES = [
    {"id": "comb",   "label": "Combustion"},
    {"id": "decomp", "label": "Thermal decomposition"},
    {"id": "ox",     "label": "Oxidation"},
    {"id": "disp",   "label": "Displacement"},
    {"id": "none",   "label": "None of the four"},
]

# ── the eight reactions (Design's `ITEMS`) ──────────────────────────────
#
# `level` is Design's own difficulty tag and is rendered as the card's mono
# accent eyebrow. `type` is the authored classification and is emitted
# NOWHERE — see the module docstring for the two assertions it guards.
#
# ⚠️ THE ORDER IS THE RISING STAKES AND IS NEVER SORTED OR FILTERED. Four
# straightforward, three harder, one that is not any of the four; the lede
# above them promises exactly that and the promise is checked against the
# cards rather than trusted.
_REACTIONS = [
    {"id": "i1", "type": "comb", "level": "Straightforward",
     "text": "Methane burns on a hob with a blue flame, making carbon dioxide "
             "and water.",
     "answer": "Combustion.",
     "why": "A fuel and oxygen, a flame, energy out. It is also an oxidation "
            "— combustion is the specific name and the better answer."},
    {"id": "i2", "type": "decomp", "level": "Straightforward",
     "text": "Green copper carbonate is heated in a test tube and turns black, "
             "giving off a gas that turns limewater milky.",
     "answer": "Thermal decomposition.",
     "why": "One reactant, two products, heat needed continuously, and the "
            "mass in the tube falls. Nothing else in the unit has one "
            "reactant."},
    {"id": "i3", "type": "disp", "level": "Straightforward",
     "text": "A strip of zinc is dropped into blue copper sulfate solution. "
             "The blue fades and a brown solid collects on the zinc.",
     "answer": "Displacement.",
     "why": "A metal and a compound of a less reactive metal. Zinc is above "
            "copper, so it takes its place, and the copper appears as a "
            "solid."},
    # ⚑ RE-AUTHORED LAST CLAUSE, and only the last. Design's read "the same
    # reaction as burning, running slowly enough to take a decade" — one
    # sentence after "with water needed as well", which burning iron does not
    # need. Burning iron and rusting iron are both oxidations of iron and are
    # not the same reaction: different oxide, and only one of them needs
    # water. The clause now claims the gain of oxygen, which is the thing the
    # two really share and the thing this item is here to teach.
    {"id": "i4", "type": "ox", "level": "Straightforward",
     "text": "An iron gate left outdoors for ten years is covered in orange "
             "flakes and is heavier than when it was new.",
     "answer": "Oxidation.",
     "why": "Iron gaining oxygen, with water needed as well. No flame, so not "
            "combustion — the same gain of oxygen that burning makes in "
            "seconds, running slowly enough to take a decade."},
    {"id": "i5", "type": "decomp", "level": "Harder",
     "text": "Limestone is heated in a kiln at 900 °C. Carbon dioxide comes "
             "off and a white solid is left that hisses when water is dropped "
             "on it.",
     "answer": "Thermal decomposition.",
     "why": "No colour change to help you, and nothing burnt: one reactant "
            "broken apart by heat. The hissing white solid is calcium oxide, "
            "a new substance."},
    {"id": "i6", "type": "disp", "level": "Harder",
     "text": "Aluminium powder mixed with iron oxide is lit. It reaches "
             "2500 °C and molten iron pours out.",
     "answer": "Displacement.",
     "why": "Spectacular, and still a displacement: aluminium is more "
            "reactive than iron, so it takes the oxygen and the iron is "
            "pushed out. The drama is not the diagnosis — the reactants are."},
    # ⚑ NOTES §4 flag 15. Confirmed and kept whole: the biology cross-link is
    # deliberate, and the sentence that carries it is the one that makes the
    # point — same reactants, same products, no flame.
    {"id": "i7", "type": "ox", "level": "Harder",
     "text": "Glucose reacts with oxygen inside your cells, releasing energy "
             "and producing carbon dioxide and water.",
     "answer": "Oxidation.",
     "why": "The same reactants and products as burning glucose, at 37 °C and "
            "with no flame. Respiration is an oxidation, and biology gives it "
            "its own name for its own reasons."},
    # ⚑ NOTES §4 flag 18, RULED KEEP. The answer line and the first half of
    # the reveal are strengthened so a teacher reading only the answer cannot
    # misread it; every sentence of Design's after that is intact. See the
    # module docstring.
    {"id": "i8", "type": "none", "level": "Awkward on purpose",
     "text": "Marble chips are dropped into hydrochloric acid. The mixture "
             "fizzes and a gas comes off that turns limewater milky.",
     "answer": "None of the four. That is the correct answer, not a gap in "
               "what you know.",
     "why": "Two reactants, neither of them oxygen, and no metal displacing "
            "another — so none of the four names fits, and there was nothing "
            "you were meant to spot. The four are a useful set, not a "
            "complete one. This reaction has a name of its own: it is "
            "<strong>neutralisation</strong>, an acid reacting with a "
            "carbonate, and it is the whole of the next unit. Knowing that a "
            "case falls outside your rule is worth as much as knowing the "
            "rule."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 220 character for character.
    "slug":        "which-reaction-is-this",
    "title":       "Which reaction is this?",
    "discipline":  "chemistry",
    "unit":        "types-of-reaction",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚖️ `KS3.C.CR.03e` — the commander's ruling, minted in
    # `ks3_data/substatements.py` with the full reasoning. CR.03 names four
    # reaction types in one bullet and C5 gives each a lesson; clause `e` is
    # the bullet's integrative demand — telling the four apart, including
    # where more than one name is right and where none of the four applies.
    # It is NOT a fifth reaction type and there is no fifth type.
    #
    # The three alternatives were all worse and are rejected in that file:
    # owning the parent alongside a–d breaks `validate()` rule 5, sharing one
    # of a–d breaks rule 4, and `beyond_statutory` is false because telling
    # the four apart is what the bullet actually demands.
    "covers":      ["KS3.C.CR.03e"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 4},
                    {"id": "particles", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to `c5-04`, and the lesson
    # cannot be attempted without all four types having been met — but
    # displacement is the one that came immediately before and the one the
    # graph is built on.
    #
    # ⚠️ THE FORWARD REFERENCE CROSSES A UNIT BOUNDARY, so it takes the DICT
    # form: §4.6 makes the bare string mean "a lesson in this unit", and
    # `acids-and-alkalis` is C6's. NOTES §6 flags it as the only
    # forward-dangling link in C3, C4 or C5 and asks for a coming-soon row
    # rather than a dead link; that is what an unauthored target renders as
    # (`<span class="ks3-pending">`), so nothing here has to special-case it.
    "requires":    ["displacement"],
    "assumes":     ["combustion", "thermal-decomposition", "oxidation"],
    "references":  [{"unit": "C6", "lesson": "acids-and-alkalis"}],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    # Byte-identical. Its second half is the promise item 8 keeps, and it is
    # the reason the big question is not simply "which of the four is it?".
    "big_question": "Four types, and nobody labels them for you. What do you "
                    "look at first — and what do you do with a reaction that "
                    "fits none of them?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, in her order with her ids and her short
    # labels. `done_when` restates her own `DONE()`: the hook on a commitment,
    # the sorter when all eight are named, `#s-rule` when the comparison
    # version has been opened, `#s-think` on a commitment, the ladder when
    # every rung is answered and both self-marked rungs checked.
    #
    # ⚠️ THE DECISION-RULE BLOCK GETS NO STOP. Design draws it with no `id`
    # and it is not in her `RAIL` — it is a reference block, like `c5-04`'s
    # `s-series` and `c5-01`'s fire triangle. The rail ticks activities only,
    # and a stop that could never tick is not added (MRB-249).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Four types", "done_when": "committed"},
        {"anchor": "s-sort",   "short": "SORT",
         "label": "Name eight", "done_when": "all_eight_named"},
        {"anchor": "s-rule",   "short": "RULE",
         "label": "In your words", "done_when": "comparison_shown"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Overlapping names", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
    # OPTION IS UNTOUCHED AND UNMOVED. Design's set ran 4, 9, 5 and 5 words
    # with the correct one longest by exactly the gate's four. It carries no
    # `answer`, so the gate skips it — which is why it mattered more, not
    # less: this is the commitment the whole lesson argues with, and a
    # visibly-longest right answer means no student ever commits to a wrong
    # sorting rule for `#s-think` and the sorter to break.
    #
    # Each distractor is now a WRONG SORTING RULE in the correct option's own
    # two-part shape — the three the lesson names as the drama rather than the
    # diagnosis. Measured: 10 / 9 / 8 / 8 words, correct not longest.
    "phenomenon": {
        "kind": "narrative",
        "title": "Four reaction types. One of them gets heavier, one gets "
                 "lighter, one glows and one changes colour in a beaker.",
        "prompt": "You have met combustion, thermal decomposition, oxidation "
                  "and displacement. In an exam nobody tells you which one "
                  "you are looking at — you are given what happened and "
                  "expected to name it.",
        "commit": "Which single question sorts them fastest?",
        "options": [
            "What the colour change was, and how fast it happened",
            "How many reactants there are, and what they are",
            "Whether it gave out heat, and how much",
            "Whether a gas was produced, and which gas",
        ],
        "reveal": "How many reactants there are, and what they are. "
                  "<strong>One reactant</strong> means decomposition — "
                  "nothing else does that. <strong>Two, one of which is "
                  "oxygen</strong> means oxidation, and combustion if it "
                  "burns. <strong>A metal and a compound of another "
                  "metal</strong> means displacement. Count first, name "
                  "second.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS RESOLVE AGAINST THIS PAGE'S OWN MARKUP (MRB-244/248), and
    # the universe of legal names is exactly `id="…"` and `data-activity="…"`.
    # `think-commit-one-box` is emitted as this page's `data-activity` on the
    # `#s-think` section, and it is the id both joins name.
    #
    # ⊖ NOTES §5 proposes `think-reveal-subset` as the confrontation site. NO
    # SUCH ID CAN BE EMITTED FROM A LANE, and the register says so under
    # `REACT` in as many words: `build_ks3.py`'s shared `r_activity` emits the
    # confrontation reveal as `<div class="ks3-reveal" hidden data-reveal>`
    # with no `id`, and `build_ks3.py` is not a file this lane may touch. The
    # two confronting paragraphs are INSIDE the activity that also owns the
    # commitment, so the join names THE ACTIVITY — c4-01's form for `REACT-01`
    # and c3-03's for `MIX-06`, and it is also what satisfies Law 3, which
    # wants a `confronted_by` that is a real activity id.
    #
    # `statement` is the line the PAGE quotes, not the register's shorter
    # handle — `r_confrontation` prints `statement` as the `#s-think` quote,
    # and Design's line is the one that must render.
    #
    # ⚖️ REACT-18 STAYS A `REACT` ID. Design flagged it as NOS-shaped rather
    # than a factual error and asked for the `NOS` call before C8; the
    # commander ruled that whether `NOS` absorbs entries out of content
    # families is a register-taxonomy decision that changes permanent ids
    # across many units, and doing it one entry at a time in the middle of a
    # content unit is how a taxonomy fragments. Nothing about this lesson
    # changes either way.
    "misconceptions": [
        {"id": "REACT-18",
         "statement": "A reaction can only be one of the four types, so if it "
                      "is oxidation it cannot be combustion.",
         "elicited_by": "think-commit-one-box",
         "confronted_by": "think-commit-one-box"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 105–108 — two paragraphs, so two blocks: `r_explainer`
        # draws one <p>. The second is the one that does the work.
        {"type": "explainer",
         "text": "The four types are not four unrelated facts. Combustion is "
                 "a special case of oxidation — the fast, flaming kind. "
                 "Decomposition is the only one that runs a compound "
                 "backwards. Displacement is the only one where a metal has a "
                 "rival."},
        {"type": "explainer",
         "text": "So the useful test is structural, not visual. Look at the "
                 "equation, not the drama."},

        # Page lines 110–120 — the reference block, and the CLASSIFY family's
        # own spine step: the rule, stated before the student has to apply it.
        # A `rule` block rather than four explainers, because the four
        # questions are ASKED IN ORDER and rule 4 refers to "the answer to 3"
        # by number — the badges are what make that sentence true.
        #
        # ⚠️ NO ANCHOR AND NO RAIL STOP. Design gives this section no `id` and
        # it is not in her `RAIL`. It is read, not done.
        {"type": "rule",
         "eyebrow": "Reference · the decision rule",
         "statement": "Four questions, in this order",
         "cards": [
             {"num": 1,
              "term": "Is there only one reactant?",
              "gloss": "Then it is <strong>thermal decomposition</strong>, if "
                       "heat did it."},
             {"num": 2,
              "term": "Is one reactant a metal and the other a compound "
                      "containing a different metal?",
              "gloss": "Then it is <strong>displacement</strong>."},
             {"num": 3,
              "term": "Is one reactant oxygen, and did it burn with a flame?",
              "gloss": "Then it is <strong>combustion</strong>."},
             {"num": 4,
              "term": "Is one reactant oxygen, with no flame?",
              "gloss": "Then it is <strong>oxidation</strong> — and note that "
                       "the answer to 3 is also oxidation, just a more "
                       "specific name for it."},
         ],
         "close": "Mass is the tie-breaker when you are unsure. Gaining "
                  "oxygen makes the product heavier. Losing a gas makes what "
                  "is left lighter. Both of those are measurable, and neither "
                  "depends on what the reaction looked like."},

        # #s-sort — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ `reactions`, NOT `items`. The MRB-177 gate walks `activity.items`
        # as VERDICT CARDS — per-card options with a per-card answer — and
        # this instrument has neither: one shared five-way list stands under
        # all eight, and `answer` is a sentence rather than an option. Under
        # the key `items` the gate would resolve reaction 8's answer against
        # the shared list and measure "None of the four" (4 words) against
        # four one- and two-word type names, reporting a length tell that does
        # not exist — the same five buttons are on screen under every reaction
        # and a student picking the longest gets one of eight. The key names
        # what these are.
        {"type": "type-sorter", "id": "eight-reactions", "anchor": "s-sort",
         "eyebrow": "Your turn · eight reactions, rising difficulty",
         "heading": "Name the type. Commit before you read the answer.",
         "head_counter": {"format": "{n} of {total} named", "total": 8,
                          "tone": "accent"},
         "demand": "classify",
         "prompt": "The last three are deliberately awkward. Two of them have "
                   "a defensible second answer, and the eighth is not any of "
                   "the four.",
         # The card's mono eyebrow. `{n}` is the reaction's position, 1-based.
         "reaction_label": "Reaction {n}",
         "options": _TYPES,
         "reactions": _REACTIONS,
         "close": "Eight named. Notice how little the appearance helped: two "
                  "of the eight involved no visible drama at all, and two of "
                  "the most dramatic were the easiest to mislabel. Every one "
                  "of them was settled by counting reactants and looking for "
                  "oxygen or a metal."},

        {"type": "key-fact", "ref": "name-it-from-the-reactants"},

        # #s-rule — the CLASSIFY family's "state the rule in your own words"
        # step, and the one activity on the page that nothing marks. Light
        # `ks3-block` → `check`.
        {"type": "rule-write", "id": "own-rule", "anchor": "s-rule",
         "eyebrow": "In your words",
         "heading": "Write the rule you would give someone who missed this "
                    "unit",
         "demand": "construct",
         "prompt": "One sentence per type, and each one has to say what you "
                   "would <em>look at</em> rather than what it looks like. "
                   "Nobody marks this. Compare it with the version underneath "
                   "when you are done.",
         "field_label": "Your four rules",
         "placeholder": "Thermal decomposition: look for…",
         "button": "Show a version to compare with",
         # Design's four model rules, one per type, in her order — which is
         # not the decision rule's order, and is not sorted to match it: this
         # is a comparison for a student who has already written four of their
         # own, and the order they wrote them in is their own.
         "model": [
             "<strong>Thermal decomposition:</strong> one reactant, two or "
             "more products, heat needed all the way through, mass left "
             "behind goes down.",
             "<strong>Combustion:</strong> a fuel and oxygen, a flame, energy "
             "given out, and carbon dioxide and water if the fuel contains "
             "carbon and hydrogen.",
             "<strong>Oxidation:</strong> something gains oxygen and the "
             "product is heavier. Combustion is the fast version of this.",
             "<strong>Displacement:</strong> a metal and a compound of a less "
             "reactive metal, and the less reactive one comes out as a solid.",
         ],
         "close": "If yours says the same things in worse English, yours is "
                  "the more useful one — you will remember it."},

        {"type": "misconception", "id": "think-commit-one-box",
         "anchor": "s-think", "targets": "REACT-18"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page, and she is right not to:
    # this lesson's picture is eight reactions in words with the same five
    # buttons under each, because the whole claim is that what a reaction
    # LOOKS like is not what names it. A diagram here would be the drama.
    # §5.4 allows an empty list where it does not allow an absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "name-it-from-the-reactants",
         "text": "Name a reaction from its reactants, not from its "
                 "appearance. One reactant means decomposition; a metal and "
                 "another metal's compound means displacement; oxygen means "
                 "oxidation, and combustion if it burns.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-commit-one-box",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-18",
         "prompt": "The four have four different names, which certainly "
                   "suggests four separate boxes. Commit before you read on.",
         # ⚠️ MEASURED AND UNCHANGED (MRB-177): 8 / 13 / 10 / 9 words, correct
         # at index 1. It is the longest, by three words over a longest
         # distractor of ten and at a ratio of 1.3 — inside both of the gate's
         # thresholds, and inside them on the merits rather than by luck: two
         # of the three distractors state a wrong RULE about classification at
         # very nearly the same length as the right one.
         "options": [
             "Right — each reaction has exactly one type",
             "Wrong — combustion is a kind of oxidation, so both names can "
             "apply",
             "Right, because the four types are defined not to overlap",
             "Wrong — all four types overlap with each other",
         ],
         "reveal": [
             "Burning magnesium is combustion <em>and</em> oxidation, and "
             "both answers are right. The names are not four boxes side by "
             "side: <strong>combustion sits inside oxidation</strong>, as the "
             "case where the reaction is fast enough to burn. Naming it "
             "combustion is more specific and therefore usually the better "
             "answer — it says more.",
             "The two that genuinely cannot overlap are decomposition and the "
             "rest, because decomposition has one reactant and the others "
             "have two. So if you are ever torn between combustion and "
             "oxidation, you are not confused — you have noticed something "
             "true. Give the more specific name, and say why the other also "
             "applies.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her
    # rung labels are the engine's own defaults character for character
    # ("Recall", "The one that catches people", "Explain", "Take it somewhere
    # new"), so no rung authors a `title`. `feedback` is keyed by the INT
    # index of each wrong option, which is what `_rung_marked` reads.
    "ladder": {
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED AND UNMOVED. Design's set was "Thermal
        # decomposition" (2 words) against "Combustion", "Displacement" and
        # "Oxidation" (1 each): the correct answer strictly the longest at a
        # ratio of 2.0, which trips the gate's 1.4× on a rung whose options
        # are BARE TYPE NAMES and where the tell is therefore permanent — one
        # of the four types is a two-word name and the other three are not.
        #
        # Fixed at the distractor, and by naming each type as this unit itself
        # names it: `c5-01` teaches complete combustion, `c5-03` teaches
        # rusting as slow oxidation, `c5-04` teaches metal displacement. Every
        # option is now two words, every one still names exactly the type it
        # names, and each of Design's corrections still answers the option it
        # is attached to.
        "recall": {
            "q": "A reaction has exactly one reactant and two products, and "
                 "stops when the flame is removed. Which type is it?",
            "options": [
                "Complete combustion",
                "Thermal decomposition",
                "Metal displacement",
                "Slow oxidation",
            ],
            "answer": 1,
            "feedback": {
                0: "Combustion needs two reactants, one of which is oxygen, "
                   "and once started it supplies its own heat.",
                2: "Displacement needs a metal and a compound of another "
                   "metal — two reactants.",
                3: "Oxidation needs oxygen as a reactant. One reactant on its "
                   "own rules it out.",
            }},
        # The one that catches people, and it is `REACT-18` at the ladder.
        #
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED AND UNMOVED. Design's set ran 15, 9, 11 and 7
        # words: the correct answer strictly the longest and clear of the
        # field by four, which is the gate's threshold exactly. It is the
        # construct §13 names — the correct option here states a RULE with a
        # consequence ("both, and here is which one to give") while each
        # distractor stated a short verdict — so the fix is to make each
        # distractor state a wrong rule at the same length. Measured after:
        # 15 / 13 / 14 / 14, correct longest by one at a ratio of 1.07.
        "apply": {
            "q": "Magnesium ribbon burns in air with a bright white flame. A "
                 "student writes \"oxidation\" and another writes "
                 "\"combustion\". Who is right?",
            "options": [
                "Only the one who wrote combustion; oxidation is the wrong "
                "name for burning",
                "Only the one who wrote oxidation; combustion applies to "
                "fuels and not to metals",
                "Both — combustion is a kind of oxidation, and combustion is "
                "the more specific answer",
                "Neither — burning a metal in air is a displacement, not "
                "either of those",
            ],
            "answer": 2,
            "feedback": {
                0: "Magnesium gains oxygen, so it is unquestionably an "
                   "oxidation. Combustion is more specific, not more correct.",
                1: "Magnesium is behaving as a fuel: it burns with a flame "
                   "and gives out energy. Combustion fits.",
                3: "There is no second metal for it to displace. Displacement "
                   "needs a metal compound as a reactant.",
            }},
        "explain": {
            "q": "Two reactions both leave a black solid in a test tube: "
                 "heating copper carbonate, and heating copper in air until "
                 "it goes black. Explain how you would tell which is which "
                 "using only a balance and a limewater test, and name each "
                 "type.",
            "field_label": "Your explanation",
            "placeholder": "I would weigh the tube before and after…",
            "success": [
                "Says to weigh the contents before and after in both cases.",
                "Says the copper carbonate loses mass, because a gas leaves.",
                "Says the copper gains mass, because oxygen joins it.",
                "Says the limewater turns milky only for the carbonate, "
                "showing carbon dioxide.",
                "Names them correctly: thermal decomposition and oxidation.",
            ]},
        # The `produce` rung is item 8 asked as a question rather than met as
        # a card, and it is the rung that assesses `covers`: a set has edges,
        # and knowing you are standing on one is a scientific move rather than
        # a failure.
        "produce": {
            "q": "A student is told that a reaction between two colourless "
                 "solutions produced a solid, with no heat and no gas. They "
                 "try to fit it into the four types and fail. Explain why a "
                 "classification failing is not the same as the student "
                 "failing, and what they should do with the case.",
            "field_label": "Your answer",
            "placeholder": "None of the four types describes it because…",
            "success": [
                "Checks the case against the four rules and shows why none "
                "fits — no oxygen, no single reactant, no metal displacing "
                "another.",
                "Says a classification covers the cases it was built for, not "
                "every reaction there is.",
                "Says the right response is to describe what happened "
                "accurately rather than force a label.",
                "Suggests that other reaction types exist and names or "
                "describes one.",
                "Says a case that does not fit is information about the rule, "
                "and worth recording.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Byte-identical. It carries the whole decision rule and the tie-breaker
    # in five sentences, which is what a photographed note has to do.
    "key_note": "Name a reaction from its reactants. One reactant broken "
                "apart by heat is thermal decomposition. A metal plus a "
                "compound of a less reactive metal is displacement. Oxygen as "
                "a reactant is oxidation, and combustion when it burns with a "
                "flame — so combustion sits inside oxidation rather than "
                "beside it. Mass is the tie-breaker: gaining oxygen makes it "
                "heavier, losing a gas makes it lighter.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design's two "Going further" paragraphs, byte-identical. The first names
    # the two reactions the page has already shown without a label; the second
    # says what a classification is FOR, which is the argument item 8 makes
    # by example.
    "stretch": [
        {"type": "explainer", "id": "more-than-four",
         "text": "There are more reaction types than four, and the two you "
                 "have already met without a label are worth naming. Marble "
                 "chips in acid is <strong>neutralisation</strong>, which is "
                 "the whole of the next unit. Iron and sulfur heated together "
                 "to make iron sulfide is <strong>synthesis</strong> — two "
                 "elements joining to make one compound, the exact reverse of "
                 "decomposition. Chemists also cut the same set a different "
                 "way: exothermic reactions give out energy, endothermic ones "
                 "take it in, which puts combustion and displacement on one "
                 "side and thermal decomposition on the other."},
        {"type": "explainer", "id": "what-a-type-is-for",
         "text": "None of these classifications is a fact about nature; they "
                 "are all ways of grouping reactions so that a prediction "
                 "becomes possible. That is what a type is for. Knowing a "
                 "reaction is a displacement lets you predict the products "
                 "from a reactivity order you can look up, and knowing one is "
                 "a combustion lets you predict carbon dioxide and water "
                 "without being told. A name that does not let you predict "
                 "anything would not be worth learning."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent. Design
    # draws no support layer on this page, and the decision-rule block does
    # the job a support layer would: the rule is on screen, in order, above
    # the eight reactions that need it.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The key is `definition`, NOT `gloss` — `build_ks3.py:939` hard-indexes
    # `v["definition"]`.
    #
    # The four type names are re-glossed here even though each has its own
    # lesson, because this is the page a student comes back to when they
    # cannot tell them apart, and a glossary that assumed the other four
    # lessons were fresh would be useless to exactly that student. The last
    # four terms are the ones the stretch layer introduces.
    "vocabulary": [
        {"term": "reactant",
         "definition": "A substance you start with. It is written on the left "
                       "of an equation, and counting the reactants is the "
                       "first thing that names a reaction."},
        {"term": "product",
         "definition": "A substance the reaction makes. It is written on the "
                       "right of an equation."},
        {"term": "combustion",
         "definition": "Burning: a fuel reacting with oxygen, with a flame, "
                       "giving out energy. It is a fast oxidation, and the "
                       "more specific of the two names."},
        {"term": "thermal decomposition",
         "definition": "One substance broken down by heating into two or "
                       "more. The only one of the four types with a single "
                       "reactant."},
        {"term": "oxidation",
         "definition": "A substance gaining oxygen. The product is heavier "
                       "than the substance you started with, whether it "
                       "burned or not."},
        {"term": "displacement",
         "definition": "A more reactive metal taking the place of a less "
                       "reactive one in its compound. The less reactive metal "
                       "comes out as a solid."},
        {"term": "neutralisation",
         "definition": "An acid reacting with a base — including a carbonate. "
                       "It is not one of the four types, and it is the "
                       "reaction marble chips and acid are doing."},
        {"term": "synthesis",
         "definition": "Two or more substances joining to make one compound. "
                       "It is decomposition run the other way."},
        {"term": "exothermic",
         "definition": "Giving out energy to the surroundings. Combustion and "
                       "displacement are both exothermic."},
        {"term": "endothermic",
         "definition": "Taking energy in from the surroundings. Thermal "
                       "decomposition is endothermic, which is why the "
                       "heating has to keep going."},
    ],

    # ⊖ NO `safety_note`, and the decision is deliberate rather than an
    # omission (contract §16). This page gives no method and asks for nothing
    # to be done at a bench: the kiln, the thermite, the acid and the test
    # tubes are all DESCRIBED, in the past tense, as things that happened.
    # There is no instruction on the page a student could carry out.
    #
    # ⊖ AND NO `safeguarding_note`. Item 7 is respiration in the student's own
    # cells and item 4 is a gate rusting, and neither touches the student's
    # health or risk — this is a substance lesson exactly as C3's seven were.
    # Reported to the commander rather than added silently.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure whether to answer oxidation or "
                      "combustion?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Reaction types extended with neutralisation, "
                   "precipitation and redox — and classifying by energy "
                   "change as well as by reactants.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Classification against a stated rule, and what a scientist does with a
    # case the rule does not cover — which is item 8 and the `produce` rung.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
