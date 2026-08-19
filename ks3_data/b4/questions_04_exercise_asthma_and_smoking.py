# -*- coding: utf-8 -*-
"""B4 lesson 04 — Exercise, asthma and smoking: twelve questions (MRB-269).

The lesson makes one argument, and the bench is built on it: three factors act
on three different parts of one system. Exercise moves the breathing muscles
and leaves the airways, the alveoli and the blood untouched. An asthma attack
narrows the airways and leaves the exchange surface undamaged. Smoking hits the
alveoli, the airways and the blood at once, and only one of the three damages
is permanent. Every question here asks the student to locate a fault, or to
compare two factors that are easily blurred into "three things that are bad for
your lungs".

The distractors are built from the lesson's three declared misconceptions.
BREATH-09 ("being out of breath means your lungs cannot hold enough air")
supplies the volume answers — the sprinter's lungs still refilling, the trained
runner with bigger lungs, the emphysema patient whose lungs have "shrunk".
BREATH-10 ("during an asthma attack there is not enough oxygen in the air")
supplies every option that puts the fault in the air rather than in the route
to the alveoli, including the one that says breathing harder draws in richer
air. BREATH-11 ("tar is the harmful part of cigarette smoke") supplies the
options that make tar do carbon monoxide's job and vice versa. Three further
errors the lesson exists to correct are worked as well: that exercise widens
the airways or enlarges the alveoli, that emphysema is a narrowing, and that a
large sample is what turns a correlation into a cause.

No question restates a ladder rung. The rungs already own what the body detects
during exercise, which smoking damage is permanent, the inhaler explanation and
the emphysema volume-versus-transfer argument, so the bank works around all
four: the carbon dioxide trigger appears only as the reason hard breathing
continues after a sprint, permanence appears only inside distractors, and the
reliever is used as a diagnostic test on two patients rather than as an
explanation to be written out.

`figure` is `None` throughout — the lesson declares no figures, and every stem
here is self-contained.
"""

UNIT = "B4"
LESSON = "exercise-asthma-and-smoking"
LESSON_NUMBER = 4

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-04-e01",
        "band": "easier",
        "text": "An asthma attack acts on one part of the breathing system. "
                "Which part?",
        "options": [
            {"text": "The airways — the bronchioles narrow", "correct": True},
            {"text": "The alveoli — the exchange surface is damaged",
             "correct": False,
             "why": "The alveoli are undamaged during an attack. Damaged "
                    "alveoli is what years of smoking does, and unlike an "
                    "attack it does not reverse."},
            {"text": "The blood — it cannot carry the oxygen away",
             "correct": False,
             "why": "The blood is fine during an attack. Carbon monoxide from "
                    "smoke is the thing in this lesson that stops blood "
                    "carrying oxygen."},
            {"text": "The air — it holds less oxygen than usual",
             "correct": False,
             "why": "The air is still 21% oxygen, exactly as it was a minute "
                    "earlier. What has changed is the route to the alveoli, "
                    "not the air."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e02",
        "band": "easier",
        "text": "Cigarette smoke paralyses and then destroys the cilia lining "
                "the airways. What follows directly from that?",
        "options": [
            {"text": "The lungs can hold much less air than before",
             "correct": False,
             "why": "Cilia have nothing to do with how much air fits in. They "
                    "are tiny moving hairs that sweep mucus, and losing them "
                    "is a clearing problem."},
            {"text": "The bronchioles narrow because their muscle contracts",
             "correct": False,
             "why": "That is an asthma attack, and a reliever inhaler "
                    "reverses it. Cilia are hairs on the lining, not muscle "
                    "in the wall."},
            {"text": "Mucus has to be coughed out instead of swept out",
             "correct": True},
            {"text": "Less oxygen can dissolve across the alveolar wall",
             "correct": False,
             "why": "Cilia play no part in exchange. Smoking does reduce "
                    "exchange, but by breaking down alveolar walls, which is "
                    "a separate damage."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e03",
        "band": "easier",
        "text": "During hard exercise, what actually changes inside the "
                "breathing system?",
        "options": [
            {"text": "The bronchioles widen to let more air through",
             "correct": False,
             "why": "Exercise alters nothing about the airways. Widening a "
                    "bronchiole is what a reliever inhaler does, and only "
                    "because the muscle had contracted."},
            {"text": "The diaphragm and intercostals contract harder and more "
                     "often", "correct": True},
            {"text": "The alveoli get bigger, so more oxygen can cross",
             "correct": False,
             "why": "The alveoli are not altered by running. What changes is "
                    "how often the air inside them is refreshed, not their "
                    "size."},
            {"text": "The blood makes extra haemoglobin to carry more oxygen",
             "correct": False,
             "why": "Nothing about the blood is altered during a run. The one "
                    "thing in this lesson that changes what the blood can "
                    "carry is carbon monoxide."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e04",
        "band": "easier",
        "text": "Four substances in cigarette smoke do four different "
                "damages. Which one acts on the blood rather than on the "
                "lungs?",
        "options": [
            {"text": "Tar", "correct": False,
             "why": "Tar acts on the airways and the alveoli — it coats the "
                    "lining, destroys cilia, and its irritation drives the "
                    "inflammation that breaks down alveolar walls."},
            {"text": "Carbon monoxide", "correct": True},
            {"text": "Nicotine", "correct": False,
             "why": "Nicotine acts on the blood vessels and the heart, "
                    "narrowing vessels and raising heart rate and blood "
                    "pressure. It does not occupy haemoglobin."},
            {"text": "Particulates and heat", "correct": False,
             "why": "These irritate the airway lining directly, raising mucus "
                    "production at the same time as the cilia that would "
                    "clear it are being disabled."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-04-s01",
        "band": "standard",
        "text": "Someone runs 400 metres flat out, stops, and keeps breathing "
                "hard for several minutes afterwards. Why does the hard "
                "breathing carry on once they have stopped running?",
        "options": [
            {"text": "The lungs are still refilling after being emptied",
             "correct": False,
             "why": "Nothing measures how full your lungs are in order to set "
                    "the rate. Lung volume is almost never the limit, before "
                    "the run or after it."},
            {"text": "The muscles are still tired and are signalling the "
                     "brain", "correct": False,
             "why": "Breathing rate rises before any tiredness and stays "
                    "raised after you stop. It tracks a chemical in the "
                    "blood, not muscle fatigue."},
            {"text": "There is a backlog of carbon dioxide still to clear",
             "correct": True},
            {"text": "The blood ran out of oxygen and has to be refilled",
             "correct": False,
             "why": "Blood oxygen changes remarkably little during ordinary "
                    "exercise. Your brain stem monitors the waste product "
                    "instead, because it is the more sensitive signal."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s02",
        "band": "standard",
        "text": "During an attack a bronchiole narrows to about half its "
                "usual radius. Roughly what happens to the air flow through "
                "it?",
        "options": [
            {"text": "It drops to about a sixteenth of what it was",
             "correct": True},
            {"text": "It drops to about a half, in step with the radius",
             "correct": False,
             "why": "Flow does not track radius in step. It depends far more "
                    "steeply than that, which is exactly why a modest "
                    "narrowing has such a dramatic effect."},
            {"text": "It drops to about a quarter, in step with the area",
             "correct": False,
             "why": "Closer, but still nowhere near steep enough. Halving the "
                    "radius drops the flow around sixteenfold, not "
                    "fourfold."},
            {"text": "It barely changes, since the air is still 21% oxygen",
             "correct": False,
             "why": "The oxygen in the air was never the problem. What has "
                    "changed is how fast air can get down a tube that is now "
                    "half as wide."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s03",
        "band": "standard",
        "text": "A long-term smoker coughs most mornings. What is the cough "
                "doing?",
        "options": [
            {"text": "Forcing the collapsed alveolar walls back open",
             "correct": False,
             "why": "Lost alveolar walls never grow back, and coughing does "
                    "nothing to them. The morning cough is about mucus, not "
                    "about the exchange surface."},
            {"text": "Clearing carbon monoxide that built up overnight",
             "correct": False,
             "why": "Carbon monoxide sits on haemoglobin in the blood, not in "
                    "the airways, and it clears within about a day of the "
                    "last cigarette."},
            {"text": "Pulling in extra air because the lungs have shrunk",
             "correct": False,
             "why": "The lungs have not shrunk — a smoker's lung volume stays "
                    "close to normal. Being out of breath is not a shortage "
                    "of room for air."},
            {"text": "Clearing mucus the destroyed cilia can no longer sweep",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s04",
        "band": "standard",
        "text": "Breathing faster and deeper during exercise gets more oxygen "
                "across the alveolar wall each second. How?",
        "options": [
            {"text": "The air you breathe in contains more oxygen when you "
                     "breathe harder", "correct": False,
             "why": "The air is 21% oxygen whether you breathe hard or "
                    "gently. Breathing harder changes how often it is "
                    "replaced, not what is in it."},
            {"text": "Alveolar air is refreshed more often, keeping the "
                     "concentration difference steep", "correct": True},
            {"text": "The alveolar wall becomes thinner, so oxygen crosses "
                     "more quickly", "correct": False,
             "why": "The wall is one cell thick and stays that way. Exercise "
                    "changes the air on one side of it, not the barrier "
                    "itself."},
            {"text": "Extra alveoli open up, adding surface area for "
                     "exchange", "correct": False,
             "why": "You do not gain alveoli by running. Your surface area is "
                    "the same at the end of a sprint as it was at the "
                    "start."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-04-h01",
        "band": "harder",
        "text": "Two people the same age run together. One can go much "
                "further before becoming breathless. What most likely "
                "explains the difference?",
        "options": [
            {"text": "Their lungs are far larger and hold much more air",
             "correct": False,
             "why": "Trained athletes do not generally have much bigger lungs "
                    "than anyone else. Lung capacity is almost never what "
                    "runs out first."},
            {"text": "Their bronchioles are permanently wider than average",
             "correct": False,
             "why": "Airway width is not what training changes. That is the "
                    "variable an asthma attack alters and a reliever "
                    "restores, over minutes."},
            {"text": "Their muscles make almost no carbon dioxide when they "
                     "run", "correct": False,
             "why": "Working muscles respire faster and make more carbon "
                    "dioxide, trained or not. Their brain stem still detects "
                    "it and still raises the rate."},
            {"text": "Their heart, circulation and muscles use the delivered "
                     "oxygen better", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h02",
        "band": "harder",
        "text": "Doll and Hill could never run an experiment that made people "
                "smoke. Which of their findings did most to show smoking "
                "causes lung cancer, rather than merely going with it?",
        "options": [
            {"text": "The risk rose with the number smoked and fell when "
                     "people stopped", "correct": True},
            {"text": "They followed 40 000 doctors, which is a very large "
                     "sample", "correct": False,
             "why": "A big sample makes a correlation reliable, not causal. "
                    "It sharpens the link without showing which way the link "
                    "runs."},
            {"text": "Doll himself gave up smoking two years into his own "
                     "study", "correct": False,
             "why": "That is a scientist changing his mind on his own "
                    "evidence, which is rarer than it should be — but one "
                    "person's decision is not evidence about a cause."},
            {"text": "Smokers and non-smokers were surveyed in hospital in "
                     "1950", "correct": False,
             "why": "The hospital survey is where the link was first spotted. "
                    "A correlation seen once is where the case starts, not "
                    "where it is proved."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h03",
        "band": "harder",
        "text": "Two breathless patients are each given a reliever inhaler. "
                "One improves within minutes; the other does not improve at "
                "all. What can be concluded?",
        "options": [
            {"text": "The second patient's lungs have become too small to "
                     "hold enough air", "correct": False,
             "why": "Lung volume is almost never the limit — in emphysema it "
                    "stays close to normal. What is lost is exchange surface, "
                    "not room for air."},
            {"text": "The second patient is breathing air with less oxygen in "
                     "it", "correct": False,
             "why": "Both patients are breathing the same 21% oxygen. A "
                    "reliever contains no oxygen anyway — all it does is "
                    "relax airway muscle."},
            {"text": "The first has narrowed airways; the second's fault is "
                     "elsewhere", "correct": True},
            {"text": "The first patient's alveoli were damaged and have now "
                     "recovered", "correct": False,
             "why": "Alveolar walls do not grow back — that is the one "
                    "permanent damage here. A reliever widens a tube; it "
                    "cannot rebuild a surface."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h04",
        "band": "harder",
        "text": "An asthma attack and long-term emphysema both mean less "
                "oxygen reaches the blood. Which comparison of the two is "
                "right?",
        "options": [
            {"text": "Both destroy the alveoli, but emphysema does it more "
                     "slowly", "correct": False,
             "why": "An attack leaves the alveoli completely undamaged. That "
                    "is why it reverses in minutes with a reliever and "
                    "emphysema never reverses at all."},
            {"text": "Asthma blocks delivery to an undamaged surface; "
                     "emphysema destroys the surface", "correct": True},
            {"text": "Both narrow the bronchioles, but emphysema narrows them "
                     "for good", "correct": False,
             "why": "Emphysema is not a narrowing. Alveolar walls break down "
                    "and merge, so the volume stays similar while the surface "
                    "area falls sharply."},
            {"text": "Both reduce the oxygen in the air arriving at the "
                     "lungs", "correct": False,
             "why": "Neither touches the air, which stays at 21% oxygen "
                    "throughout. One blocks the route in; the other wrecks "
                    "the surface at the end of it."},
        ],
        "figure": None,
    },
]
