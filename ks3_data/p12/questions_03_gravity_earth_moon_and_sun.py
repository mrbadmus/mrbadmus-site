"""P12 lesson 03 — Gravity between Earth, Moon and Sun: twelve questions
(MRB-223).

Written against Design's page. The falling Moon, the four gravitational
pairs and the separation multiplier are hers.

The discriminations, in the order the lesson builds them:

  · gravity is an ATTRACTION between any two masses and never pushes;
  · both masses count, and the two forces in a pair are equal and opposite
    however different the bodies (`SPACE-09`);
  · the fall-off is the INVERSE SQUARE, not a straight proportion
    (`SPACE-10`);
  · an orbit is falling and missing, with no outward force anywhere in it
    (`SPACE-08`). The harder band sits here.

⚠️ POSITION IS AUTHORED — 1,3,0,2 · 2,0,3,1 · 0,2,1,3, three of each.

⚠️ Neither marked rung is restated: the two spacecraft at three times the
separation and the Sun–Earth pair at 3.5 × 10^22 N are the ladder's, and
nothing here reuses either.

⚠️ MRB-338 night 3 top-up (e10–e30, s10–s30, h10–h30): 21 more per band,
continuing each band's id sequence. Coverage, self-checks and content
decisions are in the executor's final report for this run.
"""

UNIT = "P12"
LESSON = "gravity-earth-moon-and-sun"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p12-03-e01",
        "band": "easier",
        "text": "Gravity between two masses is always which of these?",
        "options": [
            {"text": "A push", "correct": False,
             "why": "Gravity never pushes. There is no known circumstance in "
                    "which two masses repel each other gravitationally."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "A pull, always and only", "correct": True},
            {"text": "A push or a pull, depending on the two masses",
             "correct": False,
             "why": "Electric charges can do either. Gravity only ever "
                    "attracts, whatever the two masses are."},
            {"text": "Neither, until the two objects touch", "correct": False,
             "why": "Gravity is a non-contact force. It reaches across empty "
                    "space with nothing in between."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e02",
        "band": "easier",
        "text": "Two objects are moved twice as far apart. What happens to "
                "the gravitational pull between them?",
        "options": [
            {"text": "It doubles", "correct": False,
             "why": "More distance means less pull, never more."},
            {"text": "It halves", "correct": False,
             "why": "That is a straight proportion. Gravity falls off as the "
                    "SQUARE of the distance, so it drops further than that."},
            {"text": "It stays the same", "correct": False,
             "why": "Distance is one of the two things that set the strength "
                    "of a gravitational pull."},
            {"text": "It falls to a quarter", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e03",
        "band": "easier",
        "text": "Which pairs of objects have a gravitational pull between "
                "them?",
        "options": [
            {"text": "Every pair of objects there is", "correct": True},
            {"text": "Only pairs where at least one is a planet or a star",
             "correct": False,
             "why": "Every mass attracts every other mass. Large bodies are "
                    "simply the only pairs where the pull is big enough to "
                    "notice."},
            {"text": "Only pairs that are close enough to touch",
             "correct": False,
             "why": "Gravity acts across empty space. The Sun and the Earth "
                    "are 150 million km apart."},
            {"text": "Only pairs where both objects are in space",
             "correct": False,
             "why": "You and the Earth are a pair, and neither of you is in "
                    "space."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e04",
        "band": "easier",
        "text": "What is an orbit?",
        "options": [
            {"text": "A path along which gravity has been cancelled out "
                     "completely", "correct": False,
             "why": "Nothing cancels gravity. An orbiting body is being "
                    "pulled the whole time, which is why its path curves."},
            {"text": "A groove in space that a moon or a planet runs along",
             "correct": False,
             "why": "There is nothing there to run along. The path is the "
                    "result of a pull and a sideways motion, not a track."},
            {"text": "A body falling towards another while moving sideways "
                     "fast enough to keep missing it", "correct": True},
            {"text": "A balance between gravity pulling inwards and some "
                     "other force pushing outwards", "correct": False,
             "why": "There is no outward force. If the forces balanced, the "
                    "body would travel in a straight line and leave."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p12-03-s01",
        "band": "standard",
        "text": "Two satellites are moved four times as far apart as they "
                "started. The pull between them was 8 N. What is it now?",
        "options": [
            {"text": "2 N", "correct": False,
             "why": "That divides by 4. The inverse square law divides by 4 "
                    "squared, which is 16."},
            {"text": "32 N", "correct": False,
             "why": "That multiplies. Moving further apart always weakens a "
                    "gravitational pull."},
            {"text": "0.5 N", "correct": True},
            {"text": "0 N", "correct": False,
             "why": "Gravity never reaches zero, however far apart two masses "
                    "are. It gets small, and it stays."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s02",
        "band": "standard",
        "text": "You are standing on the Earth. Which statement about the "
                "gravitational forces is right?",
        "options": [
            {"text": "You pull the Earth up exactly as hard as it pulls you "
                     "down", "correct": True},
            {"text": "The Earth pulls you down and you do not pull it at all",
             "correct": False,
             "why": "Every mass attracts every other mass. You are pulling "
                    "the Earth, and the force is the same size as the one on "
                    "you."},
            {"text": "You pull the Earth, but far less hard, because you are "
                     "far smaller", "correct": False,
             "why": "Both masses appear in the same calculation, so the pair "
                    "of forces is equal. Your smallness changes the EFFECT, "
                    "not the force."},
            {"text": "Neither pulls the other, because you are touching the "
                     "ground", "correct": False,
             "why": "Touching has nothing to do with it. Gravity acts across "
                    "any separation, contact or not."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s03",
        "band": "standard",
        "text": "The Sun pulls the Earth and the Earth pulls the Sun with "
                "equal forces. Why does the Earth move round the Sun rather "
                "than the other way about?",
        "options": [
            {"text": "Because the Sun's pull is stronger, even though the two "
                     "forces are called equal", "correct": False,
             "why": "The two forces really are equal. Calling them equal and "
                    "then treating one as stronger is the contradiction the "
                    "question is testing."},
            # ⊕ MRB-297 · 1 Sep 2026 — the third option was widened so the
            # correct answer stops being resolvable as the second-longest.
            {"text": "Because the Sun is anchored by the pull of the rest of "
                     "the galaxy", "correct": False,
             "why": "The Sun is not anchored by anything. The galaxy's pull "
                    "is what makes it orbit the centre of the galaxy, not "
                    "what holds it still."},
            {"text": "Because the Sun has far more mass, so the same force "
                     "moves it far less", "correct": True},
            {"text": "Because the Earth is moving and the Sun is standing "
                     "still", "correct": False,
             "why": "Both are moving. The Sun does wobble under the Earth's "
                    "pull — just by a very small amount."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s04",
        "band": "standard",
        "text": "A student says gravity must be strong between two people "
                "standing next to each other, because they are very close "
                "together. What is wrong?",
        "options": [
            {"text": "Closeness makes no difference to gravity at all, because "
                     "only the two masses decide how strong the pull is",
             "correct": False,
             "why": "Closeness makes a great deal of difference — it is one "
                    "of the two things that set the strength."},
            {"text": "The two masses are tiny, so even at that distance the "
                     "pull is far too small to notice", "correct": True},
            {"text": "Gravity only acts between objects that are far apart, so "
                     "two things side by side attract each other least of all",
             "correct": False,
             "why": "Gravity acts at every separation, and is strongest when "
                    "objects are close."},
            {"text": "People are not massive enough to feel gravity at all, so "
                     "a pull needs at least one body the size of a planet",
             "correct": False,
             "why": "They feel the Earth's gravity perfectly well. What is "
                    "missing is enough mass on BOTH sides of the pair."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p12-03-h01",
        "band": "harder",
        "text": "A probe is released above the Moon with no sideways motion "
                "at all. What happens, and why?",
        "options": [
            {"text": "It falls straight down onto the Moon, because there is "
                     "nothing to curve its path", "correct": True},
            {"text": "It goes into orbit, because anything released in "
                     "space orbits something", "correct": False,
             "why": "An orbit needs the sideways motion as well as the pull. "
                    "With only the pull, there is nothing to miss with."},
            {"text": "It stays exactly where it is, because it has no "
                     "weight out there in space", "correct": False,
             "why": "It has a weight — the Moon's field is pulling on it. "
                    "That pull is what makes it fall."},
            {"text": "It drifts slowly away, because the Moon's gravity is "
                     "far too weak to hold it", "correct": False,
             "why": "The Moon's field is about a sixth of Earth's, which is "
                    "weak but nowhere near nothing. It pulls the probe in."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h02",
        "band": "harder",
        "text": "The Earth–Moon pull is about 2 × 10^20 N. If the Moon were "
                "somehow moved to five times its present distance, roughly "
                "what would the pull become?",
        "options": [
            {"text": "About 4 × 10^19 N", "correct": False,
             "why": "That divides by 5. The inverse square law divides by 5 "
                    "squared, which is 25."},
            {"text": "About 1 × 10^21 N", "correct": False,
             "why": "That multiplies by 5. Moving further apart weakens the "
                    "pull."},
            {"text": "About 8 × 10^18 N", "correct": True},
            {"text": "About 2 × 10^20 N still, because neither mass has "
                     "changed", "correct": False,
             "why": "Both masses matter and so does the separation. Changing "
                    "any one of the three changes the force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h03",
        "band": "harder",
        "text": "On a fairground ride that spins you in a circle, you feel "
                "pressed against the outside wall. How does that compare with "
                "what keeps the Moon in orbit?",
        "options": [
            {"text": "It is the same effect: an outward force acts on you "
                     "and on the Moon alike", "correct": False,
             "why": "There is no outward force in either case. The wall "
                    "pushes you INWARDS, which is what bends your path."},
            {"text": "It is the opposite: the ride pushes you outwards "
                     "while gravity pulls the Moon steadily inwards",
             "correct": False,
             "why": "The ride does not push outwards. The only force it "
                    "applies to you is the wall pushing in."},
            {"text": "Both are the same thing: your body carrying on straight "
                     "while something bends its path inwards", "correct": True},
            {"text": "They are unrelated, because the ride uses a real "
                     "force and gravity is not one", "correct": False,
             "why": "Gravity is as real a force as the wall's push. Both bend "
                    "a path that would otherwise be straight."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h04",
        "band": "harder",
        "text": "Astronomers detect a distant star wobbling slightly, in a "
                "regular rhythm. What is the best explanation?",
        "options": [
            {"text": "The star is pulsing in and out in a steady rhythm as "
                     "it burns its fuel", "correct": False,
             "why": "Some stars do pulse, and that changes their brightness "
                    "rather than moving them from side to side."},
            {"text": "The star is being pulled by something orbiting it, "
                     "because gravitational pulls come in pairs", "correct": True},
            {"text": "Something is pushing the star first from one side and "
                     "then from the other", "correct": False,
             "why": "Gravity never pushes, and there is nothing in the "
                    "picture that could."},
            {"text": "The light is bending on its way to us, so the star "
                     "only appears to move from side to side",
             "correct": False,
             "why": "Light does bend near very massive objects, and it would "
                    "not produce a regular repeating rhythm."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p12-03-e05",
        "band": "easier",
        "text": "Gravity acts between…",
        "options": [
            {"text": "any two masses", "correct": True},
            {"text": "planets and stars only", "correct": False,
             "why": "It acts between any two masses; a planet's is simply "
                    "large enough to notice."},
            {"text": "objects that are touching", "correct": False,
             "why": "It reaches across empty space, which is how the Moon is "
                    "held."},
            {"text": "magnets and magnetic materials", "correct": False,
             "why": "That is magnetism, a different non-contact force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e06",
        "band": "easier",
        "text": "Does gravity need something in the gap to act across it?",
        "options": [
            {"text": "Yes — the air carries it", "correct": False,
             "why": "It acts through the vacuum of space, where there is no "
                    "air at all."},
            {"text": "Yes, but only over very long distances",
             "correct": False,
             "why": "It needs nothing in between at any distance."},
            {"text": "No, nothing is needed in between", "correct": True},
            {"text": "Only when both objects are moving", "correct": False,
             "why": "Two stationary masses attract each other just as well."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e07",
        "band": "easier",
        "text": "What makes the gravitational pull between two objects "
                "stronger?",
        "options": [
            {"text": "Larger masses on either side", "correct": True},
            {"text": "A greater distance between them", "correct": False,
             "why": "Distance weakens it, and quickly."},
            {"text": "One of them being made of metal", "correct": False,
             "why": "What a thing is made of makes no difference; only how "
                    "much mass it has."},
            {"text": "One of them being charged", "correct": False,
             "why": "Charge belongs to the electrostatic force, not to "
                    "gravity."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e08",
        "band": "easier",
        "text": "An orbiting body is best described as…",
        "options": [            {"text": "held up by a force flinging it outwards",
             "correct": False,
             "why": "There is no outward force; gravity is the only one "
                    "acting."},
            {"text": "beyond the reach of gravity", "correct": False,
             "why": "Gravity is exactly what keeps it in orbit; without it "
                    "the body would fly off straight."},
            {"text": "permanently falling and permanently missing",
             "correct": True},
            {"text": "moving in a straight line at a steady speed",
             "correct": False,
             "why": "A straight line is what it would do with no force; the "
                    "orbit is a constant turn."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e09",
        "band": "easier",
        "text": "Is there gravity where the International Space Station "
                "orbits?",
        "options": [            {"text": "No — that is why astronauts float", "correct": False,
             "why": "They float because they are falling with the station, "
                    "not because gravity has gone."},
            {"text": "Yes, but only about a hundredth of the ground value",
             "correct": False,
             "why": "At that height it is close to nine tenths of the "
                    "surface value."},
            {"text": "No, because it is above the atmosphere",
             "correct": False,
             "why": "Air has nothing to do with gravity; the field reaches "
                    "far beyond the atmosphere."},
            {"text": "Yes, nearly as strong as at the ground", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p12-03-s05",
        "band": "standard",
        "text": "Two objects 2 m apart attract with 36 N. They are moved to "
                "6 m apart. What is the pull now?",
        "options": [            {"text": "4 N", "correct": True},
            {"text": "12 N", "correct": False,
             "why": "That divides by three, in step with the distance; the "
                    "fall goes with the SQUARE."},
            {"text": "108 N", "correct": False,
             "why": "Moving further apart always weakens the pull."},
            {"text": "18 N", "correct": False,
             "why": "That halves it, which matches neither the distance nor "
                    "its square."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s06",
        "band": "standard",
        "text": "Why does the Moon not simply fall into the Earth?",
        "options": [            {"text": "Because the Earth's gravity does not reach that far",
             "correct": False,
             "why": "It reaches easily; it is what holds the Moon in orbit at "
                    "all."},
            {"text": "Because an outward force balances the pull",
             "correct": False,
             "why": "There is no outward force; gravity is the only one "
                    "acting on it."},
            {"text": "Because it is moving sideways fast enough to keep "
                     "missing",
             "correct": True},
            {"text": "Because it is too far away to be pulled", "correct": False,
             "why": "It is pulled constantly — that is what curves its path "
                    "into an orbit."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s07",
        "band": "standard",
        "text": "Why does the Moon not fly off into space instead?",
        "options": [            {"text": "Because space pushes back on it", "correct": False,
             "why": "Space pushes on nothing; there is no material there to "
                    "do it."},
            {"text": "Because the Sun holds it in place", "correct": False,
             "why": "The Sun pulls it too, but the Earth's pull is what keeps "
                    "it in orbit around us."},
            {"text": "Because it is not moving fast enough to escape the "
                     "atmosphere",
             "correct": False,
             "why": "It is far above any atmosphere; gravity is what holds "
                    "it."},
            {"text": "Because the Earth's gravity keeps pulling it round",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s08",
        "band": "standard",
        "text": "A student says the Sun must pull the Earth harder than the "
                "Earth pulls the Sun. What is right?",
        "options": [            {"text": "The two pulls are equal and opposite", "correct": True},
            {"text": "They are right — the more massive object always pulls "
                     "harder",
             "correct": False,
             "why": "The two forces in a gravitational pair are always "
                    "equal, whatever the masses."},
            {"text": "The Earth pulls harder, because it is closer to itself",
             "correct": False,
             "why": "Distance is the same for both, and it would not break "
                    "the equality anyway."},
            {"text": "Only the Sun pulls",
             "correct": False,
             "why": "Every gravitational force comes with an equal one the "
                    "other way."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s09",
        "band": "standard",
        "text": "Why is the gravitational pull between two people standing "
                "side by side far too small to notice?",
        "options": [            {"text": "Because gravity only acts on very large objects",
             "correct": False,
             "why": "It acts between any two masses; theirs are simply "
                    "tiny."},
            {"text": "Because they are too close together", "correct": False,
             "why": "Being close makes the pull larger, not smaller."},
            {"text": "Because their masses are tiny compared with a planet's",
             "correct": True},
            {"text": "Because the Earth's pull cancels it out", "correct": False,
             "why": "The Earth's pull acts downwards and does not cancel a "
                    "sideways one; the sideways pull is just minute."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p12-03-h05",
        "band": "harder",
        "text": "The pull between two masses is 100 N at 1 m. What is it at "
                "5 m?",
        "options": [            {"text": "20 N", "correct": False,
             "why": "That divides by five, in step with the distance rather "
                    "than with its square."},
            {"text": "50 N", "correct": False,
             "why": "That halves it, which matches neither rule."},
            {"text": "2500 N", "correct": False,
             "why": "Moving apart weakens the pull; nothing about separating "
                    "them strengthens it."},
            {"text": "4 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h06",
        "band": "harder",
        "text": "A satellite's engines are switched off for good. Why does it "
                "stay in orbit?",
        "options": [            {"text": "Because nothing stops its sideways motion, and gravity "
                     "keeps turning it",
             "correct": True},
            {"text": "Because the engines had built up a store of motion it "
                     "slowly uses",
             "correct": False,
             "why": "Nothing is stored and spent; with no resistance its "
                    "sideways motion simply continues."},
            {"text": "Because at that height gravity is exactly balanced by "
                     "another force",
             "correct": False,
             "why": "There is no second force; gravity acts alone and is "
                    "unbalanced."},
            {"text": "Because it is beyond the reach of the Earth's gravity",
             "correct": False,
             "why": "It is well inside it — otherwise it would travel "
                    "straight off."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h07",
        "band": "harder",
        "text": "Why is an orbit NOT a balance between gravity pulling in and "
                "a force flinging outwards?",
        "options": [
            {"text": "Because gravity is far too weak to balance anything at "
                     "that distance",
             "correct": False,
             "why": "It is easily strong enough; the trouble is that there is "
                    "nothing to balance."},
            {"text": "Because the two forces are equal, so the body would "
                     "stand still",
             "correct": False,
             "why": "No second force exists at all, so there is no pair to "
                    "compare."},
            {"text": "Because there is no outward force — gravity acts alone "
                     "and changes the direction",
             "correct": True},
            {"text": "Because an orbit needs no force of any kind",
             "correct": False,
             "why": "A constant change of direction needs a resultant force, "
                    "and gravity supplies it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h08",
        "band": "harder",
        "text": "Two spacecraft double their separation and the pull falls to "
                "a quarter, not a half. Why?",
        "options": [            {"text": "Because some of the pull is absorbed by the space "
                     "between them",
             "correct": False,
             "why": "Nothing absorbs gravity; empty space takes none of it."},
            {"text": "Because their masses fall as they separate",
             "correct": False,
             "why": "Neither mass changes; only the distance does."},
            {"text": "Because the pull falls with the SQUARE of the distance",
             "correct": True},
            {"text": "Because gravity acts in two directions at once",
             "correct": False,
             "why": "It does come in a pair, and that has nothing to do with "
                    "how it falls off."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h09",
        "band": "harder",
        "text": "The Earth pulls a 1 kg apple with 10 N. How hard does the "
                "apple pull the Earth?",
        "options": [            {"text": "Almost nothing, because the apple is tiny",
             "correct": False,
             "why": "Its mass is tiny and its pull is not: the two forces in "
                    "the pair are equal."},
            {"text": "Nothing at all", "correct": False,
             "why": "The Earth is not the only puller. Every gravitational "
                    "force comes with an equal one in the opposite "
                    "direction."},
            {"text": "Far more than 10 N, because the Earth is enormous",
             "correct": False,
             "why": "The Earth's size affects how hard IT pulls, and the pair "
                    "is still equal both ways."},
            {"text": "10 N, exactly as hard", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p12-03-e10",
        "band": "easier",
        "text": "Which two things decide how strong the gravitational "
                "pull between two objects is?",
        "options": [
            {"text": "The two masses involved, and the distance between "
                     "them", "correct": True},
            {"text": "The two masses involved, and how fast each one is "
                     "moving", "correct": False,
             "why": "How fast an object moves has no effect on the "
                    "gravitational pull on it; only its mass and its "
                    "position do."},
            {"text": "The distance between them, and what each object is "
                     "made of", "correct": False,
             "why": "Gravity treats every material alike — a kilogram of "
                    "rock and a kilogram of ice are pulled identically."},
            {"text": "How fast each one is moving, and what each object "
                     "is made of", "correct": False,
             "why": "Neither speed nor material affects a gravitational "
                    "pull; the two things that do are the masses and the "
                    "separation."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e11",
        "band": "easier",
        "text": "If the distance between two masses is reduced to a quarter "
                "of what it was, what happens to the pull between them?",
        "options": [
            {"text": "It falls to a quarter", "correct": False,
             "why": "Reducing the distance brings the masses closer, which "
                    "makes the pull stronger, not weaker."},
            {"text": "It becomes four times as strong", "correct": False,
             "why": "That matches the distance factor rather than its "
                    "square, which the inverse square law actually uses."},
            {"text": "It becomes sixteen times as strong", "correct": True},
            {"text": "It stays exactly the same", "correct": False,
             "why": "Distance is one of the two things that decide how "
                    "strong a gravitational pull is."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e12",
        "band": "easier",
        "text": "Two masses start 4 m apart and are then moved to 8 m "
                "apart. By what factor does the gravitational pull between "
                "them change?",
        "options": [
            {"text": "It doubles", "correct": False,
             "why": "More distance always weakens a gravitational pull, "
                    "never strengthens it."},
            {"text": "It falls to a quarter of what it was", "correct": True},
            {"text": "It falls to a half of what it was", "correct": False,
             "why": "That matches the distance factor (2 times further) "
                    "rather than its square, which the law actually uses."},
            {"text": "It stays the same", "correct": False,
             "why": "The separation has changed, and distance is one of the "
                    "two things that decide the strength of the pull."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e13",
        "band": "easier",
        "text": "Which of these correctly states the rule connecting "
                "gravity and distance?",
        "options": [
            {"text": "Doubling the distance leaves the pull unchanged",
             "correct": False,
             "why": "Distance genuinely affects the strength of a "
                    "gravitational pull."},
            {"text": "Doubling the distance doubles the pull", "correct": False,
             "why": "More distance weakens a pull; it never strengthens it."},
            {"text": "Doubling the distance halves the pull", "correct": False,
             "why": "That is a straight proportion; gravity follows an "
                    "inverse SQUARE law, so it falls further than a simple "
                    "half."},
            {"text": "Doubling the distance quarters the pull",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e14",
        "band": "easier",
        "text": "Two masses are moved to exactly half their original "
                "distance apart. What happens to the gravitational pull "
                "between them?",
        "options": [
            {"text": "It becomes four times as strong", "correct": True},
            {"text": "It becomes twice as strong", "correct": False,
             "why": "That matches the distance factor rather than its "
                    "square, which the inverse square law actually uses."},
            {"text": "It becomes half as strong", "correct": False,
             "why": "Moving closer together always makes a gravitational "
                    "pull stronger, never weaker."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "Distance is one of the two things that decide how "
                    "strong a gravitational pull is."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e15",
        "band": "easier",
        "text": "What did Newton conclude was special about the force "
                "pulling an apple to the ground and the force holding the "
                "Moon in its orbit?",
        "options": [
            {"text": "They are two separate forces that happen to behave "
                     "similarly", "correct": False,
             "why": "Newton's insight was precisely that they are not "
                    "separate at all — they are one and the same force."},
            {"text": "The force on the apple is far stronger, because the "
                     "apple is closer to the Earth", "correct": False,
             "why": "The same law connects the two, but Newton's conclusion "
                    "was about their being the same force, not about "
                    "comparing their sizes."},
            {"text": "The Moon's orbit has nothing to do with gravity at "
                     "all", "correct": False,
             "why": "The Moon's orbit is entirely a result of the Earth's "
                    "gravity acting on it."},
            {"text": "They are the very same force, acting between "
                     "different masses at different distances",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e16",
        "band": "easier",
        "text": "Which of these is a genuine example of two objects "
                "attracting each other gravitationally?",
        "options": [
            {"text": "Two magnets with opposite poles facing each other",
             "correct": False,
             "why": "That is magnetism, a different non-contact force from "
                    "gravity."},
            {"text": "The Earth and an orbiting satellite", "correct": True},
            {"text": "A balloon rubbed on a jumper sticking to a wall",
             "correct": False,
             "why": "That is static electricity, not gravity."},
            {"text": "Iron filings gathering around a bar magnet",
             "correct": False,
             "why": "That is magnetism again, not gravity."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e17",
        "band": "easier",
        "text": "Which of these is NOT an example of a non-contact force "
                "acting between two objects?",
        "options": [
            {"text": "Gravity pulling the Moon towards the Earth",
             "correct": False,
             "why": "This is gravity, which is one of the non-contact "
                    "forces."},
            {"text": "A hand pushing a shopping trolley", "correct": True},
            {"text": "Two like magnetic poles repelling each other",
             "correct": False,
             "why": "This is magnetism, another non-contact force."},
            {"text": "A charged balloon attracting someone's hair",
             "correct": False,
             "why": "This is a static electric force, another non-contact "
                    "force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e18",
        "band": "easier",
        "text": "A spacecraft travels far beyond the edge of the Solar "
                "System, further than any planet. Does the Sun's gravity "
                "still pull on it at all?",
        "options": [
            {"text": "No — the Sun's pull has a fixed range, and the "
                     "spacecraft has left it", "correct": False,
             "why": "Gravity has no fixed range at which it simply stops."},
            {"text": "No — gravity only acts between a star and its own "
                     "planets", "correct": False,
             "why": "Gravity acts between any two masses at all, not only "
                    "within a designated set of planets."},
            {"text": "Yes — the pull is far weaker there, but it never "
                     "reaches exactly zero", "correct": True},
            {"text": "Yes — the pull is exactly as strong there as it is "
                     "near the Sun", "correct": False,
             "why": "Gravity does weaken with distance; it would not be "
                    "exactly as strong so far away."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e19",
        "band": "easier",
        "text": "A satellite's engines fail completely, leaving only "
                "gravity to act on it. What single word best describes its "
                "motion afterwards?",
        "options": [
            {"text": "Floating", "correct": False,
             "why": "It is not simply drifting motionless — gravity is "
                    "actively pulling it the whole time."},
            {"text": "Falling", "correct": True},
            {"text": "Stopping", "correct": False,
             "why": "Nothing about losing its engines makes a satellite in "
                    "orbit slow down and stop."},
            {"text": "Repelling", "correct": False,
             "why": "Gravity never repels; it only ever attracts."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e20",
        "band": "easier",
        "text": "The Sun's gravity reaches all the way to the edge of the "
                "Solar System and beyond. What does this tell you about "
                "gravity's range?",
        "options": [
            {"text": "It has a fixed maximum range, beyond which it "
                     "switches off completely", "correct": False,
             "why": "Gravity has no such fixed cut-off distance."},
            {"text": "Its range depends on how bright the Sun is",
             "correct": False,
             "why": "Gravity's reach has nothing to do with how much light "
                    "a star gives off."},
            {"text": "It has no fixed edge — it simply gets weaker and "
                     "weaker with distance", "correct": True},
            {"text": "Its range is exactly the distance to the furthest "
                     "planet, Neptune", "correct": False,
             "why": "Gravity does not stop at Neptune; it continues, "
                    "weaker still, beyond it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e21",
        "band": "easier",
        "text": "Which correctly compares the gravitational pull between "
                "two ordinary 1 kg masses with the pull between the Earth "
                "and the Moon?",
        "options": [
            {"text": "The Earth-Moon pull is vastly stronger, because both "
                     "masses involved are enormously larger", "correct": True},
            {"text": "The two pulls are actually about the same size, "
                     "because gravity does not care about mass",
             "correct": False,
             "why": "Gravity strongly depends on both masses involved; "
                    "enormous masses like the Earth and the Moon give a "
                    "vastly bigger pull."},
            {"text": "The two 1 kg masses pull harder, because they are "
                     "usually much closer together", "correct": False,
             "why": "Even accounting for the shorter distance, the pull "
                    "between two 1 kg masses is unimaginably smaller than "
                    "the Earth-Moon pull."},
            {"text": "It cannot be compared, because one pair is a pair of "
                     "masses and the other is a planet and a moon",
             "correct": False,
             "why": "A planet and a moon are simply two more masses; the "
                    "same comparison applies to any pair."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e22",
        "band": "easier",
        "text": "A tennis ball and a bowling ball are placed near each "
                "other on a table. Is there a gravitational pull between "
                "them?",
        "options": [
            {"text": "No — objects that small have no gravitational pull "
                     "at all", "correct": False,
             "why": "Every mass attracts every other mass; theirs is simply "
                    "far too small to notice."},
            {"text": "Yes, though far too small to detect without "
                     "sensitive equipment", "correct": True},
            {"text": "No — gravity only acts between astronomical objects "
                     "like planets and moons", "correct": False,
             "why": "Gravity acts between any two masses, whatever their "
                    "size."},
            {"text": "Yes, and it would be strong enough to make the balls "
                     "roll towards each other", "correct": False,
             "why": "The pull between two everyday objects like these is "
                    "far too small to produce any noticeable movement."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e23",
        "band": "easier",
        "text": "In which direction does the gravitational pull between "
                "two masses always act?",
        "options": [
            {"text": "Sideways to the line joining their centres",
             "correct": False,
             "why": "The pull acts exactly along the line joining the two "
                    "centres, not sideways to it."},
            {"text": "Away from each other, along the line joining their "
                     "centres", "correct": False,
             "why": "Gravity is an attraction, so it pulls the two masses "
                    "towards each other, not apart."},
            {"text": "Towards each other, along the line joining their "
                     "centres", "correct": True},
            {"text": "In whichever direction each mass happens to be "
                     "moving", "correct": False,
             "why": "The direction of the pull depends only on where the "
                    "two masses are, not on how either of them is moving."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e24",
        "band": "easier",
        "text": "A 2 kg mass and a 20 kg mass are 1 m apart. Which one is "
                "pulled towards the other with the bigger force?",
        "options": [
            {"text": "The 2 kg mass, because smaller objects are always "
                     "pulled harder", "correct": False,
             "why": "Nothing about being smaller makes an object pulled "
                    "harder; the two forces in a gravitational pair are "
                    "equal."},
            {"text": "The 20 kg mass, because bigger objects are always "
                     "pulled harder", "correct": False,
             "why": "Bigger objects are not pulled harder in a pair; the "
                    "two forces are equal, whatever the two masses are."},
            {"text": "Neither — the two forces are equal in size",
             "correct": True},
            {"text": "It cannot be known without knowing the exact "
                     "distance between them", "correct": False,
             "why": "The equal-and-opposite rule holds at any separation, "
                    "so the exact distance does not change this answer."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e25",
        "band": "easier",
        "text": "Which pair of objects would you expect to have a "
                "MEASURABLE gravitational pull between them, using "
                "ordinary equipment?",
        "options": [
            {"text": "Two paperclips on a desk", "correct": False,
             "why": "Their masses are far too small for any ordinary "
                    "equipment to detect a pull between them."},
            {"text": "A car and a nearby lamp post", "correct": False,
             "why": "Even objects this size produce a gravitational pull "
                    "far too small for ordinary equipment to measure."},
            {"text": "Two dust particles floating in the air",
             "correct": False,
             "why": "Dust particles have an extremely small mass, giving "
                    "an immeasurably tiny pull."},
            {"text": "The Earth and the Moon", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e26",
        "band": "easier",
        "text": "Gravity is described as a 'non-contact' force. What does "
                "that mean?",
        "options": [
            {"text": "It only acts when two objects are touching",
             "correct": False,
             "why": "That would make it a contact force; a non-contact "
                    "force is the opposite of this."},
            {"text": "It cannot be measured, because nothing can detect a "
                     "force with no contact", "correct": False,
             "why": "Non-contact forces are measured all the time, for "
                    "example using a spring balance to read a weight."},
            {"text": "It can act across empty space, with nothing "
                     "physically joining the two objects", "correct": True},
            {"text": "It only works between objects made of the same "
                     "material", "correct": False,
             "why": "Gravity acts between any two masses, whatever they "
                    "are made of."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e27",
        "band": "easier",
        "text": "Which everyday observation is best explained by gravity "
                "being a non-contact force?",
        "options": [
            {"text": "A ball bounces higher on a hard floor than on a "
                     "soft one, because harder surfaces store and return "
                     "more energy", "correct": False,
             "why": "That is about how each surface pushes back on the "
                    "ball, not about gravity acting without contact."},
            {"text": "A dropped book falls towards the floor even though "
                     "nothing above it is touching it", "correct": True},
            {"text": "A magnet picks up a paperclip", "correct": False,
             "why": "That is magnetism, a different non-contact force, not "
                    "gravity."},
            {"text": "A balloon floats upward across a room when it is filled "
                     "with helium",
             "correct": False,
             "why": "That is about upthrust from the surrounding air, not "
                    "about gravity's own non-contact nature."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e28",
        "band": "easier",
        "text": "A book is held above a table and then released. Which "
                "force makes it fall, and does that force need the book to "
                "be touching anything?",
        "options": [
            {"text": "Air resistance; yes, it needs contact with the air",
             "correct": False,
             "why": "Air resistance actually slows a fall; it is not what "
                    "makes the book start falling in the first place."},
            {"text": "Friction; yes, it needs contact with a surface",
             "correct": False,
             "why": "Friction needs two surfaces in contact, and nothing "
                    "is in contact with the book while it falls."},
            {"text": "Upthrust; no, it needs no contact", "correct": False,
             "why": "Upthrust pushes up rather than down, and cannot be "
                    "what makes the book fall."},
            {"text": "Gravity; no, it acts without any contact at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e29",
        "band": "easier",
        "text": "Two identical spacecraft are the same distance from "
                "Earth. One has twice the mass of the other. Which one "
                "does the Earth pull harder?",
        "options": [
            {"text": "The one with twice the mass", "correct": True},
            {"text": "Neither — Earth pulls every object the same amount, "
                     "whatever its mass", "correct": False,
             "why": "A bigger mass is pulled with a bigger force; the two "
                    "pulls are not the same."},
            {"text": "The lighter spacecraft, because lighter objects are "
                     "pulled harder", "correct": False,
             "why": "It is the opposite — a bigger mass gives a bigger "
                    "pull, not a smaller one."},
            {"text": "It cannot be known without knowing Earth's exact "
                     "mass", "correct": False,
             "why": "Earth's own mass is the same for both spacecraft; "
                    "what differs between them is their own mass, which is "
                    "enough to answer the question."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-e30",
        "band": "easier",
        "text": "Doubling the distance between two masses makes the "
                "gravitational pull between them ___ as strong.",
        "options": [
            {"text": "twice", "correct": False,
             "why": "More distance weakens a pull; it never strengthens "
                    "it."},
            {"text": "half", "correct": False,
             "why": "That is a straight proportion; gravity follows an "
                    "inverse SQUARE law, so it falls further than a simple "
                    "half."},
            {"text": "the same", "correct": False,
             "why": "Distance is one of the two things that decide how "
                    "strong a gravitational pull is."},
            {"text": "a quarter", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p12-03-s10",
        "band": "standard",
        "text": "Two asteroids are 100 km apart and attract each other "
                "with a force of 48 N. They drift to 400 km apart. What is "
                "the force between them now?",
        "options": [
            {"text": "12 N", "correct": False,
             "why": "That divides by 4, in step with the distance rather "
                    "than with its square."},
            {"text": "192 N", "correct": False,
             "why": "Moving further apart always weakens a gravitational "
                    "pull, never strengthens it."},
            {"text": "0 N", "correct": False,
             "why": "Gravity never reaches exactly zero, however far apart "
                    "two masses are moved."},
            {"text": "3 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s11",
        "band": "standard",
        "text": "A satellite orbiting Jupiter is moved to three times its "
                "original distance from the planet. The original pull on "
                "it was 90 N. What is the new pull?",
        "options": [
            {"text": "30 N", "correct": False,
             "why": "That divides by 3, in step with the distance rather "
                    "than with its square."},
            {"text": "810 N", "correct": False,
             "why": "Moving further away always weakens a gravitational "
                    "pull, never strengthens it."},
            {"text": "0 N", "correct": False,
             "why": "Gravity never reaches exactly zero, however far apart "
                    "the two bodies are."},
            {"text": "10 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s12",
        "band": "standard",
        "text": "Explain why an artificial satellite orbiting the Earth "
                "does not simply fall straight down onto the planet.",
        "options": [
            {"text": "Because there is an outward force balancing the "
                     "Earth's pull", "correct": False,
             "why": "There is no outward force; gravity acts on the "
                    "satellite alone and unbalanced."},
            {"text": "Because the satellite is too far away for Earth's "
                     "gravity to reach it", "correct": False,
             "why": "The satellite is well within Earth's field — that "
                    "pull is exactly what keeps it in orbit."},
            {"text": "Because it is moving sideways fast enough to keep "
                     "missing the Earth as it falls", "correct": True},
            {"text": "Because the satellite has no weight once it reaches "
                     "orbit", "correct": False,
             "why": "The satellite has a real weight in orbit — close to "
                    "what it would have at the surface — which is exactly "
                    "why it is falling around the Earth."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s13",
        "band": "standard",
        "text": "Explain why an artificial satellite does not fly off into "
                "space instead of orbiting the Earth.",
        "options": [
            {"text": "Because the Earth's gravity keeps pulling it round "
                     "in a curve", "correct": True},
            {"text": "Because the satellite is moving too slowly to "
                     "escape", "correct": False,
             "why": "No particular speed is needed to stop it flying off — "
                    "it is the constant pull of gravity that curves its "
                    "path."},
            {"text": "Because the vacuum of space pushes back on anything "
                     "moving through it", "correct": False,
             "why": "A vacuum contains nothing to push back with; there is "
                    "no such force."},
            {"text": "Because the Sun's gravity holds the satellite near "
                     "the Earth", "correct": False,
             "why": "The Sun does pull the satellite too, but it is the "
                    "Earth's own gravity that keeps it orbiting the Earth "
                    "specifically."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s14",
        "band": "standard",
        "text": "Two moons orbit different planets. Moon A is twice as far "
                "from its planet as Moon B is from its planet, and the two "
                "planets have identical mass. How do the gravitational "
                "pulls on the two moons compare, assuming the moons have "
                "equal mass too?",
        "options": [
            {"text": "Moon A feels twice the pull of Moon B", "correct": False,
             "why": "Greater distance weakens a gravitational pull; it "
                    "does not strengthen it."},
            {"text": "The two pulls are exactly equal, because the "
                     "planets have the same mass", "correct": False,
             "why": "The planets' equal mass is not the only thing that "
                    "matters — the different distances make a real "
                    "difference too."},
            {"text": "Moon A feels a quarter of the pull that Moon B "
                     "feels", "correct": True},
            {"text": "Moon A feels half the pull that Moon B feels",
             "correct": False,
             "why": "That matches the distance factor rather than its "
                    "square, which the inverse square law actually uses."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s15",
        "band": "standard",
        "text": "A student says the Moon's orbit works 'because gravity "
                "pulls it in exactly as hard as it wants to fly out.' What "
                "is the flaw in this statement?",
        "options": [
            {"text": "There is no force flinging the Moon outward — "
                     "gravity acts alone and unbalanced, which is what "
                     "curves its path", "correct": True},
            {"text": "The flaw is that gravity does not pull the Moon at "
                     "all, only the Sun does", "correct": False,
             "why": "It is the Earth's gravity, above all, that is "
                    "responsible for the Moon's orbit around it."},
            {"text": "The flaw is that the Moon's own gravity cancels the "
                     "Earth's pull", "correct": False,
             "why": "The Moon does pull on the Earth, but that pull acts "
                    "on the Earth, not back on the Moon to cancel "
                    "anything."},
            {"text": "There is no flaw — the statement correctly describes "
                     "a balance of forces", "correct": False,
             "why": "There is no outward force to balance against; an "
                    "orbit is the result of an unbalanced pull, not a "
                    "balance."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s16",
        "band": "standard",
        "text": "The pull between two ships at sea, each of mass "
                "50 000 kg, 200 m apart, is far too small to notice. Why, "
                "given that they are much more massive than two people?",
        "options": [
            {"text": "Because water blocks most of the gravitational pull "
                     "between them", "correct": False,
             "why": "Gravity passes through water and any other material "
                    "with nothing blocking it."},
            {"text": "Because even 50 000 kg is still tiny next to the "
                     "mass of a planet, and 200 m is a fairly large "
                     "separation", "correct": True},
            {"text": "Because ships cannot be pulled by gravity while "
                     "floating", "correct": False,
             "why": "Floating changes nothing about whether gravity acts; "
                    "it is simply too weak here to notice against "
                    "everything else going on."},
            {"text": "Because gravity only becomes noticeable between "
                     "objects on land", "correct": False,
             "why": "Gravity works identically whether the two masses are "
                    "on land, at sea, or in space."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s17",
        "band": "standard",
        "text": "The gravitational pull between two space probes is 18 N "
                "when they are 2 m apart. What would it be if they were "
                "moved to 6 m apart?",
        "options": [
            {"text": "6 N", "correct": False,
             "why": "That divides by 3, in step with the distance rather "
                    "than with its square."},
            {"text": "162 N", "correct": False,
             "why": "That multiplies by the square of the distance factor "
                    "instead of dividing by it; moving further apart "
                    "weakens a pull, never strengthens it."},
            {"text": "2 N", "correct": True},
            {"text": "0 N", "correct": False,
             "why": "Gravity never reaches exactly zero, however far apart "
                    "the two probes are moved."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s18",
        "band": "standard",
        "text": "A student claims: 'The Sun barely moves because the "
                "Earth pulls it far more gently than the Sun pulls the "
                "Earth.' What is wrong with this claim?",
        "options": [
            {"text": "Nothing is wrong — smaller masses always pull more "
                     "gently", "correct": False,
             "why": "The two forces in a gravitational pair are equal in "
                    "size, whatever the two masses are."},
            {"text": "The two pulls are actually equal in size; it is the "
                     "Sun's enormous mass that keeps its own movement "
                     "small", "correct": True},
            {"text": "The claim is right, but only because the Earth is "
                     "further from the Sun's centre", "correct": False,
             "why": "Distance from the centre is the same quantity for "
                    "both bodies in the pair; it does not make the two "
                    "forces unequal."},
            {"text": "The Sun does not move at all, so the comparison is "
                     "meaningless", "correct": False,
             "why": "The Sun does wobble very slightly under the Earth's "
                    "pull — it is simply too massive to move by very "
                    "much."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s19",
        "band": "standard",
        "text": "A 10 kg object and a 1000 kg object are 2 m apart. "
                "Compare the size of the gravitational force each exerts "
                "on the other.",
        "options": [
            {"text": "The two forces are exactly equal in size",
             "correct": True},
            {"text": "The 1000 kg object pulls with 100 times the force",
             "correct": False,
             "why": "The two forces in a gravitational pair are always "
                    "equal, whatever the two masses are."},
            {"text": "The 10 kg object pulls with 100 times the force",
             "correct": False,
             "why": "Neither object pulls harder than the other; the two "
                    "forces are equal."},
            {"text": "It cannot be compared without knowing the exact "
                     "gravitational constant", "correct": False,
             "why": "The equal-and-opposite rule holds regardless of the "
                    "exact numbers involved."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s20",
        "band": "standard",
        "text": "Explain why a communications satellite, once placed in "
                "orbit with the right speed, can stay there for years "
                "without using any fuel to keep going.",
        "options": [
            {"text": "Because there is no gravity acting on it once it "
                     "reaches orbit", "correct": False,
             "why": "Gravity is very much still acting on it — that pull "
                    "is exactly what keeps it curving round the Earth "
                    "rather than flying off straight."},
            {"text": "Because its engines continue firing very gently the "
                     "whole time", "correct": False,
             "why": "The satellite is described as using no fuel at all; "
                    "nothing needs to keep firing."},
            {"text": "Because with nothing resisting its sideways motion, "
                     "gravity alone keeps curving its path into a "
                     "repeating orbit", "correct": True},
            {"text": "Because the satellite gradually loses mass, which "
                     "keeps it in orbit", "correct": False,
             "why": "Losing mass is not what keeps a satellite orbiting, "
                    "and in any case a working satellite's mass does not "
                    "fall away like this."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s21",
        "band": "standard",
        "text": "Jupiter is the most massive planet in the Solar System, "
                "yet the planets orbit the Sun rather than Jupiter. "
                "Explain why, in terms of gravity.",
        "options": [
            {"text": "The Sun's mass is around a thousand times "
                     "Jupiter's, so its pull on the planets is far "
                     "greater", "correct": True},
            {"text": "Jupiter is a gas planet, and gas has no "
                     "gravitational pull of its own", "correct": False,
             "why": "Gravity depends on how much mass there is, not on "
                    "whether it is gas, liquid or solid — Jupiter pulls "
                    "hard, just far less hard than the Sun."},
            {"text": "Jupiter sits further from the Sun than most "
                     "planets, and distance on its own settles which body "
                     "anything ends up orbiting", "correct": False,
             "why": "Distance matters, but so does mass, and the Sun's "
                    "enormous mass is what makes its pull on the planets "
                    "so much the larger."},
            {"text": "The Sun is far hotter than Jupiter, and a hotter body "
                     "exerts a stronger gravitational pull", "correct": False,
             "why": "Temperature plays no part in gravity at all; the "
                    "Sun's pull comes from its mass, not from its heat."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s22",
        "band": "standard",
        "text": "A tugboat pulls a barge using a rope. A student says this "
                "is similar to how gravity 'pulls' the Moon around the "
                "Earth. Explain one important way the two are different.",
        "options": [
            {"text": "They are not different at all — a rope and gravity are "
                     "both ordinary contact forces, and each one pulls only "
                     "where it is in touch with the thing it moves", "correct": False,
             "why": "The rope is a contact force, pulling only where it "
                    "physically touches the barge; gravity is a "
                    "non-contact force, reaching across empty space."},
            {"text": "The rope only works while it is taut and touching "
                     "the barge; gravity reaches across empty space with "
                     "nothing physically connecting the two bodies",
             "correct": True},
            {"text": "Gravity is stronger than a rope could ever be, "
                     "which is the key difference between the two, and is "
                     "why planets never simply snap free of their stars the "
                     "way an overloaded rope might", "correct": False,
             "why": "The strength of the two forces is not the point of "
                    "the comparison; what differs is whether physical "
                    "contact is needed at all."},
            {"text": "A rope can push as well as pull, unlike gravity",
             "correct": False,
             "why": "It is a rope that can only pull, never push — "
                    "gravity, too, can only ever pull, never push."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s23",
        "band": "standard",
        "text": "A binary star system has two stars of equal mass "
                "orbiting a point exactly midway between them. Why does "
                "neither star simply fall into the other?",
        "options": [
            {"text": "Because their gravitational pulls on each other "
                     "exactly cancel out", "correct": False,
             "why": "The two pulls do not cancel; they are what keep each "
                    "star curving around the shared point rather than "
                    "flying off straight."},
            {"text": "Because stars are too far apart for gravity to have "
                     "any real effect", "correct": False,
             "why": "The two stars are close enough that gravity's pull "
                    "on each is exactly what holds the system together."},
            {"text": "Because each star is moving sideways fast enough to "
                     "keep missing the other as it falls towards it",
             "correct": True},
            {"text": "Because equal-mass stars cannot exert a "
                     "gravitational pull on each other", "correct": False,
             "why": "Any two masses exert a gravitational pull on each "
                    "other, whatever their relative sizes."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s24",
        "band": "standard",
        "text": "Why would a space probe launched with too little sideways "
                "speed fall back to Earth instead of reaching orbit?",
        "options": [
            {"text": "Because a slower sideways speed reduces the Earth's "
                     "gravitational pull on the probe as it travels along", "correct": False,
             "why": "The probe's speed has no effect on how hard gravity "
                    "pulls on it; only its position does."},
            {"text": "Because it would be falling towards the Earth "
                     "faster than it is moving sideways to miss it",
             "correct": True},
            {"text": "Because the Earth's gravity switches off below a certain "
                     "orbital speed", "correct": False,
             "why": "Gravity does not depend on the probe's speed at all; "
                    "it acts on the probe whatever speed it has."},
            {"text": "Because the atmosphere pushes stationary probes "
                     "back down", "correct": False,
             "why": "The failure described here happens even above most "
                    "of the atmosphere; it is the balance of falling and "
                    "sideways motion that decides the outcome."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s25",
        "band": "standard",
        "text": "A 5 kg satellite part and an 8 kg satellite part are both "
                "released from a spacecraft at the same distance from "
                "Earth, with no sideways motion. Which reaches the Earth's "
                "surface first, ignoring air resistance?",
        "options": [
            {"text": "The 8 kg part, because it is pulled down harder",
             "correct": False,
             "why": "The 8 kg part is pulled down harder, but it also "
                    "needs proportionally more force to speed it up, and "
                    "the two effects cancel."},
            {"text": "The 5 kg part, because lighter objects fall faster",
             "correct": False,
             "why": "Lighter objects do not fall faster; both accelerate "
                    "at the same rate under gravity alone."},
            {"text": "It cannot be decided without knowing the exact "
                     "distance to Earth", "correct": False,
             "why": "Whatever that distance is, the two parts fall at the "
                    "same rate and reach the surface together."},
            {"text": "Neither — they arrive together", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s26",
        "band": "standard",
        "text": "Two space probes attract each other with a force of "
                "12 N. A third, identical probe is then bolted onto one "
                "of them, doubling that probe's mass, with the separation "
                "unchanged. What is the pull between the two objects now?",
        "options": [
            {"text": "12 N", "correct": False,
             "why": "Both masses affect the size of a gravitational pull, "
                    "not only the separation between them."},
            {"text": "24 N", "correct": True},
            {"text": "48 N", "correct": False,
             "why": "It is the DISTANCE that enters as a square. Doubling "
                    "one of the two masses simply doubles the pull."},
            {"text": "6 N", "correct": False,
             "why": "A pull is not shared out between masses; adding mass "
                    "to one side makes the attraction stronger, not "
                    "weaker."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s27",
        "band": "standard",
        "text": "A moon orbits its planet at a steady distance for "
                "millions of years without crashing into it or drifting "
                "away. What does this tell you about the moon's sideways "
                "speed?",
        "options": [
            {"text": "It must be closely matched to the planet's pull, "
                     "so that falling and missing repeat indefinitely",
             "correct": True},
            {"text": "It must have been increasing very slowly over those "
                     "millions of years", "correct": False,
             "why": "A stable orbit repeating for millions of years needs "
                    "a sideways speed that stays essentially the same, not "
                    "one that keeps changing."},
            {"text": "It has nothing to do with the moon staying in "
                     "orbit", "correct": False,
             "why": "Sideways speed, together with the planet's pull, is "
                    "exactly what keeps the moon in a stable orbit."},
            {"text": "It must be too slow to matter compared with the "
                     "planet's pull, so the moon's speed plays no real "
                     "part in keeping it there", "correct": False,
             "why": "If the sideways speed were too slow, the moon would "
                    "spiral in towards the planet rather than staying at a "
                    "steady distance."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s28",
        "band": "standard",
        "text": "Explain why the tiny gravitational pull between two "
                "people standing near each other has no noticeable "
                "effect, while the pull between the Earth and a person is "
                "very noticeable indeed.",
        "options": [
            {"text": "Because people are not massive enough to have any "
                     "gravity at all", "correct": False,
             "why": "Every mass, however small, exerts a real "
                    "gravitational pull; two people's is simply far too "
                    "small to notice."},
            {"text": "Because the Earth's enormous mass gives a vastly "
                     "bigger pull than two ordinary human masses ever "
                     "could", "correct": True},
            {"text": "Because two people standing near each other are still too "
                     "far apart for gravity to reach between them", "correct": False,
             "why": "Gravity reaches across any separation; the pull "
                    "between two nearby people is small because of their "
                    "mass, not their distance."},
            {"text": "Because the Earth is a special kind of object that "
                     "ordinary masses are not, following different rules "
                     "of attraction from everything else", "correct": False,
             "why": "The Earth attracts things for exactly the same "
                    "reason any two masses attract each other — it simply "
                    "has vastly more mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s29",
        "band": "standard",
        "text": "A rocket firm claims a new satellite will 'escape "
                "gravity entirely' once it leaves the Earth's atmosphere. "
                "Evaluate this claim.",
        "options": [
            {"text": "The claim is correct — gravity cannot act on anything "
                     "once it has left the atmosphere", "correct": False,
             "why": "Gravity has nothing to do with the atmosphere; it "
                    "reaches far beyond it, weakening only with distance."},
            {"text": "The claim is correct, but only for satellites above "
                     "a certain mass", "correct": False,
             "why": "A satellite's own mass does not let it escape "
                    "gravity; every mass remains subject to gravity from "
                    "every other mass."},
            {"text": "The claim is partly right — gravity becomes exactly zero "
                     "the moment the satellite reaches a stable orbit "
                     "around the Earth", "correct": False,
             "why": "Gravity in orbit is close to its surface value, not "
                    "zero; it is what keeps the satellite orbiting at "
                    "all."},
            {"text": "The claim is wrong — gravity never switches off "
                     "completely, however far the satellite travels",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-s30",
        "band": "standard",
        "text": "A comet passes close to Jupiter and its path curves "
                "noticeably. Explain why, in terms of gravity.",
        "options": [
            {"text": "Jupiter's magnetism bends the comet's path",
             "correct": False,
             "why": "Magnetism is a different force from gravity, and it "
                    "is Jupiter's mass, not any magnetism, that curves the "
                    "comet's path here."},
            {"text": "Jupiter's gravity pulls on the comet, curving its "
                     "path towards Jupiter as it passes", "correct": True},
            {"text": "The comet's own gravity pulls Jupiter out of the "
                     "comet's way as it approaches and passes by", "correct": False,
             "why": "The comet's pull on Jupiter is real but negligible "
                    "compared with Jupiter's own mass; it is Jupiter's "
                    "much larger pull that curves the comet's path."},
            {"text": "The comet speeds up so much that gravity has no "
                     "time to act on it", "correct": False,
             "why": "Gravity acts on the comet continuously, however fast "
                    "it is moving, and that pull is exactly what curves "
                    "its path."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p12-03-h10",
        "band": "harder",
        "text": "Two spacecraft attract each other with a force of 800 N "
                "when 3 m apart. What separation would give a force of "
                "200 N?",
        "options": [
            {"text": "1.5 m", "correct": False,
             "why": "That moves the spacecraft closer, which would make "
                    "the pull stronger, not weaker."},
            {"text": "12 m", "correct": False,
             "why": "That uses a distance factor of 4 rather than 2 — the "
                    "force ratio is 4, and the distance factor is its "
                    "square root, 2."},
            {"text": "9 m", "correct": False,
             "why": "That adds 6 m rather than finding the correct new "
                    "separation from the inverse square relationship."},
            {"text": "6 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h11",
        "band": "harder",
        "text": "A moon's orbit around its planet is disturbed so that its "
                "average distance from the planet increases by 50%. "
                "Roughly what happens to the gravitational pull holding it "
                "in orbit?",
        "options": [
            {"text": "It falls to two-thirds of its original value",
             "correct": False,
             "why": "That matches the distance factor's reciprocal rather "
                    "than the square of the distance factor, which the "
                    "inverse square law actually uses."},
            {"text": "It falls to exactly half its original value",
             "correct": False,
             "why": "A distance factor of 1.5 squares to 2.25, not 2, so "
                    "the pull does not fall to precisely a half."},
            {"text": "It falls to roughly 44% of its original value",
             "correct": True},
            {"text": "It stays the same, because 50% is too small a "
                     "change to matter", "correct": False,
             "why": "Even a modest change in distance changes the pull "
                    "noticeably, because the law depends on the square of "
                    "the distance."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h12",
        "band": "harder",
        "text": "A student says: 'If we could somehow double the mass of "
                "every object in the universe, gravity between any two of "
                "them would double.' Evaluate this claim.",
        "options": [
            {"text": "The claim is wrong — mass has no effect on "
                     "gravitational pull at all", "correct": False,
             "why": "Mass is one of the two things that decide the "
                    "strength of a gravitational pull; it certainly has an "
                    "effect."},
            {"text": "The claim is right, but only for objects on the "
                     "same planet", "correct": False,
             "why": "The rule that bigger masses give a bigger pull holds "
                    "between any two masses anywhere, not only on one "
                    "planet."},
            {"text": "The claim is wrong — doubling BOTH masses in a pair "
                     "would actually quadruple the pull between them, not "
                     "merely double it", "correct": True},
            {"text": "The claim is right exactly as stated", "correct": False,
             "why": "Doubling every mass doubles each side of the pair, "
                    "and the two effects multiply together rather than "
                    "simply adding, so the pull would rise by more than "
                    "double."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h13",
        "band": "harder",
        "text": "A tiny moon orbits an asteroid. Both are far smaller "
                "than a planet or a proper moon. A student argues this "
                "cannot be a 'real' orbit because the masses involved are "
                "so small. Evaluate this argument.",
        "options": [
            {"text": "The argument is right — an orbit needs at least "
                     "one body the size of a planet", "correct": False,
             "why": "Nothing about the size of an orbit sets a minimum "
                    "mass; any two masses can orbit each other if the "
                    "balance of falling and sideways motion is right."},
            {"text": "The argument is wrong — an orbit only needs a "
                     "gravitational pull and the right sideways speed, "
                     "whatever the masses involved", "correct": True},
            {"text": "The argument is right, because small masses cannot "
                     "produce a strong enough pull to hold an orbit at "
                     "all, whatever sideways speed the smaller body "
                     "happens to have", "correct": False,
             "why": "A smaller pull simply gives a different, more easily "
                    "disturbed orbit — it does not rule an orbit out "
                    "entirely."},
            {"text": "The argument is wrong, but only because asteroids turn "
                     "out to be every bit as massive as small planets",
             "correct": False,
             "why": "Asteroids are certainly far less massive than "
                    "planets; the argument fails for a different reason — "
                    "orbit needs no minimum mass at all."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h14",
        "band": "harder",
        "text": "Two students disagree about a satellite's fuel-free "
                "orbit. One says gravity is 'used up' keeping the "
                "satellite orbiting, like a battery running down. Evaluate "
                "this claim.",
        "options": [
            {"text": "The claim is wrong — gravity is a permanent pull "
                     "between two masses and is never used up or spent",
             "correct": True},
            {"text": "The claim is right — that is exactly why old "
                     "satellites eventually fall from orbit", "correct": False,
             "why": "Satellites that fall from orbit are usually slowed "
                    "by tiny amounts of atmosphere at low altitude, not by "
                    "gravity running out."},
            {"text": "The claim is right, but only for very old "
                     "satellites", "correct": False,
             "why": "Gravity does not weaken with a satellite's age; its "
                    "pull depends only on the masses and the distance "
                    "between them."},
            {"text": "It cannot be evaluated without knowing the "
                     "satellite's mass", "correct": False,
             "why": "Whatever the satellite's mass, gravity is not a "
                    "resource that can be consumed or run down."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h15",
        "band": "harder",
        "text": "A 4 kg object and a 9 kg object, 2 m apart, attract each "
                "other with a force of F newtons. The 9 kg object is then "
                "replaced with an 18 kg object at the same distance. What "
                "happens to the force?",
        "options": [
            {"text": "It stays the same, because only the separation "
                     "affects the size of a gravitational pull",
             "correct": False,
             "why": "Both masses affect the size of the pull, not only "
                    "the separation between them."},
            {"text": "It doubles", "correct": True},
            {"text": "It quadruples", "correct": False,
             "why": "Doubling only one of the two masses doubles the "
                    "force; quadrupling would need both masses to "
                    "double."},
            {"text": "It falls to half its original value", "correct": False,
             "why": "Increasing a mass in the pair makes the pull "
                    "stronger, not weaker."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h16",
        "band": "harder",
        "text": "A satellite's orbit is disturbed so that it now moves in "
                "a much bigger circle around the Earth than before, at a "
                "steady distance throughout. Which of these must also "
                "have changed?",
        "options": [
            {"text": "Nothing else needs to change — the same sideways "
                     "speed works at any distance", "correct": False,
             "why": "A bigger, steady circular orbit needs the sideways "
                    "speed to be matched to the weaker pull at the new "
                    "distance; the old speed would not keep it in a "
                    "stable circle there."},
            {"text": "The satellite's sideways speed, to match the "
                     "weaker pull it now experiences at the greater "
                     "distance", "correct": True},
            {"text": "The Earth's mass, to provide a stronger pull at the "
                     "new distance", "correct": False,
             "why": "The Earth's own mass has not changed at all; it is "
                    "the satellite's speed that must be matched to the "
                    "new distance instead."},
            {"text": "The direction gravity acts in, so that it now pulls "
                     "the satellite sideways instead of towards the Earth",
             "correct": False,
             "why": "Gravity always pulls directly towards the Earth's "
                    "centre, at every distance — its direction has not "
                    "changed."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h17",
        "band": "harder",
        "text": "A textbook states that the Earth's pull on the Moon is "
                "roughly 2 × 10^20 N. A student calculates that the "
                "Moon's pull on the Earth must therefore be far smaller, "
                "since the Moon is so much less massive. Identify the "
                "error.",
        "options": [
            {"text": "The two forces are equal in size, whatever the "
                     "difference in mass between the Earth and the Moon",
             "correct": True},
            {"text": "There is no error — smaller masses always exert a "
                     "smaller gravitational force in a pair", "correct": False,
             "why": "The two forces in a gravitational pair are always "
                    "equal, however different the two masses are."},
            {"text": "The error is that the figure of 2 × 10^20 N is "
                     "itself wrong", "correct": False,
             "why": "The size of the figure is not the issue here; the "
                    "error is in assuming the reverse pull must be "
                    "different."},
            {"text": "The error is that the Moon has no gravity of its "
                     "own at all", "correct": False,
             "why": "The Moon does have gravity — it is what holds a "
                    "lunar orbiter, for instance, in orbit around it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h18",
        "band": "harder",
        "text": "A moon of Jupiter orbits much closer to Jupiter than "
                "Earth's Moon orbits the Earth, and completes each "
                "circuit in far less time. What must be true about the "
                "pull it experiences?",
        "options": [
            {"text": "The pull on it must be weaker than the pull on Earth's "
                     "Moon, because it has a very much smaller circle to travel "
                     "round each time", "correct": False,
             "why": "Being closer to Jupiter, and Jupiter's far greater "
                    "mass, both point towards a stronger pull, not a "
                    "weaker one."},
            {"text": "The pull has nothing to do with how quickly it "
                     "completes an orbit", "correct": False,
             "why": "The strength of the pull, together with the "
                    "distance, is exactly what decides how fast an "
                    "orbiting body must move to stay in a stable orbit."},
            {"text": "The pull it experiences must be substantially "
                     "stronger, since a tighter and faster orbit needs a "
                     "harder pull to curve the path that sharply",
             "correct": True},
            {"text": "The pull must be identical to the one on Earth's "
                     "Moon, because every moon in the Solar System is "
                     "held in place by a pull of the same standard "
                     "strength", "correct": False,
             "why": "A pull's strength depends on the planet's mass and "
                    "on the distance from it, and both differ sharply "
                    "between these two cases."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h19",
        "band": "harder",
        "text": "A 1 kg object is released with no sideways motion at "
                "each of three different distances from a planet: close, "
                "medium and far. At which distance does it take the "
                "LONGEST to hit the planet, and why?",
        "options": [
            {"text": "The furthest distance, because the pull on it is "
                     "weaker there, giving it less initial acceleration, "
                     "on top of having further to fall", "correct": True},
            {"text": "The closest distance, because the object falls the "
                     "shortest way there", "correct": False,
             "why": "Falling a shorter distance would tend to take less "
                    "time, not more — the closest object also experiences "
                    "the strongest pull, both of which point towards "
                    "falling fastest, not slowest."},
            {"text": "All three take the same time, because gravity acts "
                     "identically at every distance from a planet",
             "correct": False,
             "why": "Gravity actually weakens with distance, so the pull "
                    "— and the fall — is not identical at all three "
                    "distances."},
            {"text": "It cannot be worked out without knowing the "
                     "object's exact mass", "correct": False,
             "why": "Mass affects the pull on it, but by exactly the "
                    "same cancelling relationship as always — the fall "
                    "time depends on the field strength and distance, not "
                    "on the object's own mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h20",
        "band": "harder",
        "text": "Explain why a rocket needs far more fuel to reach orbit "
                "from the Earth's surface than it would need to move the "
                "same distance sideways once already safely in orbit.",
        "options": [
            {"text": "On the surface, the rocket must fight the Earth's "
                     "full pull to climb away; once in orbit it is "
                     "already falling around the Earth, so a small nudge "
                     "is enough to shift it sideways", "correct": True},
            {"text": "Gravity is much stronger at the Earth's surface "
                     "than anywhere else in the universe", "correct": False,
             "why": "Gravity is strongest AT the surface compared with "
                    "orbit, but it does not stop being present the moment "
                    "the rocket clears the ground — the real difference is "
                    "what the fuel has to achieve in each case."},
            {"text": "There is no real difference — both manoeuvres need "
                     "exactly the same amount of fuel", "correct": False,
             "why": "Climbing away from the surface against the Earth's "
                    "full pull needs far more fuel than a small sideways "
                    "nudge once already in a stable orbit."},
            {"text": "Rockets in orbit do not need fuel because gravity "
                     "has already been switched off there completely, "
                     "the moment the rocket clears the last traces of the "
                     "Earth's atmosphere on its way up", "correct": False,
             "why": "Gravity has not switched off in orbit; it is very "
                    "much still acting, and is what curves the rocket's "
                    "path into an orbit in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h21",
        "band": "harder",
        "text": "Two planets, A and B, orbit different stars. Planet A "
                "takes 2 Earth years to orbit its star; Planet B takes 8 "
                "Earth years. If both are the same distance from their "
                "(identical mass) stars, does this difference make "
                "sense?",
        "options": [
            {"text": "Yes — planets can take any length of time to "
                     "orbit, regardless of their distance or their star's "
                     "mass", "correct": False,
             "why": "For the same star mass and the same distance, the "
                    "physics gives essentially the same orbital period; "
                    "something else must differ to explain the mismatch "
                    "here."},
            {"text": "Yes — Planet B is simply moving in the opposite "
                     "direction, which takes four times as long",
             "correct": False,
             "why": "The direction a planet orbits in has no bearing on "
                    "how long a full orbit takes."},
            {"text": "It cannot be judged without knowing the planets' "
                     "own masses", "correct": False,
             "why": "For an orbiting planet, its own mass makes very "
                    "little difference to its orbital period compared "
                    "with its star's mass and its distance from it."},
            {"text": "No — with identical star masses and identical "
                     "distances, the two orbital periods should be about "
                     "the same, so something else about the two systems "
                     "must actually differ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h22",
        "band": "harder",
        "text": "A 'gravity assist' manoeuvre lets a spacecraft speed up "
                "by passing close to a planet, using only gravity and no "
                "fuel. Explain how this can increase the spacecraft's "
                "speed without anything pushing it.",
        "options": [
            {"text": "The planet's gravity pulls the spacecraft in "
                     "throughout the manoeuvre, but has to let it go just "
                     "as strongly, so no lasting speed change is really "
                     "possible", "correct": False,
             "why": "A real, lasting speed change genuinely does result "
                    "from a correctly designed gravity assist — the "
                    "planet's own motion is what allows this."},
            {"text": "As the spacecraft swings past, it exchanges a "
                     "little momentum with the moving planet, borrowing "
                     "some of the planet's own motion around its star",
             "correct": True},
            {"text": "The spacecraft's engines fire briefly, drawing on the "
                     "planet's gravitational field as a fuel supply and "
                     "converting it into forward motion", "correct": False,
             "why": "Gravity assists are specifically used because they "
                    "need no fuel at all; nothing about the manoeuvre "
                    "uses the field as an energy source in that way."},
            {"text": "Gravity briefly reverses and pushes the spacecraft "
                     "forward like a sling", "correct": False,
             "why": "Gravity never pushes, only pulls; the speed gain "
                    "comes from the geometry of the pass and the planet's "
                    "own motion, not from a reversed force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h23",
        "band": "harder",
        "text": "A comet on a very long, stretched-out orbit moves much "
                "faster when close to the Sun than when far away. Explain "
                "this in terms of the changing gravitational pull on it.",
        "options": [
            {"text": "Its speed has nothing to do with the pull — comets "
                     "simply travel at a fixed speed set when they "
                     "formed, unaffected by anything they later pass "
                     "close to", "correct": False,
             "why": "A comet's speed changes markedly around its orbit, "
                    "and that change is closely tied to how strongly the "
                    "Sun is pulling on it at each point."},
            {"text": "The pull stays constant throughout its orbit, and it is "
                     "the comet's own mass that changes as it approaches the "
                     "Sun",
             "correct": False,
             "why": "The comet's mass does not change meaningfully during "
                    "a single orbit; what changes is its distance from "
                    "the Sun and therefore the Sun's pull on it."},
            {"text": "The comet slows down near the Sun because the pull "
                     "there is so strong it resists the comet's motion",
             "correct": False,
             "why": "A stronger pull draws the comet in and speeds it up "
                    "as it falls closer, rather than resisting or slowing "
                    "its motion."},
            {"text": "Close to the Sun the pull is much stronger, "
                     "accelerating the comet; far away the pull is weak, "
                     "and the comet coasts more slowly", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h24",
        "band": "harder",
        "text": "Explain why the Moon's gravity, though much weaker than "
                "the Earth's, is still strong enough to raise ocean tides "
                "on Earth, while the gravitational pull of a passing "
                "aircraft overhead has no such measurable effect on the "
                "sea.",
        "options": [
            {"text": "Because the Moon is closer to the sea than any "
                     "aircraft ever gets", "correct": False,
             "why": "The Moon is vastly further from the sea than any "
                    "aircraft; distance is not what makes the difference "
                    "here."},
            {"text": "Because aircraft are made of metal, which does not "
                     "respond to gravity the way water does", "correct": False,
             "why": "Gravity affects every mass in the same general way; "
                    "what an aircraft is made of is not the relevant "
                    "factor here."},
            {"text": "Because the Moon's mass, though small next to the "
                     "Earth's, is enormously larger than an aircraft's, "
                     "giving a far bigger pull despite the huge distance",
             "correct": True},
            {"text": "Because tides are caused by wind and currents, not "
                     "by gravity at all", "correct": False,
             "why": "Tides are caused principally by the gravitational "
                    "pull of the Moon (and, to a smaller extent, the "
                    "Sun), not by wind or currents."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h25",
        "band": "harder",
        "text": "A space station and a small satellite are both in the "
                "same orbit around the Earth, at the same distance and "
                "moving at the same speed. The station has a mass 1000 "
                "times greater than the satellite. Which of them curves "
                "around the Earth in a tighter circle?",
        "options": [
            {"text": "Neither — both orbit in exactly the same circle, "
                     "because the mass of the orbiting object cancels out "
                     "of the calculation", "correct": True},
            {"text": "The station, because its far greater mass gives it "
                     "a stronger pull from the Earth, curving its path "
                     "more sharply than the satellite's", "correct": False,
             "why": "The station does feel a stronger pull, but it also "
                    "needs proportionally more force to curve at the same "
                    "rate, so the two effects cancel and its path is "
                    "unaffected by its own mass."},
            {"text": "The satellite, because a lighter object is far easier for "
                     "the Earth's gravity to redirect", "correct": False,
             "why": "Being lighter does not make an object's orbital "
                    "path any different — mass cancels out of what shape "
                    "of orbit a given speed and distance produce."},
            {"text": "It cannot be decided without knowing the exact "
                     "distance from Earth", "correct": False,
             "why": "Whatever that distance is, the two objects' own "
                    "masses make no difference to the shape of the orbit "
                    "— only their shared distance and speed do."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h26",
        "band": "harder",
        "text": "A 20 kg satellite part and a 5 kg satellite part are "
                "released together, motionless relative to each other, "
                "deep in space far from any star or planet. Do they "
                "eventually drift together, pulled by their own mutual "
                "gravity?",
        "options": [
            {"text": "No — objects this small have no gravitational "
                     "field of their own at all", "correct": False,
             "why": "Every mass has a gravitational field, however "
                    "small; the two parts do attract each other, just "
                    "extremely weakly."},
            {"text": "No — gravity only acts between a small object and a much "
                     "larger body, such as a planet or a star", "correct": False,
             "why": "Gravity acts between any two masses whatsoever, not "
                    "only between a small object and something much "
                    "larger."},
            {"text": "Yes, eventually — their mutual pull, though "
                     "extremely weak, never reaches zero and would very "
                     "slowly draw them together", "correct": True},
            {"text": "Yes, and they would meet within seconds, because "
                     "nothing else is acting on them at all out there to "
                     "slow their approach down in any way", "correct": False,
             "why": "The pull between two masses this small is so weak "
                    "that drawing them together would take an immensely "
                    "long time, not seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h27",
        "band": "harder",
        "text": "Two students argue about whether the International "
                "Space Station is 'weightless.' One says it has zero "
                "weight; the other says it has almost its full surface "
                "weight, but simply APPEARS weightless. Who is closer to "
                "being right, and why?",
        "options": [
            {"text": "The first student — objects genuinely lose all "
                     "their weight once they reach the height of the ISS",
             "correct": False,
             "why": "Earth's field at that height is still close to 90% "
                    "of its surface value, so the station's true weight "
                    "is far from zero."},
            {"text": "Neither — weight is not a meaningful idea for "
                     "anything in orbit", "correct": False,
             "why": "Weight is exactly as meaningful in orbit as "
                    "anywhere else; it is simply not felt in the usual "
                    "way, because nothing presses back against it there."},
            {"text": "The second student — the ISS is pulled by nearly "
                     "its full surface weight, and only appears "
                     "weightless because it is falling around the Earth "
                     "with nothing to press against", "correct": True},
            {"text": "The first student, but only because the ISS "
                     "travels so fast that gravity cannot keep up with "
                     "it", "correct": False,
             "why": "Gravity is not a force that can be 'outrun' by "
                    "speed; it continues to act on the station fully "
                    "throughout its orbit."},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h28",
        "band": "harder",
        "text": "A planet's moon is observed to take exactly four times "
                "as long to complete an orbit after being nudged into a "
                "new, more distant orbit. A scientist claims this alone "
                "proves the new distance is exactly four times the old "
                "one. Evaluate this claim, given that orbital period and "
                "distance are NOT related by a simple one-to-one ratio.",
        "options": [
            {"text": "The claim is definitely correct — orbital period "
                     "and distance always change by the same factor as "
                     "each other, whatever the two values happen to be", "correct": False,
             "why": "Orbital period and distance are related, but not by "
                    "a simple one-to-one factor, so a four-times-longer "
                    "period does not by itself prove a four-times-greater "
                    "distance."},
            {"text": "The claim cannot be evaluated at all without "
                     "knowing the moon's own mass", "correct": False,
             "why": "For an orbiting moon, its own mass has very little "
                    "bearing on this particular relationship between "
                    "period and distance."},
            {"text": "The claim is correct, but only if the moon's own orbital "
                     "speed has also stayed exactly the same", "correct": False,
             "why": "The moon's speed is very unlikely to have stayed "
                    "the same after being nudged into a wider orbit; a "
                    "wider, slower-moving orbit is the more typical "
                    "outcome."},
            {"text": "The claim is not proven by the period change "
                     "alone, since period and distance are not related "
                     "by a simple one-to-one factor", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h29",
        "band": "harder",
        "text": "A student proposes testing gravity's inverse square law "
                "by measuring the pull between two 1 kg masses at 1 m, "
                "then at 2 m, using kitchen scales. Evaluate whether this "
                "experiment could actually work.",
        "options": [
            {"text": "It would work perfectly, since kitchen scales are "
                     "sensitive enough to detect any force at all, "
                     "however small, once the reading is looked at "
                     "closely enough",
             "correct": False,
             "why": "The gravitational pull between two 1 kg masses is "
                    "many orders of magnitude too small for kitchen "
                    "scales, which are built to detect forces from "
                    "ordinary weights, not such a tiny pull."},
            {"text": "It would work, but only if the two masses were "
                     "made of iron", "correct": False,
             "why": "What the masses are made of makes no difference to "
                    "gravity between them; the practical problem is the "
                    "pull's size being far too small to detect, not the "
                    "material."},
            {"text": "It would work if the whole experiment were repeated many "
                     "times over and the readings averaged", "correct": False,
             "why": "No amount of repeating and averaging can reveal a "
                    "signal that is completely swamped by the equipment's "
                    "own limitations; specialised, far more sensitive "
                    "apparatus is needed."},
            {"text": "It would not work — the gravitational pull between "
                     "two everyday 1 kg masses is far too small for "
                     "kitchen scales to detect at all", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-03-h30",
        "band": "harder",
        "text": "Explain why, when calculating the orbit of a satellite "
                "around the Earth, scientists can safely ignore the tiny "
                "gravitational pull the satellite itself exerts back on "
                "the Earth.",
        "options": [
            {"text": "The Earth's mass is so enormous compared with the "
                     "satellite's that the effect of the satellite's pull "
                     "on the Earth's motion is utterly negligible, even "
                     "though the two forces are equal in size",
             "correct": True},
            {"text": "Because the satellite's pull on the Earth does not "
                     "actually exist — only the Earth pulls on the "
                     "satellite, since gravity only ever acts one way "
                     "between any two masses of very different size", "correct": False,
             "why": "Every gravitational pull comes as an equal pair; "
                    "the satellite genuinely does pull on the Earth too."},
            {"text": "Because the two forces are equal, so they cancel "
                     "each other out and can be ignored for that reason",
             "correct": False,
             "why": "Equal forces acting on two different objects do not "
                    "cancel each other; each force acts fully on the "
                    "object it pulls, and only the effect on the far more "
                    "massive Earth is negligible."},
            {"text": "Because gravity only acts on smaller objects, "
                     "never back on the larger one", "correct": False,
             "why": "Gravity acts equally both ways in any pair; it is "
                    "the Earth's enormous mass, not any one-way limit on "
                    "gravity, that makes the effect on it negligible."},
        ],
        "figure": None,
    },
]
