"""Biology · Homeostasis — the MRB-338 expansion of `nervous-system`.

The original twelve rows in `nervous-system.py` take a nerve running to a leg
muscle as PNS, the 120 m/s top impulse speed, a motor neurone's target being a
gland, what happens to transmitter after it has acted, myelin loss slowing
conduction, a receptor-blocking poison, why extra synapses add delay, why
transmission is one-way, the electrical-inside/chemical-across contrast, why
synapses are useful rather than wasteful, a vesicle-blocking poison, and a
synapse-crossing-time calculation.

This file takes what they leave: the CNS/PNS definition itself, the three
neurone types told from their direction and their structure rather than their
speed, the synapse's own structure (pre-synaptic side, vesicles, receptor
proteins, breakdown or reabsorption), and how stimulant, depressant and SSRI
drugs act on it -- including what tolerance and addiction actually are at the
synapse, which the spec names but the baseline twelve never reach. `easier`
recall stays close to naming the parts; `standard` and `harder` build the
scenarios a real exam asks -- predicting from a described fault, comparing two
neurone types, and reasoning about a drug's effect from what it does at the
synapse rather than from memorising the drug's name.
"""

TOPIC = "homeostasis"
SUBJECT = "biology"

QUESTIONS = [
    {
        "id": "ks4-nervous-system-e05",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What two organs together make up the central nervous system?",
        "options": [
            "The brain and the spinal cord, which together process information and coordinate the body's responses",
            "The brain and the heart",
            "The spinal cord and the nerves",
            "The brain and every sense organ",
        ],
        "correct_index": 0,
        "why": "The CNS is defined as the brain and spinal cord; everything else is "
                "the peripheral nervous system.",
    },
    {
        "id": "ks4-nervous-system-e06",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In which direction does a sensory neurone carry an impulse?",
        "options": [
            "From the CNS to an effector, once a decision has been made about how to respond",
            "From a receptor to the CNS",
            "Only between two other neurones inside the CNS",
            "From one sense organ directly to another",
        ],
        "correct_index": 1,
        "why": "A sensory neurone's whole job is carrying the signal from where it "
                "was detected to the central nervous system.",
    },
    {
        "id": "ks4-nervous-system-e07",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where in the body is a relay neurone found?",
        "options": [
            "Only inside a muscle, where it helps trigger contraction directly",
            "Only inside a sense organ, where it helps detect a stimulus",
            "Entirely within the CNS",
            "Running the whole distance between a receptor and an effector",
        ],
        "correct_index": 2,
        "why": "A relay neurone connects sensory to motor neurones and never leaves "
                "the brain or spinal cord.",
    },
    {
        "id": "ks4-nervous-system-e08",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What is the function of the myelin sheath around a neurone?",
        "options": [
            "It manufactures the neurotransmitter the neurone will later release into the synapse",
            "It converts an electrical impulse into a chemical signal once it reaches the axon",
            "It anchors the neurone firmly in place within the tissue that surrounds it",
            "It insulates the axon",
        ],
        "correct_index": 3,
        "why": "The fatty myelin sheath insulates the axon, which allows the impulse "
                "to travel faster along it.",
    },
    {
        "id": "ks4-nervous-system-e09",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "On which side of a synapse are the vesicles of neurotransmitter "
                "found before an impulse arrives?",
        "options": [
            "In the pre-synaptic neurone, so it is ready to release them the instant an impulse arrives",
            "In the post-synaptic neurone",
            "Free-floating in the middle of the synaptic gap",
            "Equally split between both neurones",
        ],
        "correct_index": 0,
        "why": "Vesicles are stored in the sending (pre-synaptic) neurone, ready to "
                "fuse with its membrane and release their contents.",
    },
    {
        "id": "ks4-nervous-system-e10",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a stimulant drug such as caffeine does to activity at a "
                "synapse.",
        "options": [
            "It destroys the vesicles inside the pre-synaptic neurone so no further transmitter can ever be released",
            "It increases neurotransmitter activity there",
            "It reduces neurotransmitter activity there",
            "It widens the synaptic gap so nothing can cross it",
        ],
        "correct_index": 1,
        "why": "A stimulant increases activity at synapses, which raises alertness "
                "and speeds up nervous responses.",
    },
    {
        "id": "ks4-nervous-system-e11",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what kind of effect alcohol has on synaptic transmission, "
                "given that it is classified as a depressant.",
        "options": [
            "It increases neurotransmitter activity there, in the same way a stimulant would",
            "It permanently destroys the receptor proteins on the post-synaptic membrane",
            "It lowers activity there",
            "It has no measurable effect on synapses",
        ],
        "correct_index": 2,
        "why": "A depressant lowers activity at synapses, slowing reactions and "
                "reducing coordination.",
    },
    {
        "id": "ks4-nervous-system-e12",
        "subtopic_slug": "nervous-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "SSRIs are a type of antidepressant. Which neurotransmitter do they "
                "act on?",
        "options": [
            "Adrenaline, which SSRIs prevent the adrenal glands from releasing into the blood",
            "Insulin, which SSRIs stop the pancreas releasing after a meal",
            "Testosterone, which SSRIs block the testes from producing",
            "Serotonin",
        ],
        "correct_index": 3,
        "why": "SSRIs block the reabsorption of serotonin, keeping it in the synapse "
                "longer and helping to improve mood.",
    },
    {
        "id": "ks4-nervous-system-s05",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a sensory neurone carrying an impulse from a burnt "
                "finger is described as part of the PNS rather than the CNS, right up "
                "until it reaches the spinal cord.",
        "options": [
            "The PNS is every neurone outside the brain and spinal cord, and the finger and its nerve lie outside both",
            "Sensory neurones are only ever found inside the spinal cord",
            "The PNS only includes neurones that carry impulses towards an effector",
            "The finger itself counts as part of the central nervous system",
        ],
        "correct_index": 0,
        "why": "The PNS is defined by location — everything connecting the CNS to "
                "the rest of the body, including the long sensory neurone from a "
                "finger.",
    },
    {
        "id": "ks4-nervous-system-s06",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motor neurone running from the spinal cord to a muscle in the foot "
                "can be over a metre long. Explain why this neurone is heavily "
                "myelinated.",
        "options": [
            "Myelin is only ever added to neurones that carry impulses towards the CNS rather than away from it",
            "So the impulse still reaches the muscle quickly, despite the distance",
            "A neurone's length has no effect on whether it is myelinated",
            "Myelin protects the neurone from physical damage caused by the muscle it supplies",
        ],
        "correct_index": 1,
        "why": "Over a long axon, myelination matters even more, since it is what "
                "keeps the impulse travelling quickly enough for a timely response.",
    },
    {
        "id": "ks4-nervous-system-s07",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why someone who regularly uses a stimulant drug such as "
                "nicotine can become addicted to it.",
        "options": [
            "The drug permanently destroys every receptor protein found anywhere in the brain",
            "Addiction only ever happens with depressant drugs, never with a stimulant",
            "The brain adapts to the raised activity and needs the drug to feel normal",
            "The drug stops the pre-synaptic neurone releasing any transmitter",
        ],
        "correct_index": 2,
        "why": "With repeated stimulant use the brain adjusts to the raised level of "
                "transmitter activity, so it comes to depend on the drug to feel "
                "normal.",
    },
    {
        "id": "ks4-nervous-system-s08",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an SSRI antidepressant leaves more serotonin in the "
                "synapse than usual, even though it does not increase how much is "
                "released.",
        "options": [
            "It makes the pre-synaptic neurone release serotonin roughly twice as often as normal",
            "It widens the synaptic gap itself, so the serotonin already there simply lingers for longer",
            "It stops enzymes anywhere else in the body from breaking down any hormone at all",
            "It blocks its reabsorption after release",
        ],
        "correct_index": 3,
        "why": "Blocking reabsorption keeps the serotonin already released in the "
                "gap for longer, rather than increasing the amount released.",
    },
    {
        "id": "ks4-nervous-system-s09",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the structure of a sensory neurone with the structure of a "
                "motor neurone.",
        "options": [
            "A sensory neurone has a long dendron leading to the cell body; a motor neurone has a long axon leaving it, carrying the impulse to an effector",
            "Both carry impulses towards a receptor, along an identically shaped fibre",
            "A sensory neurone has no cell body at all, unlike a motor neurone",
            "A motor neurone is always shorter than a sensory neurone",
        ],
        "correct_index": 0,
        "why": "A sensory neurone's long fibre carries the impulse towards its cell "
                "body, while a motor neurone's long axon carries the impulse away "
                "from its cell body to the effector.",
    },
    {
        "id": "ks4-nervous-system-s10",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient is given a general anaesthetic before surgery, and no "
                "impulses can be initiated in the neurones it reaches. Suggest what "
                "this tells you about how the drug acts.",
        "options": [
            "It only slows conduction slightly, in much the same way a fall in temperature would",
            "It stops a neurone responding to a stimulus at all",
            "It has no effect on neurones at all and works purely on muscle tissue instead",
            "It only ever affects neurones inside the peripheral nervous system",
        ],
        "correct_index": 1,
        "why": "A general anaesthetic prevents an impulse from starting at all in "
                "the neurones it reaches, rather than merely reducing its speed.",
    },
    {
        "id": "ks4-nervous-system-s11",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the peripheral nervous system, rather than the central "
                "nervous system, is described as 'everywhere the CNS is not'.",
        "options": [
            "The CNS and PNS are really the same structure under two different names",
            "The PNS only exists in the limbs, rather than throughout the rest of the body",
            "Its job is connecting the CNS to every other part of the body",
            "The PNS is a small CNS copy inside major organs",
        ],
        "correct_index": 2,
        "why": "The nervous system is divided by location: the CNS processes "
                "information, and the PNS is every nerve carrying signals to and from "
                "it.",
    },
    {
        "id": "ks4-nervous-system-s12",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a stimulant such as cocaine can cause a dangerously fast "
                "heart rate.",
        "options": [
            "It converts electrical impulses into a faster form of energy that the heart then absorbs",
            "It stops the heart muscle contracting at its normal rate altogether",
            "It only ever acts on synapses found in the spinal cord, and nowhere else",
            "It raises synaptic activity generally, and that includes the heart's own pathway",
        ],
        "correct_index": 3,
        "why": "A stimulant raises synaptic activity generally, and that includes "
                "the pathways that speed up the heart.",
    },
    {
        "id": "ks4-nervous-system-s13",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a relay neurone is well suited to connecting sensory and "
                "motor neurones, rather than a sensory neurone connecting straight to "
                "a motor neurone.",
        "options": [
            "Being entirely inside the CNS lets it act as a junction where a signal can be passed on, filtered or directed to the correct pathway",
            "It is the only type of neurone able to carry an electrical impulse",
            "It is longer than either a sensory or a motor neurone",
            "It removes the need for any synapse in the whole pathway",
        ],
        "correct_index": 0,
        "why": "Sitting entirely within the CNS lets a relay neurone act as a "
                "processing junction, directing a signal to the right pathway.",
    },
    {
        "id": "ks4-nervous-system-s14",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient stops taking an SSRI suddenly after months of use. Suggest "
                "why their mood may worsen for a while afterwards.",
        "options": [
            "SSRIs permanently increase the total number of neurones found in the brain",
            "Their synapses had adjusted to the raised serotonin level",
            "Serotonin is only ever produced while a person is actually taking an SSRI",
            "Stopping the drug destroys the receptors",
        ],
        "correct_index": 1,
        "why": "The nervous system adjusts to a drug's presence, so removing it "
                "changes the balance the synapses had settled into.",
    },
    {
        "id": "ks4-nervous-system-s15",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why damage to the spinal cord, rather than to a peripheral "
                "nerve, is more likely to affect several different parts of the body "
                "at once.",
        "options": [
            "The spinal cord contains only a single neurone, shared by the whole of the body",
            "Peripheral nerves are never actually connected to the spinal cord at all",
            "Many peripheral nerves converge there, so one injury interrupts several pathways",
            "Spinal cord damage only ever affects the neurones directly above the injury site",
        ],
        "correct_index": 2,
        "why": "Because many peripheral pathways converge on the spinal cord, damage "
                "there can interrupt signals to and from several different body parts "
                "at once.",
    },
    {
        "id": "ks4-nervous-system-s16",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why doctors are cautious about prescribing depressant drugs "
                "such as sleeping tablets alongside alcohol.",
        "options": [
            "Alcohol is actually a stimulant, so it cancels out the effect of a sleeping tablet",
            "Sleeping tablets have no effect on the nervous system",
            "The two substances chemically neutralise one another completely inside the stomach",
            "Both lower synaptic activity, so together the effect is far greater",
        ],
        "correct_index": 3,
        "why": "Two depressants both reduce synaptic activity, so combining them can "
                "slow the nervous system far more than either alone.",
    },
    {
        "id": "ks4-nervous-system-s17",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the CNS and the PNS work completely independently of "
                "one another. Explain why this is wrong.",
        "options": [
            "The PNS carries every signal that reaches or leaves the CNS, so the two depend on each other constantly",
            "The CNS and PNS never actually connect to each other at any point",
            "The PNS only becomes active once the CNS has already stopped working",
            "Only the CNS is needed for a person to respond to a stimulus",
        ],
        "correct_index": 0,
        "why": "The PNS is the CNS's only connection to the rest of the body, so the "
                "two systems constantly depend on each other.",
    },
    {
        "id": "ks4-nervous-system-s18",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an SSRI takes several weeks to improve a patient's mood, "
                "even though it starts blocking serotonin reabsorption within hours.",
        "options": [
            "The drug genuinely has no real effect until it has been taken for several weeks",
            "The nervous system takes time to adjust to raised serotonin activity",
            "Serotonin only affects mood once it has built up inside a neurone's own nucleus",
            "The reabsorption process speeds up gradually over weeks",
        ],
        "correct_index": 1,
        "why": "Although the chemical change is immediate, the wider changes in the "
                "nervous system that improve mood take longer to develop.",
    },
    {
        "id": "ks4-nervous-system-s19",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student mixes up sensory and motor neurones. Suggest a reliable "
                "way to tell them apart from a labelled diagram.",
        "options": [
            "Sensory neurones are always drawn in a completely different colour from motor neurones",
            "Only a sensory neurone is ever shown connected to a synapse in a diagram",
            "Check the direction of travel",
            "Motor neurones are always drawn shorter than sensory neurones in every diagram",
        ],
        "correct_index": 2,
        "why": "Direction is the defining feature: sensory neurones carry impulses "
                "towards the CNS, motor neurones carry them away from it.",
    },
    {
        "id": "ks4-nervous-system-s20",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why heavy long-term alcohol use can permanently damage "
                "coordination, even years after a person stops drinking.",
        "options": [
            "Alcohol only ever affects coordination while a person is still actively drinking it",
            "Coordination is controlled entirely outside the nervous system, in the muscles themselves",
            "Alcohol strengthens every synapse it reaches, which then works far too quickly",
            "Damaged neurones are never replaced",
        ],
        "correct_index": 3,
        "why": "Prolonged, heavy depression of the nervous system can damage "
                "neurones directly, and unlike many other cells they are not replaced "
                "once lost.",
    },
    {
        "id": "ks4-nervous-system-s21",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a relay neurone with a fault that lets it fire on its "
                "own, without any signal from a sensory neurone, would cause problems "
                "even though the sensory and motor neurones either side of it are "
                "perfectly healthy.",
        "options": [
            "It could trigger a motor response with no real stimulus behind it at all, since the relay neurone is the link the whole pathway depends on",
            "It would have no effect, since a relay neurone cannot influence a motor neurone directly",
            "It would only affect the sensory neurone's own ability to detect a stimulus",
            "The fault would simply be corrected automatically by the motor neurone",
        ],
        "correct_index": 0,
        "why": "The relay neurone is the link the whole pathway depends on, so a "
                "fault there can trigger a response with no real stimulus behind it.",
    },
    {
        "id": "ks4-nervous-system-s22",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why doctors sometimes describe stimulant and depressant "
                "drugs as opposite ends of the same scale.",
        "options": [
            "Only one of the two types has any effect on the nervous system",
            "One raises synaptic activity and the other lowers it, from the same baseline",
            "Both types always produce exactly the same effect on any person who takes them",
            "Stimulants and depressants only differ in how they are taken, never in how they act",
        ],
        "correct_index": 1,
        "why": "Both act on synaptic activity, but in opposite directions from a "
                "normal baseline, which is why they are described as opposite ends of "
                "a scale.",
    },
    {
        "id": "ks4-nervous-system-s23",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a doctor would want to know both the dose and the speed "
                "of a drug's action at synapses before prescribing it alongside "
                "another nervous-system drug.",
        "options": [
            "The speed of a drug's action never has any bearing at all on how safe a combination is",
            "Only the dose matters; the type of action is irrelevant",
            "Two similarly-acting drugs can combine to a far stronger overall effect",
            "Combining any two nervous-system drugs always cancels out both of their effects",
        ],
        "correct_index": 2,
        "why": "Drugs acting the same way at synapses can add together, so "
                "understanding both matters for judging a safe combination.",
    },
    {
        "id": "ks4-nervous-system-s24",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nerve conducts impulses in both directions when it is stimulated "
                "in a laboratory, yet a real reflex arc always sends its signal the "
                "correct way round the body. Explain this using what a synapse does.",
        "options": [
            "Impulses inside a living body are always considerably slower than in a laboratory test",
            "The nerve itself physically changes shape in order to enforce a single direction",
            "A reflex arc contains no synapses at all, unlike a nerve tested in a laboratory",
            "Its synapses only allow transmission one way",
        ],
        "correct_index": 3,
        "why": "A synapse only releases transmitter from the pre-synaptic side, so "
                "it is the synapses along a pathway that enforce a single direction "
                "of travel.",
    },
    {
        "id": "ks4-nervous-system-s25",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person who has taken both a stimulant and a depressant "
                "at the same time can still show a dangerously fast heart rate.",
        "options": [
            "The two drugs do not necessarily cancel out evenly across every pathway they affect, so one effect can dominate",
            "Stimulants and depressants always cancel each other out exactly, whatever the pathway",
            "A depressant permanently switches off the heart's own pathway entirely",
            "Only the first drug taken ever has any effect on the body",
        ],
        "correct_index": 0,
        "why": "The two drugs act on different synapses and different pathways to "
                "different extents, so their overall effects do not simply cancel "
                "out.",
    },
    {
        "id": "ks4-nervous-system-s26",
        "subtopic_slug": "nervous-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why removing caffeine from a person's diet after years of "
                "daily use often causes a headache and tiredness for a few days.",
        "options": [
            "Caffeine permanently increases the total number of receptor proteins made in the brain",
            "The nervous system had adjusted to the raised activity",
            "Withdrawal symptoms of this kind only ever occur with a depressant drug",
            "The body returns to normal the very moment caffeine is stopped completely",
        ],
        "correct_index": 1,
        "why": "Regular stimulant use shifts the baseline the nervous system settles "
                "at, so removing it leaves activity lower than the adjusted normal "
                "until the body readjusts.",
    },
    {
        "id": "ks4-nervous-system-h05",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The PNS and the CNS are two different versions of "
                "the same system, doing the same job in different places.' Evaluate "
                "this claim.",
        "options": [
            "It is right, since both process information equally and entirely independently of each other",
            "It is right, provided both systems are given exactly the same amount of time to act",
            "It is wrong — the CNS decides, while the PNS carries signals",
            "It is wrong, but only because the PNS is physically larger than the CNS overall",
        ],
        "correct_index": 2,
        "why": "The two have different jobs: the CNS processes information and "
                "decides on responses, while the PNS's role is purely to carry "
                "signals.",
    },
    {
        "id": "ks4-nervous-system-h06",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what happens at a synapse when a stimulant is present with "
                "what happens when an SSRI is present.",
        "options": [
            "Both drugs work in exactly the same way, on exactly the same single transmitter",
            "A stimulant blocks reabsorption entirely, while an SSRI increases how much transmitter is released",
            "Neither drug has any measurable effect at the synapse itself, according to current evidence",
            "One raises release generally; the other blocks reabsorption",
        ],
        "correct_index": 3,
        "why": "A stimulant broadly raises transmitter activity, while an SSRI works "
                "through one specific mechanism — blocking the reabsorption of "
                "serotonin.",
    },
    {
        "id": "ks4-nervous-system-h07",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A new drug is found to bind permanently to receptor proteins on the "
                "post-synaptic membrane, without ever releasing them. Predict the "
                "long-term effect on signalling at that synapse, given that a synapse "
                "normally resets by breaking down or reabsorbing its transmitter.",
        "options": [
            "Signalling would eventually stop, because the receptors would be permanently occupied and unable to respond to any further transmitter release",
            "Signalling would be completely unaffected, since receptors play no role in resetting a synapse",
            "Signalling would speed up permanently, since a blocked receptor fires continuously",
            "The pre-synaptic neurone would simply stop making any transmitter at all",
        ],
        "correct_index": 0,
        "why": "If the receptors are always occupied, new transmitter has nothing "
                "left to bind to, so the synapse can no longer pass on a fresh "
                "signal.",
    },
    {
        "id": "ks4-nervous-system-h08",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim: 'Because stimulants and depressants both change "
                "behaviour, either could be used to treat either condition of "
                "over-activity or under-activity in the nervous system.'",
        "options": [
            "True, since both drugs affect exactly the same synapses in exactly the same way",
            "False — each suits the opposite problem from the other",
            "True, provided the dose given is carefully adjusted to compensate for it",
            "False, but only because stimulants happen to be illegal for medical use",
        ],
        "correct_index": 1,
        "why": "The two act in opposite directions on synaptic activity, so using "
                "the wrong one would move the problem the wrong way.",
    },
    {
        "id": "ks4-nervous-system-h09",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher records that a certain neurone type always fires before "
                "another, never after, across thousands of trials of the same reflex. "
                "Determine which two neurone types this is most consistent with, and "
                "why.",
        "options": [
            "Motor before sensory, because effectors always respond before any stimulus is even detected",
            "Relay before sensory, because relay neurones are able to generate their own signals independently",
            "Sensory before relay — a signal must enter the CNS before it can be passed on",
            "The order tells you nothing, since every type fires at once",
        ],
        "correct_index": 2,
        "why": "The pathway order is fixed by structure: a sensory neurone must "
                "deliver its signal into the CNS before a relay neurone there can act "
                "on it.",
    },
    {
        "id": "ks4-nervous-system-h10",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient takes a stimulant every day for a year, then stops. "
                "Predict what a measurement of their baseline synaptic activity would "
                "most likely show in the days just after stopping.",
        "options": [
            "Activity exactly the same as that of someone who has never taken any stimulant",
            "Activity that stays permanently raised for the rest of their entire life",
            "No synaptic activity until the drug restarts",
            "Activity below what is normal for someone who never took it",
        ],
        "correct_index": 3,
        "why": "Long-term stimulant use pushes the nervous system to compensate "
                "downward, so removing the drug can leave activity lower than an "
                "untreated baseline for a while.",
    },
    {
        "id": "ks4-nervous-system-h11",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that a faster neurone must always mean a faster "
                "overall reaction, so myelination is the only factor worth improving. "
                "Evaluate this using what else affects the speed of a whole pathway.",
        "options": [
            "It is too narrow — the number of synapses on the pathway matters just as much, since crossing each one always adds a real delay",
            "It is correct, because synapses add no measurable delay at all to any pathway",
            "It is correct, because every pathway in the body contains exactly the same number of synapses",
            "It is too narrow, but only because muscle strength also affects overall reaction time",
        ],
        "correct_index": 0,
        "why": "Overall pathway speed depends on both conduction along neurones and "
                "the delay at every synapse crossed, so myelination alone does not "
                "decide it.",
    },
    {
        "id": "ks4-nervous-system-h12",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two patients each take a drug that raises synaptic activity, but one "
                "drug also blocks reabsorption of the transmitter while the other "
                "does not. Compare how long you would expect each drug's effect to "
                "last after a single dose.",
        "options": [
            "Both drugs should act for exactly the same length of time, whatever their mechanism",
            "The one blocking reabsorption should act for longer",
            "The one blocking reabsorption should actually act for a shorter time than the other",
            "Neither drug's duration depends on reabsorption in any way whatsoever",
        ],
        "correct_index": 1,
        "why": "Blocking reabsorption slows how quickly transmitter is cleared from "
                "the gap, so its raised effect on the synapse should last longer.",
    },
    {
        "id": "ks4-nervous-system-h13",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a motor neurone that has lost its myelin sheath, but is "
                "otherwise undamaged, would still eventually deliver an impulse to a "
                "muscle, just more slowly.",
        "options": [
            "An unmyelinated axon cannot conduct an impulse under any circumstances whatsoever",
            "The impulse would instead be carried entirely by the muscle fibre itself",
            "Myelin speeds conduction rather than being essential for it",
            "Losing myelin converts the electrical signal into a chemical one along the whole axon",
        ],
        "correct_index": 2,
        "why": "Myelination increases conduction speed but is not required for "
                "conduction to happen at all, so a demyelinated axon still carries an "
                "impulse, only more slowly.",
    },
    {
        "id": "ks4-nervous-system-h14",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient on an SSRI is later prescribed a second drug that also "
                "raises serotonin levels by a different mechanism. Doctors are "
                "cautious about this combination. Suggest why.",
        "options": [
            "The two drugs would simply cancel each other's effect on serotonin out completely",
            "Combining any two drugs that act on the nervous system is always completely safe",
            "Serotonin levels are fixed entirely by genetics and cannot be changed by any drug",
            "The two mechanisms can add together",
        ],
        "correct_index": 3,
        "why": "Two drugs raising the same transmitter by different routes can "
                "combine their effects, producing a level higher than either would "
                "alone.",
    },
    {
        "id": "ks4-nervous-system-h15",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that because the CNS 'does the thinking', the PNS's "
                "role in a reflex or a voluntary action barely matters. Evaluate this "
                "claim using what the PNS actually carries.",
        "options": [
            "It is wrong — without the PNS carrying the original signal in and the final signal out, the CNS would never receive or act on any information at all",
            "It is broadly correct, since the CNS can detect a stimulus with no input from the PNS",
            "It is broadly correct, since effectors respond directly to the CNS with no PNS involved",
            "It is wrong, but only because the PNS is longer in total than the CNS",
        ],
        "correct_index": 0,
        "why": "The CNS depends entirely on the PNS to deliver information in and "
                "carry its decisions out; without it, the CNS has nothing to process "
                "and no way to act.",
    },
    {
        "id": "ks4-nervous-system-h16",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why doctors distinguish between a drug's effect on how MUCH "
                "transmitter is released and its effect on how LONG that transmitter "
                "remains active.",
        "options": [
            "They do not really need to, since the two always change together in the same drug",
            "The two are separate mechanisms a drug can affect independently",
            "Only the amount released matters for the effect's strength",
            "Only the duration ever matters, since the amount released is fixed by the body",
        ],
        "correct_index": 1,
        "why": "Amount released and duration of activity are controlled by different "
                "steps of the process, so a drug affecting one need not affect the "
                "other.",
    },
    {
        "id": "ks4-nervous-system-h17",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a reflex response if the sensory "
                "neurone in its arc conducted normally, but every synapse along the "
                "whole pathway conducted transmitter at only half the usual rate.",
        "options": [
            "The response would be unaffected, since synapses add no delay to a pathway at all",
            "The response would actually happen faster, since less transmitter is used overall",
            "The whole response would be slower, since delay is added at every synapse crossed",
            "The reflex would stop completely, since any change at all to a synapse blocks it",
        ],
        "correct_index": 2,
        "why": "Since the delay is added once for every synapse crossed, halving the "
                "rate at each one slows the whole pathway rather than stopping it.",
    },
    {
        "id": "ks4-nervous-system-h18",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Depressant drugs are always dangerous and stimulant "
                "drugs are always safe.' Evaluate this using what each does at a "
                "synapse.",
        "options": [
            "It is correct, because only a depressant can ever slow a vital function such as breathing",
            "It is correct, because a stimulant has no effect at all on the heart or on breathing",
            "It is wrong, but only because depressants happen to be illegal while stimulants are not",
            "Either type can be dangerous or useful depending on the dose",
        ],
        "correct_index": 3,
        "why": "Both types change synaptic activity from normal, and either can be "
                "harmful or medically useful depending on the dose and the situation.",
    },
    {
        "id": "ks4-nervous-system-h19",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which structural feature best explains why a motor neurone "
                "supplying a muscle in the foot can still respond quickly, despite "
                "its axon being well over a metre long.",
        "options": [
            "It is heavily myelinated, which increases the speed at which the impulse travels along that great length",
            "It contains far more mitochondria than a much shorter motor neurone does",
            "It has no cell body at all, which removes one possible source of delay",
            "It carries the impulse in both directions at once, in order to save time",
        ],
        "correct_index": 0,
        "why": "Heavy myelination compensates for the neurone's great length, "
                "keeping conduction fast enough for a timely response.",
    },
    {
        "id": "ks4-nervous-system-h20",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the CNS's role in a voluntary decision with its role in a "
                "spinal reflex, given that both pass through the spinal cord.",
        "options": [
            "In both cases the signal always reaches the conscious brain before any response occurs",
            "A voluntary decision also involves the conscious brain; a reflex does not",
            "In both cases the spinal cord is bypassed completely, in favour of the brain alone",
            "A reflex involves more of the CNS than a decision does",
        ],
        "correct_index": 1,
        "why": "A reflex is completed within the spinal cord alone, while a "
                "voluntary response involves the conscious processing of the brain "
                "before a decision is made.",
    },
    {
        "id": "ks4-nervous-system-h21",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug is found to increase both the amount of transmitter released "
                "and how long it stays active in the synapse. Predict how its overall "
                "effect would compare with a drug that only does one of those two "
                "things.",
        "options": [
            "Its overall effect should be identical, since only one mechanism can ever matter at a time",
            "Its overall effect should actually be smaller, since the two mechanisms cancel each other out",
            "Its effect should be larger, since both routes raise activity together",
            "Its effect depends only on which mechanism happens first",
        ],
        "correct_index": 2,
        "why": "Two separate mechanisms both raising activity should combine, "
                "producing a stronger effect than either alone.",
    },
    {
        "id": "ks4-nervous-system-h22",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a scientist studying reaction time would want to know "
                "whether a participant has recently taken caffeine, even in a study "
                "that has nothing to do with drugs.",
        "options": [
            "Caffeine has no measurable effect at all on any part of the nervous system",
            "Caffeine only ever affects blood glucose, which has no real link to reaction time",
            "Caffeine use being illegal would end the study regardless of any effect it has",
            "It could change reaction time as an unwanted variable",
        ],
        "correct_index": 3,
        "why": "Since caffeine changes synaptic activity, it could affect reaction "
                "time and needs to be controlled for as a variable.",
    },
    {
        "id": "ks4-nervous-system-h23",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of the following would most strongly support the "
                "claim that a new chemical acts as a depressant rather than a "
                "stimulant.",
        "options": [
            "Reduced neurotransmitter activity and slower reaction times in people who have taken it, measured directly",
            "Measurements showing the chemical has no effect on any synapse studied",
            "Measurements showing a faster heart rate and raised alertness in people who took it",
            "Measurements showing the chemical only affects the structure of bone",
        ],
        "correct_index": 0,
        "why": "A depressant is defined by reducing synaptic activity, so reduced "
                "activity and slower responses are the evidence that would support "
                "that claim.",
    },
    {
        "id": "ks4-nervous-system-h24",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student proposes that addiction is simply 'liking a drug too "
                "much'. Using what tolerance means at a synapse, suggest a more "
                "accurate description.",
        "options": [
            "Addiction is purely a choice, with no physical basis in the nervous system at all",
            "The nervous system adapts, needing more for the same effect",
            "Addiction only ever happens with a drug that has no effect on any synapse",
            "Tolerance means a synapse becomes permanently unable to respond to anything at all",
        ],
        "correct_index": 1,
        "why": "Tolerance is the nervous system adapting to a drug's presence, which "
                "is why more is needed over time and why stopping causes withdrawal "
                "effects.",
    },
    {
        "id": "ks4-nervous-system-h25",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the risk of a sudden, large dose of a stimulant with the "
                "risk of a sudden, large dose of a depressant, in terms of the vital "
                "functions each could disrupt.",
        "options": [
            "Both always disrupt exactly the same vital function, and in exactly the same way",
            "Neither type of drug is able to affect any vital, automatic body function at all",
            "A stimulant risks a fast heart rate; a depressant risks breathing slowing",
            "Only a depressant can affect the heart or breathing rate",
        ],
        "correct_index": 2,
        "why": "Because both raise or lower activity at synapses throughout the "
                "body, a large dose of either can disrupt the automatic functions "
                "those synapses control, though in opposite directions.",
    },
    {
        "id": "ks4-nervous-system-h26",
        "subtopic_slug": "nervous-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a drug acting only on the PNS could never "
                "affect a person's mood, memory or decision-making.",
        "options": [
            "It is unsound, since the PNS alone is what carries out all conscious thought",
            "It is unsound, because the CNS has no role at all in mood or in memory",
            "It is sound, but only because the PNS happens to sit physically closer to the brain",
            "It is broadly sound, since those depend on CNS processing",
        ],
        "correct_index": 3,
        "why": "Mood, memory and decision-making are CNS functions, so a drug "
                "confined to the PNS would not be expected to reach them.",
    },
]
