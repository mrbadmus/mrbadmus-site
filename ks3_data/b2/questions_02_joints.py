"""B2 lesson 02 — Joints: twelve questions (MRB-269).

These probe the one claim the lesson is built on — the shape of the bone ends
decides what a joint can do, and every direction it allows is a direction it
cannot resist. The distractors are built from the lesson's three declared
misconceptions: BODY-04 (muscles hold the bones together at a joint), which
runs through the ligament, cartilage and physiotherapy questions; BODY-05 (all
joints work the same way, some are just stiffer), which the fixed-versus-hinge
question attacks head on; and BODY-06 (a joint would rotate further if the
muscles were stronger or the ligaments looser), taken to a knee rather than the
elbow the ladder already uses. The other recurring error is the tendon /
ligament / cartilage three-way swap, which the lesson says has consequences
students do not expect. The `harder` band takes the model somewhere the lesson
never goes (turning a screwdriver, a dancer stretching for a turn she can never
have, a physiotherapist's advice) and turns the closing line back on the
student: the thumb's misfit is information, not a fault in the model.
"""

UNIT = "B2"
LESSON = "joints"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-02-e01",
        "band": "easier",
        "text": "You can feel a thick strap at the side of your knee tighten "
                "when you straighten your leg. What is a ligament's job?",
        "options": [
            {"text": "It joins a muscle to a bone, so that the muscle's pull "
                     "can move that bone.",
             "correct": False,
             "why": "That is a tendon — the Achilles at the back of your "
                    "ankle is the biggest one you have. A ligament runs from "
                    "bone to bone."},
            {"text": "It is the smooth facing on the end of each bone that "
                     "keeps the two from grinding.",
             "correct": False,
             "why": "That is cartilage. It stops the ends wearing on each "
                    "other; it does not strap anything together."},
            {"text": "It joins bone to bone, holding the joint together and "
                     "stopping it moving in directions it should not.",
             "correct": True},
            {"text": "It is the muscle wrapped round the joint, and the "
                     "muscle is what holds the two bones in place.",
             "correct": False,
             "why": "Muscles move bones; they do not hold the joint together. "
                    "Ligaments do that, which is why a joint with torn "
                    "ligaments stays loose however strong the muscles are."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e02",
        "band": "easier",
        "text": "Two bone ends meet inside your knee and move against each "
                "other thousands of times a day. What stops them wearing each "
                "other away?",
        "options": [
            {"text": "A layer of smooth cartilage faces each end, so the two "
                     "slide instead of grinding.",
             "correct": True},
            {"text": "The ligaments hold the two ends slightly apart, so that "
                     "they never actually touch.",
             "correct": False,
             "why": "Ligaments strap the bones together, not apart. What "
                    "keeps the ends from grinding is the smooth cartilage "
                    "facing them."},
            {"text": "The muscles take the weight, so nothing ever presses "
                     "the two bone ends together.",
             "correct": False,
             "why": "The joint is loaded every time you stand on it. The load "
                    "is real, and cartilage is what it is carried on."},
            {"text": "The bone ends are shaped so that they only ever touch "
                     "each other at the very edges.",
             "correct": False,
             "why": "The shape of the ends decides which directions the joint "
                    "moves in, not whether they touch. They meet across a "
                    "broad face, and that face is cartilage."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e03",
        "band": "easier",
        "text": "On the bench you drag the hinge joint as far as it will go, "
                "then press \"Try to twist it\". What does the model do?",
        "options": [
            {"text": "It bends as far as it goes, then turns a little way "
                     "about its long axis.",
             "correct": False,
             "why": "It turns not at all. The twist button is there so you "
                    "can watch the refusal, and the refusal is the point."},
            {"text": "It bends to 180 degrees, the same range as the "
                     "ball-and-socket joint has.",
             "correct": False,
             "why": "The hinge stops at 145 degrees. A 180-degree swing "
                    "belongs to the ball and socket, which is a different "
                    "shape entirely."},
            {"text": "It refuses to bend past 90 degrees, because a groove "
                     "only ever allows a right angle.",
             "correct": False,
             "why": "The hinge runs from 0 to 145 degrees. Look at your own "
                    "elbow — it folds well past a right angle."},
            {"text": "It bends to 145 degrees and then will not turn at all, "
                     "because one bone end sits in a groove.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e04",
        "band": "easier",
        "text": "You shake your head to mean \"no\". Which joint is doing "
                "that, and what kind of joint is it?",
        "options": [
            {"text": "The joint at the top of the neck, and it is a hinge, "
                     "because the neck bends.",
             "correct": False,
             "why": "A hinge bends and straightens along one line and cannot "
                    "turn at all. Shaking your head is a turn, not a bend."},
            {"text": "The joint at the top of the neck, and it is a pivot — "
                     "one bone turning inside a ring of ligament.",
             "correct": True},
            {"text": "The joint at the top of the neck, and it is a ball and "
                     "socket, since the head moves several ways.",
             "correct": False,
             "why": "Ball-and-socket joints are your shoulder and hip. The "
                    "head-shake is a single turn about one axis, and a turn "
                    "about one axis is what a pivot does."},
            {"text": "The seams across the skull, which loosen a little to "
                     "let the whole head swing round.",
             "correct": False,
             "why": "Skull seams are fixed joints. The bones interlock along "
                    "a jagged line and allow no movement at all."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-02-s01",
        "band": "standard",
        "text": "A footballer is tackled with his studs planted, and his knee "
                "is twisted hard. Why is a twist so much worse for a knee "
                "than a heavy bend?",
        "options": [
            {"text": "The knee is a hinge, so a twist is the one direction it "
                     "has no give in and the ligaments take all of it.",
             "correct": True},
            {"text": "Twisting stretches the cartilage, and the cartilage is "
                     "what holds the joint together.",
             "correct": False,
             "why": "Cartilage is the smooth facing that stops the ends "
                    "grinding; ligaments hold the joint. The knee is a hinge, "
                    "so the twist is the direction it cannot give way to."},
            {"text": "The muscles round the knee are weaker sideways than "
                     "they are front to back.",
             "correct": False,
             "why": "Muscle strength is not the limit here. The shape is: a "
                    "groove permits one direction, and a twist is not it."},
            {"text": "A bend puts far more force through the joint than a "
                     "twist does, so the bend is the safer of the two.",
             "correct": False,
             "why": "It is not about how much force. The knee bends by "
                    "design and gives way safely; it has no design for "
                    "turning, so a twist goes straight into the ligaments."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s02",
        "band": "standard",
        "text": "Your hip and your shoulder are the same kind of joint, yet "
                "shoulders dislocate far more often than hips do. What is "
                "different about the hip?",
        "options": [
            {"text": "The hip is strapped by ligaments and the shoulder is "
                     "held only by the muscle around it.",
             "correct": False,
             "why": "Both are strapped by ligaments, and the shoulder also "
                    "has a deep cuff of muscle. What differs is how deep the "
                    "socket is."},
            {"text": "The hip is not really a ball and socket at all; it is a "
                     "stiff hinge that happens to swing.",
             "correct": False,
             "why": "The hip swings your leg forwards, backwards and out to "
                    "the side, and turns your foot outwards. That is three "
                    "directions. A hinge has one."},
            {"text": "The hip's ligaments are trained by every step you take, "
                     "so they tighten over the years.",
             "correct": False,
             "why": "Ligaments do not tighten with use, and looseness is not "
                    "the story. The hip's socket is simply the deeper of the "
                    "two."},
            {"text": "Its socket is deeper. Less range comes out of it, and "
                     "far fewer dislocations go with that.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s03",
        "band": "standard",
        "text": "Two players are hurt in the same match. One tears a tendon "
                "behind the ankle; the other tears a ligament at the side of "
                "it. Which describes the torn tendon?",
        "options": [
            {"text": "The ankle now moves too far sideways, in a direction it "
                     "was never meant to move in.",
             "correct": False,
             "why": "That is the torn ligament. A ligament is the strap that "
                    "refuses a direction, so tearing one lets the joint go "
                    "where it should not."},
            {"text": "The muscle can no longer pull on that bone, so the "
                     "movement it drove is lost.",
             "correct": True},
            {"text": "The two bones of the ankle come apart, because nothing "
                     "is joining them to each other any more.",
             "correct": False,
             "why": "A tendon joins muscle to bone, not bone to bone. "
                    "Ligaments are what hold the two bones together."},
            {"text": "The bone ends begin to grind, because the smooth facing "
                     "between them has been torn away.",
             "correct": False,
             "why": "That is damaged cartilage, which is a third thing again. "
                    "A tendon is the cord carrying a muscle's pull to a "
                    "bone."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s04",
        "band": "standard",
        "text": "\"A fixed joint is just a hinge that has gone very stiff.\" "
                "What is wrong with that statement?",
        "options": [
            {"text": "Nothing is wrong — a fixed joint is a hinge whose "
                     "ligaments have tightened up completely.",
             "correct": False,
             "why": "Joints are not one design at different settings. They "
                    "are different shapes, and the shape is what decides what "
                    "each one can do."},
            {"text": "Fixed joints are stiffer than that — they are the "
                     "stiffest joints anywhere in the body.",
             "correct": False,
             "why": "It is not a matter of degree at all. A fixed joint has "
                    "no range to be stiff in: the bones interlock and are "
                    "effectively one bone."},
            {"text": "Different shapes, not settings: a groove allows one "
                     "direction, an interlocking seam none.",
             "correct": True},
            {"text": "A fixed joint does bend, but only in a baby, so "
                     "\"stiff\" is the right word for an adult one.",
             "correct": False,
             "why": "Skull seams move while the skull is still growing, then "
                    "lock. After that there is no movement at all — that is a "
                    "shape, not a stiffness."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-02-h01",
        "band": "harder",
        "text": "You turn a screwdriver by rolling your palm from facing up "
                "to facing down, keeping your elbow tucked in and still. "
                "Which joint has done the turning?",
        "options": [
            {"text": "The elbow, which turns a little way as well as bending "
                     "and straightening.",
             "correct": False,
             "why": "The elbow is a hinge. It bends and straightens along one "
                    "line and does not turn at all — which is why you could "
                    "keep it still and still turn the screwdriver."},
            {"text": "A pivot joint between the two forearm bones, one turning "
                     "inside a ring of ligament.",
             "correct": True},
            {"text": "The shoulder, since it is the only joint in the whole "
                     "arm that is able to rotate.",
             "correct": False,
             "why": "The shoulder can rotate, but you held it and the elbow "
                    "still. The forearm has a pivot of its own, between its "
                    "two bones."},
            {"text": "The wrist, which is loose enough to let the whole hand "
                     "spin round on the end of the arm.",
             "correct": False,
             "why": "Your hand turned because your forearm turned. Roll your "
                    "palm over and watch the two forearm bones cross — that "
                    "is where it happens."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h02",
        "band": "harder",
        "text": "A dancer wants to turn her lower leg the way she can turn "
                "her forearm, and plans to stretch her knee ligaments until "
                "it does. Predict what she will get.",
        "options": [
            {"text": "Some turn at the knee, with a slightly less stable knee "
                     "as the price she pays for it.",
             "correct": False,
             "why": "There is no turn there to gain. Looser ligaments do not "
                    "add a direction — they only remove a refusal."},
            {"text": "No change whatever, because ligaments cannot be "
                     "stretched by any amount of training.",
             "correct": False,
             "why": "Ligaments can be stretched, and that is exactly the "
                    "danger. What they cannot do is give a joint a direction "
                    "its bone ends do not have."},
            {"text": "Some turn, once the muscles round the knee have grown "
                     "strong enough to drive the leg round.",
             "correct": False,
             "why": "Muscles drive a joint through the directions it already "
                    "has. No amount of strength will make a groove turn."},
            {"text": "No new direction, and a knee that resists the old ones "
                     "less well — the bone ends are what decide.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h03",
        "band": "harder",
        "text": "The joint at the base of your thumb turns out to be none of "
                "the four types. A student says that shows the four-type "
                "model is not worth much. What is the better answer?",
        "options": [
            {"text": "The model sorts most of the skeleton, and the joints it "
                     "fails on are the ones worth studying.",
             "correct": True},
            {"text": "The thumb joint is really a ball and socket, so the "
                     "four types do cover it after all.",
             "correct": False,
             "why": "A ball and socket moves in three directions. The thumb's "
                    "saddle shape gives it two, which is precisely why it "
                    "does not fit."},
            {"text": "The four types were only ever meant for the leg, so the "
                     "thumb was never inside the model's scope.",
             "correct": False,
             "why": "The four types sort joints all over the body — the neck, "
                    "the skull, the shoulder, the hip. The thumb is a genuine "
                    "misfit, not an exclusion."},
            {"text": "A model has to fit every case, so a fifth type should be "
                     "added and the thumb dropped into it.",
             "correct": False,
             "why": "A model stretched to fit everything has stopped telling "
                    "you anything. The misfits are information, not a hole to "
                    "be patched over."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h04",
        "band": "harder",
        "text": "A physiotherapist tells someone with a sore knee to keep "
                "using it gently rather than resting it completely. Which "
                "reason fits what you know about cartilage?",
        "options": [
            {"text": "Moving the joint pumps fresh blood through the "
                     "cartilage, and blood is what repairs it.",
             "correct": False,
             "why": "Cartilage has no blood supply of its own — that is the "
                    "whole problem with it. What reaches it is fluid squeezed "
                    "through as the joint is loaded."},
            {"text": "Moving the joint stretches the ligaments, so it regains "
                     "a direction it had lost.",
             "correct": False,
             "why": "Stretched ligaments add no direction; they leave the "
                    "joint less able to resist. This is about feeding the "
                    "cartilage, not about range."},
            {"text": "Cartilage is fed by fluid squeezed through it each time "
                     "the joint is loaded and unloaded.",
             "correct": True},
            {"text": "Moving the joint builds the muscles round it, and the "
                     "muscles are what hold the two bones together.",
             "correct": False,
             "why": "Ligaments hold the bones together, not muscles. And the "
                    "reason for moving here is the cartilage, which has no "
                    "other way of being fed."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-02-e05",
        "band": "easier",
        "text": "What makes a place in the body a joint?",
        "options": [
            {"text": "Two bones meeting at a place where the skeleton can "
                     "bend.",
             "correct": False,
             "why": "Bending is not the test. The seams of an adult skull are "
                    "joints, and nothing there moves at all."},
            {"text": "Two or more bones meeting, whether or not anything "
                     "moves there.",
             "correct": True},
            {"text": "A muscle joining onto a bone, so that its pull can move "
                     "that bone.",
             "correct": False,
             "why": "That is where a tendon attaches. A joint is a meeting of "
                    "bones, and the muscle crosses it from outside."},
            {"text": "A gap between two bones, held open by fluid so that "
                     "they never touch.",
             "correct": False,
             "why": "The two ends do meet, across a broad face. What keeps "
                    "them from grinding is the smooth cartilage on that face, "
                    "not a gap."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e06",
        "band": "easier",
        "text": "Where in the body would you find a fixed joint?",
        "options": [
            {"text": "At the elbow, where the arm bends along one line.",
             "correct": False,
             "why": "The elbow is a hinge. It folds to about 145 degrees, "
                    "which is a great deal more than a fixed joint allows."},
            {"text": "At the top of the neck, where the head turns from side "
                     "to side on a peg of bone.",
             "correct": False,
             "why": "That turn happens at a pivot. A fixed joint would not "
                    "let the head turn at all."},
            {"text": "At the base of the thumb, which swings across the palm "
                     "to the fingers.",
             "correct": False,
             "why": "The thumb's joint moves in two directions, which is why "
                    "it fits none of the four types. A fixed joint moves in "
                    "none."},
            {"text": "Between the plates of an adult skull, along a jagged "
                     "seam.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e07",
        "band": "easier",
        "text": "A ball-and-socket joint moves in three directions. Which pair "
                "below are both ball and socket?",
        "options": [
            {"text": "The shoulder and the hip.",
             "correct": True},
            {"text": "The elbow and the knee.",
             "correct": False,
             "why": "Both are hinges. They bend and straighten along one line "
                    "and refuse every other direction."},
            {"text": "The top of the neck and the joint between the two "
                     "forearm bones.",
             "correct": False,
             "why": "Those are the two pivots. They turn about one axis and "
                    "cannot swing in three directions."},
            {"text": "The wrist and the seams across the skull.",
             "correct": False,
             "why": "Skull seams are fixed joints and allow no movement at all, "
                    "so the pair cannot be right. The two ball-and-socket "
                    "joints are the shoulder and the hip."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e08",
        "band": "easier",
        "text": "What is a dislocation?",
        "options": [
            {"text": "A bone broken close to a joint.",
             "correct": False,
             "why": "A break is a break in the bone itself. In a dislocation "
                    "the bone is whole and has come out of place."},
            {"text": "A ligament torn so that the joint moves further than it "
                     "should when it is loaded.",
             "correct": False,
             "why": "That is a sprain, and it makes a dislocation more "
                    "likely. A dislocation is the bone ends themselves no "
                    "longer sitting together."},
            {"text": "A joint pushed out of place, so the bone ends come "
                     "apart.",
             "correct": True},
            {"text": "A joint that has become too stiff to move through its "
                     "usual range.",
             "correct": False,
             "why": "A dislocated joint is not stiff — it has come apart. "
                    "Stiffness is the opposite complaint."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e09",
        "band": "easier",
        "text": "Range and stability are bought from each other at every joint. "
                "Complete the rule: every direction a joint can move in is "
                "also...",
        "options": [
            {"text": "...a direction it is strongest in.",
             "correct": False,
             "why": "That is the rule backwards. If a joint moves in a "
                    "direction, nothing is refusing that direction — which is "
                    "where it is weakest."},
            {"text": "...a direction its muscles have been trained for.",
             "correct": False,
             "why": "Training changes nothing about which directions exist. "
                    "The shape of the bone ends decides that."},
            {"text": "...a direction its cartilage has worn smooth.",
             "correct": False,
             "why": "Cartilage stops the ends grinding wherever they meet. It "
                    "does not decide which directions a joint has."},
            {"text": "...a direction it cannot resist.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e10",
        "band": "easier",
        "text": "Your elbow and your knee are the same type of joint. Which "
                "type, and in how many directions does it move?",
        "options": [
            {"text": "A pivot, which turns about one axis.",
             "correct": False,
             "why": "A pivot turns and cannot bend. Your elbow bends and will "
                    "not turn, which is the other way round."},
            {"text": "A hinge, which moves in one direction only.",
             "correct": True},
            {"text": "A ball and socket, which moves in three directions.",
             "correct": False,
             "why": "That is the shoulder and the hip. An elbow refuses every "
                    "direction but one."},
            {"text": "A fixed joint, which moves in none.",
             "correct": False,
             "why": "Fixed joints are the skull seams and the adult pelvis. "
                    "A knee that could not move would be no use for "
                    "walking."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e11",
        "band": "easier",
        "text": "Four types cover most joints: hinge, ball and socket, pivot "
                "and fixed. Which of these joints is none of the four, and why "
                "not?",
        "options": [
            {"text": "The base of the thumb — its saddle shape moves two "
                     "ways, and no type does.",
             "correct": True},
            {"text": "The top of the neck — it turns much further in each "
                     "direction than the four types allow.",
             "correct": False,
             "why": "That turn is exactly what a pivot does, and about 80 "
                    "degrees each way is its ordinary range."},
            {"text": "The shoulder — it moves in more directions than a ball "
                     "and socket has.",
             "correct": False,
             "why": "Three directions is what a ball and socket gives, and the "
                    "shoulder is the clearest example of one there is."},
            {"text": "The knee — it bends and also turns, so it is both a "
                     "hinge and a pivot at once.",
             "correct": False,
             "why": "A knee does not turn. That refusal is exactly why a "
                    "twisting tackle damages one so badly."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e12",
        "band": "easier",
        "text": "Which joint in the body is dislocated most often, and what "
                "makes it that one?",
        "options": [
            {"text": "The knee, because it takes more of the body's weight "
                     "than any other joint.",
             "correct": False,
             "why": "Weight is not what pushes a joint out of place. The knee "
                    "is a hinge, and a hinge refuses almost every "
                    "direction."},
            {"text": "The hip, because it swings the leg in several "
                     "directions.",
             "correct": False,
             "why": "It does swing in several, but its socket is deep. "
                    "Deeper socket, less range, far fewer dislocations."},
            {"text": "The shoulder, because it refuses the fewest directions.",
             "correct": True},
            {"text": "The elbow, because it is used more often than any other "
                     "joint.",
             "correct": False,
             "why": "How often a joint is used does not decide it. The elbow "
                    "is one of the least dislocated joints there is, because "
                    "a groove allows one direction and no others."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-e13",
        "band": "easier",
        "text": "Which of these is true of the cartilage inside a joint?",
        "options": [
            {"text": "It joins one bone to another and holds the joint "
                     "together.",
             "correct": False,
             "why": "That is a ligament. Cartilage is the smooth facing on "
                    "the ends of the bones and straps nothing."},
            {"text": "It carries a muscle's pull across the joint to the bone "
                     "being moved.",
             "correct": False,
             "why": "That is a tendon. Cartilage does not attach to a muscle "
                    "at all."},
            {"text": "It heals faster than bone does, because it is softer.",
             "correct": False,
             "why": "It heals slowly and often not at all. Softness is not "
                    "what decides healing — a blood supply is, and cartilage "
                    "has none."},
            {"text": "No blood supply — it is fed by fluid squeezed through "
                     "it.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-02-s05",
        "band": "standard",
        "text": "Why does a fixed joint suit the plates of the skull, and why "
                "would one be no use at the knee?",
        "options": [
            {"text": "A box protecting a brain is worth more with no moving "
                     "parts, while a knee has to bend for you to walk.",
             "correct": True},
            {"text": "The skull's bones are much thinner than a knee's, and a "
                     "thin bone cannot carry a joint that moves.",
             "correct": False,
             "why": "Thickness does not decide a joint's type. The shape of "
                    "the meeting between the two bones does."},
            {"text": "The skull is never loaded the way a knee is, so it does "
                     "not need the strength that movement costs.",
             "correct": False,
             "why": "A skull takes impacts, so it is loaded hard exactly when "
                    "it matters. It is fixed because nothing there needs to "
                    "move."},
            {"text": "A fixed joint is simply the strongest of the four, and "
                     "the brain needs the strongest one there is.",
             "correct": False,
             "why": "There is no ranking of strength across the four. Each "
                    "shape refuses what its job needs refused — and a knee's "
                    "job requires bending."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s06",
        "band": "standard",
        "text": "A surgeon fitting an artificial hip can choose a deeper or a "
                "shallower socket. What does the patient gain, and lose, with "
                "the deeper one?",
        "options": [
            {"text": "They gain range of movement and lose nothing, because a "
                     "deeper socket holds the ball better.",
             "correct": False,
             "why": "Nothing here is free. A deeper socket buys stability, "
                    "and range of movement is what pays for it."},
            {"text": "They gain stability and range together, because the "
                     "ball is held more firmly.",
             "correct": False,
             "why": "Those two are bought from each other. Holding the ball "
                    "more firmly means fewer directions, not more."},
            {"text": "They gain stability against dislocation, and lose some "
                     "of the leg's range of movement.",
             "correct": True},
            {"text": "They lose stability but gain range, because a deep "
                     "socket lets the ball turn further.",
             "correct": False,
             "why": "The wrong way round. Compare a real hip with a shoulder: "
                    "the deeper socket is the one that swings less and "
                    "dislocates less."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s07",
        "band": "standard",
        "text": "Months after a bad ankle sprain the joint moves freely, but "
                "the person says they still cannot trust it. What was "
                "damaged, and why does that description fit?",
        "options": [
            {"text": "The cartilage — the joint grinds, and that is what "
                     "makes it feel unreliable.",
             "correct": False,
             "why": "Worn cartilage grinds and hurts; it does not make a "
                    "joint feel loose. This one moves freely."},
            {"text": "A ligament — it was the strap refusing a direction, so "
                     "the joint now goes where it should not.",
             "correct": True},
            {"text": "A tendon — the muscle can no longer move the joint, so "
                     "it cannot be relied on.",
             "correct": False,
             "why": "A torn tendon leaves a movement missing altogether. This "
                    "ankle moves freely; what is missing is a refusal."},
            {"text": "The bone ends — their shape has changed, so the joint "
                     "has gained a new direction.",
             "correct": False,
             "why": "A sprain stretches and tears the straps around a joint; "
                    "it does not reshape bone. The direction was always "
                    "there, and now nothing refuses it."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s08",
        "band": "standard",
        "text": "You can hang your whole body weight from a bent elbow and it "
                "will not fold sideways. What is doing the refusing?",
        "options": [
            {"text": "The muscles round the elbow, which tighten under load and "
                     "hold the two bones firmly in place.",
             "correct": False,
             "why": "Muscles move bones; they do not hold a joint together. "
                    "The refusal comes from the shape of the ends and the "
                    "ligaments strapping them."},
            {"text": "The cartilage, which is thick enough at the elbow to "
                     "block any sideways movement of the joint.",
             "correct": False,
             "why": "Cartilage is the smooth facing that stops the ends "
                    "grinding. It decides nothing about direction."},
            {"text": "Nothing is refusing it — an elbow does fold sideways, "
                     "only by too little to notice.",
             "correct": False,
             "why": "It does not. One bone end sits in a groove in the other, "
                    "and a groove allows one direction and no others."},
            {"text": "The shape of the ends — one sits in a groove — with "
                     "strong ligaments down both sides.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s09",
        "band": "standard",
        "text": "A student says a joint with more ligaments round it must "
                "move in more directions. Test that against the elbow and the "
                "shoulder.",
        "options": [
            {"text": "It is backwards: ligaments take directions away, and "
                     "the elbow has only one.",
             "correct": True},
            {"text": "It is right: the shoulder has a whole ring of ligaments "
                     "and moves in three directions.",
             "correct": False,
             "why": "The shoulder does have a ring of them and does move "
                    "most, but not because of them. Ligaments are what stop "
                    "it going further; the round ball in a round socket is "
                    "what lets it move."},
            {"text": "It is right for the elbow and wrong for the shoulder, "
                     "because the two are strapped quite differently.",
             "correct": False,
             "why": "The rule fails at both. Ligaments restrict at every "
                    "joint in the body, and the shape of the bone ends "
                    "decides the directions."},
            {"text": "Neither joint has ligaments, so the comparison cannot "
                     "be made at all.",
             "correct": False,
             "why": "Both are strapped by them — down each side at the elbow, "
                    "in a ring at the shoulder. That is what makes the "
                    "comparison worth making."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s10",
        "band": "standard",
        "text": "The seams across a baby's skull can still move; an adult's "
                "cannot. What does that tell you about what those joints are "
                "for?",
        "options": [
            {"text": "They are hinges that stiffen as the child grows, until in "
                     "the end they can no longer bend.",
             "correct": False,
             "why": "They are not hinges at any age. Once locked, the plates "
                    "interlock along a jagged seam and are effectively one "
                    "bone."},
            {"text": "A baby's ligaments are looser, and they tighten across "
                     "the seams as the child grows up.",
             "correct": False,
             "why": "It is not a matter of straps. The plates themselves grow "
                    "together and lock."},
            {"text": "Movement there is worth having only while the skull is "
                     "growing; after that a sealed box is worth more.",
             "correct": True},
            {"text": "The plates fuse together because a fully grown brain no "
                     "longer needs the protection it once did.",
             "correct": False,
             "why": "The opposite is true: fusing is what completes the "
                    "protection. What is no longer needed is the movement."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s11",
        "band": "standard",
        "text": "A pivot joint at the top of the neck turns about 80 degrees "
                "each way and cannot bend. What does the trade between range "
                "and stability predict about it?",
        "options": [
            {"text": "It will be very stable, because a joint that does nothing "
                     "but turn cannot be pushed anywhere.",
             "correct": False,
             "why": "Turning is somewhere. Every direction a joint allows is "
                    "one it cannot refuse, and this one allows a large turn."},
            {"text": "The turn is the direction it cannot resist, so a "
                     "violent twist is what is most likely to injure it.",
             "correct": True},
            {"text": "It will be injured most easily by bending, because "
                     "bending is the one direction it refuses to allow.",
             "correct": False,
             "why": "A refused direction is the one a joint resists best. It "
                    "is the movement a joint allows that leaves it exposed."},
            {"text": "It has no weak direction at all, because a complete ring "
                     "of ligament holds the bone inside it.",
             "correct": False,
             "why": "The ring is what stops it going further, not a promise "
                    "that nothing can. The trade applies to every joint, "
                    "including this one."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s12",
        "band": "standard",
        "text": "Two people injure a knee: one tears a ligament, the other "
                "damages the smooth facing on a bone end. Which injury is "
                "expected to heal more slowly, and why?",
        "options": [
            {"text": "The ligament, because a strap is thicker tissue and "
                     "thicker tissue always takes longer.",
             "correct": False,
             "why": "Thickness is not what decides healing. What decides it "
                    "is whether a blood supply is delivering the material to "
                    "repair with."},
            {"text": "The ligament, because it is loaded again every time the "
                     "person stands up.",
             "correct": False,
             "why": "Loading is not the problem — the facing is loaded just "
                    "as often, and being loaded is how cartilage is fed. The "
                    "difference is the blood supply."},
            {"text": "Neither — they heal at about the same rate, since both "
                     "are made of the same tissue.",
             "correct": False,
             "why": "They are two different tissues doing two different jobs, "
                    "and only one of them has a blood supply."},
            {"text": "The cartilage, because it has no blood supply to "
                     "deliver what a repair needs.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-s13",
        "band": "standard",
        "text": "Someone is told the cartilage in their hip has worn away. "
                "Predict what they will notice when they walk, and why.",
        "options": [
            {"text": "Grinding and pain, because the smooth facing that kept "
                     "the two bone ends apart has gone.",
             "correct": True},
            {"text": "A loose joint that gives way, because nothing is "
                     "holding the two bones together any more.",
             "correct": False,
             "why": "Ligaments hold the bones together, and they are "
                    "untouched. Losing the facing leads to grinding, not to "
                    "looseness."},
            {"text": "New directions of movement, because there is now more "
                     "room inside the joint.",
             "correct": False,
             "why": "The shape of the bone ends decides the directions, and "
                    "wearing the facing away does not hand the joint a new "
                    "one."},
            {"text": "No difference while walking, because cartilage only "
                     "matters when a joint is at rest.",
             "correct": False,
             "why": "It is the other way round. Cartilage is loaded every "
                    "time you stand on the joint, which is exactly when the "
                    "grinding is felt."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-02-h05",
        "band": "harder",
        "text": "A rescue robot needs a joint at the top of its mast that "
                "sweeps a camera left and right, and that a falling brick "
                "must not knock out of place. Which of the four types?",
        "options": [
            {"text": "A ball and socket, because a camera ought to be able to "
                     "look anywhere at all.",
             "correct": False,
             "why": "It could look anywhere, and a falling brick could push "
                    "it anywhere too. Every direction it allows is a "
                    "direction it cannot resist."},
            {"text": "A pivot, because it turns through a large angle and "
                     "refuses every other direction.",
             "correct": True},
            {"text": "A hinge, because it moves in one direction and is very "
                     "hard to fold sideways.",
             "correct": False,
             "why": "A hinge bends; it does not turn. The camera would nod up "
                    "and down rather than sweep left and right."},
            {"text": "A fixed joint, because then nothing could push it out "
                     "of place at all.",
             "correct": False,
             "why": "Nothing could move it either, the operator included. "
                    "Some movement has to be allowed, and the job is to "
                    "choose which."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h06",
        "band": "harder",
        "text": "The joints of a horse's lower leg are all hinges, and "
                "the whole limb swings in one line. A monkey's shoulder "
                "is a ball and socket. What has each been built for?",
        "options": [
            {"text": "The horse for reach and the monkey for stability, since "
                     "a hinge moves in more directions.",
             "correct": False,
             "why": "A hinge moves in one direction and a ball and socket in "
                    "three, so the reach belongs to the monkey."},
            {"text": "Both for stability, because bone ends of any shape "
                     "refuse most directions.",
             "correct": False,
             "why": "A round ball in a round socket refuses almost nothing, "
                    "which is why the shoulder is the most dislocated joint "
                    "there is."},
            {"text": "The horse for stability in one line at speed; the "
                     "monkey for reaching in many directions.",
             "correct": True},
            {"text": "Both for speed, because the shape of a joint has "
                     "nothing to do with how stable it is.",
             "correct": False,
             "why": "Shape is exactly what decides stability. Every direction "
                    "a joint allows is a direction it cannot resist."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h07",
        "band": "harder",
        "text": "A finger joint is so badly damaged that a surgeon fuses the "
                "two bones together. Which of the four types has she made, "
                "and what has the patient traded?",
        "options": [
            {"text": "A fixed joint — they lose that finger's bend and gain a "
                     "joint nothing can push out of place.",
             "correct": True},
            {"text": "A hinge — they keep the bend at that joint and lose the "
                     "ability to twist the finger.",
             "correct": False,
             "why": "A fused joint does not bend at all, and a finger joint "
                    "was already a hinge, so twisting was never on offer."},
            {"text": "A pivot — the finger can now only turn, which is all that "
                     "fusing a joint leaves behind.",
             "correct": False,
             "why": "Fusing leaves no movement of any kind. A pivot turns, "
                    "and turning is a movement."},
            {"text": "None of the four — once it is fused, a joint stops "
                     "counting as a joint at all.",
             "correct": False,
             "why": "A joint is a place where bones meet, and meeting is what "
                    "makes it one. The seams of an adult skull are joints on "
                    "exactly those grounds."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h08",
        "band": "harder",
        "text": "Your forearm has two bones running side by side rather than "
                "one thick one. What does that let you do, and what would a "
                "single bone cost you?",
        "options": [
            {"text": "It lets the elbow bend much further; a single thick bone "
                     "would stop it at a right angle.",
             "correct": False,
             "why": "The elbow bends to about 145 degrees because of the "
                    "shape of its own ends, not because of how many bones lie "
                    "below it."},
            {"text": "It makes the forearm much stronger; a single thick bone "
                     "would snap far more easily under load.",
             "correct": False,
             "why": "Strength is not the story here. What two bones give you "
                    "is a movement that one bone could not."},
            {"text": "It lets the wrist bend in more directions; a single thick "
                     "bone would leave the wrist stiff and awkward.",
             "correct": False,
             "why": "The turn happens between the two forearm bones "
                    "themselves. Roll your palm over and watch the forearm "
                    "rather than the hand."},
            {"text": "It lets one bone turn against the other, so you can "
                     "roll your palm over — one bone could not.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h09",
        "band": "harder",
        "text": "The bones of an adult pelvis meet at fixed joints. What does "
                "that suit the pelvis to do?",
        "options": [
            {"text": "Swing the legs in several directions, which needs a "
                     "rigid frame to swing them from.",
             "correct": False,
             "why": "The legs swing at the hips, which are ball-and-socket "
                    "joints. The fixed joints are the ones inside the pelvis "
                    "itself."},
            {"text": "Carry the weight of everything above it into the legs, "
                     "with nothing able to shift out of place.",
             "correct": True},
            {"text": "Cushion the load coming down the spine, by giving very "
                     "slightly at each seam.",
             "correct": False,
             "why": "A fixed joint gives nothing at all. The bones interlock "
                    "and are effectively one bone."},
            {"text": "Make blood cells, because a joint that never moves can "
                     "hold marrow safely.",
             "correct": False,
             "why": "Marrow sits inside bones rather than at joints, and it "
                    "is there whether the bone moves or not."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h10",
        "band": "harder",
        "text": "An engineer builds a model skeleton using the same rubber "
                "straps and the same smooth facing at every joint, and is "
                "surprised that all of them move the same way. What has she "
                "left out?",
        "options": [
            {"text": "The muscles — without them no joint can be held to one "
                     "direction.",
             "correct": False,
             "why": "Muscles move bones; they do not decide which directions "
                    "exist. A skeleton with no muscles on it still has a "
                    "hinge at the elbow and a ball at the shoulder."},
            {"text": "The fluid inside each joint, which is what makes some "
                     "turn and others bend.",
             "correct": False,
             "why": "Fluid keeps a joint working smoothly wherever it is. It "
                    "has nothing to do with which directions the joint has."},
            {"text": "The shapes of the bone ends, which the straps and "
                     "facing cannot supply.",
             "correct": True},
            {"text": "The tendons — each type of joint needs its own kind of "
                     "tendon to give it its movement.",
             "correct": False,
             "why": "A tendon carries a muscle's pull to a bone, and it is "
                    "the same kind of cord at every joint. Shape is what "
                    "differs."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h11",
        "band": "harder",
        "text": "A hinge and a pivot both move in one direction. Why is it "
                "wrong to call them the same type of joint?",
        "options": [
            {"text": "One bends along a line and cannot turn; the other turns "
                     "about its long axis and cannot bend.",
             "correct": True},
            {"text": "One is held by ligaments and the other by muscle, so "
                     "they are held together differently.",
             "correct": False,
             "why": "Both are held by ligaments — down each side at a hinge, "
                    "in a ring at a pivot. What differs is the movement each "
                    "one allows."},
            {"text": "A pivot moves far less than a hinge, so a pivot is "
                     "really a stiff hinge.",
             "correct": False,
             "why": "A pivot turns about 80 degrees each way, which is a "
                    "great deal of movement. It is a different movement, not "
                    "a smaller one."},
            {"text": "They are the same type, and the two names are used in "
                     "different parts of the body.",
             "correct": False,
             "why": "Try it on yourself: your elbow bends and will not turn, "
                    "and your forearm turns and will not bend there. Two "
                    "movements need two shapes."},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h12",
        "band": "harder",
        "text": "A dislocated shoulder is usually pushed back into place and "
                "expected to work again. A torn ligament in the same shoulder "
                "takes far longer to trust. Why the difference?",
        "options": [
            {"text": "A dislocation is the milder injury of the two, because no "
                     "tissue at all is damaged when one happens.",
             "correct": False,
             "why": "Straps are often stretched or torn as the joint comes "
                    "out, which is why a shoulder that has dislocated once "
                    "does it again more easily. The difference is what has to "
                    "heal."},
            {"text": "A torn ligament stops the joint from moving altogether, "
                     "and getting that movement back again always takes months.",
             "correct": False,
             "why": "A torn ligament leaves a joint moving too much rather "
                    "than too little, and that is precisely what makes it "
                    "hard to trust."},
            {"text": "A dislocation only shifts the cartilage a little way, and "
                     "cartilage slides back into its own place quite easily.",
             "correct": False,
             "why": "A dislocation takes the whole bone end out of its "
                    "socket. Cartilage is the facing on that end and goes "
                    "nowhere on its own."},
            {"text": "Back in place, the bone ends work by their shape again; "
                     "a torn strap must heal before it can refuse a "
                     "direction.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-02-h13",
        "band": "harder",
        "text": "The seams of an adult skull are called joints even though "
                "nothing moves there. A student says they should not count. "
                "What is the best reply?",
        "options": [
            {"text": "They should not count, because the word joint is properly "
                     "kept for the places where two bones move on each other.",
             "correct": False,
             "why": "The definition is not loose. A joint is a place where "
                    "bones meet, and the plates of the skull meet along a "
                    "jagged seam."},
            {"text": "Meeting is what makes a joint, not moving — so a seam "
                     "where two plates lock together is one.",
             "correct": True},
            {"text": "They count because they moved in a baby, and a joint "
                     "keeps the name once it has had it.",
             "correct": False,
             "why": "They would count even if they had never moved at all. "
                    "What makes a joint is bones meeting, at any age."},
            {"text": "They count because they still move a tiny amount, too "
                     "little to feel.",
             "correct": False,
             "why": "In an adult they are locked. The plates interlock along "
                    "a wavy join and are effectively one bone."},
        ],
        "figure": None,
    },


    # ══ MRB-338 expansion ══════════════════════════════════════════════
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": 'b2-02-e14',
        "band": 'easier',
        "text": 'A knuckle at the base of a finger bends forward and also spreads a little to the side. How many directions is that?',
        "options": [
            {"text": 'Two directions.', "correct": True},
            {"text": 'One direction of movement only.', "correct": False,
             "why": 'A hinge allows exactly one direction. The knuckle allows a second, smaller one as well.'},
            {"text": 'Three separate directions of movement.', "correct": False,
             "why": 'Three directions is a full swing, like the shoulder. The knuckle cannot turn about its own length at all.'},
            {"text": 'No directions of movement at all.', "correct": False,
             "why": 'The finger visibly bends and spreads there. That is real, usable movement, not none.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e15',
        "band": 'easier',
        "text": 'The meniscus is a curved pad of cartilage inside the knee. What is its job?',
        "options": [
            {"text": 'Straps the two bones of the knee together.', "correct": False,
             "why": "Strapping bone to bone is a ligament's job, not cartilage's."},
            {"text": 'Cushions the bone ends so they do not grind.', "correct": True},
            {"text": "Carries a muscle's pull to the shin bone.", "correct": False,
             "why": "Carrying a muscle's pull is a tendon's job. The meniscus attaches to no muscle."},
            {"text": 'Makes the fluid that lubricates the joint.', "correct": False,
             "why": 'The meniscus is fed by that fluid, not the maker of it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e16',
        "band": 'easier',
        "text": 'A ligament called the ACL runs through the middle of the knee. Based on what a ligament does everywhere else, what is its job?',
        "options": [
            {"text": "Carries a thigh muscle's pull down to the shin.", "correct": False,
             "why": "That is a tendon's job. A ligament joins bone to bone, not muscle to bone."},
            {"text": 'Cushions the bone ends inside the joint.', "correct": False,
             "why": "That is cartilage's job, such as the meniscus. A ligament straps bones rather than cushioning them."},
            {"text": 'Joins two bones and refuses a direction.', "correct": True},
            {"text": 'Gives the cartilage its own blood supply.', "correct": False,
             "why": 'Cartilage has no blood supply, and a ligament does not give it one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e17',
        "band": 'easier',
        "text": 'The jaw mostly opens and closes along one line, like a book. Which type is that closest to?',
        "options": [
            {"text": 'A pivot, since it is near the head.', "correct": False,
             "why": 'A pivot turns about an axis rather than opening and closing. Location does not decide the type.'},
            {"text": 'A ball and socket, for chewing.', "correct": False,
             "why": "A ball and socket swings in three directions. Opening and closing on one line is a hinge's movement."},
            {"text": 'A fixed joint, once it is shut.', "correct": False,
             "why": 'Biting down is the joint being used, not fixed. A fixed joint allows no movement at any time.'},
            {"text": 'A hinge — one line of movement.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e18',
        "band": 'easier',
        "text": 'A ring of tendon, the rotator cuff, wraps the shoulder alongside the ligaments. What does a tendon do there that a ligament does not?',
        "options": [
            {"text": "Carries a muscle's pull to the bone.", "correct": True},
            {"text": 'Joins the two bones of the joint.', "correct": False,
             "why": "Joining bone to bone is the ligaments' job. A tendon joins a muscle to a bone."},
            {"text": 'Cushions the ball inside the socket.', "correct": False,
             "why": "Cushioning is cartilage's job. A tendon carries a muscle's pull, and nothing more."},
            {"text": 'Feeds the cartilage with fresh blood.', "correct": False,
             "why": 'Cartilage has no blood supply, from a tendon or anywhere else.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e19',
        "band": 'easier',
        "text": 'A movable joint needs a smooth cartilage facing so its bone ends do not grind. Why does a fixed joint, like a skull seam, not need one?',
        "options": [
            {"text": 'Its bones are too small to carry cartilage.', "correct": False,
             "why": 'Size is not the reason. Cartilage faces bone ends that move, whatever their size.'},
            {"text": 'Nothing there ever moves or grinds.', "correct": True},
            {"text": 'Its ligaments already do that job instead.', "correct": False,
             "why": "Ligaments strap bones together; they do not stop grinding. That is cartilage's job at a movable joint."},
            {"text": 'Cartilage only grows at bending joints.', "correct": False,
             "why": 'A pivot turns rather than bends and still carries cartilage where its bone ends meet.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e20',
        "band": 'easier',
        "text": 'Is the wrist really one joint, the way the elbow is one meeting of two bones?',
        "options": [
            {"text": 'Yes, a single ball-and-socket joint.', "correct": False,
             "why": 'The wrist does not swing three ways, and it is not one meeting of two bones either.'},
            {"text": 'Yes, one long hinge running the length of the forearm.', "correct": False,
             "why": 'A hinge is one meeting of two bones. The wrist has several separate small bones.'},
            {"text": 'No, several small bones meeting.', "correct": True},
            {"text": 'No, it is too flexible to be a joint.', "correct": False,
             "why": 'Bones genuinely meet there, several times over — that makes it several joints, not none.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e21',
        "band": 'easier',
        "text": 'The small joints between neighbouring vertebrae let the spine curl a little at each level. Which of the four types is that?',
        "options": [
            {"text": 'A hinge, since bending is one direction.', "correct": False,
             "why": 'A hinge swings through a large angle in its one direction. Each spinal joint only glides a little.'},
            {"text": 'A pivot, since the whole spine can turn.', "correct": False,
             "why": 'Turning the spine happens mostly at the top of the neck. Lower joints only glide; they do not each turn.'},
            {"text": 'A fixed joint, since the movement there is so tiny.', "correct": False,
             "why": 'A tiny amount is still movement. A fixed joint allows none at all.'},
            {"text": 'None of the four types.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e22',
        "band": 'easier',
        "text": "A bird's wing folds partway along its length, at a joint like a human elbow. Which of the four types is that?",
        "options": [
            {"text": 'A hinge, folding along one line.', "correct": True},
            {"text": 'A ball and socket, for free angling.', "correct": False,
             "why": 'A ball and socket swings three ways. A joint that only folds does one thing: bend along one line.'},
            {"text": 'A pivot, so the wing can rotate.', "correct": False,
             "why": "A pivot turns about an axis rather than folding. This joint's whole movement is a bend."},
            {"text": 'A fixed joint, holding the wing rigid.', "correct": False,
             "why": 'The wing visibly folds there. A fixed joint would allow no fold at all.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e23',
        "band": 'easier',
        "text": "A snake's jaw joint opens far wider than a human's. Based on the range-and-stability trade, what has it given up?",
        "options": [
            {"text": 'Nothing — that range costs it nothing.', "correct": False,
             "why": 'Every direction a joint allows is one it cannot resist. This much range is not free.'},
            {"text": 'Stability — it is easy to push out of place.', "correct": True},
            {"text": 'The ability to close its mouth again.', "correct": False,
             "why": 'The jaw still closes fully between meals. What the extra range costs is stability, not closing.'},
            {"text": 'Its own blood supply to the joint.', "correct": False,
             "why": 'Range and blood supply are unconnected. The cost of range is stability, nothing else.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e24',
        "band": 'easier',
        "text": "Some people's ligaments are naturally a little stretchier than average. What would that let one of their hinge joints do?",
        "options": [
            {"text": 'Turn about its own length, like a pivot.', "correct": False,
             "why": 'Stretchier straps do not hand a joint a new direction. The bone ends still allow only one.'},
            {"text": 'Work as a ball and socket instead.', "correct": False,
             "why": 'The shape of the bone ends decides the type, and that has not changed.'},
            {"text": 'Move a few extra degrees in its one direction.', "correct": True},
            {"text": 'Manage without needing any cartilage.', "correct": False,
             "why": 'Cartilage still stops the bone ends grinding, whatever the ligaments are like.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e25',
        "band": 'easier',
        "text": 'The joint at the front of the pelvis is normally fixed. Late in pregnancy it loosens slightly. In one word, why does that matter?',
        "options": [
            {"text": "Growth — the mother's bones lengthen.", "correct": False,
             "why": 'Adult bone does not lengthen. This is a temporary change in range, not renewed growth.'},
            {"text": 'Protection — a looser joint shields more.', "correct": False,
             "why": 'A looser joint gives up protection, if anything. What it buys here is a little extra space.'},
            {"text": 'Repair — the joint is healing itself.', "correct": False,
             "why": 'Nothing there has been damaged. This is a deliberate, temporary change.'},
            {"text": 'Space — it widens the birth canal a little.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e26',
        "band": 'easier',
        "text": "An engineer designing an artificial knee copies the natural knee's own joint type. Which type does she choose?",
        "options": [
            {"text": 'A hinge, matching the natural knee.', "correct": True},
            {"text": 'A ball and socket, for free movement.', "correct": False,
             "why": 'A knee is not built for free movement. Copying its shape means copying a hinge.'},
            {"text": 'A pivot, so the leg can turn freely.', "correct": False,
             "why": 'That turn belongs to the forearm, not the knee, which only bends along one line.'},
            {"text": 'A fixed joint, so it can never come loose again.', "correct": False,
             "why": 'A fixed knee could not bend at all, and walking needs one that does.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e27',
        "band": 'easier',
        "text": "An artificial hip's ball is made from smooth, hard ceramic rather than natural cartilage. What is that chosen for?",
        "options": [
            {"text": 'So the joint carries a bigger load.', "correct": False,
             "why": "A natural hip already carries the body's full weight. Load-carrying is not what the ceramic adds."},
            {"text": 'So the two surfaces slide smoothly.', "correct": True},
            {"text": 'So fewer ligaments are needed to strap it.', "correct": False,
             "why": "Ligaments still do the strapping. The ceramic's job is the smooth facing, not the strap."},
            {"text": 'So the joint gains its own blood supply.', "correct": False,
             "why": 'Ceramic has no blood supply. It works by being hard and smooth, not by being fed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e28',
        "band": 'easier',
        "text": 'What stops your elbow bending backwards past dead straight?',
        "options": [
            {"text": 'The muscles, tightening at straight.', "correct": False,
             "why": 'Muscles move bones; they do not hold a joint together. Ligaments do the refusing here.'},
            {"text": 'The cartilage, stiffening at straight.', "correct": False,
             "why": 'Cartilage stops grinding; it does not decide how far a joint can move.'},
            {"text": 'Ligaments at the front, and the bone shape.', "correct": True},
            {"text": 'Nothing — a healthy elbow bends back a fair way.', "correct": False,
             "why": "A healthy elbow's straight position is its limit. Something is refusing to let it go further."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e29',
        "band": 'easier',
        "text": 'A pivot turns about 80 degrees each way. What is its total range from side to side?',
        "options": [
            {"text": 'About 80 degrees.', "correct": False,
             "why": 'That is one side only. The total is both sides added together.'},
            {"text": 'About 240 degrees.', "correct": False,
             "why": 'That is three lots of 80, not two. Add the two sides together instead.'},
            {"text": 'About 40 degrees.', "correct": False,
             "why": 'That is half of 80, the wrong direction for a total.'},
            {"text": 'About 160 degrees.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e30',
        "band": 'easier',
        "text": 'Ranking the four types by how much they move, which allows the least of all?',
        "options": [
            {"text": 'A fixed joint, allowing none at all.', "correct": True},
            {"text": 'A hinge, since it moves one way.', "correct": False,
             "why": 'A hinge still swings through a large angle. Something allows less movement than that.'},
            {"text": 'A pivot, since it cannot bend.', "correct": False,
             "why": 'A pivot turns through a large angle even without bending. That is still a great deal of movement.'},
            {"text": 'A ball and socket, the most dislocated of all.', "correct": False,
             "why": 'Dislocating often is a sign of a lot of movement, the opposite end of the scale.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e31',
        "band": 'easier',
        "text": 'Does a place in the body need a muscle crossing it to count as a joint?',
        "options": [
            {"text": 'Yes, without a muscle it is not a joint.', "correct": False,
             "why": 'The skull seams are joints with no muscle crossing them. Meeting is what makes a joint.'},
            {"text": 'No, bones meeting is enough on its own.', "correct": True},
            {"text": 'Yes, but only for joints that can bend.', "correct": False,
             "why": 'The knee is a joint because bones meet there, not because a muscle happens to cross it.'},
            {"text": 'No, a muscle decides which type it is.', "correct": False,
             "why": 'The shape of the bone ends decides the type, not a muscle crossing it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-e32',
        "band": 'easier',
        "text": 'The joints between the ribs and the breastbone allow only a small gliding movement. Which of the four types is that?',
        "options": [
            {"text": 'A pivot, since a small turn is a turn.', "correct": False,
             "why": 'A pivot turns through a large angle about a fixed axis. A small glide with no axis is not that.'},
            {"text": 'A hinge, since the ribcage swings.', "correct": False,
             "why": "The whole ribcage's swing comes from many small gliding joints together, not one big hinge."},
            {"text": 'None of the four types.', "correct": True},
            {"text": 'A fixed joint, since the movement there is so small.', "correct": False,
             "why": 'A small amount is still movement. A fixed joint allows none at all.'},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": 'b2-02-s14',
        "band": 'standard',
        "text": "A student says a finger's knuckle must be a hinge, because it bends. Use the fact that it also spreads sideways to correct them.",
        "options": [
            {"text": 'It really is a hinge — the sideways spread is just how a hinge happens to look close up.', "correct": False,
             "why": 'A hinge refuses every direction but one. A genuine second direction is a real direction, not a look.'},
            {"text": 'It moves in two directions, matching none of the four types exactly.', "correct": True},
            {"text": 'It is a ball and socket, since it moves more than one way.', "correct": False,
             "why": 'A ball and socket moves three ways, with a full turn included. Bending and spreading is only two.'},
            {"text": 'It is a pivot, since spreading is a kind of turning.', "correct": False,
             "why": 'A pivot turns about an axis along the bone, which a knuckle cannot do at all.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s15',
        "band": 'standard',
        "text": "A footballer's ACL tears during a sudden change of direction. Predict what the knee can now do that it could not before.",
        "options": [
            {"text": 'Bend forwards further, since a direction has been freed up.', "correct": False,
             "why": 'The ACL does not refuse ordinary bending. What it was refusing is the shin sliding forward.'},
            {"text": 'Turn a little, the way a pivot does, missing a strap.', "correct": False,
             "why": 'Removing a strap does not hand a hinge a new direction. The bone ends still refuse turning.'},
            {"text": 'Let the shin slide too far forward under the thigh.', "correct": True},
            {"text": 'Nothing changes, since other ligaments take over the job.', "correct": False,
             "why": "The other ligaments refuse other directions. None was refusing forward sliding, which is the ACL's own job."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s16',
        "band": 'standard',
        "text": 'Years of a sport that twists hard at the knee wears the meniscus thin. Predict how quickly it heals, and why.',
        "options": [
            {"text": 'Quickly, since twisting feeds it plenty of fresh fluid.', "correct": False,
             "why": 'Feeding it fluid is not the same as fast repair. It heals slowly regardless, having no blood supply.'},
            {"text": 'At the same rate as a torn ligament nearby.', "correct": False,
             "why": 'Ligaments have a better blood supply than cartilage, so the two do not heal at the same rate.'},
            {"text": 'Quickly, because constant loading speeds repair.', "correct": False,
             "why": 'Loading feeds cartilage a little; it does not speed repair, which the lack of blood supply limits.'},
            {"text": 'Slowly, or not at all — it has no blood supply.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s17',
        "band": 'standard',
        "text": 'The jaw is close to a hinge, and hinges rarely dislocate. Yet a jaw genuinely can, if opened too wide. What does that suggest?',
        "options": [
            {"text": 'It must not be a pure hinge — it can slide, too.', "correct": True},
            {"text": 'That the rule about hinges is simply wrong.', "correct": False,
             "why": 'The rule still holds for a true hinge like the elbow. It suggests the jaw is not a pure hinge.'},
            {"text": "The jaw's ligaments are simply weaker than an "
                     "elbow's own.", "correct": False,
             "why": "A true hinge's shape refuses the direction outright, whatever the ligaments are like."},
            {"text": 'A dislocated jaw does not really count as one.', "correct": False,
             "why": 'A joint pushed out of place is a dislocation wherever it happens. The jaw meets that definition.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s18',
        "band": 'standard',
        "text": "An athlete tears their rotator cuff tendons, but the shoulder's ligaments are untouched. Predict what changes.",
        "options": [
            {"text": 'Nothing — the ligaments keep the ball in place.', "correct": False,
             "why": 'The ligaments still strap the joint, but the cuff muscles actively drive and steady it. Losing them changes something.'},
            {"text": 'Passive holding stays, but active strength is lost.', "correct": True},
            {"text": 'The joint would dislocate at once without the tendons at all.', "correct": False,
             "why": 'The ligaments still refuse their own direction. An immediate dislocation is not what tendon loss causes.'},
            {"text": 'New cartilage grows to replace the tendons.', "correct": False,
             "why": 'Cartilage and tendons are different tissues with different jobs. One does not regrow as the other.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s19',
        "band": 'standard',
        "text": "The pelvis's front joint normally allows no movement, but loosens slightly late in pregnancy. Suggest what is traded, and why it might be worth it.",
        "options": [
            {"text": 'Protection for stability — it shields more.', "correct": False,
             "why": 'Protection is not what a loosened joint gains. The trade is stability for a little extra space.'},
            {"text": 'Blood supply for calcium, to rebuild later.', "correct": False,
             "why": 'Neither of those is what changes here. What is traded is stability, for a small gain in space.'},
            {"text": 'Stability for a little space, which may help birth.', "correct": True},
            {"text": 'Nothing — the change costs nothing at all.', "correct": False,
             "why": 'Every direction a joint gains is one it cannot resist. This loosened joint is genuinely less stable.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s20',
        "band": 'standard',
        "text": "An artificial hip's ball is smooth ceramic rather than natural cartilage. Explain one advantage ceramic has that cartilage does not.",
        "options": [
            {"text": 'It repairs itself faster once it has worn down.', "correct": False,
             "why": 'Ceramic cannot repair itself at all. Its benefit is not needing feeding in the first place.'},
            {"text": 'It adds material where the load goes, like bone.', "correct": False,
             "why": "That is bone's own trick, done by its living cells. Ceramic does not adapt to load at all."},
            {"text": 'It grows with the patient over the years.', "correct": False,
             "why": 'Nothing about ceramic grows. It is a fixed shape that simply needs no feeding.'},
            {"text": 'It needs no blood supply, so it cannot be starved.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s21',
        "band": 'standard',
        "text": 'An engineer designing an artificial knee copies the hinge rather than a ball and socket. Why would a ball-and-socket knee be worse?',
        "options": [
            {"text": 'It allows directions the real knee never had.', "correct": True},
            {"text": 'It would be too costly to manufacture well.', "correct": False,
             "why": 'Cost is not the reasoning here. The problem is what the extra directions do to stability.'},
            {"text": 'It would not fit inside the leg at all.', "correct": False,
             "why": "Size is not what rules it out. It would move in directions the leg's load-bearing never expects."},
            {"text": 'It would need no ligaments to strap it together at all.', "correct": False,
             "why": 'A ball and socket still needs ligaments — the shoulder has a whole ring of them.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s22',
        "band": 'standard',
        "text": "A bird's wing folds at a hinge-like joint, similar to a human elbow. Predict whether it can also rotate, the way a human forearm's pivot does.",
        "options": [
            {"text": 'Yes, every joint in a wing must turn for flight.', "correct": False,
             "why": 'Flight does not require every joint to turn. A hinge shape refuses rotation whatever it is used for.'},
            {"text": 'No — a hinge shape refuses rotation, as an elbow does.', "correct": True},
            {"text": 'Yes, but only while the bird is airborne.', "correct": False,
             "why": 'What a joint can do is decided by its bone shape, not by whether the animal is flying.'},
            {"text": 'It cannot really be known without seeing the wing actually move.', "correct": False,
             "why": 'The model predicts this directly: a hinge shape refuses turning wherever it is found.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s23',
        "band": 'standard',
        "text": "A snake's jaw joint lets it swallow prey wider than its own head. What has it given up to get that range?",
        "options": [
            {"text": 'Its blood supply, to make room for movement.', "correct": False,
             "why": "Blood supply and range are unconnected. A joint's range trades against how well it resists a push."},
            {"text": 'Its cartilage, since range needs none of it.', "correct": False,
             "why": 'Even a very mobile joint still needs a smooth facing to stop its bone ends grinding.'},
            {"text": 'Stability — the joint is easy to push aside.', "correct": True},
            {"text": 'Nothing — that much range costs it nothing.', "correct": False,
             "why": 'Every direction a joint allows is one it cannot resist. That much range cannot come free.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s24',
        "band": 'standard',
        "text": "Two gymnasts train identically, but one's knee moves a few degrees further before the ligaments refuse it. Whose knee is more at risk from a hard twist?",
        "options": [
            {"text": 'The less flexible one, under more strain twisting.', "correct": False,
             "why": 'A stiffer joint refuses the twisting direction sooner, which is what protects it.'},
            {"text": 'Neither, since training identically evens it out.', "correct": False,
             "why": 'The ligaments differ, and ligaments decide when a direction is refused. That difference changes the risk.'},
            {"text": 'The more flexible one, but only if weaker too.', "correct": False,
             "why": 'Nothing says their muscles differ. The risk here comes from ligament looseness, not muscle strength.'},
            {"text": 'The more flexible one, since its refusal comes later.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s25',
        "band": 'standard',
        "text": 'A student says the spine barely bends, since each joint between two vertebrae only glides a tiny amount. Explain why the whole spine still curls a long way.',
        "options": [
            {"text": 'Each tiny movement adds up along the whole chain.', "correct": True},
            {"text": 'The student is right — the spine barely bends.', "correct": False,
             "why": 'The spine visibly curls a long way forward. That curl has to come from somewhere along the chain.'},
            {"text": 'One joint near the base does most of the work.', "correct": False,
             "why": 'No single spinal joint carries a large range. The curl is shared in small amounts across the chain.'},
            {"text": 'The vertebrae themselves bend a little too.', "correct": False,
             "why": 'Bone does not bend under an ordinary load. The curl comes entirely from the joints between the bones.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s26',
        "band": 'standard',
        "text": 'A sudden hard pull tries to yank an arm from its socket. Which tissue is already in place, resisting that pull from the first instant?',
        "options": [
            {"text": 'The muscles, which have to contract before they can resist anything.', "correct": False,
             "why": 'A muscle adds to a joint\'s steadiness, but it has to be told to contract first. The ligaments are strapped across the joint before the pull ever arrives.'},
            {"text": 'The ligaments, strapped bone to bone across the joint.', "correct": True},
            {"text": 'Neither, since the pull is too fast for any tissue to resist.', "correct": False,
             "why": 'A ligament needs no warning and no reaction time — it is already taut when the pull arrives.'},
            {"text": 'The cartilage, cushioning any sudden movement.', "correct": False,
             "why": 'Cartilage cushions against grinding; it does nothing to stop the ball leaving the socket.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s27',
        "band": 'standard',
        "text": 'A hinge model bends through 0 to 145 degrees, and a ball-and-socket model swings through 0 to 180. By how many degrees does the second beat the first?',
        "options": [
            {"text": 'By 325 degrees.', "correct": False,
             "why": 'That is the two ranges added, not the gap between them. Subtract one from the other instead.'},
            {"text": 'By 180 degrees, its own full range.', "correct": False,
             "why": "180 is the ball and socket's own range, not how much bigger it is than the hinge's."},
            {"text": 'By 35 degrees.', "correct": True},
            {"text": 'By 145 degrees, its own full range.', "correct": False,
             "why": "145 is the hinge's own range, not the gap between the two figures."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s28',
        "band": 'standard',
        "text": "Some people's elbows bend backward a few degrees past straight, since their front ligaments are looser than average. Is the elbow now a different type of joint?",
        "options": [
            {"text": 'Yes, since it moves further than average now.', "correct": False,
             "why": 'The bone ends have not changed shape. The range has changed, not the type.'},
            {"text": 'Yes, the extra backward movement is a genuine second direction of movement.', "correct": False,
             "why": "Backward past straight is the same line of movement a hinge already has, unlike the thumb's true saddle."},
            {"text": 'No, but only if the bones are shaped differently.', "correct": False,
             "why": 'The scenario is about looser ligaments, not a different bone shape.'},
            {"text": 'No — still a hinge, with more range in one line.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s29',
        "band": 'standard',
        "text": 'A student says the wrist is one joint, like the elbow. Using what makes the elbow one joint, explain why the wrist is not.',
        "options": [
            {"text": 'Several small bones meet, so it is really several joints.', "correct": True},
            {"text": 'The wrist has no bones meeting, only cartilage.', "correct": False,
             "why": "Cartilage faces bone ends; it does not replace them. The wrist's bones genuinely meet in several places."},
            {"text": 'The elbow is not one joint either, so it fails too.', "correct": False,
             "why": "The elbow really is one pair of bones meeting. The comparison fails on the wrist's side."},
            {"text": 'The wrist moves too little to count as a joint.', "correct": False,
             "why": 'How much a joint moves does not decide whether it counts. Bones meeting is what makes one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s30',
        "band": 'standard',
        "text": 'An artificial hip usually needs replacing after fifteen to twenty years, while a healthy natural hip can last a lifetime. Suggest why, based on living tissue.',
        "options": [
            {"text": 'Ceramic is heavier, straining the rest of the leg.', "correct": False,
             "why": 'Weight is not the reason. Living tissue repairs itself; ceramic simply cannot.'},
            {"text": 'Living tissue repairs and adapts; ceramic just wears.', "correct": True},
            {"text": 'Both are fed by a blood supply, so both should last.', "correct": False,
             "why": 'An artificial hip has no blood supply at all, which is exactly why it cannot repair itself.'},
            {"text": 'The body eventually rejects any implant, however well it was fitted.', "correct": False,
             "why": 'Rejection is not what limits its life. It wears down mechanically, with nothing to repair it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s31',
        "band": 'standard',
        "text": 'A student says the rib-to-spine joints must be pivots, since they allow a turning-like gliding motion. Explain why that is wrong.',
        "options": [
            {"text": 'Any joint that turns any amount counts as a pivot.', "correct": False,
             "why": 'Size matters here. A pivot turns a large angle about a fixed axis; these joints move far too little.'},
            {"text": 'Pivots only exist in the neck and forearm.', "correct": False,
             "why": 'The model is not tied to two locations. What rules this out is the size and shape of the movement.'},
            {"text": 'A pivot turns a large angle about a fixed axis; these joints only glide a little.', "correct": True},
            {"text": 'They are pivots, just small and weak ones.', "correct": False,
             "why": "A pivot's whole movement is a large turn about an axis. A small glide with no axis is a different thing."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-s32',
        "band": 'standard',
        "text": 'A knee brace after an ACL injury stops the shin sliding forward, not the knee bending. Explain why it still lets the knee bend freely.',
        "options": [
            {"text": 'The brace cannot be made stiff enough to stop bending too.', "correct": False,
             "why": "A brace could be built rigid if that were the aim. Bending was never the ACL's own direction to refuse."},
            {"text": 'Bending and sliding forward are the same direction.', "correct": False,
             "why": "They are different: bending is the hinge's normal movement, and forward sliding is the ACL's own job."},
            {"text": 'It lets the knee bend to test if it has healed.', "correct": False,
             "why": 'The reason is mechanical, not a test. It replaces only the direction the torn ligament used to refuse.'},
            {"text": "Bending is the hinge's own allowed direction.", "correct": True},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": 'b2-02-h14',
        "band": 'harder',
        "text": 'An engineer needs a robot shoulder that reaches in almost any direction, and accepts it will be the weakest joint in the robot. Which type, and what has she accepted?',
        "options": [
            {"text": 'A pivot, accepting it can only reach one plane.', "correct": False,
             "why": "A pivot turns about one axis, which does not match reaching almost anywhere. That is a ball-and-socket's job."},
            {"text": 'A hinge, accepting that it folds sideways under a knock.', "correct": False,
             "why": 'A hinge does the opposite of what is wanted: it refuses almost every direction, sideways included.'},
            {"text": 'A ball and socket, accepting low stability.', "correct": True},
            {"text": 'A fixed joint, accepting frequent replacement.', "correct": False,
             "why": 'A fixed joint reaches in no direction at all, failing the brief rather than trading anything away.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h15',
        "band": 'harder',
        "text": 'A surgeon fits an artificial knee with the natural hinge range, but leaves out the front ligaments that stop it bending backward past straight. What goes wrong first?',
        "options": [
            {"text": 'It twists sideways, its groove left too shallow.', "correct": False,
             "why": 'Sideways twisting is refused by the groove shape itself, which the surgeon has copied unchanged.'},
            {"text": 'It loses its bending range and becomes fixed.', "correct": False,
             "why": 'The hinge shape, not the missing ligaments, gives the joint its bending range. That shape is unchanged.'},
            {"text": 'Nothing — the groove already stops all overextension entirely.', "correct": False,
             "why": "The groove stops sideways movement and twisting. Stopping the joint at straight is the ligaments' own job."},
            {"text": 'It bends backward past straight under load.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h16',
        "band": 'harder',
        "text": 'Someone tears both their ACL and meniscus in one fall. The meniscus causes more trouble years later. Explain why, using blood supply.',
        "options": [
            {"text": 'The meniscus has almost no blood supply of its own.', "correct": True},
            {"text": 'The ACL has no blood supply, so it heals the faster of the two.', "correct": False,
             "why": 'Having no blood supply slows healing, not speeds it. The ACL is actually fed better than the meniscus.'},
            {"text": 'Both tissues heal at exactly the same steady rate.', "correct": False,
             "why": 'The two are fed differently, and that difference explains why one causes more lasting trouble.'},
            {"text": 'The meniscus is simply the bigger of the two structures.', "correct": False,
             "why": 'Size does not decide healing. What decides it is whether living cells are being supplied to repair it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h17',
        "band": 'harder',
        "text": "A student argues the pelvis is not really a 'fixed' joint, since it demonstrably loosens in pregnancy. Using the skull's own fixed joints, give the better reply.",
        "options": [
            {"text": 'The skull alone proves fixed joints never move, so the pelvis must be a different type entirely.', "correct": False,
             "why": "The skull seams do move, but only in a baby, before locking for good. That already shows a fixed joint's state can change."},
            {"text": 'Like a skull seam, fixed describes a usual state, not an unbreakable promise.', "correct": True},
            {"text": 'The student is right, and fixed should mean never moving at all.', "correct": False,
             "why": "Applied that strictly, the skull seams would fail too, since they move while a baby's head grows."},
            {"text": 'The pelvis and skull cannot be compared at all.', "correct": False,
             "why": 'What they share is the relevant point: both are usually fixed, and both can change state at one time.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h18',
        "band": 'harder',
        "text": "Compare a snake's jaw joint with a human's. Explain why a human could not safely have a snake's joint, even though it would widen what we could eat.",
        "options": [
            {"text": "A snake's joint would not fit inside a human skull at all.", "correct": False,
             "why": 'Size is not the point. The problem is what the joint could withstand once fitted — a hard bite would fail it.'},
            {"text": "A snake's jaw already refuses far more directions than a human jaw does.", "correct": False,
             "why": "It is the opposite: the snake's joint allows far more range and refuses far less."},
            {"text": 'It trades stability for range; a hard bite would dislocate it.', "correct": True},
            {"text": 'Nothing at all prevents the swap; it would work exactly as well.', "correct": False,
             "why": "A human's joint has to resist forceful biting, which a snake's joint, built for range, never has to do."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h19',
        "band": 'harder',
        "text": "A bird's wing has a hinge-like joint and a ball-and-socket shoulder, matching a human arm. Yet it cannot roll its wingtip the way a human wrist can. What does that tell you?",
        "options": [
            {"text": "That a bird's shoulder is really a pivot.", "correct": False,
             "why": 'Swinging the whole wing is exactly what a ball and socket does. The missing movement is a rolling turn.'},
            {"text": 'That its hinge secretly allows some rotation too.', "correct": False,
             "why": 'A hinge shape refuses rotation by its shape alone. What is missing is a separate pivot, not a hidden ability.'},
            {"text": 'That flight makes a rolling wrist unnecessary.', "correct": False,
             "why": "A joint's movement is decided by its bone shape, not switched off by what an animal needs."},
            {"text": "That the wing lacks the forearm's own pivot joint.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h20',
        "band": 'harder',
        "text": 'A sudden hard pull tries to yank an arm from its socket. Explain why the cuff muscles, not the ligaments, respond to how sudden and hard the pull is.',
        "options": [
            {"text": 'Muscles can contract harder the instant a pull arrives.', "correct": True},
            {"text": 'Ligaments tire, so a muscle has to take over from them.', "correct": False,
             "why": 'A ligament does not tire — it is not contracting. What it cannot do is vary how hard it resists, which is the muscle\'s own trick.'},
            {"text": 'Ligaments only work while the joint is still.', "correct": False,
             "why": 'Ligaments resist a pull at all times; they simply cannot adjust how hard they resist.'},
            {"text": 'Neither responds — bone shape alone resists it.', "correct": False,
             "why": "The shoulder's shape allows almost every direction rather than resisting them, which is why the muscles and ligaments both matter."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h21',
        "band": 'harder',
        "text": 'A hinge model bends through 145 degrees, and a pivot model turns through 170 in total. Which is bigger, and by how many degrees?',
        "options": [
            {"text": 'The hinge, by 25 degrees.', "correct": False,
             "why": "170 is bigger than 145 — the pivot's total is the larger figure."},
            {"text": 'The pivot, by 25 degrees.', "correct": True},
            {"text": "The pivot, by 170 degrees, its own full range.", "correct": False,
             "why": "170 is the pivot's whole range, not the gap between the two totals."},
            {"text": 'Neither — the two figures are close enough to be treated as equal.', "correct": False,
             "why": 'They are different figures with a genuine gap, worked out by subtraction: 170 minus 145 is 25.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h22',
        "band": 'harder',
        "text": "A student calls a broken wrist bone 'a broken joint.' Using how many bones meet at the wrist, explain why that is imprecise.",
        "options": [
            {"text": 'Any injury anywhere in the hand counts as a joint injury too.', "correct": False,
             "why": 'A joint is specifically bones meeting, not any injury nearby. A break inside a bone is a different kind of damage.'},
            {"text": 'The wrist does not really contain a true joint at all.', "correct": False,
             "why": 'The wrist does contain true joints, wherever its small bones meet each other.'},
            {"text": 'Several bones meet there, so breaking one differs from a joint.', "correct": True},
            {"text": 'A broken bone always heals faster than a broken joint.', "correct": False,
             "why": 'Healing speed is not the issue. A break inside one bone is not the same as bones coming apart at a joint.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h23',
        "band": 'harder',
        "text": "A gymnast's elbows bend backward further than average, and a coach calls this 'a different, looser kind of hinge.' Is the coach right?",
        "options": [
            {"text": 'Yes, any hinge moving more than average becomes a new type of joint.', "correct": False,
             "why": 'Type is decided by bone shape, unchanged here. Extra range in the same direction is not a new type.'},
            {"text": 'Yes, a looser hinge behaves more like a ball and socket joint.', "correct": False,
             "why": "A ball and socket allows three directions. The gymnast's elbow still refuses every direction but one."},
            {"text": 'It cannot be judged at all without knowing if it can twist.', "correct": False,
             "why": 'The scenario already states the extra movement is backward bending, which is enough to settle it.'},
            {"text": 'No — it is the same type of joint, just with extra range in one direction.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h24',
        "band": 'harder',
        "text": "A student claims that because each rib-to-spine joint only glides a tiny amount, the ribcage 'barely moves' when breathing. Use the spine's own joints as a parallel case against that.",
        "options": [
            {"text": 'Many tiny glides add up along the chain, just as they do in the spine.', "correct": True},
            {"text": 'The student is right, since tiny movements stay tiny overall.', "correct": False,
             "why": "The spine's own case shows the opposite: many small movements along a chain add up to a large curl."},
            {"text": 'The comparison fails, since the two bend in different directions.', "correct": False,
             "why": 'The direction differs, but the point does not: many small joint movements together produce a large one.'},
            {"text": 'Only the joint nearest the breastbone moves, and it moves a great deal.', "correct": False,
             "why": 'No single rib joint carries a large range. The ribcage\'s swing is shared in small amounts along the whole chain, exactly as the spine\'s curl is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h25',
        "band": 'harder',
        "text": "An engineer claims a ceramic hip is 'better than the real thing in every way,' since it never wears from a lack of blood supply. Evaluate that.",
        "options": [
            {"text": 'Correct — needing no blood supply removes every problem.', "correct": False,
             "why": 'It removes one disadvantage. It does not give ceramic the ability to repair or adapt, which living tissue can.'},
            {"text": 'Not quite — it also cannot repair or adapt itself.', "correct": True},
            {"text": 'Wrong only because ceramic costs more to make.', "correct": False,
             "why": 'Cost is not the relevant gap. The real one is that ceramic cannot repair or adapt itself.'},
            {"text": 'Wrong because ceramic has its own, weaker blood supply.', "correct": False,
             "why": 'Ceramic has no blood supply at all, which is exactly why it cannot repair or adapt.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h26',
        "band": 'harder',
        "text": "A rescue robot's camera pivot and a snake's wide-gaping jaw use the range-and-stability trade in opposite directions. Explain why the same rule gives two such different designs.",
        "options": [
            {"text": "The rule cannot apply to an evolved joint like a snake's.", "correct": False,
             "why": "The trade applies to any joint. The snake's jaw pays for its range with instability, exactly as the rule predicts."},
            {"text": 'Both solve exactly one problem, so the two designs must really be the same underneath.', "correct": False,
             "why": 'They solve different problems — resisting a fall against swallowing something wide — which is why the rule gives opposite designs.'},
            {"text": 'The robot needs stability against a knock; the snake needs huge range to swallow prey.', "correct": True},
            {"text": 'The rule applies to the robot but never to any animal at all.', "correct": False,
             "why": "The trade is a consequence of shape, not of who built the joint. It governs the snake's jaw too."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h27',
        "band": 'harder',
        "text": "A rotator cuff tendon has a better blood supply than the knee's meniscus. Predict which — a torn tendon or a torn meniscus — heals better without surgery, and why.",
        "options": [
            {"text": 'The meniscus, since cartilage resists damage better.', "correct": False,
             "why": 'Toughness is not what decides healing. The meniscus heals poorly because it has almost no blood supply.'},
            {"text": 'Neither; a tendon and a meniscus heal at the same rate.', "correct": False,
             "why": 'The two tissues are fed very differently, and blood supply is what decides how well an injury heals.'},
            {"text": 'The meniscus, fed directly by the joint fluid instead.', "correct": False,
             "why": 'Joint fluid feeds cartilage far less reliably than a genuine blood supply, which is why it heals so poorly.'},
            {"text": 'The tendon — better blood supply means better repair.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h28',
        "band": 'harder',
        "text": 'An engineer wants an artificial knee to last as long as possible in an active young patient, compared with an elderly one. Suggest why the material choice might differ.',
        "options": [
            {"text": "A young patient's joint takes far more repeated force each year.", "correct": True},
            {"text": 'It does not need to differ for either patient at all.', "correct": False,
             "why": 'More force, more often, over more years wears a material that cannot adapt the way living bone does.'},
            {"text": 'A young patient needs a much softer material instead.', "correct": False,
             "why": 'An artificial knee is fitted once growth is finished, and softness is not the issue here.'},
            {"text": 'An elderly patient needs the tougher, more expensive material instead.', "correct": False,
             "why": 'The elderly, less active patient puts less repeated force through the joint over the years remaining.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h29',
        "band": 'harder',
        "text": 'A student says that because the knee and elbow are the same type of joint, they must be equally at risk of injury. Using body weight, explain why they are not.',
        "options": [
            {"text": 'Being the same type of joint decides risk on its own, whatever else differs.', "correct": False,
             "why": 'Shape decides what directions a joint allows, not how much real-world force actually passes through it.'},
            {"text": "The knee carries the body's whole weight, unlike the elbow.", "correct": True},
            {"text": 'The elbow must really be a completely different type of joint.', "correct": False,
             "why": 'Both are genuinely hinges. What differs is the load each ordinarily carries, not their type.'},
            {"text": 'More weight passing through a hinge makes it more stable, not less.', "correct": False,
             "why": 'More weight puts more strain through the same refused directions, raising risk rather than lowering it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h30',
        "band": 'harder',
        "text": 'A surgeon could fuse a badly arthritic hip solid instead of replacing it with a ball and socket. State one thing the patient gains, and one they lose.',
        "options": [
            {"text": 'Gains full movement and loses nothing at all.', "correct": False,
             "why": 'A fused joint has no movement at all, since fusing removes it rather than only removing a weakness.'},
            {"text": 'Gains a normal walking gait, loses a little strength.', "correct": False,
             "why": 'A fused hip cannot bend or swing at all, so a normal gait is exactly what is lost, not gained.'},
            {"text": 'Gains stability against dislocation, loses all movement.', "correct": True},
            {"text": 'Gains and loses nothing measurable either way.', "correct": False,
             "why": 'The two are opposite trades: a replacement keeps range for less stability, and fusing does the reverse.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h31',
        "band": 'harder',
        "text": "A rescue robot's camera pivot and the human neck's own pivot solve the same kind of problem. Name it, and explain why a ball and socket would be wrong for both.",
        "options": [
            {"text": 'Needing to bend forward and back, which needs a hinge instead.', "correct": False,
             "why": 'Neither joint is built mainly for bending. The shared need is a large turn, side to side.'},
            {"text": 'Needing the strongest joint possible, and a ball and socket is weakest.', "correct": False,
             "why": 'A ball and socket is not always the weakest — it is built for range rather than resistance.'},
            {"text": 'Neither is really about range and stability; a camera cannot dislocate.', "correct": False,
             "why": 'A pivoted camera mount can be knocked out of place just as a real joint can.'},
            {"text": 'A useful turn while resisting a knock from other directions.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-02-h32',
        "band": 'harder',
        "text": "A student claims 'every joint trades range for stability, except fixed joints, which get both for free.' Evaluate that using the skull.",
        "options": [
            {"text": 'Not for free — it trades away every direction of movement in return for its stability.', "correct": True},
            {"text": 'Correct, since a joint that cannot move cannot be pushed out of place, so it costs nothing.', "correct": False,
             "why": 'Losing every direction of movement is itself a cost, even though nothing can push it out of place.'},
            {"text": 'Correct for the skull, but wrong for every other fixed joint.', "correct": False,
             "why": 'The same reasoning applies to any fixed joint: all buy stability by giving up movement entirely.'},
            {"text": 'Wrong, because fixed joints are less stable than hinges, not more.', "correct": False,
             "why": 'A fixed joint refuses every direction, making it the most stable of the four, not the least.'},
        ],
        "figure": None,
    },
]
