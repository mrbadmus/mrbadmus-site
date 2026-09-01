"""P11 L3 — Temperature, particle motion and internal energy (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p11/p11-03-temperature-and-internal-energy.dc.html`.

Her page wins outright. The spark and the bath, the four amounts of water
on one thermometer, the logarithmic bar panel and all four rungs are hers,
ported from her JavaScript constants rather than from her HTML.

⚠️ **THE TITLE IS `structure.py`'s, NOT THE PAGE'S SHORT ONE.** The slot is
named *"Temperature, particle motion and internal energy"* and the slug is
`temperature-and-internal-energy`; slugs are permanent and come from
`structure.py` character for character (§8.4). Design's `<h1>` is the same
long form, so nothing diverges here.

── ⚖️ TWO STATUTORY STATEMENTS, ONE LESSON ──────────────────────────

`KS3.P.EIM.01` (changes with temperature in motion and spacing of
particles) and `KS3.P.EIM.02` (internal energy stored in materials) are
both taken whole. The bench is the join between them: one thermometer
reading over four amounts of the same substance, so the average per
particle is held fixed while the total moves by five orders of magnitude.

── ⚖️ HER NOTE ASKS FOR A CONTROL POSITION THAT DOES NOT EXIST ───────

Her closing sentence is *"Drop the temperature to 0 °C and every bar
collapses"*, and her `SLIDER` is `[10, 20, 40, 60, 80, 100]` — there is no
0 on it. Her `pct` also carries an `e <= 0 ? 1.5` branch that nothing can
reach for the same reason, and her legal line explains a 0 °C reading the
bench cannot show.

Measured, and the DRAWING is what is built: the slider keeps her six
positions, the dead branch is not ported, and the sentence is re-authored
to describe what the control can actually do — *"Take the temperature down
and every bar shrinks"* — which is true at every step of her own slider.
An instruction to move a control to a place it does not go is worse than a
missing sentence: a student tries it. Registered, with the legal line.

── ⚖️ THE FIGURES IN THE NOTE ARE DERIVED, NOT TYPED ─────────────────

Her note says a teaspoon holds *"sixteen thousand times less"* than a
bathful. That is `80 ÷ 0.005`, and it is now computed from the masses in
the payload and printed as `16,000`, so it cannot drift from them. The
label of the smallest and the largest tab are derived too; the drawer
refuses a payload with a tie at either end, because both sentences NAME
one tab.

── ⚖️ `#s-think` IS THE THIRD RAIL STOP ──────────────────────────────

Design's `DONE` reads `s.answers.r1 !== null || s.hookChoice !== null`.
See the package note.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0. **Her
option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices **3 and 1**.

── ⚠️ MRB-177 · TWO DISTRACTORS FINISHED, ON HER SETS ────────────────

Both marked rungs are length tells (22w against 15w; 25w against 13w).
Remedied at the DISTRACTOR both times. Registered.

── ⚠️ NO CHILDLINE BLOCK. NO DRAFT MARKINGS. ─────────────────────────
"""

# XU-1 (MRB-295/MRB-298, ruled 28 Aug 2026). THIS IS THE SITE THAT WAS
# ALREADY RIGHT, and it is deliberately NOT rewritten to import
# ks3_data/quantities.py. Every occurrence of the definition on this page is
# embedded in the temperature-VERSUS-internal-energy contrast that the whole
# lesson is built on, and the "one particle" / "a single particle" phrasing
# is what makes that contrast land: temperature is the average for ONE
# particle, internal energy is the total for ALL of them. Swapping in the
# estate-wide sentence would flatten the one lesson that gets this right.
# The two forms say the same thing; this one says it more sharply, in the
# place that needs it sharpest.


LESSON = {
    "slug": "temperature-and-internal-energy",
    "title": "Temperature, particle motion and internal energy",
    "discipline": "physics",
    "unit": "Matter and the particle model",
    "family": "MODEL",

    "covers": ["KS3.P.EIM.01", "KS3.P.EIM.02"],
    "touches": ["KS3.WS.ANA.03"],
    "beyond_statutory": False,
    "threads": [{"id": "particles", "level": 2},
                {"id": "energy", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["brownian-motion"],
    "assumes": [],
    "references": [{"unit": "P1", "lesson": "heating-and-thermal-equilibrium",
                    "why": "Which way energy travels when two things at "
                           "different temperatures touch — this lesson is "
                           "about how much there is to travel."},
                   {"unit": "C1", "lesson": "changes-of-state",
                    "why": "Where the energy goes while the temperature is "
                           "not moving."},
                   {"unit": "C1", "lesson": "solids-liquids-and-gases",
                    "why": "What the particles are doing in each state, "
                           "before a temperature is put on it."}],
    "ks4_links": [],

    # ⊕ MRB-297 · 1 Sep 2026. Both fields said a bath at 40 °C "can injure
    # a small child". That is wrong, and it contradicts the comment on the
    # hook nineteen lines below, which this run wrote: a bath is RUN at
    # 37-40 °C and scalding needs about 50 °C. It was also new safety
    # wording, which this run was not authoring. The contrast the lesson
    # needs is spark-at-1000 against bath-at-40, and it does not need a
    # hazard. Both now say the bath already feels properly hot.
    "meta_description": "A spark at a thousand degrees bounces off your arm. "
                        "A bath at forty, barely above body temperature, "
                        "already feels properly hot. Both facts are about "
                        "energy, not about temperature alone.",

    "big_question": "A spark from a grinder is at a thousand degrees and it "
                    "bounces off your arm without a mark. A bath at forty, "
                    "barely more than body temperature, already feels "
                    "properly hot. Both facts are about energy, and neither "
                    "is about temperature alone.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "A spark and a bath", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",
         "label": "Four amounts of water",
         "done_when": "gate_and_a_control"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Hot is not the same as a lot",
         "done_when": "hook_or_first_rung"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A spark at 1000 °C and a bath at 40 °C.",
        # ⚖️ P11-13. This read "A bath run too hot at 40 °C will take the
        # skin off you". A bath is RUN at 37–40 °C; scalding needs about
        # 50 °C and up, which is why water is stored at 60 °C and
        # thermostatic mixers exist. Every child in the room has had a bath
        # at about this temperature, so the class contradicts it out loud —
        # at the opening sentence of the page that most needs to be
        # believed. P1's `heating-and-thermal-equilibrium` already runs this
        # hook honestly, and this now matches it. The comparison does not
        # need the exaggeration: 40 °C really does hold ~10⁸ times a
        # spark's internal energy.
        # ⊕ MRB-297 · 1 Sep 2026. The clause read "will make you flinch, and
        # it can genuinely injure a small child" — put there while the
        # older "take the skin off you" was being fixed, and just as untrue.
        # It also contradicted the comment directly above it. It now says
        # what a 40 °C bath really is: hot to get into, and nothing worse.
        "prompt": "A grinding wheel throws a shower of white-hot sparks "
                  "against your forearm and you feel a faint tick, nothing "
                  "more. A bath at 40 °C, barely more than body "
                  "temperature, already feels properly hot.",
        "commit": "Which one holds more energy?",
        "options": [
            "The spark, because it is far hotter",
            "The bath, because there is far more of it",
            "Neither — they are both the same kind of energy",
            "The spark, because sparks are made of metal",
        ],
        "answer": 1,
        "reveal": "The bath, easily — by something like a hundred million "
                  "times. The spark is at about 1000 °C and the bath at "
                  "40 °C, so the spark wins on temperature by a wide margin "
                  "and loses on everything else. Temperature says how much "
                  "kinetic energy each particle has, on average. Internal "
                  "energy is that added up over every particle there is, "
                  "and a bath has "
                  "an enormous number of particles while a spark has almost "
                  "none. That is why the spark bounces off your arm and does "
                  "nothing, while the bath, far cooler on the thermometer, "
                  # ⊕ MRB-297 · 1 Sep 2026. Ended "can genuinely injure a
                  # small child"; see the note on the prompt above.
                  "holds enough to keep a whole body warm for an hour.",
    },

    "misconceptions": [
        {"id": "ENER-28",
         "statement": "Temperature and heat are two words for the same thing.",
         "elicited_by": "s-think",
         "confronted_by": "think-hot-is-not-a-lot"},
        {"id": "ENER-29",
         "statement": "Adding energy to something always makes it hotter.",
         "elicited_by": "s-think",
         "confronted_by": "think-hot-is-not-a-lot"},
        # ⊕ RE-CONFRONTED, NOT RE-MINTED. `ENER-13` was opened by P1's
        # `heating-and-thermal-equilibrium` and its statement is exactly what
        # this page's hook asks for and what its bench takes apart. The
        # register carries a second row with the IDENTICAL statement, which
        # is the shape `CELL-08` already uses for a genuine reappearance.
        {"id": "ENER-13",
         "statement": "Temperature and energy are the same thing — if "
                      "something is hotter it must hold more energy.",
         "elicited_by": "s-hook",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every particle in every object is moving — vibrating in a "
                 "solid, sliding past its neighbours in a liquid, flying "
                 "about in a gas. <strong>Temperature</strong> is a measure "
                 "of how much kinetic energy one particle has, on average. It "
                 "says nothing whatever about how many particles there are."},
        {"type": "explainer",
         "text": "<strong>Internal energy</strong> is the total: the kinetic "
                 "energy of every particle in the object, plus the energy "
                 "stored in the forces holding them together. It is measured "
                 "in joules, and it depends on the temperature <em>and</em> "
                 "on how much stuff there is. Two objects at the same "
                 "temperature can hold wildly different internal energies."},
        {"type": "explainer",
         "text": "Heating moves internal energy from the hotter object to the "
                 "colder one, and it keeps going until both are at the same "
                 "temperature. Which way it goes is decided by temperature; "
                 "how much there is to move is decided by internal energy. "
                 "Confusing the two is the commonest mistake in this part of "
                 "physics, and the spark is the cleanest place to see the "
                 "difference."},

        # ── #s-bench · four amounts of water, one thermometer ──────────
        {"type": "matter-bench",
         "id": "bench",
         "anchor": "s-bench",
         "model": "internal-energy",
         "eyebrow": "At the bench · four amounts of the same substance, one "
                    "thermometer",
         "heading": "Same temperature, wildly different energies.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Every one of these is water, and the slider sets all four "
                 "to the same temperature. The bars are the energy each one "
                 "holds — and they are nothing like each other.",
         "gate": {
             "prompt": "Commit first. A mug and a bath are both at 60 °C. "
                       "Which holds more internal energy?",
             "options": [
                 "The same — they are at the same temperature",
                 "The mug, because the water is more concentrated in it",
                 "The bath, because internal energy counts every particle",
                 "It cannot be compared unless they are the same size",
             ],
             "answer": 2,
         },
         "tabs_label": "How much water",
         "start_tab": 1,
         "tabs": [
             {"id": "teaspoon", "label": "A teaspoon",
              "name": "a teaspoon of water", "m": "0.005", "m_label": "5 g"},
             {"id": "mug", "label": "A mug",
              "name": "a mug of water", "m": "0.25", "m_label": "250 g"},
             {"id": "kettle", "label": "A kettleful",
              "name": "a kettleful of water", "m": "1.7", "m_label": "1.7 kg"},
             {"id": "bath", "label": "A bathful",
              "name": "a bathful of water", "m": "80", "m_label": "80 kg"},
         ],
         "slider": {"label": "Temperature of all four",
                    "values": [10, 20, 40, 60, 80, 100],
                    "start": 2,
                    "value_label": "{v} °C"},
         "bars_caption": "Energy needed to warm each one from 0 °C — each bar "
                         "step is ten times the one before",
         "bars_alt": "Four bars on a ten-times scale showing the energy in a "
                     "teaspoon, a mug, a kettleful and a bathful of water, "
                     "all at {v} degrees Celsius.",
         "bars": [
             {"id": "teaspoon", "label": "{label} · {mlabel}",
              "value": "{energy}",
              "sub": "at {v} °C, the same as the other three"},
             {"id": "mug", "label": "{label} · {mlabel}",
              "value": "{energy}",
              "sub": "at {v} °C, the same as the other three"},
             {"id": "kettle", "label": "{label} · {mlabel}",
              "value": "{energy}",
              "sub": "at {v} °C, the same as the other three"},
             {"id": "bath", "label": "{label} · {mlabel}",
              "value": "{energy}",
              "sub": "at {v} °C, the same as the other three"},
         ],
         "readouts": [
             {"id": "thermo", "label": "Thermometer reads",
              "value": "{v} °C", "sub": "identical for all four"},
             {"id": "mass", "label": "Mass of water",
              "value": "{mlabel}", "sub": "{name}"},
             {"id": "energy", "label": "Internal energy above 0 °C",
              "value": "{energy}", "sub": "every particle added up"},
             # ⚠️ A READOUT'S LABEL IS STATIC IN THE SHIPPED BYTES — only
             # `value` and `sub` are templates — so this is Design's own
             # wording and it names the largest tab. The drawer refuses a
             # payload with two tabs tied at the largest mass, which is what
             # keeps the sentence true.
             {"id": "compare", "label": "A bathful holds",
              "value": "{holds}", "sub": "at exactly the same temperature"},
         ],
         "words": {
             "biggest_holds": "this one",
             "rest_holds": "{ratio} × more",
         },
         "notes": {
             "biggest": "All four are at {v} °C, so in all four the "
                        "individual water molecules are moving at the same "
                        "average speed. That is what a temperature reading "
                        "is: a measure of the average kinetic energy of one "
                        "particle. Internal energy is a different quantity — "
                        "it is that average multiplied by how many particles "
                        "there are — and {name} holds {energy} of it. "
                        "{smallest_label} at the same temperature holds about "
                        "{minratio} times less. Take the temperature down and "
                        "every bar shrinks, because you are taking the energy "
                        "out — but the number of particles has not changed at "
                        "all.",
             "rest": "All four are at {v} °C, so in all four the individual "
                     "water molecules are moving at the same average speed. "
                     "That is what a temperature reading is: a measure of the "
                     "average kinetic energy of one particle. Internal energy "
                     "is a different quantity — it is that average multiplied "
                     "by how many particles there are — and {name} holds "
                     "{energy} of it. {biggest_label} at the same temperature "
                     "holds about {ratio} times more, without being one "
                     "degree hotter. Take the temperature down and every bar "
                     "shrinks, because you are taking the energy out — but "
                     "the number of particles has not changed at all.",
         }},

        {"type": "key-fact", "ref": "temperature-is-not-energy"},

        {"type": "misconception", "id": "think-hot-is-not-a-lot",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-hot-is-not-a-lot",
         "kind": "matter-think",
         "demand": "explain",
         "targets": "ENER-28",
         "ticks_when": "The hook is committed, or ladder rung 1 is answered "
                       "— Design's own predicate for this stop, and neither "
                       "control is inside this section.",
         "statements": [
             {"quote": "Temperature and heat are two words for the same "
                       "thing.",
              "targets": "ENER-28",
              "body": [
                  "They are not even the same kind of quantity. Temperature "
                  "is a state an object is in, measured in degrees; heating "
                  "is a process — energy on the move from a hotter object to "
                  "a colder one — measured in joules. An object does not "
                  "contain heat. It contains internal energy, and heating is "
                  "one of the ways that energy gets in or out. The everyday "
                  "sentence “the heat in this room” is really about internal "
                  "energy, and the confusion it creates is worth undoing "
                  "carefully.",
              ]},
             {"quote": "Adding energy to something always makes it hotter.",
              "targets": "ENER-29",
              "body": [
                  "Not while it is changing state. Put a beaker of ice and "
                  "water on a hotplate and the thermometer sits at 0 °C, "
                  "minute after minute, while the energy pours in — because "
                  "that energy is going into breaking the forces holding the "
                  "solid together rather than into speeding the particles up. "
                  "Only when the last of the ice has gone does the "
                  "temperature start to climb again. The internal energy rose "
                  "the whole time; the temperature did not.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "temperature-is-not-energy",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Temperature measures the average kinetic energy of one "
                 "particle, in degrees Celsius. Internal energy is the total "
                 "energy of all the particles added together, in joules. "
                 "Temperature decides which way heating goes; internal energy "
                 "decides how much there is to move."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 3 and 1.
    "ladder": {
        "recall": {
            "q": "Two beakers of water are at 50 °C. One holds 100 g, the "
                 "other 400 g. Which statement is right?",
            "options": [
                "The particles in the 400 g beaker are moving four times "
                "faster.",
                # ⚠️ MRB-177 — Design's distractor, FINISHED. Her correct
                # option is 22 words against a longest distractor of 15.
                # Remedied at the distractor; her own correction for it
                # already answers the finished sentence.
                "Both hold the same internal energy, because both are at the "
                "same temperature, so a thermometer reading is all you need "
                "to compare two amounts of the same substance.",
                "The 100 g beaker is hotter, because the same energy is "
                "packed into less water.",
                "The particles in both are moving at the same average speed, "
                "but the 400 g beaker holds four times the internal energy.",
            ],
            "answer": 3,
            "feedback": {
                0: "Average particle speed is set by temperature alone, and "
                   "both are at 50 °C. What differs is how many particles "
                   "there are.",
                1: "Temperature is an average per particle; internal energy "
                   "is the total. Four times the particles at the same "
                   "average is four times the total.",
                2: "Both thermometers read 50 °C. Nothing has been said about "
                   "giving them equal energy.",
            },
            "title": "Rung 1 · Read the model"},
        "apply": {
            "q": "A spark from an angle grinder lands on your arm at about "
                 "1000 °C and does no harm. Why not?",
            "options": [
                "Sparks are not really hot; the number is exaggerated.",
                "It has almost no mass, so despite the very high temperature "
                "its internal energy is tiny — and it cools to skin "
                "temperature almost instantly.",
                # ⚠️ MRB-177 — finished, for the same reason.
                "Skin is a good conductor, so the energy passes straight "
                "through and spreads out through the rest of your body "
                "instead of staying where the spark landed.",
                "The spark cools on the way through the air, so it arrives "
                "cold.",
            ],
            "answer": 1,
            "feedback": {
                0: "The temperature is real. What is small is the amount of "
                   "matter at that temperature.",
                2: "Skin is a poor conductor. The reason nothing happens is "
                   "that there is almost no energy in the spark to pass "
                   "anywhere.",
                3: "It does cool on the way, and it still arrives hot. The "
                   "point is that a hot thing with almost no mass carries "
                   "almost no energy.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain the difference between temperature and internal "
                 "energy, using a mug of tea and a swimming pool.",
            "field_label": "Your explanation",
            "placeholder": "Temperature tells you…",
            "success": [
                "Says temperature measures the average kinetic energy of the "
                "particles.",
                "Says internal energy is the total energy of all the "
                "particles added together.",
                "Says a mug of tea can be at a much higher temperature than a "
                "pool.",
                "Says the pool still holds far more internal energy, because "
                "it has vastly more particles.",
                "Says the two quantities have different units — degrees "
                "Celsius against joules.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A storage heater holds bricks that are warmed overnight and "
                 "give the energy out through the day. Explain why bricks are "
                 "used rather than the same volume of air, in terms of "
                 "particles and internal energy.",
            "field_label": "Your answer",
            "placeholder": "A brick has far more particles in the same space "
                           "because…",
            "success": [
                "Says a brick is far denser than air, so the same volume "
                "holds vastly more particles.",
                "Says internal energy depends on the number of particles as "
                "well as the temperature.",
                "Says the bricks can therefore store a large amount of energy "
                "at a modest temperature.",
                "Says the same volume of air at the same temperature would "
                "store almost nothing.",
                "Says the stored energy is released by heating the room, "
                "which happens because the bricks are hotter than the air "
                "around them.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Temperature measures the average kinetic energy per "
                "particle, and is read in degrees Celsius. "
                "Internal energy is the total energy of every particle in "
                "an object, measured in "
                "joules, and depends on the temperature and on how much "
                "matter there is. A spark at 1000 °C holds almost no internal "
                "energy because it has almost no mass; a bath at 40 °C holds "
                "an enormous amount. Heating is energy transferred from a "
                "hotter object to a colder one, and it stops when their "
                "temperatures are equal.",

    "stretch": [
        {"id": "water-is-expensive-to-warm",
         "type": "explainer",
         "text": "Water is unusually expensive to warm up. It takes about "
                 "4200 J to raise one kilogram of it by one degree, against "
                 "roughly 900 J for aluminium and 130 J for lead. That number "
                 "is the specific heat capacity, and water has one of the "
                 "highest of any ordinary substance — which is why it is used "
                 "in radiators and cooling systems, why coastal towns have "
                 "milder winters than inland ones, and why a hot water bottle "
                 "stays useful for hours."},
        {"id": "absolute-zero",
         "type": "explainer",
         "text": "There is a floor to all this. Cool an object and its "
                 "particles move less; at −273.15 °C they carry the least "
                 "energy the laws of physics permit, and no further cooling "
                 "is possible. That point is absolute zero, and it is why "
                 "scientists usually measure temperature in kelvin, which "
                 "starts there. Nothing has ever reached it, though "
                 "laboratories have got within a few billionths of a degree."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "temperature",
         "definition": "A measure of how much kinetic energy one particle "
                       "has, on average, read in degrees Celsius. It says "
                       "nothing about how many particles there are."},
        {"term": "internal energy",
         "definition": "The total energy of every particle in an object — "
                       "their motion plus the energy stored in the forces "
                       "holding them together — measured in joules."},
        {"term": "heating",
         "definition": "Energy moving from a hotter object to a colder one. "
                       "It is a process, not a thing an object contains, and "
                       "it stops when the two temperatures are equal."},
        {"term": "absolute zero",
         "definition": "−273.15 °C, the temperature at which particles carry "
                       "the least energy the laws of physics permit. Nothing "
                       "can be cooled below it."},
    ],

    "tutor": {
        "prompt": "Ask Mr Badmus AI",
        "body": "Muddled about when to say temperature and when to say "
                "energy?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Specific heat capacity and its required practical, "
                   "specific latent heat, and internal energy as the sum of "
                   "kinetic and potential stores in the particle model.",

    "convention_note": "The bench is a teaching model. Energies are "
                       "calculated as mass × 4200 J/kg°C × temperature above "
                       "0 °C, using a single specific heat capacity for water "
                       "and ignoring its small variation with temperature. "
                       "Masses are nominal: a teaspoon 5 g, a mug 250 g, a "
                       "kettleful 1.7 kg and a bathful 80 kg. The bars use a "
                       "logarithmic scale so that four quantities spanning "
                       "five orders of magnitude can be shown together, and "
                       "0 °C is the reference the energies are measured "
                       "above rather than a reading the bench takes.",

    "ws": ["analysis-and-evaluation"],
}
