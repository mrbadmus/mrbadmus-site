"""Biology · Bioenergetics — the MRB-338 expansion of `response-to-exercise`.

One leaf only: AQA 8461 §4.4.2.3. The original twelve rows in
`bioenergetics.py` take lactic acid's name, blood redirected away from
digestion, glucose and oxygen both rising in demand, resting heart rate
falling with training, the case for breathing deeper as well as faster,
vasodilation reddening the face, more mitochondria delaying the anaerobic
switch, correcting when oxygen debt is actually repaid, why harder
exercise means longer recovery, holding the breath during a sprint, a
heart-rate-times-stroke-volume calculation, and comparing two runners by
the size of their oxygen debt.

This file takes what they leave: glycogen breakdown named and explained,
stroke volume as its own quantity distinct from heart rate, the warm-up
and cool-down as deliberate uses of the same responses, minute
ventilation worked as its own arithmetic in both directions, and a run of
predict/evaluate items that test recovery, training adaptation and oxygen
debt from unfamiliar angles — a damaged heart, two athletes with
identical times, a scientist proposing recovery heart rate as a fitness
test.

Numbers here are heart-rate-times-stroke-volume and
breathing-rate-times-tidal-volume arithmetic, matched in spirit to the
original 9800/4900 row but never repeating its figures.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═══════════════════════════════════════
    {
        "id": "ks4-response-to-exercise-e05",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process that widens blood vessels near the skin during exercise.",
        "options": [
            "Vasodilation",
            "Vasoconstriction",
            "Osmosis",
            "Diffusion",
        ],
        "correct_index": 0,
        "why": "Vasodilation is the widening of blood vessels near the skin, bringing more "
               "blood to the surface during exercise.",
    },
    {
        "id": "ks4-response-to-exercise-e06",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the storage carbohydrate broken down in the liver and muscles to "
               "release glucose during exercise.",
        "options": [
            "Cellulose",
            "Glycogen",
            "Starch",
            "Chitin",
        ],
        "correct_index": 1,
        "why": "Glycogen stored in the liver and muscles is broken down into glucose to fuel "
               "exercising muscles.",
    },
    {
        "id": "ks4-response-to-exercise-e07",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which three body systems work together to meet the demands of "
               "exercise.",
        "options": [
            "The heart, the skin and the kidneys",
            "The lungs, the stomach and the liver, not the heart itself",
            "The heart, the lungs and the blood vessels",
            "The brain, the bones and the muscles",
        ],
        "correct_index": 2,
        "why": "The heart, lungs and blood vessels work together to deliver more oxygen and "
               "glucose to exercising muscles.",
    },
    {
        "id": "ks4-response-to-exercise-e08",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term for the extra oxygen needed by the body after hard exercise "
               "has stopped.",
        "options": [
            "Oxygen surplus",
            "Oxygen reserve",
            "Oxygen store",
            "Oxygen debt",
        ],
        "correct_index": 3,
        "why": "Oxygen debt is the name for the extra oxygen needed after exercise to deal "
               "with the lactic acid that built up.",
    },
    {
        "id": "ks4-response-to-exercise-e09",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to a person's stroke volume, the blood pumped with each "
               "heartbeat, during exercise.",
        "options": [
            "It increases",
            "It decreases",
            "It stays exactly the same",
            "It drops to zero",
        ],
        "correct_index": 0,
        "why": "Stroke volume rises during exercise, so more blood is pumped with every "
               "heartbeat.",
    },
    {
        "id": "ks4-response-to-exercise-e10",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these increases during exercise, besides heart rate.",
        "options": [
            "Blood flow to the digestive system",
            "Breathing rate and depth",
            "The concentration of urea in the blood",
            "The number of red blood cells made that second",
        ],
        "correct_index": 1,
        "why": "Breathing rate and depth both increase during exercise, delivering more "
               "oxygen and removing more carbon dioxide.",
    },
    {
        "id": "ks4-response-to-exercise-e11",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what glycogen breakdown in the liver releases into the blood.",
        "options": [
            "Oxygen",
            "Lactic acid",
            "Glucose",
            "Carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Breaking down stored glycogen releases glucose into the blood, fuelling "
               "exercising muscles.",
    },
    {
        "id": "ks4-response-to-exercise-e12",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these does NOT typically increase during exercise.",
        "options": [
            "Heart rate",
            "Breathing rate",
            "Vasodilation in the working leg and arm muscles",
            "The gut's supply of blood during exercise",
        ],
        "correct_index": 3,
        "why": "Blood flow to the digestive system is reduced during exercise, as blood is "
               "redirected towards the muscles.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════
    {
        "id": "ks4-response-to-exercise-s05",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why blood is redirected away from the digestive system during hard "
               "exercise.",
        "options": [
            "The muscles need the extra blood far more urgently at that moment",
            "Digestion stops completely the moment any exercise begins",
            "The digestive system makes its own oxygen, needing less blood",
            "Blood flow to the gut rises to digest food faster",
        ],
        "correct_index": 0,
        "why": "The working muscles need extra oxygen and glucose more urgently, so blood is "
               "redirected towards them and away from the gut.",
    },
    {
        "id": "ks4-response-to-exercise-s06",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the liver breaks down its stored glycogen during exercise.",
        "options": [
            "It converts glycogen into oxygen for the muscles to use",
            "It releases glucose into the blood to fuel respiring muscles",
            "It converts glycogen into lactic acid to send to the lungs",
            "It stores extra ATP in reserve for use later in the day",
        ],
        "correct_index": 1,
        "why": "Breaking glycogen back down into glucose supplies the extra fuel that "
               "respiring muscles need during exercise.",
    },
    {
        "id": "ks4-response-to-exercise-s07",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why vasodilation near the skin occurs during hard exercise.",
        "options": [
            "It moves blood into the digestive system to absorb food more quickly than "
            "usual",
            "It increases the blood supply reaching the brain specifically",
            "It brings warm blood to the surface, helping the body lose heat",
            "It reduces the total volume of blood in circulation",
        ],
        "correct_index": 2,
        "why": "Widened blood vessels near the skin carry warm blood to the surface, where "
               "the body can lose the extra heat exercise produces.",
    },
    {
        "id": "ks4-response-to-exercise-s08",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to the process of a stored carbohydrate being broken "
               "down into glucose in muscle cells.",
        "options": [
            "Photosynthesis",
            "Fermentation",
            "Deamination",
            "Glycogen breakdown",
        ],
        "correct_index": 3,
        "why": "Glycogen breakdown converts the stored carbohydrate back into glucose for "
               "the muscle to respire.",
    },
    {
        "id": "ks4-response-to-exercise-s09",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a rise in stroke volume, rather than heart rate alone, helps "
               "deliver oxygen to muscles.",
        "options": [
            "More blood moves with every beat, so more oxygen is delivered per heartbeat",
            "A rising stroke volume slows the heart rate down in response",
            "Stroke volume has no connection to how much oxygen reaches the muscles",
            "A higher stroke volume means less blood is pumped with each beat",
        ],
        "correct_index": 0,
        "why": "A larger stroke volume means each heartbeat delivers more blood, and so more "
               "oxygen, to the working muscles.",
    },
    {
        "id": "ks4-response-to-exercise-s10",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why breathing rate and breathing depth both increase during "
               "exercise, rather than just one of them.",
        "options": [
            "Rate alone would remove all the extra carbon dioxide a muscle produces "
            "during a hard bout of exercise",
            "Together they raise the total volume of air exchanged each minute far more "
            "than either alone",
            "Depth alone doubles the oxygen entering the blood every time",
            "Increasing both together reduces the total air exchanged per minute",
        ],
        "correct_index": 1,
        "why": "Rate and depth rising together raise the total volume of air moved each "
               "minute by far more than changing either one on its own.",
    },
    {
        "id": "ks4-response-to-exercise-s11",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an athlete's resting breathing rate can be lower after months of "
               "training, while still supplying enough oxygen during a race.",
        "options": [
            "Training stops the lungs needing extra oxygen during a race",
            "A lower resting breathing rate means the lungs have stopped working properly "
            "as it normally and properly should",
            "Training increases the volume of air moved with each breath, making each "
            "breath count for more",
            "Training removes the need to breathe faster during exercise",
        ],
        "correct_index": 2,
        "why": "A trained person moves more air with each breath, so fewer breaths per "
               "minute are needed to supply the same oxygen.",
    },
    {
        "id": "ks4-response-to-exercise-s12",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the heart's stroke volume, not just its rate, increases with "
               "fitness training.",
        "options": [
            "Training lowers the amount of blood the heart can hold with each beat",
            "A trained heart beats faster but pumps less blood with each beat",
            "Stroke volume has no connection to how fit a person is",
            "Training strengthens the heart muscle, letting it pump more blood per beat",
        ],
        "correct_index": 3,
        "why": "A stronger, trained heart muscle can contract more forcefully, pumping more "
               "blood with every beat.",
    },
    {
        "id": "ks4-response-to-exercise-s13",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's face reddens during intense exercise, referring to "
               "blood vessels.",
        "options": [
            "Blood vessels near the skin widen, bringing more blood towards the surface",
            "Blood vessels near the skin narrow, trapping blood beneath the muscles",
            "Red blood cells multiply within seconds of exercise starting",
            "The skin absorbs extra oxygen directly from the surrounding air",
        ],
        "correct_index": 0,
        "why": "Widened blood vessels near the skin surface carry more blood there, which is "
               "what reddens the face.",
    },
    {
        "id": "ks4-response-to-exercise-s14",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A runner does a slow, gentle jog immediately after a hard race, rather than "
               "stopping completely. Suggest why.",
        "options": [
            "Stopping completely would convert all lactic acid into glucose immediately "
            "immediately and painlessly",
            "Keeping the muscles moving helps blood keep clearing lactic acid faster than "
            "resting would",
            "A gentle jog stops the heart rate falling back towards normal",
            "A gentle jog removes the need for the body to repay any oxygen debt",
        ],
        "correct_index": 1,
        "why": "Light continued movement keeps blood flowing through the muscles, helping "
               "clear lactic acid faster than standing still would.",
    },
    {
        "id": "ks4-response-to-exercise-s15",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person's breathing rate stays raised for several minutes after "
               "they stop exercising.",
        "options": [
            "Breathing rate falls to its resting value the instant exercise ends finally",
            "The lungs need time to cool down after exercising hard",
            "Extra oxygen is still needed to repay the oxygen debt built up during "
            "exercise",
            "Raised breathing rate has no connection to the oxygen debt",
        ],
        "correct_index": 2,
        "why": "Breathing stays raised so that extra oxygen keeps arriving to help repay the "
               "oxygen debt built up during exercise.",
    },
    {
        "id": "ks4-response-to-exercise-s16",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why athletes performing a warm-up before a race gradually increase "
               "their exercise intensity.",
        "options": [
            "A gradual warm-up removes the need for oxygen during the race itself",
            "Increasing intensity gradually stops the heart rate rising during the race, "
            "which contradicts what a warm-up is designed to do",
            "A gradual warm-up converts glycogen directly into protein before the race",
            "It gradually raises heart rate, breathing and blood flow so the muscles are "
            "ready when the race starts",
        ],
        "correct_index": 3,
        "why": "A gradual warm-up raises heart rate, breathing and blood flow ahead of time, "
               "so the muscles are already prepared for the race's demands.",
    },
    {
        "id": "ks4-response-to-exercise-s17",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person's resting breathing rate is 12 breaths per minute, taking in 500 "
               "cm3 of air each breath. Determine the volume of air breathed in one minute.",
        "options": [
            "6,000 cm3",
            "512 cm3",
            "500 cm3",
            "12 cm3",
        ],
        "correct_index": 0,
        "why": "12 breaths x 500 cm3 each gives 6,000 cm3 of air breathed per minute.",
    },
    {
        "id": "ks4-response-to-exercise-s18",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During exercise, a person's breathing rate rises to 24 breaths per minute, "
               "each of 600 cm3. Calculate the extra volume of air breathed per minute "
               "compared with a resting rate of 12 breaths of 500 cm3 each.",
        "options": [
            "14,400 cm3",
            "8,400 cm3",
            "6,000 cm3 at rest",
            "600 cm3",
        ],
        "correct_index": 1,
        "why": "Exercise gives 24 x 600 = 14,400 cm3 and rest gives 12 x 500 = 6,000 cm3, so "
               "the extra volume is 14,400 - 6,000 = 8,400 cm3.",
    },
    {
        "id": "ks4-response-to-exercise-s19",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine a person's minute ventilation, the volume of air breathed per "
               "minute, if they take 20 breaths, each of 450 cm3.",
        "options": [
            "470 cm3",
            "450 cm3",
            "9,000 cm3",
            "20 cm3",
        ],
        "correct_index": 2,
        "why": "20 breaths x 450 cm3 each gives 9,000 cm3 of minute ventilation.",
    },
    {
        "id": "ks4-response-to-exercise-s20",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A resting heart rate is 65 beats per minute, pumping 70 cm3 with each beat. "
               "Calculate the volume of blood pumped in one minute.",
        "options": [
            "65 cm3",
            "70 cm3",
            "135 cm3",
            "4,550 cm3",
        ],
        "correct_index": 3,
        "why": "65 beats x 70 cm3 each gives 4,550 cm3 of blood pumped per minute.",
    },
    {
        "id": "ks4-response-to-exercise-s21",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person's heart rate can return to its resting value faster "
               "after training than before they were trained.",
        "options": [
            "A trained heart recovers more efficiently, restoring normal circulation "
            "sooner",
            "Training keeps the heart rate permanently raised instead of falling instead "
            "of ever falling back",
            "A trained heart stops needing to pump extra blood during exercise",
            "Recovery speed has no connection to how fit a person's heart is",
        ],
        "correct_index": 0,
        "why": "A trained cardiovascular system recovers more efficiently, so heart rate "
               "returns to its resting value sooner.",
    },
    {
        "id": "ks4-response-to-exercise-s22",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a doctor might measure how quickly a patient's heart rate falls "
               "after a short burst of exercise.",
        "options": [
            "It shows exactly how much glucose the patient has eaten that day",
            "A faster recovery generally reflects a fitter cardiovascular system",
            "It shows how much oxygen the patient's blood can carry at most",
            "Heart rate recovery has no link to general fitness",
        ],
        "correct_index": 1,
        "why": "How quickly the heart rate falls back to resting reflects how efficiently a "
               "fit cardiovascular system recovers.",
    },
    {
        "id": "ks4-response-to-exercise-s23",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a swimmer's heart rate rises even before they dive into the "
               "pool, during their warm-up routine.",
        "options": [
            "The heart only responds once a person is standing in the water itself each "
            "time",
            "Warm-up movements lower heart rate before an event begins",
            "Anticipation and light movement already raise the muscles' demand for oxygen",
            "Heart rate rising before a race has no connection to exercise",
        ],
        "correct_index": 2,
        "why": "Light warm-up movement, and the body's anticipation of effort, already raise "
               "the muscles' demand for oxygen before the race begins.",
    },
    {
        "id": "ks4-response-to-exercise-s24",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the immediate effect of exercise on heart rate with its effect on "
               "breathing depth.",
        "options": [
            "Heart rate falls while breathing depth rises during exercise",
            "Neither heart rate nor breathing depth changes during exercise",
            "Breathing depth falls while heart rate rises during exercise",
            "Both heart rate and breathing depth rise together during exercise",
        ],
        "correct_index": 3,
        "why": "Exercise raises both heart rate and breathing depth together, as the body "
               "responds to the same rising demand for oxygen.",
    },
    {
        "id": "ks4-response-to-exercise-s25",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a football coach tracks how quickly players' heart rates fall "
               "during rest periods in training.",
        "options": [
            "It gives a practical measure of how fit and recovered each player currently "
            "is",
            "It shows exactly how much water each player has drunk that day personally "
            "that very same day",
            "A slow-falling heart rate means a player is not tired",
            "Heart rate recovery has no bearing on a player's fitness",
        ],
        "correct_index": 0,
        "why": "How quickly a player's heart rate falls in a rest period gives the coach a "
               "practical, repeatable measure of fitness and recovery.",
    },
    {
        "id": "ks4-response-to-exercise-s26",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine a swimmer's minute ventilation if they take 16 breaths per minute, "
               "each of 550 cm3.",
        "options": [
            "566 cm3",
            "8,800 cm3",
            "550 cm3",
            "16 cm3",
        ],
        "correct_index": 1,
        "why": "16 breaths x 550 cm3 each gives 8,800 cm3 of minute ventilation.",
    },

    # ══ harder · h05–h26 ═══════════════════════════════════════
    {
        "id": "ks4-response-to-exercise-h05",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that vasodilation during exercise serves only to cool the "
               "body down.",
        "options": [
            "It is correct; cooling is the sole reason blood vessels widen during "
            "exercise during any bout of exercise",
            "It is correct, provided the exercise takes place in a cold environment",
            "It is only part of the picture; widened vessels also deliver more blood to "
            "the working muscles",
            "It is wrong; vasodilation has no effect on blood flow to the muscles",
        ],
        "correct_index": 2,
        "why": "Vasodilation both helps lose heat and increases blood flow to the working "
               "muscles, so cooling is only part of its role.",
    },
    {
        "id": "ks4-response-to-exercise-h06",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient recovering from a heart condition is told their stroke volume is "
               "unusually low. Predict the effect on their heart rate during exercise, and "
               "explain.",
        "options": [
            "Heart rate would fall further, compounding the low stroke volume even more "
            "than before",
            "Heart rate would stay exactly the same as an unaffected person's",
            "Heart rate has no relationship to a person's stroke volume",
            "Heart rate would rise more than usual, to compensate for the lower volume "
            "pumped per beat",
        ],
        "correct_index": 3,
        "why": "With less blood pumped per beat, the heart must beat faster than usual to "
               "keep delivering enough blood to the muscles.",
    },
    {
        "id": "ks4-response-to-exercise-h07",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two athletes run the same race in an identical time, but one shows a much "
               "smaller rise in breathing rate than the other. Suggest what this shows about "
               "their fitness.",
        "options": [
            "The athlete with the smaller rise is likely the fitter of the two, needing "
            "to work their lungs less",
            "The athlete with the smaller rise is definitely the less fit of the two, not "
            "simply the fitter of the two by chance",
            "Breathing rate rise has no connection to a runner's fitness",
            "Both athletes must be equally fit, since their times were identical",
        ],
        "correct_index": 0,
        "why": "A smaller rise in breathing rate for the same effort suggests a more "
               "efficient, fitter cardiovascular and respiratory system.",
    },
    {
        "id": "ks4-response-to-exercise-h08",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's minute ventilation can rise by a much greater "
               "factor than their breathing rate alone during hard exercise.",
        "options": [
            "Minute ventilation depends on rate alone, so depth changes nothing about it "
            "during exercise",
            "Depth increases alongside rate, so the volume moved rises more than rate "
            "alone suggests",
            "Minute ventilation falls whenever breathing rate rises",
            "Breathing depth stays fixed no matter how hard a person exercises",
        ],
        "correct_index": 1,
        "why": "Because both rate and depth rise together, the total volume of air moved "
               "each minute increases by more than rate alone would suggest.",
    },
    {
        "id": "ks4-response-to-exercise-h09",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sports scientist records that an athlete's oxygen debt is much smaller "
               "after a race than after an identical race a year earlier. Suggest what "
               "training has most likely improved.",
        "options": [
            "The athlete's oxygen debt has no link to how well trained they are in recent "
            "months of training",
            "The athlete must be running the whole race more slowly than before this time",
            "Better aerobic capacity, so less of the race relied on anaerobic respiration",
            "The athlete's muscles have stopped needing any oxygen",
        ],
        "correct_index": 2,
        "why": "A smaller oxygen debt for the same race suggests improved aerobic capacity, "
               "so less of the effort had to rely on anaerobic respiration.",
    },
    {
        "id": "ks4-response-to-exercise-h10",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how quickly heart rate returns to resting level with how quickly "
               "breathing rate does so, after moderate exercise.",
        "options": [
            "Heart rate takes far longer to recover than breathing rate",
            "Neither heart rate nor breathing rate ever returns fully to its resting "
            "level to exactly its original state",
            "Breathing rate recovers, but heart rate does not return to its resting value",
            "Both generally recover over a broadly similar timescale, reflecting the same "
            "recovery processes",
        ],
        "correct_index": 3,
        "why": "Both heart rate and breathing rate are driven by the same underlying "
               "recovery processes, so they generally settle back over a similar timescale.",
    },
    {
        "id": "ks4-response-to-exercise-h11",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist's heart rate is 68 beats per minute at rest, pumping 72 cm3 per "
               "beat, and rises to 150 beats per minute during a climb, still pumping 72 cm3 "
               "per beat. Determine the increase in blood volume pumped per minute.",
        "options": [
            "5,904 cm3 per minute",
            "10,800 cm3 per minute",
            "4,896 cm3 per minute now",
            "82 cm3 per minute",
        ],
        "correct_index": 0,
        "why": "150 x 72 = 10,800 cm3 and 68 x 72 = 4,896 cm3, so the increase is 10,800 - "
               "4,896 = 5,904 cm3 per minute.",
    },
    {
        "id": "ks4-response-to-exercise-h12",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a footballer's oxygen debt after a match is likely to be smaller "
               "than a sprinter's after a 100 m race, even though the footballer exercises "
               "for far longer overall.",
        "options": [
            "A footballer's overall effort is more anaerobic than a sprinter's",
            "A sprint packs intense, mostly anaerobic effort into a few seconds, unlike "
            "the more varied pace of a match",
            "Oxygen debt depends just on the total time spent exercising",
            "A footballer does not rely on anaerobic respiration during a match",
        ],
        "correct_index": 1,
        "why": "A sprint concentrates intense, mostly anaerobic effort into a few seconds, "
               "while a match's pace varies and stays more aerobic overall.",
    },
    {
        "id": "ks4-response-to-exercise-h13",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient with a heart condition cannot raise their stroke volume during "
               "exercise. Predict how their body is likely to compensate to still deliver "
               "more oxygen to the muscles, and explain.",
        "options": [
            "The body cannot compensate for this in any way",
            "Blood vessels near the muscles would narrow instead of widening",
            "Heart rate would rise more than usual, since stroke volume cannot make up "
            "the difference",
            "Breathing would stop increasing, since it is unrelated to blood flow in any "
            "way whatsoever",
        ],
        "correct_index": 2,
        "why": "With stroke volume unable to rise, the heart compensates by beating faster, "
               "to keep total blood flow to the muscles rising.",
    },
    {
        "id": "ks4-response-to-exercise-h14",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the changes in blood distribution during exercise with the changes "
               "during rest after a large meal.",
        "options": [
            "Both direct extra blood to the same organs for the same reason",
            "Neither situation changes how blood is distributed around the body",
            "Exercise directs blood to the gut; digestion directs it to the muscles "
            "instead",
            "Exercise directs blood towards the muscles; digestion directs it towards the "
            "gut",
        ],
        "correct_index": 3,
        "why": "Blood is redirected towards whichever organs have the greater immediate "
               "demand — the muscles during exercise, the gut after a large meal.",
    },
    {
        "id": "ks4-response-to-exercise-h15",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a lower resting heart rate always means a person is "
               "fitter than someone with a higher one.",
        "options": [
            "It is not a reliable rule on its own; other factors, including genuine "
            "health conditions, can also lower it",
            "It is correct without exception; resting heart rate is the one useful "
            "measure of fitness of general fitness in every case",
            "It is wrong; resting heart rate does not reflect a person's fitness",
            "It is correct, provided the person is under the age of eighteen",
        ],
        "correct_index": 0,
        "why": "Resting heart rate is influenced by fitness but also by other factors, so a "
               "lower reading alone is not a reliable rule about fitness.",
    },
    {
        "id": "ks4-response-to-exercise-h16",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sprinter and a marathon runner are compared. Explain why the sprinter's "
               "muscles rely far more heavily on glycogen stores during their event.",
        "options": [
            "A marathon runner's muscles contain no glycogen stores",
            "A sprint's intense, short burst draws rapidly on the muscle's own local "
            "glycogen",
            "Glycogen stores are used mainly during a long, steady-paced marathon race, "
            "unlike in a sprint",
            "A sprinter's muscles convert all their glycogen into fat before the race "
            "even begins",
        ],
        "correct_index": 1,
        "why": "A sprint's sudden, intense demand is met largely by the muscle's own local "
               "glycogen store, broken down rapidly.",
    },
    {
        "id": "ks4-response-to-exercise-h17",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Over a rowing race, a competitor's heart climbs from a resting 62 beats per "
               "minute to 168 beats per minute, with the stroke volume fixed at 75 cm3 "
               "throughout. Work out how much extra blood this pumps each minute.",
        "options": [
            "12,600 cm3 per minute",
            "4,650 cm3 per minute",
            "7,950 cm3 per minute",
            "106 cm3 per minute",
        ],
        "correct_index": 2,
        "why": "168 x 75 = 12,600 cm3 and 62 x 75 = 4,650 cm3, so the increase is 12,600 - "
               "4,650 = 7,950 cm3 per minute.",
    },
    {
        "id": "ks4-response-to-exercise-h18",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a marathon runner's blood distribution differs from a sprinter's "
               "over the course of their event.",
        "options": [
            "A marathon runner sends no blood to their muscles at any point",
            "A sprinter's blood distribution does not change throughout their race",
            "Blood distribution is identical in both events, regardless of the distance",
            "A marathon holds a broadly steady distribution for longer, while a sprint "
            "shifts blood suddenly and briefly",
        ],
        "correct_index": 3,
        "why": "A marathon sustains a steady redirection of blood over a long period, while "
               "a sprint shifts blood suddenly for only a brief, intense effort.",
    },
    {
        "id": "ks4-response-to-exercise-h19",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that oxygen debt is repaid the instant a person stops "
               "exercising.",
        "options": [
            "It is wrong; heavy breathing continues for some time afterwards while the "
            "debt is gradually repaid",
            "It is correct; the debt vanishes within one second of stopping",
            "It is correct, provided the exercise was of low intensity",
            "It is wrong; oxygen debt is not repaid, however long a person rests",
        ],
        "correct_index": 0,
        "why": "Heavy breathing continues for some time after exercise stops, as the oxygen "
               "debt is repaid gradually rather than all at once.",
    },
    {
        "id": "ks4-response-to-exercise-h20",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A study compares two runners with identical race times but very different "
               "heart rate recovery afterwards. Suggest what the faster-recovering runner's "
               "result most likely reflects.",
        "options": [
            "A faster recovery has no bearing on either runner's underlying fitness",
            "A more efficient cardiovascular system, better able to restore normal "
            "circulation",
            "A slower race pace throughout, despite the identical finishing time of the "
            "whole distance",
            "A larger oxygen debt built up during the race itself",
        ],
        "correct_index": 1,
        "why": "Faster heart rate recovery generally reflects a more efficient "
               "cardiovascular system, better able to restore normal circulation after "
               "effort.",
    },
    {
        "id": "ks4-response-to-exercise-h21",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's minute ventilation rises by a far greater "
               "proportion than their heart rate during very hard exercise.",
        "options": [
            "Heart rate rises by a greater proportion than minute ventilation does",
            "Minute ventilation is fixed and cannot rise during exercise",
            "Breathing depth and rate can both rise sharply, whereas heart rate has a "
            "much lower practical ceiling",
            "Neither measure changes meaningfully during hard exercise",
        ],
        "correct_index": 2,
        "why": "Breathing rate and depth together can rise very sharply, while a heart's "
               "rate has a far lower practical ceiling it can reach.",
    },
    {
        "id": "ks4-response-to-exercise-h22",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist proposes measuring recovery heart rate, rather than resting "
               "heart rate alone, as a fitness test. Evaluate why recovery heart rate might "
               "be the more informative measure.",
        "options": [
            "Recovery heart rate has no connection to cardiovascular fitness",
            "Resting heart rate alone gives a complete picture of fitness",
            "Recovery heart rate can just be measured in a hospital setting",
            "It reflects how efficiently the whole cardiovascular system responds to and "
            "recovers from a real demand",
        ],
        "correct_index": 3,
        "why": "Recovery heart rate captures how the cardiovascular system responds to and "
               "recovers from an actual demand, not just its state at rest.",
    },
    {
        "id": "ks4-response-to-exercise-h23",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person's oxygen debt after exercise cannot simply be equal to "
               "the total oxygen used during the exercise.",
        "options": [
            "Aerobic respiration continues supplying most of the oxygen used throughout, "
            "so only the anaerobic shortfall needs repaying",
            "All of the oxygen used during exercise has to be fully repaid afterwards",
            "No oxygen is used during exercise, so there is nothing to repay",
            "Oxygen debt is unrelated to how the exercise was fuelled",
        ],
        "correct_index": 0,
        "why": "Most of the oxygen used during exercise is supplied as it happens by aerobic "
               "respiration; only the anaerobic shortfall becomes the debt to repay "
               "afterwards.",
    },
    {
        "id": "ks4-response-to-exercise-h24",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the oxygen debt of two sprinters running the same distance, one of "
               "whom finishes with visibly higher lactic acid levels than the other.",
        "options": [
            "The sprinter with higher lactic acid levels must have run with a smaller "
            "oxygen debt",
            "The sprinter with higher lactic acid levels most likely built up the larger "
            "oxygen debt",
            "Lactic acid level has no bearing on the size of a sprinter's oxygen debt",
            "Both sprinters must have built up exactly the same oxygen debt",
        ],
        "correct_index": 1,
        "why": "More lactic acid built up during the race points to a larger reliance on "
               "anaerobic respiration, and so a larger oxygen debt to repay.",
    },
    {
        "id": "ks4-response-to-exercise-h25",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a marathon runner never builds up any oxygen debt "
               "during their race.",
        "options": [
            "It is correct; a marathon is run entirely at an aerobic pace with no "
            "anaerobic effort at any stage of the event",
            "It is correct, provided the runner keeps a perfectly constant pace "
            "throughout",
            "It is not entirely true; brief surges, hills or a sprint finish can still "
            "demand some anaerobic effort",
            "It is wrong; a marathon runner builds the same oxygen debt as a sprinter",
        ],
        "correct_index": 2,
        "why": "Even a mostly aerobic marathon can include brief surges or a finishing "
               "sprint that demand some anaerobic effort, building a small oxygen debt.",
    },
    {
        "id": "ks4-response-to-exercise-h26",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why comparing two athletes' oxygen debt values only makes sense if "
               "their races were of a similar intensity and duration.",
        "options": [
            "Oxygen debt is identical regardless of the intensity or duration of a race",
            "Oxygen debt has no connection to how intense or how long a race is",
            "A shorter, gentler race produces a larger oxygen debt than a longer, harder "
            "one, contrary to what is generally observed in practice",
            "A harder or more anaerobic effort tends to build a bigger debt, so only "
            "similar efforts are fairly compared",
        ],
        "correct_index": 3,
        "why": "Oxygen debt reflects how anaerobic an effort was, so comparing it fairly "
               "needs races of a similar intensity and duration.",
    },
]
