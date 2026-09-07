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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-01-e05",
        "band": "easier",
        "text": "Which part of the skeleton shields the heart and the lungs, "
                "and does a second job at the same time?",
        "options": [
            {"text": "The ribcage — it shields them, and it swings up and "
                     "outwards to pull air in", "correct": True},
            {"text": "The skull — it is a fused box, and it also holds the "
                     "head upright", "correct": False,
             "why": "The skull is a box around the brain, and the heart and "
                    "lungs are nowhere near it. Holding the head up is done "
                    "by the bones of the neck."},
            {"text": "The femur and hip — they take the weight of the chest "
                     "and shield what is inside it", "correct": False,
             "why": "The femur carries load into the ground, and it sits in "
                    "the thigh. Nothing down there is shielding a heart."},
            {"text": "The marrow — it lies inside the ribs and protects them "
                     "from the inside", "correct": False,
             "why": "The marrow makes blood cells and protects nothing. What "
                    "shields the heart and lungs is the cage of bone built "
                    "around them."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e06",
        "band": "easier",
        "text": "Standing still, one bone carries the entire weight of "
                "everything above it into the ground. Which of the four jobs "
                "is that?",
        "options": [
            {"text": "Protection, because taking a load is a way of shielding "
                     "what sits above it", "correct": False,
             "why": "Protection means keeping an impact out, the way the "
                    "skull does. Carrying a load is a different job with a "
                    "different name."},
            {"text": "Movement, because the leg has to carry that weight "
                     "about all day", "correct": False,
             "why": "Movement is a muscle pulling on a rigid bar. This is the "
                    "bar standing still and not folding, which is support."},
            {"text": "Making blood cells, because the marrow inside that bone "
                     "is what takes the strain", "correct": False,
             "why": "Two jobs mixed up. The marrow makes red blood cells; the "
                    "bone around it is what carries the load."},
            {"text": "Support — a rigid bar, stacked in line, carrying the "
                     "load into the ground", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e07",
        "band": "easier",
        "text": "Respiration happens inside every living cell. What does it "
                "do?",
        "options": [
            {"text": "It takes oxygen in from the air and passes carbon "
                     "dioxide back out", "correct": False,
             "why": "That is breathing, which is how the oxygen arrives. "
                    "Respiration is what a cell does with it once it is "
                    "there."},
            {"text": "It releases the energy in food, which is what every "
                     "cell needs to work", "correct": True},
            {"text": "It makes new red blood cells to carry oxygen round the "
                     "body", "correct": False,
             "why": "That is the marrow's job. Respiration is a reaction "
                    "inside a cell, not a way of building cells."},
            {"text": "It repairs a bone after a break, using the blood supply "
                     "inside it", "correct": False,
             "why": "Bone does repair itself, but repair is not respiration. "
                    "Respiration is what releases the energy the repairing "
                    "cells run on."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e08",
        "band": "easier",
        "text": "Red blood cells wear out and are removed. Roughly how long "
                "does one of them last?",
        "options": [
            {"text": "About four days", "correct": False,
             "why": "Far too short. If they lasted days, a marrow that "
                    "stopped would leave someone in trouble within a week, "
                    "and it takes months."},
            {"text": "About four weeks", "correct": False,
             "why": "Still too short. The gap between a marrow failing and "
                    "the breathlessness starting is measured in months."},
            {"text": "About four months", "correct": True},
            {"text": "For the rest of your life, once they have been made",
             "correct": False,
             "why": "Then the marrow would have nothing left to do after "
                    "childhood. It makes about two million a second precisely "
                    "because the old ones keep wearing out."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e09",
        "band": "easier",
        "text": "A femur is a hollow tube rather than a solid rod. What is in "
                "the hollow space?",
        "options": [
            {"text": "Nothing — it is left empty so that the leg stays light",
             "correct": False,
             "why": "Being a tube is what keeps it light, and the space is "
                    "not wasted. The marrow is in there, making blood cells."},
            {"text": "Cartilage, which cushions the bone from the inside",
             "correct": False,
             "why": "Cartilage faces the ends of bones inside a joint. It is "
                    "not what fills the shaft."},
            {"text": "A core of softer bone, which stops the tube from "
                     "splitting", "correct": False,
             "why": "A bar loaded from the side is barely stressed down its "
                    "middle, so a core would add weight and almost no "
                    "strength."},
            {"text": "Bone marrow, the soft living tissue where new blood "
                     "cells are made", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e10",
        "band": "easier",
        "text": "Bone is rebuilt continuously. Roughly how much of your "
                "skeleton do you replace in a year?",
        "options": [
            {"text": "About a tenth of it", "correct": True},
            {"text": "None of it, once you have finished growing",
             "correct": False,
             "why": "Rebuilding never stops. It is going on in you now, and "
                    "it is one of the reasons bone counts as living tissue."},
            {"text": "All of it, several times over", "correct": False,
             "why": "Far too fast. At that rate a bone could not hold its "
                    "shape from one month to the next."},
            {"text": "Only the parts that have been broken", "correct": False,
             "why": "A break is repaired, but rebuilding happens everywhere "
                    "all the time, whether a bone has been damaged or not."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e11",
        "band": "easier",
        "text": "About how many new red blood cells does the marrow make "
                "every second?",
        "options": [
            {"text": "About two hundred", "correct": False,
             "why": "Far too few. At that rate it would take centuries to "
                    "replace the cells you lose in a single day."},
            {"text": "About two thousand", "correct": False,
             "why": "Still far too few — the real figure is a thousand times "
                    "bigger than this one."},
            {"text": "About two million", "correct": True},
            {"text": "About two billion", "correct": False,
             "why": "A thousand times too many. Two million a second is "
                    "already enough to replace the whole supply every few "
                    "months."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e12",
        "band": "easier",
        "text": "What does the word skeleton mean?",
        "options": [
            {"text": "The hard outer layer of a single bone, with the marrow "
                     "inside it", "correct": False,
             "why": "That describes one bone cut across. The skeleton is all "
                    "the bones together, working as one system."},
            {"text": "All the bones of the body, taken together as one "
                     "system", "correct": True},
            {"text": "The dry frame that is left behind after an animal has "
                     "died", "correct": False,
             "why": "That is a museum skeleton. The one you are sitting on is "
                    "living tissue doing four jobs at once."},
            {"text": "The bones, the muscles and the tendons, working as one "
                     "system", "correct": False,
             "why": "Muscles and tendons work with the skeleton, but they are "
                    "not part of it. The skeleton is the bones."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e13",
        "band": "easier",
        "text": "What does the word tissue mean?",
        "options": [
            {"text": "A group of similar cells working together to do one "
                     "job", "correct": True},
            {"text": "A group of organs working together to do one job",
             "correct": False,
             "why": "That is an organ system. A tissue sits below an organ, "
                    "and it is built from cells."},
            {"text": "A single cell that carries out one particular job on "
                     "its own", "correct": False,
             "why": "One cell is a cell. It takes a group of them, working "
                    "together, to make a tissue."},
            {"text": "The fluid that surrounds the cells of the body and "
                     "feeds them", "correct": False,
             "why": "A tissue is the cells themselves, not what is around "
                    "them. Bone is a tissue, and so is the marrow inside "
                    "it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-01-s05",
        "band": "standard",
        "text": "A broken finger is taped up and you carry on. A broken rib "
                "makes every single breath hurt. What is it about a rib that "
                "does that?",
        "options": [
            {"text": "A rib is a much bigger bone than a finger bone, and a "
                     "bigger bone means a worse injury", "correct": False,
             "why": "Size is not what decides it. A femur is far bigger than "
                    "a rib and breaking one does not make breathing painful."},
            {"text": "A rib sits close to the heart, so damage there is felt "
                     "more sharply than damage further out", "correct": False,
             "why": "Being near an organ is not the point. The pain arrives "
                    "with every breath because the rib itself has to move for "
                    "you to breathe."},
            {"text": "The ribcage has to swing up and outwards for every "
                     "breath, so a broken rib is moved thousands of times a "
                     "day", "correct": True},
            {"text": "Ribs hold far more marrow than finger bones do, so much "
                     "more is going wrong inside them", "correct": False,
             "why": "Ribs do hold marrow, but a marrow failure is silent and "
                    "slow. What hurts here is a broken bone being moved with "
                    "every breath."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s06",
        "band": "standard",
        "text": "Someone's leg is in a plaster cast for eight weeks. When it "
                "comes off, the bones of that leg are measurably thinner than "
                "the other leg's. Why?",
        "options": [
            {"text": "The marrow in that leg stopped working while the leg "
                     "was held still", "correct": False,
             "why": "Marrow does not depend on movement, and when it fails it "
                    "shows up in the blood rather than in the thickness of "
                    "the bone."},
            {"text": "Bone lays down material where force goes through it, "
                     "and the cast took the force away", "correct": True},
            {"text": "Bone is dead material, so it slowly decays wherever it "
                     "is not being used", "correct": False,
             "why": "Bone is living tissue. It has not decayed — it has been "
                    "rebuilt thinner, because nothing was demanding the extra "
                    "material."},
            {"text": "The muscles wasted away, and the bone shrank with them "
                     "because the two are attached", "correct": False,
             "why": "The muscles do waste, but they do not drag the bone "
                    "thinner. The bone thins because the load it used to "
                    "carry has gone."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s07",
        "band": "standard",
        "text": "A museum skeleton is dry bone with nothing living left in "
                "it. Which of the four jobs can you find no evidence of in it "
                "at all?",
        "options": [
            {"text": "Support, because dry bone has none of the strength it "
                     "needed to carry a body",
             "correct": False,
             "why": "Stand a museum skeleton up and it holds its own shape. "
                    "The shapes built for carrying load are all still there "
                    "to see."},
            {"text": "Protection, because the empty skull can no longer keep "
                     "anything out of the space inside", "correct": False,
             "why": "The fused box is still a fused box. What it was "
                    "protecting has gone, but the evidence of the job is in "
                    "the shape."},
            {"text": "Movement, because there are no muscles left anywhere on "
                     "it to pull the bones about", "correct": False,
             "why": "The attachment points remain — a heel bone marked where "
                    "a tendon sat well behind the ankle still tells you what "
                    "the pull was doing."},
            {"text": "Making blood cells, because the marrow that did it has "
                     "gone and left an empty tube", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s08",
        "band": "standard",
        "text": "A chest wall is so badly broken that it no longer holds its "
                "shape. The diaphragm still pulls down as normal. Why does "
                "far less air get into the lungs?",
        "options": [
            {"text": "Air only moves in when the chest gets bigger, and a "
                     "loose chest wall is pulled inwards instead",
             "correct": True},
            {"text": "The broken ribs press on the lungs and block the air "
                     "from getting past them", "correct": False,
             "why": "Nothing is blocked. The route in is clear; what has gone "
                    "is the increase in volume that draws air along it."},
            {"text": "The diaphragm is weakened by the injury, so its pull is "
                     "no longer strong enough", "correct": False,
             "why": "The diaphragm is untouched and pulls exactly as before. "
                    "The trouble is that the chest wall no longer holds out "
                    "against it."},
            {"text": "The ribs carry oxygen to the blood, so broken ribs "
                     "deliver less of it", "correct": False,
             "why": "Bone carries loads, not oxygen. The ribcage's part in "
                    "breathing is mechanical: it makes the chest bigger."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s09",
        "band": "standard",
        "text": "A femur is a hollow tube and a skull is a sealed box. What "
                "do those two shapes tell you about the jobs the two bones "
                "do?",
        "options": [
            {"text": "Both shapes are chosen to make the bone as light as it "
                     "possibly can be", "correct": False,
             "why": "Lightness matters for the tube, but a sealed box is not "
                    "the light option. It is the shape that keeps an impact "
                    "out."},
            {"text": "A tube carries a load along its length; a sealed box "
                     "keeps an impact out", "correct": True},
            {"text": "Both shapes exist to make room for marrow, which is "
                     "what a bone is really for", "correct": False,
             "why": "Only the tube holds marrow, and the skull's space is "
                    "full of brain. One shape is for load, the other for "
                    "protection."},
            {"text": "The tube is the protecting shape and the box is the "
                     "supporting one", "correct": False,
             "why": "The right two jobs, swapped over. A tube is a "
                    "load-carrying shape, and a box with almost no holes in "
                    "it is a shielding one."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s10",
        "band": "standard",
        "text": "Someone whose marrow has stopped working is given extra "
                "oxygen through a mask, and it helps very little. Their lungs "
                "are healthy. Why?",
        "options": [
            {"text": "The oxygen cannot reach the lungs at all while the "
                     "marrow is damaged", "correct": False,
             "why": "It reaches the lungs perfectly well. The problem starts "
                    "after that, when the blood has to carry it away."},
            {"text": "Their bones have weakened, so the chest cannot be "
                     "lifted to take the oxygen in", "correct": False,
             "why": "That is the ribcage's failure, and here the chest is "
                    "intact. This one is about what the blood can carry."},
            {"text": "There are too few red blood cells to carry the oxygen, "
                     "however much of it arrives", "correct": True},
            {"text": "Oxygen is only useful once the marrow has turned it "
                     "into red blood cells", "correct": False,
             "why": "The marrow makes the cells; it does not turn oxygen into "
                    "anything. The cells are the carriers, and there are not "
                    "enough of them."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s11",
        "band": "standard",
        "text": "A sprinter's calf muscle pulls on a tendon fixed to the heel "
                "bone, well behind the ankle. What would happen if that heel "
                "bone were soft rather than rigid?",
        "options": [
            {"text": "The pull would be bigger, because a soft bone gives the "
                     "tendon further to travel", "correct": False,
             "why": "Softness does not hand out extra distance. A pull that "
                    "bends what it is attached to moves nothing at the far "
                    "end."},
            {"text": "Nothing would change, because it is the muscle that "
                     "does all of the work", "correct": False,
             "why": "The muscle would contract exactly as before. Without a "
                    "rigid bar to pull against, that contraction moves "
                    "nothing."},
            {"text": "The muscle would push instead of pulling, to make up "
                     "for the missing stiffness", "correct": False,
             "why": "No muscle can push. It shortens, and shortening only "
                    "ever pulls."},
            {"text": "The muscle would still contract, but the pull would "
                     "bend the heel rather than lift the body", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s12",
        "band": "standard",
        "text": "A collarbone is the strut holding the shoulder out from the "
                "chest. Someone breaks one. They walk perfectly well but "
                "cannot lift that arm out to the side. Why not?",
        "options": [
            {"text": "The muscles still pull, but the rigid strut they were "
                     "pulling against has gone", "correct": True},
            {"text": "The muscles of that shoulder are torn whenever a "
                     "collarbone breaks", "correct": False,
             "why": "The muscles are intact and contracting. What is missing "
                    "is something rigid for them to work against."},
            {"text": "The marrow in the collarbone has stopped, so the arm "
                     "has lost its blood supply", "correct": False,
             "why": "One bone's marrow is not the arm's blood supply, and "
                    "marrow failure takes months. This happened the moment "
                    "the bone gave way."},
            {"text": "The collarbone carried the weight of the arm, and that "
                     "weight is now too much to lift", "correct": False,
             "why": "The arm has not got heavier. The problem is not weight "
                    "at all — it is that the muscles have nothing to pull "
                    "on."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s13",
        "band": "standard",
        "text": "A patient whose marrow has stopped is given a transfusion of "
                "donated red blood cells. It works, but it has to be repeated "
                "every few weeks. Why is it not a cure?",
        "options": [
            {"text": "The donated cells are rejected by the body within a few "
                     "weeks of arriving", "correct": False,
             "why": "Matched cells are not thrown out. They simply wear out, "
                    "in the same way anybody's do."},
            {"text": "The donated cells wear out too, and the patient's own "
                     "marrow is still making none", "correct": True},
            {"text": "A transfusion cannot reach the bones, so the marrow is "
                     "never repaired by it", "correct": False,
             "why": "A transfusion is not aimed at the marrow at all. It "
                    "replaces the cells the marrow would have made, and only "
                    "for as long as those cells last."},
            {"text": "Donated cells carry less oxygen than the patient's own "
                     "cells would have done", "correct": False,
             "why": "They carry oxygen perfectly well. The trouble is that "
                    "nothing is replacing them once they wear out."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-01-h05",
        "band": "harder",
        "text": "A student suggests filling in the hollow middle of the femur "
                "with solid bone, to make the leg stronger. Name the two "
                "things wrong with that.",
        "options": [
            {"text": "The leg would be too heavy to lift, and bone cannot be "
                     "added once you have stopped growing", "correct": False,
             "why": "Bone is added and removed all your life. And weight is "
                    "only half the objection — the bigger half is what the "
                    "space is for."},
            {"text": "There would be nowhere left for the cartilage, and the "
                     "bone would grind at the hip", "correct": False,
             "why": "Cartilage faces the ends of bones inside a joint, not "
                    "the hollow of the shaft. Nothing in the middle of a "
                    "femur is a joint surface."},
            {"text": "It would add weight for almost no strength, and it "
                     "would fill the space where blood is made",
             "correct": True},
            {"text": "The bone could no longer bend at all, and a femur has "
                     "to bend a little to take weight", "correct": False,
             "why": "A femur is meant to be rigid, and bending is not one of "
                    "its jobs. The real costs are weight and the loss of the "
                    "marrow space."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h06",
        "band": "harder",
        "text": "A student says making blood cells is the least important of "
                "the four jobs, because you cannot see it and its failure "
                "takes months. What is the strongest argument against?",
        "options": [
            {"text": "It is the most important of the four, because blood "
                     "reaches every cell in the body", "correct": False,
             "why": "Ranking them the other way round is the same mistake. "
                    "All four end in the same place, so none of them is "
                    "spare."},
            {"text": "Its failure is fast, not slow — a damaged marrow leaves "
                     "someone breathless within days", "correct": False,
             "why": "It genuinely is slow, because the red blood cells they "
                    "already have last about four months. Slow is not the "
                    "same as survivable."},
            {"text": "You can see it, because the marrow is what makes a bone "
                     "look thick on an X-ray", "correct": False,
             "why": "The marrow is the soft middle; the thickness on an X-ray "
                    "is the bone around it. Being invisible would not make a "
                    "job unimportant in any case."},
            {"text": "Its chain ends exactly where the ribcage's does — every "
                     "cell in the body short of oxygen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h07",
        "band": "harder",
        "text": "\"The skeleton's job is holding you up; the other things "
                "bones do are extras.\" Use the ribcage on its own to show "
                "that this is wrong.",
        "options": [
            {"text": "The ribcage holds nothing up, and without its movement "
                     "each breath brings in far too little air",
             "correct": True},
            {"text": "The ribcage holds the chest up, so it is doing exactly "
                     "the job the student describes", "correct": False,
             "why": "Nothing rests on the ribcage. The weight of the body "
                    "above it travels down the spine, while the ribs are busy "
                    "with two other jobs."},
            {"text": "The ribcage makes blood cells, and that matters more "
                     "than holding anything up", "correct": False,
             "why": "Ribs do hold marrow, but that failure takes months. The "
                    "fastest thing the ribcage does is move air — and holding "
                    "you up is not on its list at all."},
            {"text": "The ribcage protects the heart, and protecting is a "
                     "kind of holding up", "correct": False,
             "why": "Protection and support are different jobs with different "
                    "shapes. Calling one a version of the other is the "
                    "student's mistake, not the answer to it."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h08",
        "band": "harder",
        "text": "A student cuts a bone open, finds the middle soft rather "
                "than hard, and concludes that the middle of a bone must be "
                "dead. What have they actually found?",
        "options": [
            {"text": "Cartilage, which is soft because it is fed by fluid "
                     "rather than by blood", "correct": False,
             "why": "Cartilage sits on the ends of a bone, inside a joint. It "
                    "is not what fills the shaft."},
            {"text": "The marrow — the busiest living tissue in the bone, "
                     "making about two million cells a second",
             "correct": True},
            {"text": "Old bone that has not been rebuilt yet, which is why it "
                     "has gone soft", "correct": False,
             "why": "Rebuilding replaces bone with bone; it does not leave a "
                    "soft middle behind. What is in there is marrow, and it "
                    "is meant to be soft."},
            {"text": "The blood supply, which is soft because it is liquid "
                     "all the way through", "correct": False,
             "why": "Bone does have a blood supply running inside it, but the "
                    "soft middle is a tissue rather than a pool of blood."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h09",
        "band": "harder",
        "text": "Two people arrive at a hospital. One has a fractured skull "
                "and feels fine. One has a fractured finger and is in agony. "
                "Which is watched more closely overnight, and why?",
        "options": [
            {"text": "The finger, because pain is the body's own measure of "
                     "how serious an injury is", "correct": False,
             "why": "Pain tells you something is wrong. It does not tell you "
                    "what was depending on the bone that broke."},
            {"text": "The finger, because a smaller bone heals faster and the "
                     "patient can be sent home sooner", "correct": False,
             "why": "Healing time is not the question here. The skull is "
                    "watched for what may happen next, not for how long it "
                    "takes to knit."},
            {"text": "The skull, because protection is the job where nothing "
                     "happens until it fails, and then everything does",
             "correct": True},
            {"text": "The skull, because a bigger bone means a bigger injury "
                     "and a longer recovery", "correct": False,
             "why": "Size is not what decides it. What makes the skull the "
                    "worry is the brain underneath and damage that does not "
                    "show yet."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h10",
        "band": "harder",
        "text": "Switch the femur off and the chain still ends at cells with "
                "nothing to respire — but after days rather than minutes. "
                "What is happening during those days?",
        "options": [
            {"text": "The marrow inside the femur runs down, and the blood "
                     "slowly carries less oxygen", "correct": False,
             "why": "That is the marrow's chain, and it takes months. The "
                    "femur's chain leaves the leg long before it reaches the "
                    "blood."},
            {"text": "The leg muscles use up the last of their own store of "
                     "oxygen before they fail", "correct": False,
             "why": "There is no store that lasts days. What runs out is not "
                    "oxygen in the leg but the ability to reach food at all."},
            {"text": "The bone dies without the load it used to carry, and "
                     "the damage spreads outwards from it", "correct": False,
             "why": "Bone thins when it is not loaded; it does not die and "
                    "spread. This chain leaves the bone at the first step, "
                    "when the leg stops working."},
            {"text": "No standing and no walking means no route to food, so "
                     "the cells run out of what they respire",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h11",
        "band": "harder",
        "text": "One bone does three of the four jobs at the same time. Which "
                "bone, and which three?",
        "options": [
            {"text": "The femur — it supports the body, muscles pull on it to "
                     "move the leg, and its marrow makes blood cells",
             "correct": True},
            {"text": "The skull — it protects the brain, holds the head up, "
                     "and its plates move to let the head turn",
             "correct": False,
             "why": "The plates of an adult skull are fused solid and nothing "
                    "slides. It does protection; the bones of the neck hold "
                    "the head up."},
            {"text": "The ribcage — it protects the heart, moves air in, and "
                     "carries the weight of the chest", "correct": False,
             "why": "It does protect and it does move, but nothing rests on "
                    "the ribcage. The weight above it travels down the "
                    "spine."},
            {"text": "A finger bone — it supports the hand, muscles pull on "
                     "it, and it shields the nerves inside it",
             "correct": False,
             "why": "Muscles do pull on it, but a finger holds nothing up and "
                    "shields nothing. The nerves of the hand do not run "
                    "inside the bone."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h12",
        "band": "harder",
        "text": "A hip replacement puts a metal stem inside the femur so that "
                "the metal, not the bone, carries the load. Over the years "
                "the bone around the stem grows thinner. Explain why.",
        "options": [
            {"text": "The metal wears the bone away wherever the two are in "
                     "contact", "correct": False,
             "why": "The stem is fixed in place rather than grinding. The "
                    "thinning is not wear — it is bone being rebuilt "
                    "thinner."},
            {"text": "Bone lays down material where force goes, and the stem "
                     "has taken the force away from it", "correct": True},
            {"text": "The bone is dead once the stem is fitted, so from then "
                     "on it slowly decays", "correct": False,
             "why": "The bone is alive and rebuilding as usual, which is "
                    "exactly why it responds to having its load removed."},
            {"text": "The marrow is displaced by the stem, so there is less "
                     "material left to make bone with", "correct": False,
             "why": "The marrow makes blood cells, not bone. The bone around "
                    "the stem thins because it is no longer being loaded."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h13",
        "band": "harder",
        "text": "\"Switch off any part of the skeleton and the damage ends at "
                "cells with no oxygen.\" A student says that means all four "
                "failures are really one failure. What is the best reply?",
        "options": [
            {"text": "They are one failure, and the four names are just "
                     "different ways of describing it", "correct": False,
             "why": "One destination is not one failure. The four take "
                    "different routes over very different times, and "
                    "treatment has to meet the route."},
            {"text": "They are four failures, because each one ends at a "
                     "different kind of cell", "correct": False,
             "why": "All four finish at cells short of oxygen, and there is "
                    "nothing special about which ones. The difference lies in "
                    "how they get there."},
            {"text": "Same destination, four different routes — and one takes "
                     "minutes while another takes months", "correct": True},
            {"text": "Only two of them really end there; the skull's and the "
                     "femur's stop before they reach the cells",
             "correct": False,
             "why": "All four reach cells. The skull's damage ends at nerve "
                    "cells, and the femur's at cells that can no longer be "
                    "fed."},
        ],
        "figure": None,
    },
]
