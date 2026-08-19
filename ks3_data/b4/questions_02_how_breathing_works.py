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
                     "reference everything else is quoted against.",
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
            {"text": "In both, the pressure around the lung can no longer be "
                     "made lower than the air outside.",
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
]
