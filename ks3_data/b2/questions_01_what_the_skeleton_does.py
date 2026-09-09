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
            {"text": "Nothing — the shaft is left hollow and empty to keep "
                     "the leg light",
             "correct": False,
             "why": "Being a tube is what keeps it light, and the space is "
                    "not wasted. The marrow is in there, making blood cells."},
            {"text": "Cartilage, which cushions the bone from the inside",
             "correct": False,
             "why": "Cartilage faces the ends of bones inside a joint. It is "
                    "not what fills the shaft."},
            {"text": "A core of softer spongy bone, which stops the hollow "
                     "tube from splitting open", "correct": False,
             "why": "A bar loaded from the side is barely stressed down its "
                    "middle, so a core would add weight and almost no "
                    "strength."},
            {"text": "Bone marrow, the soft living tissue that makes blood "
                     "cells", "correct": True},
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
            {"text": "A rib sits close to the heart, so damage in the ribcage "
                     "is felt more sharply than damage further out",
             "correct": False,
             "why": "Being near an organ is not the point. The pain arrives "
                    "with every breath because the rib itself has to move for "
                    "you to breathe."},
            {"text": "Every breath moves the ribcage, so the broken rib is "
                     "disturbed constantly", "correct": True},
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
            {"text": "Air only moves in when the chest gets bigger, and this "
                     "one is pulled inwards", "correct": True},
            {"text": "The broken ribs press inwards on the lungs and block "
                     "the air getting past them to the airways",
             "correct": False,
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
            {"text": "The pull would be bigger, because a soft bone gives way "
                     "and lets the tendon travel further", "correct": False,
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
            {"text": "The muscle would still pull, but it would bend the "
                     "heel, not lift you", "correct": True},
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
            {"text": "The ribcage holds nothing up, yet each breath depends "
                     "on it moving", "correct": True},
            {"text": "The ribcage holds the whole chest up, so it is doing "
                     "exactly the job the student describes", "correct": False,
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
            {"text": "Cartilage, which is soft because joint fluid rather "
                     "than blood seeps in to feed it", "correct": False,
             "why": "Cartilage sits on the ends of a bone, inside a joint. It "
                    "is not what fills the shaft."},
            {"text": "The marrow — living tissue making two million cells a "
                     "second", "correct": True},
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
            {"text": "The skull, because with protection nothing shows until "
                     "it fails", "correct": True},
            {"text": "The skull, because a bigger bone means a bigger injury, "
                     "more bleeding inside and a longer recovery",
             "correct": False,
             "why": "Size is not what decides it, and a skull fracture need "
                    "not bleed heavily to be dangerous. What makes the skull "
                    "the worry is the brain underneath and damage that does "
                    "not show yet."},
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

    # ══ MRB-338 expansion ══════════════════════════════════════════════
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-01-e14",
        "band": "easier",
        "text": "The vertebrae are a chain of small bones running down your "
                "back. Which part of the body do they shield?",
        "options": [
            {"text": "The heart and the lungs, which sit in the chest in front "
                     "of them", "correct": False,
             "why": "The heart and lungs are caged by the ribs. The vertebrae "
                    "are behind them, and what runs through the vertebrae is "
                    "the spinal cord."},
            {"text": "The brain, which is joined onto the top of the spinal "
                     "column", "correct": False,
             "why": "The brain sits inside the cranium. The spine begins below "
                    "it and shields the cord that leaves it."},
            {"text": "The spinal cord, which threads down a tunnel through "
                     "them", "correct": True},
            {"text": "The bladder and the intestines, low down in the "
                     "body", "correct": False,
             "why": "Those sit inside the bowl of the pelvis, much lower down "
                    "and further forward than the vertebrae."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e15",
        "band": "easier",
        "text": "The pelvis is a broad bowl of bone at the base of the body. "
                "Which organs sit inside that bowl?",
        "options": [
            {"text": "The lungs, which need a rigid case around them to "
                     "work", "correct": False,
             "why": "The lungs sit high in the chest, inside the ribcage. "
                    "Nothing in the pelvis is anywhere near them."},
            {"text": "The brain, which is the softest organ in the whole "
                     "body", "correct": False,
             "why": "The brain is shielded by the cranium at the top of the "
                    "body. The pelvis is at the bottom of it."},
            {"text": "The bladder and the lower part of the "
                     "intestines", "correct": True},
            {"text": "The spinal cord, which runs down through the middle of "
                     "the back", "correct": False,
             "why": "The spinal cord runs through a tunnel in the vertebrae "
                    "and ends above the pelvis."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e16",
        "band": "easier",
        "text": "Which bone of the skeleton is the case around the brain?",
        "options": [
            {"text": "The sternum, the flat bone down the front of the "
                     "chest", "correct": False,
             "why": "The sternum is the breastbone. The ribs join onto it, and "
                    "it shields the chest rather than the head."},
            {"text": "The vertebrae, the chain of bones running all the way "
                     "down the back", "correct": False,
             "why": "The vertebrae shield the spinal cord. The brain sits "
                    "above them, inside the cranium."},
            {"text": "The cranium, the domed box at the top of the "
                     "skeleton", "correct": True},
            {"text": "The scapula, the flat blade at the back of the "
                     "shoulder", "correct": False,
             "why": "The scapula is the shoulder blade. Muscles anchor to it, "
                    "and it shields nothing at the head."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e17",
        "band": "easier",
        "text": "Where in the body is the femur, and what is it usually "
                "called?",
        "options": [
            {"text": "In the upper arm, and it is called the arm "
                     "bone", "correct": False,
             "why": "The bone of the upper arm is the humerus. The femur is in "
                    "the leg."},
            {"text": "In the thigh, and it is called the thigh "
                     "bone", "correct": True},
            {"text": "In the lower leg, and it is called the shin "
                     "bone", "correct": False,
             "why": "The shin bone is the tibia. The femur is above the knee, "
                    "not below it."},
            {"text": "In the chest, and it is called the "
                     "breastbone", "correct": False,
             "why": "The breastbone is the sternum. The femur is the long bone "
                    "of the thigh."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e18",
        "band": "easier",
        "text": "Which of these pairs a bone correctly with its everyday name?",
        "options": [
            {"text": "Scapula — the breastbone, down the front of the "
                     "chest", "correct": False,
             "why": "The scapula is the shoulder blade. The breastbone is the "
                    "sternum."},
            {"text": "Sternum — the long bone of the upper "
                     "arm", "correct": False,
             "why": "The bone of the upper arm is the humerus. The sternum is "
                    "the breastbone."},
            {"text": "Cranium — the bowl of bone at the base of the "
                     "body", "correct": False,
             "why": "That bowl is the pelvis. The cranium is the box around "
                    "the brain."},
            {"text": "Patella — the kneecap, at the front of the "
                     "knee", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e19",
        "band": "easier",
        "text": "About how many bones are there in an adult human skeleton?",
        "options": [
            {"text": "About 20, because only the big limb bones are "
                     "counted", "correct": False,
             "why": "There are more than twenty in one hand alone. The adult "
                    "total is a little over two hundred."},
            {"text": "About 60, one for each part of the body you can "
                     "name", "correct": False,
             "why": "Still far too few. The spine on its own is built from "
                    "more than thirty separate bones."},
            {"text": "About 2000, because each bone is really built from many "
                     "smaller ones", "correct": False,
             "why": "A bone is one piece of tissue, not a stack of little "
                    "bones. The adult total is around 206."},
            {"text": "About 206, from the cranium down to the bones of the "
                     "toes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e20",
        "band": "easier",
        "text": "A newborn baby has about 300 bones and an adult has about "
                "206. What has happened in between?",
        "options": [
            {"text": "Separate bones have grown together into single "
                     "bones", "correct": True},
            {"text": "Bones have worn away and been lost as the child moved "
                     "about", "correct": False,
             "why": "Nothing is lost. Bone grows stronger where it is used, "
                    "and it does not wear away to nothing."},
            {"text": "The baby's count includes the teeth, which an adult's "
                     "leaves out", "correct": False,
             "why": "Teeth are not bones and are in neither count. The drop "
                    "comes from bones fusing together."},
            {"text": "Some bones have dissolved, because a baby takes in very "
                     "little calcium", "correct": False,
             "why": "The drop happens in every healthy child, whatever they "
                    "eat. Separate bones simply join up."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e21",
        "band": "easier",
        "text": "Which mineral does the body need from food to keep bone hard "
                "and strong?",
        "options": [
            {"text": "Iron, which the body uses to build the hard part of "
                     "bone", "correct": False,
             "why": "Iron is needed for the red blood cells the marrow turns "
                    "out, not for hardening the bone around them."},
            {"text": "Calcium, which is laid down in bone and makes it "
                     "hard", "correct": True},
            {"text": "Sodium, which the body takes in as ordinary table "
                     "salt", "correct": False,
             "why": "Salt plays no part in hardening bone. The mineral bone is "
                    "built with is calcium."},
            {"text": "Carbon, which every living thing is largely built "
                     "from", "correct": False,
             "why": "Carbon is in every tissue you have. What makes bone "
                    "specifically hard is calcium."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e22",
        "band": "easier",
        "text": "Which of these meals gives the best supply of the mineral "
                "that hardens bone?",
        "options": [
            {"text": "Milk, cheese and yoghurt, with green leafy "
                     "vegetables", "correct": True},
            {"text": "Rice, pasta and bread, which are all rich in starch and "
                     "energy", "correct": False,
             "why": "Starchy foods are a good energy supply, but they carry "
                    "very little calcium."},
            {"text": "Fruit juice and sweets, which are both rich in sugar and "
                     "quick energy", "correct": False,
             "why": "Sugars release energy quickly and supply almost no "
                    "calcium at all."},
            {"text": "Chicken and eggs, which are both rich in "
                     "protein", "correct": False,
             "why": "Protein is needed for growth and repair, but dairy and "
                    "leafy greens carry far more calcium."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e23",
        "band": "easier",
        "text": "Where in the body is bone marrow found?",
        "options": [
            {"text": "In a layer just under the skin, all over the "
                     "body", "correct": False,
             "why": "Marrow is sealed inside bone. There is none of it "
                    "anywhere under the skin."},
            {"text": "In the gaps where one bone meets the next "
                     "one", "correct": False,
             "why": "Marrow sits in the hollow shaft of a bone, not in the "
                    "spaces between bones."},
            {"text": "In the soft hollow middle of the bigger "
                     "bones", "correct": True},
            {"text": "In the hard outer wall of every bone in the "
                     "body", "correct": False,
             "why": "The outer wall is the hard part that carries load. Marrow "
                    "is the soft tissue it surrounds."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e24",
        "band": "easier",
        "text": "What does bone marrow make?",
        "options": [
            {"text": "New bone, which is how a broken bone knits itself back "
                     "together again", "correct": False,
             "why": "Repair is done by the bone's own living cells. What the "
                    "marrow turns out is blood cells."},
            {"text": "New blood cells, which are then carried away in the "
                     "blood", "correct": True},
            {"text": "The energy that a cell needs, released from the food you "
                     "eat", "correct": False,
             "why": "That is respiration, and it happens inside every cell in "
                    "the body. Marrow makes cells."},
            {"text": "The calcium that the body lays down to harden "
                     "bone", "correct": False,
             "why": "Calcium comes in through the diet. Marrow does not make "
                    "minerals, it makes cells."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e25",
        "band": "easier",
        "text": "Bone has its own blood supply running inside it. What does "
                "that blood deliver to the bone's cells?",
        "options": [
            {"text": "Calcium only, because calcium is all that a bone is made "
                     "out of", "correct": False,
             "why": "Blood does carry calcium, but bone cells need oxygen and "
                    "food like any other living cell."},
            {"text": "Oxygen and food, so those cells can respire and "
                     "work", "correct": True},
            {"text": "Nothing — the blood is only passing through to the "
                     "marrow", "correct": False,
             "why": "Bone is built from living cells, and a living cell has to "
                    "be supplied wherever it sits."},
            {"text": "Air, which is pumped along the hollow middle of the "
                     "bone", "correct": False,
             "why": "No air is pumped anywhere inside you. Oxygen travels in "
                    "the blood, carried by red blood cells."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e26",
        "band": "easier",
        "text": "A student says that cartilage is just soft bone. Why is that "
                "wrong?",
        "options": [
            {"text": "Cartilage is a tissue of its own, not a softer version "
                     "of bone", "correct": True},
            {"text": "Cartilage is soft bone, but only in children — in adults "
                     "it hardens", "correct": False,
             "why": "Adults keep cartilage for life, in the ears and the nose "
                    "among other places. It is its own tissue."},
            {"text": "Cartilage is not a tissue at all, because it is really a "
                     "fluid", "correct": False,
             "why": "Cartilage is firm and holds its shape. A fluid would "
                    "simply flow away from where it was needed."},
            {"text": "Cartilage is bone that has gone soft because it was "
                     "never used", "correct": False,
             "why": "Bone does thin where it is not loaded, but it never turns "
                    "into cartilage. They are separate tissues."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e27",
        "band": "easier",
        "text": "Much of a newborn baby's skeleton is cartilage rather than "
                "bone. What happens to it as the child grows?",
        "options": [
            {"text": "It stays exactly as it is, and new bones grow up around "
                     "it", "correct": False,
             "why": "The cartilage itself is replaced. The skeleton a child "
                    "ends up with is very largely bone."},
            {"text": "It dries out and is absorbed, leaving the skeleton "
                     "hollow", "correct": False,
             "why": "Nothing is left hollow by it. Bone tissue takes the "
                    "cartilage's place as the child grows."},
            {"text": "It hardens into a tougher cartilage, and that is what "
                     "bone really is", "correct": False,
             "why": "Bone is not a tough kind of cartilage. They are two "
                    "different tissues, and one replaces the other."},
            {"text": "It is gradually replaced by bone, and the skeleton "
                     "hardens", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e28",
        "band": "easier",
        "text": "A jellyfish has no skeleton at all. Which of these is it "
                "therefore unable to do?",
        "options": [
            {"text": "Move any part of its body, in water or out of "
                     "it", "correct": False,
             "why": "It swims perfectly well by squeezing its bell. What it "
                    "cannot do is hold a shape out of water."},
            {"text": "Grow larger than a few millimetres across, at any "
                     "depth", "correct": False,
             "why": "Some grow more than a metre across. The water supports "
                    "them, so size in the sea is not the problem."},
            {"text": "Hold its own shape once it is out of the "
                     "water", "correct": True},
            {"text": "Take in any food at all, or get rid of its "
                     "waste", "correct": False,
             "why": "Feeding and waste have nothing to do with a skeleton. The "
                    "limit is holding a shape out of water."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e29",
        "band": "easier",
        "text": "An insect's skeleton is a hard case on the outside of its "
                "body. What is that kind of skeleton called?",
        "options": [
            {"text": "A hydrostatic skeleton, because it is filled with "
                     "fluid", "correct": False,
             "why": "A hydrostatic skeleton is fluid held under pressure, as "
                    "in an earthworm. An insect's case is hard and dry."},
            {"text": "An endoskeleton, which is the same kind of skeleton you "
                     "have", "correct": False,
             "why": "Endo means inside. Yours is inside you; an insect's is "
                    "the case wrapped around it."},
            {"text": "A cartilage skeleton, because it is not made out of "
                     "bone", "correct": False,
             "why": "Not being bone does not make something cartilage. A "
                    "skeleton on the outside is an exoskeleton."},
            {"text": "An exoskeleton, because it is on the outside of the "
                     "animal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e30",
        "band": "easier",
        "text": "An earthworm has no hard parts anywhere in its body, yet it "
                "pushes through soil. What do its muscles squeeze against?",
        "options": [
            {"text": "A row of tiny bones running along its "
                     "back", "correct": False,
             "why": "There are no bones anywhere in an earthworm. What its "
                    "muscles squeeze is the fluid held inside it."},
            {"text": "Fluid held under pressure inside its "
                     "body", "correct": True},
            {"text": "A hard case wrapped around the outside of its "
                     "body", "correct": False,
             "why": "That is an insect's exoskeleton. An earthworm has no hard "
                    "parts on the outside or the inside."},
            {"text": "Nothing at all — the soil pulls the worm along as it "
                     "moves", "correct": False,
             "why": "Soil does not pull anything along. The worm squeezes the "
                    "fluid inside it and drives itself forward."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e31",
        "band": "easier",
        "text": "Muscles pull, but a pull on its own moves nothing. What does "
                "the skeleton give a muscle so that movement happens?",
        "options": [
            {"text": "The energy for the pull, which is stored up inside the "
                     "bone itself", "correct": False,
             "why": "That energy comes from respiration inside the muscle's "
                    "own cells. Bone supplies rigidity, not energy."},
            {"text": "The signal that tells the muscle the moment to "
                     "contract", "correct": False,
             "why": "That signal arrives along a nerve. What bone supplies is "
                    "a rigid part to pull on."},
            {"text": "Something rigid to pull against, so the pull becomes "
                     "movement", "correct": True},
            {"text": "Extra length, because bone stretches when a muscle pulls "
                     "on it", "correct": False,
             "why": "Bone does not stretch at all. Being rigid is exactly what "
                    "makes it useful to a muscle."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-e32",
        "band": "easier",
        "text": "Why is the skeleton built from many separate bones rather "
                "than one solid piece?",
        "options": [
            {"text": "So that a break in one bone can spread safely to the "
                     "others", "correct": False,
             "why": "Damage spreading would be a disadvantage, not a design. "
                    "Separate bones are what allow movement."},
            {"text": "So that the whole thing weighs less than one piece "
                     "would", "correct": False,
             "why": "Weight is saved by hollow shafts, not by cutting the "
                    "frame into pieces. The reason is movement."},
            {"text": "So that there is somewhere for the marrow to be "
                     "stored", "correct": False,
             "why": "Marrow sits in the hollow middle of a bone, and a single "
                    "piece could have a hollow too."},
            {"text": "So that parts of it can move relative to each "
                     "other", "correct": True},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-01-s14",
        "band": "standard",
        "text": "Someone damages a vertebra low in their back. Explain why the "
                "trouble that follows can show up in the legs.",
        "options": [
            {"text": "The vertebrae carry the weight of the legs, so the legs "
                     "have lost the support they stood on", "correct": False,
             "why": "The legs carry the body, not the other way round. What "
                    "the vertebrae carry through them is the spinal cord."},
            {"text": "The marrow in the vertebrae supplies blood to the legs "
                     "and to nothing else", "correct": False,
             "why": "Marrow makes blood cells for the whole body, and blood "
                    "reaches the legs through arteries wherever it was made."},
            {"text": "The spinal cord threads through the vertebrae, and the "
                     "signals that reach the legs travel along "
                     "it", "correct": True},
            {"text": "The leg muscles are anchored to the vertebrae, so their "
                     "pull can no longer reach the leg", "correct": False,
             "why": "Leg muscles anchor to the pelvis and to the leg bones. "
                    "What the back carries down to the legs is the cord."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s15",
        "band": "standard",
        "text": "The pelvis is shaped as a bowl rather than a flat plate. Give "
                "one thing that shape does which a flat plate could not.",
        "options": [
            {"text": "It holds far more marrow than any other bone in the "
                     "body, because of all the space inside "
                     "it", "correct": False,
             "why": "The hollow of the pelvis is filled by organs, not by "
                    "marrow. Its shape is about surrounding them."},
            {"text": "It curves round the organs low in the body, shielding "
                     "them from the sides as well as from "
                     "below", "correct": True},
            {"text": "It stretches as the body moves, which a flat plate of "
                     "bone could never do", "correct": False,
             "why": "Bone does not stretch, whatever shape it has been built "
                    "into. The bowl surrounds and shields."},
            {"text": "It makes blood cells, which a flat plate of bone would "
                     "have no room to do", "correct": False,
             "why": "Flat bones hold marrow too — the sternum is one of them. "
                    "The bowl shape is about what it can surround."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s16",
        "band": "standard",
        "text": "The ribs are curved bars with gaps between them rather than "
                "one continuous plate of bone. Why is that the better design?",
        "options": [
            {"text": "Bars with gaps can swing up and outwards, so the cage "
                     "shields and still moves", "correct": True},
            {"text": "Bars with gaps use less calcium than a solid plate, so "
                     "less has to come in from food", "correct": False,
             "why": "The saving is real but tiny. The gaps are there because "
                    "the cage has to change shape with every breath."},
            {"text": "Bars with gaps let air pass straight through the chest "
                     "wall to the lungs", "correct": False,
             "why": "Air reaches the lungs along the windpipe. Nothing enters "
                    "through the wall of the chest."},
            {"text": "Bars with gaps leave room for marrow that a solid plate "
                     "would squeeze out", "correct": False,
             "why": "Marrow sits inside each rib itself. The gaps between the "
                    "ribs are what let the cage change shape."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s17",
        "band": "standard",
        "text": "A textbook says a child has more bones than their parent, and "
                "yet the child has lost none. Explain how both can be true.",
        "options": [
            {"text": "Separate bones grow together into single bones, so the "
                     "count falls without anything being "
                     "lost", "correct": True},
            {"text": "The child's bones are smaller, and small bones are left "
                     "out of the adult count", "correct": False,
             "why": "Size does not decide what gets counted. The count falls "
                    "because separate bones fuse into one."},
            {"text": "The parent's bones have slowly worn down over the years "
                     "until some of them have disappeared", "correct": False,
             "why": "Bone is rebuilt continuously throughout life. None of it "
                    "wears away to nothing."},
            {"text": "The child's count includes cartilage, which is counted "
                     "as bone until it hardens", "correct": False,
             "why": "Cartilage is not counted as bone at any age. The drop "
                    "comes from bones fusing together."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s18",
        "band": "standard",
        "text": "Two people eat the same amount of food, but one takes in far "
                "less calcium. Predict the difference in their skeletons over "
                "several years.",
        "options": [
            {"text": "The one taking in less makes fewer red blood cells, "
                     "because calcium is what the marrow builds them "
                     "from", "correct": False,
             "why": "The marrow builds blood cells and calcium hardens bone. "
                    "Two different jobs going on in the same bone."},
            {"text": "Neither skeleton changes at all, because bone stops "
                     "changing once you are fully grown", "correct": False,
             "why": "You rebuild bone throughout life, so what you take in "
                    "keeps mattering long after growing has stopped."},
            {"text": "The one taking in less has shorter bones, because "
                     "calcium is what makes a bone grow "
                     "longer", "correct": False,
             "why": "Length is set by growth at the ends of a bone. Calcium "
                    "decides how hard and strong that bone is."},
            {"text": "The one taking in less builds weaker bone, because "
                     "calcium is what the body lays down to harden "
                     "it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s19",
        "band": "standard",
        "text": "Astronauts come back from months in orbit with weaker bones "
                "than they left with, even though they exercise every day. "
                "Explain why.",
        "options": [
            {"text": "Bone is dead material, and dead material slowly decays "
                     "once it is away from the Earth", "correct": False,
             "why": "Bone is living tissue and is rebuilt all the time. What "
                    "has changed in orbit is the force going through it."},
            {"text": "There is no calcium in the food they eat while they are "
                     "in orbit, so no new bone can be built", "correct": False,
             "why": "Their food carries calcium as usual. The missing thing is "
                    "the load that bone responds to."},
            {"text": "In orbit almost no force passes through their bones, so "
                     "less material is laid down", "correct": True},
            {"text": "Their marrow stops making blood cells in orbit, so the "
                     "bone around it thins", "correct": False,
             "why": "Marrow makes blood cells, not bone. Bone thickness "
                    "follows the force going through the bone."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s20",
        "band": "standard",
        "text": "A crab has to shed its whole hard case in order to grow, and "
                "is soft and vulnerable for days afterwards. What does that "
                "show about an exoskeleton?",
        "options": [
            {"text": "It cannot grow with the animal, so it has to be thrown "
                     "off and replaced", "correct": True},
            {"text": "It is made of cartilage, which cannot harden again once "
                     "it has been shed", "correct": False,
             "why": "A crab's case is not cartilage, and it does harden again. "
                    "The trouble is that the old case could not get bigger."},
            {"text": "It is not really a skeleton, because a skeleton has to "
                     "be inside the animal", "correct": False,
             "why": "A skeleton is whatever holds the body in shape and gives "
                    "muscles something to pull on. It can be inside or "
                    "outside."},
            {"text": "It holds no marrow, so the crab cannot repair it while "
                     "it is being worn", "correct": False,
             "why": "No exoskeleton holds marrow. What forces the shed is "
                    "simply that a hard case cannot grow."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s21",
        "band": "standard",
        "text": "Compare an insect's exoskeleton with your own skeleton. Give "
                "one advantage that each design has over the other.",
        "options": [
            {"text": "The case grows along with the animal, while a skeleton "
                     "inside has to be shed and then "
                     "replaced", "correct": False,
             "why": "That is the wrong way round. A hard outer case cannot get "
                    "bigger, which is why it has to be shed."},
            {"text": "The case shields the whole animal at once; a skeleton "
                     "inside grows along with the body", "correct": True},
            {"text": "The case makes the blood cells; a skeleton inside has to "
                     "take them in from the gut instead", "correct": False,
             "why": "Blood cells are made in the marrow inside bone, and no "
                    "skeleton takes them in from anywhere."},
            {"text": "The case is living tissue; a skeleton inside is dead "
                     "material laid down once", "correct": False,
             "why": "Bone is living tissue and is rebuilt throughout life. "
                    "That is one of the advantages of a skeleton inside."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s22",
        "band": "standard",
        "text": "An earthworm squeezes the fluid inside one end of its body, "
                "and that end becomes long and thin. Explain how squeezing "
                "changes the shape.",
        "options": [
            {"text": "The fluid is compressed into a smaller space, so the "
                     "body around it shrinks to fit", "correct": False,
             "why": "A fluid barely compresses at all. Squeezing it in one "
                    "direction pushes it out in another."},
            {"text": "The fluid drains away into the soil, so that part of the "
                     "body collapses inwards", "correct": False,
             "why": "The fluid is sealed inside the worm. It moves about "
                    "within the body rather than leaving it."},
            {"text": "Fluid cannot be squashed smaller, so it moves and pushes "
                     "the body out somewhere else", "correct": True},
            {"text": "The fluid hardens wherever it is squeezed, giving the "
                     "worm a temporary bone", "correct": False,
             "why": "Nothing hardens anywhere. The stiffness comes from fluid "
                    "held under pressure, which is why it is called "
                    "hydrostatic."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s23",
        "band": "standard",
        "text": "A slug the size of a horse could not exist on land. Give the "
                "reason that comes from the skeleton.",
        "options": [
            {"text": "It would have no marrow, so it could not make enough "
                     "blood cells for a body that size", "correct": False,
             "why": "Plenty of animals with no bone make blood without any "
                    "marrow. The problem is holding the shape up."},
            {"text": "With nothing rigid inside it, a body that size would "
                     "spread out under its own weight", "correct": True},
            {"text": "Its muscles would not be strong enough to contract at "
                     "all at that size", "correct": False,
             "why": "Muscle strength rises with muscle size. What it lacks is "
                    "anything rigid for a muscle to pull on."},
            {"text": "It could not take in enough calcium to harden a body of "
                     "that size", "correct": False,
             "why": "There would be nothing there to harden. A slug has no "
                    "bone to lay calcium into in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s24",
        "band": "standard",
        "text": "A student writes: 'The skeleton moves the body.' Rewrite that "
                "sentence so that it is correct.",
        "options": [
            {"text": "The skeleton moves the body by shortening its own bones, "
                     "and the muscles simply hold it all "
                     "steady", "correct": False,
             "why": "A bone cannot shorten or change shape at all. Being rigid "
                    "is precisely what makes it useful."},
            {"text": "Muscles move the body by pulling on the skeleton, which "
                     "is rigid enough to be pulled", "correct": True},
            {"text": "The skeleton moves the body, and the muscles protect the "
                     "bones from wearing themselves out", "correct": False,
             "why": "Muscles are the parts that pull. Protecting bone from "
                    "wear is not a job they do."},
            {"text": "Muscles move the body on their own, without needing the "
                     "skeleton at all", "correct": False,
             "why": "A pull needs something rigid at the far end of it. "
                    "Without the skeleton, a contraction moves nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s25",
        "band": "standard",
        "text": "The ends of a femur are filled with a light honeycomb of "
                "bone, while the shaft is a hollow tube. Suggest why the two "
                "parts are built differently.",
        "options": [
            {"text": "The ends spread the load over a wider area, and a "
                     "honeycomb does that for very little "
                     "weight", "correct": True},
            {"text": "The ends are where all the marrow is, and a honeycomb is "
                     "exactly what that marrow is made of", "correct": False,
             "why": "Marrow is a soft tissue sitting in the spaces. The "
                    "honeycomb around it is bone."},
            {"text": "The ends have to be soft, so that they can be squashed "
                     "each time you land", "correct": False,
             "why": "The honeycomb is hardened bone and it is stiff. It "
                    "spreads a load rather than squashing under it."},
            {"text": "The ends are still growing, so they are bone that has "
                     "not yet been hardened", "correct": False,
             "why": "It is fully hardened bone. Its structure is about "
                    "spreading load, not about being unfinished."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s26",
        "band": "standard",
        "text": "Using the levels of organisation, state what bone is and what "
                "the whole skeleton is.",
        "options": [
            {"text": "Bone is a tissue, and the whole skeleton is an organ "
                     "system", "correct": True},
            {"text": "Bone is a cell, and the whole skeleton is one single "
                     "large organ", "correct": False,
             "why": "Bone is built from many cells working together. One cell "
                    "is far too small to be a bone."},
            {"text": "Bone is an organ system, and the whole skeleton is an "
                     "organism", "correct": False,
             "why": "An organism is a whole living thing. The skeleton is one "
                    "system inside one."},
            {"text": "Bone is an organ, and the whole skeleton is one very "
                     "large tissue", "correct": False,
             "why": "It is the other way up. A tissue is the smaller unit and "
                    "a system is the larger one."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s27",
        "band": "standard",
        "text": "The marrow turns out new red blood cells every second of your "
                "life. Explain why it has to keep working at that rate for a "
                "whole lifetime.",
        "options": [
            {"text": "The body keeps on growing all through life, so it needs "
                     "more and more red blood cells each "
                     "year", "correct": False,
             "why": "Growth stops in early adulthood. The demand carries on "
                    "because existing cells wear out and are removed."},
            {"text": "Red blood cells are used up each time they deliver "
                     "oxygen to a cell", "correct": False,
             "why": "One red blood cell delivers oxygen over and over again "
                    "for months before it wears out."},
            {"text": "Blood is constantly leaking away, so the cells that are "
                     "lost have to be made good again", "correct": False,
             "why": "Blood is held inside a closed set of vessels. What is "
                    "lost is cells wearing out, not blood escaping."},
            {"text": "Red blood cells wear out after about four months and "
                     "have to be replaced constantly", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s28",
        "band": "standard",
        "text": "Name the bone that shields the front of the chest and also "
                "holds marrow, and say which two jobs it is doing.",
        "options": [
            {"text": "The sternum — protection, and making blood "
                     "cells", "correct": True},
            {"text": "The scapula — support, and the making of blood "
                     "cells", "correct": False,
             "why": "The scapula is the shoulder blade, at the back. Nothing "
                    "at the front of the chest is shielded by it."},
            {"text": "The patella — protection, and movement at the "
                     "knee", "correct": False,
             "why": "The patella is the kneecap. It sits at the knee, nowhere "
                    "near the chest."},
            {"text": "The cranium — protection, and support for the "
                     "head", "correct": False,
             "why": "The cranium shields the brain, and it is the bones of the "
                    "neck that hold the head up."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s29",
        "band": "standard",
        "text": "Two bones break in one fall. One knits quickly; the other, "
                "where the blood vessels running into it were torn, takes far "
                "longer. Explain the difference.",
        "options": [
            {"text": "Bone is dead material, so repair depends only on how "
                     "tightly the two ends are held "
                     "together", "correct": False,
             "why": "Bone is living tissue. Holding the ends still does help, "
                    "but it is living cells that do the knitting."},
            {"text": "Torn vessels mean less calcium arrives, and calcium is "
                     "what does the knitting on its own", "correct": False,
             "why": "Calcium hardens new bone, but the bone's own cells build "
                    "it, and those cells have to be supplied."},
            {"text": "The marrow was torn too, so no new blood cells were made "
                     "to go and repair the break", "correct": False,
             "why": "Repair is not done by blood cells. The break is slower "
                    "because the bone's own cells are poorly supplied."},
            {"text": "Repair is done by living cells, and cells cannot work "
                     "without a supply of oxygen and food", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s30",
        "band": "standard",
        "text": "Your ear and the end of your nose bend and spring back, and "
                "neither contains any bone. Suggest why cartilage suits those "
                "parts better.",
        "options": [
            {"text": "They are not important enough to be given bone, since "
                     "nothing very much depends on them", "correct": False,
             "why": "A tissue is chosen for what the part has to do, never for "
                    "how important the part is."},
            {"text": "Bone cannot be grown that far out from the centre of the "
                     "body, whatever its shape", "correct": False,
             "why": "The bones of your fingers and toes sit further out than "
                    "your ears do. Distance is not the reason."},
            {"text": "They need to hold a shape and still bend without "
                     "breaking, which bone cannot do", "correct": True},
            {"text": "They will turn into bone later on, once the rest of the "
                     "skeleton has finished all its growing", "correct": False,
             "why": "They stay as cartilage for life. Not all cartilage is on "
                    "its way to becoming bone."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s31",
        "band": "standard",
        "text": "An engineer proposes a one-piece moulded shell in place of a "
                "skeleton: same shape, same strength, no separate bones. State "
                "two things the body could no longer do.",
        "options": [
            {"text": "Carry any weight at all, and shield the organs from a "
                     "knock", "correct": False,
             "why": "A rigid shell of the same strength would do both of those "
                    "perfectly well. Moving and growing are what it rules "
                    "out."},
            {"text": "Make blood cells, and lay calcium down wherever it was "
                     "needed", "correct": False,
             "why": "A shell could be hollow and hold marrow just as a bone "
                    "does. Moving and growing are the losses."},
            {"text": "Respire, and get the oxygen in the blood through to the "
                     "cells", "correct": False,
             "why": "Respiration happens inside cells and does not depend on "
                    "the shape of the skeleton at all."},
            {"text": "Bend or move at all, and grow any larger than the shell "
                     "it was given", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-s32",
        "band": "standard",
        "text": "A car has a rigid chassis, and that is all it has. Using that "
                "comparison, explain what a skeleton does that a chassis does "
                "not.",
        "options": [
            {"text": "It shields organs, gives muscles something to pull "
                     "against, and makes the body's blood "
                     "cells", "correct": True},
            {"text": "It carries load without bending, which a chassis could "
                     "never manage to do", "correct": False,
             "why": "A chassis carries load extremely well. Carrying load is "
                    "the one job the two designs share."},
            {"text": "It is heavier than a chassis, so the body is a good deal "
                     "more stable when it moves about", "correct": False,
             "why": "A skeleton is remarkably light for its strength. What it "
                    "adds is three jobs a chassis has no part in."},
            {"text": "It is rigid, which is the one thing that a chassis is "
                     "not", "correct": False,
             "why": "A chassis is rigid; that is its whole purpose. The "
                    "difference lies in everything else the skeleton does."},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-01-h14",
        "band": "harder",
        "text": "The cranium is a sealed box and the vertebrae are a chain of "
                "separate rings. Both shield nervous tissue. Explain why the "
                "two are built so differently.",
        "options": [
            {"text": "The head does not have to bend, but the back does, so "
                     "its shield is built in segments", "correct": True},
            {"text": "The spinal cord is tougher than the brain, so it can "
                     "manage with a weaker shield", "correct": False,
             "why": "Both are nervous tissue and neither replaces what it "
                    "loses. The difference is that the back has to bend."},
            {"text": "The rings hold marrow and the box does not, so the rings "
                     "had to be kept separate", "correct": False,
             "why": "Both of them hold marrow. What decides the shape is "
                    "whether that part of the body has to move."},
            {"text": "The box is the later design, and the chain of rings is "
                     "what the body started out with", "correct": False,
             "why": "Neither is a later design than the other. Each shape "
                    "suits what its part of the body has to do."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h15",
        "band": "harder",
        "text": "Bone holds most of the body's calcium, and the body draws "
                "calcium back out of bone when the blood runs short. Explain "
                "what that shows about the skeleton.",
        "options": [
            {"text": "It is a dead frame, and calcium simply leaks out of it "
                     "when there is less in the blood", "correct": False,
             "why": "Nothing leaks. Living cells take the calcium out and put "
                    "it back, which a dead frame could not do."},
            {"text": "It is a store first, and carrying load is a side effect "
                     "of being packed with calcium", "correct": False,
             "why": "The skeleton carries load, shields organs and anchors "
                    "muscles. Storing calcium is one job among several."},
            {"text": "The calcium in bone is fixed once it has been laid down, "
                     "so the blood has to find its own "
                     "elsewhere", "correct": False,
             "why": "It is not fixed at all. Bone gives calcium up to the "
                    "blood and takes it back again."},
            {"text": "It is a living store as well as a frame — material moves "
                     "into it and back out of it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h16",
        "band": "harder",
        "text": "A robot designer wants a gripping arm with no rigid parts, "
                "and copies an earthworm: a sealed sleeve of fluid with "
                "muscles wound around it. Predict one advantage and one limit.",
        "options": [
            {"text": "It can lift more than a rigid arm, but it cannot change "
                     "shape once it has been filled", "correct": False,
             "why": "Fluid under pressure is far less stiff than a rigid bar. "
                    "Changing shape is the thing it is good at."},
            {"text": "It needs no energy to hold a shape, but it can only be "
                     "used under water", "correct": False,
             "why": "Holding a shape means holding muscles contracted, which "
                    "costs energy, and the fluid is sealed in."},
            {"text": "It is rigid in every direction, but the fluid inside has "
                     "to be replaced regularly", "correct": False,
             "why": "It is not rigid at all, which is the whole point of the "
                    "design. The fluid stays sealed inside."},
            {"text": "It can squeeze into gaps a rigid arm cannot, but it "
                     "cannot hold a heavy load steady", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h17",
        "band": "harder",
        "text": "A marionette has rigid wooden limbs below and strings running "
                "up to a crossbar the puppeteer holds. Which part plays the "
                "skeleton's role, and which the muscle's?",
        "options": [
            {"text": "The strings are the skeleton, because they run the whole "
                     "length of the puppet", "correct": False,
             "why": "The strings do the pulling and they are not rigid. The "
                    "wooden limbs play the skeleton's part."},
            {"text": "The wooden limbs are the skeleton, and the strings that "
                     "pull on them are the muscles", "correct": True},
            {"text": "The crossbar is the skeleton, because everything else "
                     "hangs down from it", "correct": False,
             "why": "The crossbar is what does the pulling, so it belongs on "
                    "the muscle's side of the comparison."},
            {"text": "The wooden limbs are the muscles, because they are the "
                     "parts that move", "correct": False,
             "why": "Being moved is not the same as doing the moving. The "
                    "limbs are pulled about, exactly as bones are."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h18",
        "band": "harder",
        "text": "An archaeologist can tell a child's skeleton from an adult's "
                "without measuring the length of a single bone. Suggest how.",
        "options": [
            {"text": "A child's bones hold no marrow, because blood cells are "
                     "only made once you are grown", "correct": False,
             "why": "Marrow is at work from before birth. What gives the age "
                    "away is the count of separate bones."},
            {"text": "The number of separate bones is higher in a child, "
                     "because fusing is not finished", "correct": True},
            {"text": "A child's bones contain no calcium yet, so the whole "
                     "skeleton is a great deal lighter to "
                     "lift", "correct": False,
             "why": "A child's bones contain calcium and are already "
                    "hardening. What differs is how many separate pieces there "
                    "are."},
            {"text": "A child's bones are made of cartilage the whole way "
                     "through until adulthood", "correct": False,
             "why": "Much of a newborn's skeleton is cartilage, but bone "
                    "replaces it steadily right through childhood."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h19",
        "band": "harder",
        "text": "A child's long bones lengthen at plates near their ends, and "
                "those plates turn to bone once growth is over. Explain why an "
                "adult cannot grow taller by eating more calcium.",
        "options": [
            {"text": "Adults take in no calcium at all, so there is nothing "
                     "available to build with", "correct": False,
             "why": "Adults take calcium in and use it to maintain bone. "
                    "Height stops because the growth plates have closed."},
            {"text": "Calcium only hardens bone in children, and does nothing "
                     "to an adult skeleton", "correct": False,
             "why": "Calcium goes on hardening bone throughout life. It is "
                    "length, not hardness, that can no longer change."},
            {"text": "Length comes from those plates, and once they are bone "
                     "there is nowhere left to lengthen", "correct": True},
            {"text": "Adult bone is dead, so nothing whatever can be added to "
                     "it after growth", "correct": False,
             "why": "Adult bone is living and is rebuilt constantly. What has "
                    "gone is the plate where lengthening happened."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h20",
        "band": "harder",
        "text": "A student says a human skeleton made entirely of cartilage "
                "would be better, because cartilage bends instead of breaking. "
                "Evaluate that.",
        "options": [
            {"text": "It would be better in every way, because a tissue that "
                     "bends can never be damaged", "correct": False,
             "why": "Cartilage tears and wears away. And a skeleton that bends "
                    "under load cannot hold a body up at all."},
            {"text": "It would be worse only because cartilage cannot repair "
                     "itself once it is damaged", "correct": False,
             "why": "Cartilage does repair, though slowly. The larger problem "
                    "is that it is not rigid enough to carry a body."},
            {"text": "It would make no difference, because cartilage is simply "
                     "bone that has not hardened", "correct": False,
             "why": "Cartilage is a separate tissue, not unhardened bone. Its "
                    "properties differ from bone's throughout life."},
            {"text": "It would bend under load rather than hold the body up, "
                     "and it would hold no marrow", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h21",
        "band": "harder",
        "text": "The marrow makes about two million red blood cells every "
                "second. Calculate roughly how many that is in one hour.",
        "options": [
            {"text": "About 120,000,000", "correct": False,
             "why": "That is one minute's worth. An hour is 3,600 seconds, so "
                    "multiply by 3,600 and not by 60."},
            {"text": "About 7,200,000", "correct": False,
             "why": "A power of ten has been dropped: two million multiplied "
                    "by 3,600 is seven thousand two hundred million."},
            {"text": "About 2,000,000", "correct": False,
             "why": "That is one second's worth, which is the number the "
                    "question started from."},
            {"text": "About 7,200,000,000", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h22",
        "band": "harder",
        "text": "Red blood cells wear out after a set time, and the number of "
                "them in the blood stays steady. What must therefore be true "
                "of the rate the marrow works at?",
        "options": [
            {"text": "It must work in bursts every four months, replacing the "
                     "whole lot at once", "correct": False,
             "why": "The cells are not all the same age, so they are not all "
                    "lost together. Losses happen continuously."},
            {"text": "It must replace them as fast as they are lost, day after "
                     "day", "correct": True},
            {"text": "It must speed up steadily, because there are more cells "
                     "to replace each month", "correct": False,
             "why": "The number in the blood stays steady, so the number lost "
                    "each day stays steady as well."},
            {"text": "It must slow down over the years, because cells last "
                     "longer as a person ages", "correct": False,
             "why": "Lifespan does not lengthen with age. A steady number "
                    "means a steady rate of replacement."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h23",
        "band": "harder",
        "text": "Standing still, the weight of the upper body passes down the "
                "vertebrae, into the pelvis and on into the legs. State one "
                "job the pelvis does that the vertebrae do not, and one they "
                "share.",
        "options": [
            {"text": "The pelvis makes blood cells and the vertebrae do not; "
                     "both shield nervous tissue", "correct": False,
             "why": "Both of them hold marrow, and no spinal cord runs through "
                    "the pelvis."},
            {"text": "The pelvis lets the body bend and the vertebrae do not; "
                     "both shield the spinal cord", "correct": False,
             "why": "It is the other way round: the chain of vertebrae bends, "
                    "and an adult pelvis is solid."},
            {"text": "The pelvis anchors muscles and the vertebrae do not; "
                     "both make blood cells", "correct": False,
             "why": "Muscles anchor to the vertebrae as well as to the pelvis, "
                    "so that half is wrong."},
            {"text": "The pelvis surrounds and shields the organs low in the "
                     "body; both carry the load downwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h24",
        "band": "harder",
        "text": "A student argues that a one-piece skeleton could never break, "
                "because there would be no weak points where bones meet. "
                "Evaluate that.",
        "options": [
            {"text": "One piece would still break, and the body could then "
                     "neither move nor grow", "correct": True},
            {"text": "It is right — a single piece has no weak points, so it "
                     "could not break at all", "correct": False,
             "why": "Any material breaks if the force on it is large enough. "
                    "Being in one piece changes nothing about that."},
            {"text": "It is right, and the body would still move, because bone "
                     "bends a little under load", "correct": False,
             "why": "Bone barely bends. Movement comes from separate bones "
                    "moving against each other, not from bending."},
            {"text": "One piece would not break, but it would hold no marrow "
                     "and so make no blood cells", "correct": False,
             "why": "A single piece could be hollow and hold marrow. What it "
                    "truly rules out is movement and growth."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h25",
        "band": "harder",
        "text": "A deep-sea animal with no skeleton keeps its shape a "
                "kilometre down, but collapses into a puddle when it is "
                "brought up to the surface. Explain what was holding its "
                "shape.",
        "options": [
            {"text": "The pressure inside it, which was released as soon as it "
                     "was lifted out", "correct": False,
             "why": "The pressure inside matched the water outside. What it "
                    "lost at the surface was the water around it."},
            {"text": "A skeleton of cartilage, which dissolves as soon as it "
                     "meets the air", "correct": False,
             "why": "It has no skeleton of any kind, and no tissue of an "
                    "animal dissolves in air."},
            {"text": "The water around it, which supported a body its own "
                     "tissue could not", "correct": True},
            {"text": "Its muscles, which stop contracting the moment the "
                     "animal leaves the water", "correct": False,
             "why": "Muscles pull; they cannot hold a soft body in shape "
                    "without something rigid. The water was doing that."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h26",
        "band": "harder",
        "text": "A student says the skeleton cannot be an organ system, "
                "because a system has to do one job and the skeleton does "
                "four. Evaluate that.",
        "options": [
            {"text": "They are right, so the skeleton is better described as "
                     "one very large organ", "correct": False,
             "why": "The skeleton is many organs working together, and that is "
                    "exactly what a system is."},
            {"text": "They are right, and it is really four systems that "
                     "happen to share the same bones", "correct": False,
             "why": "One set of parts doing several jobs is still one system, "
                    "not four separate ones."},
            {"text": "They are wrong, because the skeleton really only does "
                     "one job — holding you up", "correct": False,
             "why": "It does four jobs. And the definition of a system never "
                    "required there to be only one."},
            {"text": "An organ system is a set of organs working together, and "
                     "it may do several jobs", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h27",
        "band": "harder",
        "text": "Someone claims that eating twice as much calcium would make "
                "their bones twice as strong. Explain why that does not "
                "follow.",
        "options": [
            {"text": "Bone is built to match the force going through it, and "
                     "extra calcium is not laid down without "
                     "it", "correct": True},
            {"text": "It does follow, because the hardness of bone rises with "
                     "every extra gram of calcium taken in", "correct": False,
             "why": "Bone is built by living cells to match the load on it. It "
                    "is not simply filled up with whatever arrives."},
            {"text": "It does not follow, because calcium plays no part in "
                     "building bone at all", "correct": False,
             "why": "Calcium is exactly what hardens bone. The point is that "
                    "more of it does not automatically mean more bone."},
            {"text": "It does not follow, because calcium is used to make red "
                     "blood cells instead", "correct": False,
             "why": "Red blood cells are made in the marrow, and calcium is "
                    "not the material they are built from."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h28",
        "band": "harder",
        "text": "Compare an exoskeleton with a skeleton inside the body, for a "
                "small animal that must not dry out in a hot, dry place. Which "
                "suits it better, and why?",
        "options": [
            {"text": "The skeleton inside, because it grows with the animal "
                     "and never has to be shed", "correct": False,
             "why": "Growing without a shed is a genuine advantage, but at "
                    "small size the case's waterproofing matters more here."},
            {"text": "The exoskeleton, because it is living tissue and repairs "
                     "itself between moults", "correct": False,
             "why": "It is the skeleton inside that is living tissue. A hard "
                    "outer case is largely non-living once it has formed."},
            {"text": "The exoskeleton, because a hard case around the whole "
                     "body also holds water in", "correct": True},
            {"text": "The skeleton inside, because it holds marrow and "
                     "therefore supplies more oxygen", "correct": False,
             "why": "Marrow is an advantage of bone, but it has nothing at all "
                    "to do with surviving somewhere dry."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h29",
        "band": "harder",
        "text": "A bone can be built as a long tube, a curved plate or a broad "
                "bowl. Match each shape to the job it does best, naming a bone "
                "for each.",
        "options": [
            {"text": "Tube for protection, as the femur; plate for support, as "
                     "the cranium; bowl for movement, as the "
                     "pelvis", "correct": False,
             "why": "The femur carries load along its length, and the curved "
                    "plates of the cranium are there to keep impacts out."},
            {"text": "Tube for making blood, as the femur; plate for support, "
                     "as the sternum; bowl for protection, as the "
                     "pelvis", "correct": False,
             "why": "All three of those bones hold marrow, so the tube shape "
                    "is not what makes blood. A tube carries load."},
            {"text": "Tube for support, as the femur; plate for protection, as "
                     "the cranium; bowl for surrounding, as the "
                     "pelvis", "correct": True},
            {"text": "Tube for movement, as the femur; plate for making blood, "
                     "as the cranium; bowl for support, as the "
                     "pelvis", "correct": False,
             "why": "Shape follows the load or the impact, not the marrow, "
                    "since all three of those bones hold marrow."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h30",
        "band": "harder",
        "text": "Three animals: one with bone inside, one with a hard case "
                "outside, and one held up by fluid under pressure. Which can "
                "grow largest on land, and why?",
        "options": [
            {"text": "The one with the case outside, because a shell is "
                     "stronger than anything held inside a "
                     "body", "correct": False,
             "why": "A case has to thicken as an animal grows, until its own "
                    "weight defeats it. That is why land insects stay small."},
            {"text": "The one with bone inside, because it grows with the "
                     "animal and is strong for its weight", "correct": True},
            {"text": "The one held up by fluid, because fluid will fill a body "
                     "of any size at all", "correct": False,
             "why": "Fluid under pressure is far less stiff than bone, so a "
                    "large body would spread out under its own weight."},
            {"text": "All three could reach the same size, because size "
                     "depends only on the food supply", "correct": False,
             "why": "Food matters, but on land the skeleton sets a ceiling, "
                    "and both the case and the fluid reach theirs sooner."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h31",
        "band": "harder",
        "text": "An engineer says bone is the best material she knows: it "
                "repairs itself, it adapts to load, and it is light for its "
                "size. Which of the three would a steel bar of the same size "
                "also manage?",
        "options": [
            {"text": "All three, because steel is stronger than bone in just "
                     "about every way that matters", "correct": False,
             "why": "Steel is strong, but it cannot repair a crack or lay down "
                    "more material where the force goes."},
            {"text": "None of the three — steel repairs nothing, adapts to "
                     "nothing, and is far heavier for its "
                     "size", "correct": True},
            {"text": "Only the repairing, because a small crack in steel "
                     "closes up again under load", "correct": False,
             "why": "A crack in steel grows under load, it does not close. "
                    "Repair needs living cells."},
            {"text": "Only the adapting, because steel hardens in the places "
                     "where it is worked hardest", "correct": False,
             "why": "Steel can harden a little with working, but it does not "
                    "add material where the force goes. Bone does."},
        ],
        "figure": None,
    },
    {
        "id": "b2-01-h32",
        "band": "harder",
        "text": "A skeleton is found with a cranium, a sternum, a pelvis and "
                "two femurs, and nothing else. Which of the four jobs can you "
                "still find evidence for?",
        "options": [
            {"text": "All four — between them those bones support, shield, "
                     "anchor muscles and hold marrow", "correct": True},
            {"text": "Only support and protection, because marrow is only ever "
                     "found inside the long limb bones", "correct": False,
             "why": "The sternum and the pelvis are flat bones, and both of "
                    "them hold marrow."},
            {"text": "Only protection, because not one of those bones has "
                     "anything at all attached to pull on "
                     "it", "correct": False,
             "why": "Muscles anchor to every one of them, and the femur "
                    "carries the whole body's load."},
            {"text": "None of them, because a skeleton with parts missing "
                     "cannot show any of its jobs at all", "correct": False,
             "why": "The question asks what the bones themselves show, and "
                    "each of these four shows something."},
        ],
        "figure": None,
    },
]
