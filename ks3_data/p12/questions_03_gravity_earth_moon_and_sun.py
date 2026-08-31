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
            {"text": "A pull", "correct": True},
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
            {"text": "Because the Sun is anchored in place by the rest of the "
                     "galaxy", "correct": False,
             "why": "The Sun is not anchored to anything; it orbits the "
                    "centre of the galaxy itself."},
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
]
