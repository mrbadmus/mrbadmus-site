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
            {"text": "Neither — lactic acid causes no pain and no "
                     "breathlessness.",
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
            {"text": "The hard breathing, because oxygen is owed for dealing "
                     "with the acid.",
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
            {"text": "Lactic acid has built up in the working muscles and is "
                     "forcing the slow-down.",
             "correct": True},
            {"text": "They have used up all the glucose stored in their leg "
                     "muscles.",
             "correct": False,
             "why": "Glucose stores are not emptied in twenty seconds. What "
                    "has built up is lactic acid, and that is what limits the "
                    "effort."},
            {"text": "Their muscles have used up the oxygen they stored "
                     "before the start.",
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
            {"text": "It warms the muscles, which breaks the lactic acid down "
                     "faster.",
             "correct": False,
             "why": "Temperature is not what deals with lactic acid. The "
                    "blood is needed to move it, and to bring oxygen to the "
                    "muscles."},
            {"text": "It pushes the lactic acid out through the skin in "
                     "sweat.",
             "correct": False,
             "why": "Sweat carries no lactic acid away. The blood carries it "
                    "to the liver, and the liver is what deals with it."},
            {"text": "It delivers oxygen to the muscles and carries the "
                     "lactic acid to the liver.",
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
            {"text": "Pedalling gently holds demand below what oxygen "
                     "delivery covers, and keeps the blood moving.",
             "correct": True},
            {"text": "Stopping dead makes the muscles produce more lactic "
                     "acid than pedalling does.",
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
