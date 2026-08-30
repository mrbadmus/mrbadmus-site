"""C8 L7 — Metal and non-metal oxides (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-07-metal-and-non-metal-oxides.dc.html`, and her
author's notes `NOTES-C8.md` §8 (the pH table, the two counter-cases, the
37-state bench, `PTAB-11`–`PTAB-14`).

── ⊕ `KS3.C.PT.06` IS CLOSED, 23 AUGUST 2026 ────────────────────────────

Until this file existed, `PT.06` — the chemical properties of metal and
non-metal oxides with respect to acidity — was **the only uncovered statutory
statement in C1–C8**, recorded as a real hole in three places. This lesson owns
it SOLELY. It is a statutory statement and not `beyond_statutory`: the ruling
is settled and it is a `PT` statement rather than a `CR` one because the whole
argument is that POSITION IN THE TABLE predicts which way the oxide goes.

`c8-06` touches `PT.06` in one prediction card and still does. Touching is not
owning; the register counts `covers`, and nothing about c8-06's record changes
now that this one exists. Its `⊖ R2` note — that no forward-link PROSE was
authored into the lesson body — is a decision about c8-06 and is still correct:
the endmatter prev/next is generated from unit order, so the link resolves on
its own today without a sentence having been written for it.

── FIVE RAIL STOPS, NOT SIX ─────────────────────────────────────────────

`README.txt` in the delivery says six, and `NOTES-C8.md` §7 says
"five in every lesson except `c8-06` and `c8-07`, which have six". **Design's
own page says five**, and the page is the measurement (MRB-205, MRB-249):

    const RAIL = [ s-hook, s-rule, s-bench, s-think, s-ladder ];

Five entries, and `docs/ks3/rail-manifest.md` — which is GENERATED from her
delivered page rather than written by hand — records the same five with
`s-rule=s-hook` as the mirror. The closing key note is a dark section the
engine emits itself and has never been a rail stop in this unit; counting it
would give c8-01 through c8-05 six stops as well.

── THE SPINE, AND BOTH PLACES THE FAMOUS VERSION BREAKS ─────────────────

Metal oxides are bases; non-metal oxides are acidic. The version a student
arrives with is "metal oxide means the water goes alkaline", and it is wrong
twice. **Both counter-cases are ON THE BENCH, not in a footnote:**

1. **COPPER OXIDE IS A BASE AND THE WATER STAYS AT 7.** It is insoluble, so
   there is nothing in solution for the indicator to report. `r_oxide_bench`
   refuses a chip flagged `insoluble` that does not read exactly 7 AND does not
   draw a residue with real depth — the student has to SEE black powder sitting
   under an unmoved number, because the reading alone reads as a refutation of
   the rule and the drawing is what makes it a distinction instead.
2. **WATER IS A NON-METAL OXIDE AND IT IS NEUTRAL.** Hydrogen oxide is on the
   tray and reads 7. The renderer refuses a bench with no neutral non-metal
   oxide, for the same reason.

The two of them read the SAME NUMBER for two completely different reasons,
which is why the comparison sentence has to be derived rather than stored: put
them side by side and the equal branch fires, and its tail names whichever chip
is the insoluble one.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

Design's indices are KEPT — recall at 2, apply at 3. C8's twelve marked rungs
measured three at each of the four positions before this lesson; fourteen now
measure 3 / 3 / 4 / 4, which is inside MRB-278's law (no index over half, none
at zero). Moving them would have been churn for a distribution that was already
uniform.

MRB-177 holds on both without a distractor being touched. On recall all four
options are eleven words; on apply the correct option is the SHORTEST (11
against 13, 14, 13), so it cannot be picked on length.

── ⊕ THE LAW 7 VOCABULARY BLOCK IS ADDED HERE ───────────────────────────

`README.txt` flags it: Design's page carries no vocabulary block, so its three
definitions live only in the KEY FACT box. That satisfies §4.8.1 B and fails
MRB-281's key-stage-wide `vocabulary` gate, which covers all 103 lessons with
no named escapes. Five cards are authored below and a `keyword` block placed at
`#s-words`, exactly as c8-06 does — the same position, the same component, and
NOT a rail stop on either page.

The five terms are the three the KEY FACT already defines (oxide, base, alkali)
plus the two words the bench cannot be read without: **insoluble**, which is
the whole of the copper-oxide case, and **neutral**, which is the whole of the
water case. No definition here contradicts the KEY FACT box; each is the same
sentence said to a student who is looking the word up rather than reading past
it.

── SCIENCE ─────────────────────────────────────────────────────────────

pH values are the ones NOTES-C8 §8 tabulates and Design's own `OXIDES` array
carries: CaO 12, MgO 10, CuO 7, H2O 7, CO2 5, SO2 3. All six are right for a
spatula of solid or a few seconds of gas in a beaker of water at KS3, and the
ordering — calcium above magnesium, sulfur below carbon — is the part a student
is asked to reason from, so it is the part that matters.

⚑ ACID RAIN IS FACTUAL AND CARRIES NO BLAME. Sulfur dioxide from coal and oil,
nitrogen oxides from hot engines, clean rain already near pH 6 because of
dissolved carbon dioxide, industrial rain measured near pH 4, limestone
weathering and lakes limed with powdered limestone. That is the whole of it.
No apocalypse and no personal guilt — the same standard C8-06's helium
paragraph was re-authored to under flag 18, and the one C10-06 holds.

⚑ ALUMINIUM OXIDE reacting both ways is amphoteric behaviour named as "an
element in between gives an oxide in between", in the stretch layer, where it
qualifies the rule without retracting it (MRB-225). The lesson body never says
"every oxide is one or the other", so nothing in it is taken back.

⚠️ NO FORWARD REFERENCES. Nothing here needs C9 or C10. The soil rung asks for
a base to be spread on acid soil, which is C6's neutralisation run outdoors,
and the copper-oxide-plus-acid equation is C6-06's salt preparation. Both are
Year 7 and both are already met.
"""

LESSON = {
    "slug":  "metal-and-non-metal-oxides",
    "title": "Metal and non-metal oxides",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "CONTRAST",

    # ⊕ THE LAST UNCOVERED STATUTORY STATEMENT IN C1–C8, CLOSED.
    "covers": ["KS3.C.PT.06"],
    "touches": ["KS3.C.PT.01", "KS3.C.PT.03a", "KS3.C.PT.03b",
                "KS3.C.CR.07a"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "particles-and-matter", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires": ["metals-and-non-metals"],
    "assumes": [],
    "references": ["the-ph-scale-and-indicators", "neutralisation",
                   "group-0-and-why-groups-exist"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Burn a metal and burn a non-metal, drop each product into "
                    "water, and the two solutions go opposite ways on the pH "
                    "scale. The side of the table the element came from "
                    "decides which way.",

    # FIVE stops, matched to Design's own RAIL const. `s-rule` carries no
    # control and mirrors the hook, which is her own DONE() and the mirror the
    # generated rail manifest records.
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "Two flames",       "done_when": "committed"},
        {"anchor": "s-rule",  "short": "KINDS",
         "label": "The two kinds",    "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "The oxide bench",  "done_when": "all_six_tested"},
        {"anchor": "s-think", "short": "THINK",
         "label": "Basic, not alkaline", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A ribbon of magnesium and a spoonful of sulfur, burned in "
                 "the same flame.",
        "prompt": "Both catch. Both leave a product behind, and both products "
                  "go into water and give a colourless solution you could not "
                  "tell apart by looking. Then the universal indicator goes "
                  "in: one beaker turns purple, the other turns red.",
        "commit": "What decided which way each one went?",
        "options": [
            "How hot the flame was",
            "Which side of the periodic table the element came from",
            "How much of the element was burned",
            "Whether the oxide came out as a solid or a gas",
        ],
        "reveal": "Magnesium is a metal, and its oxide takes the water above "
                  "7. Sulfur is a non-metal, and its oxide takes the water "
                  "below 7. Swap the flame for a hotter one, burn ten times as "
                  "much, use twice the water — the direction does not move. "
                  "What sets it is which side of the periodic table the "
                  "element started on.",
    },

    # ── ⊕ PTAB-11 … PTAB-14 (NOTES-C8 §8) ───────────────────────────────
    #
    # ⚠️ `PTAB-14` IS A NAMED SPARE RESERVED FOR C9 AND IS DELIBERATELY NOT IN
    # THIS LIST. It is recorded in `docs/ks3/misconception-register.md` in
    # prose, not as a table row, because `ks3_parity.check_misconception_
    # register` asserts BOTH directions: a row whose lesson is authored must be
    # referenced BY that lesson. Registering it here to "hold the number" would
    # therefore make it a live entry with no confrontation — Law 3's exact
    # failure — and registering it as a row without listing it here turns the
    # gate red. Prose registration is the `EARTH-18` shape and is the one that
    # holds a number without spending it.
    #
    # ⚠️ AND THE JOINS NAME ACTIVITIES, NEVER `think-reveal-*`. The shared
    # `r_activity` draws a confrontation's reveal with NO id, so a
    # `confronted_by` naming one would resolve against nothing (MRB-244). The
    # register's own PTAB section says this at length and it is why every C8
    # row already names the activity that owns both halves.
    #
    # ⚠️ `PTAB-11`'S STATEMENT IS DESIGN'S OWN DRAWN QUOTE, AND THAT IS WHY IT
    # IS ORDERED FIRST. `_misconception_quote` prints the statement of whatever
    # id the activity `targets` as the `.ks3-mis-quote` — so the sentence
    # authored here IS the sentence in the amber block. Design drew
    # *"The copper oxide left the pH at 7, so it cannot be a base."* and it is
    # the belief said concretely, about the chip the student has just tested.
    # Writing the abstract form there instead would have replaced her words
    # with a paraphrase for no gain (MRB-205).
    #
    # `PTAB-12` is the same belief with the concrete case taken out, and it is
    # confronted by the same block's LAST paragraph, which does nothing else:
    # "Basic is what a substance does to an acid. Alkaline is a description of
    # a solution." Two entries rather than one because a student can hold
    # either without the other — the `PTAB-02` / `PTAB-06` argument.
    "misconceptions": [
        # THE KEY DISCRIMINATING ENTRY. It is what makes copper oxide's 7 look
        # like a refutation rather than a distinction, and it is confronted by
        # the acid test in `#s-think` — the only test that can find a base the
        # water cannot report.
        {"id": "PTAB-11",
         "statement": "The copper oxide left the pH at 7, so it cannot be a "
                      "base.",
         "elicited_by": "think-commit-basic",
         "confronted_by": "think-commit-basic"},

        {"id": "PTAB-12",
         "statement": "Alkaline and basic mean the same thing.",
         "elicited_by": "think-commit-basic",
         "confronted_by": "think-commit-basic"},

        # Elicited and confronted on the BENCH rather than in the think block:
        # the tray holds two chips that dissolve completely, one that dissolves
        # a little, one that does not dissolve at all and two that are not
        # solids in the first place. The closing panel reads all six.
        {"id": "PTAB-13",
         "statement": "All oxides dissolve in water.",
         "elicited_by": "bench-six-oxides",
         "confronted_by": "bench-pattern"},
    ],

    # ── the confrontation (Law 3) ───────────────────────────────────────
    # ⚑ The QUOTE is not authored here: `_confrontations` takes it from the row
    # for `targets` in `docs/ks3/misconception-register.md`, so the register
    # and the page have one source and cannot drift.
    "activities": [
        {"id": "think-commit-basic",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-11",
         "prompt": "It is the reading everyone trusts. Commit before you read "
                   "on.",
         # ⚑ MRB-177. Design's four are 9, 13, 11 and 8 words, so the correct
         # one is neither the longest nor the shortest and each wrong option
         # states a WRONG RULE at full length rather than being a stub. Kept as
         # she wrote them.
         "options": [
             "Right — a base always takes the pH above 7",
             "Wrong — it hardly dissolved, so nothing was in the water to read",
             "Right — copper oxide is neutral, the same as water is",
             "Wrong — copper oxide is really an acidic oxide",
         ],
         "reveal": [
             "Pour warm dilute sulfuric acid onto that black powder and it "
             "disappears. The liquid turns blue, and what has formed is copper "
             "sulfate.",
             "copper oxide + sulfuric acid → copper sulfate + water",
             "A salt and water, out of an acid. That is what a base does, and "
             "the copper oxide has just done it.",
             "The pH test was never asking the right question. It reads what "
             "is dissolved, and almost no copper oxide dissolves. "
             "<strong>Basic</strong> is what a substance does to an acid. "
             "<strong>Alkaline</strong> is a description of a solution. Copper "
             "oxide is the first and never the second.",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Burn almost any element in air and it joins with oxygen. "
                 "What is left behind is an <strong>oxide</strong>."},
        # ⚑ THE ARROW IS DRAWN, NEVER TYPED. `t()` swaps U+2192 for the SVG
        # mark — the shipped latin subsets carry no arrow glyph — and `<sub>`
        # is a real element, which is the C2 flag 13 convention for the whole
        # course. Both survive `rich()`; neither would survive a data
        # attribute, which is why these two lines are markup and not payload.
        {"type": "explainer",
         "text": "magnesium + oxygen → magnesium oxide, MgO"},
        {"type": "explainer",
         "text": "sulfur + oxygen → sulfur dioxide, SO<sub>2</sub>"},
        {"type": "explainer",
         "text": "Both of those are oxides and neither looks anything like the "
                 "element that made it. Put each one in water and test the "
                 "solution, and the two results sit at opposite ends of the "
                 "pH scale."},

        # ── #s-rule — the reference. A `comparison` block: no control, and a
        # rail stop ticked by the hook (MRB-249, and Design's own DONE()).
        {"type": "comparison", "anchor": "s-rule",
         "eyebrow": "Reference · keep this one open",
         "eyebrow_tone": "accent-text",
         "statement": "The two kinds of oxide",
         "ground": "card",
         "columns": [{"caption": "Metal oxides", "tone": "accent-text"},
                     {"caption": "Non-metal oxides", "tone": "ink-muted"}],
         "row_tones": ["accent-tint", "band"],
         "rows": [
             {"name": "What it is",
              "cells": ["A base — it reacts with an acid to make a salt and "
                        "water",
                        "Acidic — it reacts with an alkali to make a salt and "
                        "water"]},
             {"name": "Shaken with water",
              "cells": ["Above pH 7, if it dissolves at all", "Below pH 7"]},
             {"name": "Universal indicator",
              "cells": ["Blue, or purple", "Orange, or red"]},
             {"name": "Where its element sits",
              "cells": ["Left and middle of the periodic table",
                        "Top right of the periodic table"]},
             {"name": "On the bench below",
              "cells": ["calcium oxide, magnesium oxide, copper oxide",
                        "carbon dioxide, sulfur dioxide, water"]},
         ],
         },

        # ⚑ DESIGN DRAWS THESE TWO PANELS INSIDE `#s-rule`, under the table.
        # `r_comparison` reads anchor, columns, eyebrow, eyebrow_tone, ground,
        # key_fact, row_tones, rows and statement — and nothing else — so a
        # `cards` key authored on the block above would be a dead key and two
        # empty panels. They are a `rule` block immediately after it instead:
        # same order on the page, same two definitions, and the anchor stays on
        # the comparison where the rail points at it.
        {"type": "rule",
         "eyebrow": "Two words that are not the same word",
         "statement": "A base does not have to dissolve. A base that has "
                      "dissolved is an alkali.",
         "cards": [
             {"role": "Base",
              "term": "Reacts with an acid to make a salt and water.",
              "gloss": "It does not have to dissolve to be one."},
             {"role": "Alkali",
              "term": "A base that has dissolved in water.",
              "gloss": "Only a dissolved base can move a pH reading."},
         ],
         "close": "The second row of the table is the one to read twice. A "
                  "metal oxide only shows up as an alkaline solution if it "
                  "dissolves, and not all of them do."},

        # ── #s-bench — six oxides, two beakers. Light `ks3-block` → `check`.
        {"type": "oxide-bench", "id": "bench-six-oxides", "anchor": "s-bench",
         "eyebrow": "Your turn · six oxides, two beakers",
         "heading": "Two beakers of the same water.",
         "demand": "investigate",
         "lead": "Every one of these six is an oxide — an element joined with "
                 "oxygen. Nothing else about them is the same.",
         "slot_fmt": "Beaker %d",
         "ph_label": "pH of the solution",
         "indicator_label": "Universal indicator:",
         "empty_kind": "water only",
         "empty_title": "Water, nothing added",
         "empty_line": "The baseline. Both beakers start here.",
         "compare_eyebrow": "Side by side",
         "clear_label": "Empty both beakers",
         "untested_lead": "Not yet in a beaker:",
         "all_tested": "All six have been in a beaker.",

         # ⚠️ FORMULAE ARE PLAIN DIGITS HERE. These strings land in a chip and
         # in a `data-` attribute the runtime reads, where markup is not
         # available — the C8 packaging-pass convention (`XO2`, `GeO2`,
         # `CO2`). `<sub>` belongs in the explainer above, which is markup.
         "oxides": [
             {"id": "cao", "name": "calcium oxide", "formula": "CaO",
              "kind": "metal", "ph": 12, "residue": "clear",
              "title": "Calcium oxide, stirred in",
              "residue_line": "All of it dissolved. Nothing left on the "
                              "bottom.",
              "note": "Calcium is a metal, so calcium oxide is a base. This "
                      "one dissolves freely, so there is plenty of it in "
                      "solution and the reading goes a long way up the "
                      "scale."},
             {"id": "mgo", "name": "magnesium oxide", "formula": "MgO",
              "kind": "metal", "ph": 10, "residue": "thin",
              "title": "Magnesium oxide, stirred in",
              "residue_line": "A little dissolved. Most of the white powder "
                              "is still on the bottom.",
              "note": "Magnesium is a metal, so magnesium oxide is a base. "
                      "Only a little of it dissolves, so the solution is "
                      "alkaline but the reading does not climb to the top of "
                      "the scale."},
             # ⊕ DISCRIMINATING CASE 1. A base, at pH 7, with the solid still
             # visible on the bottom. `r_oxide_bench` refuses this chip if the
             # reading moves or if the heap has no depth.
             {"id": "cuo", "name": "copper oxide", "formula": "CuO",
              "kind": "metal", "ph": 7, "residue": "heap", "insoluble": True,
              "title": "Copper oxide, stirred in",
              "residue_line": "None of it dissolved. The black powder is "
                              "sitting on the bottom exactly as it went in.",
              "note": "Copper is a metal, so copper oxide is a base — and "
                      "this reading cannot show that. Almost nothing went "
                      "into solution, so there is nothing in the water for "
                      "the indicator to report."},
             # ⊕ DISCRIMINATING CASE 2. A non-metal oxide that is neutral.
             {"id": "h2o", "name": "water", "formula": "H2O",
              "kind": "non-metal", "ph": 7, "residue": "self",
              "title": "Water — the oxide is the water",
              "residue_line": "Nothing to dissolve. This oxide is the water.",
              "note": "Hydrogen is a non-metal, so water is a non-metal "
                      "oxide: hydrogen oxide. It is also the liquid already "
                      "in the beaker. Not every non-metal oxide is acidic — "
                      "this one is the definition of neutral."},
             {"id": "co2", "name": "carbon dioxide", "formula": "CO2",
              "kind": "non-metal", "ph": 5, "residue": "gas",
              "title": "Carbon dioxide, bubbled through",
              "residue_line": "Bubbled in. The gas dissolves as it goes.",
              "note": "Carbon is a non-metal, so carbon dioxide is acidic. "
                      "Dissolved in water it makes carbonic acid, which is "
                      "why rain is slightly acidic before it has touched "
                      "anything at all."},
             {"id": "so2", "name": "sulfur dioxide", "formula": "SO2",
              "kind": "non-metal", "ph": 3, "residue": "gas",
              "title": "Sulfur dioxide, bubbled through",
              "residue_line": "Bubbled in. The gas dissolves as it goes.",
              "note": "Sulfur is a non-metal, so sulfur dioxide is acidic. It "
                      "dissolves readily, and the reading drops well down the "
                      "scale."},
         ],

         # DERIVED AND CHECKED. Two above 7, two below, two unmoved — counted
         # off the six readings above and refused if they disagree.
         "pattern_claim": {"above": 2, "below": 2, "same": 2},
         "close_id": "bench-pattern",
         "close_title": "Two went above 7. Two went below. Two did not move "
                        "at all.",
         "close": [
             "Calcium oxide and magnesium oxide are oxides of metals, and both "
             "took the water above 7. Carbon dioxide and sulfur dioxide are "
             "oxides of non-metals, and both took it below. Then there is "
             "copper oxide, a metal oxide that left the reading at 7 because "
             "it would not dissolve — and water, a non-metal oxide that left "
             "the reading at 7 because it is neutral. Same number, two "
             "different reasons, and neither of them is a hole in the "
             "pattern.",
         ]},

        {"type": "key-fact", "ref": "oxide-base-alkali"},

        {"type": "misconception", "id": "think-commit-basic",
         "anchor": "s-think", "targets": "PTAB-11"},

        # ⊕ LAW 7 (§5.4). Not drawn by Design — added here because her own
        # README asks for it and because MRB-281's vocabulary gate covers all
        # 103 lessons with no named escapes. Same component, same position and
        # the same five-card shape as c8-06.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. If "
                 "you cannot say it, you do not know it yet.",
         "terms": ["Oxide", "Base", "Alkali", "Insoluble", "Neutral"]},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        # Design's own box, verbatim. All three definitions plus the pattern —
        # NOTES-C8 §8 asks for exactly that, and the reason is `PTAB-11`: the
        # difference between a base and an alkali is what the copper-oxide
        # reading turns on, so it cannot be an aside.
        {"id": "oxide-base-alkali", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "An oxide is an element joined with oxygen. Metal oxides are "
                 "bases; non-metal oxides are acidic. A base that dissolves is "
                 "an alkali and takes the pH above 7 — a base that will not "
                 "dissolve is still a base."},
    ],

    "ladder": {
        # index 2 — Design's own. All four options are eleven words.
        "recall": {
            "q": "Sulfur is burned in air and the product is shaken with "
                 "water. What will that solution do to universal indicator?",
            "options": [
                "Turn it purple, because the oxide of a non-metal is alkaline",
                "Leave it green, because burning an element gives a neutral "
                "oxide",
                "Turn it red, because the oxide of a non-metal is acidic",
                "Turn it blue, because every oxide raises the pH of water",
            ],
            "answer": 2,
            "feedback": {
                0: "That is the metal oxide result. Non-metal oxides go the "
                   "other way.",
                1: "Burning sulfur gives sulfur dioxide, and its solution is "
                   "acidic, not neutral.",
                3: "Only metal oxides raise it. Sulfur is a non-metal.",
            }},

        # index 3 — Design's own, and the correct option is the SHORTEST of
        # the four, so it cannot be picked on length (MRB-177).
        "apply": {
            "q": "Copper oxide is stirred into water. The black powder sits on "
                 "the bottom and the pH reads 7. What does that tell you?",
            "options": [
                "It is neutral, because adding it did not move the pH at all",
                "It is an acidic oxide that is far too weak for water to show",
                "It is not a base, because every base pushes the pH above 7",
                "Nothing yet — it barely dissolves, so water cannot show it",
            ],
            "answer": 3,
            "feedback": {
                0: "A pH reading only reports what dissolved. Almost none of "
                   "this did.",
                1: "Copper is a metal, and metal oxides are bases, not acidic.",
                2: "Only a base that dissolves can do that. A base does not "
                   "have to dissolve.",
            }},

        "explain": {
            "q": "Copper oxide and magnesium oxide are both metal oxides. "
                 "Stirred into water, magnesium oxide takes the pH to 10 while "
                 "copper oxide leaves it at 7. Explain how both can still be "
                 "bases.",
            "field_label": "Your explanation",
            "placeholder": "Both of them are bases because…",
            "success": [
                "Says a base is a substance that reacts with an acid to make a "
                "salt and water.",
                "Says magnesium oxide dissolves, so its solution is alkaline "
                "and reads above 7.",
                "Says almost no copper oxide dissolves.",
                "Says a pH reading can only report what has dissolved.",
                "Says adding an acid to copper oxide would show it is a base.",
            ]},

        "produce": {
            "q": "A grower finds the soil in one field is too acidic for the "
                 "crop. Using the oxides on the bench above, say what could be "
                 "spread on that field and why. Then explain why burning a "
                 "heap of sulfur at the edge of the field would make the "
                 "problem worse.",
            "field_label": "Your answer",
            "placeholder": "I would spread…",
            "success": [
                "Chooses a metal oxide — calcium oxide or magnesium oxide.",
                "Says a metal oxide is a base, so it reacts with the acid in "
                "the soil.",
                "Says burning sulfur makes sulfur dioxide, which is a "
                "non-metal oxide.",
                "Says that oxide dissolves in water to give an acidic "
                "solution.",
                "Says adding more acid to soil that is already too acidic "
                "makes it worse.",
            ]},
    },

    "key_note": "An oxide is an element joined with oxygen. Metal oxides are "
                "bases: they react with acids to give a salt and water, and "
                "the ones that dissolve give alkaline solutions above pH 7. "
                "Non-metal oxides are acidic: dissolved in water they give "
                "solutions below pH 7. Two cases show why the words have to be "
                "exact. Copper oxide is a base that barely dissolves, so its "
                "reading stays at 7 and the acid test is the only one that "
                "finds it. Water is itself a non-metal oxide, and it is "
                "neutral.",

    "stretch": [
        # ⚑ ACID RAIN, FACTUAL, NO BLAME. See the docstring.
        {"type": "explainer", "id": "acid-rain",
         "text": "Coal and oil contain sulfur, so burning them sends sulfur "
                 "dioxide up the chimney, and an engine running hot enough "
                 "will make nitrogen and oxygen from the air combine into "
                 "nitrogen oxides. Both are non-metal oxides and both dissolve "
                 "in rain. Clean rain is already slightly acidic at about "
                 "pH 6, because carbon dioxide from the air dissolves in it; "
                 "rain measured downwind of heavy industry has come in nearer "
                 "pH 4. Limestone is calcium carbonate and reacts with acid, "
                 "which is why carved stone weathers faster in it, and why "
                 "powdered limestone is the thing tipped into an acidified "
                 "lake."},
        # ⚑ AMPHOTERIC BEHAVIOUR, NAMED WITHOUT THE WORD, AND IT RETRACTS
        # NOTHING (MRB-225). The lesson body never claims every oxide is one
        # or the other; it claims that the side of the table predicts which
        # way, and the staircase between the two sides is where that prediction
        # runs out.
        {"type": "explainer", "id": "in-between-oxides",
         "text": "The staircase of elements that will not commit to being "
                 "metals or non-metals has oxides to match. Aluminium oxide "
                 "reacts with acids the way a metal oxide should, and with "
                 "alkalis the way a non-metal oxide should. An element in "
                 "between gives an oxide in between — which is a useful "
                 "reminder that the rule in this lesson is a summary of "
                 "behaviour rather than a law that behaviour obeys."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Oxide",
         "definition": "A compound of an element with oxygen.",
         "note": "Burn almost anything in air and an oxide is what is left."},
        {"term": "Base",
         "definition": "A substance that reacts with an acid to make a salt "
                       "and water.",
         "note": "It does not have to dissolve to be one."},
        {"term": "Alkali",
         "definition": "A base that has dissolved in water, giving a solution "
                       "above pH 7.",
         "note": "Every alkali is a base. Not every base is an alkali."},
        {"term": "Insoluble",
         "definition": "Will not dissolve, so almost none of it ever gets into "
                       "the solution.",
         "note": "Copper oxide. It is why the pH test cannot find it."},
        {"term": "Neutral",
         "definition": "Neither acidic nor alkaline — pH exactly 7.",
         "note": "Water is a non-metal oxide and it is the definition of it."},
    ],

    # ⚠️ C8-16 — this lesson burns magnesium AND sulfur and shipped with an
    # EMPTY safety_note while every other demonstration lesson carried one.
    # The line below is Mide's, authored by him and approved 28 Aug 2026, and
    # it is reproduced VERBATIM. Do not reword, shorten or extend it.
    "safety_note": "Teacher demonstration only. Burning sulfur must be done "
                   "in a fume cupboard — the gas it gives off irritates your "
                   "lungs. Do not look straight at burning magnesium; the "
                   "light is bright enough to hurt your eyes. Eye protection "
                   "for everyone in the room.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still unsure how copper oxide can be a base at pH 7?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Amphoteric oxides, the trend in oxide acidity across a "
                   "period, and neutralisation written as an ionic equation.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
