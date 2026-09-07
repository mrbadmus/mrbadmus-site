"""P5 lesson 03 — Upthrust, floating and sinking: twelve questions
(MRB-223).

Written against Design's page. The beach ball, the five one-litre blocks
and the two-panel beam are hers.

The discriminations, in the order the lesson builds them:

  · upthrust comes from the pressure DIFFERENCE across the object;
  · everything in a liquid gets it, sinkers included (`PRESS-10`);
  · it equals the weight of what is pushed out of the way, so it depends
    on VOLUME and not on weight (`PRESS-11`);
  · weight alone decides nothing (`PRESS-09`) — the harder band sits
    here and on the submarine;
  · hollowness is not the rule (`PRESS-12`).

⚠️ POSITION IS AUTHORED — index cycles 0, 1, 2, 3, giving three of each.

⚠️ Rung 1 (45 N in air, 37 N in water) and Rung 2 (the bolt and the ship)
are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P5"
LESSON = "upthrust-floating-and-sinking"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p5-03-e01",
        "band": "easier",
        "text": "Upthrust acts…",
        "options": [
            {"text": "upwards", "correct": True},
            {"text": "downwards", "correct": False,
             "why": "That is the weight. Upthrust is what opposes it."},
            {"text": "sideways", "correct": False,
             "why": "The sideways pushes on an object cancel each other. It "
                    "is the up-and-down difference that is left over."},
            {"text": "in the direction the object is moving", "correct": False,
             "why": "It acts upwards whether the object is rising, sinking "
                    "or still."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e02",
        "band": "easier",
        "text": "Upthrust on an object is equal to…",
        "options": [
            {"text": "the weight of the object, whether it floats or "
                     "sinks", "correct": False,
             "why": "Only when it floats. A sinker's upthrust is less than "
                    "its weight, which is why it sinks."},
            {"text": "the weight of the liquid it pushes out of the way",
             "correct": True},
            {"text": "the depth it is at, measured down from the surface",
             "correct": False,
             "why": "A depth is not a force. A block gets the same upthrust "
                    "at 1 m and at 10 m, once it is fully under."},
            {"text": "the pressure of the liquid at the bottom of the "
                     "object", "correct": False,
             "why": "That is a pressure, not a force — and it is only half "
                    "the story. The push on the top counts too."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e03",
        "band": "easier",
        "text": "A stone weighs 20 N in air and 14 N when hanging fully "
                "under water. What is the upthrust?",
        "options": [
            {"text": "34 N", "correct": False,
             "why": "Adding gives a force bigger than the stone's own "
                    "weight. The water takes weight OFF the balance."},
            {"text": "6 N", "correct": True},
            {"text": "14 N", "correct": False,
             "why": "That is the reading in the water, which is what is LEFT "
                    "after the upthrust has been taken off."},
            {"text": "1.4 N", "correct": False,
             "why": "That is 20 ÷ 14, a ratio rather than a force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e04",
        "band": "easier",
        "text": "An object floats when…",
        "options": [
            {"text": "it is lighter than water, whatever shape it has been "
                     "made into", "correct": False,
             "why": "A ship is not lighter than water. What matters is the "
                    "water it pushes aside."},
            {"text": "it has air sealed inside it, because air always "
                     "keeps things up", "correct": False,
             "why": "A sealed tin full of air sinks if it is heavy enough. "
                    "Air only helps by changing what is pushed aside."},
            {"text": "the upthrust on it equals its weight, so nothing is "
                     "left over", "correct": True},
            {"text": "it is sitting at the surface instead of down in the "
                     "water", "correct": False,
             "why": "That is the result, not the reason. Something held at "
                    "the surface by a hand is not floating."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p5-03-s01",
        "band": "standard",
        "text": "Two one-litre blocks, one cork and one steel, are both held "
                "completely under water. Which gets the bigger upthrust?",
        "options": [
            {"text": "The steel, because it weighs far more than the "
                     "cork.", "correct": False,
             "why": "Upthrust does not depend on the object's weight. It "
                    "depends on what the object pushes aside."},
            {"text": "The same on both — each pushes aside one litre.",
             "correct": True},
            {"text": "The cork, because it is the one trying to rise.",
             "correct": False,
             "why": "Trying to rise is the RESULT of its small weight, not "
                    "a bigger upthrust."},
            {"text": "The steel, because it is the one that goes deeper.",
             "correct": False,
             "why": "Once fully under, going deeper changes nothing: the "
                    "pushes on top and bottom both rise by the same amount."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s02",
        "band": "standard",
        "text": "A one-litre block of ice weighs 9.2 N. One litre of water "
                "weighs 10 N. How much of the ice sits below the surface?",
        "options": [
            {"text": "All of it — ice is only just lighter.",
             "correct": False,
             "why": "Fully under it would get 10 N of upthrust against 9.2 N "
                    "of weight, and 0.8 N would push it back up."},
            {"text": "About 92 per cent of it.", "correct": True},
            {"text": "About 8 per cent of it.", "correct": False,
             "why": "That is the fraction that shows ABOVE the surface, "
                    "which is why an iceberg looks so small."},
            {"text": "Exactly half.", "correct": False,
             "why": "Half would push aside 5 N of water, nowhere near enough "
                    "to hold up 9.2 N."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s03",
        "band": "standard",
        "text": "A heavy rock feels easier to lift while it is still under "
                "water and suddenly heavier as it breaks the surface. Why?",
        "options": [
            {"text": "The water makes the rock itself lighter, so there is "
                     "genuinely less of it to lift while it is under.",
             "correct": False,
             "why": "Its weight is unchanged throughout. What changes is "
                    "how much of it you have to supply."},
            {"text": "Water reduces the pull of gravity on it, so the "
                     "object genuinely weighs less the whole time it is "
                     "under",
             "correct": False,
             "why": "Gravity is unchanged. Something else is helping you "
                    "while the rock is submerged."},
            {"text": "Under water the upthrust is taking part of the weight, "
                     "and it stops as soon as the rock leaves the water.",
             "correct": True},
            {"text": "You get more grip on a wet rock, so less of your "
                     "effort is wasted while it is still in the water.",
             "correct": False,
             "why": "Grip is a separate matter, and a wet rock is usually "
                    "harder to hold, not easier."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s04",
        "band": "standard",
        "text": "A ship's steel is melted down and cast into one solid "
                "block. The block sinks. What changed?",
        "options": [
            {"text": "The weight of the steel went up when it was cast, so "
                     "the water can no longer hold the block up.",
             "correct": False,
             "why": "It is the same steel and the same weight. Nothing was "
                    "added."},
            {"text": "Steel became denser when it was melted, so the same "
                     "block of it now weighs more for its size.",
             "correct": False,
             "why": "The steel is unchanged. What changed is the SHAPE it "
                    "is in."},
            {"text": "Gravity acts more strongly on a solid shape than it "
                     "does on a hollow one of exactly the same weight",
             "correct": False,
             "why": "Gravity does not care about shape. Neither does the "
                    "weight."},
            {"text": "The volume of water it can push aside collapsed, so "
                     "the upthrust can no longer match the weight.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p5-03-h01",
        "band": "harder",
        "text": "Where does upthrust actually come from?",
        "options": [
            {"text": "From the liquid trying to get back to the space "
                     "where the object is, and shoving it out of the way "
                     "as it does", "correct": False,
             "why": "A liquid does not try to do anything. The force has a "
                    "mechanical origin."},
            {"text": "From the pressure being greater on the bottom of the "
                     "object than on the top, because the bottom is deeper.",
             "correct": True},
            {"text": "From the object being lighter than the liquid around "
                     "it, which is what allows the liquid to hold it up.",
             "correct": False,
             "why": "A sinker is heavier than its own volume of water and "
                    "still gets upthrust."},
            {"text": "From the surface of the liquid pushing down "
                     "everywhere, and that push reaching the object from "
                     "below.", "correct": False,
             "why": "The surface presses down on the top of the object. It "
                    "is the DIFFERENCE with the bottom that is left over."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h02",
        "band": "harder",
        "text": "A submarine dives by flooding its ballast tanks. What "
                "happens to the upthrust on it?",
        "options": [
            {"text": "It falls, because the submarine is now a great deal "
                     "heavier.",
             "correct": False,
             "why": "Upthrust does not depend on the submarine's weight. It "
                    "depends on the water it pushes aside."},
            {"text": "It rises, because the submarine is now sitting "
                     "deeper.",
             "correct": False,
             "why": "Once fully submerged, depth changes nothing: the pushes "
                    "on top and bottom rise together."},
            {"text": "It stays the same — the shape and volume have not "
                     "changed.", "correct": True},
            {"text": "It becomes zero, and that is why the submarine sinks "
                     "at all.",
             "correct": False,
             "why": "It is still fully supported by the same upthrust. What "
                    "changed is that the weight now exceeds it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h03",
        "band": "harder",
        "text": "A hot-air balloon rises. Which sentence describes it in the "
                "same terms as a cork in water?",
        "options": [
            {"text": "Hot air rises because heat always travels upwards, "
                     "and the balloon is carried along with the heat.",
             "correct": False,
             "why": "That describes nothing about the forces, and heat "
                    "travelling upwards is a separate idea."},
            {"text": "The envelope is sealed, so nothing heavy can get "
                     "into it and there is nothing at all to weigh it "
                     "down.",
             "correct": False,
             "why": "Sealed things sink all the time. What matters is what "
                    "is pushed aside."},
            {"text": "The balloon is lighter than the air, so gravity "
                     "misses it altogether and there is nothing to pull it "
                     "down", "correct": False,
             "why": "Gravity pulls on it exactly as on anything else. The "
                    "upthrust simply beats it."},
            {"text": "The hot air inside weighs less than the cold air the "
                     "envelope pushes out of the way, so the upthrust wins.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h04",
        "band": "harder",
        "text": "A ship's Plimsoll line has different marks for fresh water "
                "and salt water. Why?",
        "options": [
            {"text": "Salt water is more corrosive, so the hull must sit "
                     "higher up to keep the paint clear of the water",
             "correct": False,
             "why": "Corrosion is a real problem and a separate one. The "
                    "marks are about how deep the hull may legally sit."},
            {"text": "A cubic metre of salt water weighs more, so the same "
                     "hull pushes aside more weight and floats higher.",
             "correct": True},
            {"text": "Salt water is denser than fresh, so a ship pushes "
                     "further down into it and has to be marked lower.",
             "correct": False,
             "why": "The premise is right and the conclusion is backwards. "
                    "Denser water gives MORE upthrust, so the hull rides "
                    "higher."},
            {"text": "The ship's weight changes between fresh water and "
                     "salt water, so the safe mark has to change too.",
             "correct": False,
             "why": "The ship's weight is whatever it is loaded to. It is "
                    "the water that has changed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-03-e05",
        "band": "easier",
        "text": "What causes upthrust on an object in a liquid?",
        "options": [
            {"text": "The liquid pushing harder on its bottom than on its "
                     "top",
             "correct": True},
            {"text": "The object being lighter than the liquid",
             "correct": False,
             "why": "A heavy sinking object gets upthrust too; the cause is "
                    "the pressure difference."},
            {"text": "The liquid clinging to the sides of the object",
             "correct": False,
             "why": "Clinging is surface tension, which is a much smaller "
                    "effect and not this one."},
            {"text": "Air trapped underneath the object", "correct": False,
             "why": "A solid block with no trapped air still gets upthrust."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e06",
        "band": "easier",
        "text": "Does an object that sinks get any upthrust?",
        "options": [
            {"text": "No — upthrust only acts on things that float",
             "correct": False,
             "why": "It acts on anything in a liquid; a sinking object simply "
                    "weighs more than the upthrust."},
            {"text": "Yes, but only for the first moment", "correct": False,
             "why": "It is there the whole time it is under, which is why it "
                    "feels lighter throughout."},
            {"text": "Yes — just not enough to match its weight",
             "correct": True},
            {"text": "No — upthrust turns into weight when something sinks",
             "correct": False,
             "why": "One force never becomes another; both act on the object "
                    "at once."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e07",
        "band": "easier",
        "text": "A block weighs 30 N in air and 22 N hanging fully under "
                "water. What is the upthrust?",
        "options": [
            {"text": "52 N", "correct": False,
             "why": "That adds the two readings; upthrust is the difference "
                    "between them."},
            {"text": "22 N", "correct": False,
             "why": "That is the reading in water, which is the weight minus "
                    "the upthrust."},
            {"text": "30 N", "correct": False,
             "why": "That is the weight in air, before any upthrust acts."},
            {"text": "8 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e08",
        "band": "easier",
        "text": "Upthrust is measured in…",
        "options": [
            {"text": "newtons", "correct": True},
            {"text": "pascals", "correct": False,
             "why": "Pascals measure pressure. Upthrust is a force, so it is "
                    "in newtons."},
            {"text": "kilograms", "correct": False,
             "why": "Kilograms measure mass, and upthrust is a force."},
            {"text": "cubic centimetres", "correct": False,
             "why": "That is a volume — the volume displaced matters, but "
                    "upthrust itself is a force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e09",
        "band": "easier",
        "text": "An object sinks when…",
        "options": [
            {"text": "its weight is more than the upthrust even fully under",
             "correct": True},
            {"text": "it is heavy", "correct": False,
             "why": "A ship is enormously heavy and floats; weight alone "
                    "settles nothing."},
            {"text": "it is solid rather than hollow", "correct": False,
             "why": "A solid block of wood floats and a hollow steel ball can "
                    "sink if it is thick enough."},
            {"text": "there is no upthrust acting on it at all, however deep "
                     "it goes",
             "correct": False,
             "why": "Upthrust acts on it the whole way down; it is simply too "
                    "small."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e10",
        "band": "easier",
        "text": "Upthrust is equal to the weight of…",
        "options": [
            {"text": "the object itself", "correct": False,
             "why": "That is only true for something that floats, and it is "
                    "the result rather than the rule."},
            {"text": "the liquid the object pushes out of the way",
             "correct": True},
            {"text": "all of the liquid in the whole container", "correct": False,
             "why": "A tiny cork in a huge tank does not feel the whole "
                    "tank's weight."},
            {"text": "the liquid directly above the object", "correct": False,
             "why": "A floating object has almost nothing above it, and still "
                    "gets upthrust."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e11",
        "band": "easier",
        "text": "For an object floating at rest, the upthrust is…",
        "options": [
            {"text": "larger than its weight, which is why it stays up",
             "correct": False,
             "why": "A larger upthrust would push it further out of the "
                    "water; at rest the two match."},
            {"text": "smaller than its weight, but only just", "correct": False,
             "why": "A smaller upthrust leaves a downward resultant, and it "
                    "would sink."},
            {"text": "equal to its weight", "correct": True},
            {"text": "zero, because nothing is moving", "correct": False,
             "why": "Nothing moving means the forces balance, and one of "
                    "those forces is the upthrust."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e12",
        "band": "easier",
        "text": "A cork is held under water and then released. What happens, "
                "and why?",
        "options": [
            {"text": "It stays where it is, because the forces balance",
             "correct": False,
             "why": "They do not balance under water: the upthrust on a "
                    "submerged cork beats its weight."},
            {"text": "It sinks, because it has been pushed down",
             "correct": False,
             "why": "Being pushed down does not leave a force in it; once "
                    "released the upthrust wins."},
            {"text": "It rises, because the upthrust is bigger than its "
                     "weight",
             "correct": True},
            {"text": "It rises, because water pushes everything upwards "
                     "equally",
             "correct": False,
             "why": "Water pushes up on a stone too, and the stone still "
                    "sinks."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e13",
        "band": "easier",
        "text": "Does upthrust act in air as well as in liquids?",
        "options": [
            {"text": "No — air is too thin to push anything up",
             "correct": False,
             "why": "A helium balloon rises on exactly this force, so air "
                    "certainly can."},
            {"text": "Yes, and it is what lifts a balloon", "correct": True},
            {"text": "No — air has no weight, so it displaces nothing",
             "correct": False,
             "why": "Air has weight, which is why atmospheric pressure "
                    "exists."},
            {"text": "Yes, but only on objects that are already moving",
             "correct": False,
             "why": "A balloon resting against a ceiling is held there by "
                    "upthrust without moving."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-03-s05",
        "band": "standard",
        "text": "A crown weighs 50 N in air and 45 N fully under water. What "
                "is the upthrust, and what does the displaced water weigh?",
        "options": [
            {"text": "5 N of upthrust, and 5 N of displaced water",
             "correct": True},
            {"text": "5 N of upthrust, and 45 N of displaced water",
             "correct": False,
             "why": "45 N is the crown's reading in water. The displaced "
                    "water weighs exactly what the upthrust is."},
            {"text": "45 N of upthrust, and 50 N of displaced water",
             "correct": False,
             "why": "Upthrust is the DIFFERENCE between the two readings, not "
                    "the smaller one."},
            {"text": "95 N of upthrust, and 95 N of displaced water",
             "correct": False,
             "why": "That adds the readings; the upthrust cannot exceed the "
                    "crown's own weight here."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s06",
        "band": "standard",
        "text": "Two blocks of the same size, one aluminium and one lead, are "
                "held completely under water. Which gets more upthrust?",
        "options": [
            {"text": "The lead, because it is heavier", "correct": False,
             "why": "Upthrust does not depend on the object's weight, only on "
                    "the water it pushes aside."},
            {"text": "The aluminium, because it is much lighter than the lead "
                     "block", "correct": False,
             "why": "Being lighter makes it easier to float, but the upthrust "
                    "itself is the same."},
            {"text": "The same, because they displace the same volume",
             "correct": True},
            {"text": "The lead, because it sinks faster", "correct": False,
             "why": "How fast it sinks follows from the weight, and it does "
                    "not change the upthrust."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s07",
        "band": "standard",
        "text": "A ship sails from the sea into a fresh-water river and sits "
                "lower in the water. Why?",
        "options": [
            {"text": "Because fresh water is less dense, so more must be "
                     "pushed aside",
             "correct": True},
            {"text": "Because the ship becomes heavier once it is in fresh "
                     "water",
             "correct": False,
             "why": "Its weight is unchanged; the water around it is what has "
                    "changed."},
            {"text": "Because a river is shallower than the sea",
             "correct": False,
             "why": "Depth does not affect how high a ship floats, as long as "
                    "it is not aground."},
            {"text": "Because fresh water gives no upthrust at all",
             "correct": False,
             "why": "It gives plenty — just a little less for each cubic "
                    "metre displaced."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s08",
        "band": "standard",
        "text": "A helium balloon rises through the air. Which statement is "
                "right?",
        "options": [
            {"text": "The upthrust on it is larger than its weight",
             "correct": True},
            {"text": "Helium has no weight, so nothing pulls it down",
             "correct": False,
             "why": "Helium has weight; it is simply far lighter than the air "
                    "it displaces."},
            {"text": "The balloon is pulled upwards by the sky",
             "correct": False,
             "why": "Nothing pulls from above. The surrounding air pushes it "
                    "up from below."},
            {"text": "Gravity does not act on gases", "correct": False,
             "why": "It acts on every mass, which is why the atmosphere has "
                    "weight at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s09",
        "band": "standard",
        "text": "A block floats with nine tenths of its volume below the "
                "surface. What does that tell you?",
        "options": [
            {"text": "That nine tenths of its weight is supported and the "
                     "rest is not",
             "correct": False,
             "why": "All of its weight is supported — that is what floating "
                    "at rest means."},
            {"text": "That the water it pushes aside weighs the same as the "
                     "whole block",
             "correct": True},
            {"text": "That the block is nine times as heavy as the water",
             "correct": False,
             "why": "It is LESS dense than the water, which is why it floats "
                    "at all."},
            {"text": "That one tenth of the block is hollow", "correct": False,
             "why": "Nothing needs to be hollow; a solid block less dense "
                    "than water floats too."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s10",
        "band": "standard",
        "text": "Cargo is loaded into a floating boat. What happens to the "
                "water it pushes out of the way?",
        "options": [
            {"text": "It stays the same, because the boat is the same shape",
             "correct": False,
             "why": "The boat sits lower, so more of its hull is under water "
                    "and more is displaced."},
            {"text": "It decreases, because the boat is pressed down harder",
             "correct": False,
             "why": "Sitting lower means pushing MORE water aside, not less."},
            {"text": "It increases, because the upthrust must match the new "
                     "weight",
             "correct": True},
            {"text": "It stays the same until the boat is full",
             "correct": False,
             "why": "Every kilogram added sinks the boat a little further and "
                    "displaces a little more."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s11",
        "band": "standard",
        "text": "A hollow plastic ball is held completely under water by a "
                "hand. What must the hand be doing?",
        "options": [
            {"text": "Pushing down with the difference between the upthrust "
                     "and the ball's weight",
             "correct": True},
            {"text": "Holding still, because the forces on the ball balance "
                     "by themselves",
             "correct": False,
             "why": "If they balanced it would stay put on its own, and it "
                    "does not."},
            {"text": "Pushing down with the whole upthrust", "correct": False,
             "why": "The ball's own weight already opposes some of the "
                    "upthrust, so the hand supplies only the rest."},
            {"text": "Pulling upwards, to stop it sinking", "correct": False,
             "why": "A ball that would rise on its own does not need holding "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s12",
        "band": "standard",
        "text": "A stone is weighed hanging in water and then in oil, which "
                "is less dense. Where is the balance reading larger?",
        "options": [
            {"text": "In water, because water is thicker", "correct": False,
             "why": "Denser water gives MORE upthrust, so the reading there "
                    "is smaller."},
            {"text": "In oil, because it gives less upthrust", "correct": True},
            {"text": "The same in both, because the stone is unchanged",
             "correct": False,
             "why": "The stone is unchanged, but the upthrust depends on the "
                    "liquid around it."},
            {"text": "In oil, because oil is slippery", "correct": False,
             "why": "Right answer, wrong reason: it is the density of the "
                    "liquid that decides."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s13",
        "band": "standard",
        "text": "Why does a swimmer float more easily in the Dead Sea than in "
                "a freshwater lake?",
        "options": [
            {"text": "Because the water is warmer, so the swimmer relaxes",
             "correct": False,
             "why": "Comfort is not the physics; the density of the water "
                    "is."},
            {"text": "Because very salty water is denser, so less of them "
                     "needs to be under",
             "correct": True},
            {"text": "Because salt water gives no upthrust, so nothing pushes "
                     "them down",
             "correct": False,
             "why": "It gives MORE upthrust than fresh water, which is "
                    "exactly why floating is easier."},
            {"text": "Because a swimmer weighs less in salt water",
             "correct": False,
             "why": "Their weight is unchanged; the upward push on them has "
                    "increased."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-03-h05",
        "band": "harder",
        "text": "A block weighs 60 N in air, 45 N in water and 38 N in a "
                "denser liquid. Which upthrust is larger, and by how much?",
        "options": [
            {"text": "The water's, at 45 N against 38 N", "correct": False,
             "why": "Those are the balance readings, not the upthrusts; the "
                    "upthrust is the difference from 60 N."},
            {"text": "The denser liquid's, at 22 N against 15 N",
             "correct": True},
            {"text": "The water's, at 15 N against 22 N", "correct": False,
             "why": "The figures are right but attached the wrong way round: "
                    "the smaller reading means the larger upthrust."},
            {"text": "They are equal, because it is the same block",
             "correct": False,
             "why": "The same block displaces the same volume, but a denser "
                    "liquid weighs more for that volume."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h06",
        "band": "harder",
        "text": "A boat floating on a pond carries a heavy stone. The stone "
                "is thrown overboard and sinks. What happens to the pond's "
                "level?",
        "options": [
            {"text": "It rises, because the stone is now in the water",
             "correct": False,
             "why": "It was already displacing water — by its whole weight — "
                    "while it sat in the boat."},
            {"text": "It stays the same, because nothing has left the pond",
             "correct": False,
             "why": "Nothing has left, but the stone now displaces its VOLUME "
                    "rather than its weight."},
            {"text": "It falls, because the stone now displaces only its own "
                     "volume",
             "correct": True},
            {"text": "It falls, because the boat rises out of the water",
             "correct": False,
             "why": "The boat does rise, and that is half the story — the "
                    "other half is what the sunk stone now displaces."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h07",
        "band": "harder",
        "text": "A solid block is six tenths as dense as water. What fraction "
                "of it sits below the surface when it floats?",
        "options": [
            {"text": "Four tenths", "correct": False,
             "why": "That is the fraction ABOVE the surface, which is what is "
                    "left over."},
            {"text": "All of it, because it is solid", "correct": False,
             "why": "Being solid is irrelevant; anything less dense than "
                    "water floats partly above it."},
            {"text": "Six tenths", "correct": True},
            {"text": "It cannot be told without knowing the block's size",
             "correct": False,
             "why": "The fraction is set by the two densities and is the same "
                    "whatever the size."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h08",
        "band": "harder",
        "text": "A sealed rigid bottle is held 2 m under water, then 10 m "
                "under. What happens to the upthrust on it?",
        "options": [
            {"text": "It rises, because the pressure down there is greater",
             "correct": False,
             "why": "The pressure on both top and bottom rises, and the "
                    "DIFFERENCE between them is what matters."},
            {"text": "It stays the same, because it displaces the same volume",
             "correct": True},
            {"text": "It falls, because the water above is squashing it",
             "correct": False,
             "why": "The bottle is rigid, so it displaces the same volume at "
                    "either depth."},
            {"text": "It falls to zero once it is deep enough",
             "correct": False,
             "why": "Upthrust does not run out with depth; the difference in "
                    "pressure across the bottle is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h09",
        "band": "harder",
        "text": "A diver puts on a weight belt so they neither rise nor sink. "
                "Explain what the belt has done.",
        "options": [
            {"text": "It has reduced the upthrust on the diver",
             "correct": False,
             "why": "The belt is small, so the volume displaced barely "
                    "changes; the weight is what has moved."},
            {"text": "It has raised the diver's weight until it matches the "
                     "upthrust",
             "correct": True},
            {"text": "It has made the diver denser than water, so they hang "
                     "still",
             "correct": False,
             "why": "Denser than water means sinking. Hanging still needs the "
                    "two to be equal."},
            {"text": "It has cancelled the upthrust, leaving no forces at all",
             "correct": False,
             "why": "Both forces are still there and still large; they now "
                    "balance rather than vanish."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h10",
        "band": "harder",
        "text": "A ship is unloaded at a dock. What happens to the upthrust "
                "on it?",
        "options": [
            {"text": "It stays the same, because the ship is the same ship",
             "correct": False,
             "why": "The upthrust always matches the weight of a floating "
                    "object, and the weight has fallen."},
            {"text": "It rises, because the ship floats higher", "correct": False,
             "why": "Floating higher means displacing LESS water, so the "
                    "upthrust falls."},
            {"text": "It falls, because it floats higher and displaces less "
                     "water",
             "correct": True},
            {"text": "It falls to zero once the ship is completely empty",
             "correct": False,
             "why": "An empty hull still weighs a great deal and still needs "
                    "an upthrust to match it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h11",
        "band": "harder",
        "text": "Why does the upthrust on a submerged object not depend on "
                "how heavy the object is?",
        "options": [
            {"text": "Because heavy objects sink, and sinking objects get no "
                     "upthrust",
             "correct": False,
             "why": "They do get upthrust; that is why a rock feels lighter "
                    "under water."},
            {"text": "Because it equals the weight of liquid pushed aside, "
                     "set by volume",
             "correct": True},
            {"text": "Because the liquid cannot tell how heavy the object is",
             "correct": False,
             "why": "True as far as it goes, but it does not say what the "
                    "upthrust DOES depend on."},
            {"text": "Because upthrust always equals the object's own weight",
             "correct": False,
             "why": "That holds only for something floating; a sinking object "
                    "gets less."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h12",
        "band": "harder",
        "text": "A steel block of volume 2 litres weighs 156 N. One litre of "
                "water weighs 10 N. Will it float?",
        "options": [
            {"text": "Yes, because steel ships float", "correct": False,
             "why": "A ship encloses a great deal of air; this solid block "
                    "displaces only its own two litres."},
            {"text": "No — the upthrust is only 20 N against a weight of "
                     "156 N",
             "correct": True},
            {"text": "No — the upthrust is 10 N against a weight of 156 N",
             "correct": False,
             "why": "10 N is one litre's worth, and the block displaces two "
                    "litres."},
            {"text": "It cannot be decided without knowing the depth",
             "correct": False,
             "why": "Depth does not change the upthrust on a fully submerged "
                    "rigid block."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h13",
        "band": "harder",
        "text": "An iceberg floats with about one ninth of its volume above "
                "the surface. What does that say about the two densities?",
        "options": [
            {"text": "That ice is nine times as dense as sea water",
             "correct": False,
             "why": "Nine times denser would sink at once. Ice is the LESS "
                    "dense of the two."},
            {"text": "That ice is about eight ninths as dense as sea water",
             "correct": True},
            {"text": "That ice is one ninth as dense as sea water",
             "correct": False,
             "why": "That would leave only a ninth submerged, not eight "
                    "ninths of it."},
            {"text": "That the two have the same density, so it just balances",
             "correct": False,
             "why": "Equal densities would leave it fully submerged and "
                    "hanging, with nothing above the surface."},
        ],
        "figure": None,
    },
]
