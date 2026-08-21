"""C9 L1 — The reactivity series (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c9/c9-01-the-reactivity-series.dc.html`, and her
author's notes `NOTES-C9.md` §1, §3, §4 flags 1–5, §5, §6 (`MATL-01` to
`MATL-03`) and §10.

── ⭐ FIVE RAIL STOPS, NOT FOUR, AND DESIGN'S OWN DRAWING SETTLES IT ─────

`NOTES-C9.md` §10 records a CORRECTION: "An earlier draft of this section
recorded FIVE stops... The count is four, matching B9–B11, P4/P5, P6/P7 and
P8/P9", with the misconception block losing its stop.

**Her own `RAIL` constant draws FIVE**, on all four pages, and the frozen
reference is what `ks3_rail_manifest.py` reads — it already records
`s-hook s-series s-bench s-think s-ladder` with `s-series=s-hook`. The
standing build law is that where prose and instrument disagree, THE INSTRUMENT
IS THE MEASUREMENT and the prose changes. So the build is five, and `#s-think`
keeps the stop her note would have taken from it.

⊕ And the note's own reasoning survives intact under the five: what MRB-249
licenses is a CONTROLLESS stop, and `#s-series` is exactly that — a reference
to be read while the bench beside it is worked. It carries `mirrors: s-hook`,
which is what her `isDone()` gives and what the manifest records.

── ⚖️ THE ORDER IS DERIVED, AND THIS IS THE FIRST TIME PAST FOUR ROWS ───

Six metals, twelve cells. `NOTES-C8.md` §4 anticipated C9's series as the
first instrument with more than four rows to test C5's ruling that ORDER IS
DATA. It holds: `rank` decides the order in one function, the BANDS are
checked against the twelve cells for every metal, and `order_claim` is checked
against the ranks. Re-sorting the payload cannot move a metal between bands or
change the order the panel states.

── ⚑ `WS.EXP.02` IS NOT THIS LESSON'S, AND `MATS.01` IS OWNED WHOLE ─────

`MATS.01` names "metals **and carbon**", so carbon's position is established
here — in the reference list, marked as a non-metal, with the prose saying what
earns it the place — rather than left to c9-03 to claim as well. No sub-ID is
minted: §11.11 allows a clause split and the statement does not need one, and a
mint is permanent once referenced.

── SCIENCE FLAGS, AND THE COMMANDER'S RULINGS ───────────────────────────

⚑ Flag 1 — MAGNESIUM IN COLD WATER IS HEDGED, NOT DENIED, AND THE HEDGE IS
LOAD-BEARING. Many schemes say flatly "no reaction". The reaction is real and
too slow to watch, and the band label is "needs acid before much happens"
rather than "no reaction with water" precisely because of it. KEPT: a page that
says "no reaction" and a band that says "not much" cannot both be true, and the
true one is the hedge.

⚑ Flag 2 — POTASSIUM IN DILUTE ACID IS NOT DONE, AT ANY CONCENTRATION, AND
THE CELL SAYS SO. Safety over completeness, KEPT. The cell is readable and the
note IS the teaching: potassium is violent with water alone, dilute acid is
mostly water, and the water test has already settled its position. This is the
fourth cell state that `reactivity-grid` has no room for and the reason
`reaction-audit` is its own family.

⚑ Flag 3 — the apparatus line sits on the potassium cell only, because that is
the cell where the CHEMISTRY needs it. KEPT. It is not a control measure and
the page is not a risk assessment; see §5 below.

⚑ Flag 4 — calcium turning the water cloudy white (calcium hydroxide, slightly
soluble). KEPT and correct.

⚑ Flag 5 — "iron chloride" without the (II). KEPT, matching the C5 flag-11 and
C6 flag-11 convention: the number in brackets is a GCSE distinction and naming
it here would introduce a notation the page never explains.

── §5 · PRACTICALS AND RISK ASSESSMENT ──────────────────────────────────

This bench is a SIMULATION OF A DEMONSTRATION and is not a method. Potassium
and calcium in water, and four metals in dilute hydrochloric acid, all need a
written risk assessment before anything is run in a room. The `safety_note`
says so; the apparatus line on the potassium cell does not stand in for one.

── ⚑ MRB-278 · ANSWER POSITION ──────────────────────────────────────────

C9's eight marked rungs are authored two to each index. This lesson holds
**index 0** (recall, Design's own) and **index 1** (apply, moved). Only the
order moves and no option text is edited.

── SAFEGUARDING ─────────────────────────────────────────────────────────

No lesson in C9 touches a student's own body or health — the unit is
reactivity, extraction and materials throughout — so Design carried no
Childline block and none is added. The judgement is recorded rather than
assumed, because the absence of a block is indistinguishable from an oversight
unless somebody writes down that it was checked.
"""

LESSON = {
    "slug":  "the-reactivity-series",
    "title": "The reactivity series",
    "discipline": "chemistry",
    "unit": "Metals and materials",
    "family": "CLASSIFY",

    "covers": ["KS3.C.MATS.01"],
    "touches": ["KS3.C.PT.04a", "KS3.C.PT.05"],
    "beyond_statutory": False,
    "threads": [{"id": "substances-and-reactions", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    "requires": ["displacement"],
    "assumes": [],
    "references": ["displacement", "acid-plus-metal",
                   "group-1-the-alkali-metals"],
    "connects_heading": "Next in this unit",
    "ks4_links": [],

    "big_question": "Potassium attacks cold water hard enough to set fire to "
                    "its own hydrogen. Copper carries cold water through "
                    "houses for fifty years and does not change. Both are "
                    "metals — so what is the difference made of?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Three beakers",       "done_when": "committed"},
        # Controlless reference (MRB-249): read while the bench is worked.
        {"anchor": "s-series", "short": "SERIES",
         "label": "The reactivity series", "mirrors": "s-hook",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Twelve tubes",        "done_when": "all_twelve_read"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "One test is not enough", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",      "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Three beakers of cold water. A pea-sized piece of "
                 "potassium, a lump of calcium, and a coil of copper wire.",
        "prompt": "The potassium fizzes so hard it skids across the surface "
                  "and the gas it gives off catches fire. The calcium sinks, "
                  "streams bubbles and turns the water cloudy. The copper "
                  "does nothing — and copper pipes carry cold water in houses "
                  "for fifty years without changing at all.",
        "commit": "All three are metals. So why does one of them attack water "
                  "and another ignore it?",
        "options": [
            "The potassium piece was smaller, so it reacted faster",
            "Reactivity is a property of the element, and it differs",
            "The copper was coated, so the water never reached it",
            "Cold water only reacts with metals that are soft",
        ],
        "reveal": "Because <strong>reactivity is a property of the element"
                  "</strong>, like melting point, and it differs from metal "
                  "to metal. It is not about how hard, how heavy or how shiny "
                  "the metal is. Test enough metals against the same thing "
                  "and the differences line up into one order — and that "
                  "order holds for every reaction, not just the one you "
                  "tested.",
    },

    "misconceptions": [
        {"id": "MATL-01",
         "statement": "A metal that does nothing in cold water is unreactive.",
         "elicited_by": "think-commit-water",
         "confronted_by": "think-commit-water"},
        # ⚑ NOTES-C9 §6 anchors `MATL-02` on `rung-2` / `rung-2-feedback`.
        # The ladder emits neither an `id` nor a `data-activity` per rung, so
        # both would fail MRB-244 / MRB-248 — the same correction C8 needed.
        # The bench elicits it (a steel-strong metal doing nothing while a
        # soft one fizzes) and its closing panel confronts it.
        {"id": "MATL-02",
         "statement": "Reactivity is the same thing as strength or hardness.",
         "elicited_by": "bench-twelve",
         "confronted_by": "bench-close"},
        # ⚑ NO `elicited_by`, DELIBERATELY (audit law 15). Nothing on the page
        # asks the student to commit to the belief that carbon does not
        # belong; the reference list simply presents it, marked, with the
        # reason. Inventing an anchor to fill the column would be the
        # dishonest version. Absence is legal under MRB-248.
        {"id": "MATL-03",
         "statement": "Carbon cannot belong in an order of metals.",
         "confronted_by": "s-series"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "A metal's <strong>reactivity</strong> is how readily it "
                 "takes part in a chemical reaction. Put the metals in order, "
                 "most reactive first, and you have the <strong>reactivity "
                 "series</strong>."},
        {"type": "explainer",
         "text": "The order is settled by evidence, and two tests do most of "
                 "the work: cold water, and dilute acid. A metal high in the "
                 "series manages both. One in the middle does nothing in "
                 "water but reacts with acid. One at the bottom does "
                 "neither."},

        # ── #s-series — THE REFERENCE BLOCK. No family, no wiring, and a rail
        # stop that mirrors the hook. `MATL-03` is confronted here, on the
        # card that carries carbon and says what earns it the place.
        {"type": "rule", "anchor": "s-series",
         "eyebrow": "Reference · keep this one open",
         "statement": "Most reactive at the top, least reactive at the "
                      "bottom",
         "cards": [
             {"term": "1 · Potassium (K)", "gloss": "stored under oil"},
             {"term": "2 · Sodium (Na)", "gloss": "stored under oil"},
             {"term": "3 · Calcium (Ca)", "gloss": "fizzes in cold water"},
             {"term": "4 · Magnesium (Mg)",
              "gloss": "barely touches cold water; fizzes in acid"},
             {"term": "5 · Aluminium (Al)",
              "gloss": "high in the order, but an oxide layer hides it"},
             {"term": "6 · Carbon (C)",
              "gloss": "not a metal — and it belongs here anyway, because it "
                       "takes oxygen from the oxides of everything below it"},
             {"term": "7 · Zinc (Zn)", "gloss": "needs acid to get going"},
             {"term": "8 · Iron (Fe)", "gloss": "slow even in acid"},
             {"term": "9 · Lead (Pb)", "gloss": "barely reacts with acid"},
             {"term": "10 · Copper (Cu)",
              "gloss": "neither water nor acid touches it"},
             {"term": "11 · Silver (Ag)", "gloss": "used for contacts and "
                                                   "mirrors because it stays "
                                                   "as it is"},
             {"term": "12 · Gold (Au)",
              "gloss": "found in the ground as the metal itself"},
         ],
         "close": "Nobody was told this order. It was assembled by doing what "
                  "you are about to do — putting metals into the same liquids "
                  "and recording what happened. The bench below covers six of "
                  "these twelve; the same method extended down the list "
                  "produces the rest of it. <strong>Carbon is in the list "
                  "because it can take oxygen away from the oxides of every "
                  "metal below it</strong>, which is how those metals are got "
                  "out of the ground."},

        # ── #s-bench — twelve tubes. Light `ks3-block` → `check`.
        {"type": "reaction-audit", "id": "bench-twelve", "anchor": "s-bench",
         "eyebrow": "Your turn · twelve tubes",
         "heading": "Six metals, two liquids. Say what will happen, then "
                    "look.",
         "demand": "predict",
         "resting": "Pick a tube.",
         "resting_mark": "?",
         "head_counter": {"format": "{n} of {total} read", "start": 0,
                          "total": 12},
         "predict_prompt": "Say it before you look.",
         "predict_options": [
             {"id": "yes",  "label": "Something happens"},
             {"id": "some", "label": "Almost nothing"},
             {"id": "no",   "label": "Nothing at all"},
         ],
         "verdict_yes": "It reacts.",
         "verdict_no": "Nothing worth watching.",
         "verdict_skipped": "This one is not done.",
         # ORDER IS DATA. The bands below are CHECKED against these cells.
         "order_claim": ["k", "ca", "mg", "zn", "fe", "cu"],
         "reagents": [
             {
                 "id": "water",
                 "label": "Cold water",
                 "phrase": "a beaker of cold water",
             },
             {
                 "id": "acid",
                 "label": "Dilute acid",
                 "phrase": "a test tube of dilute hydrochloric acid",
             },
         ],
         "bands": [
             {
                 "id": "water",
                 "label": "Fizzes in cold water",
                 "note": "Water alone is enough. Potassium and calcium are the top of the"
                          " series, and both have to be kept away from air and damp.",
             },
             {
                 "id": "acid",
                 "label": "Needs acid before much happens",
                 "note": "Cold water gives nothing worth watching; acid gets a real"
                          " reaction. Magnesium, zinc and iron are the middle of the series,"
                          " and the fizzing gets weaker the further down you go.",
             },
             {
                 "id": "neither",
                 "label": "Neither liquid touches it",
                 "note": "Nothing in water, nothing in acid. Copper is the bottom of the"
                          " series here — the kind of metal we leave outdoors, run water"
                          " through and make coins from.",
             },
         ],
         "metals": [
             {
                 "id": "k",
                 "name": "Potassium",
                 "rank": 0,
                 "band": "water",
                 "form": "A piece the size of a pea, freshly cut",
                 "water": {
                              "happens": True,
                              "vigour": "violent",
                              "obs": "It fizzes hard enough to skid across the surface, and the"
                                      " hydrogen it releases catches fire with a lilac flame.",
                              "eq": [
                                        "potassium + water",
                                        "potassium hydroxide + hydrogen",
                                    ],
                              "care": "Teacher demonstration only, behind a safety screen, with the"
                                       " smallest piece that can be cut.",
                          },
                 "acid": {
                             "skipped": True,
                             "obs": "This one is not done, at any concentration. Potassium is violent"
                                     " with water alone, and dilute acid is mostly water, so the"
                                     " reaction would be faster still. Potassium’s place at the top of"
                                     " the order is already settled by the water test — there is"
                                     " nothing left for the acid to tell you.",
                         },
             },
             {
                 "id": "ca",
                 "name": "Calcium",
                 "rank": 1,
                 "band": "water",
                 "form": "A small lump",
                 "water": {
                              "happens": True,
                              "vigour": "vigorous",
                              "obs": "Bubbles stream off the whole surface and the water turns cloudy"
                                      " white as calcium hydroxide forms.",
                              "eq": [
                                        "calcium + water",
                                        "calcium hydroxide + hydrogen",
                                    ],
                          },
                 "acid": {
                             "happens": True,
                             "vigour": "vigorous",
                             "obs": "It fizzes hard enough to warm the tube, and the bubbles come too"
                                     " fast to count.",
                             "eq": [
                                       "calcium + hydrochloric acid",
                                       "calcium chloride + hydrogen",
                                   ],
                         },
             },
             {
                 "id": "mg",
                 "name": "Magnesium",
                 "rank": 2,
                 "band": "acid",
                 "form": "A cleaned ribbon",
                 "water": {
                              "happens": False,
                              "obs": "Almost nothing. After several minutes a few tiny bubbles cling"
                                      " to the ribbon — the reaction is real but far too slow to watch.",
                          },
                 "acid": {
                             "happens": True,
                             "vigour": "vigorous",
                             "obs": "A fast stream of bubbles, the tube becomes warm to hold, and the"
                                     " ribbon disappears.",
                             "eq": [
                                       "magnesium + hydrochloric acid",
                                       "magnesium chloride + hydrogen",
                                   ],
                         },
             },
             {
                 "id": "zn",
                 "name": "Zinc",
                 "rank": 3,
                 "band": "acid",
                 "form": "A few granules",
                 "water": {
                              "happens": False,
                              "obs": "Nothing. The granules sit on the bottom unchanged for as long as"
                                      " you care to watch.",
                          },
                 "acid": {
                             "happens": True,
                             "vigour": "steady",
                             "obs": "A steady stream of small bubbles from every granule.",
                             "eq": [
                                       "zinc + hydrochloric acid",
                                       "zinc chloride + hydrogen",
                                   ],
                         },
             },
             {
                 "id": "fe",
                 "name": "Iron",
                 "rank": 4,
                 "band": "acid",
                 "form": "Iron filings",
                 "water": {
                              "happens": False,
                              "obs": "Nothing you can see. Left damp for days it rusts — but that is a"
                                      " slow reaction with water and air together, not with water alone.",
                          },
                 "acid": {
                             "happens": True,
                             "vigour": "slow",
                             "obs": "Sparse bubbles that take a while to get going, and the tube"
                                     " barely warms.",
                             "eq": [
                                       "iron + hydrochloric acid",
                                       "iron chloride + hydrogen",
                                   ],
                         },
             },
             {
                 "id": "cu",
                 "name": "Copper",
                 "rank": 5,
                 "band": "neither",
                 "form": "A coil of wire",
                 "water": {
                              "happens": False,
                              "obs": "Nothing. Copper carries cold water in houses for fifty years and"
                                      " comes out the same colour.",
                          },
                 "acid": {
                             "happens": False,
                             "obs": "Nothing. No bubbles, no warming, no change in the acid — and no"
                                     " amount of waiting will start it.",
                         },
             },
         ],
         "close_id": "bench-close",
         "close_title": "Twelve tubes, three answers.",
         "close": [
             "Nothing on this bench sorted the metals by how hard or how "
             "heavy they were. Magnesium bends between your fingers and beats "
             "iron; copper is soft and beats nothing. <strong>Reactivity is "
             "its own property</strong>, and the only way to find it is to "
             "put metals into the same liquid and watch.",
             "Read the three bands as one list and they give an order: "
             "potassium, calcium, magnesium, zinc, iron, copper. The same "
             "method run down the rest of the list produces the whole series.",
         ]},

        {"type": "key-fact", "ref": "one-order-fixed-by-evidence"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Reactivity", "Reactivity series", "Dilute acid",
                   "Hydrogen", "Evidence"]},

        {"type": "misconception", "id": "think-commit-water",
         "anchor": "s-think", "targets": "MATL-01"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    # ⊖ NO FIGURES, DELIBERATELY (NOTES-C9 §8, audit law 8). Every diagram
    # this unit could want would be a worse copy of an instrument already on
    # the page: a reactivity ladder duplicates the reference list above, and
    # a test-tube diagram duplicates the bench. Design offers a composite
    # cross-section for c9-04 as the one arguable candidate; it is not
    # declared, and the offer is recorded there rather than taken here.
    "figures": [],

    "activities": [
        {"id": "think-commit-water",
         "kind": "predict",
         "demand": "explain",
         "targets": "MATL-01",
         "prompt": "One test, one result, one conclusion. Commit before you "
                   "read on.",
         # ⚑ MRB-177 — distractors at the answer's own length: 15, 16, 14, 15.
         "options": [
             "Right — a metal that ignores cold water has shown you it is "
             "unreactive",
             "Wrong — zinc does nothing in water and fizzes steadily in "
             "dilute acid",
             "Right, because cold water is the test that settles where a "
             "metal belongs",
             "Wrong — zinc is at the very top of the series and reacts with "
             "everything",
         ],
         "reveal": [
             "Zinc did nothing <strong>in cold water</strong>. In dilute acid "
             "the same granules fizz steadily, and zinc will pull the oxygen "
             "off copper oxide if you heat the two together. Unreactive is "
             "not a word you can earn from one liquid.",
             "This is why the series needs more than one test. Water "
             "separates the top of the list; acid separates the middle; the "
             "bottom three ignore both and have to be sorted by other "
             "reactions altogether. <strong>“Nothing happened” tells "
             "you where a metal is not, and that is still evidence.</strong>",
         ]},
    ],

    "key_facts": [
        {"id": "one-order-fixed-by-evidence", "placement": "top-level",
         "ground": "card", "eyebrow": "Key fact",
         "text": "The reactivity series is the metals in order of how readily "
                 "they react. It is one order, fixed by evidence, and it "
                 "predicts every reaction they take part in — not just the "
                 "test that established it."},
    ],

    "ladder": {
        # index 0 — Design's own.
        "recall": {
            "q": "Which of these lists the six metals from the bench in "
                 "order, most reactive first?",
            "options": [
                "Potassium, calcium, magnesium, zinc, iron, copper",
                "Copper, iron, zinc, magnesium, calcium, potassium",
                "Potassium, magnesium, calcium, iron, zinc, copper",
                "Iron, copper, zinc, magnesium, calcium, potassium",
            ],
            "answer": 0,
            "feedback": {
                1: "That is the order upside down — least reactive first.",
                2: "Calcium reacts with cold water and magnesium barely "
                   "does, so calcium is above it, not below.",
                3: "Iron and copper are the bottom two of these six, not the "
                   "top two.",
            }},

        # index 1 — moved from Design's 0. `MATL-02` at the ladder.
        "apply": {
            "q": "A steel bicycle frame holds up a rider. A strip of "
                 "magnesium bends between your fingers. Which is the more "
                 "reactive metal?",
            "options": [
                "Steel, because a metal that holds its shape holds its atoms "
                "more tightly and so reacts more",
                "Magnesium, because reactivity is how readily a metal reacts "
                "and strength is a separate property",
                "Steel, because the harder a metal is the higher it sits in "
                "the reactivity series",
                "Neither, because strength and reactivity are the same "
                "property measured two ways",
            ],
            "answer": 1,
            "feedback": {
                0: "Holding a shape and holding on to atoms are different "
                   "things. Magnesium fizzes in acid; iron barely does.",
                2: "Hardness has no place in the series. Sodium is soft "
                   "enough to cut and sits near the top of it.",
                3: "They are two different properties. A metal can be strong "
                   "and unreactive, like steel, or weak and reactive, like "
                   "sodium.",
            }},

        "explain": {
            "q": "Zinc granules sit unchanged in a beaker of cold water. "
                 "Explain why this does not show that zinc is unreactive, and "
                 "describe one test that would place zinc properly.",
            "field_label": "Your explanation",
            "placeholder": "Doing nothing in water shows…",
            "success": [
                "Says doing nothing in cold water only rules out the top of "
                "the series.",
                "Says zinc reacts with dilute acid, giving hydrogen.",
                "Says a metal has to be tested against more than one thing.",
                "Describes adding zinc to dilute acid and looking for "
                "bubbles.",
                "Says the result places zinc below the metals that react with "
                "water and above those that react with neither.",
            ]},

        "produce": {
            "q": "You are given an unknown metal M. It does not react with "
                 "cold water, it fizzes gently in dilute acid, and it is "
                 "displaced from its sulfate by zinc. Say where M sits in the "
                 "series and justify each part of your answer.",
            "field_label": "Your answer",
            "placeholder": "M must be below…",
            "success": [
                "Says M is below the metals that react with cold water.",
                "Says M is above the metals that react with neither liquid.",
                "Places M below zinc, because zinc displaces it.",
                "Says the acid test and the displacement test agree with each "
                "other.",
                "Names a position consistent with all three results, such as "
                "between iron and copper.",
            ]},
    },

    "key_note": "The reactivity series runs potassium, sodium, calcium, "
                "magnesium, aluminium, carbon, zinc, iron, lead, copper, "
                "silver, gold. Potassium, sodium and calcium react with cold "
                "water. Magnesium, zinc and iron need dilute acid before much "
                "happens. Copper, silver and gold react with neither. Carbon "
                "is a non-metal placed in the same order, below aluminium and "
                "above zinc, because that is where its power to take oxygen "
                "from a metal oxide puts it.",

    "stretch": [
        {"type": "explainer", "id": "storage-is-a-clue",
         "text": "Potassium and sodium are kept in jars under oil, and the "
                 "oil is doing something specific: it keeps air and water "
                 "vapour off the surface. Left out on a bench, a cut piece of "
                 "sodium goes dull within seconds as it reacts with the air. "
                 "A bottle of copper turnings needs no oil at all. How a "
                 "substance has to be <strong>stored</strong> is a clue to "
                 "where it sits in the series."},
        {"type": "explainer", "id": "aluminium-is-awkward",
         "text": "Aluminium is the awkward one. Its position is high — just "
                 "below magnesium — but a saucepan made of it can be filled "
                 "with cold water and boiled with nothing happening at all. "
                 "The moment aluminium meets air it grows a tough, invisible "
                 "layer of aluminium oxide, and the water never reaches the "
                 "metal underneath. The position is about the element; the "
                 "everyday behaviour is about the coating. This is worth "
                 "remembering, because it is the reason aluminium is used for "
                 "things that get wet."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "Reactivity",
         "definition": "How readily an element takes part in a chemical "
                       "reaction.",
         "note": "A property of the element, like a melting point."},
        {"term": "Reactivity series",
         "definition": "The metals, and carbon, listed in order of "
                       "reactivity with the most reactive at the top.",
         "note": "One order, and it predicts every reaction they take part "
                 "in."},
        {"term": "Dilute acid",
         "definition": "An acid with a lot of water in it — the second test "
                       "used to place a metal in the series.",
         "note": "It separates the middle of the list, where water gives "
                 "nothing."},
        {"term": "Hydrogen",
         "definition": "The gas given off when a metal reacts with water or "
                       "with an acid. It pops with a lit splint.",
         "note": "The same gas from both tests, which is a clue in itself."},
        {"term": "Evidence",
         "definition": "What you actually observed, including observing that "
                       "nothing happened.",
         "note": "“Nothing happened” tells you where a metal is "
                 "not."},
    ],

    "safety_note": "This bench is a simulation of a demonstration and is not "
                   "a method. Potassium and calcium in water, and the four "
                   "metals in dilute hydrochloric acid, all need a written "
                   "risk assessment before anything is run in a room. "
                   "Potassium is a teacher demonstration only, behind a "
                   "screen, with the smallest piece that can be cut — and it "
                   "is never put into acid at any concentration.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why “nothing happened” counts "
                      "as evidence?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Reactivity explained as how readily a metal atom loses "
                   "electrons, oxidation and reduction written as half "
                   "equations, and the series extended to include hydrogen so "
                   "that reactions with acid can be ordered too.",

    "ws": ["analysis-and-evaluation", "experimental-skills-and-investigations"],
    "review_state": "draft",
}
