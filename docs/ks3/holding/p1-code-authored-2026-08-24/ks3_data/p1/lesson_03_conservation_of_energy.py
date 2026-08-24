"""P1 L3 — Conservation of energy (MODEL).

The lesson the unit turns on. p1-01 named the stores and p1-02 said one goes
down as another goes up; this one adds the only fact that makes any of that
worth doing — **the two amounts are equal, always, with no exceptions** — and
then draws the conclusion that follows from it and catches everybody.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**Nothing is used up, and "wasted" does not mean "gone".** `ENER-11` is the
misconception, and it is held by nearly every Year 7 because the everyday word
for a flat battery is *used up*. It is not used up. The substances inside it
have reacted into other substances that hold less, and every joule that left
is in the thermal store of the phone, your hand and the room. `#s-count` is
built so the numbers say this before any sentence does: every device on the
bench takes in 100 J and puts out 100 J, and the two columns always add.

**"Wasted" is a judgement about what you wanted, not about physics.** The
bench calls the second column *warmed the surroundings*, and the close says
plainly that the only thing that makes it waste is that nobody asked for it.
A student who thinks waste energy has been destroyed will fail every
conservation question they ever meet.

── ⚖️ MRB-204: THIS FORMULA IS A SUM, SO IT GETS THE BEAM AND THE BAR ───

    total energy at the start = total energy at the end

is a CONSERVATION statement. It is not `A = B x C` and there is no product
anywhere in it, so a triangle is forbidden — it would tell a student that one
of the three quantities is the other two multiplied together, which is false
and which they would then try to use.

    the whole = the useful part + the part that warmed the surroundings

is a SUM, which is what the part-whole bar draws. The beam says the total does
not move; the bar says what the total splits into. Both, one block, checked
against the arithmetic: the bar's two weights are 30 and 70 and they are the
LED lamp's own two numbers from the bench above it, so the drawing and the
data cannot drift.

`KS3.P.CIS.01` asks for energy "as a quantity that can be quantified and
calculated", which is why a MODEL lesson carries a worked example and a
student attempt at all. The arithmetic is the statement, not decoration on it.

── ⚖️ `KS3.P.CIS.03`, AND WHY IT IS IN THIS LESSON ──────────────────────

The bullet says to use physical processes and mechanisms, RATHER THAN ENERGY,
to explain the intermediate steps. That instruction only becomes reasonable
once conservation is known: if the total never changes, energy was never
consumed, and a quantity that is never consumed cannot be the reason anything
happened. `#s-why` is where the student does it — and it is deliberately NOT
a block where the mechanism always wins. Two of its five questions are
quantity questions that the energy account answers better, because a student
who learns "always pick the mechanism" has learned a rule about this page
rather than a distinction about physics.
"""

LESSON = {
    "slug":        "conservation-of-energy",
    "title":       "Conservation of energy",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # Both are whole parent statements; neither needed splitting. The
    # reasoning that put CIS.03 here rather than on p1-02 is in
    # `ks3_data/p1/__init__.py` and in the docstring above.
    "covers":      ["KS3.P.CIS.01", "KS3.P.CIS.03"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["energy-transfers-before-and-after"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "The total before a change equals the total after it. "
                        "Wasted energy is not destroyed — it has spread into the "
                        "surroundings as warmth.",

    "big_question": "A phone battery goes flat and everyone says the energy "
                    "was used up. Weigh the whole room before and after and "
                    "the total has not moved by one joule. So where is it?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # SIX stops — the most in the unit, because this lesson carries two
    # statutory statements and MRB-204's four-part sequence. The rule block
    # and the worked example are NOT stops: they are read, not done.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The flat battery", "done_when": "committed"},
        {"anchor": "s-count",  "short": "COUNT",
         "label": "One hundred in, one hundred out",
         "done_when": "all_devices_read"},
        {"anchor": "s-why",    "short": "WHY",
         "label": "What actually explains it", "done_when": "all_cases_judged"},
        {"anchor": "s-build",  "short": "STEPS",
         "label": "Your own four steps", "done_when": "steps_opened"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Used up, or moved?", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The battery is flat and the phone weighs exactly what it "
                 "weighed this morning.",
        "prompt": "Charge a phone overnight and use it until it dies. Nothing "
                  "has come out of it, nothing has gone into it, and it is "
                  "the same mass to the milligram. Something left the "
                  "battery, and it went somewhere.",
        "commit": "Where did it go?",
        "options": [
            "It was used up — that is what a flat battery means",
            "It is still inside, but the battery can no longer reach it",
            "It left as heat and light, and is now spread through the room",
            "It turned into the electricity that ran the phone, and that is "
            "gone",
        ],
        "reveal": "It is in the room. Every joule that left the battery ended "
                  "up warming the phone, your hand, the air and whatever the "
                  "phone was resting on — spread so thinly that you cannot "
                  "feel it. Nothing was used up. Add up every store in the "
                  "room and the total is exactly what it was before.",
    },

    "misconceptions": [
        {"id": "ENER-11",
         "statement": "Energy gets used up, which is why a battery goes flat.",
         "elicited_by": "think-commit-usedup",
         "confronted_by": "think-commit-usedup"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Energy cannot be made and it cannot be destroyed. Add up "
                 "every store before a change and every store after it, and "
                 "the two totals are the same number. This has been tested "
                 "for two hundred years, in every kind of change anyone has "
                 "thought to try, and nothing has ever broken it."},

        # #s-count — the flagship. Ink-dark practical.
        {"type": "energy-audit", "id": "hundred-in", "anchor": "s-count",
         "eyebrow": "At the bench · five machines",
         "heading": "One hundred joules in. Now find them.",
         "head_counter": {"format": "{n} of 5 machines read", "total": 5},
         "demand": "investigate",
         "targets": "ENER-11",
         "prompt": "Every machine here is given exactly 100 J. Pick one, "
                   "commit to how much of it does the job you wanted, then "
                   "read the account.",
         "gate": {"prompt": "Commit first. Across all five machines, what "
                            "happens to the total after each one has run?",
                  "options": ["Some machines lose a little of it",
                              "It is 100 J every time",
                              "Only the efficient ones keep all of it",
                              "It depends whether anything gets hot"]},
         "resting": "Pick a machine to read it.",
         "unit": "J",
         "total_in": 100,
         "labels": {"in": "Given to it", "useful": "Did the job",
                    "waste": "Warmed the surroundings", "total": "Total out"},
         "guesses": ["Nearly all of it", "About half of it",
                     "About a quarter of it", "Almost none of it"],
         # ⚖️ EVERY ROW ADDS TO `total_in` AND THE RENDERER REFUSES ONE THAT
         # DOES NOT. The whole lesson is that the two columns add; a row that
         # did not would teach the opposite while rendering perfectly.
         "machines": [
             {"id": "filament", "name": "An old filament light bulb",
              "job": "light leaving the bulb", "useful": 5,
              "note": "Five joules of light and ninety-five joules of warm "
                      "air. A filament bulb is a heater that happens to glow, "
                      "which is why they were banned from sale."},
             {"id": "engine", "name": "A petrol car engine",
              "job": "the car's kinetic store", "useful": 25,
              "note": "A quarter moves the car. The other seventy-five "
                      "joules leave down the exhaust and through the "
                      "radiator, which is what the radiator is for."},
             {"id": "led", "name": "An LED lamp",
              "job": "light leaving the lamp", "useful": 30,
              "note": "Six times as much light as the filament bulb for the "
                      "same hundred joules. Same job, same rule, different "
                      "split."},
             {"id": "microwave", "name": "A microwave oven",
              "job": "the food's thermal store", "useful": 50,
              "note": "Half and half. The other fifty joules warm the "
                      "turntable, the walls of the oven and the room — and "
                      "the fan is there to move them out."},
             {"id": "kettle", "name": "An electric kettle",
              "job": "the water's thermal store", "useful": 90,
              "note": "Ninety joules into the water. The best of the five, "
                      "and the reason is that the job you wanted was heating "
                      "something — so the ten joules that warm the kettle "
                      "body are nearly the only way to miss."},
         ],
         "close": [
             "Five machines, five different splits, one total. Not one of "
             "them lost a joule.",
             "The second column is only called <em>waste</em> because nobody "
             "asked for it. The kettle's ninety joules and the filament "
             "bulb's ninety-five joules are the same kind of thing in the "
             "same kind of store — the difference is entirely in what you "
             "were trying to do.",
         ]},

        # ── the rule, alone in its own block (MRB-204 part 1) ──────────────
        # Not a rail stop: it is read, not done.
        {"type": "formula", "id": "the-rule",
         "eyebrow": "The rule",
         "statement": "total energy at the start = total energy at the end",
         "support": ["the surroundings count",
                     "energy is measured in joules (J)"],
         # ⚖️ part 2 — DRAWN, in the shape the relationship has. A CONSERVATION
         # statement, so a BEAM. Never a triangle: there is no product here.
         "figure": {
             "shape": "balance",
             "aria_label": "A balance beam, level. On the left pan: the total "
                           "energy in every store at the start. On the right "
                           "pan: the total energy in every store at the end. "
                           "The two are equal.",
             "pans": {"left": "at the start", "right": "at the end"},
             "caption": "always level"},
         # ⚖️ the cover interaction, on a part-whole BAR, because the second
         # statement IS a sum. The weights are the LED lamp's own two numbers
         # from the bench above, so the drawing cannot disagree with the data.
         "cover": {
             "shape": "bar",
             "eyebrow": "The bar",
             "heading": "Cover the one you want",
             "aria_label": "A bar model. One long bar is the hundred joules "
                           "given to the LED lamp. Underneath, the same "
                           "length is split into two: thirty joules that left "
                           "as light, and seventy that warmed the "
                           "surroundings. Covering one part leaves the way to "
                           "work it out.",
             "whole": {"id": "whole", "label": "everything given to it",
                       "button": "Cover the whole"},
             "parts": [
                 {"id": "useful", "label": "did the job",
                  "button": "Cover the useful part", "weight": 30},
                 {"id": "waste", "label": "warmed the surroundings",
                  "button": "Cover the warming", "weight": 70},
             ],
             "covered": "waste",
             "results": {
                 "whole": {"result": "everything in = did the job + warmed the surroundings",
                           "sentence": "Cover the whole bar and the two parts are left side by side. Add them."},
                 "useful": {"result": "did the job = everything in − the warming",
                            "sentence": "Cover the useful part and you are left with the whole bar and the warming. Take one from the other."},
                 "waste": {"result": "the warming = everything in − what did the job",
                           "sentence": "Cover the warming and you are left with the whole bar and the useful part. This is the one you will be asked for, because the warming is the part nobody measures directly."},
             },
             "close": "Two parts side by side make the whole. Cover the part "
                      "you want and take the other one away from the whole."}},

        # ── the worked example (MRB-204 part 3) — read, not done ───────────
        {"type": "worked-example", "id": "led-worked"},

        # ── #s-build (MRB-204 part 4) — the student fills the same four ────
        {"type": "fifa-pick", "id": "your-four-steps", "anchor": "s-build",
         "ground": "inset",
         "eyebrow": "Your turn · the same four steps",
         "heading": "A filament bulb is given 4000 J from the mains and 200 J "
                    "leaves it as light.",
         "demand": "construct",
         "prompt": "Work out how much warmed the room. Commit to each line, "
                   "then open the worked version.",
         "picks": [
             {"label": "Step 1 · The rule",
              "options": [
                  "everything in = what did the job + what warmed the "
                  "surroundings",
                  "what did the job = everything in + what warmed the "
                  "surroundings",
                  "what warmed the surroundings = everything in + what did "
                  "the job",
              ]},
             {"label": "Step 2 · Insert",
              "options": [
                  "4000 = 200 + the warming",
                  "200 = 4000 + the warming",
                  "the warming = 4000 + 200",
              ]},
         ],
         "field": {"label": "Steps 3 and 4 · Work it out, then answer",
                   "hint": "Your answer as a number",
                   "placeholder": "0",
                   "unit_hint": "Unit",
                   "unit_placeholder": "choose a unit",
                   "units": ["J", "kJ", "N", "W"]},
         "button": "Show the four steps",
         "progress": {"format": "{n} of 3 lines committed", "done": "Opened"},
         "reveal_head": "The filament bulb, done four ways",
         "steps": [
             {"letter": "F", "label": "Formula",
              "line": "everything in = what did the job + what warmed the "
                      "surroundings",
              "note": "Nothing is lost, so the two parts have to add up to "
                      "the whole."},
             {"letter": "I", "label": "Insert",
              "line": "4000 = 200 + the warming",
              "note": "4000 J went in. 200 J of that left as light."},
             {"letter": "F", "label": "Fine-tune",
              "line": "the warming = 4000 − 200",
              "note": "Cover the warming on the bar. Rearranged so the "
                      "unknown is on its own, with both numbers already in "
                      "joules."},
             {"letter": "A", "label": "Answer",
              "line": "the warming = 3800 J",
              "note": "Nineteen times as much as the light. That bulb is a "
                      "3800 J heater with a 200 J lamp attached to it."},
         ],
         "close": {"template": "You wrote {answer} {unit}. The worked answer "
                               "is 3800 J.",
                   "blank": "—"}},

        {"type": "key-fact", "ref": "never-used-up"},

        # #s-why — `KS3.P.CIS.03`. Not every answer is the mechanism.
        {"type": "mechanism-or-energy", "id": "what-explains-it",
         "anchor": "s-why",
         "eyebrow": "Two true answers · only one of them explains",
         "heading": "Energy tells you how much. It never tells you how.",
         "head_counter": {"format": "{n} of 5 questions judged", "total": 5},
         "demand": "explain",
         "prompt": "Each question below comes with two answers, and both of "
                   "them are true. Pick the one that actually answers THAT "
                   "question, then read why.",
         "tools": [
             {"id": "account", "label": "The energy account"},
             {"id": "mechanism", "label": "The mechanism"},
         ],
         "resting": "Pick a question to open it.",
         "cases": [
             {"id": "kettle-why",
              "question": "Why did the water in the kettle get hot?",
              "account": "Because energy moved from the chemical store at "
                         "the power station into the water's thermal store.",
              "mechanism": "Because a current in the element made the metal's "
                           "particles vibrate harder, and those particles "
                           "knocked the water particles next to them into "
                           "faster motion.",
              "answers": "mechanism",
              "note": "Both are true. But \"energy moved\" is what happened "
                      "to the accounts — it would be equally true of a "
                      "microwave, a flame or a friction heater, and it "
                      "cannot tell those apart. The second answer names the "
                      "actual physical steps, and it is the only one you "
                      "could use to design a kettle."},
             {"id": "kettle-much",
              "question": "Two kettles run for the same time, one holding "
                          "1 kg of water and one holding 2 kg. Which water "
                          "ends up hotter?",
              "account": "The same number of joules is shared among twice as "
                         "much water in the second kettle, so its water rises "
                         "by half as much.",
              "mechanism": "In both kettles the element's particles vibrate "
                           "and knock the water particles into faster motion.",
              "answers": "account",
              "note": "This is a HOW MUCH question, and the mechanism is "
                      "identical in the two kettles so it cannot separate "
                      "them. Counting joules is exactly the right tool here "
                      "— which is the point of having it."},
             {"id": "ball-stop",
              "question": "Why did the rolling ball stop on the grass but "
                          "keep going on the ice?",
              "account": "On grass its kinetic store emptied into a thermal "
                         "store faster than it did on ice.",
              "mechanism": "Grass blades bend and drag against the ball, and "
                           "the rough surfaces catch on each other. Ice is "
                           "smooth and has a thin slippery film on top, so "
                           "there is far less to catch on.",
              "answers": "mechanism",
              "note": "The account is true and it restates the question. "
                      "\"It emptied faster\" is another way of saying \"it "
                      "stopped sooner\". The mechanism says what the "
                      "surfaces were doing, and that is a different piece of "
                      "information."},
             {"id": "ball-where",
              "question": "Where did the ball's movement go when it stopped?",
              "account": "Into the thermal stores of the grass, the ball and "
                         "the air — all very slightly warmer.",
              "mechanism": "The grass blades bent and rubbed against the "
                           "ball's surface as it passed.",
              "answers": "account",
              "note": "A WHERE question is an accounting question, and this "
                      "is what the accounts are for. The mechanism describes "
                      "the rubbing without ever saying what came of it."},
             {"id": "duvet",
              "question": "Why does a duvet keep you warm?",
              "account": "It slows the transfer from your thermal store to "
                         "the room's.",
              "mechanism": "It holds a thick layer of still air in place. "
                           "Air is very bad at passing vibration from "
                           "particle to particle, and holding it still stops "
                           "it carrying warmth away by moving.",
              "answers": "mechanism",
              "note": "The account is true and is nearly a definition of "
                      "\"keeps you warm\". The mechanism names the still air, "
                      "and only the mechanism explains why a thin duvet "
                      "packed tight works worse than a thick loose one."},
         ],
         "close": [
             "Three of the five were answered by the mechanism and two by "
             "the account, and there is no way to tell which is which "
             "without reading the question.",
             "The rule is simple. <strong>How much</strong> and "
             "<strong>where</strong> are energy questions. "
             "<strong>Why</strong> and <strong>how</strong> are mechanism "
             "questions, and answering them with energy sounds like an "
             "explanation while saying nothing at all.",
         ]},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Conservation of energy", "Dissipated", "Wasted energy",
                   "Mechanism"]},

        {"type": "misconception", "id": "think-commit-usedup",
         "anchor": "s-think", "targets": "ENER-11"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "never-used-up",
         "text": "Energy is never made and never destroyed. When we say it "
                 "was wasted, we mean it ended up spread thinly in the "
                 "surroundings, warming them — where it still is, and where "
                 "it is too spread out to be useful.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Conservation of energy",
         "definition": "The total energy in every store before a change is "
                       "equal to the total in every store after it.",
         "note": "No exceptions have ever been found, in any change anyone "
                 "has tested."},
        {"term": "Dissipated",
         "definition": "Spread out thinly into the surroundings, usually as "
                       "warmth.",
         "note": "Dissipated energy is still there. It is just spread so "
                 "thinly that nothing can collect it back up."},
        {"term": "Wasted energy",
         "definition": "The part of a transfer that did not do the job you "
                       "wanted.",
         "note": "A judgement about what you were trying to do, not about "
                 "the physics. The kettle's warming is useful; the light "
                 "bulb's is not."},
        {"term": "Mechanism",
         "definition": "The actual physical steps by which something "
                       "happened.",
         "note": "Particles colliding, a surface dragging, a current "
                 "flowing. Energy accounts say how much; mechanisms say how."},
    ],

    "activities": [
        # The worked example (MRB-204 part 3). Staged: one step at a time.
        {"id": "led-worked",
         "kind": "worked-example",
         "demand": "explain",
         "eyebrow": "Worked example · one step at a time",
         "heading": "An LED lamp is given 4000 J from the mains and 1200 J "
                    "leaves it as light.",
         "head_counter": {"format": "Step {n} of 4", "total": 4},
         "staged": True,
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All four shown",
                     "done_note": "Now the same four steps on the filament "
                                  "bulb."},
         "fifa": [
             {"letter": "F", "label": "Formula",
              "line": "everything in = what did the job + what warmed the surroundings",
              "note": "Nothing is created and nothing is destroyed, so the two parts have to add up to the whole."},
             {"letter": "I", "label": "Insert",
              "line": "4000 = 1200 + the warming",
              "note": "4000 J came in from the mains. 1200 J of it left the lamp as light."},
             {"letter": "F", "label": "Fine-tune",
              "line": "the warming = 4000 − 1200",
              "note": "Cover the warming on the bar. Rearranged so the unknown is on its own, and both numbers are already in joules."},
             {"letter": "A", "label": "Answer",
              "line": "the warming = 2800 J",
              "note": "Which is why an LED lamp is warm to the touch and never hot. Thirty joules in every hundred did the job — the same split the bench gave."},
         ]},

        {"id": "think-commit-usedup",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-11",
         "prompt": "A torch is left on until the cell is flat. Commit before "
                   "you read on.",
         "options": [
             "The energy in the cell has been used up and no longer exists",
             "The energy is still in the cell but is now too weak to reach "
             "the bulb",
             "The energy left the cell and is now spread thinly through the "
             "room",
             "The energy turned into light, and light does not last",
         ],
         "reveal": [
             "It is in the room. The cell's chemical store emptied, a "
             "current carried it to the bulb, and the bulb sent it out as "
             "light and warmth. The light crossed the room, landed on the "
             "walls and the furniture, and warmed them by an amount far too "
             "small to feel. Every joule is accounted for.",
             "What has actually run out is not energy but <strong>usefulness"
             "</strong>. Energy concentrated in one small place — a cell, a "
             "tank of petrol, a stretched spring — can be made to do things. "
             "The same energy spread evenly through a room can do nothing at "
             "all, because there is nowhere for it to flow to. That is what "
             "a flat battery is: not less energy, just energy nobody can use.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "A machine is given 200 J and 150 J of that does the job it "
                 "was built for. How much warmed the surroundings?",
            "options": [
                "350 J",
                "150 J",
                "50 J",
                "It cannot be worked out without knowing the machine",
            ],
            "answer": 2,
            "feedback": {
                0: "That is 200 + 150. The two parts add up to the whole; "
                   "they are not both added to it.",
                1: "That is the part that did the job. The question asks for "
                   "the other part.",
                3: "Conservation does not care which machine it is. Whatever "
                   "went in has to come out somewhere.",
            }},
        "apply": {
            "q": "A bouncing ball is dropped from 1 m and bounces back to "
                 "0.6 m, then lower each time until it stops. What has "
                 "happened to the energy?",
            "options": [
                "It has spread into the thermal stores of the ball, the "
                "floor and the air",
                "It has been destroyed a little at a time by each bounce",
                "It is still in the ball's gravitational store, unreachable",
                "It was never there — the ball only had energy while it "
                "was moving",
            ],
            "answer": 0,
            "feedback": {
                1: "Nothing destroys energy. Each bounce squashes the ball "
                   "and the floor, and squashing warms them very slightly.",
                2: "The ball ends up on the floor with its gravitational "
                   "store empty. That store is where the energy came FROM.",
                3: "It had a gravitational store at 1 m before it moved at "
                   "all, which is exactly what made it fall.",
            }},
        "explain": {
            # ⚠️ NO MARKUP IN A RUNG QUESTION. `r_ladder` puts this through
            # `t()`, which escapes, so an `<em>` here ships as visible
            # `&lt;em&gt;`. Caught by verify_ks3's escaped-tag sweep.
            "q": "An old filament bulb turns 5 joules in every 100 into "
                 "light. A student says \"so 95 joules are lost\". Explain "
                 "what is actually wrong with the word lost, and say where "
                 "those 95 joules are.",
            "field_label": "Your explanation",
            "placeholder": "Nothing is lost, because…",
            "success": [
                "Says nothing is lost — energy is never destroyed.",
                "Says the 95 J warmed the bulb, the fitting, the air and "
                "the room.",
                "Says it is still there, spread thinly.",
                "Says it is called wasted only because nobody wanted the "
                "room warmed.",
                "Says that in a heater the same 95 J would be the useful "
                "part.",
            ]},
        "produce": {
            "q": "Design a fair way to show a class that a bouncing ball "
                 "loses no energy at all. Say what you would measure, what "
                 "you could not measure, and how you would argue for the "
                 "part you could not measure.",
            "field_label": "Your method and argument",
            "placeholder": "I would measure the drop height and…",
            "success": [
                "Measures drop height and bounce height, repeated.",
                "Identifies the missing amount as the difference between the "
                "two gravitational stores.",
                "Says the ball, the floor and the air get warmer, and that "
                "this is what cannot be measured with school equipment.",
                "Gives a reason to believe it anyway — the ball and floor "
                "are squashed and released on every bounce, and squashing "
                "warms things.",
                "Says that conservation is what lets you claim the missing "
                "amount is exactly equal to the drop, rather than roughly.",
            ]},
    },

    "key_note": "The total energy before a change equals the total after it, "
                "always. Wasted energy is not destroyed — it has spread into "
                "the surroundings as warmth, where it still is. And because "
                "energy is never consumed, it can never be the reason "
                "something happened: for that you name the mechanism.",

    "stretch": [
        {"type": "explainer", "id": "why-it-runs-one-way",
         "text": "If nothing is ever lost, why can you not run the room "
                 "backwards and recharge the battery from the warmth? "
                 "Because energy spread evenly through a room has nowhere to "
                 "flow to, and flowing is the only thing that gets work done. "
                 "This is the second great law of energy, and it is the one "
                 "that gives time a direction: the total never changes, but "
                 "the spreading only ever goes one way. Everything anybody "
                 "calls waste, wear, decay or running down is this one idea."},
    ],

    "support": [],

    "safety_note": "",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure where the energy in a flat battery went?",
              "cta": "Ask about this lesson",
              "anchor": "s-count"},

    "ks4_becomes": "Efficiency as a calculated percentage, Sankey diagrams, "
                   "and dissipation as the reason a transfer cannot be run "
                   "backwards.",

    "ws": ["analysis-and-evaluation", "measurement"],

    "review_state": "draft",
}
