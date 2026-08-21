"""C8 L1 — Metals and non-metals (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c8/c8-01-metals-and-non-metals.dc.html`, and her
author's notes `NOTES-C8.md` §1, §3, §4, §5 flags 1–4, §6 (`PTAB-01`,
`PTAB-02`) and §7.

Every student-facing string is lifted from the approved page — `RAIL`,
`CONTRAST`, `BENCH`, `RUNGS` and `SELF_RUNGS` through the node extractor, and
the hook options and reveal, the two explainer paragraphs, the bench's
progress line and closing panel, the key fact, the `#s-think` options and its
two reveal paragraphs, the key note and both "Going further" paragraphs by
reading `lessonVals()`, which is where most of a lesson's words live and which
a lift of the top-level constants alone silently loses. Where a string moves it
is marked ⚑ below.

── THREE STATEMENTS, ONE LESSON, AND ONE OF THEM IS A MINTED CLAUSE ─────

`PT.01` (varying properties of different elements) and `PT.05` (the properties
of metals and non-metals) are owned whole. `PT.03` is compound — "the periodic
table: periods and groups; metals and non-metals" — and Design's §1 gives it to
this lesson AND to c8-03. It is split in `ks3_data/substatements.py`: `PT.03a`
is the address system and belongs to c8-03; `PT.03b` is the metal / non-metal
divide and belongs here.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

Design puts the correct option FIRST on BOTH marked rungs, which is the
100%-at-index-0 defect the position gate was built for — every one of the 58
marked chemistry rungs measured on 21 Aug had its answer at index 0.

C8's twelve marked rungs are authored to hold three of each index. This lesson
holds **index 0** (recall, Design's own, unchanged) and **index 1** (apply,
moved). Only the ORDER moves: every option keeps its text and every `feedback`
key is re-keyed to the index its own option now sits at.

⚑ AND THE APPLY RUNG'S DISTRACTORS ARE RE-AUTHORED FOR LENGTH (MRB-177).
Design's correct option is 15 words against distractors of 8, 8 and 6 — the
answer is the long one and a student can see it without reading it. The fix is
made AT THE DISTRACTOR, never by trimming the answer: each is rewritten as a
WRONG RULE in the correct answer's shape ("it must be X, because <false general
claim>"), which is what MRB-177 asks for, and lands them at 13, 12 and 12.

── SCIENCE FLAGS, AND THE COMMANDER'S RULINGS ON THEM ───────────────────

⚑ Flag 1 — graphite conducting used as the discriminating case in BOTH the
hook and the misconception. KEPT (R4). It is the same fact doing two different
jobs: in the hook it defeats a test the student proposed, and at `#s-think` it
defeats a rule they hold. Nothing is retracted by a later sentence (MRB-225).

⚑ Flag 2 — mercury and bromine as the two liquid elements. KEPT, correct, and
it is the whole content of the apply rung.

⚑ Flag 3 — sodium "cuts like hard cheese" and floats. KEPT and deliberately
placed: it breaks the "metals are hard and heavy" habit three lessons before
c8-04 needs it gone.

⚑ Flag 4 — METALLIC BONDING STAYS, IN THE STRETCH LAYER, AND NOTHING ON ANY
RUNG MAY DEPEND ON IT (R4). It is KS4 content in one paragraph. Unlike C5's
sacrificial protection it contradicts no definition this unit has already
given — it EXPLAINS the list the lesson spent its whole length establishing,
which is what a stretch layer is for. The constraint is load-bearing and is
checked by eye against all four rungs: r1 and r2 are property lists, r3 is a
test method, r4 is a saucepan. Not one of them can be answered only by knowing
about free electrons, and not one of them is easier if you do.
"""

LESSON = {
    "slug":  "metals-and-non-metals",
    "title": "Metals and non-metals",
    "discipline": "chemistry",
    "unit": "The periodic table",
    "family": "CONTRAST",

    # PT.03b is the minted clause — the metal / non-metal divide. PT.03a (the
    # address system) is c8-03's. See substatements.py.
    "covers": ["KS3.C.PT.01", "KS3.C.PT.03b", "KS3.C.PT.05"],
    # ⚖️ `touches`, not a second `covers`. The lesson USES the table's shape
    # in its stretch layer (the staircase, silicon) without owning PT.03a.
    "touches": ["KS3.C.PT.03a"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3},
                {"id": "particles-and-matter", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ⚠️ NOT `measuring-a-temperature-change`. Design's page back-links to
    # c7-04, but `structure.py` puts C8 in Year 8 and C7 in Year 9, so
    # requiring a C7 lesson from here is a FORWARD reference in the default
    # sequence — the gate names it as one, and a student following the
    # sequence would meet this page months before the lesson it depends on.
    # Design's link is an assumption about order, and the skeleton is the
    # order. `elements` (C2) is the real prerequisite: this lesson sorts
    # elements, and a student who cannot say what one is cannot start.
    "requires": ["elements"],
    "assumes": [],
    "references": ["elements", "the-atom-daltons-model"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Two grey solids, both dull, both heavy, and both of them "
                    "conduct electricity. One is a metal and one is not — so "
                    "which single test tells them apart?",

    # ── the rail · FIVE stops, Design's own, matched stop for stop ─────────
    # `s-table` carries NO control and is ticked by the hook's commitment,
    # which is what MRB-249 licenses: the reference exists to be READ while
    # the bench beside it is worked.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Lead and graphite",     "done_when": "committed"},
        # ⚠️ NO CONTROL ON THIS STOP, SO IT MUST DECLARE WHAT IT MIRRORS.
        # `#s-table` is a `comparison` block: a reference to be read WHILE the
        # bench beside it is worked, which MRB-249 licenses. But a stop with
        # no control carries none of the signals `doneByDom()` reads, so
        # without `mirrors` it can never tick and the rail would stall at 1 of
        # 5 for a student who did everything on the page.
        {"anchor": "s-table",  "short": "LISTS",
         "label": "The two lists",         "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Six samples",           "done_when": "all_six_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "One test is not enough", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two grey solids on the bench. One is lead. One is a lump of "
                 "graphite from a pencil.",
        "prompt": "Both are dull grey. Both are heavy for their size. Both "
                  "mark paper if you press hard enough, and — the awkward "
                  "part — both conduct electricity when you wire them into a "
                  "circuit with a bulb.",
        "commit": "Which single test would separate them?",
        "options": [
            "Wire each into a circuit and see which conducts",
            "Hit each with a hammer",
            "Weigh equal volumes of each",
            "Look at which one is shinier",
        ],
        "reveal": "Hit them. The lead flattens; the graphite shatters into "
                  "black dust. Metals are <strong>malleable</strong> — they "
                  "change shape without breaking, because their atoms can "
                  "slide past each other and stay held together. Non-metal "
                  "solids are <strong>brittle</strong> and crack. Conducting "
                  "electricity was never going to settle it: graphite is the "
                  "one non-metal that conducts, and it is the reason no "
                  "single property can be trusted on its own.",
    },

    "misconceptions": [
        # `think-commit-conduct` is the misconception block's own id, which
        # `r_activity` emits as `data-activity`. NOTES-C8 §6 proposes
        # `think-reveal-graphite` for the confrontation; no `think-reveal-*`
        # id can be emitted from a lane — the shared renderer draws the reveal
        # with no id at all — so the join names the ACTIVITY that owns both
        # the commitment and the reveal. Same resolution as C7's `ENER-03`.
        {"id": "PTAB-01",
         "statement": "If it conducts electricity it must be a metal.",
         "elicited_by": "think-commit-conduct",
         "confronted_by": "think-commit-conduct"},

        # ⚑ NOTES-C8 §6 proposes `rung-2` / `rung-2-feedback` for `PTAB-02`.
        # NEITHER IS EMITTED. The mastery ladder draws no per-rung `id` and no
        # `data-activity`, so both values name a real place in the author's
        # head and no element in the document — which is precisely the MRB-244
        # defect, and it would have failed the gate rather than shipped.
        #
        # The join is moved to the two places that DO confront it and DO
        # render: the bench elicits it (sample C is a liquid the student has
        # to judge) and the bench's closing panel confronts it by name
        # ("Mercury is a metal that is liquid"). `bench-close` is authored on
        # the payload's `close_id`, so the register and the markup have one
        # source.
        {"id": "PTAB-02",
         "statement": "A liquid element cannot be a metal.",
         "elicited_by": "bench-six",
         "confronted_by": "bench-close"},
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
        {"id": "think-commit-conduct",
         "kind": "predict",
         "demand": "explain",
         "targets": "PTAB-01",
         "prompt": "Conducting is the property everyone reaches for first. Commit"
                    " before you read on.",
         # ⚑ MRB-177 / MRB-278 — THE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set gave the answer away on
         # length alone, which turns a commitment device into a shape puzzle:
         # a student picks the long one, never commits to the belief, and is
         # therefore never confronted with it. Each distractor now states its
         # wrong RULE at full length, which is what MRB-177 asks for.
         # 12, 13, 10, 12 words.
         "options": [
             "Right — anything that conducts electricity has to be a metal"
             " somewhere",
             "Wrong — graphite is a non-metal and conducts as well as some"
             " metals",
             "Right, because every single non-metal is an insulator without"
             " exception",
             "Wrong — metals do not conduct at all, they resist the current",
         ],
         "reveal": [
             "Graphite conducts electricity as well as some metals do, and"
             " it is carbon — one of the most thoroughly non-metallic"
             " elements there is. It is brittle, it has no shine worth the"
             " name, and it forms the acidic oxide that made your limewater"
             " go milky.",
             "Which is why classification uses a set of properties and not a"
             " single test. <strong>One property is a clue. Four agreeing"
             " properties is an identification.</strong> The same logic runs"
             " through the whole of chemical analysis.",
         ]},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "About three-quarters of the elements are "
                 "<strong>metals</strong>. They are shiny when freshly cut, "
                 "conduct heat and electricity, bend rather than break, and "
                 "nearly all of them are solid at room temperature with high "
                 "melting points."},
        {"type": "explainer",
         "text": "<strong>Non-metals</strong> are the opposite on every "
                 "count: dull, poor conductors, brittle if solid at all, and "
                 "many are gases. There are only about twenty of them — and "
                 "they include the ones life is made of."},

        # ── #s-table — the reference. A `comparison` block: no control, and
        # a rail stop ticked by the hook (MRB-249).
        {"type": "comparison", "anchor": "s-table",
         "eyebrow": "Reference · keep this one open",
         "eyebrow_tone": "accent-text",
         "statement": "The two lists, side by side",
         "ground": "card",
         "columns": [{"caption": "Metals", "tone": "accent-text"},
                     {"caption": "Non-metals", "tone": "on-dark"}],
         "row_tones": ["accent-tint", "band"],
         "rows": [
             {"name": "Appearance",
              "cells": ["Shiny when freshly cut or polished",
                        "Dull, or transparent, or invisible as a gas"]},
             {"name": "Hit with a hammer",
              "cells": ["Flattens — malleable", "Shatters — brittle"]},
             {"name": "Electricity",
              "cells": ["Conducts, all of them",
                        "Insulates, except graphite"]},
             {"name": "Heat",
              "cells": ["Conducts well — a metal spoon in tea gets hot",
                        "Insulates — a wooden one does not"]},
             {"name": "Melting point",
              "cells": ["Usually high; iron melts at 1538 °C",
                        "Usually low; most are gases at room temperature"]},
             {"name": "Sound",
              "cells": ["Rings when struck — sonorous", "Thuds or cracks"]},
         ],
         },

        # ⚑ NOT A `foot` KEY ON THE COMPARISON BLOCK. `r_comparison` reads
        # `anchor`, `columns`, `eyebrow`, `eyebrow_tone`, `ground`,
        # `key_fact`, `row_tones`, `rows` and `statement` — and nothing else.
        # A `foot` authored there is a dead key: the sentence never reaches
        # the page, and the page still builds and still reads. Caught by
        # `ks3_key_audit.py` as "read by nothing", which is what it was.
        {"type": "explainer",
         "text": "Every row has an exception somewhere in the table. That is "
                 "not a flaw in the list — it is the reason you judge an "
                 "element on several properties rather than one."},

        # ── #s-bench — six unlabelled samples. Light `ks3-block` → `check`.
        {"type": "property-sorter", "id": "bench-six", "anchor": "s-bench",
         "eyebrow": "Your turn · six unlabelled samples",
         "heading": "Read the data. Metal or non-metal?",
         "demand": "classify",
         "lead": "Three of the six break one of the rules in the table above "
                 "and are still what they are.",
         "head_counter": {"format": "{n} of {total} decided", "start": 0,
                          "total": 6},
         "options": [{"id": "metal", "label": "Metal"},
                     {"id": "non-metal", "label": "Non-metal"}],
         # ⚖️ `breaks` is the flag the closing panel's count is DERIVED from,
         # and `breaks_named` is checked to be real samples that carry it. The
         # panel says "three" and names three; the renderer refuses to ship a
         # panel that counts differently from the cards above it.
         "breaks_claim": 3,
         "breaks_named": ["x3", "x2", "x5"],
         "samples": [
             {"id": "x1", "code": "Sample A", "state": "solid",
              "answer": "metal",
              "facts": ["Silvery and shiny where it has been cut",
                        "Bends around a former without cracking",
                        "Conducts electricity; melts at 660 °C"],
              "why": "Aluminium. A metal on every count — shiny, malleable, "
                     "conducting, high melting point. Every property agrees, "
                     "which is what an easy identification looks like."},
             {"id": "x2", "code": "Sample B", "state": "solid",
              "answer": "non-metal", "breaks": True,
              "facts": ["Dull grey and marks paper",
                        "Shatters into flakes when hit",
                        "Conducts electricity"],
              "why": "Graphite — carbon, and a non-metal. The conducting is "
                     "the exception; the brittleness and the dullness are the "
                     "rule. Three properties against one settles it."},
             {"id": "x3", "code": "Sample C", "state": "liquid",
              "answer": "metal", "breaks": True,
              "facts": ["Silvery and mirror-bright",
                        "Conducts electricity",
                        "Freezes solid at −39 °C"],
              "why": "Mercury — a metal, and the one that is liquid at room "
                     "temperature. Its melting point breaks the pattern; "
                     "everything else about it is metallic."},
             {"id": "x4", "code": "Sample D", "state": "solid",
              "answer": "non-metal",
              "facts": ["Bright yellow and crumbly",
                        "Does not conduct electricity",
                        "Melts at 115 °C and burns with a blue flame"],
              "why": "Sulfur, a non-metal. Dull, brittle, insulating and "
                     "low-melting — non-metallic on every count and the "
                     "easiest sample here."},
             {"id": "x5", "code": "Sample E", "state": "solid",
              "answer": "metal", "breaks": True,
              "facts": ["Cuts with a knife like hard cheese",
                        "Floats on water and reacts with it violently",
                        "Shiny on the freshly cut surface, then dulls in "
                        "seconds"],
              "why": "Sodium — a metal, and one you will meet again. Soft "
                     "enough to cut and light enough to float, which is "
                     "nothing like the metals in a toolbox. The shine on the "
                     "cut surface is the giveaway."},
             {"id": "x6", "code": "Sample F", "state": "gas",
              "answer": "non-metal",
              "facts": ["Colourless and has no smell",
                        "Does not conduct electricity",
                        "Boils at −196 °C"],
              "why": "Nitrogen, a non-metal, and three-quarters of the air "
                     "in the room. No element that is a gas at room "
                     "temperature is a metal."},
         ],
         "close_id": "bench-close",
         "close_title": "Three of those broke a rule and were still what "
                        "they were.",
         "close": [
             "Mercury is a metal that is liquid. Graphite is a non-metal that "
             "conducts. Sodium is a metal soft enough to cut with a knife and "
             "light enough to float. If you had judged any of them on one "
             "property you would have got them wrong — and if you had judged "
             "them on four, you would have got them right.",
         ]},

        {"type": "key-fact", "ref": "whole-pattern"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Six words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Metal", "Non-metal", "Malleable", "Brittle",
                   "Sonorous", "Conductor"]},

        {"type": "misconception", "id": "think-commit-conduct",
         "anchor": "s-think", "targets": "PTAB-01"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "figures": [],

    "key_facts": [
        {"id": "whole-pattern", "placement": "top-level", "ground": "card",
         "eyebrow": "Key fact",
         "text": "Metals are shiny, malleable conductors with high melting "
                 "points. Non-metals are dull, brittle insulators, and many "
                 "are gases. Judge an element on the whole set, never on one "
                 "property."},
    ],

    "ladder": {
        # index 0 — Design's own order, unchanged.
        "recall": {
            "q": "Which set of properties describes a typical metal?",
            "options": [
                "Shiny, malleable, conducts electricity, high melting point",
                "Dull, brittle, insulating, low melting point",
                "Shiny, brittle, insulating, low density",
                "Always a solid, always dense, never reactive",
            ],
            "answer": 0,
            "feedback": {
                1: "That is the non-metal list.",
                2: "Brittle and insulating are non-metal properties — this "
                   "set contradicts itself.",
                3: "Mercury is liquid, sodium floats on water, and potassium "
                   "is one of the most reactive elements there is.",
            }},

        # index 1 — MOVED from Design's index 0, and the three distractors
        # re-authored as wrong RULES in the answer's shape (MRB-177).
        # `PTAB-02` at the ladder: the liquid that is a metal.
        "apply": {
            "q": "An unknown element is a liquid at room temperature. What "
                 "can you conclude?",
            "options": [
                "It must be a non-metal, because every one of the metals is "
                "solid",
                "Nothing on its own — mercury is a liquid metal and bromine "
                "is a liquid non-metal",
                "It must be a metal, because non-metals are gases or brittle "
                "solids",
                "It cannot be an element, because elements are solid or "
                "gaseous only",
            ],
            "answer": 1,
            "feedback": {
                0: "Mercury is a metal and is liquid at room temperature, so "
                   "the rule the answer rests on is false.",
                2: "Bromine is a liquid non-metal — a dark red one — so "
                   "non-metals are not only gases and brittle solids.",
                3: "Both mercury and bromine are elements, and both are "
                   "liquid at room temperature.",
            }},

        "explain": {
            "q": "A student is given an unknown solid element. Describe the "
                 "tests you would carry out to decide whether it is a metal "
                 "or a non-metal, and explain why one test alone would not "
                 "be enough.",
            "field_label": "Your method",
            "placeholder": "First I would look at…",
            "success": [
                "Looks at whether it is shiny or dull.",
                "Hits or bends it to see whether it is malleable or brittle.",
                "Tests whether it conducts electricity in a simple circuit.",
                "Considers its melting point or whether it conducts heat.",
                "Says exceptions exist, so the decision is made on the "
                "pattern of several results.",
            ]},

        "produce": {
            "q": "Saucepans are made of metal but the handles are usually "
                 "plastic or wood. Explain the choice of each material in "
                 "terms of the properties in this lesson, and say what would "
                 "go wrong if the two were swapped.",
            "field_label": "Your answer",
            "placeholder": "The pan is metal because…",
            "success": [
                "Says the pan is metal because metals conduct heat well.",
                "Says the handle is a non-metal because it does not conduct "
                "heat.",
                "Says metals also have high melting points, so the pan "
                "survives the hob.",
                "Says a metal handle would become too hot to hold.",
                "Says a plastic pan would melt or would not pass heat to the "
                "food.",
            ]},
    },

    "key_note": "Metals are shiny, malleable, sonorous, and good conductors "
                "of heat and electricity, with high melting and boiling "
                "points. Non-metals are dull, brittle when solid, poor "
                "conductors, and often gases. Exceptions exist for every "
                "single property — mercury, graphite, sodium — so elements "
                "are classified on the whole pattern rather than one test.",

    "stretch": [
        {"type": "explainer", "id": "the-staircase",
         "text": "The dividing line on the periodic table runs as a staircase "
                 "down the right-hand side, and the elements sitting on it "
                 "refuse to choose. Silicon is shiny like a metal and brittle "
                 "like a non-metal; it conducts, but only a bit, and only "
                 "under some conditions. That halfway behaviour is the reason "
                 "it is in every computer ever built — a semiconductor is "
                 "useful precisely because it can be persuaded to conduct or "
                 "not."},
        # ⚑ Flag 4. KS4 content, kept (R4), and NOTHING ON ANY RUNG DEPENDS
        # ON IT. It explains the list rather than replacing it, and it
        # contradicts no definition the lesson has already given (MRB-225).
        {"type": "explainer", "id": "one-idea-five-properties",
         "text": "The properties are not a list to be memorised; they all "
                 "follow from one thing. In a metal, the outer electrons are "
                 "not tied to individual atoms — they move freely through the "
                 "whole structure. Free electrons carry charge, which makes "
                 "metals conduct; they carry energy, which makes metals "
                 "conduct heat; and they let layers of atoms slide over each "
                 "other and stay bonded, which makes metals bend instead of "
                 "shatter. One idea, five properties."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Metal",
         "definition": "An element that is shiny, malleable and a good "
                       "conductor of heat and electricity, usually with a "
                       "high melting point.",
         "note": "About three-quarters of all the elements."},
        {"term": "Non-metal",
         "definition": "An element that is dull, brittle when solid and a "
                       "poor conductor, and often a gas at room temperature.",
         "note": "Only about twenty of them, and life is built from them."},
        {"term": "Malleable",
         "definition": "Able to be hammered or bent into a new shape without "
                       "breaking.",
         "note": "The test that separates lead from graphite."},
        {"term": "Brittle",
         "definition": "Breaks or shatters when hit rather than changing "
                       "shape.",
         "note": "What every non-metal solid does under a hammer."},
        {"term": "Sonorous",
         "definition": "Rings with a clear note when it is struck.",
         "note": "Why bells are metal and never wood."},
        {"term": "Conductor",
         "definition": "A material that lets electricity or heat pass "
                       "through it easily.",
         "note": "Graphite is the non-metal that does it anyway."},
    ],

    "safety_note": "Sample E is sodium and is a teacher demonstration, "
                   "behind a screen, with the smallest piece that can be cut. "
                   "Mercury is not handled in a school laboratory at all — "
                   "the sample on this bench is data, not a bottle on a "
                   "shelf.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still unsure why graphite breaks the rule?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Metallic bonding and the sea of delocalised electrons, "
                   "and how position in the table predicts whether an oxide "
                   "is acidic or basic.",

    "ws": ["analysis-and-evaluation"],
    "review_state": "draft",
}
