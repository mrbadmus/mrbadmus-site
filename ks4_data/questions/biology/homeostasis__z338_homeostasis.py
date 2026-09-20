"""Biology · Homeostasis — the MRB-338 expansion of `homeostasis`.

The original twelve rows in `homeostasis.py` take the pancreas as coordination
centre, the effector role of a sweat gland, the 5 mmol/L glucose set point,
the hypothalamus coordinating both temperature and water, why a controlled
variable oscillates rather than sitting exactly on its set point, water
content as a third controlled condition, an effector failing to respond, and
the Arctic-to-desert argument for why homeostasis matters.

This file takes what they leave: the generic role of each of the three
components (receptor, coordination centre, effector) told from a fresh
example each time, what happens to enzymes and to cells at the two extremes
the spec names, multi-system scenarios where several controlled variables
change together (exercise, dehydration, a head injury, a hormone-blocking
drug), and the misconceptions that "negative feedback" means either "harmful"
or "keeps a value at exactly one point" or "prevents change happening at
all". `easier` recall stays close to naming the three components and the
three controlled conditions; `standard` and `harder` build genuine multi-step
scenarios, because that is where this subtopic's real demand sits once the
headline facts are known.
"""

TOPIC = "homeostasis"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05-e12 ═════════════════════════════════════════════════
    {
        "id": "ks4-homeostasis-e05",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a homeostatic control system, what is the role of a "
                "receptor?",
        "options": [
            "It detects a change in the internal environment and sends a signal to the coordination centre",
            "It carries out the response that corrects the deviation",
            "It compares the signal against the set point",
            "It stores the set point for future use",
        ],
        "correct_index": 0,
        "why": "A receptor's job is detection — sensing that a condition has "
               "changed and generating a signal about it.",
    },
    {
        "id": "ks4-homeostasis-e06",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What name is given to the target value that a homeostatic "
                "system tries to keep a condition at?",
        "options": [
            "The stimulus — the original change that starts the whole control system running",
            "The set point",
            "The coordination centre",
            "The negative feedback loop",
        ],
        "correct_index": 1,
        "why": "The set point is the value the system is trying to hold a "
               "condition at, against which the coordination centre compares "
               "each reading.",
    },
    {
        "id": "ks4-homeostasis-e07",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which three conditions does the human body control through "
                "homeostasis?",
        "options": [
            "Blood pressure and pulse rate",
            "Breathing rate and body mass index",
            "Body temperature, blood glucose concentration and water content",
            "Muscle mass, bone density, blood pressure and resting heart rate",
        ],
        "correct_index": 2,
        "why": "The three conditions homeostasis is specified to control are "
               "body temperature, blood glucose concentration and water "
               "content.",
    },
    {
        "id": "ks4-homeostasis-e08",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "If core body temperature rises well above 37 °C, what "
                "happens to the enzymes controlling the body's reactions?",
        "options": [
            "They become more active, so reactions speed up further",
            "They change colour a little, though their activity stays exactly the same",
            "They multiply rapidly, producing many more copies in every cell",
            "They denature, and the reactions they control slow or stop",
        ],
        "correct_index": 3,
        "why": "Far above the optimum, an enzyme's active site changes shape "
               "permanently, and it can no longer catalyse its reaction.",
    },
    {
        "id": "ks4-homeostasis-e09",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the first effect on the brain if blood glucose "
                "concentration falls very low.",
        "options": [
            "Brain cells are starved of glucose, so the person quickly becomes confused or faints",
            "The brain releases glucose stored inside its own cells",
            "The brain begins to shiver in order to generate glucose",
            "The brain stops receiving impulses from the spinal cord",
        ],
        "correct_index": 0,
        "why": "The brain depends almost entirely on glucose for respiration, "
               "so a low supply causes confusion very quickly.",
    },
    {
        "id": "ks4-homeostasis-e10",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "If a person's blood becomes more dilute than normal, what "
                "happens to their body cells?",
        "options": [
            "Water moves out of the cells by osmosis and they shrink",
            "Water moves into the cells by osmosis and they swell",
            "The cells are unaffected, since water cannot cross a membrane",
            "The cell membrane actively pumps the extra water straight back out into the blood plasma",
        ],
        "correct_index": 1,
        "why": "A more dilute blood draws water into the more concentrated "
               "cells by osmosis, and they swell.",
    },
    {
        "id": "ks4-homeostasis-e11",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where in the body are the receptors that detect the "
                "temperature of the surroundings found?",
        "options": [
            "In the wall of the small intestine",
            "In the retina at the back of each eye",
            "In the skin itself",
            "In the muscles of the upper arm and thigh, which contract to help generate heat",
        ],
        "correct_index": 2,
        "why": "Thermoreceptors in the skin detect the temperature of the "
               "immediate surroundings and signal it to the coordination "
               "centre.",
    },
    {
        "id": "ks4-homeostasis-e12",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What is meant by an 'effector' in a homeostatic control "
                "system?",
        "options": [
            "A structure that detects the original change in a condition",
            "A chemical messenger released into the blood that travels slowly to a distant target organ",
            "The point where a signal is compared with the set point",
            "Only a muscle or a gland can carry out the corrective response",
        ],
        "correct_index": 3,
        "why": "An effector is whatever physically carries out the "
               "correction — always a muscle or a gland.",
    },

    # ══ standard · s05-s26 ═══════════════════════════════════════════════
    {
        "id": "ks4-homeostasis-s05",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A marathon runner's core temperature rises during the race "
                "even though the air temperature has not changed. Explain "
                "the source of this heat.",
        "options": [
            "Respiration in the working muscles releases heat as a by-product, and harder exercise means more of both",
            "The air around the runner warms up as they run through it faster",
            "The runner's set point automatically rises during hard exercise",
            "Sweating itself generates extra heat as it leaves the sweat glands",
        ],
        "correct_index": 0,
        "why": "Muscle respiration releases heat as a by-product, and harder "
               "exercise means more respiration and more heat.",
    },
    {
        "id": "ks4-homeostasis-s06",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During the same race, the runner's blood glucose "
                "concentration and the water content of their blood both "
                "fall. Explain why two separate systems correct both at "
                "once.",
        "options": [
            "A single receptor in the pancreas detects both conditions",
            "Each condition has its own receptor and its own response",
            "Falling water content is what triggers the fall in glucose",
            "One single hormone is released that restores both conditions back to their set points together",
        ],
        "correct_index": 1,
        "why": "Blood glucose and water content are controlled by separate "
               "receptors and separate corrective pathways, so both can "
               "respond at once without depending on each other.",
    },
    {
        "id": "ks4-homeostasis-s07",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fever of 39 °C, though uncomfortable, does not "
                "itself denature the body's enzymes.",
        "options": [
            "Fevers only affect the skin, not enzymes deeper in the body",
            "The immune system actively shields every enzyme in the body from any change in temperature",
            "39 °C is still below the temperature at which enzymes denature",
            "Enzymes denature only once a person also becomes dehydrated",
        ],
        "correct_index": 2,
        "why": "Denaturation begins at around 40 °C, so a 39 °C fever, while "
               "unpleasant, has not yet crossed that threshold.",
    },
    {
        "id": "ks4-homeostasis-s08",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient is given an intravenous drip of pure water far "
                "faster than their kidneys can remove the excess. Predict "
                "the effect on their red blood cells.",
        "options": [
            "They lose water by osmosis and shrink",
            "They are unaffected, since red blood cells cannot take up water this way",
            "They release stored glucose to balance the extra water",
            "They take in water by osmosis and may swell or burst",
        ],
        "correct_index": 3,
        "why": "Diluting the blood makes it less concentrated than the "
               "cells, so water enters them by osmosis and they can swell "
               "and burst.",
    },
    {
        "id": "ks4-homeostasis-s09",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a coordination centre, not just a receptor, is "
                "needed in a homeostatic system.",
        "options": [
            "A receptor only detects that a change has occurred; something else must compare it with the set point and choose the response",
            "A receptor works too slowly without help from a coordination centre",
            "A coordination centre exists only to store the set point",
            "A receptor cannot generate an electrical signal by itself",
        ],
        "correct_index": 0,
        "why": "Detection alone achieves nothing without a centre that "
               "compares the reading with the set point and decides what "
               "response is needed.",
    },
    {
        "id": "ks4-homeostasis-s10",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students argue about why humans keep a constant "
                "internal temperature. Student A says it is so cells don't "
                "freeze; Student B says it is so enzymes stay near their "
                "optimum. Evaluate their claims.",
        "options": [
            "A is closer to the truth — freezing is the greater danger",
            "B is closer to the truth — enzyme activity matters more than freezing",
            "Both are equally correct, because freezing and enzyme activity are really the same underlying issue",
            "Neither is correct — body temperature has no effect on enzymes",
        ],
        "correct_index": 1,
        "why": "Human body temperature is nowhere near freezing; the real "
               "reason it is controlled so closely is that enzymes work "
               "best within a narrow temperature range.",
    },
    {
        "id": "ks4-homeostasis-s11",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital patient's temperature control stops working "
                "properly after a head injury, and their skin no longer "
                "responds even though receptors still detect a change. "
                "Explain what has most likely failed.",
        "options": [
            "The receptors themselves are the most likely source of the fault",
            "The set point has increased on a permanent basis",
            "The coordination centre or the pathway to the effector",
            "The negative feedback loop has been replaced by a positive feedback loop instead",
        ],
        "correct_index": 2,
        "why": "If detection still works but the effector never responds, "
               "the fault lies between the two — in the coordination centre "
               "or the signal reaching the effector.",
    },
    {
        "id": "ks4-homeostasis-s12",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A doctor explains that dehydration makes blood glucose "
                "readings appear falsely high. Suggest why concentrating "
                "the blood in this way affects the reading.",
        "options": [
            "Dehydration causes the pancreas to release far less insulin than it would normally produce",
            "Dehydration prevents glucose from being absorbed into cells",
            "Dehydration causes glycogen to be converted to glucose faster",
            "Less water in the same blood volume makes glucose more concentrated",
        ],
        "correct_index": 3,
        "why": "Removing water from the blood without removing glucose "
               "raises the concentration of glucose in each millilitre "
               "sampled.",
    },
    {
        "id": "ks4-homeostasis-s13",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why homeostasis is described as keeping conditions "
                "'within narrow limits' rather than at one exact value.",
        "options": [
            "Negative feedback only acts once a change has already been detected, so the value always drifts a little before it is corrected",
            "The set point itself moves up and down freely",
            "Receptors are too inaccurate to detect a precise value",
            "Coordination centres allow large swings to save energy",
        ],
        "correct_index": 0,
        "why": "Negative feedback is corrective rather than preventive — the "
               "variable has to move away from the set point before "
               "anything is done, so it drifts before returning.",
    },
    {
        "id": "ks4-homeostasis-s14",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'The water content of blood does not really "
                "need controlling, because cells can survive any "
                "concentration.' Evaluate this claim.",
        "options": [
            "It is correct — only temperature and glucose need to be controlled",
            "It is wrong — cells can be damaged by shrinking or swelling",
            "It is correct — water content matters only to the kidneys, not to cells",
            "It is wrong, but only because blood would eventually freeze without any control",
        ],
        "correct_index": 1,
        "why": "A large enough shift in water content moves water into or "
               "out of cells by osmosis strongly enough to shrink or burst "
               "them.",
    },
    {
        "id": "ks4-homeostasis-s15",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete training hard experiences "
                "homeostatic responses for both temperature and water "
                "content at the same time.",
        "options": [
            "Hard exercise on its own raises body temperature and lowers water content directly, with no separate underlying cause",
            "Cold, thin air stops both systems working at the same time",
            "Exercise generates heat from respiration and loses water as sweat, so both respond",
            "Only the temperature system responds; water content is unaffected by exercise",
        ],
        "correct_index": 2,
        "why": "Exercise both releases heat through respiration and loses "
               "water through sweating, so it disturbs two controlled "
               "conditions at once.",
    },
    {
        "id": "ks4-homeostasis-s16",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a very premature baby, whose control systems "
                "are not yet fully developed, is nursed in an incubator.",
        "options": [
            "Incubators are able to speed up every one of the baby's enzyme reactions artificially",
            "A premature baby's set point is permanently different from an adult's",
            "Incubators remove the need for the baby to control blood glucose",
            "Its own control system cannot yet keep temperature stable unaided",
        ],
        "correct_index": 3,
        "why": "An incubator provides the stable warmth a premature baby's "
               "own, still-developing temperature control cannot yet "
               "guarantee.",
    },
    {
        "id": "ks4-homeostasis-s17",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug destroys the coordination centre that normally "
                "corrects a person's fluid balance, but their kidneys and "
                "skin receptors still work normally. Predict what happens.",
        "options": [
            "It drifts steadily away from the set point, because nothing is left to decide how the deviation should be corrected",
            "It corrects itself automatically, because the kidneys act as a backup coordinator",
            "It stays exactly at the set point, since receptors alone are sufficient",
            "It is unaffected, since fluid balance is controlled by temperature receptors",
        ],
        "correct_index": 0,
        "why": "Detection without a working coordination centre achieves "
               "nothing, since no decision is made and no corrective signal "
               "is sent.",
    },
    {
        "id": "ks4-homeostasis-s18",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why negative feedback, rather than a response that "
                "pushes a value further from its set point, is used to "
                "control internal conditions.",
        "options": [
            "A response that pushed the value further away would work exactly as well as one that opposed it",
            "A response pushing the value further away would worsen the deviation",
            "Pushing the value further away is avoided only to save energy",
            "Pushing the value further away happens between meals, not constantly",
        ],
        "correct_index": 1,
        "why": "A response has to oppose the deviation to correct it; a "
               "system that pushed the value further away would let it "
               "spiral out of control.",
    },
    {
        "id": "ks4-homeostasis-s19",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why two healthy people can have slightly different "
                "resting body temperatures and both still be considered "
                "normal.",
        "options": [
            "One of them must have a faulty coordination centre",
            "Homeostasis would only apply to one of the two people being compared here",
            "There is natural variation between individuals in what is normal",
            "Their receptors are detecting distinctly different external temperatures",
        ],
        "correct_index": 2,
        "why": "A healthy set point varies a little between individuals, so "
               "small differences between two healthy people are expected "
               "rather than a sign of fault.",
    },
    {
        "id": "ks4-homeostasis-s20",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures their own body temperature five times in "
                "one day and gets slightly different readings, all close to "
                "37 °C. Explain why.",
        "options": [
            "Body temperature changes by several degrees at different points across a single day, without being corrected",
            "The thermometer used must be unreliable throughout the day",
            "The set point itself changes several times during the day",
            "Negative feedback keeps temperature oscillating near the set point",
        ],
        "correct_index": 3,
        "why": "Because correction follows detection, temperature is "
               "always drifting slightly and being brought back, so exact "
               "repeats of a single value are not expected.",
    },
    {
        "id": "ks4-homeostasis-s21",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a person's cells if every "
                "homeostatic mechanism in their body stopped working at "
                "once.",
        "options": [
            "Conditions inside the body would drift further and further from their set points, damaging cells as they went",
            "Nothing would change, since cells can regulate themselves without any help",
            "The body would instantly reach a new, stable set of conditions",
            "Only the skin would be affected, since it senses external conditions",
        ],
        "correct_index": 0,
        "why": "Without correction, internal conditions would keep moving "
               "away from their set points until cells could no longer "
               "function.",
    },
    {
        "id": "ks4-homeostasis-s22",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the brain is especially vulnerable when "
                "homeostasis of blood glucose fails, compared with a "
                "muscle.",
        "options": [
            "The brain contains a far greater number of receptors than any other organ in the body",
            "The brain relies on glucose, but muscle can also use other fuels",
            "The brain cannot regulate its own temperature, unlike other organs",
            "The brain has no blood supply of its own, unlike muscle tissue",
        ],
        "correct_index": 1,
        "why": "Muscle can respire using fats as well as glucose, but the "
               "brain depends almost entirely on a steady glucose supply.",
    },
    {
        "id": "ks4-homeostasis-s23",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that homeostasis is 'the body fighting "
                "against nature'. Suggest a more accurate way to describe "
                "what it does.",
        "options": [
            "It changes the external environment to suit the body's needs",
            "It stops any external condition from ever changing at all",
            "It keeps the internal environment stable despite outside changes",
            "It gradually adjusts every one of the body's set points to match the surrounding weather conditions",
        ],
        "correct_index": 2,
        "why": "Homeostasis does not change the outside world; it keeps the "
               "inside of the body stable whatever the outside is doing.",
    },
    {
        "id": "ks4-homeostasis-s24",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the receptor and the effector in a homeostatic "
                "system can sometimes be found in the same organ.",
        "options": [
            "All receptors and effectors are always found in the same organ",
            "Effectors are never able to detect a change; that ability belongs only to receptors",
            "This happens only by coincidence and serves no functional purpose",
            "Some organs, such as the pancreas, both detect and help correct a change",
        ],
        "correct_index": 3,
        "why": "The pancreas is a good example: its cells detect the "
               "glucose concentration directly and also release the "
               "hormone that starts the correction.",
    },
    {
        "id": "ks4-homeostasis-s25",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student is asked to identify the coordination centre in "
                "an unfamiliar homeostatic system they have not studied "
                "before. Suggest what feature would identify it.",
        "options": [
            "It would receive a signal from a receptor and decide what response the deviation actually calls for",
            "It would be the structure furthest from the receptor in the body",
            "It would be a muscle or gland that physically changes the condition",
            "It would be the largest organ involved in the whole pathway",
        ],
        "correct_index": 0,
        "why": "Whatever else it looks like, a coordination centre's defining "
               "job is receiving a signal and deciding what response it "
               "calls for.",
    },
    {
        "id": "ks4-homeostasis-s26",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a large loss of blood, which lowers water "
                "content sharply, triggers a stronger response than a small "
                "dietary change in water intake.",
        "options": [
            "Blood loss and dietary changes always produce identical responses",
            "A larger deviation produces a larger corrective signal from the receptors",
            "Blood loss stops receptors detecting water content altogether",
            "Only dietary changes are ever able to trigger a response from the coordination centre at all",
        ],
        "correct_index": 1,
        "why": "The size of the receptors' signal reflects the size of the "
               "deviation, so a bigger disturbance drives a stronger "
               "corrective response.",
    },

    # ══ harder · h05-h26 ═════════════════════════════════════════════════
    {
        "id": "ks4-homeostasis-h05",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Homeostasis stops the internal "
                "environment changing at all.' Which correction is most "
                "accurate?",
        "options": [
            "It is correct — a healthy internal environment never changes at all",
            "It is correct, but only because the external environment never changes in any way at all",
            "It does not stop change — it corrects a deviation once it has already happened",
            "It is correct, because receptors are able to prevent any deviation before it can start",
        ],
        "correct_index": 2,
        "why": "Negative feedback is a response to a change that has already "
               "occurred, not a barrier that prevents any change from "
               "happening.",
    },
    {
        "id": "ks4-homeostasis-h06",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the effector for temperature control (shivering "
                "muscle) differs in kind from the effector for blood glucose "
                "control (the pancreas releasing a hormone).",
        "options": [
            "Both effectors are muscles, though one of them happens to contract a great deal faster than the other",
            "Both effectors are glands, but they release into different body fluids",
            "The pancreas is a muscle and shivering is caused by a gland instead",
            "One is a muscle contracting; the other is a gland secreting a chemical messenger",
        ],
        "correct_index": 3,
        "why": "An effector can be either kind: shivering is a muscular "
               "response, while the pancreas releasing a hormone is a "
               "glandular one.",
    },
    {
        "id": "ks4-homeostasis-h07",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rare condition destroys a patient's hypothalamus "
                "completely, but leaves the pancreas and skin receptors "
                "intact. Predict which homeostatic functions are lost.",
        "options": [
            "Temperature and water content control are lost, because the hypothalamus coordinates both, but blood glucose control continues unaffected",
            "All homeostatic control is lost, since the hypothalamus runs every system",
            "Only blood glucose control is lost; temperature and water content continue",
            "Nothing is lost, since the pancreas can take over every function",
        ],
        "correct_index": 0,
        "why": "The hypothalamus is the coordination centre for temperature "
               "and water content; blood glucose is coordinated separately "
               "by the pancreas, so it is unaffected.",
    },
    {
        "id": "ks4-homeostasis-h08",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim: 'A negative feedback system always keeps "
                "a variable exactly at its set point.'",
        "options": [
            "True — that is the definition of negative feedback",
            "False — it corrects deviations, so the variable oscillates around the point",
            "True, provided the receptor happens to be working correctly",
            "False — negative feedback deliberately avoids the set point altogether, on every single occasion",
        ],
        "correct_index": 1,
        "why": "Correction only follows detection, so a controlled variable "
               "is always oscillating gently around the set point rather "
               "than fixed on it.",
    },
    {
        "id": "ks4-homeostasis-h09",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student proposes a homeostatic system with a receptor and "
                "an effector, but no coordination centre. Evaluate whether "
                "this could reliably work.",
        "options": [
            "It would work identically to a normal system, just more simply",
            "It would work, because effectors are perfectly able to interpret raw receptor signals directly and without help",
            "It could not reliably work — nothing would compare the signal to a set point",
            "It would work better, since removing a step makes the system faster",
        ],
        "correct_index": 2,
        "why": "Detection alone carries no information about what the set "
               "point is or what response is appropriate; that decision is "
               "the coordination centre's job.",
    },
    {
        "id": "ks4-homeostasis-h10",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two conditions are compared: a small, brief rise in blood "
                "glucose after a snack, and a small, brief drop in room "
                "temperature. Explain what a healthy body does in each "
                "case.",
        "options": [
            "Only the glucose change produces a response, since temperature is fixed externally",
            "Only the temperature change produces a response, since glucose is always buffered by the liver instead",
            "Neither produces a response, since both changes are too small to detect",
            "Both would produce a response, since homeostasis reacts to deviations either way",
        ],
        "correct_index": 3,
        "why": "Homeostasis responds to a deviation from a set point "
               "whatever its size or direction, so both small changes are "
               "corrected.",
    },
    {
        "id": "ks4-homeostasis-h11",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because negative feedback 'opposes "
                "change', it must always lower a variable that has changed. "
                "Correct this misunderstanding.",
        "options": [
            "Negative feedback always opposes whichever direction the change was in, raising a variable that fell just as readily as it lowers one that rose",
            "Negative feedback only ever lowers a variable, never raises one",
            "Negative feedback only responds to variables that are already low",
            "Negative feedback only opposes changes caused by external factors",
        ],
        "correct_index": 0,
        "why": "'Negative' describes opposing the direction of the "
               "deviation, whichever way it runs, not always lowering the "
               "value.",
    },
    {
        "id": "ks4-homeostasis-h12",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why comparing a single body-temperature reading "
                "with the 37 °C set point is not enough on its own to "
                "diagnose a fault in the control system.",
        "options": [
            "One reading is always sufficient, since 37 °C is a fixed universal value",
            "A near-normal reading could still follow an abnormal response, and readings vary slightly anyway",
            "A single reading proves the system faulty unless it reads exactly 37.0 °C",
            "Body temperature cannot ever be measured accurately enough for any single reading to matter at all",
        ],
        "correct_index": 1,
        "why": "A near-normal reading can hide a fault in how it was "
               "reached, and small variation around the set point is normal "
               "rather than diagnostic.",
    },
    {
        "id": "ks4-homeostasis-h13",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect on blood glucose homeostasis of a fault "
                "that stops the pancreas's receptor cells detecting glucose "
                "concentration at all.",
        "options": [
            "Blood glucose would still be corrected normally, because the liver is able to detect it completely independently",
            "Only rises in blood glucose would go uncorrected; falls would still be detected",
            "Blood glucose would drift uncorrected both ways, since the change is never detected",
            "The fault would have no effect, since hormone release never depends on detection",
        ],
        "correct_index": 2,
        "why": "Both insulin and glucagon release depend on the pancreas's "
               "cells detecting glucose concentration, so losing that "
               "detection leaves both directions uncorrected.",
    },
    {
        "id": "ks4-homeostasis-h14",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how quickly the body can correct a sudden drop in "
                "blood glucose with how quickly it corrects a sudden drop in "
                "body temperature after stepping outside on a cold day.",
        "options": [
            "Blood glucose correction is instant; temperature correction takes minutes",
            "Temperature correction is instant; blood glucose correction, by contrast, takes several minutes to complete",
            "Both corrections are completed within a single heartbeat",
            "Both take some time, since hormone release and heat production are not instant",
        ],
        "correct_index": 3,
        "why": "Both glucagon release and the muscle response of shivering "
               "take a short but real time to build up their full "
               "corrective effect.",
    },
    {
        "id": "ks4-homeostasis-h15",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says organisms without a hypothalamus, such as "
                "insects, cannot show any form of homeostasis. Evaluate this "
                "claim using the definition of homeostasis.",
        "options": [
            "It is too strong — homeostasis means maintaining stable internal conditions, and that does not specifically require a hypothalamus",
            "It is correct, since only mammals can maintain a stable internal environment",
            "It is correct, since the hypothalamus is the only possible coordination centre",
            "It is too strong, but only because insects also happen to have a pancreas",
        ],
        "correct_index": 0,
        "why": "Homeostasis is defined by what it achieves — a stable "
               "internal environment — not by which structure coordinates "
               "it, so the claim overreaches.",
    },
    {
        "id": "ks4-homeostasis-h16",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a coordination centre needs to know the set "
                "point as well as the current reading from the receptor.",
        "options": [
            "It does not need the set point; the receptor already makes that comparison",
            "Without it there is no reference value to judge whether a correction is needed",
            "The set point is only needed to trigger the receptor in the first place",
            "The set point tells the effector, rather than the coordination centre, exactly how strong its response should be",
        ],
        "correct_index": 1,
        "why": "The coordination centre's job is comparison, and comparison "
               "is meaningless without knowing both the current reading and "
               "the value it should be near.",
    },
    {
        "id": "ks4-homeostasis-h17",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why very young children are more at risk from "
                "extreme temperatures than healthy adults, given what "
                "homeostasis requires.",
        "options": [
            "Children's cells denature at a much lower body temperature than adult cells do",
            "Children have a permanently different, and never-changing, set point from adults throughout life",
            "Their control systems, including temperature correction, are still developing",
            "Children's receptors detect temperature but send no signal anywhere",
        ],
        "correct_index": 2,
        "why": "A young child's corrective responses are not yet as "
               "efficient as an adult's, leaving them less able to hold "
               "temperature at the set point.",
    },
    {
        "id": "ks4-homeostasis-h18",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'If the effector for a system is destroyed, "
                "the receptor and coordination centre become useless.' "
                "Evaluate this.",
        "options": [
            "This is wrong — the receptor takes over the effector's role instead",
            "This is correct — without a working effector nothing at all continues to function properly",
            "This is wrong — the coordination centre can act as its own effector",
            "They can still detect and decide correctly; only the correction itself is lost",
        ],
        "correct_index": 3,
        "why": "Detection and decision-making do not depend on the effector "
               "working; only the actual physical correction is lost if "
               "the effector fails.",
    },
    {
        "id": "ks4-homeostasis-h19",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of the three headline conditions controlled "
                "by homeostasis would be affected by a two-hour hike in hot "
                "weather with no water taken.",
        "options": [
            "All three, always, because exercise raises temperature, uses up glucose and loses water through sweat together",
            "Only temperature, because glucose and water content are unaffected by exercise",
            "Only water content, because temperature and glucose stay constant during exercise",
            "None of the three, because homeostasis only responds to conditions at rest",
        ],
        "correct_index": 0,
        "why": "Sustained exercise in the heat raises heat production, uses "
               "up glucose for respiration, and loses water through sweat, "
               "disturbing all three conditions together.",
    },
    {
        "id": "ks4-homeostasis-h20",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that homeostasis and evolution are 'the "
                "same idea', since both help organisms survive. Evaluate "
                "this claim.",
        "options": [
            "They are the same, since both involve receptors detecting change",
            "They are different — homeostasis acts within a lifetime; evolution across generations",
            "They are the same, because both processes keep an organism's characteristics permanently fixed",
            "They are different, but only because evolution happens faster than homeostasis",
        ],
        "correct_index": 1,
        "why": "Homeostasis keeps one organism's internal conditions stable "
               "during its own life; evolution is a change in a "
               "population's characteristics over many generations.",
    },
    {
        "id": "ks4-homeostasis-h21",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why doctors treat a very high fever as a medical "
                "emergency even though, in one sense, it is the immune "
                "system working as intended.",
        "options": [
            "A fever is never linked to the immune system in any way",
            "Doctors treat fevers only because patients happen to find the sensation deeply uncomfortable",
            "Once temperature rises far enough, the risk of denaturation always outweighs the benefit",
            "Fevers are treated only to stop the set point rising permanently",
        ],
        "correct_index": 2,
        "why": "A fever that climbs too high threatens enzyme function "
               "throughout the body, and that danger eventually outweighs "
               "any advantage the raised temperature gives the immune "
               "system.",
    },
    {
        "id": "ks4-homeostasis-h22",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student is given two unlabelled graphs of a body "
                "condition over time: one oscillates gently around a fixed "
                "line, the other rises steadily with no correction. "
                "Determine which shows a homeostatic system working.",
        "options": [
            "The steadily rising graph, because homeostasis means steady change",
            "Neither, because a genuinely working system would show a perfectly flat, unchanging line at all times",
            "Both, because homeostasis cannot be identified from a graph alone",
            "The oscillating graph, since feedback keeps correcting it towards the set point",
        ],
        "correct_index": 3,
        "why": "A condition under negative feedback control drifts and is "
               "corrected repeatedly, producing gentle oscillation rather "
               "than either a flat line or unchecked drift.",
    },
    {
        "id": "ks4-homeostasis-h23",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an astronaut's body must work harder to maintain "
                "homeostasis in the extreme cold of open space than a "
                "person feels on the coldest UK winter day.",
        "options": [
            "The temperature difference between the body and its surroundings is far greater, so heat is lost much faster than on Earth",
            "Homeostasis does not operate at all outside the Earth's atmosphere",
            "The astronaut's set point is automatically lowered while in space",
            "Space suits remove the need for any homeostatic response at all",
        ],
        "correct_index": 0,
        "why": "The rate of heat loss depends on the temperature "
               "difference between the body and its surroundings, and that "
               "difference is far more extreme in space.",
    },
    {
        "id": "ks4-homeostasis-h24",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures body temperature every ten minutes "
                "during a two-hour run and plots the results. Explain why "
                "the graph is not a perfectly straight horizontal line at "
                "37 °C.",
        "options": [
            "The thermometer used must have been faulty throughout the run",
            "Feedback corrects deviations after they occur, so temperature drifts a little first",
            "Body temperature is not actually regulated at all during exercise",
            "The set point changes every ten minutes throughout the whole of a sustained two-hour run",
        ],
        "correct_index": 1,
        "why": "Because correction follows detection, temperature always "
               "drifts a little from the set point before the corrective "
               "response brings it back.",
    },
    {
        "id": "ks4-homeostasis-h25",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the timescale over which body temperature is "
                "corrected with the timescale over which blood glucose is "
                "corrected after a large meal.",
        "options": [
            "Temperature is corrected within seconds, while glucose takes several hours to correct fully",
            "Glucose is corrected in seconds; temperature takes hours",
            "Both act over minutes, since signals must travel through the blood or nerves first",
            "Both are corrected completely instantly, with absolutely no delay between detection and response",
        ],
        "correct_index": 2,
        "why": "Neither correction is instant: hormone release and the "
               "muscular or metabolic responses that follow both need a few "
               "minutes to take full effect.",
    },
    {
        "id": "ks4-homeostasis-h26",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student concludes that, because homeostasis keeps "
                "conditions stable, an organism showing homeostasis can "
                "never become ill. Evaluate this conclusion.",
        "options": [
            "It is sound, since homeostasis is able to prevent absolutely every possible illness a person could get",
            "It is sound, provided the organism always eats a healthy diet",
            "It is unsound, but only because homeostasis stops working after childhood",
            "It is unsound — homeostasis limits fluctuation but cannot prevent illness or injury",
        ],
        "correct_index": 3,
        "why": "Homeostasis only controls the internal conditions it is "
               "specified to control; it has no mechanism to prevent "
               "infection, injury or inherited disease.",
    },
]
