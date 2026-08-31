"""P2 L1 — Energy in food (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p2/p2-01-energy-in-food.dc.html`.

Her page wins outright. Every food, every capture fraction, every rung and
every line of the two notes below is hers; what this file adds is the
engine's shape and the rulings the record has to carry.

⊕ AMENDED MRB-297, 31 Aug 2026 — the sentence above is no longer true of
one food and is kept rather than deleted so the provenance is not silently
overstated. Design's second sample was a peanut; Mide ruled it out of the
practical on 30 Aug 2026 and a cheese puff replaces it. Its energy figure,
its capture fraction, its note, the commit-gate option that named it and
rung 3's two numbers are this repository's, not hers. The other three foods
are untouched. Full row in `DEPARTURES-P2.md` as D-P2-02.

── ⚖️ RULED · THIS LESSON OWNS THE FOOD-ENERGY FIGURES ──────────────────

`KS3.P.FUEL.01` — "comparing energy values of different foods (from labels)
(kJ)" — is a single statement and this is a single lesson, so unlike P1
nothing is split. `structure.py` §4.6 makes this the OWNER: Biology B3's
`a-balanced-diet` carries the `⇄ Owned by Physics P2` marker and references
this lesson rather than duplicating it. Design's endmatter names B3 under
"Also used by". When B3 is authored it must link here and must NOT restate
the energy figures — one owning lesson, referenced from elsewhere, never
two copies.

── ⚖️ RULED · THE CALORIMETER READS LOW ON PURPOSE ──────────────────────

Design's science flag 1 asks for a ruling and this is it: the capture
fractions stay exactly as she set them (0.30–0.46), and the bench keeps
reading 30–46% of the label figure.

That gap IS the lesson. Rung 3's fifth criterion is that repeating a
measurement does nothing about a systematic leak, and it can only be
answered by a student who has watched their own value come out low. Every
error source she names runs ONE WAY — energy escaping the flame into the
room, the glass absorbing some, the sample not burning out — so none of
them could ever push the reading high. "Fixing" the fractions to match the
labels would leave a bench that agrees with the packet and a rung that
cannot be answered from it.

── ⚖️ RULED · 1 kcal = 4.18 kJ, NOT 4.2 ────────────────────────────────

Design's flag 3 offers 4.2 for arithmetic simplicity. Kept at 4.18, for a
reason internal to the page rather than to taste: her hook quotes a real
packet, 229 kcal and 958 kJ, and 229 × 4.18 = 957.2, which rounds to the
958 printed. At 4.2 it gives 961.8 and the hook's own arithmetic stops
landing on the number the student can read off the bag. The constant and
the worked example are the same constant, so it cannot be changed in one
place only.

── ⚖️ MRB-204 · TRIANGLE, AND IT IS THE RIGHT SHAPE ────────────────────

`E = e × m` is a genuine product — energy per gram multiplied by a mass —
so `A = B × C` holds and the triangle encodes a relationship that exists.
Checked against the arithmetic, not against the habit of drawing one.
Design draws it as a triangle and says so on the canvas. Nothing in this
lesson is a sum, so no beam appears.

── ⚠️ FOUR RAIL STOPS · `s-think` IS NOT ONE ───────────────────────────

Measured off Design's own `RAIL` constant:

    s-hook · s-burn · s-worked · s-ladder

`#s-think` is a full section with a commit and it is NOT on the rail —
the `NOTES-C9` §10 correction, which drops the misconception block's stop
where the lesson has a fuller third section. `#s-worked` is that section
here. The id is kept, so the in-page anchor and the tutor link still work.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ─────────────────

    #s-burn    `ks3-block`                    → `check`
    #s-think   `ks3-block ks3-misconception`  → `misconception`

── ⚖️ RULED · THE FAMILY IS `ENER`, AND THIS LESSON RE-USES ONE ────────

Design's `NOTES-P2.md` §1 says this lesson "re-confronts `ENERGY-01`". No
`ENERGY-` id exists or may exist — the register's ruling is explicit that
a physics lane meeting an energy misconception adds to `ENER`. Her
`ENERGY-01` is this repository's **`ENER-09`** ("energy gets used up"),
minted by `p1-01`, and its `reappears_in` list predicted exactly this
arrival. So the gym quote re-confronts `ENER-09` and mints nothing.

The SECOND quote is a different matter. "A calorie on a food label is the
same calorie physicists use" is not an energy-conservation error at all —
it is a units error, and a student can hold it while being perfectly sound
on stores. It is confronted in its own panel with its own arithmetic, so
it is minted here as **`ENER-20`**.

⚠️ Design's §1 table predates that second quote: her notes are 15 Aug and
the second misconception quote was added to all sixteen P1–P3 lessons by
her own 23 Aug audit (§2). Reported, not escalated — the drawing is newer
than the note and the drawing was measured.

── ⚠️ NO MARKUP IN A RUNG QUESTION ─────────────────────────────────────

`r_ladder` puts a rung's `q` through `t()`, which escapes. Rung prose that
wants emphasis finds it in word order instead.
"""

LESSON = {
    "slug":  "energy-in-food",
    "title": "Energy in food",
    "discipline": "physics",
    "unit": "Energy at home",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.FUEL.01"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 9}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["simple-machines"],
    "assumes": [],
    "references": ["energy-stores"],
    "ks4_links": [],

    "meta_description": "A packet says 229 kcal and also 958 kJ for the same "
                        "crisps. Neither is a mistake. Burn a weighed sample "
                        "under 20 g of water, measure the rise, and find out "
                        "why your answer comes out well below the label.",

    "big_question": "A packet says “229 kcal” and also “958 "
                    "kJ”. Two completely different numbers for the same "
                    "crisps. Is one of them wrong?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Two numbers",    "done_when": "committed"},
        {"anchor": "s-burn",   "short": "BURN",
         "label": "Calorimeter",    "done_when": "three_runs_recorded"},
        {"anchor": "s-worked", "short": "CFIFA",
         "label": "CFIFA",          "done_when": "both_attempts_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two numbers, one packet.",
        "prompt": "Every food label in the country carries both. A 50 g bag "
                  "of crisps: 229 kcal, 958 kJ. Neither number is a mistake "
                  "and neither is a rounding of the other.",
        "commit": "Commit to why there are two.",
        # ⚑ MRB-177 — Design's four kept verbatim. Each is a sentence a real
        # student says, and only B names two units for one quantity.
        # ⊕ AMENDED MRB-297, 31 Aug 2026 — the line above is no longer true of
        # all four and is kept rather than deleted so the provenance is not
        # silently overstated. The CORRECT option is still hers, byte for
        # byte. Distractors were re-authored to the same length and shape,
        # because Design's terse ones made the correct option the visibly
        # longest and a student could answer this hook without reading it.
        "options": [
            "Calories are what your body uses; joules are the total in the "
            "food",
            "They are the same energy in two different units",
            "One number is for the fat and the other is for the carbohydrate",
            "The kJ figure counts the packaging as well as the food itself",
        ],
        "answer": 1,
        "reveal": "They are the same amount of energy in two different units, "
                  "like 6 feet and 1.83 metres. One kilocalorie is 4.18 "
                  "kilojoules, and 229 × 4.18 gives 957 — which "
                  "rounds to the 958 on the packet. The joule is the "
                  "scientific unit; the calorie survives on labels because "
                  "people are used to it. <strong>Nothing about the crisps "
                  "changes.</strong>",
    },

    "misconceptions": [
        {"id": "ENER-09",
         "statement": "Energy gets used up. When something stops, the energy "
                      "it had has been spent and is gone.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "ENER-20",
         "statement": "A calorie on a food label is the same calorie a "
                      "physicist uses.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Food is a chemical store, and like any store it holds a "
                 "measurable number of joules. This lesson <em>measures</em> "
                 "it — with an instrument that gets an answer close to "
                 "the label and not identical to it, which is the honest "
                 "result and worth understanding."},

        # ── #s-burn · the calorimeter ────────────────────────────────────
        {"type": "calorimeter",
         "id": "food-calorimeter",
         "anchor": "s-burn",
         "eyebrow": "The calorimeter · burn it and watch the water",
         "heading": "Measure the store, do not look it up.",
         "prompt": "A weighed sample of food burned under a boiling tube "
                   "holding 20 g of water. The energy released warms the "
                   "water, and the temperature rise tells you how much.",
         "gate": {
             "prompt": "Commit first. Which of these do you expect to hold "
                       "the most energy per gram?",
             # ⚖️ MRB-297 · the peanut goes here too. The answer stays at
             # index 1 and stays correct: among the four offered, the puff
             # at 21.6 kJ/g beats cheese at 17.0 and pasta at 15.0. The
             # gate asks "which of these", and the crisps are not offered.
             "options": [
                 "Dry pasta — it is pure carbohydrate",
                 "A cheese puff — it is mostly fat",
                 "Cheese — it is the heaviest",
                 "They are all about the same per gram",
             ],
             "answer": 1,
         },
         "water_g": 20,
         "shc": 4.18,
         # ⚠️ D-P2-01 — Design's slider is 5-30 g, which puts her own
         # thermometer between 295 °C and 4469 °C in every state it can
         # reach. See DEPARTURES-P2.md. The water, the constant, the foods
         # and the capture fractions are all hers and all unchanged, and
         # because the measured kJ/g divides the mass back out, no number
         # this lesson teaches moves.
         "mass_min": 0.10,
         "mass_max": 0.50,
         "mass_step": 0.05,
         "mass_start": 0.30,
         "start_food": 1,
         "runs_to_record": 3,
         # ⚖️ CAPTURE FRACTIONS ARE THE LESSON. See the ruling above.
         # ⚖️ MRB-297 · THE PEANUT IS OUT. Ruled by Mide, 30 Aug 2026: a nut
         # in a classroom is not a wording problem, and no safety note
         # protects a child who reacts to airborne particles from burning
         # nut. Design's second sample was a peanut at 24.5 kJ/g, capture
         # 0.46. A cheese puff replaces it — the standard UK non-nut
         # sample, extruded and high in fat, so it lights at once and
         # burns steadily on a mounted needle, which is the only property
         # the peanut was here for. The bench keeps its comparison.
         #
         # ⚠️ IT IS NO LONGER THE HIGHEST OF THE FOUR, AND THAT IS HONEST.
         # The crisps at 22.0 now top the bench. No non-nut classroom food
         # beats a crisp on energy density, because a crisp is already
         # about a third fat and near the ceiling for a dry snack, and
         # nuts led precisely because they are about half fat. The figure
         # is not adjusted to preserve the old ordering.
         "foods": [
             {"id": "crisp",  "label": "Crisps",      "kj_per_g": 22.0,
              "capture": 0.42,
              "note": "Crisps are largely fat, and fat is the densest store "
                      "in food — about 37 kJ per gram on its own."},
             # ⚑ 21.6 kJ/g is the UK nutrition label, not an estimate:
             # 2156 kJ per 100 g (516 kcal), fat 30.3 g per 100 g.
             # ⚑ 0.38 is a MODELLING CONSTANT, not a measurement. Capture
             # is a property of the bench, not of the food. A puffed snack
             # is mostly air, so it flares fast and more of what it
             # releases goes sideways into the room than a dense peanut's
             # did — below the peanut's 0.46, inside the ruled 0.30–0.46.
             {"id": "puff",   "label": "Cheese puff", "kj_per_g": 21.6,
              "capture": 0.38,
              "note": "Mostly fat and air. It lights at once and burns "
                      "steadily, which is why a prep room reaches for a "
                      "puffed snack."},
             {"id": "pasta",  "label": "Dry pasta",   "kj_per_g": 15.0,
              "capture": 0.34,
              "note": "Mostly carbohydrate, at roughly 17 kJ per gram — "
                      "well under half of fat."},
             {"id": "cheese", "label": "Cheese",      "kj_per_g": 17.0,
              "capture": 0.30,
              "note": "Fatty, but wet — and the water in it soaks up "
                      "energy without ever reaching your thermometer."},
         ],
         "columns": ["Run", "Food", "Mass", "Rise", "Energy per gram"],
         "burn_label": "Burn the sample",
         "fresh_label": "Fresh sample",
         "record_label": "Record this run",
         "alt": "A calorimeter: a weighed food sample burning under a boiling "
                "tube holding 20 grams of water, with a thermometer in the "
                "water and orange specks of escaping energy leaving the "
                "flame sideways.",
         "close": "Every value you record is well below the packet figure, "
                  "and every one is low for the same reasons — which is "
                  "the difference between a systematic error and a scatter."},

        {"type": "key-fact", "ref": "energy-is-density-times-mass"},

        # ── #s-worked · the formula, then CFIFA ─────────────────────────
        # ⚖️ MRB-204: a genuine product, so a triangle. Arrows here are SVG;
        # the only typed arrows in this file are in prose.
        # ⚠️ NO ANCHOR ON THE FORMULA — MRB-208. A `formula` block
        # carries no demand and emits no `data-stage-done`, so a rail stop
        # anchored to it can never tick: `doneByDom()` finds none of the
        # signals it reads and the stop is dead. Design draws the statement,
        # the triangle and the CFIFA inside one `#s-worked`; the engine
        # renders one section per block, so the id goes on the block that
        # can actually complete — the worked example, which is what this
        # stop's own label ("CFIFA") names anyway.
        {"type": "formula",
         "id": "energy-density-rule",
         "eyebrow": "Five lines, every time · CFIFA",
         "statement": "Energy in a portion = energy per gram × mass",
         "support": [
             "energy in the portion, E, is measured in kilojoules (kJ)",
             "energy per gram, e, is measured in kilojoules per gram (kJ/g)",
             "mass of the portion, m, is measured in grams (g)",
         ],
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Total energy E sits above a "
                           "dividing line; energy per gram e and mass m sit "
                           "below it, multiplied together. Covering one "
                           "letter leaves the way to work it out.",
             "top":   {"label": "E", "button": "Cover E",
                       "text": "Energy sits alone at the top. Cover it and "
                               "the other two are side by side — "
                               "multiply."},
             "left":  {"label": "e", "button": "Cover e",
                       "text": "Energy per gram sits underneath with total "
                               "energy above. Cover it and you get E over m "
                               "— divide."},
             "right": {"label": "m", "button": "Cover m",
                       "text": "Mass sits underneath with total energy "
                               "above. Cover it and you get E over e — "
                               "divide."},
             "close": "Two things side by side means multiply. One thing "
                      "over another means divide.",
         }},

        {"type": "worked-example", "id": "cfifa-food-plain",
         "anchor": "s-worked"},
        {"type": "worked-example", "id": "cfifa-food-convert"},

        # ── #s-think · NOT a rail stop ──────────────────────────────────
        {"type": "misconception", "id": "think-burned-off", "anchor": "s-think"},

        {"type": "key-fact", "ref": "chemical-store-filled-and-emptied"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        # ── #s-think · BOTH of Design's quotes, in her order ────────────
        # ⚠️ NO COMMIT WIDGET HERE, AND IT IS NOT AN OVERSIGHT. Design draws a
        # commit inside every `#s-think` in P1-P3. The engine's `misconception`
        # block renders `r_confrontation` FIRST and the generic
        # prompt/options/reveal branch AFTER it, so a commit authored here
        # would appear BELOW both quotes rather than between them, which
        # inverts her order and makes the second quote read as part of the
        # first one's reveal. All eight live P1 lessons resolve this the same
        # way — both quotes and all their prose, no commit — and P2
        # follows P1 rather than splitting the treatment mid-key-stage.
        # Reported as a design flag; not a departure, because nothing of hers
        # is changed, only a widget the engine cannot place where she drew it.
        {"id": "think-burned-off",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-09",
         "statements": [
             {"quote": "You burn off the calories at the gym, and then they "
                       "are gone.",
              "targets": "ENER-09",
              "body": [
                  "Nothing is destroyed at the gym. The chemical store in "
                  "the food empties, a small part of it fills a kinetic "
                  "store while you are actually moving, and almost all of it "
                  "ends up as a thermal store in you and the room — "
                  "which is why a gym is warm and why you sweat. Weigh the "
                  "room's air and you would find the energy has not left the "
                  "building.",
                  "You met this belief when a rolling ball stopped, and again "
                  "when a car braked, and again when a battery went flat. "
                  "Every time, the temptation is to say the energy was "
                  "consumed, and every time the honest answer is a thermal "
                  "store somewhere unglamorous. <strong>“Burned off” "
                  "is a fair everyday phrase for “moved out of my "
                  "body's store” and a bad description of what happened "
                  "to the joules.</strong>",
                  "One more thing the calorimeter cannot tell you: burning "
                  "food in air and respiring it are not the same process, "
                  "even though the energy released is nearly identical. Your "
                  "body does it in dozens of small controlled steps at "
                  "37 °C, not in one flame — and it cannot get at "
                  "all of it, which is part of why your measured value and "
                  "the label disagree.",
              ]},
             {"quote": "A calorie on a food label is the same calorie "
                       "physicists use.",
              "targets": "ENER-20",
              "body": [
                  "It is a thousand of them. The physicist's calorie warms "
                  "one gram of water by one degree; the label's Calorie "
                  "— properly a kilocalorie — warms a kilogram. "
                  "A chocolate bar at 250 kcal is 250 000 of the small ones, "
                  "or about 1050 kJ. The kilojoule figure beside it on the "
                  "label exists precisely so that nobody has to know which "
                  "calorie is meant.",
              ]},
         ]},

        # ── CFIFA · Design's two worked examples, verbatim ──────────────
        {"id": "cfifa-food-plain",
         "kind": "worked-example",
         "demand": "apply",
         "eyebrow": "Worked example",
         "heading": "A crisp releases 22.0 kJ for every gram. What does a "
                    "30 g portion hold?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Now the same five steps where the units "
                                  "do need converting."},
         "staged": True,
         "fifa": [
                 {"letter": "C", "label": "Convert",
                  "line": "22.0 kJ/g stays 22.0 kJ/g · 30 g stays 30 g",
                  "note": "The energy density is per gram and the portion is "
                          "in grams, so there is nothing to convert."},
                 {"letter": "F", "label": "Formula",
                  "line": "E = e × m",
                  "note": "Cover E on the triangle: e sits beside m, so you "
                          "multiply."},
                 {"letter": "I", "label": "Insert",
                  "line": "E = 22.0 kJ/g × 30 g",
                  "note": "The grams on the bottom of kJ/g cancel the grams "
                          "of the portion."},
                 {"letter": "F", "label": "Fine-tune",
                  "line": "22.0 × 30 = 660",
                  "note": "Kilojoules per gram times grams gives "
                          "kilojoules."},
                 {"letter": "A", "label": "Answer",
                  "line": "E = 660 kJ",
                  "note": "Six hundred and sixty kilojoules, about 158 kcal "
                          "on a food label."},
         ]},

        {"id": "cfifa-food-convert",
         "kind": "worked-example",
         "demand": "apply",
         "eyebrow": "Worked example",
         "heading": "A cereal releases 15.0 kJ for every gram. What does a "
                    "0.045 kg portion hold?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Both worked examples are open. Now the "
                                  "same five lines on your own numbers."},
         "staged": True,
         "fifa": [
                 {"letter": "C", "label": "Convert",
                  "line": "0.045 kg × 1000 = 45 g",
                  "note": "The energy density is per gram, so the mass has "
                          "to be in grams before it can multiply."},
                 {"letter": "F", "label": "Formula",
                  "line": "E = e × m",
                  "note": "Cover E on the triangle: e sits beside m, so you "
                          "multiply."},
                 {"letter": "I", "label": "Insert",
                  "line": "E = 15.0 kJ/g × 45 g",
                  "note": "The converted mass goes in. The 0.045 never "
                          "does."},
                 {"letter": "F", "label": "Fine-tune",
                  "line": "15.0 × 45 = 675",
                  "note": "Kilojoules per gram times grams gives "
                          "kilojoules."},
                 {"letter": "A", "label": "Answer",
                  "line": "E = 675 kJ",
                  "note": "Insert 0.045 instead of 45 and the answer comes "
                          "out 0.675 kJ — a thousand times too small."},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "energy-is-density-times-mass",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Food holds a chemical store, measured in joules. Energy in "
                 "a portion = energy per gram × mass. One kilocalorie "
                 "is 4.18 kilojoules — the same energy, a different "
                 "unit."},
        {"id": "chemical-store-filled-and-emptied",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Energy in food is measured in kilojoules; the kcal a label "
                 "prints is 4.18 kJ. A portion holds energy per gram × "
                 "mass, and that chemical store is filled by eating and "
                 "emptied by everything the body does, awake or asleep."},
    ],

    "ladder": {
        "recall": {
            "q": "Cheddar holds 17 kJ per gram. How much energy is in a 30 g "
                 "portion?",
            "options": ["510 kJ", "0.57 kJ", "47 kJ", "1.76 kJ"],
            "answer": 0,
            "feedback": {
                1: "That is 17 ÷ 30. More cheese means more energy, so "
                   "this has to be a multiplication.",
                2: "That is 17 + 30, and you cannot add a per-gram figure to "
                   "a mass.",
                3: "That is 30 ÷ 17. Check which quantity belongs on "
                   "top of the triangle.",
            }},
        "apply": {
            "q": "A label reads 229 kcal and 958 kJ for the same bag. Which "
                 "statement is correct?",
            # ⚠️ MRB-278 — the correct option is NOT at index 0.
            # Across P2's ten ladder sets the answer sits at 0 three
            # times, 1 three times, 2 twice and 3 twice, so no button
            # beats reading. Each distractor keeps its OWN feedback:
            # the keys are option indices, so reordering without
            # rewriting them attaches every explanation to the wrong
            # option, silently.
            "options": [
                "The kJ figure includes energy your body cannot use",
                "They are the same energy in different units — 1 kcal "
                "is about 4.18 kJ",
                "Calories measure fat and joules measure everything",
                "The kcal figure is per bag and the kJ figure is per 100 g",
            ],
            "answer": 1,
            "feedback": {
                0: "Both figures describe the same available energy. The "
                   "difference is purely the unit.",
                2: "Neither unit is tied to a food group. Both are units of "
                   "energy.",
                3: "Labels give both units for the same stated quantity, "
                   "side by side.",
            }},
        "explain": {
            # ⚖️ MRB-297 · re-derived from the sample that replaced the
            # peanut, not carried across. The bench computes a measured
            # value of `kj_per_g × capture`, so the cheese puff reads
            # 21.6 × 0.38 = 8.208, which is 8.2 to the readout's precision;
            # the packet figure is the label itself, 21.6. Design's pair
            # was 9 against 24, off the peanut's 24.5 × 0.46. None of the
            # five success criteria quotes a figure, so none of them moves.
            "q": "Your calorimeter gives 8.2 kJ per gram for a cheese puff. "
                 "The packet says 21.6 kJ per gram. Explain three reasons "
                 "your value is lower, and say whether repeating the "
                 "measurement would fix it.",
            "field_label": "Your explanation",
            "placeholder": "Not all the energy released reached the water…",
            "success": [
                "Says energy escaped from the flame into the surrounding air "
                "instead of the water.",
                "Says some energy warmed the glass tube and the apparatus "
                "rather than the water.",
                "Says the sample may not have burned completely.",
                "Notes that every one of these errors makes the reading too "
                "low, never too high.",
                "Says repeating would not fix it, because this is systematic "
                "error rather than random scatter.",
            ]},
        "produce": {
            "q": "Two 100 g snacks have the same energy figure, but one is "
                 "mostly fat and the other mostly carbohydrate. Explain how "
                 "that is possible, and say what the energy figure alone "
                 "does not tell you about a food.",
            "field_label": "Your answer",
            "placeholder": "Fat holds about twice the energy per gram…",
            "success": [
                "Says fat holds roughly twice the energy per gram as "
                "carbohydrate or protein.",
                "Says the fatty snack must therefore contain less actual fat "
                "than the other contains carbohydrate, plus more water or "
                "fibre.",
                "Says the total energy is a product of density and mass, so "
                "different combinations can give the same total.",
                "Says the energy figure says nothing about vitamins, "
                "minerals, protein or fibre.",
                "Says two foods with equal energy can differ greatly in how "
                "useful they are to the body.",
            ]},
    },

    "key_note": "Food is a chemical store measured in joules. Fat holds "
                "about twice as much per gram as protein or carbohydrate. "
                "1 kcal = 4.18 kJ, same energy. And nothing is destroyed by "
                "exercise — it moves into a thermal store.",

    "stretch": [
        {"id": "every-error-runs-one-way",
         "type": "explainer",
         "text": "Your school calorimeter will read low — usually 20 to "
                 "60 per cent below the label — and every source of "
                 "that error is worth naming, because they are all in the "
                 "same direction. Energy escapes from the flame into the "
                 "room instead of the water. The glass of the tube absorbs "
                 "some. The sample often stops burning before it is fully "
                 "consumed. None of these could ever make the reading too "
                 "high. That one-sidedness is what tells you it is "
                 "systematic error rather than random scatter, and it is why "
                 "the professional version is a sealed steel bomb "
                 "calorimeter, pressurised with pure oxygen and immersed in "
                 "a weighed water bath — the same idea with every "
                 "escape route closed. <strong>Repeating a measurement helps "
                 "with scatter. It does nothing at all about a "
                 "leak.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        {"term": "chemical store",
         "definition": "Energy held in the arrangement of particles in fuel, "
                       "food or a battery, released when they rearrange."},
        {"term": "energy density",
         "definition": "The energy held per gram of a food, in kJ/g. Fat is "
                       "about 37, carbohydrate and protein about 17."},
        {"term": "calorimeter",
         "definition": "Apparatus that measures the energy released by a "
                       "burning sample from the temperature rise of a known "
                       "mass of water."},
        {"term": "kilocalorie",
         "definition": "The Calorie printed on a food label. One kilocalorie "
                       "is 4.18 kilojoules — the same energy, a "
                       "different unit."},
        {"term": "systematic error",
         "definition": "An error that pushes every reading the same way. "
                       "Repeating the measurement does not remove it."},
    ],

    "tutor": {
        "anchor": "s-burn",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure why your value is lower than the packet?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Specific heat capacity and the energy transferred when a "
                   "fuel or food is burned, calorimetry as a required "
                   "practical, and the difference between the energy a food "
                   "contains and the energy a body can actually get out of "
                   "it.",

    # ⚖️ MRB-297 · Mide's wording, approved 30 Aug 2026. Not to be edited.
    "safety_note": "Teacher demonstration only. Eye protection for everyone. "
                   "Burning food spits, and the boiling tube gets hot enough "
                   "to burn — a hot tube looks exactly like a cold one, so "
                   "put it on a heatproof mat and leave it there. Never taste "
                   "any of the samples, before or after.",

    "ws": ["measurement", "analysis-and-evaluation"],
}
