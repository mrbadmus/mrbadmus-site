"""C6 L2 — The pH scale and indicators (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c6/c6-02-indicators-and-the-ph-scale.dc.html` (643
lines), and her author's notes `docs/ks3/design-reference/c6/NOTES-C6.md` §1,
§3, §5 flags 3, 4, 5, 9, §6 (`ACID-03`, `ACID-04`) and §7.

⚠️ THE TITLE AND SLUG ARE `structure.py`'s, NOT THE PAGE'S. Design's page is
headed "Indicators and the pH scale"; the skeleton's slot is
`the-ph-scale-and-indicators` / "The pH scale and indicators", the slug is
permanent (§8.4) and the title is what every index, breadcrumb and rail link
already prints. Nothing else moves: the teaching content, the instruments and
the words are hers.

── THREE THINGS THIS PAGE HAS THAT NO OTHER C6 PAGE HAS ────────────────

1. **A SIXTH RAIL STOP THAT MIRRORS THE FIRST.** Design's `DONE('s-scale')`
   returns `s.hookChoice !== null` — the identical expression to `s-hook`. That
   is a MIRROR in MRB-249's sense: the pH chart is a reference the student
   reads, it takes no commitment of its own, and three earlier units read
   exactly that as "a stop that cannot tick" and dropped it, shipping a rail
   Design did not draw. It is kept, with `mirrors: "s-hook"`, and
   `ks3_parity.check_rail_matches_design` asserts the mirror map against her
   own `isDone()`.

2. **THE CHART IS A DRAWN FIGURE.** Design's markup is fifteen flex divs in an
   `overflow-x: auto` box. It is authored here as a `figure` block with an
   `anchor` — legal since C3 (MRB-272) — and drawn by `ks3_art.c6._ph_strip`.
   The reason is containment: an absolutely positioned child escapes a scroller
   that is not `position: relative`, `overflow: hidden` does not fix it, and
   that is what widened five C5 pages by 140px at 390px. An SVG's children are
   inside its viewBox by construction, and `.ks3-figure-scroll` is the
   platform's already-measured, already-faded scroll region.

3. **FIFTEEN LITERAL HEX VALUES.** NOTES-C6 §7 flags this as the only
   non-token colour in C1–C8 and asks for a ruling. RULED AND KEPT: the ramp is
   the printed universal-indicator chart, which is scientific data rather than
   brand colour, and routing it through `--ks3-accent` would make the chart
   wrong to make the palette tidy. The ruling is conditional and the condition
   is enforced in code: every cell of the strip and every reading the bench
   prints carries its NUMBER, so identity is never hue-only and a colour-blind
   student reads the same instrument. The reason is written beside the array in
   `ks3_art/c6.py`, which is the file a future tidy-up would open.

── THE VERDICT IS DERIVED FROM THE NUMBER, NOT AUTHORED BESIDE IT ──────

Design computes a sample's verdict with a chain of ternaries on its pH. §5A
says a comparative label is derived at render and a verdict branches on the
thing the lesson teaches. So the five bands are authored ONCE with their
ranges and their verdicts, and `r_ph_bench` looks every sample's band up from
its own pH — refusing any sample filed under a band its number contradicts,
refusing ranges that leave a gap or overlap, refusing a band no sample lands
in, and refusing to let pH 7 share a band with 6 or 8, because "neutral is a
single point you cross" is the claim `neutralisation` is about to make.

── SCIENCE FLAGS, ALL RULED, ALL KEPT ──────────────────────────────────

⚑ Flag 3 — the classroom pH figures (battery acid 0, lemon 2, rainwater 6,
pure water 7, baking soda 9, oven cleaner 13). KEPT, all conventional.

⚑ Flag 4 — "each pH step is a factor of ten", made explicitly. KEPT, and it is
the reason this page has a `#s-think` block at all. It is the single most
repeated misconception in the topic and the lesson attacks it head on rather
than leaving the scale looking like a number line.

⚑ Flag 5 — rainwater at pH 6 because of dissolved carbon dioxide. KEPT. It is
C10-06's content arriving early, and it is what stops "pure water is 7" being
taught as "rain is 7".

⚑ Flag 9 — enamel dissolving below about pH 5.5, in rung 4. KEPT, standard
figure, and the rung is careful with it: the criteria require the student to
notice that pH alone does not settle the claim, because how long the drink
stays on the teeth matters too.
"""

from ks3_art.c6 import PH_COLOURS

# ── the six samples (Design's `SAMPLES`) ────────────────────────────────
#
# In her order, which walks the scale from one end to the other: 0, 2, 6, 7, 9,
# 13. The bench opens on battery acid, so the first thing a student meets is
# the far end rather than the middle.
#
# ⚠️ `band` IS NOT AUTHORED FREELY. `r_ph_bench` derives it from `ph` against
# the ranges below and raises if the two disagree — see the module docstring.
# It is written out here so the record reads as a record rather than as a
# lookup, and so the disagreement has something to be a disagreement WITH.
_SAMPLES = [
    {"id": "s1", "label": "Battery acid", "ph": 0, "band": "strong-acid",
     "litmus": "red",
     "setup": "A few drops from a car battery, handled with gloves and a face "
              "shield.",
     "why": "Sulfuric acid, and about as far down the scale as anything you "
            "will ever meet. It is a hundred thousand times more acidic than "
            "the vinegar on a chip shop counter."},
    {"id": "s2", "label": "Lemon juice", "ph": 2, "band": "strong-acid",
     "litmus": "red",
     "setup": "Squeezed straight from the fruit, no water added.",
     "why": "Citric acid. The same pH as the acid in your own stomach, and "
            "safe to drink because your mouth and stomach are built for it — "
            "your tooth enamel less so."},
    # ⚑ Flag 5 is this sample's `why`, kept whole.
    {"id": "s3", "label": "Rainwater", "ph": 6, "band": "weak-acid",
     "litmus": "red",
     "setup": "Collected clean, in the open, well away from a road.",
     "why": "Slightly acidic even when perfectly clean, because carbon "
            "dioxide from the air dissolves into it. Genuinely pure water at "
            "pH 7 is a laboratory object, not a weather event."},
    {"id": "s4", "label": "Pure water", "ph": 7, "band": "neutral",
     "litmus": "no change",
     "setup": "Distilled, straight from the still, kept sealed.",
     "why": "The definition of neutral. Leave the bottle open for an hour and "
            "it will drift towards 6 as air dissolves in."},
    {"id": "s5", "label": "Baking soda solution", "ph": 9,
     "band": "weak-alkali", "litmus": "blue",
     "setup": "A spatula of sodium hydrogencarbonate stirred into water.",
     "why": "A mild alkali — mild enough to eat, which is why it is in cakes "
            "and in some toothpastes, where it works against the acid that "
            "attacks enamel."},
    {"id": "s6", "label": "Oven cleaner", "ph": 13, "band": "strong-alkali",
     "litmus": "blue",
     "setup": "Sprayed into a beaker, in a fume cupboard, gloves on.",
     "why": "Sodium hydroxide. It is as far from neutral as the battery acid "
            "was, in the other direction, and it does comparable damage — but "
            "it feels soapy instead of stinging."},
]

# ── the five bands (Design's `guessButtons` and her verdict ternary) ────
#
# The buttons and the verdicts are ONE list here, because they are one thing:
# the band a student guesses is the band the reading is reported in, and
# authoring them apart is how the two drift. `lo`/`hi` must tile 0 to 14 with
# no gap and no overlap; pH 7 gets a band to itself, which is the shape the
# titration cliff in the next lesson depends on.
#
# The verdict strings are Design's own, character for character, from
# `const band = sample.ph < 3 ? 'Strongly acidic' : …`.
_BANDS = [
    {"id": "strong-acid",   "label": "pH 0–2",   "lo": 0,  "hi": 2,
     "verdict": "Strongly acidic."},
    {"id": "weak-acid",     "label": "pH 3–6",   "lo": 3,  "hi": 6,
     "verdict": "Weakly acidic."},
    {"id": "neutral",       "label": "pH 7",     "lo": 7,  "hi": 7,
     "verdict": "Neutral."},
    {"id": "weak-alkali",   "label": "pH 8–10",  "lo": 8,  "hi": 10,
     "verdict": "Weakly alkaline."},
    {"id": "strong-alkali", "label": "pH 11–14", "lo": 11, "hi": 14,
     "verdict": "Strongly alkaline."},
]

# ── the three jobs (Design's `JOBS`) ────────────────────────────────────
#
# ⭐ THE THIRD JOB'S ANSWER IS "NEITHER", and it is the reason the block has
# three options rather than two. A tool-choice exercise where every job has a
# right tool teaches that there is always one; this one ends on a question pH
# cannot answer at all, which is the difference between how acidic a solution
# is and how much acid is dissolved in it.
_JOBS = [
    {"id": "j1",
     "q": "A technician needs to know whether a spilled solution is acid or "
          "alkali, immediately, before deciding what to clean it up with.",
     "options": [{"id": "lit", "label": "Litmus"},
                 {"id": "uni", "label": "Universal indicator"},
                 {"id": "none", "label": "Neither"}],
     "answer": "lit",
     "reply": "Litmus. One question, one answer, no chart to consult: red "
              "means acid, blue means alkali. A pH number would be more "
              "information than the decision needs, and it would take longer "
              "to read."},
    {"id": "j2",
     "q": "A fish farmer must keep pond water between pH 6.5 and 8, and needs "
          "to know when it drifts out of range.",
     "options": [{"id": "lit", "label": "Litmus"},
                 {"id": "uni", "label": "Universal indicator"},
                 {"id": "none", "label": "Neither"}],
     "answer": "uni",
     "reply": "Universal indicator — or better, a pH meter. Litmus cannot "
              "help here at all: both ends of the acceptable range are close "
              "to neutral, and litmus only tells you which side of it you are "
              "on. This job needs a number."},
    {"id": "j3",
     "q": "A student wants to know how much acid is in a bottle of vinegar "
          "compared with a bottle of lemon juice.",
     "options": [{"id": "lit", "label": "Litmus"},
                 {"id": "uni", "label": "Universal indicator"},
                 {"id": "none", "label": "Neither"}],
     "answer": "none",
     "reply": "Neither, on its own. pH tells you how acidic the solution is, "
              "not how much acid is dissolved in it — a weak acid at high "
              "concentration and a strong acid at low concentration can read "
              "the same. Answering this properly means neutralising each with "
              "a measured alkali and comparing how much it took."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 225 character for character.
    "slug":        "the-ph-scale-and-indicators",
    "title":       "The pH scale and indicators",
    "discipline":  "chemistry",
    "unit":        "acids-and-alkalis",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.CR.05` is "the pH scale for measuring acidity/alkalinity; and
    # indicators", and this lesson owns both halves of it: the scale is the
    # figure and the bench, the indicators are the explainer and the job
    # chooser.
    "covers":      ["KS3.C.CR.05"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "measurement-and-uncertainty", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires":    ["acids-and-alkalis"],
    "assumes":     [],
    "references":  [],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A dye squeezed out of a boiled cabbage can tell you "
                    "something about a liquid that no amount of looking at it "
                    "will. What is it actually reading?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # SIX stops, Design's `RAIL`, in her order. ⭐ `s-scale` MIRRORS `s-hook`:
    # her `DONE('s-scale')` is `s.hookChoice !== null`, identical to the hook's,
    # because the chart is a reference the student reads rather than an
    # activity that takes a commitment. MRB-249 — a stop with no control of its
    # own is not a stop that can be dropped.
    #
    # ⚠️ NOTES-C6 §7 says five stops on this page. The RAIL const says six and
    # `docs/ks3/rail-manifest.md` records six, derived from that const. The
    # drawing wins over the note (MRB-205), and the gate compares against the
    # drawing.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Cabbage water", "done_when": "committed"},
        {"anchor": "s-scale",  "short": "SCALE",
         "label": "The pH scale", "done_when": "committed",
         "mirrors": "s-hook"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Testing bench", "done_when": "four_tested"},
        {"anchor": "s-choose", "short": "JOBS",
         "label": "Pick the indicator", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Ten times, not twice", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ THE HOOK CLOSES THE DOORS BY CONSTRUCTION, NOT BY SAYING SO. "Nothing
    # else was added and the cabbage water was the same in every beaker" is
    # what rules out A, C and D: the dye is the constant, so whatever it is
    # responding to is a property of the six beakers.
    "phenomenon": {
        "kind": "narrative",
        "title": "Boil a red cabbage, keep the purple water, and throw away "
                 "the cabbage. You have made a scientific instrument.",
        "prompt": "A few drops of that purple liquid go into six beakers. It "
                  "comes out red in one, pink in another, purple in the "
                  "third, then blue, then green, then yellow. Nothing else "
                  "was added and the cabbage water was the same in every "
                  "beaker.",
        "commit": "What is the cabbage dye responding to?",
        # MRB-177: 5, 7, 8, 7 words. The correct option is index 1 and is not
        # the longest — C is. Design's set, unchanged.
        "options": [
            "The temperature of each beaker",
            "How acidic or alkaline each one is",
            "Whether anything is dissolved in it at all",
            "How much water each beaker holds",
        ],
        "reveal": "How acidic or alkaline each beaker is. The dye is a "
                  "molecule that changes shape depending on the acid around "
                  "it, and a different shape reflects a different colour. Six "
                  "beakers, six positions on one scale — and because the "
                  "colours come in a fixed order, the colour is a "
                  "<strong>reading</strong>, not a decoration. That is what "
                  "an <strong>indicator</strong> is.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⊖ NOTES-C6 §6 proposes `think-reveal-factor-ten` for `ACID-03` and
    # `rung-2` / `rung-2-feedback` for `ACID-04`. Neither set of names can be
    # emitted from a lane: the `#s-think` reveal panel is drawn by
    # `build_ks3.py`'s shared `r_activity` with no id, and the ladder's rungs
    # are drawn by `r_ladder`, which numbers them but gives them no id either.
    # `build_ks3.py` is not a file this lane may touch.
    #
    # ⊕ So `ACID-03` names the activity that holds both its commitment and its
    # answer, which is the `c5-02` / `c4-01` reconciliation and what satisfies
    # Law 3's requirement for a real ACTIVITY id. `ACID-04` names `s-ladder`,
    # the section that holds rung 2 — that is exactly the fix MRB-244 made for
    # `b2-02`'s `BODY-06`, which had named "ladder" and now names the anchor
    # the page actually emits. Both the belief and its correction are inside
    # that section; the register says so and the built page can be checked.
    "misconceptions": [
        {"id": "ACID-03",
         "statement": "pH 2 is twice as acidic as pH 4 — it is half the "
                      "number, so it is double the strength.",
         "elicited_by": "think-commit-scale",
         "confronted_by": "think-commit-scale"},
        {"id": "ACID-04",
         "statement": "More indicator gives a different pH reading.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 105–106 — two paragraphs, so two blocks.
        {"type": "explainer",
         "text": "An <strong>indicator</strong> is a dye that changes colour "
                 "depending on whether it is in an acid or an alkali. "
                 "<strong>Litmus</strong> is the simple one: red in acid, "
                 "blue in alkali, and nothing in between. It answers one "
                 "question — which side of neutral is this? — and answers it "
                 "instantly."},
        {"type": "explainer",
         "text": "<strong>Universal indicator</strong> is a mixture of "
                 "several dyes, and its colour changes gradually all the way "
                 "along. Match that colour to a printed chart and you get a "
                 "number: the <strong>pH</strong>. Below 7 is acidic, above 7 "
                 "is alkaline, and 7 exactly is neutral."},

        # #s-scale — the reference. A drawn FIGURE with an anchor, and the rail
        # stop above mirrors the hook. See the module docstring for why it is
        # drawn rather than built out of flex divs.
        {"type": "figure", "ref": "ph-scale", "anchor": "s-scale"},

        # #s-bench — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ THE LEAD IS TEACHING STANCE, NOT A NARRATION OF THE CONTROLS.
        # Design's line is "N of 6 tested. Guess the band before you drop the
        # indicator in — a guess you commit to is worth ten you keep to
        # yourself." The count is not a head counter here — Design draws no
        # block-head readout on this section — so the sentence keeps its
        # teaching half and the count is dropped rather than invented.
        {"type": "ph-bench", "id": "bench-six", "anchor": "s-bench",
         "eyebrow": "Your turn · the testing bench",
         "heading": "Pick a sample, guess its pH, then drop the indicator in.",
         "prompt": "A guess you commit to is worth ten you keep to yourself.",
         "demand": "investigate",
         "guess_prompt": "Which band is it in?",
         "litmus_label": "Litmus:",
         "samples": _SAMPLES,
         "bands": _BANDS,
         # Design's own `DONE`: four of the six. Four is enough to have met
         # both ends of the scale and the middle; six would make the stop a
         # completion bar rather than a record of participation.
         "done_at": 4},

        {"type": "key-fact", "ref": "a-number-not-a-side"},

        # #s-choose — three jobs. Light `ks3-block` → `check`.
        {"type": "acid-judgements", "id": "jobs-three", "anchor": "s-choose",
         "eyebrow": "Three jobs · pick the right indicator",
         "heading": "Litmus, universal indicator, or neither",
         "prompt": "Commit to each. The right tool is the one that answers "
                   "the question being asked — no more than that.",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} decided", "start": 0},
         "items": _JOBS},

        {"type": "misconception", "id": "think-commit-scale",
         "anchor": "s-think", "targets": "ACID-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # ⚑ THE FIFTEEN HEX VALUES LIVE IN `ks3_art/c6.py` AS `PH_COLOURS` AND ARE
    # IMPORTED HERE RATHER THAN RETYPED. Two copies of a fifteen-entry ramp is
    # two places for one of them to be edited, and the bench's result chips are
    # painted from the same array — a strip and a chip that disagreed about the
    # colour of pH 9 would be the instrument contradicting its own reference.
    #
    # `neutral_at` is the assertion, not a setting: `_ph_strip` refuses any
    # value but 7, because the key fact, the key note and both marked rungs all
    # rest on it.
    "figures": [
        {"id": "ph-scale",
         "kind": "diagram",
         "status": "drawn",
         "art": "ph-strip",
         "title": "The pH scale",
         "desc": "Fifteen coloured cells in a row, numbered 0 to 14. Cells 0 "
                 "to 6 run from red through orange to yellow-green and are "
                 "the acids; cell 7 is green and is labelled neutral; cells 8 "
                 "to 14 run from green-blue through blue to purple and are "
                 "the alkalis. Each cell carries its own number.",
         # Design's own paragraph from page line 112, whole. It sits directly
         # under the strip and describes exactly what the strip is, so it is
         # the figure's caption rather than a separate explainer.
         "caption": "Fifteen whole numbers, one colour each. The reds and "
                    "oranges are acid, green is neutral, and the blues and "
                    "purples are alkali. The numbers matter more than the "
                    "colours: colour-blind chemists use a pH meter and get "
                    "the same answer.",
         "data": {
             "colours": PH_COLOURS,
             "neutral_at": 7,
             # Design's three mono captions, at her own wording.
             "acid_end": "Strongly acidic",
             "neutral_label": "Neutral · 7",
             "alkali_end": "Strongly alkaline",
             "note": "Every step of one is a factor of ten.",
         }},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "a-number-not-a-side",
         "text": "Litmus tells you which side of neutral you are on. "
                 "Universal indicator gives you a number on the pH scale — "
                 "and every step down that scale is ten times more acidic.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-scale",
         "kind": "predict",
         "demand": "explain",
         "targets": "ACID-03",
         "prompt": "It looks like an ordinary number line. Commit before you "
                   "read on.",
         # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
         # OPTION IS UNTOUCHED. Design's set ran 18 tokens against 8, 11 and 9:
         # strictly the longest by seven and at 1.64x, and a student could take
         # it without reading the quotation. Each now states a WRONG RULE about
         # the same scale, at the correct answer's own length — 18, 16, 17
         # against 18. Every distractor still carries the wrong idea it always
         # carried: half the number means double, the numbers are only labels,
         # and the range 0 to 14 is what makes 2 half of 4.
         "options": [
             "Right — half the number means double the acidity, so pH 2 is "
             "twice as strong as pH 4",
             "Wrong — each step is ten times, so pH 2 is a hundred times more "
             "acidic than pH 4",
             "Wrong — the numbers are only labels for the colours and say "
             "nothing at all about strength",
             "Right, because the scale runs from 0 to 14 and 2 is half of 4 "
             "on it",
         ],
         "reveal": [
             "Each step of one on the pH scale is a factor of "
             "<strong>ten</strong>. pH 3 is ten times more acidic than pH 4; "
             "pH 2 is a hundred times more acidic than pH 4; pH 1 is a "
             "thousand times. The numbers are close together because the "
             "scale squashes an enormous range into fifteen steps — that is "
             "the entire reason it exists.",
             "Which is why the gap between lemon juice at pH 2 and rainwater "
             "at pH 6 is not four small steps. It is ten thousand times. "
             "<strong>Two pH numbers that look near each other can describe "
             "liquids that behave nothing alike.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        # MRB-278: the answer moves to index 2. Design puts the correct option
        # first on all fourteen C6 rungs; the twelve this unit builds are
        # authored level at three per index, from the start rather than
        # rebalanced afterwards.
        #
        # ⚑ MRB-177 — ONE DISTRACTOR IS RE-AUTHORED AND THE CORRECT OPTION IS
        # UNTOUCHED. Design's set ran 15 tokens against 8, 11 and 10: longest
        # by four, which is exactly the threshold. The "more accurate" option
        # now states its wrong rule in the correct answer's own two-clause
        # shape and at 14 tokens, so 15 against 14 is ordinary unevenness. Its
        # correction is unchanged and still answers it, because it still
        # claims the indicator measures danger.
        "recall": {
            "q": "What does universal indicator do that litmus does not?",
            "options": [
                "It works on solids as well as solutions",
                "It is more accurate, so it tells you whether something is "
                "dangerous rather than just acidic",
                "It changes gradually, so it gives a pH number rather than "
                "just acid or alkali",
                "It changes colour permanently, so the result can be kept",
            ],
            "answer": 2,
            "feedback": {
                0: "Both need the substance in solution — a dry powder "
                   "changes nothing.",
                1: "Neither indicator measures danger. They measure position "
                   "on the pH scale.",
                3: "The colour of both depends on the solution they are "
                   "sitting in; neither is a permanent record.",
            }},
        # ⭐ THIS RUNG IS `ACID-04`, AND IT IS WHERE THE REGISTER POINTS. The
        # belief is that a deeper colour is a different reading; the rung
        # elicits it and its correction takes it apart, both inside `#s-ladder`.
        #
        # ⚑ MRB-177 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE CORRECT
        # OPTION IS UNTOUCHED. Design's set ran 11 words against 5, 5 and 7:
        # strictly the longest by four and at 1.57x, which is the construct §13
        # measures — the answer stated a RULE and each distractor was a short
        # bare claim. Each now states a WRONG RULE at the correct answer's own
        # length: 12, 12, 12 against 11. Every one of Design's corrections is
        # unchanged and still answers its own option, because each distractor
        # still carries the same wrong idea — more neutral, slightly alkaline,
        # too concentrated to read.
        "apply": {
            "q": "A solution turns universal indicator green. A student adds "
                 "more indicator and the green gets deeper. What has changed "
                 "about the solution?",
            "options": [
                "It has become more neutral — the deeper green is a stronger "
                "7",
                "It has become slightly alkaline, because the extra dye "
                "pushed it up",
                "It is now too concentrated to test, so the reading cannot be "
                "trusted",
                "Nothing — more dye gives a stronger colour, not a different "
                "pH",
            ],
            "answer": 3,
            "feedback": {
                0: "There is no more neutral. pH 7 is a single point, and the "
                   "amount of dye has nothing to do with where the solution "
                   "sits.",
                1: "The indicator reports the solution; it does not push it "
                   "up or down the scale in any way you could read.",
                2: "The dye is not the thing being measured. Adding more of "
                   "it only makes the same reading easier to see.",
            }},
        "explain": {
            "q": "Explain how you would find the pH of a soil sample from a "
                 "garden, and why the answer would be useful to the gardener.",
            "field_label": "Your method",
            "placeholder": "I would shake the soil with…",
            "success": [
                "Says to shake the soil with distilled water and let it "
                "settle or filter it.",
                "Says to add universal indicator to the liquid.",
                "Says to match the colour against the pH chart to read a "
                "number.",
                "Says different plants need different pH ranges.",
                "Says an out-of-range result tells the gardener what to add — "
                "lime for acid soil.",
            ]},
        # ⚑ Flag 9 lives here and is kept, with the hedge that makes it
        # honest: the last criterion requires the student to notice that pH
        # alone does not settle the claim.
        "produce": {
            "q": "A drinks company claims its new drink is “gentle on "
                 "teeth”. Enamel starts to dissolve below about pH 5.5. "
                 "Design a fair test that would check the claim against an "
                 "ordinary cola, and say what result would support it.",
            "field_label": "Your plan",
            "placeholder": "I would measure the pH of…",
            "success": [
                "Measures the pH of both drinks with universal indicator or a "
                "pH meter.",
                "Keeps the volume, temperature and method the same for both.",
                "Repeats the measurement to check it is reliable.",
                "Says the claim is supported only if the new drink reads "
                "above about 5.5.",
                "Notes that pH alone does not settle it — how long the drink "
                "stays on the teeth matters too.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "An indicator is a dye whose colour depends on how acidic or "
                "alkaline a solution is. Litmus is red in acid and blue in "
                "alkali. Universal indicator changes gradually and is matched "
                "against a chart to give a pH number: below 7 acidic, 7 "
                "neutral, above 7 alkaline. Each step on the scale is a "
                "factor of ten.",

    # ── the stretch layer (§5.6) ────────────────────────────────────────────
    "stretch": [
        {"type": "explainer", "id": "dyes-out-of-plants",
         "text": "Litmus is not a manufactured chemical. It is squeezed out "
                 "of lichens — the crusty growths on gravestones and stone "
                 "walls — and has been used as a dye since long before anyone "
                 "knew what pH was. Red cabbage, beetroot, blackberries and "
                 "the petals of hydrangeas all work for the same reason: the "
                 "pigment that makes them coloured is a molecule that changes "
                 "shape in acid. Hydrangeas go further and read the soil, "
                 "coming up blue in acid ground and pink in alkaline."},
        {"type": "explainer", "id": "nobody-judges-by-eye",
         "text": "Nobody in a working laboratory judges pH by eye any more. A "
                 "pH meter puts a thin glass bulb into the solution and "
                 "measures a voltage across it, giving two decimal places in "
                 "a second and no argument about whether the colour is more "
                 "yellow-green than green. Colour charts survive because they "
                 "are cheap, need no power and cannot go out of calibration "
                 "halfway through a lesson."},
    ],

    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Indicator",
         "definition": "A dye that changes colour depending on whether it is "
                       "in an acid or an alkali."},
        {"term": "Litmus",
         "definition": "The simplest indicator: red in acid, blue in alkali, "
                       "and nothing in between. It tells you which side of "
                       "neutral you are on and no more."},
        {"term": "Universal indicator",
         "definition": "A mixture of dyes whose colour changes gradually all "
                       "the way along the scale, so it gives a pH number "
                       "rather than a side.",
         "note": "Matched against a printed chart to read the number off."},
        {"term": "pH scale",
         "definition": "The numbered scale, 0 to 14, for how acidic or "
                       "alkaline a solution is. Each step of one is a factor "
                       "of ten."},
        {"term": "Neutral",
         "definition": "pH exactly 7 — neither acidic nor alkaline. It is a "
                       "single point on the scale, not a region."},
        {"term": "pH meter",
         "definition": "An instrument that measures pH electrically and reads "
                       "out a number, with no colour to judge by eye."},
    ],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # ⚑ NEW PROSE. ⊖ No safeguarding block — see `lesson_01`'s note; this is
    # lab safety and it takes a plain note.
    #
    # Scoped so it adds to the method rather than withdrawing it: the page
    # tests oven cleaner and battery acid on purpose, and this says how.
    "safety_note": "Two of the six samples on that bench are corrosive. They "
                   "are tested a few drops at a time, in a beaker, with "
                   "gloves and eye protection — never by dipping a strip into "
                   "the bottle, which contaminates what is left in it.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the scale jumps by ten?",
              "cta": "Ask about this lesson",
              "anchor": "s-scale"},

    "ks4_becomes": "pH as a measure of hydrogen ion concentration, the "
                   "logarithmic scale, and choosing indicators by the range "
                   "over which they change.",

    "ws": ["measurement", "analysis-and-evaluation"],

    "review_state": "draft",
}
