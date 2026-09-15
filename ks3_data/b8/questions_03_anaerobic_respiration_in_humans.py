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
            {"text": "It shuts down as soon as the oxygen runs short, and "
                     "anaerobic respiration takes over",
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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-03-e05",
        "band": "easier",
        "text": "Anaerobic respiration in human muscle uses no oxygen. Which "
                "two substances does it therefore never produce?",
        "options": [
            {"text": "Carbon dioxide and water", "correct": True},
            {"text": "Lactic acid and water", "correct": False,
             "why": "Lactic acid is the one thing it does produce. Water "
                    "needs the glucose broken down completely, and without "
                    "oxygen it never is."},
            {"text": "Glucose and lactic acid", "correct": False,
             "why": "Glucose is what goes in and lactic acid is what comes "
                    "out. Neither of them is missing from this reaction."},
            {"text": "Carbon dioxide and lactic acid", "correct": False,
             "why": "Half right. There is no carbon dioxide, but lactic acid "
                    "is exactly what is left behind in the muscle."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e06",
        "band": "easier",
        "text": "What does the word anaerobic tell you about this kind of "
                "respiration?",
        "options": [
            {"text": "That it goes on without releasing any energy at all.",
             "correct": False,
             "why": "Energy is released — it is what keeps a sprinter moving. "
                    "There is simply far less of it from each glucose "
                    "molecule."},
            {"text": "That it happens outside the body rather than inside "
                     "it.",
             "correct": False,
             "why": "It happens inside your muscle cells. The word names a "
                    "condition the reaction runs under, not a place."},
            {"text": "That it happens without any glucose being needed.",
             "correct": False,
             "why": "Glucose is still the fuel and still what is broken down. "
                    "What is missing is the oxygen, not the fuel."},
            {"text": "That it happens without any oxygen being used.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e07",
        "band": "easier",
        "text": "Which of these is most likely to make your leg muscles "
                "respire anaerobically?",
        "options": [
            {"text": "Walking slowly to the bus stop.", "correct": False,
             "why": "Walking asks for far less than your oxygen supply can "
                    "deliver, so no gap opens and nothing anaerobic is "
                    "needed."},
            {"text": "Sitting still through a lesson.", "correct": False,
             "why": "Sitting still is the lowest demand of the day. Aerobic "
                    "respiration covers it several times over."},
            {"text": "Sprinting flat out for the last ten metres.",
             "correct": True},
            {"text": "Sleeping through the night after a hard day.",
             "correct": False,
             "why": "Demand falls to its lowest overnight. The anaerobic "
                    "route is for when demand climbs above what oxygen "
                    "delivery can cover."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e08",
        "band": "easier",
        "text": "Anaerobic respiration gets far less energy out of each "
                "glucose molecule than aerobic respiration does. So what is "
                "its advantage?",
        "options": [
            {"text": "It leaves a product the liver can make use of "
                     "afterwards.",
             "correct": False,
             "why": "The liver does recover the lactic acid, but that is "
                    "repairing the cost rather than the point of taking the "
                    "route. The advantage is speed."},
            {"text": "It supplies energy quickly, without waiting for oxygen "
                     "to arrive.",
             "correct": True},
            {"text": "It uses less glucose, so a muscle's fuel lasts much "
                     "longer.",
             "correct": False,
             "why": "The opposite is true. Getting less from each molecule "
                    "means breaking down more of them for the same amount of "
                    "work."},
            {"text": "It can carry on for hours, long after aerobic "
                     "respiration stops.",
             "correct": False,
             "why": "It is the short-term route. Lactic acid accumulates "
                    "within seconds and forces you to slow down."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e09",
        "band": "easier",
        "text": "During a sprint, where in the body does anaerobic "
                "respiration actually happen?",
        "options": [
            {"text": "In the muscle cells that are doing the work.",
             "correct": True},
            {"text": "In the lungs, where the oxygen has run short.",
             "correct": False,
             "why": "The lungs are where air is exchanged; nothing is "
                    "respired in them. The shortfall is felt in the working "
                    "muscle."},
            {"text": "In the blood, which is carrying the lactic acid.",
             "correct": False,
             "why": "The blood carries the lactic acid away afterwards. The "
                    "reaction itself happened inside the muscle cells."},
            {"text": "In the liver, which is where the lactic acid ends up.",
             "correct": False,
             "why": "The liver is the destination, not the source. It deals "
                    "with lactic acid the muscles have already made."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-e10",
        "band": "easier",
        "text": "Straight after a sprint you are breathing hard; two days "
                "after a new training session your legs ache. Which of those "
                "two is caused by lactic acid?",
        "options": [
            {"text": "Both, since lactic acid is behind all soreness from "
                     "exercise.",
             "correct": False,
             "why": "It clears within about an hour of stopping, so two days "
                    "later there is none of it left to cause anything."},
            {"text": "Neither — lactic acid causes no pain during exercise "
                     "and no breathlessness.",
             "correct": False,
             "why": "It does cause the burning during the effort, and "
                    "repaying the oxygen debt it created is why you keep "
                    "breathing hard."},
            {"text": "The ache two days later, because the acid drains away "
                     "slowly.",
             "correct": False,
             "why": "It does not drain slowly. The blood removes it to the "
                    "liver within the hour, and the later ache is damage to "
                    "the muscle fibres."},
            {"text": "The hard breathing — oxygen is owed for clearing the "
                     "acid.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-03-s05",
        "band": "standard",
        "text": "Oxygen delivery rises towards a ceiling of 80 units. A "
                "runner picks a hard run, which asks for 85 units. What "
                "happens to the lactic acid?",
        "options": [
            {"text": "None is made, because 85 and 80 are so close "
                     "together.",
             "correct": False,
             "why": "A gap is a gap. Five units is slow accumulation rather "
                    "than none, which is why a hard run can be held for "
                    "minutes and a sprint cannot."},
            {"text": "It accumulates as fast as it does in a flat-out "
                     "sprint.",
             "correct": False,
             "why": "A sprint asks 150 units against the same ceiling — a gap "
                    "of 70, not 5. How fast it accumulates depends on the "
                    "size of the gap."},
            {"text": "It accumulates slowly, because demand is just above the "
                     "ceiling.",
             "correct": True},
            {"text": "None is made, because aerobic respiration shuts down "
                     "instead.",
             "correct": False,
             "why": "Aerobic respiration is working flat out at 80 units, "
                    "which is most of the job. Only the extra five units come "
                    "from anywhere else."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s06",
        "band": "standard",
        "text": "A runner in the last 50 m of a 200 m is trying just as hard "
                "as at the start, and is visibly slowing down. What is the "
                "best explanation?",
        "options": [
            {"text": "Lactic acid has built up in the muscles, forcing the "
                     "slow-down.",
             "correct": True},
            {"text": "They have used up all the glucose stored in their leg "
                     "muscles.",
             "correct": False,
             "why": "Glucose stores are not emptied in twenty seconds. What "
                    "has built up is lactic acid, and that is what limits the "
                    "effort."},
            {"text": "Their muscles have used up the store of oxygen they "
                     "took in before the start.",
             "correct": False,
             "why": "There was no store to use up. Oxygen has been arriving "
                    "throughout; it has simply never arrived fast enough."},
            {"text": "Aerobic respiration has stopped, so far less energy is "
                     "available.",
             "correct": False,
             "why": "Aerobic respiration has run flat out from the gun and "
                    "has not stopped. What has changed is how much lactic "
                    "acid sits on top of it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s07",
        "band": "standard",
        "text": "The word summary for anaerobic respiration in humans has "
                "only one substance on the right-hand side. Why is there "
                "nothing else there?",
        "options": [
            {"text": "Because anything else dissolves in the blood and leaves "
                     "at once.",
             "correct": False,
             "why": "Nothing is being hidden — the other substances are not "
                    "made at all. Carbon dioxide and water need oxygen, and "
                    "there is none."},
            {"text": "Because with no oxygen the glucose is only partly "
                     "broken down.",
             "correct": True},
            {"text": "Because the muscle keeps the rest for the liver to "
                     "collect later.",
             "correct": False,
             "why": "The liver collects the lactic acid, and that is all "
                    "there is to collect. The reaction stops before anything "
                    "else can form."},
            {"text": "Because carbon dioxide and water count as waste rather "
                     "than as products.",
             "correct": False,
             "why": "Neither is made here at all. When they are made — "
                    "aerobically — they are products, and they are written as "
                    "products."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s08",
        "band": "standard",
        "text": "A footballer sprints, then jogs, then sprints again, for "
                "ninety minutes. When is the lactic acid from those sprints "
                "being cleared?",
        "options": [
            {"text": "Only at half time and at the final whistle, once the "
                     "running stops.",
             "correct": False,
             "why": "Clearing starts as soon as delivery is ahead of demand, "
                    "and that happens during the jogging rather than only "
                    "when the game does."},
            {"text": "Not at all until the match ends, so it builds up all "
                     "game.",
             "correct": False,
             "why": "If it did, nobody would finish. The jogging spells are "
                    "when the debt is repaid, which is why players keep "
                    "moving rather than standing still."},
            {"text": "During the sprints, when the heart and lungs work "
                     "hardest.",
             "correct": False,
             "why": "The sprints are when it is made. Delivery is at its "
                    "highest then, but demand is higher still, so the gap is "
                    "open rather than closing."},
            {"text": "During the jogging, when demand drops below what "
                     "delivery covers.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s09",
        "band": "standard",
        "text": "After a sprint your heart goes on beating fast as well as "
                "your lungs working hard. How does the fast heartbeat help?",
        "options": [
            {"text": "It warms the working muscles, and the extra warmth "
                     "breaks the lactic acid down.",
             "correct": False,
             "why": "Temperature is not what deals with lactic acid. The "
                    "blood is needed to move it, and to bring oxygen to the "
                    "muscles."},
            {"text": "It pushes the lactic acid out through the skin in "
                     "sweat.",
             "correct": False,
             "why": "Sweat carries no lactic acid away. The blood carries it "
                    "to the liver, and the liver is what deals with it."},
            {"text": "It brings oxygen in and carries the lactic acid to the "
                     "liver.",
             "correct": True},
            {"text": "It refills the muscles' store of oxygen ready for the "
                     "next sprint.",
             "correct": False,
             "why": "There is no store to refill. Whatever the next sprint "
                    "needs will have to arrive while it is happening."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-s10",
        "band": "standard",
        "text": "A student says a sprinter could avoid anaerobic respiration "
                "altogether by simply breathing more deeply during the race. "
                "Why will that not work?",
        "options": [
            {"text": "Because you cannot breathe at all while sprinting flat "
                     "out.",
             "correct": False,
             "why": "You can, and sprinters do. The limit is not whether you "
                    "breathe but how fast oxygen can be delivered to the "
                    "muscles."},
            {"text": "Because delivery has a ceiling — heart, lungs and blood "
                     "can only move so much.",
             "correct": True},
            {"text": "Because deep breathing lets in more carbon dioxide as "
                     "well as more oxygen.",
             "correct": False,
             "why": "Air is almost all nitrogen and oxygen, so breathing "
                    "deeply does not flood you with carbon dioxide. The limit "
                    "is delivery, not what the air holds."},
            {"text": "Because the oxygen taken in during a sprint is stored "
                     "for afterwards.",
             "correct": False,
             "why": "None of it is stored. It is used as fast as it arrives, "
                    "all the way through the race."},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-03-h05",
        "band": "harder",
        "text": "During a sprint a runner's muscles demand 150 units of "
                "energy supply per 10 seconds, and oxygen delivery has "
                "reached 62 units. How many units must be covered "
                "anaerobically?",
        "options": [
            {"text": "212 units", "correct": False,
             "why": "That is 150 + 62, adding the supply to the demand. The "
                    "anaerobic route covers only what the oxygen cannot, so "
                    "the two are subtracted."},
            {"text": "150 units", "correct": False,
             "why": "That would be right only if no oxygen were arriving at "
                    "all. Aerobic respiration is running flat out at 62 "
                    "units, and the shortfall is what is left over."},
            {"text": "80 units", "correct": False,
             "why": "80 is the ceiling delivery could eventually reach, not "
                    "what it has reached at this moment. Use the 62 units "
                    "actually being delivered."},
            {"text": "88 units", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h06",
        "band": "harder",
        "text": "A runner finishes with 88 units of lactic acid, and recovery "
                "clears about 22 units every 30 seconds. Roughly how long "
                "will it take to clear?",
        "options": [
            {"text": "About 2 minutes", "correct": True},
            {"text": "About 30 seconds", "correct": False,
             "why": "Thirty seconds clears 22 units, a quarter of the total. "
                    "Four such periods are needed, and four half-minutes make "
                    "two minutes."},
            {"text": "About 1 minute", "correct": False,
             "why": "A minute clears 44 units, half of it. Divide 88 by 22 to "
                    "get four periods, each of 30 seconds."},
            {"text": "About 4 minutes", "correct": False,
             "why": "The right number of periods, each given the wrong "
                    "length. There are four of them and each lasts 30 "
                    "seconds, not a minute."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h07",
        "band": "harder",
        "text": "A person whose heart cannot pump strongly is breathless "
                "after one flight of stairs, while a healthy person of the "
                "same age is not. Explain that using demand and supply.",
        "options": [
            {"text": "Their muscles make lactic acid at every activity, "
                     "including sitting still.",
             "correct": False,
             "why": "At rest no gap is open in either person, so neither is "
                    "accumulating anything. What differs is how hard each of "
                    "them can work before a gap opens at all."},
            {"text": "The stairs are harder work for them, so their muscles "
                     "demand more energy.",
             "correct": False,
             "why": "The stairs cost about the same in both people. What has "
                    "changed is the supply side — how much oxygen can be "
                    "delivered — not the demand."},
            {"text": "Their delivery ceiling is low, so even stairs open a "
                     "gap covered anaerobically.",
             "correct": True},
            {"text": "Their muscles have no store of oxygen left to spend on "
                     "the stairs.",
             "correct": False,
             "why": "Nobody has one, healthy or not. The difference is how "
                    "fast oxygen can be delivered while the stairs are being "
                    "climbed."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h08",
        "band": "harder",
        "text": "A cyclist attacks up a hill, then keeps pedalling gently at "
                "the top instead of stopping. She recovers faster than a "
                "rider who stops dead. Why?",
        "options": [
            {"text": "Her leg muscles use the lactic acid up directly, as a "
                     "second fuel.",
             "correct": False,
             "why": "The muscles do not consume it themselves — the blood "
                    "takes it to the liver. What gentle pedalling does is "
                    "keep that blood moving quickly."},
            {"text": "Pedalling gently keeps demand below oxygen delivery "
                     "and the blood moving.",
             "correct": True},
            {"text": "Stopping dead makes the muscles go on producing more "
                     "lactic acid than pedalling does.",
             "correct": False,
             "why": "Both riders stop producing it the moment the effort "
                    "ends. The difference is how quickly what is already "
                    "there is carried away."},
            {"text": "Pedalling gently means she never went into oxygen debt "
                     "in the first place.",
             "correct": False,
             "why": "The attack up the hill put her into debt exactly as it "
                    "did the other rider. What differs is how quickly the "
                    "debt is repaid."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h09",
        "band": "harder",
        "text": "Blood taken from a sprinter's arm one minute after a 400 m "
                "contains lactic acid, even though the arm did none of the "
                "hard work. How did it get there?",
        "options": [
            {"text": "The arm muscles respired anaerobically too, from the "
                     "effort of swinging.",
             "correct": False,
             "why": "The arm swing asks nothing like the demand the legs "
                    "made. This lactic acid was produced in the legs and has "
                    "travelled."},
            {"text": "Lactic acid forms in the blood itself whenever oxygen "
                     "runs short anywhere.",
             "correct": False,
             "why": "It forms inside cells that are respiring, not in the "
                    "blood. The blood is what carries it away from them."},
            {"text": "The blood carried it out of the leg muscles, on its way "
                     "to the liver.",
             "correct": True},
            {"text": "The liver made it and sent it out to the muscles that "
                     "needed it.",
             "correct": False,
             "why": "The liver receives lactic acid and deals with it. What "
                    "it sends back out to the muscles is glucose."},
        ],
        "figure": None,
    },
    {
        "id": "b8-03-h10",
        "band": "harder",
        "text": "A sprinter's muscles work at a demand of 150 units against "
                "an oxygen ceiling of 80, and can hold it for about ten "
                "seconds. Why only ten?",
        "options": [
            {"text": "Because the muscles run out of glucose after about ten "
                     "seconds of it.",
             "correct": False,
             "why": "There is far more glucose available than that. What runs "
                    "out is tolerance of the lactic acid, which accumulates "
                    "while the gap is open."},
            {"text": "Because lactic acid accumulates fast while the gap is "
                     "open, and forces a slow-down.",
             "correct": True},
            {"text": "Because oxygen delivery hits its ceiling after ten "
                     "seconds and then falls away.",
             "correct": False,
             "why": "Delivery climbs towards the ceiling and stays there. It "
                    "is the accumulating lactic acid that ends the effort, "
                    "not a fall in supply."},
            {"text": "Because ten seconds is as long as anyone can hold their "
                     "breath while sprinting.",
             "correct": False,
             "why": "Sprinters breathe throughout the race. The limit is "
                    "chemical, and it is not a matter of holding your "
                    "breath."},
        ],
        "figure": None,
    },
]

_MRB338_NEW_QUESTIONS = [
    {
        "id": 'b8-03-e11',
        "band": 'easier',
        "text": 'What does the word ‘anaerobic’ mean, in the context of respiration?',
        "options": [
            {"text": 'Happening without any oxygen being used.', "correct": True},
            {"text": 'Happening at a very fast heart rate.', "correct": False,
             "why": 'Anaerobic describes the absence of oxygen, not how fast the heart is beating.'},
            {"text": 'Happening only in the leg muscles.', "correct": False,
             "why": 'Anaerobic respiration can happen in any muscle working hard enough; it is not limited to the legs.'},
            {"text": 'Happening only outside the human body.', "correct": False,
             "why": 'Anaerobic respiration happens inside human muscle cells, not outside the body.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e12',
        "band": 'easier',
        "text": 'Why does anaerobic respiration release far less energy from each glucose molecule than aerobic respiration?',
        "options": [
            {"text": 'Because it happens much more slowly than aerobic respiration.', "correct": False,
             "why": 'Anaerobic respiration is actually the faster of the two routes, not the slower one.'},
            {"text": 'Because muscle cells contain fewer mitochondria than other cells.', "correct": False,
             "why": 'Anaerobic respiration does not use the mitochondria at all, so their number is not the reason.'},
            {"text": 'The glucose is only partly broken down, leaving energy still trapped in the lactic acid.', "correct": True},
            {"text": 'Because some of the glucose escapes from the cell unused.', "correct": False,
             "why": 'The glucose that is respired anaerobically is fully taken into the reaction; none of it escapes unused.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e13',
        "band": 'easier',
        "text": 'The term ‘oxygen debt’ describes what, exactly?',
        "options": [
            {"text": 'The oxygen a muscle stored before exercise and has now used up completely during the effort.', "correct": False,
             "why": 'Muscles hold no meaningful store of oxygen to use up in the first place.'},
            {"text": 'The oxygen missing from the air when you exercise in a stuffy room.', "correct": False,
             "why": "The oxygen debt is about the runner's own body, not about the air in the room."},
            {"text": 'The amount of oxygen a sprinter breathes in during the race itself.', "correct": False,
             "why": 'The debt is repaid afterwards, once the race is over, not breathed in during it.'},
            {"text": 'The extra oxygen needed after exercise to deal with the lactic acid that built up.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e14',
        "band": 'easier',
        "text": 'What happens to lactic acid after a sprint?',
        "options": [
            {"text": 'The blood carries it to the liver, which deals with it using oxygen.', "correct": True},
            {"text": 'It is breathed out through the lungs as a waste gas.', "correct": False,
             "why": 'Lactic acid is not a gas and cannot be breathed out; it leaves the muscle in the blood.'},
            {"text": 'It stays in the muscle that made it and slowly fades away there over several hours.', "correct": False,
             "why": 'Lactic acid is carried away from the muscle in the blood rather than staying and fading in place.'},
            {"text": 'It is sweated out through the skin during the cool-down.', "correct": False,
             "why": 'Sweat does not carry away meaningful amounts of lactic acid; the blood carries it to the liver.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e15',
        "band": 'easier',
        "text": 'Muscle soreness that appears two days after hard exercise is caused mainly by what?',
        "options": [
            {"text": 'Lactic acid that has built up in the muscle and stayed there.', "correct": False,
             "why": 'Blood lactate returns to its resting level within about an hour of stopping, long before the soreness appears two days later.'},
            {"text": 'Microscopic damage to the muscle fibres, and the repair that follows.', "correct": True},
            {"text": 'Oxygen debt that has still not been fully repaid.', "correct": False,
             "why": 'Oxygen debt is repaid within minutes of stopping, not still outstanding two days later.'},
            {"text": 'Carbon dioxide trapped in the muscle from anaerobic respiration.', "correct": False,
             "why": 'Human anaerobic respiration produces no carbon dioxide at all; that is one way it differs from the aerobic route.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e16',
        "band": 'easier',
        "text": 'During a sprint, does aerobic respiration stop happening?',
        "options": [
            {"text": 'Yes — the body switches over to the anaerobic route.', "correct": False,
             "why": 'Aerobic respiration never switches off; anaerobic respiration runs alongside it, making up the shortfall.'},
            {"text": 'Yes — aerobic respiration pauses until the sprint is over.', "correct": False,
             "why": 'Aerobic respiration keeps running throughout a sprint at the fastest rate the oxygen supply allows.'},
            {"text": 'No — it carries on at its highest possible rate throughout.', "correct": True},
            {"text": 'Only for the first few seconds, then it restarts.', "correct": False,
             "why": 'Aerobic respiration is running from the very first second, not restarting partway through.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e17',
        "band": 'easier',
        "text": 'What has to happen before a muscle starts respiring anaerobically as well as aerobically?',
        "options": [
            {"text": 'The energy demand has to rise above what the oxygen supply can deliver.', "correct": True},
            {"text": 'The muscle has to run out of glucose completely before it can start respiring anaerobically.', "correct": False,
             "why": 'Anaerobic respiration still uses glucose; running out of it would stop both routes, not start the anaerobic one.'},
            {"text": 'The heart has to stop beating for a moment before anaerobic respiration can begin at all.', "correct": False,
             "why": 'The heart keeps beating throughout; nothing about it stopping is what triggers anaerobic respiration.'},
            {"text": "The body's temperature has to rise above normal.", "correct": False,
             "why": 'Temperature is not what decides whether anaerobic respiration starts; the oxygen supply against demand is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e18',
        "band": 'easier',
        "text": 'Why does a marathon runner deliberately hold a pace just below their fastest possible speed?',
        "options": [
            {"text": 'To save their leg muscles from getting too hot over the whole two hours, which would otherwise force them to stop.', "correct": False,
             "why": 'Overheating is not the reason for this pacing; avoiding a build-up of lactic acid is.'},
            {"text": 'To keep energy demand below what their oxygen supply can cover, avoiding a build-up of lactic acid.', "correct": True},
            {"text": 'Because running any faster would use up all their glucose in the first mile.', "correct": False,
             "why": 'Glucose supply is not the limiting factor here; the oxygen delivery ceiling is.'},
            {"text": 'To make sure their heart rate never rises above its resting rate.', "correct": False,
             "why": "A marathon runner's heart rate is well above its resting rate throughout the race; that is not the reason for pacing."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e19',
        "band": 'easier',
        "text": 'Six months of training later, the same runner can hold a faster pace before lactic acid starts to build up. What has most likely improved?',
        "options": [
            {"text": 'Their muscles now need far less glucose than before to run at exactly the same pace, which is what training mainly achieves.', "correct": False,
             "why": 'The improvement described is about delivering more oxygen at a faster pace, not about needing less fuel.'},
            {"text": 'Their body has grown a store of extra oxygen to draw on.', "correct": False,
             "why": 'The body holds no meaningful store of oxygen at any fitness level; delivery, not storage, has improved.'},
            {"text": 'Their heart and lungs now deliver oxygen faster, raising the pace at which the gap opens.', "correct": True},
            {"text": 'Their muscles have stopped producing lactic acid altogether.', "correct": False,
             "why": 'Trained muscles still produce lactic acid once demand exceeds supply; training raises the pace at which that happens, not removes it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e20',
        "band": 'easier',
        "text": "A runner's muscles demand 150 units of energy delivery, but oxygen delivery can only supply 90 units. How many units are being supplied anaerobically?",
        "options": [
            {"text": '150 units', "correct": False,
             "why": 'That is the total demand, not the gap being covered anaerobically.'},
            {"text": '90 units', "correct": False,
             "why": 'That is the amount being delivered aerobically, not the anaerobic shortfall.'},
            {"text": '240 units', "correct": False,
             "why": 'That comes from adding the two figures together instead of subtracting one from the other.'},
            {"text": '60 units', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e21',
        "band": 'easier',
        "text": "A sprinter's lactic acid clears at a steady 20 units every 30 seconds. How long does it take to clear 100 units completely?",
        "options": [
            {"text": '150 seconds', "correct": True},
            {"text": '100 seconds', "correct": False,
             "why": 'That divides the total by 1 unit per second rather than using the stated clearance rate.'},
            {"text": '20 seconds', "correct": False,
             "why": 'That reads the clearance rate itself as if it were the time taken.'},
            {"text": '600 seconds', "correct": False,
             "why": 'That multiplies instead of dividing the total by the clearance rate.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e22',
        "band": 'easier',
        "text": 'A weightlifter holds a heavy bar completely still for 30 seconds, straining hard. Does lactic acid build up in the working muscles?',
        "options": [
            {"text": 'No — nothing at all builds up in the muscles, because the bar itself never physically moves.', "correct": False,
             "why": 'The muscles are contracting hard to hold the bar still, even though the bar has no visible movement.'},
            {"text": 'Yes — the muscles are working hard even though nothing is visibly moving.', "correct": True},
            {"text": 'No — lactic acid only ever builds up during running, never during any kind of lifting.', "correct": False,
             "why": 'Lactic acid builds up in any hard-working muscle, in any activity, not only during running.'},
            {"text": 'Only if the lifter is also moving around the room.', "correct": False,
             "why": 'The muscles are working hard by staying contracted, whether or not the lifter is also moving around.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e23',
        "band": 'easier',
        "text": 'A person whose heart cannot pump strongly becomes breathless walking up a flight of stairs, though a healthy person would not. Why?',
        "options": [
            {"text": 'Their muscles have no store of oxygen left to spend on stairs.', "correct": False,
             "why": "No one's muscles hold a meaningful oxygen store; the issue here is a low delivery ceiling from a weak heart."},
            {"text": 'Stairs demand more energy from a weak heart.', "correct": False,
             "why": 'The stairs demand the same energy from anyone climbing them; what differs is how much oxygen each heart can deliver.'},
            {"text": 'Their oxygen delivery ceiling is low, so even stairs push demand above it.', "correct": True},
            {"text": 'Their lungs are too small to take in enough air on stairs.', "correct": False,
             "why": 'The situation describes a weak heart, not small lungs, as the limiting factor.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e24',
        "band": 'easier',
        "text": 'Which of these correctly gives the products of anaerobic respiration in human muscle?',
        "options": [
            {"text": 'Only lactic acid, nothing else.', "correct": True},
            {"text": 'Carbon dioxide and lactic acid.', "correct": False,
             "why": 'Human anaerobic respiration makes no carbon dioxide at all; that is one way it differs from the aerobic route.'},
            {"text": 'Carbon dioxide and water.', "correct": False,
             "why": 'Those are the aerobic products; anaerobic respiration in human muscle makes only lactic acid.'},
            {"text": 'Lactic acid and water.', "correct": False,
             "why": 'Anaerobic respiration in human muscle makes no water; water is a product of the aerobic route.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e25',
        "band": 'easier',
        "text": "A blood sample taken from a sprinter's arm straight after a race shows raised lactate. What does this show?",
        "options": [
            {"text": 'That the sprinter has been breathing too fast.', "correct": False,
             "why": 'Breathing rate is not what a lactate reading measures; it measures a chemical made by anaerobic respiration.'},
            {"text": 'That the muscles have been respiring anaerobically.', "correct": True},
            {"text": "That the sprinter's oxygen supply is now higher than normal.", "correct": False,
             "why": 'A raised lactate reading shows the opposite — that demand outran the oxygen supply during the race.'},
            {"text": 'That the sprinter has eaten too much sugar recently.', "correct": False,
             "why": 'Raised lactate comes from muscles respiring anaerobically during exercise, not from what was eaten.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e26',
        "band": 'easier',
        "text": 'A coach tells a sprinter to take deeper breaths during the race so that no lactic acid can form. Will that work?',
        "options": [
            {"text": 'Yes — breathing more deeply always supplies as much oxygen as any muscle could possibly need, however hard it is working.', "correct": False,
             "why": 'Delivery to the muscles depends on the whole cardiovascular system working together, not on breathing depth alone.'},
            {"text": 'No — a sprinter cannot breathe at all while running flat out.', "correct": False,
             "why": 'A sprinter does keep breathing during a race; the limit is delivery capacity, not an inability to breathe.'},
            {"text": 'No — the limit is how fast the heart and lungs together can deliver oxygen to the muscles, not how deeply they breathe.', "correct": True},
            {"text": 'Yes — but only sprinters with unusually large lungs can manage it.', "correct": False,
             "why": 'Lung size is not described as the limiting factor here; overall delivery capacity is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e27',
        "band": 'easier',
        "text": 'Two joggers run at the same speed. One is much fitter than the other. Which of them is more likely to need anaerobic respiration at that speed?',
        "options": [
            {"text": 'The fitter jogger, because they can push themselves much harder than before.', "correct": False,
             "why": 'Being fitter raises the oxygen delivery ceiling, which makes anaerobic respiration less likely at a given speed, not more.'},
            {"text": 'Neither — it depends only on speed, not on fitness.', "correct": False,
             "why": 'Fitness changes how much oxygen the heart and lungs can deliver, which changes whether a given speed needs anaerobic respiration.'},
            {"text": 'Both equally, since they are running at exactly the same speed.', "correct": False,
             "why": "The same speed can demand more than one person's oxygen supply can cover while staying well within another's, depending on fitness."},
            {"text": 'The less fit jogger, because their oxygen delivery ceiling is lower.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e28',
        "band": 'easier',
        "text": 'What is measured in a lactate threshold test?',
        "options": [
            {"text": 'The pace at which lactic acid starts to build up rapidly in the blood.', "correct": True},
            {"text": "The total amount of oxygen a runner's lungs are physically able to hold at their maximum capacity.", "correct": False,
             "why": 'Lung capacity is a different measurement; a lactate threshold test is about the pace at which lactic acid starts to accumulate.'},
            {"text": "How many times a runner's heart beats in a minute at rest.", "correct": False,
             "why": 'Resting heart rate is a different measurement from the pace at which lactate starts to build up.'},
            {"text": 'The total distance a runner can cover in one hour.', "correct": False,
             "why": 'Distance covered is not what a lactate threshold test measures; it measures the pace where lactate starts rising sharply.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e29',
        "band": 'easier',
        "text": 'A student says breathing out more carbon dioxide during a sprint proves the muscles are respiring anaerobically. Is this good evidence?',
        "options": [
            {"text": 'Yes — carbon dioxide is exactly what anaerobic respiration produces in human muscle, every single time it runs.', "correct": False,
             "why": 'Human anaerobic respiration produces no carbon dioxide at all; the gas comes from the aerobic respiration still running.'},
            {"text": 'No — carbon dioxide comes from the aerobic route, which is still running at full rate throughout the sprint.', "correct": True},
            {"text": 'Yes — more carbon dioxide always means more anaerobic respiration is happening.', "correct": False,
             "why": 'Carbon dioxide is a product of the aerobic route, which is running flat out throughout a sprint; it says nothing about the anaerobic route.'},
            {"text": 'No — because sprinting produces no carbon dioxide of any kind.', "correct": False,
             "why": 'Sprinting does produce carbon dioxide, from the aerobic respiration that continues throughout; it is just not evidence of the anaerobic route.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-e30',
        "band": 'easier',
        "text": 'A student claims that during a sprint, muscles switch to breaking down a completely different fuel instead of glucose, and that this is why the process is called anaerobic. Is this correct?',
        "options": [
            {"text": 'No — the same glucose is broken down; the difference is that no oxygen is used and it is not taken all the way to carbon dioxide and water.', "correct": True},
            {"text": 'Yes — the muscle switches to burning fat instead, because fat needs less oxygen to break down.', "correct": False,
             "why": "Anaerobic respiration uses no oxygen at all, so the reason cannot be about needing less of it. It is still the same glucose being broken down, only partly."},
            {"text": 'Yes — the muscle switches to burning protein, which releases energy faster than glucose does.', "correct": False,
             "why": 'The fuel does not change to protein. Glucose is still the substance being broken down; what changes is that the breakdown stops partway and skips using oxygen.'},
            {"text": 'No — but only because the muscle has run out of glucose and briefly stops respiring instead.', "correct": False,
             "why": 'The muscle has not run out of glucose or stopped respiring. Anaerobic respiration is still breaking glucose down — just without oxygen, and not as completely.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s11',
        "band": 'standard',
        "text": 'A student says muscles ‘stop breathing’ when they respire anaerobically. What is wrong with this description?',
        "options": [
            {"text": 'Muscles do not breathe at all; ‘anaerobic’ just means the reaction is happening without using oxygen.', "correct": True},
            {"text": 'Nothing — muscles genuinely stop taking in any air of their own the moment anaerobic respiration begins.', "correct": False,
             "why": 'Muscles never breathe air in the first place; breathing is a whole-body process, separate from the reaction happening inside a muscle cell.'},
            {"text": 'It is wrong because anaerobic respiration actually uses more oxygen than usual.', "correct": False,
             "why": 'Anaerobic respiration uses no oxygen at all; that is the entire meaning of the word.'},
            {"text": 'It is only wrong for leg muscles, which never stop breathing.', "correct": False,
             "why": 'No muscle breathes, in the legs or anywhere else; breathing is done by the lungs, not by muscle cells.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s12',
        "band": 'standard',
        "text": 'A PE teacher writes the summary ‘glucose + oxygen gives lactic acid’ on the board for anaerobic respiration. What is wrong with it?',
        "options": [
            {"text": 'Nothing is wrong at all; a small amount of oxygen is always needed just to get the whole reaction started.', "correct": False,
             "why": 'Anaerobic respiration needs no oxygen at any point, including at the start; the word itself means without oxygen.'},
            {"text": 'Oxygen should not appear on the left; anaerobic respiration uses none at all.', "correct": True},
            {"text": 'Carbon dioxide should also appear on the right, alongside the lactic acid, since every energy-releasing reaction produces some.', "correct": False,
             "why": 'Human anaerobic respiration makes no carbon dioxide; lactic acid is the only product.'},
            {"text": 'It should read ‘glucose gives ethanol’, not ‘lactic acid’.', "correct": False,
             "why": "Ethanol is yeast's anaerobic product; human muscle's anaerobic product is lactic acid."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s13',
        "band": 'standard',
        "text": 'A student argues that if anaerobic respiration used the same amount of glucose as aerobic respiration but got less energy out, some energy must have simply vanished. Explain the flaw.',
        "options": [
            {"text": 'The flaw is that anaerobic respiration actually uses far less glucose for the same amount of work, which is why it releases so much less energy.', "correct": False,
             "why": 'The comparison is about energy released from the same amount of glucose, and it really is far less anaerobically — nothing about glucose quantity explains that.'},
            {"text": 'The flaw is that some of the missing energy escapes as heat, since anaerobic reactions are known to run noticeably hotter inside a working cell.', "correct": False,
             "why": 'Both routes release some heat; the real reason less energy is released is that the glucose is only partly broken down anaerobically.'},
            {"text": 'No energy vanishes; it stays trapped in the lactic acid, because the glucose has only been partly broken down.', "correct": True},
            {"text": 'There is no flaw; energy really is destroyed whenever a chemical reaction like this one is left incomplete part-way through.', "correct": False,
             "why": 'Energy is never destroyed; the energy not released anaerobically simply remains stored in the lactic acid molecule.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s14',
        "band": 'standard',
        "text": 'A coach tells an athlete their ‘oxygen debt’ from a hard set is now three units. What does this actually mean for the athlete?',
        "options": [
            {"text": 'Their muscles are three units short of the oxygen they need to start moving again, and cannot contract at all again until it is fully repaid.', "correct": False,
             "why": 'The debt is about repaying what was borrowed for lactic acid made during the set, not about oxygen needed to move again.'},
            {"text": 'Their blood lost three units of oxygen permanently during the set.', "correct": False,
             "why": 'Oxygen is not lost or destroyed; the debt describes extra oxygen still needed afterwards, not oxygen that disappeared.'},
            {"text": 'They must wait three minutes before their heart rate can return to normal.', "correct": False,
             "why": 'The debt is measured in units of oxygen, not directly in minutes; recovery time follows from how large the debt is, but is not what the figure states.'},
            {"text": 'Their body needs three extra units of oxygen, on top of normal, to deal with the lactic acid made during the set.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s15',
        "band": 'standard',
        "text": "After a hard set of sprints, a runner's blood lactate falls steadily over the next hour. Which organ is doing most of the work to bring that about, and how?",
        "options": [
            {"text": 'The liver, which either uses oxygen to break the lactic acid down completely or spends energy turning it back into glucose.', "correct": True},
            {"text": 'The lungs, which filter the lactic acid straight out of the blood as it passes through.', "correct": False,
             "why": 'The lungs exchange gases; they do not filter a dissolved substance like lactic acid out of the blood.'},
            {"text": 'The kidneys, which pass the lactic acid straight out in urine.', "correct": False,
             "why": 'Very little lactic acid leaves this way; the liver deals with almost all of it by processing it chemically.'},
            {"text": 'The heart, which simply pumps the lactic acid away until it is gone.', "correct": False,
             "why": "Pumping moves the lactic acid around the body but does not remove or process it; that is the liver's job."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s16',
        "band": 'standard',
        "text": "Two days after a hard downhill run, a runner's thighs ache badly, but a blood test taken at that point shows completely normal lactate levels. Explain why the ache and the lactate reading do not match up.",
        "options": [
            {"text": 'The test must be wrong, since lactic acid always stays raised for as long as the soreness lasts, sometimes for several days after the exercise that produced it.', "correct": False,
             "why": 'Lactic acid does not stay raised for days; it returns to resting levels within about an hour of stopping.'},
            {"text": 'The ache comes from microscopic muscle damage and the repair process, which peaks a day or two later; the lactate from the run cleared within about an hour.', "correct": True},
            {"text": 'The lactate has moved out of the blood and into the sore muscles instead.', "correct": False,
             "why": 'Lactate does not relocate into the muscles to cause soreness; it is cleared from the body by the liver, and the soreness has a separate cause.'},
            {"text": 'Downhill running produces a different, longer-lasting kind of lactic acid.', "correct": False,
             "why": 'There is only one kind of lactic acid, and it clears at the same rate regardless of the type of exercise that produced it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s17',
        "band": 'standard',
        "text": 'A student sees a graph showing anaerobic energy supply rising sharply during a sprint and concludes the aerobic supply must be falling at the same time. Evaluate this conclusion.',
        "options": [
            {"text": 'It is correct, since a cell can only use one respiration route at any one moment, so as soon as one starts up the other has to switch off completely.', "correct": False,
             "why": 'A muscle cell can and does run both routes at once during a sprint; the aerobic route continues at its highest rate throughout.'},
            {"text": 'It is correct, because oxygen gets used up faster than it can be replaced, which is exactly why the whole aerobic system has to shut down until the debt is repaid.', "correct": False,
             "why": 'Aerobic respiration keeps running at the fastest rate the oxygen supply allows; it does not fall, it simply cannot rise fast enough to meet the whole demand.'},
            {"text": 'It is wrong — aerobic supply keeps rising too, up to its own ceiling; anaerobic respiration only adds on top of it.', "correct": True},
            {"text": 'It is only wrong for well-trained athletes, whose years of training let their bodies keep raising oxygen delivery no matter how hard they push.', "correct": False,
             "why": 'The same is true for any athlete, trained or not — aerobic respiration continues rather than falling during a sprint.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s18',
        "band": 'standard',
        "text": 'A swimmer finishes a hard 100 m race, climbs out of the pool, and stands still, but keeps breathing hard for over a minute. A friend says this must mean their muscles are still swimming somehow. Explain what is actually happening instead.',
        "options": [
            {"text": 'The friend is right — some muscle fibres keep contracting weakly even once a swimmer has stopped moving.', "correct": False,
             "why": 'The swimmer is standing still with no visible muscle activity; the extra breathing is driven by chemistry in the blood, not by ongoing contraction.'},
            {"text": 'The extra breathing is simply cooling the swimmer down after the effort of the race.', "correct": False,
             "why": 'Some heat does leave through breathing, but that is not what sets the elevated breathing rate after a race; the trigger is chemical.'},
            {"text": 'The lungs are slowly returning to their normal size after being stretched during the race.', "correct": False,
             "why": 'Breathing rate is controlled by signals from the blood, not by the lungs physically returning to a resting size.'},
            {"text": 'The muscles have stopped working; the extra breathing is repaying the oxygen debt built up from lactic acid made during the race.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s19',
        "band": 'standard',
        "text": 'A cyclist rides at a pace where their legs demand 100 units of energy and their heart and lungs can deliver 100 units of oxygen. What happens if they then speed up so their legs demand 120 units?',
        "options": [
            {"text": 'The extra 20 units are supplied anaerobically, and lactic acid begins to build up.', "correct": True},
            {"text": 'Nothing changes at all.', "correct": False,
             "why": 'Oxygen delivery has a ceiling for any given fitness level; demand above that ceiling has to be covered another way.'},
            {"text": "The cyclist's muscles simply run more slowly until the demand drops back down.", "correct": False,
             "why": 'The muscles keep working at the higher demand; the shortfall is covered anaerobically rather than by the muscles slowing themselves down.'},
            {"text": 'The heart instantly delivers more oxygen to match the new demand exactly.', "correct": False,
             "why": 'Oxygen delivery cannot rise instantly to match any demand; once demand exceeds the ceiling, the gap is covered anaerobically instead.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s20',
        "band": 'standard',
        "text": 'A marathon runner and a 100 m sprinter both cross their finish lines completely exhausted. Explain why the sprinter is gasping for breath afterwards while the marathon runner, running at a well-paced effort, is not.',
        "options": [
            {"text": 'The sprinter simply has weaker lungs than the marathon runner, and weaker lungs by themselves are always enough on their own to explain gasping for breath after any kind of race whatsoever.', "correct": False,
             "why": 'Lung strength is not the reason given here; it is the size of the gap between demand and the oxygen delivery ceiling during each race.'},
            {"text": 'The sprinter built up a large oxygen debt from running well above their aerobic ceiling; the marathon runner paced below theirs, so little or no debt built up.', "correct": True},
            {"text": 'The marathon runner used no oxygen at all during their much longer race.', "correct": False,
             "why": 'A marathon runner uses very large amounts of oxygen over the race; what differs is that their pace stayed within what their supply could cover.'},
            {"text": "The sprinter's muscles are simply larger and need more oxygen at rest.", "correct": False,
             "why": "Muscle size at rest is not what is being compared; the difference is in how each pace relates to each runner's own oxygen delivery ceiling."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s21',
        "band": 'standard',
        "text": "A runner's coach says that after a training programme, ‘the gap now opens later’. Explain what this means in terms of oxygen supply and demand.",
        "options": [
            {"text": "It means the runner's muscles now need less oxygen to do the same amount of work, since better-trained fibres run on a smaller supply than before.", "correct": False,
             "why": 'The improvement described is in how much oxygen can be delivered, not in how little the muscles need.'},
            {"text": 'It means the runner has built up a store of extra oxygen from training, which the body can then draw on whenever a race becomes demanding.', "correct": False,
             "why": 'No amount of training creates a meaningful oxygen store; what improves is the rate at which oxygen can be delivered.'},
            {"text": "The runner's oxygen delivery has improved, so a faster pace is now needed before demand rises above what can be supplied.", "correct": True},
            {"text": "It means lactic acid no longer forms in the runner's muscles at any pace.", "correct": False,
             "why": 'Lactic acid still forms once demand exceeds supply, however fit the runner is; training raises the pace at which that happens.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s22',
        "band": 'standard',
        "text": "During a race a cyclist's legs demand 180 units of energy for 20 seconds, while their oxygen delivery covers 140 units throughout. How many units, in total, were supplied anaerobically over those 20 seconds?",
        "options": [
            {"text": '180 units', "correct": False,
             "why": 'That is the total demand for the full 20 seconds, not the anaerobic share of it.'},
            {"text": '140 units', "correct": False,
             "why": 'That is the amount delivered aerobically, not the anaerobic shortfall.'},
            {"text": '320 units', "correct": False,
             "why": 'That comes from adding the demand and supply figures together instead of subtracting one from the other.'},
            {"text": '40 units', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s23',
        "band": 'standard',
        "text": "A runner's lactic acid level falls from 80 units to 20 units over 90 seconds of steady recovery. What is the average clearance rate, in units per 30 seconds?",
        "options": [
            {"text": '20 units per 30 seconds', "correct": True},
            {"text": '60 units per 30 seconds', "correct": False,
             "why": 'That is the total amount cleared over the whole 90 seconds, not the rate per 30-second step.'},
            {"text": '80 units per 30 seconds', "correct": False,
             "why": 'That is the starting level, not the amount cleared in each 30-second step.'},
            {"text": '10 units per 30 seconds', "correct": False,
             "why": 'That halves the correct rate, as if the total cleared were only 30 units rather than 60.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s24',
        "band": 'standard',
        "text": "A rugby player braces hard against an opponent in a scrum for 15 seconds without their body position changing at all. A teammate says nothing is happening in the player's muscles since nothing is visibly moving. Explain why this is wrong.",
        "options": [
            {"text": 'The teammate is right — a muscle only respires anaerobically while its length is visibly changing.', "correct": False,
             "why": 'A muscle held in a fixed, straining contraction is still working hard and can still build up lactic acid, even with no visible movement.'},
            {"text": 'The muscles are contracting forcefully to hold the position, and lactic acid can build up exactly as it would during running.', "correct": True},
            {"text": "The player's muscles are resting throughout, since a scrum involves pushing rather than movement.", "correct": False,
             "why": "Bracing hard in a scrum is strenuous muscle work, not rest, whatever the player's body position looks like from outside."},
            {"text": 'Lactic acid can only build up in leg muscles, never in the muscles used for pushing.', "correct": False,
             "why": 'Any hard-working muscle can build up lactic acid once its demand for energy outruns its oxygen supply, whichever part of the body it is in.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s25',
        "band": 'standard',
        "text": 'A patient recovering from a heart attack becomes breathless walking to the shops, a distance a healthy neighbour of the same age covers without any trouble. Using what you know about oxygen delivery, explain the difference.',
        "options": [
            {"text": "The patient's muscles need far more oxygen to walk the same distance, because damaged heart tissue forces every other muscle to work much harder than normal.", "correct": False,
             "why": "Walking the same distance demands a similar amount of energy from anyone; what differs here is how much oxygen each person's heart can deliver."},
            {"text": 'The patient has used up their store of oxygen earlier in the day.', "correct": False,
             "why": 'No one holds a meaningful store of oxygen to use up; the issue is the rate at which the heart can deliver oxygen right now.'},
            {"text": "The patient's heart cannot deliver oxygen as fast as a healthy heart, so their delivery ceiling is lower and everyday walking pushes demand above it.", "correct": True},
            {"text": 'The neighbour is simply younger, which is why they do not become breathless.', "correct": False,
             "why": 'The situation states they are the same age; the difference described is in how well each heart delivers oxygen, not in age.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s26',
        "band": 'standard',
        "text": 'A doctor examining muscle tissue under a microscope after a biopsy wants to know whether a sample was respiring anaerobically shortly before it was taken. Which cells should be examined, and why?',
        "options": [
            {"text": 'Blood cells passing through the tissue, since they are what carries the anaerobic reaction along as it moves through the muscle.', "correct": False,
             "why": 'Blood cells carry lactic acid away after it has been made; the reaction itself happens inside the muscle cells, not inside blood cells.'},
            {"text": 'Nerve cells running alongside the muscle, since they control when the muscle contracts and so must be doing the actual respiring themselves.', "correct": False,
             "why": 'Nerve cells signal a muscle to contract, but the anaerobic reaction itself takes place inside the muscle cells being signalled.'},
            {"text": 'Fat cells stored around the muscle, since they supply the fuel being respired.', "correct": False,
             "why": 'Fat cells may store fuel nearby, but the respiration reaction itself happens inside the working muscle cells, not inside fat cells.'},
            {"text": 'The muscle cells themselves, because that is exactly where anaerobic respiration happens during exercise.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s27',
        "band": 'standard',
        "text": 'A student tests the gas given off by a sample of contracting human muscle tissue in a lab and finds no carbon dioxide at all, even though the tissue is clearly respiring hard. Explain this result.',
        "options": [
            {"text": 'The tissue must be respiring anaerobically, since that route produces no carbon dioxide in human muscle at all.', "correct": True},
            {"text": 'The result must be a mistake, since all respiration, of every kind and in every tissue, always produces at least some carbon dioxide.', "correct": False,
             "why": 'Anaerobic respiration in human muscle genuinely produces no carbon dioxide; a clean result showing none is not necessarily a mistake.'},
            {"text": 'The tissue must not be respiring at all, since respiration without any gas being given off at all is simply not possible for a cell.', "correct": False,
             "why": 'The muscle is described as clearly respiring hard; producing lactic acid rather than a gas does not mean no respiration is happening.'},
            {"text": 'The tissue is respiring aerobically, but too slowly to detect the carbon dioxide yet, which a more sensitive instrument would surely pick up.', "correct": False,
             "why": 'Aerobic respiration would produce carbon dioxide at whatever rate it runs; the absence of any at all points to the anaerobic route instead.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s28',
        "band": 'standard',
        "text": 'A sports scientist takes two blood samples from the same runner: one at rest, one straight after a hard interval session. The second sample shows lactate far above resting levels. What can the scientist conclude, and what can they NOT conclude, from this alone?',
        "options": [
            {"text": 'They can conclude exactly how many calories were burned during the session.', "correct": False,
             "why": 'A lactate reading shows that anaerobic respiration happened; it does not by itself measure the total energy used during the session.'},
            {"text": 'They can conclude the muscles respired anaerobically during the session; they cannot conclude exactly how much energy in total the session used.', "correct": True},
            {"text": "They can conclude the runner's aerobic respiration stopped during the interval session.", "correct": False,
             "why": 'A raised lactate reading shows anaerobic respiration occurred alongside the aerobic route, not that the aerobic route stopped.'},
            {"text": "They can conclude the runner's heart is now permanently damaged.", "correct": False,
             "why": 'A single raised lactate reading after hard exercise is a normal, temporary finding and says nothing about permanent heart damage.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s29',
        "band": 'standard',
        "text": 'An athlete wearing a full-face oxygen mask, breathing pure oxygen instead of air, still builds up lactic acid during an all-out sprint. Explain why extra oxygen in the air breathed in does not remove the need for anaerobic respiration.',
        "options": [
            {"text": 'Pure oxygen is actually poisonous in large amounts, and that danger alone is the whole reason the muscles still resort to the anaerobic route rather than using the extra oxygen offered.', "correct": False,
             "why": 'Breathing pure oxygen for a short sprint is not the issue here; the point is that the limit is delivery, not the amount available to breathe.'},
            {"text": 'The mask cannot deliver oxygen fast enough for sprinting, unlike normal air.', "correct": False,
             "why": 'The mask supplies oxygen at least as fast as normal air; the limiting step is delivery from the lungs to the working muscles by the heart and blood.'},
            {"text": 'The limit during a flat-out sprint is how fast the heart and blood can deliver oxygen to the muscles, not how much oxygen is available to breathe in.', "correct": True},
            {"text": 'Anaerobic respiration happens regardless of oxygen levels and cannot be prevented by breathing anything.', "correct": False,
             "why": 'Anaerobic respiration is specifically triggered when demand exceeds supply; it is avoided at paces within the supply ceiling.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s30',
        "band": 'standard',
        "text": 'Two friends jog together at the same speed every week. After a few months, one friend can hold a conversation easily the whole way, while the other is out of breath and cannot speak in full sentences. Explain the likely difference between them.',
        "options": [
            {"text": 'The out-of-breath friend must simply be trying harder to keep up, and trying harder by itself is always enough on its own to explain running out of breath at any pace.', "correct": False,
             "why": "Both are running at the same speed; the difference described is in each person's oxygen delivery capacity, not in effort."},
            {"text": 'The friend who can talk easily must be using no oxygen at all, since anyone able to hold a full conversation cannot be respiring using any oxygen whatsoever.', "correct": False,
             "why": 'Aerobic respiration, which uses oxygen, is exactly what lets someone jog comfortably and keep talking; using no oxygen is not what is happening.'},
            {"text": 'Both friends are respiring in exactly the same way, and the difference is only in their mood.', "correct": False,
             "why": 'The described difference in breathing and ability to talk reflects a real difference in oxygen delivery, not simply mood.'},
            {"text": 'The friend who is out of breath likely has a lower oxygen delivery ceiling, so the same speed pushes them into anaerobic respiration while it does not for the other.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s31',
        "band": 'standard',
        "text": 'A sports scientist tests a runner every few weeks by taking a pinprick blood sample during a treadmill run at increasing speeds. What is this test designed to find?',
        "options": [
            {"text": "The pace at which the runner's lactate level begins to rise sharply.", "correct": True},
            {"text": 'The exact number of calories the runner burns in a typical training session.', "correct": False,
             "why": 'This test tracks lactate against pace; it does not measure total calories burned in a session.'},
            {"text": "How quickly the runner's heart rate returns to normal after they stop running.", "correct": False,
             "why": 'That is a different kind of recovery measurement; this test is about lactate rising with increasing pace, not heart rate afterwards.'},
            {"text": 'The maximum speed the runner can reach over a very short sprint.', "correct": False,
             "why": 'A short maximum sprint speed is a different test; this one increases speed gradually to find where lactate starts climbing.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-s32',
        "band": 'standard',
        "text": "During an interval training session, a coach watches a runner's breathing rate rise sharply on every hard rep and argues this alone proves lactic acid is building up each time. Evaluate the coach's reasoning.",
        "options": [
            {"text": 'The reasoning is entirely sound, since every single rise in breathing rate that has ever been recorded during any kind of exercise has always been caused by lactic acid building up and by nothing else at all.', "correct": False,
             "why": 'Breathing rate also rises during hard aerobic effort with no anaerobic contribution at all, so a rise alone does not prove lactic acid is building up.'},
            {"text": 'The reasoning is incomplete — breathing rate alone does not distinguish extra oxygen demand from a genuine build-up of lactic acid; only a lactate measurement can confirm that.', "correct": True},
            {"text": 'The reasoning is wrong, because breathing rate has nothing to do with respiration of any kind.', "correct": False,
             "why": "Breathing rate is closely linked to the body's respiration, aerobic and anaerobic; the flaw is that a rise alone cannot distinguish which kind is driving it."},
            {"text": 'The reasoning would only be sound if the runner also stopped moving completely.', "correct": False,
             "why": "Stopping moving is not what would confirm the coach's claim; only a direct lactate measurement, at any point, would show whether it is building up."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h11',
        "band": 'harder',
        "text": 'A marine biologist studying a diving seal argues that since the seal holds its breath completely underwater, every one of its cells must be respiring anaerobically for the whole dive. Evaluate this claim.',
        "options": [
            {"text": "A seal's large blood and muscle oxygen store lets many cells stay aerobic for much of a dive, so the claim overstates it.", "correct": True},
            {"text": '‘holding the breath’ and ‘respiring anaerobically’ mean exactly the same thing in every diving animal.', "correct": False,
             "why": 'Holding the breath stops new oxygen entering the body; it does not instantly mean every cell has switched over, especially with a large internal oxygen store available.'},
            {"text": 'The claim is wrong only because seals do not respire at all underwater.', "correct": False,
             "why": 'Seals continue respiring throughout a dive; the question is which route each cell is using, not whether respiration happens at all.'},
            {"text": "The claim is correct for the seal's muscles but wrong for every other organ.", "correct": False,
             "why": "The general point applies broadly, not only to muscles — a diving seal's stored oxygen can support aerobic respiration in many tissues for much of a dive."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h12',
        "band": 'harder',
        "text": 'A student rewrites the human anaerobic word summary so that ‘+ energy’ appears on the right-hand side beside the product, arguing that leaving energy off is incomplete. Evaluate this argument.',
        "options": [
            {"text": 'Energy genuinely belongs on the right, listed alongside lactic acid, in the same way carbon dioxide and water are listed for the aerobic reaction.', "correct": False,
             "why": 'Energy is not a substance that can be listed as a product; it is what the reaction releases, not something it makes.'},
            {"text": 'Energy is not a substance and is never written as a product in a word summary; leaving it off is correct, not incomplete.', "correct": True},
            {"text": 'The argument is correct, but energy should be written on the left instead, since it is put in to start the reaction.', "correct": False,
             "why": 'Anaerobic respiration does not need energy put in to start; energy is released by the reaction, not supplied to it.'},
            {"text": 'Oxygen should also be added to the left instead.', "correct": False,
             "why": 'Anaerobic respiration uses no oxygen at all; adding it would be a separate and larger error than the one about energy.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h13',
        "band": 'harder',
        "text": 'A student argues that since ‘debt’ usually means something is owed to another person, the term ‘oxygen debt’ must be scientifically misleading. Evaluate this argument.',
        "options": [
            {"text": 'The argument is correct, and scientists should stop using the term ‘oxygen debt’ altogether in every biology textbook and every classroom from now on.', "correct": False,
             "why": 'Used as the analogy it is intended to be — extra oxygen still needed afterwards — the term communicates the idea clearly rather than misleadingly.'},
            {"text": 'Oxygen genuinely has to be paid back to the air afterwards.', "correct": False,
             "why": 'The debt describes oxygen the body still needs to take in, not oxygen that has to be returned to the air.'},
            {"text": 'The correct term is actually ‘oxygen debit’, not ‘oxygen debt’.', "correct": False,
             "why": 'The issue in the argument is about the analogy behind the term, not about which of two similar words is used.'},
            {"text": 'The word is a deliberate analogy for oxygen still needed afterwards, not a literal debt to anyone; understood that way it is not misleading.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h14',
        "band": 'harder',
        "text": 'A researcher proposes that if the liver were removed from the body entirely, lactic acid made during exercise would simply stay in the blood forever with no consequence. Evaluate this claim.',
        "options": [
            {"text": 'The claim understates the risk — lactic acid would keep accumulating with nowhere to go, which has serious consequences, not none.', "correct": True},
            {"text": 'The claim is correct, since lactic acid causes no harm to the body even if it is never removed.', "correct": False,
             "why": 'Lactic acid that is never processed would go on accumulating rather than simply sitting harmlessly, which is a real problem rather than no consequence.'},
            {"text": "The claim is correct, because the kidneys would take over the liver's job of dealing with lactic acid instead.", "correct": False,
             "why": 'The kidneys are not described as an alternative route for processing lactic acid; that role belongs to the liver.'},
            {"text": 'The claim is wrong, but only because lactic acid would instead turn back into glucose on its own, without any liver at all.', "correct": False,
             "why": 'Converting lactic acid back into glucose is a process the liver specifically carries out using energy; it does not happen on its own.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h15',
        "band": 'harder',
        "text": 'A gym instructor tells a class that stretching immediately after a hard session will ‘flush out’ the lactic acid and prevent the soreness felt two days later. Evaluate this advice scientifically.',
        "options": [
            {"text": 'The advice is sound, since stretching is well known among coaches and physiotherapists to speed up how quickly lactic acid leaves a tired muscle.', "correct": False,
             "why": 'Lactic acid clears from the blood within about an hour whether or not stretching happens; stretching is not what is removing it.'},
            {"text": 'Lactic acid clears within about an hour regardless of stretching; the two-day soreness comes from muscle fibre damage and repair instead.', "correct": True},
            {"text": 'Stretching prevents lactic acid from forming in the first place.', "correct": False,
             "why": 'Stretching happens after the session, once lactic acid has already been made during the exercise; it cannot prevent something that has already occurred.'},
            {"text": 'Lactic acid actually causes no soreness at any point, during exercise or after it.', "correct": False,
             "why": 'Lactic acid genuinely does contribute to the burning felt during hard effort; the error in the advice is about what causes the soreness two days later.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h16',
        "band": 'harder',
        "text": 'A student argues that because oxygen delivery keeps rising throughout a sprint, right up to its ceiling, this proves aerobic respiration is providing most of the energy for a 100 m sprint. Evaluate this argument.',
        "options": [
            {"text": 'The argument is correct, since anything that keeps rising throughout an effort must, by that fact alone, be supplying most of the energy for the whole of that effort.', "correct": False,
             "why": "Aerobic supply rising to its ceiling does not mean it covers most of the demand; a sprint's demand is far above that ceiling."},
            {"text": 'Anaerobic respiration only ever contributes a tiny, negligible amount of energy in any sprint, however short or intense it is.', "correct": False,
             "why": 'In an all-out sprint the anaerobic contribution is large, not negligible, because demand so far exceeds what the aerobic route alone can deliver.'},
            {"text": 'Aerobic respiration flat out still supplies far less than an all-out sprint demands, so most of the extra energy comes from the anaerobic route.', "correct": True},
            {"text": 'Aerobic respiration actually falls rather than rises during a sprint.', "correct": False,
             "why": 'Aerobic respiration rises to its highest rate during a sprint rather than falling; the flaw is in what that rising supply is being compared with.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h17',
        "band": 'harder',
        "text": 'A patient recovering from surgery is given extra oxygen through a mask and is found to still be breathing hard for some time afterwards, even lying completely still. A doctor argues this must be an oxygen debt from anaerobic respiration during the operation. Evaluate this reasoning, given that the patient was under anaesthetic and not exercising.',
        "options": [
            {"text": 'Raised breathing after any kind of medical event of any sort always means an oxygen debt is currently being repaid.', "correct": False,
             "why": 'Raised breathing has many possible causes; an oxygen debt specifically comes from muscles that were working hard, which does not fit a still, anaesthetised patient.'},
            {"text": "Being placed under anaesthetic is itself a form of intense exercise for every cell in the patient's body, working just as hard as a sprinting muscle.", "correct": False,
             "why": 'Being under anaesthetic is not a form of exercise; the muscles are not working hard and producing lactic acid.'},
            {"text": 'Oxygen debts of this kind can only ever happen to trained athletes, never to ordinary hospital patients.', "correct": False,
             "why": "Oxygen debts can happen to anyone whose muscles work hard enough to outrun their oxygen supply; the issue here is that this patient's muscles were not doing that."},
            {"text": "A genuine oxygen debt comes from muscles working hard and building lactic acid, which a still, anaesthetised patient's muscles were not doing.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h18',
        "band": 'harder',
        "text": 'A physiologist proposes a rule: ‘anaerobic respiration happens whenever a muscle is working hard.’ A colleague objects that this rule is too simple. Using the idea of an oxygen delivery ceiling, explain what is missing from the proposed rule.',
        "options": [
            {"text": "‘Hard’ is relative to a person's own oxygen delivery ceiling — the same effort can stay aerobic for a fit person but push an unfit one anaerobic.", "correct": True},
            {"text": 'Nothing is missing; any muscle working hard by definition needs anaerobic respiration to help it.', "correct": False,
             "why": "Whether anaerobic respiration is needed depends on how the effort compares with that person's own oxygen delivery ceiling, not on effort alone."},
            {"text": 'The missing factor is glucose supply, since a muscle can only respire anaerobically once it starts running low on fuel.', "correct": False,
             "why": 'Anaerobic respiration is triggered by demand exceeding oxygen supply, not by a shortage of glucose; both routes use glucose as fuel.'},
            {"text": 'The missing factor is body temperature, since only a hot muscle can respire anaerobically.', "correct": False,
             "why": 'Body temperature is not what decides whether anaerobic respiration happens; the relationship between demand and oxygen supply is.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h19',
        "band": 'harder',
        "text": "A running coach sets two athletes the same target time for a race, even though one is far fitter than the other. The fitter athlete finishes feeling comfortable; the less fit one finishes gasping and sore two days later. Explain this outcome in terms of each athlete's oxygen delivery ceiling relative to the pace required.",
        "options": [
            {"text": 'The less fit athlete simply tried much harder mentally than the fitter one, and that mental effort alone is what caused all of the soreness felt two days later.', "correct": False,
             "why": "Mental effort is not described as the cause here; the difference is physiological, in how the same pace relates to each athlete's own oxygen delivery ceiling."},
            {"text": "The pace stayed below the fitter athlete's ceiling, keeping the race mostly aerobic; the same pace was above the less fit athlete's lower ceiling.", "correct": True},
            {"text": 'The fitter athlete used no anaerobic respiration at all during the entire race.', "correct": False,
             "why": 'Even a very fit athlete can use some anaerobic respiration, especially near the end of a hard effort; the key difference is how much of the race demanded it.'},
            {"text": 'Both athletes respired in exactly the same way, and the soreness is unrelated to how the race was run.', "correct": False,
             "why": "The soreness described is linked to muscle damage from working above one's own oxygen delivery ceiling, which differed between the two athletes here."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h20',
        "band": 'harder',
        "text": 'A study follows a group of new runners over a year and finds their resting heart rate falls while the pace at which their lactate starts rising sharply increases. A student claims these two findings are unrelated. Evaluate this claim.',
        "options": [
            {"text": 'The claim is correct, since resting heart rate and lactate threshold measure two completely different, entirely unconnected systems inside the human body.', "correct": False,
             "why": 'Both measurements are closely linked to how efficiently the heart delivers oxygen, which is exactly the kind of change training is expected to produce.'},
            {"text": 'Lactate threshold depends only on the muscles themselves, and not at all on how well the heart happens to be working.', "correct": False,
             "why": "The heart's ability to deliver oxygen is central to where a person's lactate threshold sits, alongside the muscles' own demand."},
            {"text": 'Both findings share one cause: a more efficient heart, which lowers resting demand and raises the pace before demand outstrips supply.', "correct": True},
            {"text": 'Resting heart rate has no connection to fitness of any kind.', "correct": False,
             "why": 'Resting heart rate is a well-established indicator of cardiovascular fitness, which is exactly the connection the claim wrongly denies exists.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h21',
        "band": 'harder',
        "text": "Over a 30-second maximal effort, a rower's legs demand a steady 220 units of energy delivery. Oxygen delivery rises linearly from 60 units to 140 units over that time. Estimate the average number of units supplied anaerobically across the whole 30 seconds, using the average oxygen delivery.",
        "options": [
            {"text": '160 units', "correct": False,
             "why": 'That subtracts only the starting oxygen delivery of 60, not the average delivery of 100, from the demand.'},
            {"text": '80 units', "correct": False,
             "why": 'That subtracts the final oxygen delivery of 140, rather than the average of 100, from the demand.'},
            {"text": '220 units', "correct": False,
             "why": 'That is the total demand, ignoring the oxygen that was delivered at all.'},
            {"text": '120 units', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h22',
        "band": 'harder',
        "text": "A sprinter's lactic acid rises from 0 to 90 units during a 12-second sprint, then clears at a steady rate of 15 units per 30 seconds during recovery. Estimate the total recovery time needed to clear it completely.",
        "options": [
            {"text": '180 seconds', "correct": True},
            {"text": '90 seconds', "correct": False,
             "why": 'That treats the clearance rate as 30 units per 30 seconds rather than the stated 15.'},
            {"text": '12 seconds', "correct": False,
             "why": 'That mistakes the length of the sprint itself for the recovery time needed afterwards.'},
            {"text": '270 seconds', "correct": False,
             "why": 'That comes from dividing by 10 units per 30 seconds instead of the stated 15.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h23',
        "band": 'harder',
        "text": 'A physiotherapist argues that isometric exercises (holding a fixed position under load) are ‘safer’ than running because they ‘never produce lactic acid’. Evaluate this claim scientifically.',
        "options": [
            {"text": 'Lactic acid can only ever build up in a muscle whose length is visibly changing from one moment to the next, never while it is simply held still under load.', "correct": False,
             "why": 'A muscle held still under load is still contracting hard and can still outrun its oxygen supply, producing lactic acid without any visible movement.'},
            {"text": 'A muscle held under a hard, sustained load can demand more energy than its oxygen supply covers, producing lactic acid exactly as running does.', "correct": True},
            {"text": 'Isometric exercises of every kind use far less total energy than any dynamic exercise such as running ever could.', "correct": False,
             "why": 'A sufficiently hard isometric hold can demand a great deal of energy, just as running can; energy use is not automatically lower with no visible movement.'},
            {"text": 'Isometric exercises actually use noticeably more oxygen overall than running does at any comparable intensity.', "correct": False,
             "why": 'The flaw in the claim is not about which uses more oxygen overall; it is the assumption that no visible movement means no lactic acid can be produced.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h24',
        "band": 'harder',
        "text": 'A cardiologist compares two patients with weak hearts: one whose heart still pumps reasonably well and one whose heart pumps very poorly. Predict which patient will become breathless at a lower level of everyday activity, and explain using the idea of an oxygen delivery ceiling.',
        "options": [
            {"text": 'Neither — both patients will become breathless at exactly the same level of activity, since both have weak hearts.', "correct": False,
             "why": 'A weaker pump generally means a lower oxygen delivery ceiling, so the patient with the more severely weakened heart should become breathless sooner.'},
            {"text": 'The patient whose heart still pumps reasonably well, since a stronger heart works harder and tires sooner.', "correct": False,
             "why": 'A stronger-pumping heart, even if still somewhat weak, delivers oxygen faster, raising the ceiling and delaying breathlessness rather than causing it sooner.'},
            {"text": 'The patient whose heart pumps very poorly, because their oxygen delivery ceiling is lower, so even mild everyday activity can push demand above it.', "correct": True},
            {"text": 'Neither patient will experience any breathlessness, since heart strength does not affect oxygen delivery to muscles.', "correct": False,
             "why": 'Heart strength directly affects how fast oxygen can be delivered to working muscles, which is exactly why a weaker heart lowers the delivery ceiling.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h25',
        "band": 'harder',
        "text": 'A scientist wants to prove that anaerobic respiration happens specifically inside muscle cells rather than in the blood vessels running through the muscle. Suggest what evidence would settle this, and explain why testing the blood alone would not be enough.',
        "options": [
            {"text": 'Testing the blood alone would be entirely enough on its own, since lactic acid always appears there no matter which tissue in the body actually produced it.', "correct": False,
             "why": 'Blood carries lactic acid away after it is made elsewhere; finding it in blood does not by itself prove where it was produced.'},
            {"text": 'Nothing could ever settle this question, since lactic acid cannot be traced back to any specific location in the body.', "correct": False,
             "why": 'Testing tissue directly, separately from the blood passing through it, could show whether the muscle cells themselves are producing lactic acid.'},
            {"text": 'Testing the surrounding fat tissue would settle it, since fat cells absorb lactic acid before the blood does.', "correct": False,
             "why": 'Fat cells are not described as absorbing lactic acid; the relevant comparison is between the muscle tissue itself and the blood carrying lactic acid away.'},
            {"text": 'Testing the muscle tissue itself, separately from the blood, would settle it; blood alone only shows lactic acid already carried away.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h26',
        "band": 'harder',
        "text": 'A researcher analyses gas given off by human muscle tissue during intense, oxygen-starved contraction and detects a small amount of carbon dioxide. A student claims this disproves the idea that human anaerobic respiration makes no carbon dioxide. Evaluate this claim.',
        "options": [
            {"text": 'Some aerobic respiration is probably still running in the tissue, and that residual activity, not the anaerobic route, is the likely source.', "correct": True},
            {"text": 'The claim is definitely correct, and the textbook rule that human anaerobic respiration makes absolutely no carbon dioxide of any kind must simply be wrong.', "correct": False,
             "why": 'A small amount of carbon dioxide is more likely explained by some aerobic respiration still occurring in the tissue than by the anaerobic route producing it.'},
            {"text": 'Oxygen-starved tissue of any kind always produces noticeably more carbon dioxide than tissue that is well oxygenated.', "correct": False,
             "why": 'Oxygen-starved tissue running mostly anaerobically would be expected to produce less carbon dioxide overall, not more, from whatever aerobic respiration remains.'},
            {"text": 'Carbon dioxide cannot be detected in tissue samples by any method.', "correct": False,
             "why": 'Carbon dioxide can be detected in tissue samples; the issue with the claim is about what is producing the small amount found.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h27',
        "band": 'harder',
        "text": "A sports scientist claims that a single blood lactate reading, taken once, straight after a training session, can reliably predict an athlete's performance in next month's race. Evaluate this claim.",
        "options": [
            {"text": "The claim is entirely sound, since a single lactate reading taken just once always predicts a runner's future race performance with complete precision.", "correct": False,
             "why": 'It is repeated testing of where the lactate threshold sits, and how that shifts with training, that is linked to predicting performance, not a single reading.'},
            {"text": 'A single reading confirms anaerobic respiration occurred, but says little about future performance, which repeated threshold testing predicts better.', "correct": True},
            {"text": 'Lactate readings are by far the single most important factor in any race, more important than the training itself.', "correct": False,
             "why": 'Lactate threshold testing is a useful tool alongside training, not a replacement for it or a guarantee of race performance on its own.'},
            {"text": 'Blood lactate has absolutely nothing at all to do with athletic performance of any kind, ever, in any sport.', "correct": False,
             "why": 'Blood lactate and the pace at which it rises are genuinely linked to endurance performance; the flaw is treating one reading as sufficient to predict it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h28',
        "band": 'harder',
        "text": 'An engineer proposes a mask that delivers oxygen at ten times the normal atmospheric concentration to a sprinter, claiming this would let them avoid anaerobic respiration completely during a 100 m race. Evaluate this proposal.',
        "options": [
            {"text": 'The proposal would definitely work, since any amount of extra oxygen breathed in always removes the need for anaerobic respiration in every situation.', "correct": False,
             "why": 'The limiting step for a sprint is delivery from lungs to muscles via the heart and blood, not the amount of oxygen available to breathe in.'},
            {"text": "The proposal would work, but only because breathing this concentrated oxygen would also make the sprinter's heart beat exactly ten times faster than normal.", "correct": False,
             "why": "Breathing a higher concentration of oxygen does not multiply heart rate in this way; the heart's own pumping capacity remains the limiting factor."},
            {"text": 'The bottleneck in a sprint is how fast the heart and blood can carry oxygen to the muscles, not how much is available to breathe in.', "correct": True},
            {"text": 'Breathing pure oxygen has no effect on the body whatsoever.', "correct": False,
             "why": 'Breathing extra oxygen does have effects on the body; the issue is specifically that it does not address the real bottleneck of delivery to the muscles.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h29',
        "band": 'harder',
        "text": "A study compares two groups of runners at the same fitness test pace: one group has trained for months, the other has not. The trained group shows lower blood lactate at that pace. A student argues this proves the trained group's muscles ‘need less energy’ to run at that pace. Evaluate this argument.",
        "options": [
            {"text": 'The argument is correct, since lower blood lactate at a given pace always means less total energy is being used to run at that pace, without exception.', "correct": False,
             "why": 'Lower lactate more likely reflects a bigger share of the same demand being met aerobically, thanks to improved oxygen delivery, rather than a smaller total demand.'},
            {"text": 'Trained muscles genuinely use less glucose to contract than untrained ones.', "correct": False,
             "why": 'The energy demand of running at a given pace does not change simply because someone is trained; what changes is how much of that demand can be met aerobically.'},
            {"text": 'Lactate levels have nothing to do with training at all.', "correct": False,
             "why": 'Lactate levels are closely linked to training status; the flaw in the argument is in what a lower reading is best explained by.'},
            {"text": "The trained group's oxygen delivery has likely improved, covering more of the same demand aerobically, rather than the muscles needing less energy.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h30',
        "band": 'harder',
        "text": "A coach uses lactate threshold results to set training paces for a squad, but one athlete's threshold pace has not changed at all after three months of hard training, unlike their teammates. Suggest two different explanations the coach should consider before assuming the training is not working.",
        "options": [
            {"text": 'The training might need adjusting for that athlete, or illness, poor recovery or a measurement inconsistency could be masking a real improvement.', "correct": True},
            {"text": 'There is only one possible explanation for this: the athlete is simply and permanently incapable of ever improving their fitness through training.', "correct": False,
             "why": 'A single unchanged reading has several plausible explanations, including training fit, recovery and measurement issues, rather than pointing to a fixed personal limit.'},
            {"text": "The athlete's oxygen delivery ceiling must be a completely fixed number that training of any kind can never move for anyone, however hard they work.", "correct": False,
             "why": "Training generally can raise an individual's oxygen delivery ceiling over time; a single unchanged result is better explained by other factors."},
            {"text": 'The threshold test itself must always give identical results for every athlete regardless of their training.', "correct": False,
             "why": 'Lactate threshold results do change with training in general; an unchanged reading points to something specific to this athlete or this test.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-03-h31',
        "band": 'harder',
        "text": "A student claims that because a sprinter's breathing rate rises sharply during a race, this alone proves carbon dioxide production has risen, which in turn proves anaerobic respiration is providing most of the sprint's energy. Evaluate this chain of reasoning, one link at a time.",
        "options": [
            {"text": 'The whole chain is sound from start to finish, since every single step correctly and necessarily follows from the one stated immediately before it.', "correct": False,
             "why": 'The final step is not sound — carbon dioxide is a marker of aerobic activity in human muscle, not of the anaerobic contribution, which produces none of it.'},
            {"text": 'The first link holds, but the second fails — the extra carbon dioxide comes from the aerobic route, not the anaerobic one, which produces none.', "correct": True},
            {"text": 'Breathing rate has no connection to carbon dioxide levels in the blood.', "correct": False,
             "why": 'Breathing rate is genuinely linked to carbon dioxide levels; the weak link in the chain is further along, in what raised carbon dioxide is taken as evidence for.'},
            {"text": 'Sprinting produces no carbon dioxide of any kind whatsoever, at any point during or after the race.', "correct": False,
             "why": 'Sprinting does produce carbon dioxide, from the aerobic respiration that continues throughout; the flaw is treating that as evidence for the anaerobic route.'},
        ],
        "figure": None,
    },
]

QUESTIONS.extend(_MRB338_NEW_QUESTIONS)
