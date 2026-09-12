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

    # ══ MRB-338 expansion ══════════════════════════════════════════════
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": 'b2-03-e14',
        "band": 'easier',
        "text": 'The iliopsoas at the front of the hip and the gluteus maximus at the back are an antagonistic pair. Which contracts to swing your leg forward in a stride?',
        "options": [
            {"text": 'The iliopsoas.', "correct": True},
            {"text": 'The gluteus maximus.', "correct": False,
             "why": "That muscle swings the leg backward, driving the stride's push-off, the opposite job."},
            {"text": 'Both, pulling together.', "correct": False,
             "why": 'Both pulling together stiffens the hip rather than swinging it either way.'},
            {"text": 'Neither — gravity swings the leg forward.', "correct": False,
             "why": 'Gravity only ever pulls straight down. Swinging a leg forward needs a muscle pulling it there.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e15',
        "band": 'easier',
        "text": 'Muscles on the front of the forearm bend the wrist towards the palm; muscles on the back bend it the other way. Which set contracts to curl the wrist towards the palm?',
        "options": [
            {"text": 'The back set.', "correct": False,
             "why": 'The back set bends the wrist the other way, lifting the hand rather than curling it towards the palm.'},
            {"text": 'The front set.', "correct": True},
            {"text": 'Both sets together.', "correct": False,
             "why": 'Both together locks the wrist rather than curling it in either direction.'},
            {"text": "Neither — the hand's own weight curls it.", "correct": False,
             "why": 'Weight alone would pull the wrist down, not curl it towards the palm.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e16',
        "band": 'easier',
        "text": 'Muscles between the ribs come in two sets: one lifts the ribcage for a breath in, the other pulls it down for a forced breath out. Which set contracts to breathe in?',
        "options": [
            {"text": 'The set that pulls the ribcage down.', "correct": False,
             "why": 'That set works for a forced breath out, not for breathing in.'},
            {"text": 'Both sets, contracting together.', "correct": False,
             "why": 'Both together would hold the ribcage still rather than lifting it for a breath.'},
            {"text": 'The set that lifts the ribcage.', "correct": True},
            {"text": 'Neither — the lungs lift the ribcage themselves.', "correct": False,
             "why": 'The lungs cannot pull on bone. Something has to contract to lift the ribcage.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e17',
        "band": 'easier',
        "text": 'A quiet breath out at rest needs no muscle to contract at all. What does the job instead?',
        "options": [
            {"text": 'The diaphragm contracts a second time.', "correct": False,
             "why": "The diaphragm's one contraction was for breathing in. A quiet breath out needs no contraction from it."},
            {"text": 'Gravity pulls the ribcage back down.', "correct": False,
             "why": "Gravity acts straight down on the body, not specifically on the ribcage's shape."},
            {"text": "The heart's beat pushes the ribcage back in.", "correct": False,
             "why": 'The heartbeat moves blood, not the ribcage. Springing back is what a stretched, elastic chest does on its own.'},
            {"text": 'The stretched ribcage and lungs simply spring back.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e18',
        "band": 'easier',
        "text": 'The jaw closes using the masseter, at the corner of the jaw. Opening the jaw again needs what?',
        "options": [
            {"text": 'A separate muscle contracting to pull it open.', "correct": True},
            {"text": 'The masseter relaxing on its own.', "correct": False,
             "why": 'Relaxing only lets go — it cannot pull the jaw open by itself.'},
            {"text": 'The weight of the lower jaw alone, every single time.', "correct": False,
             "why": 'Gravity helps a little, but the jaw opens fully and quickly enough that a muscle is doing real work too.'},
            {"text": 'The tongue, pushing the jaw down from inside.', "correct": False,
             "why": 'The tongue is a separate structure and does not drive the jaw joint.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e19',
        "band": 'easier',
        "text": 'Starting a sit-up curls the trunk forward. Which muscles contract to do that?',
        "options": [
            {"text": 'The erector spinae, running up the back.', "correct": False,
             "why": 'That set straightens and arches the back, the opposite movement to curling forward.'},
            {"text": 'The abdominal muscles, down the front of the trunk.', "correct": True},
            {"text": 'Both sets, pulling together.', "correct": False,
             "why": 'Both together would stiffen the trunk rather than curling it forward.'},
            {"text": "Neither — the head's weight pulls the trunk up.", "correct": False,
             "why": "The head's weight alone cannot curl the whole trunk forward against gravity."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e20',
        "band": 'easier',
        "text": 'One muscle ring closes your eyelid; a separate muscle opens it again. Which is contracting while your eye is shut?',
        "options": [
            {"text": 'The opening muscle, above the eye.', "correct": False,
             "why": 'That one opens the eyelid. While the eye is shut, it is relaxed, not contracting.'},
            {"text": 'Both muscles, holding the lid still.', "correct": False,
             "why": 'Both together would leave the eyelid stiff in whatever position it started in, not shut.'},
            {"text": 'The closing ring, round the eye.', "correct": True},
            {"text": 'Neither — the eyelid falls shut under its own weight.', "correct": False,
             "why": 'An eyelid is far too light to close itself under gravity. A muscle drives the movement.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e21',
        "band": 'easier',
        "text": 'The gluteus maximus, at the back of the hip, is the largest muscle in the body. Which everyday movement does it drive?',
        "options": [
            {"text": 'Bending the elbow, as when lifting a bag.', "correct": False,
             "why": 'That movement belongs to the biceps, in the arm, nowhere near the hip.'},
            {"text": 'Turning the head from side to side.', "correct": False,
             "why": 'Neck muscles turn the head. The gluteus maximus sits at the hip.'},
            {"text": 'Lifting the toes off the ground.', "correct": False,
             "why": 'That movement belongs to a muscle at the front of the shin, far from the hip.'},
            {"text": 'Straightening the hip, as when climbing stairs.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e22',
        "band": 'easier',
        "text": 'The word biceps means two-headed, and triceps means three-headed. What is this naming based on?',
        "options": [
            {"text": 'How many separate points the muscle starts from.', "correct": True},
            {"text": 'How many bones the muscle is attached to.', "correct": False,
             "why": 'A biceps and a triceps both span the same two bones, so that count cannot be what separates the names. The name counts something else about the muscle itself.'},
            {"text": 'How many joints the muscle can move.', "correct": False,
             "why": 'The biceps moves more than one joint, but that is not what the name is counting.'},
            {"text": 'How many times the muscle can contract in a row alone.', "correct": False,
             "why": 'A muscle can contract repeatedly however many heads it has. The name refers to its starting points.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e23',
        "band": 'easier',
        "text": 'A hamstring strain often happens while sprinting. At what point in the stride is the hamstring under the most strain?',
        "options": [
            {"text": 'While the leg is standing still on the ground.', "correct": False,
             "why": 'The hamstring is not driving anything while the leg stands still — the strain comes during a fast movement.'},
            {"text": 'While it is slowing the leg down as it swings forward.', "correct": True},
            {"text": 'While the person is standing up from sitting.', "correct": False,
             "why": 'That movement uses the quadriceps and gluteus maximus, not the hamstring under strain.'},
            {"text": 'While the runner is resting between sprints.', "correct": False,
             "why": 'No muscle is working hard at rest. The strain happens during the fast swing of a sprint.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e24',
        "band": 'easier',
        "text": 'A surgeon moves where a working tendon attaches on a bone, without touching the muscle itself. What can change as a result?',
        "options": [
            {"text": 'Nothing — a muscle always does the same job.', "correct": False,
             "why": "A muscle's job depends on where its tendon pulls. Moving the attachment changes what the pull does."},
            {"text": 'Only how fast the muscle can contract.', "correct": False,
             "why": 'Contraction speed depends on the muscle fibres themselves, not on where the tendon is anchored.'},
            {"text": 'The movement that muscle produces.', "correct": True},
            {"text": 'Only how much energy the muscle uses.', "correct": False,
             "why": "Energy use depends on how hard the muscle works, not on the tendon's attachment point."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e25',
        "band": 'easier',
        "text": 'Someone trains only their biceps for years and never their triceps. What is a likely result at the elbow?',
        "options": [
            {"text": 'The elbow gains a new direction of movement.', "correct": False,
             "why": 'Training a muscle does not change the shape of the bone ends, so no new direction is gained.'},
            {"text": 'The triceps grows to match the biceps anyway.', "correct": False,
             "why": 'A muscle grows from being used, not from its partner being trained instead.'},
            {"text": 'Nothing changes, since a pair always stays balanced.', "correct": False,
             "why": 'A pair is not automatically balanced. Training one side and not the other can shift the resting pull.'},
            {"text": 'The arm tends to rest in a slightly bent position.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e26',
        "band": 'easier',
        "text": "Someone carries a full tray steady at arm's length. What are the biceps and triceps doing at the elbow?",
        "options": [
            {"text": 'Both contracting together, to stiffen the joint.', "correct": True},
            {"text": 'Only the biceps, holding the tray up.', "correct": False,
             "why": 'The biceps alone would let the elbow drift, since nothing is bracing it from the other side.'},
            {"text": 'Only the triceps, holding the tray steady.', "correct": False,
             "why": 'The triceps alone would let the elbow drift the other way, with nothing bracing it.'},
            {"text": "Neither — the tray's own weight holds the arm still.", "correct": False,
             "why": 'A weight cannot hold a joint steady by itself. Something has to be actively bracing it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e27',
        "band": 'easier',
        "text": "In an arm-wrestle, one person's biceps and triceps both contract hard at the same elbow. What happens at that joint?",
        "options": [
            {"text": 'It bends twice as fast as usual.', "correct": False,
             "why": 'The two pulls oppose each other, so nothing is added to make it faster.'},
            {"text": 'It stiffens and holds its position.', "correct": True},
            {"text": 'It straightens twice as fast as usual.', "correct": False,
             "why": 'The opposing pull cancels out any extra speed in either direction.'},
            {"text": 'Nothing happens in either muscle.', "correct": False,
             "why": 'Both muscles are working hard and using energy, even though the joint itself does not move.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e28',
        "band": 'easier',
        "text": "A bird's pectoral muscle pulls its wing down for the power stroke. What must pull the wing back up?",
        "options": [
            {"text": 'The pectoral muscle, stretching itself back out.', "correct": False,
             "why": 'A muscle cannot lengthen itself. Something else has to pull the wing back up.'},
            {"text": 'Air pressure, pushing the wing upward.', "correct": False,
             "why": 'Air resistance acts on the wing, but it does not supply the pull that lifts it for the next stroke.'},
            {"text": 'A separate muscle, on the other side of the joint.', "correct": True},
            {"text": 'Nothing — the wing simply swings up under its own weight.', "correct": False,
             "why": 'Weight only ever pulls a wing down, never up.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e29',
        "band": 'easier',
        "text": 'A knuckle bends the finger forward and also spreads it sideways. How many antagonistic pairs does moving it back and forth in both of those directions need?',
        "options": [
            {"text": 'One pair, covering both directions at once.', "correct": False,
             "why": 'A single pair only ever covers one direction, back and forth along one line.'},
            {"text": 'Four pairs, one for each of the four types of joint.', "correct": False,
             "why": 'Joint type has nothing to do with how many pairs a joint needs — only how many directions it moves in does.'},
            {"text": 'None — a knuckle moves without needing any muscle pair.', "correct": False,
             "why": 'Every direction a joint moves in still needs a muscle pulling it there and a partner to bring it back.'},
            {"text": 'Two pairs, one for each direction.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e30',
        "band": 'easier',
        "text": "A cat's claws are pulled out by one tendon and drawn back in by another. Which muscle is contracting while the claws are out?",
        "options": [
            {"text": 'The one whose tendon pulls the claw out.', "correct": True},
            {"text": 'The one whose tendon draws the claw back in.', "correct": False,
             "why": 'That muscle is relaxed while the claw is out — it is the one that draws it back in again.'},
            {"text": 'Both muscles, pulling together.', "correct": False,
             "why": 'Both together would hold the claw wherever it already was, not extend it.'},
            {"text": 'Neither — the claw simply springs out on its own.', "correct": False,
             "why": 'A claw cannot move itself. A muscle has to pull it out through its tendon.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e31',
        "band": 'easier',
        "text": 'When a muscle relaxes, does it push its partner back to the starting position?',
        "options": [
            {"text": 'Yes — a relaxed muscle pushes gently as it lengthens.', "correct": False,
             "why": 'No muscle can push, relaxed or contracted. Something else has to do the pulling back.'},
            {"text": 'No — relaxing only lets go; it never pushes anything.', "correct": True},
            {"text": 'Yes, but only while it is still slightly contracted.', "correct": False,
             "why": 'A muscle that is still contracted is not relaxed. Relaxing means letting go completely.'},
            {"text": 'It depends on which joint the muscle is at.', "correct": False,
             "why": 'Relaxing means the same thing at every joint: letting go, never pushing.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-e32',
        "band": 'easier',
        "text": 'A joint that moves only one way still needs two muscles rather than one. Why?',
        "options": [
            {"text": 'One muscle would not be strong enough on its own.', "correct": False,
             "why": 'Strength is not the reason. A single muscle could be made as strong as needed and still only pull one way.'},
            {"text": 'One muscle would tire out too quickly by itself.', "correct": False,
             "why": 'Tiring is not the reason two are needed — the reason is that a muscle can only ever pull, never push back.'},
            {"text": 'One muscle can move it there; a second is needed to bring it back.', "correct": True},
            {"text": 'One muscle cannot be attached to a joint on its own.', "correct": False,
             "why": 'A single muscle can be attached across a joint. The reason two are needed is direction, not attachment.'},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": 'b2-03-s14',
        "band": 'standard',
        "text": 'Someone walks with an unusually long stride. Predict which muscle of the hip pair, the iliopsoas or the gluteus maximus, is working harder than usual during the forward swing of the leg.',
        "options": [
            {"text": 'The gluteus maximus, driving a stronger push-off.', "correct": False,
             "why": 'The push-off is the other half of the stride. During the forward swing the gluteus maximus is letting go, not pulling.'},
            {"text": 'The iliopsoas, swinging the leg further forward.', "correct": True},
            {"text": 'Both, equally, since a longer stride needs no more effort from either.', "correct": False,
             "why": 'A longer stride is more work than a normal one, not the same amount, for the muscle driving the swing.'},
            {"text": 'Neither — a longer stride comes from the knee, not the hip.', "correct": False,
             "why": "The knee bends to let the foot clear the ground, but the hip's own muscles are what swing the leg further."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s15',
        "band": 'standard',
        "text": "A tendon injury weakens the wrist flexors on the front of someone's forearm, while the extensors on the back stay healthy. Predict what their wrist rests like.",
        "options": [
            {"text": 'Curled towards the palm, from the flexors shortening on their own.', "correct": False,
             "why": 'A weakened muscle does not shorten on its own — it simply pulls less than before.'},
            {"text": 'Exactly straight, since weakening one side does not change the resting position.', "correct": False,
             "why": "A pair's resting position depends on both sides balancing each other. Weakening one side shifts it."},
            {"text": 'Bent slightly back, since the healthy extensors now pull with less to resist them.', "correct": True},
            {"text": 'Curled towards the palm, since the extensors now pull harder in that direction.', "correct": False,
             "why": 'The extensors pull the wrist the opposite way, back rather than towards the palm.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s16',
        "band": 'standard',
        "text": 'A rib injury damages the muscles that lift the ribcage for a breath in, but not the ones used for a forced breath out. Predict what the person struggles with.',
        "options": [
            {"text": 'Breathing out hard, such as blowing out a candle.', "correct": False,
             "why": 'That relies on the undamaged set. The struggle belongs to the other half of the pair.'},
            {"text": 'Both breathing in and breathing out equally.', "correct": False,
             "why": 'Only one set of the pair is damaged, so only one direction of the movement is affected.'},
            {"text": 'Neither — the diaphragm alone handles all breathing.', "correct": False,
             "why": 'The rib muscles genuinely add to breathing in. Damaging them has a real effect.'},
            {"text": 'Taking a proper breath in.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s17',
        "band": 'standard',
        "text": "During hard exercise, breathing out becomes an active movement rather than the usual quiet spring-back. What does that tell you about the ribcage's muscles?",
        "options": [
            {"text": 'A second set is now contracting to pull the ribcage down faster.', "correct": True},
            {"text": 'The same set that lifts the ribcage is now working twice as hard.', "correct": False,
             "why": "That set only ever lifts the ribcage. Pulling it down faster is a different muscle's job."},
            {"text": 'The diaphragm is now contracting for the breath out as well as in.', "correct": False,
             "why": "The diaphragm's contraction is for breathing in. Forced breathing out uses other muscles."},
            {"text": 'No muscle is involved — the lungs simply empty faster under exercise.', "correct": False,
             "why": 'Emptying faster than the elastic spring-back needs an active pull, which means a muscle contracting.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s18',
        "band": 'standard',
        "text": 'A dentist numbs only the masseter, the muscle that closes the jaw. Predict what the patient can still do.',
        "options": [
            {"text": 'Close the jaw normally, using a different muscle instead.', "correct": False,
             "why": 'The masseter is specifically numbed, so closing with full force through it is exactly what is lost.'},
            {"text": 'Open the jaw, but not close it with full force.', "correct": True},
            {"text": 'Neither open nor close the jaw at all.', "correct": False,
             "why": 'Only the closing muscle is numbed. The opening muscle is untouched and still works.'},
            {"text": 'Close the jaw as normal, since gravity does the opening anyway.', "correct": False,
             "why": "Gravity helping the jaw open does not restore the numbed muscle's closing force."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s19',
        "band": 'standard',
        "text": 'Someone with weak abdominal muscles but a healthy erector spinae tends to stand with their back arched further than normal. Explain why.',
        "options": [
            {"text": 'The erector spinae has shrunk to match the abdominal muscles.', "correct": False,
             "why": 'A healthy muscle does not shrink because its partner is weak — if anything it pulls with less opposition.'},
            {"text": 'Weak abdominal muscles pull the back into an arch directly.', "correct": False,
             "why": "The abdominal muscles curl the trunk forward when they contract; arching the back is the other muscle's job."},
            {"text": 'The erector spinae now pulls with less resistance from the front.', "correct": True},
            {"text": 'The spine itself has changed shape permanently.', "correct": False,
             "why": 'The bones have not changed shape. The posture shift comes from an imbalance between the two muscle sets.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s20',
        "band": 'standard',
        "text": "A nerve problem leaves someone's eyelid-closing muscle working weakly, while the opening muscle is fine. Predict what happens to that eye.",
        "options": [
            {"text": 'The eye stays shut, since the closing muscle is now permanently contracted.', "correct": False,
             "why": 'A weak muscle contracts less, not more. It would close the eye less firmly, not permanently.'},
            {"text": 'The opening muscle takes over the closing job as well.', "correct": False,
             "why": "A muscle can only pull its own bone in its own direction — it cannot take on its partner's job."},
            {"text": 'Nothing changes, since blinking does not need the closing muscle.', "correct": False,
             "why": "Closing the eye is exactly that muscle's job. Weakening it changes how the eye blinks."},
            {"text": 'The eye stays open more than usual and blinks weakly.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s21',
        "band": 'standard',
        "text": 'The gluteus maximus and the biceps are both muscles that contract and pull. Why can the gluteus maximus produce a much bigger force?',
        "options": [
            {"text": 'It is a much bigger muscle, with more fibres pulling together.', "correct": True},
            {"text": 'It is attached further from the hip joint than the biceps is from the elbow.', "correct": False,
             "why": 'Distance from the joint changes turning effect, not how much force the muscle itself can produce.'},
            {"text": 'It is used more often during the day than the biceps is.', "correct": False,
             "why": 'How often a muscle is used does not by itself decide how much force it can produce.'},
            {"text": 'It has a tendon rather than a direct attachment to bone.', "correct": False,
             "why": 'The biceps pulls on bone through a tendon too, so that is not what separates the two. How much force a muscle makes depends on how much muscle there is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s22',
        "band": 'standard',
        "text": 'The names biceps and triceps count how many heads a muscle starts from. A student assumes more heads always means a stronger muscle. What is wrong with that?',
        "options": [
            {"text": 'It is correct — every extra head always adds more force.', "correct": False,
             "why": "The gluteus maximus has one head and produces a far bigger force than the triceps' three."},
            {"text": "The number of heads says nothing about the muscle's overall size or strength.", "correct": True},
            {"text": 'It is wrong only because the triceps is weaker than the biceps.', "correct": False,
             "why": 'Whether the triceps is weaker is not the point — the flaw is assuming heads and strength are linked at all.'},
            {"text": 'Heads decide speed, not force, so the claim is only half right.', "correct": False,
             "why": 'The number of heads is a naming detail about where a muscle starts, unrelated to either force or speed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s23',
        "band": 'standard',
        "text": 'A sprinter suffers a hamstring strain part-way through a race. What is most likely happening to the hamstring at the moment it tears?',
        "options": [
            {"text": 'It has stopped contracting altogether during the sprint.', "correct": False,
             "why": 'A relaxed muscle is not under the tension that causes a strain — the injury happens while it is working hard.'},
            {"text": 'It is being pushed by the quadriceps on the other side of the thigh.', "correct": False,
             "why": "No muscle can push another. The strain comes from the hamstring's own pull against a fast-moving leg."},
            {"text": 'It is contracting hard while being forcefully lengthened.', "correct": True},
            {"text": 'It has run out of the fuel needed to keep pulling.', "correct": False,
             "why": 'Running out of fuel would weaken the pull, not tear the muscle under sudden tension.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s24',
        "band": 'standard',
        "text": "A tendon transfer moves a working wrist muscle's attachment from the back of the hand to the front, without touching the muscle itself. Predict the effect on the wrist.",
        "options": [
            {"text": 'The muscle stops working, since it is no longer in its usual place.', "correct": False,
             "why": 'The muscle still contracts exactly as before. Only where its pull lands has changed.'},
            {"text": 'The muscle now does both jobs, front and back, at once.', "correct": False,
             "why": 'A muscle pulls towards itself from wherever its tendon is attached — it cannot pull two ways at once.'},
            {"text": "Nothing changes, since a muscle's job never depends on its attachment.", "correct": False,
             "why": "A muscle's job depends entirely on where its pull lands, which is exactly what the surgery has moved."},
            {"text": 'The muscle now bends the wrist rather than lifting it.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s25',
        "band": 'standard',
        "text": "A coach notices one athlete's biceps is visibly bigger than their triceps, from years of arm curls with no matching triceps work. Suggest the resting effect at that elbow.",
        "options": [
            {"text": 'The arm tends to rest slightly bent, from the stronger pull of the biceps.', "correct": True},
            {"text": 'The arm tends to rest fully straight, since the triceps still refuses that direction.', "correct": False,
             "why": 'A weaker triceps refuses the straight direction less firmly, which lets the stronger biceps pull it towards bent.'},
            {"text": 'The elbow gains extra range of movement in both directions.', "correct": False,
             "why": "Training changes how hard each muscle pulls, not the shape of the bone ends that decides the joint's range."},
            {"text": 'Nothing changes, since only one side of a pair being trained has no effect.', "correct": False,
             "why": 'One side pulling much harder than its partner does change the resting balance at the joint.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s26',
        "band": 'standard',
        "text": "A gymnast holds a plank position, with the trunk dead straight and motionless. Which of the trunk's muscles are contracting?",
        "options": [
            {"text": 'Only the erector spinae, holding the back straight.', "correct": False,
             "why": "The erector spinae alone would arch the back, not hold it dead straight against gravity's own pull."},
            {"text": 'Both the abdominals and the erector spinae, together.', "correct": True},
            {"text": 'Only the abdominal muscles, curling the trunk forward.', "correct": False,
             "why": 'The abdominals alone would curl the trunk forward, not hold it dead straight.'},
            {"text": 'Neither — the trunk is simply relaxed and rigid.', "correct": False,
             "why": "A relaxed trunk under gravity's pull would sag, not stay dead straight and motionless."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s27',
        "band": 'standard',
        "text": 'A cat about to pounce keeps its claws retracted, then extends them at the last instant. Which muscle switches from relaxed to contracting at that instant?',
        "options": [
            {"text": 'The one that had been holding the claw drawn in.', "correct": False,
             "why": 'That muscle relaxes to let the claw come out — it does not contract at that instant.'},
            {"text": 'Both muscles, contracting together at that instant.', "correct": False,
             "why": 'Both contracting together would hold the claw wherever it already was, not extend it.'},
            {"text": 'The one whose tendon pulls the claw out.', "correct": True},
            {"text": 'Neither — the claw simply springs forward on its own.', "correct": False,
             "why": 'A claw cannot move by itself. A muscle has to pull it through its tendon.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s28',
        "band": 'standard',
        "text": 'A bird beats its wings much faster than a human can swing an arm. Suggest one reason its flight muscles are built as a strict antagonistic pair rather than one muscle doing both strokes.',
        "options": [
            {"text": 'Two separate muscles beat faster than one large one ever could.', "correct": False,
             "why": 'Speed of contraction depends on the muscle fibres themselves, not on splitting the job between two muscles.'},
            {"text": 'A single muscle would overheat at that speed.', "correct": False,
             "why": 'Overheating is not the reason two muscles are needed — the reason is that a muscle can only ever pull.'},
            {"text": 'Two muscles use less energy overall than one would.', "correct": False,
             "why": 'Two muscles working the wing use their own share of energy each; splitting the job does not itself save energy.'},
            {"text": 'A single muscle can only pull one way, whatever speed is needed.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s29',
        "band": 'standard',
        "text": 'A student says an arm-wrestler should contract both biceps and triceps as hard as possible to win. Explain why that is bad advice.',
        "options": [
            {"text": 'Contracting both stiffens the elbow instead of driving it in either direction.', "correct": True},
            {"text": 'Contracting both uses too much energy to keep up for the whole match.', "correct": False,
             "why": 'Energy use is a real cost, but the bigger problem is that the two pulls cancel out any actual movement.'},
            {"text": 'The triceps is always weaker than the biceps in an arm-wrestle.', "correct": False,
             "why": "Relative strength is not the issue here — even a strong triceps pulling at the same time cancels the biceps' own pull."},
            {"text": 'It is actually good advice, since two muscles pull harder than one.', "correct": False,
             "why": 'Pulling in opposite directions does not add up to a bigger useful force — it locks the joint instead.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s30',
        "band": 'standard',
        "text": 'A tendon transfer restores a lost movement by using a spare, working muscle to replace a damaged one. What must the surgeon check before choosing which spare muscle to use?',
        "options": [
            {"text": 'That the spare muscle must be exactly the same size as the muscle it replaces.', "correct": False,
             "why": 'Size is not what decides the outcome — what matters is which direction the reattached pull will move the joint in.'},
            {"text": "That the spare muscle's pull will act in the right direction once reattached.", "correct": True},
            {"text": 'That the spare muscle has never been used before the operation.', "correct": False,
             "why": 'A muscle already doing useful work can still be reassigned, as long as its own job is not lost entirely.'},
            {"text": 'That the spare muscle shares a tendon with the damaged one.', "correct": False,
             "why": 'Sharing a tendon is not required — a new tendon attachment is what a transfer creates.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s31',
        "band": 'standard',
        "text": 'A rib injury damages both the set of muscles that lift the ribcage and the diaphragm at the same time. Predict the effect on breathing.',
        "options": [
            {"text": 'Breathing is unaffected, since the two work independently of each other.', "correct": False,
             "why": 'Both genuinely drive breathing in, so losing both removes the movement almost entirely, not merely one route to it.'},
            {"text": "Only breathing out is affected, since that is a muscle's true job.", "correct": False,
             "why": 'Both damaged muscles drive breathing in. Quiet breathing out relies mainly on elastic recoil, unaffected here.'},
            {"text": 'Breathing in becomes seriously difficult, since both of its drivers are lost.', "correct": True},
            {"text": 'Breathing speeds up to make up for the lost muscles.', "correct": False,
             "why": 'Losing the muscles that drive a breath in does not supply a faster way of doing the same job.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-s32',
        "band": 'standard',
        "text": 'A student says that because a relaxed muscle does nothing, only the contracting half of a pair is ever working. Correct that idea using the biceps and triceps.',
        "options": [
            {"text": 'The student is right — a relaxed muscle really does nothing at all.', "correct": False,
             "why": 'A relaxed muscle is being controlled to let go at the right moment, which is not the same as doing nothing.'},
            {"text": "Both muscles always contract together, so the student's idea does not apply.", "correct": False,
             "why": 'In an ordinary movement one contracts while the other relaxes — they do not both contract together.'},
            {"text": 'The relaxed muscle is actually still slightly contracting throughout.', "correct": False,
             "why": 'Relaxing means letting go completely, not staying slightly contracted.'},
            {"text": 'The relaxed one is letting go under load, which is an active choice, not nothing.', "correct": True},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": 'b2-03-h14',
        "band": 'harder',
        "text": "A sprinter's stride length is limited less by the iliopsoas swinging the leg forward than by how fast the gluteus maximus and hamstrings can decelerate it again. Explain why deceleration, not the forward swing, sets the limit.",
        "options": [
            {"text": 'The iliopsoas is too weak to be the limit.', "correct": False,
             "why": 'Weakness is not what is being tested here. The argument is about timing: the swing has to be stopped before landing.'},
            {"text": 'Deceleration needs no muscle, so no limit.', "correct": False,
             "why": 'Slowing a fast-swinging leg does need active muscle work, which is exactly why it can be the limiting factor.'},
            {"text": 'The leg must be slowed before it lands.', "correct": True},
            {"text": 'The two actions happen at different joints.', "correct": False,
             "why": 'Both act on the same hip and knee. What differs is which half of the pair is working at each stage.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h15',
        "band": 'harder',
        "text": "A tendon transfer moves a healthy wrist extensor's attachment to act as a flexor instead, to replace a paralysed flexor. Explain why the patient's grip strength may still end up weaker than before the injury.",
        "options": [
            {"text": 'A transferred tendon always heals much weaker.', "correct": False,
             "why": 'Healing strength of the tendon itself is not the reason — the muscle now has one job doing the work of two.'},
            {"text": 'The wrist loses a whole direction it once had.', "correct": False,
             "why": 'The wrist keeps the same directions; what changes is which muscle drives each one, and one muscle is doing more than before.'},
            {"text": 'Nerves cannot reach a moved tendon.', "correct": False,
             "why": 'The nerve supply to the muscle itself is untouched by moving where its tendon attaches.'},
            {"text": 'One muscle now does two jobs instead of one.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h16',
        "band": 'harder',
        "text": 'A student argues that because quiet breathing out needs no muscle, breathing must be the one movement in the body that breaks the antagonistic-pair rule. Evaluate that.',
        "options": [
            {"text": 'No — a muscle drives the in breath; the return alone is passive.', "correct": True},
            {"text": 'Right — quiet breathing needs no muscle at either stage.', "correct": False,
             "why": 'A muscle is genuinely needed to breathe in. Only the return at rest is done without one.'},
            {"text": 'Right — forced breathing follows the exact same rule-free pattern throughout.', "correct": False,
             "why": 'Forced breathing out does use active muscles, restoring a genuine antagonistic pair for that situation.'},
            {"text": 'Wrong — no muscle is needed at either stage of a quiet breath.', "correct": False,
             "why": 'A quiet breath in is driven by a muscle contracting. It is only the breath out at rest that needs none.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h17',
        "band": 'harder',
        "text": 'During exercise, forced breathing out uses muscles that are silent at rest. Explain why the body does not simply use those muscles for every breath, even at rest.',
        "options": [
            {"text": 'Those muscles are simply far too weak to work at rest.', "correct": False,
             "why": 'The same muscles work hard during exercise. Weakness at rest is not the reason they stay silent.'},
            {"text": 'Contracting costs energy that recoil supplies free.', "correct": True},
            {"text": 'Using them at rest would fully block the next breath in.', "correct": False,
             "why": 'Breathing in and out are separate stages driven by different muscles; using one does not block the other.'},
            {"text": 'The lungs are not stretched enough at rest.', "correct": False,
             "why": 'The lungs are stretched by every breath in, at rest or during exercise. What differs is whether recoil alone is enough to empty them.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h18',
        "band": 'harder',
        "text": 'A jaw injury damages only the opening muscle, leaving the closing muscle undamaged. A student predicts the mouth will simply hang open, since nothing pulls it shut. Evaluate that.',
        "options": [
            {"text": 'Right — nothing drives the jaw either way now.', "correct": False,
             "why": 'The closing muscle is undamaged and still drives that direction. Only opening is genuinely lost.'},
            {"text": 'Right — gravity can no longer act on the jaw.', "correct": False,
             "why": "Gravity's pull on the jaw does not depend on which muscle is damaged. The closing muscle simply still works."},
            {"text": 'Wrong — the closing muscle still works fine.', "correct": True},
            {"text": 'Wrong — both muscles always fail together.', "correct": False,
             "why": 'The two muscles are separate structures. Damaging one does not automatically damage the other.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h19',
        "band": 'harder',
        "text": "A patient's abdominal muscles are paralysed but the erector spinae is unaffected. Explain what happens to their posture, and why sitting up from lying down becomes far harder.",
        "options": [
            {"text": 'The back flattens, with nothing at all left to shape it.', "correct": False,
             "why": 'With the abdominals gone, the undamaged erector spinae pulls with less to resist it, arching the back rather than flattening it.'},
            {"text": 'Posture is fine; sitting up simply fails some other way.', "correct": False,
             "why": 'Losing the muscles on one side of a pair changes the resting balance, so posture is affected as well as the movement itself.'},
            {"text": 'The erector spinae takes over curling forward.', "correct": False,
             "why": 'A muscle can only pull towards itself in its own direction — the erector spinae cannot curl the trunk forward.'},
            {"text": 'The back arches more, and curling forward is lost.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h20',
        "band": 'harder',
        "text": "A student says the eyelid's opening and closing muscles must be roughly equal in strength, since blinking looks smooth and even. Evaluate that claim against the elbow's biceps and triceps.",
        "options": [
            {"text": "No — the elbow's pair is unequal, yet just as controlled.", "correct": True},
            {"text": 'Yes — smooth movement needs equal forces both ways.', "correct": False,
             "why": 'The elbow moves smoothly with very unequal muscles, which shows smoothness does not require equal strength.'},
            {"text": 'Yes, but only because the eyelid is so much smaller.', "correct": False,
             "why": 'Joint size is not what links strength to smoothness. The same principle about control applies at any size.'},
            {"text": 'It cannot be judged without measuring the muscles.', "correct": False,
             "why": 'The elbow already provides a fair test of the underlying claim, which the comparison shows to be false.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h21',
        "band": 'harder',
        "text": "A robotics team copies a bird's wing with a single strong motor for the downstroke and a weak spring for the upstroke, reasoning that gravity helps the spring. Explain the flaw, using how a real bird's wing works.",
        "options": [
            {"text": "No flaw at all — a spring copies the wing muscle exactly.", "correct": False,
             "why": "A bird's upstroke is driven by a genuine muscle that can pull hard and fast, not a passive spring."},
            {"text": 'A real muscle is needed, since gravity cannot lift a wing.', "correct": True},
            {"text": 'The flaw is only that the motor is too strong.', "correct": False,
             "why": "Motor strength for the downstroke is not the issue raised here — the upstroke's power source is."},
            {"text": 'Real birds need no upstroke muscle at all.', "correct": False,
             "why": 'A bird genuinely needs to lift its wing back up against resistance, which does need an active pull.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h22',
        "band": 'harder',
        "text": 'A cat can hold its claws fully retracted for hours with almost no effort, but can only hold them fully extended for a short burst. Explain the difference using which muscle is contracting in each state.',
        "options": [
            {"text": 'Holding the claws drawn in takes constant muscle effort.', "correct": False,
             "why": 'Drawn in is close to a resting state for the muscles — it is holding the claws OUT that demands ongoing contraction.'},
            {"text": 'Both states cost the same amount of muscle effort.', "correct": False,
             "why": 'One state is close to relaxed and the other requires sustained contraction, so the effort is genuinely different.'},
            {"text": 'Drawn in rests both; out keeps one of them working.', "correct": True},
            {"text": 'Extended claws lock in place, needing no effort.', "correct": False,
             "why": 'Nothing in the claw mechanism locks it out. Ongoing muscle contraction is what holds it extended.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h23',
        "band": 'harder',
        "text": 'A hamstring tears while it is pulling hard and being stretched longer at the same time, slowing a sprinting leg. A researcher rebuilding one in the laboratory loads it in that same way — pulling while being lengthened — rather than only in shortening pulls. Suggest why.',
        "options": [
            {"text": 'Pulling while being lengthened is simply the gentler of the two.', "correct": False,
             "why": 'Pulling against a stretch is demanding, not gentle. What makes it the right choice is that it matches the loading that caused the tear.'},
            {"text": 'A shortening pull cannot be loaded in a laboratory at all.', "correct": False,
             "why": 'A shortening pull can be loaded perfectly well. The choice here is about matching the loading that caused the tear.'},
            {"text": 'Pulling while being lengthened loads the quadriceps instead.', "correct": False,
             "why": 'It loads the hamstring itself, in the exact way it is loaded while slowing a sprinting leg.'},
            {"text": 'It matches the exact way the injury first happened.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h24',
        "band": 'harder',
        "text": 'A tendon transfer restores wrist bending by rerouting a spare forearm muscle, but the surgeon warns the patient will need weeks of retraining before the new movement feels natural. Explain why retraining is needed even though the mechanics are fixed the moment the tendon is reattached.',
        "options": [
            {"text": 'The nervous system must learn to fire it differently.', "correct": True},
            {"text": 'The tendon itself takes several weeks to grow strong enough.', "correct": False,
             "why": 'A healed tendon can transmit force from the moment surgery is complete — what takes time is learning to use it for the new job.'},
            {"text": 'The muscle must grow new fibres to do the new job.', "correct": False,
             "why": "The muscle's fibres are unchanged by the surgery. What changes is where its pull lands, not what it is made of."},
            {"text": 'The bone needs time to remodel round the new site.', "correct": False,
             "why": 'Bone remodelling is not the limiting step here — learning the new muscle-to-movement pattern is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h25',
        "band": 'harder',
        "text": 'A student claims that because both muscles of a pair always use energy while one contracts and the other relaxes, co-contraction (both contracting together) must always be wasteful. Evaluate that.',
        "options": [
            {"text": 'Right — co-contraction serves no purpose at all.', "correct": False,
             "why": 'Co-contraction is exactly how a joint is deliberately braced before a knock, such as in a rugby tackle.'},
            {"text": 'Not always — it braces a joint against a shock.', "correct": True},
            {"text": 'It is wasteful only at the elbow, not elsewhere.', "correct": False,
             "why": 'The bracing purpose of co-contraction applies at any joint, not specifically the elbow.'},
            {"text": 'It actually uses less energy than one contracting.', "correct": False,
             "why": 'Co-contraction uses energy in both muscles at once, which is genuinely more, not less — the point is that the extra cost buys real stability.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h26',
        "band": 'harder',
        "text": 'During hard exercise a second set of rib muscles contracts to drive the breath out, though at rest that set stays silent. Suggest what it adds that the chest\'s own spring-back cannot.',
        "options": [
            {"text": 'It makes the breath in bigger as well.', "correct": False,
             "why": 'That set pulls the ribcage down, which empties the chest. Lifting the ribcage for a breath in is the other set\'s job.'},
            {"text": 'The chest has no spring-back of its own at all.', "correct": False,
             "why": 'The ribcage and lungs do spring back, which is exactly what empties them at rest without any muscle.'},
            {"text": 'Spring-back alone is not fast or full enough for hard exercise.', "correct": True},
            {"text": 'Nothing — spring-back already empties the chest as fast as it can be emptied.', "correct": False,
             "why": 'Spring-back happens at its own rate. Pulling the ribcage down actively empties the chest faster and further than recoil alone can.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h27',
        "band": 'harder',
        "text": "A cat's claws and a human's fingers are both worked by one tendon that moves them and a second that brings them back, yet a cat's claws stay drawn in most of the time while a human's fingers rest part-curled rather than fully open or closed. Suggest why the two rest differently.",
        "options": [
            {"text": "A cat's claws are moved by only one tendon, with nothing opposing it.", "correct": False,
             "why": 'Tendons pull the claw both ways. One pull alone could never return it.'},
            {"text": 'Human fingers curl less because the tendons that curl them are weak.', "correct": False,
             "why": 'Weakness is not the reason — a resting position reflects the balance between the two pulls, not either one failing.'},
            {"text": "They would rest exactly alike with matching tendon length.", "correct": False,
             "why": 'Tendon length is one detail among several that decide a resting balance; it is not established as the deciding factor here.'},
            {"text": 'Each pair simply settles at its own resting balance.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h28',
        "band": 'harder',
        "text": 'A weightlifter can hold a loaded bar dead still above their head for several seconds. Explain, using the shoulder\'s muscles, why this is not a case of "nothing happening."',
        "options": [
            {"text": "Muscles are contracting hard the whole time, unseen.", "correct": True},
            {"text": "The bones alone hold the bar, with muscles resting.", "correct": False,
             "why": 'Bone alone cannot hold a moving joint steady against a load — a muscle has to be actively pulling.'},
            {"text": 'Nothing is truly happening without any visible movement.', "correct": False,
             "why": 'A great deal is happening: muscles are working hard and using energy, even without visible movement.'},
            {"text": 'The bar is motionless since gravity has switched off.', "correct": False,
             "why": "Gravity acts on the bar at every height. It is matched, not switched off, by the lifter's muscles."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h29',
        "band": 'harder',
        "text": 'A student says every antagonistic pair in the body must be roughly matched in strength, or the joint would be pulled permanently out of shape over a lifetime. Use the biceps and triceps, which are not equally strong, to evaluate that.',
        "options": [
            {"text": 'Right — the two muscles are secretly matched.', "correct": False,
             "why": 'The two muscles are not equal in strength, yet the elbow does not drift permanently, which is the point against the claim.'},
            {"text": "Wrong — a healthy elbow never drifts either way.", "correct": True},
            {"text": 'Right, and this is why elbows end up permanently fixed in a bent position.', "correct": False,
             "why": 'An elbow whose biceps pulls harder may rest a little bent, but it still straightens fully. Resting bent is not the same as being fixed that way.'},
            {"text": 'It needs the exact strength of each in newtons.', "correct": False,
             "why": 'The everyday observation that healthy elbows do not drift is already enough to test the claim.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h30',
        "band": 'harder',
        "text": "Design a simple test, using only what you know about antagonistic pairs and no equipment, to check whether a patient's triceps is working at all after an injury.",
        "options": [
            {"text": 'Bend the elbow fully, since that uses both muscles.', "correct": False,
             "why": "Bending is the biceps' own job. It says nothing directly about whether the triceps is working."},
            {"text": 'Feel if the elbow is truly warm, since work makes heat.', "correct": False,
             "why": 'Temperature is not a reliable, immediate test of whether a specific muscle can contract.'},
            {"text": 'Straighten a bent elbow against light resistance.', "correct": True},
            {"text": 'Relax the arm completely and see if it falls straight down.', "correct": False,
             "why": 'A hanging arm straightens under gravity whether or not the triceps works at all, so this proves nothing about it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h31',
        "band": 'harder',
        "text": 'A prosthetic hand uses one motor to close the fingers and a spring to open them again, and a student argues this makes it "not really an antagonistic pair" since a spring is not living tissue. Evaluate that.',
        "options": [
            {"text": 'Right — only two real muscles form a true pair.', "correct": False,
             "why": 'The underlying principle is two forces pulling opposite ways at a joint — the material producing either pull is a separate question.'},
            {"text": 'Right — a spring can only push, never pull.', "correct": False,
             "why": 'A stretched spring does pull as it recoils, which is exactly the return pull a partner muscle would supply.'},
            {"text": 'Neither part compares with a muscle at all.', "correct": False,
             "why": 'Both play the same functional roles a real antagonistic pair plays — one active pull, one opposing pull — which is the comparison that matters here.'},
            {"text": 'It is still two opposite pulls, whoever supplies them.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-03-h32',
        "band": 'harder',
        "text": 'Compare the biceps-triceps pair with the intercostal muscle pair. Both are antagonistic pairs, yet one works roughly twelve times a minute without conscious thought and the other only when a person decides to move. Explain what the two genuinely share despite that difference.',
        "options": [
            {"text": 'Both work the same way: one pulls while its partner lets go.', "correct": True},
            {"text": 'Nothing at all — the two pairs work on totally different rules entirely.', "correct": False,
             "why": 'Both are built on exactly the same mechanical principle: one muscle pulling while its partner lets go, whatever triggers it.'},
            {"text": 'They share only being equally strong.', "correct": False,
             "why": 'Strength is not what is shared here, and the two pairs are not claimed to be equally strong.'},
            {"text": 'They share only sitting in the upper body.', "correct": False,
             "why": 'The biceps and triceps are in the arm, not specifically shared in location with the intercostal muscles between the ribs.'},
        ],
        "figure": None,
    },
]
