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
]
