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
            {"text": "They are different shapes, not different settings: a "
                     "groove allows one direction, an interlocking seam "
                     "allows none.",
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
            {"text": "A pivot joint between the two bones of the forearm, one "
                     "of them turning inside a ring of ligament.",
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
            {"text": "The model still sorts most of the skeleton, and the "
                     "joints it fails on are the ones worth looking at "
                     "properly.",
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
            {"text": "Cartilage is fed by fluid squeezed through it as the "
                     "joint is loaded and unloaded, so using it is the only "
                     "way to feed it.",
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
]
