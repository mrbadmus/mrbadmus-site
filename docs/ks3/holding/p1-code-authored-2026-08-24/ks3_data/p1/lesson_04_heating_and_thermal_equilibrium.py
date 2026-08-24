"""P1 L4 — Heating and thermal equilibrium (MODEL).

The first of four lessons on one mechanism. This one establishes what drives a
thermal transfer and what stops it; p1-05 and p1-06 give it two routes, and
p1-07 slows it down on purpose.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**A temperature DIFFERENCE is the only thing that drives it, and running it is
what destroys it.** That is `KS3.P.ECT.02a` in one sentence and it is the
whole lesson. Energy goes from the hotter to the cooler, which narrows the
gap, which slows the transfer, which is why everything settles and stops
rather than overshooting. A student who has this can answer half of KS4
thermal physics without being taught it again.

**Cold is not a thing and does not move.** `ENER-12` is the misconception and
it is nearly universal, because every everyday phrase encourages it — *let the
cold in*, *the cold got to me*, *keep the cold out*. There is no such
substance. A cold object is one whose thermal store holds less, and putting it
against a warm one makes the warm one's store empty into it. The fridge does
not push cold into the milk; it pulls energy out of the milk and dumps it
behind the fridge, which is why the back of a fridge is warm.

── ⚖️ THE COMPARATIVE LABEL IS COMPUTED, NOT AUTHORED ──────────────────

`#s-equil`'s readout says which block is the hotter one. That sentence is
DERIVED from the two temperatures at every one of the thirty-six states the
bench can reach, and it is never authored beside them. MRB-257 §5A.1 is the
reason and the alveoli tiles are the precedent: two authored strings that say
"more here / less here" ship a false statement the moment the two values are
equal, and equal is exactly where this bench ENDS.

So the derivation has three branches and the third is the one the lesson is
about:

    hotter on the left   ->  energy goes left to right
    hotter on the right  ->  energy goes right to left
    the same            ->  nothing goes either way, and it has stopped

⚠️ **The `same` branch is reachable in two different ways and both are driven
in review**: by running any pair to the end, and from the FIRST FRAME of the
fourth pair, which starts at 40 and 40 and never moves. A bench whose equal
state is only reachable after eight steps of a slider is a bench whose equal
state nobody tested.

── The model behind the numbers ────────────────────────────────────────

Two identical blocks, so the final temperature is the plain mean of the two
starting temperatures — no specific heat capacity, which is KS4 and is not
needed here. Each step closes 60% of the remaining gap, so the approach is
fast at first and slow at the end, which is what a real cooling curve does and
what the lesson's own argument predicts. The widest pair runs 60.0, 24.0, 9.6,
3.8, 1.6, 0.6, 0.2, 0.0, 0.0 — and it has to reach 0.0 before the last frame,
because a bench that still shows a difference when the run ends contradicts
the sentence underneath it.

Every one of the thirty-six states is computed ONCE, in `ks3_art/p1.py`, and
emitted into the document. Nothing is computed in the browser, so nothing can
disagree with the sentence beside it.
"""

LESSON = {
    "slug":        "heating-and-thermal-equilibrium",
    "title":       "Heating and thermal equilibrium",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "MODEL",

    # `KS3.P.ECT.02` is clause-split four ways across p1-04 to p1-07; clause
    # `a` is the driver and the settling. The mint is in
    # `ks3_data/substatements.py`.
    "covers":      ["KS3.P.ECT.02a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["conservation-of-energy"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "A temperature difference drives a thermal transfer, and "
                        "the transfer closes the difference. There is no such thing "
                        "as cold moving anywhere.",

    "big_question": "Leave a hot drink and a cold drink on the same table "
                    "overnight. In the morning they are the same temperature "
                    "— and it is the temperature of the table.",

    # FOUR stops. The bench carries the whole middle of the lesson and asks
    # four separate commitments inside it.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two drinks, one temperature", "done_when": "committed"},
        {"anchor": "s-equil",  "short": "SETTLE",
         "label": "Four pairs, run to the end",
         "done_when": "all_pairs_settled"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "What a fridge actually does", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A cup of tea and a glass of squash, left out overnight.",
        "prompt": "The tea starts at 80 degrees and the squash at 5. Nobody "
                  "touches either of them. By morning they are both at 19 "
                  "degrees, which is what the room is at.",
        "commit": "Why did they both stop at 19, rather than one of them "
                  "carrying on?",
        "options": [
            "Because 19 degrees is the natural temperature of liquids",
            "Because the room had nothing left to give the squash",
            "Because once nothing is hotter than anything else, there is "
            "nothing to drive a transfer",
            "Because the cold in the squash was used up by the room",
        ],
        "reveal": "Because a transfer needs a difference, and by morning "
                  "there was none. The tea was hotter than the room, so it "
                  "emptied into the room. The squash was cooler than the "
                  "room, so the room emptied into it. Both of those close the "
                  "gap, and when the gap is gone the transfer has nothing "
                  "left to run on.",
    },

    "misconceptions": [
        {"id": "ENER-12",
         "statement": "Cold moves into a warm object and cools it down.",
         "elicited_by": "think-commit-fridge",
         "confronted_by": "think-commit-fridge"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Put two things at different temperatures together and "
                 "energy moves from the hotter one to the cooler one. It "
                 "never goes the other way on its own. And every joule that "
                 "moves cools the hotter one and warms the cooler one, so "
                 "the transfer is steadily destroying the very difference "
                 "that is driving it."},

        {"type": "rule", "id": "the-driver",
         "eyebrow": "What settles it",
         "statement": "A temperature difference drives the transfer. The "
                      "transfer closes the difference. Then it stops.",
         "close": "Nothing overshoots and nothing swaps back. Two objects "
                  "left together end up at the same temperature and stay "
                  "there — which is what <strong>thermal equilibrium</strong> "
                  "means."},

        # #s-equil — the flagship. Ink-dark practical.
        {"type": "equilibrium-bench", "id": "two-blocks", "anchor": "s-equil",
         "eyebrow": "At the bench · two identical metal blocks",
         "heading": "Push them together and watch the gap close",
         "head_counter": {"format": "{n} of 4 pairs settled", "total": 4},
         "demand": "investigate",
         "targets": "ENER-12",
         "prompt": "Pick a pair of starting temperatures, then drag the time "
                   "control from the start to the end. Read the gap as you "
                   "go.",
         "gate": {"prompt": "Commit first. Two identical blocks at 80 and 20 "
                            "degrees are pushed together and left. What do "
                            "they end up at?",
                  "options": ["Both at 20, the cooler one",
                              "Both at 50, halfway",
                              "Both at 80, the hotter one",
                              "The hot one at 50 and the cold one at 30"]},
         "block_labels": {"left": "Block A", "right": "Block B"},
         "labels": {"gap": "The gap between them",
                    "time": "Time",
                    "settled": "Settled",
                    "unit": "°C"},
         "time_steps": 8,
         "time_unit": "min",
         # ⚖️ IDENTICAL BLOCKS, SO THE END IS THE PLAIN MEAN. Specific heat
         # capacity is KS4 and is not needed to make this point; unequal
         # blocks would need it and would put a number on the page that
         # nothing here can justify.
         "pairs": [
             {"id": "wide", "label": "80 and 20", "left": 80, "right": 20,
              "note": "The widest gap, and the fastest start. Sixty degrees "
                      "apart at the beginning, and most of that closes in "
                      "the first two minutes."},
             {"id": "narrow", "label": "70 and 30", "left": 70, "right": 30,
              "note": "The same finish, from a gap two thirds the size. "
                      "It settles at 50 as well, because 50 is the middle of "
                      "70 and 30 just as it is the middle of 80 and 20."},
             {"id": "cool", "label": "45 and 15", "left": 45, "right": 15,
              "note": "Neither block is hot, and it makes no difference. "
                      "What drives the transfer is the DIFFERENCE between "
                      "them, not how hot either one is."},
             {"id": "equal", "label": "40 and 40", "left": 40, "right": 40,
              "note": "No gap, so nothing happens. Run the clock as long as "
                      "you like: neither block gets hotter and neither gets "
                      "cooler, because there is nothing to drive a transfer "
                      "in either direction."},
         ],
         "close": [
             "Four pairs. Three of them settle, and the fourth was settled "
             "before it started.",
             "Every pair ends in the middle, and every pair slows down as it "
             "gets there. Those two facts are the same fact: the transfer "
             "runs on the gap, and it spends the gap as it runs.",
         ]},

        {"type": "key-fact", "ref": "difference-drives-it"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Temperature", "Thermal equilibrium", "Heating",
                   "Temperature difference"]},

        {"type": "misconception", "id": "think-commit-fridge",
         "anchor": "s-think", "targets": "ENER-12"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "difference-drives-it",
         "text": "Energy moves from the hotter object to the cooler one, "
                 "never the other way on its own. The bigger the temperature "
                 "difference, the faster it moves — and moving closes the "
                 "difference, so it always slows down and stops.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Temperature",
         "definition": "How hot something is, measured in degrees Celsius.",
         "note": "Not the same as how much energy it holds. A lit match is "
                 "hotter than a bath and holds far less."},
        {"term": "Thermal equilibrium",
         "definition": "The state two objects reach when they are at the "
                       "same temperature and no energy is going either way.",
         "note": "Everything left together long enough ends up here."},
        {"term": "Heating",
         "definition": "Energy moving from a hotter thing to a cooler thing "
                       "because of the temperature difference between them.",
         "note": "One of the four pathways. It is something that happens, "
                 "never something a thing holds."},
        {"term": "Temperature difference",
         "definition": "The gap between two temperatures. It is what drives "
                       "a thermal transfer.",
         "note": "No gap, no transfer — whatever the two temperatures "
                 "actually are."},
    ],

    "activities": [
        {"id": "think-commit-fridge",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-12",
         "prompt": "You put a warm bottle of milk into a fridge and an hour "
                   "later it is cold. Commit before you read on.",
         "options": [
             "The fridge pushed cold into the milk until it was full of it",
             "The cold air in the fridge moved into the bottle and replaced "
             "the warmth",
             "The fridge took energy out of the milk and moved it outside "
             "the fridge",
             "The milk gave up its cold to the fridge and became cold itself",
         ],
         "reveal": [
             "There is no such thing as cold, so nothing can move into the "
             "milk. Cold is simply the word for a thermal store with less in "
             "it. The milk's store emptied into the cold air around it, "
             "because the milk was the hotter of the two, which is the only "
             "direction a thermal transfer ever runs.",
             "The fridge's job is then to get that energy out of the fridge "
             "altogether, and it does — put your hand behind a working "
             "fridge and the pipes there are <strong>warm</strong>. That "
             "warmth is your milk. A fridge is a machine for moving energy "
             "from a cool place to a warm one, which is exactly the thing "
             "that never happens on its own, and is exactly why a fridge "
             "needs plugging in.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "Two objects are placed in contact. In which direction does "
                 "energy move?",
            "options": [
                "From the larger object to the smaller one",
                "From the one holding more energy to the one holding less",
                "In both directions equally, until one runs out",
                "From the hotter object to the cooler one",
            ],
            "answer": 3,
            "feedback": {
                0: "Size does not decide it. A small hot thing heats a large "
                   "cool one.",
                1: "Careful — a bath holds far more energy than a match, and "
                   "a lit match still heats the bath. Temperature decides "
                   "the direction, not the amount stored.",
                2: "Nothing ever runs out. The transfer stops when the "
                   "temperatures are equal, with both objects still holding "
                   "plenty.",
            }},
        "apply": {
            "q": "A metal block at 90 °C is placed against an identical block "
                 "at 30 °C. Ten minutes later they are both at 60 °C. What "
                 "would happen if you now left them for another ten minutes?",
            "options": [
                "The hot one would go on cooling and the cool one on warming",
                "Nothing would change, because there is no longer a "
                "difference",
                "They would slowly swap back towards 90 and 30",
                "Both would drift down together towards zero",
            ],
            "answer": 1,
            "feedback": {
                0: "They are at the same temperature now. There is no "
                   "difference left to drive a transfer in either direction.",
                2: "That would need energy to move from a cooler place to a "
                   "warmer one on its own, which never happens.",
                3: "Only if the room were colder — and the question is about "
                   "the two blocks. Between them, nothing more will happen.",
            }},
        "explain": {
            "q": "A cup of coffee cools fastest in the first few minutes and "
                 "much more slowly after that, even though the room "
                 "temperature never changes. Explain why, using the idea of "
                 "a temperature difference.",
            "field_label": "Your explanation",
            "placeholder": "At the start the coffee is…",
            "success": [
                "Says the rate of transfer depends on the size of the "
                "temperature difference.",
                "Says the difference is biggest at the start, so the "
                "transfer is fastest then.",
                "Says the coffee cooling reduces the difference.",
                "Says a smaller difference means a slower transfer.",
                "Says it never quite stops until the coffee reaches room "
                "temperature.",
            ]},
        "produce": {
            # ⚠️ NO MARKUP IN A RUNG QUESTION — see p1-03's explain rung.
            "q": "A student claims that a duvet works by keeping cold out. "
                 "Write a short reply that corrects them without once using "
                 "the word cold as a noun, and then describe an experiment "
                 "that would settle it.",
            "field_label": "Your reply, then your experiment",
            "placeholder": "Nothing is being kept out, because…",
            "success": [
                "Says there is no such thing as cold moving anywhere.",
                "Says the duvet slows energy leaving the person's thermal "
                "store.",
                "Avoids using cold as a substance throughout.",
                "Proposes wrapping something WARM and something COLD in "
                "identical duvets.",
                "Predicts that the cold object also stays cold longer, which "
                "a keeps-cold-out explanation cannot account for.",
            ]},
    },

    "key_note": "Energy moves from hotter to cooler, and only in that "
                "direction on its own. The bigger the temperature difference, "
                "the faster it moves; and because moving closes the "
                "difference, everything slows down and settles at one "
                "temperature. There is no such thing as cold moving anywhere.",

    "stretch": [
        {"type": "explainer", "id": "temperature-is-not-energy",
         "text": "Temperature and energy are not the same thing, and the "
                 "sparkler proves it. A sparkler burns at about 1500 degrees "
                 "and the sparks land on your hand without hurting, because "
                 "each spark is a speck of metal weighing almost nothing and "
                 "carries almost no energy with it. A bath at 40 degrees is "
                 "far cooler and holds thousands of times more. Temperature "
                 "tells you how hard the particles are moving; the total "
                 "energy also depends on how many of them there are."},
    ],

    "support": [],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why everything settles at the same "
                      "temperature?",
              "cta": "Ask about this lesson",
              "anchor": "s-equil"},

    "ks4_becomes": "Specific heat capacity, rate of cooling, and thermal "
                   "equilibrium used quantitatively.",

    "ws": ["measurement", "analysis-and-evaluation"],

    "review_state": "draft",
}
