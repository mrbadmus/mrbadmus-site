"""P1 L5 — Conduction (PROCESS).

The first of the two routes. p1-04 said a temperature difference drives a
transfer; this lesson says how one of the two routes actually carries it, and
`KS3.P.CIS.03` is why the lesson exists in this shape at all — the whole of
`#s-model` is a mechanism, not an energy account.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**The particles do not travel. The vibration does.** This is the single thing
a Year 7 gets wrong about conduction, and it is worth being blunt about it on
the page: a hot particle does not walk down the rod carrying warmth. It stays
roughly where it is, vibrating harder, and knocks its neighbours into
vibrating harder. `#s-model` draws the particles in fixed positions on
purpose, and the drawing is what makes the claim.

**Metals have a second route, and it is the reason they win.** The knocking
happens in every solid. What a metal also has is electrons that are free to
move right through it, and they carry the transfer far faster than the
knocking does. Without that second route there is no honest answer to "so why
is copper so much better than glass?" — both are solids and both have
particles in contact.

⚠️ **`ENER-13` is a lesson about your hand, not about the metal.** A metal
handrail and a wooden bench in the same playground are at the SAME
temperature, and the handrail feels colder because it takes energy out of your
skin faster. What your hand reports is a rate, not a temperature. This is the
misconception the lesson is built to kill, and it is the one that makes the
whole of conduction feel wrong until it is dealt with.

── The race, and the order it derives ──────────────────────────────────

Five rods, four wax blobs each, sixty seconds. The results give the order
copper, aluminium, steel, glass, wood — and the closing claim is CHECKED
against the blob data in `ks3_art/p1.py` rather than authored beside it, on
C9's ruling: a panel that states an order its own cells contradict is the page
arguing with itself in front of the student.

The times are not measurements from a real bench and are not presented as
though they were: they are a model built to put the five materials in the
right order with the right sort of spacing. What IS real is the order and the
rough scale of the gaps — copper conducts about four hundred times better
than glass and about three thousand times better than wood.
"""

LESSON = {
    "slug":        "conduction",
    "title":       "Conduction",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "PROCESS",

    "covers":      ["KS3.P.ECT.02b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2},
                    {"id": "particles", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["heating-and-thermal-equilibrium"],
    "assumes":     [],
    # §4.6 — a cross-link, never prose. The particle model is C1's and this
    # lesson does not re-teach it.
    "references":  [{"unit": "C1", "lesson": "particle-model"}],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "How a vibration is passed from particle to particle, why "
                        "metals are so much better at it, and why a metal handrail "
                        "feels colder than wood.",

    "big_question": "Grab a metal handrail and a wooden bench outside on the "
                    "same cold morning. The metal feels far colder. Put a "
                    "thermometer on each and they read the same.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The spoon in the soup", "done_when": "committed"},
        {"anchor": "s-race",   "short": "RACE",
         "label": "Five rods, sixty seconds", "done_when": "all_rods_run"},
        {"anchor": "s-model",  "short": "MODEL",
         "label": "What the particles do", "done_when": "all_steps_shown"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Why metal feels colder", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Leave a metal spoon in the soup and you cannot pick it up.",
        "prompt": "A metal spoon and a wooden spoon are left standing in the "
                  "same pan of hot soup for two minutes. The wooden one you "
                  "can hold anywhere. The metal one is too hot to touch, "
                  "right up at the handle, well clear of the soup.",
        "commit": "The soup only touches the bottom few centimetres of "
                  "either spoon. So how did the metal handle get hot?",
        "options": [
            "Hot soup travelled up the inside of the metal spoon",
            "Steam rose and heated the handle from the outside",
            "The vibration was passed along the metal from particle to "
            "particle",
            "Metal absorbs heat from the air faster than wood does",
        ],
        "reveal": "Passed along. The particles at the hot end vibrate harder, "
                  "knock their neighbours into vibrating harder, and the "
                  "disturbance runs up the spoon. No soup moved and no "
                  "particle travelled the length of the handle — but the "
                  "vibration did, and in a metal it does it fast.",
    },

    "misconceptions": [
        {"id": "ENER-13",
         "statement": "Metal is colder than wood, because it feels colder.",
         "elicited_by": "think-commit-handrail",
         "confronted_by": "think-commit-handrail"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Conduction is the route a thermal transfer takes through "
                 "something solid, and through solids that are touching. It "
                 "needs contact — no gap, no conduction — and some materials "
                 "carry it thousands of times better than others."},

        # #s-race — the flagship. Ink-dark practical.
        {"type": "conduction-race", "id": "five-rods", "anchor": "s-race",
         "eyebrow": "At the bench · five rods, one flame",
         "heading": "Wax blobs at 4, 8, 12 and 16 centimetres",
         "head_counter": {"format": "{n} of 5 rods run", "total": 5},
         "demand": "investigate",
         "prompt": "Every rod is the same length and the same thickness, "
                   "heated at one end for sixty seconds. A blob falls off "
                   "when the rod under it gets hot enough. Run all five.",
         "gate": {"prompt": "Commit first. Which of these will get the "
                            "vibration furthest along in sixty seconds?",
                  "options": ["Copper", "Steel", "Glass", "Wood"]},
         "resting": "Pick a rod and run it.",
         "run_labels": {"idle": "Run for 60 seconds", "done": "Run finished"},
         "labels": {"fell": "Blobs that fell", "still": "still there at 60 s",
                    "unit": "s", "at": "at"},
         "blob_positions": [4, 8, 12, 16],
         "position_unit": "cm",
         "duration": 60,
         # ⚖️ `rank` IS THE ORDER AND THE ARRAY POSITION IS NOT. The closing
         # claim is derived from these ranks and checked against the blob
         # times, both ways, in `ks3_art/p1.py`.
         "rods": [
             {"id": "copper", "name": "Copper", "rank": 0,
              "times": [6, 16, 31, 52],
              "note": "All four, and the last one with eight seconds to "
                      "spare. Copper is the best everyday conductor there "
                      "is, which is why saucepan bases and soldering irons "
                      "are made of it."},
             {"id": "aluminium", "name": "Aluminium", "rank": 1,
              "times": [9, 25, 50, None],
              "note": "Three of the four. A little behind copper and much "
                      "lighter and cheaper, which is why it is what most "
                      "pans and heat sinks are actually made of."},
             {"id": "steel", "name": "Steel", "rank": 2,
              "times": [28, 58, None, None],
              "note": "Two. Steel is a metal and conducts far better than "
                      "anything below it here — and still nowhere near "
                      "copper. That is why a steel pan handle is bearable "
                      "and a copper one would not be."},
             {"id": "glass", "name": "Glass", "rank": 3,
              "times": [47, None, None, None],
              "note": "One, at 47 seconds. Glass is not a metal: it has no "
                      "free electrons, so the knocking from particle to "
                      "particle is the only route it has."},
             {"id": "wood", "name": "Wood", "rank": 4,
              "times": [None, None, None, None],
              "note": "None. After sixty seconds the first blob has not "
                      "moved, and the far end of the rod is at room "
                      "temperature. Wood is full of tiny pockets of trapped "
                      "air, and air is worse at this than almost anything."},
         ],
         "order_claim": ["copper", "aluminium", "steel", "glass", "wood"],
         "close": [
             "The five results split cleanly in two. The three metals "
             "carried the vibration right along the rod inside the minute; "
             "the glass and the wood barely moved it at all.",
             "A material that carries it well is a <strong>conductor</strong> "
             "and one that does not is an <strong>insulator</strong>. Every "
             "metal on the bench is a conductor, and nothing that is not a "
             "metal came close to one.",
         ]},

        # #s-model — the mechanism. `KS3.P.CIS.03` in practice.
        {"type": "particle-relay", "id": "the-relay", "anchor": "s-model",
         "eyebrow": "The mechanism · four steps",
         "heading": "Nothing travels down the rod except the vibration",
         "head_counter": {"format": "Step {n} of 4", "total": 4},
         "demand": "explain",
         "prompt": "Step through it. Watch where the particles are, not "
                   "just which ones are hot.",
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All four shown"},
         "strip_label": "A row of particles in a solid rod. The heated end "
                        "is on the left.",
         "steps": [
             {"id": "heat", "title": "The end gets hot", "reach": 2,
              "electrons": False,
              "text": "The flame makes the particles at the left-hand end "
                      "vibrate much harder than before. They stay in the "
                      "same places — in a solid they are locked to their "
                      "neighbours — but they move further and faster about "
                      "those places."},
             {"id": "knock", "title": "They knock their neighbours", "reach": 5,
              "electrons": False,
              "text": "A particle vibrating harder bumps into the ones next "
                      "to it and shoves them. Those start vibrating harder "
                      "too. Nothing has moved along the rod; a disturbance "
                      "has been handed over."},
             {"id": "relay", "title": "The relay runs along", "reach": 8,
              "electrons": False,
              "text": "Each newly disturbed particle does the same to the "
                      "next. The vibration works its way along one handover "
                      "at a time, and this is why it is slow — and why it "
                      "arrives at the far end long after the near end got "
                      "hot."},
             {"id": "electrons", "title": "In a metal, a second route",
              "reach": 12, "electrons": True,
              "text": "A metal also has electrons that are not tied to any "
                      "one particle and can move right through it. They "
                      "carry the transfer the whole length of the rod "
                      "without waiting for a handover — which is the entire "
                      "reason copper reached the first blob in six seconds "
                      "and glass took forty-seven. Glass has no free "
                      "electrons and only the slow route."},
         ],
         "close": [
             "Nothing in that model needed the word energy to describe what "
             "happened, and that is deliberate. The account says how much "
             "moved; this says how.",
             "Two routes, then: the knocking, which every solid has, and the "
             "free electrons, which only a metal has. That is the whole "
             "difference between a conductor and an insulator.",
         ]},

        {"type": "key-fact", "ref": "vibration-not-particles"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Conduction", "Conductor", "Insulator", "Free electron"]},

        {"type": "misconception", "id": "think-commit-handrail",
         "anchor": "s-think", "targets": "ENER-13"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "vibration-not-particles",
         "text": "In conduction the particles stay where they are and pass "
                 "the vibration on by knocking into each other. Metals do it "
                 "far faster than anything else, because they also have free "
                 "electrons that carry it straight through.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Conduction",
         "definition": "A thermal transfer through a material, or between "
                       "materials in contact, passed from particle to "
                       "particle.",
         "note": "It needs contact. Across a gap there is no conduction at "
                 "all."},
        {"term": "Conductor",
         "definition": "A material that carries a thermal transfer quickly.",
         "note": "All metals. Copper is the best of the everyday ones."},
        {"term": "Insulator",
         "definition": "A material that carries a thermal transfer very "
                       "slowly.",
         "note": "Wood, plastic, glass, and above all trapped air."},
        {"term": "Free electron",
         "definition": "An electron in a metal that is not held to any one "
                       "particle and can move right through the material.",
         "note": "The reason metals conduct so much better than non-metals. "
                 "It is also the reason they conduct electricity."},
    ],

    "activities": [
        {"id": "think-commit-handrail",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-13",
         "prompt": "In the same playground on the same morning, the metal "
                   "handrail feels much colder than the wooden bench. Commit "
                   "before you read on.",
         "options": [
             "The metal really is colder, because metal gets colder than "
             "wood does",
             "They are the same temperature, and the metal takes energy out "
             "of your hand faster",
             "The wood is warmer because it holds the sunlight from "
             "yesterday",
             "The metal is colder because cold sinks into it overnight",
         ],
         "reveal": [
             "They are the same temperature, and a thermometer on each will "
             "say so. Everything left in the same place long enough reaches "
             "the same temperature — that is p1-04's whole point, and the "
             "playground is no exception.",
             "What differs is the RATE. Your hand is at about 33 degrees and "
             "both objects are at about 3, so energy leaves your hand into "
             "both of them. The metal carries it away from the contact patch "
             "almost instantly and keeps taking more; the wood cannot, so "
             "the little patch of bench under your hand warms up and the "
             "transfer nearly stops. Cold is not what you are feeling. You "
             "are feeling how fast you are losing energy.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "In conduction through a metal bar, what actually moves "
                 "along the bar?",
            "options": [
                "The vibration, passed from particle to particle, and free "
                "electrons",
                "The hot particles themselves, from one end to the other",
                "Heat, which is a fluid that flows through the metal",
                "Nothing moves; the whole bar warms at the same moment",
            ],
            "answer": 0,
            "feedback": {
                1: "In a solid the particles are locked to their neighbours. "
                   "They vibrate harder about the same place; they do not "
                   "travel.",
                2: "There is no such fluid. This is a very old idea called "
                   "caloric, and careful weighing killed it two hundred "
                   "years ago.",
                3: "The far end of the spoon gets hot much later than the "
                   "near end, which is exactly what the wax blobs show.",
            }},
        "apply": {
            "q": "A saucepan has a copper base and a wooden handle. Why is "
                 "each part made of what it is made of?",
            # ⚠️ MRB-177 — the three distractors are written OUT to the
            # length of the correct option rather than the correct one being
            # cut. A student must not be able to pick the elaborate one.
            "options": [
                "Copper is stronger than wood, and a wooden handle is "
                "lighter to lift",
                "Copper is the more expensive of the two, so it is used only "
                "where it has to be",
                "Copper carries the transfer into the food quickly; wood "
                "carries it into your hand slowly",
                "Copper holds more energy than wood does, so it heats the "
                "food up faster",
            ],
            "answer": 2,
            "feedback": {
                0: "Strength and weight are not what is being chosen here. "
                   "Both parts are chosen for how they carry a thermal "
                   "transfer.",
                1: "Copper is dearer, and that decides nothing. Ask what each "
                   "part has to do with the hob's energy.",
                3: "How much a material holds is not the point, and copper "
                   "does not hold more. What matters is how fast it passes a "
                   "transfer on.",
            }},
        "explain": {
            "q": "Explain why a metal rod conducts far better than a glass "
                 "rod of exactly the same size, even though both are solids "
                 "whose particles are touching.",
            "field_label": "Your explanation",
            "placeholder": "Both of them can pass the vibration on by…",
            "success": [
                "Says both solids pass the vibration on by particles "
                "knocking into their neighbours.",
                "Says the metal has free electrons and the glass does not.",
                "Says the free electrons can move right through the metal.",
                "Says that route is much faster than the handover from "
                "particle to particle.",
                "Concludes that the metal has two routes and the glass has "
                "only one.",
            ]},
        "produce": {
            "q": "Design a fair test to put four materials in order of how "
                 "well they conduct, using equipment a school actually has. "
                 "Say what you would change, what you would keep the same, "
                 "what you would measure, and one thing that could make your "
                 "order wrong.",
            "field_label": "Your plan",
            "placeholder": "I would change the material of the rod and…",
            "success": [
                "Changes only the material.",
                "Keeps the rod length, thickness and heat source the same.",
                "Measures a time — how long until a marker at a fixed "
                "distance falls or a thermometer reaches a set reading.",
                "Repeats the runs, or says why one run of each is not "
                "enough.",
                "Names a real problem: rods that start at different "
                "temperatures, a flame that is not the same size each time, "
                "or wax blobs of different masses.",
            ]},
    },

    "key_note": "Conduction passes a thermal transfer from particle to "
                "particle, by vibration, without the particles going "
                "anywhere. It needs contact. Metals are far better at it "
                "than anything else because free electrons carry it straight "
                "through, and a metal that feels cold is only taking energy "
                "out of your hand quickly.",

    "stretch": [
        {"type": "explainer", "id": "diamond",
         "text": "Free electrons are not quite the whole story, and the "
                 "exception is spectacular. Diamond conducts a thermal "
                 "transfer better than copper — about five times better — "
                 "and it has no free electrons at all. Its carbon atoms are "
                 "locked into a rigid lattice so stiff and so regular that "
                 "the vibration travels through it almost unimpeded, like a "
                 "sound through a perfectly tuned bar. Jewellers use this: a "
                 "real diamond draws warmth from your fingertip fast enough "
                 "to be felt, and a glass copy does not."},
    ],

    "support": [],

    "safety_note": "A rod that has been heated at one end stays hot along "
                   "its whole length for several minutes after the flame is "
                   "out, and hot metal looks exactly like cold metal.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why metal feels colder than wood?",
              "cta": "Ask about this lesson",
              "anchor": "s-model"},

    "ks4_becomes": "Thermal conductivity compared quantitatively, and the "
                   "free-electron model used for both thermal and electrical "
                   "conduction.",

    "ws": ["experimental-skills-and-investigations", "measurement"],

    "review_state": "draft",
}
