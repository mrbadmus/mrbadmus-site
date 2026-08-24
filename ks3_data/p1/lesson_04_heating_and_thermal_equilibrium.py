"""p1-04 — *Heating and thermal equilibrium*.

Ported from Claude Design's `p1-04-heating-and-thermal-equilibrium.dc.html`.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.ECT.02a` — the first quarter of the compound heating bullet. The
bullet names thermal equilibrium, conduction, radiation and insulators, and
no scheme of work teaches those in one sitting, so it is split a/b/c/d
across `p1-04`–`p1-07`. This lesson owns the temperature-difference idea and
equilibrium; the three transfer routes are the lessons after it.

⚠️ **THE UNIT ASSUMES C1.** `PART-03` — the fixed-size reference particle —
is RE-CONFRONTED here rather than restated: the mechanism for heating is
particles moving faster and nothing else, and that is the claim `c1-02`
established. Design's own `#s-think` closes on it in those terms.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

`p1-01` took 0 and 2, `p1-02` took 1 and 3, `p1-03` took 0 and 2. This
lesson takes **1 and 3**. Her option text and every correction are verbatim;
only the button order moves.

── ⚠️ MRB-177 · HER `r2` IS MARGINAL AND IS LEFT ALONE ────────────────

Measured with `verify_ks3`'s own tokeniser and threshold, her apply rung runs
13w against a longest distractor of 12w — gap 1, ratio 1.08, well inside both
limbs. It passes as drawn and is NOT re-cut. Only the rungs that actually
trip the gate are touched; a marginal pass is not a defect and rewriting one
would be exactly the drift the ruling forbids.

── ⚑ MISCONCEPTIONS ───────────────────────────────────────────────────

Two mints and one re-confrontation, following her `NOTES-P1.md` §2:

    ENER-13  temperature and energy are the same quantity   (her ENERGY-05)
    ENER-14  cold is a substance that travels               (her ENERGY-06)
    PART-03  re-confronted, not restated                    (C1's mint)

── ⚖️ TWO OF HER SCIENCE FLAGS ARE LOAD-BEARING HERE ──────────────────

Flag 10: the thermal-store bar is LOGARITHMIC and says so on the face of it.
The spark-to-bath range is about 10^9 and a linear bar would show nothing at
the spark end. Kept, and the bench labels it.

Flag 11: the "no cold travels this way" arrow is DRAWN and then labelled as
not existing. Drawing the thing that does not happen is the confrontation of
`ENER-14`, and it must not be tidied away as a contradictory label.
"""

LESSON = {
    "slug":  "heating-and-thermal-equilibrium",
    "title": "Heating and thermal equilibrium",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "MODEL",

    "covers": ["KS3.P.ECT.02a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 4}],
    "typical_year": 7,
    "typical_minutes": 55,

    "requires": ["conservation-of-energy"],
    "assumes": ["solids-liquids-and-gases"],
    "references": [],
    "ks4_links": [],

    "meta_description": "A spark at 1500 °C lands on your hand and barely "
                        "stings; a bath at 40 °C can scald. Temperature and "
                        "energy are two different quantities — learn to "
                        "separate them, and which way heating goes.",

    "big_question": "A sparkler throws sparks at 1500 °C and they do not "
                    "hurt. A bath at 40 °C can injure a small child. Which "
                    "holds more energy, and why does the cooler one do more "
                    "damage?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Spark and bath",   "done_when": "committed"},
        {"anchor": "s-two",    "short": "TWO",
         "label": "Two quantities",   "done_when": "both_axes_moved"},
        {"anchor": "s-flow",   "short": "FLOW",
         "label": "One-way flow",     "done_when": "all_three_pairs_run"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "1500 degrees, and it does not hurt.",
        "prompt": "A sparkler throws out sparks at around 1500 °C — hot "
                  "enough to melt iron. They land on your hand and you feel "
                  "a pinprick. Meanwhile a bath at 40 °C, barely more than "
                  "body temperature, will make you flinch and can genuinely "
                  "injure a small child.",
        "commit": "Commit. Which holds more energy, and why does the cooler "
                  "one do more damage?",
        "options": [
            "The spark — it is far hotter, so it has more energy",
            "The bath — temperature is an average, and it has vastly more "
            "particles",
            "They hold the same energy, just spread differently",
            "The spark, but it cools too fast to hurt you",
        ],
        "reveal": "The bath, by an enormous margin — tens of millions of "
                  "joules against a fraction of one. <strong>Temperature "
                  "tells you how fast the particles are moving on "
                  "average. Energy depends on that and on how many "
                  "particles there are.</strong> A spark is a handful of "
                  "very fast particles; a bath is a hundred kilograms of "
                  "moderately fast ones. Two different quantities, and this "
                  "lesson is about never confusing them again.",
    },

    "misconceptions": [
        {"id": "ENER-13",
         "statement": "Temperature and energy are the same thing — if "
                      "something is hotter it must hold more energy.",
         "elicited_by": "s-hook",
         "confronted_by": "two-quantities"},
        {"id": "ENER-14",
         "statement": "Cold is a substance that travels — put ice in a "
                      "drink and the cold moves out of the ice into the "
                      "drink.",
         # ⚠️ Names the ACTIVITY, not the section anchor — MRB-244/248
         # resolve these against elements the page carries.
         "elicited_by": "think-cold-travels",
         "confronted_by": "one-way-flow"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "You already know from the particle unit that heating a "
                 "substance makes its particles move faster and does not "
                 "change the particles themselves. That claim comes back "
                 "here, and it comes back harder — because this time you "
                 "have to use it to separate two things that everyday "
                 "language treats as one word."},

        # ── #s-two — bare `ks3-block` → `check`.
        {"type": "two-quantities", "id": "two-quantities",
         "anchor": "s-two",
         "demand": "investigate",
         "targets": "ENER-13",
         "eyebrow": "Two quantities · move each one on its own",
         "heading": "Temperature is not the same as energy",
         "prompt": "Set how much there is, then set how fast its particles "
                   "are moving. Watch the two readouts move independently — "
                   "that is the whole point.",
         # ⚖️ Design's flag 10 — the thermal bar is LOGARITHMIC and says so.
         # The spark-to-bath range is about 10^9; a linear bar shows nothing.
         "scale_note": "The thermal-store bar is logarithmic — the range "
                       "from a spark to a bath is about 10^9, and a linear "
                       "bar would leave the spark invisible.",
         "amounts": [
             {"id": "spark", "label": "A spark", "n": 3,
              "tag": "a few particles"},
             {"id": "mug",   "label": "A mug",   "n": 22, "tag": "300 g"},
             {"id": "bath",  "label": "A bath",  "n": 60, "tag": "100 kg"},
         ],
         "speeds": [
             {"id": "slow", "label": "Slow",      "t": 20},
             {"id": "med",  "label": "Medium",    "t": 40},
             {"id": "fast", "label": "Very fast", "t": 1500},
         ],
         "readouts": [
             {"id": "temp",  "label": "Temperature"},
             {"id": "store", "label": "Thermal store", "accent": True},
         ],
         "close": "Temperature moved when you changed the speed and did "
                  "nothing when you changed the amount. The thermal store "
                  "moved for both. They are two different quantities, and "
                  "the spark is the proof: the fastest particles on the "
                  "bench, and almost no energy at all."},

        {"type": "key-fact", "id": "temperature-is-an-average",
         "ground": "card",
         "text": "Temperature is the average speed of the particles. The "
                 "energy in a thermal store depends on that <em>and</em> on "
                 "how many particles there are."},

        # ── #s-flow — `ks3-block ks3-dark ks3-practical` → `practical`.
        {"type": "one-way-flow", "id": "one-way-flow",
         "anchor": "s-flow",
         "demand": "investigate",
         "targets": "ENER-14",
         "eyebrow": "One-way flow · run each pair",
         "heading": "Energy goes one way, and stops when they match",
         "prompt": "Run each pair and watch the arrow. There is only ever "
                   "one, and it always points the same way.",
         # ⚖️ Design's flag 11 — the arrow that does NOT exist is drawn and
         # labelled as not existing. That IS the confrontation of ENER-14,
         # and it must not be tidied away as a contradictory label.
         "ghost_label": "no cold travels this way",
         "pairs": [
             {"id": "p1", "label": "Ice in a drink",
              "hot": 22, "cold": -4, "hot_name": "Drink", "cold_name": "Ice",
              "note": "Energy leaves the drink and enters the ice. One "
                      "arrow, pointing from the drink to the ice. Nothing "
                      "at all travels the other way — the drink gets colder "
                      "because it is losing, not because it is receiving."},
             {"id": "p2", "label": "Hot spoon in cold water",
              "hot": 90, "cold": 12, "hot_name": "Spoon",
              "cold_name": "Water",
              "note": "The spoon is much hotter but tiny, so it loses "
                      "temperature fast while the water barely warms. Same "
                      "one-way flow — and it stops when they match, not "
                      "when the spoon “runs out”."},
             # ⚠️ THE EQUAL STATE. Design draws it deliberately: two blocks
             # already at the same temperature, no net flow, nothing
             # happening. It is thermal equilibrium, and it is also the
             # C1 diffusion result in a new setting.
             {"id": "p3", "label": "Two blocks the same",
              "hot": 30, "cold": 30, "hot_name": "Block A",
              "cold_name": "Block B",
              "note": "Already at the same temperature, so there is no net "
                      "flow at all and nothing happens — this is thermal "
                      "equilibrium. Particles are still colliding and still "
                      "exchanging energy in both directions; the two flows "
                      "are simply equal. That is exactly the diffusion "
                      "result from C1, in a new setting."},
         ]},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        # A REFERENCE; the payload is in `activities[]`.
        {"type": "misconception", "id": "think-cold-travels",
         "anchor": "s-think", "targets": "ENER-14"},

        {"type": "key-fact", "id": "heating-is-one-way",
         "ground": "card",
         "text": "Heating is energy moving from a hotter object to a colder "
                 "one, and it only ever goes that way. It stops when the "
                 "two reach the same temperature — thermal equilibrium — "
                 "not when one has run out of heat."},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "activities": [
        {"id": "think-cold-travels",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-14",
         "statements": [
             {"targets": "ENER-14",
              "quote": "Put ice in your drink and the cold moves out of the "
                       "ice into the drink.",
              "body": [
                  "There is no such thing as cold. Cold is not a substance, "
                  "not a store, and not a thing that can travel — it is just "
                  "a smaller amount of the same thing. Energy moves out of "
                  "the drink and into the ice, in one direction only, and "
                  "the drink is left with less. Nothing entered it.",
                  "This matters more than it sounds. If cold were a "
                  "substance you would expect a fridge to make cold and pump "
                  "it in; instead a fridge takes energy out of the food and "
                  "dumps it into your kitchen, which is why the back of a "
                  "fridge is warm and why leaving the door open warms the "
                  "room rather than cooling it. Watch the flow bench again: "
                  "there is only ever one arrow, and it always points the "
                  "same way.",
                  "And note what has not changed in either object: the "
                  "particles are the same size and the same particles "
                  "throughout. Heating and cooling change how fast they move "
                  "and nothing else — exactly as the particle model said, "
                  "now doing work in a new situation.",
              ]},
             {"quote": "A bath is hotter than a cup of tea, because there is "
                       "far more heat in it.",
              "body": [
                  "Two different quantities are being run together. "
                  "Temperature says how vigorously the particles are moving; "
                  "the energy in the thermal store also depends on how many "
                  "particles there are. A bath at 40 °C holds far more "
                  "energy than a cup at 80 °C, and yet the tea is hotter — "
                  "and it is the temperature, not the total energy, that "
                  "decides which way the heating goes when you put one in "
                  "the other.",
              ]},
         ]},
    ],

    "figures": [],
    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "Energy in a thermal store always flows from…",
            # MRB-278: correct at index 1.
            "options": [
                "colder to hotter",
                "hotter to colder",
                "bigger to smaller",
                "whichever has more energy to whichever has less",
            ],
            "answer": 1,
            "feedback": {
                0: "This never happens on its own. A fridge appears to do "
                   "it, but only by using energy to force it.",
                2: "Size does not set the direction. A tiny hot spark heats "
                   "a big cold room, not the reverse.",
                3: "Careful — a bath at 40 °C has more energy than a spark "
                   "at 1500 °C, and the spark still heats the bath.",
            }},
        "apply": {
            "q": "A mug of tea and a swimming pool are both at 30 °C. Which "
                 "statement is correct?",
            # MRB-278: correct at index 3.
            # MRB-177: 13w against 12w — gap 1, ratio 1.08. Passes as drawn;
            # not re-cut.
            "options": [
                "They have the same amount of energy, because temperature "
                "is the same",
                "The pool is hotter, because it holds more energy",
                "The mug’s particles move faster because it is smaller",
                "The average particle speed is the same; the pool has far "
                "more energy",
            ],
            "answer": 3,
            "feedback": {
                0: "Temperature is an average. The pool has vastly more "
                   "particles, so vastly more total energy.",
                1: "Hotter means higher temperature, and they are equal. "
                   "More energy is not the same as hotter.",
                2: "Size does not affect particle speed. Temperature does, "
                   "and it is the same.",
            }},
        "explain": {
            "q": "Explain why a spark at 1500 °C landing on your hand does "
                 "far less damage than water at 60 °C. Use both temperature "
                 "and energy in your answer.",
            "field_label": "Your explanation",
            "placeholder": "The spark has a high temperature because…",
            "success": [
                "Says temperature measures the average speed of the "
                "particles.",
                "Says the spark contains very few particles.",
                "Says the total energy in the spark’s thermal store is "
                "therefore tiny.",
                "Says the water has far more particles, so far more total "
                "energy to transfer to your skin.",
                "Concludes that damage depends on the energy transferred, "
                "not the temperature alone.",
            ]},
        "produce": {
            "q": "A student leaves the fridge door open on a hot day to "
                 "cool the kitchen down. Explain what will actually happen, "
                 "and why. Use the idea that cold is not a substance.",
            "field_label": "Your answer",
            "placeholder": "A fridge does not make cold…",
            "success": [
                "Says a fridge does not create or release cold — cold is "
                "not a substance.",
                "Says a fridge moves energy out of its inside and releases "
                "it at the back.",
                "Says with the door open that energy is being taken from "
                "the kitchen and returned to the kitchen.",
                "Says the motor also transfers energy into a thermal store, "
                "adding more.",
                "Concludes the kitchen will get warmer, not cooler.",
            ]},
    },

    "key_note": "Temperature and energy are two quantities, not one. "
                "Heating runs from hotter to colder until the two match, "
                "and cold is not a substance that travels — it is simply "
                "less of the same thing.",

    "stretch": [
        # ⚖️ Design's flag 12 — Rumford's 1798 cannon-boring, tied to
        # `c1-06`'s model-has-edges lesson explicitly.
        {"type": "explainer", "id": "rumford-and-caloric",
         "text": "For a long time heat was thought to be a substance, "
                 "called <em>caloric</em>, that flowed out of hot things "
                 "into cold ones. It was a good model: it explained why "
                 "heating goes one way, why things reach the same "
                 "temperature, and why a hot object cools. What killed it "
                 "was a cannon factory. In 1798 Count Rumford noticed that "
                 "boring cannon barrels produced heat without limit, as "
                 "long as the boring continued — and a substance that never "
                 "runs out is not a substance. Energy was being transferred "
                 "by the mechanical work of the drill, not poured out of a "
                 "reservoir. This is the same lesson `c1-06` teaches about "
                 "models: caloric was not stupid, it was a model that "
                 "worked until someone found its edge."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "temperature",
         "definition": "A measure of the average speed of the particles in "
                       "a substance. Measured in degrees Celsius (°C). It "
                       "does not depend on how much there is."},
        {"term": "thermal store",
         "definition": "The energy held by a substance because of the "
                       "movement of its particles. Depends on the "
                       "temperature AND on how many particles there are."},
        {"term": "thermal equilibrium",
         "definition": "The state two objects reach when they are at the "
                       "same temperature and there is no net flow of energy "
                       "between them."},
        {"term": "heating",
         "definition": "Energy moving from a hotter object to a colder one "
                       "because of the temperature difference between them."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still picturing cold as something that moves?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Specific heat capacity — the same two quantities, with "
                   "a number attached to how much energy each kilogram of a "
                   "substance needs for each degree.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],
}
