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
            {"text": "The bronchioles narrowing permanently, so less air gets "
                     "through", "correct": False,
             "why": "Emphysema is not a narrowing at all. The tubes are not "
                    "what is damaged — the exchange surface at the end of them "
                    "is."},
            {"text": "The lungs shrinking, so they hold much less air than "
                     "before", "correct": False,
             "why": "Lung volume stays close to normal, and often rises. What "
                    "falls sharply is the surface area available for "
                    "exchange."},
            {"text": "Mucus filling the alveoli, so oxygen has further to "
                     "travel", "correct": False,
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
            {"text": "The alveolar walls are beginning to regrow and are "
                     "irritating the airway", "correct": False,
             "why": "Lost alveolar walls never grow back — that is the one "
                    "permanent damage. The change behind the cough is in the "
                    "airway lining."},
            {"text": "Carbon monoxide is being released from the blood back "
                     "into the lungs", "correct": False,
             "why": "Carbon monoxide clears within about a day, and it leaves "
                    "the body without producing a cough. Weeks later, "
                    "something else is going on."},
            {"text": "The airways are producing more mucus than they did "
                     "while smoking", "correct": False,
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
            {"text": "Their lungs are larger, so they clear the air faster",
             "correct": False,
             "why": "Trained athletes do not generally have much larger lungs. "
                    "Lung size is almost never what decides how someone copes "
                    "with exercise."},
            {"text": "Their bronchioles are wider, so air leaves more "
                     "quickly", "correct": False,
             "why": "Airway width is what an asthma attack changes over "
                    "minutes, not what training changes. Recovery is about the "
                    "blood, not the tubes."},
            {"text": "They clear the carbon dioxide backlog sooner, because "
                     "heart and muscles work more efficiently",
             "correct": True},
            {"text": "Their muscles make no carbon dioxide, so there is no "
                     "backlog to clear", "correct": False,
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
            {"text": "Because the alveoli need airway muscle to work "
                     "properly", "correct": False,
             "why": "The alveoli need no help from the muscle in the airway "
                    "wall. They need air delivered to them, and that is what "
                    "has been interrupted."},
            {"text": "Because not enough air is getting through the narrowed "
                     "tubes to reach the surface", "correct": True},
            {"text": "Because the air outside has less oxygen in it during an "
                     "attack", "correct": False,
             "why": "The air is unchanged at about 21% oxygen. That is exactly "
                    "why an inhaler helps and an oxygen cylinder mostly does "
                    "not."},
            {"text": "Because the blood cannot pick up oxygen while the "
                     "airways are narrowed", "correct": False,
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
            {"text": "The gas has narrowed their bronchioles, which an "
                     "examination would not show", "correct": False,
             "why": "Narrowed bronchioles are exactly what an examination "
                    "would find, and carbon monoxide does not narrow them. "
                    "This damage is not in the lungs at all."},
            {"text": "The gas has destroyed alveolar walls, which takes years "
                     "to show up on a test", "correct": False,
             "why": "Destroyed alveolar walls are tar's slow damage, not "
                    "carbon monoxide's, and reduced gas transfer does show on "
                    "a test. Carbon monoxide acts within hours."},
            {"text": "The lungs are exchanging normally, but the blood "
                     "leaving them carries far less oxygen", "correct": True},
            {"text": "The air in the house has less oxygen in it, so less can "
                     "cross the alveolar wall", "correct": False,
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
            {"text": "A larger survey, so that the link is measured more "
                     "reliably", "correct": False,
             "why": "A larger survey sharpens a correlation without saying "
                    "which way it runs. Doll and Hill had 40 000 doctors and "
                    "still needed more than size."},
            {"text": "A laboratory test showing that coffee contains a "
                     "harmful substance", "correct": False,
             "why": "A plausible mechanism is one strand of the case and it is "
                    "not enough on its own. Many harmless things contain "
                    "substances that are harmful in other amounts."},
            {"text": "A statement from a doctor who has stopped drinking "
                     "coffee themselves", "correct": False,
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
            {"text": "Exercise does damage them a little, but the body repairs "
                     "all of it overnight", "correct": False,
             "why": "There is no damage to repair. Nothing about the airways, "
                    "the alveoli or the blood is altered by running."},
            {"text": "Nothing in the lungs is altered — only the breathing "
                     "muscles work harder, and that reverses in minutes",
             "correct": True},
            {"text": "Breathlessness proves the lungs are simply too small, "
                     "rather than that they are damaged", "correct": False,
             "why": "Lung size is almost never the limit either. "
                    "Breathlessness tracks the carbon dioxide in the blood, "
                    "and it says nothing about the size of anything."},
            {"text": "The aching shows the alveoli have been stretched, which "
                     "is harmless but quite real", "correct": False,
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
            {"text": "Exercise, which widens the airways as you work, and "
                     "asthma, which then widens them further still",
             "correct": False,
             "why": "Exercise does not alter the airways at all, and asthma "
                    "narrows them rather than widening them. Only a reliever "
                    "widens a bronchiole."},
            {"text": "Asthma, which damages the alveoli, and exercise, which "
                     "needs more surface than usual", "correct": False,
             "why": "An attack leaves the alveoli undamaged, and no amount of "
                    "running creates extra surface. Neither half is what is "
                    "happening."},
            {"text": "Smoking, which destroys the cilia, and exercise, which "
                     "moves the mucus around", "correct": False,
             "why": "Nothing in this scenario involves smoke or cilia. The two "
                    "factors present are the exercise and the asthma."},
        ],
        "figure": None,
    },
]
