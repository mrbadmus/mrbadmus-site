"""P2 L4 — Reading a fuel bill (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p2/p2-04-reading-a-fuel-bill.dc.html`.

── ⚖️ MRB-204 · THE LESSON THAT MAKES THE RULE VISIBLY NECESSARY ───────

This is the only place in KS3 where a PRODUCT and a SUM sit inside one
calculation, and Design draws both shapes rather than picking one:

    one row of the bill    units = kW × hours       a PRODUCT   TRIANGLE
    the amount due         Σ(rows) + standing       a SUM       BEAM

Her `#s-shape` says it in her own words — *"Each row of that bill is
power × time — a genuine product, and a formula triangle is the
right tool for one row. The bottom line is a different shape entirely: it
is a sum of every row, and no triangle can represent adding things up."* —
and her beam's own caption reads **"A SUM OF PRODUCTS — TRIANGLE FOR
ONE ROW, BALANCE FOR THE TOTAL"**.

Checked against the arithmetic, twice. A triangle over the amount due
would encode `A = B × C` for a quantity that is `A = B + C + D + E +
F + standing`, which is a relationship that does not exist. The beam's pans
are `every row, added` and `amount due`, and it is DEAD LEVEL — the
same treatment `p1-03` gives conservation, and for the same reason.

The row triangles are drawn ON the beam's left pan rather than as a
separate cover-triangle: Design stacks one small triangle per row there, so
a student sees five products being added in one picture. That is why this
lesson's `formula` block carries a `figure` and no `triangle` key — the
triangles are inside the figure.

── ⚖️ RULED · THE LESSON OWNS `KS3.P.FUEL.04` OUTRIGHT ────────────────

"domestic fuel bills, fuel use and costs" — one statement, one lesson.

── ⚠️ FOUR RAIL STOPS · THREE SECTIONS ARE NOT ON IT ──────────────────

    s-hook · s-bill · s-cfifa · s-ladder

`#s-kwh`, `#s-shape` and `#s-think` are full sections and none is a rail
stop. Design's audit: "p2-04 drops UNIT, SHAPE and THINK". All three keep
their `id` — and `#s-think` must, because this page's tutor link
points at it.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ────────────────

    #s-kwh     `ks3-block`                    → `check`
    #s-bill    `ks3-block`                    → `check`
    #s-shape   `ks3-block`                    → (a `formula` block)
    #s-think   `ks3-block ks3-misconception`  → `misconception`

── ⚖️ TWO MINTS ──────────────────────────────────────────────────────

`ENER-25` is a unit misread: a compound unit is read as its first word, so
a kilowatt-hour is taken for a power. `ENER-26` is a belief about the BILL
rather than about the physics — that the whole of it responds to usage
— and it survives even in a student who has `ENER-25` right. Two roots,
two rows.

Design's `NOTES-P2.md` §1 predicts one (her `ENERGY-13`); the second quote
arrived with her 23 Aug audit. Same gap, same resolution: the drawing was
measured.

── ⚠️ PRICE AND STANDING CHARGE ARE TWO NAMED CONSTANTS ──────────────

27p per kWh and 53p per day, over a 30-day month. Design's flag 12 records
that they are plausible mid-2020s UK values rather than live figures, and
that she isolated them as constants precisely because they will date. They
are constants here for the same reason. They are not a quotation and the
page does not present them as one.

⊕ RULED 30 Aug 2026 (MRB-297) — DATE THE MONEY, WHERE SHOWN. The figures
stay at 27p and 53p; only the dating changes. The cap moves quarterly, so
ONE clause in the hook (`phenomenon.prompt`) dates the whole page, and the
p2-03 bench readout label carries Mide's own "(2026)". A figure that is a
STIPULATED INPUT to a calculation — a ladder stem, a bank stem, a CFIFA
line — is not dated again: the question supplies its own price and no
reader takes it as a claim about today. A figure that is a claim about the
WORLD is dated: `#s-think`'s "around 53p a day here in 2026".

⊕ RULED 30 Aug 2026 (MRB-297) — THE GAS BILL. `stretch` gains a second
entry covering the gas meter's m³ → kWh conversion, closing
`KS3.P.FUEL.04` properly. The title, `covers` and the rail are unchanged.
"""

LESSON = {
    "slug":  "reading-a-fuel-bill",
    "title": "Reading a fuel bill",
    "discipline": "physics",
    "unit": "Energy at home",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.FUEL.04"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 12}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["calculating-energy-transferred"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "A real bill says “units used: 412” and "
                        "charges 27p each, and never once says what a unit "
                        "is. Build the bill row by row — and meet the "
                        "one calculation in KS3 that needs two different "
                        "diagrams.",

    "big_question": "A real electricity bill lists “units used: "
                    "412” and charges 27p for each one. Nowhere on the "
                    "page does it say what a unit is. What have you been "
                    "buying?",

    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "412 units",           "done_when": "committed"},
        {"anchor": "s-bill",  "short": "BILL",
         "label": "Build the bill",      "done_when": "bill_built"},
        {"anchor": "s-cfifa", "short": "CFIFA",
         "label": "Five lines on a row", "done_when": "both_attempts_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",      "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "412 of something, at 27p each.",
        # ⚖️ RULED 30 Aug 2026 (MRB-297) — ONE dating clause, here in the
        # hook, for the whole page. The prices are real 2026 figures and the
        # cap that sets them moves quarterly; the arithmetic does not.
        "prompt": "A real electricity bill lists “units used: "
                  "412” and charges 27p for each one. Nowhere on the "
                  "page does it say what a unit is — the word appears "
                  "eleven times and is never defined. The prices on this "
                  "page are 2026 ones, and the cap that sets them moves "
                  "every three months.",
        "commit": "Commit. A unit on an electricity bill is one…",
        "options": [
            "Kilowatt — a measure of power",
            "Kilowatt-hour — a measure of energy",
            "Joule — the standard measure of energy",
            "Watt per hour — a measure of energy used",
        ],
        "answer": 1,
        "reveal": "One kilowatt-hour — the energy a 1 kW appliance "
                  "transfers in one hour, which is 3 600 000 joules. "
                  "<strong>It is a unit of energy, not power</strong>, "
                  "despite starting with the word kilowatt. Every fuel bill "
                  "in the country is written in it and almost none of them "
                  "explain it.",
    },

    "misconceptions": [
        {"id": "ENER-25",
         "statement": "A kilowatt-hour is a measure of power — it has "
                      "kilowatt in the name.",
         "elicited_by": "s-hook",
         "confronted_by": "kwh-rectangles"},
        {"id": "ENER-26",
         "statement": "Switch everything off and the bill goes to zero.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "This lesson is the one place where the arithmetic of the "
                 "last two lessons meets money. A bill is a list of products "
                 "— power times time, appliance by appliance — "
                 "added together. <strong>That structure matters, because it "
                 "is a sum of products, and the way you write it down has to "
                 "show both.</strong>"},

        # ── #s-kwh · one kilowatt-hour, four ways. NOT a rail stop. ─────
        {"type": "kwh-rectangles",
         "id": "kwh-rectangles",
         "anchor": "s-kwh",
         "eyebrow": "What one unit actually is",
         "heading": "One kilowatt-hour, four ways",
         "prompt": "The same amount of energy, spent four different ways. "
                   "Pick each one and watch the product come out the same.",
         # ⚖️ EQUAL AREA IS THE CLAIM. Each rectangle is `w` wide and `h`
         # tall in the instrument's own units, and every one has an area of
         # exactly 1 kWh. The renderer checks it rather than trusting it.
         "ways": [
             {"id": "k1", "label": "1 kW for 1 hour",
              "watts": 1000, "hours": 1.0,
              "note": "The definition, straight off the label: a "
                      "one-kilowatt heater, running for one hour."},
             {"id": "k2", "label": "2 kW for 30 min",
              "watts": 2000, "hours": 0.5,
              "note": "Twice the power, half the time. Same product, same "
                      "unit on the bill, same 27p."},
             {"id": "k3", "label": "100 W for 10 hours",
              "watts": 100, "hours": 10.0,
              "note": "A tenth of the power for ten times as long. Still one "
                      "unit — which is why a forgotten lamp matters."},
             {"id": "k4", "label": "9 W LED for 111 hours",
              "watts": 9, "hours": 111.1,
              "note": "Nearly five days of continuous light for a single "
                      "unit. This is what replacing filament bulbs actually "
                      "bought."},
         ],
         "alt": "Four rectangles of equal area. Each is a different width "
                "and height — power against time — and every one "
                "encloses exactly one kilowatt-hour.",
         "close": "Four different shapes, one area. That area is the unit "
                  "you are billed for."},

        {"type": "key-fact", "ref": "a-unit-is-a-kilowatt-hour"},

        # ── #s-bill · the bill builder ─────────────────────────────────
        {"type": "bill-builder",
         "id": "bill-builder",
         "anchor": "s-bill",
         "eyebrow": "Build the bill · a sum of products",
         "heading": "Set the household's habits and watch the total.",
         # ⊕ MRB-297 · 1 Sep 2026. This said the motor "only runs about
         # half" the day, and the row below started at 12 h. At 90 W that
         # is 1.08 kWh a day, which is about twice a real fridge-freezer
         # (0.4-0.55 kWh) and 2.25 times what this page's own CFIFA
         # teaches a few blocks down (120 W for 4.0 h = 0.48 kWh). The
         # CFIFA is the one that is right, so the bench moved to it: the
         # row now starts at 5 h, giving 0.45 kWh a day.
         "prompt": "Five appliances, five sliders. Each row is a product; "
                   "the bottom line is their sum, plus a standing charge "
                   "that no slider can touch. The hours are the hours a "
                   "thing is drawing power — a fridge is plugged in all "
                   "day, but its motor only runs a few hours of it.",
         "gate": {
             "prompt": "Commit first. In a typical UK home, which of these "
                       "is usually the largest single item on the "
                       "electricity bill?",
             # ⚠️ MRB-177 — Design's correct option is six words against a
             # longest distractor of four, which is a length tell by the
             # ruled measure. Her four CLAIMS are unchanged and in her
             # order; the weights are evened so the set is decided by
             # reading. Engine policy, not a science departure.
             "options": [
                 "Lighting, throughout the whole house",
                 "Phone and laptop chargers, left plugged in",
                 "Heating water — the shower, kettle and oven",
                 "The television, on most of the evening",
             ],
             "answer": 2,
         },
         # ⚖️ RULED 30 Aug 2026 (MRB-297) — these are 2026 UK figures and the
         # price cap that sets them moves quarterly. They are NOT rendered as
         # authored text: `build_ks3.py` emits them as `data-price` /
         # `data-standing` for the instrument, so the dating a reader sees is
         # the hook's clause, not a label here. If the instrument ever paints
         # the tariff into the DOM, that label wants "(2026)" too.
         "price_per_kwh": 0.27,
         "standing_per_day": 0.53,
         "days": 30,
         "columns": ["Appliance", "Power", "Hours per day",
                     "Units in 30 days", "Cost"],
         "rows": [
             {"id": "shower", "name": "Electric shower", "watts": 8500,
              "min": 0, "max": 60,  "start": 20, "unit": "min/day",
              "per_hour": 60},
             {"id": "oven",   "name": "Oven and hob",    "watts": 2200,
              "min": 0, "max": 180, "start": 50, "unit": "min/day",
              "per_hour": 60},
             {"id": "kettle", "name": "Kettle",          "watts": 2000,
              "min": 0, "max": 60,  "start": 12, "unit": "min/day",
              "per_hour": 60},
             # ⊕ MRB-297 · 1 Sep 2026 — `start` was 12. See the prompt.
             {"id": "fridge", "name": "Fridge-freezer",  "watts": 90,
              "min": 0, "max": 24,  "start": 5, "unit": "h/day",
              "per_hour": 1},
             {"id": "lights", "name": "Lighting, whole house", "watts": 72,
              "min": 0, "max": 24,  "start": 5,  "unit": "h/day",
              "per_hour": 1},
         ],
         "alt": "An itemised electricity bill. Five appliance rows, each "
                "with its power, its hours per day, the units it uses in "
                "thirty days and what those cost — then a standing "
                "charge and a total.",
         "close": "Every row responds to its slider. The standing charge "
                  "does not respond to anything."},

        # ── #s-shape · MRB-204's two shapes. NOT a rail stop. ──────────
        {"type": "formula",
         "id": "bill-shape",
         "anchor": "s-shape",
         "eyebrow": "Writing it down · two shapes in one calculation",
         "statement": "amount due = (row + row + row + row + row) + "
                      "standing charge",
         "support": [
             "each row is power in kilowatts × time in hours — a "
             "product",
             "the amount due is every row added — a sum",
             "no single diagram does both jobs, so the drawing does both",
         ],
         # ⚖️ A BALANCE, NOT A TRIANGLE. See the MRB-204 note at the top.
         # The per-row triangles are drawn on the left pan, inside this
         # figure, which is why there is no separate `triangle` key.
         "figure": {
             "shape": "balance",
             "caption": "a sum of products — triangle for one row, "
                        "balance for the total",
             "pans": {"left": "every row, added",
                      "right": "amount due"},
             "aria_label": "A level balance beam. On the left pan, a stack "
                           "of the five appliance rows plus the standing "
                           "charge, each row drawn as a small formula "
                           "triangle because each row is a product. On the "
                           "right pan, the single amount due. The two are "
                           "equal.",
         }},

        # ⚠️ Design's second `#s-shape` paragraph is an EXPLAINER, not part
        # of the formula block. `r_formula` reads `statement`, `support`,
        # `eyebrow`, `figure`, `triangle` and `cover` and NOTHING else — a
        # `close` authored on it would be dropped in silence, which is what
        # `ks3_key_audit.py` exists to catch.
        {"type": "explainer",
         "text": "Read it as a balance: everything on the left pan, added, "
                 "equals the amount due on the right. Change any one row and "
                 "the beam stays level — the total simply follows. This "
                 "is the same shape you met for conservation of energy, and "
                 "for the same reason: <strong>whenever the top-level "
                 "relationship is an addition, a triangle would teach you a "
                 "relationship that does not exist.</strong>"},

        # ── #s-cfifa · one row, five lines ─────────────────────────────
        {"type": "worked-example", "id": "cfifa-bill-plain",
         "anchor": "s-cfifa"},
        {"type": "worked-example", "id": "cfifa-bill-convert"},

        # ── #s-think · NOT a rail stop ─────────────────────────────────
        {"type": "misconception", "id": "think-kwh-is-power",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        {"id": "think-kwh-is-power",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-25",
         "statements": [
             {"quote": "A kilowatt-hour is a measure of power — it has "
                       "kilowatt in the name.",
              "targets": "ENER-25",
              "body": [
                  "The “hour” on the end is the giveaway: a time "
                  "has already been multiplied in, which turns a rate into a "
                  "total. A kilowatt is a rate. <strong>A kilowatt-hour is a "
                  "rate multiplied by a time, and a rate times a time is "
                  "always an amount.</strong>",
                  "It is worth saying what the amount is. One kilowatt-hour "
                  "is 1000 W × 3600 s = 3 600 000 J. Bills are written "
                  "in it rather than in joules for the same reason "
                  "shopkeepers do not price flour by the grain.",
              ]},
             {"quote": "Switch everything off and the bill goes to zero.",
              "targets": "ENER-26",
              "body": [
                  "The units do; the standing charge does not. It is a fixed "
                  "daily amount for being connected to the network — "
                  "around 53p a day here in 2026, or about £16 a month "
                  "— and it is on the bill whether you use one unit or "
                  "a thousand. "
                  "<strong>That is why the cheapest month is never free, and "
                  "why comparing suppliers on unit price alone is not "
                  "enough.</strong>",
              ]},
         ]},

        {"id": "cfifa-bill-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines on one row · CFIFA",
         "heading": "An oven rated 2.0 kW runs for 1.5 hours. How many units "
                    "does it use?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Now the same five steps where the rating "
                                  "does need converting."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "2.0 kW stays 2.0 kW · 1.5 h stays 1.5 h",
              "note": "A unit is a kilowatt-hour, and the rating is already "
                      "in kilowatts and the time already in hours, so there "
                      "is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "units = power in kW × time in hours",
              "note": "Two quantities multiplied — one row of a bill."},
             {"letter": "I", "label": "Insert",
              "line": "units = 2.0 kW × 1.5 h",
              "note": "The kilowatt and the hour are what make the answer a "
                      "kilowatt-hour."},
             {"letter": "F", "label": "Fine-tune",
              "line": "2.0 × 1.5 = 3.0",
              "note": "Kilowatts times hours leaves kilowatt-hours."},
             {"letter": "A", "label": "Answer",
              "line": "units = 3.0 kWh",
              "note": "Three units, which at 27p each is 81p."},
         ]},

        # ⚖️ RULED 30 Aug 2026 (MRB-297) — P2-24. This example was "A 900 W
        # fridge compressor", which is a commercial chiller, disagrees
        # tenfold with this page's own bill row (Fridge-freezer 90 W) and
        # with `p2-03`'s bench, and put a domestic fridge at 3.6 kWh a day.
        # 120 W over a 4.0 h duty cycle is a real fridge: 0.120 × 4.0 =
        # 0.48 kWh. The ÷1000 step the example exists to teach survives,
        # and the Answer note's wrong-conversion figure (480 units a day)
        # is now true against this page's own household of 412 a month.
        {"id": "cfifa-bill-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines on one row · CFIFA",
         "heading": "A 120 W fridge compressor runs for 4.0 hours a day. How "
                    "many units in a day?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Both are open. One row done five times "
                                  "is the whole of a bill."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "120 W ÷ 1000 = 0.120 kW",
              "note": "A unit is a kilowatt-hour, so a rating printed in "
                      "watts has to become kilowatts first."},
             {"letter": "F", "label": "Formula",
              "line": "units = power in kW × time in hours",
              "note": "Two quantities multiplied — one row of a bill."},
             {"letter": "I", "label": "Insert",
              "line": "units = 0.120 kW × 4.0 h",
              "note": "The converted rating goes in. The 120 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "0.120 × 4.0 = 0.48",
              "note": "Kilowatts times hours leaves kilowatt-hours."},
             {"letter": "A", "label": "Answer",
              "line": "units = 0.48 kWh",
              "note": "Insert 120 instead of 0.120 and the fridge comes out "
                      "using 480 units a day — more than the whole house "
                      "uses in a month."},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "a-unit-is-a-kilowatt-hour",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "One unit on a bill is one kilowatt-hour: 3 600 000 J. It "
                 "is an amount of energy, not a power. Cost = units × "
                 "price per unit."},
    ],

    "ladder": {
        "recall": {
            "q": "One unit on an electricity bill is one…",
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": ["joule", "kilowatt", "kilowatt-hour",
                        "watt per hour"],
            "answer": 2,
            "feedback": {
                0: "A joule is far too small to bill in — one unit is "
                   "3 600 000 of them.",
                1: "A kilowatt is a power. A unit is an amount of energy "
                   "— the “hour” is doing essential work.",
                3: "Not a real unit. Watts already contain “per "
                   "second”; dividing again gives nothing useful.",
            }},
        "apply": {
            "q": "A 2.2 kW oven runs for 45 minutes a day for 30 days, at "
                 "27p a unit. What does it cost?",
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": ["About £29.70", "About £0.45", "About £802",
                        "About £13.37"],
            "answer": 3,
            "feedback": {
                0: "That looks like the oven running a full hour a day and "
                   "then some. Check the 0.75 h.",
                1: "That is one day. The question asks for 30 days.",
                2: "You have probably used 45 minutes as 45 hours. Convert "
                   "to 0.75 h first.",
            }},
        "explain": {
            "q": "A household uses 412 units in 30 days at 27p a unit, plus "
                 "a standing charge of 53p a day. Work out the bill, and "
                 "explain why cutting their usage by half would not halve "
                 "what they pay.",
            "field_label": "Your working and explanation",
            "placeholder": "412 × 0.27 = …",
            "success": [
                "Calculates the usage charge as 412 × £0.27 = £111.24.",
                "Calculates the standing charge as 30 × £0.53 = £15.90.",
                "Adds them to give a total of about £127.14.",
                "Says the standing charge does not change with usage.",
                "Concludes that halving usage gives about £71.52, which is "
                "more than half of £127.14 — so the saving is less than "
                "50 per cent.",
            ]},
        "produce": {
            "q": "A family is told to “switch off lights to save "
                 "money”. Using the bill you built, say whether that is "
                 "the best advice available to them, and justify your answer "
                 "with numbers.",
            "field_label": "Your answer",
            "placeholder": "Lighting the whole house at 72 W for 5 hours a "
                           "day is…",
            "success": [
                "Calculates the lighting figure — roughly 0.36 kWh a "
                "day, about 11 units a month.",
                "Compares it with a larger item such as the shower or the "
                "oven, with a number.",
                "Concludes that lighting is a small share of the bill.",
                "Identifies where the bigger savings actually are, and says "
                "why.",
                "Notes that the standing charge cannot be reduced by any "
                "change in behaviour.",
            ]},
    },

    "key_note": "A unit is a kilowatt-hour, which is energy, not power. "
                "Cost = units × price. A bill is a sum of products "
                "— triangle for a row, balance for the total. And a "
                "standing charge is owed whether you use anything or not.",

    "stretch": [
        {"id": "why-a-standing-charge-exists",
         "type": "explainer",
         "text": "The standing charge is the line people argue about, and it "
                 "is worth understanding why it exists rather than just "
                 "resenting it. The cables, substations, meters and the crew "
                 "who come out when a line goes down all cost the same "
                 "whether your house draws 400 units a month or none "
                 "— so that cost is billed per day rather than per "
                 "unit. It has a consequence that catches people out: "
                 "<strong>a household that cuts its usage in half does not "
                 "halve its bill, because a fixed portion never "
                 "moves.</strong> If you ever want to work out what a "
                 "genuine saving would be worth, the standing charge has to "
                 "come out of the calculation first, and it is the one row "
                 "on the bill that no change in behaviour will touch."},

        # ⚖️ RULED 30 Aug 2026 (MRB-297) — THE GAS BILL. The lesson claims
        # `KS3.P.FUEL.04`, "domestic fuel bills, fuel use and costs", and
        # covered electricity only. Gas is the larger bill in most UK homes.
        # Ruled: cover it HERE, in Going further, and keep the title — so
        # `covers` is unchanged and no new statutory claim is added. The VAT
        # clause folds in. The conversion is the one printed on every UK gas
        # bill; 1.02264 is the regulator's volume correction factor, 39.5 the
        # calorific value in MJ/m³ (it genuinely varies, ~37.5–43.0), and
        # ÷3.6 is MJ→kWh because 1 kWh = 3.6 MJ. Worked check:
        # 100 × 1.02264 = 102.264 → × 39.5 = 4039.428 MJ → ÷ 3.6 = 1122.06 kWh.
        {"id": "what-a-gas-meter-actually-measures",
         "type": "explainer",
         "text": "Gas is the other half of most fuel bills, and its meter "
                 "counts volume, not energy: the number in the little window "
                 "is cubic metres of gas that have gone past, and that is not "
                 "the number you are billed for. The bill converts it with a "
                 "formula printed on every UK gas bill — kWh = m³ × "
                 "1.02264 × 39.5 ÷ 3.6. The 1.02264 is a volume "
                 "correction factor, fixed by the regulator, bringing the "
                 "measured volume to a standard temperature and pressure. The "
                 "39.5 is the calorific value in megajoules per cubic metre "
                 "— how much energy that gas carries. The network "
                 "measures it and prints it on the bill, and it does vary, "
                 "roughly 37.5 to 43.0, with where the gas came from. "
                 "Dividing by 3.6 turns megajoules into kilowatt-hours, "
                 "because one kilowatt-hour is 3.6 MJ. So 100 m³ gives "
                 "100 × 1.02264 = 102.264, then × 39.5 = 4039.4 MJ, "
                 "then ÷ 3.6 = 1122 kWh. Domestic energy is charged VAT "
                 "at 5 per cent, not the standard 20. <strong>The unit at the "
                 "end is the same kilowatt-hour the electricity side is "
                 "billed in</strong> — which is what lets you compare "
                 "the two halves of a bill."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "unit (on a bill)",
         "definition": "One kilowatt-hour, 3 600 000 J. An amount of energy, "
                       "and what the price per unit is charged against."},
        {"term": "standing charge",
         "definition": "A fixed daily amount for being connected to the "
                       "network. It does not change with how much you use."},
        {"term": "sum of products",
         "definition": "A total made by multiplying within each row and then "
                       "adding down the column. It needs two diagrams, not "
                       "one."},
    ],

    "tutor": {
        "anchor": "s-think",
        "prompt": "Ask Mr Badmus AI",
        "body": "Still unsure whether kWh is power or energy?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Domestic energy costs, and the National Grid's role in "
                   "matching supply to demand.",

    "ws": ["analysis-and-evaluation"],
}
