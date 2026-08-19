# -*- coding: utf-8 -*-
"""B8 lesson 03 — Anaerobic respiration in humans: twelve questions (MRB-269).

The lesson turns on one shape: demand rises above what oxygen delivery can
ever cover, the gap is paid for anaerobically, and the bill arrives after the
running has stopped. Every question here probes one of the three places a
student loses that shape — what the anaerobic route actually costs and leaves
behind, whether it replaces aerobic respiration or runs on top of it, and when
lactic acid is present and when it is long gone.

The distractors are built from the lesson's two declared misconceptions.
RESP-05 ("lactic acid is why your legs ache two days after a hard session")
supplies the delayed-soreness options — the burning attributed to fibre damage,
the coach's stiffness explanation, the lactic acid that supposedly takes days
to clear or migrates to the joints. RESP-06 ("when you sprint, you switch from
aerobic to anaerobic respiration") supplies every option in which aerobic
respiration shuts down, pauses, slows to save oxygen, or restarts at the finish
line. Four further errors the lesson exists to correct are worked as well: that
a muscle holds a store of oxygen to draw on, that anaerobic respiration is a
faster route to the same energy yield, that lactic acid is exhaled or sweated
out rather than carried to the liver, and that human muscle makes carbon
dioxide — or alcohol — the way yeast does.

No question restates a ladder rung. The rungs already own the word summary
itself and the "why do you keep breathing hard after a sprint" question, so
the bank works around both: the summary appears only through what is absent
from its right-hand side, and the oxygen debt is approached through what it is
a definition of, where the lactic acid goes, and why the episode is a loan
rather than a loss. Rung 4's trained-versus-untrained comparison is left alone
too — the fitness idea appears here only as a lactate-threshold measurement
moving across six months of training.

`figure` is `None` throughout — the lesson declares no figures at all, and
every stem here is self-contained.
"""

UNIT = "B8"
LESSON = "anaerobic-respiration-in-humans"
LESSON_NUMBER = 3

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-03-e01",
        "band": "easier",
        "text": "A glucose molecule is broken down anaerobically instead of "
                "aerobically. How much energy is transferred from it?",
        "options": [
            {"text": "Far less, because the glucose is only partly broken "
                     "down", "correct": True},
            {"text": "More, because anaerobic respiration is much faster to "
                     "get going",
             "correct": False,
             "why": "Anaerobic respiration is quicker off the mark, but speed "
                    "is not the same as yield. Each glucose molecule gives "
                    "far less energy this way — that is the price of not "
                    "waiting for oxygen."},
            {"text": "Exactly the same, because it is the same glucose "
                     "molecule either way",
             "correct": False,
             "why": "The molecule is the same, but it is not taken apart the "
                    "same distance. Stopping at lactic acid leaves most of "
                    "the energy still locked inside it."},
            {"text": "None at all, because releasing energy always needs "
                     "oxygen",
             "correct": False,
             "why": "Energy is released — that is the whole point, and it is "
                    "what keeps a sprinter moving for ten seconds. It is just "
                    "far less than the aerobic route would get."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e02",
        "band": "easier",
        "text": "Halfway through a hard 400 m your legs start to burn. What "
                "is causing that burning?",
        "options": [
            {"text": "The shortage of oxygen itself, felt directly in the "
                     "muscle",
             "correct": False,
             "why": "You cannot feel oxygen running low. What you feel is the "
                    "lactic acid the shortfall makes — no acid, no burning."},
            {"text": "Microscopic damage to the muscle fibres, being repaired",
             "correct": False,
             "why": "That damage is real, but it is what makes you ache a day "
                    "or two later. During the effort itself the burning is "
                    "lactic acid."},
            {"text": "Lactic acid building up in the working muscles",
             "correct": True},
            {"text": "Heat from the muscles contracting so hard for so long",
             "correct": False,
             "why": "Working muscles do get hot, and you feel that as warmth "
                    "all over. The burning is chemical, and it sits only in "
                    "the muscles doing the work."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e03",
        "band": "easier",
        "text": "What is the oxygen debt?",
        "options": [
            {"text": "The oxygen a muscle stored before the race and has now "
                     "used up",
             "correct": False,
             "why": "There is no store of oxygen in a muscle to draw on. That "
                    "is exactly why the shortfall has to be covered "
                    "anaerobically in the first place."},
            {"text": "The oxygen missing from the air when you exercise in a "
                     "crowded room",
             "correct": False,
             "why": "The air holds the same oxygen as always. The shortage is "
                    "in delivery — your heart and lungs cannot move it to the "
                    "muscles fast enough."},
            {"text": "The extra oxygen your heart and lungs deliver while you "
                     "are running",
             "correct": False,
             "why": "That delivery is aerobic respiration's supply, and it is "
                    "happening during the run. The debt is what is still owed "
                    "once the running has stopped."},
            {"text": "The oxygen still owed after you stop, to deal with the "
                     "lactic acid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e04",
        "band": "easier",
        "text": "A sprint has left lactic acid in a runner's leg muscles. "
                "What happens to it next?",
        "options": [
            {"text": "It is breathed out through the lungs as a waste gas",
             "correct": False,
             "why": "Lactic acid is not a gas and does not leave in your "
                    "breath. The hard breathing supplies the oxygen needed to "
                    "deal with it; it does not exhale it."},
            {"text": "The blood carries it to the liver, which deals with it "
                     "there", "correct": True},
            {"text": "It stays in the muscle that made it and slowly fades "
                     "away",
             "correct": False,
             "why": "It does not just fade. It leaves the muscle in the "
                    "blood, and the liver either oxidises it or converts it "
                    "back into glucose."},
            {"text": "It is sweated out through the skin during the cool-down",
             "correct": False,
             "why": "Sweat cools you and carries no lactic acid away. The "
                    "blood does the carrying and the liver does the work."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-03-s01",
        "band": "standard",
        "text": "On the bench, oxygen delivery rises towards a ceiling of 80 "
                "units. You pick Jogging, which asks for 50 units, and press "
                "Run for 10 s. What does the lactic acid bar do?",
        "options": [
            {"text": "It climbs, because any exercise harder than sitting "
                     "makes some",
             "correct": False,
             "why": "Lactic acid is only made when demand goes above what "
                    "oxygen can cover. Jogging asks 50 units against a "
                    "ceiling of 80, so no gap ever opens."},
            {"text": "It climbs slowly, because jogging is a gentler version "
                     "of sprinting",
             "correct": False,
             "why": "It is not a gentler version of the same thing. Below the "
                    "ceiling the demand is met entirely aerobically, so the "
                    "rate is zero, not small."},
            {"text": "It stays at zero — demand is inside what the oxygen "
                     "supply covers", "correct": True},
            {"text": "It stays at zero, because lactic acid is only made once "
                     "you stop",
             "correct": False,
             "why": "That is the wrong way round. Lactic acid is made during "
                    "the effort, while the gap is open, and it is cleared "
                    "after you stop."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s02",
        "band": "standard",
        "text": "During a flat-out sprint, what is aerobic respiration doing?",
        "options": [
            {"text": "It shuts down, and anaerobic respiration takes over "
                     "from it",
             "correct": False,
             "why": "Nothing switches off. Aerobic respiration carries on at "
                    "the highest rate the oxygen supply allows, and anaerobic "
                    "respiration makes up the shortfall on top of it."},
            {"text": "It carries on flat out, with anaerobic respiration "
                     "covering the shortfall", "correct": True},
            {"text": "It slows down, saving oxygen to be used after the race "
                     "instead",
             "correct": False,
             "why": "Oxygen cannot be saved up for later. It is being used as "
                    "fast as it arrives, all the way through the sprint."},
            {"text": "It pauses, then restarts the moment you cross the "
                     "finish line",
             "correct": False,
             "why": "It never paused. If it had, the oxygen delivery bar "
                    "would drop when the demand bar rises — on the bench it "
                    "climbs instead."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s03",
        "band": "standard",
        "text": "One runner picks a pace just below the point where the gap "
                "between demand and supply opens. Another picks a pace just "
                "above it. What is the difference?",
        "options": [
            {"text": "The first can hold that pace; the second accumulates "
                     "lactic acid and slows", "correct": True},
            {"text": "The second gets more energy per glucose molecule, so "
                     "finishes fresher",
             "correct": False,
             "why": "Going faster does not improve the deal. The extra energy "
                    "above the ceiling comes anaerobically, which gets far "
                    "less from each glucose molecule, not more."},
            {"text": "The first uses no oxygen at all, so has nothing to "
                     "repay afterwards",
             "correct": False,
             "why": "The first runner is entirely aerobic — using oxygen is "
                    "exactly what they are doing. It is the second who has "
                    "gone beyond what oxygen can cover."},
            {"text": "Both build up lactic acid; the second one simply feels "
                     "it sooner",
             "correct": False,
             "why": "Below the ceiling nothing accumulates at all. That is "
                    "what makes the first pace holdable for an hour rather "
                    "than a minute."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s04",
        "band": "standard",
        "text": "A coach tells the class that the stiffness they feel two "
                "days after a new session is lactic acid still sitting in "
                "their muscles. What is wrong with that?",
        "options": [
            {"text": "Nothing — lactic acid does take several days to clear "
                     "from a muscle",
             "correct": False,
             "why": "Blood lactate is back to its resting level within about "
                    "an hour of stopping, usually much sooner. Two days "
                    "later there is none left to blame."},
            {"text": "The lactic acid has moved into the joints rather than "
                     "the muscles",
             "correct": False,
             "why": "It does not travel to the joints. It leaves the muscle "
                    "in the blood and the liver deals with it, long before "
                    "the stiffness arrives."},
            {"text": "Lactic acid never causes any pain at all, during or "
                     "afterwards",
             "correct": False,
             "why": "It does cause pain — the burning during the effort is "
                    "lactic acid, and it is what forces you to slow down. Its "
                    "job simply ends when you stop."},
            {"text": "The lactic acid cleared within about an hour; that ache "
                     "is fibre damage", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-03-h01",
        "band": "harder",
        "text": "A weightlifter holds a heavy bar still for 30 seconds. The "
                "muscle is squeezed so hard that almost no blood can flow "
                "through it, though she breathes normally throughout. What "
                "happens inside that muscle?",
        "options": [
            {"text": "Nothing builds up, because the bar is not moving and no "
                     "work is done",
             "correct": False,
             "why": "A held contraction is expensive. The muscle is "
                    "transferring energy the whole time even though nothing "
                    "moves, so the demand is high, not zero."},
            {"text": "Aerobic respiration continues normally, because she is "
                     "breathing steadily",
             "correct": False,
             "why": "Breathing is only the first step. The oxygen still has "
                    "to reach the muscle in the blood, and here it cannot — "
                    "so delivery fails however well she breathes."},
            {"text": "The muscle stops respiring until blood flow returns "
                     "after the lift",
             "correct": False,
             "why": "Respiration does not stop — it could not hold the bar up "
                    "if it did. It just has to run without oxygen for those "
                    "thirty seconds."},
            {"text": "Lactic acid builds up, because oxygen cannot be "
                     "delivered to the muscle", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h02",
        "band": "harder",
        "text": "The lesson calls the lactic acid from a sprint borrowed "
                "rather than wasted. Which fact best justifies calling it a "
                "loan?",
        "options": [
            {"text": "The liver oxidises it, or converts it back into glucose "
                     "for the muscles", "correct": True},
            {"text": "It leaves the body in your breath, so nothing is left "
                     "behind at all",
             "correct": False,
             "why": "Nothing is exhaled here. What makes it a loan is that "
                    "the lactic acid itself is recovered — into energy or "
                    "back into glucose — not that it is disposed of."},
            {"text": "It gives the same energy per glucose molecule as the "
                     "aerobic route",
             "correct": False,
             "why": "It does not. Anaerobic respiration gets far less from "
                    "each glucose molecule. The loan is the lactic acid being "
                    "used later, not the yield being equal."},
            {"text": "The oxygen owed afterwards is less than the oxygen "
                     "skipped during it",
             "correct": False,
             "why": "The lesson never claims the debt comes out smaller. What "
                    "makes it a loan is that nothing is thrown away — the "
                    "lactic acid is put back to work."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h03",
        "band": "harder",
        "text": "A runner is treadmill-tested twice, six months apart. The "
                "pace at which her blood lactate starts to climb has moved "
                "from 12 km/h to 14 km/h. What has changed?",
        "options": [
            {"text": "Her muscles now make lactic acid more slowly at every "
                     "speed, including rest",
             "correct": False,
             "why": "At rest and at easy paces none was accumulating before "
                    "either, because no gap was open. What has moved is the "
                    "speed at which a gap first appears."},
            {"text": "Her lungs are larger, so she can store more oxygen "
                     "before she starts",
             "correct": False,
             "why": "There is no store of oxygen to fill. The test measures "
                    "the pace at which delivery stops keeping up with demand, "
                    "and that pace has risen."},
            {"text": "Oxygen delivery covers a faster pace, so no gap opens "
                     "until 14 km/h", "correct": True},
            {"text": "She no longer produces any lactic acid at all, however "
                     "fast she runs",
             "correct": False,
             "why": "Above 14 km/h she still will. The threshold has moved "
                    "up the speed scale; it has not disappeared."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h04",
        "band": "harder",
        "text": "A student says you can prove a sprinter respired "
                "anaerobically because they breathe out far more carbon "
                "dioxide at the end of the race. Why does that not prove it?",
        "options": [
            {"text": "Anaerobic respiration does make carbon dioxide, but far "
                     "too little to detect",
             "correct": False,
             "why": "It makes none at all. In human muscle the glucose is "
                    "only partly broken down, and lactic acid is the single "
                    "product."},
            {"text": "Anaerobic respiration in humans makes no carbon "
                     "dioxide — that is aerobic", "correct": True},
            {"text": "Anaerobic respiration makes carbon dioxide and alcohol, "
                     "so the reading lies",
             "correct": False,
             "why": "Carbon dioxide and alcohol are what yeast produces, and "
                    "that is fermentation. Human muscle produces lactic acid "
                    "and no gas at all."},
            {"text": "Carbon dioxide is only breathed out at rest, never "
                     "during hard exercise",
             "correct": False,
             "why": "You breathe out more of it during exercise, not less — "
                    "aerobic respiration is running flat out the whole time. "
                    "That is precisely whose carbon dioxide it is."},
        ],
        "figure": None,
    },
]
