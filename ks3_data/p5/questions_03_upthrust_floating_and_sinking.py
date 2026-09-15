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
            {"text": "Because the ship becomes heavier the moment it leaves "
                     "the salty water behind it",
             "correct": False,
             "why": "Its weight is unchanged; the water around it is what "
                    "has changed."},
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
            {"text": "It stays the same, because a stone displaces the same "
                     "water wherever it is",
             "correct": False,
             "why": "In the boat it displaced its own WEIGHT of water; on "
                    "the bottom it displaces only its own volume."},
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
            {"text": "It stays the same, because the upthrust is fixed by "
                     "the size of the hull itself",
             "correct": False,
             "why": "Upthrust matches the weight of a floating object, and "
                    "the weight has fallen, so the hull rides higher and "
                    "displaces less."},
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
            {"text": "Because heavy objects sink, and anything that sinks "
                     "gets no upthrust from the water",
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
            {"text": "It cannot be decided without knowing how deep the "
                     "block is put under the water",
             "correct": False,
             "why": "Depth does not change the upthrust on a fully "
                    "submerged rigid block."},
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

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-03-e14",
        "band": "easier",
        "text": "A solid object floats in water when its density is…",
        "options": [
            {"text": "greater than the water's", "correct": False,
             "why": "Denser than water means its own volume of water weighs "
                    "less than it does, so it goes down."},
            {"text": "less than the water's", "correct": True},
            {"text": "exactly the same as the water's", "correct": False,
             "why": "Matching densities leave it hanging fully under the "
                    "surface rather than floating on it."},
            {"text": "greater than the air's", "correct": False,
             "why": "Almost everything is denser than air, including the "
                    "things that sink."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e15",
        "band": "easier",
        "text": "Which two forces act on a boat floating at rest?",
        "options": [
            {"text": "Its weight downwards and friction upwards",
             "correct": False,
             "why": "Friction acts along a surface, and it is not what holds "
                    "a boat up."},
            {"text": "Upthrust upwards and air resistance downwards",
             "correct": False,
             "why": "Air resistance acts on something moving through air, and "
                    "the boat's weight has been left out."},
            {"text": "Its weight downwards and the pressure of the water "
                     "sideways", "correct": False,
             "why": "The sideways pushes on a hull cancel each other; what is "
                    "left over acts upwards."},
            {"text": "Its weight downwards and the upthrust upwards",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e16",
        "band": "easier",
        "text": "One-litre blocks of steel, aluminium, ice and lead are "
                "dropped into water. Which one floats?",
        "options": [
            {"text": "Steel", "correct": False,
             "why": "A litre of steel weighs about 79 N against the 10 N its "
                    "litre of water weighs, so it sinks."},
            {"text": "Lead", "correct": False,
             "why": "Lead is heavier still for its size than steel, so it "
                    "sinks faster rather than floating."},
            {"text": "Ice", "correct": True},
            {"text": "Aluminium", "correct": False,
             "why": "A litre of aluminium weighs about 27 N, well over the "
                    "10 N of water it pushes aside."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e17",
        "band": "easier",
        "text": "The liquid an object pushes out of the way is said to have "
                "been…",
        "options": [
            {"text": "displaced", "correct": True},
            {"text": "dissolved", "correct": False,
             "why": "Dissolving mixes one substance into another; the water "
                    "here is simply shoved aside."},
            {"text": "compressed", "correct": False,
             "why": "A liquid is very hard to squash, and it moves out of the "
                    "way rather than shrinking."},
            {"text": "evaporated", "correct": False,
             "why": "Evaporating turns a liquid into a gas, which is not what "
                    "a block lowered into water does to it."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-03-s14",
        "band": "standard",
        "text": "Two objects weigh exactly the same, but one takes up twice "
                "the volume. Both are held fully under water. Which gets more "
                "upthrust?",
        "options": [
            {"text": "Neither, because their weights match", "correct": False,
             "why": "Weight is not what upthrust is measured from; the volume "
                    "pushed aside is."},
            {"text": "The smaller one, because it is packed tighter",
             "correct": False,
             "why": "Being tightly packed means pushing aside less water, "
                    "which gives less upthrust."},
            {"text": "The one with twice the volume", "correct": True},
            {"text": "Whichever is nearer the bottom of the tank",
             "correct": False,
             "why": "Depth makes no difference once an object is fully under "
                    "the surface."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s15",
        "band": "standard",
        "text": "A ball floating on water is pushed steadily downwards, but "
                "is not yet fully under. What happens to the upthrust on it?",
        "options": [
            {"text": "It grows, because more water is being pushed aside",
             "correct": True},
            {"text": "It stays the same, because the ball has not changed",
             "correct": False,
             "why": "The ball is unchanged, and how much of it is under the "
                    "surface is not."},
            {"text": "It falls, because the water above starts pressing down "
                     "on it", "correct": False,
             "why": "The push on the top is already counted; the difference "
                    "across the ball still grows."},
            {"text": "It falls, because the ball is being forced out of its "
                     "resting place", "correct": False,
             "why": "Being forced under is what makes the upthrust rise, "
                    "which is why the ball fights back."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s16",
        "band": "standard",
        "text": "A fish lets gas expand a bladder inside its body and begins "
                "to rise. Why does that work?",
        "options": [
            {"text": "The gas is lighter than water, and light things are "
                     "pulled upwards", "correct": False,
             "why": "Nothing pulls upwards. The fish rises because the "
                    "upthrust on it now beats its weight."},
            {"text": "Its volume rises while its weight hardly does, so the "
                     "upthrust rises", "correct": True},
            {"text": "The gas pushes on the water below the fish and drives "
                     "it upwards", "correct": False,
             "why": "The bladder is sealed inside the fish and pushes on "
                    "nothing outside it."},
            {"text": "Gas inside a body cancels out part of that body's "
                     "weight", "correct": False,
             "why": "The weight is barely changed. What has changed is how "
                    "much water is pushed aside."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s17",
        "band": "standard",
        "text": "A sealed box shoves 7 litres of water aside when it is held "
                "under. One litre of water weighs 10 N. What upthrust acts on "
                "the box?",
        "options": [
            {"text": "10 N", "correct": False,
             "why": "10 N is one litre's worth, and seven litres have been "
                    "pushed aside."},
            {"text": "7 N", "correct": False,
             "why": "That reads the volume in litres as though it were a "
                    "force in newtons."},
            {"text": "0.7 N", "correct": False,
             "why": "That divides the litres by the weight, where the two "
                    "should be multiplied."},
            {"text": "70 N", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-03-h14",
        "band": "harder",
        "text": "A sealed object is made to have exactly the same density as "
                "the water it is placed in. What does it do?",
        "options": [
            {"text": "It hangs wherever it is put, neither rising nor "
                     "sinking", "correct": True},
            {"text": "It floats with about half of it above the surface",
             "correct": False,
             "why": "Half out would push aside only half its own volume, "
                    "giving half the upthrust it needs."},
            {"text": "It sinks slowly, because matching densities cancel the "
                     "upthrust", "correct": False,
             "why": "The upthrust is at its full value and matches the "
                    "weight, so nothing is left over to move it."},
            {"text": "It rises slowly, because water always pushes an object "
                     "towards the surface", "correct": False,
             "why": "Water pushes up on a stone too, and the stone goes down "
                    "all the same."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h15",
        "band": "harder",
        "text": "A block of volume 5 litres weighs 30 N. One litre of water "
                "weighs 10 N. What does the block do in water?",
        "options": [
            {"text": "It sinks, because 30 N is heavier than a litre of "
                     "water", "correct": False,
             "why": "The comparison is with the five litres it can push "
                    "aside, which come to 50 N."},
            {"text": "It floats, with all 5 litres just under the surface",
             "correct": False,
             "why": "Fully under it would get 50 N of upthrust against 30 N "
                    "of weight, and 20 N would push it back up."},
            {"text": "It hangs fully under the surface without moving",
             "correct": False,
             "why": "Hanging still needs the two forces to match, and here "
                    "the upthrust would beat the weight."},
            {"text": "It floats, with 3 litres below the surface",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h16",
        "band": "harder",
        "text": "A glass is filled to the brim with water and a lump of ice "
                "floats in it. The ice melts without being touched. What "
                "happens to the water level?",
        "options": [
            {"text": "It rises, and the glass overflows", "correct": False,
             "why": "The melted ice takes up exactly the room the floating "
                    "lump was already making for itself."},
            {"text": "It stays where it was", "correct": True},
            {"text": "It falls, because ice shrinks as it turns into water",
             "correct": False,
             "why": "Only the part standing above the surface was taking up "
                    "extra room, and that part was displacing nothing."},
            {"text": "It rises at first and then falls back below its "
                     "starting point", "correct": False,
             "why": "There is no stage at which the level moves; the melting "
                    "lump replaces its own displacement as it goes."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h17",
        "band": "harder",
        "text": "A sealed hollow steel ball with thick walls sinks. A student "
                "says hollow things always float. What is the right rule?",
        "options": [
            {"text": "Hollow things float when the trapped air is heavier "
                     "than the shell around it", "correct": False,
             "why": "Air is far lighter than steel, so this could not "
                    "describe any hollow object at all."},
            {"text": "Hollow things sink whenever they are sealed, because no "
                     "water can get in", "correct": False,
             "why": "A sealed plastic bottle floats perfectly well, so "
                    "sealing is not what decides it."},
            {"text": "Being hollow helps only when it makes the object push "
                     "aside more water than it weighs", "correct": True},
            {"text": "Hollow things float when their walls are thinner than "
                     "the water around them", "correct": False,
             "why": "Water has no thickness to compare a wall with, so the "
                    "rule cannot be applied to anything."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · easier ─────────────────────────────
    {
        "id": "p5-03-e18",
        "band": "easier",
        "text": "A block weighs 40 N in air and gets 9 N of upthrust under "
                "water. What does a spring balance read while it hangs "
                "there?",
        "options": [
            {"text": "31 N", "correct": True},
            {"text": "49 N", "correct": False,
             "why": "That adds the upthrust on. Upthrust takes weight off a "
                    "balance rather than putting it on."},
            {"text": "9 N", "correct": False,
             "why": "That is the upthrust itself, not what is left for the "
                    "balance to carry."},
            {"text": "40 N", "correct": False,
             "why": "That is the reading in air, before the water started "
                    "helping to hold the block up."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e19",
        "band": "easier",
        "text": "Who first worked out that the upthrust equals the weight of "
                "the fluid pushed out of the way?",
        "options": [
            {"text": "Newton", "correct": False,
             "why": "Newton's work on forces came about two thousand years "
                    "later."},
            {"text": "Archimedes", "correct": True},
            {"text": "Torricelli", "correct": False,
             "why": "Torricelli's work was on the pressure of the air, not on "
                    "floating."},
            {"text": "Pascal", "correct": False,
             "why": "Pascal has the unit of pressure named after him, and the "
                    "floating rule is not his."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e20",
        "band": "easier",
        "text": "A small block of pine floats. Would a block of the same pine "
                "ten times as large float too?",
        "options": [
            {"text": "No — a bigger block is far heavier", "correct": False,
             "why": "It is heavier, and it pushes aside ten times as much "
                    "water as well, so the two grow together."},
            {"text": "No — only small things can float", "correct": False,
             "why": "Ships weigh millions of newtons and float perfectly "
                    "well."},
            {"text": "Yes — floating depends on the wood, not the size",
             "correct": True},
            {"text": "Yes — but only if it is hollowed out first",
             "correct": False,
             "why": "Solid pine floats as it is; hollowing it would only make "
                    "it float higher."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e21",
        "band": "easier",
        "text": "A block floating at rest weighs 12 N. What does the water it "
                "pushes out of the way weigh?",
        "options": [
            {"text": "More than 12 N", "correct": False,
             "why": "A bigger upthrust than the weight would push the block "
                    "further out of the water until the two matched."},
            {"text": "Less than 12 N", "correct": False,
             "why": "A smaller upthrust would leave a force downwards and the "
                    "block would sink lower."},
            {"text": "It cannot be told without the block's volume",
             "correct": False,
             "why": "The volume decides how deep it floats, not the weight of "
                    "water it ends up displacing."},
            {"text": "12 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e22",
        "band": "easier",
        "text": "Which change would make an object more likely to float?",
        "options": [
            {"text": "Giving it a bigger volume for the same weight",
             "correct": True},
            {"text": "Giving it a smaller volume for the same weight",
             "correct": False,
             "why": "A smaller volume pushes aside less water, so the "
                    "upthrust falls."},
            {"text": "Making it heavier without changing its volume",
             "correct": False,
             "why": "The upthrust would be unchanged while the weight rose, "
                    "which is the wrong way round."},
            {"text": "Painting it with something waterproof", "correct": False,
             "why": "Paint changes neither the weight nor the volume enough "
                    "to matter."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e23",
        "band": "easier",
        "text": "A person standing in a swimming pool feels lighter than they "
                "do on the poolside. What is doing that?",
        "options": [
            {"text": "The water has made them weigh less", "correct": False,
             "why": "Their weight is the same in or out of the pool; "
                    "something else is now helping to carry it."},
            {"text": "The upthrust from the water", "correct": True},
            {"text": "Gravity is weaker under water", "correct": False,
             "why": "Gravity pulls on them exactly as hard in the pool as on "
                    "the poolside."},
            {"text": "The water is holding them up by friction",
             "correct": False,
             "why": "Friction acts along a surface, and it is not what lifts "
                    "a swimmer."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e24",
        "band": "easier",
        "text": "A small boat with a hole in it slowly sinks. Why?",
        "options": [
            {"text": "The hole lets the upthrust escape", "correct": False,
             "why": "Upthrust is a force, not something that can leak out of "
                    "a hole."},
            {"text": "Holes make a hull weaker, so it gives way", "correct": False,
             "why": "The hull is not being crushed; it is taking on weight."},
            {"text": "Water coming in adds weight until the weight beats the "
                     "upthrust", "correct": True},
            {"text": "Water coming in leaves the hull pushing aside much "
                     "less water than it did before",
             "correct": False,
             "why": "The hull still shoves the same water aside; what has "
                    "changed is how much the boat weighs."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e25",
        "band": "easier",
        "text": "How does the upthrust on a block half under the surface "
                "compare with the upthrust on it fully under?",
        "options": [
            {"text": "Bigger, because more of it is out in the air",
             "correct": False,
             "why": "Air gives almost no upthrust, so the part above the "
                    "surface contributes next to nothing."},
            {"text": "The same, because it is the same block", "correct": False,
             "why": "It is the same block pushing aside different amounts of "
                    "water in the two cases."},
            {"text": "Smaller, because it pushes aside less water",
             "correct": True},
            {"text": "Zero, because it has not gone right under",
             "correct": False,
             "why": "It is displacing water with the half that is under, so "
                    "there is a real upthrust on it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e26",
        "band": "easier",
        "text": "An object hangs from a spring balance in air, well away from "
                "any water. What does the balance read?",
        "options": [
            {"text": "Its full weight", "correct": True},
            {"text": "Nothing, because nothing is holding it up",
             "correct": False,
             "why": "The balance itself is holding it up, and what it reads "
                    "is how hard it has to pull."},
            {"text": "Its weight plus the upthrust from the air",
             "correct": False,
             "why": "Air gives a tiny upthrust, and it takes a little off "
                    "rather than adding on."},
            {"text": "Half its weight, with gravity taking the rest",
             "correct": False,
             "why": "Gravity is what gives the object its weight; it does not "
                    "carry part of it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e27",
        "band": "easier",
        "text": "The upward force a liquid or a gas puts on anything in it is "
                "called…",
        "options": [
            {"text": "weight", "correct": False,
             "why": "Weight is the downward pull of gravity, which upthrust "
                    "works against."},
            {"text": "upthrust", "correct": True},
            {"text": "pressure", "correct": False,
             "why": "Pressure is measured in pascals and is what causes "
                    "upthrust, not the force itself."},
            {"text": "density", "correct": False,
             "why": "Density says how much a substance weighs for its size "
                    "and is not a force at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e28",
        "band": "easier",
        "text": "Why does a ship sit lower in the water once its cargo is "
                "loaded?",
        "options": [
            {"text": "Because the extra weight squashes the hull flatter",
             "correct": False,
             "why": "A steel hull keeps its shape; what changes is how deep "
                    "it settles."},
            {"text": "Because loading pushes the water out from under it",
             "correct": False,
             "why": "Water is not driven away; the hull simply sinks further "
                    "into it."},
            {"text": "Because the sea gives a heavy ship less upthrust than "
                     "it gives a light one",
             "correct": False,
             "why": "The sea gives more upthrust as the hull goes deeper, "
                    "which is how the ship stays afloat."},
            {"text": "Because it must push aside more water to match its new "
                     "weight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e29",
        "band": "easier",
        "text": "A helium balloon is taken to the Moon and released. What "
                "happens to it?",
        "options": [
            {"text": "It rises, as it would on Earth", "correct": False,
             "why": "Rising needs a surrounding fluid to push it up, and the "
                    "Moon has none."},
            {"text": "It falls, because there is no air to give it upthrust",
             "correct": True},
            {"text": "It floats where it is, because there is nothing to move "
                     "it", "correct": False,
             "why": "Gravity still pulls it down, and nothing is left to push "
                    "it back up."},
            {"text": "It rises faster, because the Moon's gravity is weaker",
             "correct": False,
             "why": "Weaker gravity slows the fall; it does not turn a fall "
                    "into a rise."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e30",
        "band": "easier",
        "text": "Two litres of water weigh 20 N. What upthrust acts on a "
                "two-litre block held completely under the water?",
        "options": [
            {"text": "2 N", "correct": False,
             "why": "That reads the volume in litres as though it were a "
                    "force in newtons."},
            {"text": "10 N", "correct": False,
             "why": "10 N is one litre's worth, and the block pushes aside "
                    "two."},
            {"text": "20 N", "correct": True},
            {"text": "40 N", "correct": False,
             "why": "That doubles again; two litres of water weigh 20 N, not "
                    "40 N."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · standard ───────────────────────────
    {
        "id": "p5-03-s18",
        "band": "standard",
        "text": "A stone gets 4 N of upthrust under water. One litre of water "
                "weighs 10 N. What is the stone's volume?",
        "options": [
            {"text": "4 litres", "correct": False,
             "why": "That reads the upthrust in newtons as a volume in "
                    "litres."},
            {"text": "40 litres", "correct": False,
             "why": "That multiplies where the two figures should be divided, "
                    "giving a stone the size of a bin."},
            {"text": "0.4 litres", "correct": True},
            {"text": "2.5 litres", "correct": False,
             "why": "That is 10 ÷ 4, the division the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s19",
        "band": "standard",
        "text": "Two crowns weigh the same in air, but one gets more upthrust "
                "under water. What does that tell you about them?",
        "options": [
            {"text": "The one with more upthrust takes up more room, so it is "
                     "less dense", "correct": True},
            {"text": "The one with more upthrust is the heavier, because a "
                     "heavier object is pushed up harder",
             "correct": False,
             "why": "They weigh the same in air, which the question states, "
                    "and upthrust is set by the volume pushed aside rather "
                    "than by weight."},
            {"text": "The one with more upthrust is made of a purer metal",
             "correct": False,
             "why": "Purity only matters here through the density, and the "
                    "upthrust points the other way."},
            {"text": "The one with more upthrust was lowered in deeper",
             "correct": False,
             "why": "Depth makes no difference once an object is fully under "
                    "the surface."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s20",
        "band": "standard",
        "text": "A raft weighing 1200 N can push aside 400 litres of water "
                "before its deck goes under. One litre weighs 10 N. What load "
                "can it carry?",
        "options": [
            {"text": "4000 N", "correct": False,
             "why": "That is the whole upthrust available, and the raft's own "
                    "1200 N has already used part of it."},
            {"text": "1200 N", "correct": False,
             "why": "That is the raft's own weight, not what is left over for "
                    "a load."},
            {"text": "5200 N", "correct": False,
             "why": "That adds the raft's weight to the upthrust instead of "
                    "taking it away."},
            {"text": "2800 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s21",
        "band": "standard",
        "text": "A block floats in water and is then floated in oil, which is "
                "less dense. How does the upthrust on it compare?",
        "options": [
            {"text": "The same in both, because it equals the block's weight "
                     "either way", "correct": True},
            {"text": "Less in the oil, because a block cannot push aside as "
                     "much oil as it can water",
             "correct": False,
             "why": "The block simply sinks further into the oil until it "
                    "has pushed aside its own weight again."},
            {"text": "More in the oil, because it sits deeper in it",
             "correct": False,
             "why": "Sitting deeper is how the upthrust is kept the same, not "
                    "how it is made bigger."},
            {"text": "Nothing in the oil, because oil cannot hold things up",
             "correct": False,
             "why": "Plenty of things float on oil, so it clearly gives an "
                    "upthrust."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s22",
        "band": "standard",
        "text": "Cargo is loaded into a boat floating on a small pond. What "
                "happens to the pond's water level?",
        "options": [
            {"text": "It falls, because the boat sits lower", "correct": False,
             "why": "The boat sitting lower is exactly what pushes more water "
                    "out of the way."},
            {"text": "It rises", "correct": True},
            {"text": "It stays the same, because nothing has entered the "
                     "water", "correct": False,
             "why": "The cargo has entered the boat, and the boat must now "
                    "displace more water to carry it."},
            {"text": "It rises and then falls back as the boat settles",
             "correct": False,
             "why": "Once the boat has settled it is displacing more water "
                    "than before, and it stays that way."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s23",
        "band": "standard",
        "text": "A sealed tin full of beans sinks, while an identical sealed "
                "empty tin floats. Why?",
        "options": [
            {"text": "The empty tin is sealed more tightly", "correct": False,
             "why": "Both are sealed, and how tightly makes no difference to "
                    "either weight or volume."},
            {"text": "The empty tin pushes aside more water", "correct": False,
             "why": "The tins are identical in size, so a submerged one would "
                    "push aside exactly as much as the other."},
            {"text": "The full tin has air in it, and air sinks",
             "correct": False,
             "why": "It is the beans rather than air that fills the full tin, "
                    "and air is what helps the empty one float."},
            {"text": "The empty tin weighs far less while displacing the same "
                     "water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s24",
        "band": "standard",
        "text": "A solid block sinks in water but floats in mercury. What does "
                "that say about its density?",
        "options": [
            {"text": "It is lower than water's and lower than mercury's",
             "correct": False,
             "why": "Anything less dense than water floats on it, and this "
                    "block sinks."},
            {"text": "It is higher than water's and lower than mercury's",
             "correct": True},
            {"text": "It is higher than water's and higher than mercury's",
             "correct": False,
             "why": "Anything denser than mercury sinks in it, and this block "
                    "floats."},
            {"text": "It is exactly the same as water's", "correct": False,
             "why": "A block matching water's density hangs in it rather than "
                    "sinking."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s25",
        "band": "standard",
        "text": "A stone hanging from a balance is lowered slowly into water. "
                "What does the reading do?",
        "options": [
            {"text": "It falls steadily until the stone is right under, then "
                     "stops changing", "correct": True},
            {"text": "It falls steadily all the way to the bottom of the "
                     "tank", "correct": False,
             "why": "Once the stone is completely under, going deeper pushes "
                    "aside no more water."},
            {"text": "It drops all at once as the stone touches the surface",
             "correct": False,
             "why": "The upthrust builds as more of the stone goes under, "
                    "rather than arriving in one step."},
            {"text": "It rises, because the water is pressing down on the "
                     "stone", "correct": False,
             "why": "The water pushes harder on the stone's underside than on "
                    "its top, so the balance is relieved, not loaded."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s26",
        "band": "standard",
        "text": "A diver hanging still under water unbuckles their lead weight "
                "belt and lets it go. What happens to the diver?",
        "options": [
            {"text": "They stay where they are, because the belt was not "
                     "holding them", "correct": False,
             "why": "The belt's weight was part of what balanced the "
                    "upthrust, so losing it upsets the balance."},
            {"text": "They sink, because they have let go of something",
             "correct": False,
             "why": "Dropping weight makes a diver lighter, and a lighter "
                    "diver rises."},
            {"text": "They rise, because their weight is now less than the "
                     "upthrust", "correct": True},
            {"text": "They rise, because the upthrust on them has grown",
             "correct": False,
             "why": "The verdict is right and the reason is wrong: the belt "
                    "is small, so the water displaced barely changes."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s27",
        "band": "standard",
        "text": "How could a spring balance and a beaker of water be used to "
                "find the volume of an oddly shaped stone?",
        "options": [
            {"text": "Weigh it in air and under water; the drop in the "
                     "reading gives the weight of water displaced",
             "correct": True},
            {"text": "Weigh it in air and under water; adding the two "
                     "readings together gives the weight of the water "
                     "pushed aside", "correct": False,
             "why": "Adding them gives a force larger than the stone's own "
                    "weight, which cannot be what the water it pushed aside "
                    "weighs."},
            {"text": "Weigh it dry and then wet; the extra weight is the "
                     "water it holds", "correct": False,
             "why": "A stone holds hardly any water on its surface, and that "
                    "says nothing about its volume."},
            {"text": "Weigh it in air and divide by the density of water",
             "correct": False,
             "why": "That would use the stone's own weight where the weight "
                    "of displaced water is wanted."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s28",
        "band": "standard",
        "text": "A ship is holed and one compartment floods. Why does it sit "
                "lower rather than dropping straight to the bottom?",
        "options": [
            {"text": "Because the hull traps air that cannot escape",
             "correct": False,
             "why": "Air does help, and what settles the ship at a new level "
                    "is the extra water the hull pushes aside."},
            {"text": "Because the water coming in makes the ship lighter "
                     "until it has filled the compartment", "correct": False,
             "why": "Water entering makes it heavier, which is why it "
                    "settles lower."},
            {"text": "Because the extra weight is matched by pushing aside "
                     "more water", "correct": True},
            {"text": "Because the sea pushes hardest on a damaged hull",
             "correct": False,
             "why": "The sea does not treat a hole differently; the upthrust "
                    "depends on the water displaced."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s29",
        "band": "standard",
        "text": "A wooden block held under water is released. It rises, "
                "breaks the surface and settles. Why does it stop rising?",
        "options": [
            {"text": "Because the water stops pushing upwards the moment "
                     "any part of the block has broken the surface", "correct": False,
             "why": "The water still pushes on the submerged part; it "
                    "simply pushes exactly enough."},
            {"text": "Because the block gets heavier as it dries",
             "correct": False,
             "why": "Drying takes weight off rather than adding it, and it is "
                    "far too slow to stop the rise."},
            {"text": "Because the air above pushes it back down with an equal "
                     "force", "correct": False,
             "why": "Air gives only a tiny push, nowhere near enough to "
                    "balance a floating block."},
            {"text": "Because it displaces less water as it rises, until the "
                     "upthrust matches its weight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s30",
        "band": "standard",
        "text": "A hot-air balloon's burner is turned up and the balloon "
                "begins to climb. Why?",
        "options": [
            {"text": "The flame pushes downwards and drives the balloon up",
             "correct": False,
             "why": "The burner points into the envelope, and its push is far "
                    "too small to lift a balloon."},
            {"text": "The air inside thins out, so the balloon weighs less "
                     "while displacing the same air", "correct": True},
            {"text": "Hot air is drawn upwards, taking the balloon with it",
             "correct": False,
             "why": "Nothing draws the balloon upwards; the surrounding air "
                    "pushes it up from below."},
            {"text": "Heating makes the envelope bigger, so it displaces more "
                     "air", "correct": False,
             "why": "The envelope is already full and holds its shape, so its "
                    "volume barely changes."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · harder ─────────────────────────────
    {
        "id": "p5-03-h18",
        "band": "harder",
        "text": "An object weighs 90 N in air and 78 N fully under water. One "
                "litre of water weighs 10 N. What is its volume, and is it "
                "denser than water?",
        "options": [
            {"text": "1.2 litres, and yes", "correct": True},
            {"text": "1.2 litres, and no", "correct": False,
             "why": "1.2 litres of water weigh 12 N, and the object weighs "
                    "90 N, so it is far denser."},
            {"text": "7.8 litres, and yes", "correct": False,
             "why": "7.8 comes from the reading in water rather than from the "
                    "12 N drop that measures the upthrust."},
            {"text": "16.8 litres, and no", "correct": False,
             "why": "That adds the two readings; the upthrust is the "
                    "difference between them."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h19",
        "band": "harder",
        "text": "A block floats in water with two thirds of it under the "
                "surface. It is moved into a liquid twice as dense as water. "
                "What fraction is under now?",
        "options": [
            {"text": "Two thirds, because the block has not changed",
             "correct": False,
             "why": "The block is unchanged and the liquid is not, so it "
                    "needs to displace a different volume."},
            {"text": "Four thirds, because the liquid is twice as dense",
             "correct": False,
             "why": "No object can have more than all of it under the "
                    "surface."},
            {"text": "One third", "correct": True},
            {"text": "All of it, because a denser liquid holds it down",
             "correct": False,
             "why": "A denser liquid gives more upthrust, so the block floats "
                    "higher rather than being pulled under."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h20",
        "band": "harder",
        "text": "A stone weighs 60 N in air, 52 N under water and 46 N under "
                "a third liquid. How dense is that liquid compared with "
                "water?",
        "options": [
            {"text": "1.75 times as dense", "correct": True},
            {"text": "0.57 times as dense", "correct": False,
             "why": "That is 8 ÷ 14, the ratio the wrong way up; the bigger "
                    "upthrust belongs to the denser liquid."},
            {"text": "1.13 times as dense", "correct": False,
             "why": "That compares the two balance readings rather than the "
                    "two upthrusts."},
            {"text": "6 times as dense", "correct": False,
             "why": "6 N is the gap between the two upthrusts, which is not "
                    "the same as the ratio between them."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h21",
        "band": "harder",
        "text": "A lump of ice floats in a glass of very salty water and then "
                "melts. What happens to the level?",
        "options": [
            {"text": "It rises, because the melted ice is less dense than the "
                     "salty water it was displacing", "correct": True},
            {"text": "It stays exactly where it was, because the melted ice "
                     "fills exactly the hole it had been sitting in", "correct": False,
             "why": "In fresh water the melted ice fills its own "
                    "displacement exactly; salty water is denser, so the "
                    "meltwater more than fills the gap."},
            {"text": "It falls, because ice takes up more room than water",
             "correct": False,
             "why": "The extra room the ice took up was above the surface, "
                    "where it was displacing nothing."},
            {"text": "It falls, because salt water holds the ice higher",
             "correct": False,
             "why": "It does hold the ice higher, and that is why the melted "
                    "water more than fills the gap left behind."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h22",
        "band": "harder",
        "text": "Two balloons of exactly the same size are released indoors, "
                "one full of helium and one full of air. Explain what each "
                "does.",
        "options": [
            {"text": "Both rise, because a balloon always rises",
             "correct": False,
             "why": "An air-filled balloon drifts down, which is why party "
                    "balloons need helium to stay up."},
            {"text": "The helium one rises because it gets more upthrust than "
                     "the air one", "correct": False,
             "why": "They are the same size, so they displace the same air "
                    "and get the same upthrust."},
            {"text": "Both get the same upthrust; only the helium one weighs "
                     "less than it", "correct": True},
            {"text": "The air one rises, because the air inside matches the "
                     "air outside", "correct": False,
             "why": "Matching would leave it hanging at best, and the skin "
                    "adds weight, so it comes down."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h23",
        "band": "harder",
        "text": "The pressure at 20 m down is ten times the pressure at 2 m. "
                "Why does a submerged block get the same upthrust at both "
                "depths?",
        "options": [
            {"text": "Because the pressure on its top rises by just as much "
                     "as the pressure on its bottom", "correct": True},
            {"text": "Because pressure stops acting on an object once it is "
                     "fully under", "correct": False,
             "why": "The water presses on it hard at both depths, and harder "
                    "at the deeper one."},
            {"text": "Because upthrust comes from the surface of the water "
                     "above rather than from the depth the block has "
                     "reached", "correct": False,
             "why": "It comes from the difference in pressure across the "
                    "object, wherever that object happens to be."},
            {"text": "Because a block displaces less water the deeper it "
                     "goes", "correct": False,
             "why": "A rigid block displaces exactly its own volume at any "
                    "depth."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h24",
        "band": "harder",
        "text": "A solid cube measuring 0.10 m along each edge is held under "
                "water. One cubic metre of water weighs 10 000 N. What "
                "upthrust acts on it?",
        "options": [
            {"text": "10 N", "correct": True},
            {"text": "100 N", "correct": False,
             "why": "That uses a volume of 0.01 m³, which squares the edge "
                    "instead of cubing it."},
            {"text": "1000 N", "correct": False,
             "why": "That uses 0.1 m³, which is the edge length itself rather "
                    "than a volume."},
            {"text": "1 N", "correct": False,
             "why": "That divides once too often; 0.10 m cubed is 0.001 m³, "
                    "which is worth 10 N of water."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h25",
        "band": "harder",
        "text": "A submarine hanging still in the sea sails into a river "
                "mouth, where the water is much fresher. What must the crew "
                "do to hang still again?",
        "options": [
            {"text": "Take on more water, because the upthrust has risen",
             "correct": False,
             "why": "Fresher water weighs less for its size, so the upthrust "
                    "has fallen rather than risen."},
            {"text": "Nothing, because the submarine's weight has not "
                     "changed", "correct": False,
             "why": "Its weight is the same and the upthrust is not, so the "
                    "two no longer balance."},
            {"text": "Pump water out, because the upthrust has fallen",
             "correct": True},
            {"text": "Dive deeper, where the upthrust will be greater",
             "correct": False,
             "why": "Depth does not change the upthrust on a fully submerged "
                    "hull."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h26",
        "band": "harder",
        "text": "Why must a ship built to carry 8000 tonnes have a hull far "
                "bigger than the cargo it holds?",
        "options": [
            {"text": "Because cargo has to be stacked loosely so that air can "
                     "reach it", "correct": False,
             "why": "How cargo is stowed is a separate matter and is not what "
                    "sets the hull's size."},
            {"text": "Because a bigger hull is stronger, and strength is what "
                     "keeps a ship up", "correct": False,
             "why": "Strength keeps a hull from breaking; what keeps it up is "
                    "the water it pushes aside."},
            {"text": "Because the hull must push aside a weight of water "
                     "equal to the ship and its cargo together",
             "correct": True},
            {"text": "Because water pushes back harder on a larger surface, "
                     "whatever is inside it", "correct": False,
             "why": "It is the volume displaced that sets the upthrust, not "
                    "the amount of surface on show."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h27",
        "band": "harder",
        "text": "A sealed gas-filled balloon is taken deep enough for the "
                "water to squeeze it to half its volume. What happens to the "
                "upthrust on it?",
        "options": [
            {"text": "It stays the same, because the gas inside still weighs "
                     "what it did", "correct": False,
             "why": "Upthrust follows the volume displaced, not the weight of "
                    "what is inside."},
            {"text": "It doubles, because the gas is packed tighter",
             "correct": False,
             "why": "Packing the gas tighter shrinks the balloon, so it "
                    "shoves less water aside."},
            {"text": "It halves", "correct": True},
            {"text": "It stays the same, because a rigid object gets the same "
                     "upthrust at any depth", "correct": False,
             "why": "That holds for a rigid object, and this balloon is one "
                    "that changes size."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h28",
        "band": "harder",
        "text": "A student insists a sinking object gets no upthrust at all. "
                "Which measurement would settle it?",
        "options": [
            {"text": "Timing how long the object takes to reach the bottom",
             "correct": False,
             "why": "A sinking time depends on drag and shape as well, so it "
                    "settles nothing on its own."},
            {"text": "Weighing the object on a balance in air and again while "
                     "it hangs under water", "correct": True},
            {"text": "Weighing the whole tank of water before the object "
                     "goes in and again once it is resting on the bottom", "correct": False,
             "why": "The tank gains the object's weight either way, which "
                    "says nothing about the push on the object."},
            {"text": "Measuring how deep the object ends up in the tank",
             "correct": False,
             "why": "Any sinker ends up on the bottom, whatever upthrust it "
                    "is getting on the way."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h29",
        "band": "harder",
        "text": "A crew lower a heavy anchor on a rope so that it hangs in "
                "the water without touching the bottom. What happens to how "
                "deep the boat floats?",
        "options": [
            {"text": "It floats higher, because the anchor is now in the "
                     "water", "correct": False,
             "why": "The rope still hands the anchor's weight, less its own "
                    "upthrust, back to the boat."},
            {"text": "It floats lower, because the rope pulls the boat down",
             "correct": False,
             "why": "The anchor was already on board, so nothing new is "
                    "pulling on the boat."},
            {"text": "It floats a little higher, by the upthrust the water "
                     "gives the anchor", "correct": True},
            {"text": "It stays at exactly the same level", "correct": False,
             "why": "The water now carries part of the anchor's weight, so "
                    "the boat has a little less to support."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h30",
        "band": "harder",
        "text": "Two identical sealed tins go into water: the empty one "
                "floats and the sand-filled one sinks. Compare the upthrust "
                "on each once both have settled.",
        "options": [
            {"text": "The same on both, because the tins are identical",
             "correct": False,
             "why": "They are the same size, and only the sunk one has all of "
                    "that size under the surface."},
            {"text": "Greater on the floating tin, because floating needs "
                     "more support", "correct": False,
             "why": "The floating tin needs only enough upthrust to match its "
                    "small weight, so it barely dips in."},
            {"text": "Greater on the sunk tin, because all of it is under and "
                     "pushing water aside", "correct": True},
            {"text": "Zero on the sunk tin, since it failed to stay up",
             "correct": False,
             "why": "It gets the full upthrust of a whole tin's volume; that "
                    "is simply less than the sand makes it weigh."},
        ],
        "figure": None,
    },
]
