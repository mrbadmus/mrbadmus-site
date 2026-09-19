"""P4 lesson 04 — What forces do to motion: twelve questions (MRB-223).

Written against Design's page. The curling stone, the trolley and gates
and the four cards are hers.

The discriminations, in the order the lesson builds them:

  · moving needs NO force; changing motion does (`FORCE-24`);
  · a force against the motion is what slowing down IS;
  · a force ACROSS the motion bends the path and keeps the rest
    (`FORCE-25`) — the harder band sits here and on the orbit;
  · the force does not switch off when the object stops (`FORCE-26`);
  · a force is not a supply that drains (`FORCE-27`).

⚠️ POSITION IS AUTHORED — index cycles 0, 1, 2, 3, giving three of each.

⚠️ Rung 1 (the freewheeling cyclist) and Rung 2 (the ball at the top of a
throw) are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "what-forces-do-to-motion"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-04-e01",
        "band": "easier",
        "text": "A resultant force can do all of these EXCEPT one. Which?",
        "options": [
            {"text": "Keep something moving at a steady speed with no change "
                     "at all", "correct": True},
            {"text": "Speed something up", "correct": False,
             "why": "That is one of the three. A resultant in the direction "
                    "of travel makes it faster."},
            {"text": "Slow something down", "correct": False,
             "why": "That is one of the three. A resultant against the "
                    "motion makes it slower."},
            {"text": "Change the direction something is going, and nothing "
                     "else about its motion",
             "correct": False,
             "why": "That is one of the three. A resultant across the motion "
                    "bends the path."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e02",
        "band": "easier",
        "text": "A trolley moving at 2 m/s has a resultant force of 0 N on "
                "it. One second later it is travelling at…",
        "options": [
            {"text": "0 m/s", "correct": False,
             "why": "Stopping is a change, and a change needs something left "
                    "over. Nothing is."},
            {"text": "2 m/s", "correct": True},
            {"text": "4 m/s", "correct": False,
             "why": "Speeding up is a change too. With 0 N left over nothing "
                    "about the motion changes."},
            {"text": "1 m/s", "correct": False,
             "why": "Slowing needs a resultant against the motion, and there "
                    "is none."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e03",
        "band": "easier",
        "text": "A curling stone slides across smooth ice with nothing "
                "touching it. Why does it keep going?",
        "options": [
            {"text": "The ice pushes it forwards.", "correct": False,
             "why": "The ice rubs backwards very slightly. Nothing pushes it "
                    "along."},
            {"text": "The push it was given is still inside it.",
             "correct": False,
             "why": "A force is not stuff and cannot be stored. The push "
                    "ended when the hand let go."},
            {"text": "Nothing is stopping it, and moving needs no force.",
             "correct": True},
            {"text": "It is heavy enough to keep itself moving.",
             "correct": False,
             "why": "Being heavy changes how much a force alters the motion, "
                    "not whether motion needs a force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e04",
        "band": "easier",
        "text": "A car is speeding up. What must be true?",
        "options": [
            {"text": "The forces on it are balanced.", "correct": False,
             "why": "Balanced forces mean no change. Speeding up is a "
                    "change."},
            {"text": "Only the engine is acting on it.", "correct": False,
             "why": "Air resistance and friction are acting too. What "
                    "matters is what is LEFT OVER."},
            {"text": "There are no backwards forces at all.",
             "correct": False,
             "why": "There always are. The forward force is simply bigger "
                    "than they are."},
            {"text": "There is a resultant force forwards.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-04-s01",
        "band": "standard",
        "text": "A trolley travelling right has a resultant force pushing "
                "left for long enough. What happens?",
        "options": [
            {"text": "It slows, stops, and then starts moving left.",
             "correct": True},
            {"text": "It slows, stops, and stays stopped.", "correct": False,
             "why": "Nothing switches off when it reaches zero. The force is "
                    "still acting, so the motion keeps changing."},
            {"text": "It carries on right but more slowly for ever.",
             "correct": False,
             "why": "A steady backwards resultant keeps changing the motion "
                    "until it has reversed it."},
            {"text": "It immediately reverses direction.", "correct": False,
             "why": "A force changes motion gradually. It has to slow to a "
                    "stop before it can go the other way."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s02",
        "band": "standard",
        "text": "A trolley is travelling right when a resultant force acts "
                "SIDEWAYS on it. What happens to the motion it already had?",
        "options": [
            {"text": "It is cancelled at once, and the trolley now goes "
                     "sideways only.",
             "correct": False,
             "why": "Nothing cancels it. A resultant force adds a change; it "
                    "does not replace the motion."},
            {"text": "It is kept, and the path bends: the trolley goes right "
                     "AND sideways.", "correct": True},
            {"text": "It stops dead for as long as the sideways force keeps "
                     "acting.",
             "correct": False,
             "why": "The rightward motion continues throughout. The force is "
                    "not acting against it."},
            {"text": "It doubles in size, because two motions are now "
                     "happening at once.",
             "correct": False,
             "why": "The rightward speed is unchanged. What is added is a "
                    "sideways change."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s03",
        "band": "standard",
        "text": "The same resultant force acts on the same trolley for three "
                "seconds instead of one. Compared with one second, the "
                "change in its motion is…",
        "options": [
            {"text": "the same, because the force is the same",
             "correct": False,
             "why": "How long a force acts matters. Three times as long "
                    "makes three times the change."},
            {"text": "a third as much, because it is spread over more time",
             "correct": False,
             "why": "It is not spread. The force keeps acting, so the change "
                    "keeps accumulating."},
            {"text": "three times as much", "correct": True},
            {"text": "nine times as much", "correct": False,
             "why": "Nothing here is squared. Three times as long gives "
                    "three times the change in speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s04",
        "band": "standard",
        "text": "A box is pushed across a floor at a steady speed. Someone "
                "says “the push is winning, so the box moves.” What is wrong "
                "with that?",
        "options": [
            {"text": "The push is not really acting.", "correct": False,
             "why": "It is, and it is doing real work. The problem is what "
                    "the sentence claims it is FOR."},
            {"text": "Friction cannot act on a moving object.",
             "correct": False,
             "why": "Friction acts on the box the whole time it slides. That "
                    "is what the push is matching."},
            {"text": "Nothing is wrong — a push is what makes things move, "
                     "and anything moving must have one behind it.",
             "correct": False,
             "why": "Moving needs no force. Only a CHANGE in motion does."},
            {"text": "At a steady speed nothing is winning: the push matches "
                     "the friction, and the box would keep going anyway.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-04-h01",
        "band": "harder",
        "text": "A satellite circles the Earth at a constant speed with its "
                "engines off. Is its motion changing?",
        "options": [
            {"text": "Yes — its direction is changing all the time, and "
                     "that is a change.", "correct": True},
            {"text": "No, because its speed is constant.", "correct": False,
             "why": "Motion is speed AND direction. Going round a circle "
                    "changes direction continuously."},
            {"text": "No, because there is no force on it in space, and a "
                     "thing with no force on it cannot keep going",
             "correct": False,
             "why": "The Earth's pull is acting the whole time. It is what "
                    "keeps the satellite in orbit."},
            {"text": "Yes, because it is slowly speeding up.",
             "correct": False,
             "why": "The speed is constant, as the question says. It is the "
                    "direction that changes."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h02",
        "band": "harder",
        "text": "Galileo rolled balls down one slope and up another, making "
                "the surfaces smoother each time. What did he conclude that "
                "he could never directly observe?",
        "options": [
            {"text": "That every ball eventually stops.", "correct": False,
             "why": "That is what he COULD see, and it is what everyone "
                    "before him concluded from it."},
            {"text": "That with the friction removed entirely, a ball would "
                     "never stop.", "correct": True},
            {"text": "That heavier balls roll further.", "correct": False,
             "why": "Not the point of the experiment, and not what he "
                    "concluded."},
            {"text": "That slopes make balls speed up, which is a property "
                     "of slopes rather than of forces", "correct": False,
             "why": "True and directly observable. The powerful move was "
                    "imagining the limit he could not reach."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h03",
        "band": "harder",
        "text": "The same 1 N resultant acts on an empty trolley and on the "
                "same trolley loaded with bricks. What differs?",
        "options": [
            {"text": "The loaded one changes its motion less for the same "
                     "force.", "correct": True},
            {"text": "The loaded one changes its motion more, because there "
                     "is more of it.", "correct": False,
             "why": "It is the other way round. More mass means the same "
                    "force produces a smaller change."},
            {"text": "Nothing — the same force always gives the same "
                     "change.", "correct": False,
             "why": "Push a shopping trolley empty and full and the "
                    "difference is obvious."},
            {"text": "The resultant force on the loaded one is bigger.",
             "correct": False,
             "why": "The question fixes the resultant at 1 N for both. What "
                    "differs is what that 1 N achieves."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h04",
        "band": "harder",
        "text": "Voyager 1 switched its engines off in 1980 and is still "
                "travelling at about 17 km/s. Which statement explains this "
                "best?",
        "options": [
            {"text": "Its engines are still producing a small push.",
             "correct": False,
             "why": "They are off. Nothing is pushing it along."},
            {"text": "It has stored the force from the engines and is "
                     "spending it slowly.", "correct": False,
             "why": "A force cannot be stored. What it has is speed, and "
                    "speed needs nothing to maintain it."},
            {"text": "Gravity from the Sun is pushing it outwards.",
             "correct": False,
             "why": "The Sun's gravity PULLS it back, very slightly. It is "
                    "not what keeps it going."},
            {"text": "There is almost nothing out there to slow it down, and "
                     "moving needs no force.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-04-e05",
        "band": "easier",
        "text": "What is needed to change the DIRECTION an object is moving "
                "in?",
        "options": [
            {"text": "A resultant force acting on it", "correct": True},
            {"text": "Nothing — direction changes on its own over time",
             "correct": False,
             "why": "With no resultant force an object keeps the same "
                    "direction indefinitely."},
            {"text": "A greater speed, so that it can turn", "correct": False,
             "why": "Speed does not turn anything. A force pointing across "
                    "the motion does."},
            {"text": "The forces on it to become balanced", "correct": False,
             "why": "Balanced forces change nothing at all, including the "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e06",
        "band": "easier",
        "text": "Which of these does NOT need a resultant force?",
        "options": [
            {"text": "Starting a stationary trolley moving", "correct": False,
             "why": "Starting something moving is a change of motion, so it "
                    "needs a resultant force."},
            {"text": "Bringing a moving trolley to a stop", "correct": False,
             "why": "Stopping is a change of motion too, and it needs a force "
                    "against the movement."},
            {"text": "Keeping a steady speed in a straight line",
             "correct": True},
            {"text": "Making a moving trolley turn a corner", "correct": False,
             "why": "Changing direction is a change of motion, so a force is "
                    "needed for it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-04-s05",
        "band": "standard",
        "text": "A ball rolls across a level floor and gradually slows down. "
                "What is the resultant force on it?",
        "options": [
            {"text": "A small force backwards, from friction", "correct": True},
            {"text": "A small force forwards, left over from the push",
             "correct": False,
             "why": "The push ended when the hand let go, and a forward "
                    "resultant would make it speed up."},
            {"text": "Zero, because it is still moving", "correct": False,
             "why": "A zero resultant would keep the speed steady, and this "
                    "ball is slowing."},
            {"text": "A large force downwards, from its weight",
             "correct": False,
             "why": "The weight is balanced by the floor pushing up; it is "
                    "not what slows the ball."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s06",
        "band": "standard",
        "text": "A probe in deep space fires an engine that pushes it "
                "forwards with 500 N, with nothing to resist it. What happens "
                "while the engine keeps firing?",
        "options": [
            {"text": "It settles at a top speed and goes no faster",
             "correct": False,
             "why": "A top speed needs a resistance to grow and match the "
                    "push, and out there nothing does."},
            {"text": "It speeds up for as long as the engine fires",
             "correct": True},
            {"text": "It moves at a steady 500 m/s while the engine is on",
             "correct": False,
             "why": "500 N is a force, not a speed, and a resultant force "
                    "keeps changing the speed."},
            {"text": "Nothing, because there is nothing to push against",
             "correct": False,
             "why": "It pushes against its own exhaust gas, which is the "
                    "second object in the pair."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-04-h05",
        "band": "harder",
        "text": "A ball thrown straight upwards is momentarily at rest at the "
                "very top. Why is the resultant force not zero at that "
                "instant?",
        "options": [
            {"text": "Because the throwing force is still in the ball at the "
                     "top",
             "correct": False,
             "why": "Nothing carries a force along. The hand's push ended at "
                    "the moment of release."},
            {"text": "Because gravity keeps pulling down whether the ball is "
                     "moving or not",
             "correct": True},
            {"text": "Because being at rest always means the forces are "
                     "unbalanced",
             "correct": False,
             "why": "A book at rest on a table has balanced forces; being at "
                    "rest settles nothing on its own."},
            {"text": "Because air resistance acts upwards at the top",
             "correct": False,
             "why": "Air resistance opposes the motion, and at the instant of "
                    "rest there is none to oppose."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h06",
        "band": "harder",
        "text": "A car brakes to a standstill. A student says the braking "
                "force was used up in stopping it. What is wrong?",
        "options": [
            {"text": "Nothing — a force is used up doing its job",
             "correct": False,
             "why": "A force is not a supply and cannot be spent. It exists "
                    "only while the interaction lasts."},
            {"text": "The braking force existed only while the surfaces "
                     "rubbed, and ended with the motion",
             "correct": True},
            {"text": "The braking force is still acting, which is why the car "
                     "stays still",
             "correct": False,
             "why": "The car stays still because the forces on it are now "
                    "balanced, not because braking continues."},
            {"text": "The braking force turned into the car's weight",
             "correct": False,
             "why": "One force never becomes another; the weight was there "
                    "throughout, unchanged."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ────────────────────────────────
    {
        "id": "p4-04-e07",
        "band": "easier",
        "text": "An ice hockey puck slides across smooth ice with a resultant "
                "force of 0 N acting on it. What happens to its motion?",
        "options": [
            {"text": "It keeps travelling at the same speed in the same "
                     "direction.", "correct": True},
            {"text": "It slowly loses speed until it stops.", "correct": False,
             "why": "That needs a force against the motion, and there is "
                    "none acting here."},
            {"text": "It speeds up on its own.", "correct": False,
             "why": "Nothing is pushing it faster. With 0 N left over "
                    "nothing about its motion changes."},
            {"text": "It curves gently to one side.",
             "correct": False,
             "why": "A curve needs a sideways force, and there is none "
                    "acting on the puck."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e08",
        "band": "easier",
        "text": "A steel ball rolls along a level track with no resultant "
                "force acting on it at all. One second later, is it moving "
                "faster, slower, or the same?",
        "options": [
            {"text": "Faster, because rolling things naturally speed up.",
             "correct": False,
             "why": "Nothing speeds anything up on its own. A resultant "
                    "force is needed for that."},
            {"text": "The same — nothing is left over to change it.",
             "correct": True},
            {"text": "Slower, because it must eventually stop.",
             "correct": False,
             "why": "It only slows if something acts against it, and here "
                    "nothing does."},
            {"text": "It cannot be worked out without knowing its mass.",
             "correct": False,
             "why": "Mass decides how much a force would change it, not "
                    "whether it changes at all with none acting."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e09",
        "band": "easier",
        "text": "A space probe far from any planet has a resultant force of "
                "0 N acting on it. What is true of its motion?",
        "options": [
            {"text": "It gradually comes to a complete stop.", "correct": False,
             "why": "Stopping is a change, and a change needs a force. "
                    "There is none out there."},
            {"text": "It slowly speeds up.", "correct": False,
             "why": "Speeding up needs a resultant in the direction of "
                    "travel. Nothing is providing one."},
            {"text": "It carries on at the same speed in the same "
                     "direction, indefinitely.", "correct": True},
            {"text": "Its direction slowly drifts.", "correct": False,
             "why": "A drifting direction would need a sideways force. "
                    "None is acting here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e10",
        "band": "easier",
        "text": "A hovering drone has its motors providing exactly enough "
                "thrust to cancel its weight, so the resultant force on it "
                "is 0 N. What is happening to its height?",
        "options": [
            {"text": "It slowly drifts upwards.", "correct": False,
             "why": "Rising is a change of motion, and there is nothing "
                    "left over to cause it."},
            {"text": "It slowly sinks.", "correct": False,
             "why": "Sinking would need an unbalanced weight. Here the "
                    "thrust exactly cancels it."},
            {"text": "It cannot be worked out without its speed.", "correct": False,
             "why": "A resultant of 0 N means no change whatever its "
                    "current motion — height included."},
            {"text": "It stays at the same height, neither rising nor "
                     "falling.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e11",
        "band": "easier",
        "text": "A cyclist pedals harder so that the forward force from the "
                "tyres becomes bigger than the backward resistive forces. "
                "What happens to the bicycle's speed?",
        "options": [
            {"text": "It increases — there is now a resultant force in the "
                     "direction of travel.", "correct": True},
            {"text": "It stays the same, because the cyclist was already moving forwards before this.", "correct": False,
             "why": "A steady speed needs the forces to be balanced. Here "
                    "they no longer are."},
            {"text": "It decreases, because pedalling harder makes more "
                     "drag build up against the bicycle than before.",
             "correct": False,
             "why": "The forward force has grown bigger than the resistive "
                    "forces, not smaller."},
            {"text": "It cannot change unless the bicycle starts from "
                     "rest.", "correct": False,
             "why": "A resultant force changes speed whether an object "
                    "starts at rest or is already moving."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e12",
        "band": "easier",
        "text": "A rocket's engines push it forward with more force than the "
                "resistance acting on it. What happens to its speed?",
        "options": [
            {"text": "It stays the same, since a rocket in space has nothing to push against and cannot speed up.", "correct": False,
             "why": "That is true only with 0 N left over. Here there is a "
                    "forward resultant."},
            {"text": "It increases, because the resultant force points in "
                     "the direction of travel.", "correct": True},
            {"text": "It decreases, because the fuel being used up steadily "
                     "reduces how much force the engines are able to "
                     "supply.", "correct": False,
             "why": "Speed depends on the resultant now acting, not on how "
                    "much fuel is left."},
            {"text": "It reverses direction immediately.", "correct": False,
             "why": "A force adds to the existing motion; it does not "
                    "reverse it instantly."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e13",
        "band": "easier",
        "text": "A skateboarder pushes off the ground, giving themselves a "
                "forward resultant force. What happens to their speed at "
                "that moment?",
        "options": [
            {"text": "It stays the same, because they were already "
                     "moving.", "correct": False,
             "why": "Even while moving, a resultant force in the direction "
                    "of travel makes the speed rise."},
            {"text": "It decreases.", "correct": False,
             "why": "A forward resultant speeds things up, not down."},
            {"text": "It increases.", "correct": True},
            {"text": "Only their direction changes, not their speed.",
             "correct": False,
             "why": "The push is along the way they are already going, so "
                    "it changes the speed, not the direction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e14",
        "band": "easier",
        "text": "A cyclist applies the brakes so that a backward resultant "
                "force acts on the bicycle. What happens to its speed?",
        "options": [
            {"text": "It increases.", "correct": False,
             "why": "A resultant against the motion always brings the "
                    "speed down, never up."},
            {"text": "It stays the same.", "correct": False,
             "why": "A steady speed needs the forces to balance. Braking "
                    "unbalances them."},
            {"text": "The bicycle instantly stops.", "correct": False,
             "why": "Slowing down is gradual — the speed falls bit by bit "
                    "as the force keeps acting."},
            {"text": "It decreases.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e15",
        "band": "easier",
        "text": "A shopping trolley rolling forwards is given a push backwards "
                "by a shop assistant. What effect does this backward force "
                "have?",
        "options": [
            {"text": "It slows the trolley down.", "correct": True},
            {"text": "It speeds the trolley up.", "correct": False,
             "why": "A force against the direction of travel reduces "
                    "speed; it does not add to it."},
            {"text": "It makes the trolley heavier.", "correct": False,
             "why": "A force changes motion; it does not change how much "
                    "mass the trolley has."},
            {"text": "It has no effect while the trolley is still moving "
                     "forwards.", "correct": False,
             "why": "A resultant force changes the motion at once, "
                    "whichever way the object is currently going."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e16",
        "band": "easier",
        "text": "A dart is thrown, and a resultant force acts against its "
                "direction of travel the whole way. What must be happening "
                "to its speed?",
        "options": [
            {"text": "It is getting bigger throughout the flight.",
             "correct": False,
             "why": "A force against the motion reduces speed rather than "
                    "adding to it."},
            {"text": "It is getting smaller throughout the flight.",
             "correct": True},
            {"text": "It stays exactly the same.", "correct": False,
             "why": "A steady speed would need the forces to balance, and "
                    "this resultant is against the motion."},
            {"text": "It changes only its direction, not its speed.",
             "correct": False,
             "why": "A force acting straight against the direction of "
                    "travel changes the speed, not which way it points."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e17",
        "band": "easier",
        "text": "A car travelling north has a resultant force acting due "
                "east on it. What happens to its northward motion while "
                "that force acts?",
        "options": [
            {"text": "It stops completely, because the new eastward force "
                     "cancels out everything the car was already doing.",
             "correct": False,
             "why": "The eastward force does not cancel the northward "
                    "motion; it adds to it."},
            {"text": "It reverses to southward, since the new force turns the car right around on itself.", "correct": False,
             "why": "Nothing here points south. The sideways force bends "
                    "the path rather than reversing it."},
            {"text": "It carries on unchanged while the car also starts "
                     "moving eastward.", "correct": True},
            {"text": "It gets faster.", "correct": False,
             "why": "The force is across the motion, not along it, so the "
                    "northward speed is unaffected."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e18",
        "band": "easier",
        "text": "A ball rolling in a straight line has a resultant force act "
                "on it at right angles to its motion. What happens to its "
                "path?",
        "options": [
            {"text": "It stops moving.", "correct": False,
             "why": "A sideways force does not remove the motion that is "
                    "already there; it bends the path instead."},
            {"text": "It speeds up along the same straight line.",
             "correct": False,
             "why": "A force at right angles to the motion changes "
                    "direction, not speed along the original line."},
            {"text": "Nothing changes at all.", "correct": False,
             "why": "A resultant force always changes something about the "
                    "motion — here, the direction."},
            {"text": "It curves away from the straight line.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e19",
        "band": "easier",
        "text": "A satellite already moving in a straight line has a sideways "
                "resultant force act on it continuously. What kind of path "
                "does it follow?",
        "options": [
            {"text": "A curved path.", "correct": True},
            {"text": "The same straight line, only faster.", "correct": False,
             "why": "A sideways force bends the path; it does not add "
                    "speed along the original line."},
            {"text": "It comes to a stop.", "correct": False,
             "why": "The force is across the motion, not against it, so it "
                    "does not slow the satellite down."},
            {"text": "It reverses back the way it came.", "correct": False,
             "why": "A continuous sideways force curves the path steadily; "
                    "it does not send the object backwards."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e20",
        "band": "easier",
        "text": "A stone is thrown from a hand and travels through the air. "
                "Once it has left the hand, is the throwing force still "
                "acting on it?",
        "options": [
            {"text": "Yes, and it is slowly running out as the stone flies through the air.", "correct": False,
             "why": "A force cannot be stored inside an object and spent "
                    "later."},
            {"text": "No — the throwing force ended the instant the hand "
                     "let go.", "correct": True},
            {"text": "Yes, and it stays exactly the same size for the "
                     "whole flight, however far the stone eventually "
                     "travels.", "correct": False,
             "why": "The hand is no longer touching the stone, so it "
                    "cannot still be applying a force."},
            {"text": "It depends how hard the stone was thrown.",
             "correct": False,
             "why": "However hard the throw, the force from the hand stops "
                    "the moment contact ends."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e21",
        "band": "easier",
        "text": "An arrow leaves a bow and flies through the air. Which "
                "force from the bowstring is still acting on the arrow in "
                "flight?",
        "options": [
            {"text": "A small forward force that gradually fades away.",
             "correct": False,
             "why": "There is no leftover push. Contact between string and "
                    "arrow has ended completely."},
            {"text": "The same forward force the whole way to the target.",
             "correct": False,
             "why": "The string cannot push something it is no longer "
                    "touching."},
            {"text": "None — the bowstring's force ended when the arrow "
                     "left it.", "correct": True},
            {"text": "A force that switches on and off as the arrow "
                     "travels.", "correct": False,
             "why": "Nothing switches it back on. Once contact ends the "
                    "force from the string is gone."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e22",
        "band": "easier",
        "text": "A child releases a marble from a spring-loaded launcher. "
                "After it leaves the launcher, what force from the spring "
                "is acting on the marble?",
        "options": [
            {"text": "A weakening push that lasts a few more seconds.",
             "correct": False,
             "why": "The push cannot outlast the contact between spring "
                    "and marble."},
            {"text": "The same push as when it was released.",
             "correct": False,
             "why": "Once the marble leaves the spring there is no longer "
                    "any contact to supply a force."},
            {"text": "A push that depends on how far the marble has "
                     "travelled.", "correct": False,
             "why": "Distance travelled makes no difference — the spring's "
                    "force ended at the moment of release."},
            {"text": "None at all — the spring stopped touching it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e23",
        "band": "easier",
        "text": "The same resultant force acts on a trolley for twice as long "
                "as before. What does this do to the change in its speed?",
        "options": [
            {"text": "It makes the change in speed bigger.", "correct": True},
            {"text": "It makes the change in speed smaller.", "correct": False,
             "why": "Acting for longer gives the force more time to change "
                    "the motion, not less."},
            {"text": "It has no effect on the change in speed.",
             "correct": False,
             "why": "How long a force acts for does affect how much it "
                    "changes the motion."},
            {"text": "It changes the object's mass instead of its speed.",
             "correct": False,
             "why": "A force changes motion; it does not alter how much "
                    "matter an object has."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e24",
        "band": "easier",
        "text": "Two identical trolleys start at the same speed. One gets a "
                "bigger resultant force than the other, for the same length "
                "of time. Which one changes speed more?",
        "options": [
            {"text": "The one with the smaller force.", "correct": False,
             "why": "A bigger force produces a bigger change in the same "
                    "time, not a smaller one."},
            {"text": "The one with the bigger force.", "correct": True},
            {"text": "Both change by exactly the same amount.",
             "correct": False,
             "why": "Only the force size differs here, and a bigger force "
                    "changes the motion more."},
            {"text": "Neither changes at all.", "correct": False,
             "why": "Both trolleys have a resultant force acting on them, "
                    "so both are changing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e25",
        "band": "easier",
        "text": "A resultant force acts on an object for only a very short "
                "instant. Compared with the same force acting for several "
                "seconds, the change in motion is...",
        "options": [
            {"text": "much bigger.", "correct": False,
             "why": "Less time acting gives the force less chance to "
                    "change the motion."},
            {"text": "exactly the same.", "correct": False,
             "why": "How long the force acts for matters; a shorter time "
                    "gives a smaller change."},
            {"text": "much smaller.", "correct": True},
            {"text": "impossible to say without knowing the object's "
                     "colour.", "correct": False,
             "why": "Colour has no bearing on forces or motion at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e26",
        "band": "easier",
        "text": "The same push is given to an empty wheelbarrow and then to "
                "one loaded with bricks. Which one's speed changes more?",
        "options": [
            {"text": "The loaded one.", "correct": False,
             "why": "More mass means the same push produces a smaller "
                    "change, not a bigger one."},
            {"text": "Both change by the same amount.", "correct": False,
             "why": "The loaded barrow has far more mass, so the same push "
                    "affects it less."},
            {"text": "Neither changes, because a push cannot move a "
                     "wheelbarrow.", "correct": False,
             "why": "A push is a force, and a resultant force does change "
                    "an object's motion."},
            {"text": "The empty one.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e27",
        "band": "easier",
        "text": "A gentle push is given first to a table-tennis ball and then "
                "to a bowling ball, with exactly the same force each time. "
                "Which changes speed by more?",
        "options": [
            {"text": "The table-tennis ball.", "correct": True},
            {"text": "The bowling ball.", "correct": False,
             "why": "The bowling ball has far more mass, so the same force "
                    "changes its motion less."},
            {"text": "They change by the same amount.", "correct": False,
             "why": "Their masses are very different, so the same force "
                    "affects them differently."},
            {"text": "It cannot be worked out without knowing their "
                     "colours.", "correct": False,
             "why": "Colour makes no difference to how a force changes an "
                    "object's motion."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e28",
        "band": "easier",
        "text": "A go-kart carries one passenger, then two. The same forward "
                "force is used to get it moving both times. In which case "
                "does its speed change more quickly?",
        "options": [
            {"text": "With two passengers.", "correct": False,
             "why": "More mass in the kart means the same force changes "
                    "its speed more slowly, not more quickly."},
            {"text": "With one passenger.", "correct": True},
            {"text": "It is the same in both cases.", "correct": False,
             "why": "Adding a passenger adds mass, and mass affects how "
                    "much a given force changes the motion."},
            {"text": "It cannot change with people inside it.",
             "correct": False,
             "why": "A go-kart with people in it can still speed up; the "
                    "force is simply less effective at changing its "
                    "motion."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e29",
        "band": "easier",
        "text": "A car drives around a roundabout at a perfectly steady "
                "speed. Is its motion changing?",
        "options": [
            {"text": "No, because its speed never changes.", "correct": False,
             "why": "Motion is speed AND direction together. Direction is "
                    "changing throughout."},
            {"text": "No, because it is not speeding up or slowing down.",
             "correct": False,
             "why": "Not speeding up or slowing down is only part of the "
                    "story; the direction is still changing."},
            {"text": "Yes — its direction is continually changing.",
             "correct": True},
            {"text": "Yes, because the engine is working harder on a "
                     "bend.", "correct": False,
             "why": "Whatever the engine is doing, what makes the motion "
                    "change is the changing direction, not the engine "
                    "effort."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e30",
        "band": "easier",
        "text": "A fairground ride swings passengers around in a horizontal "
                "circle at a constant speed. Is a resultant force acting on "
                "them?",
        "options": [
            {"text": "No, because their speed never changes.", "correct": False,
             "why": "A constant speed does not mean no resultant force; "
                    "the direction is still changing continuously."},
            {"text": "No, because they are not speeding up.", "correct": False,
             "why": "Not speeding up is not the same as no change of "
                    "motion. Direction still counts."},
            {"text": "Only if the ride is also going faster.", "correct": False,
             "why": "The ride does not need to go faster for a resultant "
                    "force to be acting; a changing direction is enough."},
            {"text": "Yes — a resultant force is needed to keep changing "
                     "their direction.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ──────────────────────────────
    {
        "id": "p4-04-s07",
        "band": "standard",
        "text": "A resultant force of 2 N acts on a trolley for 1 second and "
                "changes its speed by 1 m/s. If the same 2 N force instead "
                "acts for 4 seconds, by how much does the speed change?",
        "options": [
            {"text": "4 m/s", "correct": True},
            {"text": "1 m/s", "correct": False,
             "why": "That ignores the extra time entirely — the force "
                    "keeps acting for four times as long."},
            {"text": "16 m/s", "correct": False,
             "why": "That squares the time rather than simply multiplying "
                    "the change by it."},
            {"text": "2 m/s", "correct": False,
             "why": "That is only twice the change, but the time has "
                    "increased by four times, not two."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s08",
        "band": "standard",
        "text": "A resultant force acts on a skateboarder for 3 seconds and "
                "changes their speed by 6 m/s. What would the same force "
                "acting for just 1 second have changed their speed by?",
        "options": [
            {"text": "6 m/s", "correct": False,
             "why": "That is the change from three seconds, not from one "
                    "— the shorter time gives a smaller change."},
            {"text": "2 m/s", "correct": True},
            {"text": "18 m/s", "correct": False,
             "why": "That multiplies rather than divides; a shorter time "
                    "gives less change, not more."},
            {"text": "0 m/s", "correct": False,
             "why": "The force still acts and still changes the speed, "
                    "just by less in a shorter time."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s09",
        "band": "standard",
        "text": "A go-kart's engine gives a steady forward force for 2 "
                "seconds, changing its speed by 3 m/s. The same force is "
                "then used for 6 seconds from rest on an identical kart. "
                "What is the total change in speed?",
        "options": [
            {"text": "3 m/s", "correct": False,
             "why": "That is the change for two seconds only; six seconds "
                    "is three times as long."},
            {"text": "18 m/s", "correct": False,
             "why": "That doubles the six-second figure rather than "
                    "scaling correctly from the original two-second "
                    "change."},
            {"text": "9 m/s", "correct": True},
            {"text": "27 m/s", "correct": False,
             "why": "That multiplies by nine rather than by the threefold "
                    "increase in time."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s10",
        "band": "standard",
        "text": "A model rocket's engine pushes it with a steady force for 5 "
                "seconds, changing its speed by 20 m/s. If the same engine "
                "burned for only 1 second, what change in speed would "
                "result?",
        "options": [
            {"text": "20 m/s", "correct": False,
             "why": "That is the change for the full five seconds, not for "
                    "one."},
            {"text": "100 m/s", "correct": False,
             "why": "That multiplies rather than divides the change by "
                    "five."},
            {"text": "0 m/s", "correct": False,
             "why": "The force still acts for that one second and still "
                    "produces some change."},
            {"text": "4 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s11",
        "band": "standard",
        "text": "A gentle push is given to a shopping trolley and, "
                "separately, an identical push is given to a loaded "
                "delivery cart with far more mass. Which statement is "
                "correct?",
        "options": [
            {"text": "The trolley's speed changes by more, because it has "
                     "less mass to change.", "correct": True},
            {"text": "The cart's speed changes by more, because it has "
                     "more mass to push against.", "correct": False,
             "why": "More mass makes the same force LESS effective at "
                    "changing the motion, not more."},
            {"text": "Both change by exactly the same amount, since a "
                     "gentle push cannot possibly tell two different "
                     "masses apart.", "correct": False,
             "why": "Their masses are very different, so the same force "
                    "changes them by different amounts."},
            {"text": "Neither changes, because a gentle push is too weak "
                     "to move anything.", "correct": False,
             "why": "A resultant force of any size changes an object's "
                    "motion by some amount."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s12",
        "band": "standard",
        "text": "Two identical footballs are kicked with exactly the same "
                "force, except one is a normal ball and the other has been "
                "filled with sand, making it much heavier. Which ball's "
                "speed changes more?",
        "options": [
            {"text": "The sand-filled ball.", "correct": False,
             "why": "The extra mass makes the same kick change its speed "
                    "by less, not more."},
            {"text": "The normal ball.", "correct": True},
            {"text": "They change by the same amount.", "correct": False,
             "why": "Their masses differ a lot, so the identical kick "
                    "affects them differently."},
            {"text": "It depends only on how hard each ball is kicked.",
             "correct": False,
             "why": "The kick is stated to be the same force in both cases "
                    "— what differs here is the mass."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s13",
        "band": "standard",
        "text": "A canoe is pushed off from a jetty with the same force "
                "twice: once empty, and once loaded with camping gear. In "
                "which case does its speed change more for the push?",
        "options": [
            {"text": "When it is loaded.", "correct": False,
             "why": "The extra mass of the gear makes the same push change "
                    "the speed by less."},
            {"text": "Exactly the same in both cases.", "correct": False,
             "why": "The loaded canoe has more mass, so the identical push "
                    "has a smaller effect on it."},
            {"text": "When it is empty.", "correct": True},
            {"text": "It cannot be worked out without knowing the water's "
                     "temperature.", "correct": False,
             "why": "Temperature of the water has nothing to do with how "
                    "mass affects the change from a given force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s14",
        "band": "standard",
        "text": "Two drones are given the same forward thrust force. One is "
                "carrying a heavy camera, the other nothing extra. Which "
                "drone speeds up more quickly?",
        "options": [
            {"text": "The one carrying the camera, because it needs more "
                     "force to fly.", "correct": False,
             "why": "Needing more force to hover is a separate question "
                    "from how much a given thrust changes its speed."},
            {"text": "They speed up equally, since the thrust is "
                     "identical.", "correct": False,
             "why": "Identical thrust does not mean identical change — "
                    "their masses differ."},
            {"text": "The heavier one, because more mass means a bigger "
                     "resultant force.", "correct": False,
             "why": "Mass does not create extra force; the thrust is fixed "
                    "and identical for both."},
            {"text": "The one with nothing extra, because it has less "
                     "mass.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s15",
        "band": "standard",
        "text": "A hovercraft travelling east at a steady speed has a "
                "resultant force applied due south. What happens to its "
                "eastward speed while the southward force acts?",
        "options": [
            {"text": "It stays the same — the southward force only adds a "
                     "new, separate motion.", "correct": True},
            {"text": "It falls to zero immediately, because the southward "
                     "push cancels the eastward motion outright.",
             "correct": False,
             "why": "The southward force does not cancel the existing "
                    "motion; it acts at right angles to it."},
            {"text": "It increases, because two separate forces are now acting on the hovercraft at once.",
             "correct": False,
             "why": "The extra force is not in the eastward direction, so "
                    "it does not add to the eastward speed."},
            {"text": "It decreases gradually.", "correct": False,
             "why": "Slowing the eastward motion would need a force acting "
                    "against it, and this one is sideways to it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s16",
        "band": "standard",
        "text": "A cyclist riding in a straight line feels a strong crosswind "
                "pushing sideways on them. What effect does this have on "
                "the direction they were already travelling in?",
        "options": [
            {"text": "It cancels their forward motion completely, "
                     "replacing it entirely with sideways motion instead.",
             "correct": False,
             "why": "A sideways force does not remove the motion that is "
                    "already there; it adds to it."},
            {"text": "None on its own — the path simply bends to include "
                     "the sideways push as well.", "correct": True},
            {"text": "It reverses their direction.", "correct": False,
             "why": "A crosswind pushes across the motion, not directly "
                    "against it, so it bends the path rather than "
                    "reversing it."},
            {"text": "It has no effect on their path at all.",
             "correct": False,
             "why": "A sideways resultant force does change the path — it "
                    "bends it towards the direction the wind is pushing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s17",
        "band": "standard",
        "text": "A model boat sailing north on a pond has a resultant force "
                "applied due west by the wind. Which best describes what "
                "happens next?",
        "options": [
            {"text": "It stops moving north entirely and only moves west from then on.", "correct": False,
             "why": "The northward motion is not switched off by a "
                    "sideways force; both motions exist together."},
            {"text": "It speeds up while still travelling due north.",
             "correct": False,
             "why": "The wind's force is sideways to the boat's motion, "
                    "not along it, so it does not simply add speed "
                    "northward."},
            {"text": "It continues moving north while also gaining a "
                     "westward motion, so its path curves.",
             "correct": True},
            {"text": "It slows down and eventually stops.", "correct": False,
             "why": "Stopping needs a force against the direction of "
                    "travel. This force is across it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s18",
        "band": "standard",
        "text": "A rollercoaster car moving in a straight line has a "
                "sideways resultant force applied by the track as it "
                "approaches a bend. What is happening to the car's motion?",
        "options": [
            {"text": "Its speed is dropping because the track's push resists the car's forward motion.", "correct": False,
             "why": "The force described acts sideways to the motion, "
                    "which changes direction rather than reducing speed."},
            {"text": "Nothing is changing, since the car stays on the "
                     "track.", "correct": False,
             "why": "Staying on the track is exactly why the sideways "
                    "force is there — it is what bends the path."},
            {"text": "The car reverses along the same line.", "correct": False,
             "why": "A sideways force bends a path into a curve; it does "
                    "not send an object back the way it came."},
            {"text": "Its direction is changing while its speed along the "
                     "original line is unaffected by that force alone.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s19",
        "band": "standard",
        "text": "A cannonball is fired from a cannon and then travels "
                "through the air with nothing else pushing it. A student "
                "says the cannonball keeps a bit of the firing force inside "
                "it that slowly runs out. What is the flaw in this idea?",
        "options": [
            {"text": "A force cannot be stored inside an object — the "
                     "firing force ended the instant the cannonball left "
                     "the barrel.", "correct": True},
            {"text": "The cannonball is too heavy to hold any force at "
                     "all.", "correct": False,
             "why": "Weight has nothing to do with whether a force can be "
                    "stored — no object can store a force, heavy or not."},
            {"text": "The firing force is real, but it runs out instantly rather than fading slowly.", "correct": False,
             "why": "The issue is not the speed at which it runs out — a "
                    "force simply cannot be stored to run out at all."},
            {"text": "The cannonball actually speeds up in flight because "
                     "of the stored force.", "correct": False,
             "why": "It does not speed up in flight; with no additional "
                    "force at all, its horizontal motion stays the same "
                    "throughout."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s20",
        "band": "standard",
        "text": "A javelin leaves the athlete's hand and travels through the "
                "air. A student says the throw gives it a store of force "
                "that gradually gets used up. Which correction is right?",
        "options": [
            {"text": "The store of force is real, but it is used up within the first instant of flight.", "correct": False,
             "why": "The problem is not the speed of use — no force can be "
                    "stored to be used up in the first place."},
            {"text": "There is no store of force at all — the hand's force "
                     "ended the moment it let go of the javelin.",
             "correct": True},
            {"text": "The javelin creates its own new force as it flies.",
             "correct": False,
             "why": "Nothing about flying through the air creates a force "
                    "from nothing."},
            {"text": "The javelin's weight is what the student is really "
                     "describing.", "correct": False,
             "why": "Weight is a separate, constant force. It is not a "
                    "stored version of the throw."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s21",
        "band": "standard",
        "text": "A heavy brass disc slides the length of a polished shuffleboard table. A spectator says something must still be pushing it, or it would stop instantly. Explain what is actually true.",
        "options": [
            {"text": "Something invisible must be pushing it the whole "
                     "way, since nothing continues moving entirely on its "
                     "own.", "correct": False,
             "why": "Nothing needs to push it. A resultant force is needed "
                    "only to CHANGE motion, not to continue it."},
            {"text": "The disc would stop instantly without a continuous push.", "correct": False,
             "why": "It does not stop instantly with no force; with 0 N "
                    "left over it keeps going at the same speed."},
            {"text": "Nothing is pushing the disc — a steady speed needs no force at all, so it simply keeps going.",
             "correct": True},
            {"text": "The push from the hand fades away slowly over the whole length of the slide.", "correct": False,
             "why": "The push ended the instant the hand released the disc — nothing about it lingers or fades."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s22",
        "band": "standard",
        "text": "A tennis ball is hit and flies across the court. Somebody "
                "claims the racket's force follows the ball all the way to "
                "the other side. What is the correct picture?",
        "options": [
            {"text": "The force does follow the ball the whole way across "
                     "the court, weakening gradually with every metre it "
                     "travels.", "correct": False,
             "why": "Nothing follows the ball once contact with the racket "
                    "ends — there is no force left to weaken."},
            {"text": "The force stays exactly the same size the whole "
                     "flight.", "correct": False,
             "why": "There is no force from the racket in flight at all, "
                    "constant or otherwise, once contact has ended."},
            {"text": "The ball only keeps moving because the court pushes "
                     "it along.", "correct": False,
             "why": "The court is not touching the ball in flight, so it "
                    "cannot be supplying anything to keep it moving."},
            {"text": "The racket's force acted only during contact; after "
                     "that, the ball needs no force to keep travelling.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s23",
        "band": "standard",
        "text": "A trolley is speeded up by a push for two seconds, "
                "reaching 5 m/s. The push then stops completely and "
                "nothing else acts on it. What happens to its speed after "
                "the push stops?",
        "options": [
            {"text": "It stays at 5 m/s, because with the push gone there "
                     "is nothing left to change it.", "correct": True},
            {"text": "It keeps rising, because it was already speeding "
                     "up.", "correct": False,
             "why": "Speeding up needed the push; once the push is gone "
                    "there is nothing to keep raising the speed."},
            {"text": "It falls back to 0 m/s, because removing the push "
                     "should undo all of the speeding up completely.",
             "correct": False,
             "why": "Falling to zero would need a force against the "
                    "motion, and nothing here is acting at all."},
            {"text": "It falls to half of 5 m/s.", "correct": False,
             "why": "There is no reason for it to halve — with no "
                    "resultant force it simply keeps its speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s24",
        "band": "standard",
        "text": "A remote-control car is accelerated by its motor to 4 m/s, "
                "and then the motor is switched off on a smooth, level "
                "floor with nothing resisting it. What speed does the car "
                "settle at afterwards?",
        "options": [
            {"text": "0 m/s, since switching the motor off should bring "
                     "the car straight back to a complete stop.",
             "correct": False,
             "why": "The motor being off does not itself slow anything; "
                    "only a force against the motion could do that, and "
                    "none is described."},
            {"text": "4 m/s, unchanged, since nothing is left to change "
                     "it.", "correct": True},
            {"text": "8 m/s, since the car keeps on accelerating out of habit for a while.",
             "correct": False,
             "why": "Nothing continues to accelerate the car once the "
                    "driving force has stopped."},
            {"text": "2 m/s, half of what it reached.", "correct": False,
             "why": "There is no reason for the speed to halve when "
                    "nothing is acting to change it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s25",
        "band": "standard",
        "text": "A skater is pushed off by a friend, reaching 3 m/s, and "
                "then glides with nobody touching them and nothing "
                "resisting them. What is their speed a few seconds later?",
        "options": [
            {"text": "Slower than 3 m/s, since pushes fade.", "correct": False,
             "why": "A push does not fade after contact ends — it simply "
                    "stops acting, and with nothing else acting the speed "
                    "stays put."},
            {"text": "Faster than 3 m/s, since gliding builds up speed.",
             "correct": False,
             "why": "Gliding does not add speed on its own; a resultant "
                    "force would be needed for that."},
            {"text": "Still 3 m/s.", "correct": True},
            {"text": "It cannot be worked out without knowing the "
                     "skater's mass.", "correct": False,
             "why": "Mass would matter if a NEW force were changing the "
                    "speed. With none acting, the speed simply stays as it "
                    "was."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s26",
        "band": "standard",
        "text": "A puck is struck across an air-hockey table, reaching 2 "
                "m/s, and after the striker lets go nothing else touches "
                "the puck. What is its speed just before it reaches the far "
                "end?",
        "options": [
            {"text": "Less than 2 m/s, since it has travelled a long way.",
             "correct": False,
             "why": "Distance travelled does not by itself reduce speed; "
                    "only a force against the motion would."},
            {"text": "More than 2 m/s, since it keeps gaining speed while "
                     "free.", "correct": False,
             "why": "Nothing is acting on it to add extra speed once the "
                    "striker lets go."},
            {"text": "0 m/s, since the striker is no longer touching it.",
             "correct": False,
             "why": "Losing contact with the striker does not stop the "
                    "puck — a force against its motion would be needed for "
                    "that, and none is present."},
            {"text": "2 m/s, the same as when it was struck.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s27",
        "band": "standard",
        "text": "Two identical trolleys are both moving at 2 m/s. The same "
                "resultant force acts on both for the same length of time. "
                "What is true of the change in each trolley's speed?",
        "options": [
            {"text": "The change is the same for both, because the force, "
                     "time and mass are all identical.", "correct": True},
            {"text": "The one that ends up with the higher final speed "
                     "must be the one whose speed changed by more "
                     "overall.", "correct": False,
             "why": "They start at the same speed, and identical force, "
                    "time and mass produce an identical change for both."},
            {"text": "It cannot be worked out without knowing which way "
                     "each trolley is facing.", "correct": False,
             "why": "Facing direction makes no difference here — the "
                    "force, mass and time are what set the size of the "
                    "change."},
            {"text": "The change depends on how fast each was already "
                     "going before the force started.", "correct": False,
             "why": "Starting speed does not affect how much a given "
                    "force changes the speed by; it only affects the "
                    "resulting final speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s28",
        "band": "standard",
        "text": "A skateboarder rolling at 1 m/s and one rolling at 5 m/s "
                "both receive the same forward resultant force for the "
                "same time and have the same mass. How does the change in "
                "their speeds compare?",
        "options": [
            {"text": "The faster skateboarder changes speed by more.",
             "correct": False,
             "why": "Starting speed does not change how effective a given "
                    "force is — mass, force and time decide that, and "
                    "those are all equal here."},
            {"text": "The change in speed is the same for both.",
             "correct": True},
            {"text": "The slower skateboarder changes speed by more.",
             "correct": False,
             "why": "There is nothing here to make the change bigger for "
                    "the slower rider; force, time and mass are equal for "
                    "both."},
            {"text": "It cannot be compared without a formula.",
             "correct": False,
             "why": "The comparison follows directly from force, time and "
                    "mass being equal — no formula is needed to see the "
                    "change must match."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s29",
        "band": "standard",
        "text": "A go-kart is given a 4 N resultant force, and an identical "
                "kart is given an 8 N resultant force, both for the same "
                "time. Which change in speed is bigger?",
        "options": [
            {"text": "The one that received 4 N.", "correct": False,
             "why": "A bigger resultant force produces a bigger change in "
                    "the same time, not a smaller one."},
            {"text": "Both change by the same amount.", "correct": False,
             "why": "The forces are different sizes, and a bigger force "
                    "changes the motion by more in the same time."},
            {"text": "The one that received 8 N.", "correct": True},
            {"text": "It cannot be worked out without their starting "
                     "speeds.", "correct": False,
             "why": "Starting speed does not affect how much a given "
                    "force changes the speed by in a fixed time — only the "
                    "force, time and mass matter."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s30",
        "band": "standard",
        "text": "A supermarket trolley and an identical one loaded with a "
                "sack of compost are both given a 20 N push for the same "
                "length of time. How does the change in speed compare?",
        "options": [
            {"text": "The loaded trolley changes speed by more, because "
                     "it needs a bigger push to notice.", "correct": False,
             "why": "Needing a bigger push to notice is exactly why a "
                    "given push changes it LESS, not more."},
            {"text": "Both trolleys change speed by the same amount.",
             "correct": False,
             "why": "Their masses differ, and the same push affects a "
                    "bigger mass by a smaller amount."},
            {"text": "The empty trolley changes speed by less, since it is "
                     "lighter and less stable.", "correct": False,
             "why": "Being lighter makes the same push change its speed "
                    "by MORE, not less; stability is not the issue here."},
            {"text": "The loaded trolley changes speed by less, because it "
                     "has more mass.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ────────────────────────────────
    {
        "id": "p4-04-h07",
        "band": "harder",
        "text": "A hammer thrower swings a hammer in a circle at a constant "
                "speed before releasing it. While it is being swung, is a "
                "resultant force acting on it, and what does that force "
                "do?",
        "options": [
            {"text": "Yes — a resultant force acts continuously, "
                     "constantly changing the direction of the hammer's "
                     "motion.", "correct": True},
            {"text": "No, because its speed never changes while it is "
                     "being swung.", "correct": False,
             "why": "A constant speed does not mean no resultant force; "
                    "the direction is changing the whole time, which is "
                    "itself a change of motion."},
            {"text": "Yes, and that force is making the hammer travel faster and faster the longer the thrower keeps swinging it.", "correct": False,
             "why": "The stated speed is constant, so the force is not "
                    "adding speed — it is bending the path into a "
                    "circle."},
            {"text": "No, because forces can only ever act on objects "
                     "that are speeding up or slowing down, never on ones "
                     "moving at a constant speed.", "correct": False,
             "why": "A force can also act to change direction alone, "
                    "exactly as it does here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h08",
        "band": "harder",
        "text": "A car goes round a roundabout at a genuinely constant "
                "speed. A student says no force is needed because the "
                "speedometer reading never changes. What is wrong with "
                "this?",
        "options": [
            {"text": "Nothing is wrong; a constant speedometer reading is proof enough that no resultant force can be acting on the car here.", "correct": False,
             "why": "The speedometer only measures speed, not direction, "
                    "and the direction is changing continuously on a "
                    "bend."},
            {"text": "Speed is only part of motion — a resultant force is "
                     "still needed because the car's direction is "
                     "constantly changing.", "correct": True},
            {"text": "The student is right about the force, but wrong "
                     "that the speed stays constant.", "correct": False,
             "why": "The scenario states the speed is genuinely constant; "
                    "the flaw is ignoring the changing direction, not the "
                    "speed."},
            {"text": "The car does need a force, but only because "
                     "roundabouts are built steeper than flat roads, not "
                     "because of anything to do with its direction.",
             "correct": False,
             "why": "Steepness has nothing to do with it — the reason a "
                    "force is needed is the continuously changing "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h09",
        "band": "harder",
        "text": "The Moon orbits the Earth at roughly the same speed the "
                "whole way round. Explain why a resultant force must still "
                "be acting on it.",
        "options": [
            {"text": "There is no resultant force acting, since the Moon's speed does not change, and a change of speed is what a force would produce.", "correct": False,
             "why": "Speed staying the same is not the whole picture — the "
                    "direction changes throughout the orbit, and that "
                    "needs a force too."},
            {"text": "A resultant force is needed only because the Moon "
                     "is so very far away from the Earth, further than "
                     "where ordinary forces would normally reach.",
             "correct": False,
             "why": "Distance from Earth is irrelevant to whether a force "
                    "is needed; what matters is the continuously changing "
                    "direction."},
            {"text": "Because the Moon's direction is continuously "
                     "changing as it goes round, and that is a change of "
                     "motion needing a force.", "correct": True},
            {"text": "The force is needed to stop the Moon from speeding "
                     "up.", "correct": False,
             "why": "Nothing here suggests the Moon is speeding up — the "
                    "force is bending its path, not adding to its speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h10",
        "band": "harder",
        "text": "A fairground waltzer spins riders around in a horizontal "
                "circle at what feels like a constant speed. Someone argues "
                "that because nothing is speeding them up or slowing them "
                "down, no force is needed. What is the flaw?",
        "options": [
            {"text": "There is no flaw at all — the argument holds for any fairground ride that keeps moving round in a circle at one speed.",
             "correct": False,
             "why": "The argument overlooks that direction is part of "
                    "motion; continually changing it needs a resultant "
                    "force."},
            {"text": "The flaw is that the ride is actually speeding up "
                     "throughout.", "correct": False,
             "why": "The scenario is given as constant speed — the "
                    "missing idea is about direction, not about speed "
                    "changing."},
            {"text": "The flaw is that riders feel a strong sideways push, "
                     "which on its own proves their whole argument wrong "
                     "regardless of any reasoning about direction.",
             "correct": False,
             "why": "Feeling a push is not the reasoning that matters here "
                    "— the physics reason is the continuously changing "
                    "direction requiring a resultant force."},
            {"text": "Changing direction is itself a change of motion, so "
                     "a resultant force is needed even without any change "
                     "in speed.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h11",
        "band": "harder",
        "text": "The same resultant force is applied to an empty shipping "
                "container and to one loaded with cargo, for the same "
                "length of time. A student claims the loaded one must end "
                "up going faster because it has more momentum to build. "
                "What is wrong with this reasoning?",
        "options": [
            {"text": "More mass means the same force produces a SMALLER "
                     "change in speed, so the loaded container ends up "
                     "going slower, not faster.", "correct": True},
            {"text": "Nothing is wrong — heavier objects always end up "
                     "faster under the same force.", "correct": False,
             "why": "It is the opposite: for the same force and time, "
                    "more mass means a smaller change in speed."},
            {"text": "The reasoning is correct only if the containers "
                     "start from rest.", "correct": False,
             "why": "Whether or not they start from rest, more mass still "
                    "means a smaller change for the same force and time."},
            {"text": "The mistake is only in the word 'momentum', not in "
                     "the conclusion.", "correct": False,
             "why": "The conclusion itself is wrong too — the loaded "
                    "container changes speed by less, not more."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h12",
        "band": "harder",
        "text": "A canoe carries first a light paddler and then a heavier "
                "one, and is pushed off the bank with exactly the same "
                "force each time. The lighter paddler's canoe ends up "
                "moving faster. A friend says this must mean the force was "
                "bigger for the light paddler. Is that the only possible "
                "explanation?",
        "options": [
            {"text": "Yes, a bigger final speed always means a bigger "
                     "force was used.", "correct": False,
             "why": "A smaller mass changes speed by more even under an "
                    "IDENTICAL force, so the force need not have "
                    "differed."},
            {"text": "No — even with an identical force, less mass alone "
                     "would make the canoe's speed change more.",
             "correct": True},
            {"text": "Yes, unless the water resistance was different.",
             "correct": False,
             "why": "Water resistance is a separate factor; the direct "
                    "explanation here is simply the difference in mass, "
                    "which alone explains it."},
            {"text": "No, because mass has no effect on how much a force "
                     "changes speed.", "correct": False,
             "why": "Mass has exactly the opposite effect claimed here: "
                    "more mass makes a given force change the speed by "
                    "less, and less mass by more."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h13",
        "band": "harder",
        "text": "Two identical drones, one carrying extra batteries, are "
                "both given the same thrust force for the same time from a "
                "standing start. The lighter drone reaches a higher speed. "
                "Explain why, without assuming the thrust was different.",
        "options": [
            {"text": "The lighter drone must have received more thrust, "
                     "since it went faster.", "correct": False,
             "why": "The question states the thrust and time are the same "
                    "for both — the difference is explained by mass, not "
                    "by unequal thrust."},
            {"text": "The extra batteries make the heavier drone's motors "
                     "noticeably weaker, which is why it cannot keep pace "
                     "with the lighter one at all.", "correct": False,
             "why": "Nothing about carrying extra weight changes how "
                    "strong the motors are; the thrust is stated as "
                    "identical."},
            {"text": "For the same thrust and time, the drone with less "
                     "mass gains more speed, because mass affects how much "
                     "a force changes motion.", "correct": True},
            {"text": "Speed reached has nothing to do with mass, only with "
                     "thrust.", "correct": False,
             "why": "Mass does affect it: a smaller mass changes speed by "
                    "more for the same force, which is exactly the effect "
                    "described."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h14",
        "band": "harder",
        "text": "A cyclist and, separately, a cyclist towing a loaded "
                "trailer both experience the same forward resultant force "
                "for the same time from rest. A student argues that towing "
                "the trailer must reduce the forward force, since the "
                "cyclist with the trailer ends up slower. Assess this "
                "argument.",
        "options": [
            {"text": "The argument is correct, since a lower final speed "
                     "always means a smaller force.", "correct": False,
             "why": "A lower final speed can be fully explained by the "
                    "extra mass alone, with the force staying exactly the "
                    "same."},
            {"text": "The argument is correct, but only because trailers "
                     "create extra air resistance.", "correct": False,
             "why": "The scenario already fixes the resultant force as "
                    "identical in both cases; extra mass alone is enough "
                    "to explain the smaller change."},
            {"text": "The argument is wrong, because mass cannot affect "
                     "how a force changes speed.", "correct": False,
             "why": "Mass is exactly what does affect it — more mass "
                    "means a smaller change in speed for the same force "
                    "and time."},
            {"text": "The argument is unnecessary — an identical force "
                     "still produces a smaller change in speed on the "
                     "greater mass of cyclist-plus-trailer.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h15",
        "band": "harder",
        "text": "A satellite is nudged slightly by a tiny thruster burn and "
                "then coasts with the thruster off for years, its speed "
                "unchanged in that direction. Someone argues the "
                "thruster's push must still be acting weakly the whole "
                "time to explain the unchanged speed. What is the correct "
                "physics?",
        "options": [
            {"text": "No ongoing push is needed at all — with nothing "
                     "resisting it, the satellite needs no force "
                     "whatsoever to keep the speed the burn gave it.",
             "correct": True},
            {"text": "The push does continue, but at an extremely low level that instruments cannot detect, since a thruster burn leaves a faint trace of thrust inside the craft for years afterwards.", "correct": False,
             "why": "There is no mechanism for a thruster burn to keep "
                    "acting after it ends; a force requires ongoing "
                    "contact or interaction, and there is none here."},
            {"text": "The push is stored in the satellite's fuel tanks and "
                     "released gradually.", "correct": False,
             "why": "Stored fuel that is not being burned supplies no "
                    "force at all; the burn itself is what mattered, and "
                    "it is over."},
            {"text": "The unchanged speed proves the satellite is still accelerating very slowly, because anything coasting in space gains a little speed each year.", "correct": False,
             "why": "An unchanged speed is the opposite of accelerating — "
                    "it shows nothing is left over to change the motion."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h16",
        "band": "harder",
        "text": "In 1977 the Voyager probes left Earth under rocket power "
                "and have travelled for decades with their main engines "
                "off. Explain, without inventing any ongoing force, why "
                "they have not needed continuous power to keep moving.",
        "options": [
            {"text": "Their engines give tiny occasional bursts that go unreported, because a probe that had stopped burning fuel altogether would gradually lose the speed it had built up.", "correct": False,
             "why": "The question specifies the engines are off; "
                    "explaining their continued motion does not require "
                    "inventing extra thrust."},
            {"text": "Moving needs no force at all; with almost nothing "
                     "out there to resist them, the probes simply keep the "
                     "speed their engines gave them.", "correct": True},
            {"text": "The Sun's gravity pushes them steadily forward from behind, giving each probe a small shove outwards that keeps its speed up year after year.", "correct": False,
             "why": "The Sun's gravity pulls them BACK, very slightly, "
                    "rather than pushing them forward — it is not what "
                    "keeps them going."},
            {"text": "Deep space itself pushes objects along once they "
                     "reach it.", "correct": False,
             "why": "Empty space exerts no force on anything; it is "
                    "precisely the ABSENCE of resistance that lets the "
                    "probes keep going."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h17",
        "band": "harder",
        "text": "A curling stone is released and, on an unusually smooth "
                "sheet, travels almost the full length of the rink at a "
                "nearly constant speed. A commentator says the stone 'is "
                "still being pushed by the momentum of the throw.' Correct "
                "this statement using the idea that a force cannot be "
                "stored.",
        "options": [
            {"text": "Momentum is a kind of stored force that keeps the "
                     "stone moving.", "correct": False,
             "why": "A force cannot be stored as anything, including as "
                    "'momentum' in this everyday sense — no force is "
                    "acting on the stone at all once it is released."},
            {"text": "The commentator is right, but the push is weakening the whole way down the rink, which is why the stone finally comes to rest near the far end instead of carrying on.", "correct": False,
             "why": "There is no ongoing push to weaken. Once released, "
                    "the stone needs no force to continue at a steady "
                    "speed."},
            {"text": "The throw's force ended the instant the hand "
                     "released the stone; nothing is pushing it — it needs "
                     "no force to keep going at a steady speed.",
             "correct": True},
            {"text": "The ice itself is quietly pushing the stone along the whole way, since a polished surface returns a little of the push it was given at the start.", "correct": False,
             "why": "The ice resists the stone very slightly rather than "
                    "pushing it forward; nothing is driving it along."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h18",
        "band": "harder",
        "text": "A student watches a video of an astronaut giving a wrench "
                "a gentle push in the International Space Station, and it "
                "drifts across the cabin at a constant speed until it hits "
                "the far wall. The student writes: 'the wrench keeps a bit "
                "of the push stored inside it the whole way across.' "
                "Rewrite this correctly.",
        "options": [
            {"text": "The push is stored but is far too small to measure "
                     "once it is moving.", "correct": False,
             "why": "A push cannot be stored inside an object in any "
                    "amount, measurable or not — it simply ends when "
                    "contact ends."},
            {"text": "The wrench is being pushed by the air inside the "
                     "cabin the whole way across.", "correct": False,
             "why": "Air resistance would act against the motion, not "
                    "maintain it, and in any case moving at a steady speed "
                    "needs no such push."},
            {"text": "The wrench slowly loses its stored push and would eventually stop even with nothing in its way, because the push it was given is spent a little at a time as it crosses the cabin on its own.",
             "correct": False,
             "why": "With nothing resisting it, the wrench would never "
                    "slow down at all — there is no stored push to lose in "
                    "the first place."},
            {"text": "There is nothing stored inside the wrench at all; "
                     "the push ended the instant the astronaut's hand let "
                     "go, and the wrench needs no force to keep drifting "
                     "at that steady speed.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h19",
        "band": "harder",
        "text": "A resultant force of 3 N acting for 2 seconds changes a "
                "trolley's speed by 6 m/s. If BOTH the force and the time "
                "are doubled, by how much does the speed change?",
        "options": [
            {"text": "24 m/s", "correct": True},
            {"text": "12 m/s", "correct": False,
             "why": "That only accounts for one of the two doublings, not "
                    "both together."},
            {"text": "48 m/s", "correct": False,
             "why": "That scales the original change up by one factor of "
                    "two too many."},
            {"text": "6 m/s", "correct": False,
             "why": "That is the original change with no scaling applied "
                    "at all, even though both the force and the time have "
                    "doubled."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h20",
        "band": "harder",
        "text": "A force of 4 N acting for 3 seconds gives a skateboarder a "
                "speed change of 6 m/s. If the force is halved but the "
                "time is trebled, what is the new speed change?",
        "options": [
            {"text": "3 m/s", "correct": False,
             "why": "That halves the change for the smaller force but forgets that the time has also been trebled."},
            {"text": "9 m/s", "correct": True},
            {"text": "18 m/s", "correct": False,
             "why": "That trebles the original change without accounting "
                    "for the force being halved at the same time."},
            {"text": "6 m/s", "correct": False,
             "why": "That assumes no net change at all, but halving the "
                    "force and trebling the time do not exactly cancel — "
                    "they leave a net increase."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h21",
        "band": "harder",
        "text": "A go-kart under a 5 N force for 2 seconds changes speed by "
                "4 m/s. The same kart is then given a 10 N force for 4 "
                "seconds instead. What is the new change in speed?",
        "options": [
            {"text": "8 m/s", "correct": False,
             "why": "That accounts for only the doubled force or the "
                    "doubled time, not both together."},
            {"text": "4 m/s", "correct": False,
             "why": "That is the original change, but both the force and "
                    "the time have increased here."},
            {"text": "16 m/s", "correct": True},
            {"text": "32 m/s", "correct": False,
             "why": "That scales up by eight rather than by the fourfold "
                    "increase from doubling both force and time."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h22",
        "band": "harder",
        "text": "A resultant force of 6 N acting on a trolley for 5 seconds "
                "produces a 10 m/s change in speed. If the force is "
                "reduced to 3 N and the time is cut to 1 second, what is "
                "the new change in speed?",
        "options": [
            {"text": "5 m/s", "correct": False,
             "why": "That only accounts for the force being halved, "
                    "ignoring that the time has also been cut to a "
                    "fifth."},
            {"text": "2 m/s", "correct": False,
             "why": "That only accounts for the time being cut to a "
                    "fifth, ignoring that the force has also been halved."},
            {"text": "10 m/s", "correct": False,
             "why": "That treats the two reductions as having no effect at "
                    "all, when together they reduce the change to a tenth "
                    "of what it was."},
            {"text": "1 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h23",
        "band": "harder",
        "text": "A student writes: 'A resultant force is only needed to "
                "start something moving — once it's going, it looks after "
                "itself.' Which reply best corrects this?",
        "options": [
            {"text": "A resultant force is needed for ANY change of "
                     "motion, not just starting — including speeding up, "
                     "slowing down and turning.", "correct": True},
            {"text": "The student is completely right, and this is exactly what balanced forces show: once the forces on something balance, its motion looks after itself with nothing further needed.", "correct": False,
             "why": "Balanced forces (no resultant) explain why steady "
                    "motion needs nothing further — that is different from "
                    "claiming a force is 'only' needed to start motion."},
            {"text": "The student is wrong because forces are needed even for steady motion, and something must keep supplying one for as long as an object keeps moving.", "correct": False,
             "why": "Steady motion in a straight line needs no resultant "
                    "force at all — the flaw is limiting force to "
                    "starting, not this."},
            {"text": "The student is wrong because objects never keep "
                     "moving once started.", "correct": False,
             "why": "Objects do keep moving once started, exactly as long "
                    "as nothing changes their motion — this is not the "
                    "flaw in the statement."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h24",
        "band": "harder",
        "text": "A student says: 'If two forces are unequal, the bigger one "
                "wins and the object moves in that direction, dragging the "
                "smaller force along with it.' What is the accurate "
                "correction?",
        "options": [
            {"text": "The correction is right that the bigger force wins, "
                     "but the smaller one is destroyed rather than dragged "
                     "along.", "correct": False,
             "why": "Neither force is destroyed; both continue acting, "
                    "but together they combine into one resultant force."},
            {"text": "It is not a contest — the two forces simply combine "
                     "into a single resultant, in the direction and size "
                     "given by that combination.", "correct": True},
            {"text": "The student's picture is essentially correct for "
                     "any pair of unequal forces.", "correct": False,
             "why": "Describing it as a 'contest' with a winner misses "
                    "that forces combine mathematically into a resultant "
                    "rather than one overpowering the other."},
            {"text": "The correction is that only the smaller force "
                     "actually acts on the object.", "correct": False,
             "why": "Both forces genuinely act; the resultant reflects "
                    "both of them combined, not just the smaller one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h25",
        "band": "harder",
        "text": "A student claims: 'An object moving at a steady speed must "
                "have a forward force bigger than the backward ones, or it "
                "would slow down.' Identify the flaw.",
        "options": [
            {"text": "There is no flaw; a bigger forward force is needed "
                     "to maintain any steady speed.", "correct": False,
             "why": "A bigger forward force would make the object speed "
                    "up, not hold a steady speed — equal forces are what "
                    "keep speed steady."},
            {"text": "The flaw is that backward forces do not exist once "
                     "an object is moving steadily.", "correct": False,
             "why": "Backward forces such as resistance are still acting; "
                    "they are simply matched exactly by the forward "
                    "force."},
            {"text": "A steady speed means the forces are exactly "
                     "balanced, with the forward and backward forces "
                     "equal — not the forward one bigger.", "correct": True},
            {"text": "The flaw is that speed and force are unrelated "
                     "ideas entirely.", "correct": False,
             "why": "Force and speed are related through the resultant; "
                    "the specific flaw here is about which force needs to "
                    "be bigger, not whether they relate at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h26",
        "band": "harder",
        "text": "A student argues: 'A resultant force changes an object's "
                "mass as well as its motion, because a stronger push makes "
                "something feel heavier.' Correct this claim.",
        "options": [
            {"text": "The claim is correct, because forces do increase an object's mass while they act, which is why a heavily loaded trolley grows harder to push the faster it is already going.", "correct": False,
             "why": "A force never changes how much matter an object "
                    "contains; only its motion changes."},
            {"text": "The claim is correct, but only for very large "
                     "forces.", "correct": False,
             "why": "No size of force changes an object's mass; the claim "
                    "is wrong regardless of how big the force is."},
            {"text": "The claim is wrong because forces cannot be felt as heaviness at all, and what a push feels like says nothing about what is happening to the object.", "correct": False,
             "why": "A push CAN feel like extra weight in the moment; the "
                    "actual error is claiming this changes the object's "
                    "true mass."},
            {"text": "A resultant force changes only an object's motion; "
                     "feeling heavier under a push is not the same as the "
                     "object's mass actually changing.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h27",
        "band": "harder",
        "text": "A trolley starts at rest. For the first 2 seconds a 4 N "
                "forward force acts, changing its speed by 4 m/s. For the "
                "next 2 seconds the force switches to 4 N BACKWARD "
                "instead. What is the trolley's speed at the end of the 4 "
                "seconds?",
        "options": [
            {"text": "0 m/s", "correct": True},
            {"text": "4 m/s", "correct": False,
             "why": "That ignores the second stage entirely, where the "
                    "backward force undoes exactly the change the first "
                    "stage made."},
            {"text": "8 m/s", "correct": False,
             "why": "That adds both changes as if they were in the same "
                    "direction, but the second force acts the opposite "
                    "way."},
            {"text": "-4 m/s", "correct": False,
             "why": "The two equal and opposite changes cancel to zero; "
                    "they do not leave a net backward speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h28",
        "band": "harder",
        "text": "A skater is pushed forward, gaining 3 m/s, and then a "
                "friend gives an equal and opposite push for the same "
                "length of time, cancelling the forward force exactly. "
                "What happens to the skater's speed during the second "
                "push?",
        "options": [
            {"text": "It keeps rising, since two pushes have now acted on "
                     "the skater.", "correct": False,
             "why": "The second push is in the OPPOSITE direction and "
                    "undoes the first, rather than adding to it."},
            {"text": "It falls back towards 0 m/s, undoing the first "
                     "push's effect.", "correct": True},
            {"text": "It stays at 3 m/s throughout the second push.",
             "correct": False,
             "why": "An equal and opposite force is a resultant against "
                    "the existing motion, so the speed changes — it does "
                    "not stay fixed."},
            {"text": "It becomes impossible to predict without knowing the "
                     "skater's mass.", "correct": False,
             "why": "The two pushes are stated as equal and opposite for "
                    "the same time, so the second exactly reverses the "
                    "first's effect regardless of mass."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h29",
        "band": "harder",
        "text": "A car accelerates under the engine's forward force for 5 "
                "seconds, then the driver lifts off the accelerator so the "
                "only resultant force becomes air resistance and friction, "
                "now acting backward. What must be true about the car's "
                "speed after the accelerator is released?",
        "options": [
            {"text": "It stays exactly the same, since the engine has stopped actively pushing the car along the road.", "correct": False,
             "why": "With a genuine resultant now acting backward, the "
                    "speed changes — it does not simply freeze at its "
                    "current value."},
            {"text": "It keeps increasing for a short while out of habit.",
             "correct": False,
             "why": "Once the resultant points backward, the speed begins "
                    "falling immediately, whatever it was doing before."},
            {"text": "It starts to decrease, because the resultant force "
                     "is now against the direction of travel.",
             "correct": True},
            {"text": "It cannot change at all unless the brakes are also "
                     "applied firmly, on top of whatever resistance is "
                     "already acting on the car.", "correct": False,
             "why": "The stated backward resultant from resistance and "
                    "friction is enough on its own to start reducing the "
                    "speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h30",
        "band": "harder",
        "text": "A remote-control car speeds up under a forward force for 3 "
                "seconds, reaching 6 m/s, and then the forward force is "
                "removed completely while a separate constant backward "
                "resistive force remains, acting for the next 3 seconds. "
                "Which statement about its motion is correct?",
        "options": [
            {"text": "The speed stays at 6 m/s, since the driving force "
                     "has stopped.", "correct": False,
             "why": "Stopping the driving force is not the same as no "
                    "resultant force — the resistive force is still "
                    "acting, and unopposed, so the speed changes."},
            {"text": "The speed keeps rising, because the car was already "
                     "moving fast.", "correct": False,
             "why": "Already moving fast does not sustain or add to "
                    "speed; the resultant now acting is backward, which "
                    "reduces speed rather than raising it."},
            {"text": "The speed instantly drops all the way to 0 m/s the "
                     "very moment the forward force stops acting on the "
                     "car.", "correct": False,
             "why": "The change is gradual, building up over the 3 "
                    "seconds the backward force acts, not instantaneous."},
            {"text": "The speed decreases throughout those next 3 "
                     "seconds, because the only resultant force left "
                     "points backward.", "correct": True},
        ],
        "figure": None,
    },
]
