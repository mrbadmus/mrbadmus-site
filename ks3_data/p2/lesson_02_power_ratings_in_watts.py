"""P2 L2 — Power ratings in watts (QUANTITATIVE).

Authored against Claude Design's approved page — which for this lesson
alone is not the delivered file:

    docs/ks3/design-reference/p2/p2-02-power-ratings-in-watts.DECODED.html

── ⚠️ THE ONE BUNDLED PAGE IN THE WHOLE PHYSICS DELIVERY ────────────────

`p2-02-power-ratings-in-watts.dc.html` is 697 KB and is the ONLY file in
the P1/P2/P3 tree carrying a `__bundler/manifest` signature.

What it hides is the MARKUP, and only the markup. Measured:

  · Her `data-dc-script` block is plain text in the outer file. `const
    RAIL`, `SORT_CARDS`, `RUNGS` and `cfifaExamples` all read normally,
    and `ks3_rail_manifest.py` reads this lesson's four rail stops off it
    with no special case.
  · The page body is a JSON string literal inside
    `<script type="__bundler/template">` — one line, every quote
    escaped — and `Cfifa.dc.html`, `support.js`, React and seven woff2
    faces are base64+deflate blobs in the manifest beside it.

So `grep 'id="s-'` returns 0, because the file holds `id=\"s-`; and a
per-occurrence count of a class name collapses to 1, because `grep -c`
counts LINES and the whole body is one. Both look like findings about the
lesson and are artefacts of the container.

It was unpacked, and the decoded page is committed beside the original so
the next lane measures markup rather than a container. The manifest glob is
`*/*.dc.html`, so the decoded copy takes no manifest row of its own.

Decoded, it is an ordinary lesson: six sections, four rail stops, one
`Cfifa` import and a formula triangle over `E = P × t`.

⚠️ **AND IT CONTRADICTS HER NOTES.** `NOTES-P2.md` §4 says of this lesson
and `p2-05`: *"no formula diagram; neither lesson has a calculable
relationship at its centre."* The drawing has `#s-cfifa`, a triangle, two
worked examples and two student attempts. Her own 23 Aug audit explains
why — `p2-02` is listed under "Built from nothing: P2 `p2-02` and `p2-04`,
which were declared QUANTITATIVE and carried no worked example in any
form." The notes are 15 Aug and the drawing is 23 Aug. THE DRAWING WAS
MEASURED. Reported, not escalated.

── ⚖️ RULED · THE LESSON OWNS `KS3.P.FUEL.02` OUTRIGHT ─────────────────

"comparing power ratings of appliances in watts (W, kW)" — one statement,
one lesson, no split.

── ⚖️ MRB-204 · TRIANGLE, AND CHECKED ──────────────────────────────────

The relationship is `E = P × t` — a genuine product — so `A = B × C`
holds and a triangle encodes something that exists. E sits above the bar; P
and t sit below it side by side. The lesson then covers E to get `P = E ÷
t`, which is the rearrangement the triangle is FOR. No sum appears anywhere
in this lesson, so no beam does either.

── ⚠️ FOUR RAIL STOPS · `s-sort` AND `s-think` ARE NOT AMONG THEM ──────

Measured off the DECODED page's own `RAIL` constant:

    s-hook · s-bench · s-cfifa · s-ladder

Design's audit records the cut in as many words: "p2-02 drops SORT and
THINK". Both sections keep their `id` — the tutor link on this page
points at `#s-sort`, so dropping the id would break it.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ─────────────────

    #s-bench   `ks3-block`                        → `check`
    #s-sort    `ks3-block ks3-dark ks3-practical` → `practical`
    #s-think   `ks3-block ks3-misconception`      → `misconception`

── ⚖️ TWO MINTS, AND WHY THE SECOND IS NOT THE FIRST AGAIN ─────────────

`ENER-21` is the rate/total confusion: a rating is read as a quantity of
electricity. `ENER-22` is a factual belief about the appliance — that
standby draws nothing at all — and a student can hold it while being
perfectly sound that power is a rate. Different roots, so two rows.

Design's `NOTES-P2.md` §1 predicts one id for this lesson (her
`ENERGY-12`); the second quote arrived with her own 23 Aug audit, which
added "a second misconception quote" to all sixteen P1–P3 lessons. Same
notes-vs-drawing gap as above, same resolution.

── ⚠️ THE KETTLE/ROUTER ARITHMETIC IS EXACT AND IS CHECKED ─────────────

2000 W × 180 s = 360 000 J. 15 W × 28 800 s = 432 000 J. The crossover is
where 2000 t = 15 × 28 800 · t/28800 … in Design's bench it is the time at
which the router's running total overtakes the kettle's finished total:
360 000 ÷ 15 = 24 000 s = 6 h 40 min, which is her "6.67 h". The bench
COMPUTES it rather than being told it, so the number on screen cannot drift
from the numbers above it.

── ⚖️ MRB-297 · P2-09 · THE APPLIANCE IS A ROUTER, AND WAS A CHARGER ───

Design's hook raced the kettle against a phone charger left plugged in for
eight hours, and the bench drew that charger at a flat 15 W for all eight.
A charger does not do that. It draws near its rating only while the battery
is taking charge — an hour or two — and then trickles, and one plugged in
with nothing on the end of it is held by law to a fraction of a watt. Flat
out for 8 h it would deliver 120 Wh into a phone that holds about 17 Wh.
Realistically it transfers about 90 kJ overnight, so the KETTLE wins and
the answer the page credited was wrong — which the page's own second
misconception quote already says: standby is a low power, not no power.

A home router is rated in the same range, genuinely draws its rating all
night, and is in every house. So the appliance changed and not one number
did: 2000 W × 180 s = 360 000 J, 15 W × 28 800 s = 432 000 J, crossover at
360 000 ÷ 15 = 24 000 s = 6 h 40 min.

⚠️ ONE SITE IS NOT IN THIS FILE. `shared/ks3.js` hardcodes the bench's
past-crossover caption — "The 15 W charger has now transferred more energy
than the 2000 W kettle did all day" — inside the power-bench wiring. It
still says charger, and this lane may not edit that file.
"""

LESSON = {
    "slug":  "power-ratings-in-watts",
    "title": "Power ratings in watts",
    "discipline": "physics",
    "unit": "Energy at home",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.FUEL.02"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 10}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["energy-in-food"],
    "assumes": [],
    "references": ["energy-stores"],
    "ks4_links": [],

    "meta_description": "A kettle is 130 times the power of a home router "
                        "and still costs less to run. Power is a rate, energy "
                        "is a total, and confusing the two is the most "
                        "expensive mistake people make about their own bill.",

    "big_question": "A 2000 W kettle and a 15 W home router. Which one "
                    "costs you more over a day?",

    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "Kettle vs router",        "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Power bench",             "done_when": "crossover_seen"},
        {"anchor": "s-cfifa", "short": "CFIFA",
         "label": "Triangle and five lines", "done_when":
         "both_attempts_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A kettle is 130 times the power of a router.",
        "prompt": "The kettle is rated 2000 W and runs for about three "
                  "minutes a day. The router is rated 15 W and is left on "
                  "for eight hours every night.",
        "commit": "Commit. Which uses more energy in a day?",
        "options": [
            "The kettle — 2000 W is far more than 15 W",
            "The router — it runs for 160 times as long",
            "Exactly the same, by coincidence",
            "Impossible to say without the voltage",
        ],
        "answer": 1,
        "reveal": "The router — 432 000 J against the kettle's "
                  "360 000 J. The kettle wins on power by a factor of 130 "
                  "and still loses on energy, because power says nothing at "
                  "all about how long the thing runs. <strong>Two different "
                  "quantities, and confusing them is the single most "
                  "expensive mistake people make about their own electricity "
                  "bill.</strong>",
    },

    "misconceptions": [
        {"id": "ENER-21",
         "statement": "A higher-wattage appliance uses more electricity, so "
                      "switching to a lower-wattage one always saves energy.",
         "elicited_by": "s-hook",
         "confronted_by": "power-bench"},
        {"id": "ENER-22",
         "statement": "An appliance on standby is off, so it costs nothing.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Power is a <em>rate</em>: joules per second. A watt "
                 "<em>is</em> a joule per second — the unit tells you "
                 "the definition if you read it. The rating on an appliance "
                 "is a statement about how fast it transfers energy while "
                 "running, and nothing whatever about the total."},

        # ── #s-bench · the power bench ──────────────────────────────────
        {"type": "power-bench",
         "id": "power-bench",
         "anchor": "s-bench",
         "eyebrow": "The power bench · two dials, two answers",
         "heading": "Race a kettle against a router.",
         "prompt": "Two appliances running side by side. The tall bar is "
                   "power — how fast energy is flowing right now. The "
                   "filling bar is the total so far.",
         "gate": {
             "prompt": "Commit first. What does a rating of 2000 W actually "
                       "tell you?",
             "options": [
                 "It transfers 2000 J in total",
                 "It transfers 2000 J every second while running",
                 "It costs 2000 units to run",
                 "It can boil 2000 ml of water",
             ],
             "answer": 1,
         },
         "appliances": [
             {"id": "kettle",  "label": "Kettle",  "watts": 2000,
              "runs_for_s": 180},
             {"id": "router",  "label": "Router",  "watts": 15,
              "runs_for_s": 28800},
         ],
         "jumps": [
             {"id": "three-min", "label": "Jump to 3 min",        "at_s": 180},
             {"id": "crossover", "label": "Jump to the crossover",
              "at": "crossover"},
             {"id": "eight-hr",  "label": "Jump to 8 hours",    "at_s": 28800},
         ],
         "run_label": "Run the day",
         "reset_label": "Back to zero",
         "readouts": [
             {"id": "clock",   "label": "Clock"},
             {"id": "kettle",  "label": "Kettle total"},
             {"id": "router",  "label": "Router total"},
         ],
         "alt": "Two appliances side by side: a kettle rated 2000 watts and "
                "a router rated 15 watts, each with a tall bar showing its "
                "power and a filling bar showing the energy it has "
                "transferred so far.",
         "close": "The kettle's bar is over a hundred times taller and its "
                  "total is smaller. A rating is a height; the bill is an "
                  "area."},

        {"type": "key-fact", "ref": "power-is-a-rate"},

        # ── #s-sort · NOT a rail stop ───────────────────────────────────
        {"type": "power-energy-sort",
         "id": "power-energy-sort",
         "anchor": "s-sort",
         "eyebrow": "Which quantity is it?",
         "heading": "Sort each unit and each sentence",
         "prompt": "If you can do this reliably, the next two lessons are "
                   "arithmetic. If you cannot, they will feel impossible.",
         "power_label": "Power",
         "energy_label": "Energy",
         # ⚠️ `sort_items`, never `cards` — `cards` is claimed by
         # `r_activity` and a payload using it renders twice and blank.
         "sort_items": [
             {"id": "s1", "text": "The watt (W)", "is_power": True,
              "right": "Power. One watt is one joule every second.",
              "wrong": "This is the unit of power — read it as joules "
                       "per second and it tells you itself."},
             {"id": "s2", "text": "The joule (J)", "is_power": False,
              "right": "Energy. The total amount, with no time attached.",
              "wrong": "The joule is the unit of energy. Power needs a "
                       "“per second” in it."},
             {"id": "s3", "text": "“This shower is rated 8.5 kW.”",
              "is_power": True,
              "right": "Power — a rate. It says nothing about how long "
                       "anyone stands in it.",
              "wrong": "A rating is always a rate. It is how fast the shower "
                       "transfers energy while running."},
             {"id": "s4", "text": "“The oven used 1.8 kWh last night.”",
              "is_power": False,
              "right": "Energy. The h on the end means an hour of time has "
                       "already been multiplied in.",
              "wrong": "This one is energy, despite starting with kilowatt "
                       "— the “hour” turns a rate into a total."},
             {"id": "s5", "text": "“A sprinter peaks at about "
                                  "1000 W.”",
              "is_power": True,
              "right": "Power. It is a peak rate, sustainable for only a few "
                       "seconds.",
              "wrong": "A peak figure in watts is a rate — the fastest "
                       "they can transfer energy, not the amount."},
             {"id": "s6", "text": "“A cheese sandwich holds "
                                  "1200 kJ.”",
              "is_power": False,
              "right": "Energy. A store, sitting there, with no rate "
                       "involved.",
              "wrong": "Kilojoules are energy. Nothing here says how quickly "
                       "the sandwich would be used."},
         ]},

        # ── #s-cfifa · the formula, then CFIFA ──────────────────────────
        # ⚠️ NO ANCHOR ON THE FORMULA — MRB-208, same reason as p2-01.
        # A `formula` block cannot tick, so the stop goes on the CFIFA.
        {"type": "formula",
         "id": "power-rule",
         "eyebrow": "Five lines, every time · CFIFA",
         "statement": "Energy transferred = power × time",
         "support": [
             "energy transferred, E, is measured in joules (J)",
             "power, P, is measured in watts (W) — joules per second",
             "time, t, is measured in seconds (s)",
         ],
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Energy E sits above a "
                           "dividing line; power P and time t sit below it, "
                           "multiplied together. Covering one letter leaves "
                           "the way to work it out.",
             "top":   {"label": "E", "button": "Cover E",
                       "text": "Energy sits alone at the top. Cover it and "
                               "the other two are side by side — "
                               "multiply."},
             "left":  {"label": "P", "button": "Cover P",
                       "text": "Power sits underneath with energy above it. "
                               "Cover P and you get E over t — divide."},
             "right": {"label": "t", "button": "Cover t",
                       "text": "Time sits underneath with energy above it. "
                               "Cover t and you get E over P — divide."},
             "close": "Two things side by side means multiply. One thing "
                      "over another means divide. And the seconds are always "
                      "seconds — a watt is a joule EACH SECOND, so a "
                      "time in minutes has to be converted before it goes "
                      "anywhere near this triangle.",
         }},

        {"type": "worked-example", "id": "cfifa-power-plain",
         "anchor": "s-cfifa"},
        {"type": "worked-example", "id": "cfifa-power-convert"},

        # ── #s-think · NOT a rail stop ──────────────────────────────────
        {"type": "misconception", "id": "think-lower-wattage",
         "anchor": "s-think"},

        {"type": "key-fact", "ref": "rating-is-how-fast"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        # ⚠️ NO COMMIT WIDGET — see the note in `lesson_01`. The engine's
        # `misconception` block renders confrontations BEFORE the generic
        # options branch, so a commit authored here would sit below both
        # quotes and read as part of the second one. All eight live P1
        # lessons resolve it the same way.
        {"id": "think-lower-wattage",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-21",
         "statements": [
             {"quote": "A higher-wattage appliance uses more electricity, so "
                       "switch to a lower-wattage one.",
              "targets": "ENER-21",
              "body": [
                  "A higher rating means <em>faster</em>, not <em>more</em>. "
                  "What you pay for is joules, and joules are power "
                  "multiplied by time — so a rating on its own cannot "
                  "tell you the bill.",
                  "Worse, the advice can backfire. Swap a 2000 W kettle for "
                  "a 1000 W one and it takes twice as long to boil the same "
                  "water, transferring almost exactly the same total energy "
                  "— and slightly more, because it has longer to lose "
                  "energy to the kitchen. <strong>The genuinely useful "
                  "question is never “how many watts” but “how "
                  "many watts, for how long”.</strong>",
                  "Where ratings really do matter is safety and wiring: "
                  "2000 W through a thin extension lead is a fire, whatever "
                  "the total energy. Power tells you what the cable must "
                  "survive. Energy tells you what the bill will say.",
              ]},
             {"quote": "An appliance on standby is off, so it costs nothing.",
              "targets": "ENER-22",
              "body": [
                  "Standby is a low power, not no power. A set-top box "
                  "drawing 8 W looks harmless against a 2000 W kettle "
                  "— until you notice it draws that 8 W for 8760 hours "
                  "a year while the kettle runs for perhaps 30. That is "
                  "70 kWh against 60 kWh: <strong>the thing you thought was "
                  "off costs more than the thing you thought was "
                  "expensive.</strong> Power ratings tell you nothing until "
                  "you multiply by the time.",
              ]},
         ]},

        {"id": "cfifa-power-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "A motor transfers 9000 J in 30 s. What is its power?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Now the same five steps where the units "
                                  "do need converting."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "9000 J stays 9000 J · 30 s stays 30 s",
              "note": "A watt is a joule each second, and both readings are "
                      "already in those units, so there is nothing to "
                      "convert."},
             {"letter": "F", "label": "Formula",
              "line": "P = E ÷ t",
              "note": "Power is energy shared out over the time it took."},
             {"letter": "I", "label": "Insert",
              "line": "P = 9000 J ÷ 30 s",
              "note": "The energy on top, because power is joules per "
                      "second."},
             {"letter": "F", "label": "Fine-tune",
              "line": "9000 ÷ 30 = 300",
              "note": "Joules divided by seconds leaves joules each "
                      "second."},
             {"letter": "A", "label": "Answer",
              "line": "P = 300 W",
              "note": "Three hundred watts — the rating this motor "
                      "would carry on its plate."},
         ]},

        {"id": "cfifa-power-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "A heater transfers 540 000 J in 3.0 minutes. What is "
                    "its power?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Both are open. The first line is the one "
                                  "that decides the answer."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "3.0 min × 60 = 180 s",
              "note": "A watt is a joule each second, so the minutes have to "
                      "become seconds before anything divides."},
             {"letter": "F", "label": "Formula",
              "line": "P = E ÷ t",
              "note": "Power is energy shared out over the time it took."},
             {"letter": "I", "label": "Insert",
              "line": "P = 540 000 J ÷ 180 s",
              "note": "The converted time goes in. The 3.0 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "540 000 ÷ 180 = 3000",
              "note": "Joules divided by seconds leaves joules each "
                      "second."},
             {"letter": "A", "label": "Answer",
              "line": "P = 3000 W",
              "note": "Divide by 3.0 instead of 180 and the rating comes out "
                      "180 000 W — sixty times too big."},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "power-is-a-rate",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Power is the rate of energy transfer. One watt is one "
                 "joule per second. A rating tells you how fast, never how "
                 "much."},
        {"id": "rating-is-how-fast",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Power is the rate of transfer: P = E ÷ t, measured in "
                 "watts. One watt is one joule each second. A rating tells "
                 "you how fast an appliance transfers energy, never how much "
                 "— for that you also need the time."},
    ],

    "ladder": {
        "recall": {
            "q": "One watt is equal to…",
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": ["one second per joule", "one joule",
                        "one joule per second", "one thousand joules"],
            "answer": 2,
            "feedback": {
                0: "The right way up is joules on top: how much energy each "
                   "second.",
                1: "A joule is an amount. A watt is an amount per second "
                   "— the time is the whole point.",
                3: "That is a kilojoule, and it is still energy rather than "
                   "power.",
            }},
        "apply": {
            "q": "A 2000 W kettle runs for 3 minutes. A 15 W router runs "
                 "for 8 hours. Which transfers more energy?",
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": [
                "You cannot tell without knowing the voltage",
                "The kettle, because 2000 W is much higher",
                "They are equal",
                "The router",
            ],
            "answer": 3,
            "feedback": {
                0: "Power and time are all you need. The voltage is already "
                   "inside the power figure.",
                1: "Higher power, far shorter time. 2000 × 180 = "
                   "360 kJ; 15 × 28 800 = 432 kJ.",
                2: "Close, but not equal — work both products out and "
                   "the router comes out ahead.",
            }},
        "explain": {
            "q": "Explain the difference between power and energy, using a "
                 "2000 W kettle and a 15 W router as your example. Say what "
                 "each quantity is useful for deciding.",
            "field_label": "Your explanation",
            "placeholder": "Power is a rate…",
            "success": [
                "Says power is a rate — energy transferred each second.",
                "Says energy is a total, found by multiplying power by the "
                "time.",
                "Uses the numbers: the kettle is higher power but runs "
                "briefly.",
                "States that the router transfers more energy over a day "
                "despite its low rating.",
                "Says power matters for safety and cable choice, and energy "
                "matters for the bill.",
            ]},
        "produce": {
            "q": "A shop assistant says a 1000 W kettle is cheaper to run "
                 "than a 2000 W one. Explain why this is close to false, and "
                 "describe the one situation where a lower rating genuinely "
                 "saves energy.",
            "field_label": "Your answer",
            "placeholder": "The 1000 W kettle takes twice as long…",
            "success": [
                "Says the 1000 W kettle takes about twice as long to boil "
                "the same water.",
                "Says the total energy is therefore roughly the same, "
                "because power × time is unchanged.",
                "Notes the slower kettle is slightly worse, because it has "
                "longer to lose energy to the kitchen.",
                "Says a lower rating saves energy only if it does less of "
                "the job — e.g. an LED giving the same light for fewer "
                "watts.",
                "Distinguishes doing the same job more efficiently from "
                "simply doing it slower.",
            ]},
    },

    "key_note": "One watt is one joule per second. Power is a rate; energy "
                "is a total. A rating tells you how fast and how thick the "
                "cable needs to be — never how much the thing costs to "
                "run.",

    "stretch": [
        {"id": "watt-and-the-horse",
         "type": "explainer",
         "text": "James Watt did not invent the unit named after him; he "
                 "invented the marketing problem it solved. Selling steam "
                 "engines in the 1770s to mine owners who had only ever "
                 "bought horses, he needed a number they could compare, so "
                 "he measured what a strong pit horse could lift and called "
                 "it one horsepower — about 750 watts. It was a "
                 "generous figure, arguably deliberately so, and it made his "
                 "engines sound modest. Your own body sustains around 100 W "
                 "of useful output over a working day and can peak near "
                 "1000 W for a few seconds in a sprint. <strong>The kettle "
                 "on the bench above outruns you by a factor of twenty, "
                 "continuously, and costs a few pence.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        {"term": "power",
         "definition": "The rate at which energy is transferred — how "
                       "many joules each second. Measured in watts."},
        {"term": "watt",
         "definition": "One joule per second. The unit says the definition "
                       "if you read it as joules-per-second."},
        {"term": "rating",
         "definition": "The power an appliance draws while it is running. It "
                       "says how fast, never how much."},
        {"term": "standby",
         "definition": "A low power an appliance draws while apparently off. "
                       "Low is not zero, and it runs for thousands of hours "
                       "a year."},
    ],

    "tutor": {
        "anchor": "s-sort",
        "prompt": "Ask Mr Badmus AI",
        "body": "Still mixing up watts and joules?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "P = E ÷ t alongside P = IV and P = I²R, and the National "
                   "Grid.",

    "ws": ["analysis-and-evaluation"],
}
