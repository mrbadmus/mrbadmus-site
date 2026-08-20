"""B2 lesson 01 — What the skeleton does: twelve questions (MRB-269).

The lesson's claim is that the skeleton does four jobs at once, that every one
of them fails by a different route to the same destination — cells with no
oxygen to respire with — and that none of it makes sense unless bone is living
tissue. These twelve probe exactly that: the four jobs read off a described
structure rather than recited, the four switch-off chains applied to situations
the lesson does not draw (a fractured hip, a damaged marrow, a broken finger
beside a broken femur), the timescale that separates the ribcage from the
marrow, and — in the harder band — the same rules carried into unfamiliar
contexts: a helmet compared with the skull that outlives it, and a carbon-fibre
femur that does three of the four jobs perfectly.

The distractors are built from the lesson's three declared misconceptions.
BODY-03 "how bad a break is depends on how big the bone is" supplies the size,
pain and healing-time wrong answers in the femur questions. BODY-02 "the
skeleton's job is holding you up; the rest are extras" supplies the answers
that treat a rigid replacement as a complete one, that hand movement to the
muscles alone, and that expect the damage to stay inside the bone. BODY-01
"bones are dead" supplies the answers that say a femur cannot knit, that bone
thickness is fixed at birth, and that hardness is what a skeleton is for. A
fourth family of distractor runs through the whole bank: the two jobs students
most readily swap, marrow-makes-blood and bone-carries-load, and the very
different timescales on which they fail.
"""

UNIT = "B2"
LESSON = "what-the-skeleton-does"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-01-e01",
        "band": "easier",
        "text": "A student lists the skeleton's jobs as: support, protection, "
                "movement, and keeping you warm. Which correction do they "
                "need?",
        "options": [
            {"text": "Movement is not one — muscles move you, and the bones "
                     "just get dragged along", "correct": False,
             "why": "A muscle can only shorten. It moves nothing at all unless "
                    "there is something rigid for it to pull on, so movement "
                    "is a skeletal job as much as a muscular one."},
            {"text": "Keeping you warm is not one — the fourth job is making "
                     "blood cells", "correct": True},
            {"text": "Protection is not one — shielding your organs is what "
                     "skin and muscle are for", "correct": False,
             "why": "Skin and muscle over your brain would not stop a knock. "
                    "The skull is a fused box of bone precisely because soft "
                    "tissue cannot do that job."},
            {"text": "Nothing needs correcting — those are the four jobs the "
                     "skeleton does", "correct": False,
             "why": "Keeping you warm is not a job of the skeleton. The one "
                    "they have missed is making blood cells, in the marrow "
                    "inside the big bones."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e02",
        "band": "easier",
        "text": "Which of these is evidence that bone is living tissue rather "
                "than a dead frame?",
        "options": [
            {"text": "A broken bone repairs itself and knits back together",
             "correct": True},
            {"text": "Bone is hard enough to carry your entire body weight",
             "correct": False,
             "why": "Hardness says nothing about being alive. Concrete carries "
                    "enormous loads and there is not one living thing in it."},
            {"text": "Bones stop changing once you have finished growing",
             "correct": False,
             "why": "They never stop. You replace roughly a tenth of your "
                    "whole skeleton every year, for your entire life — which "
                    "is itself evidence that bone is alive."},
            {"text": "A skeleton in a museum keeps its shape for centuries",
             "correct": False,
             "why": "That is what is left once the living parts have gone. The "
                    "skeleton in the corner of the lab is dead; the one you "
                    "are sitting on is not."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e03",
        "band": "easier",
        "text": "The skull is eight curved plates fused into a single box, "
                "with holes only where nerves and blood vessels have to pass "
                "through. Which job is that shape built for?",
        "options": [
            {"text": "Support — it is what holds your head up above your "
                     "shoulders", "correct": False,
             "why": "The bones of your neck carry the weight of your head. A "
                    "sealed box with almost no holes in it is not a shape for "
                    "carrying loads — it is a shape for keeping things out."},
            {"text": "Making blood cells — the space inside the box is where "
                     "they are made", "correct": False,
             "why": "The space inside your skull is full of brain. Blood cells "
                    "are made in the marrow, in the hollow middle of the big "
                    "bones."},
            {"text": "Movement — the plates slide across each other as you "
                     "turn your head", "correct": False,
             "why": "Fused means joined solid. Nothing in an adult skull "
                    "slides, and that rigidity is the entire point of the "
                    "design."},
            {"text": "Protection — a fused box takes an impact the brain could "
                     "not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e04",
        "band": "easier",
        "text": "Switch off any part of the skeleton — skull, ribcage, femur "
                "or marrow — and the damage always finishes in the same place. "
                "Where?",
        "options": [
            {"text": "At the bone that was switched off, because the damage "
                     "stays where it started", "correct": False,
             "why": "Not one of the four chains stays inside the bone. Every "
                    "one of them leaves it within a step, which is why "
                    "switching a part off tells you what it was doing."},
            {"text": "At the muscles, because muscles are attached to every "
                     "bone in the body", "correct": False,
             "why": "The femur's chain does start at muscle, but the ribcage's "
                    "and the marrow's never touch it — and all four still end "
                    "up in the same place."},
            {"text": "At cells that no longer get the oxygen they need to "
                     "respire", "correct": True},
            {"text": "At the brain, because the brain is what controls every "
                     "other organ", "correct": False,
             "why": "Only the skull's chain starts at the brain. The marrow's "
                    "chain goes nowhere near it and still ends at cells with "
                    "no oxygen."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-01-s01",
        "band": "standard",
        "text": "A ribcage failure and a marrow failure end in exactly the "
                "same place. What is the real difference between them?",
        "options": [
            {"text": "How fast they get there — the ribcage in minutes, the "
                     "marrow over months", "correct": True},
            {"text": "Only the ribcage failure reaches the cells; the marrow "
                     "one stops in the blood", "correct": False,
             "why": "The marrow chain finishes with every cell in the body "
                    "short of oxygen. Both end at the cells — that is why the "
                    "lesson puts them side by side."},
            {"text": "The marrow one is worse, because red blood cells can "
                     "never be replaced", "correct": False,
             "why": "They are replaced constantly — about two million a "
                    "second. The trouble is that the ones you have wear out in "
                    "about four months and nothing new arrives."},
            {"text": "The ribcage one is worse, because it leaves the heart "
                     "unprotected", "correct": False,
             "why": "The ribcage does shield the heart, but that is not what "
                    "kills in minutes. It is the movement job: with the "
                    "chest wall loose, each breath moves far too little "
                    "air."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s02",
        "band": "standard",
        "text": "An 80-year-old breaks their hip. The bone will heal. Why do "
                "doctors treat this as far more dangerous than a broken wrist "
                "that heals in the same time?",
        "options": [
            {"text": "The broken bone stops making blood cells, so they are "
                     "short of oxygen within days", "correct": False,
             "why": "That is one bone's worth of marrow, and the rest of the "
                    "skeleton carries on making blood. Even a total marrow "
                    "failure takes months, not days."},
            {"text": "Their leg muscles stop contracting now the bone beneath "
                     "them has broken", "correct": False,
             "why": "The muscles contract and shorten exactly as before. What "
                    "has gone is the rigid bar for them to pull against, so "
                    "the contraction moves nothing."},
            {"text": "Nothing can be reached and nothing escaped from — "
                     "including food, warmth and help", "correct": True},
            {"text": "Bone is dead material, so a femur that has broken cannot "
                     "knit together again", "correct": False,
             "why": "Bone is living tissue with its own blood supply and it "
                    "repairs itself at any age. The danger is everything that "
                    "stops working while it does."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s03",
        "band": "standard",
        "text": "A tennis player's racket arm has measurably denser bone than "
                "their other arm. A student says they were simply born that "
                "way. What does the lesson say instead?",
        "options": [
            {"text": "Bone thickness is fixed at birth, so what is really "
                     "denser must be the muscle", "correct": False,
             "why": "Bone thickness is fixed at nothing. You rebuild about a "
                    "tenth of your skeleton every year, and where you rebuild "
                    "it depends on what you have been doing."},
            {"text": "Bone is living, and it lays down more material exactly "
                     "where the force goes", "correct": True},
            {"text": "The racket arm holds more marrow, and marrow is what "
                     "makes a bone dense", "correct": False,
             "why": "Two jobs mixed up. The marrow makes red blood cells; the "
                    "extra material in a hard-worked bone is bone, laid down "
                    "where the load is."},
            {"text": "That arm has been used more, so its bones have grown "
                     "longer than the other side", "correct": False,
             "why": "Denser, not longer. The bone added material where the "
                    "force went through it — it did not add length."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s04",
        "band": "standard",
        "text": "Two people break a bone on the same morning: one a finger, "
                "one a femur. Both will heal. Why is only one of them an "
                "emergency?",
        "options": [
            {"text": "The femur is a far bigger bone, and a bigger bone means "
                     "a bigger injury", "correct": False,
             "why": "Size is not what decides it. A rib is much smaller than a "
                    "femur, and breaking one makes every single breath hurt."},
            {"text": "A broken femur hurts far more, and pain is how you "
                     "measure a serious injury", "correct": False,
             "why": "Pain tells you something is wrong. It does not tell you "
                    "how much was depending on the part that broke, and that "
                    "is what decides how serious it is."},
            {"text": "The whole body above it rested on the femur, so standing "
                     "and walking stop", "correct": True},
            {"text": "The femur takes far longer to heal, and healing time is "
                     "what makes a break serious", "correct": False,
             "why": "Both bones heal. What differs is the pile of things that "
                    "stop working in the meantime — which comes back to the "
                    "job the bone was doing."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-01-h01",
        "band": "harder",
        "text": "A student writes: 'Bones cannot be alive, because they do not "
                "do anything — they just sit there while the muscles do the "
                "work.' Two separate things are wrong. Which option names "
                "both?",
        "options": [
            {"text": "Bones do move themselves, and they count as alive "
                     "because they are warm to the touch", "correct": False,
             "why": "Bones cannot contract — muscles pull them. And warmth is "
                    "not the evidence: bone has its own cells, its own blood "
                    "supply, and it heals."},
            {"text": "Bones are alive only while you are still growing, and "
                     "after that the muscles do everything", "correct": False,
             "why": "You replace roughly a tenth of your skeleton every year "
                    "for your whole life, long after you have stopped "
                    "growing."},
            {"text": "Bone rebuilds itself all your life, and muscles move "
                     "nothing without something rigid to pull on",
             "correct": True},
            {"text": "Blood flows past bone to keep it alive, and muscles are "
                     "attached to the skin rather than to bone", "correct": False,
             "why": "Bone has a blood supply running inside it, not merely "
                    "past it — and muscles pull on bone. That attachment is "
                    "why movement is a skeletal job at all."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h02",
        "band": "harder",
        "text": "A cancer treatment damages a patient's bone marrow. Their "
                "bones stay strong and unbroken. They feel fine for a few "
                "weeks, then grow steadily more breathless. Why the delay?",
        "options": [
            {"text": "The red blood cells they already had keep working, and "
                     "wear out after four months", "correct": True},
            {"text": "The damage spreads slowly outwards through the bone "
                     "before it ever reaches the blood", "correct": False,
             "why": "Nothing has to spread. From the moment the marrow stops, "
                    "no new red blood cells are made anywhere — the chain "
                    "leaves the bone at the very first step."},
            {"text": "The bones weaken first, so the chest cannot be lifted "
                     "and less air comes in", "correct": False,
             "why": "That is the ribcage's movement job, and here the bones "
                    "are strong and the chest wall is intact. This failure "
                    "is about what the blood can carry, not about how much "
                    "air gets in."},
            {"text": "The lungs take several weeks to stop loading oxygen onto "
                     "the blood", "correct": False,
             "why": "The lungs are untouched and load oxygen perfectly well. "
                    "The problem is that there are fewer and fewer red blood "
                    "cells for them to load it onto."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h03",
        "band": "harder",
        "text": "A helmet and a skull both shield a brain by taking the energy "
                "of an impact, and a crushed helmet is thrown away afterwards. "
                "What can the skull do that the helmet cannot?",
        "options": [
            {"text": "Spread the force so widely across itself that it is "
                     "never damaged at all", "correct": False,
             "why": "A hard enough impact fractures a skull. The difference is "
                    "not that it escapes damage — it is what happens to it "
                    "afterwards."},
            {"text": "Take an impact without any of the energy reaching the "
                     "brain underneath", "correct": False,
             "why": "Neither can promise that. Both work by taking energy so "
                    "that less of it reaches the brain, and a big enough "
                    "impact still gets through."},
            {"text": "Make new blood cells to replace the ones lost in the "
                     "injury", "correct": False,
             "why": "Two jobs mixed up. The marrow does make blood cells, but "
                    "that is not what mends a cracked bone — the bone's own "
                    "living cells do."},
            {"text": "Repair itself, because it is living tissue with its own "
                     "blood supply", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h04",
        "band": "harder",
        "text": "An engineer offers to replace a patient's whole femur and hip "
                "with carbon-fibre copies: same shape, same strength, muscles "
                "reattached. Which of the four jobs would that leg no longer "
                "do?",
        "options": [
            {"text": "Support, because only living bone can carry the weight "
                     "of a whole body", "correct": False,
             "why": "Rigidity is rigidity. A bar that is strong enough carries "
                    "the load whether it is alive or not, which is exactly why "
                    "the replacement is worth doing."},
            {"text": "Making blood cells, because there is no marrow inside a "
                     "carbon-fibre tube", "correct": True},
            {"text": "Movement, because a muscle can only pull on something "
                     "that is alive", "correct": False,
             "why": "A muscle needs something rigid, not something living. "
                    "Reattached to a rigid copy, the pull still straightens "
                    "the leg."},
            {"text": "None of them — a copy of the same shape and strength "
                     "does everything the bone did", "correct": False,
             "why": "That answer assumes holding you up is the whole job. The "
                    "one you cannot see from the outside is the one the copy "
                    "cannot do."},
        ],
        "figure": None,
    },
]
