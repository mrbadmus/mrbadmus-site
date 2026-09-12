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
            {"text": "Alveolar air is refreshed faster, keeping the "
                     "concentration difference steep", "correct": True},
            {"text": "The alveolar wall stretches thinner as the lungs fill, "
                     "so oxygen crosses faster", "correct": False,
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
            {"text": "Their lungs are far larger, so they hold much more air "
                     "with each breath",
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
            {"text": "Both destroy the alveoli, but emphysema does it far "
                     "more slowly and permanently", "correct": False,
             "why": "An attack leaves the alveoli completely undamaged. That "
                    "is why it reverses in minutes with a reliever and "
                    "emphysema never reverses at all."},
            {"text": "Asthma blocks delivery to an undamaged surface; "
                     "emphysema destroys it", "correct": True},
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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-04-e05",
        "band": "easier",
        "text": "Three things happen to a bronchiole during an asthma attack. "
                "Which set is right?",
        "options": [
            {"text": "The cartilage tightens, the lining dries out and the "
                     "cilia stop", "correct": False,
             "why": "Bronchioles have no cartilage at all — that is the "
                    "trachea and the bronchi. What they do have is muscle in "
                    "the wall, and it is that muscle which contracts."},
            {"text": "The walls thicken permanently, the tube shortens and "
                     "mucus dries", "correct": False,
             "why": "Nothing permanent happens in an attack, which is why a "
                    "reliever can reverse it within minutes. The changes are "
                    "muscle, swelling and mucus."},
            {"text": "The muscle contracts, the lining swells and extra mucus "
                     "is produced", "correct": True},
            {"text": "The alveoli merge, the airway widens and the blood "
                     "thickens", "correct": False,
             "why": "Merging alveoli is emphysema, from years of smoking, and "
                    "a widening airway is what a reliever produces. An attack "
                    "narrows the tube."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e06",
        "band": "easier",
        "text": "What is emphysema?",
        "options": [
            {"text": "Alveolar walls breaking down, so many small alveoli "
                     "merge into fewer large ones", "correct": True},
            {"text": "Bronchioles narrowing permanently, so far less air can "
                     "ever reach the alveoli", "correct": False,
             "why": "Emphysema is not a narrowing at all. The tubes are not "
                    "what is damaged — the exchange surface at the end of them "
                    "is."},
            {"text": "The lungs shrinking overall, so a good deal less air "
                     "fits in with every breath", "correct": False,
             "why": "Lung volume stays close to normal, and often rises. What "
                    "falls sharply is the surface area available for "
                    "exchange."},
            {"text": "Mucus filling up the alveoli, so oxygen has much "
                     "further to travel to the blood", "correct": False,
             "why": "Extra mucus is a separate smoking damage and it sits in "
                    "the airways. In emphysema the walls between alveoli are "
                    "destroyed."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e07",
        "band": "easier",
        "text": "Someone is running hard and breathing deeply. How does the "
                "air they are breathing in compare with the air they were "
                "breathing at rest?",
        "options": [
            {"text": "It contains more oxygen, which is why deep breathing "
                     "helps", "correct": False,
             "why": "The air is not altered by how you breathe it. Deep "
                    "breathing moves more air, not richer air."},
            {"text": "It contains less oxygen, because they are using it up "
                     "faster", "correct": False,
             "why": "You cannot use up the oxygen in the room by running "
                    "through it. Each breath still starts from about 21% "
                    "oxygen."},
            {"text": "It contains more carbon dioxide, breathed back in from "
                     "the last breath out", "correct": False,
             "why": "Exhaled air disperses long before the next breath. The "
                    "carbon dioxide that matters during exercise is in the "
                    "blood, not in the air."},
            {"text": "It is exactly the same air — still about 21% oxygen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e08",
        "band": "easier",
        "text": "What is a bronchiole?",
        "options": [
            {"text": "A tiny air sac where oxygen crosses out of the air into "
                     "the blood",
             "correct": False,
             "why": "That is an alveolus. A bronchiole is one of the tubes "
                    "carrying air towards the alveoli, and nothing crosses "
                    "into the blood along it."},
            {"text": "One of the smallest air tubes, with muscle in its wall "
                     "that narrows it", "correct": True},
            {"text": "The single wide tube running down the front of the "
                     "neck", "correct": False,
             "why": "That is the trachea, and it is held open by C-shaped "
                    "cartilage rings. Bronchioles are far narrower and lie "
                    "deep inside the lungs."},
            {"text": "A small blood vessel running across the outside surface "
                     "of an alveolus", "correct": False,
             "why": "That is a capillary, which carries blood. A bronchiole "
                    "carries air."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e09",
        "band": "easier",
        "text": "Which substance in cigarette smoke is the reason that "
                "stopping smoking is a medical matter rather than simply a "
                "decision?",
        "options": [
            {"text": "Tar", "correct": False,
             "why": "Tar does a great deal of damage to the airways and "
                    "alveoli, but it is not what makes stopping physically "
                    "difficult."},
            {"text": "Carbon monoxide", "correct": False,
             "why": "Carbon monoxide occupies haemoglobin and clears within "
                    "about a day of the last cigarette. It is dangerous "
                    "without being the substance people depend on."},
            {"text": "Nicotine", "correct": True},
            {"text": "Particulates and heat", "correct": False,
             "why": "These irritate the airway lining and raise mucus "
                    "production. Unpleasant, but not the cause of "
                    "dependence."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-e10",
        "band": "easier",
        "text": "Long-term smoking is the one factor here that damages more "
                "than one part of the system. Which parts does it reach?",
        "options": [
            {"text": "The airways, the alveoli and the blood",
             "correct": True},
            {"text": "The airways, the alveoli and the breathing muscles",
             "correct": False,
             "why": "The breathing muscles are the one part smoke leaves "
                    "alone — they are what exercise works. Carbon monoxide in "
                    "the smoke reaches the blood instead."},
            {"text": "The alveoli, the blood and the breathing muscles",
             "correct": False,
             "why": "Two of these are right, but the airways cannot be left "
                    "out: that is where the cilia are destroyed and the mucus "
                    "builds up. The muscles are untouched."},
            {"text": "The airways, the blood and the exchange surface only",
             "correct": False,
             "why": "The exchange surface IS the alveoli, so this names two "
                    "parts under three headings. Written properly it is the "
                    "airways, the alveoli and the blood."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-04-s05",
        "band": "standard",
        "text": "Someone gives up smoking, and over the following weeks their "
                "cough gets worse before it gets better. What is happening?",
        "options": [
            {"text": "The alveolar walls are already growing back, and the "
                     "new tissue irritates the lining", "correct": False,
             "why": "Lost alveolar walls never grow back — that is the one "
                    "permanent damage. The change behind the cough is in the "
                    "airway lining."},
            {"text": "Carbon monoxide is leaving the blood slowly, and it "
                     "irritates the airways on its way", "correct": False,
             "why": "Carbon monoxide clears within about a day, and it leaves "
                    "the body without producing a cough. Weeks later, "
                    "something else is going on."},
            {"text": "The airways are making a great deal more mucus now than "
                     "they did while smoking", "correct": False,
             "why": "Mucus production falls once the irritation stops. What "
                    "has changed is not how much is made but whether it can be "
                    "moved."},
            {"text": "The cilia are recovering, so mucus is being brought up "
                     "that had been sitting there", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s06",
        "band": "standard",
        "text": "A pupil recovering from a chest infection is producing a lot "
                "of mucus, but their cilia are healthy. How does their "
                "situation differ from a long-term smoker's?",
        "options": [
            {"text": "The pupil's alveoli are being damaged by the mucus, "
                     "while the smoker's are not", "correct": False,
             "why": "Mucus sits in the airways and damages no alveoli. It is "
                    "the smoker whose alveolar walls have been destroyed, and "
                    "not by mucus."},
            {"text": "The pupil's mucus can still be swept out; the smoker's "
                     "has to be coughed out", "correct": True},
            {"text": "The pupil has more mucus than the smoker, which is why "
                     "the infection is worse", "correct": False,
             "why": "How much mucus there is is not the difference that "
                    "matters. What matters is whether anything is able to "
                    "clear it."},
            {"text": "The smoker's bronchioles have narrowed, so the mucus "
                     "cannot get past", "correct": False,
             "why": "Narrowed bronchioles are an asthma attack, and a reliever "
                    "reverses them. The smoker's problem is destroyed cilia."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s07",
        "band": "standard",
        "text": "After the same sprint, a trained runner's breathing settles "
                "back to normal much sooner than an untrained runner's. What "
                "does that suggest?",
        "options": [
            {"text": "Their lungs are simply larger, so a single deep breath "
                     "clears the waste gas away much faster",
             "correct": False,
             "why": "Trained athletes do not generally have much larger lungs. "
                    "Lung size is almost never what decides how someone copes "
                    "with exercise."},
            {"text": "Their bronchioles are permanently wider, so the used "
                     "air can leave the chest far quicker", "correct": False,
             "why": "Airway width is what an asthma attack changes over "
                    "minutes, not what training changes. Recovery is about the "
                    "blood, not the tubes."},
            {"text": "They clear the carbon dioxide backlog sooner, because "
                     "heart and muscles work more efficiently",
             "correct": True},
            {"text": "Working muscles make no carbon dioxide at all during a "
                     "sprint, so no backlog ever forms",
             "correct": False,
             "why": "Working muscles always make carbon dioxide, trained or "
                    "not. Training changes how quickly the backlog is dealt "
                    "with, not whether there is one."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s08",
        "band": "standard",
        "text": "A reliever inhaler relaxes the airway muscle, and a "
                "bronchiole that had narrowed to half its usual radius "
                "returns to normal. Roughly what happens to the air flow "
                "through it?",
        "options": [
            {"text": "It rises to about sixteen times what it was before the "
                     "puff", "correct": True},
            {"text": "It rises to about twice what it was, in step with the "
                     "radius", "correct": False,
             "why": "Flow does not track radius in step. It depends far more "
                    "steeply than that, which is why so modest a widening "
                    "helps so much."},
            {"text": "It rises to about four times what it was, in step with "
                     "the area", "correct": False,
             "why": "Closer, but still nowhere near steep enough. Doubling the "
                    "radius raises flow around sixteenfold, not fourfold."},
            {"text": "It barely changes, because the oxygen in the air was "
                     "never the problem", "correct": False,
             "why": "The oxygen was indeed never the problem, but that is why "
                    "widening the tube works. The flow changes enormously."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s09",
        "band": "standard",
        "text": "A heavy smoker may have about a tenth of their haemoglobin "
                "occupied by carbon monoxide at any moment. Predict how they "
                "will find climbing several flights of stairs.",
        "options": [
            {"text": "No different, because their lungs take in the same "
                     "amount of air as anyone else's", "correct": False,
             "why": "Taking the air in is only half the job. Blood that can "
                    "carry less oxygen delivers less to the muscles, whatever "
                    "the lungs manage."},
            {"text": "Easier, because carbon monoxide makes the heart beat "
                     "faster and deliver more", "correct": False,
             "why": "Nicotine raises heart rate, and a faster heart pushing "
                    "oxygen-poor blood does not help. Carbon monoxide takes "
                    "red cells out of service."},
            {"text": "No different, because a reliever inhaler would widen "
                     "the airways if needed", "correct": False,
             "why": "The airways are not the problem here, so widening them "
                    "would change nothing. This damage is in the blood."},
            {"text": "Harder than expected, because their blood carries less "
                     "oxygen than it should", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-s10",
        "band": "standard",
        "text": "During an asthma attack the alveoli are completely "
                "undamaged. So why does less oxygen reach the blood?",
        "options": [
            {"text": "Because the alveoli depend on the airway muscle to pull "
                     "them open before they work", "correct": False,
             "why": "The alveoli need no help from the muscle in the airway "
                    "wall. They need air delivered to them, and that is what "
                    "has been interrupted."},
            {"text": "Because not enough air is getting through the narrowed "
                     "tubes to reach the surface", "correct": True},
            {"text": "Because the air being breathed in holds far less oxygen "
                     "than usual during an attack", "correct": False,
             "why": "The air is unchanged at about 21% oxygen. That is exactly "
                    "why an inhaler helps and an oxygen cylinder mostly does "
                    "not."},
            {"text": "Because the blood itself stops picking up any oxygen "
                     "while the airways stay narrow", "correct": False,
             "why": "The blood is perfectly capable throughout an attack. It "
                    "is a delivery problem in the tubes, not a carrying "
                    "problem in the blood."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-04-h05",
        "band": "harder",
        "text": "A faulty boiler leaks carbon monoxide into a house. A "
                "non-smoker living there becomes breathless on the stairs "
                "although a lung examination finds nothing wrong. Explain "
                "how both can be true.",
        "options": [
            {"text": "The gas has narrowed their bronchioles, and a narrowing "
                     "that slight would not show up", "correct": False,
             "why": "Narrowed bronchioles are exactly what an examination "
                    "would find, and carbon monoxide does not narrow them. "
                    "This damage is not in the lungs at all."},
            {"text": "The gas has destroyed alveolar walls, and that damage "
                     "takes years to show on a test", "correct": False,
             "why": "Destroyed alveolar walls are tar's slow damage, not "
                    "carbon monoxide's, and reduced gas transfer does show on "
                    "a test. Carbon monoxide acts within hours."},
            {"text": "The lungs are exchanging normally, but the blood "
                     "leaving them carries far less oxygen", "correct": True},
            {"text": "The air in the house holds far less oxygen, so less of "
                     "it can cross the alveolar wall", "correct": False,
             "why": "A leak of carbon monoxide does not measurably lower the "
                    "oxygen in a room. The harm is done after the oxygen "
                    "arrives, by a gas that occupies haemoglobin."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h06",
        "band": "harder",
        "text": "A runner trains at high altitude for a month and returns "
                "with more red blood cells than before. Which part of the "
                "system has changed, and would this help someone during an "
                "asthma attack?",
        "options": [
            {"text": "The blood, and no — an attack is a problem in the "
                     "airways", "correct": True},
            {"text": "The blood, and yes — more red cells would carry oxygen "
                     "past the narrowing", "correct": False,
             "why": "The part is right, the conclusion is not. If air cannot "
                    "reach the alveoli, extra carrying capacity has nothing to "
                    "collect."},
            {"text": "The alveoli, and yes — altitude adds exchange surface",
             "correct": False,
             "why": "You do not gain alveoli by training anywhere. Surface "
                    "area is fixed, and altitude changes what the blood "
                    "carries."},
            {"text": "The breathing muscles, and no — an attack is a problem "
                     "in the blood", "correct": False,
             "why": "Both halves are misplaced. More red cells is a change in "
                    "the blood, and an asthma attack is a narrowing of the "
                    "airways."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h07",
        "band": "harder",
        "text": "A newspaper reports that people who drink more coffee have "
                "more heart attacks, and concludes that coffee causes them. "
                "Using the way the smoking case was built, what would be "
                "needed before that conclusion held?",
        "options": [
            {"text": "A much larger survey, so that the size of the link is "
                     "measured far more reliably", "correct": False,
             "why": "A larger survey sharpens a correlation without saying "
                    "which way it runs. Doll and Hill had 40 000 doctors and "
                    "still needed more than size."},
            {"text": "Laboratory evidence that coffee contains some substance "
                     "known to harm the heart", "correct": False,
             "why": "A plausible mechanism is one strand of the case and it is "
                    "not enough on its own. Many harmless things contain "
                    "substances that are harmful in other amounts."},
            {"text": "A public statement from a doctor who has given up "
                     "drinking coffee themselves", "correct": False,
             "why": "One person changing their habits is not evidence about a "
                    "cause, however sincerely they do it. Doll giving up "
                    "smoking was a consequence of his evidence, not part of "
                    "it."},
            {"text": "Evidence that the risk rises with the amount drunk and "
                     "falls when people stop", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h08",
        "band": "harder",
        "text": "A pupil argues that because hard exercise leaves you "
                "breathless and aching, exercise must be damaging your lungs. "
                "What is the strongest reply?",
        "options": [
            {"text": "Exercise does damage the alveoli a little each time, "
                     "but the body repairs every bit of it overnight", "correct": False,
             "why": "There is no damage to repair. Nothing about the airways, "
                    "the alveoli or the blood is altered by running."},
            {"text": "Nothing in the lungs is altered — only the breathing "
                     "muscles work harder, and that reverses in minutes",
             "correct": True},
            {"text": "Breathlessness proves only that the lungs are too small "
                     "for the job, rather than that they are harmed",
             "correct": False,
             "why": "Lung size is almost never the limit either. "
                    "Breathlessness tracks the carbon dioxide in the blood, "
                    "and it says nothing about the size of anything."},
            {"text": "The aching shows the alveoli have been stretched by all "
                     "the deeper breathing, which is quite harmless", "correct": False,
             "why": "Aching is in the muscles, not in the lungs, and the "
                    "alveoli are not stretched by running. The one thing "
                    "exercise changes is muscular work."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h09",
        "band": "harder",
        "text": "At rest someone takes 14 breaths a minute of 0.5 litres "
                "each. During hard exercise they take 40 breaths a minute of "
                "2.5 litres each. Roughly how many times more air do they "
                "move each minute?",
        "options": [
            {"text": "About 3 times", "correct": False,
             "why": "That is the change in rate alone, 40 against 14. Each of "
                    "those breaths is also five times deeper, and both changes "
                    "count."},
            {"text": "About 5 times", "correct": False,
             "why": "That is the change in depth alone, 2.5 litres against "
                    "0.5. The rate has almost tripled as well, and the two "
                    "multiply together."},
            {"text": "About 14 times", "correct": True},
            {"text": "About 100 times", "correct": False,
             "why": "100 litres a minute is the exercise figure itself, not a "
                    "comparison. To compare, it has to be divided by the 7 "
                    "litres a minute at rest."},
        ],
        "figure": None,
    },
    {
        "id": "b4-04-h10",
        "band": "harder",
        "text": "A pupil with asthma is advised to warm up gently before "
                "running on a cold morning rather than starting flat out. "
                "Which two things are acting on their breathing at the "
                "same time?",
        "options": [
            {"text": "Exercise, which works the breathing muscles harder, and "
                     "asthma, which narrows the tubes the air passes down",
             "correct": True},
            {"text": "Exercise, which widens the airways as you work harder, "
                     "and asthma, which then widens them even further still",
             "correct": False,
             "why": "Exercise does not alter the airways at all, and asthma "
                    "narrows them rather than widening them. Only a reliever "
                    "widens a bronchiole."},
            {"text": "Asthma, which damages the alveoli permanently, and "
                     "exercise, which needs far more exchange surface than "
                     "usual", "correct": False,
             "why": "An attack leaves the alveoli undamaged, and no amount of "
                    "running creates extra surface. Neither half is what is "
                    "happening."},
            {"text": "Smoking, which destroys the cilia lining the airways, "
                     "and exercise, which moves all the trapped mucus around", "correct": False,
             "why": "Nothing in this scenario involves smoke or cilia. The two "
                    "factors present are the exercise and the asthma."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e11',
        "band": 'easier',
        "text": 'A reliever inhaler contains no oxygen at all. What does it actually do?',
        "options": [
            {"text": 'Relaxes the muscle in the airway wall, widening the tube.', "correct": True},
            {"text": 'Adds oxygen straight into the bloodstream.', "correct": False,
             "why": 'It contains no oxygen. Its job is on the airway muscle, not on the blood.'},
            {"text": 'Kills the bacteria causing the narrowing.', "correct": False,
             "why": 'An asthma attack is not an infection. Nothing is being killed — muscle, lining and mucus are the changes.'},
            {"text": 'Thins the mucus so it can be coughed up faster.', "correct": False,
             "why": "That describes clearing mucus, which is a smoking problem. A reliever's target is the muscle around the tube."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e12',
        "band": 'easier',
        "text": 'During an asthma attack, what happens to mucus production in the bronchioles?',
        "options": [
            {"text": 'It stops completely.', "correct": False,
             "why": 'Production does not stop — it increases, adding to the narrowing alongside the muscle and swelling.'},
            {"text": 'Extra mucus is produced.', "correct": True},
            {"text": 'It moves from the bronchioles into the alveoli.', "correct": False,
             "why": 'Mucus stays in the airway. Nothing about an attack sends it further down to the alveoli.'},
            {"text": 'It is replaced by the reliever drug.', "correct": False,
             "why": 'The reliever does not replace mucus. Its job is relaxing the muscle in the wall.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e13',
        "band": 'easier',
        "text": 'Carbon monoxide binds to haemoglobin roughly how many times more strongly than oxygen does?',
        "options": [
            {"text": 'About 2 times.', "correct": False,
             "why": 'This badly understates it. The real figure is roughly a hundred times larger than this.'},
            {"text": 'About 20 times.', "correct": False,
             "why": 'Closer, but still ten times too small. The figure is roughly 200 times.'},
            {"text": 'About 200 times.', "correct": True},
            {"text": 'About 2000 times.', "correct": False,
             "why": 'This is ten times too large. The figure given in this lesson is roughly 200 times.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e14',
        "band": 'easier',
        "text": "Roughly what fraction of a heavy smoker's haemoglobin may be occupied by carbon monoxide at any moment?",
        "options": [
            {"text": 'About a half.', "correct": False,
             "why": 'This is far higher than the figure this lesson gives, which is roughly a tenth.'},
            {"text": 'Almost all of it.', "correct": False,
             "why": 'This would be a medical emergency, not the everyday figure this lesson gives for a heavy smoker.'},
            {"text": 'None of it, since carbon monoxide only affects the lungs.', "correct": False,
             "why": "Carbon monoxide's whole effect in this lesson is on the blood, occupying roughly a tenth of a heavy smoker's haemoglobin."},
            {"text": 'About a tenth.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e15',
        "band": 'easier',
        "text": 'Roughly how long do paralysed cilia take to recover after someone stops smoking?',
        "options": [
            {"text": 'Over months.', "correct": True},
            {"text": 'A few seconds.', "correct": False,
             "why": 'Recovery is nowhere near this fast. This lesson gives a timescale of months.'},
            {"text": 'About a day.', "correct": False,
             "why": 'A day is how long carbon monoxide takes to clear. Cilia take considerably longer — months.'},
            {"text": 'They never recover.', "correct": False,
             "why": 'Cilia do recover — it is the destroyed alveolar walls that never grow back, not the cilia.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e16',
        "band": 'easier',
        "text": "Roughly how long does carbon monoxide take to clear from the blood after someone's last cigarette?",
        "options": [
            {"text": 'About a minute.', "correct": False,
             "why": 'It stays bound to haemoglobin far longer than this — roughly a day, not a minute.'},
            {"text": 'About a day.', "correct": True},
            {"text": 'About a month.', "correct": False,
             "why": 'A month is closer to how long cilia take to recover. Carbon monoxide clears much sooner.'},
            {"text": 'It never clears.', "correct": False,
             "why": 'It does clear, within about a day. The damage that never clears is the destroyed alveolar walls.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e17',
        "band": 'easier',
        "text": 'What are cilia?',
        "options": [
            {"text": 'Muscle fibres in the bronchiole wall.', "correct": False,
             "why": 'That is the muscle that contracts during an attack. Cilia are hairs, not muscle.'},
            {"text": 'The cells that produce mucus in the first place.', "correct": False,
             "why": 'Cilia move mucus rather than making it. Their job is sweeping, not producing.'},
            {"text": 'Tiny moving hairs on the airway lining that sweep mucus up and out.', "correct": True},
            {"text": 'Small sacs where gas crosses into the blood.', "correct": False,
             "why": 'That describes an alveolus. Cilia sit much higher up, in the airway.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e18',
        "band": 'easier',
        "text": 'What is asthma, in terms of what happens to the bronchioles?',
        "options": [
            {"text": 'A condition where the alveoli lose their surface area.', "correct": False,
             "why": 'That describes emphysema. In asthma the alveoli are left completely undamaged.'},
            {"text": "A condition where the trachea's cartilage rings soften.", "correct": False,
             "why": "The trachea's cartilage is not involved. Asthma narrows much narrower tubes further down."},
            {"text": 'A condition where carbon monoxide occupies the blood.', "correct": False,
             "why": 'That is a smoking effect, unrelated to asthma. Asthma is a narrowing of the bronchioles.'},
            {"text": 'A condition where the bronchioles narrow through muscle, swelling and mucus.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e19',
        "band": 'easier',
        "text": 'What is a reliever inhaler, in terms of what it contains and does?',
        "options": [
            {"text": 'A puff of a drug that relaxes airway muscle, widening the tube.', "correct": True},
            {"text": 'A small tank of pure oxygen for emergencies.', "correct": False,
             "why": 'It contains no oxygen at all. Its job is relaxing muscle in the airway wall.'},
            {"text": 'A device that filters tar and particulates from the air.', "correct": False,
             "why": 'It filters nothing — it is a drug delivered as a puff, targeting the muscle in the airway wall.'},
            {"text": 'A spray that dissolves mucus in the bronchioles.', "correct": False,
             "why": 'It does not act on mucus. Its target is the muscle narrowing the tube.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e20',
        "band": 'easier',
        "text": 'In emphysema, what becomes of the alveolar walls?',
        "options": [
            {"text": 'They thicken, making the diffusion distance longer.', "correct": False,
             "why": 'Thickening is a different kind of damage. In emphysema the walls are lost, not thickened.'},
            {"text": 'They break down, merging many small alveoli into fewer large ones.', "correct": True},
            {"text": 'They narrow, like a bronchiole during an attack.', "correct": False,
             "why": 'Alveolar walls do not narrow — they break down. Narrowing describes asthma, a different part.'},
            {"text": 'They swell with extra mucus.', "correct": False,
             "why": 'Mucus sits in the airways, not on alveolar walls. Emphysema is walls breaking down and merging.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e21',
        "band": 'easier',
        "text": 'Of the three factors — exercise, asthma and long-term smoking — which one acts on the breathing muscles alone, leaving the airways, alveoli and blood untouched?',
        "options": [
            {"text": 'Asthma.', "correct": False,
             "why": 'Asthma narrows the airways, leaving the breathing muscles unaffected — the opposite pairing.'},
            {"text": 'Smoking.', "correct": False,
             "why": 'Smoking reaches the airways, alveoli and blood, never the breathing muscles.'},
            {"text": 'Exercise.', "correct": True},
            {"text": 'None of the three — all three touch every part equally.', "correct": False,
             "why": 'Each factor has its own distinct part. Exercise is the one confined to the breathing muscles.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e22',
        "band": 'easier',
        "text": 'Of the three factors, which acts on the airways while leaving the alveoli and the blood completely undamaged?',
        "options": [
            {"text": 'Exercise.', "correct": False,
             "why": 'Exercise touches the breathing muscles, not the airways at all.'},
            {"text": 'Long-term smoking.', "correct": False,
             "why": 'Smoking damages the alveoli and the blood as well as the airways — it is not confined to one part.'},
            {"text": 'None of the three leaves the alveoli undamaged.', "correct": False,
             "why": 'An asthma attack leaves the alveoli completely undamaged — that is exactly why a reliever restores things fully.'},
            {"text": 'An asthma attack.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e23',
        "band": 'easier',
        "text": 'Roughly what year did Doll and Hill begin surveying hospital patients about smoking?',
        "options": [
            {"text": '1950.', "correct": True},
            {"text": '1850.', "correct": False,
             "why": 'This is a century too early — well before the study this lesson describes.'},
            {"text": '1990.', "correct": False,
             "why": 'This is decades too late. The hospital survey that began the case was in 1950.'},
            {"text": '2010.', "correct": False,
             "why": "This is far too recent. Doll and Hill's survey began in 1950, and the doctor study ran for decades after."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e24',
        "band": 'easier',
        "text": 'Roughly how many British doctors did Doll and Hill follow for decades?',
        "options": [
            {"text": '40.', "correct": False,
             "why": 'This is a thousand times too few. The study followed roughly 40,000 doctors.'},
            {"text": '40,000.', "correct": True},
            {"text": '4,000.', "correct": False,
             "why": 'Ten times too few. The figure this lesson gives is roughly 40,000.'},
            {"text": '4,000,000.', "correct": False,
             "why": 'This is a hundred times too many. The real figure is roughly 40,000.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e25',
        "band": 'easier',
        "text": 'What did Richard Doll himself do partway through his own study, and why?',
        "options": [
            {"text": 'He started smoking, to test the effects himself.', "correct": False,
             "why": 'It was the opposite — he smoked at the start and gave up two years into the study.'},
            {"text": 'He resigned from the study entirely.', "correct": False,
             "why": 'He did not leave the study. He changed his own behaviour in response to the evidence he was gathering.'},
            {"text": 'He gave up smoking, on his own evidence.', "correct": True},
            {"text": 'He switched to a different research topic.', "correct": False,
             "why": 'The change described is personal, not professional — he stopped smoking, not the research.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e26',
        "band": 'easier',
        "text": 'During hard exercise, does the total volume of air moved each minute rise, fall, or stay the same compared with rest?',
        "options": [
            {"text": 'It falls.', "correct": False,
             "why": 'Hard exercise moves far more air a minute than rest does, both faster and deeper.'},
            {"text": 'It stays exactly the same.', "correct": False,
             "why": 'Both the rate and the depth of breathing increase during hard exercise.'},
            {"text": 'It rises at first, then falls below the resting value.', "correct": False,
             "why": 'It stays raised for as long as the exercise continues, not just at first.'},
            {"text": 'It rises.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e27',
        "band": 'easier',
        "text": "Because carbon monoxide occupies part of a heavy smoker's haemoglobin, which gas is their blood worse at carrying?",
        "options": [
            {"text": 'Oxygen.', "correct": True},
            {"text": 'Carbon dioxide.', "correct": False,
             "why": "Haemoglobin's job affected here is carrying oxygen. Carbon monoxide occupies the sites oxygen would use."},
            {"text": 'Nitrogen.', "correct": False,
             "why": 'Nitrogen is not carried by haemoglobin at all. The gas affected is oxygen.'},
            {"text": 'Water vapour.', "correct": False,
             "why": "Water vapour plays no part here. Haemoglobin's oxygen-carrying is what carbon monoxide interferes with."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e28',
        "band": 'easier',
        "text": 'Does a reliever inhaler widen or narrow a bronchiole?',
        "options": [
            {"text": 'It narrows it further.', "correct": False,
             "why": 'Narrowing is what the attack itself does. The reliever relaxes the muscle, widening the tube.'},
            {"text": 'It widens it.', "correct": True},
            {"text": 'It does neither — it only clears mucus.', "correct": False,
             "why": 'It acts on the muscle in the wall, not on mucus, and widening is exactly what that does.'},
            {"text": 'It depends on how severe the attack is.', "correct": False,
             "why": 'Its action is the same either way — relaxing the muscle and widening the tube.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e29',
        "band": 'easier',
        "text": 'In emphysema, total lung volume changes very little. What falls sharply instead?',
        "options": [
            {"text": 'The number of breaths taken each minute.', "correct": False,
             "why": 'Breathing rate is not what emphysema damages directly. What falls is the exchange surface.'},
            {"text": 'The width of the trachea.', "correct": False,
             "why": 'The trachea is untouched. Emphysema damages the alveolar walls, far further down.'},
            {"text": 'The gas exchange surface area.', "correct": True},
            {"text": 'The amount of carbon dioxide the blood carries.', "correct": False,
             "why": 'Carbon dioxide carrying is not what falls here. The quantity lost in emphysema is exchange surface.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e30',
        "band": 'easier',
        "text": "How quickly does exercise's effect on breathing reverse once someone stops running?",
        "options": [
            {"text": 'Only after several days.', "correct": False,
             "why": 'It reverses far sooner than this — within minutes of stopping, not days.'},
            {"text": 'It never fully reverses.', "correct": False,
             "why": "Exercise's effect on breathing is fully reversible, unlike some of the smoking damage in this lesson."},
            {"text": 'Only if a reliever inhaler is used.', "correct": False,
             "why": 'A reliever plays no part here — breathing settles back down on its own within minutes.'},
            {"text": 'Completely, within minutes.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e31',
        "band": 'easier',
        "text": "Does long-term smoking typically change a person's total lung volume very much?",
        "options": [
            {"text": 'No, it stays close to normal even in emphysema.', "correct": True},
            {"text": 'Yes, it shrinks sharply as alveoli are destroyed.', "correct": False,
             "why": 'Volume stays close to normal, and can even rise slightly. What falls sharply is exchange surface.'},
            {"text": 'Yes, it grows sharply to compensate for lost surface.', "correct": False,
             "why": 'There is no compensating growth. Volume simply stays close to its usual value.'},
            {"text": 'It depends entirely on how many cigarettes a day are smoked.', "correct": False,
             "why": 'Even heavy, long-term smoking with emphysema keeps volume close to normal — it is surface that falls.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-e32',
        "band": 'easier',
        "text": 'Which of the three factors is treated with a reliever inhaler?',
        "options": [
            {"text": 'Exercise.', "correct": False,
             "why": 'Exercise needs no treatment — it reverses on its own within minutes of stopping.'},
            {"text": 'An asthma attack.', "correct": True},
            {"text": 'Long-term smoking.', "correct": False,
             "why": "A reliever inhaler does nothing for smoking's damage, since the airway is not what smoking narrows."},
            {"text": 'All three factors.', "correct": False,
             "why": 'Only the asthma attack responds to a reliever — it targets muscle narrowing a bronchiole, which only an attack causes.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s11',
        "band": 'standard',
        "text": 'Carbon monoxide binds haemoglobin far more strongly than oxygen does. Explain why even a modest level of exposure has an outsized effect on how much oxygen the blood carries.',
        "options": [
            {"text": 'Each occupied site is lost for a long time, not briefly, because the binding is so strong.', "correct": True},
            {"text": 'Oxygen stops being carried by any haemoglobin at all once carbon monoxide is present.', "correct": False,
             "why": 'Unaffected haemoglobin keeps carrying oxygen normally. Only the sites carbon monoxide has bound to are lost.'},
            {"text": 'A modest exposure always occupies most of the haemoglobin, whatever the actual dose is.', "correct": False,
             "why": 'The fraction occupied does depend on the dose. It is the strength of the binding that makes the effect outsized.'},
            {"text": 'Carbon monoxide is heavier than oxygen, so it settles at the bottom of each red blood cell.', "correct": False,
             "why": 'Weight and position play no part here — it is the strength and length of the binding that matters.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s12',
        "band": 'standard',
        "text": "A smoker's carbon monoxide level roughly halves overnight as their body clears it. Predict what happens to their available haemoglobin.",
        "options": [
            {"text": 'It falls further, since clearing carbon monoxide also destroys red blood cells.', "correct": False,
             "why": 'Clearing carbon monoxide frees haemoglobin rather than destroying cells.'},
            {"text": 'It rises back towards normal as the occupied sites are freed.', "correct": True},
            {"text": 'It stays exactly the same, since the red blood cell count is unchanged.', "correct": False,
             "why": 'The count staying fixed does not matter — what rises is how much of it is free to carry oxygen.'},
            {"text": 'It cannot recover until entirely new red blood cells are made.', "correct": False,
             "why": 'The existing cells recover as carbon monoxide lets go — nothing needs replacing.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s13',
        "band": 'standard',
        "text": "Suppose the fraction of a smoker's haemoglobin occupied by carbon monoxide doubles, from about a tenth to about a fifth. Predict the effect on climbing stairs.",
        "options": [
            {"text": 'Easier, since a faster heartbeat fully compensates for the extra carbon monoxide.', "correct": False,
             "why": 'A faster heart moves the same impaired blood faster — it does not restore what carbon monoxide has occupied.'},
            {"text": 'No different, since the total red blood cell count has not changed at all.', "correct": False,
             "why": 'The count staying fixed does not help — what matters is how much of it is free, and that has fallen further.'},
            {"text": 'Noticeably harder, since less haemoglobin is now free to carry oxygen.', "correct": True},
            {"text": "Impossible to predict without knowing the smoker's exact lung volume.", "correct": False,
             "why": 'Lung volume is not the limiting factor here — the available fraction of haemoglobin is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s14',
        "band": 'standard',
        "text": "Using nicotine's mechanism — narrowing blood vessels and raising heart rate — and carbon monoxide's separate mechanism, explain why a smoker's fingers and toes might feel colder than a non-smoker's on a cool day.",
        "options": [
            {"text": 'Carbon monoxide freezes solid inside the smallest blood vessels in cold weather.', "correct": False,
             "why": 'Carbon monoxide does not freeze anywhere — its effect is occupying haemoglobin, not blocking vessels physically.'},
            {"text": 'Tar coats the fingers and toes directly, trapping the warmth that would otherwise escape.', "correct": False,
             "why": 'Tar is inhaled into the lungs, not deposited on the skin of the extremities.'},
            {"text": 'Particulates and heat from the smoke raise skin temperature everywhere except the extremities.', "correct": False,
             "why": 'Particulates and heat act on the airway lining they are inhaled through, not on distant skin.'},
            {"text": 'Nicotine narrows the vessels supplying the extremities, reducing blood flow there.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s15',
        "band": 'standard',
        "text": 'Exercise and an asthma attack both change how well someone breathes, but in different ways. Compare what each one actually changes.',
        "options": [
            {"text": 'Exercise works the breathing muscles harder; an attack narrows the tubes air passes through.', "correct": True},
            {"text": 'Both change the same thing — how hard the breathing muscles have to work.', "correct": False,
             "why": 'An attack does not make the muscles work harder — it narrows the airway itself, a different part.'},
            {"text": 'Exercise actually narrows the airways instead; an attack works the breathing muscles far harder.', "correct": False,
             "why": 'This swaps the two. Exercise leaves the airways untouched, and an attack does not tire the muscles.'},
            {"text": 'Neither one produces any measurable change in breathing at all.', "correct": False,
             "why": 'Both produce large, measurable changes — one in effort, the other in airway width.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s16',
        "band": 'standard',
        "text": 'One person has smoked for five years; another for twenty-five. Which effects are likely present in both, and which are likely only in the twenty-five-year smoker?',
        "options": [
            {"text": 'All four mechanisms need decades, so neither smoker shows any effect at all yet.', "correct": False,
             "why": 'Carbon monoxide and cilia damage act quickly, within hours or weeks, not decades.'},
            {"text": 'Cilia and carbon monoxide effects appear early; emphysema-level loss needs far longer exposure.', "correct": True},
            {"text": 'Emphysema-level surface loss appears within the very first few years, for both smokers equally.', "correct": False,
             "why": "This lesson's emphysema case describes twenty-five years, not five — it builds slowly."},
            {"text": 'The five-year smoker is entirely unaffected until the twenty-five-year mark arrives.', "correct": False,
             "why": 'Carbon monoxide and cilia damage do not wait — they act far sooner than alveolar damage.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s17',
        "band": 'standard',
        "text": "A reliever inhaler helps someone's wheezing within minutes, but does nothing for a cough caused by a cold. Explain why the same drug does not help both.",
        "options": [
            {"text": 'The reliever only ever works on cold mornings, never during an actual cold.', "correct": False,
             "why": 'Temperature is not the relevant variable — the reliever targets airway muscle, which a cold does not affect.'},
            {"text": "A cold's cough is actually caused by exactly the same muscle narrowing that produces the wheezing.", "correct": False,
             "why": 'If it were the same mechanism, the reliever would help both — it does not, which shows they differ.'},
            {"text": 'The two problems have different mechanisms — muscle narrowing versus mucus needing clearing.', "correct": True},
            {"text": 'Reliever inhalers simply stop working after their very first use each day.', "correct": False,
             "why": 'Nothing in this lesson limits a reliever to one use — the mismatch is about mechanism, not timing.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s18',
        "band": 'standard',
        "text": 'Breathlessness after exercise resolves alone within minutes, but a serious attack may need emergency help. Using reversibility, explain the difference in urgency.',
        "options": [
            {"text": 'Exercise is more dangerous, since it works the muscles harder than any attack does.', "correct": False,
             "why": 'Harder muscle work is not dangerous, and it reverses without help — unlike a stalled attack.'},
            {"text": 'Neither one is genuinely urgent, since both usually settle down by themselves eventually.', "correct": False,
             "why": 'An attack not responding to a reliever is a medical emergency — it does not reliably settle.'},
            {"text": 'An attack is less urgent, since the alveoli stay completely undamaged throughout it.', "correct": False,
             "why": 'Undamaged alveoli do not make an unresponsive attack safe — the airway is still dangerously narrow.'},
            {"text": 'Exercise reverses on its own; an unresponsive attack needs a drug to reverse it.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s19',
        "band": 'standard',
        "text": 'A lung function test shows reduced gas transfer that improves substantially with a reliever inhaler. Which structure is most likely at fault?',
        "options": [
            {"text": 'The bronchioles, since only airway narrowing responds to a reliever.', "correct": True},
            {"text": 'The alveoli, since gas transfer itself is reduced in this patient.', "correct": False,
             "why": 'Alveolar damage does not improve with a reliever — improving points to the airway instead.'},
            {"text": 'The blood, since carbon monoxide has occupied part of the haemoglobin.', "correct": False,
             "why": 'A reliever does nothing to haemoglobin. Improving with one points to the airway, not the blood.'},
            {"text": 'It cannot be narrowed down at all from this evidence alone.', "correct": False,
             "why": 'Responding to a reliever is exactly the evidence that narrows it to the airway.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s20',
        "band": 'standard',
        "text": 'One attack narrows a bronchiole to half its radius; another narrows a different one to a third. Which cuts flow more severely, and by roughly what factor?',
        "options": [
            {"text": 'The half attack, since halving sounds like the bigger change of the two.', "correct": False,
             "why": 'The size of the fraction does not decide severity — a smaller radius always cuts flow further.'},
            {"text": 'The one-third attack, by roughly five times worse.', "correct": True},
            {"text": 'Both are equally severe, since both are narrowings of the very same tube.', "correct": False,
             "why": 'Flow depends steeply on radius, so different radii give very different degrees of narrowing.'},
            {"text": 'The half attack, by roughly five times worse than the third-radius one.', "correct": False,
             "why": 'This has the two the wrong way round — the smaller radius, one-third, is the more severe one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s21',
        "band": 'standard',
        "text": 'A peak-flow meter reading rises sharply minutes after someone uses their reliever during an attack. What is it measuring, and why has it changed?',
        "options": [
            {"text": 'Blood oxygen, which rises because the reliever adds oxygen straight into the blood.', "correct": False,
             "why": 'A peak-flow meter measures air flow, not blood oxygen, and the reliever adds no oxygen at all.'},
            {"text": 'Lung volume, which rises because the reliever expands the alveoli themselves.', "correct": False,
             "why": 'The alveoli are unchanged throughout an attack — the reading is about airflow, not volume.'},
            {"text": 'Air flow, which rises because the reliever has widened the narrowed bronchioles.', "correct": True},
            {"text": 'Heart rate, which rises because the reliever directly stimulates the heart muscle.', "correct": False,
             "why": 'A peak-flow meter reads air flow through the airway, not heart rate at all.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s22',
        "band": 'standard',
        "text": "One patient's lung function test shows reduced gas transfer that does not improve with an inhaler. Explain why this points to the alveoli rather than the airway.",
        "options": [
            {"text": 'It shows the airway is completely blocked, well beyond what any drug could ever open.', "correct": False,
             "why": 'Nothing suggests total blockage — a reliever not helping points away from the airway entirely.'},
            {"text": 'It shows the patient has been using the inhaler incorrectly every single time.', "correct": False,
             "why": 'Technique is not what this evidence points to — a genuine non-response points elsewhere.'},
            {"text": "It shows carbon monoxide has permanently disabled the reliever drug's active ingredient.", "correct": False,
             "why": 'Carbon monoxide acts on haemoglobin, not on drugs — the non-response points to the alveoli.'},
            {"text": 'A reliever only fixes airway muscle narrowing, so no improvement points elsewhere.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s23',
        "band": 'standard',
        "text": 'A pupil says asthma and long-term smoking both eventually damage the alveoli, just at different speeds. Correct this.',
        "options": [
            {"text": 'Asthma leaves the alveoli completely undamaged; only smoking reaches them.', "correct": True},
            {"text": 'They are right, but smoking works roughly ten times faster at causing the same damage.', "correct": False,
             "why": 'Speed is not the issue — asthma never damages the alveoli at all, at any speed.'},
            {"text": 'They are right, and both kinds of damage are fully reversible with the right treatment.', "correct": False,
             "why": 'Alveolar damage from smoking is permanent, and asthma causes no alveolar damage to reverse.'},
            {"text": 'Neither factor ever affects the alveoli in any way at all.', "correct": False,
             "why": 'Smoking does reach the alveoli, breaking down their walls — only asthma leaves them undamaged.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s24',
        "band": 'standard',
        "text": 'Carbon monoxide clears within a day and cilia recover over months, but alveolar damage never reverses. Explain the different outlook for someone quitting after two years versus after twenty.',
        "options": [
            {"text": 'Both recover in exactly the very same identical way, since carbon monoxide and cilia damage are the only effects that ever really matter.', "correct": False,
             "why": 'After twenty years, emphysema-level damage is far more likely, and that part never reverses.'},
            {"text": 'After two years little alveolar damage has likely built up, so most effects can fully resolve; after twenty, some is probably permanent.', "correct": True},
            {"text": 'Neither recovers at all once smoking has started, whatever the total duration was.', "correct": False,
             "why": 'Carbon monoxide and cilia damage do recover regardless of history — only alveolar walls do not.'},
            {"text": 'The two-year smoker is worse off, since stopping early wastes an adaptation the body was building.', "correct": False,
             "why": 'No such adaptation is described in this lesson — stopping earlier is consistently the better outcome.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s25',
        "band": 'standard',
        "text": "Someone's resting heart rate falls noticeably in the weeks after they stop smoking. Which substance's absence explains this?",
        "options": [
            {"text": 'Tar, which raises heart rate by irritating the airway lining directly.', "correct": False,
             "why": 'Tar damages the airways and alveoli, not heart rate — that link belongs to nicotine.'},
            {"text": 'Carbon monoxide, which raises heart rate by acting on the heart muscle.', "correct": False,
             "why": "Carbon monoxide's effect is on haemoglobin, not on heart rate directly."},
            {"text": 'Nicotine, which raises heart rate while someone is smoking.', "correct": True},
            {"text": 'Particulates, which raise heart rate by irritating the airway lining.', "correct": False,
             "why": 'Particulates irritate the lining and raise mucus, not heart rate.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s26',
        "band": 'standard',
        "text": 'Nicotine narrows blood vessels and raises heart rate and blood pressure. Predict whether blood pressure is higher soon after a cigarette or several hours later.',
        "options": [
            {"text": 'Higher several hours later, since nicotine takes that long before it starts working at all.', "correct": False,
             "why": "Nicotine's effect is present quickly, not delayed for hours."},
            {"text": 'Exactly the same at both times, since blood pressure never responds to nicotine at all.', "correct": False,
             "why": 'This lesson states directly that nicotine raises blood pressure, so the two times should differ.'},
            {"text": 'Lower soon after, since nicotine widens blood vessels for a short while.', "correct": False,
             "why": 'Nicotine narrows vessels, which raises pressure, the opposite of widening.'},
            {"text": "Higher soon after, since nicotine's effect is present then and fades as it clears.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s27',
        "band": 'standard',
        "text": "A smoker's heart beats faster because of nicotine. Explain why this does not compensate for carbon monoxide's damage.",
        "options": [
            {"text": 'The blood pumped faster still carries proportionally less oxygen, since haemoglobin itself is impaired.', "correct": True},
            {"text": 'It does compensate completely and fully, since much more blood overall reaches every tissue each minute.', "correct": False,
             "why": 'Moving more of the same oxygen-poor blood does not restore what carbon monoxide has occupied.'},
            {"text": 'The faster heartbeat only ever affects the lungs, never the rest of the body.', "correct": False,
             "why": 'A faster heartbeat moves blood everywhere, but moving impaired blood faster does not fix it.'},
            {"text": 'Nicotine and carbon monoxide simply cancel each other out completely.', "correct": False,
             "why": 'The two act on different things, heart rate and haemoglobin, and neither reverses the other.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s28',
        "band": 'standard',
        "text": "Years after quitting smoking, a patient's airway lining shows healthy, active cilia. What does that tell you, and what can it NOT tell you about their alveoli?",
        "options": [
            {"text": 'It shows the alveoli have also fully recovered, since the two tissues always heal together.', "correct": False,
             "why": 'Cilia and alveolar walls are different tissues — one can recover while the other stays damaged.'},
            {"text": 'It shows cilia have recovered; it says nothing about whether the alveoli have too.', "correct": True},
            {"text": 'It shows carbon monoxide is still present somewhere in the blood.', "correct": False,
             "why": 'Carbon monoxide clears within about a day and leaves no trace in the cilia.'},
            {"text": 'It shows the patient never smoked for very long in the first place.', "correct": False,
             "why": 'Cilia recovery does not reveal smoking history — only that enough time has passed since stopping.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s29',
        "band": 'standard',
        "text": 'Emphysema merges many small alveoli into fewer, larger ones, while total lung volume stays about the same. Explain why fewer larger sacs give less total surface.',
        "options": [
            {"text": 'Larger sacs have thicker walls, which directly reduces the surface each one has.', "correct": False,
             "why": 'Wall thickness is a separate property, and emphysema is not described as thickening walls.'},
            {"text": 'Merging sacs together always destroys some of the total volume as well as some surface.', "correct": False,
             "why": 'The question states volume stays the same — it is surface, not volume, that falls.'},
            {"text": 'Splitting a volume into many small sacs gives far more total surface than fewer large ones.', "correct": True},
            {"text": 'Larger sacs cannot hold as much air per sac, so less surface is needed overall.', "correct": False,
             "why": 'How much surface is needed is not the issue — the point is how much merging actually leaves behind.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s30',
        "band": 'standard',
        "text": 'A reliever successfully treats an attack in a patient who also smokes twenty a day. Explain why this does nothing about their long-term risk from smoking.',
        "options": [
            {"text": 'The reliever actively makes the smoking damage somewhat worse each time it is used.', "correct": False,
             "why": 'Nothing links reliever use to worsening smoking damage — the two are unrelated mechanisms.'},
            {"text": 'Treating the attack also slows the alveolar damage, though not completely.', "correct": False,
             "why": 'A reliever acts on airway muscle only, with no effect on the separate alveolar damage.'},
            {"text": 'There is no long-term risk left once an attack has been treated successfully.', "correct": False,
             "why": 'Treating one attack changes nothing about the ongoing damage smoking is still causing.'},
            {"text": "The attack is temporary and reversible; smoking's damage is separate and ongoing.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s31',
        "band": 'standard',
        "text": 'Of the four substances in cigarette smoke, one acts mainly on the blood vessels and heart rather than lung tissue. Name it, and explain what sets it apart.',
        "options": [
            {"text": 'Nicotine, since it narrows vessels and raises heart rate rather than damaging lung structures.', "correct": True},
            {"text": 'Tar, since it is carried in the blood all the way to the heart.', "correct": False,
             "why": 'Tar coats the airway lining and damages alveolar walls — it does not act on the heart.'},
            {"text": 'Carbon monoxide, since it raises heart rate directly by acting on it.', "correct": False,
             "why": 'Carbon monoxide occupies haemoglobin, rather than acting on the heart or vessels directly.'},
            {"text": 'Particulates and heat, since they irritate the blood vessels the very moment they are inhaled.', "correct": False,
             "why": 'Particulates and heat irritate the airway lining, not the blood vessels.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-s32',
        "band": 'standard',
        "text": 'A pupil argues that since carbon monoxide “takes red blood cells out of service,” a heavy smoker must have fewer red blood cells overall. Correct this.',
        "options": [
            {"text": 'They are entirely right — carbon monoxide destroys red blood cells permanently and completely, every single time.', "correct": False,
             "why": 'Nothing describes cells being destroyed. Carbon monoxide occupies haemoglobin temporarily, then clears.'},
            {"text": 'The cells are still there; each is just temporarily unable to carry oxygen while carbon monoxide is bound to it.', "correct": True},
            {"text": 'They are right, but only in smokers who also happen to have asthma as well.', "correct": False,
             "why": "Asthma plays no part in carbon monoxide's effect — no cells are destroyed either way."},
            {"text": 'Neither claim is true — carbon monoxide has no real effect on red blood cells at all.', "correct": False,
             "why": 'It does have a real effect, occupying haemoglobin — just not the one the pupil describes.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h11',
        "band": 'harder',
        "text": "A pupil argues: “15% of a smoker's haemoglobin is occupied by carbon monoxide, so their oxygen delivery must simply be 85% of normal.” Evaluate this claim.",
        "options": [
            {"text": 'Exactly right, since haemoglobin percentages translate directly into delivered oxygen percentages.', "correct": False,
             "why": 'Delivery also depends on how close demand already sits to capacity, which the simple percentage ignores.'},
            {"text": 'It overstates the impact, since a faster heart fully cancels out the loss.', "correct": False,
             "why": 'A faster heart moves the same impaired blood faster — it does not restore lost capacity.'},
            {"text": 'It understates the impact, since resting demand may already use nearly all normal capacity.', "correct": True},
            {"text": 'It cannot be judged without knowing exactly how many cigarettes were smoked that day.', "correct": False,
             "why": 'The occupied fraction is already given directly — cigarette count adds nothing further.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h12',
        "band": 'harder',
        "text": 'A researcher claims that because nicotine raises heart rate all day, smokers effectively get free cardiovascular training and better exercise tolerance. Evaluate this.',
        "options": [
            {"text": 'Sound — any sustained rise in heart rate improves fitness the same way real exercise does.', "correct": False,
             "why": 'This lesson elsewhere shows smoking harms exercise tolerance rather than improving it.'},
            {"text": 'Sound, but only for smokers who also happen to exercise regularly.', "correct": False,
             "why": "Even alongside exercise, nicotine's raised heart rate is stress on the vessels, not adaptation."},
            {"text": 'It cannot be evaluated, since heart rate is hard to measure accurately in smokers.', "correct": False,
             "why": 'Nothing suggests heart rate is hard to measure — the flaw is in the reasoning, not the measurement.'},
            {"text": 'Flawed — a chemically raised heart rate reflects stress on vessels, not efficient training.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h13',
        "band": 'harder',
        "text": 'A heavy smoker and a non-smoker do identical hard exercise. Both breathing rates rise similarly, since both are driven by rising carbon dioxide. Explain why the smoker may still become breathless sooner.',
        "options": [
            {"text": 'The same drive is present, but oxygen delivery already lags demand, so breathlessness arrives sooner.', "correct": True},
            {"text": "The smoker's own carbon dioxide trigger is far weaker overall, so their brain simply reacts much later.", "correct": False,
             "why": 'Nothing weakens the carbon dioxide trigger itself — the mismatch is on the delivery side.'},
            {"text": "The smoker's breathing muscles are physically smaller after years of smoking.", "correct": False,
             "why": 'Smoking is not described as shrinking the breathing muscles — delivery is the limit.'},
            {"text": 'There is no real physical difference; any breathlessness is purely psychological.', "correct": False,
             "why": 'Carbon monoxide genuinely reduces oxygen delivery — a physical limit, not an imagined one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h14',
        "band": 'harder',
        "text": 'Evaluate: “Since asthma and emphysema both reduce how much air reaches the alveoli, a reliever should help both conditions.”',
        "options": [
            {"text": 'True — both conditions narrow the same tubes, so the same drug should widen both equally.', "correct": False,
             "why": 'Emphysema damages the exchange surface itself, not the airway tubes.'},
            {"text": "False — emphysema is not an airway-narrowing problem, so a reliever's target does not apply.", "correct": True},
            {"text": 'True, but only in patients who happen to have both conditions at once.', "correct": False,
             "why": 'Even then, a reliever only reaches the asthma half of the problem.'},
            {"text": 'False, but only because emphysema patients cannot physically use an inhaler device.', "correct": False,
             "why": 'The reason a reliever fails is mechanism, not whether the device can be used.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h15',
        "band": 'harder',
        "text": "Doll and Hill's case rested on dose-response, reversibility, consistency across settings and a plausible mechanism. For “wearing red shoes causes more colds,” which strand is hardest to find evidence for?",
        "options": [
            {"text": 'Dose-response, since it is hard to imagine wearing red shoes more often causing more colds.', "correct": False,
             "why": 'A dose-response pattern could be claimed easily even if false — mechanism is genuinely missing.'},
            {"text": 'Consistency across settings, since red shoes are sold in every single country.', "correct": False,
             "why": 'Availability everywhere is not the hardest strand to fake or claim here.'},
            {"text": 'A plausible mechanism, since no biological pathway links shoe colour to catching a cold.', "correct": True},
            {"text": 'Reversibility, since nobody could ever stop wearing red shoes once they have started.', "correct": False,
             "why": 'People clearly could stop wearing red shoes — this is not the strand genuinely missing.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h16',
        "band": 'harder',
        "text": 'An advert claims: “our filters remove all the tar, so our cigarettes only deliver nicotine and carbon monoxide, making them safer.” Evaluate this.',
        "options": [
            {"text": 'Strong — tar is genuinely responsible for every single mechanism in the whole table, so removing it removes all risk.', "correct": False,
             "why": 'Tar is only one of four substances — carbon monoxide and nicotine act through separate mechanisms.'},
            {"text": 'Strong, since nicotine and carbon monoxide become harmless once tar is removed entirely.', "correct": False,
             "why": 'Nothing makes nicotine or carbon monoxide harmless — each has its own independent damage.'},
            {"text": 'Weak, but only because particulates and heat are actually worse than tar itself.', "correct": False,
             "why": "The claim's weakness is that two OTHER mechanisms survive intact, not a ranking of harm."},
            {"text": "Weak — carbon monoxide's circulation effect and nicotine's dependence and heart effects remain fully active.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h17',
        "band": 'harder',
        "text": "Halving a bronchiole's radius drops flow to about a sixteenth. A severe attack drops flow to about a sixty-fourth of normal. Roughly what fraction of the normal radius remains?",
        "options": [
            {"text": 'Roughly a third of the normal radius.', "correct": True},
            {"text": 'Roughly a quarter of the normal radius.', "correct": False,
             "why": 'A quarter of the radius would drop flow further than a sixty-fourth — the true fraction is larger.'},
            {"text": 'Roughly a sixty-fourth of the normal radius.', "correct": False,
             "why": 'This applies the flow fraction directly to the radius, but flow falls far more steeply than radius.'},
            {"text": 'Roughly a sixteenth of the normal radius.', "correct": False,
             "why": 'A sixteenth of the radius would drop flow by far more than a factor of sixty-four.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h18',
        "band": 'harder',
        "text": "A critic argues Doll and Hill's finding could instead be explained by people at higher genetic risk of cancer also being more likely to smoke. Which part of the evidence makes this weak?",
        "options": [
            {"text": 'The study followed 40,000 doctors, far too large a sample for genetics to matter.', "correct": False,
             "why": 'Sample size does not rule out a genetic explanation on its own.'},
            {"text": 'The risk fell when people stopped smoking, which a fixed genetic risk could not explain.', "correct": True},
            {"text": 'The survey began in a hospital in 1950, which predates modern genetics entirely.', "correct": False,
             "why": 'When the study began has no bearing on whether genetics could explain the pattern.'},
            {"text": 'Doll himself gave up smoking, which proves genetics played no part in his own personal case.', "correct": False,
             "why": "One person's decision says nothing about the general population's genetics."},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h19',
        "band": 'harder',
        "text": 'A pupil claims carbon monoxide is worse for a marathon runner who smokes than for a desk worker who smokes the same amount, because the runner needs more oxygen. Evaluate this.',
        "options": [
            {"text": 'False — carbon monoxide occupies the same fraction of haemoglobin whoever is affected by it.', "correct": False,
             "why": 'The occupied fraction being the same is exactly why the effect bites harder against higher demand.'},
            {"text": 'False — runners are protected from carbon monoxide by their overall fitness level.', "correct": False,
             "why": 'Nothing gives fitness a protective effect against carbon monoxide binding to haemoglobin.'},
            {"text": 'True — the same reduced supply collides more severely with a demand that is already higher.', "correct": True},
            {"text": 'It cannot be judged without knowing exactly how many cigarettes each person smokes weekly.', "correct": False,
             "why": 'The claim already states the SAME smoking amount for both — that is not what needs judging.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h20',
        "band": 'harder',
        "text": "A twenty-year smoker's breathlessness has not improved with an inhaler, but their morning cough has recently eased a little even though they still smoke. Explain what this does and does not tell you.",
        "options": [
            {"text": 'It clearly shows the emphysema itself is reversing, since one of the two symptoms has visibly improved.', "correct": False,
             "why": 'Alveolar damage never reverses — a cough easing does not touch that separate, permanent loss.'},
            {"text": 'It shows the earlier lung function test result must have been mistaken.', "correct": False,
             "why": 'Two symptoms changing differently is not evidence the test itself was wrong.'},
            {"text": 'It shows the reliever inhaler has finally started working on the alveoli directly.', "correct": False,
             "why": 'A reliever targets airway muscle, and the breathlessness is explicitly unimproved by it.'},
            {"text": 'It may reflect a change in mucus clearance; it says nothing about the separate alveolar damage.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h21',
        "band": 'harder',
        "text": 'Stopping smoking is often a medical matter rather than simply a decision. Using only nicotine dependence, explain why deciding to stop is often not enough alone.',
        "options": [
            {"text": "Nicotine creates a physical dependence, so stopping involves the body's chemistry, not just choice.", "correct": True},
            {"text": 'Tar physically builds up deep in the lungs and prevents anyone from ever actually stopping.', "correct": False,
             "why": "Tar damages the airways and alveoli — it is nicotine's role to explain why stopping is hard."},
            {"text": 'Carbon monoxide lowers a person\'s willpower directly by steadily reducing oxygen reaching their brain.', "correct": False,
             "why": 'The difficulty of stopping is attributed to nicotine dependence, not to carbon monoxide.'},
            {"text": 'Particulates and heat make the act of stopping physically painful to carry out.', "correct": False,
             "why": 'Particulates and heat irritate the airway lining — they play no part in why stopping is hard.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h22',
        "band": 'harder',
        "text": 'A pupil concludes that a reliever reversing an attack within minutes shows the ATTACK is temporary, but says nothing about whether the tendency to have further attacks has gone. Evaluate this.',
        "options": [
            {"text": 'Flawed — a condition that reverses within minutes cannot reasonably be considered ongoing at all.', "correct": False,
             "why": 'It is the ATTACK that reverses quickly, not the underlying tendency to have further attacks.'},
            {"text": 'Sound — quick reversal of one attack does not mean the underlying tendency has gone away.', "correct": True},
            {"text": 'Flawed, since the alveoli are left completely undamaged by every single attack.', "correct": False,
             "why": 'Undamaged alveoli say nothing either way about the tendency, and an unresponsive attack is still an emergency.'},
            {"text": 'It cannot be evaluated without knowing exactly how often the attacks happen.', "correct": False,
             "why": 'The reasoning separates one attack from the tendency behind it, which holds whatever the frequency.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h23',
        "band": 'harder',
        "text": 'A swimmer who periodically holds their breath while training claims this “trains their lungs to hold more air.” Evaluate this using what actually limits performance.',
        "options": [
            {"text": 'Correct — holding the breath physically stretches every alveolus, permanently enlarging them all over time.', "correct": False,
             "why": 'Nothing describes alveoli being stretched larger — their number and structure are fixed.'},
            {"text": 'Correct, since more air held means more oxygen is delivered per breath afterwards.', "correct": False,
             "why": 'Air held is not new capacity gained — the structures involved do not actually change.'},
            {"text": 'Unlikely — breath-holding does not increase alveolar number; any benefit is tolerance to rising carbon dioxide.', "correct": True},
            {"text": 'It cannot be evaluated, since swimming and running use entirely different sets of muscles.', "correct": False,
             "why": 'Which muscles are used is beside the point — the claim is specifically about the lungs.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h24',
        "band": 'harder',
        "text": "A smoker's blood pressure and their exercise tolerance are both affected by smoking. Explain why this happens through two separate mechanisms rather than one causing the other.",
        "options": [
            {"text": 'Raised blood pressure directly reduces exercise tolerance by squeezing the alveoli shut.', "correct": False,
             "why": 'Nothing links vessel narrowing to squeezing alveoli — the two effects trace to different substances.'},
            {"text": 'Reduced exercise tolerance is actually what raises blood pressure, since the tired heart has to work much harder.', "correct": False,
             "why": 'This reverses the causation — both effects trace back to separate substances, not to each other.'},
            {"text": 'They are not really independent — nicotine alone accounts for both effects entirely on its own.', "correct": False,
             "why": 'Reduced exercise tolerance is attributed to carbon monoxide, a separate substance from nicotine.'},
            {"text": 'Nicotine raises blood pressure by narrowing vessels; carbon monoxide reduces tolerance by impairing oxygen carrying.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h25',
        "band": 'harder',
        "text": "A pupil says: “the air breathed in during an asthma attack is still about 21% oxygen, so the air itself is not what has gone wrong.” Is that reasoning sound, and what does it identify as the fault?",
        "options": [
            {"text": 'Sound — the air is unchanged, so the fault is getting it through narrowed airways, which is what a reliever widens.', "correct": True},
            {"text": 'Unsound — the share of oxygen in the air falls sharply during an attack, and that fall is the real problem.', "correct": False,
             "why": 'The air stays at about 21% oxygen throughout an attack. What changes is how much of it can reach the alveoli.'},
            {"text": 'Unsound — an attack changes the air itself, filling it with extra carbon dioxide before it is breathed in.', "correct": False,
             "why": 'The air breathed in is ordinary room air. The narrowing happens inside the airways, not in the room.'},
            {"text": 'Sound — but only because the alveoli themselves are damaged during every attack.', "correct": False,
             "why": 'An asthma attack leaves the alveoli undamaged. The narrowed bronchioles are the fault.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h26',
        "band": 'harder',
        "text": "A pupil argues that because carbon monoxide and nicotine act within hours or minutes while tar's damage takes years, “the fast-acting substances must be more dangerous overall.” Evaluate this.",
        "options": [
            {"text": 'Sound — a substance that acts much faster always causes far more lasting harm than one acting slowly.', "correct": False,
             "why": 'Speed and permanence differ here — the fast-acting substances are also the reversible ones.'},
            {"text": "Flawed — carbon monoxide and nicotine's fast effects reverse fully, while tar's slow damage is permanent.", "correct": True},
            {"text": 'Sound, since permanent damage from tar is impossible if it takes years to appear.', "correct": False,
             "why": "Taking years to appear does not make tar's damage any less permanent once it has happened."},
            {"text": 'It cannot be evaluated, since danger cannot ever be compared across different substances.', "correct": False,
             "why": 'This lesson compares the four substances directly by mechanism, which is enough to judge the claim.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h27',
        "band": 'harder',
        "text": "A reliever helps an asthma attack within minutes but does nothing for a smoker's emphysema. Explain what this contrast reveals about the TYPE of problem each condition represents.",
        "options": [
            {"text": 'Both are exactly the same type of problem, just at different stages of severity.', "correct": False,
             "why": 'Total success in one and total failure in the other is strong evidence they differ in kind.'},
            {"text": 'It reveals emphysema is simply a more severe form of an ordinary asthma attack.', "correct": False,
             "why": 'The two damage entirely different structures — airway muscle versus alveolar walls.'},
            {"text": 'One is a delivery problem a drug can rapidly relieve; the other is a loss of tissue no drug can restore.', "correct": True},
            {"text": 'It really only reveals that relievers work in younger patients, whatever their underlying condition happens to be.', "correct": False,
             "why": 'Age plays no part — the deciding factor is which structure is actually at fault.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h28',
        "band": 'harder',
        "text": 'A pupil argues that someone who lives with a heavy smoker but never smokes themselves still has some raised risk, because dose-response tracks exposure to the substances rather than who lit the cigarette. Evaluate this using dose-response.',
        "options": [
            {"text": 'Flawed — dose-response only ever really applies to someone who personally holds and actually lights a cigarette.', "correct": False,
             "why": 'The substances themselves do not care who lit the cigarette — exposure through the air still counts.'},
            {"text": "Flawed, since carbon monoxide only ever affects the smoker's own haemoglobin directly.", "correct": False,
             "why": 'Carbon monoxide in shared air can be inhaled by anyone present.'},
            {"text": 'It cannot be evaluated, since no exact figures for secondhand exposure are given.', "correct": False,
             "why": 'The dose-response logic still applies without an exact figure — lower exposure implies some risk.'},
            {"text": 'Sound — dose-response is about exposure to the substances, and inhaling shared smoke is still exposure.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h29',
        "band": 'harder',
        "text": "A pupil argues that Doll's own smoking at the start of his study makes the whole case biased, since “the lead scientist had a personal reason to find smoking dangerous.” Evaluate this.",
        "options": [
            {"text": 'Backwards — Doll changed his own behaviour because of the evidence, a sign of following it rather than confirming bias.', "correct": True},
            {"text": 'Correct — a scientist who smokes can never study smoking fairly or without bias.', "correct": False,
             "why": 'The direction of the change, quitting because of the evidence, points against bias, not towards it.'},
            {"text": 'Correct, since Doll likely wanted to justify his own decision to quit after the fact.', "correct": False,
             "why": 'The quitting happened DURING the study, in response to evidence, not as a later justification.'},
            {"text": "It cannot really be evaluated at all, since nobody can ever truly know a scientist's own private motivations for certain.", "correct": False,
             "why": 'The observable sequence, evidence then a change in behaviour, is enough to judge the argument.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h30',
        "band": 'harder',
        "text": "A person's tissues function without symptoms above 80% of usual oxygen-carrying capacity. If carbon monoxide occupies 12% of their haemoglobin, are they above or below that threshold, and by how much?",
        "options": [
            {"text": 'Below it, by 8 percentage points.', "correct": False,
             "why": '100% minus 12% leaves 88%, which is ABOVE the 80% threshold, not below it.'},
            {"text": 'Above it, by 8 percentage points.', "correct": True},
            {"text": 'Above it, by 12 percentage points.', "correct": False,
             "why": 'This uses the occupied figure directly rather than the gap between 88% and 80%.'},
            {"text": 'Exactly at the threshold, with nothing at all to spare.', "correct": False,
             "why": '88% available capacity sits clearly above 80%, with 8 percentage points to spare.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h31',
        "band": 'harder',
        "text": "One lung report reads “reduced gas transfer that does not improve with an inhaler.” A second, different patient's reads “improves substantially with an inhaler.” Which more likely has emphysema, and which poorly controlled asthma?",
        "options": [
            {"text": 'The first more likely has asthma, since asthma is by far the more common condition overall.', "correct": False,
             "why": 'How common a condition is does not decide this — only asthma responds to a reliever, which patient one does not show.'},
            {"text": 'Both reports simply describe the same condition at two different stages of treatment.', "correct": False,
             "why": 'A reliever either restores airway function or it does not — the two outcomes point to different faults.'},
            {"text": 'The first — no improvement — more likely emphysema; the second, clear improvement, more likely asthma.', "correct": True},
            {"text": 'Neither one can be identified without also taking a chest X-ray of each patient.', "correct": False,
             "why": 'The reliever-response pattern given is exactly the evidence this lesson uses to tell the two apart.'},
        ],
        "figure": None,
    },
    {
        "id": 'b4-04-h32',
        "band": 'harder',
        "text": "A headline claims: “scientists still don't know for certain that smoking causes cancer, only that the two are linked.” Using Doll and Hill's four strands of evidence, evaluate this.",
        "options": [
            {"text": 'Fair — a correlation can never become anything stronger than “a link,” however much evidence is gathered.', "correct": False,
             "why": 'Multiple strands converging is exactly how science moves from correlation towards a causal case.'},
            {"text": 'Fair, since Doll and Hill only ever studied British doctors, not the whole population.', "correct": False,
             "why": "The case's strength does not depend on studying everyone — it rests on the four converging strands."},
            {"text": 'Not fair, but only because the study followed 40,000 people rather than some smaller number.', "correct": False,
             "why": 'Sample size alone is not what makes the evidence strong — it is the combination of four strands.'},
            {"text": 'Not fair — dose-response, reversibility, consistency and a plausible mechanism together go well beyond a mere link.', "correct": True},
        ],
        "figure": None,
    },
]
