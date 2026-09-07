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
            {"text": "The pressure of the air around you, from its particles "
                     "colliding with surfaces.",
             "correct": True},
            {"text": "The pressure your lungs produce when they push air back "
                     "out again.",
             "correct": False,
             "why": "Your lungs produce no pressure of their own — they have "
                    "no muscle. Atmospheric pressure belongs to the air "
                    "outside you and is there whether you breathe or not."},
            {"text": "The force with which your diaphragm pulls air down into "
                     "the chest.",
             "correct": False,
             "why": "The diaphragm never pulls air anywhere. It changes the "
                    "volume of the chest, and the atmosphere outside does the "
                    "pushing."},
            {"text": "The weight of the air that is already sitting inside your "
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
            {"text": "The lungs contract to push the air, which they do not "
                     "do in a quiet breath.",
             "correct": False,
             "why": "A lung has no muscle, so it cannot contract at any time. "
                    "The extra effort comes from muscles outside the lungs."},
            {"text": "The diaphragm contracts harder, which is what forces "
                     "the air out.",
             "correct": False,
             "why": "Contracting the diaphragm flattens it and makes the chest "
                    "bigger, which is a breath in. Forcing air out needs the "
                    "chest to be made smaller than its resting size."},
            {"text": "Nothing is different — a hard breath out is just a "
                     "faster version of the same thing.",
             "correct": False,
             "why": "A quiet breath out costs no muscular effort at all: the "
                    "muscles relax and the stretched chest springs back. "
                    "Forcing air out is the version that needs work."},
            {"text": "Muscles contract to squeeze the chest smaller, instead "
                     "of relying on elastic recoil alone.",
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
            {"text": "The air arriving is richer, because a deep breath "
                     "reaches fresher air.",
             "correct": False,
             "why": "The air is the same air either way. What changes is how "
                    "much of it moves, and that depends on how far the muscles "
                    "enlarge the chest."},
            {"text": "The muscles contract harder, the volume grows more, and "
                     "the pressure falls further.",
             "correct": True},
            {"text": "The lungs stretch themselves further, which is what "
                     "makes the breath deeper.",
             "correct": False,
             "why": "The lungs never stretch themselves — they have no muscle. "
                    "They are stretched further because the space around them "
                    "has been made bigger."},
            {"text": "The air is pushed in faster, which is what enlarges the "
                     "chest further.",
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
                     "diaphragm for the patient.",
             "correct": False,
             "why": "The machine never touches the diaphragm. It raises the "
                    "pressure at the mouth end instead, which is a different "
                    "mechanism reaching the same result."},
            {"text": "The machine lowers the pressure in the lungs, exactly "
                     "as a diaphragm does.",
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
            {"text": "The machine raises the pressure at the mouth; a healthy "
                     "chest lowers the pressure inside.",
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
            {"text": "The ribs are strong enough to take the whole of it on "
                     "their own.",
             "correct": False,
             "why": "The ribs would not manage it if the pressure were "
                    "one-sided. What saves you is that it is not one-sided — "
                    "there is air inside you at almost exactly the same "
                    "pressure."},
            {"text": "Air is far too light to press hard on anything as solid "
                     "as a chest.",
             "correct": False,
             "why": "Air presses very hard indeed: 101 kPa over the area of a "
                    "chest is an enormous total push. It is balanced rather "
                    "than small."},
            {"text": "The diaphragm holds the pressure out by staying "
                     "contracted all the time.",
             "correct": False,
             "why": "The diaphragm relaxes between breaths, and nothing is "
                    "being held out. The air inside the chest is doing the "
                    "balancing, not a muscle."},
            {"text": "The air inside your chest is at almost the same "
                     "pressure, pushing out just as hard.",
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
            {"text": "Your mouth cannot make enough of a vacuum to pull that "
                     "much liquid up.",
             "correct": False,
             "why": "This still describes a pull. You are never pulling: you "
                    "enlarge your mouth cavity, and the atmosphere pushes the "
                    "drink up for you."},
            {"text": "All the pushing is done by the atmosphere, and it can "
                     "only push a column so high.",
             "correct": True},
            {"text": "The liquid is too heavy to move at all in a tube that "
                     "long.",
             "correct": False,
             "why": "It moves perfectly well in the first few metres. The "
                    "limit is not the weight by itself but the fact that the "
                    "atmosphere's push is a fixed size."},
            {"text": "Friction inside the straw stops the drink before it "
                     "gets to the top.",
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
]
