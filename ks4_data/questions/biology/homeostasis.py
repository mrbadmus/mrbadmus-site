"""Biology · Homeostasis and response — the twelve subtopics of AQA 4.5.

Covers homeostasis and negative feedback, the nervous system and synapses,
reflex actions, thermoregulation, the endocrine system, blood glucose and
diabetes, reproductive hormones, contraception and fertility treatment,
reaction time, and the Triple-only brain and eye subtopics.

Distractors are built from the four errors this topic actually produces in
a classroom: insulin and glucagon swapped, the reflex arc routed through the
conscious brain, vasodilation described as vessels "moving" to the surface,
and the concave/convex corrections for short- and long-sight reversed. The
accommodation questions and the eye-structure questions are all worded so
that no diagram is needed — the structures are named in order in the stem.

Four subtopics here are Triple-only (thermoregulation, the-brain, the-eye,
defects-of-the-eye); the other eight are BASE and carry no Higher-tier or
Triple-only content in either their stems or their options.
"""

TOPIC = "homeostasis"
SUBJECT = "biology"

QUESTIONS = [
    # ── homeostasis ─────────────────────────────────────────────────────
    {
        "id": "ks4-homeostasis-e01",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which organ acts as the coordination centre for the control "
                "of blood glucose concentration?",
        "options": [
            "The pancreas",
            "The liver",
            "The hypothalamus",
            "The pituitary gland",
        ],
        "correct_index": 0,
        "why": "The pancreas detects the glucose concentration of the blood "
               "and decides which hormone to release; the liver is only the "
               "effector that stores or releases glucose.",
    },
    {
        "id": "ks4-homeostasis-e02",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person becomes too hot and their sweat glands begin to "
                "release sweat. Which part of a homeostatic control system "
                "are the sweat glands acting as?",
        "options": [
            "The receptor",
            "The effector",
            "The coordination centre",
            "The set point",
        ],
        "correct_index": 1,
        "why": "An effector is the muscle or gland that carries out the "
               "corrective response — here the sweat glands make the sweat "
               "that cools the body.",
    },
    {
        "id": "ks4-homeostasis-e03",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a healthy person, blood glucose concentration is kept at "
                "approximately which value?",
        "options": [
            "0.5 mmol/L",
            "50 mmol/L",
            "5 mmol/L",
            "500 mmol/L",
        ],
        "correct_index": 2,
        "why": "Blood glucose is held close to 5 mmol/L, and only a small "
               "drift either side of that is tolerated before cells begin to "
               "be harmed.",
    },
    {
        "id": "ks4-homeostasis-e04",
        "subtopic_slug": "homeostasis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which region acts as the coordination centre for both body "
                "temperature and the water content of the blood?",
        "options": [
            "The thyroid gland in the neck",
            "The thermoreceptors in the skin",
            "The pancreas, behind the stomach",
            "The hypothalamus in the brain",
        ],
        "correct_index": 3,
        "why": "The hypothalamus receives signals from receptors, compares "
               "them with the set point and decides what the effectors must "
               "do.",
    },
    {
        "id": "ks4-homeostasis-s01",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A monitor records a patient's core temperature every minute. "
                "The readings rise and fall slightly around 37 °C "
                "rather than staying at exactly 37 °C. Explain why.",
        "options": [
            "The monitor is faulty — a healthy body holds 37 °C exactly",
            "Corrective responses begin only once temperature has already drifted",
            "The set point itself moves up and down every few minutes",
            "Receptors cannot detect any change smaller than one degree",
        ],
        "correct_index": 1,
        "why": "Negative feedback is corrective, not preventive: the variable "
               "has to move away from the set point before anything is done "
               "about it, so it always oscillates gently.",
    },
    {
        "id": "ks4-homeostasis-s02",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person drinks two litres of water in a few minutes. State "
                "which internal condition their body must now correct.",
        "options": [
            "The core body temperature",
            "The blood glucose concentration",
            "The water content of the blood",
            "The oxygen concentration of the blood",
        ],
        "correct_index": 2,
        "why": "Water content is one of the conditions homeostasis controls — "
               "too much water and cells swell, too little and they shrink.",
    },
    {
        "id": "ks4-homeostasis-s03",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a control system the receptor still detects a change, but "
                "the effector can no longer respond. Predict what happens to "
                "the internal condition being controlled.",
        "options": [
            "It returns to the set point more slowly than it normally would",
            "It is held at the set point by the coordination centre instead",
            "It returns to the set point but then overshoots it every time",
            "It keeps moving away from the set point and is not corrected",
        ],
        "correct_index": 3,
        "why": "Detecting a change achieves nothing on its own — without a "
               "working effector no corrective response is ever carried out.",
    },
    {
        "id": "ks4-homeostasis-s04",
        "subtopic_slug": "homeostasis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how homeostasis allows humans to live both in the "
                "Arctic and in a hot desert.",
        "options": [
            "Internal conditions stay near their set points whatever the weather",
            "Human enzymes have a different optimum in each climate",
            "The body slowly changes its set point to match the outside air",
            "Cells stop respiring whenever outside conditions are extreme",
        ],
        "correct_index": 0,
        "why": "Homeostasis keeps the internal environment stable and "
               "independent of the external one, so enzymes always work close "
               "to their optimum.",
    },
    {
        "id": "ks4-homeostasis-h01",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Negative feedback is called negative "
                "because the change it causes is bad for the body.' Which "
                "correction is needed?",
        "options": [
            "It is called negative because it only works when a value falls",
            "It is called negative because the receptor sends a weaker signal",
            "It is called negative because the response opposes the change",
            "It is called negative because it lowers the value of the set point",
        ],
        "correct_index": 2,
        "why": "'Negative' describes the direction of the response — it acts "
               "against the deviation, returning the variable to the set "
               "point.",
    },
    {
        "id": "ks4-homeostasis-h02",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students disagree. A says the coordination centre for "
                "temperature is the skin, because that is where you feel "
                "cold. B says it is the hypothalamus. Evaluate their claims.",
        "options": [
            "A is right — the skin decides the response as it detects first",
            "Both are right — the skin and the brain each decide one response",
            "Neither is right — the effectors decide once they get a signal",
            "B is right — the skin holds receptors, the brain decides",
        ],
        "correct_index": 3,
        "why": "Receptors only detect and signal; the coordination centre "
               "compares that signal with the set point and decides what the "
               "effectors must do.",
    },
    {
        "id": "ks4-homeostasis-h03",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's blood glucose stays at 12 mmol/L for hours after "
                "a meal instead of returning to about 5 mmol/L. Suggest which "
                "part of the control system is most likely to be failing.",
        "options": [
            "The effector response — glucose is not being stored away",
            "The receptor — nobody's pancreas can detect glucose directly",
            "The set point — it has permanently risen to 12 mmol/L here",
            "The stimulus — a meal no longer contains any carbohydrate",
        ],
        "correct_index": 0,
        "why": "The change is being detected but not corrected, so the fault "
               "lies in the response that should move glucose out of the "
               "blood.",
    },
    {
        "id": "ks4-homeostasis-h04",
        "subtopic_slug": "homeostasis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient is given too much salty fluid, so the water "
                "content of their blood falls below its normal level. Predict "
                "what happens to their body cells, and explain why.",
        "options": [
            "The cells swell and may burst, because water is drawn into them",
            "The cells shrink, because water leaves them by osmosis into the blood",
            "The cells are unchanged, because water cannot cross a cell membrane",
            "The cells shrink, because salt is actively pumped out of them",
        ],
        "correct_index": 1,
        "why": "Water content is one of the conditions homeostasis controls: "
               "if the blood becomes too concentrated, water moves out of the "
               "cells by osmosis and they shrink.",
    },

    # ── nervous-system ──────────────────────────────────────────────────
    {
        "id": "ks4-nervous-system-e01",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is part of the peripheral nervous system?",
        "options": [
            "The spinal cord, which runs down the back",
            "A nerve running from the spine to a muscle in the leg",
            "The relay neurones found inside the spinal cord",
            "The brain, protected inside the skull",
        ],
        "correct_index": 1,
        "why": "The peripheral nervous system is everything outside the brain "
               "and spinal cord — the nerves connecting the CNS to the rest "
               "of the body.",
    },
    {
        "id": "ks4-nervous-system-e02",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Approximately how fast can an electrical impulse travel "
                "along a neurone?",
        "options": [
            "Up to about 1.2 m/s",
            "Up to about 12 m/s",
            "Up to about 1200 m/s",
            "Up to about 120 m/s",
        ],
        "correct_index": 3,
        "why": "Impulses travel at up to about 120 m/s, which is why nervous "
               "responses are so much faster than hormonal ones.",
    },
    {
        "id": "ks4-nervous-system-e03",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these could a motor neurone carry an impulse to?",
        "options": [
            "A gland in the skin",
            "A receptor in the retina",
            "A relay neurone in the spinal cord",
            "A sensory neurone in the finger",
        ],
        "correct_index": 0,
        "why": "Motor neurones carry impulses to effectors, and an effector "
               "is always a muscle or a gland.",
    },
    {
        "id": "ks4-nervous-system-e04",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "After a neurotransmitter has triggered an impulse in the "
                "next neurone, what happens to it?",
        "options": [
            "It stays in the gap and keeps the next neurone firing",
            "It passes into the blood and is carried to the liver",
            "It is broken down by enzymes or taken back up",
            "It is turned into an electrical impulse and used up",
        ],
        "correct_index": 2,
        "why": "The transmitter has to be removed to reset the synapse, or "
               "the next neurone would keep firing after the signal has "
               "finished.",
    },
    {
        "id": "ks4-nervous-system-s01",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A disease gradually destroys the myelin sheath around a "
                "person's motor neurones. Predict the effect on their "
                "movements.",
        "options": [
            "Impulses travel faster, so movements become jerky",
            "Impulses stop at once and the muscle wastes away immediately",
            "Impulses cross synapses more slowly but travel normally along axons",
            "Impulses travel more slowly, so movements become slow and weak",
        ],
        "correct_index": 3,
        "why": "The myelin sheath insulates the axon and speeds conduction, "
               "so losing it slows the impulse reaching the muscle.",
    },
    {
        "id": "ks4-nervous-system-s02",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substance blocks the receptor proteins on the membrane of "
                "the second neurone at a synapse. Explain the effect on the "
                "signal.",
        "options": [
            "Transmitter is released but cannot trigger the next impulse",
            "Transmitter is no longer released from the first neurone at all",
            "The impulse jumps the gap instead, so the signal is unchanged",
            "The transmitter is released and crosses, but travels backwards",
        ],
        "correct_index": 0,
        "why": "The signal only continues if the transmitter binds to "
               "receptor proteins on the next neurone, so blocking them "
               "breaks the pathway.",
    },
    {
        "id": "ks4-nervous-system-s03",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a signal takes longer to travel a pathway "
                "containing several synapses than one of the same length "
                "containing none.",
        "options": [
            "The gap is wider than the whole length of the axon",
            "Impulses must be made stronger before they can cross a gap",
            "Transmitter has to be released and diffuse across each gap",
            "The neurones must physically join together before each signal",
        ],
        "correct_index": 2,
        "why": "Diffusion of the transmitter across the synaptic cleft takes "
               "time, so every extra synapse adds a small delay.",
    },
    {
        "id": "ks4-nervous-system-s04",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the transmitter released at a synapse affects "
                "the next neurone and not the other cells around it.",
        "options": [
            "The transmitter is too large to reach any other cell nearby",
            "Only the next neurone carries the matching receptor proteins",
            "The transmitter is destroyed the instant it leaves the vesicle",
            "Nearby cells are insulated from the gap by a layer of myelin",
        ],
        "correct_index": 1,
        "why": "A transmitter only affects a cell carrying receptor proteins "
               "of a complementary shape, so the signal stays on its own "
               "pathway.",
    },
    {
        "id": "ks4-nervous-system-h01",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a signal travels along an axon with how it "
                "passes from one neurone to the next.",
        "options": [
            "Electrical along the axon, chemical at the synapse",
            "Chemical along the axon, electrical across the synapse",
            "Electrical in both, but slower across the synapse",
            "Chemical in both, but much faster along the axon",
        ],
        "correct_index": 0,
        "why": "An impulse travels along a neurone as an electrical signal "
               "but can only cross the gap between neurones as a chemical.",
    },
    {
        "id": "ks4-nervous-system-h02",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Synapses only slow signals down, so it "
                "would be better if neurones were joined into one long "
                "fibre.' Suggest why synapses are useful.",
        "options": [
            "They make the impulse stronger each time it crosses one",
            "They allow impulses to travel in either direction as needed",
            "They keep signals one-way and direct them to the right pathway",
            "They store the signal so the same response can be repeated later on",
        ],
        "correct_index": 2,
        "why": "Transmitter is released on one side and receptors sit on the "
               "other, so a synapse fixes the direction of a signal and lets "
               "the CNS route it.",
    },
    {
        "id": "ks4-nervous-system-h03",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A poison stops vesicles fusing with the membrane of the "
                "first neurone at a synapse. Predict the effect at a synapse "
                "between a motor neurone and a muscle.",
        "options": [
            "The next neurone fires continuously, so the muscle stays contracted",
            "No transmitter is released, so the muscle gets no impulse and cannot move",
            "The impulse crosses more slowly, so the muscle contracts weakly",
            "The muscle contracts normally because the impulse is electrical",
        ],
        "correct_index": 1,
        "why": "Vesicles must fuse with the membrane to release "
               "neurotransmitter, and with no transmitter the signal stops at "
               "the synapse.",
    },
    {
        "id": "ks4-nervous-system-h04",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In one response, impulses travel a total of 1.2 m along "
                "neurones at 120 m/s, and the whole response takes 0.05 s. "
                "Calculate the total time spent crossing synapses.",
        "options": [
            "0.01 s",
            "0.06 s",
            "0.05 s",
            "0.04 s",
        ],
        "correct_index": 3,
        "why": "The impulses take 1.2 ÷ 120 = 0.01 s along the "
               "neurones, so the remaining 0.04 s of the 0.05 s is spent at "
               "synapses.",
    },

    # ── reflex-actions ──────────────────────────────────────────────────
    {
        "id": "ks4-reflex-actions-e01",
        "subtopic_slug": "reflex-actions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a reflex action?",
        "options": [
            "Deciding to catch a ball that is thrown to you",
            "Writing your name at the top of a page",
            "Blinking as an object moves towards your eye",
            "Walking across the classroom to a window",
        ],
        "correct_index": 2,
        "why": "A reflex is automatic and involuntary — the blink happens "
               "without any conscious decision being made.",
    },
    {
        "id": "ks4-reflex-actions-e02",
        "subtopic_slug": "reflex-actions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a typical time for a spinal reflex "
                "response?",
        "options": [
            "About 0.05 s",
            "About 0.5 s",
            "About 2.0 s",
            "About 5.0 s",
        ],
        "correct_index": 0,
        "why": "A spinal reflex takes roughly 0.04-0.1 s, several times "
               "faster than a voluntary response of 0.2-0.3 s.",
    },
    {
        "id": "ks4-reflex-actions-e03",
        "subtopic_slug": "reflex-actions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reflex is described as involuntary. What does this mean?",
        "options": [
            "It happens only when you decide to allow it",
            "It happens more slowly than a decided action",
            "It happens only in young children, not in adults",
            "It happens whether or not you choose it to",
        ],
        "correct_index": 3,
        "why": "Involuntary means the response is not under conscious "
               "control — you cannot decide to switch a reflex off.",
    },
    {
        "id": "ks4-reflex-actions-e04",
        "subtopic_slug": "reflex-actions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The knee-jerk reflex is tested by tapping the tendon just "
                "below the kneecap. What is the stimulus in this reflex?",
        "options": [
            "The impulse passing along the sensory neurone to the cord",
            "The tap that stretches the tendon below the knee",
            "The contraction of the muscle in the thigh",
            "The movement of the lower leg forwards",
        ],
        "correct_index": 1,
        "why": "The stimulus is the change that starts the reflex; the "
               "muscle contraction and the leg movement are the response.",
    },
    {
        "id": "ks4-reflex-actions-s01",
        "subtopic_slug": "reflex-actions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An injury destroys the relay neurones in one region of a "
                "patient's spinal cord. Predict the effect on a withdrawal "
                "reflex in the part of the body served by that region.",
        "options": [
            "The reflex is lost, though receptors and muscle still work",
            "The reflex still works but the person no longer feels the pain",
            "The reflex becomes faster because there is one fewer synapse",
            "The reflex still works because the brain takes over the pathway",
        ],
        "correct_index": 0,
        "why": "The relay neurone links the sensory and motor neurones inside "
               "the spinal cord — without it the arc is broken.",
    },
    {
        "id": "ks4-reflex-actions-s02",
        "subtopic_slug": "reflex-actions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person steps on a sharp stone and their foot lifts before "
                "they are aware of it. Explain how they become aware at all.",
        "options": [
            "The brain plays no part in the reflex and never learns about it",
            "Pain receptors in the skin work more slowly than touch receptors do",
            "The motor neurone signals the brain only after the muscle has moved",
            "The relay neurone also signals the brain, which learns of it later",
        ],
        "correct_index": 3,
        "why": "The reflex is completed in the spinal cord while a separate "
               "signal travels up to the brain, so awareness follows the "
               "response.",
    },
    {
        "id": "ks4-reflex-actions-s03",
        "subtopic_slug": "reflex-actions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why reflexes are described as survival mechanisms.",
        "options": [
            "Reflexes use stronger impulses that cause a bigger movement",
            "Reflexes move the body from danger before harm is done",
            "Reflexes can be practised until they become faster than thought",
            "Reflexes are learned in childhood and improve with experience",
        ],
        "correct_index": 1,
        "why": "The short spinal pathway produces the protective response in "
               "a fraction of the time a conscious decision would take.",
    },
    {
        "id": "ks4-reflex-actions-s04",
        "subtopic_slug": "reflex-actions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A voluntary response to a light takes 0.25 s and a reflex "
                "response takes 0.05 s. Calculate how many times faster the "
                "reflex is.",
        "options": [
            "0.2 times",
            "0.3 times",
            "5 times",
            "20 times",
        ],
        "correct_index": 2,
        "why": "0.25 ÷ 0.05 = 5, so the reflex response is five "
               "times faster than the voluntary one.",
    },
    {
        "id": "ks4-reflex-actions-h01",
        "subtopic_slug": "reflex-actions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'In a reflex the brain receives the signal "
                "and sends it straight back to the muscle, which is why it is "
                "quick.' Which correction is needed?",
        "options": [
            "The signal is sent by the brain but along a much shorter nerve",
            "The brain is not involved at all, and never becomes aware of it",
            "The signal reaches the muscle before any receptor has detected it",
            "The spinal cord completes the response before the brain acts",
        ],
        "correct_index": 3,
        "why": "The relay neurone connects sensory to motor inside the spinal "
               "cord, so the conscious brain is bypassed rather than used.",
    },
    {
        "id": "ks4-reflex-actions-h02",
        "subtopic_slug": "reflex-actions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug adds 4 ms of delay at every synapse. A spinal reflex "
                "arc contains 2 synapses and a voluntary pathway contains 6. "
                "Calculate how much more delay the voluntary pathway gains.",
        "options": [
            "8 ms",
            "16 ms",
            "24 ms",
            "32 ms",
        ],
        "correct_index": 1,
        "why": "The drug adds 6 × 4 = 24 ms to the voluntary pathway and "
               "2 × 4 = 8 ms to the reflex, a difference of 16 ms.",
    },
    {
        "id": "ks4-reflex-actions-h03",
        "subtopic_slug": "reflex-actions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the route taken by a reflex with the route taken by "
                "a voluntary response to the same stimulus.",
        "options": [
            "Both signals travel up to the brain, but the reflex uses faster neurones",
            "The reflex is processed by the brain and the voluntary response by the cord",
            "The reflex stops at the cord; the voluntary route goes to the brain and back",
            "Neither signal reaches the brain; only the number of synapses is different",
        ],
        "correct_index": 2,
        "why": "The reflex is completed within the spinal cord, while a "
               "voluntary response needs the extra journey up to the cortex "
               "and back down again.",
    },
    {
        "id": "ks4-reflex-actions-h04",
        "subtopic_slug": "reflex-actions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newborn baby grips a finger placed in its palm, although "
                "it has never done so before. Suggest why this reflex needs "
                "no learning.",
        "options": [
            "Reflex arcs are fixed nerve pathways that need no conscious learning",
            "Newborn babies have faster neurones than adults do",
            "The baby copies the movement from watching an adult do it",
            "A newborn's brain processes incoming signals faster than an adult's does",
        ],
        "correct_index": 0,
        "why": "A reflex depends on a built-in pathway from receptor to "
               "effector, so it works from birth without any practice.",
    },

    # ── thermoregulation (TRIPLE only) ──────────────────────────────────
    {
        "id": "ks4-thermoregulation-e01",
        "subtopic_slug": "thermoregulation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which muscles contract to make the body hairs stand upright "
                "when a person is cold?",
        "options": [
            "The circular muscles around the skin pores",
            "The skeletal muscles just under the skin",
            "The smooth muscles in the walls of the sweat glands",
            "The erector pili muscles at the base of each hair",
        ],
        "correct_index": 3,
        "why": "Erector pili muscles pull the hairs upright so that a layer "
               "of warm air is trapped against the skin.",
    },
    {
        "id": "ks4-thermoregulation-e02",
        "subtopic_slug": "thermoregulation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "The hypothalamus receives temperature information from "
                "thermoreceptors in two places. Which two?",
        "options": [
            "The lungs and the liver",
            "The heart muscle and the kidneys",
            "The hypothalamus itself and the surface of the skin",
            "The spinal cord and the sweat glands",
        ],
        "correct_index": 2,
        "why": "Central thermoreceptors in the hypothalamus monitor the "
               "temperature of the blood, while peripheral ones in the skin "
               "sense the surroundings.",
    },
    {
        "id": "ks4-thermoregulation-e03",
        "subtopic_slug": "thermoregulation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Above roughly which core body temperature do human enzymes "
                "begin to denature?",
        "options": [
            "About 34 °C",
            "About 40 °C",
            "About 45 °C",
            "About 50 °C",
        ],
        "correct_index": 1,
        "why": "Above about 40 °C proteins including enzymes start to "
               "denature, which is why a very high fever is dangerous.",
    },
    {
        "id": "ks4-thermoregulation-e04",
        "subtopic_slug": "thermoregulation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sweat is produced by glands in the skin. What is sweat "
                "mainly made of?",
        "options": [
            "Water and dissolved salts",
            "Water and dissolved glucose",
            "Fat and dissolved proteins",
            "Water, salts and red blood cells",
        ],
        "correct_index": 0,
        "why": "Sweat is mostly water with dissolved salts, and it is the "
               "water evaporating that removes heat from the skin.",
    },
    {
        "id": "ks4-thermoregulation-s01",
        "subtopic_slug": "thermoregulation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a runner's skin looks flushed and red after a "
                "hard training session.",
        "options": [
            "Sweat glands push warm sweat into the skin and this colours it red",
            "The blood vessels in the skin move nearer to the surface of the body",
            "Arterioles near the skin widen, so more blood flows near the surface",
            "Red blood cells swell in the heat, which makes them easier to see",
        ],
        "correct_index": 2,
        "why": "Vasodilation brings more blood close to the skin surface so "
               "more heat is radiated away, and the extra blood makes the "
               "skin look red.",
    },
    {
        "id": "ks4-thermoregulation-s02",
        "subtopic_slug": "thermoregulation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why sweating cools a person less effectively on a "
                "hot day when the air is very humid.",
        "options": [
            "The air is already warm, so no heat at all can leave the skin",
            "Water evaporates more slowly, so less heat is taken from the skin",
            "Sweat glands stop working when the air contains a lot of water",
            "The skin absorbs water from the air instead of losing heat to it",
        ],
        "correct_index": 1,
        "why": "Cooling comes from the energy taken as sweat evaporates, so "
               "if evaporation is slow little heat is removed.",
    },
    {
        "id": "ks4-thermoregulation-s03",
        "subtopic_slug": "thermoregulation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a person's fingers turn pale after a long walk "
                "in very cold weather.",
        "options": [
            "Arterioles near the skin surface narrow, so less blood flows through them",
            "The blood in the fingers freezes slightly and loses its red colour",
            "Red blood cells are pulled back towards the heart by the cold",
            "Sweat on the surface of the skin makes the fingers look paler",
        ],
        "correct_index": 0,
        "why": "Vasoconstriction reduces blood flow to the skin so that less "
               "heat is lost, and less blood near the surface makes the skin "
               "look pale.",
    },
    {
        "id": "ks4-thermoregulation-s04",
        "subtopic_slug": "thermoregulation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why goosebumps do far less to keep a human warm than "
                "raised fur does for a cat.",
        "options": [
            "Human hairs lie flat again too quickly to trap any air at all",
            "Human skin is thicker, so the trapped air cannot reach the surface",
            "Human erector pili muscles are too weak to raise the hairs fully",
            "Humans have very little body hair, so little air is trapped",
        ],
        "correct_index": 3,
        "why": "The insulating effect depends on a layer of air held between "
               "raised hairs, and humans have too little hair to hold much.",
    },
    {
        "id": "ks4-thermoregulation-h01",
        "subtopic_slug": "thermoregulation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'When you get too hot, the blood vessels "
                "move towards the surface of the skin.' Which correction is "
                "needed?",
        "options": [
            "They stay where they are; they narrow so less blood reaches the skin",
            "They stay where they are; the arterioles widen and more blood flows",
            "They really do move, but only in the hands and in the feet",
            "They stay where they are; the heart pumps the blood harder instead",
        ],
        "correct_index": 1,
        "why": "Blood vessels cannot move — vasodilation is a widening of the "
               "arterioles that lets more warm blood flow close to the skin.",
    },
    {
        "id": "ks4-thermoregulation-h02",
        "subtopic_slug": "thermoregulation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of negative feedback, why sweating slows "
                "down as core temperature returns towards 37 °C.",
        "options": [
            "Receptors detect a smaller deviation, so the response is reduced",
            "The set point rises to match whatever temperature has been reached",
            "The sweat glands run out of water and cannot produce any more sweat",
            "The hypothalamus switches to the opposite response and begins shivering",
        ],
        "correct_index": 0,
        "why": "Negative feedback is self-limiting: as the variable returns "
               "to the set point the signal weakens and the corrective "
               "response fades.",
    },
    {
        "id": "ks4-thermoregulation-h03",
        "subtopic_slug": "thermoregulation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A runner in hot conditions drinks nothing for two hours and "
                "eventually stops sweating. Predict and explain what happens "
                "to their core temperature.",
        "options": [
            "It falls, because the body conserves the water it has left",
            "It stays at 37 °C, because vasodilation alone is enough",
            "It rises slowly, then the hypothalamus resets the set point",
            "It rises, because evaporative cooling has been lost",
        ],
        "correct_index": 3,
        "why": "Without evaporation from the skin the body loses its main way "
               "of removing heat, so heat from respiration and the "
               "surroundings builds up.",
    },
    {
        "id": "ks4-thermoregulation-h04",
        "subtopic_slug": "thermoregulation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare vasoconstriction with vasodilation.",
        "options": [
            "Constriction widens arterioles and raises heat loss; dilation narrows them again",
            "Both narrow the arterioles; constriction simply happens faster than dilation",
            "Constriction narrows arterioles and cuts heat loss; dilation does the opposite",
            "Both widen the arterioles; only the amount of sweat produced is different",
        ],
        "correct_index": 2,
        "why": "Constriction reduces blood flow near the skin so less heat is "
               "lost; dilation increases it so more heat is lost.",
    },

    # ── endocrine-system ────────────────────────────────────────────────
    {
        "id": "ks4-endocrine-system-e01",
        "subtopic_slug": "endocrine-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Endocrine glands differ from exocrine glands such as the "
                "salivary glands. State how an endocrine gland releases its "
                "product.",
        "options": [
            "Endocrine glands release hormones straight into the blood",
            "Endocrine glands release hormones along ducts into the gut",
            "Endocrine glands release hormones into the nerves beside them",
            "Endocrine glands release hormones directly onto the target organ",
        ],
        "correct_index": 0,
        "why": "Endocrine glands are ductless — they secrete their hormone "
               "into the bloodstream, which carries it around the whole body.",
    },
    {
        "id": "ks4-endocrine-system-e02",
        "subtopic_slug": "endocrine-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where in the body is the pituitary gland found?",
        "options": [
            "Just below the thyroid gland in the neck",
            "Just below the spinal cord where it meets the skull",
            "Just below the hypothalamus in the brain",
            "Just below the adrenal gland above the kidney",
        ],
        "correct_index": 2,
        "why": "The pituitary sits just under the hypothalamus, which is how "
               "the brain's control centre directs the endocrine system.",
    },
    {
        "id": "ks4-endocrine-system-e03",
        "subtopic_slug": "endocrine-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where are the adrenal glands found?",
        "options": [
            "In the neck, on either side of the windpipe",
            "Just above each kidney",
            "Behind the stomach, next to the small intestine",
            "In the brain, just below the hypothalamus",
        ],
        "correct_index": 1,
        "why": "There is one adrenal gland sitting on top of each kidney, and "
               "that is where adrenaline is made.",
    },
    {
        "id": "ks4-endocrine-system-e04",
        "subtopic_slug": "endocrine-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these organs is NOT an endocrine gland?",
        "options": [
            "The thyroid gland",
            "The pancreas",
            "The adrenal gland",
            "The liver",
        ],
        "correct_index": 3,
        "why": "The liver responds to hormones and stores glycogen, but it "
               "does not secrete hormones into the blood.",
    },
    {
        "id": "ks4-endocrine-system-s01",
        "subtopic_slug": "endocrine-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Adrenaline is released when a person is frightened. Suggest "
                "how its effects help them run from danger.",
        "options": [
            "It makes the muscles contract without needing any nerve impulses",
            "It lowers the amount of glucose the leg muscles need to respire",
            "It raises heart rate, so more oxygen reaches the muscles faster",
            "It slows breathing, so less energy is wasted while running away",
        ],
        "correct_index": 2,
        "why": "Adrenaline raises heart and breathing rates and sends more "
               "blood to the muscles, so they can respire faster and release "
               "more energy.",
    },
    {
        "id": "ks4-endocrine-system-s02",
        "subtopic_slug": "endocrine-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person is stung, pulls their hand away instantly, and is "
                "still shaky several minutes later. Explain the two responses.",
        "options": [
            "The endocrine system pulls the hand away while the nerves keep you shaky",
            "Nerves give the instant response; adrenaline keeps you ready for longer",
            "Both responses are nervous; the shakiness is a slow second reflex",
            "Both responses are hormonal; the fast one uses a stronger hormone",
        ],
        "correct_index": 1,
        "why": "Nervous responses are fast but brief, while hormonal ones are "
               "slower to start and last far longer.",
    },
    {
        "id": "ks4-endocrine-system-s03",
        "subtopic_slug": "endocrine-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Blood carries a hormone to every organ, yet only one organ "
                "responds to it. Explain why.",
        "options": [
            "The blood only carries the hormone to the organ that needs it",
            "The hormone is destroyed by every organ except its target organ",
            "Nerves guide the hormone from the gland to the correct organ",
            "Only the target organ has receptor proteins for that hormone",
        ],
        "correct_index": 3,
        "why": "Blood carries a hormone everywhere, but only cells with a "
               "complementary receptor protein can respond to it.",
    },
    {
        "id": "ks4-endocrine-system-s04",
        "subtopic_slug": "endocrine-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's thyroid gland produces too little thyroxine. "
                "Suggest why they feel cold and tired.",
        "options": [
            "Metabolic rate falls, so less energy and less heat are released in cells",
            "Metabolic rate rises, so energy is used up faster than it is made",
            "Blood glucose falls, so the brain has less glucose to respire",
            "Adrenaline is released constantly, which is tiring over time",
        ],
        "correct_index": 0,
        "why": "Thyroxine sets the rate of the chemical reactions in cells, "
               "so too little slows respiration and releases less energy and "
               "less heat.",
    },
    {
        "id": "ks4-endocrine-system-h01",
        "subtopic_slug": "endocrine-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Hormones travel along nerves to their "
                "target organ, which is why hormonal responses are the "
                "fastest in the body.' Evaluate this statement.",
        "options": [
            "Only the first part is wrong — hormonal responses really are fastest",
            "Both parts are wrong — hormones travel in blood and act more slowly",
            "Only the second part is wrong — hormones do travel along nerve fibres",
            "Neither part is wrong — this is a correct description of hormone action",
        ],
        "correct_index": 1,
        "why": "Hormones are carried dissolved in the blood, so they reach "
               "their targets far more slowly than a nerve impulse does.",
    },
    {
        "id": "ks4-endocrine-system-h02",
        "subtopic_slug": "endocrine-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Growth continues steadily over many years. Explain which "
                "communication system is better suited to controlling it.",
        "options": [
            "The nervous system, because an impulse can reach every cell along a nerve",
            "The nervous system, because its impulses can be repeated endlessly",
            "Either system, because the two work at exactly the same speed",
            "The endocrine system, because its effects are widespread and lasting",
        ],
        "correct_index": 3,
        "why": "Hormones circulate for hours or days and act on every organ "
               "with the right receptor, which suits a slow, body-wide "
               "process.",
    },
    {
        "id": "ks4-endocrine-system-h03",
        "subtopic_slug": "endocrine-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the body does not use a hormone to pull a hand "
                "away from a hot surface.",
        "options": [
            "A hormone would arrive far too late to prevent the burn",
            "A hormone cannot reach muscles, only glands and the liver",
            "Hormones are not made quickly enough by the adrenal glands",
            "Hormones would reach the hand but not the arm muscles above it",
        ],
        "correct_index": 0,
        "why": "Withdrawing a hand needs a response in hundredths of a "
               "second, and a hormone takes seconds or minutes to reach its "
               "target.",
    },
    {
        "id": "ks4-endocrine-system-h04",
        "subtopic_slug": "endocrine-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gland releases its hormone normally, but the receptor "
                "proteins on the target organ are faulty. Predict what "
                "happens.",
        "options": [
            "The gland stops making the hormone once no response occurs",
            "The hormone is destroyed at once, so its blood level falls fast",
            "The hormone circulates but the target organ does not respond",
            "The hormone acts on a different organ that has spare receptors",
        ],
        "correct_index": 2,
        "why": "A hormone can only act by binding to a receptor protein, so "
               "without working receptors the message arrives but is never "
               "read.",
    },

    # ── blood-glucose-diabetes ──────────────────────────────────────────
    {
        "id": "ks4-blood-glucose-diabetes-e01",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which cells of the pancreas release glucagon?",
        "options": [
            "The beta cells",
            "The alpha cells",
            "The liver cells",
            "The muscle cells",
        ],
        "correct_index": 1,
        "why": "Alpha cells detect a fall in blood glucose and release "
               "glucagon; the beta cells release insulin when glucose is too "
               "high.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-e02",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Glucose is stored in the liver as which molecule?",
        "options": [
            "Glycogen",
            "Glucagon",
            "Glycerol",
            "Cellulose",
        ],
        "correct_index": 0,
        "why": "Glycogen is the storage polymer, while glucagon is the "
               "hormone that breaks it back down — the two names are easy to "
               "confuse.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-e03",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What name is given to a blood glucose concentration that has "
                "fallen too low?",
        "options": [
            "Hyperglycaemia",
            "Glycogenolysis",
            "Hypothermia",
            "Hypoglycaemia",
        ],
        "correct_index": 3,
        "why": "'Hypo' means below, so hypoglycaemia is too little glucose in "
               "the blood, which affects the brain very quickly.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-e04",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which type of diabetes usually begins in childhood or "
                "adolescence?",
        "options": [
            "Type 2 diabetes, caused by body cells resisting insulin",
            "Neither type — both types are only ever diagnosed in adults",
            "Type 1 diabetes, caused by loss of insulin-producing cells",
            "Both types equally, because they have exactly the same cause",
        ],
        "correct_index": 2,
        "why": "Type 1 usually appears young, when the immune system destroys "
               "the beta cells that make insulin.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-s01",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why confusion and fainting are among the first signs "
                "that blood glucose has fallen too low.",
        "options": [
            "The brain relies almost entirely on glucose for respiration",
            "The brain is the first organ the blood reaches after a meal",
            "The brain has no blood supply of its own between meals",
            "Brain cells use glucose only once the muscles have finished",
        ],
        "correct_index": 0,
        "why": "The brain depends almost entirely on glucose as its energy "
               "source, so it is affected as soon as the supply falls.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-s02",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient with Type 2 diabetes has a normal level of insulin "
                "in their blood but a high blood glucose. Explain how both "
                "can be true.",
        "options": [
            "Their pancreas is releasing glucagon instead of insulin by mistake",
            "Their liver has run out of space to store any more glycogen",
            "The insulin they make has the wrong shape to be a hormone",
            "Their body cells no longer respond properly to the insulin",
        ],
        "correct_index": 3,
        "why": "In Type 2 diabetes the cells become resistant to insulin, so "
               "glucose is not taken out of the blood even though the hormone "
               "is there.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-s03",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why years of poorly controlled high blood glucose "
                "can lead to blindness and kidney failure.",
        "options": [
            "Glucose crystals block the airways and reduce the oxygen supply",
            "Glucose is turned into fat that coats the surface of the eye",
            "High glucose damages the walls of blood vessels, cutting blood supply",
            "High glucose stops the kidneys making any urine at all",
        ],
        "correct_index": 2,
        "why": "Persistently high glucose damages the walls of blood vessels, "
               "so tissues such as the retina and the kidney lose their blood "
               "supply.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-s04",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person with Type 1 diabetes injects their usual insulin "
                "dose and then plays football without eating. Predict what "
                "may happen to their blood glucose, and why.",
        "options": [
            "Blood glucose rises sharply, because exercise releases glycogen",
            "Blood glucose falls too low, because insulin and exercise both remove glucose",
            "Blood glucose stays the same, because the two effects are opposite",
            "Blood glucose rises slowly, because insulin stops working during exercise",
        ],
        "correct_index": 1,
        "why": "Insulin moves glucose out of the blood into storage while "
               "working muscles respire it, so together they can drive "
               "glucose dangerously low.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-h01",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'After a meal, glucagon is released and "
                "converts glucose into glycogen so blood glucose falls.' "
                "Which correction is needed?",
        "options": [
            "The hormone is right, but the glucose is stored in the pancreas",
            "The hormone is right, but blood glucose rises rather than falls",
            "The description is correct as it is written and needs no correction",
            "The hormone is wrong — it is insulin that causes glycogen storage",
        ],
        "correct_index": 3,
        "why": "Insulin is released when glucose is high and stores it as "
               "glycogen; glucagon does the opposite, releasing glucose from "
               "store.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-h02",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person's blood glucose rises from 5.0 mmol/L to 9.0 mmol/L "
                "after a meal. Calculate the percentage increase.",
        "options": [
            "44%",
            "4.0%",
            "80%",
            "180%",
        ],
        "correct_index": 2,
        "why": "The rise is 4.0 mmol/L, and 4.0 ÷ 5.0 × 100 = 80% of the "
               "starting value.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-h03",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why weight loss and exercise can control Type 2 "
                "diabetes but could never control Type 1.",
        "options": [
            "Type 1 patients cannot exercise safely, so it is never used",
            "Type 2 cells can regain sensitivity; Type 1 makes no insulin at all",
            "Type 2 is milder, so any treatment will work for it eventually",
            "Type 1 patients make too much insulin, which exercise cannot lower",
        ],
        "correct_index": 1,
        "why": "Weight loss and exercise make cells respond to insulin again, "
               "but nothing makes a pancreas with no beta cells produce "
               "insulin.",
    },
    {
        "id": "ks4-blood-glucose-diabetes-h04",
        "subtopic_slug": "blood-glucose-diabetes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim: 'Everyone who has diabetes has to inject "
                "insulin.'",
        "options": [
            "False — many Type 2 patients manage with diet, exercise and drugs",
            "True — both types of diabetes destroy the cells that make insulin",
            "True — insulin injection is the only treatment that lowers glucose",
            "False — nobody with diabetes ever needs to inject any insulin",
        ],
        "correct_index": 0,
        "why": "Type 1 always needs injected insulin, but Type 2 is often "
               "controlled by lifestyle change and medicines such as "
               "metformin.",
    },

    # ── human-reproduction-hormones ─────────────────────────────────────
    {
        "id": "ks4-human-reproduction-hormones-e01",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What name is given to the lining of the uterus?",
        "options": [
            "The corpus luteum",
            "The follicle",
            "The endometrium",
            "The cervix",
        ],
        "correct_index": 2,
        "why": "The endometrium is the uterus lining that thickens each cycle "
               "and is shed at menstruation.",
    },
    {
        "id": "ks4-human-reproduction-hormones-e02",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which event marks Day 1 of the menstrual cycle?",
        "options": [
            "The egg is released from one of the ovaries",
            "The uterus lining reaches its greatest thickness",
            "A follicle begins to mature inside the ovary",
            "The uterus lining begins to be shed",
        ],
        "correct_index": 3,
        "why": "Day 1 is the first day of menstruation, when the lining built "
               "up in the previous cycle breaks down and is lost.",
    },
    {
        "id": "ks4-human-reproduction-hormones-e03",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The corpus luteum forms after ovulation. What is it?",
        "options": [
            "What is left of the follicle after the egg is released",
            "The embryo before it implants in the uterus lining",
            "The thickened lining of the uterus in the second half",
            "An unfertilised egg that has begun to break down",
        ],
        "correct_index": 0,
        "why": "After ovulation the empty follicle becomes the corpus luteum, "
               "and this is what secretes progesterone.",
    },
    {
        "id": "ks4-human-reproduction-hormones-e04",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which change at puberty is caused by oestrogen?",
        "options": [
            "The voice breaking as the larynx enlarges",
            "Widening of the pelvis",
            "Growth of facial hair",
            "An increase in muscle mass",
        ],
        "correct_index": 1,
        "why": "Oestrogen from the ovaries causes female secondary sexual "
               "characteristics; the other three are caused by testosterone.",
    },
    {
        "id": "ks4-human-reproduction-hormones-s01",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A blood sample is taken on Day 20 of a 28-day menstrual "
                "cycle. Which hormone would be at its highest concentration?",
        "options": [
            "FSH, because a new follicle is already maturing",
            "LH, because the surge continues until menstruation",
            "Oestrogen, because the lining is still being repaired",
            "Progesterone, because the corpus luteum is active",
        ],
        "correct_index": 3,
        "why": "After ovulation the corpus luteum secretes progesterone to "
               "maintain the lining through the second half of the cycle.",
    },
    {
        "id": "ks4-human-reproduction-hormones-s02",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why it is useful that low levels of oestrogen "
                "inhibit the production of FSH.",
        "options": [
            "It stops several eggs maturing at the same time",
            "It stops the uterus lining being shed too early",
            "It keeps the LH surge going for the whole cycle",
            "It prevents progesterone from being made too soon",
        ],
        "correct_index": 0,
        "why": "FSH matures follicles, so damping it down keeps the ovary to "
               "roughly one mature egg per cycle.",
    },
    {
        "id": "ks4-human-reproduction-hormones-s03",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the uterus lining if the corpus "
                "luteum breaks down earlier than usual.",
        "options": [
            "Progesterone rises early and the uterus lining thickens further",
            "Progesterone falls early, so the lining breaks down sooner",
            "Oestrogen falls early, so ovulation happens a second time",
            "FSH falls early, so the next cycle cannot begin at all",
        ],
        "correct_index": 1,
        "why": "The corpus luteum is the source of progesterone, and it is "
               "progesterone that keeps the lining in place.",
    },
    {
        "id": "ks4-human-reproduction-hormones-s04",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "If an embryo implants, progesterone stays high instead of "
                "falling. Explain why this matters.",
        "options": [
            "It stops the embryo from dividing too quickly at first",
            "It restarts the cycle so a second egg can be released",
            "It keeps the lining in place to support the embryo",
            "It causes the lining to be shed and then rebuilt more thickly",
        ],
        "correct_index": 2,
        "why": "Menstruation would remove the lining the embryo is implanted "
               "in, so progesterone must stay high to prevent it.",
    },
    {
        "id": "ks4-human-reproduction-hormones-h01",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'FSH is made in the ovaries and causes the "
                "egg to be released on Day 14.' Which correction is needed?",
        "options": [
            "FSH is made in the pituitary and matures the egg; LH releases it",
            "FSH is made in the pituitary, and it does release the egg on Day 14",
            "FSH is made in the ovaries, but oestrogen is what releases the egg",
            "FSH is made in the ovaries and matures the egg; LH then releases it",
        ],
        "correct_index": 0,
        "why": "The pituitary makes FSH and LH; FSH matures the follicle, and "
               "it is the LH surge that triggers ovulation.",
    },
    {
        "id": "ks4-human-reproduction-hormones-h02",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woman's pituitary produces very little FSH. Explain the "
                "chain of events that means she does not ovulate.",
        "options": [
            "Without FSH the corpus luteum cannot form, so no egg is released",
            "Without FSH no follicle matures, so no oestrogen rise and no LH surge",
            "Without FSH the uterus lining is never shed, so ovulation is blocked entirely",
            "Without FSH progesterone stays high, which prevents an egg maturing",
        ],
        "correct_index": 1,
        "why": "FSH starts the chain: follicle growth produces the oestrogen "
               "that triggers the LH surge, and it is LH that releases the "
               "egg.",
    },
    {
        "id": "ks4-human-reproduction-hormones-h03",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Progesterone inhibits the production of FSH and LH. Explain "
                "why this is an example of negative feedback.",
        "options": [
            "The hormone increases its own production, making levels rise further",
            "The hormone has no effect on the pituitary, only on the uterus lining",
            "The hormone reduces the signals that would start another follicle",
            "The hormone speeds up the cycle so that ovulation happens sooner",
        ],
        "correct_index": 2,
        "why": "Negative feedback means the product acts back to reduce its "
               "own trigger, so high progesterone suppresses FSH and LH and "
               "no new follicle starts.",
    },
    {
        "id": "ks4-human-reproduction-hormones-h04",
        "subtopic_slug": "human-reproduction-hormones",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a woman with a 35-day cycle, ovulation happens 14 days "
                "before the next menstruation begins. Determine the day of "
                "the cycle on which she ovulates.",
        "options": [
            "Day 14",
            "Day 17",
            "Day 28",
            "Day 21",
        ],
        "correct_index": 3,
        "why": "35 minus 14 = 21, so ovulation falls on Day 21 rather than "
               "Day 14 in this longer cycle.",
    },

    # ── contraception-fertility ─────────────────────────────────────────
    {
        "id": "ks4-contraception-fertility-e01",
        "subtopic_slug": "contraception-fertility",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In IVF, what does 'in vitro' mean?",
        "options": [
            "Inside the fallopian tube",
            "Using hormone injections only",
            "Inside the uterus wall",
            "In glass — outside the body",
        ],
        "correct_index": 3,
        "why": "'In vitro' means in glass — the egg and sperm are mixed in a "
               "dish in a laboratory rather than inside the body.",
    },
    {
        "id": "ks4-contraception-fertility-e02",
        "subtopic_slug": "contraception-fertility",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which surgical method of contraception is used in women?",
        "options": [
            "A vasectomy, which cuts the vas deferens",
            "Tubal ligation, cutting the fallopian tubes",
            "A diaphragm that is fitted over the cervix",
            "A copper coil that is placed in the uterus",
        ],
        "correct_index": 1,
        "why": "Tying or cutting the fallopian tubes stops eggs reaching the "
               "uterus, and it is intended to be permanent.",
    },
    {
        "id": "ks4-contraception-fertility-e03",
        "subtopic_slug": "contraception-fertility",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "How often is the contraceptive injection normally given?",
        "options": [
            "Every day",
            "Every week",
            "Every 8-12 weeks",
            "Every 3 years",
        ],
        "correct_index": 2,
        "why": "One progesterone injection prevents ovulation for about two "
               "to three months, so it is repeated every 8-12 weeks.",
    },
    {
        "id": "ks4-contraception-fertility-e04",
        "subtopic_slug": "contraception-fertility",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which structure does a diaphragm cover?",
        "options": [
            "The cervix",
            "The ovary",
            "The fallopian tube",
            "The uterus lining",
        ],
        "correct_index": 0,
        "why": "A diaphragm is a barrier placed over the cervix so that sperm "
               "cannot pass through into the uterus.",
    },
    {
        "id": "ks4-contraception-fertility-s01",
        "subtopic_slug": "contraception-fertility",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the progesterone-only pill can still prevent "
                "pregnancy in a cycle in which ovulation does happen.",
        "options": [
            "It destroys any egg released from the ovary each month",
            "It thickens cervical mucus so sperm cannot reach the egg",
            "It makes the uterus lining shed before an embryo can implant",
            "It stops sperm being made in the male partner's testes",
        ],
        "correct_index": 1,
        "why": "The mini-pill works mainly by thickening the mucus at the "
               "cervix, so sperm are blocked even when an egg is released.",
    },
    {
        "id": "ks4-contraception-fertility-s02",
        "subtopic_slug": "contraception-fertility",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In IVF, progesterone is given after the embryo has been "
                "placed in the uterus. Explain why.",
        "options": [
            "To make the transferred embryo divide more quickly",
            "To stimulate the ovaries to release more eggs at once",
            "To keep the uterus lining thick for implantation",
            "To prevent the woman's immune system rejecting it",
        ],
        "correct_index": 2,
        "why": "Progesterone maintains the endometrium, and an embryo can "
               "only implant into a lining that is still thick.",
    },
    {
        "id": "ks4-contraception-fertility-s03",
        "subtopic_slug": "contraception-fertility",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why women given fertility drugs are more likely to "
                "have twins or triplets.",
        "options": [
            "Several eggs may mature and more than one be fertilised",
            "The drugs split a single fertilised egg into two separate embryos",
            "The drugs make the uterus lining thick enough for two",
            "The drugs make the woman ovulate twice in one cycle",
        ],
        "correct_index": 0,
        "why": "FSH stimulates the ovaries to mature several follicles at "
               "once, so more than one egg can be released and fertilised.",
    },
    {
        "id": "ks4-contraception-fertility-s04",
        "subtopic_slug": "contraception-fertility",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A man has a vasectomy but his testosterone level is "
                "unchanged afterwards. Explain why.",
        "options": [
            "Testosterone is made in the pituitary, not in the testes",
            "The operation removes the testes but not the adrenal glands",
            "Testosterone passes along the vas deferens with the sperm",
            "The testes still make the hormone, which enters the blood",
        ],
        "correct_index": 3,
        "why": "Cutting the vas deferens only blocks the tube carrying sperm; "
               "the testes are untouched and still secrete testosterone into "
               "the blood.",
    },
    {
        "id": "ks4-contraception-fertility-h01",
        "subtopic_slug": "contraception-fertility",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A couple ask whether IVF is worth trying when the woman is "
                "42. Evaluate their chances.",
        "options": [
            "It should always be offered, as success does not depend on age",
            "It should never be offered, as it cannot work after the age of 40",
            "It may well be worth trying, but success rates fall sharply with age",
            "It will certainly work, since 30-40% succeed on every cycle",
        ],
        "correct_index": 2,
        "why": "IVF succeeds in roughly 30-40% of cycles for women under 35 "
               "and less often with age, so it is possible but far from "
               "certain.",
    },
    {
        "id": "ks4-contraception-fertility-h02",
        "subtopic_slug": "contraception-fertility",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Each IVF cycle has a 35% chance of pregnancy, and the cycles "
                "are independent. Calculate the probability that a couple are "
                "still not pregnant after two cycles.",
        "options": [
            "42%",
            "30%",
            "70%",
            "12%",
        ],
        "correct_index": 0,
        "why": "The chance of one cycle failing is 65%, so two failing is "
               "0.65 × 0.65 = 0.42, which is 42%.",
    },
    {
        "id": "ks4-contraception-fertility-h03",
        "subtopic_slug": "contraception-fertility",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the copper coil with the contraceptive implant.",
        "options": [
            "Both use progesterone, but the coil simply releases it more slowly",
            "Both prevent ovulation, and the coil does this using copper ions",
            "Neither uses hormones; both work by killing sperm inside the uterus",
            "Only the implant uses a hormone; the coil's copper is toxic to sperm",
        ],
        "correct_index": 3,
        "why": "The implant releases progesterone to prevent ovulation, while "
               "the copper coil contains no hormone and acts by poisoning "
               "sperm.",
    },
    {
        "id": "ks4-contraception-fertility-h04",
        "subtopic_slug": "contraception-fertility",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one argument against creating more embryos during "
                "IVF than will be transferred to the uterus.",
        "options": [
            "The extra embryos make the whole treatment much less likely to work",
            "Unused embryos are frozen or destroyed, which some think is wrong",
            "Extra embryos always lead to twins or triplets being born",
            "Doctors are not allowed to store an embryo for longer than a day",
        ],
        "correct_index": 1,
        "why": "Spare embryos must be stored, donated or destroyed, and "
               "people disagree about the moral status of an early embryo.",
    },

    # ── reaction-time ───────────────────────────────────────────────────
    {
        "id": "ks4-reaction-time-e01",
        "subtopic_slug": "reaction-time",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What is meant by reaction time?",
        "options": [
            "The time between detecting a stimulus and responding",
            "The time an impulse takes to cross one single synapse",
            "The total time taken to carry out a whole experiment",
            "The length of time for which a stimulus lasts",
        ],
        "correct_index": 0,
        "why": "Reaction time covers the whole pathway — receptor, sensory "
               "neurone, CNS, motor neurone and effector.",
    },
    {
        "id": "ks4-reaction-time-e02",
        "subtopic_slug": "reaction-time",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the ruler drop test, which quantity is measured "
                "directly?",
        "options": [
            "The time between dropping and catching the ruler",
            "The speed at which the ruler is falling when caught",
            "The force with which the ruler is caught",
            "The distance the ruler falls before it is caught",
        ],
        "correct_index": 3,
        "why": "Such a short interval cannot be timed by hand, so the "
               "distance is measured and the time is calculated from it.",
    },
    {
        "id": "ks4-reaction-time-e03",
        "subtopic_slug": "reaction-time",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which type of stimulus do people generally respond to "
                "fastest?",
        "options": [
            "A change in the temperature of the air",
            "A light appearing on a screen",
            "A sound such as a starting pistol",
            "A smell released into the room",
        ],
        "correct_index": 2,
        "why": "Reactions to sound are typically slightly faster than "
               "reactions to light, which is why sprint starts use a sound.",
    },
    {
        "id": "ks4-reaction-time-e04",
        "subtopic_slug": "reaction-time",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What is a typical simple reaction time for a healthy adult?",
        "options": [
            "About 0.02 s",
            "About 0.25 s",
            "About 1.5 s",
            "About 3.0 s",
        ],
        "correct_index": 1,
        "why": "Simple human reaction times are usually 0.2-0.3 s, because "
               "the impulse must travel along neurones and across synapses.",
    },
    {
        "id": "ks4-reaction-time-s01",
        "subtopic_slug": "reaction-time",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a ruler drop test a student catches the ruler after it "
                "has fallen 5.0 cm. Calculate their reaction time. "
                "(g = 10 m/s²)",
        "options": [
            "1.0 s",
            "0.010 s",
            "0.0050 s",
            "0.10 s",
        ],
        "correct_index": 3,
        "why": "t = √(2 × 0.050 ÷ 10) = √0.010 = 0.10 s — the distance must be converted to metres "
               "first.",
    },
    {
        "id": "ks4-reaction-time-s02",
        "subtopic_slug": "reaction-time",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student has a reaction time of 0.40 s. Calculate how far a "
                "long rule would fall before they caught it. (g = 10 m/s²)",
        "options": [
            "1.6 m",
            "2.0 m",
            "0.80 m",
            "0.080 m",
        ],
        "correct_index": 2,
        "why": "d = ½ × 10 × 0.40² = ½ × 10 × 0.16 = 0.80 m.",
    },
    {
        "id": "ks4-reaction-time-s03",
        "subtopic_slug": "reaction-time",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Five trials give reaction times of 0.22 s, 0.19 s, 0.25 s, "
                "0.21 s and 0.23 s. Calculate the mean reaction time.",
        "options": [
            "0.19 s",
            "0.22 s",
            "0.28 s",
            "0.25 s",
        ],
        "correct_index": 1,
        "why": "The five values total 1.10 s, and 1.10 ÷ 5 = 0.22 s.",
    },
    {
        "id": "ks4-reaction-time-s04",
        "subtopic_slug": "reaction-time",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a computer-based reaction test gives a more "
                "accurate result than the ruler drop test.",
        "options": [
            "It removes the error in judging where the ruler was caught",
            "It uses a stimulus that the nervous system responds to faster",
            "It does not need the person to be paying any attention at all",
            "It measures the distance more accurately than a ruler does",
        ],
        "correct_index": 0,
        "why": "A computer times the interval directly, so the human error in "
               "reading a falling scale disappears.",
    },
    {
        "id": "ks4-reaction-time-h01",
        "subtopic_slug": "reaction-time",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students take the ruler drop test. A catches the ruler "
                "after 12 cm and B after 27 cm. Determine how many times "
                "longer B's reaction time is than A's.",
        "options": [
            "1.2 times",
            "2.25 times",
            "1.5 times",
            "0.67 times",
        ],
        "correct_index": 2,
        "why": "Distance is proportional to time squared, so the times are in "
               "the ratio √(27 ÷ 12) = √2.25 = 1.5.",
    },
    {
        "id": "ks4-reaction-time-h02",
        "subtopic_slug": "reaction-time",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student tests caffeine by measuring their reaction time "
                "once before a coffee and once 20 minutes after. Identify the "
                "biggest weakness in this method.",
        "options": [
            "The coffee should have been drunk before the very first measurement",
            "Only one measurement was made each time, so no mean could be calculated",
            "Reaction time cannot be measured accurately with a ruler at all",
            "The student should have tested a friend instead of themselves",
        ],
        "correct_index": 1,
        "why": "Reaction time varies randomly from trial to trial, so a "
               "single reading before and after cannot show a real effect.",
    },
    {
        "id": "ks4-reaction-time-h03",
        "subtopic_slug": "reaction-time",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Alcohol is a depressant. Explain, in terms of what happens "
                "at synapses, why it increases reaction time.",
        "options": [
            "It reduces transmitter activity, so fewer impulses get through",
            "It thickens the myelin sheath, so impulses travel much further",
            "It blocks the receptors in the skin, so no stimulus is ever detected",
            "It makes the synaptic gap wider so nothing can cross it at all",
        ],
        "correct_index": 0,
        "why": "A depressant lowers activity at synapses, so signals take "
               "longer to pass from one neurone to the next.",
    },
    {
        "id": "ks4-reaction-time-h04",
        "subtopic_slug": "reaction-time",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student's mean reaction time rises from 0.24 s to 0.30 s "
                "after a night without sleep. Calculate the percentage "
                "increase.",
        "options": [
            "6%",
            "20%",
            "24%",
            "25%",
        ],
        "correct_index": 3,
        "why": "The increase is 0.06 s, and 0.06 ÷ 0.24 × 100 = 25% of the original time.",
    },

    # ── the-brain (TRIPLE only) ─────────────────────────────────────────
    {
        "id": "ks4-the-brain-e01",
        "subtopic_slug": "the-brain",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Why is the cerebral cortex highly folded?",
        "options": [
            "To make room for the cerebellum beneath it",
            "To increase its surface area for more neurones",
            "To allow blood vessels to run across its surface",
            "To protect it from knocks against the skull",
        ],
        "correct_index": 1,
        "why": "Folding packs a much larger area of cortex, and so many more "
               "neurones, into the space inside the skull.",
    },
    {
        "id": "ks4-the-brain-e02",
        "subtopic_slug": "the-brain",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Approximately how many neurones does the human brain "
                "contain?",
        "options": [
            "About 86 thousand",
            "About 86 million",
            "About 86 billion",
            "About 86 trillion",
        ],
        "correct_index": 2,
        "why": "The brain holds roughly 86 billion neurones, each connected "
               "to thousands of others, which is why it is so complex.",
    },
    {
        "id": "ks4-the-brain-e03",
        "subtopic_slug": "the-brain",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which side of the cerebral cortex processes information "
                "coming from the right hand?",
        "options": [
            "Both sides equally, at the same time",
            "The right side, which is on the same side as the hand",
            "Neither side — the cerebellum does this instead",
            "The left side, on the opposite side of the body",
        ],
        "correct_index": 3,
        "why": "Each hemisphere deals with the opposite side of the body, so "
               "the left hemisphere handles the right hand.",
    },
    {
        "id": "ks4-the-brain-e04",
        "subtopic_slug": "the-brain",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "What is the blood-brain barrier?",
        "options": [
            "Packed cells that keep many substances out of brain tissue",
            "A layer of bone between the brain and the blood vessels",
            "A thick membrane that stops blood reaching the brain altogether",
            "The point where the spinal cord joins on to the base of the brain",
        ],
        "correct_index": 0,
        "why": "The barrier protects the brain from toxins and pathogens, but "
               "it also keeps many useful drugs out.",
    },
    {
        "id": "ks4-the-brain-s01",
        "subtopic_slug": "the-brain",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "After surgery a patient can move and speak normally but can "
                "no longer form new long-term memories. Which region was most "
                "likely removed?",
        "options": [
            "The cerebellum",
            "The medulla oblongata",
            "The hippocampus",
            "The spinal cord",
        ],
        "correct_index": 2,
        "why": "Removal of the hippocampus in patient HM left movement and "
               "speech intact but destroyed the ability to lay down new "
               "memories.",
    },
    {
        "id": "ks4-the-brain-s02",
        "subtopic_slug": "the-brain",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how an fMRI scan can show which region of the brain "
                "a person uses while they are speaking.",
        "options": [
            "It records the electrical waves the speech centres produce",
            "It stimulates each region in turn until speech is produced",
            "It measures the size of each region while a person speaks",
            "It detects the extra blood flowing to the active region",
        ],
        "correct_index": 3,
        "why": "An active brain region needs more oxygen, so fMRI locates "
               "activity by picking up the increased blood flow.",
    },
    {
        "id": "ks4-the-brain-s03",
        "subtopic_slug": "the-brain",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why damage to the medulla is far more likely to be "
                "fatal than damage to a similar volume of cerebral cortex.",
        "options": [
            "It controls heart rate and breathing, which cannot stop",
            "It contains far more neurones than the cortex does",
            "It is the only region with no blood supply of its own",
            "It stores all the memories a person has ever formed",
        ],
        "correct_index": 0,
        "why": "The medulla runs the unconscious functions that keep the body "
               "alive, so damage there stops breathing or the heartbeat.",
    },
    {
        "id": "ks4-the-brain-s04",
        "subtopic_slug": "the-brain",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "During surgery a conscious patient reports seeing a flash of "
                "light when one region is stimulated electrically. What does "
                "this tell the surgeon?",
        "options": [
            "That region is damaged and should be removed carefully",
            "That region is involved in processing what the eyes see",
            "That the patient's eyes have been damaged by the surgery",
            "That the stimulation has reached the optic nerve directly",
        ],
        "correct_index": 1,
        "why": "Stimulating a region and recording what the patient "
               "experiences maps that region on to the function it carries "
               "out.",
    },
    {
        "id": "ks4-the-brain-h01",
        "subtopic_slug": "the-brain",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the information an EEG gives with the information an "
                "fMRI gives.",
        "options": [
            "Both show blood flow, but the EEG is much quicker to carry out",
            "Both show electrical activity, but only the fMRI needs electrodes",
            "The EEG shows blood flow; the fMRI records electrical activity",
            "The EEG records electrical activity; the fMRI shows blood flow",
        ],
        "correct_index": 3,
        "why": "EEG electrodes on the scalp pick up electrical waves, while "
               "fMRI locates activity from the blood supplying it.",
    },
    {
        "id": "ks4-the-brain-h02",
        "subtopic_slug": "the-brain",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A new drug kills brain tumour cells grown in a laboratory "
                "dish. Suggest why it may still fail in a patient.",
        "options": [
            "The blood-brain barrier may stop it ever reaching the tumour",
            "Brain tumour cells cannot be grown in a dish at all",
            "Drugs always lose their effect once they enter the blood",
            "The tumour would have been removed before it was tried",
        ],
        "correct_index": 0,
        "why": "A drug can only work where it arrives, and the blood-brain "
               "barrier keeps many molecules out of brain tissue.",
    },
    {
        "id": "ks4-the-brain-h03",
        "subtopic_slug": "the-brain",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why so much of what is known about brain function "
                "has come from accidents and disease rather than from planned "
                "experiments.",
        "options": [
            "Brain tissue changes too quickly to be studied while alive",
            "Brain tissue cannot safely be biopsied or experimented on in a patient",
            "Scanners were only invented in the last five years",
            "The brain is too small for its regions to be separated",
        ],
        "correct_index": 1,
        "why": "Ethical limits mean the brain cannot be cut into or "
               "experimented on, so much has been learned from injury and "
               "disease.",
    },
    {
        "id": "ks4-the-brain-h04",
        "subtopic_slug": "the-brain",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why stem cell research is of particular interest for "
                "treating damage caused by a stroke.",
        "options": [
            "Stem cells can pass through the blood-brain barrier easily",
            "Stem cells destroy the scar tissue a stroke leaves behind",
            "Adult neurones cannot regenerate, so the damage is permanent",
            "Stem cells make the remaining neurones divide much faster",
        ],
        "correct_index": 2,
        "why": "Because damaged adult neurones are never replaced, growing "
               "replacements from stem cells is one of the few possible "
               "routes to recovery.",
    },

    # ── the-eye (TRIPLE only) ───────────────────────────────────────────
    {
        "id": "ks4-the-eye-e01",
        "subtopic_slug": "the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which photoreceptor cells allow a person to see in dim "
                "light, but not in colour?",
        "options": [
            "Cones",
            "Ciliary cells",
            "Rods",
            "Optic nerve cells",
        ],
        "correct_index": 2,
        "why": "Rods respond to low light intensity but not to colour, which "
               "is why everything looks grey at night.",
    },
    {
        "id": "ks4-the-eye-e02",
        "subtopic_slug": "the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which part of the retina holds the highest density of "
                "cones?",
        "options": [
            "The blind spot",
            "The fovea",
            "The outer edge of the retina",
            "The suspensory ligaments",
        ],
        "correct_index": 1,
        "why": "Cones are packed most densely at the fovea, which is why "
               "looking straight at something gives the sharpest colour "
               "vision.",
    },
    {
        "id": "ks4-the-eye-e03",
        "subtopic_slug": "the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Why does each eye have a blind spot?",
        "options": [
            "There are no photoreceptors where the optic nerve leaves",
            "The lens cannot focus light onto that part of the retina",
            "The cornea is thicker there and blocks the light coming in",
            "The iris casts a shadow onto that part of the retina",
        ],
        "correct_index": 0,
        "why": "At the point where the optic nerve leaves the eye there are "
               "no rods or cones, so light landing there cannot be detected.",
    },
    {
        "id": "ks4-the-eye-e04",
        "subtopic_slug": "the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which structures connect the lens to the ciliary muscle?",
        "options": [
            "The optic nerve fibres",
            "The circular muscles of the iris",
            "The layers of the retina",
            "The suspensory ligaments",
        ],
        "correct_index": 3,
        "why": "The suspensory ligaments transfer the pull of the ciliary "
               "muscle to the lens, which is how the lens changes shape.",
    },
    {
        "id": "ks4-the-eye-s01",
        "subtopic_slug": "the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person walks from a bright street into a dark cinema. "
                "Describe what happens in the iris.",
        "options": [
            "The circular muscles contract and the pupil gets smaller",
            "The radial muscles contract and the pupil gets wider",
            "Both sets of muscles relax and the pupil stays the same",
            "The lens becomes rounder to let more light through the pupil",
        ],
        "correct_index": 1,
        "why": "In dim light the radial muscles of the iris pull the pupil "
               "open so that more light can reach the retina.",
    },
    {
        "id": "ks4-the-eye-s02",
        "subtopic_slug": "the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how the pupil reflex differs from accommodation.",
        "options": [
            "The pupil reflex controls the light entering; accommodation focuses",
            "The pupil reflex focuses the image; accommodation controls light",
            "Both change the shape of the lens, but at different speeds",
            "Both change the size of the pupil, using different muscles",
        ],
        "correct_index": 0,
        "why": "The iris changes how much light gets in, while the lens "
               "changes shape to bring objects at different distances into "
               "focus.",
    },
    {
        "id": "ks4-the-eye-s03",
        "subtopic_slug": "the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student looks up from a book and focuses on a distant "
                "hill. Describe the changes in the ciliary muscle, the "
                "suspensory ligaments and the lens.",
        "options": [
            "Ciliary muscles contract, ligaments slacken, the lens gets rounder",
            "Ciliary muscles contract, ligaments tighten, the lens gets flatter",
            "Ciliary muscles relax, ligaments slacken, the lens gets rounder",
            "Ciliary muscles relax, ligaments tighten, the lens gets flatter",
        ],
        "correct_index": 3,
        "why": "Distant objects need less refraction, so the ciliary muscle "
               "relaxes, the ligaments pull tight and the lens is flattened.",
    },
    {
        "id": "ks4-the-eye-s04",
        "subtopic_slug": "the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why colours are very hard to tell apart by "
                "moonlight.",
        "options": [
            "The lens cannot refract the weak light enough to focus it",
            "The pupil is too wide for colours to be told apart",
            "There is too little light for the cones to respond",
            "The rods absorb all the coloured light before the cones can",
        ],
        "correct_index": 2,
        "why": "Cones need bright light to work, so in very dim conditions "
               "only the rods respond and vision is effectively monochrome.",
    },
    {
        "id": "ks4-the-eye-h01",
        "subtopic_slug": "the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The cornea provides about 70% of the eye's refraction. "
                "Explain why a lens is needed as well.",
        "options": [
            "The cornea's refraction is fixed; only the lens can be adjusted",
            "The cornea refracts light the wrong way and the lens corrects it",
            "The lens does most of the refraction once an object is close by",
            "The lens protects the retina from very bright light entering",
        ],
        "correct_index": 0,
        "why": "The cornea's curvature cannot change, so focusing on near and "
               "far objects depends entirely on the lens changing shape.",
    },
    {
        "id": "ks4-the-eye-h02",
        "subtopic_slug": "the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'To look at something close up, the "
                "ciliary muscles relax so that the lens can bulge.' Which "
                "correction is needed?",
        "options": [
            "The ciliary muscles do relax, but it is the cornea that bulges",
            "The ciliary muscles do relax, and the lens becomes flatter, not rounder",
            "The description is correct: relaxing the muscle lets the lens bulge",
            "The ciliary muscles contract; relaxing them would flatten the lens",
        ],
        "correct_index": 3,
        "why": "Contracting the ciliary muscle slackens the suspensory "
               "ligaments, letting the lens spring into a rounder, more "
               "powerful shape.",
    },
    {
        "id": "ks4-the-eye-h03",
        "subtopic_slug": "the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict the effect on a person's vision if their ciliary "
                "muscle became permanently relaxed.",
        "options": [
            "Near objects would be clear, distant ones blurred",
            "Both near and distant objects would be blurred",
            "Distant objects would be clear, near ones blurred",
            "Vision would be unaffected, as the cornea focuses light",
        ],
        "correct_index": 2,
        "why": "A relaxed ciliary muscle keeps the lens flat, which is the "
               "shape needed for distant objects but not for near ones.",
    },
    {
        "id": "ks4-the-eye-h04",
        "subtopic_slug": "the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person notices a bright light at the edge of their vision "
                "but cannot read small print there. Explain why.",
        "options": [
            "The lens focuses only the centre of the image onto the retina",
            "Cones are concentrated at the fovea, with mostly rods further out",
            "The blind spot covers the whole edge of the retina in each eye",
            "Light reaching the edge of the retina has passed through the iris",
        ],
        "correct_index": 1,
        "why": "Detail and colour come from cones, which are packed at the "
               "fovea, so the edge of the retina detects light but little "
               "detail.",
    },

    # ── defects-of-the-eye (TRIPLE only) ────────────────────────────────
    {
        "id": "ks4-defects-of-the-eye-e01",
        "subtopic_slug": "defects-of-the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which type of lens has a negative power value?",
        "options": [
            "A convex lens, which converges light",
            "A cornea reshaped by laser surgery",
            "Any lens used in a pair of reading glasses",
            "A concave lens, which diverges light",
        ],
        "correct_index": 3,
        "why": "Diverging (concave) lenses are given negative powers; "
               "converging (convex) lenses are positive.",
    },
    {
        "id": "ks4-defects-of-the-eye-e02",
        "subtopic_slug": "defects-of-the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "What is presbyopia?",
        "options": [
            "Long-sight caused by the lens stiffening with age",
            "Short-sight caused by the eyeball growing too long",
            "Loss of colour vision caused by damaged cone cells",
            "Blurring caused by the cornea becoming scratched",
        ],
        "correct_index": 0,
        "why": "As the lens loses flexibility it can no longer round up "
               "enough for near objects, which is why reading glasses are "
               "common after 40.",
    },
    {
        "id": "ks4-defects-of-the-eye-e03",
        "subtopic_slug": "defects-of-the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Where does a contact lens sit?",
        "options": [
            "Behind the iris, in front of the lens",
            "Directly on the cornea",
            "On the retina at the back of the eye",
            "Inside the pupil opening itself",
        ],
        "correct_index": 1,
        "why": "A contact lens rests on the cornea, so it refracts light "
               "before that light enters the eye, just as glasses do.",
    },
    {
        "id": "ks4-defects-of-the-eye-e04",
        "subtopic_slug": "defects-of-the-eye",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Short-sight has become far more common in young people. "
                "Which factor is thought to be linked to this?",
        "options": [
            "Eating far more sugar than previous generations did",
            "Watching television from across a large room",
            "More close-up work and less time spent outdoors",
            "Reading in bright sunlight for long periods",
        ],
        "correct_index": 2,
        "why": "The rise is associated with long periods of close focusing on "
               "screens and books, and with less time spent outside.",
    },
    {
        "id": "ks4-defects-of-the-eye-s01",
        "subtopic_slug": "defects-of-the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 55-year-old has always seen distant objects clearly but "
                "now needs glasses to read. Explain the cause.",
        "options": [
            "The lens has become less flexible, so it cannot round up",
            "The eyeball has grown longer, so the image falls short of it",
            "The cornea has become much more curved with age",
            "The retina has slowly moved forward inside the eye",
        ],
        "correct_index": 0,
        "why": "With age the lens stiffens and can no longer become rounded "
               "enough to focus near objects onto the retina.",
    },
    {
        "id": "ks4-defects-of-the-eye-s02",
        "subtopic_slug": "defects-of-the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a person with long-sight sees distant objects "
                "more clearly than near ones.",
        "options": [
            "Distant objects are larger, so less detail is needed",
            "Distant objects need less refraction to be focused",
            "Distant light enters through a wider part of the pupil",
            "Distant objects are focused by the cornea alone",
        ],
        "correct_index": 1,
        "why": "A long-sighted eye lacks refracting power, and distant "
               "objects need the least refraction, so those are the ones it "
               "can still focus.",
    },
    {
        "id": "ks4-defects-of-the-eye-s03",
        "subtopic_slug": "defects-of-the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a concave lens worn in front of a short-sighted "
                "eye brings the image onto the retina.",
        "options": [
            "It converges the light so that the focus moves forwards",
            "It blocks some of the light so the image looks sharper",
            "It diverges the light so the focus moves back to the retina",
            "It changes the shape of the cornea as the light passes through",
        ],
        "correct_index": 2,
        "why": "A short-sighted eye focuses light too soon, so spreading the "
               "rays out first pushes the focal point back onto the retina.",
    },
    {
        "id": "ks4-defects-of-the-eye-s04",
        "subtopic_slug": "defects-of-the-eye",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare glasses and contact lenses as ways of correcting a "
                "sight defect.",
        "options": [
            "Contact lenses use different lens types from those in glasses",
            "Contact lenses cannot correct long-sight, only short-sight",
            "Glasses reshape the cornea while contact lenses do not",
            "Both use the same lens types, but contacts risk infection",
        ],
        "correct_index": 3,
        "why": "Both use concave lenses for short-sight and convex for "
               "long-sight; the difference is that a contact lens sits on the "
               "eye and must be kept clean.",
    },
    {
        "id": "ks4-defects-of-the-eye-h01",
        "subtopic_slug": "defects-of-the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Long-sight is caused by the eyeball being "
                "too long, so the image forms in front of the retina.' Which "
                "correction is needed?",
        "options": [
            "The eyeball is too long, but the image would form behind the retina",
            "The eyeball is too short, and the image would form behind the retina",
            "The eyeball is the right length, but the lens is far too curved",
            "The description is correct — this is exactly what long-sight is",
        ],
        "correct_index": 1,
        "why": "A long-sighted eye is too short from front to back, so light "
               "from near objects has not yet converged when it reaches the "
               "retina.",
    },
    {
        "id": "ks4-defects-of-the-eye-h02",
        "subtopic_slug": "defects-of-the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why laser surgery for long-sight increases the "
                "curvature of the cornea.",
        "options": [
            "It flattens the cornea, so less refraction happens",
            "It thins the retina so that light reaches it more easily",
            "It curves the cornea more, so the focal point moves forwards",
            "It shortens the eyeball so the retina moves backwards",
        ],
        "correct_index": 2,
        "why": "A long-sighted eye needs more refraction, so increasing the "
               "cornea's curvature brings the focal point forward onto the "
               "retina.",
    },
    {
        "id": "ks4-defects-of-the-eye-h03",
        "subtopic_slug": "defects-of-the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 17-year-old asks whether they should have laser eye "
                "surgery instead of wearing glasses. Evaluate this.",
        "options": [
            "It is ideal, because young eyes heal fastest after surgery",
            "It is ideal, because it removes the need for glasses for life",
            "It is unsuitable, because lasers cannot reshape a young cornea",
            "It is unsuitable, because the prescription is not yet stable",
        ],
        "correct_index": 3,
        "why": "Laser surgery is permanent and is only offered to adults "
               "whose prescription has stopped changing.",
    },
    {
        "id": "ks4-defects-of-the-eye-h04",
        "subtopic_slug": "defects-of-the-eye",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person's eyeball is a normal length, but their lens stays "
                "too curved even when the ciliary muscles are fully relaxed. "
                "Determine the defect and how it is corrected.",
        "options": [
            "Short-sight, corrected with a concave lens",
            "Long-sight, corrected with a convex lens",
            "Short-sight, corrected with a convex lens",
            "Long-sight, corrected with a concave lens",
        ],
        "correct_index": 0,
        "why": "Too much refraction brings light to a focus in front of the "
               "retina — that is short-sight, and a diverging lens moves the "
               "focus back.",
    },
]
