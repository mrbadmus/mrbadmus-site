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
        "text": "A small NEGATIVE charge is placed at point P on the "
                "electric field map. Which way is it pushed?",
        "options": [
            {"text": "To the right, along the arrow", "correct": False,
             "why": "That is what a positive charge would do. A negative "
                    "one always goes against the arrow."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "To the left, against the arrow, as it is negative",
             "correct": True},
            {"text": "It feels no force, because the map is drawn for "
                     "positive charges only", "correct": False,
             "why": "The map works for both. It is drawn for a positive "
                    "charge, and a negative one simply reverses it."},
            {"text": "It depends how big the negative charge is, because "
                     "a bigger charge could overcome the field",
             "correct": False,
             "why": "The size changes how HARD it is pushed, never which "
                    "way. Direction comes from the sign."},
        ],
        "figure": "p9-field-point-marked",
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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "In the gap between the two charges, where both "
                     "fields add", "correct": True},
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
            # ⊕ MRB-297 · 1 Sep 2026 — the third option was widened so the
            # correct answer stops being resolvable as the second-longest.
            {"text": "The metal absorbs the whole signal and turns it into "
                     "heat inside the walls", "correct": False,
             "why": "Very little is absorbed, and the walls do not warm up. "
                    "The free charges in the metal rearrange so that almost "
                    "no field gets inside."},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p9-03-e05",
        "band": "easier",
        "text": "Around a single POSITIVE charge, which way do the field "
                "arrows point?",
        "options": [
            {"text": "Outwards, away from the charge", "correct": True},
            {"text": "Inwards, towards the charge", "correct": False,
             "why": "Arrows point inwards around a NEGATIVE charge, which "
                    "would attract a small positive test charge."},
            {"text": "In circles around the charge", "correct": False,
             "why": "Circular field patterns belong to a current-carrying "
                    "wire, not to a lone charge."},
            {"text": "In whichever direction the nearest object lies",
             "correct": False,
             "why": "The field is there whether or not anything else is "
                    "nearby."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e06",
        "band": "easier",
        "text": "An electric field is strongest…",
        "options": [
            {"text": "far from the charge", "correct": False,
             "why": "It weakens quickly with distance, so far away is where "
                    "it is weakest."},
            {"text": "close to the charge", "correct": True},
            {"text": "at the same strength everywhere", "correct": False,
             "why": "If it were even, a scrap of paper would be pulled just "
                    "as hard from across the room."},
            {"text": "only where something is placed in it", "correct": False,
             "why": "The field is there whether or not anything is in it to "
                    "feel it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e07",
        "band": "easier",
        "text": "A field arrow shows the direction a small ___ charge would "
                "be pushed.",
        "options": [
            {"text": "negative", "correct": False,
             "why": "A negative charge is pushed the opposite way to the "
                    "arrows, which is the point of the convention."},
            {"text": "positive", "correct": True},
            {"text": "neutral", "correct": False,
             "why": "A neutral object feels no push from the field in the way "
                    "a charge does."},
            {"text": "heavy", "correct": False,
             "why": "Mass has nothing to do with an electric field; charge "
                    "does."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e08",
        "band": "easier",
        "text": "What is a null point?",
        "options": [
            {"text": "A place where the field is very weak but still there",
             "correct": False,
             "why": "It is not merely weak: the two contributions cancel to "
                    "nothing at all."},
            {"text": "A place where two contributions to a field cancel "
                     "exactly",
             "correct": True},
            {"text": "The point where a charge is placed", "correct": False,
             "why": "That is where the field is strongest, not where it "
                    "vanishes."},
            {"text": "The edge of a field, beyond which nothing acts",
             "correct": False,
             "why": "A field has no edge; it simply fades with distance."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e09",
        "band": "easier",
        "text": "Does a field exist at a point where nothing has been placed?",
        "options": [
            {"text": "No — a field only appears when something is there to "
                     "feel it",
             "correct": False,
             "why": "Put a charge there afterwards and it is pushed at once, "
                    "which shows the field was already waiting."},
            {"text": "Yes, whether or not anything is in it", "correct": True},
            {"text": "No, unless the point is very close to the charge",
             "correct": False,
             "why": "Distance changes the strength, never whether the field "
                    "is present."},
            {"text": "Only if the air has been removed", "correct": False,
             "why": "Air is not what carries a field; removing it changes "
                    "nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e10",
        "band": "easier",
        "text": "Which of these is also described using a field?",
        "options": [
            {"text": "Friction", "correct": False,
             "why": "Friction is a contact force between two surfaces, not a "
                    "force acting across a gap."},
            {"text": "Air resistance", "correct": False,
             "why": "That is a contact force from the air pushing on a moving "
                    "object."},
            {"text": "Gravity", "correct": True},
            {"text": "Upthrust", "correct": False,
             "why": "Upthrust comes from a liquid or gas pressing on a "
                    "surface, so it needs contact."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e11",
        "band": "easier",
        "text": "Longer field arrows on a map mean the field is…",
        "options": [
            {"text": "weaker there", "correct": False,
             "why": "Length shows strength, so a long arrow is a strong "
                    "field."},
            {"text": "stronger there", "correct": True},
            {"text": "pointing the opposite way", "correct": False,
             "why": "Direction is shown by which way the arrow points, not by "
                    "its length."},
            {"text": "acting on a larger charge", "correct": False,
             "why": "The map describes the space itself, whatever is later "
                    "placed in it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e12",
        "band": "easier",
        "text": "Two charged objects act on each other across a gap with the "
                "air pumped out. What is in the gap?",
        "options": [
            {"text": "Air, which carries the force", "correct": False,
             "why": "The air has been removed, and the force still acts."},
            {"text": "Nothing at all, and no force acts", "correct": False,
             "why": "The force certainly acts, which is why something must "
                    "describe the space."},
            {"text": "An electric field, filling the gap", "correct": True},
            {"text": "A stream of electrons crossing between them",
             "correct": False,
             "why": "No charge crosses the gap; both objects keep the charge "
                    "they have."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e13",
        "band": "easier",
        "text": "A small negative charge is placed where a field arrow points "
                "to the right. Which way is it pushed?",
        "options": [
            {"text": "To the right, following the arrow", "correct": False,
             "why": "The arrow shows where a POSITIVE charge would go; a "
                    "negative one goes the other way."},
            {"text": "To the left", "correct": True},
            {"text": "Straight downwards", "correct": False,
             "why": "That is what gravity does; the electric field pushes "
                    "along its own direction."},
            {"text": "Nowhere — negative charges are not affected",
             "correct": False,
             "why": "They are affected just as strongly, only in the opposite "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e14",
        "band": "easier",
        "text": "Field arrows point towards an object at the centre of a map. "
                "What is its charge?",
        "options": [
            {"text": "Positive", "correct": False,
             "why": "Arrows point AWAY from a positive charge, since a "
                    "positive test charge would be repelled."},
            {"text": "Negative", "correct": True},
            {"text": "Neutral", "correct": False,
             "why": "A neutral object makes no field of its own, so there "
                    "would be no arrows to draw."},
            {"text": "Either, depending on how strong it is", "correct": False,
             "why": "Strength affects the length of the arrows, never which "
                    "way they point."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e15",
        "band": "easier",
        "text": "Does anything have to cross the gap for one charge to push "
                "another?",
        "options": [
            {"text": "Yes — electrons must jump across", "correct": False,
             "why": "If electrons crossed, both charges would change, and "
                    "they do not."},
            {"text": "Yes — the air must be pushed from one to the other",
             "correct": False,
             "why": "The force works in a vacuum, with no air to push."},
            {"text": "No — the field is already there at every point",
             "correct": True},
            {"text": "No, because the two objects are really touching",
             "correct": False,
             "why": "They can be centimetres apart and the force still acts."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e16",
        "band": "easier",
        "text": "A field map is drawn for one charge. What happens to it if a "
                "second charge is brought up?",
        "options": [
            {"text": "Nothing — each charge keeps its own map unchanged",
             "correct": False,
             "why": "The two contributions add at every point, so the pattern "
                    "changes."},
            {"text": "The map changes, because the two fields add at every "
                     "point",
             "correct": True},
            {"text": "The first map disappears and only the new one is left",
             "correct": False,
             "why": "Neither field vanishes; both contribute everywhere."},
            {"text": "The map only changes where the second charge is",
             "correct": False,
             "why": "Its field reaches everywhere, so the whole pattern is "
                    "affected."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e17",
        "band": "easier",
        "text": "Which quantity does a field arrow NOT show?",
        "options": [
            {"text": "The direction of the field at that point",
             "correct": False,
             "why": "That is exactly what the arrow's direction shows."},
            {"text": "How strong the field is at that point", "correct": False,
             "why": "That is shown by the arrow's length."},
            {"text": "The size of the charge that will be put there later",
             "correct": True},
            {"text": "Which way a small positive charge would be pushed",
             "correct": False,
             "why": "That is the definition of the arrow's direction."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e18",
        "band": "easier",
        "text": "Around a lone charge, the field arrows get shorter as you "
                "move away. What does that show?",
        "options": [
            {"text": "That the field runs out at a fixed distance",
             "correct": False,
             "why": "It never runs out; it fades gradually and has no edge."},
            {"text": "That the field is weaker further away", "correct": True},
            {"text": "That the field changes direction further away",
             "correct": False,
             "why": "Direction is shown by where the arrows point, and that "
                    "does not reverse."},
            {"text": "That the charge is getting smaller", "correct": False,
             "why": "The charge is unchanged; it is the field at each point "
                    "that differs."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p9-03-s05",
        "band": "standard",
        "text": "A test charge is placed at a point and then replaced by one "
                "three times as large. What happens?",
        "options": [
            {"text": "The force triples and the field triples", "correct": False,
             "why": "The field belongs to the space and does not depend on "
                    "what is put in it."},
            {"text": "The force triples and the field is unchanged",
             "correct": True},
            {"text": "The force is unchanged and the field triples",
             "correct": False,
             "why": "A larger charge in the same field certainly feels a "
                    "larger force."},
            {"text": "Neither changes", "correct": False,
             "why": "Three times the charge feels three times the push at the "
                    "same point."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s06",
        "band": "standard",
        "text": "One positive and one negative charge sit near each other. "
                "Which way do the arrows run in the space between them?",
        "options": [
            {"text": "From the negative towards the positive",
             "correct": False,
             "why": "A small positive test charge is pushed away from the "
                    "positive and pulled towards the negative."},
            {"text": "Outwards from both, away from the pair",
             "correct": False,
             "why": "Only the positive charge pushes a test charge away; the "
                    "negative one pulls it in."},
            {"text": "Inwards towards both, from outside the pair",
             "correct": False,
             "why": "Only the negative charge pulls a test charge in; the "
                    "positive one pushes it away."},
            {"text": "From the positive towards the negative", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s07",
        "band": "standard",
        "text": "Why does a charged comb bend a thin stream of water without "
                "touching it?",
        "options": [
            {"text": "Because the water is charged and is attracted to the "
                     "comb",
             "correct": False,
             "why": "Tap water from a tap is neutral; the comb's field is "
                    "what shifts its charges."},
            {"text": "Because the comb's field shifts the water's own "
                     "charges, and it is pulled in",
             "correct": True},
            {"text": "Because the comb heats the air, which pushes the stream "
                     "over",
             "correct": False,
             "why": "Nothing measurable is warmed, and the bend follows the "
                    "comb wherever it is held."},
            {"text": "Because the comb blows air at the stream",
             "correct": False,
             "why": "Holding it still does it just as well, with no air "
                    "moving at all."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s08",
        "band": "standard",
        "text": "A field map leaves a blank ring close around each charge "
                "rather than drawing arrows there. Why?",
        "options": [
            {"text": "Because there is no field that close in",
             "correct": False,
             "why": "That is where the field is strongest of all; it is the "
                    "drawing that gives out."},
            {"text": "Because the arrows would be far too long to fit on the "
                     "page",
             "correct": True},
            {"text": "Because the field points in every direction at once "
                     "there",
             "correct": False,
             "why": "It has one clear direction at every point, close in as "
                    "much as far out."},
            {"text": "Because the charge occupies that space itself",
             "correct": False,
             "why": "The blank ring is far wider than the charged object "
                    "drawn at its centre."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s09",
        "band": "standard",
        "text": "Two equal positive charges sit a short way apart. What is "
                "the field exactly halfway between them?",
        "options": [
            {"text": "At its strongest, because that point is close to both",
             "correct": False,
             "why": "The two contributions point in opposite directions "
                    "there, so they cancel rather than add."},
            {"text": "Zero, because the two contributions cancel",
             "correct": True},
            {"text": "Twice the field of one charge on its own",
             "correct": False,
             "why": "That is what would happen if they pointed the same way, "
                    "and they do not."},
            {"text": "Pointing towards the nearer charge", "correct": False,
             "why": "The point is the same distance from each, so neither is "
                    "nearer."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s10",
        "band": "standard",
        "text": "One field arrow is twice as long as another. What does "
                "that say about the force on the same test charge there?",
        "options": [
            {"text": "It is twice as large where the arrow is longer",
             "correct": True},
            {"text": "It is half as large where the arrow is longer",
             "correct": False,
             "why": "A longer arrow means a stronger field, so the force "
                    "there is bigger, not smaller."},
            {"text": "It is the same, because the test charge has not "
                     "changed",
             "correct": False,
             "why": "The charge is the same, but the field it sits in is "
                    "twice as strong."},
            {"text": "It points in the opposite direction there",
             "correct": False,
             "why": "Direction is shown by where an arrow points, not by how "
                    "long it is."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s11",
        "band": "standard",
        "text": "A student says the field is only real once a charge is put "
                "into it. What is the best reply?",
        "options": [
            {"text": "They are right — a field with nothing in it does "
                     "nothing",
             "correct": False,
             "why": "Place a charge there at any moment and it is pushed "
                    "immediately, with no delay to set anything up."},
            {"text": "The field is already there; the test charge only "
                     "reveals it",
             "correct": True},
            {"text": "The field is made by the test charge itself",
             "correct": False,
             "why": "The test charge has its own field, but it is the source "
                    "charge's field that pushes it."},
            {"text": "Fields are only real for magnets, not for charges",
             "correct": False,
             "why": "All three of gravity, magnetism and charge are described "
                    "in exactly the same way."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s12",
        "band": "standard",
        "text": "Where should the arrows be longest on a map of a single "
                "charge?",
        "options": [
            {"text": "At the edge of the map", "correct": False,
             "why": "That is furthest from the charge, so the field is "
                    "weakest there."},
            {"text": "Nearest the charge, where it is strongest", "correct": True},
            {"text": "Evenly spread, since the charge is the same everywhere",
             "correct": False,
             "why": "The charge is one object; the field it makes varies from "
                    "point to point."},
            {"text": "Wherever another charge happens to be placed",
             "correct": False,
             "why": "The map describes the space before anything is placed in "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s13",
        "band": "standard",
        "text": "A charged rod is held near a hanging ball inside a sealed "
                "jar, and the air is pumped out. What happens to the ball?",
        "options": [
            {"text": "It stops moving, because there is no air to carry the "
                     "force",
             "correct": False,
             "why": "Nothing carries the force. The field acts across empty "
                    "space."},
            {"text": "It moves just as it did before", "correct": True},
            {"text": "It moves the opposite way once the air has gone",
             "correct": False,
             "why": "Removing the air does not reverse anything; the field is "
                    "unchanged."},
            {"text": "It falls straight down, because upthrust has gone",
             "correct": False,
             "why": "Upthrust from air is far too small to matter, and it "
                    "does not affect the electric force."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s14",
        "band": "standard",
        "text": "Which pair of statements about field arrows is right?",
        "options": [
            {"text": "Away from positive, away from negative",
             "correct": False,
             "why": "A positive test charge is pulled TOWARDS a negative "
                    "charge, so those arrows point in."},
            {"text": "Towards positive, towards negative", "correct": False,
             "why": "A positive test charge is pushed AWAY from a positive "
                    "charge, so those arrows point out."},
            {"text": "Away from positive, towards negative", "correct": True},
            {"text": "Towards positive, away from negative", "correct": False,
             "why": "Both halves are the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s15",
        "band": "standard",
        "text": "Why is a person safer inside a car during a thunderstorm?",
        "options": [
            {"text": "Because the rubber tyres insulate the car from the "
                     "ground",
             "correct": False,
             "why": "A lightning bolt has already crossed kilometres of air; "
                    "a few centimetres of rubber stops nothing."},
            {"text": "Because the metal shell carries the charge round the "
                     "outside",
             "correct": True},
            {"text": "Because the car's windows block the electric field",
             "correct": False,
             "why": "Glass is an insulator and does not cancel a field; the "
                    "metal shell is what protects."},
            {"text": "Because the car is earthed through the road surface",
             "correct": False,
             "why": "Tarmac is a poor conductor, and the protection works "
                    "even on a dry road."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s16",
        "band": "standard",
        "text": "What do a gravitational field and an electric field have in "
                "common?",
        "options": [
            {"text": "Both act only on objects that are touching",
             "correct": False,
             "why": "Both act across a gap, which is the reason they need "
                    "fields to describe them."},
            {"text": "Both can attract and repel", "correct": False,
             "why": "Gravity only ever attracts; the electric field does "
                    "both."},
            {"text": "Both have a size and a direction at every point",
             "correct": True},
            {"text": "Both need air to carry them", "correct": False,
             "why": "Neither does; both act perfectly well in a vacuum."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s17",
        "band": "standard",
        "text": "A small positive charge is released in a field pointing "
                "steadily to the left. What does it do?",
        "options": [
            {"text": "Stays where it is, because the field is steady",
             "correct": False,
             "why": "A steady field still pushes; steady means the push does "
                    "not change, not that there is none."},
            {"text": "Moves to the left, in the direction of the arrows",
             "correct": True},
            {"text": "Moves to the right, against the arrows", "correct": False,
             "why": "That is what a NEGATIVE charge would do."},
            {"text": "Moves at right angles to the arrows", "correct": False,
             "why": "The force is along the field direction, not across it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s18",
        "band": "standard",
        "text": "A charged comb bends a stream of water in the lab. What "
                "would happen in a vacuum?",
        "options": [
            {"text": "Nothing, because there would be no air to carry the "
                     "force",
             "correct": False,
             "why": "Air carries nothing; the field acts across empty "
                    "space."},
            {"text": "The same bending, because the field does not need air",
             "correct": True},
            {"text": "The stream would bend the other way", "correct": False,
             "why": "Nothing reverses the direction of the force."},
            {"text": "The water would be repelled instead", "correct": False,
             "why": "The induction that attracts it works the same way "
                    "whatever surrounds it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p9-03-h05",
        "band": "harder",
        "text": "A small POSITIVE charge is released at rest just outside a "
                "lone negative charge. What happens?",
        "options": [
            {"text": "It is pushed away, along the arrows", "correct": False,
             "why": "The arrows point INWARDS around a negative charge, so a "
                    "positive test charge is drawn in."},
            {"text": "It is pulled inwards, along the arrows", "correct": True},
            {"text": "It stays put, because it was released at rest",
             "correct": False,
             "why": "Being at rest is not being in balance: a force acts on "
                    "it the moment it is there."},
            {"text": "It circles the charge at a steady distance",
             "correct": False,
             "why": "The force points straight at the charge, so a stationary "
                    "test charge moves straight in."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h06",
        "band": "harder",
        "text": "A test charge is released exactly at a null point between "
                "two like charges. What happens?",
        "options": [
            {"text": "It is pushed towards the nearer charge", "correct": False,
             "why": "The point is equidistant from both, and the two pushes "
                    "cancel there."},
            {"text": "It stays put — but the balance is easily upset",
             "correct": True},
            {"text": "It stays put permanently, whatever disturbs it",
             "correct": False,
             "why": "Move it a hair either way and one charge wins, so the "
                    "balance does not hold."},
            {"text": "It is pushed straight out at right angles",
             "correct": False,
             "why": "At the null point itself there is no field at all, so "
                    "nothing pushes it anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h07",
        "band": "harder",
        "text": "Why is a null point described as no field at all rather than "
                "a weak one?",
        "options": [
            {"text": "Because the two contributions are equal and opposite, "
                     "so they add to nothing",
             "correct": True},
            {"text": "Because the charges are too far away to reach that "
                     "point",
             "correct": False,
             "why": "Both reach it strongly; it is the directions that "
                    "cancel."},
            {"text": "Because a field cannot exist between two like charges",
             "correct": False,
             "why": "It exists everywhere else between them; only one point "
                    "cancels."},
            {"text": "Because the point is exactly halfway, and halfway "
                     "always cancels",
             "correct": False,
             "why": "Halfway cancels only when the two charges are equal; "
                    "unequal ones cancel elsewhere."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h08",
        "band": "harder",
        "text": "A student says the air in the gap must be carrying the force "
                "between two charges. Which observation refutes it?",
        "options": [
            {"text": "The force gets weaker as the charges are moved apart",
             "correct": False,
             "why": "Air could be imagined to weaken with distance too, so "
                    "this does not settle it."},
            {"text": "The force still acts with all the air pumped out",
             "correct": True},
            {"text": "The force is stronger between larger charges",
             "correct": False,
             "why": "That is about the charges, and says nothing about what "
                    "lies between them."},
            {"text": "The force acts equally on both objects", "correct": False,
             "why": "True, and true of contact forces as well, so it does not "
                    "rule the air out."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h09",
        "band": "harder",
        "text": "Why does a metal box protect what is inside it from an "
                "outside electric field?",
        "options": [
            {"text": "Because metal reflects the field back the way it came",
             "correct": False,
             "why": "Nothing bounces off; the metal's own charges do the "
                    "work."},
            {"text": "Because the metal's free charges move until their field "
                     "cancels the outside one",
             "correct": True},
            {"text": "Because a field cannot pass through any solid",
             "correct": False,
             "why": "It passes through wood, plastic and glass perfectly "
                    "well; free charges are what matter."},
            {"text": "Because the box is earthed through whatever it stands "
                     "on",
             "correct": False,
             "why": "It works while standing on an insulator too, so earthing "
                    "is not what does it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h10",
        "band": "harder",
        "text": "A charged rod is held first above a stream of water and "
                "then below it. Which way does the stream bend each time?",
        "options": [
            {"text": "Upwards then downwards — always towards the rod",
             "correct": True},
            {"text": "Downwards both times, because the water falls",
             "correct": False,
             "why": "Gravity pulls it down anyway; the question is the extra "
                    "bend, and that follows the rod."},
            {"text": "Away from the rod both times, because water carries no "
                     "charge",
             "correct": False,
             "why": "Neutral water is attracted by induction, so it bends "
                    "towards the rod rather than away."},
            {"text": "Upwards both times, because charge always lifts",
             "correct": False,
             "why": "Nothing about charge lifts things; the bend follows "
                    "wherever the rod is held."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h11",
        "band": "harder",
        "text": "Two unequal like charges sit a short distance apart. Where "
                "is the null point?",
        "options": [
            {"text": "Exactly halfway between them", "correct": False,
             "why": "Halfway only works for equal charges; the bigger one "
                    "reaches further."},
            {"text": "Nearer the smaller charge", "correct": True},
            {"text": "Nearer the larger charge", "correct": False,
             "why": "Close to the larger charge its contribution dominates, "
                    "so nothing can cancel there."},
            {"text": "Outside the pair, beyond the larger charge",
             "correct": False,
             "why": "Outside the pair both contributions point the same way, "
                    "so they add rather than cancel."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h12",
        "band": "harder",
        "text": "Why does a field description work for gravity, magnetism and "
                "charge alike?",
        "options": [
            {"text": "Because all three are really the same force",
             "correct": False,
             "why": "They are distinct forces; only the way they are "
                    "described is shared."},
            {"text": "Because all three act across a gap",
             "correct": True},
            {"text": "Because all three are carried by the air",
             "correct": False,
             "why": "None of them is; all three work in a vacuum."},
            {"text": "Because all three attract and repel", "correct": False,
             "why": "Gravity only attracts, and the field picture still "
                    "works for it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h13",
        "band": "harder",
        "text": "A test charge is moved from 2 cm to 6 cm from a lone charge. "
                "Roughly what happens to the force on it?",
        "options": [
            {"text": "It falls to a third", "correct": False,
             "why": "That scales with the distance, and the force falls far "
                    "faster than that."},
            {"text": "It falls to about a ninth", "correct": True},
            {"text": "It is unchanged, because the test charge is the same",
             "correct": False,
             "why": "The field varies from point to point, so the force on "
                    "the same charge changes with position."},
            {"text": "It falls to a half", "correct": False,
             "why": "Three times the distance takes far more than half the "
                    "force away."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h14",
        "band": "harder",
        "text": "Field arrows are drawn for a positive test charge. Why is "
                "that a choice rather than a fact about nature?",
        "options": [
            {"text": "Because nature has no positive charges, only negative "
                     "ones",
             "correct": False,
             "why": "Both exist; protons are positive and electrons "
                    "negative."},
            {"text": "Because they could have been drawn for a negative test "
                     "charge instead",
             "correct": True},
            {"text": "Because the direction of a field cannot really be "
                     "measured",
             "correct": False,
             "why": "It is measured easily by seeing which way a charge is "
                    "pushed."},
            {"text": "Because arrows are only a rough guide to a real field",
             "correct": False,
             "why": "They are a precise record of size and direction; the "
                    "convention is about which sign to use."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h15",
        "band": "harder",
        "text": "Why is a lightning conductor made with a sharp point at the "
                "top?",
        "options": [
            {"text": "Because a point is the strongest shape for a metal rod",
             "correct": False,
             "why": "Strength is not the reason; what happens to the field "
                    "there is."},
            {"text": "Because the field is strongest at a sharp point, so "
                     "charge escapes there first",
             "correct": True},
            {"text": "Because a point cannot be struck by lightning",
             "correct": False,
             "why": "It is the most likely place to be struck, which is part "
                    "of how it protects the building."},
            {"text": "Because a point holds more charge than a flat surface",
             "correct": False,
             "why": "It is where the field is most concentrated, rather than "
                    "where more charge sits."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h16",
        "band": "harder",
        "text": "Two students disagree about whether there is a field inside "
                "a hollow charged metal sphere. Who is right?",
        "options": [
            {"text": "There is a strong field inside, because charge "
                     "surrounds it",
             "correct": False,
             "why": "The contributions from all round the shell cancel, "
                    "leaving nothing inside."},
            {"text": "There is no field inside, which is why a metal box "
                     "shields",
             "correct": True},
            {"text": "There is a field, but only near the walls",
             "correct": False,
             "why": "It cancels throughout the inside, not merely at the "
                    "centre."},
            {"text": "It depends on whether the sphere is positive or "
                     "negative",
             "correct": False,
             "why": "The cancelling works the same way for either sign."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h17",
        "band": "harder",
        "text": "A field map is drawn with no charges anywhere on it, yet "
                "arrows are shown. What must be true?",
        "options": [
            {"text": "The map is wrong, since arrows need a charge to start "
                     "from",
             "correct": False,
             "why": "The sources may simply be off the edge of the drawing."},
            {"text": "There are charges somewhere outside the area drawn",
             "correct": True},
            {"text": "The arrows show gravity rather than an electric field",
             "correct": False,
             "why": "Nothing about the map says that, and a gravitational map "
                    "would need masses off the page just the same."},
            {"text": "The field has appeared on its own", "correct": False,
             "why": "A field is always what some charge does to the space "
                    "around it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h18",
        "band": "harder",
        "text": "Why is it wrong to say the field pushes a negative charge "
                "backwards along the arrows because the arrows are wrong?",
        "options": [
            {"text": "Because the arrows are wrong, and should be redrawn for "
                     "each charge",
             "correct": False,
             "why": "One map serves every charge; redrawing it per charge "
                    "would defeat the purpose."},
            {"text": "Because the arrows are a convention, and a negative "
                     "charge goes the other way",
             "correct": True},
            {"text": "Because negative charges are not pushed by fields at "
                     "all",
             "correct": False,
             "why": "They are pushed exactly as hard as a positive charge of "
                    "the same size."},
            {"text": "Because a field cannot act on a negative charge without "
                     "contact",
             "correct": False,
             "why": "It acts across a gap on either sign."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ────────────────────────────────────────
    {
        "id": "p9-03-e19",
        "band": "easier",
        "text": "What two things does an electric field have at every point "
                "in space?",
        "options": [
            {"text": "A size and a direction", "correct": True},
            {"text": "A charge and a mass", "correct": False,
             "why": "The field belongs to the space itself. Charge and mass "
                    "belong to objects, not to the empty points around "
                    "them."},
            {"text": "A colour and a temperature", "correct": False,
             "why": "Neither of those is part of what a field is. A field "
                    "is a push, described by how big it is and which way it "
                    "acts."},
            {"text": "A start and a finish", "correct": False,
             "why": "A field has no beginning or end of its own; it is "
                    "there at every point, with a size and a direction."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e20",
        "band": "easier",
        "text": "At one single point in space, how many directions can an "
                "electric field point in at the same time?",
        "options": [
            {"text": "Two, if two different charges are involved",
             "correct": False,
             "why": "However many charges are involved, their contributions "
                    "add together first. The result is one field, one "
                    "direction."},
            {"text": "As many as there are charges nearby", "correct": False,
             "why": "The separate pushes are combined before anything "
                    "feels them, leaving a single field at that point."},
            {"text": "Only one", "correct": True},
            {"text": "None — a point can only have a size, not a direction",
             "correct": False,
             "why": "A field's value always includes a direction as well "
                    "as a size, at every point where it exists."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e21",
        "band": "easier",
        "text": "The cable to a TV aerial has a wire in the middle wrapped "
                "in a metal braid. What is the braid there to do?",
        "options": [
            {"text": "Carry the picture signal instead of the inner wire",
             "correct": False,
             "why": "The signal still travels down the inner wire; the "
                    "braid is not the path the signal uses."},
            {"text": "Make the cable stronger so it does not snap",
             "correct": False,
             "why": "A braid does add some strength, but that is not why "
                    "it surrounds the signal wire specifically."},
            {"text": "Stop the cable from picking up charge by rubbing "
                     "against the wall", "correct": False,
             "why": "Rubbing is not the problem being solved here; it is "
                    "outside fields reaching the signal wire that the "
                    "braid stops."},
            {"text": "Shield the inner wire from outside electric fields",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e22",
        "band": "easier",
        "text": "Of a gravitational field, a magnetic field and an electric "
                "field, which one can only ever pull, never push?",
        "options": [
            {"text": "The gravitational field", "correct": True},
            {"text": "The magnetic field", "correct": False,
             "why": "A magnetic field can push or pull, depending on which "
                    "poles are facing each other."},
            {"text": "The electric field", "correct": False,
             "why": "An electric field can push or pull, depending on the "
                    "two signs involved."},
            {"text": "All three fields can only pull", "correct": False,
             "why": "Only gravity is limited that way. The other two do "
                    "both, which is why only mass has no opposite sign."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e23",
        "band": "easier",
        "text": "Who first pictured the space around a magnet as filled "
                "with lines of force?",
        "options": [
            {"text": "James Clerk Maxwell", "correct": False,
             "why": "Maxwell came later, and turned the picture into proper "
                    "mathematics rather than inventing it."},
            {"text": "Isaac Newton", "correct": False,
             "why": "Newton's own field, if he can be said to have had one, "
                    "concerned gravity, and centuries earlier."},
            {"text": "Nobody in particular — the idea grew slowly with no "
                     "single originator", "correct": False,
             "why": "It has a clear origin: one scientist's picture of "
                    "space around a magnet, with no mathematics behind it "
                    "at first."},
            {"text": "Michael Faraday", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e24",
        "band": "easier",
        "text": "The charge making a field is doubled, and nothing else "
                "changes. What happens to the field it produces at a fixed "
                "point?",
        "options": [
            {"text": "It stays exactly the same", "correct": False,
             "why": "The field is set by the charge that made it, so "
                    "changing that charge changes the field too."},
            {"text": "It halves", "correct": False,
             "why": "A bigger source charge produces a bigger field, not a "
                    "smaller one."},
            {"text": "It doubles too", "correct": True},
            {"text": "It depends on the test charge used to explore it",
             "correct": False,
             "why": "The field belongs to the space made by the source "
                    "charge; the test charge used to explore it makes no "
                    "difference at all."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e25",
        "band": "easier",
        "text": "A map already shows the combined field of two charges. A "
                "third charge is now brought up close by. What happens to "
                "the map?",
        "options": [
            {"text": "It changes everywhere, as the third contribution "
                     "adds to the other two", "correct": True},
            {"text": "It changes only in the small region right next to "
                     "the new charge", "correct": False,
             "why": "A field reaches everywhere, so the whole pattern "
                    "shifts, not just the area nearest the new charge."},
            {"text": "It stays the same, because a map can only ever show "
                     "two charges at once", "correct": False,
             "why": "A map can show the combined field of any number of "
                    "charges; there is no limit of two."},
            {"text": "The two original charges stop contributing, and only "
                     "the new one is shown", "correct": False,
             "why": "All three charges keep contributing. None of them "
                    "switches off just because another one arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e26",
        "band": "easier",
        "text": "A magnetic field can be a push or a pull. What decides "
                "which one it is?",
        "options": [
            {"text": "How far apart the two magnets are", "correct": False,
             "why": "Distance changes how strong the force is, not whether "
                    "it pushes or pulls."},
            {"text": "How large the two magnets are", "correct": False,
             "why": "Size affects the strength of the force, not its "
                    "direction."},
            {"text": "Whether the magnets are moving", "correct": False,
             "why": "Two stationary magnets can push or pull each other "
                    "just as well; movement is not what decides it."},
            {"text": "Which poles are facing each other", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e27",
        "band": "easier",
        "text": "An electric field can be a push or a pull, and it is "
                "described as being much stronger than gravity. What "
                "decides whether it pushes or pulls?",
        "options": [
            {"text": "How far apart the two charges are", "correct": False,
             "why": "Distance changes how strong the push or pull is, not "
                    "which one it is."},
            {"text": "How big the two charges are", "correct": False,
             "why": "Size changes the strength, not whether it is a push "
                    "or a pull."},
            {"text": "The two signs involved", "correct": True},
            {"text": "Whether the charges are touching", "correct": False,
             "why": "The force acts across a gap; the charges never need "
                    "to touch for it to act."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e28",
        "band": "easier",
        "text": "What is the name for a mark on a field map that shows a "
                "field's size and direction at one point?",
        "options": [
            {"text": "A null point", "correct": False,
             "why": "A null point is a place where the field cancels to "
                    "zero, not the mark showing size and direction."},
            {"text": "A test charge", "correct": False,
             "why": "A test charge is the small charge imagined at a "
                    "point, not the mark drawn to describe the field "
                    "there."},
            {"text": "A charge symbol", "correct": False,
             "why": "That marks where an actual charge sits, not the field "
                    "it makes at some other point."},
            {"text": "A field arrow", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e29",
        "band": "easier",
        "text": "What is meant by the term \"electric field\"?",
        "options": [
            {"text": "The state a charged object puts the space around it "
                     "into", "correct": True},
            {"text": "The total charge stored on an object", "correct": False,
             "why": "That is simply the object's own charge. The field is "
                    "what that charge does to the space around it."},
            {"text": "The force felt only when two objects touch",
             "correct": False,
             "why": "The field acts across a gap, with no contact needed "
                    "at all."},
            {"text": "The path an electron follows between two charges",
             "correct": False,
             "why": "No electron travels between the charges; nothing "
                    "crosses the gap."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-e30",
        "band": "easier",
        "text": "Of a gravitational field, a magnetic field and an electric "
                "field, which one is made by something with charge?",
        "options": [
            {"text": "The gravitational field", "correct": False,
             "why": "A gravitational field is made by mass, not by "
                    "charge."},
            {"text": "The magnetic field", "correct": False,
             "why": "A magnetic field is made by a magnet or by a current, "
                    "not directly by a charge sitting still."},
            {"text": "The electric field", "correct": True},
            {"text": "All three, since they all come from the same "
                     "underlying property", "correct": False,
             "why": "Mass, magnetism and charge are three separate "
                    "properties, so an object can have any one of them "
                    "without the others."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ───────────────────────────────────────
    {
        "id": "p9-03-s19",
        "band": "standard",
        "text": "A test point is moved from a distance d away from a "
                "single charge to a distance 2d away. Roughly what happens "
                "to the field there?",
        "options": [
            {"text": "It falls to about a half", "correct": False,
             "why": "That would be true if the field tracked distance "
                    "directly. It falls faster than that."},
            {"text": "It stays about the same", "correct": False,
             "why": "The field depends strongly on distance from the "
                    "charge, so doubling the distance changes it a great "
                    "deal."},
            {"text": "It doubles", "correct": False,
             "why": "Moving further from a charge always weakens its "
                    "field, never strengthens it."},
            {"text": "It falls to about a quarter", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s20",
        "band": "standard",
        "text": "The field's direction is defined using a small positive "
                "test charge. Why does the test charge have to be small?",
        "options": [
            {"text": "So it is light enough to be pushed by a weak field",
             "correct": False,
             "why": "Weight has nothing to do with it; the field would "
                    "push a heavy charge too, just less noticeably."},
            {"text": "So it fits neatly onto a diagram", "correct": False,
             "why": "The drawing is not the reason; a real measurement "
                    "needs a small test charge for the same reason."},
            {"text": "So it does not add its own field and disturb the one "
                     "being measured", "correct": True},
            {"text": "So its own charge cancels out exactly with the field "
                     "it measures", "correct": False,
             "why": "Nothing cancels. A small test charge simply disturbs "
                    "the arrangement as little as possible while still "
                    "being pushed by it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s21",
        "band": "standard",
        "text": "Two equal positive charges sit a short way apart. A point "
                "is much closer to one of them than the other, not at the "
                "midpoint. Which way does the total field point there?",
        "options": [
            {"text": "Away from the nearer charge", "correct": True},
            {"text": "Away from the further charge", "correct": False,
             "why": "The nearer charge's push is the stronger of the two, "
                    "so its direction wins, not the further one's."},
            {"text": "It is zero, as the point is between the two charges",
             "correct": False,
             "why": "The field is only zero exactly at the midpoint, where "
                    "the two equal pushes cancel. Off-centre, one wins."},
            {"text": "Towards the nearer charge", "correct": False,
             "why": "Both charges are positive, so both push a test charge "
                    "away from themselves, never towards."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s22",
        "band": "standard",
        "text": "A positive charge and a negative charge sit a short way "
                "apart. A point lies beyond the positive charge, on the far "
                "side from the negative one. Which way does the field "
                "point there?",
        "options": [
            {"text": "Towards the negative charge", "correct": False,
             "why": "That direction only holds in the gap between the two "
                    "charges. Beyond the positive charge the rule "
                    "changes."},
            {"text": "It cancels to zero at every point beyond either "
                     "charge", "correct": False,
             "why": "For opposite charges the two contributions never "
                    "fully cancel outside the gap; one of them always "
                    "wins."},
            {"text": "Towards the positive charge", "correct": False,
             "why": "A positive charge always pushes a test charge away "
                    "from itself, never pulls it in."},
            {"text": "Away from the positive charge", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s23",
        "band": "standard",
        "text": "On a map of a single charge, every point the same "
                "distance from the charge has an arrow of the same length. "
                "Why?",
        "options": [
            {"text": "Because the field's strength depends only on "
                     "distance from the charge, not on the direction you "
                     "look", "correct": True},
            {"text": "Because the charge itself is spread evenly around a "
                     "circle", "correct": False,
             "why": "The charge sits at a single point. It is the field it "
                    "produces that happens to be the same strength all "
                    "round."},
            {"text": "Because the map is drawn to a fixed scale in every "
                     "direction", "correct": False,
             "why": "The scale is the same throughout the map, but that "
                    "alone would not make equal-distance arrows match in "
                    "length."},
            {"text": "Because arrows are only ever drawn at a few chosen "
                     "distances", "correct": False,
             "why": "The field has a value at every point, not only at "
                    "the distances a map happens to sample."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s24",
        "band": "standard",
        "text": "Maxwell turned Faraday's field picture into proper "
                "mathematics. What did his equations predict that nobody "
                "had asked for?",
        "options": [
            {"text": "That electric and magnetic fields could not exist "
                     "at the same time", "correct": False,
             "why": "The two exist together throughout this topic; "
                    "nothing rules one out in the presence of the other."},
            {"text": "That a field needs air to travel through, so his "
                     "equations gave no answer at all for the empty space "
                     "between the planets",
             "correct": False,
             "why": "The opposite: fields work in a total vacuum, which "
                    "is part of what makes this prediction so surprising."},
            {"text": "That a changing field travels through empty space "
                     "at a fixed speed, which turned out to be the speed "
                     "of light", "correct": True},
            {"text": "That gravity and electric charge are the same force "
                     "underneath", "correct": False,
             "why": "They remain two separate forces; only the way they "
                    "are described using fields is shared."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s25",
        "band": "standard",
        "text": "An aircraft is struck by lightning in mid-flight, and the "
                "electronics inside are undamaged. Which fact explains "
                "this?",
        "options": [
            {"text": "The metal skin's free charges rearrange so the "
                     "field inside stays nearly zero", "correct": True},
            {"text": "The aircraft is moving too fast for the strike to do "
                     "any damage", "correct": False,
             "why": "Speed makes no difference here; a stationary metal "
                    "shell protects its inside just as well."},
            {"text": "The electronics are too far from the outer skin to "
                     "be affected", "correct": False,
             "why": "Distance from the skin is not what protects them — "
                    "it is the skin's own charges rearranging that does "
                    "the work."},
            {"text": "Lightning strikes tend to miss metal objects in the "
                     "sky", "correct": False,
             "why": "Metal is exactly what a strike is likely to hit; the "
                    "protection comes after the strike, not from being "
                    "missed."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s26",
        "band": "standard",
        "text": "A small positive test charge is released on the line "
                "between two equal positive charges, a little to one side "
                "of the null point rather than exactly on it. What happens?",
        "options": [
            {"text": "It stays exactly where it was released, because the "
                     "two charges are equal in size",
             "correct": False,
             "why": "The field is zero only exactly at the null point. A "
                    "little to one side, the nearer charge's push wins."},
            {"text": "It is pushed further from the null point, towards "
                     "the charge it is nearer to", "correct": False,
             "why": "The nearer charge pushes a positive test charge away "
                    "from itself, not towards itself."},
            {"text": "It is pushed sideways, at right angles to the line "
                     "joining the two charges", "correct": False,
             "why": "Both pushes act along that line, so the total field "
                    "does too. Nothing acts across it."},
            {"text": "It is pushed back past the null point, away from "
                     "the charge it is nearer to", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s27",
        "band": "standard",
        "text": "Which single fact is true of BOTH the magnetic field and "
                "the electric field, but not of the gravitational field?",
        "options": [
            {"text": "Both act across a gap with nothing needed in "
                     "between", "correct": False,
             "why": "Gravity acts across a gap too — that is exactly why "
                    "all three are described using fields in the first "
                    "place."},
            {"text": "Both have a size and a direction at every point",
             "correct": False,
             "why": "All three fields have a size and a direction at "
                    "every point, gravity included."},
            {"text": "Both can be a push or a pull", "correct": True},
            {"text": "Both are made by something with mass", "correct": False,
             "why": "Mass makes a gravitational field. A magnet or a "
                    "current makes the magnetic one, and charge makes the "
                    "electric one."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s28",
        "band": "standard",
        "text": "Two different test charges are placed, one at a time, at "
                "the same point in a field. The second is twice the size "
                "of the first. Compare the forces each one feels there.",
        "options": [
            {"text": "The second feels twice the force of the first",
             "correct": True},
            {"text": "Both feel exactly the same force, since the field "
                     "at that point is fixed", "correct": False,
             "why": "The field being fixed is exactly why a bigger test "
                    "charge there feels a bigger force, not the same one."},
            {"text": "The second feels half the force of the first",
             "correct": False,
             "why": "A bigger test charge feels a bigger force at the "
                    "same point, not a smaller one."},
            {"text": "The forces cannot be compared without knowing the "
                     "source charge's size", "correct": False,
             "why": "The ratio of the two forces depends only on the "
                    "ratio of the two test charges, whatever the source "
                    "charge happens to be."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s29",
        "band": "standard",
        "text": "A point lies in the field of two separate charges. How is "
                "the total field there actually found?",
        "options": [
            {"text": "By adding just the two lengths, ignoring which way "
                     "each one points", "correct": False,
             "why": "Direction matters as much as size; two contributions "
                    "that point opposite ways can cancel rather than add "
                    "up."},
            {"text": "By using whichever contribution is larger and "
                     "ignoring the other", "correct": False,
             "why": "Both charges contribute at every point; the smaller "
                    "contribution still affects the total."},
            {"text": "By averaging the two contributions", "correct": False,
             "why": "Averaging would halve the answer when the two point "
                    "the same way, which is not what actually happens."},
            {"text": "By adding the two contributions as arrows, taking "
                     "their directions into account", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-s30",
        "band": "standard",
        "text": "In one experiment the charge making a field is doubled. In "
                "a separate experiment an unrelated field is left alone, "
                "but the TEST charge placed in it is doubled instead. In "
                "which experiment does the field itself get bigger?",
        "options": [
            {"text": "Only the second one, where the test charge was "
                     "doubled", "correct": False,
             "why": "The test charge changes the force it feels, not the "
                    "field it sits in."},
            {"text": "Both experiments", "correct": False,
             "why": "Doubling the test charge leaves the field exactly as "
                    "it was; only the force on it changes."},
            {"text": "Only the first one, where the source charge was "
                     "doubled", "correct": True},
            {"text": "Neither experiment", "correct": False,
             "why": "Doubling the source charge really does double the "
                    "field it produces at every point."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "p9-03-h19",
        "band": "harder",
        "text": "Two equal charges, one positive and one negative, sit a "
                "fixed distance apart. Both charges are moved further "
                "apart until the separation has doubled, with their sizes "
                "unchanged. What happens to the field at the new midpoint, "
                "compared with the old one?",
        "options": [
            {"text": "It falls to about a quarter of what it was",
             "correct": True},
            {"text": "It falls to about a half of what it was",
             "correct": False,
             "why": "That would hold if the field tracked distance "
                    "directly. It falls faster, by the square of the "
                    "change."},
            {"text": "It stays the same, because the two charges have not "
                     "changed", "correct": False,
             "why": "Distance from each charge to the midpoint has also "
                    "grown, and that weakens each contribution."},
            {"text": "It doubles, because the gap between the charges is "
                     "now twice as wide", "correct": False,
             "why": "A wider gap means the midpoint is further from each "
                    "charge, which weakens the field there rather than "
                    "strengthening it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h20",
        "band": "harder",
        "text": "The metal braid around a coaxial cable's inner wire is "
                "damaged and cut away over a short section. What would you "
                "expect at that section?",
        "options": [
            {"text": "The signal is unaffected, since the inner wire "
                     "still carries it", "correct": False,
             "why": "The wire still carries the signal, but with no braid "
                    "around it there the shielding is gone."},
            {"text": "The whole cable stops working, from end to end",
             "correct": False,
             "why": "Only the unshielded section is exposed; the braided "
                    "lengths either side still protect the wire there."},
            {"text": "The braid's job is to add strength, so nothing "
                     "electrical changes", "correct": False,
             "why": "The braid's main job is shielding the wire from "
                    "outside fields, not adding strength."},
            {"text": "That section is no longer shielded, so outside "
                     "fields can now reach the wire directly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h21",
        "band": "harder",
        "text": "A charge is spread evenly over a hollow metal sphere. Just "
                "outside its surface, how does its field compare with the "
                "field of the same total charge concentrated at a single "
                "point at the sphere's centre?",
        "options": [
            {"text": "The sphere's field is weaker, because the charge is "
                     "spread over a larger area", "correct": False,
             "why": "Spreading the charge over the shell does not weaken "
                    "its effect outside; from out there it behaves like a "
                    "point charge of the same size."},
            {"text": "The sphere's field is stronger, because more of the "
                     "charge sits closer to the surface", "correct": False,
             "why": "Nothing about spreading the charge over the shell "
                    "makes the outside field any stronger."},
            {"text": "They are the same, outside the sphere", "correct": True},
            {"text": "They cannot be compared, since a spread-out charge "
                     "has no field of its own", "correct": False,
             "why": "A hollow charged sphere certainly has a field "
                    "outside it; it is the inside where there is none."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h22",
        "band": "harder",
        "text": "A field is measured at 2 cm from a charge, then again at "
                "8 cm — four times as far. Roughly what has happened to "
                "the field?",
        "options": [
            {"text": "It has fallen to about a quarter", "correct": False,
             "why": "That would hold if the field tracked distance "
                    "directly. It falls by the square of the change, not "
                    "in step with it."},
            {"text": "It has fallen to about an eighth", "correct": False,
             "why": "The distance changed by a factor of four, so the "
                    "field falls by four squared, not by four itself."},
            {"text": "It has stayed roughly the same", "correct": False,
             "why": "Multiplying the distance by four changes the field a "
                    "very great deal; it cannot stay roughly the same."},
            {"text": "It has fallen to about a sixteenth", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h23",
        "band": "harder",
        "text": "Charge A is twice the size of charge B, and the two sit a "
                "fixed distance apart. Compare the field A makes at B's "
                "location with the field B makes at A's location.",
        "options": [
            {"text": "A's field at B's location is twice as strong as B's "
                     "field at A's location", "correct": True},
            {"text": "The two fields are exactly equal, because the "
                     "forces on A and B are equal and opposite",
             "correct": False,
             "why": "The forces on the two are equal, but each charge's "
                    "own field depends only on itself, so the bigger "
                    "charge makes the stronger field."},
            {"text": "B's field at A's location is twice as strong, since "
                     "the smaller charge has further to reach",
             "correct": False,
             "why": "A field's strength comes from the size of the charge "
                    "that made it, not from which charge is doing the "
                    "reaching."},
            {"text": "Neither charge makes a field at the other's exact "
                     "location", "correct": False,
             "why": "Every charge makes a field at every point around it, "
                    "including at the other charge's location."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h24",
        "band": "harder",
        "text": "Two charges, the same size but opposite sign, sit a short "
                "way apart. Between two LIKE charges there is always a "
                "null point somewhere. Is there a null point anywhere on "
                "the line through this pair?",
        "options": [
            {"text": "Yes, exactly halfway between them, just as for two "
                     "like charges, because at the midpoint the two "
                     "contributions point in opposite directions and "
                     "cancel", "correct": False,
             "why": "Halfway between opposite charges the two "
                    "contributions point the same way and add, rather "
                    "than cancelling."},
            {"text": "Yes, but only far beyond one of the two charges",
             "correct": False,
             "why": "Beyond either charge the nearer one's contribution "
                    "dominates; the two never balance to zero out there "
                    "either."},
            {"text": "It depends on which one is called positive and "
                     "which is called negative", "correct": False,
             "why": "Swapping the labels changes nothing about the "
                    "geometry; an opposite pair has no null point on the "
                    "line either way."},
            {"text": "No — outside or between an opposite pair the two "
                     "contributions never point in exactly opposite "
                     "directions with equal size", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h25",
        "band": "harder",
        "text": "A student measures the field made by charge X, then swaps "
                "in a bigger test charge to measure the field made by "
                "charge Y. Why is that comparison unfair?",
        "options": [
            {"text": "Because the two source charges being compared "
                     "should also have been made equal first, so that the "
                     "only thing left different between the two "
                     "measurements is the test charge",
             "correct": False,
             "why": "The whole point is to compare two different source "
                    "charges; they are not supposed to be made equal."},
            {"text": "Because a bigger test charge always reads a smaller "
                     "field than a smaller one would", "correct": False,
             "why": "The field itself does not depend on the test charge "
                    "at all; only the force measured with it changes."},
            {"text": "Because using two different test charges makes the "
                     "measured forces hard to compare fairly, even though "
                     "neither field itself has actually changed",
             "correct": True},
            {"text": "Because only one single test charge may ever be "
                     "used in the whole topic", "correct": False,
             "why": "Any small test charge will do; what matters is using "
                    "the same one for both measurements, not one fixed "
                    "charge forever."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h26",
        "band": "harder",
        "text": "A student says a stronger field always means a bigger "
                "push, so field and force are really just two names for "
                "the same thing. Using the definition of the field, "
                "explain why they are not.",
        "options": [
            {"text": "They are the same thing; the two words are simply "
                     "used in different parts of the topic, one when "
                     "drawing a map of the space and the other when "
                     "working out a force in newtons", "correct": False,
             "why": "The definitions differ: the field is a property of "
                    "space, and the force is what a particular charge "
                    "feels because of it."},
            {"text": "Force is a property of space and field is a "
                     "property of the object placed in it", "correct": False,
             "why": "That has the two ideas swapped round: the field "
                    "belongs to the space, and the force is what a "
                    "particular object feels."},
            {"text": "They differ only in their units, and otherwise mean "
                     "exactly the same physical thing", "correct": False,
             "why": "It is more than a difference of units — the field "
                    "does not depend on what is placed in it, while the "
                    "force does."},
            {"text": "The field is the push a small test charge would "
                     "feel there; the actual force also depends on the "
                     "size of whatever charge is really placed at that "
                     "point", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h27",
        "band": "harder",
        "text": "Two equal positive charges sit 6 cm apart. A point on the "
                "line between them is 2 cm from one charge and 4 cm from "
                "the other. What is the field at that point?",
        "options": [
            {"text": "Zero, since the point lies between the two charges",
             "correct": False,
             "why": "It is zero only exactly at the midpoint, 3 cm from "
                    "each. This point is not there."},
            {"text": "Pointing away from the further charge, since a "
                     "bigger distance always gives the bigger "
                     "contribution", "correct": False,
             "why": "The opposite is true: the closer charge always makes "
                    "the stronger contribution at a point."},
            {"text": "Pointing away from the nearer charge, since its "
                     "contribution at 2 cm is the bigger of the two",
             "correct": True},
            {"text": "Equal to the field of just one charge on its own, "
                     "since the other is too far away to matter",
             "correct": False,
             "why": "4 cm is not far enough to ignore; the further charge "
                    "still makes a real, if smaller, contribution."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h28",
        "band": "harder",
        "text": "A source charge is tripled in size, and at the same time "
                "the distance to the test point is doubled. Overall, is "
                "the field there bigger, smaller, or unchanged?",
        "options": [
            {"text": "Smaller — about three-quarters of what it was",
             "correct": True},
            {"text": "Bigger, because tripling the charge always wins "
                     "over doubling the distance", "correct": False,
             "why": "Doubling the distance divides the field by four, "
                    "which outweighs the charge only being tripled."},
            {"text": "Unchanged, because the two changes exactly cancel "
                     "out", "correct": False,
             "why": "Tripling the charge multiplies the field by three, "
                    "while doubling the distance divides it by four — "
                    "those do not cancel to leave it unchanged."},
            {"text": "Smaller — about a third of what it was",
             "correct": False,
             "why": "That ignores the effect of the charge tripling, "
                    "which partly makes up for the distance increasing."},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h29",
        "band": "harder",
        "text": "Which of these would make the field at a fixed point "
                "weaker: moving the point further from the source charge, "
                "or shrinking the size of the test charge placed there?",
        "options": [
            {"text": "Only shrinking the test charge", "correct": False,
             "why": "The test charge's size changes the force it feels, "
                    "not the field that is already there at that point."},
            {"text": "Both of them weaken the field", "correct": False,
             "why": "Shrinking the test charge does not touch the field "
                    "at all; only moving the point changes it."},
            {"text": "Neither — the field depends only on the source "
                     "charge's own size", "correct": False,
             "why": "Distance from the source charge matters a great deal "
                    "too; moving the point further away genuinely weakens "
                    "the field."},
            {"text": "Only moving the point further away", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-03-h30",
        "band": "harder",
        "text": "Two unequal positive charges have a null point somewhere "
                "between them. The smaller of the two charges is now "
                "replaced with a larger one, while the original bigger "
                "charge stays the same. Which way does the null point "
                "shift?",
        "options": [
            {"text": "Towards the charge that was just increased",
             "correct": False,
             "why": "A stronger charge reaches further before the other "
                    "one catches it up, pushing the null point away from "
                    "itself, not towards it."},
            {"text": "It stays exactly where it was, since only one of "
                     "the two charges changed", "correct": False,
             "why": "Changing either charge's size shifts the balance "
                    "point between them."},
            {"text": "Away from the charge that was just increased",
             "correct": True},
            {"text": "It moves to the exact midpoint between the two "
                     "charges", "correct": False,
             "why": "The midpoint is only the null point when the two "
                    "charges are equal, and after the change they no "
                    "longer are."},
        ],
        "figure": None,
    },
]
