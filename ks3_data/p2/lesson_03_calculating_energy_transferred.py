"""P2 L3 — Calculating energy transferred (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p2/p2-03-calculating-energy-transferred.dc.html`.

Her page wins outright. Every appliance, every rating, every rung and both
worked examples are hers.

── ⚖️ RULED · THE LESSON OWNS `KS3.P.FUEL.03` OUTRIGHT ─────────────────

"comparing amounts of energy transferred (J, kJ, kW hour)" — one
statement, one lesson, no split.

── ⚖️ MRB-204 · TRIANGLE, AND CHECKED ──────────────────────────────────

`E = P × t` is a genuine product, so `A = B × C` holds and the triangle
encodes a relationship that exists. Checked against the arithmetic. Nothing
in this lesson is a sum — the appliance bench COMPARES totals rather than
adding them — so no beam appears. `p2-04` is where the sum arrives, and
that is where the beam does.

⚠️ The triangle sits in `#s-tri`, which is a section of its own and is NOT
a rail stop. Design's audit: "p2-03 drops TRIANGLE and THINK".

── ⚖️ RULED · THE UNIT-PAIRING PANEL STAYS, AND STAYS FLAT ─────────────

Design's flag 9 asks about the canvas stating "W × min IS ALWAYS
WRONG" without hedging. It stays flat, and it stays. The ×60 error is this
lesson's entire misconception — Rung 2 is built on it, `#s-think`'s first
quote is it verbatim, and the second worked example exists to show the
Convert line catching it. A hedge on the one sentence that has to stick
would cost more than it bought, and the statement is also simply true:
there is no legal reading in which watts multiply minutes.

Two consistent pairings exist and no others, and the page says so:
**watts with seconds gives joules; kilowatts with hours gives
kilowatt-hours.**

── ⚠️ FOUR RAIL STOPS ─────────────────────────────────────────────────

    s-hook · s-bench · s-worked · s-ladder

`#s-tri` and `#s-think` are full sections and neither is on the rail. Both
keep their `id`.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ────────────────

    #s-tri     `ks3-block`                    → (a `formula` block, not an
                                                 instrument)
    #s-bench   `ks3-block`                    → `check`
    #s-think   `ks3-block ks3-misconception`  → `misconception`

── ⚖️ TWO MINTS ───────────────────────────────────────────────────────

Design's `NOTES-P2.md` §1 records this lesson as "(unit discipline, no
ID)". That was true of the 15 Aug page; the 23 Aug drawing carries a
`#s-think` with a commit and two quotes, and both name beliefs a student
holds.

`ENER-23` is the ×60 error — a rule about which unit of time the
formula takes. `ENER-24` is a belief about the SIZE of a joule, and it is
what lets the first error survive: a student who knew a joule was tiny
would reject 6000 J for a kettle on sight. Different roots, so two rows,
and the second is why the first is not caught.

── ⚠️ THE FRIDGE OUTRANKS THE OVEN, AND THAT IS THE POINT ─────────────

90 W × 24 h = 2.16 kWh against 2200 W × 45 min = 1.65 kWh.
Design's flag 10 flags it deliberately: it is `ENER-21` from `p2-02`
paying off one lesson later, on real appliances. The bench COMPUTES both,
so the ordering cannot drift from the ratings above it.
"""

LESSON = {
    "slug":  "calculating-energy-transferred",
    "title": "Calculating energy transferred",
    "discipline": "physics",
    "unit": "Energy at home",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.FUEL.03"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 11}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["power-ratings-in-watts"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "An 8500 W shower for ten minutes, and a 60 W lamp "
                        "left on all day. They transfer almost exactly the "
                        "same energy. E = P × t — and the time is in "
                        "seconds, which is the slip worth a factor of sixty.",

    "big_question": "An electric shower is rated 8500 W and you are in it "
                    "for ten minutes. Someone leaves a 60 W lamp on for a "
                    "full day. Which one transferred more energy?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Shower vs lamp",  "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Appliance bench", "done_when": "three_appliances_priced"},
        {"anchor": "s-worked", "short": "CFIFA",
         "label": "CFIFA",           "done_when": "both_attempts_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",  "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Ten minutes against twenty-four hours.",
        "prompt": "An electric shower is rated 8500 W. You are in it for ten "
                  "minutes. Someone else in the house leaves a 60 W lamp on "
                  "all day — twenty-four hours.",
        "commit": "Commit. Which transferred more energy?",
        "options": [
            "The shower, by a wide margin",
            "They are almost exactly equal",
            "The lamp, by a wide margin",
            "The shower, but only by about a tenth",
        ],
        "answer": 1,
        "reveal": "The shower gives 5.1 MJ, against the lamp's 5.2 MJ. They "
                  "are almost identical, which nobody guesses. Ten minutes "
                  "of shower and a full day of forgotten lamp cost the same, "
                  "and <strong>the only way to know that is to do the "
                  "multiplication.</strong>",
    },

    "misconceptions": [
        {"id": "ENER-23",
         "statement": "The time in E = P × t goes in as it was given, "
                      "so a 2000 W kettle for 3 minutes transfers "
                      "2000 × 3 = 6000 J.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "ENER-24",
         "statement": "A joule is a decent amount of energy, so a few "
                      "thousand joules sounds about right for boiling a "
                      "kettle.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "One relationship, one line of working, and one trap. The "
                 "relationship is energy = power × time. The trap is "
                 "units: <strong>watts want seconds, kilowatts want "
                 "hours</strong>, and mixing them is the single most common "
                 "way to be wrong by a factor of 3600."},

        # ── #s-tri · the formula. NOT a rail stop. ──────────────────────
        {"type": "formula",
         "id": "energy-rule",
         "anchor": "s-tri",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Energy = power × time",
         "support": [
             "W with s gives J",
             "kW with h gives kWh",
             "and no other pairing is legal",
         ],
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Energy E sits above a "
                           "dividing line; power P and time t sit below it, "
                           "multiplied together. Covering one letter leaves "
                           "the way to work it out.",
             "top":   {"label": "E", "button": "Cover E",
                       "text": "Energy is alone at the top. Cover it and the "
                               "other two sit side by side — multiply."},
             "left":  {"label": "P", "button": "Cover P",
                       "text": "Power sits underneath with energy above it. "
                               "Cover it and you are left with E over t "
                               "— divide."},
             "right": {"label": "t", "button": "Cover t",
                       "text": "Time sits underneath with energy above it. "
                               "Cover it and you are left with E over P "
                               "— divide."},
             "close": "Two things side by side means multiply. One thing "
                      "over another means divide. And there are exactly two "
                      "legal unit pairings: <strong>watts × seconds "
                      "gives joules; kilowatts × hours gives "
                      "kilowatt-hours.</strong> Watts × minutes is "
                      "always wrong.",
         }},

        # ── #s-bench · the appliance bench ──────────────────────────────
        {"type": "appliance-bench",
         "id": "appliance-bench",
         "anchor": "s-bench",
         "eyebrow": "The appliance bench · set it up and price it",
         "heading": "Two units, one answer.",
         "prompt": "Pick an appliance, set a realistic time, and read the "
                   "same energy in both legal unit pairings — with what "
                   "it costs beside them.",
         "gate": {
             "prompt": "Commit first. A 2000 W kettle runs for 3 minutes. "
                       "Which calculation gives the energy in joules?",
             "options": ["2000 × 3", "2000 × 180", "2 × 3",
                         "2000 ÷ 180"],
             "answer": 1,
         },
         "price_per_kwh": 0.27,
         "mins_min": 1,
         "mins_max": 1440,
         "mins_start": 3,
         "appliances_to_price": 3,
         "appliances": [
             {"id": "kettle", "label": "Kettle", "watts": 2000,
              "typical_min": 3,
              "tnote": "about three minutes to boil"},
             {"id": "shower", "label": "Electric shower", "watts": 8500,
              "typical_min": 10,
              "tnote": "a ten-minute shower"},
             {"id": "lamp", "label": "LED lamp", "watts": 9,
              "typical_min": 300,
              "tnote": "five hours in an evening"},
             {"id": "oven", "label": "Oven", "watts": 2200,
              "typical_min": 45,
              "tnote": "a 45-minute roast"},
             {"id": "fridge", "label": "Fridge", "watts": 90,
              "typical_min": 1440,
              "tnote": "all day, every day"},
         ],
         "readouts": [
             {"id": "joules", "label": "In joules"},
             {"id": "kwh",    "label": "In kilowatt-hours"},
             {"id": "cost",   "label": "At 27p per kWh"},
         ],
         "alt": "An appliance bench. A rating in watts and a running time in "
                "minutes, with the same energy shown in joules and in "
                "kilowatt-hours side by side, and the cost beside them.",
         "close": "The fridge — 90 W, the second-lowest rating on the "
                  "bench — is the biggest consumer of the five, because "
                  "it never switches off. Nothing about its rating hints at "
                  "that."},

        {"type": "key-fact", "ref": "convert-on-the-insert-line"},

        # ── #s-worked · CFIFA ───────────────────────────────────────────
        {"type": "worked-example", "id": "cfifa-energy-plain",
         "anchor": "s-worked"},
        {"type": "worked-example", "id": "cfifa-energy-convert"},

        # ── #s-think · NOT a rail stop ──────────────────────────────────
        {"type": "misconception", "id": "think-times-sixty",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        {"id": "think-times-sixty",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-23",
         "statements": [
             {"quote": "A 2000 W kettle for 3 minutes: 2000 × 3 = "
                       "6000 J.",
              "targets": "ENER-23",
              "body": [
                  "The time is in minutes and the watt is defined per "
                  "<em>second</em>. Three minutes is 180 seconds, so the "
                  "answer is 360 000 J — sixty times what was written.",
                  "There is a check that catches this every time, and it "
                  "costs you five seconds: <strong>ask whether the answer is "
                  "a sensible size.</strong> 6000 J is roughly the energy in "
                  "a mouthful of bread. It could not possibly boil a litre "
                  "of water. When your answer is absurd, suspect the units "
                  "before you suspect the physics.",
                  "The safest habit is to convert on the Insert line, never "
                  "later — write “180 s” into the working rather "
                  "than converting the answer afterwards. Two consistent "
                  "pairs exist and no others: watts with seconds gives "
                  "joules; kilowatts with hours gives kilowatt-hours.",
              ]},
             {"quote": "A joule is a decent amount of energy, so 6000 J for "
                       "a kettle sounds about right.",
              "targets": "ENER-24",
              "body": [
                  "A joule is tiny. Lifting an apple from the floor to a "
                  "table takes about one; a single AA cell holds around "
                  "10 000. A kettle boiling a mugful needs about 360 000 J, "
                  "which is why the answers in this lesson run into hundreds "
                  "of thousands and why kilojoules and megajoules exist at "
                  "all. <strong>If a kettle calculation comes out in the "
                  "thousands, the time was almost certainly left in "
                  "minutes.</strong>",
              ]},
         ]},

        {"id": "cfifa-energy-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "A 60 W lamp is left on for 300 s. How much energy does "
                    "it transfer?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Now the same five steps where the time "
                                  "does need converting."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "60 W stays 60 W · 300 s stays 300 s",
              "note": "A watt is a joule each second, and the time is "
                      "already in seconds, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "E = P × t",
              "note": "Cover E on the triangle: P sits beside t, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "E = 60 W × 300 s",
              "note": "The seconds on the bottom of the watt cancel the "
                      "seconds of the time."},
             {"letter": "F", "label": "Fine-tune",
              "line": "60 × 300 = 18 000",
              "note": "Watts times seconds gives joules."},
             {"letter": "A", "label": "Answer",
              "line": "E = 18 000 J",
              "note": "Eighteen thousand joules, which is 18 kJ."},
         ]},

        {"id": "cfifa-energy-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "A 2000 W kettle runs for 3 minutes. How much energy "
                    "does it transfer?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Both are open. The Convert line is the "
                                  "one that decides the answer."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "3 min × 60 = 180 s",
              "note": "A watt is a joule each second, so the minutes have to "
                      "become seconds before anything multiplies."},
             {"letter": "F", "label": "Formula",
              "line": "E = P × t",
              "note": "Cover E on the triangle: P sits beside t, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "E = 2000 W × 180 s",
              "note": "The converted time goes in. The 3 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "2000 × 180 = 360 000",
              "note": "Watts times seconds gives joules."},
             {"letter": "A", "label": "Answer",
              "line": "E = 360 000 J",
              "note": "Insert 3 instead of 180 and the answer comes out "
                      "6000 J — sixty times too small. That is the "
                      "mistake at the top of the next section."},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "convert-on-the-insert-line",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "E = P × t, with the power in watts and the time in "
                 "seconds. Converting the time is part of the calculation, "
                 "not an afterthought — minutes and hours never go into "
                 "the formula as they stand."},
    ],

    "ladder": {
        "recall": {
            "q": "A 1200 W microwave runs for 90 seconds. How much energy "
                 "does it transfer?",
            # ⚠️ MRB-177 — Design writes these as "1290 J", "13.3 J",
            # "1800 J" against a correct answer of "108 000 J", and the
            # space in the correct one makes it the longest by the gate's
            # own measure. A student can score it without reading it. The
            # numbers are hers and are unchanged; only the thousands
            # separator is applied consistently, which it should have been
            # anyway. ENGINE POLICY, not a science departure.
            "options": ["108 000 J", "1 290 J", "13.3 J", "1 800 J"],
            "answer": 0,
            "feedback": {
                1: "That is 1200 + 90. The two quantities are multiplied.",
                2: "That is 1200 ÷ 90. Cover E on the triangle — it "
                   "comes out as a multiplication.",
                3: "That looks like 1200 × 1.5 minutes. Watts need the "
                   "time in seconds, so use 90.",
            }},
        "apply": {
            "q": "A 2000 W kettle runs for 3 minutes. A student writes "
                 "2000 × 3 = 6000 J. What is wrong?",
            # ⚠️ MRB-177 — Design's correct option runs to thirteen words
            # against a longest distractor of seven, which the gate reads as
            # a length tell: the longest option is the answer and a student
            # need not read any of them. Her four CLAIMS are unchanged and
            # in her order; the correct one is trimmed to the claim itself
            # and the three distractors are given the same weight, so the
            # set is decided by reading rather than by measuring. ENGINE
            # POLICY, not a science departure — see DEPARTURES-P2.md.
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": [
                "Nothing is wrong — that working is correct",
                "The time must be in seconds, not minutes",
                "The power should have been given in kilowatts",
                "They should have divided rather than multiplied",
            ],
            "answer": 1,
            "feedback": {
                0: "Check the size of the answer: 6000 J could not warm a "
                   "cup of water, let alone boil a litre. Three minutes is "
                   "180 s, so the answer is 360 000 J.",
                2: "You could work in kilowatts, but then the time must be "
                   "in hours. Mixing kW with minutes is a different error.",
                3: "The operation is right. The unit of time is not.",
            }},
        "explain": {
            "q": "An 8500 W shower runs for 10 minutes and a 60 W lamp is "
                 "left on for 24 hours. Show that they transfer almost the "
                 "same energy, and explain what this tells you about judging "
                 "appliances by their rating.",
            "field_label": "Your working and explanation",
            "placeholder": "Shower: 8500 W × 600 s = …",
            "success": [
                "Converts 10 minutes to 600 s and calculates 5 100 000 J for "
                "the shower.",
                "Converts 24 hours to 86 400 s and calculates 5 184 000 J "
                "for the lamp.",
                "States that the two totals are within a few per cent of "
                "each other.",
                "Says the rating alone cannot tell you the energy, because "
                "the times differ by a factor of 144.",
                "Draws the conclusion that a low-power appliance left on for "
                "a long time can cost as much as a high-power one used "
                "briefly.",
            ]},
        "produce": {
            "q": "A household wants to cut its electricity bill and has a "
                 "2200 W oven used 45 minutes a day, a 90 W fridge running "
                 "constantly, and eight 9 W LED lamps on about 5 hours a "
                 "day. Work out which costs most per day and advise them, "
                 "using numbers.",
            "field_label": "Your answer",
            "placeholder": "Oven: 2.2 kW × 0.75 h = …",
            "success": [
                "Calculates the oven at about 1.65 kWh per day.",
                "Calculates the fridge at about 2.16 kWh per day.",
                "Calculates the lamps at about 0.36 kWh per day in total.",
                "Identifies the fridge as the largest, despite having the "
                "lowest power rating.",
                "Gives advice that follows from the numbers — and notes "
                "that the fridge cannot simply be switched off, so the "
                "realistic saving is elsewhere.",
            ]},
    },

    "key_note": "E = P × t. Convert the time on the Insert line, not "
                "afterwards. Watts with seconds, or kilowatts with hours "
                "— and always ask whether the answer is a sensible "
                "size.",

    "stretch": [
        {"id": "the-mars-climate-orbiter",
         "type": "explainer",
         "text": "Unit slips of exactly this kind are not confined to "
                 "homework. In 1999 NASA lost the Mars Climate Orbiter "
                 "— a spacecraft that took nine months to arrive "
                 "— because one team supplied thrust figures in "
                 "pound-force seconds and the receiving software expected "
                 "newton seconds. <strong>Nobody made an arithmetic "
                 "mistake.</strong> Every number was correct in its own "
                 "units, and the craft entered the atmosphere about 170 km "
                 "lower than intended and was destroyed. The discipline you "
                 "are being asked for here, of writing the unit next to "
                 "every number in the working, is the same discipline that "
                 "would have saved a $327 million mission."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "kilowatt-hour",
         "definition": "A kilowatt for an hour — 3 600 000 J. It is a "
                       "unit of energy, not of power, and it is the “unit” "
                       "an electricity bill charges for."},
        {"term": "convert",
         "definition": "Change a quantity into the unit the formula needs, "
                       "on the Insert line, before anything is multiplied."},
        {"term": "order of magnitude",
         "definition": "Roughly how big an answer should be. Checking it "
                       "catches a unit slip faster than re-reading the "
                       "arithmetic."},
    ],

    "tutor": {
        "anchor": "s-worked",
        "prompt": "Ask Mr Badmus AI",
        "body": "Answer coming out sixty times too small?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Energy transferred by an appliance, efficiency "
                   "calculations, and the cost of electricity.",

    "ws": ["analysis-and-evaluation"],
}
