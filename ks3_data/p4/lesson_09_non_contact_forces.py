"""P4 L9 — Non-contact forces (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-09-non-contact-forces.dc.html`.

Her page wins outright. The balloon and the hair, the eight-case sorter,
the three cards and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NONE IS OWED ───────────────────

A classification. Nothing here is calculated, and the inverse-square law
is not KS3. Design draws no figure of a relationship and the word
"triangle" appears zero times on her page.

── ⚖️ RULED · THE SORTER SEALS ITS VERDICT UNTIL A LABEL IS PRESSED ──

The diagram — two bodies, a gap or contact marker, a force arrow — is
drawn from the start, because it carries the evidence the classification
is made from. The verdict is not. Printing the answer beside the drawing
would remove the only demand the block makes, so `r_force_sorter` emits
every verdict hidden and the unlabelled state says in words that nothing
is revealed until you commit.

The four buttons LOCK on commit. A sorter that lets a student cycle
through labels until the tick appears has been reduced to a guessing game.

── ⚖️ RULED · AIR RESISTANCE IS A CONTACT FORCE ──────────────────────

Design's own note calls this one *"worth arguing about"* and files it as
contact, because air is made of particles and they strike the canopy;
nothing acts across a gap. It is deliberately in the deck: it is the card
a student who has only half-heard `p4-01` gets wrong, and rung 1's second
option is the same trap with the same correction — *a gap you cannot see
is not a gap*.

── ⚖️ `p4-09` RE-TEACHES THE SPLIT RATHER THAN REFERRING BACK ────────

`p4-01` already draws the contact/non-contact distinction. This lesson
teaches it as a classification from first principles and does not assume
`p4-01` has happened — no lesson in P4 assumes sequence, and every
cross-reference is an offer rather than a recap.

── ⚠️ FOUR RAIL STOPS, AND `s-three` TICKS AT ONE CASE ───────────────

    s-hook · s-bench · s-three · s-ladder

Design's `DONE`: `s-bench` is `count >= CASES.length` — all eight — and
`s-three` is `count >= 1`. The sorter marks the band section at one.

── ⚖️ THREE MISCONCEPTIONS, AND `FORCE-45` HAS NO `elicited_by` ──────

    FORCE-44  a force needs something in between to carry it across
    FORCE-45  there is no gravity in space
    FORCE-46  magnets attract all metals

`FORCE-45` has no `elicited_by`: nothing on the page asks a student to
commit to it before it is confronted, and rung 2 marks it wrong rather
than eliciting it. `FORCE-46` is confronted only by the *tell* line on
card 2 — *not aluminium, not copper, not gold* — which is where a
student's own counter-example lands.

⚠️ Design's proposed table has `FORCE-35` for the magnet belief with
*(none)* as its elicitation. Kept, renumbered.
"""

LESSON = {
    "slug":  "non-contact-forces",
    "title": "Non-contact forces",
    "discipline": "physics",
    "unit": "Forces",
    "family": "CLASSIFY",

    "covers": ["KS3.P.FORCES.08"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["springs-and-hookes-law"],
    "assumes": [],
    "references": ["what-a-force-is", "friction",
                   "balanced-and-unbalanced"],
    "ks4_links": [],

    "meta_description": "Rub a balloon and the hair reaches out to meet it "
                        "across a clear centimetre of air. Three forces at "
                        "KS3 act across a gap, and one of them is holding "
                        "you to the planet.",

    "big_question": "Every force so far has needed something to touch "
                    "something. Three of them do not, and one of those is "
                    "holding you to the planet right now.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Balloon and hair", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "SORT",
         "label": "The sorter",       "done_when": "all_eight_labelled"},
        {"anchor": "s-three",  "short": "THREE",
         "label": "The three",        "done_when": "one_case_labelled"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The hair moves before the balloon arrives.",
        "prompt": "Rub a balloon on a jumper and bring it slowly towards "
                  "someone's head. The hair stands up and reaches out to "
                  "meet it — while there is still a clear centimetre of air "
                  "in between.",
        "commit": "What is pulling the hair?",
        "options": [
            "The air in between is pushing the hair upwards",
            "The balloon touches the hair too quickly to see",
            "Some forces act across a gap, with nothing in between",
            "Static is a stickiness rather than a force",
        ],
        "answer": 2,
        "reveal": "A force is acting across the gap. Rubbing moved electric "
                  "charge from the jumper to the balloon, and charge "
                  "attracts and repels other charge without any contact at "
                  "all. There are three forces in KS3 that work like this "
                  "— gravity, magnetism and electrostatic force — and "
                  "calling them <strong>non-contact</strong> forces is the "
                  "whole of the classification.",
    },

    "misconceptions": [
        {"id": "FORCE-44",
         "statement": "A force needs something in between to carry it "
                      "across.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "FORCE-45",
         "statement": "There is no gravity in space.",
         "confronted_by": "s-think"},
        {"id": "FORCE-46",
         "statement": "Magnets attract all metals.",
         "confronted_by": "three-forces"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>contact force</strong> needs the two objects to "
                 "be touching: friction, air resistance, tension in a rope, "
                 "the push of a table. A <strong>non-contact force</strong> "
                 "acts across a gap with nothing in between: gravity, "
                 "magnetism, and the electrostatic force between charges. "
                 "Both kinds are measured in newtons and both change motion "
                 "in exactly the same three ways."},

        # ── #s-bench · the sorter ──────────────────────────────────────
        {"type": "force-sorter",
         "id": "sorter",
         "anchor": "s-bench",
         "eyebrow": "At the bench · the sorter",
         "heading": "Eight situations. Four labels.",
         "progress": "0 of 8 labelled",
         "lead": "Pick a situation, look at whether the two things are "
                 "touching, then give it a label. The diagram marks the gap "
                 "or the contact for you; the naming is yours.",
         "ask_label": "Give it a label",
         "sealed_label": "Unlabelled. Nothing is revealed until you commit "
                         "to one of the four.",
         "contact_label_id": "contact",
         "band_anchor": "s-three",
         "band_at": 1,
         "labels": [
             {"id": "contact", "label": "Contact force"},
             {"id": "gravity", "label": "Gravity"},
             {"id": "magnetic", "label": "Magnetism"},
             {"id": "static", "label": "Electrostatic"},
         ],
         "cases": [
             {"id": "book", "tab": "Book on a table",
              "title": "A book resting on a table",
              "a": "table top", "b": "book", "answer": "contact",
              "touch": True, "sense": "Push, upwards",
              "note": "The two are pressed together, so this is a contact "
                      "force — the squashed surface of the table pushing "
                      "back on the book. Move the book a millimetre clear "
                      "and the force vanishes instantly, which is the test "
                      "for contact."},
             {"id": "kick", "tab": "Kicking a football",
              "title": "A boot kicking a football",
              "a": "boot", "b": "ball", "answer": "contact",
              "touch": True, "sense": "Push, forwards",
              "note": "Contact, and only while they touch — about a "
                      "hundredth of a second. Once the ball has left the "
                      "boot nothing is pushing it forwards at all, which is "
                      "the whole argument of the lesson on what forces do to "
                      "motion."},
             {"id": "chute", "tab": "Air on a parachute",
              "title": "Air resistance on an open parachute",
              "a": "air", "b": "canopy", "answer": "contact",
              "touch": True, "sense": "Push, upwards",
              "note": "This one is worth arguing about, and it is a contact "
                      "force. Air is made of particles, and they strike the "
                      "canopy; nothing acts across a gap. If it feels like "
                      "an odd fit, that is because the thing doing the "
                      "touching is a fluid rather than a solid."},
             {"id": "stone", "tab": "A dropped stone",
              "title": "A stone falling after being dropped",
              "a": "Earth", "b": "stone", "answer": "gravity",
              "touch": False, "sense": "Pull, downwards",
              "note": "Gravity, acting across the gap between the Earth and "
                      "the stone. Nothing is touching the stone once your "
                      "hand has let go, and the pull is the same whether the "
                      "stone is one metre up or a hundred."},
             {"id": "moon", "tab": "The Moon in orbit",
              "title": "The Moon circling the Earth",
              "a": "Earth", "b": "Moon", "answer": "gravity",
              "touch": False, "sense": "Pull, towards the Earth",
              "note": "Gravity across 384 000 kilometres of vacuum. The pull "
                      "is sideways-on to the Moon’s motion, so it bends "
                      "the path into a circle instead of dragging the Moon "
                      "in — a force acting at a distance, doing exactly "
                      "what a resultant force always does."},
             {"id": "fridge", "tab": "Magnet on a fridge",
              "title": "A magnet holding a note on a steel fridge door",
              "a": "magnet", "b": "steel door", "answer": "magnetic",
              "touch": False, "sense": "Pull, together",
              "note": "Magnetism. The magnet is resting on the door, but the "
                      "force does not need that contact: slide a sheet of "
                      "paper or a hand between them and it still holds. That "
                      "is the difference between two things touching and a "
                      "force that needs touch."},
             {"id": "compass", "tab": "A compass needle",
              "title": "A compass needle swinging to point north",
              "a": "Earth", "b": "needle", "answer": "magnetic",
              "touch": False, "sense": "Turn, towards north",
              "note": "Magnetism, from the Earth itself, acting on a needle "
                      "thousands of kilometres away through the air, through "
                      "the case and through nothing. Notice what the force "
                      "does here: it does not move the needle along, it "
                      "turns it — a moment."},
             {"id": "balloon", "tab": "Balloon and hair",
              "title": "A rubbed balloon lifting someone’s hair",
              "a": "balloon", "b": "hair", "answer": "static",
              "touch": False, "sense": "Pull, together",
              "note": "The electrostatic force, between charge on the "
                      "balloon and charge in the hair. It works across a "
                      "visible gap of a centimetre or two, and it stops "
                      "working after a while as the charge leaks away — "
                      "especially on a damp day."},
         ],
         "readouts": [
             {"id": "yours", "label": "Your label"},
             {"id": "true", "label": "The force"},
             {"id": "kind", "label": "Contact or not"},
             {"id": "sense", "label": "Pull or push"},
         ]},

        # ── #s-three · the three, and how to tell them apart ───────────
        {"type": "force-band",
         "id": "three-forces",
         "anchor": "s-three",
         "eyebrow": "The three, and how to tell them apart",
         "heading": "Only one of them can never push.",
         "panels": [
             {"num": "1", "name": "Gravity",
              "body": "Acts between anything with mass — you and the "
                      "Earth, the Earth and the Moon, you and this page. It "
                      "never switches off, and it gets weaker the further "
                      "apart the two things are.",
              "tell": "Tell it by: it only ever pulls. There is no such "
                      "thing as gravitational repulsion."},
             {"num": "2", "name": "Magnetism",
              "body": "Acts between magnets, and between a magnet and a "
                      "magnetic material — iron, steel, nickel, cobalt. "
                      "Not aluminium, not copper, not gold, so a magnet does "
                      "not attract all metals.",
              "tell": "Tell it by: like poles repel, unlike poles attract. "
                      "It can push as well as pull."},
             {"num": "3", "name": "The electrostatic force",
              "body": "Acts between electric charges, which is what rubbing "
                      "two materials together moves about. Same reason your "
                      "jumper crackles and cling film sticks to itself.",
              "tell": "Tell it by: like charges repel, opposite charges "
                      "attract. It fades as the charge leaks away."},
         ],
         "close": "That difference matters more than it looks. Magnetism and "
                  "electrostatic force can cancel themselves out, because "
                  "for every attraction there is a repulsion available. "
                  "Gravity cannot, so it never cancels — it only ever adds "
                  "up. <strong>Which is why the weakest of the three is the "
                  "one that shapes planets, stars and galaxies.</strong>"},

        {"type": "key-fact", "id": "three-act-at-a-distance"},

        {"type": "misconception", "id": "think-something-in-between",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-something-in-between",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-44",
         "statements": [
             {"quote": "Something must be in between to carry the force "
                       "across.",
              "targets": "FORCE-44",
              "body": [
                  "It is a reasonable demand — every force you can feel "
                  "with your hands is delivered by contact — and for two "
                  "hundred years it bothered the best physicists alive. "
                  "Newton himself would not claim to explain how the Sun "
                  "pulls on the Earth across a hundred and fifty million "
                  "kilometres of nothing; he only gave the arithmetic. Take "
                  "the air out of a jar and a magnet still attracts a "
                  "paperclip inside it; put a vacuum between the Earth and "
                  "the Moon, which is what is actually there, and the pull "
                  "continues. The modern answer is not a substance but a "
                  "<strong>field</strong>: the magnet changes the space "
                  "around it, and anything magnetic that enters that space "
                  "feels a force. What travels is a change in the field, and "
                  "it travels through nothing quite happily.",
              ]},
             {"quote": "There is no gravity in space.",
              "targets": "FORCE-45",
              "body": [
                  "If that were true the space station would fly off in a "
                  "straight line and the Moon would leave. The station "
                  "orbits about four hundred kilometres up, where the "
                  "Earth's pull is only slightly weaker than it is in your "
                  "classroom, and <strong>the astronauts inside are not "
                  "weightless — they are falling.</strong> So is the "
                  "station, at exactly the same rate, which is why nothing "
                  "inside presses on anything: they fall together, and the "
                  "sideways speed means the fall keeps missing the planet. "
                  "The word for what they experience is <em>free fall</em>, "
                  "and you get a tiny sample of it at the top of a "
                  "trampoline bounce.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "three-act-at-a-distance",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Gravity, magnetism and the electrostatic force act at a "
                 "distance, with no contact and nothing needed in between. "
                 "Gravity only ever attracts; the other two attract and "
                 "repel. All are measured in newtons, and all change motion "
                 "in the same three ways as a push or a pull."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3,
    # closing the unit's eighteen rungs on [5, 5, 4, 4] across the four
    # indices — no index over half, none unused.
    "ladder": {
        "recall": {
            "q": "Which of these is a non-contact force?",
            "options": [
                "Air resistance slowing a cyclist down.",
                "The tension in a tug-of-war rope.",
                "The Earth pulling on a satellite four hundred kilometres "
                "above it.",
                "Friction between a brake block and a wheel rim.",
            ],
            "answer": 2,
            "feedback": {
                0: "Air is made of particles that strike the cyclist, so "
                   "this is contact. A gap you cannot see is not a gap.",
                1: "The rope touches both teams. Let go and the force is "
                   "gone at once, which is the mark of a contact force.",
                3: "Friction only exists between surfaces that are touching. "
                   "Lift the block clear and there is no friction at all.",
            },
            "title": "Rung 1 · Classify"},
        "apply": {
            "q": "Astronauts float around inside the space station. Why?",
            "options": [
                "There is no gravity that far from the Earth.",
                "The speed of the station cancels out gravity, because "
                "anything moving fast enough sideways stops being pulled "
                "downwards at all.",
                "They are above the atmosphere, and gravity needs "
                "something in between to carry it across, so it stops acting "
                "once the air has run out.",
                "Gravity is still pulling on them — they and the station "
                "are falling around the Earth together, so nothing presses "
                "on anything.",
            ],
            "answer": 3,
            "feedback": {
                0: "At that height the Earth’s pull is only a little "
                   "weaker than at the ground. With no gravity the station "
                   "would leave in a straight line.",
                1: "Speed does not cancel a force. The sideways speed means "
                   "the fall keeps missing the Earth, which is what an orbit "
                   "is — the gravity is still there, unopposed.",
                2: "Gravity crosses a vacuum perfectly well — that is what "
                   "non-contact means. It is also how the Moon is held.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A plastic ruler rubbed on a sleeve picks up small pieces "
                 "of paper from the desk before it reaches them. Explain why "
                 "this is a non-contact force, and describe one thing you "
                 "could do to show the force is real rather than the paper "
                 "being blown about.",
            "field_label": "Your explanation",
            "placeholder": "Rubbing the ruler…",
            "success": [
                "Says rubbing moves electric charge on to the ruler.",
                "Says the electrostatic force acts between that charge and "
                "the paper.",
                "Says the paper moves while there is still a gap, with "
                "nothing touching it.",
                "Names a check that rules out air movement — for example "
                "moving the ruler in slowly and steadily, or holding it "
                "still above the paper.",
                "Says the force gets stronger as the ruler gets closer, or "
                "weaker as the charge leaks away.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A maglev train floats about a centimetre above its track "
                 "and is pushed along without anything touching it. Sort the "
                 "forces acting on it into contact and non-contact, and "
                 "explain why it can reach higher speeds than a train on "
                 "steel wheels.",
            "field_label": "Your answer",
            "placeholder": "The forces holding it up and pushing it along "
                           "are…",
            "success": [
                "Says the lifting force and the driving force are both "
                "magnetic, and therefore non-contact.",
                "Says the train’s weight is the gravitational pull of "
                "the Earth, also non-contact.",
                "Says air resistance is a contact force and is still acting "
                "on it.",
                "Says there is almost no friction, because no surfaces are "
                "sliding or rolling on each other.",
                "Says that with the backwards forces reduced to air "
                "resistance alone, the train can hold a much higher steady "
                "speed for the same driving force.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A contact force needs the two objects to be touching; a "
                "non-contact force acts across a gap with nothing in "
                "between. The three at Key Stage 3 are gravity, magnetism "
                "and the electrostatic force. Gravity only ever attracts; "
                "the other two can attract or repel. All are measured in "
                "newtons and all change motion the same three ways.",

    "stretch": [
        {"id": "the-field-answer",
         "type": "explainer",
         "text": "Newton gave the arithmetic of gravity and refused to guess "
                 "at the mechanism — <em>hypotheses non fingo</em>, I do "
                 "not feign hypotheses — and that refusal stood for over a "
                 "century. The answer, when it came, arrived from magnetism: "
                 "Faraday, who had almost no mathematics, imagined lines "
                 "filling the space around a magnet and insisted that the "
                 "space itself was doing something. Maxwell then wrote the "
                 "equations. A <strong>field</strong> is not a substance "
                 "sitting in the gap; it is a property the space has, and "
                 "the force is what an object feels for being in it. It also "
                 "means the force is not instant: change the magnet and the "
                 "change spreads outwards at the speed of light."},
        {"id": "the-weakest-one-wins",
         "type": "explainer",
         "text": "Gravity is by far the weakest of the three — a fridge "
                 "magnet a few centimetres across beats the entire Earth in "
                 "a straight pull on a paperclip. What it has instead is "
                 "that it never cancels. Every atom in a planet pulls every "
                 "atom in you, always attracting, so the total adds up "
                 "without limit; magnetism and electrostatic force are "
                 "stronger but come in two signs, so on any large object "
                 "they very nearly cancel themselves out. That is why the "
                 "weakest of the three is the one that decides the shape of "
                 "the universe, and the other two decide the shape of "
                 "everything smaller than a mountain."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "contact force",
         "definition": "A force that only acts while the two objects are "
                       "touching. Move them apart and it vanishes at once."},
        {"term": "non-contact force",
         "definition": "A force that acts across a gap with nothing in "
                       "between. Gravity, magnetism, and the force between "
                       "charges."},
        {"term": "electrostatic force",
         "definition": "The force between electric charges. Like charges "
                       "repel, opposite charges attract, and it fades as the "
                       "charge leaks away."},
        {"term": "field",
         "definition": "What a magnet, a charge or a mass does to the space "
                       "around it. Anything entering that space feels a "
                       "force, with nothing in between."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a situation you cannot decide how to label?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Gravitational, magnetic and electric fields, field lines "
                   "and field strength, and how the force between two "
                   "objects falls with distance.",

    "convention_note": "The sorter uses the three non-contact forces named "
                       "at Key Stage 3. There are others in physics — the "
                       "forces inside an atomic nucleus among them — and "
                       "they are not in scope here. Air resistance is filed "
                       "as a contact force because the air particles strike "
                       "the surface; the diagram draws the two objects at a "
                       "fixed size and does not show relative distances to "
                       "scale.",

    "ws": [],
}
