"""B4 lesson 02 — How breathing works: twelve questions (MRB-269).

The lesson has one argument — volume first, pressure second, air last — and
everything here is built to catch a student who has the order wrong. The
easier band holds the four facts the argument rests on: what the diaphragm
does when it contracts, that a lung contains no muscle, that ventilation is
not respiration, and that a quiet breath out is relaxation plus elastic
recoil. The standard band works the bell jar the student actually used — which
readout is the fixed reference, why the pressure falls, what the rigid glass
wall cannot show — and puts the causation to the test with a wind blowing into
someone's face. The harder band takes the argument somewhere new: the iron
lung from the stretch layer, a paralysed diaphragm set beside the hook's chest
wound, the dome-versus-flat-sheet limit, and the foot line's claim that a real
chest swings by under 1 kPa.

The distractors are the lesson's three declared misconceptions, used
repeatedly because they are what a Year 8 class actually brings. BREATH-04
("the lungs expand and pull the air in") supplies the pulled-down diaphragm in
e01, the self-filling lung in e02, the self-squeezing lung in e04 and the
lung-has-lost-its-strength option in h02. BREATH-05 ("air rushes in, and that
is what makes the chest get bigger") supplies the air-pulls-them-open option
in e02 and both wrong halves of s03. BREATH-14 ("something sucks the air in")
supplies the tank-sucks-it-out option in h01. Two errors the lesson corrects
in passing supply the rest: particles changing size or amount when a space
enlarges (s02), and the direction of diaphragm movement on relaxing (e04,
h03).

`figure` is None throughout — this lesson declares no figures at all, so there
is nothing a question could legitimately point at.
"""

UNIT = "B4"
LESSON = "how-breathing-works"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-02-e01",
        "band": "easier",
        "text": "The diaphragm is a domed sheet of muscle at rest. What "
                "happens to it, and to the chest, when it contracts?",
        "options": [
            {"text": "It domes upwards more strongly and the chest gets "
                     "smaller.",
             "correct": False,
             "why": "That is what the diaphragm does when it relaxes — it "
                    "domes back up and the chest gets smaller, which is a "
                    "breath out. Contracting does the opposite."},
            {"text": "It flattens downwards, and the volume of the chest "
                     "increases.",
             "correct": True},
            {"text": "It is pulled downwards by the lungs stretching above "
                     "it.",
             "correct": False,
             "why": "Nothing in a lung can pull, because there is no muscle "
                    "tissue anywhere in one. The diaphragm moves itself, and "
                    "the lungs are stretched by the space around them "
                    "growing."},
            {"text": "It stays still while the ribs do all of the work.",
             "correct": False,
             "why": "The intercostal muscles do swing the ribs up and out, "
                    "but that is only about a third of quiet breathing. The "
                    "diaphragm does the rest, and it moves on every breath."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e02",
        "band": "easier",
        "text": "Your lungs contain no muscle tissue at all. What does that "
                "tell you about how they fill with air?",
        "options": [
            {"text": "They are inflated by the pressure around them falling, "
                     "not by their own effort.",
             "correct": True},
            {"text": "They fill themselves slowly, which is why a breath in "
                     "takes about a second.",
             "correct": False,
             "why": "A lung has no way of expanding itself, quickly or "
                    "slowly. It is stretched by the space around it growing "
                    "when the diaphragm and the intercostals move."},
            {"text": "They are pulled open by the air arriving through the "
                     "windpipe and bronchi.",
             "correct": False,
             "why": "The air arriving is the result, never the cause. Seal "
                    "the tube on the bell-jar model so no air can enter, work "
                    "the sheet, and the volume still changes."},
            {"text": "The muscle in the walls of the alveoli squeezes them "
                     "open and shut.",
             "correct": False,
             "why": "There is no muscle in a lung at any scale, alveoli "
                    "included. The muscles that ventilate you — the diaphragm "
                    "and the intercostals — sit outside the lungs entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e03",
        "band": "easier",
        "text": "A student writes: “Respiration is when you breathe air "
                "in and out of your lungs.” What is wrong with that "
                "sentence?",
        "options": [
            {"text": "Nothing is wrong — respiration and breathing are two "
                     "words for the same thing.",
             "correct": False,
             "why": "They are not. Respiration is a reaction that happens "
                    "inside cells; moving air in and out of the lungs is "
                    "ventilation. Mixing the two up is the commonest lost "
                    "mark in this topic."},
            {"text": "Respiration is the exchange of gases across the "
                     "alveoli, not the moving of air.",
             "correct": False,
             "why": "Gas exchange across the alveoli is not respiration "
                    "either. Respiration happens inside cells, and moving air "
                    "in and out of the lungs is called ventilation."},
            {"text": "Respiration only happens when you breathe out, because "
                     "that is when carbon dioxide leaves.",
             "correct": False,
             "why": "Respiration is not tied to a breath at all — it runs "
                    "inside your cells every second, whether you are "
                    "breathing in or out. The word for moving the air is "
                    "ventilation."},
            {"text": "Moving air in and out of the lungs is ventilation; "
                     "respiration happens inside cells.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e04",
        "band": "easier",
        "text": "You breathe out quietly, without forcing it. What is doing "
                "most of the work?",
        "options": [
            {"text": "The diaphragm contracting hard to push upwards against "
                     "the lungs.",
             "correct": False,
             "why": "When the diaphragm contracts it flattens and makes the "
                    "chest bigger — that is a breath in. A quiet breath out "
                    "happens when it relaxes and domes back up."},
            {"text": "The lungs squeezing themselves back down to their "
                     "resting size.",
             "correct": False,
             "why": "A lung has no muscle and cannot squeeze anything. What "
                    "returns it to size is elastic recoil: stretched tissue "
                    "springing back on its own, with nothing driving it."},
            {"text": "The muscles relaxing, and the stretched chest recoiling "
                     "elastically to its resting size.",
             "correct": True},
            {"text": "The intercostal muscles contracting to pull the ribs "
                     "down and squeeze the chest.",
             "correct": False,
             "why": "In a quiet breath out the intercostals relax and the "
                    "ribs simply drop. You only recruit muscles to push air "
                    "out when you force a breath, such as blowing up a "
                    "balloon."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-02-s01",
        "band": "standard",
        "text": "The bell-jar model has four readouts: chest volume, pressure "
                "inside, pressure outside and air movement. You slide the "
                "diaphragm up and down. Which readout never changes, and why?",
        "options": [
            {"text": "Pressure outside — atmospheric pressure is the fixed "
                     "reference here.",
             "correct": True},
            {"text": "Chest volume — the jar is rigid, so the space inside it "
                     "cannot change.",
             "correct": False,
             "why": "The glass wall is rigid, but the rubber sheet across the "
                    "bottom is not. Moving that sheet is exactly what changes "
                    "the volume, and the readout climbs as you pull it down."},
            {"text": "Pressure inside — the jar is sealed, so nothing can get "
                     "in to change it.",
             "correct": False,
             "why": "Sealing a jar does not fix the pressure inside it. That "
                    "pressure falls as the same air is spread through a "
                    "bigger space, and watching it fall is the whole point of "
                    "the model."},
            {"text": "Air movement — the balloon is fixed to the tube, so no "
                     "air can pass.",
             "correct": False,
             "why": "Air passes freely through the tube in the lid, which is "
                    "why the balloon inflates at all. The air readout "
                    "switches between in, out and none as you move the "
                    "sheet."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s02",
        "band": "standard",
        "text": "Your chest enlarges and the same air now fills a bigger "
                "space. Explain why the pressure inside falls.",
        "options": [
            {"text": "The air particles spread out and get bigger, so each "
                     "one pushes more weakly.",
             "correct": False,
             "why": "Particles never change size. Spreading the same "
                    "particles through more space does not shrink them — it "
                    "means fewer of them reach any given patch of wall each "
                    "second."},
            {"text": "There is now less air in the chest, and less air always "
                     "means less pressure.",
             "correct": False,
             "why": "No air has left, so the amount is exactly the same. Only "
                    "the space it occupies has changed, and that is enough to "
                    "lower how often the particles hit the walls."},
            {"text": "The same particles now fill a bigger space, so they hit "
                     "the walls less often.",
             "correct": True},
            {"text": "The air cools down as it expands, and cold air always "
                     "has a lower pressure than warm air.",
             "correct": False,
             "why": "You do not need temperature here, and nothing on the "
                    "model changes it. Pressure comes from how often "
                    "particles collide with the walls, and enlarging the "
                    "space lowers that rate on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s03",
        "band": "standard",
        "text": "A strong wind blows into your face, pushing air at your "
                "mouth and nose. Does your chest inflate?",
        "options": [
            {"text": "Yes — extra air arriving is what makes the chest get "
                     "bigger.",
             "correct": False,
             "why": "This has the causation backwards, and it is the "
                    "commonest wrong answer in the topic. If arriving air "
                    "could enlarge a chest, you would inflate every time the "
                    "wind blew."},
            {"text": "No — only muscles change the chest volume, and arriving "
                     "air is the result.",
             "correct": True},
            {"text": "Yes, but only slightly, because the wind is not as "
                     "strong as your diaphragm.",
             "correct": False,
             "why": "The wind is not competing with the diaphragm at all. Air "
                    "moving into a space cannot make that space bigger — the "
                    "volume change has to come first, and only muscles "
                    "produce it."},
            {"text": "No — the air cannot get past the ribs, which hold the "
                     "chest at a fixed size.",
             "correct": False,
             "why": "The ribs are not fixed: the intercostal muscles swing "
                    "them up and out on every breath. Your chest stays put "
                    "because air is never the cause of a volume change, not "
                    "because it is sealed."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s04",
        "band": "standard",
        "text": "The bell jar has a rigid glass wall, and a rubber sheet "
                "across the bottom is the only part that moves. Which part of "
                "real breathing can it therefore not show at all?",
        "options": [
            {"text": "Pressure inside falling when the volume of the space "
                     "increases.",
             "correct": False,
             "why": "The model shows this better than almost anything — it is "
                    "the readout the whole thing exists for. A rigid wall "
                    "does not stop the pressure changing."},
            {"text": "The diaphragm changing the volume of the chest below "
                     "the lungs.",
             "correct": False,
             "why": "That is the one thing the jar does show, and it isolates "
                    "it deliberately. The rubber sheet is the diaphragm, and "
                    "moving it is what changes the volume."},
            {"text": "Air moving in and out of a balloon through a single "
                     "tube.",
             "correct": False,
             "why": "The tube through the lid does exactly this, and the "
                    "balloon on the end of it inflates and empties. As a "
                    "model of the airway it is fair enough."},
            {"text": "The ribs swinging up and out, moved by the intercostal "
                     "muscles.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-02-h01",
        "band": "harder",
        "text": "An iron lung seals a patient's body from the neck down and "
                "lowers the air pressure inside the tank. Their head is "
                "outside, in the room. How does air get into their lungs?",
        "options": [
            {"text": "The machine pushes air down the patient's throat under "
                     "pressure through a tube.",
             "correct": False,
             "why": "That is a modern ventilator, which reverses the "
                    "geometry. An iron lung puts nothing at all into the body "
                    "— it works entirely from the outside."},
            {"text": "The low pressure in the tank sucks the air out of the "
                     "lungs, which then refill.",
             "correct": False,
             "why": "There is no such thing as sucking. Nothing reaches out "
                    "and draws air along; there is only higher-pressure air "
                    "being pushed into a space where fewer particles push "
                    "back."},
            {"text": "The chest expands because the tank pressure is now "
                     "lower, so air flows in from the room.",
             "correct": True},
            {"text": "The machine squeezes the chest to empty it, and the "
                     "lungs then spring back and refill.",
             "correct": False,
             "why": "That is a breath out followed by recoil, and it is not "
                    "what dropping the tank pressure does. Lowering the "
                    "pressure round the chest lets the chest enlarge, which "
                    "is a breath in."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h02",
        "band": "harder",
        "text": "Patient A has a paralysed diaphragm. Patient B has a wound "
                "letting air into the space around one lung. Both have "
                "healthy lungs and clear airways. What do the two cases have "
                "in common?",
        "options": [
            {"text": "In both, air is blocked somewhere on its way down to "
                     "the alveoli.",
             "correct": False,
             "why": "Neither airway is blocked — you are told both are clear. "
                    "What has failed in both is the pressure difference that "
                    "normally drives air in."},
            {"text": "In both, the chest can no longer lower the pressure "
                     "around the lung.",
             "correct": True},
            {"text": "In both, the lung itself has lost the strength it needs "
                     "to expand.",
             "correct": False,
             "why": "A lung has no strength to lose, because it has no "
                    "muscle. It is inflated by a pressure difference produced "
                    "outside it, and in both patients that difference has "
                    "gone."},
            {"text": "In both, the elastic recoil of the lung has been "
                     "damaged by the injury.",
             "correct": False,
             "why": "Recoil is what empties a lung, not what fills it, and "
                    "neither lung is damaged. What has failed is the chest's "
                    "ability to hold the lung below the outside pressure."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h03",
        "band": "harder",
        "text": "On the model, the rubber sheet is flat and your hand pulls "
                "it down into a cone. Spot what that gets wrong about a real "
                "diaphragm, even though the direction of movement is right.",
        "options": [
            {"text": "A real diaphragm is domed at rest and moves down by "
                     "flattening itself when it contracts.",
             "correct": True},
            {"text": "A real diaphragm is flat at rest and is pushed into a "
                     "dome by the lungs sitting above it.",
             "correct": False,
             "why": "Both halves are the wrong way round. The diaphragm is "
                    "domed at rest, and nothing above it pushes it — it "
                    "changes its own shape when it contracts."},
            {"text": "A real diaphragm is pulled downwards by the ribs as "
                     "they swing up and outwards.",
             "correct": False,
             "why": "The ribs and the diaphragm are worked by different "
                    "muscles, and neither drags the other. The intercostals "
                    "move the ribs; the diaphragm moves itself."},
            {"text": "A real diaphragm moves upwards to make the chest "
                     "bigger, rather than downwards.",
             "correct": False,
             "why": "Moving up is what it does when it relaxes, and that "
                    "makes the chest smaller. The model has the direction "
                    "right, which is exactly why it is still worth using."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h04",
        "band": "harder",
        "text": "The foot line says a real chest's pressure swings by under 1 "
                "kPa, against an atmosphere of about 101 kPa. A student says "
                "a difference that small could never move any air. What is "
                "the best reply?",
        "options": [
            {"text": "The real swing is far bigger than 1 kPa; the model has "
                     "simply been scaled down.",
             "correct": False,
             "why": "The model's numbers are illustrative, but their size is "
                    "honest — the swings in a real chest during quiet "
                    "breathing really are under 1 kPa. Small does not mean "
                    "ineffective."},
            {"text": "The pressure inside has to reach zero before any air "
                     "will move into the lungs.",
             "correct": False,
             "why": "Nothing has to reach zero. Air moves whenever two places "
                    "are at different pressures, and it always moves from the "
                    "higher pressure towards the lower one."},
            {"text": "Air only moves when the difference is large, which is "
                     "why deep breaths are needed.",
             "correct": False,
             "why": "Quiet breathing moves air perfectly well on a swing of "
                    "under 1 kPa. A pressure difference does not have to be "
                    "big to make air flow — it only has to be there."},
            {"text": "Under 1 kPa is right, and air moves whenever there is "
                     "any difference at all.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-02-e05",
        "band": "easier",
        "text": "What do the intercostal muscles do, and roughly how much of "
                "quiet breathing do they account for?",
        "options": [
            {"text": "They squeeze the lungs directly, and they do almost all "
                     "of the work.",
             "correct": False,
             "why": "Nothing squeezes a lung directly. The intercostals sit "
                    "between the ribs, outside the lungs, and they move the "
                    "ribs rather than the lungs."},
            {"text": "They pull the diaphragm downwards, and they do about "
                     "half of the work.",
             "correct": False,
             "why": "The diaphragm moves itself by contracting; nothing drags "
                    "it. The intercostals work the ribs, and they supply "
                    "roughly a third of quiet breathing."},
            {"text": "They swing the ribs up and out, and they account for "
                     "about a third of it.",
             "correct": True},
            {"text": "They hold the ribs still, and they account for none of "
                     "it while you are at rest.",
             "correct": False,
             "why": "The ribs are not held still — they swing up and out on "
                    "every breath in and drop again on the way out. That "
                    "movement is about a third of quiet breathing."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e06",
        "band": "easier",
        "text": "What is atmospheric pressure?",
        "options": [
            {"text": "The pressure of the air around you, from its "
                     "particles hitting surfaces.",
             "correct": True},
            {"text": "The pressure your lungs produce themselves when they "
                     "squeeze down and push all the air back out.",
             "correct": False,
             "why": "Your lungs produce no pressure of their own — they have "
                    "no muscle. Atmospheric pressure belongs to the air "
                    "outside you and is there whether you breathe or not."},
            {"text": "The force with which your diaphragm pulls air down "
                     "the windpipe and into the chest.",
             "correct": False,
             "why": "The diaphragm never pulls air anywhere. It changes the "
                    "volume of the chest, and the atmosphere outside does the "
                    "pushing."},
            {"text": "The weight of the air already sitting inside your "
                     "lungs.",
             "correct": False,
             "why": "It is not about the air inside you. It is the pressure of "
                    "the air surrounding you, and it is the fixed reference "
                    "every breath is measured against."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e07",
        "band": "easier",
        "text": "Two spaces are joined by an open tube and the pressures in "
                "them are different. Which way does the air move?",
        "options": [
            {"text": "Towards whichever space is larger.",
             "correct": False,
             "why": "Size does not decide it. A small space at high pressure "
                    "will empty into a large space at low pressure quite "
                    "happily."},
            {"text": "It is drawn towards the lower pressure, which pulls it "
                     "along.",
             "correct": False,
             "why": "Nothing pulls. There is no force that reaches out and "
                    "draws air along — there is only air at higher pressure "
                    "being pushed by its own particles."},
            {"text": "Both ways equally, so nothing overall happens.",
             "correct": False,
             "why": "Particles do cross both ways, but not equally when the "
                    "pressures differ. More come from the higher-pressure "
                    "side, so the net movement is one way."},
            {"text": "From the higher pressure towards the lower pressure.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e08",
        "band": "easier",
        "text": "Where in the body is the diaphragm, and what is it made of?",
        "options": [
            {"text": "Between the ribs, and it is made of cartilage.",
             "correct": False,
             "why": "Between the ribs are the intercostal muscles. Cartilage "
                    "is the stiff tissue that rings the trachea, and the "
                    "diaphragm is not made of it."},
            {"text": "Underneath the lungs, and it is a sheet of muscle.",
             "correct": True},
            {"text": "Inside each lung, and it is a sheet of muscle.",
             "correct": False,
             "why": "There is no muscle inside a lung at all. The diaphragm "
                    "lies below both lungs and forms the floor of the chest."},
            {"text": "Around the trachea, and it is a ring of muscle.",
             "correct": False,
             "why": "The trachea is ringed with cartilage, not muscle, and the "
                    "diaphragm is nowhere near it. It sits at the bottom of "
                    "the chest, beneath the lungs."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e09",
        "band": "easier",
        "text": "During a breath out, what happens to the volume of the chest "
                "and to the pressure inside it?",
        "options": [
            {"text": "The volume increases and the pressure rises above "
                     "atmospheric.",
             "correct": False,
             "why": "A bigger space lowers the pressure, never raises it. And "
                    "the chest gets smaller on the way out, not bigger."},
            {"text": "The volume stays the same and only the pressure "
                     "changes.",
             "correct": False,
             "why": "The pressure cannot change on its own — nothing else "
                    "could make it. The volume changes first, and the pressure "
                    "changes because of it."},
            {"text": "The volume decreases and the pressure rises above "
                     "atmospheric.",
             "correct": True},
            {"text": "The volume decreases and the pressure falls below "
                     "atmospheric.",
             "correct": False,
             "why": "Squeezing the same air into a smaller space makes the "
                    "particles hit the walls more often, so the pressure goes "
                    "up. Falling pressure is what draws air in."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e10",
        "band": "easier",
        "text": "In the bell-jar model of breathing, what does the rubber "
                "sheet stretched across the bottom of the jar stand for?",
        "options": [
            {"text": "The diaphragm.", "correct": True},
            {"text": "The trachea.", "correct": False,
             "why": "The tube through the lid is the airway. The sheet is at "
                    "the bottom, where the muscle that changes the chest's "
                    "volume sits."},
            {"text": "The ribs.", "correct": False,
             "why": "The model has no ribs at all — the rigid glass wall is "
                    "one of the four things it gets wrong. The moving sheet "
                    "underneath is the diaphragm."},
            {"text": "A lung.", "correct": False,
             "why": "The balloon on the end of the tube is the lung. The sheet "
                    "is the muscle below it, and moving that sheet is what "
                    "makes the balloon inflate."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e11",
        "band": "easier",
        "text": "You blow up a balloon, forcing the air out hard. How is that "
                "different from a quiet breath out?",
        "options": [
            {"text": "The lungs contract to squeeze the air out, and they "
                     "simply do not do that in a quiet breath.",
             "correct": False,
             "why": "A lung has no muscle, so it cannot contract at any time. "
                    "The extra effort comes from muscles outside the lungs."},
            {"text": "The diaphragm contracts harder, which forces the air "
                     "out.",
             "correct": False,
             "why": "Contracting the diaphragm flattens it and makes the chest "
                    "bigger, which is a breath in. Forcing air out needs the "
                    "chest to be made smaller than its resting size."},
            {"text": "Nothing is different — a hard breath out is just a "
                     "faster version of exactly the same thing happening.",
             "correct": False,
             "why": "A quiet breath out costs no muscular effort at all: the "
                    "muscles relax and the stretched chest springs back. "
                    "Forcing air out is the version that needs work."},
            {"text": "Muscles squeeze the chest smaller instead of leaving "
                     "it to elastic recoil.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-02-s05",
        "band": "standard",
        "text": "Compared with a quiet breath in, what is different about "
                "taking the deepest breath in you can?",
        "options": [
            {"text": "The air arriving is richer in oxygen, because a "
                     "deeper breath reaches fresher air.",
             "correct": False,
             "why": "The air is the same air either way. What changes is how "
                    "much of it moves, and that depends on how far the muscles "
                    "enlarge the chest."},
            {"text": "The muscles pull harder, the volume grows more, the "
                     "pressure drops more.",
             "correct": True},
            {"text": "The lungs stretch themselves further than usual, "
                     "which is what makes the breath a deeper one.",
             "correct": False,
             "why": "The lungs never stretch themselves — they have no muscle. "
                    "They are stretched further because the space around them "
                    "has been made bigger."},
            {"text": "The air is pushed in faster, which is what enlarges "
                     "the chest.",
             "correct": False,
             "why": "The causation is backwards. Enlarging the chest is what "
                    "lowers the pressure, and the air moves in afterwards as a "
                    "result."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s06",
        "band": "standard",
        "text": "A hiccup is a sudden involuntary contraction of the "
                "diaphragm. Using the order of events, predict what happens "
                "at that moment.",
        "options": [
            {"text": "Air is forced out sharply, because a contracting "
                     "diaphragm squeezes the chest.",
             "correct": False,
             "why": "A contracting diaphragm flattens and makes the chest "
                    "bigger, not smaller. It is relaxing that squeezes air "
                    "out."},
            {"text": "Nothing moves, because the diaphragm cannot act on its "
                     "own without the ribs.",
             "correct": False,
             "why": "The diaphragm does about two thirds of quiet breathing by "
                    "itself. It does not need the ribs in order to change the "
                    "volume of the chest."},
            {"text": "The chest suddenly enlarges, the pressure drops, and "
                     "air rushes sharply in.",
             "correct": True},
            {"text": "The pressure inside rises first, and the sudden air "
                     "movement then pulls the diaphragm down.",
             "correct": False,
             "why": "Pressure never changes before volume, and moving air "
                    "cannot pull a muscle. The muscle is always the first "
                    "thing in the chain."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s07",
        "band": "standard",
        "text": "A singer holds one long, steady note for twenty seconds. "
                "What must they be doing that a quiet breath out does not "
                "involve?",
        "options": [
            {"text": "Contracting muscles to control how fast the chest gets "
                     "smaller.",
             "correct": True},
            {"text": "Holding the diaphragm contracted so that no air can "
                     "escape at all.",
             "correct": False,
             "why": "If no air escaped there would be no note. What a singer "
                    "controls is the rate at which air leaves, not whether it "
                    "leaves."},
            {"text": "Tightening the lungs slowly so that the air trickles "
                     "out.",
             "correct": False,
             "why": "A lung cannot tighten — there is no muscle in one. Every "
                    "bit of control over a breath comes from muscles outside "
                    "the lungs."},
            {"text": "Keeping the chest volume constant while the air leaves "
                     "steadily.",
             "correct": False,
             "why": "Air can only leave if the space it is in gets smaller. A "
                    "constant volume would mean a constant pressure and no "
                    "flow at all."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s08",
        "band": "standard",
        "text": "A modern ventilator pushes air into a patient through a tube "
                "in the airway. How does that differ from the way a healthy "
                "person breathes in?",
        "options": [
            {"text": "There is no difference; the machine simply moves the "
                     "patient's own diaphragm up and down for them.",
             "correct": False,
             "why": "The machine never touches the diaphragm. It raises the "
                    "pressure at the mouth end instead, which is a different "
                    "mechanism reaching the same result."},
            {"text": "The machine lowers the pressure inside the lungs, in "
                     "exactly the way a diaphragm does.",
             "correct": False,
             "why": "It does the opposite. A ventilator raises the pressure at "
                    "the airway; a diaphragm lowers the pressure inside the "
                    "chest."},
            {"text": "The machine adds oxygen to the air, which the chest "
                     "cannot do.",
             "correct": False,
             "why": "Adding oxygen is a separate matter and is not what makes "
                    "air move. What differs is which end of the tube the "
                    "pressure difference is made at."},
            {"text": "The machine raises the pressure at the mouth end; a "
                     "chest lowers it inside.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s09",
        "band": "standard",
        "text": "On the bell-jar model you pull the rubber sheet down twice "
                "as far as before. What happens to the pressure reading "
                "inside the jar?",
        "options": [
            {"text": "It rises further above atmospheric, because the sheet "
                     "is stretched harder.",
             "correct": False,
             "why": "How hard the rubber is stretched makes no difference to "
                    "the gas. What matters is the space the same air now fills "
                    "— and that space has grown."},
            {"text": "It falls further below atmospheric pressure than it did on "
                     "the smaller pull.",
             "correct": True},
            {"text": "It stays where it was, because the jar is sealed and no "
                     "air has left.",
             "correct": False,
             "why": "The amount of air is indeed unchanged, and that is "
                    "exactly why the pressure falls. The same particles in a "
                    "bigger space hit the walls less often."},
            {"text": "It returns to atmospheric, because a bigger movement "
                     "lets more air in.",
             "correct": False,
             "why": "Air flowing in does reduce the difference, but the "
                    "pressure is lowest at the point of largest volume. A "
                    "bigger pull makes the difference bigger, not smaller."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s10",
        "band": "standard",
        "text": "A student writes: “When you breathe in, you pull air into "
                "your body.” Rewrite it so that it is defensible.",
        "options": [
            {"text": "Your lungs pull the air down the airway by expanding "
                     "themselves.",
             "correct": False,
             "why": "This keeps the pull and adds a second error. A lung has "
                    "no muscle, so it cannot expand itself or draw anything "
                    "anywhere."},
            {"text": "The air pulls itself into the low pressure your chest "
                     "has created.",
             "correct": False,
             "why": "Air has nothing to pull with. Low pressure is simply a "
                    "place where fewer particles are pushing back, so the "
                    "higher-pressure air outside wins."},
            {"text": "Your muscles enlarge the chest, and the atmosphere "
                     "pushes air in.",
             "correct": True},
            {"text": "Your muscles create a vacuum, and the vacuum sucks the "
                     "air in.",
             "correct": False,
             "why": "There is no vacuum and no sucking. The pressure only "
                    "falls slightly — under 1 kPa — and every bit of the "
                    "pushing is done by the air outside."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s11",
        "band": "standard",
        "text": "Air enters through the mouth and leaves through the mouth, "
                "along the very same tube. Explain how one tube can carry "
                "traffic both ways.",
        "options": [
            {"text": "Because air always moves from higher to lower pressure, "
                     "and which end is higher keeps swapping.",
             "correct": True},
            {"text": "Because the airway has two channels side by side, one "
                     "in and one out.",
             "correct": False,
             "why": "There is only one route, and it is the same route in both "
                    "directions. What changes is not the tube but which end of "
                    "it is at the higher pressure."},
            {"text": "Because the cilia sweep the used air back up the way it "
                     "came.",
             "correct": False,
             "why": "Cilia move mucus, not air, and they move it far too "
                    "slowly to matter here. Air moves because of a pressure "
                    "difference and nothing else."},
            {"text": "Because breathing out uses a higher pressure than "
                     "breathing in does, so it overtakes the incoming air.",
             "correct": False,
             "why": "Nothing overtakes anything — the two never happen at "
                    "once. On a breath in the pressure inside is the lower of "
                    "the two, and on a breath out it is the higher."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-02-h05",
        "band": "harder",
        "text": "Atmospheric pressure of about 101 kPa presses on every "
                "square centimetre of your chest. Explain why your chest is "
                "not crushed by it.",
        "options": [
            {"text": "The ribs are strong enough to take all of it on their "
                     "own.",
             "correct": False,
             "why": "The ribs would not manage it if the pressure were "
                    "one-sided. What saves you is that it is not one-sided — "
                    "there is air inside you at almost exactly the same "
                    "pressure."},
            {"text": "Air is far too light to press with any real force on "
                     "something as solid as a chest.",
             "correct": False,
             "why": "Air presses very hard indeed: 101 kPa over the area of a "
                    "chest is an enormous total push. It is balanced rather "
                    "than small."},
            {"text": "The diaphragm holds the pressure out by staying "
                     "contracted all the time, even between breaths.",
             "correct": False,
             "why": "The diaphragm relaxes between breaths, and nothing is "
                    "being held out. The air inside the chest is doing the "
                    "balancing, not a muscle."},
            {"text": "The air inside the chest is at almost the same "
                     "pressure, pushing out too.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h06",
        "band": "harder",
        "text": "However hard you try, you cannot drink through a straw ten "
                "metres long. Explain why, using what makes air move.",
        "options": [
            {"text": "Your mouth cannot make a strong enough vacuum to pull "
                     "that much liquid all the way up the straw.",
             "correct": False,
             "why": "This still describes a pull. You are never pulling: you "
                    "enlarge your mouth cavity, and the atmosphere pushes the "
                    "drink up for you."},
            {"text": "The atmosphere does the pushing, and it can only push "
                     "a column so high.",
             "correct": True},
            {"text": "The liquid is too heavy to move at all in a tube that "
                     "long.",
             "correct": False,
             "why": "It moves perfectly well in the first few metres. The "
                    "limit is not the weight by itself but the fact that the "
                    "atmosphere's push is a fixed size."},
            {"text": "Friction against the inside of the straw stops the "
                     "drink before it reaches the top.",
             "correct": False,
             "why": "Friction slows a drink down but does not set a height "
                    "limit. Even a perfectly smooth straw would fail at the "
                    "same sort of height."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h07",
        "band": "harder",
        "text": "A patient's intercostal muscles are paralysed, but their "
                "diaphragm still works normally. Predict what happens to "
                "their breathing.",
        "options": [
            {"text": "They cannot breathe at all, because the ribs must move "
                     "for the chest to change size.",
             "correct": False,
             "why": "The diaphragm changes the volume of the chest on its own "
                    "by flattening. It is the larger of the two contributions "
                    "to quiet breathing."},
            {"text": "Their breathing is unaffected, because the intercostals "
                     "do nothing while at rest.",
             "correct": False,
             "why": "The intercostals do work at rest — roughly a third of "
                    "quiet breathing. Losing them is not nothing."},
            {"text": "They can still breathe, but the chest enlarges less, so "
                     "each breath is shallower.",
             "correct": True},
            {"text": "They can breathe in but not out, because the ribs are "
                     "needed to squeeze the chest.",
             "correct": False,
             "why": "A quiet breath out needs no muscles at all — the "
                    "stretched chest recoils elastically. Breathing out is the "
                    "half that survives most easily."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h08",
        "band": "harder",
        "text": "At rest a chest holds 2.4 litres of air at 101.0 kPa. On a "
                "breath in the volume becomes 2.9 litres and the pressure "
                "inside falls to 100.7 kPa. What pressure difference is "
                "driving the air in?",
        "options": [
            {"text": "0.3 kPa", "correct": True},
            {"text": "0.5 kPa", "correct": False,
             "why": "0.5 is the change in volume, in litres. That is the "
                    "cause, and the question asks for the pressure difference "
                    "that resulted from it."},
            {"text": "100.7 kPa", "correct": False,
             "why": "That is the new pressure inside, not a difference. A "
                    "difference is what is left when you take one pressure "
                    "away from the other."},
            {"text": "201.7 kPa", "correct": False,
             "why": "The two pressures have been added instead of subtracted. "
                    "Adding them describes nothing physical — air responds to "
                    "the gap between them."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h09",
        "band": "harder",
        "text": "A frog has no diaphragm and no ribs that move. It fills its "
                "lungs by closing its mouth and raising the floor of its "
                "mouth to push air down. How does that compare with the way "
                "you breathe in?",
        "options": [
            {"text": "It is the same mechanism, because both end with air "
                     "arriving in the lungs.",
             "correct": False,
             "why": "The same result does not make it the same mechanism. One "
                    "raises the pressure at the mouth; the other lowers the "
                    "pressure in the chest."},
            {"text": "The frog is pulling air in, whereas your muscles push "
                     "it in.",
             "correct": False,
             "why": "Both halves are back to front. Nothing pulls air anywhere "
                    "— and it is the frog, not you, whose muscles push the "
                    "air along."},
            {"text": "The frog has no need of a pressure difference, because "
                     "it moves the air directly.",
             "correct": False,
             "why": "Raising the floor of the mouth is exactly how the frog "
                    "makes a pressure difference. Air never moves without "
                    "one."},
            {"text": "The frog raises the pressure behind the air; you lower "
                     "the pressure in front of it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h10",
        "band": "harder",
        "text": "Someone is sealed inside a rigid airtight box just bigger "
                "than their body, with one tube running from their mouth to "
                "the air outside. Predict what happens when they try to "
                "breathe in.",
        "options": [
            {"text": "They breathe normally, because the tube gives them all "
                     "the fresh air they need.",
             "correct": False,
             "why": "The tube does supply air, but supply is never what starts "
                    "a breath. The chest has to make room first, and inside a "
                    "sealed box it cannot."},
            {"text": "Their chest can barely enlarge, because the air sealed "
                     "around it has nowhere to go.",
             "correct": True},
            {"text": "Air is forced into them, because the box holds the "
                     "outside air at a higher pressure.",
             "correct": False,
             "why": "The air in the box sits at ordinary pressure, and nothing "
                    "raises it until the chest tries to move. Nothing is being "
                    "forced anywhere."},
            {"text": "They can breathe out but not in, because a rigid box "
                     "has no give in it at all.",
             "correct": False,
             "why": "Both halves of the breath meet the same wall. Making the "
                    "chest smaller would mean stretching the box's sealed air "
                    "into a bigger space, which is no easier."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h11",
        "band": "harder",
        "text": "When you blow hard, the pressure inside your chest goes well "
                "above atmospheric. Explain how, given that the lungs contain "
                "no muscle at all.",
        "options": [
            {"text": "The lungs contract harder than usual, which is what "
                     "raises the pressure.",
             "correct": False,
             "why": "A lung cannot contract at any effort level, because there "
                    "is no muscle in one. Everything that squeezes it is "
                    "outside it."},
            {"text": "The elastic recoil of the lungs is stronger when you "
                     "have taken a deeper breath.",
             "correct": False,
             "why": "Recoil does return a stretched chest to its resting size, "
                    "and no further. Blowing hard takes the chest smaller than "
                    "resting, which recoil alone can never do."},
            {"text": "Muscles outside the lungs contract to make the chest "
                     "smaller than its resting size.",
             "correct": True},
            {"text": "The diaphragm contracts hard and pushes upwards against "
                     "the lungs.",
             "correct": False,
             "why": "Contracting flattens the diaphragm downwards and enlarges "
                    "the chest — the movement for a breath in. It rises when "
                    "it relaxes."},
        ],
        "figure": None,
    },

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-02-e12",
        "band": "easier",
        "text": "What does the word ventilation mean?",
        "options": [
            {"text": "Moving air in and out of the lungs.",
             "correct": True},
            {"text": "The reaction inside cells that releases energy from "
                     "glucose, which is going on all the time.",
             "correct": False,
             "why": "That is respiration, and it happens in every cell. "
                    "Ventilation is the muscular job of getting air to the "
                    "lungs and back out again."},
            {"text": "Warming and cleaning the air on its way down.",
             "correct": False,
             "why": "The airway does treat the air on its way past, but "
                    "that is not what the word means. Ventilation is the "
                    "movement itself."},
            {"text": "Breathing out only, since breathing in has its own "
                     "name.",
             "correct": False,
             "why": "Ventilation covers both halves of the cycle. There is "
                    "one word for the whole job of moving air in and out."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e13",
        "band": "easier",
        "text": "What is meant by elastic recoil?",
        "options": [
            {"text": "A muscle inside the lung shortening to squeeze the "
                     "air back out again.",
             "correct": False,
             "why": "There is no muscle inside a lung, so nothing in one "
                    "can shorten. Recoil needs no muscle at all — it is "
                    "stretched tissue springing back."},
            {"text": "The diaphragm contracting a second time to push the "
                     "air out.",
             "correct": False,
             "why": "Contracting the diaphragm flattens it and makes the "
                    "chest bigger, which is a breath in. Recoil happens "
                    "while the muscles are doing nothing."},
            {"text": "A stretched tissue springing back to its resting size "
                     "on its own.",
             "correct": True},
            {"text": "Air bouncing back off the bottom of the lungs once it "
                     "has run out of room to travel any further.",
             "correct": False,
             "why": "Air does not bounce. The air leaves because the "
                    "stretched chest springs back and makes the space "
                    "smaller."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e14",
        "band": "easier",
        "text": "A balloon hangs from a tube inside the bell jar. Which "
                "part of the body is it there to play?",
        "options": [
            {"text": "The chest wall.",
             "correct": False,
             "why": "The rigid glass jar plays that part. The balloon is "
                    "the soft, hollow thing the air ends up inside."},
            {"text": "A lung.",
             "correct": True},
            {"text": "The diaphragm.",
             "correct": False,
             "why": "The rubber sheet underneath is the diaphragm. That is "
                    "the part your hand moves, and the balloon responds to "
                    "it."},
            {"text": "The airway running from the mouth down into the "
                     "chest.",
             "correct": False,
             "why": "That is the tube through the lid. The balloon sits on "
                    "the end of the tube, in the position a lung takes."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e15",
        "band": "easier",
        "text": "The glass wall of the bell jar cannot move at all. Which "
                "part of a real body is it standing in for?",
        "options": [
            {"text": "The diaphragm, which forms the floor of the chest and "
                     "is the part that does most of the moving.",
             "correct": False,
             "why": "The rubber sheet across the bottom is the diaphragm. "
                    "The glass is the part that does not move."},
            {"text": "The skin of the chest, which is why the model is made "
                     "of something you can see through.",
             "correct": False,
             "why": "The model is not about skin. The jar takes the place "
                    "of the chest wall and ribcage, which enclose the lungs "
                    "on every side except below."},
            {"text": "The air outside the body, pressing inwards.",
             "correct": False,
             "why": "The air outside is simply the air in the room around "
                    "the jar. The jar is the boundary the lungs sit inside."},
            {"text": "The chest wall and ribcage, which enclose the lungs.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e16",
        "band": "easier",
        "text": "A tube passes through the lid of the bell jar. What job is "
                "that tube doing in the model?",
        "options": [
            {"text": "It is the airway, letting outside air reach the "
                     "balloon.",
             "correct": True},
            {"text": "It holds the balloon up so that it cannot drop to the "
                     "bottom of the jar.",
             "correct": False,
             "why": "It does hold the balloon, but that is not what it "
                    "stands for. Its job in the model is to be the route "
                    "the air takes in and out."},
            {"text": "It lets air in and out of the jar itself, so that the "
                     "pressure in the jar matches the room.",
             "correct": False,
             "why": "The jar has to be sealed, or the pressure inside it "
                    "could never change and the balloon would never "
                    "inflate. The tube opens into the balloon, not into the "
                    "jar."},
            {"text": "It is the diaphragm, because it is the only part of "
                     "the model that moves.",
             "correct": False,
             "why": "Nothing about the tube moves. The rubber sheet at the "
                    "bottom is the diaphragm, and it is the part your hand "
                    "works."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e17",
        "band": "easier",
        "text": "Name the muscles that do the work of a quiet breath in.",
        "options": [
            {"text": "The lungs and the diaphragm.",
             "correct": False,
             "why": "A lung is not a muscle and contains none. The pair "
                    "that does the work is the diaphragm and the "
                    "intercostals."},
            {"text": "The muscles of the throat and mouth, which narrow and "
                     "widen the air's way in.",
             "correct": False,
             "why": "Those shape the opening the air passes through, but "
                    "they do not change the volume of the chest, and the "
                    "volume is where a breath starts."},
            {"text": "The diaphragm, underneath the lungs, and the "
                     "intercostal muscles between the ribs.",
             "correct": True},
            {"text": "The diaphragm on its own.",
             "correct": False,
             "why": "It does most of it, but not all. The intercostals "
                    "swing the ribs up and out at the same time, which is "
                    "about a third of a quiet breath."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e18",
        "band": "easier",
        "text": "What do your ribs do while you are breathing in?",
        "options": [
            {"text": "They stay completely still until the breath is over.",
             "correct": False,
             "why": "They swing on every breath. Holding them still would "
                    "remove about a third of the movement a quiet breath "
                    "depends on."},
            {"text": "They swing upwards and outwards.",
             "correct": True},
            {"text": "They squeeze inwards to press on the lungs and push "
                     "the air along the airway.",
             "correct": False,
             "why": "Pressing inwards makes the chest smaller, which forces "
                    "air out. That is the movement of a breath out, not a "
                    "breath in."},
            {"text": "They drop downwards to make room underneath for the "
                     "diaphragm.",
             "correct": False,
             "why": "The ribs drop when you breathe out. On the way in they "
                    "lift, and the diaphragm makes its own room by "
                    "flattening."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e19",
        "band": "easier",
        "text": "During a quiet breath out the intercostal muscles relax. "
                "Describe the movement of the ribcage that follows.",
        "options": [
            {"text": "It stays exactly where it is until the next breath in "
                     "pulls it back down again.",
             "correct": False,
             "why": "Nothing holds it up once the muscles let go, and "
                    "nothing pulls it down later. It falls back as soon as "
                    "they relax."},
            {"text": "It lifts further up and out as the muscles let go.",
             "correct": False,
             "why": "Letting go cannot lift anything. Relaxing intercostals "
                    "let the ribs fall back, which makes the chest smaller."},
            {"text": "It swings outwards while the volume of the chest "
                     "stays the same.",
             "correct": False,
             "why": "Any movement of the ribcage changes the chest's "
                    "volume. On the way out it moves down and in, and the "
                    "volume falls."},
            {"text": "It drops down and in, so the chest gets smaller.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e20",
        "band": "easier",
        "text": "About how many breaths a minute does a Year 8 student take "
                "while sitting still?",
        "options": [
            {"text": "Between 12 and 18.",
             "correct": True},
            {"text": "Between 2 and 4.",
             "correct": False,
             "why": "That is far too slow — it would leave twenty seconds "
                    "between one breath and the next. A resting rate sits "
                    "at roughly 12 to 18."},
            {"text": "Between 60 and 80.",
             "correct": False,
             "why": "That is closer to a resting pulse. Breathing is far "
                    "slower than the heartbeat, at about 12 to 18 a minute."},
            {"text": "Between 100 and 120.",
             "correct": False,
             "why": "Nobody breathes twice a second at rest. There would be "
                    "no time for the chest to empty between breaths."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e21",
        "band": "easier",
        "text": "How do you measure someone's breathing rate?",
        "options": [
            {"text": "Count how many times their chest rises and falls in "
                     "one second.",
             "correct": False,
             "why": "One second is far too short — nearly everyone would "
                    "score nought or one. Counting over a whole minute "
                    "gives a number you can compare."},
            {"text": "Time how long a single breath lasts.",
             "correct": False,
             "why": "That is the length of one breath, not a rate. A rate "
                    "is how many breaths happen in a fixed time."},
            {"text": "Count the number of complete breaths, in and out, "
                     "that they take in one minute.",
             "correct": True},
            {"text": "Count every movement of the chest, both in and out, "
                     "over a minute and add them together.",
             "correct": False,
             "why": "That counts each breath twice. One breath is one "
                    "movement in and one movement out, together."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e22",
        "band": "easier",
        "text": "You start running. What happens to your breathing rate?",
        "options": [
            {"text": "It falls, because the body saves air for the muscles.",
             "correct": False,
             "why": "Air is not saved or stored. Working muscles need "
                    "oxygen delivered faster and carbon dioxide taken away "
                    "faster, so you breathe more often."},
            {"text": "It rises.",
             "correct": True},
            {"text": "It stays the same, and only the depth of each breath "
                     "changes.",
             "correct": False,
             "why": "The depth does increase, but so does the rate. Both go "
                    "up together during exercise."},
            {"text": "It rises for a few seconds and then settles below its "
                     "resting value.",
             "correct": False,
             "why": "It stays high for as long as the exercise lasts, and "
                    "only returns towards resting once you stop."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e23",
        "band": "easier",
        "text": "As well as breathing more often during exercise, what "
                "changes about each individual breath?",
        "options": [
            {"text": "It becomes shallower, so that the breaths can be "
                     "fitted in more quickly.",
             "correct": False,
             "why": "Rate and depth rise together. Shallower breaths would "
                    "move less air, which is the opposite of what a working "
                    "body needs."},
            {"text": "Nothing about the breath itself changes.",
             "correct": False,
             "why": "Each breath gets deeper as well as more frequent, "
                    "because the chest is enlarged further than it is at "
                    "rest."},
            {"text": "It takes in the same volume but holds it for longer.",
             "correct": False,
             "why": "Air is not held during exercise. A bigger volume moves "
                    "in, and straight back out again."},
            {"text": "It becomes deeper, so more air moves in and out.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e24",
        "band": "easier",
        "text": "In which part of the body does respiration take place?",
        "options": [
            {"text": "In every cell.",
             "correct": True},
            {"text": "In the lungs, which is why breathing and respiration "
                     "are two words for one thing.",
             "correct": False,
             "why": "They are two words for two different things. "
                    "Respiration is a chemical reaction inside cells; "
                    "breathing is the muscular job of moving air."},
            {"text": "In the chest, wherever air happens to be moving.",
             "correct": False,
             "why": "Moving air is ventilation. Respiration releases energy "
                    "inside cells, and it carries on whether air is moving "
                    "at that moment or not."},
            {"text": "In the blood, on the way from the lungs to the "
                     "muscles.",
             "correct": False,
             "why": "The blood carries what respiration needs, but the "
                    "reaction happens inside the cells it delivers to."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e25",
        "band": "easier",
        "text": "While air is flowing into your lungs, how does the "
                "pressure inside your chest compare with the pressure of "
                "the air outside you?",
        "options": [
            {"text": "Higher inside than outside.",
             "correct": False,
             "why": "Air always moves from higher pressure to lower. If the "
                    "inside were higher, air would be on its way out."},
            {"text": "Exactly equal, which is what lets the air through.",
             "correct": False,
             "why": "Equal pressures mean no net movement at all — that is "
                    "the still moment between two breaths."},
            {"text": "Lower inside than outside.",
             "correct": True},
            {"text": "Lower inside, but only once the air has arrived and "
                     "settled in the chest.",
             "correct": False,
             "why": "The pressure falls first, because the chest has "
                    "enlarged, and the air moves in afterwards because of "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e26",
        "band": "easier",
        "text": "What does the diaphragm do when it relaxes, and what does "
                "that do to the chest?",
        "options": [
            {"text": "It flattens downwards, which makes the chest bigger.",
             "correct": False,
             "why": "Flattening is what contracting does. A relaxed "
                    "diaphragm returns to its dome and the chest gets "
                    "smaller."},
            {"text": "It domes back upwards into the chest, so the volume "
                     "of the chest decreases and air is pushed out.",
             "correct": True},
            {"text": "It stays flat, and the ribs do the rest.",
             "correct": False,
             "why": "It springs back to its dome every time it relaxes. "
                    "Left flat, the chest could never return to its resting "
                    "size."},
            {"text": "It moves downwards again, though more slowly than it "
                     "did on the way in, and not quite so far.",
             "correct": False,
             "why": "It does not move down at all when it relaxes — it "
                    "rises. Down is the direction it takes when it "
                    "contracts."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e27",
        "band": "easier",
        "text": "A student says the lungs suck air in. What is actually "
                "pushing air into your lungs?",
        "options": [
            {"text": "The lungs, once they have expanded far enough to make "
                     "room for it.",
             "correct": False,
             "why": "A lung can neither push nor pull, because there is no "
                    "muscle in one. It is stretched by the space around it "
                    "growing."},
            {"text": "The diaphragm, which drives the air down the airway "
                     "ahead of itself.",
             "correct": False,
             "why": "The diaphragm moves downwards, away from the airway. "
                    "It makes room; it never touches the air that arrives."},
            {"text": "Nothing pushes — a low pressure pulls the air along.",
             "correct": False,
             "why": "There is no pull. A low pressure is simply a place "
                    "where fewer particles are pushing back, so the ones "
                    "outside win."},
            {"text": "The air outside, at the higher pressure.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e28",
        "band": "easier",
        "text": "Roughly what volume of air moves in and out of your lungs "
                "in one quiet breath?",
        "options": [
            {"text": "About half a litre.",
             "correct": True},
            {"text": "About five litres, which is roughly what a chest can "
                     "hold altogether.",
             "correct": False,
             "why": "Five litres is closer to the total a chest holds after "
                    "the deepest breath possible. A quiet breath moves "
                    "about a tenth of that."},
            {"text": "About two millilitres.",
             "correct": False,
             "why": "Two millilitres is less than a teaspoon. A quiet "
                    "breath moves roughly half a litre, some 250 times "
                    "more."},
            {"text": "About fifty litres.",
             "correct": False,
             "why": "Fifty litres is about the volume of a large suitcase. "
                    "No chest can change its volume by anything like that."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e29",
        "band": "easier",
        "text": "In what unit is a person's breathing rate given?",
        "options": [
            {"text": "Litres of air moved per breath.",
             "correct": False,
             "why": "That is the depth of a breath — how much air moves "
                    "each time — rather than how often a breath happens."},
            {"text": "Breaths per minute.",
             "correct": True},
            {"text": "Complete breaths per second.",
             "correct": False,
             "why": "The count is taken over a minute, because at rest a "
                    "person takes fewer than one breath every three "
                    "seconds."},
            {"text": "Kilopascals per breath.",
             "correct": False,
             "why": "Kilopascals measure pressure, which is what drives the "
                    "air. The rate counts how often the whole cycle "
                    "happens."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e30",
        "band": "easier",
        "text": "Ten minutes after finishing a run, what has happened to a "
                "student's breathing rate?",
        "options": [
            {"text": "It has stayed at its exercise value, because the "
                     "muscles worked hard.",
             "correct": False,
             "why": "The rate is set by what the body needs now, not by "
                    "what it did earlier. Once the demand drops, so does "
                    "the rate."},
            {"text": "It has dropped below its resting value, to make up "
                     "for the exercise.",
             "correct": False,
             "why": "There is nothing to make up. Breathing settles back to "
                    "its resting value and stays there."},
            {"text": "It has fallen back towards its resting value.",
             "correct": True},
            {"text": "It has risen further, because the effects of exercise "
                     "keep building up afterwards.",
             "correct": False,
             "why": "The rate peaks during the exercise, or just after it, "
                    "and then falls. It does not keep climbing once you "
                    "stop."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e31",
        "band": "easier",
        "text": "What is the name of the muscles that lie between the ribs?",
        "options": [
            {"text": "The intercostal muscles.",
             "correct": True},
            {"text": "The diaphragm, which is the sheet of muscle filling "
                     "the gaps between the ribs.",
             "correct": False,
             "why": "The diaphragm is a single sheet lying underneath the "
                    "lungs, not a set of muscles between the ribs."},
            {"text": "The bronchial muscles.",
             "correct": False,
             "why": "The bronchi are tubes inside the lungs, and they are "
                    "nowhere near the gaps between the ribs."},
            {"text": "The cartilage muscles.",
             "correct": False,
             "why": "Cartilage is not muscle at all — it is the stiff "
                    "tissue that keeps the airway open."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-e32",
        "band": "easier",
        "text": "No air at all is moving in or out of your lungs. What must "
                "be true about the pressure inside your chest?",
        "options": [
            {"text": "It is zero.",
             "correct": False,
             "why": "There is still air in the chest, and its particles are "
                    "still pushing on every surface. Zero would mean no air "
                    "at all."},
            {"text": "It is higher than outside, which is what holds the "
                     "air still.",
             "correct": False,
             "why": "A higher pressure inside sends air out. Nothing stays "
                    "still while there is a difference."},
            {"text": "It is lower than outside, and the airway is holding "
                     "the air back.",
             "correct": False,
             "why": "A lower pressure inside brings air in. If nothing is "
                    "moving, there is no difference to move it."},
            {"text": "It is equal to the pressure of the air outside.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-02-s12",
        "band": "standard",
        "text": "A student counts 34 complete breaths in 2 minutes while "
                "sitting still. Calculate their breathing rate in breaths "
                "per minute.",
        "options": [
            {"text": "68 breaths per minute.",
             "correct": False,
             "why": "That multiplies by the two minutes instead of dividing "
                    "by them. Halve 34 to get the rate for one minute."},
            {"text": "17 breaths per minute.",
             "correct": True},
            {"text": "34 breaths per minute.",
             "correct": False,
             "why": "That is the total for the whole two minutes. A rate is "
                    "always for one minute, so it must be halved."},
            {"text": "8.5 breaths per minute.",
             "correct": False,
             "why": "That divides by four rather than by two. There are two "
                    "minutes in the count, not four."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s13",
        "band": "standard",
        "text": "Someone takes 15 breaths a minute and each breath moves "
                "0.5 litres of air. Calculate the volume of air passing in "
                "and out of their lungs in one minute.",
        "options": [
            {"text": "30 litres.",
             "correct": False,
             "why": "That divides 15 by 0.5 instead of multiplying. Fifteen "
                    "lots of half a litre come to 7.5 litres."},
            {"text": "15.5 litres.",
             "correct": False,
             "why": "The rate and the depth are added there. They have to "
                    "be multiplied: each of the 15 breaths carries 0.5 "
                    "litres."},
            {"text": "75 litres.",
             "correct": False,
             "why": "That is ten times too big — a slipped decimal point. "
                    "15 × 0.5 is 7.5, not 75."},
            {"text": "7.5 litres.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s14",
        "band": "standard",
        "text": "In an investigation into breathing, why should each "
                "student's rate be counted three times and a mean taken?",
        "options": [
            {"text": "Because breathing rate varies a little from minute to "
                     "minute, and a mean of three counts is closer to the "
                     "true value.",
             "correct": True},
            {"text": "Because one count is always wrong, and three counts "
                     "cannot all be wrong at once.",
             "correct": False,
             "why": "A single count is not automatically wrong, and three "
                    "can certainly all be out. Repeating is about reducing "
                    "the effect of ordinary variation."},
            {"text": "Because three counts added together give a bigger "
                     "number that is easier to compare.",
             "correct": False,
             "why": "A mean is not a total, and a bigger number is no "
                    "easier to compare. The point is to get nearer the true "
                    "value."},
            {"text": "Because the rate rises with each count, so three "
                     "readings show the trend.",
             "correct": False,
             "why": "Sitting still and counting does not drive the rate up "
                    "each time. Any rise like that would be a fault in the "
                    "method, not the result you want."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s15",
        "band": "standard",
        "text": "Before testing how exercise changes breathing, why must "
                "each student's resting rate be recorded first?",
        "options": [
            {"text": "So that every student begins the exercise breathing "
                     "at exactly the same rate as everyone else.",
             "correct": False,
             "why": "You cannot make two people's resting rates match, and "
                    "you do not need to. What matters is how far each "
                    "person's own rate moves."},
            {"text": "Because the resting rate is the result the "
                     "investigation is looking for.",
             "correct": False,
             "why": "The result is the change caused by exercise. The "
                    "resting rate is the starting point that change is "
                    "measured from."},
            {"text": "So that the change caused by the exercise can be "
                     "worked out for each person separately.",
             "correct": True},
            {"text": "So that anyone who happens to be breathing unusually "
                     "quickly can be left out of the results.",
             "correct": False,
             "why": "A high resting rate is data, not a fault. Removing "
                    "someone because you dislike their starting value "
                    "biases the whole set."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s16",
        "band": "standard",
        "text": "Explain why asking someone to count their own breaths "
                "gives an unreliable result.",
        "options": [
            {"text": "Thinking about your breathing changes it, so the rate "
                     "counted is not the normal one.",
             "correct": True},
            {"text": "It is impossible to feel your own chest moving "
                     "without putting a hand on it.",
             "correct": False,
             "why": "Most people can feel their own breathing perfectly "
                    "well. The trouble is that noticing it alters it."},
            {"text": "Breathing rate is always higher sitting down than "
                     "standing up, so the figure means nothing.",
             "correct": False,
             "why": "Sitting usually gives a slightly lower rate, not a "
                    "higher one, and either way the position is something "
                    "you can keep the same."},
            {"text": "You cannot count and breathe at the same time.",
             "correct": False,
             "why": "Breathing carries on without any attention at all. The "
                    "problem is that attention changes its rate and depth."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s17",
        "band": "standard",
        "text": "Explain why your breathing rate rises when you exercise.",
        "options": [
            {"text": "Your lungs tire, so they have to work more often to "
                     "hold the same amount of air.",
             "correct": False,
             "why": "A lung does no work and cannot tire — it has no "
                    "muscle. The rate rises because the demand on the body "
                    "has risen."},
            {"text": "Your muscles are respiring faster, so oxygen has to "
                     "arrive more quickly and carbon dioxide has to leave "
                     "more quickly.",
             "correct": True},
            {"text": "The air becomes thinner as you move through it, so "
                     "each breath contains less.",
             "correct": False,
             "why": "Moving through air does not thin it. The air you "
                    "breathe running is the same air you breathe sitting "
                    "down."},
            {"text": "The warm chest becomes more elastic, so it springs "
                     "back more often.",
             "correct": False,
             "why": "Recoil returns the chest to its resting size; it does "
                    "not set how often you breathe. The demand of the "
                    "muscles does."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s18",
        "band": "standard",
        "text": "A student says exercise changes only how often you "
                "breathe. State the other change and say why it matters.",
        "options": [
            {"text": "Nothing else changes, because rate is the only thing "
                     "a body can alter.",
             "correct": False,
             "why": "The depth changes too. The muscles can enlarge the "
                    "chest further, and that moves more air per breath."},
            {"text": "The air moves in faster, but the volume each time "
                     "stays the same, so nothing is gained.",
             "correct": False,
             "why": "The volume does change. Deeper breaths are the second "
                    "half of how the body moves more air."},
            {"text": "Each breath becomes deeper, so more air moves each "
                     "time as well as more often.",
             "correct": True},
            {"text": "The breaths become shallower, and the extra rate "
                     "makes up for it.",
             "correct": False,
             "why": "Rate and depth rise together during exercise. "
                    "Shallower breaths would work against the very thing "
                    "the body is trying to do."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s19",
        "band": "standard",
        "text": "Explain why breathing out quietly costs almost no effort "
                "while breathing in always costs some.",
        "options": [
            {"text": "Breathing out uses the lungs' own muscle, which is "
                     "far stronger than the diaphragm and does the whole "
                     "job of emptying the chest easily.",
             "correct": False,
             "why": "A lung has no muscle of any strength. What empties it "
                    "is the stretched chest springing back."},
            {"text": "Air leaves more easily than it arrives because it is "
                     "warmer and lighter on the way out.",
             "correct": False,
             "why": "Warmth is not what moves it. Air leaves because the "
                    "chest gets smaller and the pressure inside rises."},
            {"text": "Both cost the same effort — a breath out only feels "
                     "easier than it is.",
             "correct": False,
             "why": "A quiet breath out really does cost nothing: the "
                    "muscles stop working and elasticity does the rest."},
            {"text": "Breathing in needs muscles to enlarge the chest, "
                     "while breathing out is those same muscles relaxing "
                     "and the stretched chest springing back.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s20",
        "band": "standard",
        "text": "A cough drives air out far faster than a quiet breath out. "
                "Explain what the muscles must be doing.",
        "options": [
            {"text": "Muscles contract to squeeze the chest smaller than "
                     "its resting size, taking the pressure inside well "
                     "above atmospheric.",
             "correct": True},
            {"text": "The diaphragm contracts as hard as it can, driving "
                     "the air upwards through the airway and out of the "
                     "chest at speed.",
             "correct": False,
             "why": "Contracting flattens the diaphragm downwards and "
                    "enlarges the chest, which is a breath in. Emptying the "
                    "chest needs it to rise."},
            {"text": "The lungs contract suddenly, which is what makes the "
                     "noise.",
             "correct": False,
             "why": "A lung cannot contract at all. The noise comes from "
                    "air forced past the vocal cords at speed."},
            {"text": "Elastic recoil is stronger because the chest was "
                     "stretched further first.",
             "correct": False,
             "why": "Recoil only ever returns the chest to its resting "
                    "size. A cough takes it smaller than that, which needs "
                    "muscle."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s21",
        "band": "standard",
        "text": "Blowing out the candles on a cake takes a hard, fast "
                "breath out. How does it differ from the breath out you "
                "take between two sentences?",
        "options": [
            {"text": "The diaphragm is pulled further down first, so that "
                     "there is a larger supply of air in the chest to use.",
             "correct": False,
             "why": "A deeper breath in does help, but nothing pulls the "
                    "diaphragm — it flattens itself. The real difference is "
                    "on the way out, where muscles now push."},
            {"text": "Muscles actively squeeze the chest below its resting "
                     "size, instead of letting it recoil to it.",
             "correct": True},
            {"text": "The lungs squeeze themselves much harder than usual, "
                     "in the way a fist tightens around something.",
             "correct": False,
             "why": "There is no muscle in a lung, at any effort level. "
                    "Everything that squeezes one is outside it."},
            {"text": "There is no difference inside the chest at all — the "
                     "air simply leaves faster through a much smaller "
                     "opening.",
             "correct": False,
             "why": "Pursed lips do speed the jet up, but the pressure "
                    "behind it has to be raised by muscles first, and a "
                    "quiet breath out never does that."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s22",
        "band": "standard",
        "text": "A heavy rucksack is rested on the chest of someone lying "
                "on their back. Predict the effect on their breathing and "
                "explain it.",
        "options": [
            {"text": "No effect at all, because the diaphragm sits well "
                     "underneath the lungs and is not covered by the "
                     "rucksack.",
             "correct": False,
             "why": "Enlarging the chest lifts the chest wall as well, and "
                    "the ribs cannot swing up freely with a weight sitting "
                    "on them."},
            {"text": "Breathing becomes easier, because the weight of the "
                     "rucksack helps to press the air down into the chest.",
             "correct": False,
             "why": "Pressing on the chest makes it smaller, which drives "
                    "air out. Nothing about a weight helps air in."},
            {"text": "Each breath in is smaller, because the muscles must "
                     "now lift the weight as well as enlarge the chest.",
             "correct": True},
            {"text": "The lungs have to work harder to pull against the "
                     "weight.",
             "correct": False,
             "why": "The lungs do no work in the first place. The extra "
                    "load falls on the diaphragm and the intercostals."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s23",
        "band": "standard",
        "text": "A very tight belt is done up around someone's waist. "
                "Explain why a deep breath in becomes difficult.",
        "options": [
            {"text": "The diaphragm cannot flatten fully, because "
                     "flattening pushes the contents of the abdomen down "
                     "and out.",
             "correct": True},
            {"text": "The belt squeezes the lungs directly, so they are "
                     "unable to expand.",
             "correct": False,
             "why": "The lungs sit well above a waist belt, inside the "
                    "ribcage. What the belt reaches is the abdomen below "
                    "the diaphragm."},
            {"text": "The belt stops the ribs from swinging up and out.",
             "correct": False,
             "why": "A belt at the waist is below the ribcage, so the ribs "
                    "can still swing. It is the diaphragm's movement that "
                    "is blocked."},
            {"text": "The belt raises the pressure of the air outside the "
                     "body.",
             "correct": False,
             "why": "Nothing you wear changes atmospheric pressure. The "
                    "belt limits movement, not the air."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s24",
        "band": "standard",
        "text": "On the bell-jar model you push the rubber sheet upwards "
                "into the jar. Predict what the balloon does, and say why.",
        "options": [
            {"text": "It deflates, because the space in the jar shrinks and "
                     "the pressure there rises above the air outside.",
             "correct": True},
            {"text": "It inflates further, because pushing forces air along "
                     "the tube and into it.",
             "correct": False,
             "why": "Your hand pushes the sheet, not the air. The volume "
                    "changes first, the pressure second, and the air "
                    "responds last."},
            {"text": "Nothing happens, because only pulling the sheet can "
                     "change the pressure.",
             "correct": False,
             "why": "Any movement of the sheet changes the volume, and any "
                    "change of volume changes the pressure. The direction "
                    "decides which way the air goes."},
            {"text": "It inflates either way, because the sheet moving at "
                     "all is what fills it, whichever direction it takes.",
             "correct": False,
             "why": "The direction matters. Moving the sheet inwards makes "
                    "the space smaller, and a smaller space empties the "
                    "balloon."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s25",
        "band": "standard",
        "text": "The bell jar has no ribs and no intercostal muscles. Give "
                "the reason it is still a good model of breathing.",
        "options": [
            {"text": "Because the ribs contribute nothing to a quiet breath "
                     "anyway, so nothing has been lost.",
             "correct": False,
             "why": "The ribs supply roughly a third of quiet breathing. "
                    "The model leaves out something real, and you have to "
                    "know that it has."},
            {"text": "It isolates one variable, so the effect of the "
                     "diaphragm on its own can be seen clearly.",
             "correct": True},
            {"text": "Because a model is always simpler than the real "
                     "thing, so whatever it leaves out is acceptable.",
             "correct": False,
             "why": "Leaving out the wrong thing ruins a model. This one "
                    "works because you can say exactly what is missing and "
                    "account for it."},
            {"text": "Because a model can never be checked against the real "
                     "body, so its faults do not matter.",
             "correct": False,
             "why": "Models are checked against reality constantly — that "
                    "is how their limits get named. Knowing where one stops "
                    "being true is what makes it usable."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s26",
        "band": "standard",
        "text": "Explain what a person is doing, in terms of muscles and "
                "pressure, while they hold their breath.",
        "options": [
            {"text": "They keep the pressure inside the chest down at zero "
                     "until the moment they choose to breathe again.",
             "correct": False,
             "why": "The chest is still full of air pushing on every "
                    "surface, so the pressure is nowhere near zero. It is "
                    "simply not changing."},
            {"text": "They stop the air outside the body from pressing in "
                     "on them for a few seconds at a time, deliberately.",
             "correct": False,
             "why": "Nothing can switch atmospheric pressure off. Holding a "
                    "breath only stops the difference across the airway "
                    "from being made."},
            {"text": "They hold the chest at a fixed volume with the airway "
                     "closed, so no pressure difference is made.",
             "correct": True},
            {"text": "Their lungs grip the air, which is what stops it "
                     "escaping.",
             "correct": False,
             "why": "A lung cannot grip anything. The air stays put because "
                    "the way out is closed and the volume is not changing."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s27",
        "band": "standard",
        "text": "You block the nozzle of a syringe with a thumb and draw "
                "the plunger out a little. Explain what happens to the "
                "trapped air and how it matches a breath in.",
        "options": [
            {"text": "The air particles grow bigger to fill the new space "
                     "they are given, so the pressure inside stays exactly "
                     "as it was.",
             "correct": False,
             "why": "Particles never change size, and no new ones appear. "
                    "The same particles simply spread out and hit the walls "
                    "less often."},
            {"text": "Air is pulled in past the plunger to fill the gap.",
             "correct": False,
             "why": "The syringe is sealed, so nothing gets in. That is "
                    "exactly why the pressure has to fall."},
            {"text": "The pressure rises, because the air inside is being "
                     "stretched.",
             "correct": False,
             "why": "Air is not a sheet that can be stretched. Spreading "
                    "the same particles through more space lowers the "
                    "pressure."},
            {"text": "The same air now fills a bigger space, so its "
                     "pressure falls — just as the chest's does when the "
                     "diaphragm flattens.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s28",
        "band": "standard",
        "text": "Explain why it is fair to say the atmosphere does the work "
                "of every breath and your muscles only make room.",
        "options": [
            {"text": "Muscles change the volume of the chest, and the air "
                     "is then pushed in by the pressure of the atmosphere.",
             "correct": True},
            {"text": "Because the atmosphere presses down on you hard "
                     "enough to force your diaphragm to move down and out "
                     "of the way.",
             "correct": False,
             "why": "The diaphragm moves because you contract it. The "
                    "atmosphere's job begins once the room has been made."},
            {"text": "Because your muscles are too weak to shift air on "
                     "their own.",
             "correct": False,
             "why": "Strength is not the issue. The muscles never act on "
                    "the air at all — they act on the chest."},
            {"text": "Because the air pulls itself in along the pressure "
                     "difference.",
             "correct": False,
             "why": "Air is pushed, never pulled. A pressure difference is "
                    "one side winning a pushing contest."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s29",
        "band": "standard",
        "text": "Student A takes 15 breaths a minute of 0.5 litres. Student "
                "B takes 30 breaths a minute of 0.25 litres. Compare the "
                "volume of air each moves in a minute.",
        "options": [
            {"text": "Student B moves twice as much, because they breathe "
                     "twice as often.",
             "correct": False,
             "why": "The rate is doubled but the depth is halved, so the "
                    "two changes cancel. Both move 7.5 litres."},
            {"text": "They move the same volume, 7.5 litres each.",
             "correct": True},
            {"text": "Student A moves twice as much, because their breaths "
                     "are twice as deep.",
             "correct": False,
             "why": "Depth alone does not decide it. Student B makes up for "
                    "shallower breaths by taking twice as many."},
            {"text": "Student B moves 15 litres and Student A moves 7.5 "
                     "litres.",
             "correct": False,
             "why": "That doubles B's rate without halving their depth. 30 "
                    "× 0.25 is 7.5, the same as 15 × 0.5."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s30",
        "band": "standard",
        "text": "In mouth-to-mouth rescue breathing, air is blown into a "
                "patient's lungs. Explain how that differs from the way the "
                "patient would normally breathe in.",
        "options": [
            {"text": "There is no difference — air enters a chest the same "
                     "way whatever moves it.",
             "correct": False,
             "why": "The difference in pressure is made in a different "
                    "place. Normally the chest end is lowered; here the "
                    "outside end is raised."},
            {"text": "The patient's own diaphragm is doing the work as "
                     "usual, helped along by the extra air the rescuer "
                     "supplies.",
             "correct": False,
             "why": "Rescue breathing is used precisely because the "
                    "patient's muscles are not working. The rescuer "
                    "supplies all of the pressure."},
            {"text": "The air is pushed in at a pressure above atmospheric, "
                     "instead of moving in because the chest has enlarged "
                     "first.",
             "correct": True},
            {"text": "The lungs are inflated by their own elastic recoil.",
             "correct": False,
             "why": "Recoil empties a stretched lung; it never fills one. "
                    "And a lung has no way of inflating itself."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s31",
        "band": "standard",
        "text": "After running up the stairs a student says, “I am "
                "respiring faster.” Is that a fair thing to say?",
        "options": [
            {"text": "No — respiring is simply another word for breathing, "
                     "so the sentence adds nothing extra at all.",
             "correct": False,
             "why": "They are different words for different things. "
                    "Respiration is a reaction in cells; breathing moves "
                    "air."},
            {"text": "No — respiration happens only in the lungs, and the "
                     "lungs themselves cannot speed up or slow down.",
             "correct": False,
             "why": "Respiration happens in every cell, not in the lungs. "
                    "The muscle cells that did the running are respiring "
                    "hardest."},
            {"text": "Yes, because respiring is the word for moving air "
                     "quickly in and out.",
             "correct": False,
             "why": "The conclusion is right for the wrong reason. "
                    "Respiring is the chemical reaction in the cells, not "
                    "the air movement."},
            {"text": "Yes — their cells really are respiring faster, and "
                     "that is why they are breathing faster too.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-s32",
        "band": "standard",
        "text": "A class investigates how one minute of step-ups changes "
                "breathing rate. Which variable must be kept the same for "
                "every student?",
        "options": [
            {"text": "The number of steps taken each minute during the "
                     "exercise.",
             "correct": True},
            {"text": "The resting breathing rate that each student happens "
                     "to start from.",
             "correct": False,
             "why": "You cannot set another person's resting rate, and you "
                    "should not try. It is recorded as each student's own "
                    "starting point."},
            {"text": "The height of each student taking part.",
             "correct": False,
             "why": "Height cannot be controlled by the experimenter at "
                    "all. The variable you can fix is how hard the exercise "
                    "is."},
            {"text": "The number of breaths counted in the minute after the "
                     "exercise.",
             "correct": False,
             "why": "That is the result of the investigation. Fixing it "
                    "would leave nothing to find out."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-02-h12",
        "band": "harder",
        "text": "A resting adult takes 18 breaths a minute, each moving "
                "0.45 litres of air. Calculate the volume of air passing "
                "through their lungs in one hour.",
        "options": [
            {"text": "8.1 litres.",
             "correct": False,
             "why": "That is the volume for one minute. The question asks "
                    "for an hour, so it must be multiplied by 60."},
            {"text": "27 litres.",
             "correct": False,
             "why": "That multiplies the depth by 60 and forgets the rate "
                    "entirely. Work out the volume per minute first, then "
                    "scale it up."},
            {"text": "486 litres.",
             "correct": True},
            {"text": "48.6 litres.",
             "correct": False,
             "why": "That is ten times too small — a lost power of ten. 18 "
                    "× 0.45 × 60 comes to 486."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h13",
        "band": "harder",
        "text": "After identical exercise, Student A's breathing rate is "
                "back to resting after 2 minutes and Student B's after 5. "
                "Evaluate what that suggests.",
        "options": [
            {"text": "Student A is likely to be the fitter, because their "
                     "body cleared the extra demand of the exercise more "
                     "quickly.",
             "correct": True},
            {"text": "Student B is fitter, because their body kept working "
                     "hard for longer afterwards.",
             "correct": False,
             "why": "Needing longer to recover means the demand took longer "
                    "to settle. A quick return is the sign of fitness, not "
                    "a slow one."},
            {"text": "Nothing can be said, because fitness has no effect on "
                     "breathing.",
             "correct": False,
             "why": "Fitness shows up clearly in how fast breathing returns "
                    "to resting, which is why recovery time is measured at "
                    "all."},
            {"text": "Student A must have worked less hard, which is why "
                     "their rate came down sooner.",
             "correct": False,
             "why": "The exercise was identical for both, so effort is not "
                    "what separates them. The difference is in how quickly "
                    "each body recovered."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h14",
        "band": "harder",
        "text": "At the summit of a high mountain the air pressure is about "
                "55 kPa rather than 101 kPa. Explain why each breath "
                "delivers less air to the chest than it would at sea level.",
        "options": [
            {"text": "The muscles cannot enlarge the chest at all, because "
                     "there is too little pressure outside to push back "
                     "against them.",
             "correct": False,
             "why": "Muscles enlarge the chest whatever is outside it. The "
                    "chest still expands by the usual amount up there."},
            {"text": "The chest still enlarges by the same amount, but the "
                     "air that fills it holds fewer particles in every "
                     "litre.",
             "correct": True},
            {"text": "Air travels the other way at that pressure, leaving "
                     "the chest rather than entering it, until the two "
                     "pressures match.",
             "correct": False,
             "why": "Enlarging the chest still drops the pressure inside "
                    "below the 55 kPa outside, so air still travels "
                    "inwards."},
            {"text": "The lungs have to pull very much harder than usual, "
                     "because there is far less air up there for them to "
                     "take hold of.",
             "correct": False,
             "why": "A lung neither pulls nor grips — it has no muscle. "
                    "What changes is how much air a given volume contains."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h15",
        "band": "harder",
        "text": "An iron lung lowers the pressure in a sealed tank around "
                "the body; a modern ventilator blows air down a tube. In "
                "which is the chest pressure below atmospheric as air "
                "enters?",
        "options": [
            {"text": "The iron lung, because the chest is enlarged first "
                     "and room air is then pushed in through the mouth.",
             "correct": True},
            {"text": "Both of them, because air only ever enters a chest "
                     "whose pressure has fallen below atmospheric pressure.",
             "correct": False,
             "why": "Air enters whenever there is a difference the right "
                    "way round. A ventilator makes that difference by "
                    "raising the outside end instead of lowering the inside "
                    "one."},
            {"text": "The ventilator, because a tube in the airway lowers "
                     "the pressure inside the chest.",
             "correct": False,
             "why": "The tube raises the pressure at the airway, above "
                    "atmospheric, which is exactly how it drives air in."},
            {"text": "Neither, because in both machines the chest stays at "
                     "atmospheric pressure throughout.",
             "correct": False,
             "why": "Air cannot move at all without a difference. Each "
                    "machine creates one, at opposite ends of the airway."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h16",
        "band": "harder",
        "text": "A plastic bottle with its base cut off, a balloon inside "
                "on a straw, and a rubber glove stretched across the open "
                "base. Compare this with the bell jar as a model of "
                "breathing.",
        "options": [
            {"text": "It is better, because a bottle is closer to the shape "
                     "of a real chest than a jar is.",
             "correct": False,
             "why": "Shape is not what either model is for. Both stand or "
                    "fall on showing that changing the volume changes the "
                    "pressure."},
            {"text": "It is worse, because a bottle cannot be sealed "
                     "properly, so the pressure inside it can never change "
                     "at all.",
             "correct": False,
             "why": "Stretching the glove over the cut base seals it. Once "
                    "sealed, moving the glove changes the pressure exactly "
                    "as the rubber sheet does."},
            {"text": "It is not a model of breathing at all, because it "
                     "contains nothing at all playing the part of a "
                     "diaphragm underneath.",
             "correct": False,
             "why": "The glove is the diaphragm — it is the part you move, "
                    "and the part that changes the volume inside."},
            {"text": "It works on exactly the same principle, and shares "
                     "the same fault: rigid sides that cannot move as ribs "
                     "do.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h17",
        "band": "harder",
        "text": "At one instant the pressure inside a person's chest is "
                "101.4 kPa and the air around them is at 101.0 kPa. State "
                "which way air is moving and what the muscles have just "
                "done.",
        "options": [
            {"text": "Air is moving out, because the chest has been made "
                     "smaller and the pressure inside has risen.",
             "correct": True},
            {"text": "Air is moving in, because the pressure inside the "
                     "chest is the higher of the two figures given.",
             "correct": False,
             "why": "Air travels from high pressure to low. A higher "
                    "pressure inside sends air outwards, not inwards."},
            {"text": "No air is moving, because 0.4 kPa is far too small a "
                     "difference to shift anything.",
             "correct": False,
             "why": "Quiet breathing runs on differences under 1 kPa. Small "
                    "differences move air perfectly well across a large "
                    "area."},
            {"text": "Air is moving out, because the diaphragm has "
                     "contracted and flattened.",
             "correct": False,
             "why": "The direction is right but the cause is wrong. "
                    "Flattening enlarges the chest and lowers the pressure; "
                    "here the diaphragm has relaxed."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h18",
        "band": "harder",
        "text": "With each breath a person's chest volume goes from 2.4 "
                "litres to 3.0 litres and back. They take 14 breaths a "
                "minute. Calculate the volume of air moved in one minute.",
        "options": [
            {"text": "42 litres.",
             "correct": False,
             "why": "That uses the full 3.0 litres in the chest. Only the "
                    "change of 0.6 litres actually moves in and out."},
            {"text": "8.4 litres.",
             "correct": True},
            {"text": "33.6 litres.",
             "correct": False,
             "why": "That uses the resting 2.4 litres, which stays in the "
                    "chest the whole time. The air that moves is the "
                    "difference between the two volumes."},
            {"text": "1.2 litres.",
             "correct": False,
             "why": "That counts the breath twice and forgets the rate. One "
                    "breath moves 0.6 litres in and the same 0.6 litres "
                    "out, and there are 14 of them."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h19",
        "band": "harder",
        "text": "A student moves 7.2 litres of air a minute while taking 16 "
                "breaths a minute. Calculate the volume of one breath.",
        "options": [
            {"text": "115.2 litres.",
             "correct": False,
             "why": "That multiplies where the equation has to be "
                    "rearranged. Divide the volume per minute by the number "
                    "of breaths."},
            {"text": "2.2 litres.",
             "correct": False,
             "why": "That divides 16 by 7.2, which is the division the "
                    "wrong way round. It is 7.2 ÷ 16."},
            {"text": "0.45 litres.",
             "correct": True},
            {"text": "4.5 litres.",
             "correct": False,
             "why": "The digits are right but the power of ten is out. A "
                    "single breath of 4.5 litres would be close to the "
                    "whole capacity of a chest."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h20",
        "band": "harder",
        "text": "A condition stiffens the rib joints so that the ribs "
                "barely move, while the diaphragm and the lungs stay "
                "healthy. Predict the effect on breathing and justify it.",
        "options": [
            {"text": "Breathing stops entirely, because the chest can no "
                     "longer change its volume.",
             "correct": False,
             "why": "The diaphragm can still flatten, and that alone "
                    "changes the volume. Breathing continues, just with "
                    "less of it."},
            {"text": "Breathing is unaffected, because the lungs themselves "
                     "are perfectly healthy.",
             "correct": False,
             "why": "Healthy lungs cannot help — they have no muscle. What "
                    "matters is how much the chest around them can move."},
            {"text": "Breathing carries on completely unchanged, because "
                     "the diaphragm does all of the work in a quiet breath "
                     "anyway.",
             "correct": False,
             "why": "The diaphragm does about two thirds of a quiet breath, "
                    "not all of it. Losing the ribs' share is a real loss."},
            {"text": "Breathing continues, but each breath is smaller, "
                     "because roughly a third of the usual volume change is "
                     "lost.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h21",
        "band": "harder",
        "text": "Fluid gathers in the space between one lung and the chest "
                "wall, taking up room there. The lung, the airway and the "
                "muscles are all healthy. Predict what happens to that "
                "lung.",
        "options": [
            {"text": "It cannot fill properly, because the space it would "
                     "expand into is already occupied.",
             "correct": True},
            {"text": "It fills normally, because the muscles are healthy "
                     "and can still enlarge the chest.",
             "correct": False,
             "why": "Enlarging the chest is not enough if something else is "
                    "already in the room the lung needs."},
            {"text": "It expands further than usual, because the fluid "
                     "presses it open from the outside.",
             "correct": False,
             "why": "Pressing on a lung from outside squashes it. Only a "
                    "lower pressure around a lung lets it fill."},
            {"text": "It empties completely, in just the way it would if "
                     "air had entered that space instead.",
             "correct": False,
             "why": "Air opens the space to the outside and destroys the "
                    "pressure difference altogether. Fluid takes up room "
                    "but leaves the chest sealed, so the lung is squashed "
                    "rather than emptied."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h22",
        "band": "harder",
        "text": "During hard exercise the volume, the pressure and the "
                "airflow of every breath all change. State the one thing "
                "about the mechanism that does not change.",
        "options": [
            {"text": "The order of events changes, because the air now has "
                     "to move first in order to keep up with the demand.",
             "correct": False,
             "why": "The order never changes. Muscles, then volume, then "
                    "pressure, then air — at any rate of breathing."},
            {"text": "Air still moves from higher pressure to lower "
                     "pressure; only the size of the difference changes.",
             "correct": True},
            {"text": "Nothing stays the same, because exercise breathing "
                     "works by a different mechanism.",
             "correct": False,
             "why": "It is the same mechanism throughout, worked harder. "
                    "There is no second way of getting air into a chest."},
            {"text": "The diaphragm now draws the air in directly, rather "
                     "than making room for it.",
             "correct": False,
             "why": "The diaphragm never acts on the air, at any intensity. "
                    "It only ever changes the volume of the chest."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h23",
        "band": "harder",
        "text": "To find out whether the diaphragm or the ribs do more of a "
                "quiet breath, a student proposes strapping the ribs still "
                "and measuring the air moved. Evaluate that method.",
        "options": [
            {"text": "It is a good method, because holding the ribs still "
                     "takes the diaphragm out of the experiment.",
             "correct": False,
             "why": "Strapping the ribs leaves the diaphragm working — that "
                    "is the whole point of the test. It removes the ribs' "
                    "share, not the diaphragm's."},
            {"text": "It cannot work, because the ribs and the diaphragm "
                     "always move by exactly the same amount.",
             "correct": False,
             "why": "They contribute unequally, which is why the question "
                    "is worth asking: the diaphragm supplies roughly two "
                    "thirds of a quiet breath."},
            {"text": "It is sound in principle, but a strap tight enough to "
                     "stop the ribs would also restrict the abdomen the "
                     "diaphragm has to push into.",
             "correct": True},
            {"text": "It is pointless, because the lungs and not the "
                     "muscles decide how much air moves.",
             "correct": False,
             "why": "The lungs decide nothing — they contain no muscle. The "
                    "volume moved is set entirely by the muscles around "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h24",
        "band": "harder",
        "text": "Someone tries to breathe quietly through a garden hose 1.5 "
                "m long that holds 0.9 litres of air. Explain why it fails.",
        "options": [
            {"text": "Air cannot travel that far along a narrow tube.",
             "correct": False,
             "why": "Air travels along tubes very readily. The trouble is "
                    "how much of it a quiet breath can move at once."},
            {"text": "The pressure difference a chest can make is too small "
                     "to shift air along 1.5 m.",
             "correct": False,
             "why": "Under 1 kPa moves air along an airway perfectly well, "
                    "and a hose is no harder. The limit here is volume, not "
                    "pressure."},
            {"text": "A quiet breath moves about 0.5 litres, less than the "
                     "hose holds, so they draw back the air they have just "
                     "breathed out.",
             "correct": True},
            {"text": "The hose seals itself as soon as the pressure inside "
                     "it falls.",
             "correct": False,
             "why": "A garden hose is far too stiff to close under such a "
                    "small pressure difference. It stays open throughout."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h25",
        "band": "harder",
        "text": "Evaluate the claim that a quiet breath out is simply a "
                "breath in run backwards.",
        "options": [
            {"text": "It is entirely correct, because the same muscles "
                     "simply move the other way.",
             "correct": False,
             "why": "Muscles do not move the other way — they only ever "
                    "contract or relax. Breathing out is the relaxing half."},
            {"text": "It is wrong, because a completely different set of "
                     "muscles moves the chest in each of the two "
                     "directions, one for each way.",
             "correct": False,
             "why": "In quiet breathing the same two muscle groups are "
                    "involved either way. Forcing air out is what recruits "
                    "extra muscles."},
            {"text": "The movements do reverse, but the causes do not: "
                     "breathing in is muscles contracting, and breathing "
                     "out is those muscles relaxing.",
             "correct": True},
            {"text": "It is wrong, because the air moves for a different "
                     "reason in each direction.",
             "correct": False,
             "why": "The reason is the same both times — a pressure "
                    "difference. What differs is how that difference is "
                    "produced."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h26",
        "band": "harder",
        "text": "A trained athlete breathes 10 times a minute at rest; an "
                "untrained person of the same size breathes 16 times. "
                "Suggest why the athlete manages on fewer breaths.",
        "options": [
            {"text": "Each of their breaths is deeper, so the same volume "
                     "of air is moved in fewer of them.",
             "correct": True},
            {"text": "Their cells need less oxygen than anyone else's cells "
                     "do, whatever they happen to be doing.",
             "correct": False,
             "why": "A resting body of a given size has much the same "
                    "demand either way. What differs is how efficiently the "
                    "air is moved."},
            {"text": "Their lungs hold more muscle, so each breath is more "
                     "powerful.",
             "correct": False,
             "why": "No lung holds any muscle, trained or not. Training "
                    "strengthens the diaphragm and the intercostals around "
                    "them."},
            {"text": "Their breathing rate is lower because their lungs are "
                     "smaller and hold rather less air than usual.",
             "correct": False,
             "why": "Smaller lungs would force more breaths, not fewer. The "
                    "athlete moves more air per breath, not less."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h27",
        "band": "harder",
        "text": "The bell jar has four faults: rigid sides, a balloon in "
                "place of a lung, a flat sheet instead of a dome, and "
                "nothing alive. Which matters least for a lesson on "
                "ventilation?",
        "options": [
            {"text": "The rigid sides, because the ribs contribute nothing "
                     "to a quiet breath.",
             "correct": False,
             "why": "The ribs supply roughly a third of quiet breathing, so "
                    "leaving them out costs the model a real part of the "
                    "mechanism."},
            {"text": "The flat sheet, because the direction the sheet "
                     "travels is wrong as well as its shape.",
             "correct": False,
             "why": "The direction is right — down on the way in. The shape "
                    "is wrong about the very muscle this lesson is "
                    "teaching, so it is not the fault that matters least."},
            {"text": "The balloon in place of a lung, because this model is "
                     "about moving air rather than what happens to it "
                     "afterwards.",
             "correct": True},
            {"text": "Nothing alive, because a model of a mechanism never "
                     "needs to resemble living tissue at all in order for "
                     "it to be useful.",
             "correct": False,
             "why": "Missing recoil matters a great deal here, since recoil "
                    "is what drives a quiet breath out. That fault is not "
                    "the harmless one."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h28",
        "band": "harder",
        "text": "At rest a person takes 12 breaths a minute of 0.5 litres. "
                "During hard exercise they take 30 breaths a minute of 2.0 "
                "litres. Calculate how many times greater their ventilation "
                "becomes.",
        "options": [
            {"text": "2.5 times greater, because that is how much the rate "
                     "has risen.",
             "correct": False,
             "why": "The rate is only half the story. The depth has risen "
                    "four times as well, and the two multiply together."},
            {"text": "4 times greater, because that is how much the depth "
                     "has risen.",
             "correct": False,
             "why": "Depth alone leaves out the rate, which has risen 2.5 "
                    "times. Multiply the two increases together."},
            {"text": "60 times greater, because 60 litres a minute now move "
                     "through the lungs.",
             "correct": False,
             "why": "Sixty litres a minute is the new value, not the "
                    "increase. Compare it with the 6 litres a minute at "
                    "rest."},
            {"text": "10 times greater.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h29",
        "band": "harder",
        "text": "The bell-jar model reads −0.8 kPa for the pressure inside. "
                "A student says the jar must contain a vacuum. Explain why "
                "they are wrong.",
        "options": [
            {"text": "The reading is measured against atmospheric pressure, "
                     "so it means 0.8 kPa below about 101 kPa — still "
                     "almost a full atmosphere.",
             "correct": True},
            {"text": "A negative pressure cannot exist anywhere in nature, "
                     "so the model must simply have gone wrong somewhere in "
                     "its readings.",
             "correct": False,
             "why": "The minus sign is not a negative pressure. It is a "
                    "reading below the reference the scale is quoted from."},
            {"text": "They are right: any pressure below zero is a vacuum "
                     "by definition.",
             "correct": False,
             "why": "The zero on this scale is atmospheric pressure, not "
                    "empty space. A true vacuum would read about −101 kPa "
                    "on it."},
            {"text": "It means the jar holds 0.8 kPa of air, which is very "
                     "nearly a vacuum.",
             "correct": False,
             "why": "The figure is a difference, not a total. The air in "
                    "the jar is at roughly 100.2 kPa."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h30",
        "band": "harder",
        "text": "A newborn baby breathes about 40 times a minute; an adult "
                "about 14. Suggest why the baby's rate is so much higher.",
        "options": [
            {"text": "The baby's diaphragm is stronger, so it is able to "
                     "work a great deal faster than a grown adult's can.",
             "correct": False,
             "why": "A baby's muscles are far weaker, not stronger. The "
                    "high rate makes up for how little each breath can "
                    "move."},
            {"text": "A baby's chest is far smaller, so each breath moves "
                     "very little air and more of them are needed.",
             "correct": True},
            {"text": "Babies have no intercostal muscles of their own yet, "
                     "so the diaphragm has to do all of the work quickly.",
             "correct": False,
             "why": "Babies have intercostal muscles from birth. The "
                    "difference is the size of the chest, not a missing "
                    "muscle group."},
            {"text": "The air nearer the floor, where a baby usually lies, "
                     "is thinner than the air higher up.",
             "correct": False,
             "why": "Air in a room is the same at floor level as at head "
                    "height. Nothing about the position explains the rate."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h31",
        "band": "harder",
        "text": "To save time, a student counts breaths for 15 seconds and "
                "multiplies by four. Evaluate that against counting for a "
                "full minute.",
        "options": [
            {"text": "It is more accurate, because a shorter count leaves "
                     "less room for a mistake.",
             "correct": False,
             "why": "A shorter count does not reduce error; it magnifies "
                    "it, because whatever you miscount gets multiplied by "
                    "four."},
            {"text": "It is exactly as good, because multiplying afterwards "
                     "puts back everything that the shorter count left out.",
             "correct": False,
             "why": "Multiplying restores the scale but not the "
                    "information. It scales the error up with the reading."},
            {"text": "It gives a quicker result, but a miscount of one "
                     "breath becomes an error of four in the final figure.",
             "correct": True},
            {"text": "It cannot work at all, because breathing rate is only "
                     "defined over a whole minute.",
             "correct": False,
             "why": "A rate can be found from any interval and then scaled. "
                    "The objection is about precision, not about "
                    "definition."},
        ],
        "figure": None,
    },
    {
        "id": "b4-02-h32",
        "band": "harder",
        "text": "A spacesuit holds its wearer's air at about 30 kPa instead "
                "of the usual 101 kPa. Explain whether the wearer can still "
                "breathe in.",
        "options": [
            {"text": "No — a pressure that low has no power to push air "
                     "anywhere.",
             "correct": False,
             "why": "Any pressure pushes. All that is needed is for the "
                    "pressure in the chest to be lower still, and enlarging "
                    "the chest sees to that."},
            {"text": "Yes, but only because the lungs then pull very much "
                     "harder than usual in order to make up the whole "
                     "difference.",
             "correct": False,
             "why": "Lungs never pull, at any pressure. The conclusion is "
                    "right but the mechanism given for it does not exist."},
            {"text": "No — air moves into a chest only when the pressure of "
                     "the air outside it is about 101 kPa, as it is on "
                     "Earth.",
             "correct": False,
             "why": "There is nothing special about 101 kPa. What matters "
                    "is that the outside pressure is higher than the "
                    "pressure inside the chest."},
            {"text": "Yes — enlarging the chest still takes the pressure "
                     "inside below 30 kPa, so the suit's air is pushed in.",
             "correct": True},
        ],
        "figure": None,
    },
]
