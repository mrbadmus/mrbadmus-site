"""C7 lesson 04 — Measuring a temperature change: twelve questions (MRB-272).

The lesson's argument is one shape: an energy change is measured as a
temperature change, and a temperature change is only as good as the apparatus
around it. The page teaches it by ruling on somebody else's plan and then
building eight rigs, none of which reaches the true value, so these twelve
probe the angles the mastery ladder leaves alone: which two readings are
needed, why the peak is the one to take, and what repeating an experiment can
and cannot fix.

The distractors are built from the lesson's two declared misconceptions.

`ENER-07` (repeating an experiment and averaging makes the result accurate)
drives the wrong options in e04, s02, h01 and h04. Each treats more data as a
cure for any error at all. h04 is the one that matters: it offers a group five
more repeats and asks what that would buy them, where the honest answer is
nothing.

`ENER-08` (results that agree closely with each other must be correct) drives
e03, s03 and h02, where precision is read as accuracy. h02 puts a set of five
readings that agree to a tenth of a degree in front of a student and asks
whether that settles anything.

A third strand, on the page and in neither register entry, is that the FINAL
temperature is the one to record. e01, e02 and s01 are built on it: the peak
arrives within seconds and everything after it is a measure of how long you
were away.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each and C7's four banks hold
twelve of each — level across the four indices by construction rather than by
a rebalancing pass.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, at the correct answer's own
length, and each is a mistake a real student actually makes.
"""

UNIT = "C7"
LESSON = "measuring-a-temperature-change"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c7-04-e01",
        "band": "easier",
        "text": "Which two readings do you need in order to find the "
                "temperature change of a reaction?",
        "options": [
            {"text": "The starting temperature of the solution and the "
                     "highest temperature it reaches", "correct": True},
            {"text": "The temperature of the room and the temperature of the "
                     "mixture at the end", "correct": False,
             "why": "The room may not be at the same temperature as your "
                    "solution. Measure the solution itself before you start."},
            {"text": "The temperature at the start and the temperature ten "
                     "minutes afterwards", "correct": False,
             "why": "Ten minutes later the mixture has cooled back towards "
                    "the room. You need the peak."},
            {"text": "The highest temperature reached and the temperature of "
                     "the alkali you added", "correct": False,
             "why": "What you subtract from is the mixture's own starting "
                    "temperature, not one reactant's."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e02",
        "band": "easier",
        "text": "Why should the highest reading be recorded rather than the "
                "reading after five minutes?",
        "options": [
            {"text": "Because a thermometer becomes less accurate the longer "
                     "it is left in a liquid", "correct": False,
             "why": "A thermometer does not drift like that. What changes in "
                    "five minutes is the mixture, not the instrument."},
            {"text": "Because the peak is the closest the apparatus gets to "
                     "the true value, and heat loss wins after it",
             "correct": True},
            {"text": "Because the reaction is still going after five minutes "
                     "and the number is not final", "correct": False,
             "why": "The reaction has usually finished within seconds. What "
                    "happens in the next five minutes is cooling."},
            {"text": "Because the highest reading is easier to read off a "
                     "scale than a falling one", "correct": False,
             "why": "Both are equally readable. The peak is chosen because it "
                    "is the least spoiled by heat loss."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e03",
        "band": "easier",
        "text": "A group repeats a reaction five times and gets +6.7, +6.8, "
                "+6.8, +6.7 and +6.8 °C. What can they say?",
        "options": [
            {"text": "The result is correct, because five readings agree that "
                     "closely", "correct": False,
             "why": "Close agreement is precision, not accuracy. Five "
                    "readings can agree and all be wrong in the same way."},
            {"text": "The result must be wrong, because real measurements "
                     "always scatter more than that", "correct": False,
             "why": "Tight agreement is a good sign about the method. It is "
                    "just not a guarantee about the value."},
            {"text": "Their readings are precise, but that does not tell them "
                     "whether they are accurate", "correct": True},
            {"text": "Nothing at all, because five readings is too small a "
                     "sample to say anything", "correct": False,
             "why": "Five readings say plenty about how repeatable the method "
                    "is. What they cannot say is whether it is right."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e04",
        "band": "easier",
        "text": "Why is a polystyrene cup better than a glass beaker for this "
                "experiment?",
        "options": [
            {"text": "Because polystyrene reacts less with acids than glass "
                     "does", "correct": False,
             "why": "Glass is famously unreactive with dilute acids. That is "
                    "not the problem with it here."},
            {"text": "Because a cup is smaller, so the same energy warms it "
                     "more", "correct": False,
             "why": "The volume of solution is kept the same either way. The "
                    "difference is in the container itself."},
            {"text": "Because the cup can be thrown away, so there is less "
                     "washing up between runs", "correct": False,
             "why": "Convenience is not a measurement argument, and the "
                    "readings really do differ."},
            {"text": "Because it insulates better and absorbs less of the "
                     "energy warming itself up", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c7-04-s01",
        "band": "standard",
        "text": "Four groups run the same neutralisation and report +5, +7, "
                "+2 and +7 °C. Nobody made anything up. What is the most "
                "likely explanation?",
        "options": [
            {"text": "The reaction released different amounts of energy in "
                     "different beakers", "correct": False,
             "why": "The same reaction with the same amounts releases the "
                    "same energy. The reaction is not the variable."},
            {"text": "The groups lost different amounts of heat before they "
                     "read their thermometers", "correct": True},
            {"text": "Some groups must have used more concentrated acid than "
                     "the others", "correct": False,
             "why": "The question says same acid, same alkali, same volumes. "
                    "What differed was the measuring, not the chemistry."},
            {"text": "School thermometers are unreliable and disagree with "
                     "each other by several degrees", "correct": False,
             "why": "Thermometers are not that bad, and the +2 group's rig "
                    "explains their reading without blaming the instrument."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s02",
        "band": "standard",
        "text": "A group's rig loses heat, so every reading is too low. They "
                "repeat the experiment ten times and take the mean. What does "
                "that achieve?",
        "options": [
            {"text": "It removes the heat loss, because errors cancel out "
                     "over enough repeats", "correct": False,
             "why": "Only errors that fall on BOTH sides of the truth cancel. "
                    "Heat loss falls on one side every time."},
            {"text": "It makes no difference at all, so repeating is a waste "
                     "of time", "correct": False,
             "why": "Repeating genuinely reduces random scatter and shows how "
                    "repeatable the method is. It just cannot fix this."},
            {"text": "It reduces the scatter between their readings, but the "
                     "mean is still too low", "correct": True},
            {"text": "It doubles the accuracy, because ten readings are worth "
                     "twice as much as five", "correct": False,
             "why": "Accuracy is about closeness to the true value, and no "
                    "number of repeats moves a result that is always low."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s03",
        "band": "standard",
        "text": "Which of these is a SYSTEMATIC error in this experiment?",
        "options": [
            {"text": "Misreading the scale by a tenth of a degree, sometimes "
                     "high and sometimes low", "correct": False,
             "why": "That is a random error. It falls on both sides of the "
                    "truth and averaging reduces it."},
            {"text": "Stirring slightly harder on some runs than on others",
             "correct": False,
             "why": "Also random. It changes the reading a little in either "
                    "direction from run to run."},
            {"text": "Spilling a little of the alkali on one of the five "
                     "runs", "correct": False,
             "why": "That is a mistake affecting one run, which is why it "
                    "would show up as an anomalous result you could "
                    "identify."},
            {"text": "Heat escaping from an uninsulated beaker on every "
                     "single run", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s04",
        "band": "standard",
        "text": "A student fits a lid to the cup but leaves a small hole in "
                "it for the thermometer. Why not seal it completely?",
        "options": [
            {"text": "Because a sealed cup could build up pressure and the "
                     "thermometer has to go through somewhere",
             "correct": True},
            {"text": "Because a completely sealed cup would stop the reaction "
                     "happening at all", "correct": False,
             "why": "The reaction does not need air. Sealing it would not "
                    "stop the chemistry."},
            {"text": "Because the hole lets excess heat out and stops the "
                     "reading going too high", "correct": False,
             "why": "The whole point of the lid is to keep heat IN. The hole "
                    "is a cost of the method, not a feature."},
            {"text": "Because a sealed lid would make the reading too "
                     "accurate to compare with other groups", "correct": False,
             "why": "There is no such thing as too accurate, and no group is "
                    "trying to match anybody else's error."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c7-04-h01",
        "band": "harder",
        "text": "Two students compare methods. A uses a glass beaker and "
                "reads at the peak; B uses an insulated cup and reads two "
                "minutes later. Both get about +5 °C. What does that show?",
        "options": [
            {"text": "That the two methods are equally good, since they agree "
                     "with each other", "correct": False,
             "why": "Two methods with different faults can land on the same "
                    "wrong number. Agreement between them proves nothing."},
            {"text": "That the true value must be +5 °C, because two "
                     "different rigs found it", "correct": False,
             "why": "Both rigs lose heat, so both read low. Agreeing on a low "
                    "number does not make it the true one."},
            {"text": "That good apparatus and prompt reading are both needed, "
                     "and each one alone leaves a similar shortfall",
             "correct": True},
            {"text": "That the container makes no difference, since only the "
                     "timing changed the result", "correct": False,
             "why": "Both things changed between the two methods. Nothing "
                    "here isolates the container."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h02",
        "band": "harder",
        "text": "The best rig a school bench can build reads +6.8 °C when the "
                "true value is +7.0 °C. Where did the missing 0.2 °C go?",
        "options": [
            {"text": "Into a rounding error, because thermometers cannot read "
                     "to a tenth of a degree", "correct": False,
             "why": "A digital probe reads to a hundredth. The shortfall is "
                    "real energy, not a rounding artefact."},
            {"text": "Nowhere — it was never released, because the reaction "
                     "did not quite finish", "correct": False,
             "why": "The reaction finishes. What happens to the energy after "
                    "it is released is the question."},
            {"text": "Into the air, which is why the lid was fitted in the "
                     "first place", "correct": False,
             "why": "The lid has already stopped most of that. What is left "
                    "is the apparatus itself absorbing energy."},
            {"text": "Into warming the cup, the lid and the thermometer "
                     "themselves", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h03",
        "band": "harder",
        "text": "A class compares three fuels by heating a beaker of water "
                "with each in turn. Every value they get is far below the "
                "published figure. Is the comparison worthless?",
        "options": [
            {"text": "No, because the same loss applies to all three, so the "
                     "ranking between the fuels still holds", "correct": True},
            {"text": "Yes, because values that far from the published ones "
                     "cannot support any conclusion", "correct": False,
             "why": "They can support a comparison. Being wrong by a similar "
                    "amount each time is exactly what leaves the ranking "
                    "usable."},
            {"text": "Yes, unless they repeat it enough times for the mean to "
                     "approach the published figure", "correct": False,
             "why": "The mean will never approach it. Every reading is low "
                    "for the same reason, so the mean is low too."},
            {"text": "No, because the published figures are themselves only "
                     "estimates and no better than the class's",
             "correct": False,
             "why": "Published figures come from a bomb calorimeter and are "
                    "far better. The reason the comparison survives is that "
                    "the error is shared."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h04",
        "band": "harder",
        "text": "A group with a leaking rig asks whether five more repeats or "
                "a lid would improve their result more. What should you tell "
                "them?",
        "options": [
            {"text": "The repeats, because more data always improves a "
                     "measurement", "correct": False,
             "why": "More data improves precision. It does nothing to an "
                    "error that runs the same way every time."},
            {"text": "The lid, because it attacks the error that is actually "
                     "making every reading wrong", "correct": True},
            {"text": "Neither, because the true value cannot be reached with "
                     "school apparatus anyway", "correct": False,
             "why": "It cannot be reached exactly — but a lid gets them from "
                    "well below it to close to it, which is worth having."},
            {"text": "Both equally, since one reduces scatter and the other "
                     "reduces loss by the same amount", "correct": False,
             "why": "They are not equal here. The scatter is already small "
                    "and the loss is large."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-04-e05",
        "band": "easier",
        "text": "What is insulation?",
        "options": [
            {"text": "Material that stops heat escaping altogether, so that "
                     "an insulated cup loses none of the energy the reaction "
                     "inside it releases",
             "correct": False,
             "why": "Nothing stops it altogether. Even the best school rig "
                    "still reads low"},
            {"text": "Material that keeps electricity in a wire",
             "correct": False,
             "why": "The word is used that way too. Here it is about heat"},
            {"text": "The lid on top of the cup",
             "correct": False,
             "why": "A lid helps, and insulation is what the cup itself is "
                    "made of"},
            {"text": "Material that slows heat escaping",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e06",
        "band": "easier",
        "text": "What is a systematic error?",
        "options": [
            {"text": "An error that pushes every reading the same way",
             "correct": True},
            {"text": "An error made by following the method incorrectly, so "
                     "that the whole experiment has to be set up again from "
                     "the beginning",
             "correct": False,
             "why": "That is a mistake. A systematic error can happen in a "
                    "perfectly followed method"},
            {"text": "An error that scatters readings either side of the "
                     "truth",
             "correct": False,
             "why": "That is a random error, and it is the kind averaging "
                    "reduces"},
            {"text": "An error in the arithmetic",
             "correct": False,
             "why": "That is a mistake in the calculation rather than in the "
                    "measurement"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e07",
        "band": "easier",
        "text": "What is a random error?",
        "options": [
            {"text": "An error that happens without any cause at all, which "
                     "is why nothing can be done to reduce one however the "
                     "apparatus is improved",
             "correct": False,
             "why": "Random errors have causes — reading a scale slightly "
                    "differently each time. Averaging reduces them"},
            {"text": "An error that scatters readings on both sides of the "
                     "true value",
             "correct": True},
            {"text": "An error that makes every reading too low",
             "correct": False,
             "why": "That is systematic, and heat loss is the example in this "
                    "lesson"},
            {"text": "An error made by a careless student",
             "correct": False,
             "why": "Careful workers get random errors too. It is about the "
                    "measurement, not the person"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e08",
        "band": "easier",
        "text": "What is the peak temperature?",
        "options": [
            {"text": "The highest temperature the reaction is capable of "
                     "producing, which is worked out afterwards rather than "
                     "read off the thermometer during the run",
             "correct": False,
             "why": "It is a reading you take at the time. Nothing is worked "
                    "out"},
            {"text": "The reading five minutes after mixing",
             "correct": False,
             "why": "By then heat loss has been winning for some time and the "
                    "number has fallen"},
            {"text": "The highest reading the thermometer reaches",
             "correct": True},
            {"text": "The temperature of the room",
             "correct": False,
             "why": "The room is a separate thing, and it is not what the "
                    "peak measures"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e09",
        "band": "easier",
        "text": "What is meant by the true value?",
        "options": [
            {"text": "The mean of all the readings a group takes, which is "
                     "the closest anybody can get to a value with real "
                     "apparatus and is therefore treated as the true one",
             "correct": False,
             "why": "A mean can be wrong in the same direction every time. "
                    "The true value is what a perfect measurement would "
                    "give"},
            {"text": "The reading the teacher gets",
             "correct": False,
             "why": "A teacher's apparatus loses heat too"},
            {"text": "The largest reading anyone obtained",
             "correct": False,
             "why": "In this experiment the largest is likely to be the "
                    "closest, and that is not what the phrase means"},
            {"text": "The value a perfect measurement would give",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e10",
        "band": "easier",
        "text": "Why does polystyrene foam insulate so well?",
        "options": [
            {"text": "Because it is mostly trapped air, and air is a poor "
                     "conductor",
             "correct": True},
            {"text": "Because the plastic it is made of conducts heat "
                     "extremely badly, far worse than any other material a "
                     "school laboratory has on the shelf",
             "correct": False,
             "why": "Solid polystyrene is a fair insulator and nothing "
                    "special. It is the trapped air that does the work"},
            {"text": "Because it is white, so it reflects heat",
             "correct": False,
             "why": "Colour matters a little for radiation. The trapped air "
                    "is the reason"},
            {"text": "Because it is light",
             "correct": False,
             "why": "It is light BECAUSE it is mostly air. The air is the "
                    "insulator"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e11",
        "band": "easier",
        "text": "How is the temperature change worked out?",
        "options": [
            {"text": "The highest temperature reached, minus the temperature "
                     "of the room",
             "correct": False,
             "why": "The room may not be at the same temperature as the "
                    "solution. You measure the solution before you start"},
            {"text": "The highest or lowest temperature reached, minus the "
                     "starting temperature",
             "correct": True},
            {"text": "The highest temperature reached",
             "correct": False,
             "why": "One reading on its own says nothing. A change is a "
                    "difference"},
            {"text": "The mean of all the readings taken during the run",
             "correct": False,
             "why": "The mean would include readings from before the reaction "
                    "and after it had cooled"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e12",
        "band": "easier",
        "text": "Which way does heat loss push the measured temperature "
                "change?",
        "options": [
            {"text": "It makes it too large",
             "correct": False,
             "why": "Losing heat means the peak is lower than it should be, "
                    "so the change comes out smaller"},
            {"text": "It scatters it either side of the true value, so that "
                     "some runs come out too high and some too low",
             "correct": False,
             "why": "That would be a random error. Heat loss only ever runs "
                    "one way"},
            {"text": "It makes it too small",
             "correct": True},
            {"text": "It has no effect if the cup is insulated",
             "correct": False,
             "why": "Insulation reduces it and never removes it. Even the "
                    "best rig reads low"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c7-04-s05",
        "band": "standard",
        "text": "A group mixes the solutions, writes up their method, and "
                "then reads the thermometer five minutes later. What has that "
                "cost them?",
        "options": [
            {"text": "Nothing, provided they record what they see, since the "
                     "reading five minutes on is a perfectly honest "
                     "measurement of the temperature at that moment",
             "correct": False,
             "why": "It is honest and it is not the quantity wanted. The peak "
                    "has been and gone"},
            {"text": "The starting temperature",
             "correct": False,
             "why": "That was taken before mixing and is unaffected by the "
                    "delay"},
            {"text": "Nothing much, because the reaction is still going",
             "correct": False,
             "why": "A neutralisation finishes in seconds. Five minutes later "
                    "only cooling is happening"},
            {"text": "The peak — the mixture has been cooling towards room "
                     "temperature since it passed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s06",
        "band": "standard",
        "text": "Why is the STARTING temperature of the solution measured, "
                "rather than the temperature of the room?",
        "options": [
            {"text": "Because the solution may not be at room temperature "
                     "when you start",
             "correct": True},
            {"text": "Because a thermometer in a solution is more accurate "
                     "than one in air, and a reading taken in air can be out "
                     "by several degrees either way",
             "correct": False,
             "why": "The thermometer works fine in air. The problem is that "
                    "the solution may not be at room temperature"},
            {"text": "Because the room's temperature changes during the "
                     "lesson",
             "correct": False,
             "why": "It changes very slowly. The point is that the solution "
                    "and the room can differ from the outset"},
            {"text": "Because the room is always warmer than the solution",
             "correct": False,
             "why": "It may be either. That is exactly why you measure rather "
                    "than assume"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s07",
        "band": "standard",
        "text": "Two groups report +7 °C and +2 °C for the same reaction, and "
                "neither invented anything. Which is likely to be closer to "
                "the truth?",
        "options": [
            {"text": "The +2, because a smaller reading means less heat was "
                     "lost during the run and so less of the energy escaped "
                     "before the thermometer could register it",
             "correct": False,
             "why": "Exactly backwards. Losing heat is what makes a reading "
                    "SMALL"},
            {"text": "The +7, because every error in this experiment makes "
                     "the reading too small",
             "correct": True},
            {"text": "The mean of the two, at +4.5",
             "correct": False,
             "why": "Averaging a good result with a bad one gives a worse "
                    "one. These errors do not cancel"},
            {"text": "It cannot be said without knowing which group was more "
                     "careful",
             "correct": False,
             "why": "The direction of the error is known, and it points to "
                    "the larger reading whoever took it"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s08",
        "band": "standard",
        "text": "The same reaction in a glass beaker gives a smaller rise "
                "than in a polystyrene cup. Give BOTH reasons.",
        "options": [
            {"text": "Glass conducts heat away faster, and the reaction runs "
                     "more slowly in glass because the surface of the beaker "
                     "does not stir the mixture as a cup does",
             "correct": False,
             "why": "The container does not change the reaction. The second "
                    "reason is that glass warms itself"},
            {"text": "Glass is transparent, and glass is heavier",
             "correct": False,
             "why": "Neither affects the reading. Conduction and heat "
                    "capacity do"},
            {"text": "Glass conducts heat away faster, and glass absorbs more "
                     "energy warming itself up",
             "correct": True},
            {"text": "Glass reacts with the acid, and glass is colder",
             "correct": False,
             "why": "Glass does not react with dilute acid, and both "
                    "containers start at room temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s09",
        "band": "standard",
        "text": "Why must the volumes and concentrations be kept the same "
                "between runs?",
        "options": [
            {"text": "So that the reaction finishes in the same time each "
                     "run, which is what makes the peak readings comparable "
                     "with one another",
             "correct": False,
             "why": "The timing is a side effect. The reason is that a "
                    "changed variable makes the comparison meaningless"},
            {"text": "So that the same amount of heat is lost each time",
             "correct": False,
             "why": "Heat loss depends on insulation and timing rather than "
                    "on the volumes. Fair comparison is the reason"},
            {"text": "Because the method says so",
             "correct": False,
             "why": "The method says so for a reason, and it is the reason "
                    "that is being asked for"},
            {"text": "So that the only thing being compared is the thing you "
                     "meant to compare",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s10",
        "band": "standard",
        "text": "What would a set of readings need in order to be both "
                "PRECISE and ACCURATE?",
        "options": [
            {"text": "To agree closely with each other AND with the true "
                     "value",
             "correct": True},
            {"text": "To agree closely with each other, taken enough times "
                     "that the mean can be trusted to have settled on the "
                     "right answer",
             "correct": False,
             "why": "That is precision alone. Five readings can agree closely "
                    "and all be low"},
            {"text": "To be taken by more than one person",
             "correct": False,
             "why": "Two people using the same leaking rig get the same low "
                    "answer"},
            {"text": "To be taken with a thermometer reading to two decimal "
                     "places",
             "correct": False,
             "why": "A finer scale improves precision and does nothing about "
                    "a heat loss that is already there"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s11",
        "band": "standard",
        "text": "A group records the peak at 27 °C but forgets to take a "
                "starting temperature. What can they report?",
        "options": [
            {"text": "A change of 27 °C, since the reading they have is the "
                     "one the reaction produced and the other would only have "
                     "been the temperature of the room anyway",
             "correct": False,
             "why": "The solution was already at some temperature before the "
                    "reaction. 27 is where it ended, not how far it moved"},
            {"text": "Nothing about the temperature change, because a change "
                     "needs two readings",
             "correct": True},
            {"text": "A change of about 7 °C, using room temperature as the "
                     "start",
             "correct": False,
             "why": "Room temperature is a guess at the missing reading. It "
                    "may not be what the solution was at"},
            {"text": "That the reaction was exothermic, and nothing else",
             "correct": False,
             "why": "Even that needs a comparison. One reading on its own "
                    "does not show a rise"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s12",
        "band": "standard",
        "text": "A group already has an insulated cup, a lid and a prompt "
                "reading, and their answer is still slightly low. What is "
                "left?",
        "options": [
            {"text": "Nothing at all — a rig with those three things is "
                     "perfect, so any remaining shortfall has to be a random "
                     "error rather than a systematic one",
             "correct": False,
             "why": "There is still a systematic shortfall, and it is the "
                    "apparatus absorbing energy"},
            {"text": "More repeats",
             "correct": False,
             "why": "Repeats do nothing about an error that runs one way "
                    "every time"},
            {"text": "The energy that goes into warming the cup, the lid and "
                     "the thermometer themselves",
             "correct": True},
            {"text": "A larger volume of solution",
             "correct": False,
             "why": "More solution changes the amounts rather than the "
                    "shortfall"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-04-h05",
        "band": "harder",
        "text": "A group with a visibly leaking rig reports a value exactly "
                "equal to the published one. What is the most honest thing to "
                "say?",
        "options": [
            {"text": "That the rig cannot have been leaking after all, since "
                     "a result that matches the published value is the best "
                     "evidence there is that the apparatus was working",
             "correct": False,
             "why": "Matching once is not evidence the rig was sound. It "
                    "invites the question of what else was wrong"},
            {"text": "That the published value must be wrong",
             "correct": False,
             "why": "One school reading is a poor reason to doubt a published "
                    "figure"},
            {"text": "That the result should be reported without comment",
             "correct": False,
             "why": "A result that disagrees with what the apparatus should "
                    "do is exactly the kind that needs a comment"},
            {"text": "That it is suspicious — a leaking rig should read low, "
                     "so something else has pushed it back up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h06",
        "band": "harder",
        "text": "A bomb calorimeter is weighed and its own heat capacity "
                "measured before any reaction is run. Why go to that trouble?",
        "options": [
            {"text": "Because the vessel absorbs some of the energy itself, "
                     "and that share has to be known to be added back in",
             "correct": True},
            {"text": "Because the vessel has to be identical from one "
                     "laboratory to the next, and weighing it is how that is "
                     "checked before a measurement is published anywhere",
             "correct": False,
             "why": "Vessels differ, which is exactly why each one's own heat "
                    "capacity is measured"},
            {"text": "Because a heavier vessel loses heat faster",
             "correct": False,
             "why": "Heat loss depends on insulation. The mass matters "
                    "because of what the steel absorbs"},
            {"text": "To check nothing has been left inside it",
             "correct": False,
             "why": "Sensible practice and not the reason. The measurement is "
                    "used in the arithmetic afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h07",
        "band": "harder",
        "text": "Why is a polystyrene cup a genuine piece of scientific "
                "apparatus rather than a cheap substitute for something "
                "better?",
        "options": [
            {"text": "It insulates well enough that no heat escapes from it "
                     "at all, which is the property a container for this "
                     "measurement most needs to have",
             "correct": False,
             "why": "Heat still escapes — the best school rig reads low. Its "
                    "second virtue is its small heat capacity"},
            {"text": "It insulates well AND absorbs very little energy "
                     "warming itself up",
             "correct": True},
            {"text": "It is cheap, so a class can have one each",
             "correct": False,
             "why": "True and beside the point. The question is about the "
                    "physics"},
            {"text": "It cannot break",
             "correct": False,
             "why": "It can be crushed easily enough. Durability is not what "
                    "makes it suitable"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h08",
        "band": "harder",
        "text": "The calorie figures on a food packet come from burning a "
                "sample in a machine. Why is that measurement more trustworthy "
                "than a school one?",
        "options": [
            {"text": "The machine burns a far larger sample, so the "
                     "temperature rise is big enough for the losses to be too "
                     "small to matter beside it",
             "correct": False,
             "why": "The samples are small. What makes it trustworthy is that "
                    "the losses are controlled and accounted for"},
            {"text": "The people running it are more careful",
             "correct": False,
             "why": "Care helps and cannot remove a systematic error. Better "
                    "apparatus can"},
            {"text": "The vessel is sealed and insulated, and its own heat "
                     "capacity is measured and allowed for",
             "correct": True},
            {"text": "It uses electricity rather than a flame",
             "correct": False,
             "why": "Electric ignition is a detail. The insulation and the "
                    "known heat capacity are what matter"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h09",
        "band": "harder",
        "text": "A student proposes comparing three fuels by measuring the "
                "temperature of each FLAME rather than the water. Why is that "
                "no use?",
        "options": [
            {"text": "Because a thermometer put into a flame would break "
                     "before it could take a reading, so no measurement could "
                     "be made at all",
             "correct": False,
             "why": "There are thermometers that survive a flame. The "
                    "objection is that the reading answers the wrong "
                    "question"},
            {"text": "Because all three flames would be at the same "
                     "temperature",
             "correct": False,
             "why": "They would differ. And even different readings would not "
                    "measure energy released"},
            {"text": "Because a flame has no fixed temperature",
             "correct": False,
             "why": "A flame's temperature varies across it and can be "
                    "measured. It is still the wrong quantity"},
            {"text": "Because a flame's temperature says nothing about how "
                     "much energy the fuel released",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h10",
        "band": "harder",
        "text": "Why does averaging genuinely help with a RANDOM error, when "
                "it does nothing for a systematic one?",
        "options": [
            {"text": "Because random errors fall on both sides of the truth, "
                     "so they tend to cancel",
             "correct": True},
            {"text": "Because a random error is smaller than a systematic "
                     "one, so it takes fewer readings to average it away to "
                     "nothing at all",
             "correct": False,
             "why": "Size is not the difference. Direction is — a random "
                    "error can be large and still cancels"},
            {"text": "Because random errors happen less often",
             "correct": False,
             "why": "They happen on every reading. What matters is which way "
                    "they push"},
            {"text": "Because averaging removes the largest and smallest "
                     "readings",
             "correct": False,
             "why": "A mean uses every reading. Nothing is discarded"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h11",
        "band": "harder",
        "text": "A group improves its rig and the answer rises from +5.0 to "
                "+6.8 °C. Has the reaction changed?",
        "options": [
            {"text": "Yes — the better insulation keeps more of the energy in "
                     "the mixture, so the reaction releases more of it and "
                     "the temperature goes higher",
             "correct": False,
             "why": "The reaction releases the same energy whatever it is "
                    "sitting in. What changed is how much of it stayed"},
            {"text": "No — the reaction was always the same, and the "
                     "measurement has got closer to it",
             "correct": True},
            {"text": "Yes, because the conditions were changed",
             "correct": False,
             "why": "The apparatus changed rather than the chemistry. The "
                    "same substances reacted in the same amounts"},
            {"text": "It cannot be known without repeating both",
             "correct": False,
             "why": "Repeating is good practice and the question is settled "
                    "by reasoning: a reaction does not depend on its cup"},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h12",
        "band": "harder",
        "text": "The lesson insists that one temperature reading on its own "
                "says nothing. Why is that a statement about the QUANTITY "
                "rather than about carelessness?",
        "options": [
            {"text": "Because a single reading might have been taken at the "
                     "wrong moment, and only a second one taken later shows "
                     "whether the first was at the peak",
             "correct": False,
             "why": "Timing is a separate worry. Even a perfectly timed peak "
                    "is useless without a start"},
            {"text": "Because thermometers are unreliable",
             "correct": False,
             "why": "A perfect thermometer would not help. The quantity "
                    "itself needs two readings"},
            {"text": "Because a temperature change is a difference, and a "
                     "difference cannot be got from one number",
             "correct": True},
            {"text": "Because the room temperature has to be recorded as "
                     "well",
             "correct": False,
             "why": "The room is not the second reading. The solution's "
                    "starting temperature is"},
        ],
        "figure": None,
    },
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c7-04-e13",
        "band": "easier",
        "text": "What should be used to stir the mixture while the reaction "
                "is running?",
        "options": [
            {"text": "The thermometer", "correct": False,
             "why": "Stirring with a thermometer is how they get broken, and "
                    "a broken one in acid is a real incident."},
            {"text": "The measuring cylinder", "correct": False,
             "why": "A measuring cylinder is for measuring out a volume. It "
                    "is not put into the mixture at all."},
            {"text": "A stirring rod", "correct": True},
            {"text": "Nothing at all", "correct": False,
             "why": "Unstirred, the thermometer reads one warm pocket rather "
                    "than the mixture as a whole."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e14",
        "band": "easier",
        "text": "A reaction starts at 17 °C and reaches a peak of 23 °C. What "
                "is the temperature change?",
        "options": [
            {"text": "40 °C", "correct": False,
             "why": "The two readings have been added. A change is found by "
                    "subtracting, never by adding."},
            {"text": "6 °C", "correct": True},
            {"text": "23 °C", "correct": False,
             "why": "That is the peak reading itself. The change is 23 − 17, "
                    "the difference between the two."},
            {"text": "17 °C", "correct": False,
             "why": "That is the starting reading. On its own it says nothing "
                    "about how far the temperature moved."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e15",
        "band": "easier",
        "text": "An endothermic reaction starts at 20 °C and the thermometer "
                "falls to 14 °C. What is the temperature change?",
        "options": [
            {"text": "A rise of 6 °C", "correct": False,
             "why": "The size is right and the direction is not. This mixture "
                    "got colder, so the change is a fall."},
            {"text": "A fall of 14 °C", "correct": False,
             "why": "14 °C is the lowest reading, not the change. The fall is "
                    "20 − 14, which is 6 °C."},
            {"text": "A fall of 6 °C", "correct": True},
            {"text": "A fall of 34 °C", "correct": False,
             "why": "The two readings have been added together. A change is "
                    "the gap between them, not their total."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e16",
        "band": "easier",
        "text": "What does fitting a lid to the container do?",
        "options": [
            {"text": "It stops heat escaping from the open top, so more of "
                     "the rise reaches the thermometer", "correct": True},
            {"text": "It makes the reaction release more energy, because the "
                     "heat that is held in goes on building up inside",
             "correct": False,
             "why": "A lid cannot change the chemistry. The same amounts of "
                    "the same substances release the same energy."},
            {"text": "It stops the thermometer reading too high, by keeping "
                     "the warm air off the top of the stem", "correct": False,
             "why": "The reading is too low, not too high. A lid pushes it "
                    "upwards, closer to the true value."},
            {"text": "It holds the mixture at room temperature",
             "correct": False,
             "why": "A lid slows heat escaping. It does not hold anything at "
                    "any particular temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e17",
        "band": "easier",
        "text": "Why is a polystyrene cup a good insulator?",
        "options": [
            {"text": "Because the plastic feels cold to touch, and a cold "
                     "material keeps the mixture inside it cool",
             "correct": False,
             "why": "Feeling cool is about how fast a material carries heat "
                    "away from skin, not about insulating."},
            {"text": "Because it is mostly trapped air, and air is a poor "
                     "conductor of heat", "correct": True},
            {"text": "Because it is white, and a white surface reflects heat "
                     "back into whatever is inside it", "correct": False,
             "why": "Colour makes no useful difference here. It is the "
                    "trapped air inside the foam that insulates."},
            {"text": "Because its walls are thicker than glass, and thick "
                     "walls hold heat in", "correct": False,
             "why": "Thickness is not the reason. A thick glass beaker still "
                    "conducts heat away far faster than foam."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e18",
        "band": "easier",
        "text": "At what point should the starting temperature be taken?",
        "options": [
            {"text": "Before anything is added to the first solution",
             "correct": True},
            {"text": "Just after the two solutions have been mixed, once the "
                     "reading has begun to move", "correct": False,
             "why": "By then the reaction has already begun and some of the "
                    "change has already happened."},
            {"text": "At the very end of the run, once the reading has "
                     "settled down again", "correct": False,
             "why": "By the end the mixture has cooled back towards the room, "
                    "so that is not where it started."},
            {"text": "At any convenient moment during the reaction, so long "
                     "as it is written down", "correct": False,
             "why": "A value taken part-way through is not a starting value, "
                    "and the change comes out too small."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e19",
        "band": "easier",
        "text": "Taking the mean of several repeats reduces which kind of "
                "error?",
        "options": [
            {"text": "Systematic error", "correct": False,
             "why": "A systematic error shifts every repeat the same way, so "
                    "the mean is shifted by exactly as much."},
            {"text": "Both kinds equally", "correct": False,
             "why": "Averaging only cancels errors that fall on both sides of "
                    "the truth. A one-way error survives it."},
            {"text": "Neither kind", "correct": False,
             "why": "Scatter either side of the truth genuinely does cancel, "
                    "so a mean is better than one reading."},
            {"text": "Random error", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e20",
        "band": "easier",
        "text": "Trapped air is what makes polystyrene foam insulate. Which "
                "everyday object works on the same principle?",
        "options": [
            {"text": "A metal saucepan", "correct": False,
             "why": "A saucepan is built to conduct heat quickly, which is "
                    "the opposite of insulating."},
            {"text": "A duvet", "correct": True},
            {"text": "A single window pane", "correct": False,
             "why": "One pane conducts heat out of a room. It is double "
                    "glazing, with air between, that insulates."},
            {"text": "A radiator", "correct": False,
             "why": "A radiator is made to release heat as fast as it can. "
                    "Nothing about it traps air."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e21",
        "band": "easier",
        "text": "Why does the mixture need stirring at all?",
        "options": [
            {"text": "Because without it the thermometer reads one warm "
                     "pocket rather than the whole mixture", "correct": True},
            {"text": "Because stirring makes the reaction finish sooner, so "
                     "there is less time to lose heat", "correct": False,
             "why": "Stirring may mix the reactants, but the reason it is "
                    "done here is to make the reading fair."},
            {"text": "Because an unstirred mixture cools down faster than a "
                     "stirred one does", "correct": False,
             "why": "Stirring does not slow cooling. If anything it brings "
                    "warm liquid up to the surface faster."},
            {"text": "Because a thermometer will not respond unless liquid "
                     "is moving past its bulb", "correct": False,
             "why": "A thermometer responds in still liquid perfectly well. "
                    "It reports whatever is touching it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e22",
        "band": "easier",
        "text": "Which reading of the thermometer is the one to record?",
        "options": [
            {"text": "The reading taken exactly one minute after mixing, so "
                     "that every group uses the same wait", "correct": False,
             "why": "A fixed wait is not the peak. Many reactions have peaked "
                    "and begun cooling well inside a minute."},
            {"text": "The highest reading it reaches", "correct": True},
            {"text": "The reading taken once the mixture has settled back "
                     "down to a steady value", "correct": False,
             "why": "Once it settles it is back near room temperature, and "
                    "the change has been lost almost entirely."},
            {"text": "The mean of every reading taken during the run, so "
                     "that nothing is left out", "correct": False,
             "why": "Averaging across the run mixes the peak with cooler "
                    "values and gives a change that is too small."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e23",
        "band": "easier",
        "text": "What happens to the thermometer reading in the minutes after "
                "an exothermic reaction has peaked?",
        "options": [
            {"text": "It holds steady at the peak, because the energy "
                     "released has nowhere left to go", "correct": False,
             "why": "Nothing holds the heat in. A warm mixture in a cooler "
                    "room starts losing energy at once."},
            {"text": "It goes on climbing slowly, because the reaction keeps "
                     "on releasing energy for hours on end", "correct": False,
             "why": "The climb stops when the reaction does. After that only "
                    "the losses to the room continue."},
            {"text": "It falls back towards room temperature", "correct": True},
            {"text": "It drops well below room temperature before climbing "
                     "back up to meet it again", "correct": False,
             "why": "There is nothing to take it below the room. Cooling "
                    "stops once the two are level."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e24",
        "band": "easier",
        "text": "A set of readings that agree closely with one another is "
                "described as what?",
        "options": [
            {"text": "Accurate", "correct": False,
             "why": "Accurate means close to the true value. A set can be "
                    "tightly grouped and still all be wrong."},
            {"text": "Systematic", "correct": False,
             "why": "Systematic describes an error that runs one way, not a "
                    "set of readings that agree."},
            {"text": "Precise", "correct": True},
            {"text": "Anomalous", "correct": False,
             "why": "An anomalous reading is one that sits well away from the "
                    "others, which is the opposite of this."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e25",
        "band": "easier",
        "text": "A reading that sits close to the true value is described as "
                "what?",
        "options": [
            {"text": "Precise", "correct": False,
             "why": "Precise describes how closely repeats agree with each "
                    "other, not how close they are to the truth."},
            {"text": "Repeatable", "correct": False,
             "why": "Getting the same value again says nothing about whether "
                    "that value is the right one."},
            {"text": "Consistent", "correct": False,
             "why": "Consistent readings agree with one another. They can "
                    "agree and still sit well away from the truth."},
            {"text": "Accurate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e26",
        "band": "easier",
        "text": "Why should the starting temperature be written down rather "
                "than remembered?",
        "options": [
            {"text": "Because a number carried in the head is the one that "
                     "gets lost, and without it there is no change to "
                     "calculate", "correct": True},
            {"text": "Because writing it down slows the experiment to a "
                     "safer pace", "correct": False,
             "why": "Recording is about keeping the data, not about pace. "
                    "Speed matters at the peak, not at the start."},
            {"text": "Because a written number is more accurate than the "
                     "same number spoken", "correct": False,
             "why": "The reading is the same either way. What changes is "
                    "whether it still exists ten minutes later."},
            {"text": "Because it has to be countersigned", "correct": False,
             "why": "Nothing in the method needs countersigning. The reason "
                    "is simply that data has to survive."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e27",
        "band": "easier",
        "text": "What is a bomb calorimeter?",
        "options": [
            {"text": "A thermometer that reads to a hundredth of a degree, "
                     "used for very small changes", "correct": False,
             "why": "The fine thermometer is one part of it. The instrument "
                    "is the sealed vessel and its water jacket."},
            {"text": "A machine that measures how quickly a fuel burns away "
                     "once it has been lit", "correct": False,
             "why": "It measures the energy released, not the rate. How fast "
                    "a fuel burns is a different quantity."},
            {"text": "A stronger polystyrene cup, built to take the heat of "
                     "a burning fuel", "correct": False,
             "why": "It is steel, sealed and weighed, with its own heat "
                    "capacity measured. That is another instrument."},
            {"text": "A sealed steel vessel sitting in a measured mass of "
                     "water inside an insulated jacket", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e28",
        "band": "easier",
        "text": "Which quantity is measured in order to judge the energy "
                "change of a reaction?",
        "options": [
            {"text": "The mass of the container before the reaction and "
                     "again once it has finished", "correct": False,
             "why": "The container does not change mass, and weighing it "
                    "reports nothing about energy."},
            {"text": "The time the reaction takes from the moment of mixing "
                     "to the moment it stops", "correct": False,
             "why": "A slow reaction can release plenty of energy and a fast "
                    "one very little. Time does not measure it."},
            {"text": "The volume of solution left in the cup at the end of "
                     "the run", "correct": False,
             "why": "The volume is kept the same on purpose, so that it is "
                    "not what differs between runs."},
            {"text": "The temperature change of the mixture", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e29",
        "band": "easier",
        "text": "Heat escaping to the room during an exothermic reaction has "
                "what effect on the measured temperature change?",
        "options": [
            {"text": "It always makes the measured change smaller than the "
                     "true change", "correct": True},
            {"text": "It makes the measured change larger, because the "
                     "escaping heat warms the air around the thermometer",
             "correct": False,
             "why": "The bulb is in the liquid, not the air. Energy that "
                    "escapes is energy it never reads."},
            {"text": "It has no effect at all, because the reaction releases "
                     "the same energy whatever the apparatus",
             "correct": False,
             "why": "The energy released is the same. How much of it reaches "
                    "the thermometer is not."},
            {"text": "It turns the measured rise into a fall",
             "correct": False,
             "why": "An exothermic reaction still gives a rise. Losses make "
                    "that rise smaller, never negative."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-e30",
        "band": "easier",
        "text": "Why is glass a poor choice of container for this "
                "experiment?",
        "options": [
            {"text": "Because glass reacts with the dilute acid and takes "
                     "part in what is happening inside the cup",
             "correct": False,
             "why": "Glass is used in laboratories precisely because dilute "
                    "acids do not attack it."},
            {"text": "Because a glass beaker is far too heavy to be lifted "
                     "once the reaction has begun", "correct": False,
             "why": "Weight is irrelevant, and the container is not meant to "
                    "be moved during the run anyway."},
            {"text": "Because glass conducts heat away and absorbs a share "
                     "of it warming itself up", "correct": True},
            {"text": "Because no lid can be fitted to a beaker",
             "correct": False,
             "why": "A beaker takes a lid perfectly well. The trouble is what "
                    "the glass does with the heat."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c7-04-s13",
        "band": "standard",
        "text": "Group A records 18.0 °C then 24.5 °C. Group B records 20.0 °C "
                "then 27.5 °C. Which group measured the larger temperature "
                "change, and by how much?",
        "options": [
            {"text": "Group B, by 3.0 °C", "correct": False,
             "why": "3.0 is the gap between the two final readings. Each "
                    "group's change has to be worked out first."},
            {"text": "Group A, by 1.0 °C", "correct": False,
             "why": "A rose 6.5 °C and B rose 7.5 °C. Starting lower does not "
                    "make the change bigger."},
            {"text": "Group B, by 1.0 °C", "correct": True},
            {"text": "Neither, both 6.5 °C", "correct": False,
             "why": "24.5 − 18.0 is 6.5, but 27.5 − 20.0 is 7.5. The two "
                    "changes differ by a whole degree."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s14",
        "band": "standard",
        "text": "An endothermic reaction is run twice. Without a lid the "
                "lowest reading is 15.0 °C from a start of 22.0 °C; with a lid "
                "it is 13.5 °C from the same start. Which run is closer to the "
                "true value?",
        "options": [
            {"text": "The lidded run, because its fall of 8.5 °C let less "
                     "heat leak in from the room to the mixture",
             "correct": True},
            {"text": "The open run, because a smaller fall is the safer "
                     "figure to report", "correct": False,
             "why": "The smaller fall is the one that gained most from the "
                    "room. Caution is not the same as accuracy."},
            {"text": "Neither, because a lid can help only a reaction that "
                     "gets hotter", "correct": False,
             "why": "A lid slows heat crossing the boundary either way, so it "
                    "helps both kinds of reaction."},
            {"text": "Both equally, since the starts matched",
             "correct": False,
             "why": "A shared starting value does not make two rigs equal. "
                    "What differs is how much heat crossed."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s15",
        "band": "standard",
        "text": "A cup insulates well but is left open at the top. By what "
                "two routes is heat still escaping?",
        "options": [
            {"text": "Straight down through the base into the bench, and "
                     "sideways through the walls of the cup itself",
             "correct": False,
             "why": "The foam is exactly what blocks those two routes. The "
                    "open top is the gap the cup does not cover."},
            {"text": "By evaporation from the surface, and by warm air "
                     "rising away from it", "correct": True},
            {"text": "Through the thermometer and through the stirring rod, "
                     "both of which stick out into the air", "correct": False,
             "why": "Those carry a little, but the open surface loses far "
                    "more by evaporation and by rising air."},
            {"text": "By the reaction running backwards, and by the acid "
                     "cooling as it is used up", "correct": False,
             "why": "Neither happens. A neutralisation does not reverse, and "
                    "using up acid cools nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s16",
        "band": "standard",
        "text": "Two students use identical rigs, but one reads the "
                "thermometer at the peak and the other two minutes later. "
                "Predict how their reported changes will compare.",
        "options": [
            {"text": "The late reader will report the larger change, because "
                     "waiting lets the reaction finish properly",
             "correct": False,
             "why": "The reaction finished long before. Those two minutes are "
                    "spent losing heat, not gaining it."},
            {"text": "Both will report the same change, because they used "
                     "the same apparatus and chemicals", "correct": False,
             "why": "Identical apparatus does not rescue a late reading. When "
                    "you look is a variable of its own."},
            {"text": "The late reader will always report the smaller change",
             "correct": True},
            {"text": "The late reader's value will be the more reliable, "
                     "having been given longer to settle", "correct": False,
             "why": "Settling means cooling here. The settled value is the "
                    "one furthest from the truth."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s17",
        "band": "standard",
        "text": "Why should both solutions be at the same temperature as each "
                "other before they are mixed?",
        "options": [
            {"text": "Because mixing two liquids at different temperatures "
                     "changes the reading on its own, before any reaction is "
                     "counted", "correct": True},
            {"text": "Because a warmer solution reacts faster and so "
                     "releases more energy overall", "correct": False,
             "why": "A warmer start speeds a reaction up but does not change "
                    "how much energy it releases."},
            {"text": "Because a thermometer cannot be moved between two "
                     "liquids at different temperatures", "correct": False,
             "why": "A thermometer moves between liquids freely. The problem "
                    "lies in what mixing them does."},
            {"text": "Because both must share one measuring cylinder",
             "correct": False,
             "why": "Volume measurement is unaffected. The difficulty is that "
                    "the reading would not be the reaction's."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s18",
        "band": "standard",
        "text": "Two students read the same thermometer at the same moment "
                "and write down 24 °C and 25 °C. What kind of error is that, "
                "and what would reduce it?",
        "options": [
            {"text": "A systematic error, reduced by fitting a lid to the "
                     "container they are using", "correct": False,
             "why": "A systematic error pushes every reading the same way. "
                    "These two disagree in opposite directions."},
            {"text": "A systematic error, reduced by reading the thermometer "
                     "sooner after the two are mixed", "correct": False,
             "why": "Timing did not separate these two. They read the same "
                    "instrument at the same instant."},
            {"text": "A random error, reduced by repeating and averaging",
             "correct": True},
            {"text": "A random error, reduced by insulating the cup with a "
                     "second layer of foam", "correct": False,
             "why": "Insulation attacks heat loss, which is the one-way "
                    "error. It does nothing about scale reading."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s19",
        "band": "standard",
        "text": "A group's three readings are 5.0, 7.0 and 9.0 °C, and the "
                "true value is 7.0 °C. How should that set be described?",
        "options": [
            {"text": "Accurate on average but not precise", "correct": True},
            {"text": "Precise but not accurate, because the readings are "
                     "grouped tightly around one wrong figure",
             "correct": False,
             "why": "They are spread over four degrees, which is the opposite "
                    "of tightly grouped."},
            {"text": "Neither precise nor accurate, since not one reading in "
                     "the set landed on the true value", "correct": False,
             "why": "One of them did land on 7.0, and so does the mean. The "
                    "trouble is the spread, not the centre."},
            {"text": "Both precise and accurate, because the mean of the "
                     "three readings comes out at exactly the true value",
             "correct": False,
             "why": "A correct mean does not make a scattered set precise. "
                    "Precision is about how closely repeats agree."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s20",
        "band": "standard",
        "text": "A group already uses an insulated cup but writes up the "
                "method before reading the thermometer. Which single change "
                "would improve their result most?",
        "options": [
            {"text": "Adding a second layer of insulation around the cup "
                     "they are already using", "correct": False,
             "why": "The cup is already doing its job. The two-minute wait is "
                    "throwing that benefit away."},
            {"text": "Using twice the volume of both solutions so that the "
                     "rise comes out bigger and easier to see",
             "correct": False,
             "why": "Doubling both gives much the same change, and a delayed "
                    "reading still loses most of it."},
            {"text": "Repeating the whole experiment five more times and "
                     "taking the mean of all six runs", "correct": False,
             "why": "All six would be read late, so the mean would come out "
                    "just as low as the first run."},
            {"text": "Reading the thermometer at the peak", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s21",
        "band": "standard",
        "text": "Explain why some of the energy released never shows up on "
                "the thermometer even when the container is sealed.",
        "options": [
            {"text": "Some of it is destroyed as the reaction comes to an "
                     "end, and cannot be recovered afterwards",
             "correct": False,
             "why": "Energy is never destroyed. It ends up somewhere other "
                    "than in the liquid being measured."},
            {"text": "Some of it goes into warming the container, the lid "
                     "and the thermometer", "correct": True},
            {"text": "Some of it is spent making the new substances weigh "
                     "more than the old ones did", "correct": False,
             "why": "The products weigh the same as the reactants. Nothing is "
                    "spent on making mass."},
            {"text": "Some of it leaves the cup as light", "correct": False,
             "why": "A neutralisation in a cup gives out no light worth "
                    "measuring. The losses are to the apparatus."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s22",
        "band": "standard",
        "text": "A student suggests warming the acid to 40 °C first, so that "
                "the rise will be easier to see. Why is that a poor idea?",
        "options": [
            {"text": "Because a warm mixture sits further above room "
                     "temperature, so it loses heat to the room faster all "
                     "the way through", "correct": True},
            {"text": "Because warming the acid uses it up before the alkali "
                     "can be added", "correct": False,
             "why": "Warming does not consume the acid. All of it is still "
                    "there when the alkali goes in."},
            {"text": "Because a laboratory thermometer cannot be trusted "
                     "above 40 °C", "correct": False,
             "why": "Laboratory thermometers read far higher than that "
                    "without any difficulty."},
            {"text": "Because the rise would be harder to read",
             "correct": False,
             "why": "A larger rise would be easier to read. The real problem "
                    "is that it will not be larger."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s23",
        "band": "standard",
        "text": "A group runs the same reaction twice in the same rig and "
                "gets +6.6 °C and +6.8 °C. What should they do with those two "
                "values?",
        "options": [
            {"text": "Report the higher one, because heat loss means the "
                     "lower value must be the faulty run of the two",
             "correct": False,
             "why": "Neither run is faulty. A 0.2 °C difference is ordinary "
                    "scatter, and choosing the high one biases the answer."},
            {"text": "Report the mean of the two, since the difference "
                     "between them is ordinary scatter", "correct": True},
            {"text": "Discard both and begin the whole thing again, as two "
                     "readings that disagree cannot be used", "correct": False,
             "why": "Repeats never agree exactly. Disagreeing by a tenth or "
                    "two is what ordinary scatter looks like."},
            {"text": "Report the lower one, because the smallest measured "
                     "value is always the safest", "correct": False,
             "why": "Choosing the smallest is not caution, it is bias. The "
                    "mean uses both runs fairly."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s24",
        "band": "standard",
        "text": "A group stretches cling film over the cup and pushes the "
                "thermometer through it. What effect will that have on the "
                "reading?",
        "options": [
            {"text": "It will fall, because sealing the top traps the "
                     "reaction and slows it right down", "correct": False,
             "why": "Covering the top does not slow a neutralisation. The "
                    "reactants are already mixed underneath."},
            {"text": "It will stay exactly the same, because only the walls "
                     "of a container matter for heat loss", "correct": False,
             "why": "The open top is one of the biggest losses of the lot, "
                    "which is why a lid is worth fitting."},
            {"text": "It will fall, because the film conducts heat away "
                     "faster than open air does", "correct": False,
             "why": "Air above the liquid rises and carries heat off with it. "
                    "The film is what stops that."},
            {"text": "It will rise, because less heat escapes from the "
                     "surface of the liquid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s25",
        "band": "standard",
        "text": "A group measures 20.0 °C then 26.4 °C. They repeat with a lid "
                "fitted and measure 20.0 °C then 27.1 °C. How much did the lid "
                "gain them?",
        "options": [
            {"text": "7.1 °C", "correct": False,
             "why": "That is the second run's final reading, which is not "
                    "even a change. The gain is 7.1 − 6.4."},
            {"text": "6.4 °C", "correct": False,
             "why": "That is the first rig's whole result, not the part of it "
                    "the lid was responsible for."},
            {"text": "1.1 °C", "correct": False,
             "why": "That subtracts 26.0, which nobody recorded. The two "
                    "changes are 6.4 °C and 7.1 °C."},
            {"text": "0.7 °C", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s26",
        "band": "standard",
        "text": "Why does the thermometer reading begin to fall the moment it "
                "has passed its peak?",
        "options": [
            {"text": "Because from that point on the heat escaping to the "
                     "room is greater than any the reaction is still "
                     "supplying", "correct": True},
            {"text": "Because the reaction starts running backwards once it "
                     "has finished", "correct": False,
             "why": "A neutralisation does not reverse itself. What follows "
                    "the peak is ordinary cooling."},
            {"text": "Because a thermometer can hold its highest reading for "
                     "only a few seconds", "correct": False,
             "why": "A thermometer holds nothing. It reports whatever the "
                    "liquid around it is doing."},
            {"text": "Because the products are colder substances",
             "correct": False,
             "why": "Substances do not carry their own temperatures. The "
                    "mixture is simply cooling towards the room."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s27",
        "band": "standard",
        "text": "Why can a systematic error not be spotted by checking how "
                "closely a group's repeats agree with one another?",
        "options": [
            {"text": "Because repeats in a school laboratory are never close "
                     "enough to one another for the comparison to mean much",
             "correct": False,
             "why": "Careful repeats agree to a tenth of a degree. Close "
                    "agreement is common and is not the difficulty."},
            {"text": "Because it shifts every repeat by much the same "
                     "amount, leaving them still in close agreement",
             "correct": True},
            {"text": "Because a systematic error shows itself only in the "
                     "first run of a set, and not in any later one",
             "correct": False,
             "why": "It affects every run. That is exactly what makes it "
                    "systematic rather than random."},
            {"text": "Because a systematic error appears only once the "
                     "results have been averaged", "correct": False,
             "why": "It is present in every individual reading. Averaging "
                    "neither creates it nor reveals it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s28",
        "band": "standard",
        "text": "One class uses glass beakers and another uses polystyrene "
                "cups for the same reaction. Every cup result is higher than "
                "every beaker result. What does that pattern show?",
        "options": [
            {"text": "That the class with the cups must have worked more "
                     "carefully than the class with the beakers",
             "correct": False,
             "why": "Care would scatter both ways between individuals. This "
                    "difference tracks the apparatus exactly."},
            {"text": "That the container is causing a difference that runs "
                     "one way", "correct": True},
            {"text": "That the reaction releases more energy in a cup than "
                     "it does in a glass beaker", "correct": False,
             "why": "The chemistry is identical. What differs is how much of "
                    "the energy reaches the thermometer."},
            {"text": "That the beaker class must have misread their "
                     "thermometers on every single run", "correct": False,
             "why": "Misreading scatters in both directions. Every beaker "
                    "value being lower is not misreading."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s29",
        "band": "standard",
        "text": "Why is 'read it at the peak' better advice than 'read it "
                "exactly thirty seconds after mixing'?",
        "options": [
            {"text": "Because a stopwatch brings an error of its own into "
                     "the measurement", "correct": False,
             "why": "Timing to a second is easy. The trouble is that the "
                    "right second differs from reaction to reaction."},
            {"text": "Because thirty seconds is too short a wait for any "
                     "reaction to get going", "correct": False,
             "why": "Many reactions peak within seconds. A fixed rule is "
                    "wrong for being fixed, not for being short."},
            {"text": "Because the peak cannot be recognised until the "
                     "reading has begun to fall", "correct": False,
             "why": "The peak is recognised exactly that way, and watching "
                    "for it is what the advice asks for."},
            {"text": "Because different reactions peak at different times, "
                     "so a fixed wait misses it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-s30",
        "band": "standard",
        "text": "A group writes 25 °C in the temperature-change column, having "
                "copied down their final reading. Their start was 18 °C. What "
                "should the column say?",
        "options": [
            {"text": "43 °C", "correct": False,
             "why": "Adding the two readings gives a number that describes "
                    "nothing. A change is a difference."},
            {"text": "18 °C", "correct": False,
             "why": "The start is one of the two readings needed, not the "
                    "change between them."},
            {"text": "25 °C", "correct": False,
             "why": "That is what the thermometer showed, but the column "
                    "asks for a change and that needs both readings."},
            {"text": "7 °C", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c7-04-h13",
        "band": "harder",
        "text": "An endothermic reaction cools the mixture below room "
                "temperature. Explain what heat loss does to the measured "
                "fall in that case.",
        "options": [
            {"text": "Heat now flows in from the warmer room, so the "
                     "measured fall always comes out smaller than the true fall",
             "correct": True},
            {"text": "Heat still flows out of the mixture, so the measured "
                     "fall is larger than it should be", "correct": False,
             "why": "Heat flows from hot to cold. A mixture below room "
                    "temperature gains energy rather than losing it."},
            {"text": "Nothing crosses either way, because a cold mixture "
                     "has no heat left to give", "correct": False,
             "why": "A mixture at 14 °C still holds plenty of energy, and a "
                    "20 °C room transfers some straight in."},
            {"text": "The two flows cancel, so the fall is the true one",
             "correct": False,
             "why": "Nothing cancels. The flow runs one way and it always "
                    "shortens the measured fall."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h14",
        "band": "harder",
        "text": "A group argues their result must be right because the group "
                "at the next bench got the same value. Why is that reasoning "
                "unsafe?",
        "options": [
            {"text": "Two groups can never run a reaction in quite the same "
                     "way, so no two values may be compared",
             "correct": False,
             "why": "They can be compared, and comparing them is useful. The "
                    "flaw is that agreement is not proof."},
            {"text": "Only readings taken by the same student may fairly be "
                     "set beside one another at all", "correct": False,
             "why": "Whose hand held the thermometer is not the issue. The "
                    "issue is what the two rigs share."},
            {"text": "Two groups using the same leaky apparatus are wrong in "
                     "the same way and still agree", "correct": True},
            {"text": "A second group's value is only a repeat",
             "correct": False,
             "why": "Repeats are evidence about scatter. They are simply not "
                    "evidence about a one-way error."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h15",
        "band": "harder",
        "text": "In a bomb calorimeter the sample is set alight by an "
                "electrically heated wire rather than a burning splint. "
                "Suggest why that matters for the measurement.",
        "options": [
            {"text": "A splint would burn its own fuel inside the vessel and "
                     "add energy the sample never released", "correct": True},
            {"text": "A splint would not fit through the opening in a sealed "
                     "steel vessel", "correct": False,
             "why": "Access could be engineered. The objection is the energy "
                    "the splint itself contributes."},
            {"text": "An electric wire heats the sample more evenly than any "
                     "flame could", "correct": False,
             "why": "Evenness is not the point. The sample is lit and then "
                    "burns on its own either way."},
            {"text": "A splint would use up the sample's oxygen",
             "correct": False,
             "why": "The vessel is charged with far more oxygen than a splint "
                    "could ever consume."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h16",
        "band": "harder",
        "text": "One group gains 1.4 °C by reading at the peak instead of "
                "late; another gains 0.9 °C by swapping a beaker for a cup. "
                "What does that tell you about the two original rigs?",
        "options": [
            {"text": "That the second group's rig must have been the better "
                     "built of the two from the beginning", "correct": False,
             "why": "Nothing here compares the two rigs' readings. It "
                    "compares what each group's own fault was costing."},
            {"text": "That the same piece of advice would have helped both "
                     "groups by about the same amount", "correct": False,
             "why": "It would not: timing was the first group's main loss and "
                    "the container was the second group's."},
            {"text": "That the first group's reaction released more energy "
                     "than the second group's reaction did", "correct": False,
             "why": "A gain from a method change says nothing about the "
                    "chemistry, which was the same for both."},
            {"text": "That they were losing heat mainly by different "
                     "routes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h17",
        "band": "harder",
        "text": "A group's five readings are 6.2, 6.9, 6.7, 6.8 and 6.6 °C, "
                "and one member wants to drop the 6.2. Is that justified?",
        "options": [
            {"text": "Yes, because any value sitting apart from the others "
                     "is an anomaly and has to go", "correct": False,
             "why": "Distance alone is not a reason. Discarding low values "
                    "for being low pushes the mean up."},
            {"text": "No, because five readings may never be altered once "
                     "written down", "correct": False,
             "why": "A genuinely faulty run can be excluded, provided the "
                    "reason is the fault and not the number."},
            {"text": "Only if something went wrong in that run, since "
                     "dropping a low value biases the mean", "correct": True},
            {"text": "Yes, because heat loss means the lowest reading in a "
                     "set is always the faulty one", "correct": False,
             "why": "Heat loss makes all five low together. It does not pick "
                    "out any one run as faulty."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h18",
        "band": "harder",
        "text": "Why does insulating the container do nothing about the "
                "energy that ends up in the thermometer?",
        "options": [
            {"text": "Because a thermometer is made of glass, and no "
                     "insulation can slow heat moving through glass at all",
             "correct": False,
             "why": "Insulation would slow it if it were in the way. It is "
                    "not: the bulb sits inside the liquid."},
            {"text": "Because the thermometer sits inside the mixture and "
                     "always warms with it", "correct": True},
            {"text": "Because the thermometer is warmed by the room around "
                     "it rather than by the mixture itself", "correct": False,
             "why": "Only the stem above the liquid meets the room. The bulb "
                    "takes its energy from the mixture."},
            {"text": "Because the energy inside the thermometer comes back "
                     "out again as the reading is taken", "correct": False,
             "why": "It comes back only as the mixture cools, which is after "
                    "the peak has been and gone."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h19",
        "band": "harder",
        "text": "Suggest why a school rig gets closer to the true value for a "
                "reaction that finishes in seconds than for one that takes "
                "several minutes.",
        "options": [
            {"text": "A slow reaction spends longer above room temperature "
                     "before it peaks, so more heat escapes on the way",
             "correct": True},
            {"text": "A slow reaction releases less energy in total than a "
                     "fast one does", "correct": False,
             "why": "Rate and total energy are separate. A slow reaction can "
                    "release a great deal of energy."},
            {"text": "A fast reaction warms the thermometer less, so less "
                     "energy is wasted on the instrument", "correct": False,
             "why": "The thermometer takes the same share in both. What "
                    "differs is the loss to the room."},
            {"text": "A fast reaction is easier to stir", "correct": False,
             "why": "Stirring is no harder over minutes than over seconds. "
                    "The difference is time spent losing heat."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h20",
        "band": "harder",
        "text": "One student says a lid improves accuracy; another says it "
                "improves precision. Which is right, and why?",
        "options": [
            {"text": "The second, because a lid makes a group's repeats "
                     "agree far more closely with each other",
             "correct": False,
             "why": "A lid may tidy the spread a little, but its real work is "
                    "moving every value nearer the truth."},
            {"text": "Neither, because a lid changes only how long the "
                     "experiment takes to run from start to finish",
             "correct": False,
             "why": "A lid changes how much heat escapes, which is the whole "
                    "reason it is fitted."},
            {"text": "Both equally, since accuracy and precision are two "
                     "names for the same property of a set", "correct": False,
             "why": "They are different properties. A set can agree closely "
                    "and still be far from the true value."},
            {"text": "The first, because a lid moves every reading closer "
                     "to the true value", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h21",
        "band": "harder",
        "text": "If no school apparatus ever reaches the true value, how can "
                "the true value be known at all?",
        "options": [
            {"text": "By measuring very carefully with the same cup and "
                     "taking a great many more repeats than usual",
             "correct": False,
             "why": "Repeats in the same leaky cup all come out low. Care "
                    "does not recover what has escaped."},
            {"text": "By using apparatus whose own losses are measured "
                     "beforehand and allowed for", "correct": True},
            {"text": "By settling on whichever value the largest number of "
                     "classes happened to report", "correct": False,
             "why": "A shared error survives a vote. Every class using cups "
                    "would report low together."},
            {"text": "By taking the very highest value that any group has "
                     "ever managed to record", "correct": False,
             "why": "The highest reading is still an underestimate, and "
                    "picking extremes is not a measurement."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h22",
        "band": "harder",
        "text": "Explain how a group can keep every variable the same between "
                "runs and still end up with a wrong answer.",
        "options": [
            {"text": "Controlling variables makes readings agree, and "
                     "readings that agree can never be checked against "
                     "anything", "correct": False,
             "why": "They can be checked — against apparatus with known "
                    "losses. Agreement is simply not the check."},
            {"text": "Keeping every variable the same is possible only for a "
                     "reaction that has already been run once before",
             "correct": False,
             "why": "Controls are set before the first run, not after it. "
                    "That is not where the difficulty lies."},
            {"text": "A properly controlled experiment cannot be repeated, "
                     "so its answer can never be tested", "correct": False,
             "why": "Controlling variables is what makes a repeat meaningful "
                    "in the first place."},
            {"text": "Keeping conditions identical removes differences "
                     "between runs and leaves a fault they all share",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h23",
        "band": "harder",
        "text": "A rig loses 0.6 °C of the rise and measures a change of "
                "5.9 °C. What was the true change, and what would a rig losing "
                "only 0.2 °C have measured?",
        "options": [
            {"text": "True 5.3 °C; better rig reads 5.1 °C", "correct": False,
             "why": "The loss has already happened, so it is added back to "
                    "find the truth rather than taken off again."},
            {"text": "True 6.1 °C; better rig reads 5.9 °C", "correct": False,
             "why": "6.1 subtracts the wrong pair. The measured 5.9 plus the "
                    "0.6 lost gives a true value of 6.5."},
            {"text": "True 6.5 °C; better rig reads 6.3 °C", "correct": True},
            {"text": "True 6.5 °C; better rig reads 5.7 °C", "correct": False,
             "why": "The true value is right, but the 0.2 °C comes off 6.5, "
                    "not off the already-reduced 5.9."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h24",
        "band": "harder",
        "text": "Four groups using four different thermometers all read low "
                "by about the same amount. What does that rule out?",
        "options": [
            {"text": "Heat loss, because four separate rigs could not "
                     "possibly lose the same amount", "correct": False,
             "why": "Similar rigs in one room lose similar amounts. That is "
                    "precisely why all four came out low."},
            {"text": "Random error, because random scatter cannot show up "
                     "in more than one group's results at once",
             "correct": False,
             "why": "Random scatter appears in everyone's results. It is not "
                    "what is being ruled out here."},
            {"text": "The thermometers, since one faulty instrument would "
                     "not repeat across four", "correct": True},
            {"text": "The chemistry, because one reaction cannot release "
                     "the same energy in four vessels", "correct": False,
             "why": "It releases the same energy in all four. That is the one "
                    "thing never in doubt."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h25",
        "band": "harder",
        "text": "A rig measures 5.6 °C when the true rise is 7.0 °C. What "
                "percentage of the true rise did that rig lose?",
        "options": [
            {"text": "14%", "correct": False,
             "why": "1.4 is a temperature, not a percentage. It has to be "
                    "compared with the true value first."},
            {"text": "25%", "correct": False,
             "why": "That compares the 1.4 °C lost with the measured 5.6 "
                    "rather than with the true 7.0."},
            {"text": "80%", "correct": False,
             "why": "80% is the share the rig managed to record. The question "
                    "asks for the share it lost."},
            {"text": "20%", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h26",
        "band": "harder",
        "text": "A class's answers for one reaction run from +2 to +7 °C, and "
                "the true value is 7.0 °C. Is that evidence of random error, "
                "systematic error, or both?",
        "options": [
            {"text": "Random only, because the values are spread across "
                     "five degrees", "correct": False,
             "why": "The spread is random, but a spread lying entirely below "
                    "the truth is a second, one-way effect."},
            {"text": "Both — the spread between groups is random, and every "
                     "single value below 7.0 is systematic", "correct": True},
            {"text": "Systematic only, because every group in the class fell "
                     "short of the true value", "correct": False,
             "why": "Falling short is systematic, and the five-degree spread "
                    "between groups is not explained by it."},
            {"text": "Neither, because a class using different rigs cannot "
                     "be described by either term", "correct": False,
             "why": "Different rigs are exactly where both appear. The terms "
                    "describe the pattern, not the equipment."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h27",
        "band": "harder",
        "text": "A bomb calorimeter tracks temperature to a hundredth of a "
                "degree. Why is a school thermometer marked in whole degrees "
                "not the main limit on a school result?",
        "options": [
            {"text": "Because the heat escaping from a school cup is worth "
                     "several tenths of a degree, far more than the scale "
                     "costs", "correct": True},
            {"text": "Because a whole-degree scale can be read to a tenth by "
                     "eye, so in practice it costs nothing", "correct": False,
             "why": "Estimating between marks helps a little, but the real "
                    "shortfall is much larger than either."},
            {"text": "Because the scale a thermometer carries has no bearing "
                     "at all on the value it reports", "correct": False,
             "why": "The scale does limit the reading. It is simply not the "
                    "biggest limit in this experiment."},
            {"text": "Because school reactions are too small for a finer "
                     "scale to be of any use", "correct": False,
             "why": "A finer scale would be useful. It would just be swamped "
                    "by the heat that escapes."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h28",
        "band": "harder",
        "text": "A group insists their result must be right because they "
                "followed every step of the method exactly. Explain why that "
                "does not follow.",
        "options": [
            {"text": "Because nobody can follow somebody else's method "
                     "exactly", "correct": False,
             "why": "It can be followed closely enough. The trouble is with "
                    "the apparatus the method specifies."},
            {"text": "Because the losses built into the apparatus happen "
                     "however carefully the steps are followed",
             "correct": True},
            {"text": "Because following a method carefully makes a group's "
                     "readings scatter more widely than they did before",
             "correct": False,
             "why": "Careful work reduces scatter. What it cannot reduce is a "
                    "loss the rig has by design."},
            {"text": "Because a result counts as right only when it matches "
                     "the value the teacher expected", "correct": False,
             "why": "Matching an expectation is not the test. Accuracy is "
                    "closeness to the true value."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h29",
        "band": "harder",
        "text": "Group A neutralises 25 cm³ of acid with 25 cm³ of alkali; "
                "group B uses 50 cm³ of each, in identical cups, both reading "
                "at the peak. Predict how their temperature changes compare.",
        "options": [
            {"text": "Group B's will be about twice as large, because twice "
                     "as much acid is neutralised", "correct": False,
             "why": "Twice the energy goes into twice the liquid, so the "
                    "temperature change stays about the same."},
            {"text": "Group A's will be about twice as large, because a "
                     "small volume heats up more quickly", "correct": False,
             "why": "A smaller volume needs less energy to warm, and receives "
                    "less. The two effects cancel."},
            {"text": "About the same, because twice the energy is released "
                     "and there is twice as much liquid to warm",
             "correct": True},
            {"text": "Group B's will be about half as large",
             "correct": False,
             "why": "It is shared more thinly and there is twice as much of "
                    "it. Neither doubling nor halving follows."},
        ],
        "figure": None,
    },
    {
        "id": "c7-04-h30",
        "band": "harder",
        "text": "A student proposes correcting for heat loss by adding 0.2 °C "
                "to every result the class produces. What is wrong with that?",
        "options": [
            {"text": "Nothing at all — a systematic error is a fixed amount, "
                     "so one fixed correction removes it everywhere",
             "correct": False,
             "why": "Systematic means one direction, not one size. The loss "
                    "depends on the rig and on the timing."},
            {"text": "The correction ought to be subtracted instead, because "
                     "every reading came out too high", "correct": False,
             "why": "Every reading came out too low, so a correction would be "
                    "added rather than taken off."},
            {"text": "Corrections of any kind are dishonest",
             "correct": False,
             "why": "Professional instruments are corrected for known losses "
                    "as a matter of routine."},
            {"text": "The loss depends on the container and the timing, so "
                     "it is not one fixed amount", "correct": True},
        ],
        "figure": None,
    },
]
