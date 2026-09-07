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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-03-e05",
        "band": "easier",
        "text": "Which muscle contracts to bend your elbow, and where is it?",
        "options": [
            {"text": "The biceps, at the front of the upper arm.",
             "correct": True},
            {"text": "The triceps, at the back of the upper arm.",
             "correct": False,
             "why": "The triceps attaches behind the elbow, so its pull "
                    "straightens the arm. Bending is the biceps' job."},
            {"text": "Both of them together, pulling the forearm up.",
             "correct": False,
             "why": "Both at once stiffens the elbow and holds it where it "
                    "is. In a pair, one pulls and the other lets go."},
            {"text": "The biceps, at the back of the upper arm.",
             "correct": False,
             "why": "Right muscle, wrong side. Feel your own arm as you bend "
                    "it — the bulge comes up at the front."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e06",
        "band": "easier",
        "text": "What does the phrase antagonistic pair mean?",
        "options": [
            {"text": "Two muscles side by side, pulling together to make one "
                     "bigger movement.",
             "correct": False,
             "why": "Two pulls the same way still leave nothing to bring the "
                    "bone back. A pair sits on opposite sides of the joint."},
            {"text": "A muscle and the tendon that attaches it to a bone.",
             "correct": False,
             "why": "A tendon cannot contract, so it is not half of a pair. "
                    "A pair is two muscles."},
            {"text": "Two muscles on either side of a joint, pulling it in "
                     "opposite directions.",
             "correct": True},
            {"text": "A muscle that can pull a bone one way and push it back "
                     "the other.",
             "correct": False,
             "why": "No muscle can push, which is exactly why a second one is "
                    "needed."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e07",
        "band": "easier",
        "text": "Where is the triceps, and what does contracting it do?",
        "options": [
            {"text": "At the front of the upper arm; it bends the elbow.",
             "correct": False,
             "why": "That describes the biceps. The triceps sits behind the "
                    "elbow and does the opposite job."},
            {"text": "At the back of the upper arm; it straightens the elbow.",
             "correct": True},
            {"text": "At the back of the forearm; it turns the wrist over.",
             "correct": False,
             "why": "The triceps works the elbow, not the wrist, and it lies "
                    "in the upper arm."},
            {"text": "At the back of the upper arm; it bends the elbow.",
             "correct": False,
             "why": "Right place, wrong movement. A pull behind the elbow can "
                    "only swing the forearm down and straighten the arm."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e08",
        "band": "easier",
        "text": "What is a muscle doing when it relaxes?",
        "options": [
            {"text": "Pushing the bone gently back towards where it started.",
             "correct": False,
             "why": "No muscle pushes, relaxed or otherwise. Something else "
                    "has to move the bone back."},
            {"text": "Stretching itself out to its long resting shape.",
             "correct": False,
             "why": "A muscle has no way of making itself longer. It lets go, "
                    "and its partner or a weight draws it long."},
            {"text": "Still pulling, but more gently than it was before.",
             "correct": False,
             "why": "That would leave it fighting its partner. Relaxing means "
                    "it has stopped pulling altogether."},
            {"text": "Letting go, so that something else can lengthen it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e09",
        "band": "easier",
        "text": "Which of these is the one thing a muscle cannot do?",
        "options": [
            {"text": "Shorten, and pull the bone it is attached to.",
             "correct": False,
             "why": "That is the only thing it does. Shortening and pulling "
                    "is what contracting means."},
            {"text": "Stop pulling, and let its partner lengthen it.",
             "correct": False,
             "why": "That is relaxing, and every muscle does it. It is half "
                    "of how a pair works."},
            {"text": "Keep pulling while a weight draws it out longer.",
             "correct": False,
             "why": "That is what happens when you lower a heavy box slowly. "
                    "It is hard work, but a muscle can certainly do it."},
            {"text": "Push a bone away from itself.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e10",
        "band": "easier",
        "text": "You pull your heel up towards you, bending your knee. Which "
                "muscles are contracting?",
        "options": [
            {"text": "The hamstrings, on the back of the thigh.",
             "correct": True},
            {"text": "The quadriceps, on the front of the thigh.",
             "correct": False,
             "why": "The quadriceps straighten the knee — they are what get "
                    "you up out of a chair. Bending it is their partner's "
                    "job."},
            {"text": "Both of them at once, so the movement stays under "
                     "control.",
             "correct": False,
             "why": "Both at once stiffens the knee and the heel stays where "
                    "it is. One pulls; the other lets go."},
            {"text": "Neither — gravity swings the heel up on its own.",
             "correct": False,
             "why": "Gravity only ever pulls downwards. It can drop a raised "
                    "heel, but it can never lift one."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e11",
        "band": "easier",
        "text": "Gravity can do one of these for you and never the other. "
                "Which way round is it?",
        "options": [
            {"text": "It can bend a hanging arm, but it can never straighten "
                     "one.",
             "correct": False,
             "why": "That is backwards. A hanging forearm falls downwards, "
                    "and downwards is the straightening direction."},
            {"text": "It can do both, which is why the arm muscles are needed "
                     "only for lifting.",
             "correct": False,
             "why": "It only ever pulls one way. Bending a hanging arm has to "
                    "be done by the biceps."},
            {"text": "It can straighten a hanging arm, but it can never bend "
                     "one.",
             "correct": True},
            {"text": "It can do neither, because gravity acts on the whole "
                     "body rather than on one bone.",
             "correct": False,
             "why": "It acts on every part of you, the forearm included — "
                    "which is why an arm falls straight the moment nothing is "
                    "pulling it up."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e12",
        "band": "easier",
        "text": "The muscle down the front of the shin is the calf muscle's "
                "partner. What movement does it produce?",
        "options": [
            {"text": "It lifts the heel off the ground, so that you rise up "
                     "onto your toes.",
             "correct": False,
             "why": "That is the calf's own movement, through the Achilles "
                    "tendon. The two muscles of a pair never do the same "
                    "job."},
            {"text": "It lifts the toes, the opposite of what the calf does.",
             "correct": True},
            {"text": "It bends the knee, pulling the heel up behind you.",
             "correct": False,
             "why": "That is the hamstrings, and they act on the knee. This "
                    "muscle works the ankle."},
            {"text": "It stiffens the ankle so that the calf can pull harder.",
             "correct": False,
             "why": "If it pulled while the calf pulled, the ankle would lock "
                    "and the heel would stay down. It relaxes while the calf "
                    "works."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-e13",
        "band": "easier",
        "text": "A digger's hydraulic ram can push its arm out and pull it "
                "back in. Why can no muscle do both?",
        "options": [
            {"text": "A muscle only shortens, and something that shortens can "
                     "only ever pull.",
             "correct": True},
            {"text": "A muscle is too soft to push anything, though a "
                     "stronger one could.",
             "correct": False,
             "why": "Strength has nothing to do with it. However strong a "
                    "muscle grew, shortening would still only pull."},
            {"text": "A muscle can push, but only while it is relaxed rather "
                     "than contracted.",
             "correct": False,
             "why": "Relaxing is letting go. A muscle that has let go does "
                    "even less to the bone than one that is pulling."},
            {"text": "A muscle can push, but only against a bone that is "
                     "already moving.",
             "correct": False,
             "why": "There is no push in a muscle at all. Everything it does "
                    "to a bone is a pull."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-03-s05",
        "band": "standard",
        "text": "Someone's biceps and triceps are both healthy, but the "
                "tendon joining the biceps to the forearm bone snaps. What "
                "can they no longer do?",
        "options": [
            {"text": "Nothing changes, because the biceps is still attached "
                     "at its other end.",
             "correct": False,
             "why": "A muscle moves a bone only if its pull reaches that "
                    "bone. With the lower attachment gone, the forearm never "
                    "feels it."},
            {"text": "Bend that elbow against a resistance — the pull cannot "
                     "reach the forearm.",
             "correct": True},
            {"text": "Straighten that elbow, because the biceps was what "
                     "pulled the forearm back down.",
             "correct": False,
             "why": "Straightening is the triceps' job, and gravity does it "
                    "too on a hanging arm. Both of those still work."},
            {"text": "Relax the biceps, because a snapped tendon leaves the "
                     "muscle permanently contracted and bunched.",
             "correct": False,
             "why": "The muscle can still let go. What it has lost is the "
                    "connection carrying its pull to the bone."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s06",
        "band": "standard",
        "text": "You hold a dumbbell dead still, half way through a curl, "
                "with the elbow bent. Is the biceps contracting?",
        "options": [
            {"text": "No — nothing is moving, so nothing is contracting.",
             "correct": False,
             "why": "Let go and the weight drops. Something is pulling hard; "
                    "it is simply not winning."},
            {"text": "No — the biceps has locked at that length and has "
                     "stopped working.",
             "correct": False,
             "why": "There is no lock in a muscle. It is pulling "
                    "continuously, and paying for it in energy."},
            {"text": "Yes — it is pulling hard without shortening any "
                     "further.",
             "correct": True},
            {"text": "Yes, but it is the triceps, because a held weight has "
                     "to be stopped from rising.",
             "correct": False,
             "why": "The weight is trying to straighten the arm, not raise "
                    "it. What has to be resisted is that straightening, and "
                    "resisting it is the biceps' pull."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s07",
        "band": "standard",
        "text": "Someone loses the use of the muscle down the front of their "
                "shin. Which everyday movement goes, and which still works?",
        "options": [
            {"text": "Lifting the toes goes; rising onto tiptoes still works, "
                     "because the calf is untouched.",
             "correct": True},
            {"text": "Rising onto tiptoes goes; lifting the toes still works, "
                     "because the calf does that.",
             "correct": False,
             "why": "Two jobs swapped over. The calf pulls the heel up "
                    "through the Achilles tendon; the front muscle lifts the "
                    "toes."},
            {"text": "Both go, because a pair cannot work at all with one "
                     "muscle missing.",
             "correct": False,
             "why": "The surviving muscle still pulls its own way. What is "
                    "lost is the movement back."},
            {"text": "Neither goes, because gravity can replace either muscle "
                     "at the ankle.",
             "correct": False,
             "why": "Gravity only pulls downwards. It can drop a lifted toe, "
                    "but it can neither lift one nor raise a heel."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s08",
        "band": "standard",
        "text": "The biceps attaches in front of the elbow and the triceps "
                "behind it. Why does that decide which way each one moves the "
                "forearm?",
        "options": [
            {"text": "It does not — the direction is decided by which of the "
                     "two is the stronger.",
             "correct": False,
             "why": "Strength decides how hard, not which way. A pull behind "
                    "the elbow can only ever open it."},
            {"text": "It does not — each muscle can pull either way, "
                     "depending on what the brain asks it for.",
             "correct": False,
             "why": "A muscle pulls towards itself and nowhere else. Where it "
                    "is attached is the whole of its choice."},
            {"text": "It does, because the muscle in front is longer and so "
                     "travels further.",
             "correct": False,
             "why": "Length is not the point. What matters is which side of "
                    "the joint the pull acts on."},
            {"text": "A muscle pulls towards itself: in front folds the "
                     "joint, behind opens it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s09",
        "band": "standard",
        "text": "A student calls a relaxed muscle 'switched off'. Using the "
                "arm, say what the difference is.",
        "options": [
            {"text": "There is no difference at all — both of them are doing "
                     "nothing at that particular moment.",
             "correct": False,
             "why": "The difference is what happens next. A relaxed biceps "
                    "bends the elbow the moment it is asked; a switched-off "
                    "one never will again."},
            {"text": "A relaxed muscle can pull again the instant it is asked "
                     "to; a switched-off one cannot pull at all.",
             "correct": True},
            {"text": "A relaxed muscle stays shorter than a switched-off one, "
                     "which simply hangs loose and long.",
             "correct": False,
             "why": "Both are lengthened by whatever happens to be pulling on "
                    "them. The difference is not their length but what they "
                    "can still do."},
            {"text": "A relaxed muscle is being stretched by its partner, and a "
                     "switched-off one is not being stretched.",
             "correct": False,
             "why": "Either one can be lengthened by a pull. The real "
                    "difference is that only one of them can still "
                    "contract."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s10",
        "band": "standard",
        "text": "Someone falls asleep sitting up and their head drops "
                "forward. What does that tell you about the muscles that had "
                "been holding the head up?",
        "options": [
            {"text": "They have gone into a sudden spasm and pulled the head "
                     "down onto the chest.",
             "correct": False,
             "why": "If they were pulling, the head would come up rather than "
                    "fall. It falls because nothing is pulling."},
            {"text": "They have stretched themselves out on their own, letting "
                     "the head down slowly onto the chest.",
             "correct": False,
             "why": "A muscle cannot lengthen itself. They let go, and the "
                    "weight of the head did the rest."},
            {"text": "They have relaxed, and nothing pushes a head back up — "
                     "a muscle has to pull it.",
             "correct": True},
            {"text": "They are still pulling as hard as ever, but gravity has "
                     "become stronger than they are.",
             "correct": False,
             "why": "Awake, those same muscles hold the head up easily. What "
                    "changed is that they stopped pulling, not that gravity "
                    "grew."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s11",
        "band": "standard",
        "text": "Someone is told to stretch their hamstrings after a run. "
                "Using what you know about relaxing, what is actually pulling "
                "the hamstrings long?",
        "options": [
            {"text": "The person's own weight, or another muscle — a "
                     "hamstring cannot lengthen itself.",
             "correct": True},
            {"text": "The hamstrings themselves, which lengthen once they are "
                     "told to relax.",
             "correct": False,
             "why": "Relaxing is letting go, and letting go adds no length. "
                    "Something outside the muscle has to draw it out."},
            {"text": "The quadriceps, pushing against them from the other "
                     "side of the thigh.",
             "correct": False,
             "why": "Muscles never push. The quadriceps can pull the knee "
                    "straight, and it is that pull which lengthens the "
                    "hamstrings."},
            {"text": "The tendons, which stretch and draw the muscle out "
                     "behind them.",
             "correct": False,
             "why": "A tendon carries a pull; it does not make one. Whatever "
                    "is doing the pulling is outside the muscle."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s12",
        "band": "standard",
        "text": "A student writes: 'When you punch, the biceps pushes the "
                "forearm out.' Correct it.",
        "options": [
            {"text": "The biceps pulls the forearm out, because a pull in "
                     "front of the elbow straightens it.",
             "correct": False,
             "why": "A pull in front of the elbow folds it. The straightening "
                    "pull has to come from behind the joint."},
            {"text": "The biceps relaxes, and relaxing is what straightens "
                     "the arm.",
             "correct": False,
             "why": "Relaxing lets the arm be straightened; it does not do "
                    "the straightening. Something still has to pull."},
            {"text": "The triceps pushes the forearm out from behind the "
                     "elbow.",
             "correct": False,
             "why": "The muscle is right and the word is not. Nothing in the "
                    "body pushes — the triceps pulls on the bone behind the "
                    "elbow."},
            {"text": "The triceps pulls on the bone behind the elbow, and the "
                     "forearm swings out straight.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-s13",
        "band": "standard",
        "text": "An anaesthetic switches off both muscles of the ankle pair. "
                "Predict what the foot does.",
        "options": [
            {"text": "It locks in whatever position it was in, because "
                     "neither muscle can move it.",
             "correct": False,
             "why": "Locking needs both muscles pulling. With both switched "
                    "off, nothing is holding it anywhere."},
            {"text": "It hangs down, because nothing is pulling and the "
                     "weight of the foot takes it there.",
             "correct": True},
            {"text": "It lifts, because the calf relaxes and the foot returns "
                     "to its resting angle.",
             "correct": False,
             "why": "Relaxing lifts nothing. Raising the toes needs the "
                    "muscle at the front to pull, and it cannot."},
            {"text": "It moves to and fro, because the two muscles no longer "
                     "balance each other.",
             "correct": False,
             "why": "Neither is pulling, so there is nothing to be out of "
                    "balance. It hangs, and it stays hanging."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-03-h05",
        "band": "harder",
        "text": "A fish swims by beating its tail from side to side, and it "
                "has blocks of muscle down both sides of its body. Why does "
                "it need both sets?",
        "options": [
            {"text": "One set bends the tail and the other stiffens the body "
                     "so the bend does not spread.",
             "correct": False,
             "why": "Both sets do the same kind of thing — they pull. A pull "
                    "on one side bends the tail that way, and only a pull on "
                    "the other side brings it back."},
            {"text": "One set pulls the tail across, and the other pushes it "
                     "back the other way.",
             "correct": False,
             "why": "No muscle pushes, in a fish or in you. Both sets pull, "
                    "from opposite sides."},
            {"text": "A muscle only pulls, so bending the tail one way and "
                     "back again needs one set on each side.",
             "correct": True},
            {"text": "Two sets simply give twice the force for the same beat "
                     "of the tail.",
             "correct": False,
             "why": "They lie on opposite sides, so pulling together would "
                    "stiffen the tail rather than double the beat."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h06",
        "band": "harder",
        "text": "A boxer's punch and a swimmer's stroke both push something "
                "away. Explain how, given that no muscle can push.",
        "options": [
            {"text": "A pull behind the joint straightens the limb, and the "
                     "limb pushes.",
             "correct": True},
            {"text": "The muscle contracts so hard that its pull turns into a "
                     "push at the far end of the bone.",
             "correct": False,
             "why": "A pull does not become a push however hard it is. What "
                    "straightens the limb is a pull on the other side of the "
                    "joint."},
            {"text": "The limb's own weight is thrown forwards, and the "
                     "weight does the pushing.",
             "correct": False,
             "why": "Weight alone would let the limb fold. The straightening "
                    "is driven by a muscle pulling behind the joint."},
            {"text": "The relaxing muscle pushes the bone out as it returns "
                     "to its resting length.",
             "correct": False,
             "why": "A relaxed muscle does nothing at all to the bone. "
                    "Whatever moves it is being pulled by the partner."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h07",
        "band": "harder",
        "text": "At the elbow, gravity helps the triceps. At the knee, "
                "gravity fights the quadriceps. How can the same force be a "
                "help at one joint and a hindrance at the other?",
        "options": [
            {"text": "Gravity acts downwards in the arm and upwards in the "
                     "leg, because the leg is below the body.",
             "correct": False,
             "why": "Gravity pulls downwards everywhere. What differs is "
                    "which movement downwards happens to be at each joint."},
            {"text": "The arm is lighter than the leg, so gravity is too weak "
                     "to be a hindrance there.",
             "correct": False,
             "why": "Weight is not what changes. Even a heavy arm left "
                    "hanging is straightened by gravity."},
            {"text": "The knee's muscles are stronger, so they can afford to "
                     "work against gravity.",
             "correct": False,
             "why": "Strength is why they can do it, not why they have to. "
                    "They have to because of the direction gravity happens to "
                    "pull the knee."},
            {"text": "Gravity pulls down: that straightens a hanging arm, "
                     "bends a standing knee.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h08",
        "band": "harder",
        "text": "A surgeon reattaches the Achilles tendon to the top of the "
                "foot instead of the heel bone. What would contracting the "
                "calf muscle now do?",
        "options": [
            {"text": "Nothing at all, because a muscle can only work through "
                     "its tendon in its own place.",
             "correct": False,
             "why": "The tendon is the same cord doing the same job. It would "
                    "still carry the pull — to a different bone, with a "
                    "different result."},
            {"text": "Lift the toes rather than the heel, because where a "
                     "pull attaches decides what it does.",
             "correct": True},
            {"text": "Lift the heel as before, because the calf muscle itself "
                     "has not been changed.",
             "correct": False,
             "why": "The muscle is unchanged, but a pull acts where it "
                    "attaches. Moved to the top of the foot, it can no longer "
                    "raise the heel."},
            {"text": "Bend the knee, because the calf's pull would travel up "
                     "the leg instead.",
             "correct": False,
             "why": "A muscle draws its two attachments towards each other. "
                    "Moving the lower one changes what happens at the foot, "
                    "not at the knee."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h09",
        "band": "harder",
        "text": "In a press-up the elbows straighten on the way up and bend "
                "on the way down. Which muscle is working in each half?",
        "options": [
            {"text": "The triceps on the way up, and the biceps on the way "
                     "down.",
             "correct": False,
             "why": "On the way down the body is being lowered rather than "
                    "pulled down. It is the triceps holding on, letting the "
                    "elbow bend a little at a time."},
            {"text": "The biceps on the way up, and the triceps on the way "
                     "down.",
             "correct": False,
             "why": "The biceps bends the elbow, which is what happens going "
                    "down. Going up the elbow straightens, and that is the "
                    "triceps."},
            {"text": "The triceps in both halves — pulling to straighten "
                     "going up, and pulling while drawn longer going down.",
             "correct": True},
            {"text": "The triceps on the way up, and neither on the way down, "
                     "because gravity does that half.",
             "correct": False,
             "why": "Gravity is doing the moving, but let go entirely and you "
                    "land on your face. The triceps is pulling all the way "
                    "down."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h10",
        "band": "harder",
        "text": "A nerve injury switches off someone's biceps. Which is lost: "
                "bending that elbow, or lowering a mug slowly to the table?",
        "options": [
            {"text": "Both — the biceps bends the elbow, and it also lets a "
                     "load down a little at a time.",
             "correct": True},
            {"text": "Only bending is lost. Lowering the mug is gravity's own "
                     "work, so that survives the injury untouched.",
             "correct": False,
             "why": "Gravity does the moving, but something has to hold on or "
                    "the mug drops. That something is the biceps, pulling "
                    "while it is drawn longer."},
            {"text": "Only lowering is lost. Bending survives it, because the "
                     "triceps can pull the forearm up in its place.",
             "correct": False,
             "why": "The triceps attaches behind the elbow, so its pull can "
                    "only straighten the arm. Nothing else can bend it."},
            {"text": "Neither is lost. Between them the triceps and gravity can "
                     "still manage both of these movements.",
             "correct": False,
             "why": "Between them they can straighten the arm and let it "
                    "fall. Neither can bend it, and neither can hold a load "
                    "back on the way down."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h11",
        "band": "harder",
        "text": "Both muscles at someone's elbow are switched off. A student "
                "says the arm will therefore be locked in place. Predict what "
                "actually happens.",
        "options": [
            {"text": "It locks, because with neither muscle pulling nothing "
                     "can change the angle.",
             "correct": False,
             "why": "Nothing needs to pull for the angle to change. The "
                    "forearm has weight, and weight takes it down."},
            {"text": "It locks, because the joint itself holds whatever "
                     "position it was left in.",
             "correct": False,
             "why": "A joint has no lock of its own. What stiffens an elbow "
                    "is both muscles pulling, which is the opposite of "
                    "switched off."},
            {"text": "It bends up, because a switched-off muscle shortens and "
                     "takes the forearm with it.",
             "correct": False,
             "why": "A switched-off muscle does not shorten; it does nothing "
                    "at all. Nothing here can bend the arm."},
            {"text": "It hangs and straightens under its own weight — locking "
                     "needs both muscles pulling, not neither.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h12",
        "band": "harder",
        "text": "A sloth hangs upside down from a branch for hours with its "
                "limbs bent. Which of its muscles must keep working, and "
                "which can let go?",
        "options": [
            {"text": "The straightening muscles must work, because they hold "
                     "the limb out towards the branch.",
             "correct": False,
             "why": "Straightening would drop it. What has to be held is the "
                    "bend, and a bend is held by the muscles that make one."},
            {"text": "Neither has to work, because a hanging animal is held "
                     "up by gravity.",
             "correct": False,
             "why": "Gravity is what is trying to pull it off the branch. "
                    "Something has to pull the other way."},
            {"text": "The bending muscles must keep pulling; gravity does the "
                     "straightening.",
             "correct": True},
            {"text": "Both must pull at once, because that is the only way to "
                     "hold a joint still.",
             "correct": False,
             "why": "Both pulling is one way to hold a joint still, but here "
                    "gravity is already pulling one way, so only the other "
                    "side has to work."},
        ],
        "figure": None,
    },
    {
        "id": "b2-03-h13",
        "band": "harder",
        "text": "A prosthetic hand pulls each finger shut with a cable and "
                "opens it again with a spring. A student says a spring is not "
                "a muscle, so the design cannot copy a hand. What does the "
                "spring replace?",
        "options": [
            {"text": "The tendon, because a spring and a tendon both carry a "
                     "pull to the finger.",
             "correct": False,
             "why": "The cable is doing the tendon's job of carrying a pull. "
                    "The spring is supplying a pull of its own, from the "
                    "other side."},
            {"text": "The second muscle of the pair — something has to pull "
                     "the finger the other way.",
             "correct": True},
            {"text": "The joint, because the spring decides how far the "
                     "finger is able to bend.",
             "correct": False,
             "why": "The joint is still there at the knuckle. What the spring "
                    "supplies is the return pull."},
            {"text": "Nothing — the design has no equivalent, which is why it "
                     "cannot copy a hand.",
             "correct": False,
             "why": "It has one. Any second pull from the opposite side does "
                    "the partner's job, whether it comes from a muscle, a "
                    "spring or a second cable."},
        ],
        "figure": None,
    },
]
