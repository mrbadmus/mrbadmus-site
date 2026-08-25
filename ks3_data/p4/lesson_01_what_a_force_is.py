"""P4 L1 — What a force is (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-01-what-a-force-is.dc.html`.

Her page wins outright. The wall and the skateboard, the five interaction
cases, the three questions and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA FIGURE, AND NONE IS OWED ──────────────────

Nothing on this page is calculated. It is a CLASSIFY-shaped MODEL lesson —
name both objects, give the size in newtons, say whether they touch — and
there is no relationship to draw. Design draws none, and the word
"triangle" appears zero times on her page.

── ⚖️ RULED · THE ARROWS ARE NOT DRAWN TO SCALE, AND THAT IS RIGHT ───

The five cases span about 2 N (a magnet on a paperclip) to about 200
billion billion N (the Earth on the Moon). A linear bar cannot carry
twenty orders of magnitude, so Design prints the sizes as values and draws
both arrows at ONE FIXED LENGTH. The equality the drawing asserts is that
the two forces in a pair are the SAME — true in every case — and it
asserts nothing at all about how big. The legal line says so.

Only the benches whose ranges are linear draw arrows to scale, and both of
those (`p4-02`, `p4-03`) say so in their own model-limitation line.

── ⚖️ RULED · "ABOUT" STAYS ON ALL TWELVE FORCE SIZES ────────────────

Design's hedge is load-bearing and it is not tidied. These are typical
values that depend on how hard, how fast and how far apart; removing the
word makes twelve false statements. The kick is *about* 300 N because it
depends on the boot and the contact time; the Earth–Moon pull is *about*
200 billion billion N because it depends where in the orbit you take it.

── ⚖️ RULED · WORDS, NOT STANDARD FORM, FOR 2 × 10²⁰ ─────────────────

Design's flag 7. The Bricolage and DM Mono latin subsets shipped in
`shared/fonts/` carry no superscript digits beyond ² and ³, so `10²⁰`
cannot be typeset — it would drop to a system font mid-number inside a
mono readout. "about 200 billion billion N" is what she wrote and what
ships. Her own 23 Aug audit then ruled the general convention (`10^20`
in prose); this page predates the need and reads better in words, so the
words stand.

── ⚠️ FOUR RAIL STOPS · `s-think` AND `s-keynote` ARE NOT AMONG THEM ─

    s-hook · s-bench · s-pairs · s-ladder

⚠️ **`s-pairs` TICKS AT ONE CASE, `s-bench` AT THREE.** Design's own
`DONE`: `s-bench` is `opened >= 3` and `s-pairs` is `opened >= 1`. The
band block is the payoff of the board beside it and carries no control, so
the board marks it — `band_anchor: "s-pairs"`, `band_at: 1`. MRB-249's
`mirrors` would tie the two together and tick the band stop two cases
late.

── ⚖️ FOUR MISCONCEPTIONS, AND `FORCE-13` HAS NO `elicited_by` ───────

    FORCE-12  a moving object has force in it, and it runs out
    FORCE-13  a table is not doing anything; it is just there
    FORCE-14  a force can only act between things that are touching
    FORCE-15  the force is in the movement, not in either object

`FORCE-13` has no `elicited_by`, which §5.3 allows: nothing on this page
asks the student to commit to it. It is confronted because it is the
belief sitting underneath `FORCE-12` — a force needs effort, intention or
a living thing at one end — and the second quote in `#s-think` is about
exactly that.

`FORCE-15` is NOT in Design's proposed table. It arrived with rung 1's
fourth option, *"the force is in the movement of the ball, and not in
either object"*, which is a genuinely separate belief: a student can hold
it while being perfectly sound that force does not run out.
"""

LESSON = {
    "slug":  "what-a-force-is",
    "title": "What a force is",
    "discipline": "physics",
    "unit": "Forces",
    "family": "MODEL",

    "covers": ["KS3.P.FORCES.01", "KS3.P.FORCES.05a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    # `requires` is the "Before this lesson" card; `references` is
    # "Connects to". Both are slugs, and both are validated against the flat
    # lesson registry, so a link here cannot point at a page the build did
    # not write. The forward/back moves are derived by the generator.
    "requires": [],
    "before_this": "Nothing — this is where the unit starts.",
    "assumes": [],
    "references": ["non-contact-forces", "what-forces-do-to-motion",
                   "pressure-force-over-area"],
    "ks4_links": [],

    "meta_description": "Push a wall on a skateboard and you roll away. The "
                        "wall did not move, did not spend anything and was "
                        "not trying — and it is the only thing that could "
                        "have pushed you. Name both ends of five forces.",

    "big_question": "Push a wall hard enough and you move backwards. Nothing "
                    "about you got stronger — so what actually pushed you?",

    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "The wall pushed you",  "done_when": "committed"},
        {"anchor": "s-bench", "short": "BOARD",
         "label": "Interaction board",    "done_when": "three_cases_opened"},
        {"anchor": "s-pairs", "short": "RULES",
         "label": "Three questions",      "done_when": "one_case_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The wall pushed you.",
        "prompt": "Stand on a skateboard, put your hands on a wall and push. "
                  "You roll away from the wall. The wall did not move, did "
                  "not spend anything, and was not trying — and it is the "
                  "only thing that could have pushed you.",
        "commit": "So what is a force?",
        "options": [
            "Something an object has inside it, which gets used up",
            "A push or a pull, always between two objects",
            "How fast something is going",
            "The energy stored in something that is moving",
        ],
        "answer": 1,
        "reveal": "A force is a push or a pull, and it is never something one "
                  "object has on its own. It takes two: you and the wall, "
                  "measured in newtons. <strong>Name only one object and you "
                  "have not finished describing the force.</strong>",
    },

    "misconceptions": [
        {"id": "FORCE-12",
         "statement": "A moving object has force in it, and the force runs "
                      "out.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "FORCE-13",
         "statement": "A table is not doing anything; it is just there.",
         "confronted_by": "s-think"},
        {"id": "FORCE-14",
         "statement": "A force can only act between things that are "
                      "touching.",
         "elicited_by": "board",
         "confronted_by": "board"},
        {"id": "FORCE-15",
         "statement": "The force is in the movement of the object, and not "
                      "in either object.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every force in this unit is one object pushing or pulling "
                 "another. The job on this page is to get into the habit of "
                 "naming both ends of it, and giving its size in newtons."},

        # ── #s-bench · the interaction board ───────────────────────────
        # ⚖️ The board opens on the QUESTION and no diagram. Drawing the pair
        # before the student names the partner would hand over the answer to
        # the only thing the case asks.
        {"type": "interaction-board",
         "id": "board",
         "anchor": "s-bench",
         "eyebrow": "At the bench · the interaction board",
         "heading": "Find the object on the other end",
         "progress": "0 of 5 cases opened",
         "tabs_label": "Pick a case",
         "target": 3,
         "band_anchor": "s-pairs",
         "band_at": 1,
         "cases": [
             {"id": "kick", "tab": "A kicked ball",
              "prompt": "A ball leaves a boot at speed. What is on the other "
                        "end of that force?",
              "a": "Foot", "b": "Ball", "kind": "push",
              "size": "about 300 N", "contact": True,
              "cap_a": "force on the foot", "cap_b": "force on the ball",
              "options": ["The foot", "The air around the ball",
                          "The speed the ball was given"],
              "notes": [
                  "The foot and the ball, touching for roughly a hundredth "
                  "of a second. Each feels about 300 N, in opposite "
                  "directions.",
                  "Air resistance is real, but it is not what sends the ball "
                  "up the pitch. The object on the other end is the foot, "
                  "and it feels about 300 N too.",
                  "Speed is not an object, so nothing can be on the other "
                  "end of it. The foot is the second object, and it feels "
                  "about 300 N too.",
              ],
              "alt": "A foot and a ball, touching, with an arrow on each "
                     "pointing away from the other, about 300 newtons each."},
             {"id": "caravan", "tab": "A caravan being towed",
              "prompt": "A caravan is dragged forward along a motorway. What "
                        "is on the other end of that force?",
              "a": "Tow bar", "b": "Caravan", "kind": "pull",
              "size": "about 2 000 N", "contact": True,
              "cap_a": "force on the tow bar",
              "cap_b": "force on the caravan",
              "options": ["The tow bar", "The road surface",
                          "The caravan’s own weight"],
              "notes": [
                  "The tow bar pulls the caravan forward with about 2 000 N, "
                  "and the caravan pulls back along the bar with about "
                  "2 000 N. A pull, and the two objects are touching.",
                  "The road does push up on the tyres and rub backwards on "
                  "them, but the pull along the line of travel comes from "
                  "the tow bar, at about 2 000 N.",
                  "Weight is a force, not an object, and it acts downwards "
                  "rather than forwards. The tow bar is the second object, "
                  "at about 2 000 N.",
              ],
              "alt": "A tow bar and a caravan, touching, with an arrow on "
                     "each pointing towards the other, about 2 000 newtons "
                     "each."},
             {"id": "paperclip", "tab": "A paperclip on a desk",
              "prompt": "A paperclip lifts off a desk and flies upwards. "
                        "What is on the other end of that force?",
              "a": "Magnet", "b": "Paperclip", "kind": "pull",
              "size": "about 2 N", "contact": False,
              "cap_a": "force on the magnet",
              "cap_b": "force on the paperclip",
              "options": ["A magnet held above it", "The desk",
                          "The air in the gap"],
              "notes": [
                  "The magnet pulls the paperclip up with about 2 N and the "
                  "paperclip pulls the magnet down with about 2 N, across a "
                  "gap of two centimetres with nothing in it.",
                  "The desk was holding the paperclip up, not pulling it "
                  "upwards. The pull comes from the magnet, across the gap, "
                  "at about 2 N.",
                  "Take the air out of the gap and the pull is unchanged. "
                  "The second object is the magnet, at about 2 N.",
              ],
              "alt": "A magnet and a paperclip, separated by a marked gap, "
                     "with an arrow on each pointing towards the other, "
                     "about 2 newtons each."},
             {"id": "swimmer", "tab": "A swimmer",
              "prompt": "A swimmer moves forward down the lane. What is on "
                        "the other end of that force?",
              "a": "Swimmer", "b": "Water", "kind": "push",
              "size": "about 150 N", "contact": True,
              "cap_a": "force on the swimmer", "cap_b": "force on the water",
              "options": ["The water", "The swimmer’s own muscles",
                          "The lane rope"],
              "notes": [
                  "The hand pushes about 150 N of water backwards, and the "
                  "water pushes the swimmer forwards with about 150 N. Watch "
                  "the wake: that is the other half of the pair.",
                  "Muscles are part of the swimmer, and a force needs a "
                  "second object. That object is the water, at about 150 N.",
                  "The rope marks the lane and is not touched. The forward "
                  "push comes from the water, at about 150 N.",
              ],
              "alt": "A swimmer and the water, touching, with an arrow on "
                     "each pointing away from the other, about 150 newtons "
                     "each."},
             {"id": "moon", "tab": "The Moon",
              "prompt": "The Moon keeps curving around the Earth instead of "
                        "leaving. What is on the other end of that force?",
              "a": "Earth", "b": "Moon", "kind": "pull",
              "size": "about 200 billion billion N", "contact": False,
              "cap_a": "force on the Earth", "cap_b": "force on the Moon",
              "options": ["The Earth", "Light from the Sun",
                          "The Moon’s own speed"],
              "notes": [
                  "The Earth pulls the Moon with about 200 billion billion "
                  "N, and the Moon pulls the Earth with the same force, "
                  "across 384 000 km of empty space.",
                  "Sunlight does push on things, but nowhere near hard "
                  "enough to hold a moon. The Earth is the second object, at "
                  "about 200 billion billion N.",
                  "Speed is not an object, and speed on its own would send "
                  "the Moon off in a straight line. The pull comes from the "
                  "Earth, at about 200 billion billion N.",
              ],
              "alt": "The Earth and the Moon, separated by a marked gap, "
                     "with an arrow on each pointing towards the other, "
                     "about 200 billion billion newtons each."},
         ],
         "readouts": [
             {"id": "pair", "label": "The two objects"},
             {"id": "size", "label": "Each force"},
             {"id": "kind", "label": "Push or pull"},
         ]},

        # ── #s-pairs · the three questions · NOT a bench ────────────────
        {"type": "force-band",
         "id": "three-questions",
         "anchor": "s-pairs",
         "eyebrow": "Every force, three questions",
         "heading": "Answer all three or you have not described it.",
         "panels": [
             {"num": "1", "name": "Which two objects?",
              "body": "Name both. “A force on the caravan” is half "
                      "an answer; “the tow bar pulls the caravan” "
                      "is a whole one."},
             {"num": "2", "name": "Push or pull, and how big?",
              "body": "Forces are measured in newtons, written N. An apple "
                      "resting on your hand presses down with about 1 N."},
             {"num": "3", "name": "Touching, or across a gap?",
              "body": "Most forces need contact. Gravity, magnetism and "
                      "static electricity do not, and they are no less real "
                      "for it."},
         ]},

        {"type": "key-fact", "ref": "a-force-takes-two"},

        {"type": "misconception", "id": "think-force-in-it",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        # ⚖️ TWO QUOTES, ONE BLOCK. Design draws the second behind an
        # amber-topped divider rather than as a second block: one wrong idea,
        # then the belief sitting underneath it. `_confrontations` renders
        # exactly that from `statements[]`.
        {"id": "think-force-in-it",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-12",
         "statements": [
             {"quote": "A moving object has force in it, and the force runs "
                       "out.",
              "targets": "FORCE-12",
              "body": [
                  "This is the oldest idea in physics and almost everyone "
                  "arrives holding it: a thrown ball carries a supply of "
                  "force that gradually empties, which is why it slows down "
                  "and falls. It is wrong in a way that matters, because a "
                  "force is not stuff and cannot be stored. A ball has "
                  "speed, and it has energy — both of which really are "
                  "properties of the ball on its own — but the force on it "
                  "exists only while some second object is pushing or "
                  "pulling it. The moment your hand lets go, the hand's push "
                  "on the ball stops existing. <strong>What slows the ball "
                  "down is not the push running out; it is two other "
                  "objects, the air and the Earth, pushing and pulling on it "
                  "the whole way.</strong>",
              ]},
             {"quote": "A table is not doing anything. It is just there.",
              "targets": "FORCE-13",
              "body": [
                  "Put a book on your palm and you can feel yourself pushing "
                  "up; the table is doing the same thing and feels nothing "
                  "because it is not alive. Every surface presses back on "
                  "whatever presses into it — that is what stops the book "
                  "going through the table, and it is why a shelf can only "
                  "take so much before it snaps. <strong>A force does not "
                  "require effort, intention or a living thing at either "
                  "end. It requires two objects.</strong>",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "a-force-takes-two",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A force is a push or a pull on one object, caused by a "
                 "second object. Forces are measured in newtons (N), and "
                 "they always come in pairs of the same size acting on the "
                 "two different objects."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. Design's own two rungs both sit at
    # index 0, as all 44 of hers in P4–P6 do. Her option TEXTS and her
    # correct answer are untouched; only the order in which four options are
    # listed changes, and it cycles 0,1,2,3 across the unit's eighteen rungs.
    # This lesson takes 0 and 1.
    "ladder": {
        "recall": {
            "q": "A footballer heads a ball. Which statement describes the "
                 "force correctly?",
            "options": [
                "The head pushes the ball, and the ball pushes the head just "
                "as hard.",
                "The ball has force stored in it, and the force is used up "
                "when it hits the head.",
                "The head gives its force to the ball, and the ball keeps "
                "that force until it stops.",
                "The force is in the movement of the ball, and not in either "
                "object.",
            ],
            "answer": 0,
            "feedback": {
                1: "A force is not stuff and cannot be stored or spent. It "
                   "exists only while two objects are interacting.",
                2: "Nothing is handed over. The head’s push on the ball "
                   "stops existing the moment they separate; the ball keeps "
                   "its speed, not a force.",
                3: "Movement is not a force. The force is one object pushing "
                   "another, so it has to be named at both ends.",
            },
            "title": "Rung 1 · Name the pair"},
        "apply": {
            "q": "A magnet lifts a paperclip across a gap of two "
                 "centimetres. Which statement is right?",
            "options": [
                "The air in the gap must be carrying the pull from one to "
                "the other.",
                "A force can act between two objects that are not touching.",
                "The paperclip is magnetic already, so no force is needed to "
                "lift it.",
                "The magnet uses up some force each time it pulls, so it "
                "will stop working.",
            ],
            "answer": 1,
            "feedback": {
                0: "Pump the air out and the pull is exactly the same. The "
                   "gap does not need filling for the force to act.",
                2: "Something has to lift it, and being attracted is not the "
                   "same as moving. The magnet supplies the pull.",
                3: "A magnet is not a store of force being spent. Its pull "
                   "is a property of the interaction, and it does not empty.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Someone on a skateboard pushes a wall and rolls backwards. "
                 "Name every object involved and every force in the pair, "
                 "and say which force moved the skater.",
            "field_label": "Your explanation",
            "placeholder": "The two objects are…",
            "success": [
                "Names both objects: the skater (with the board) and the "
                "wall.",
                "Says the skater pushes the wall forwards.",
                "Says the wall pushes the skater backwards.",
                "Gives both forces the same size, in newtons.",
                "Says it is the wall’s push on the skater that moved "
                "the skater, not the skater’s own push.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A spacecraft far from any planet fires its engine and "
                 "speeds up. There is nothing around it to push against. "
                 "Name the second object in that interaction, and explain "
                 "how you know a second object must exist.",
            "field_label": "Your answer",
            "placeholder": "The second object is…",
            "success": [
                "Names the exhaust gas, or the fuel thrown out of the "
                "engine, as the second object.",
                "Says the engine pushes the gas backwards.",
                "Says the gas pushes the spacecraft forwards with the same "
                "force.",
                "Says a force cannot exist with only one object, which is "
                "how you know something must be there.",
                "Notes that empty space is not a problem, because the pair "
                "does not need anything outside the spacecraft.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A force is a push or a pull, measured in newtons. It is not "
                "something an object owns and not something that runs out — "
                "it exists only while two objects are interacting, and it "
                "acts on both of them equally and in opposite directions. "
                "Some of those interactions need contact and some do not.",

    # ⊕ §5.6 — Design's "Going further" is the engine's `stretch` layer.
    "stretch": [
        {"id": "why-anything-moves",
         "type": "explainer",
         "text": "If the two forces in every pair are always equal and "
                 "opposite, why does anything ever move? Because they act on "
                 "<em>different objects</em>, and only forces on the same "
                 "object can cancel. When you push the wall, the wall's push "
                 "acts on you and yours acts on the wall — nothing cancels "
                 "anything. You accelerate because your total force is not "
                 "zero, and the wall does not because it is bolted to a "
                 "building, and to the Earth, which is very hard to shift "
                 "with 200 N."},
        {"id": "rocket-in-a-vacuum",
         "type": "explainer",
         "text": "A rocket in deep space has nothing to push against, and it "
                 "accelerates anyway. The second object is the exhaust: the "
                 "engine throws several tonnes of hot gas backwards every "
                 "second, and the gas pushes the rocket forwards with "
                 "exactly the same force. This is why a rocket works better "
                 "in a vacuum than in air, which is the opposite of what "
                 "most people guess. It is also why the newton is defined "
                 "the way it is — <strong>one newton is the force that "
                 "changes the speed of one kilogram by one metre per second, "
                 "every second</strong>, and nothing in that definition "
                 "mentions anything touching."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "force",
         "definition": "A push or a pull on one object, caused by a second "
                       "object. Measured in newtons. Never something one "
                       "object has on its own."},
        {"term": "newton",
         "definition": "The unit of force, written N. An apple resting on "
                       "your hand presses down with about 1 N."},
        {"term": "contact force",
         "definition": "A force that only acts while the two objects are "
                       "touching — friction, air resistance, the push of a "
                       "table."},
        {"term": "non-contact force",
         "definition": "A force that acts across a gap with nothing in "
                       "between: gravity, magnetism, and the force between "
                       "electric charges."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Stuck naming the second object in a case of your own?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Contact and non-contact forces, free-body diagrams, and "
                   "Newton's third law as interaction pairs.",

    # ⚖️ THE HEDGE IS DECLARED HERE, WHERE THE PAGE CAN BE HELD TO IT. Every
    # size on the board reads "about" because these are typical values that
    # depend on how hard, how fast and how far apart; the foot line says so
    # rather than leaving twelve numbers looking like measurements.
    "convention_note": "Force sizes on the interaction board are typical "
                       "values, rounded, and are marked “about” "
                       "because they depend on how hard, how fast and how "
                       "far apart. The board draws one interaction at a time "
                       "and leaves out every other force acting on the two "
                       "objects.",

    "ws": [],
}
