"""P2 L5 — Fuels and energy resources (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p2/p2-05-fuels-and-energy-resources.dc.html`.

── ⚖️ RULED · THE TWO "IMPOSSIBLE" CORNERS STAY OCCUPIED ───────────────

Design's science flag 15 flags this deliberately and asks for Mide's eye:
**nuclear is placed as non-renewable and low-carbon; wood is placed as
renewable and high-carbon.** Both stay, unsoftened, and the ruling is not a
political one — it is structural.

The belief this lesson kills is that "renewable" and "clean" are one
question. The only evidence that can kill it is a resource in each of the
two cells the belief says must be empty. Soften either and the grid has an
empty corner, the misconception survives the lesson, and Rung 2 — which
asks directly for the non-renewable low-carbon resource — has no
answer. Both placements are also simply correct: burning biomass releases
carbon dioxide and particulates, and a generating nuclear station emits
essentially none.

The page does not claim either is *best*. It refuses to name a best
resource at all, and its `#s-think` says anyone who does "has stopped
counting axes early".

── ⚖️ RULED · THE AXIS FIGURES ARE POSITIONS, NOT MEASUREMENTS ─────────

Design's flag 17: carbon, reliability and land are `0`–`1` for plotting
only. Kept, and the legal line says so. They carry an ORDERING, which is
the only claim the lesson makes with them, and an ordering is something a
relative position can honestly hold. Presenting them as data would be the
defect; presenting them as positions is not.

── ⚖️ MRB-204 · NO FORMULA FIGURE, AND THAT IS MEASURED ───────────────

`p2-05` has no calculable relationship at its centre, draws no triangle and
draws no beam. Design's `NOTES-P2.md` §4 says so and her drawing agrees
— the word "triangle" appears zero times on the page. This is the one
lesson in the unit where MRB-204 is satisfied by there being nothing to
apply it to, and that is a measurement rather than an omission.

── ⚠️ FOUR RAIL STOPS · `s-think` IS NOT ONE ─────────────────────────

    s-hook · s-sort · s-grid · s-ladder

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ───────────────

    #s-sort    `ks3-block`                    → `check`
    #s-grid    `ks3-block`                    → `check`
    #s-think   `ks3-block ks3-misconception`  → `misconception`

Both are BARE `ks3-block` — neither is dark, neither is a practical.
Not inferred from the family name.

── ⚖️ ONE MINT, AND ONE RE-USE ───────────────────────────────────────

`ENER-27` is the renewable/clean collapse, and it is Design's `ENERGY-14`.

The SECOND quote — "electricity is a clean energy resource" — mints
nothing. It is `ENER-10` ("light, sound and electricity are kinds of energy
that things store") doing work in a new situation: electricity is a
PATHWAY, not a store and not a resource, and the answer is the same
distinction `p1-01` drew and `p1-02` re-used. Following P1's own precedent,
a belief that is an established one wearing new clothes takes no new row.
"""

LESSON = {
    "slug":  "fuels-and-energy-resources",
    "title": "Fuels and energy resources",
    "discipline": "physics",
    "unit": "Energy at home",
    "family": "CLASSIFY",

    "covers": ["KS3.P.FUEL.05"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 13}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["reading-a-fuel-bill"],
    "assumes": [],
    "references": ["energy-stores"],
    "ks4_links": [],

    "meta_description": "Burning wood is renewable and smoky. A nuclear "
                        "station is non-renewable and emits almost no carbon "
                        "while generating. Both of those corners are "
                        "supposed to be empty — which is how you know "
                        "renewable and clean are two questions.",

    "big_question": "Burning wood releases carbon dioxide, soot and "
                    "particulates every time. A nuclear power station "
                    "releases no carbon dioxide at all while generating. "
                    "Wood grows back; uranium does not. So what does "
                    "“renewable” actually tell you?",

    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "Wood and uranium", "done_when": "committed"},
        {"anchor": "s-sort",  "short": "SORT",
         "label": "Will it run out",  "done_when": "all_eight_sorted"},
        {"anchor": "s-grid",  "short": "GRID",
         "label": "Two-axis grid",    "done_when": "all_three_axes_seen"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Renewable and dirty. Non-renewable and clean.",
        "prompt": "Burning wood releases carbon dioxide, soot and "
                  "particulates every time. A nuclear power station releases "
                  "no carbon dioxide at all while generating. Wood grows "
                  "back; uranium does not.",
        "commit": "Commit. What does that tell you about the word "
                  "“renewable”?",
        "options": [
            "Nothing — wood must be cleaner than it looks",
            "Renewable answers whether it runs out, and nothing else",
            "Nuclear must secretly be renewable",
            "The word renewable is meaningless",
        ],
        "answer": 1,
        "reveal": "It answers one question and one only: <strong>will it run "
                  "out?</strong> It says nothing about carbon, nothing about "
                  "pollution, nothing about safety, and nothing about cost. "
                  "Two independent questions get collapsed into one word, "
                  "and that is the mistake this whole lesson is built to "
                  "take apart.",
    },

    "misconceptions": [
        {"id": "ENER-27",
         "statement": "Renewable means clean, and non-renewable means "
                      "polluting.",
         "elicited_by": "s-hook",
         "confronted_by": "two-axis-grid"},
        # ⚖️ RE-USED, NOT MINTED. See the note at the top of this file.
        {"id": "ENER-10",
         "statement": "Light, sound and electricity are kinds of energy that "
                      "things store.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Almost every resource below traces back to the Sun, and "
                 "almost every one is a chemical or nuclear store being "
                 "emptied into a pathway. What differs is whether the store "
                 "refills on a human timescale, and what else comes out "
                 "while you use it. <strong>Those are two axes, not "
                 "one.</strong>"},

        # ── #s-sort · one question at a time ───────────────────────────
        {"type": "renewable-sort",
         "id": "renewable-sort",
         "anchor": "s-sort",
         "eyebrow": "First pass · one question at a time",
         "heading": "Will it run out?",
         "prompt": "Sort each resource on that question alone. Do not think "
                   "about pollution yet — that is deliberately a "
                   "separate step.",
         "renew_label": "Renewable",
         "finite_label": "Finite",
         # ⚠️ `sort_items`, never `cards`.
         "sort_items": [
             {"id": "coal", "text": "Coal", "renewable": False,
              "store": "Chemical store, 300 million years old",
              "note": "Will run out, and it is the highest-carbon option on "
                      "the grid. The easy case — both answers point the "
                      "same way, which is why people generalise from it."},
             {"id": "gas", "text": "Natural gas", "renewable": False,
              "store": "Chemical store, fossil",
              "note": "Finite and carbon-emitting, but around half the "
                      "carbon of coal per unit and easy to switch on and "
                      "off. This is why it is used to cover the gaps left by "
                      "wind and solar."},
             {"id": "nuclear", "text": "Nuclear", "renewable": False,
              "store": "Nuclear store in uranium",
              "note": "Non-renewable and almost carbon-free while "
                      "generating. It sits in the corner that “renewable "
                      "means clean” says cannot exist — and its "
                      "real cost is waste that stays dangerous for thousands "
                      "of years."},
             {"id": "wood", "text": "Wood and biomass", "renewable": True,
              "store": "Chemical store, grown this decade",
              "note": "Renewable — you can plant more — and it "
                      "releases carbon dioxide, soot and particulates every "
                      "time it burns. The other corner that the "
                      "misconception says is impossible."},
             {"id": "wind", "text": "Wind", "renewable": True,
              "store": "Kinetic store in moving air",
              "note": "Renewable and very low carbon, and it cannot be "
                      "switched on when the air is still. Reliability is its "
                      "real cost, not pollution."},
             {"id": "solar", "text": "Solar", "renewable": True,
              "store": "Radiation from the Sun",
              "note": "Renewable and low carbon in use — though the "
                      "panels themselves take mining and manufacturing, "
                      "which is where its carbon figure comes from."},
             {"id": "hydro", "text": "Hydroelectric", "renewable": True,
              "store": "Gravitational store of raised water",
              "note": "Renewable, low carbon and reliable — and it "
                      "takes more land than anything else on the grid, "
                      "because it means flooding a valley."},
             {"id": "tidal", "text": "Tidal", "renewable": True,
              "store": "Gravitational store, the Moon",
              "note": "Renewable and predictable to the minute, unlike wind "
                      "— but only at certain times of day, and it "
                      "disrupts estuaries where a great deal lives."},
         ]},

        # ── #s-grid · the two-axis grid ────────────────────────────────
        {"type": "two-axis-grid",
         "id": "two-axis-grid",
         "anchor": "s-grid",
         "eyebrow": "Second pass · the two-axis grid",
         "heading": "Now add the second question.",
         "prompt": "Renewable across the bottom, the second question up the "
                   "side. If the two words meant the same thing, everything "
                   "would sit on a diagonal. Nothing does.",
         # ⚠️ MIRRORS `#s-sort`'s list, and `ks3_data/p2/__init__.py`
         # CROSS-CHECKS the two so they cannot drift: if the sort said wood
         # was renewable and the grid said it was not, the grid would still
         # draw and only a browser open on the page would show it.
         "resources": [
             {"id": "coal",    "label": "Coal",              "renewable": False},
             {"id": "gas",     "label": "Natural gas",       "renewable": False},
             {"id": "nuclear", "label": "Nuclear",           "renewable": False},
             {"id": "wood",    "label": "Wood and biomass",  "renewable": True},
             {"id": "wind",    "label": "Wind",              "renewable": True},
             {"id": "solar",   "label": "Solar",             "renewable": True},
             {"id": "hydro",   "label": "Hydroelectric",     "renewable": True},
             {"id": "tidal",   "label": "Tidal",             "renewable": True},
         ],
         # ⚖️ POSITIONS, NOT MEASUREMENTS. See the ruling at the top.
         "axes": [
             {"id": "carbon", "label": "Carbon while generating",
              "low": "Almost none", "high": "A lot",
              "values": {"coal": 1.0, "gas": 0.6, "nuclear": 0.05,
                         "wood": 0.75, "wind": 0.06, "solar": 0.08,
                         "hydro": 0.07, "tidal": 0.06},
              "note": "The two words come apart immediately. Nuclear is "
                      "non-renewable and sits at the bottom; wood is "
                      "renewable and sits near the top. If renewable meant "
                      "clean, both of those cells would be empty."},
             {"id": "reliable", "label": "Available on demand",
              "low": "Intermittent", "high": "Whenever needed",
              "values": {"coal": 1.0, "gas": 1.0, "nuclear": 1.0,
                         "wood": 0.9, "wind": 0.25, "solar": 0.3,
                         "hydro": 0.85, "tidal": 0.6},
              "note": "A different picture again. Coal, gas and nuclear are "
                      "available whenever you want them; wind and solar are "
                      "not, and no amount of wanting changes it. This is the "
                      "axis that decides what a country can actually run "
                      "on."},
             {"id": "land", "label": "Land and habitat taken",
              "low": "Little", "high": "A great deal",
              "values": {"coal": 0.5, "gas": 0.3, "nuclear": 0.2,
                         "wood": 0.9, "wind": 0.6, "solar": 0.7,
                         "hydro": 1.0, "tidal": 0.8},
              "note": "And a third ordering. Hydroelectric is renewable, "
                      "low-carbon, reliable — and floods a valley. "
                      "Nuclear takes the least land of anything here. Every "
                      "axis reshuffles the ranking."},
         ],
         "renew_axis_label": "Will it run out?",
         "alt": "A grid. Renewable or finite along the bottom, and a second "
                "question up the side. Nuclear sits low on carbon in the "
                "finite column; wood sits high on carbon in the renewable "
                "column. Neither corner is empty.",
         "close": "Three axes, three different rankings, and no resource "
                  "wins all three. That is the honest picture, and it is why "
                  "the lesson refuses to name a best one."},

        {"type": "key-fact", "id": "renewable-is-one-question"},

        # ── #s-think · NOT a rail stop ────────────────────────────────
        {"type": "misconception", "id": "think-renewable-means-clean",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        {"id": "think-renewable-means-clean",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-27",
         "statements": [
             {"quote": "Renewable means clean, and non-renewable means "
                       "polluting.",
              "targets": "ENER-27",
              "body": [
                  "Look at where the corners are occupied. Nuclear is "
                  "non-renewable and emits almost no carbon. Wood is "
                  "renewable and emits a great deal, along with particulates "
                  "that damage lungs. <strong>Both of those cells would have "
                  "to be empty if the two words meant the same "
                  "thing.</strong>",
                  "And there is no resource that wins on every axis. Anyone "
                  "who names a single best resource has stopped counting "
                  "axes early — carbon, availability on demand, land, "
                  "waste and cost do not agree with each other, and a "
                  "country choosing between them is choosing which cost to "
                  "accept rather than avoiding all of them.",
              ]},
             {"quote": "Electricity is a clean energy resource.",
              "targets": "ENER-10",
              "body": [
                  "Electricity is not a resource at all. It is a "
                  "<em>pathway</em> — a way of moving energy from "
                  "wherever it was generated to wherever it is wanted "
                  "— and it is exactly as clean as whatever filled the "
                  "store at the far end. The same electric car is close to "
                  "zero-carbon on Norwegian hydro and considerably worse "
                  "than a small diesel on a coal-heavy grid. "
                  "<strong>Nothing is stored as electricity, so nothing can "
                  "be resourced as electricity either.</strong>",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "renewable-is-one-question",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Renewable means the store refills on a human timescale. It "
                 "is a separate question from how much carbon, how much "
                 "pollution, or how reliable — and the answers do not "
                 "line up."},
    ],

    "ladder": {
        "recall": {
            "q": "What does it mean to call an energy resource renewable?",
            "options": [
                "The store refills on a human timescale, so it will not run "
                "out",
                "It comes from nature rather than from a fuel, so nothing is "
                "being consumed",
                "It produces no carbon dioxide, so it does not add to the "
                "greenhouse effect",
                "It is available whenever it is needed, so it never has to "
                "be stored",
            ],
            "answer": 0,
            "feedback": {
                1: "Wood is renewable and produces a great deal. The two "
                   "questions are separate.",
                2: "Burning biomass is renewable and releases carbon "
                   "dioxide.",
                3: "Wind and solar are renewable and both are intermittent.",
            }},
        "apply": {
            "q": "Which of these is non-renewable but releases almost no "
                 "carbon dioxide while generating?",
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": ["Natural gas", "Nuclear", "Wood",
                        "There is no such resource"],
            "answer": 1,
            "feedback": {
                0: "Non-renewable, yes — but it releases substantial "
                   "carbon dioxide.",
                2: "Wood is renewable, and it is one of the higher-carbon "
                   "options.",
                3: "Nuclear is exactly this, which is why the two words "
                   "cannot mean the same thing.",
            }},
        "explain": {
            "q": "Explain why renewable and clean are not the same thing, "
                 "using one renewable resource and one non-renewable "
                 "resource as evidence.",
            "field_label": "Your explanation",
            "placeholder": "Renewable describes whether the store refills…",
            "success": [
                "Defines renewable as the store refilling on a human "
                "timescale.",
                "Gives a renewable resource that pollutes — wood or "
                "biomass — and says what it releases.",
                "Gives a non-renewable resource that is low-carbon "
                "— nuclear.",
                "States clearly that the two questions are independent of "
                "each other.",
                "Names at least one further axis that also matters, such as "
                "reliability, land or waste.",
            ]},
        "produce": {
            "q": "A country wants to close all its gas power stations and "
                 "run entirely on wind and solar. Using the grid, give the "
                 "strongest argument in favour and the strongest practical "
                 "problem — then say what evidence would help decide.",
            "field_label": "Your answer",
            "placeholder": "In favour: wind and solar are renewable and "
                           "low-carbon…",
            "success": [
                "Argues in favour using both renewability and low carbon.",
                "Identifies intermittency as the practical problem, with "
                "reference to the reliability axis.",
                "Explains that demand does not fall when the wind drops, so "
                "something must cover the gap.",
                "Suggests a specific solution and its cost — storage, "
                "nuclear backup, or overbuilding capacity.",
                "Names evidence that would help decide, such as demand data "
                "against wind and sunshine records over a full year.",
            ]},
    },

    "key_note": "Renewable answers one question: does the store refill? "
                "Carbon, pollution, reliability, land and waste are separate "
                "questions with different answers. Nuclear is non-renewable "
                "and low-carbon; wood is renewable and smoky. Both corners "
                "are occupied.",

    "stretch": [
        {"id": "almost-everything-is-the-sun",
         "type": "explainer",
         "text": "Almost everything on the grid is the Sun, wearing a "
                 "disguise. Coal is a Carboniferous forest that "
                 "photosynthesised three hundred million years ago and never "
                 "fully rotted. Oil is ancient plankton. Wind exists because "
                 "sunlight heats some parts of the atmosphere more than "
                 "others. Hydroelectric power runs on water the Sun lifted "
                 "into the sky as vapour. Even the food in your own chemical "
                 "store traces back to a plant catching light. Only three "
                 "things on the list break the pattern: geothermal, which is "
                 "heat left over from the Earth's formation plus radioactive "
                 "decay in the mantle; tidal, which is the Moon's gravity; "
                 "and nuclear, which is energy locked into heavy atoms by "
                 "exploding stars long before the Sun existed. "
                 "<strong>Everything else is sunlight with a delay — "
                 "and the length of that delay is exactly what “renewable” "
                 "is measuring.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        {"term": "renewable",
         "definition": "The store refills on a human timescale, so it will "
                       "not run out. It is a claim about supply and about "
                       "nothing else."},
        {"term": "energy resource",
         "definition": "A store we can empty to do something useful. "
                       "Electricity is not one — it is a pathway."},
        {"term": "intermittent",
         "definition": "Available only sometimes, and not when you choose. "
                       "Wind and solar are; gas and nuclear are not."},
        {"term": "biomass",
         "definition": "Fuel grown recently — wood, crops, waste. "
                       "Renewable, and it still burns and still emits."},
    ],

    "tutor": {
        "anchor": "s-grid",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to argue about which resource is best?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Energy resources, the National Grid, and the evaluation "
                   "of competing generation methods.",

    "ws": ["analysis-and-evaluation"],
}
