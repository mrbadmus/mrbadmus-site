"""P9 L3 — Electric fields (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p9/p9-03-electric-fields.dc.html`.

Her page wins outright. The comb and the water, the field map, the three
kinds of field and all four rungs are hers.

── ⚖️ RULED · NO CHILDLINE BLOCK ON THIS PAGE ───────────────────────

Mide, 21 Aug 2026, and Design's §6 reaches the same conclusion for the
same reason: *Going further* explains why a car is safe in a thunderstorm
and rung 4 asks for it, but that is safety information a student is being
GIVEN, not a risk they are being asked to disclose. Adding the block here
would dilute a block that means something where it is used.

── ⚖️ THE NULL POINT IS A STOP THE SLIDER LANDS ON ──────────────────

Two equal positives sit at 350 and 650 on a 1000-wide viewBox, so the
exact mid-point is 500 — which is step 12 of the slider's 25, because the
test point runs `x = 80 + 35 × step`. The state is not a limit the
student approaches; it is a place the control stops. That matters,
because the commit gate asks about precisely that point and rung 2 turns
on it, and a branch nobody can reach is authored copy no student will
read (5A.1). `r_field_grid` refuses an arrangement whose null point the
slider cannot land on.

Its note carries the sentence the whole rung is about: *a point like this
is not a place where the field is weak — it is a place where it cancels*.

── ⚖️ ON TOP OF A CHARGE, THE BENCH REFUSES TO REPORT ───────────────

The model treats a charge as a point, so within 62 units of one it has no
sensible value — and the grid leaves those samples out for the same
reason. The tiles say *no value here* rather than printing a very large
number, and the note says why. A bench that drew an enormous arrow there
would be teaching a figure its own model cannot support.

── ⚖️ NO FIELD STRENGTH IN NEWTONS PER COULOMB ──────────────────────

The unit is beyond this stage. The reading is a RELATIVE figure with 100
set at the strongest point the grid samples, declared as a scale in the
legal line — the same treatment `p9-02` gives its force, and for the same
reason.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0, as do
all six across P9. **Her option TEXT and every correction are verbatim;
only the ORDER moves.** This lesson takes indices **2 and 1**. Engine
policy, not a register row.

── ⚠️ MRB-177 · ONE DISTRACTOR LENGTHENED, ON HER HOOK ───────────────

The hook's correct option is 17 words against a longest distractor of 13
— a tell at the ≥4-word threshold, and the hook is the one option set
where a tell does the most damage: a student who spots the answer never
commits, and a misconception nobody commits to cannot be confronted. The
remedy is at the DISTRACTOR: option D now states its wrong rule in full
("…and two opposite charges pull on each other directly across the gap")
rather than trailing off at "the two attract directly". Registered in
`DEPARTURES-P9.md`.
"""

LESSON = {
    "slug": "electric-fields",
    "title": "Electric fields",
    "discipline": "physics",
    "unit": "Static electricity",
    "family": "MODEL",

    "covers": ["KS3.P.STAT.02"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    # ⚠️ Design's §4: `p9-03` restates induction in one clause rather than
    # depending on `p9-02` for it, so a school running the unit in another
    # order strands nobody. The edge is the honest reading order all the same.
    "requires": ["forces-between-charges"],
    "assumes": [],
    "references": ["charging-by-rubbing",
                   {"unit": "P8", "lesson": "potential-difference"},
                   {"unit": "P8", "lesson": "current-and-circuits"}],
    "ks4_links": [],

    "meta_description": "Nothing crosses the gap. A charged object changes "
                        "the space around it instead, and anything charged "
                        "that arrives feels a push or a pull straight away.",

    "big_question": "Nothing crosses the gap. A charged object changes the "
                    "space around it instead, and anything charged that "
                    "arrives in that space feels a push or a pull straight "
                    "away.",

    "rail": [
        {"anchor": "s-hook",   "short": "WATER",
         "label": "Comb and water",     "done_when": "committed"},
        {"anchor": "s-field",  "short": "BENCH",
         "label": "Move the test point", "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone. Ticked by the
        # bench through `band_anchor` / `band_at`, never by `mirrors` — see
        # `ks3_data/p9/__init__.py`.
        {"anchor": "s-reach",  "short": "FIELDS",
         "label": "Three forces",       "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The comb bends the water without touching it.",
        "prompt": "Run a tap down to the thinnest steady stream it will give "
                  "and bring a comb you have just pulled through dry hair up "
                  "to the side of it. The stream bends towards the comb, "
                  "from a couple of centimetres away, and nothing is "
                  "touching anything.",
        "commit": "What is in the gap, doing the work?",
        "options": [
            "Nothing at all — the comb changes the space around it, and the "
            "water responds to that",
            "Air, pushed sideways by the charge on the comb, which then "
            "shoves the stream over",
            "A thin thread of charge travelling from the comb to the water "
            "and pulling on it",
            # ⚠️ MRB-177 — Design's distractor, FINISHED. It ended at "and
            # the two attract directly" (13 words) against a 17-word correct
            # option, which is a tell at the ≥4-word threshold. On a hook that
            # matters more than anywhere else: a student who spots the answer
            # never commits, and a belief nobody commits to cannot be
            # confronted. Remedied at the distractor, and the added clause is
            # the wrong rule stated completely rather than padding.
            "Nothing — the water is already charged, and two opposite charges "
            "pull across the gap",
        ],
        "answer": 0,
        "reveal": "Nothing crosses the gap. The comb fills the space around "
                  "it with an <strong>electric field</strong>, and the water "
                  "— which is neutral, and stays neutral — has its own "
                  "charges pushed slightly to one side by that field, so it "
                  "is pulled in. Pump the air out and the effect is "
                  "unchanged: the field needs no material to exist in.",
    },

    "misconceptions": [
        {"id": "CHRG-09",
         "statement": "A field only exists when something is in it to feel "
                      "it.",
         "confronted_by": "s-think"},
        {"id": "CHRG-10",
         "statement": "The air in the gap must be carrying the force.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "CHRG-11",
         "statement": "The field is strongest half-way between two like "
                      "charges.",
         "elicited_by": "field",
         "confronted_by": "field"},
        {"id": "CHRG-12",
         "statement": "A negative charge follows the field arrows, the same "
                      "way a positive one does.",
         "elicited_by": "s-ladder",
         "confronted_by": "field"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Two charged objects push and pull on each other across a "
                 "gap with nothing in between, and that is genuinely "
                 "strange. Physics deals with it by splitting the problem in "
                 "two. First, a charged object fills the space around it "
                 "with an <strong>electric field</strong>. Second, anything "
                 "charged that finds itself in that space feels a force from "
                 "the field where it is standing."},
        {"type": "explainer",
         "text": "So the field is a property of <em>space itself</em>, not "
                 "of the object that made it and not of the object that "
                 "feels it. It has a value at every point, and that value "
                 "has a size and a direction. A field arrow is drawn "
                 "pointing the way a <strong>small positive charge</strong> "
                 "would be pushed if you put one there — which means arrows "
                 "point away from positive charges and towards negative "
                 "ones. A negative charge put at the same point feels a "
                 "force the other way."},
        {"type": "explainer",
         "text": "Two things follow. The field is there whether or not "
                 "anything is in it, waiting; and the field is what carries "
                 "the interaction across the gap, so no air, no wire and no "
                 "contact is needed. In a vacuum it works exactly the same."},

        # ── #s-field · a field map and one test point ──────────────────
        {"type": "field-grid",
         "id": "field",
         "anchor": "s-field",
         "eyebrow": "At the bench · a field map and one test point",
         "heading": "Move the test point around.",
         # ⚠️ A MAP OF NAMED STATES, NOT A STRING — see `p9-01`'s note and the
         # long one where `_head` is NOT, in `ks3_art/p9.py`.
         "progress": {"idle": "Change a control to begin",
                      "live": "Both controls live"},
         "lead": "The small arrows are the field, sampled on a grid: each "
                 "one shows which way a small positive charge would be "
                 "pushed there, and how hard. The big arrow is your test "
                 "point.",
         # ⚖️ HER CONSTANTS. `eref` is the field strength that reads 100 on
         # the scale; `near` is how close to a charge the model stops giving
         # a value, and it governs both the omitted grid samples and the
         # "no value here" state. `x0` and `dx` place the test point, and
         # they are what makes the null point land on step 12.
         "eref": 2.5e-4,
         "x0": 80,
         "dx": 35,
         "near": 62,
         "band_anchor": "s-reach",
         "band_at": 1,
         "start_setup": 2,
         "setup_label": "What is making the field",
         "convention_label": "EVERY ARROW POINTS THE WAY A SMALL POSITIVE "
                             "CHARGE WOULD BE PUSHED",
         "gate": {
             "prompt": "Commit first. Two equal positive charges sit a few "
                       "centimetres apart. What is the field at the point "
                       "exactly half-way between them?",
             "options": [
                 "The strongest field on the whole map, because it is close "
                 "to both charges",
                 "Zero — the two pushes are equal and exactly opposite, so "
                 "they cancel",
                 "Twice the field of one charge on its own at that distance",
                 "Half the field of one charge on its own, because the two "
                 "are shared",
             ],
             "answer": 1,
         },
         "pos": {"label": "Where the test point sits", "min": 0, "max": 24,
                 "step": 1, "start": 12, "value": "step 12 of 24"},
         "setups": [
             {"id": "one-pos", "label": "One positive charge",
              "charges": [{"x": 490, "q": 1}]},
             {"id": "one-neg", "label": "One negative charge",
              "charges": [{"x": 490, "q": -1}]},
             {"id": "dipole", "label": "A positive and a negative",
              "charges": [{"x": 350, "q": 1}, {"x": 650, "q": -1}]},
             {"id": "two-pos", "label": "Two positives",
              "charges": [{"x": 350, "q": 1}, {"x": 650, "q": 1}]},
         ],
         "strength_bands": [
             {"at_least": 90, "word": "very strong"},
             {"at_least": 35, "word": "strong"},
             {"at_least": 10, "word": "moderate"},
             {"at_least": 2, "word": "weak"},
             {"at_least": 0, "word": "very weak"},
         ],
         "readouts": [
             {"id": "dir", "label": "The field at your point", "sub": "—"},
             {"id": "strength", "label": "How strong it is there",
              "sub": "—"},
             {"id": "posf", "label": "A small positive charge here"},
             {"id": "negf", "label": "A small negative charge here"},
         ],
         # ⚠️ `{strength}` is the verdict WORD, `{rel}` the relative figure
         # rounded to a whole number, `{dir}` the direction word. `sub` is
         # the caption under the direction tile.
         "branches": {
             "on_charge": {
                 "sub": "inside the charge itself",
                 "note": "Your test point has landed on top of a charge. The "
                         "model treats charges as points, so it gives no "
                         "sensible value there — which is why the grid "
                         "arrows are left out close in as well. Slide the "
                         "test point away and the field reappears, stronger "
                         "the nearer you are."},
             "single_positive": {
                 "sub": "away from the positive charge",
                 "note": "Every arrow on the map points away from the single "
                         "positive charge, because that is the way a small "
                         "positive charge would be shoved. At your point the "
                         "field is {strength} — {rel} on this scale — and it "
                         "is stronger the closer you go. A small positive "
                         "charge released here would move {dir}; a small "
                         "negative one would go the other way, back towards "
                         "the charge."},
             "single_negative": {
                 "sub": "towards the negative charge",
                 "note": "Every arrow points inwards, towards the single "
                         "negative charge — same map as the positive charge, "
                         "arrows reversed. At your point the field is "
                         "{strength}, {rel} on this scale. A small positive "
                         "charge would be pulled in {dir}; a small negative "
                         "one would be driven away. Nothing about the map "
                         "depends on anything being in it: the arrows were "
                         "there before you put the test point down."},
             "dipole": {
                 "sub": "from the positive charge towards the negative one",
                 "note": "With a positive charge on the left and a negative "
                         "one on the right, every arrow in the middle runs "
                         "from the positive towards the negative, and the "
                         "field is strongest in the gap between them where "
                         "the two contributions point the same way and add. "
                         "At your point it is {strength}, {rel} on this "
                         "scale, and it points {dir}. Slide out beyond "
                         "either charge and the arrows thin out fast — there "
                         "is no distance at which they stop, only distances "
                         "where they are too small to matter."},
             "two_positive": {
                 "sub": "away from the nearer charge",
                 "note": "Two equal positive charges, so the arrows sweep "
                         "outwards from both and avoid the middle. At your "
                         "point the field is {strength}, {rel} on this "
                         "scale, pointing {dir} — away from whichever charge "
                         "you are nearer. Slide to the exact mid-point and "
                         "the two pushes cancel completely."},
             "null_point": {
                 "sub": "the two pushes are equal and opposite",
                 "note": "You are exactly half-way between two equal "
                         "positive charges, and here the field is zero. Both "
                         "charges push a small positive test charge with the "
                         "same strength, in exactly opposite directions, so "
                         "the two arrows add to nothing and there is no "
                         "arrow to draw. Move one step either way and the "
                         "nearer charge wins immediately. A point like this "
                         "is not a place where the field is weak — it is a "
                         "place where it cancels."},
         },
         "words": {
             "no_value": "no value here",
             "on_charge_dir": "no value — you are on top of a charge",
             "zero_dir": "the field cancels to nothing",
             "right": "to the right",
             "left": "to the left",
             "no_force": "feels no force",
             "pushed": "pushed {dir}",
             "scale": "{rel} on this scale",
             "zero_scale": "zero",
             "zero_word": "nothing at all",
             "close_word": "too close to say",
         }},

        # ── #s-reach · three forces that reach across a gap ────────────
        {"type": "charge-band",
         "id": "reach",
         "anchor": "s-reach",
         "eyebrow": "The figure",
         "heading": "Three forces that reach across a gap",
         "lead": "The electric field is not a special case. Every force you "
                 "meet at this stage that acts without contact is described "
                 "the same way: the first object fills the space with a "
                 "field, and the second one responds to the field where it "
                 "is.",
         "triple": {
             "cards": [
                 {"title": "Gravitational field", "kind": "gravity",
                  "aria_label": "Two circles separated by a dashed gap, with "
                                "an arrow from each pointing towards the "
                                "other.",
                  "body": "Anything with <strong>mass</strong> makes one. "
                          "Always a pull, never a push, which is why there "
                          "is no opposite of mass."},
                 {"title": "Magnetic field", "kind": "magnet",
                  "aria_label": "Two bars separated by a dashed gap, with an "
                                "arrow from each pointing towards the "
                                "other.",
                  "body": "A <strong>magnet</strong> or a current makes one. "
                          "Pull or push, depending on which poles face each "
                          "other."},
                 {"title": "Electric field", "kind": "charge",
                  "aria_label": "Two circles separated by a dashed gap, one "
                                "marked with a plus and one with a minus, "
                                "with an arrow from each pointing towards "
                                "the other.",
                  "body": "A <strong>charge</strong> makes one. Pull or "
                          "push, depending on the two signs — and it is "
                          "enormously stronger than gravity."},
             ],
         },
         "close": "In all three the arrows come in pairs of equal size and "
                  "opposite direction, and in all three the gap can be a "
                  "perfect vacuum. What crosses it is not a substance. It is "
                  "a field."},

        {"type": "key-fact", "ref": "a-field-fills-the-space"},

        {"type": "misconception", "id": "think-the-field-is-there-first",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-field-is-there-first",
         "kind": "predict",
         "demand": "explain",
         "targets": "CHRG-09",
         "statements": [
             {"quote": "The field only exists when there is something in it "
                       "to feel it.",
              "targets": "CHRG-09",
              "body": [
                  "The field is there first. That is the whole point of "
                  "inventing it: instead of saying two objects mysteriously "
                  "know about each other across a gap, we say the first one "
                  "changes the space, and the second one only ever responds "
                  "to the space it is standing in. Take the second object "
                  "away and the field is unchanged — put anything charged "
                  "back at that point, at any moment, and it is pushed the "
                  "same way. Bring in something twice as charged and the "
                  "force doubles while the field stays exactly as it was.",
              ]},
             {"quote": "The air in between must be carrying it.",
              "targets": "CHRG-10",
              "body": [
                  "Pump the air out and nothing changes. Two charged objects "
                  "in an evacuated jar attract and repel exactly as they "
                  "did, and the same is true of the Sun's gravitational pull "
                  "on the Earth across 150 million kilometres of almost "
                  "nothing. Air is not the messenger; it is not even in the "
                  "way. What is between them is the field, and a field does "
                  "not need a material to sit in — the same discovery that "
                  "made light so strange, for exactly the same reason.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "a-field-fills-the-space",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A charged object fills the space around it with an "
                 "electric field: a size and a direction at every point. The "
                 "arrow shows which way a small positive charge would be "
                 "pushed there, so arrows point away from positive and "
                 "towards negative. The field is there whether or not "
                 "anything is in it, and it needs nothing in the gap."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 1.
    # Design put both at 0; her option TEXT and every correction are verbatim
    # and only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "A field map shows arrows pointing outwards in every "
                 "direction, away from a single object at the centre. What "
                 "can you say about the object and about a small negative "
                 "charge released nearby?",
            "options": [
                "The object is negatively charged, and a negative charge "
                "would be pushed outwards along the arrows.",
                "The object is positively charged, and a negative charge "
                "would be pushed outwards along the arrows.",
                "The object is positively charged, and a negative charge "
                "would be pulled inwards, against the arrows.",
                "You cannot tell the sign from the map, only the strength.",
            ],
            "answer": 2,
            "feedback": {
                0: "Arrows point away from positive charges, because they "
                   "show the push on a small positive charge. And a negative "
                   "charge always goes against the arrows.",
                1: "The first half is right. But the arrows show the force "
                   "on a positive charge; a negative one feels a force in "
                   "the opposite direction, so it moves inwards.",
                3: "The direction of the arrows is exactly what tells you "
                   "the sign: outwards means positive, inwards means "
                   "negative.",
            },
            "title": "Rung 1 · Read the map"},
        "apply": {
            "q": "A student says the field between two equal positive "
                 "charges must be at its strongest half-way between them, "
                 "because that point is close to both. What is right?",
            "options": [
                "The student is right — being close to two charges instead "
                "of one makes it the strongest point on the map.",
                "It is zero there. The two charges push a positive test "
                "charge in exactly opposite directions with equal strength, "
                "so the pushes cancel.",
                "It is zero there, because the two charges cancel each other "
                "out everywhere between them.",
                "It is half the strength of a single charge at the same "
                "distance, because the two contributions are averaged.",
            ],
            "answer": 1,
            "feedback": {
                0: "Closeness matters, but direction matters too. The two "
                   "pushes are equal and exactly opposite at the mid-point, "
                   "so they cancel to nothing.",
                2: "The verdict is right and the reason is too broad. It "
                   "cancels only at that one point; move a millimetre either "
                   "way and the nearer charge wins.",
                3: "Fields are not averaged, they are added as arrows — and "
                   "two equal arrows pointing opposite ways add to nothing, "
                   "not to half.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A charged comb bends a thin stream of water from a couple "
                 "of centimetres away, with nothing touching. Explain what "
                 "is happening, using the word field, and say what would "
                 "change if the whole thing were done in a vacuum.",
            "field_label": "Your explanation",
            "placeholder": "The comb is charged, so it fills the space "
                           "around it with…",
            "success": [
                "Says the comb is charged and fills the space around it with "
                "an electric field.",
                "Says the field has a direction and a strength at every "
                "point, and is stronger closer to the comb.",
                "Says the water is neutral overall but its charges are "
                "pushed to one side, so the near side becomes oppositely "
                "charged.",
                "Says the force on the water comes from the field where the "
                "water is, not from anything crossing the gap.",
                "Says nothing would change in a vacuum, because the field "
                "does not need air or any material to exist in.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "People are told they are safe from lightning inside a car, "
                 "and that it is nothing to do with the rubber tyres. "
                 "Explain why, using the idea of a field and what you know "
                 "about conductors.",
            "field_label": "Your answer",
            "placeholder": "The body of a car is metal, which is a "
                           "conductor, so…",
            "success": [
                "Says the body of the car is metal, which is a conductor "
                "with free electrons.",
                "Says the free charges rearrange themselves on the outside "
                "surface of the shell.",
                "Says the result is that the field inside the shell is very "
                "nearly zero.",
                "Says that with almost no field inside there is almost no "
                "force on the charges in a person inside.",
                "Says the tyres are irrelevant — the protection is the metal "
                "shell surrounding you, not an insulating layer underneath.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    # ⊖ COMMANDER'S PHASE 3 REVERT, 25 Aug 2026 — HER key note, verbatim
    # (her page, `#s-keynote`). What had been here was a paraphrase of this
    # lane's own; good physics, not hers, and no row claimed it.
    "key_note": "An electric field is what a charged object does to the "
                "space around it: at every point there is a size and a "
                "direction. Anything charged placed at a point feels a force "
                "from the field there, so nothing has to cross the gap and no "
                "air or contact is needed. Field arrows are drawn the way a "
                "small positive charge would be pushed, so they point away "
                "from positive charges and towards negative ones; a negative "
                "charge at the same point is pushed the opposite way. The "
                "field is strongest close to a charge and weakens quickly "
                "with distance, and between two like charges there is a point "
                "where it cancels to nothing. Gravity and magnetism are "
                "described in exactly the same way.",

    "stretch": [
        {"id": "faraday-and-maxwell",
         "type": "explainer",
         "text": "Michael Faraday invented the idea, and he was not taken "
                 "seriously at first. He had almost no mathematics and "
                 "described the space around a magnet as filled with lines "
                 "of force — a picture, not an equation. It took James Clerk "
                 "Maxwell to write that picture down properly, and when he "
                 "did, the equations predicted something nobody had asked "
                 "for: that a field which changes can travel through empty "
                 "space at a fixed speed. That speed turned out to be the "
                 "speed of light, and light turned out to be exactly that. "
                 "Faraday's picture of empty space having a state is now the "
                 "foundation of every field theory in physics."},
        {"id": "safe-inside-a-shell",
         "type": "explainer",
         "text": "Fields also explain why you are safe inside a car in a "
                 "thunderstorm, and it is not the tyres. A metal shell is a "
                 "conductor, so its free electrons rearrange themselves "
                 "until the field <em>inside</em> the shell is very nearly "
                 "zero, whatever is happening outside — the outside surface "
                 "takes the whole strike and the inside stays quiet. The "
                 "same trick shields the cable to a television aerial, "
                 "protects the electronics inside an aircraft struck by "
                 "lightning, and is why a mobile phone loses signal in a "
                 "lift."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "electric field",
         "definition": "The state a charged object puts the space around it "
                       "into. It has a size and a direction at every point, "
                       "and it is there whether or not anything is in it."},
        {"term": "field arrow",
         "definition": "A mark showing which way a small positive charge "
                       "would be pushed at that point, and how hard. A "
                       "negative charge feels a force the other way."},
        {"term": "null point",
         "definition": "A place where two contributions to a field cancel "
                       "exactly. Not a weak field — no field at all, at that "
                       "one point."},
    ],

    "tutor": {
        "anchor": "s-field",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a charge arrangement and want to know which way the "
                "field points?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Field lines for point charges and parallel plates, field "
                   "strength as force per unit charge, and the link between "
                   "field and potential difference.",

    "convention_note": "The bench is a teaching model. Charges are treated "
                       "as points of equal size, and the field is calculated "
                       "with the standard inverse-square rule and reported "
                       "as a relative figure with 100 set at the strongest "
                       "point the grid samples — no field strength in "
                       "newtons per coulomb is given, because the unit is "
                       "beyond this stage. Grid arrows have a shortest and a "
                       "longest length, so very weak and very strong regions "
                       "are drawn clipped rather than to scale, and points "
                       "closer than a small distance to a charge are left "
                       "blank because the model gives no sensible value "
                       "there. The test point moves along the centre line "
                       "only, where the field happens to be horizontal; away "
                       "from that line it is not. Real charged objects are "
                       "not points, and a real charged sphere's field "
                       "differs from this near its surface.",

    "ws": ["measurement"],
}
