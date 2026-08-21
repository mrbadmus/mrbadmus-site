"""C8 L3 — Groups and periods (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-03-groups-and-periods.dc.html`, and her
author's notes `NOTES-C8.md` §1, §3, §4, §5 flags 9 and 10, §6 (`PTAB-05`,
`PTAB-06`) and §7.

`PT.03a` — the table's address system — is the minted clause this lesson owns.
`PT.03b`, the metal / non-metal divide, is c8-01's. See
`ks3_data/substatements.py`.

── ⭐ A NUMBER IN THE PROSE WAS WRONG TWICE, IN TWO DIFFERENT WAYS ───────

Design's page states the distance between sodium and chlorine **twice and
inconsistently**: `#s-think` says they are "seven squares apart" and the apply
rung says "three squares apart". Counting the table drawn directly above both
sentences, they are **six** columns apart — sodium heads period 3 and chlorine
is the seventh square of it.

The standing build law is that where prose and instrument disagree, **the
instrument is the measurement and the prose changes**. Here the instrument is
right and both sentences are wrong, so both are corrected to six.

⚖️ And the correction is made CHECKABLE rather than remembered. The payload
carries a `separation_claims` entry, and `r_table_reader` measures it off
`LAYOUT` and fails the build if the sentence and the table disagree again. A
student can count the squares; so, now, can the build.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

This lesson holds **index 1** (recall, moved) and **index 0** (apply, Design's
own). ⚑ The apply rung's three distractors are re-authored for length
(MRB-177): Design's answer is 14 words against 6, 10 and 5, so it is longest
by four and pickable without reading. Each distractor is rewritten as a wrong
RULE in the answer's shape and they land at 11, 11 and 12.

── SCIENCE FLAGS ────────────────────────────────────────────────────────

⚑ Flag 9 — group number = number of outer electrons, stated for groups 1, 2, 7
and 0. KEPT (R4), correct at KS3. Helium's two electrons are the authored
exception and are handled on c8-06's shell strip, not here.

⚑ Flag 10 — the trend down a group explained by atomic size and the distance
of the outer electron. KEPT. It is the mechanism that makes group 7's reversal
in c8-05 predictable rather than arbitrary, and it is introduced here so that
c8-04 and c8-05 can both lean on it.

⚠️ HYDROGEN IS DRAWN IN GROUP 1 AND ITS NOTE SAYS IT IS NOT A METAL. That is
Design's own square and it is correct: hydrogen sits above group 1 by electron
count and belongs to no family by behaviour. The note is what stops the square
teaching that hydrogen is an alkali metal.

⚠️ THE PERIOD-1 ROW IS MOSTLY EMPTY AND MUST STAY SO (NOTES-C8 §7). Hydrogen
and helium sit at opposite ends of a row with six dashed holes between them.
Collapsing that row to two squares would teach that they are neighbours, and
the SHAPE OF THE GAP is part of what the table teaches. Period 4 is likewise
cut off after calcium rather than padded. Do not tidy either.
"""

LESSON = {
    "slug":  "groups-and-periods",
    "title": "Groups and periods",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "MODEL",

    "covers": ["KS3.C.PT.03a"],
    "touches": ["KS3.C.PT.01", "KS3.C.PT.04a"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "particles-and-matter", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    "requires": ["mendeleev"],
    "assumes": [],
    "references": ["metals-and-non-metals", "chemical-symbols", "formulae"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Sodium explodes on water. Magnesium, the square next "
                    "door, sits in it and barely fizzes. Potassium is two "
                    "rows away and behaves exactly like sodium. So which "
                    "tells you more about an element — its row or its "
                    "column?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Next door and two rows down", "done_when": "committed"},
        {"anchor": "s-table",  "short": "TABLE",
         "label": "The first twenty",      "done_when": "committed"},
        {"anchor": "s-read",   "short": "READ",
         "label": "Four questions",        "done_when": "all_four_answered"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Neighbours are not family", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Sodium and magnesium sit next door to each other. Sodium "
                 "and potassium are two rows apart.",
        "prompt": "Sodium explodes on water. Magnesium, its immediate "
                  "neighbour, sits in water all day and barely fizzes. "
                  "Potassium, which is nowhere near it on the row, behaves "
                  "exactly like sodium only more so — and its compounds have "
                  "the same formulae.",
        "commit": "Which tells you more about an element: its row or its "
                  "column?",
        "options": [
            "Its row — elements next to each other must be alike",
            "Its column — elements down a column are a family",
            "Neither; position in the table is just filing",
            "Both equally",
        ],
        "reveal": "The column. A column is a <strong>group</strong>, and a "
                  "group is a family: its members react in the same way and "
                  "form compounds with the same formulae. A row is a "
                  "<strong>period</strong>, and going along one takes you "
                  "from a violent metal at the left to an unreactive gas at "
                  "the right. Neighbours along a row have almost nothing in "
                  "common. Neighbours down a column have almost everything in "
                  "common.",
    },

    "misconceptions": [
        {"id": "PTAB-05",
         "statement": "Elements next to each other in the table are similar.",
         "elicited_by": "think-commit-neighbours",
         "confronted_by": "think-commit-neighbours"},

        # ⚑ NOTES-C8 §6 proposes `rung-2` / `rung-2-feedback`. The ladder
        # emits neither an `id` nor a `data-activity` per rung, so both would
        # fail MRB-244 / MRB-248. `PTAB-06` — "the group number tells you how
        # many electrons the atom HAS" — is elicited and confronted on the
        # TABLE, where every square prints its group beside its atomic number
        # and the two are visibly different for every element past helium.
        {"id": "PTAB-06",
         "statement": "The group number tells you how many electrons the atom "
                      "has altogether.",
         "elicited_by": "table-twenty",
         "confronted_by": "table-close"},
    ],

    # ── the confrontation (Law 3) ───────────────────────────────────────
    # ⚠️ AUTHORED IN `activities`, NOT LIFTED FROM `core`. `_normalise`
    # lifts INSTRUMENT kinds only, so a `misconception` core block whose id
    # names no activity renders as NOTHING AT ALL — `r_activity` returns an
    # empty string and the section, its `id`, its `data-activity` and its
    # rail stop all vanish. The page still builds and still reads.
    #
    # ⚑ The QUOTE is not authored here: `_confrontations` takes it from the
    # row for `targets` in `docs/ks3/misconception-register.md`, so the
    # register and the page have one source and cannot drift.
    "activities": [
        {"id": "think-commit-neighbours",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-05",
         "prompt": "Neighbouring squares do share a row. Commit before you read"
                    " on.",
         "options": [
             "Right — anything next to each other in the table is related",
             "Wrong — sodium and chlorine share a period and are opposites",
             "Right, because they have similar masses",
             "Wrong — no two elements are ever similar",
         ],
         "reveal": [
             "Sodium and chlorine are in the same period, six squares apart."
             " One is a metal soft enough to cut and violent in water; the"
             " other is a choking green gas. They are so unalike that they"
             " react together — and what they make is table salt.",
             "Now compare sodium with potassium, two rows down the same"
             " column. Same appearance, same reaction with water only faster,"
             " same formula for every compound. <strong>Similarity runs down"
             " the columns, not along the rows.</strong> A period is a"
             " journey; a group is a family.",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "The <strong>groups</strong> are the vertical columns, "
                 "numbered 1 to 7 and then 0. Elements in a group behave "
                 "alike, and the group number is a fact about the atom "
                 "itself: it is the number of electrons in the outer shell. "
                 "That is why the family resemblance exists."},
        {"type": "explainer",
         "text": "The <strong>periods</strong> are the horizontal rows. Going "
                 "across a period the elements change steadily from metals on "
                 "the left, through the staircase, to non-metals on the "
                 "right — and then the row starts over."},

        # ── #s-table — the tappable table. Light `ks3-block` → `check`.
        {"type": "table-reader", "id": "table-twenty", "anchor": "s-table",
         "eyebrow": "Your turn · read the table",
         "heading": "The first twenty elements. Tap any square.",
         "demand": "investigate",
         "resting": "Tap any square to read its address and its family.",
         "address_fmt": "Group %(group)s, period %(period)s · atomic number "
                        "%(num)s",
         # ⚠️ THE LAST COLUMN IS HEADED 0, NOT 8. The noble gases close the
         # row rather than continuing the count, and `r_table_reader` checks
         # every element's `group` against the HEADING above it rather than
         # against its 1-based position, precisely so that nobody "fixes" a
         # failing noble gas by renumbering group 0 to group 8.
         "group_heads": [1, 2, 3, 4, 5, 6, 7, 0],
         # ⚠️ `null` IS DRAWN, NOT SKIPPED. Period 1 is deliberately mostly
         # empty and period 4 is deliberately cut off after calcium — the
         # SHAPE OF THE GAP is part of what the table teaches. Do not tidy.
         "layout": [
             {"label": "Period 1", "period": 1,
              "cells": ["H", None, None, None, None, None, None, "He"]},
             {"label": "Period 2", "period": 2,
              "cells": ["Li", "Be", "B", "C", "N", "O", "F", "Ne"]},
             {"label": "Period 3", "period": 3,
              "cells": ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]},
             {"label": "Period 4", "period": 4,
              "cells": ["K", "Ca", None, None, None, None, None, None]},
         ],
         # The corrected claim, made checkable. See the docstring.
         "separation_claims": [{"a": "Na", "b": "Cl", "columns": 6}],
         "elements": {
             "H": {"sym": "H", "name": "Hydrogen", "num": 1,
                    "group": 1, "period": 1, "kind": "non-metal",
                    "note": "A special case: it sits above group 1 but is a colourless"
                            " gas, not a metal. It is the most abundant element in the"
                            " universe."
                    },
             "He": {"sym": "He", "name": "Helium", "num": 2,
                    "group": 0, "period": 1, "kind": "non-metal",
                    "note": "A noble gas with a full outer shell, so it reacts with"
                            " nothing at all. Second element, and the second most abundant"
                            " in the universe."
                    },
             "Li": {"sym": "Li", "name": "Lithium", "num": 3,
                    "group": 1, "period": 2, "kind": "metal",
                    "note": "Soft enough to cut with a knife and light enough to float on"
                            " water, which it also fizzes in. The least violent of the"
                            " alkali metals."
                    },
             "Be": {"sym": "Be", "name": "Beryllium", "num": 4,
                    "group": 2, "period": 2, "kind": "metal",
                    "note": "A light, stiff, expensive metal used in aerospace. Group 2"
                            " metals are harder and less reactive than group 1."
                    },
             "B": {"sym": "B", "name": "Boron", "num": 5,
                    "group": 3, "period": 2, "kind": "non-metal",
                    "note": "Sits right on the staircase between metals and non-metals,"
                            " and behaves like both. Used in heat-resistant glass."
                    },
             "C": {"sym": "C", "name": "Carbon", "num": 6,
                    "group": 4, "period": 2, "kind": "non-metal",
                    "note": "The element every living thing is built around. Comes as"
                            " diamond, graphite and soot — same atoms, different"
                            " arrangements."
                    },
             "N": {"sym": "N", "name": "Nitrogen", "num": 7,
                    "group": 5, "period": 2, "kind": "non-metal",
                    "note": "Four out of every five molecules in the air you are"
                            " breathing. Almost unreactive as a gas, essential in every"
                            " protein."
                    },
             "O": {"sym": "O", "name": "Oxygen", "num": 8,
                    "group": 6, "period": 2, "kind": "non-metal",
                    "note": "A fifth of the air, and the other half of water. Nothing"
                            " burns without it."
                    },
             "F": {"sym": "F", "name": "Fluorine", "num": 9,
                    "group": 7, "period": 2, "kind": "non-metal",
                    "note": "The most reactive element in the entire table — a pale"
                            " yellow gas that attacks almost anything, including glass."
                    },
             "Ne": {"sym": "Ne", "name": "Neon", "num": 10,
                    "group": 0, "period": 2, "kind": "non-metal",
                    "note": "A noble gas that glows orange-red when a current is passed"
                            " through it. Reacts with nothing."
                    },
             "Na": {"sym": "Na", "name": "Sodium", "num": 11,
                    "group": 1, "period": 3, "kind": "metal",
                    "note": "Directly below lithium, and it behaves like lithium only"
                            " more violently. Its compound with chlorine is on every table"
                            " in the country."
                    },
             "Mg": {"sym": "Mg", "name": "Magnesium", "num": 12,
                    "group": 2, "period": 3, "kind": "metal",
                    "note": "Burns with a blinding white flame. Next door to sodium and"
                            " nothing like it — a period is not a family."
                    },
             "Al": {"sym": "Al", "name": "Aluminium", "num": 13,
                    "group": 3, "period": 3, "kind": "metal",
                    "note": "The most common metal in the Earth’s crust, and the last one"
                            " to be discovered, because it is too reactive to be smelted"
                            " with carbon."
                    },
             "Si": {"sym": "Si", "name": "Silicon", "num": 14,
                    "group": 4, "period": 3, "kind": "non-metal",
                    "note": "Directly below carbon, and it forms the same kinds of"
                            " compounds — SiO2 is sand. Also the element every microchip"
                            " is cut from."
                    },
             "P": {"sym": "P", "name": "Phosphorus", "num": 15,
                    "group": 5, "period": 3, "kind": "non-metal",
                    "note": "One form catches fire in air on its own. Stored under water,"
                            " and essential to every cell in your body."
                    },
             "S": {"sym": "S", "name": "Sulfur", "num": 16,
                    "group": 6, "period": 3, "kind": "non-metal",
                    "note": "Yellow, brittle and found pure around volcanoes. Burns with"
                            " a blue flame to make the gas behind acid rain."
                    },
             "Cl": {"sym": "Cl", "name": "Chlorine", "num": 17,
                    "group": 7, "period": 3, "kind": "non-metal",
                    "note": "A green choking gas, directly below fluorine and reactive"
                            " for the same reason. Used in tiny amounts to make water safe"
                            " to drink."
                    },
             "Ar": {"sym": "Ar", "name": "Argon", "num": 18,
                    "group": 0, "period": 3, "kind": "non-metal",
                    "note": "Nearly one per cent of the air, and completely unreactive —"
                            " which is why it fills light bulbs and shields welding."
                    },
             "K": {"sym": "K", "name": "Potassium", "num": 19,
                    "group": 1, "period": 4, "kind": "metal",
                    "note": "Below sodium, and more violent again: it sets fire to the"
                            " hydrogen it produces on water. The trend down group 1 is"
                            " unmistakable."
                    },
             "Ca": {"sym": "Ca", "name": "Calcium", "num": 20,
                    "group": 2, "period": 4, "kind": "metal",
                    "note": "Below magnesium. Its carbonate is limestone, chalk, marble"
                            " and your own bones."
                    },
         },
         "families": {
             0: "Group 0 — the noble gases. Full outer shells, so they"
                  " react with nothing."
             ,
             1: "Group 1 — the alkali metals. Soft, light, and more"
                  " reactive as you go down."
             ,
             2: "Group 2 — the alkaline earth metals. Harder and less"
                  " reactive than group 1."
             ,
             3: "Group 3 — where the staircase between metals and non-"
                  " metals begins."
             ,
             4: "Group 4 — carbon at the top and silicon below it: the"
                  " elements that build structures."
             ,
             5: "Group 5 — nitrogen and phosphorus, both essential to life."
             ,
             6: "Group 6 — oxygen and sulfur, both of which react hungrily"
                  " with metals."
             ,
             7: "Group 7 — the halogens. Coloured, poisonous, and less"
                  " reactive as you go down."
             ,
         },
         "close_id": "table-close",
         "close_title": "The group number is not how many electrons the atom "
                        "has.",
         "close": [
             "Every square prints two numbers and they are not the same "
             "thing. The <strong>atomic number</strong> is how many electrons "
             "the atom has altogether — chlorine has seventeen. The "
             "<strong>group number</strong> is how many are in the OUTER "
             "shell, and chlorine is in group 7. It is the outer ones that do "
             "the chemistry, which is why a column is a family and a row is "
             "not.",
         ]},

        {"type": "key-fact", "ref": "columns-are-families"},

        # ── #s-read — four questions. `predict-cards`, placement 2 of 5.
        {"type": "predict-cards", "id": "read-four", "anchor": "s-read",
         "eyebrow": "Four questions · use the table above",
         "heading": "Read it, do not remember it",
         "demand": "apply",
         "lead": "Every one of these can be answered from the grid. Commit "
                 "before you read the explanation.",
         "head_counter": {"format": "{n} of {total} answered", "start": 0,
                          "total": 4},
         "items": [
             {"id": "q1",
              "q": "Which element is in group 2 of period 3?",
              "options": [{"id": "a", "label": "Sodium"},
                          {"id": "b", "label": "Magnesium"},
                          {"id": "c", "label": "Calcium"}],
              "answer": "Magnesium. Count two columns across on the third "
                        "row. Sodium is group 1 of period 3; calcium is group "
                        "2 but period 4 — one row too far down."},
             {"id": "q2",
              "q": "Lithium reacts with water to give lithium hydroxide and "
                   "hydrogen. What would you expect potassium to do?",
              "options": [{"id": "a", "label": "Nothing at all"},
                          {"id": "b", "label": "The same reaction"},
                          {"id": "c",
                           "label": "Give a completely different product"}],
              "answer": "The same reaction, giving potassium hydroxide and "
                        "hydrogen — because it is in the same group. That is "
                        "what a group is for: knowing one member tells you "
                        "about the rest. Potassium does it far more "
                        "violently, which is the trend down the column."},
             {"id": "q3",
              "q": "Which two of these behave most alike: chlorine and argon, "
                   "or chlorine and fluorine?",
              "options": [{"id": "a", "label": "Chlorine and argon"},
                          {"id": "b", "label": "Chlorine and fluorine"},
                          {"id": "c", "label": "Both pairs equally"}],
              "answer": "Chlorine and fluorine — both group 7. Chlorine and "
                        "argon are neighbours in period 3, and could hardly "
                        "be less alike: one is a violently reactive green "
                        "gas, the other reacts with nothing at all."},
             {"id": "q4",
              "q": "Silicon forms SiO2. Carbon is directly above it. What "
                   "would you expect the formula of carbon's oxide to be?",
              "options": [{"id": "a", "label": "CO2"},
                          {"id": "b", "label": "C2O"},
                          {"id": "c", "label": "CO3"}],
              "answer": "CO2 — same group, same combining ratio. This is the "
                        "most powerful thing a group tells you, and it is "
                        "exactly how Mendeleev predicted the formulae of "
                        "compounds of elements nobody had found yet."},
         ]},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Group", "Period", "Outer shell", "Family",
                   "Transition metal"]},

        {"type": "misconception", "id": "think-commit-neighbours",
         "anchor": "s-think", "targets": "PTAB-05"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "columns-are-families", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "Groups are the columns and hold families that behave alike. "
                 "Periods are the rows and run from metal to non-metal. Same "
                 "group means same chemistry; same period means almost "
                 "nothing."},
    ],

    "ladder": {
        # index 1 — moved from Design's 0. Option texts unchanged.
        "recall": {
            "q": "What is a group in the periodic table?",
            "options": [
                "A horizontal row of elements with similar masses",
                "A vertical column of elements that behave in similar ways",
                "All the metals taken together",
                "Elements that were discovered at the same time",
            ],
            "answer": 1,
            "feedback": {
                0: "That is a period, and the elements in one are not "
                   "similar.",
                2: "Metals span many groups. A group is one column.",
                3: "Discovery dates have nothing to do with the arrangement.",
            }},

        # index 0 — Design's own position. ⚑ "three squares apart" corrected
        # to SIX, against the table (see the docstring), and the three
        # distractors re-authored for length (MRB-177).
        "apply": {
            "q": "Sodium and chlorine are in the same period, six squares "
                 "apart. What does that tell you about their properties?",
            "options": [
                "Very little — a period runs from metals to non-metals, so "
                "neighbours differ hugely",
                "They will behave in similar ways, because sharing a row "
                "makes elements related",
                "They must have similar masses and so must have similar "
                "reactions",
                "They must both be in the same group, because they are on one "
                "row",
            ],
            "answer": 0,
            "feedback": {
                1: "They are so unalike that they react violently together. "
                   "Similarity runs down groups.",
                2: "Similar mass does not mean similar chemistry — that was "
                   "the whole reason Mendeleev swapped some pairs.",
                3: "Sodium is group 1 and chlorine is group 7. Sharing a "
                   "period is not sharing a group.",
            }},

        "explain": {
            "q": "Explain the difference between a group and a period, and "
                 "why knowing an element's group is more useful than knowing "
                 "its period.",
            "field_label": "Your explanation",
            "placeholder": "A group is…",
            "success": [
                "Says a group is a vertical column and a period is a "
                "horizontal row.",
                "Says elements in the same group have similar chemical "
                "properties.",
                "Says elements in a group have the same number of outer "
                "electrons.",
                "Says going across a period the elements change from metals "
                "to non-metals.",
                "Says the group predicts how an element will react and the "
                "period does not.",
            ]},

        "produce": {
            "q": "An element you have never heard of is in group 1, period 5. "
                 "Describe what you would expect it to be like and how it "
                 "would react with water, and explain how you know.",
            "field_label": "Your answer",
            "placeholder": "It would be…",
            "success": [
                "Says it is a metal, because group 1 is on the left of the "
                "table.",
                "Says it would be soft and could be cut, like the other "
                "group 1 metals.",
                "Says it would react with water to give a hydroxide and "
                "hydrogen.",
                "Says the reaction would be more violent than potassium's, "
                "because it is further down the group.",
                "Says the reasoning works because a group is a family with "
                "one outer electron each.",
            ]},
    },

    "key_note": "Columns are groups and rows are periods. Elements in the "
                "same group have the same number of outer electrons, react in "
                "similar ways and form compounds with the same formulae. "
                "Going across a period the elements change from metals to "
                "non-metals, so elements side by side in a row are usually "
                "nothing alike.",

    "stretch": [
        {"type": "explainer", "id": "transition-metals",
         "text": "The block of metals sitting between groups 2 and 3 from "
                 "period 4 onwards — iron, copper, nickel, zinc and the "
                 "rest — are the transition metals, and they break the neat "
                 "pattern on purpose. They are harder, denser and much less "
                 "reactive than the metals on the far left, their compounds "
                 "are coloured, and many are catalysts. They are also, almost "
                 "without exception, the metals anyone has ever built "
                 "anything out of."},
        {"type": "explainer", "id": "group-number-is-a-count",
         "text": "The group number is not a label somebody chose. Group 1 "
                 "elements have one electron in their outer shell, group 2 "
                 "have two, group 7 have seven and group 0 have a full shell. "
                 "Everything a group does chemically follows from that "
                 "number — which is why the same column reacts the same way, "
                 "and why the table would have to be redrawn if it were not "
                 "true."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Group",
         "definition": "A vertical column of the periodic table. Its elements "
                       "have the same number of outer electrons and behave "
                       "alike.",
         "note": "Numbered 1 to 7, and then 0 on the end."},
        {"term": "Period",
         "definition": "A horizontal row of the periodic table, running from "
                       "metals on the left to non-metals on the right.",
         "note": "A journey, not a family."},
        {"term": "Outer shell",
         "definition": "The outermost layer of electrons around an atom. It "
                       "is the one that takes part in reactions.",
         "note": "How many are in it IS the group number."},
        {"term": "Family",
         "definition": "A set of elements that react in the same way and form "
                       "compounds with the same formulae.",
         "note": "Another word for what a group is."},
        {"term": "Transition metal",
         "definition": "One of the block of harder, denser, less reactive "
                       "metals between groups 2 and 3.",
         "note": "Iron, copper, zinc — the ones things get built from."},
    ],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still mixing up groups and periods?",
              "cta": "Ask about this lesson",
              "anchor": "s-table"},

    "ks4_becomes": "Electron configuration, why group number equals outer "
                   "electrons, and the transition metals as a block with "
                   "their own rules.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
