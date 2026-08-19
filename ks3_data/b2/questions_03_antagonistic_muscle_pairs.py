"""B2 lesson 03 — Antagonistic muscle pairs: twelve questions (MRB-269).

These probe the one idea the lesson is built on — a muscle shortens and pulls,
and nothing else, so every movement you can undo needs a second muscle on the
other side of the joint. The distractors are built from the lesson's three
declared misconceptions: BODY-07 (muscles push as well as pull), BODY-08 (the
biceps stretches itself back out) and BODY-09 (both muscles contracting is
faster or stronger). Two more come from the bench's own branches — that a
relaxed muscle is doing nothing, and that gravity is a muscle's helper in both
directions when in fact it only ever pulls a hanging limb down. The `harder`
band takes the rule somewhere the lesson never goes (a cable-driven robot
elbow), joins the eccentric box-lowering case to the relax-versus-stretch
ruling, sets the gravity-for-free line against the knee item that contradicts
it, and turns co-contraction from a fault into a purpose.
"""

UNIT = "B2"
LESSON = "antagonistic-muscle-pairs"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-03-e01",
        "band": "easier",
        "text": "A muscle contracts. What has happened inside the muscle, and "
                "what does its bone do?",
        "options": [
            {"text": "It gets longer and stiffer, and pushes the bone away "
                     "from the joint.",
             "correct": False,
             "why": "There is no push in a muscle. It shortens, and "
                    "shortening can only pull — a rope can haul a bucket up a "
                    "well, but it can never shove one down."},
            {"text": "It gets shorter and fatter, and pulls the bone it is "
                     "attached to.",
             "correct": True},
            {"text": "It gets shorter and thinner, and pulls the bone it is "
                     "attached to.",
             "correct": False,
             "why": "The pull is right, but feel your own arm as you bend it: "
                    "a working muscle bulges. The fibres shorten, so the "
                    "muscle gets fatter, not thinner."},
            {"text": "It stays the same length and stiffens, holding the bone "
                     "exactly where it was.",
             "correct": False,
             "why": "That is what a joint does when both muscles of a pair "
                    "pull at once. One muscle contracting on its own always "
                    "shortens, and the bone has to move."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e02",
        "band": "easier",
        "text": "The calf muscle reaches the heel bone through the Achilles. "
                "What is the Achilles?",
        "options": [
            {"text": "A tendon — the cord that carries the calf muscle's pull "
                     "down to the heel bone.",
             "correct": True},
            {"text": "A muscle — it contracts alongside the calf and helps to "
                     "lift the heel bone.",
             "correct": False,
             "why": "It cannot contract at all. Only muscles shorten; a "
                    "tendon is the attachment that carries a muscle's pull "
                    "across a joint to a bone."},
            {"text": "A joint — the place where the bones of the lower leg "
                     "meet the bones of the foot.",
             "correct": False,
             "why": "That is the ankle joint. The Achilles crosses the ankle "
                    "to reach the heel; it is not the joint itself."},
            {"text": "A tendon — it shortens to pull the toes upwards, off "
                     "the ground.",
             "correct": False,
             "why": "Half right: it is a tendon. But nothing about a tendon "
                    "shortens, and lifting the toes is the opposite movement, "
                    "done by the muscle down the front of the shin."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e03",
        "band": "easier",
        "text": "On the bench you contract the triceps on its own and leave "
                "the biceps alone. What does the model arm do?",
        "options": [
            {"text": "The forearm swings up and the elbow bends.",
             "correct": False,
             "why": "That is the biceps' movement. The triceps is attached "
                    "behind the elbow, so its pull swings the forearm the "
                    "other way."},
            {"text": "The elbow stiffens and holds still wherever it already "
                     "was.",
             "correct": False,
             "why": "The elbow only stiffens when both muscles pull at once. "
                    "With one of them pulling, the arm moves."},
            {"text": "Nothing moves. The triceps only lets the biceps relax.",
             "correct": False,
             "why": "The triceps is a muscle in its own right, and pulling is "
                    "the only thing it does. It does not work by releasing "
                    "the biceps."},
            {"text": "The forearm swings down and the elbow straightens.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e04",
        "band": "easier",
        "text": "You press Neither on the bench, so no muscle is pulling at "
                "all — and the arm still moves. What moves it?",
        "options": [
            {"text": "The biceps, stretching itself back out to its resting "
                     "length.",
             "correct": False,
             "why": "A muscle cannot make itself longer. It can shorten, or "
                    "it can stop shortening, and stopping is all it is doing "
                    "here."},
            {"text": "The triceps, which must still be pulling quietly in the "
                     "background.",
             "correct": False,
             "why": "Nothing is pulling — that is what Neither means, and the "
                    "status line says so. The arm comes down anyway."},
            {"text": "Gravity. The forearm falls under its own weight and the "
                     "elbow straightens.",
             "correct": True},
            {"text": "The relaxed muscles, which give the two bones a gentle "
                     "push apart.",
             "correct": False,
             "why": "A relaxed muscle pushes nothing — no muscle ever does. "
                    "It has simply let go, which leaves the forearm's weight "
                    "to do the work."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-03-s01",
        "band": "standard",
        "text": "The triceps contracts and your elbow straightens. What is "
                "happening to the biceps while that goes on?",
        "options": [
            {"text": "It relaxes, and the triceps' pull is what lengthens it.",
             "correct": True},
            {"text": "It stretches itself back out to its long shape as the "
                     "elbow opens.",
             "correct": False,
             "why": "Stretching is not something a muscle can do to itself. "
                    "It relaxes — it lets go — and then something else pulls "
                    "it long. Here that something is the triceps."},
            {"text": "It stays exactly the same length; only the triceps "
                     "changes.",
             "correct": False,
             "why": "It crosses the same joint, so it cannot stay put. Open "
                    "the elbow and the biceps is pulled longer whether it "
                    "likes it or not."},
            {"text": "It contracts a little too, to keep the movement under "
                     "control.",
             "correct": False,
             "why": "Both pulling at once stiffens the elbow rather than "
                    "steering it — you saw that on the bench. In a pair, one "
                    "contracts and the other relaxes."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s02",
        "band": "standard",
        "text": "Standing up out of a chair is hard work. Letting yourself "
                "back down into it is not. What is the difference?",
        "options": [
            {"text": "Sitting down is the hamstrings' job, and the hamstrings "
                     "are the stronger of the two.",
             "correct": False,
             "why": "Strength is not what changes. On the way down gravity is "
                    "doing the moving, so no muscle has to haul your weight "
                    "anywhere."},
            {"text": "On the way down, the quadriceps push against the floor "
                     "and lower you into the chair.",
             "correct": False,
             "why": "Muscles never push. Nothing pushes you into the chair — "
                    "your own weight takes you there while the quadriceps let "
                    "you down slowly."},
            {"text": "Going up, the quadriceps pull the knee straight "
                     "against gravity. Going down, gravity does it.",
             "correct": True},
            {"text": "Standing up uses both muscles of the pair at once, "
                     "which is twice as much work.",
             "correct": False,
             "why": "Both at once would stiffen the knee and you would not "
                    "rise at all. Standing up is the quadriceps pulling while "
                    "the hamstrings relax."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s03",
        "band": "standard",
        "text": "The biceps has been switched off on the bench. Which "
                "movement of that elbow has been lost?",
        "options": [
            {"text": "Straightening it — the biceps was what pulled the "
                     "forearm back down.",
             "correct": False,
             "why": "Straightening is the triceps' job, and gravity does it "
                    "too on a hanging arm. Both of those still work with the "
                    "biceps off."},
            {"text": "Bending it — nothing else can pull the forearm up.",
             "correct": True},
            {"text": "None of them. The triceps can push the forearm up "
                     "instead.",
             "correct": False,
             "why": "The triceps is attached behind the elbow, and a pull "
                    "there can only straighten the arm. No muscle pushes, so "
                    "nothing replaces the biceps."},
            {"text": "None of them. The forearm's own weight will swing it "
                     "back up.",
             "correct": False,
             "why": "Weight only ever pulls the forearm down. Gravity can "
                    "straighten a hanging arm for free, but it can never bend "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s04",
        "band": "standard",
        "text": "You rise onto your tiptoes and the calf muscle contracts. "
                "What is its partner, the muscle down the front of the shin, "
                "doing?",
        "options": [
            {"text": "Contracting as well, so that the two of them lift you "
                     "together.",
             "correct": False,
             "why": "They pull opposite ways — the front muscle lifts the "
                    "toes. Both at once would stiffen the ankle and leave you "
                    "flat on the floor."},
            {"text": "Stretching itself out of the way so that the calf can "
                     "shorten.",
             "correct": False,
             "why": "It does not stretch itself. It relaxes, and the calf's "
                    "pull on the heel bone is what lengthens it."},
            {"text": "Nothing at all. Only the calf is involved in a movement "
                     "this simple.",
             "correct": False,
             "why": "Every movement at a joint involves the pair. If the "
                    "front muscle did not let go, it would be fighting the "
                    "calf and the heel would stay down."},
            {"text": "Relaxing, and being lengthened as the calf pulls the "
                     "heel bone up.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-03-h01",
        "band": "harder",
        "text": "An engineer builds a robot arm. Her motors can only wind a "
                "cable in; nothing in the design can push. What does she need "
                "at the elbow joint?",
        "options": [
            {"text": "One cable and a stronger motor, so that the one cable "
                     "can drive the joint both ways.",
             "correct": False,
             "why": "Force is not the problem, direction is. A cable that "
                    "only winds in pulls one way, and no amount of power "
                    "turns a pull into a push."},
            {"text": "One cable, unwound by the motor whenever the joint has "
                     "to go back the other way.",
             "correct": False,
             "why": "Unwinding is only letting go, which is exactly what a "
                    "muscle does when it relaxes — and relaxing on its own "
                    "moves nothing."},
            {"text": "Two cables, one on each side of the joint, each pulling "
                     "it the opposite way.",
             "correct": True},
            {"text": "Two cables on the same side, pulling together so that "
                     "the joint moves twice as fast.",
             "correct": False,
             "why": "Two pulls the same way still leave nothing to bring the "
                    "joint back, and pulling together does not double the "
                    "speed. A pair works because it sits on opposite sides."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h02",
        "band": "harder",
        "text": "You lower a heavy box slowly to the floor. Your arms "
                "straighten, so the biceps is getting longer — yet it is "
                "contracting the whole way down. What is lengthening it?",
        "options": [
            {"text": "The weight of the box, pulling the biceps out while it "
                     "holds on.",
             "correct": True},
            {"text": "The biceps itself, stretching back out to its long "
                     "shape as it tires.",
             "correct": False,
             "why": "A muscle has no way of lengthening itself, tired or "
                    "fresh. Something else must pull it out, and here that "
                    "something is the box."},
            {"text": "The triceps, contracting to pull the forearm down "
                     "against it.",
             "correct": False,
             "why": "The triceps has nothing to do here — gravity is already "
                    "taking the box down. If the triceps pulled as well, the "
                    "elbow would simply stiffen."},
            {"text": "Nothing is. The biceps must be fully relaxed, or it "
                     "could not be getting longer.",
             "correct": False,
             "why": "Let go and the box drops. The biceps is pulling hard all "
                    "the way down and losing the tug of war on purpose, a "
                    "little at a time."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h03",
        "band": "harder",
        "text": "The triceps has a whole forearm to straighten, yet in "
                "ordinary life it does less work than you would expect. Why?",
        "options": [
            {"text": "The biceps takes on part of the straightening job by "
                     "stretching itself back out again.",
             "correct": False,
             "why": "The biceps cannot stretch itself, so it can take on "
                    "nothing. All it does while the elbow opens is relax and "
                    "get pulled long."},
            {"text": "The triceps is far stronger than the biceps, so the "
                     "same job costs it much less effort.",
             "correct": False,
             "why": "Strength is not the reason. Whenever the arm hangs, "
                    "gravity straightens it, so the triceps is often not "
                    "needed at all."},
            {"text": "Straightening a joint is always easier than bending "
                     "one, at every joint in the body.",
             "correct": False,
             "why": "That is not a rule. Standing up straightens the knee and "
                    "it is hard work, because at the knee gravity is pulling "
                    "the other way."},
            {"text": "Gravity straightens a hanging arm for free, so the "
                     "triceps is only needed against a resistance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h04",
        "band": "harder",
        "text": "A surgeon holds a scalpel dead still; a gymnast holds a "
                "cross on the rings. Nothing moves at either elbow, yet both "
                "tire fast. What are the muscles of each pair doing?",
        "options": [
            {"text": "Neither one is pulling. Nothing is moving, so nothing "
                     "is contracting.",
             "correct": False,
             "why": "If both let go, the arm would drop. Holding a joint "
                    "still against a knock takes both sides pulling — nothing "
                    "moving is not the same as nothing happening."},
            {"text": "Both are pulling at once. The joint stiffens, and both "
                     "are using energy.",
             "correct": True},
            {"text": "The joint itself has locked, so no muscle has to do any "
                     "work at all.",
             "correct": False,
             "why": "A joint has no lock of its own. What stiffens it is the "
                    "two muscles pulling against each other, and that is "
                    "exactly why the arm tires."},
            {"text": "One pulls, and its partner is stretched tight to brace "
                     "against it.",
             "correct": False,
             "why": "A relaxed partner can only be lengthened; it cannot "
                    "brace anything. To hold a joint steady, the partner has "
                    "to pull as well."},
        ],
        "figure": None,
    },
]
