"""P9 lesson 03 — Electric fields: twelve questions (MRB-223).

Written against Design's page. The comb and the water, the field map and
the three-field figure are hers.

The discriminations, in the order the lesson builds them:

  · the field is a property of the SPACE, and it is there first
    (`CHRG-09`);
  · nothing crosses the gap — no air, no thread of charge (`CHRG-10`);
  · an arrow is the push on a small POSITIVE charge, so a negative one
    goes the other way (`CHRG-12`);
  · two equal charges can cancel, and a null point is not a weak field
    (`CHRG-11`) — the harder band sits here.

⚠️ NO FIELD STRENGTH IN NEWTONS PER COULOMB ANYWHERE. The unit is beyond
this stage; every comparison here is relative or in words, as on the page.

⚠️ POSITION IS AUTHORED — 3,0,2,1 · 1,3,0,2 · 0,2,1,3, three of each.

⚠️ Neither marked rung is restated: the all-outwards map read for its sign
and the strongest-half-way-between claim are the ladder's, and nothing
here reuses either.
"""

UNIT = "P9"
LESSON = "electric-fields"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p9-03-e01",
        "band": "easier",
        "text": "A field arrow at a point shows…",
        "options": [
            {"text": "which way the charge that made the field would move",
             "correct": False,
             "why": "The arrow is about that POINT, not about the object "
                    "that made the field."},
            {"text": "how far the field reaches before it stops",
             "correct": False,
             "why": "A field has no edge. Its arrows get shorter and never "
                    "reach zero."},
            {"text": "how much charge is sitting at that point",
             "correct": False,
             "why": "There need be no charge there at all. The field is "
                    "there whether or not anything is in it."},
            {"text": "which way a small positive charge there would be "
                     "pushed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e02",
        "band": "easier",
        "text": "Around a single negative charge, which way do the field "
                "arrows point?",
        "options": [
            {"text": "Inwards, towards the charge", "correct": True},
            {"text": "Outwards, away from the charge", "correct": False,
             "why": "That is the map for a positive charge. Reverse every "
                    "arrow and you have the negative one."},
            {"text": "In circles around the charge", "correct": False,
             "why": "Circles are the picture for the field round a "
                    "current-carrying wire, which is a different topic."},
            {"text": "There are no arrows, because a negative charge takes "
                     "a field rather than making one", "correct": False,
             "why": "Every charge makes a field, whichever sign it is."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e03",
        "band": "easier",
        "text": "Two charged objects act on each other across a gap. What "
                "is in the gap?",
        "options": [
            {"text": "Air, which passes the force along", "correct": False,
             "why": "Pump the air out and the force is exactly the same. It "
                    "was never the messenger."},
            {"text": "A thin stream of charge travelling between them",
             "correct": False,
             "why": "Nothing travels across. Neither object loses any "
                    "charge while the force acts."},
            {"text": "A field, which needs no material to exist in",
             "correct": True},
            {"text": "Nothing at all, and physics has no explanation for "
                     "how the two objects know about each other",
             "correct": False,
             "why": "There is an explanation, and the field is it — that is "
                    "exactly why the idea was invented."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e04",
        "band": "easier",
        "text": "A charged sphere sits alone in an empty room. Is there a "
                "field around it?",
        "options": [
            {"text": "No — a field needs two objects to exist between",
             "correct": False,
             "why": "One charge makes a field. The second object is what "
                    "RESPONDS to it, and it is not needed for the field to "
                    "be there."},
            {"text": "Yes, and it is there whether or not anything is in "
                     "it", "correct": True},
            {"text": "No — a field only appears when something charged "
                     "arrives to feel it", "correct": False,
             "why": "The field is there first. That is the whole point of "
                    "inventing it."},
            {"text": "Only if the room contains air, because a field cannot "
                     "exist in a vacuum", "correct": False,
             "why": "A field needs no material at all. It is unchanged in a "
                    "vacuum."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p9-03-s01",
        "band": "standard",
        "text": "At a point on a field map the arrow points to the right. A "
                "small NEGATIVE charge is placed there. Which way is it "
                "pushed?",
        "options": [
            {"text": "To the right, along the arrow", "correct": False,
             "why": "That is what a positive charge would do. A negative "
                    "one always goes against the arrow."},
            {"text": "To the left, against the arrow", "correct": True},
            {"text": "It feels no force, because the map is drawn for "
                     "positive charges only", "correct": False,
             "why": "The map works for both. It is drawn for a positive "
                    "charge, and a negative one simply reverses it."},
            {"text": "It depends how big the negative charge is, because "
                     "the direction is set by the larger of the two",
             "correct": False,
             "why": "The size changes how HARD it is pushed, never which "
                    "way. Direction comes from the sign."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s02",
        "band": "standard",
        "text": "A test charge is doubled and put back at the same point. "
                "What happens to the force on it, and to the field there?",
        "options": [
            {"text": "Both double", "correct": False,
             "why": "The force doubles. The field does not — it is a "
                    "property of the space, and the test charge is not part "
                    "of it."},
            {"text": "Neither changes", "correct": False,
             "why": "The field is unchanged, but twice the charge feels "
                    "twice the push."},
            {"text": "The field doubles and the force stays the same",
             "correct": False,
             "why": "That is the pair the wrong way round. The field is set "
                    "by the object that MADE it."},
            {"text": "The force doubles and the field is unchanged",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s03",
        "band": "standard",
        "text": "On a map of one positive and one negative charge, where "
                "are the arrows longest?",
        "options": [
            {"text": "In the gap between the two charges", "correct": True},
            {"text": "Far out beyond both of them, where the two fields "
                     "have room to spread", "correct": False,
             "why": "Both contributions are weakest far away, so the arrows "
                    "are shortest there."},
            {"text": "Exactly half-way between them, and nowhere else",
             "correct": False,
             "why": "The mid-point is inside the strong region, but the "
                    "arrows are longer still nearer either charge."},
            {"text": "Directly above and below the mid-point, where the two "
                     "contributions meet at a right angle", "correct": False,
             "why": "There the two contributions partly cancel. In the gap "
                    "they point the same way and add."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s04",
        "band": "standard",
        "text": "Why does a field map leave a blank ring around each "
                "charge instead of drawing enormous arrows there?",
        "options": [
            {"text": "Because the field really is zero inside that ring",
             "correct": False,
             "why": "It is the opposite — that is where the field is "
                    "strongest. The blank says the MODEL has run out, not "
                    "the field."},
            {"text": "Because arrows that long would not fit on the "
                     "drawing", "correct": False,
             "why": "They could be clipped, as the long ones elsewhere are. "
                    "The real reason is that the model gives no value at "
                    "all in there."},
            {"text": "Because the model treats a charge as a point, and "
                     "gives no sensible value that close", "correct": True},
            {"text": "Because a real charged object is a conductor, so the "
                     "field inside it is zero and drawing arrows would be "
                     "wrong", "correct": False,
             "why": "True of the inside of a conducting shell, and not what "
                    "the blank ring is about — the charges here are points, "
                    "with no inside."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p9-03-h01",
        "band": "harder",
        "text": "At a null point between two like charges, a test charge "
                "is released. What happens, and why?",
        "options": [
            {"text": "It stays put, because the two pushes are equal and "
                     "exactly opposite", "correct": True},
            {"text": "It stays put, because the field is too weak there to "
                     "move anything", "correct": False,
             "why": "The verdict is right and the reason is wrong. The "
                    "field is not weak there; it is nothing, because two "
                    "equal arrows in opposite directions add to zero."},
            {"text": "It moves towards whichever charge is nearer, because "
                     "closeness always wins", "correct": False,
             "why": "At the null point neither is nearer — that is what "
                    "makes it the null point."},
            {"text": "It moves off along the line between them, because two "
                     "equal charges always give a push somewhere",
             "correct": False,
             "why": "Not at that one point. Move a millimetre either way "
                    "and the nearer charge does win."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h02",
        "band": "harder",
        "text": "Why is a mobile phone signal lost inside a metal lift?",
        "options": [
            {"text": "The metal absorbs the signal and turns it into heat "
                     "inside the walls", "correct": False,
             "why": "Very little is absorbed. The free charges in the metal "
                    "rearrange so that almost no field gets inside."},
            {"text": "The lift is moving, so the signal cannot lock on to "
                     "it", "correct": False,
             "why": "It happens with the lift standing still, and it stops "
                    "the moment the doors open."},
            {"text": "Charges in the metal shell rearrange so that the "
                     "field inside is almost zero", "correct": True},
            {"text": "The lift is earthed through the building, so any "
                     "signal reaching it runs straight to the ground",
             "correct": False,
             "why": "Earthing is not what does it. An unearthed metal box "
                    "shields its inside just as well."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h03",
        "band": "harder",
        "text": "What do a gravitational field, a magnetic field and an "
                "electric field have in common?",
        "options": [
            {"text": "All three can only pull, never push", "correct": False,
             "why": "Only gravity is always a pull. The other two do both, "
                    "which is why there is no opposite of mass."},
            {"text": "All three describe one object changing the space and "
                     "another responding to it", "correct": True},
            {"text": "All three need a material in the gap to act through",
             "correct": False,
             "why": "None of them does. All three work in a perfect "
                    "vacuum — that is the point the figure makes."},
            {"text": "All three are made by the same property of an object, "
                     "which is why they are always found together",
             "correct": False,
             "why": "Mass, magnetism and charge are three different "
                    "properties. A charged object need not be magnetic, and "
                    "everything has mass."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h04",
        "band": "harder",
        "text": "A charged comb bends a stream of water. Which statement "
                "about the water is right?",
        "options": [
            {"text": "The water gains the opposite charge from the comb, "
                     "which is why it is pulled across", "correct": False,
             "why": "Nothing crosses the gap. The water's own charges shift "
                    "within it and its total stays zero."},
            {"text": "The water must already have been charged by running "
                     "through the tap", "correct": False,
             "why": "Water straight from a tap is neutral, and the trick "
                    "works just as well however the stream was started."},
            {"text": "The water is being pushed by air that the comb has "
                     "charged", "correct": False,
             "why": "The effect is unchanged in a vacuum. Air plays no part "
                    "in it."},
            {"text": "The water stays neutral, and its own charges are "
                     "pushed to one side by the comb's field",
             "correct": True},
        ],
        "figure": None,
    },
]
