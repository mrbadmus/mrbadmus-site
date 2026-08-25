"""P12 L2 — Mass vs weight (CONTRAST, and it keeps the formula block).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p12/p12-02-mass-vs-weight.dc.html`.

Her page wins outright. The hammer on the Moon, the two columns, the
W = m × g triangle, both worked examples, both attempts and all four rungs
are hers.

── ⚖️ A CONTRAST THAT CARRIES A FORMULA, AND SHE SAYS WHY ────────────

Her README states it in terms: *"p12-02 is declared CONTRAST rather than
QUANTITATIVE and still carries the block: W = m × g is the whole content
of the contrast, and the gram-to-kilogram trap is where the distinction
between mass and weight is actually lost."*

She is right, and it is worth saying why rather than only recording that
she said it. The distinction fails in practice at the moment a student
meets 750 g and reaches for 750: they have not confused two ideas, they
have skipped the step where the mass becomes a mass in the unit the field
strength is quoted in. So the second worked example on a CONTRAST page is
the contrast, done with a number.

`W = m × g` is a PRODUCT, so it takes Design's triangle (MRB-204 as
amended); a beam or a bar would encode a sum.

── ⚖️ THE COMPARISON WITH EARTH IS COMPUTED, AND THAT IS A FIX ───────

Design's bench note ends with a conditional tail whose third branch reads
*"Take it to Jupiter and the weight nearly two-and-a-half times over; take
it to the Moon and it drops to about a sixth."* — a sentence with no verb,
and it is the branch shown on Earth AND on Mars, which is two of her four
slider positions.

The tail is now DERIVED from the two field strengths: same, less or more
than Earth, with the ratio printed. Three branches, every one of the four
positions covered, every one of them a sentence, and a fifth place could
not break it. 5A.1's rule about comparatives, applied to the one place on
this page where it was broken. Registered in `DEPARTURES-P12.md`.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

This lesson takes indices **2 and 0**. Her option TEXT and every
correction are verbatim; only the ORDER moves.

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Rung 2's correct option is 23 words against a longest distractor of 16.
All three distractors are FINISHED so that each states a complete wrong
rule; the correct answer is untouched and so is every correction.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "mass-vs-weight",
    "title": "Mass vs weight",
    "discipline": "physics",
    "unit": "Space",
    "family": "CONTRAST",

    "covers": ["KS3.P.SPACE.01b"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["gravity-and-weight"],
    "assumes": [],
    "references": [{"unit": "P4", "lesson": "what-forces-do-to-motion"},
                   {"unit": "P4", "lesson": "non-contact-forces"}],
    "ks4_links": [],

    "meta_description": "One column never moves and the other changes "
                        "everywhere — mass in kilograms travels with the "
                        "object, weight in newtons belongs to the place.",

    "big_question": "Two quantities, two units, one word used for both in "
                    "ordinary speech. Sorting them out is worth more marks "
                    "than any other single idea in this unit.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "A hammer on the Moon",    "done_when": "committed"},
        {"anchor": "s-bench",   "short": "BENCH",
         "label": "Two columns, one object", "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "You take a hammer to the Moon.",
        "prompt": "The same hammer you use on Earth, taken to the lunar "
                  "surface, where the gravitational field is about a sixth as "
                  "strong.",
        "commit": "What is different about using it?",
        "options": [
            "It would be easier to lift and easier to swing",
            "It would be easier to lift and just as hard to swing",
            "It would be just as hard to lift and easier to swing",
            "Nothing about it would change",
        ],
        "answer": 1,
        "reveal": "Easier to lift, and every bit as hard to swing. Lifting "
                  "works against weight, and on the Moon the hammer is pulled "
                  "with about a sixth of the force. Swinging works against "
                  "mass — the hammer’s reluctance to start moving and to stop "
                  "again — and the mass is exactly what it was on Earth. "
                  "Apollo astronauts described precisely this: everything "
                  "felt light in the hand and behaved like its full Earth "
                  "self the moment they tried to move it sideways or stop it.",
    },

    "misconceptions": [
        {"id": "SPACE-04",
         "statement": "In orbit things are weightless, so they have no mass.",
         "elicited_by": "s-ladder",
         "confronted_by": "think-weightless-not-massless"},
        {"id": "SPACE-05",
         "statement": "Weight and mass are the same thing measured in "
                      "different units, like metres and feet.",
         "confronted_by": "think-weightless-not-massless"},
        {"id": "SPACE-06",
         "statement": "On the Moon everything is easier, so a hammer is "
                      "easier to swing as well as easier to lift.",
         "elicited_by": "s-hook",
         "confronted_by": "s-ladder"},
        {"id": "SPACE-07",
         "statement": "A spring balance reads a mass, so it gives the same "
                      "answer wherever you take it.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Mass</strong> is a count of matter, measured in "
                 "kilograms. It is the same on Earth, on the Moon, in orbit "
                 "and in deep space, and it is also a measure of how "
                 "reluctant an object is to change how it is moving — how "
                 "hard it is to start, stop or turn."},
        {"type": "explainer",
         "text": "<strong>Weight</strong> is the force gravity pulls on that "
                 "matter with, measured in newtons. It is mass × "
                 "gravitational field strength, so it changes with where the "
                 "object is, and it never disappears entirely anywhere — but "
                 "far from any large body it falls to almost nothing."},
        {"type": "explainer",
         "text": "The two are easy to confuse because on Earth they are "
                 "locked together: multiply any mass in kilograms by ten and "
                 "you have its weight in newtons. Everyday English makes it "
                 "worse by using “weight” for both. The moment a "
                 "question leaves the Earth’s surface — or asks about free "
                 "fall, or about pushing something sideways — the two come "
                 "apart, and the answer depends on knowing which one is being "
                 "asked about."},

        # ── #s-bench · one object, four places, two columns ─────────────
        {"type": "space-bench",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · one object, four places, two columns",
         "heading": "One column never moves. The other changes everywhere.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Pick an object and move it around the solar system. The "
                 "left-hand figure is its mass and the right-hand figure is "
                 "its weight — and only one of them is a property of the "
                 "object.",
         "model": "weight-in-four-places",
         "earth_g": 10,
         "gate": {
             "prompt": "Commit first. Which of these could you measure with a "
                       "spring balance and get a different answer for on the "
                       "Moon?",
             "options": [
                 "Mass, because the object is lighter there",
                 "Weight, because the pull of gravity is weaker there",
                 "Both, because everything changes on the Moon",
                 "Neither — a balance always reads the same",
             ],
             "answer": 1,
         },
         "tabs_label": "The object",
         "start_tab": 0,
         "tabs": [
             {"id": "sugar",   "label": "A bag of sugar",
              "name": "a bag of sugar", "m": 1},
             {"id": "schoolbag", "label": "A school bag",
              "name": "a school bag",   "m": 6},
             {"id": "student", "label": "A student",
              "name": "a student",      "m": 55},
             {"id": "car",     "label": "A small car",
              "name": "a small car",    "m": 1200},
         ],
         "slider": {
             "id": "place",
             "label": "Where it is",
             "value_label": "{label}",
             "start": 1,
             "values": [
                 {"id": "earth",   "label": "Earth",    "g": 10.0},
                 {"id": "moon",    "label": "the Moon", "g": 1.6},
                 {"id": "mars",    "label": "Mars",     "g": 3.7},
                 {"id": "jupiter", "label": "Jupiter",  "g": 24.8},
             ],
         },
         "bars_caption": "The same object, weighed in four places",
         "bars_alt": "The weight of {name} in four places: {list}. The mass "
                     "is unchanged throughout, and {place} is highlighted.",
         "bars": [
             {"id": "earth",   "label": "Earth"},
             {"id": "moon",    "label": "The Moon"},
             {"id": "mars",    "label": "Mars"},
             {"id": "jupiter", "label": "Jupiter"},
         ],
         "readouts": [
             {"id": "mass",     "label": "Mass"},
             {"id": "g",        "label": "Field strength"},
             {"id": "weight",   "label": "Weight"},
             {"id": "measured", "label": "Measured with"},
         ],
         "words": {
             "mass_sub":       "identical in all four places",
             "g_sub":          "on {place}",
             "weight_sub":     "{m} × {g}",
             "measured_value": "a balance",
             "measured_sub":   "a spring balance would give the weight",
             "bar_sub":        "mass still {m} kg",
             "list_join":      "and",
         },
         # ⚠️ THREE BRANCHES, DERIVED FROM THE RATIO TO EARTH, and every one
         # of the four slider positions lands in one of them. Design's own
         # tail has two named cases and one fallback, and the fallback has no
         # verb in it.
         "notes": {
             "same": "On {place}, {name} of {m} kg weighs {w}. Move the "
                     "slider and every bar changes while the words "
                     "“mass still {m} kg” underneath do not. That "
                     "is the distinction: mass is a count of matter and "
                     "travels with the object; weight is a force and belongs "
                     "to the object and the place together. This is the Earth "
                     "figure, and every other place on the slider is measured "
                     "against it.",
             "less": "On {place}, {name} of {m} kg weighs {w}. Move the "
                     "slider and every bar changes while the words "
                     "“mass still {m} kg” underneath do not. That "
                     "is the distinction: mass is a count of matter and "
                     "travels with the object; weight is a force and belongs "
                     "to the object and the place together. Here the weight "
                     "is {ratio} times its Earth value, and the object is not "
                     "one atom smaller.",
             "more": "On {place}, {name} of {m} kg weighs {w}. Move the "
                     "slider and every bar changes while the words "
                     "“mass still {m} kg” underneath do not. That "
                     "is the distinction: mass is a count of matter and "
                     "travels with the object; weight is a force and belongs "
                     "to the object and the place together. Here the weight "
                     "is {ratio} times its Earth value, and the object is not "
                     "one atom bigger.",
         }},

        # ── #s-formula · W = m × g, again, and for the trap ────────────
        {"type": "formula",
         "id": "weight-rule-again",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Weight = mass × gravitational field strength",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The weight W sits above a "
                           "dividing line; the mass m and the field strength "
                           "g sit below it, multiplied together. Covering one "
                           "letter leaves the way to work it out.",
             "order": ["top", "left", "right"],
             "covered": "top",
             "top":   {"label": "W", "button": "Cover W",
                       "result": "W = m × g", "text": ""},
             "left":  {"label": "m", "button": "Cover m",
                       "result": "m = W ÷ g", "text": ""},
             "right": {"label": "g", "button": "Cover g",
                       "result": "g = W ÷ m", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["W · weight, a force, measured with a spring "
                           "balance · N",
                           "m · mass, a count of matter, measured with a pan "
                           "balance · kg",
                           "g · gravitational field strength where the object "
                           "is · N/kg"],
                 "condition": "The mass goes in as kilograms, because the "
                              "field strength is quoted in newtons for each "
                              "kilogram.",
             },
         }},

        {"type": "worked-example", "id": "cfifa-mass-plain-p12"},
        {"type": "worked-example", "id": "cfifa-mass-convert-p12"},
        {"type": "check", "id": "your-turn-mass", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "mass-travels-weight-does-not"},

        {"type": "misconception", "id": "think-weightless-not-massless",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-mass-plain-p12",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A spring balance on the Moon reads 32 N. Field strength "
                    "there is 1.6 N/kg. What is the mass?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "32 N stays 32 N · 1.6 N/kg stays 1.6 N/kg",
              "note": "The weight is already in newtons and the field "
                      "strength already in newtons per kilogram, so there is "
                      "nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "m = W ÷ g",
              "note": "Cover m on the triangle: W sits over g, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "m = 32 N ÷ 1.6 N/kg",
              "note": "Use the Moon’s field strength, because that is where "
                      "the reading was taken."},
             {"letter": "F", "label": "Fine-tune",
              "line": "32 ÷ 1.6 = 20",
              "note": "Newtons divided by newtons per kilogram leaves "
                      "kilograms."},
             {"letter": "A", "label": "Answer",
              "line": "m = 20 kg",
              "note": "And that 20 kg is the same on Earth, on Mars and "
                      "anywhere else."},
         ]},

        {"id": "cfifa-mass-convert-p12",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "What is the weight on Earth of a 750 g tin of paint?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "750 g ÷ 1000 = 0.750 kg",
              "note": "The field strength is in newtons per kilogram, so the "
                      "mass has to be in kilograms first."},
             {"letter": "F", "label": "Formula",
              "line": "W = m × g",
              "note": "Cover W on the triangle: m sits beside g, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "W = 0.750 kg × 10 N/kg",
              "note": "The converted mass goes in. The 750 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "0.750 × 10 = 7.5",
              "note": "Kilograms times newtons per kilogram leaves newtons."},
             {"letter": "A", "label": "Answer",
              "line": "W = 7.5 N",
              "note": "Insert 750 instead of 0.750 and the tin comes out "
                      "weighing 7500 N — three quarters of a tonne of paint."},
         ]},

        {"id": "your-turn-mass",
         "kind": "p12-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "check_label": "Check your working",
         "reveal_label": "The five lines · tick what you had",
         # The bench's opening state: the bag of sugar, and the place slider
         # resting at its second position, the Moon.
         "rest": {"m": "1", "name": "a bag of sugar", "place": "the Moon",
                  "g": "1.6", "w": "1.6", "fine": "1.6"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your object: {name} of {m} kg, on {place}, where g is "
                      "{g} N/kg.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{m} kg stays {m} kg · {g} N/kg stays {g} N/kg",
                   "note": "The mass is already in kilograms and the field "
                           "strength already in newtons per kilogram, so "
                           "there is nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "W = m × g",
                   "note": "Cover W on the triangle: m sits beside g, so you "
                           "multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "W = {m} kg × {g} N/kg",
                   "note": "The field strength is the one for {place}."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{m} × {g} = {fine}",
                   "note": "Kilograms times newtons per kilogram leaves "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "W = {w} N",
                   "note": "The mass in the first line is unchanged, and "
                           "always will be."},
              ],
              "close": "The five lines give the weight on {place}. Move the "
                       "slider and only the last four change."},
             {"id": "q2", "tab": "Question 2",
              "head": "A 900 g rock sample is brought back from Mars, where g "
                      "is 3.7 N/kg. What did it weigh on Mars?",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "900 g ÷ 1000 = 0.900 kg",
                   "note": "The field strength is in newtons per kilogram, so "
                           "the mass has to be in kilograms first."},
                  {"letter": "F", "label": "Formula",
                   "line": "W = m × g",
                   "note": "Cover W on the triangle: m sits beside g, so you "
                           "multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "W = 0.900 kg × 3.7 N/kg",
                   "note": "The converted mass goes in, with the Martian "
                           "field strength."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "0.900 × 3.7 = 3.33",
                   "note": "Kilograms times newtons per kilogram leaves "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "W = 3.33 N",
                   "note": "Insert 900 instead of 0.900 and the sample comes "
                           "out weighing 3330 N."},
              ],
              "close": "The five lines give 3.33 N on Mars. Back on Earth the "
                       "same rock weighs 9.00 N — and is still 900 g."},
         ]},

        {"id": "think-weightless-not-massless",
         "kind": "predict",
         "demand": "explain",
         "targets": "SPACE-04",
         "statements": [
             {"quote": "In orbit things are weightless, so they have no "
                       "mass.",
              "targets": "SPACE-04",
              "body": [
                  "Mass has nothing to do with gravity. An astronaut on the "
                  "space station who wants to move a 200 kg equipment rack "
                  "has to push exactly as hard as they would in a laboratory "
                  "on the ground, and has to push exactly as hard again to "
                  "stop it. Nothing is holding it down, and it is every bit "
                  "as reluctant to be shifted. This is why astronauts train "
                  "for handling large objects in orbit, and why a loose one "
                  "is dangerous.",
              ]},
             {"quote": "Weight and mass are the same thing measured in "
                       "different units, like metres and feet.",
              "targets": "SPACE-05",
              "body": [
                  "Metres and feet measure the same quantity. Kilograms and "
                  "newtons do not: one counts matter and the other measures a "
                  "force. The clue is that the conversion between them is not "
                  "a fixed number — it is 10 on Earth, 1.6 on the Moon and "
                  "24.8 on Jupiter, because it is not a conversion at all. It "
                  "is a multiplication by a physical property of the place "
                  "you happen to be standing.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "mass-travels-weight-does-not",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Mass is matter in kilograms and never changes. Weight is a "
                 "force in newtons and equals mass × field strength. On Earth "
                 "g is about 10 N/kg; on the Moon 1.6; on Jupiter 24.8. A pan "
                 "balance measures mass anywhere, a spring balance measures "
                 "weight."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 0.
    #
    # ⚠️ MRB-177 · RUNG 2'S THREE DISTRACTORS ARE FINISHED, each into a
    # complete wrong rule. The correct answer and every correction are
    # untouched.
    "ladder": {
        "recall": {
            "q": "A spring balance on Earth reads 45 N. What is the mass of "
                 "the object hanging from it?",
            "options": [
                "450 kg — multiply by 10",
                "45 kg — the balance reads the mass directly",
                "4.5 kg",
                "4.5 N — the answer is still a force",
            ],
            "answer": 2,
            "feedback": {
                0: "Cover m on the triangle and W sits over g, so you divide. "
                   "Multiplying takes you the wrong way.",
                1: "A spring balance reads a force in newtons. Divide by "
                   "10 N/kg to get the mass in kilograms.",
                3: "The number is right and the unit is wrong. Newtons "
                   "divided by newtons per kilogram leaves kilograms.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A hammer is used on the Moon. Which of these is true?",
            "options": [
                "It is easier to lift, because that works against its weight, "
                "and just as hard to swing, because that works against its "
                "mass.",
                "It is easier both to lift and to swing, because everything "
                "is lighter on the Moon and lighter things move more easily.",
                "It behaves exactly as it does on Earth, because it is the "
                "same hammer and a hammer’s mass and weight both travel with "
                "it.",
                "It is harder to swing, because there is no air to help, and "
                "without air resistance a moving tool is harder to control.",
            ],
            "answer": 0,
            "feedback": {
                1: "Swinging is about how reluctant the mass is to change its "
                   "motion, and the mass is unchanged. Only the lifting gets "
                   "easier.",
                2: "It is the same hammer, and the pull of gravity on it is "
                   "about a sixth. Lifting genuinely is easier.",
                3: "Air resistance on a hammer is negligible either way. "
                   "Swinging is set by mass, which has not changed.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain the difference between a balance and a spring "
                 "balance, and say which one would still work correctly on "
                 "Mars.",
            "field_label": "Your explanation",
            "placeholder": "A balance compares two things, so…",
            "success": [
                "Says a spring balance measures a force by how far a spring "
                "stretches.",
                "Says that force is the weight, so its reading depends on the "
                "field strength.",
                "Says a beam or pan balance compares an unknown mass against "
                "known masses.",
                "Says gravity acts on both sides of that comparison equally, "
                "so the comparison is unaffected.",
                "Concludes that the pan balance gives the right mass on Mars "
                "and the spring balance does not, unless it is recalibrated.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A shipping company charges by mass. Explain why a scale at "
                 "an airport gives an honest answer, why the same scale on a "
                 "spacecraft in orbit would read zero, and what the cargo "
                 "would still do to the crew if it broke loose.",
            "field_label": "Your answer",
            "placeholder": "The airport scale works because…",
            "success": [
                "Says the airport scale measures weight and converts it to "
                "mass using Earth’s field strength.",
                "Says that conversion is valid because the scale and the "
                "cargo are both on Earth.",
                "Says that in orbit the scale and the cargo are in free fall "
                "together, so nothing presses on the scale and it reads zero.",
                "Says the mass of the cargo has not changed at all.",
                "Says a loose crate drifting into a crew member would hit "
                "with the full force its mass demands, because stopping it "
                "depends on mass rather than weight.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Mass is the amount of matter in an object, measured in "
                "kilograms, unchanged by location, and it is also what makes "
                "an object hard to start or stop moving. Weight is the force "
                "of gravity on that mass, measured in newtons, and given by "
                "W = m × g. On Earth every kilogram weighs about 10 N, which "
                "is why the two are so easily confused. A pan balance "
                "measures mass anywhere; a spring balance measures weight and "
                "only reads a correct mass in the field strength it was "
                "calibrated for.",

    "stretch": [
        {"id": "the-two-masses",
         "type": "explainer",
         "text": "The link runs deeper than it looks. The mass in W = m × g — "
                 "how strongly gravity pulls on a thing — and the mass in "
                 "F = m × a — how strongly a thing resists being accelerated "
                 "— did not have to be the same number, and for three hundred "
                 "years nobody could say why they were. Experiments have "
                 "since shown them equal to within about one part in 10^15. "
                 "Einstein took that equality as the starting point of "
                 "general relativity, and it is the reason all objects fall "
                 "at the same rate."},
        {"id": "hammer-and-feather",
         "type": "explainer",
         "text": "That equality is what Galileo is said to have tested from "
                 "the leaning tower of Pisa and what David Scott actually did "
                 "test, on television, on the Apollo 15 mission: a hammer and "
                 "a falcon feather, released together on the airless lunar "
                 "surface, hit the ground at the same instant. The heavier "
                 "object is pulled harder and is proportionally harder to "
                 "accelerate, and the two effects cancel exactly."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "mass",
         "definition": "A count of matter, measured in kilograms. It travels "
                       "with the object and is also a measure of how hard the "
                       "object is to start, stop or turn."},
        {"term": "weight",
         "definition": "The force gravity pulls on an object’s matter with, "
                       "measured in newtons. It belongs to the object and the "
                       "place together, not to the object alone."},
        {"term": "spring balance",
         "definition": "An instrument that measures a force by how far a "
                       "spring stretches. It reads weight, so its answer "
                       "changes with the field strength where it is used."},
        {"term": "pan balance",
         "definition": "An instrument that compares an unknown mass against "
                       "known masses. Gravity acts on both sides equally, so "
                       "it gives the right mass anywhere."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure whether a question is asking about mass or about "
                "weight?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Weight, mass and gravitational field strength as a "
                   "required relationship, inertial and gravitational mass, "
                   "and resultant force = mass × acceleration.",

    "convention_note": "The bench is a teaching model. Field strengths are "
                       "surface values rounded to one decimal place: Earth "
                       "10.0, the Moon 1.6, Mars 3.7, Jupiter 24.8 N/kg, with "
                       "Jupiter quoted at the cloud tops since it has no "
                       "solid surface. Object masses are nominal round "
                       "figures. Weights are calculated from those two and "
                       "rounded for display.",

    "ws": ["measurement"],
}
